#!/usr/bin/env python3
"""Deterministic controls for the final Showrunner compliance gate."""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_ID = "fiction-role-benchmark-v1.3-final-showrunner-compliance-gate"
PACK_VERSION = "1.3.0-final-gate"
MODEL_VISIBLE_PATTERNS = ("packets/*.md", "tasks/*.md", "schemas/showrunner-output.schema.json")
EXCLUDES = {"manifests/pack-sha256.json", "manifests/packet-sha256.json"}
PRIOR_ROOTS = [
    ROOT.parent / "fiction-role-benchmark-v1.1",
    ROOT.parent / "fiction-role-benchmark-v1.2-wave1c-holdout",
]
PRIOR_MARKERS = [
    "three short beeps", "amber twice, pause, amber once", "Vesper Ridge",
    "Imani Rook", "Arun Vale", "Keir Dast", "Jo Neri", "Director Voss",
    "Northglass", "radio observatory", "archive capsule", "service-hatch telemetry",
]


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def model_visible_files(root: Path = ROOT) -> list[Path]:
    found: set[Path] = set()
    for pattern in MODEL_VISIBLE_PATTERNS:
        found.update(p for p in root.glob(pattern) if p.is_file())
    return sorted(found)


def full_pack_files() -> list[Path]:
    out = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = str(p.relative_to(ROOT))
        if rel in EXCLUDES or rel.startswith(("evidence/", "runs/")) or "__pycache__" in p.parts or p.suffix == ".pyc":
            continue
        out.append(p)
    return sorted(out)


def entries(paths: list[Path], root: Path = ROOT) -> list[dict[str, Any]]:
    return [{"path": str(p.relative_to(root)), "bytes": p.stat().st_size, "sha256": sha256_path(p)} for p in paths]


