#!/usr/bin/env python3
"""Deterministic controls for fiction-role-benchmark-v1 (stdlib only)."""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import shutil
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ROLES = ("showrunner", "writer", "editor", "reader", "researcher", "continuity", "mechanical-qa")
GLOBAL_FORBIDDEN = (
    "little did she know", "everything changed", "a chill ran down her spine",
    "ancient evil", "destiny", "somehow", "for some reason",
)
MODEL_VISIBLE_PATTERNS = ("packets/*.md", "tasks/*.md", "schemas/*-output.schema.json")


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def words(text: str) -> list[str]:
    return re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def model_visible_files() -> list[Path]:
    found: set[Path] = set()
    for pattern in MODEL_VISIBLE_PATTERNS:
        found.update(path for path in ROOT.glob(pattern) if path.is_file())
    return sorted(found)


def freeze_manifest(write: bool) -> dict[str, Any]:
    target = ROOT / "manifests" / "packet-sha256.json"
    entries = [
        {"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size, "sha256": sha256_path(path)}
        for path in model_visible_files()
    ]
    payload = {
        "benchmark_id": "fiction-role-benchmark-v1",
        "pack_version": "1.0.0",
        "algorithm": "sha256",
        "scope": list(MODEL_VISIBLE_PATTERNS),
        "files": entries,
    }
    if write:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def verify_pack() -> dict[str, Any]:
    target = ROOT / "manifests" / "packet-sha256.json"
    errors: list[str] = []
    if not target.exists():
        return {"ok": False, "errors": ["missing manifests/packet-sha256.json"]}
    manifest = load_json(target)
    expected_paths = {entry["path"] for entry in manifest.get("files", [])}
    actual_paths = {str(path.relative_to(ROOT)) for path in model_visible_files()}
    for rel in sorted(expected_paths - actual_paths):
        errors.append(f"manifest file missing: {rel}")
    for rel in sorted(actual_paths - expected_paths):
        errors.append(f"unfrozen model-visible file: {rel}")
    for entry in manifest.get("files", []):
        path = ROOT / entry["path"]
        if not path.exists():
            continue
        digest = sha256_path(path)
        if digest != entry.get("sha256"):
            errors.append(f"hash mismatch: {entry['path']}")
        if path.stat().st_size != entry.get("bytes"):
            errors.append(f"byte-size mismatch: {entry['path']}")
    if manifest.get("benchmark_id") != "fiction-role-benchmark-v1" or manifest.get("pack_version") != "1.0.0":
        errors.append("manifest identity/version mismatch")
    return {
        "ok": not errors,
        "files_checked": len(manifest.get("files", [])),
        "manifest_sha256": sha256_path(target),
        "errors": errors,
    }


def required_top_level(role: str, data: dict[str, Any]) -> list[str]:
    schema_role = "mechanical" if role == "mechanical-qa" else role
    schema = load_json(ROOT / "schemas" / f"{schema_role}-output.schema.json")
    return [key for key in schema.get("required", []) if key not in data]


def base_report(role: str, path: Path) -> dict[str, Any]:
    return {"role": role, "submission": str(path), "hard_failures": [], "warnings": [], "checks": {}, "penalty": 0}


def check_forbidden(text: str, report: dict[str, Any], hard: bool = True) -> None:
    hits = [term for term in GLOBAL_FORBIDDEN if term.casefold() in text.casefold()]
    report["checks"]["global_forbidden_hits"] = hits
    if hits:
        (report["hard_failures"] if hard else report["warnings"]).append("global forbidden expression(s) present")
        report["penalty"] += min(10, 3 * len(hits))


def validate_showrunner(data: dict[str, Any], report: dict[str, Any]) -> None:
    beats = data.get("beats", [])
    ids = [item.get("id") for item in beats if isinstance(item, dict)]
    report["checks"]["beat_ids"] = ids
    if ids != [f"S{i}" for i in range(1, 8)]:
        report["hard_failures"].append("beats must be exactly S1-S7 in order")
    required = ("fresh water", "ticket", "Eli", "11:55", "three short beeps", "stair", "decision")
    text = json.dumps(data, ensure_ascii=False)
    missing = [term for term in required if term.casefold() not in text.casefold()]
    report["checks"]["required_story_material_missing"] = missing
    if missing:
        report["warnings"].append("showrunner plan omits required story material")
        report["penalty"] += min(15, 2 * len(missing))
    if len(data.get("protected_non_actions", [])) < 2:
        report["hard_failures"].append("fewer than two protected non-actions")
    check_forbidden(text, report)


def validate_writer(text: str, report: dict[str, Any]) -> None:
    truth = load_json(ROOT / "validators" / "ground_truth.json")["writer"]
    count = len(words(text))
    report["checks"]["word_count"] = count
    if not truth["min_words"] <= count <= truth["max_words"]:
        report["hard_failures"].append(f"word count {count} outside 900-1200")
    positions: list[int] = []
    missing: list[str] = []
    folded = text.casefold()
    for marker in truth["required_markers"]:
        pos = folded.find(marker.casefold())
        positions.append(pos)
        if pos < 0:
            missing.append(marker)
    report["checks"]["required_markers_missing"] = missing
    if missing:
        report["hard_failures"].append("required beat marker(s) missing")
    if not missing and positions != sorted(positions):
        report["hard_failures"].append("required beat markers out of order")
    exact_line = "Eli sent me a message tonight"
    occurrences = folded.count(exact_line.casefold())
    report["checks"]["eli_line_occurrences"] = occurrences
    if occurrences != 1:
        report["hard_failures"].append("Eli message line must occur exactly once")
    prohibited_events = ("opened the grey case", "Tom came down", "Tom left the wheelhouse", "Nessa was lying")
    event_hits = [term for term in prohibited_events if term.casefold() in folded]
    report["checks"]["prohibited_event_hits"] = event_hits
    if event_hits:
        report["hard_failures"].append("prohibited event/canon change present")
    check_forbidden(text, report)


def source_between(packet: Path) -> str:
    text = packet.read_text(encoding="utf-8")
    return text.split("BEGIN SOURCE\n", 1)[1].split("\nEND SOURCE", 1)[0]


def validate_editor(data: dict[str, Any], report: dict[str, Any]) -> None:
    revised = data.get("revised_text", "")
    source = source_between(ROOT / "packets" / "editor.md")
    truth = load_json(ROOT / "validators" / "ground_truth.json")["editor"]
    missing = [sentence for sentence in truth["protected"] if sentence not in revised]
    retention = len(words(revised)) / max(1, len(words(source)))
    report["checks"].update({"protected_missing": missing, "word_retention": round(retention, 4), "diagnosis_count": len(data.get("diagnoses", []))})
    if missing:
        report["hard_failures"].append("protected sentence changed or removed")
    if retention < truth["min_retention"]:
        report["hard_failures"].append("revision shrank below 85% preservation floor")
    if len(data.get("diagnoses", [])) != 3:
        report["hard_failures"].append("editor must provide exactly three diagnoses")
    event_terms = ("Nessa", "Saye", "document case", "maintenance alarm", "compass", "maintenance stair")
    missing_events = [term for term in event_terms if term.casefold() not in revised.casefold()]
    report["checks"]["event_markers_missing"] = missing_events
    if missing_events:
        report["warnings"].append("revision may have removed source events")
        report["penalty"] += min(10, 2 * len(missing_events))
    check_forbidden(revised, report)


def validate_reader(data: dict[str, Any], report: dict[str, Any]) -> None:
    text = json.dumps(data, ensure_ascii=False)
    prescription = ("should rewrite", "should change", "fix this", "the writer should", "the author should", "craft technique", "line edit")
    hits = [term for term in prescription if term.casefold() in text.casefold()]
    report["checks"]["editorial_contamination_hits"] = hits
    if hits:
        report["hard_failures"].append("reader output contains editorial prescription/diagnosis")
    if data.get("desire_to_continue") not in ("yes", "maybe", "no"):
        report["hard_failures"].append("invalid desire_to_continue")
    check_forbidden(text, report)


def validate_researcher(data: dict[str, Any], report: dict[str, Any]) -> None:
    truth = load_json(ROOT / "validators" / "ground_truth.json")["researcher"]
    assessments = data.get("assessments", [])
    ids = [a.get("claim_id") for a in assessments if isinstance(a, dict)]
    report["checks"]["claim_ids"] = ids
    if ids != [f"R{i}" for i in range(1, 6)]:
        report["hard_failures"].append("assessments must be R1-R5 in order")
    wrong: list[str] = []
    invalid_citations: list[str] = []
    missing_citations: list[str] = []
    for item in assessments:
        cid = item.get("claim_id")
        if cid in truth["verdicts"] and item.get("verdict") != truth["verdicts"][cid]:
            wrong.append(cid)
        citations = item.get("citations", [])
        if not citations:
            missing_citations.append(str(cid))
        invalid_citations.extend(c for c in citations if c not in truth["sources"])
    report["checks"].update({"wrong_verdicts": wrong, "invalid_citations": invalid_citations, "missing_citations": missing_citations})
    if wrong:
        report["warnings"].append("known-answer verdict mismatch")
        report["penalty"] += min(20, 4 * len(wrong))
    if invalid_citations or missing_citations:
        report["hard_failures"].append("citation integrity failure")
    text = json.dumps(data, ensure_ascii=False)
    outside_markers = ("http://", "https://", "according to wikipedia", "external source")
    if any(x in text.casefold() for x in outside_markers):
        report["hard_failures"].append("outside evidence introduced into closed packet")
    check_forbidden(text, report)


def validate_continuity(data: dict[str, Any], report: dict[str, Any]) -> None:
    concepts = load_json(ROOT / "validators" / "ground_truth.json")["continuity"]["expected_concepts"]
    text = json.dumps(data, ensure_ascii=False).casefold()
    found = [term for term in concepts if term.casefold() in text]
    report["checks"].update({"expected_concepts_found": found, "expected_concept_recall": round(len(found) / len(concepts), 4)})
    if len(found) < 7:
        report["warnings"].append("low recall against seeded continuity traps")
        report["penalty"] += min(20, 2 * (7 - len(found)))
    if not data.get("findings"):
        report["hard_failures"].append("no continuity findings")
    repair_terms = ("rewrite it as", "replace the scene", "the fix is", "add a new scene")
    hits = [term for term in repair_terms if term in text]
    report["checks"]["repair_scope_hits"] = hits
    if hits:
        report["hard_failures"].append("continuity auditor invented repairs")
    check_forbidden(text, report)


def corrected_mechanical_source() -> str:
    source = source_between(ROOT / "packets" / "mechanical-qa.md")
    replacements = load_json(ROOT / "validators" / "ground_truth.json")["mechanical"]["replacements"]
    for old, new in replacements.items():
        source = source.replace(old, new)
    return source


def validate_mechanical(data: dict[str, Any], report: dict[str, Any]) -> None:
    corrected = data.get("corrected_text", "")
    expected = corrected_mechanical_source()
    report["checks"].update({"exact_expected_match": corrected == expected, "expected_change_count": 8, "reported_issue_count": len(data.get("issues", []))})
    if corrected != expected:
        report["hard_failures"].append("corrected passage differs from exact mechanical answer")
    if len(data.get("issues", [])) != 8:
        report["warnings"].append("issue ledger does not contain one entry per objective change")
        report["penalty"] += min(10, abs(8 - len(data.get("issues", []))))
    check_forbidden(corrected, report)


def validate_submission(role: str, path: Path) -> dict[str, Any]:
    if role not in ROLES:
        raise ValueError(f"unknown role: {role}")
    report = base_report(role, path)
    if not path.exists():
        report["hard_failures"].append("submission file missing")
        report["eligible"] = False
        return report
    try:
        if role == "writer":
            validate_writer(path.read_text(encoding="utf-8"), report)
        else:
            data = load_json(path)
            if not isinstance(data, dict):
                raise ValueError("top-level JSON must be an object")
            missing = required_top_level(role, data)
            report["checks"]["missing_top_level_fields"] = missing
            if missing:
                report["hard_failures"].append("required top-level JSON fields missing")
            validator_name = "validate_mechanical" if role == "mechanical-qa" else f"validate_{role.replace('-', '_')}"
            globals()[validator_name](data, report)
    except (json.JSONDecodeError, UnicodeDecodeError, ValueError, KeyError, IndexError) as exc:
        report["hard_failures"].append(f"parse/structure error: {exc}")
    report["penalty"] = min(30, report["penalty"])
    report["eligible"] = not report["hard_failures"]
    return report


def validate_run_record(path: Path) -> dict[str, Any]:
    errors: list[str] = []
    try:
        data = load_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "errors": [f"run record parse error: {exc}"]}
    schema = load_json(ROOT / "schemas" / "run-result.schema.json")
    missing = [key for key in schema["required"] if key not in data]
    if missing:
        errors.append("missing required fields: " + ", ".join(missing))
    if data.get("benchmark_id") != "fiction-role-benchmark-v1" or data.get("pack_version") != "1.0.0":
        errors.append("benchmark identity/version mismatch")
    if data.get("role") not in ROLES:
        errors.append("unknown role")
    requested = data.get("requested_route") or {}
    served = data.get("served_route") or {}
    if data.get("routing_status") == "verified_exact":
        if not served or (requested.get("provider"), requested.get("model")) != (served.get("provider"), served.get("model")):
            errors.append("verified_exact claimed but served route differs or is missing")
    if data.get("status") == "pass" and data.get("routing_status") != "verified_exact":
        errors.append("passing run must have verified_exact routing")
    manifest = ROOT / "manifests" / "packet-sha256.json"
    if data.get("packet_manifest_sha256") != sha256_path(manifest):
        errors.append("packet manifest hash does not match frozen pack")
    settings = data.get("settings") or {}
    if settings.get("fresh_session") is not True:
        errors.append("fresh_session must be true")
    if not isinstance(data.get("latency_ms"), int) or data.get("latency_ms", -1) < 0:
        errors.append("latency_ms must be a non-negative integer")
    for artifact in data.get("artifacts", []):
        if not re.fullmatch(r"[0-9a-f]{64}", str(artifact.get("sha256", ""))):
            errors.append("artifact contains invalid SHA-256")
    return {"ok": not errors, "run_record": str(path), "errors": errors}


