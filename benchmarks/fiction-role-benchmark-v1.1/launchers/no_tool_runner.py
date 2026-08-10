#!/usr/bin/env python3
"""Immutable no-tool launcher for fiction-role-benchmark-v1.1.

The installed Hermes CLI has no documented empty-toolset sentinel. Passing the
invalid sentinel ``none`` resolves to zero tool definitions but emits one known
warning. This launcher preserves wrapper stdout/stderr, separates that exact
warning, and stores the untouched final assistant text as the provider-response
artifact before any JSON/Markdown normalization.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
HERMES = Path("/home/andrew/.local/bin/hermes")
HERMES_SOURCE = Path("/home/andrew/.hermes/hermes-agent")
STRUCTURED_ROLES = {
    "showrunner", "editor", "reader", "researcher", "continuity", "mechanical-qa"
}
ROLES = tuple(sorted(STRUCTURED_ROLES | {"writer"}))
KNOWN_NO_TOOL_WARNING = "Warning: Unknown toolsets: none\n"


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def schema_path(role: str) -> Path:
    name = "mechanical" if role == "mechanical-qa" else role
    return ROOT / "schemas" / f"{name}-output.schema.json"


def build_candidate_prompt(role: str) -> str:
    if role not in ROLES:
        raise ValueError(f"unknown role: {role}")
    parts = [
        "# BENCHMARK INPUTS (all invented and noncanonical)",
        "## Common packet",
        (ROOT / "packets" / "common.md").read_text(encoding="utf-8").strip(),
        f"## {role} packet",
        (ROOT / "packets" / f"{role}.md").read_text(encoding="utf-8").strip(),
        "## Task",
        (ROOT / "tasks" / f"{role}.md").read_text(encoding="utf-8").strip(),
    ]
    if role in STRUCTURED_ROLES:
        parts.extend([
            "## Exact output contract visible to the candidate",
            "Return only one JSON object satisfying this exact JSON Schema. Do not add prose or code fences.",
            "```json",
            schema_path(role).read_text(encoding="utf-8").strip(),
            "```",
        ])
    return "\n\n".join(parts) + "\n"


def probe_no_tool_policy() -> dict[str, Any]:
    if str(HERMES_SOURCE) not in sys.path:
        sys.path.insert(0, str(HERMES_SOURCE))
    from model_tools import get_tool_definitions

    definitions = get_tool_definitions(enabled_toolsets=["none"], quiet_mode=True)
    names = [item.get("function", {}).get("name", "") for item in definitions]
    return {
        "toolset_argument": "none",
        "resolved_tool_count": len(definitions),
        "resolved_tool_names": names,
        "known_cli_warning": KNOWN_NO_TOOL_WARNING.strip(),
        "warning_effect": "display-only; invalid sentinel resolves to an explicit empty enabled-toolset selection",
    }


def separate_wrapper_output(stdout_text: str) -> tuple[str, str]:
    """Separate only the exact known CLI warning; preserve all other bytes/text."""
    if stdout_text.startswith(KNOWN_NO_TOOL_WARNING):
        return stdout_text[len(KNOWN_NO_TOOL_WARNING):], KNOWN_NO_TOOL_WARNING
    return stdout_text, ""


def create_run_directory(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=False)
    return path


def seal_artifact(path: Path) -> str:
    digest = sha256_path(path)
    path.chmod(path.stat().st_mode & ~stat.S_IWUSR & ~stat.S_IWGRP & ~stat.S_IWOTH)
    return digest


def _iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _profile_log(profile: str) -> Path:
    return Path.home() / ".hermes" / "profiles" / profile / "logs" / "agent.log"


def _extract_session_id(stderr_text: str) -> str | None:
    matches = re.findall(r"session_id:\s*([A-Za-z0-9_:-]+)", stderr_text)
    return matches[-1] if matches else None


def _parse_route_evidence(text: str, session_id: str | None) -> dict[str, Any]:
    relevant = [line for line in text.splitlines() if not session_id or f"[{session_id}]" in line]
    route_lines = [line for line in relevant if "API call #" in line]
    served_provider = served_model = None
    usage = {"input_tokens": None, "output_tokens": None, "cached_tokens": None, "total_tokens": None}
    latency_ms = None
    if route_lines:
        line = route_lines[-1]
        model = re.search(r"model=([^\s]+)", line)
        provider = re.search(r"provider=([^\s]+)", line)
        token_match = re.search(r"in=(\d+)\s+out=(\d+)\s+total=(\d+)", line)
        cache_match = re.search(r"cache=(\d+)/", line)
        latency_match = re.search(r"latency=([0-9.]+)s", line)
        served_model = model.group(1) if model else None
        served_provider = provider.group(1) if provider else None
        if token_match:
            usage.update({
                "input_tokens": int(token_match.group(1)),
                "output_tokens": int(token_match.group(2)),
                "total_tokens": int(token_match.group(3)),
            })
        if cache_match:
            usage["cached_tokens"] = int(cache_match.group(1))
        if latency_match:
            latency_ms = round(float(latency_match.group(1)) * 1000)
    tool_lines = [line for line in relevant if re.search(r"tool call|tool_call|Executing tool", line, re.I)]
    return {
        "served_provider": served_provider,
        "served_model": served_model,
        "usage": usage,
        "api_latency_ms": latency_ms,
        "actual_tool_turn_count": len(tool_lines),
        "lines": relevant,
    }


def _normalize_submission(role: str, provider_text: str) -> tuple[str, dict[str, Any]]:
    text = provider_text
    actions: list[str] = []
    if role in STRUCTURED_ROLES:
        stripped = text.strip()
        fence = re.fullmatch(r"```(?:json)?\s*\n?(.*?)\n?```", stripped, flags=re.S | re.I)
        if fence:
            stripped = fence.group(1).strip()
            actions.append("removed_single_outer_json_code_fence")
        text = stripped + "\n"
    return text, {"normalization_actions": actions, "provider_response_sha256": hashlib.sha256(provider_text.encode()).hexdigest()}


def example_run_record() -> dict[str, Any]:
    manifest = ROOT / "manifests" / "pack-sha256.json"
    manifest_hash = sha256_path(manifest) if manifest.exists() else "0" * 64
    return {
        "benchmark_id": "fiction-role-benchmark-v1.1",
        "pack_version": "1.1.0",
        "role": "writer",
        "attempt_id": "example",
        "requested_route": {"provider": "p", "model": "m", "profile": "profile", "evidence_path": "route-evidence.log"},
        "served_route": {"provider": "p", "model": "m", "profile": "profile", "evidence_path": "route-evidence.log"},
        "routing_status": "verified_exact",
        "profile": "profile",
        "tool_policy": "none",
        "actual_tool_turn_count": 0,
        "sampling_settings": {"temperature": None, "reasoning": "medium", "max_output_tokens": 4096},
        "packet_manifest_sha256": manifest_hash,
        "started_at": "2026-08-10T00:00:00+00:00",
        "ended_at": "2026-08-10T00:00:01+00:00",
        "latency_ms": 1000,
        "session_identifier": "session",
        "route_evidence_path": "route-evidence.log",
        "status": "pass",
        "failures": [],
        "artifacts": [],
        "usage": {"input_tokens": 1, "output_tokens": 1, "cached_tokens": 0, "total_tokens": 2},
        "score": None,
    }


def run_attempt(args: argparse.Namespace) -> int:
    run_dir = create_run_directory(Path(args.out_dir).resolve())
    prompt = build_candidate_prompt(args.role)
    prompt_path = run_dir / "prompt.txt"
    prompt_path.write_text(prompt, encoding="utf-8")

    probe = probe_no_tool_policy()
    (run_dir / "no-tool-policy-proof.json").write_text(json.dumps(probe, indent=2) + "\n", encoding="utf-8")
    if probe["resolved_tool_count"] != 0:
        raise RuntimeError("no-tool sentinel unexpectedly resolved tool definitions")

    log_path = _profile_log(args.profile)
    before_size = log_path.stat().st_size if log_path.exists() else 0
    command = [
        str(HERMES), "--profile", args.profile, "chat", "-q", prompt,
        "--provider", args.provider, "--model", args.model,
        "--toolsets", "none", "--reasoning", args.reasoning,
        "--max-turns", "1", "--ignore-rules", "--quiet", "--source", "tool",
    ]
    started_at = _iso_now()
    start = time.monotonic()
    completed = subprocess.run(command, capture_output=True, timeout=args.timeout)
    wall_latency_ms = round((time.monotonic() - start) * 1000)
    ended_at = _iso_now()

    stdout_path = run_dir / "hermes-wrapper-stdout.raw.txt"
    stderr_path = run_dir / "hermes-wrapper-stderr.raw.txt"
    stdout_path.write_bytes(completed.stdout)
    stderr_path.write_bytes(completed.stderr)
    stdout_text = completed.stdout.decode("utf-8", errors="replace")
    stderr_text = completed.stderr.decode("utf-8", errors="replace")
    provider_text, wrapper_notice = separate_wrapper_output(stdout_text)
    provider_path = run_dir / "provider-response.raw.txt"
    provider_path.write_text(provider_text, encoding="utf-8")
    (run_dir / "wrapper-notices.txt").write_text(wrapper_notice, encoding="utf-8")

    session_id = _extract_session_id(stderr_text)
    log_delta = ""
    if log_path.exists():
        with log_path.open("rb") as handle:
            handle.seek(before_size)
            log_delta = handle.read().decode("utf-8", errors="replace")
    route_path = run_dir / "route-evidence.log"
    route_path.write_text(log_delta, encoding="utf-8")
    route = _parse_route_evidence(log_delta, session_id)

    normalized, extraction = _normalize_submission(args.role, provider_text)
    suffix = ".md" if args.role == "writer" else ".json"
    submission_path = run_dir / f"submission{suffix}"
    submission_path.write_text(normalized, encoding="utf-8")
    extraction.update({
        "wrapper_stdout_sha256": sha256_path(stdout_path),
        "wrapper_stderr_sha256": sha256_path(stderr_path),
        "wrapper_notice_separated": bool(wrapper_notice),
        "submission_sha256": sha256_path(submission_path),
    })
    (run_dir / "extraction-normalization.json").write_text(json.dumps(extraction, indent=2) + "\n", encoding="utf-8")

    if str(ROOT / "validators") not in sys.path:
        sys.path.insert(0, str(ROOT / "validators"))
    import benchmark
    validation = benchmark.validate_submission(args.role, submission_path)
    (run_dir / "validation-result.json").write_text(json.dumps(validation, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    requested = {"provider": args.provider, "model": args.model, "profile": args.profile, "evidence_path": "route-evidence.log"}
    served = None
    if route["served_provider"] and route["served_model"]:
        served = {"provider": route["served_provider"], "model": route["served_model"], "profile": args.profile, "evidence_path": "route-evidence.log"}
    exact = bool(served and served["provider"] == args.provider and served["model"] == args.model)
    failures = []
    if not exact:
        failures.append({"class": "route_mismatch", "message": "served route missing or differs from requested route", "retryable": False})
    if route["actual_tool_turn_count"] != 0:
        failures.append({"class": "instruction", "message": "nonzero tool turns in no-tool mode", "retryable": False})
    if completed.returncode != 0:
        failures.append({"class": "other", "message": f"Hermes wrapper exited {completed.returncode}", "retryable": False})
    for item in validation.get("hard_failures", []):
        failures.append({"class": "instruction", "message": item, "retryable": False})

    immutable_names = [
        "prompt.txt", "no-tool-policy-proof.json", "hermes-wrapper-stdout.raw.txt",
        "hermes-wrapper-stderr.raw.txt", "provider-response.raw.txt", "wrapper-notices.txt",
        "route-evidence.log", f"submission{suffix}", "extraction-normalization.json",
        "validation-result.json",
    ]
    artifacts = []
    for name in immutable_names:
        path = run_dir / name
        artifacts.append({"path": name, "sha256": seal_artifact(path)})

    run_record = {
        "benchmark_id": "fiction-role-benchmark-v1.1",
        "pack_version": "1.1.0",
        "role": args.role,
        "attempt_id": args.attempt_id,
        "requested_route": requested,
        "served_route": served,
        "routing_status": "verified_exact" if exact else ("mismatch" if served else "unverified"),
        "profile": args.profile,
        "tool_policy": "none",
        "actual_tool_turn_count": route["actual_tool_turn_count"],
        "sampling_settings": {"temperature": None, "reasoning": args.reasoning, "max_output_tokens": args.max_output_tokens},
        "packet_manifest_sha256": sha256_path(ROOT / "manifests" / "pack-sha256.json"),
        "started_at": started_at,
        "ended_at": ended_at,
        "latency_ms": wall_latency_ms,
        "session_identifier": session_id,
        "route_evidence_path": "route-evidence.log",
        "status": "pass" if not failures and validation.get("eligible") else "fail",
        "failures": failures,
        "artifacts": artifacts,
        "usage": route["usage"],
        "wrapper_exit_code": completed.returncode,
        "api_latency_ms": route["api_latency_ms"],
        "score": None,
    }
    record_path = run_dir / "run-result.json"
    record_path.write_text(json.dumps(run_record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    run_validation = benchmark.validate_run_record(record_path)
    (run_dir / "run-record-validation.json").write_text(json.dumps(run_validation, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"run_dir": str(run_dir), "status": run_record["status"], "run_record_valid": run_validation["ok"]}, indent=2))
    return 0 if run_record["status"] == "pass" and run_validation["ok"] else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--role", choices=ROLES, required=True)
    parser.add_argument("--profile", required=True)
    parser.add_argument("--provider", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--attempt-id", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--reasoning", default="medium")
    parser.add_argument("--max-output-tokens", type=int, default=4096)
    parser.add_argument("--timeout", type=int, default=300)
    return run_attempt(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