def hash_entries(items: list[dict[str, Any]]) -> str:
    blob = json.dumps(items, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(blob).hexdigest()


def freeze_manifest(write: bool = True) -> dict[str, Any]:
    packet_path = ROOT / "manifests/packet-sha256.json"
    pack_path = ROOT / "manifests/pack-sha256.json"
    packet_items = entries(model_visible_files())
    packet = {
        "benchmark_id": BENCHMARK_ID, "pack_version": PACK_VERSION, "algorithm": "sha256",
        "scope": list(MODEL_VISIBLE_PATTERNS), "packet_hash": hash_entries(packet_items), "files": packet_items,
    }
    if write:
        packet_path.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    pack_items = entries(full_pack_files())
    pack = {
        "benchmark_id": BENCHMARK_ID, "pack_version": PACK_VERSION, "algorithm": "sha256",
        "scope": "all pack files except generated evidence/runs and self-referential manifests",
        "packet_hash": packet["packet_hash"],
        "packet_manifest_sha256": sha256_path(packet_path) if packet_path.exists() else None,
        "files": pack_items,
    }
    if write:
        pack_path.write_text(json.dumps(pack, indent=2) + "\n", encoding="utf-8")
    return pack


def verify_pack() -> dict[str, Any]:
    target = ROOT / "manifests/pack-sha256.json"
    errors = []
    if not target.exists():
        return {"ok": False, "errors": ["missing pack manifest"]}
    manifest = load_json(target)
    expected = {x["path"] for x in manifest.get("files", [])}
    actual = {str(p.relative_to(ROOT)) for p in full_pack_files()}
    for rel in sorted(expected - actual): errors.append(f"manifest file missing: {rel}")
    for rel in sorted(actual - expected): errors.append(f"unfrozen pack file: {rel}")
    for item in manifest.get("files", []):
        p = ROOT / item["path"]
        if p.exists() and (sha256_path(p) != item["sha256"] or p.stat().st_size != item["bytes"]):
            errors.append(f"hash/size mismatch: {item['path']}")
    packet_path = ROOT / "manifests/packet-sha256.json"
    if not packet_path.exists():
        errors.append("missing packet manifest")
        packet_hash = ""
    else:
        packet = load_json(packet_path)
        packet_hash = hash_entries(entries(model_visible_files()))
        if packet.get("packet_hash") != packet_hash: errors.append("packet hash mismatch")
        if manifest.get("packet_manifest_sha256") != sha256_path(packet_path): errors.append("packet manifest hash mismatch")
    if manifest.get("benchmark_id") != BENCHMARK_ID or manifest.get("pack_version") != PACK_VERSION:
        errors.append("manifest identity mismatch")
    return {"ok": not errors, "files_checked": len(manifest.get("files", [])), "manifest_sha256": sha256_path(target), "packet_hash": packet_hash, "errors": errors}


def freshness_validation() -> dict[str, Any]:
    current = model_visible_files()
    current_hashes = {sha256_path(p): str(p.relative_to(ROOT)) for p in current}
    prior_hashes: dict[str, str] = {}
    for prior in PRIOR_ROOTS:
        if not prior.exists(): continue
        for pattern in MODEL_VISIBLE_PATTERNS:
            for p in prior.glob(pattern):
                if p.is_file(): prior_hashes[sha256_path(p)] = str(p)
    overlap = [{"sha256": h, "current": current_hashes[h], "prior": prior_hashes[h]} for h in sorted(set(current_hashes) & set(prior_hashes))]
    marker_hits = []
    for p in current:
        text = p.read_text(encoding="utf-8", errors="replace").casefold()
        for marker in PRIOR_MARKERS:
            if marker.casefold() in text:
                marker_hits.append({"path": str(p.relative_to(ROOT)), "marker": marker})
    payload = {
        "ok": not overlap and not marker_hits,
        "candidate_visible_files": len(current),
        "prior_candidate_visible_hashes": len(prior_hashes),
        "exact_hash_overlap": overlap,
        "prior_marker_hits": marker_hits,
        "new_scenario_markers": ["Blackglass Estuary Laboratory", "Tamsin Roe", "LOT 6 / RETURN UNOPENED", "floor-load sensor", "blue access token"],
    }
    return payload


def schema_errors(data: Any) -> list[str]:
    from jsonschema import Draft202012Validator
    schema = load_json(ROOT / "schemas/showrunner-output.schema.json")
    return [f"{'/'.join(map(str,e.absolute_path)) or '<root>'}: {e.message}" for e in sorted(Draft202012Validator(schema).iter_errors(data), key=lambda e: list(e.absolute_path))]


def validate_submission(path: Path) -> dict[str, Any]:
    report: dict[str, Any] = {"role": "showrunner", "submission": str(path), "hard_failures": [], "warnings": [], "checks": {}, "penalty": 0}
    if not path.exists():
        report["hard_failures"].append("submission missing")
        report["eligible"] = False
        return report
    raw = path.read_text(encoding="utf-8", errors="strict")
    stripped = raw.strip()
    report["checks"]["markdown_fence_present"] = bool(re.search(r"```", raw))
    report["checks"]["raw_bytes"] = len(raw.encode())
    if report["checks"]["markdown_fence_present"]:
        report["hard_failures"].append("Markdown fence prohibited")
    try:
        decoder = json.JSONDecoder()
        lead = len(raw) - len(raw.lstrip())
        data, end = decoder.raw_decode(raw, idx=lead)
        trailing = raw[end:]
        report["checks"]["non_whitespace_trailing_content"] = bool(trailing.strip())
        if trailing.strip(): report["hard_failures"].append("commentary or data follows JSON object")
        if not isinstance(data, dict): report["hard_failures"].append("top-level JSON must be object")
        errors = schema_errors(data)
        report["checks"]["json_schema_errors"] = errors
        if errors: report["hard_failures"].append("schema validation failed: " + " | ".join(errors))
        truth = load_json(ROOT / "validators/ground_truth.json")["showrunner"]
        text = json.dumps(data, ensure_ascii=False)
        folded = text.casefold()
        ids = [b.get("id") for b in data.get("beats", []) if isinstance(b, dict)]
        missing = [x for x in truth["required_literals"] if x.casefold() not in folded]
        future_missing = [x for x in truth["protected_future_classes"] if x.casefold() not in folded]
        overclaims = [x for x in truth["forbidden_overclaims"] if x.casefold() in folded]
        report["checks"].update({
            "beat_ids": ids,
            "beat_ids_exact": ids == truth["beat_ids"],
            "required_literals_missing": missing,
            "exact_tag_occurrences": text.count(truth["exact_tag"]),
            "future_explanation_classes_missing": future_missing,
            "forbidden_overclaim_hits": overclaims,
            "protected_non_actions_count": len(data.get("protected_non_actions", [])),
            "required_inclusions_count": len(data.get("writer_handoff", {}).get("required_inclusions", [])),
            "prohibited_conclusions_count": len(data.get("writer_handoff", {}).get("prohibited_conclusions", [])),
        })
        if ids != truth["beat_ids"]: report["warnings"].append("G1-G8 beat order not exact")
        if missing: report["warnings"].append("explicit story material missing")
        if future_missing: report["warnings"].append("future explanation class missing")
        if overclaims: report["warnings"].append("evidence overclaimed")
    except (json.JSONDecodeError, UnicodeDecodeError, ValueError) as exc:
        report["hard_failures"].append(f"parse/structure error: {exc}")
    report["eligible"] = not report["hard_failures"]
    return report


def validate_run_record(path: Path) -> dict[str, Any]:
    from jsonschema import Draft202012Validator
    errors = []
    try: data = load_json(path)
    except Exception as exc: return {"ok": False, "errors": [str(exc)]}
    schema = load_json(ROOT / "schemas/run-result.schema.json")
    for e in Draft202012Validator(schema).iter_errors(data):
        errors.append(f"{'/'.join(map(str,e.absolute_path)) or '<root>'}: {e.message}")
    if data.get("benchmark_id") != BENCHMARK_ID or data.get("pack_version") != PACK_VERSION: errors.append("identity mismatch")
    for artifact in data.get("artifacts", []):
        p = path.parent / artifact["path"]
        if not p.exists() or sha256_path(p) != artifact["sha256"]: errors.append(f"artifact mismatch: {artifact['path']}")
    return {"ok": not errors, "errors": errors}


def create_blind_bundle(submission: Path, bundle: Path, alias: str = "CANDIDATE-001") -> dict[str, Any]:
    dest = bundle / alias
    if bundle.exists(): raise FileExistsError(bundle)
    dest.mkdir(parents=True)
    shutil.copy2(submission, dest / "submission.json")
    manifest = {"alias": alias, "role": "showrunner", "submission_sha256": sha256_path(dest / "submission.json"), "rubric_sha256": sha256_path(ROOT / "rubrics/showrunner.md")}
    (dest / "blind-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def scan_leakage(bundle: Path) -> dict[str, Any]:
    forbidden = ["gpt-5.6-luna", "openai-codex", "gpt56-luna", "Wave 1C", "100/100", "$schema failure", "desert radio"]
    leaks = []
    files = [p for p in bundle.rglob("*") if p.is_file()]
    for p in files:
        text = p.read_text(encoding="utf-8", errors="replace").casefold()
        for term in forbidden:
            if term.casefold() in text: leaks.append({"path": str(p.relative_to(bundle)), "term": term})
    return {"ok": not leaks, "files_scanned": len(files), "forbidden_terms": forbidden, "leaks": leaks}


def main() -> int:
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("freeze"); sub.add_parser("verify"); sub.add_parser("freshness")
    v=sub.add_parser("validate"); v.add_argument("path")
    b=sub.add_parser("blind"); b.add_argument("submission"); b.add_argument("bundle")
    l=sub.add_parser("leakage"); l.add_argument("bundle")
    args=ap.parse_args()
    if args.cmd == "freeze": result=freeze_manifest(True)
    elif args.cmd == "verify": result=verify_pack()
    elif args.cmd == "freshness": result=freshness_validation()
    elif args.cmd == "validate": result=validate_submission(Path(args.path))
    elif args.cmd == "blind": result=create_blind_bundle(Path(args.submission), Path(args.bundle))
    else: result=scan_leakage(Path(args.bundle))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("ok", result.get("eligible", True)) else 1

if __name__ == "__main__": raise SystemExit(main())