def blind_runs(runs_dir: Path, out_dir: Path, map_out: Path, seed_file: Path) -> dict[str, Any]:
    if not seed_file.exists() or not seed_file.read_bytes():
        raise ValueError("seed file must exist and be non-empty")
    candidates: list[tuple[Path, dict[str, Any], Path]] = []
    for run_record in sorted(runs_dir.glob("*/run-result.json")):
        data = load_json(run_record)
        role = data.get("role")
        if role not in ROLES:
            raise ValueError(f"invalid role in {run_record}")
        submission_candidates = [run_record.parent / "submission.md", run_record.parent / "submission.json"]
        submission = next((p for p in submission_candidates if p.exists()), None)
        if submission is None:
            raise ValueError(f"missing submission beside {run_record}")
        candidates.append((run_record.parent, data, submission))
    if not candidates:
        raise ValueError("no run-result.json files found")
    seed = int.from_bytes(hashlib.sha256(seed_file.read_bytes()).digest(), "big")
    rng = random.Random(seed)
    aliases = [f"CANDIDATE-{i:03d}" for i in range(1, len(candidates) + 1)]
    rng.shuffle(aliases)
    if out_dir.exists():
        raise ValueError("blind output directory already exists; never overwrite a scored bundle")
    out_dir.mkdir(parents=True)
    mapping: list[dict[str, Any]] = []
    for alias, (run_path, record, submission) in zip(aliases, candidates):
        target = out_dir / alias
        target.mkdir()
        copied = target / submission.name
        shutil.copyfile(submission, copied)
        blind_meta = {"blind_alias": alias, "role": record["role"], "submission_file": copied.name, "submission_sha256": sha256_path(copied), "pack_version": record.get("pack_version")}
        (target / "blind-manifest.json").write_text(json.dumps(blind_meta, indent=2) + "\n", encoding="utf-8")
        mapping.append({"blind_alias": alias, "attempt_id": record.get("attempt_id"), "role": record["role"], "requested_route": record.get("requested_route"), "served_route": record.get("served_route"), "source_run_dir": str(run_path)})
    map_out.parent.mkdir(parents=True, exist_ok=True)
    if map_out.exists():
        raise ValueError("identity map already exists; never overwrite")
    map_payload = {"benchmark_id": "fiction-role-benchmark-v1", "map": mapping}
    map_out.write_text(json.dumps(map_payload, indent=2) + "\n", encoding="utf-8")
    return {"ok": True, "candidates": len(candidates), "blind_dir": str(out_dir), "private_map": str(map_out), "map_sha256": sha256_path(map_out)}


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("verify-pack")
    freeze = sub.add_parser("freeze-pack")
    freeze.add_argument("--write", action="store_true", required=True)
    val = sub.add_parser("validate-submission")
    val.add_argument("--role", choices=ROLES, required=True)
    val.add_argument("--submission", type=Path, required=True)
    run_val = sub.add_parser("validate-run")
    run_val.add_argument("--run-record", type=Path, required=True)
    blind = sub.add_parser("blind")
    blind.add_argument("--runs-dir", type=Path, required=True)
    blind.add_argument("--out-dir", type=Path, required=True)
    blind.add_argument("--map-out", type=Path, required=True)
    blind.add_argument("--seed-file", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "verify-pack":
        result = verify_pack()
    elif args.command == "freeze-pack":
        result = freeze_manifest(True)
        result = {"ok": True, "files_frozen": len(result["files"]), "manifest": str(ROOT / "manifests" / "packet-sha256.json")}
    elif args.command == "validate-submission":
        result = validate_submission(args.role, args.submission)
    elif args.command == "validate-run":
        result = validate_run_record(args.run_record)
    else:
        result = blind_runs(args.runs_dir, args.out_dir, args.map_out, args.seed_file)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("ok", result.get("eligible", False)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
