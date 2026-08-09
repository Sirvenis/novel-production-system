#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "validators" / "benchmark.py"
spec = importlib.util.spec_from_file_location("benchmark", MODULE_PATH)
benchmark = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(benchmark)


class BenchmarkTests(unittest.TestCase):
    def write_json(self, directory: Path, name: str, data: dict) -> Path:
        path = directory / name
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def test_pack_hashes_and_all_schemas_parse(self):
        report = benchmark.verify_pack()
        self.assertTrue(report["ok"], report)
        for path in (benchmark.ROOT / "schemas").glob("*.json"):
            json.loads(path.read_text(encoding="utf-8"))

    def test_writer_positive_and_negative(self):
        beats = [
            "Mara tasted the fresh water.",
            "Saye pointed at the ticket.",
            "Nessa said Eli sent me a message tonight.",
            "The clocks showed 11:48 and 11:55.",
            "The panel gave three short beeps.",
            "Mara chose the maintenance stair.",
            "The compass turned without an answer.",
        ]
        filler = "Mara listened to the hull and watched each passenger choose where to place their hands. "
        text = "\n\n".join([beats[0], filler * 8, beats[1], filler * 8, beats[2], filler * 8, beats[3], filler * 8, beats[4], filler * 8, beats[5], filler * 8, beats[6]])
        # Extend deterministically into the allowed range without changing marker order.
        while len(benchmark.words(text)) < 900:
            text += " " + filler
        self.assertLessEqual(len(benchmark.words(text)), 1200)
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "submission.md"
            path.write_text(text, encoding="utf-8")
            good = benchmark.validate_submission("writer", path)
            self.assertTrue(good["eligible"], good)
            path.write_text("Everything changed. Eli sent me a message tonight.", encoding="utf-8")
            bad = benchmark.validate_submission("writer", path)
            self.assertFalse(bad["eligible"])
            self.assertTrue(bad["hard_failures"])

    def test_structured_roles_positive(self):
        source = benchmark.source_between(benchmark.ROOT / "packets" / "editor.md")
        revised = source.replace("Mara felt a chill run down her spine. She realised she was afraid, and the fear made her heart beat faster.", "Fear tightened Mara's grip on the deck edge; her pulse answered it.")
        mechanical = benchmark.corrected_mechanical_source()
        samples = {
            "showrunner": {
                "beats": [{"id": f"S{i}", "purpose": x, "visible_action": x, "reader_effect": "escalation", "continuity_risk": "protect decision and case", "exit_condition": "advance"} for i, x in enumerate(["fresh water", "ticket", "Eli", "11:55", "three short beeps", "stair", "decision"], 1)],
                "decision": "Mara checks the stair", "protected_non_actions": ["case stays shut", "Nessa is not exposed"], "escalation_curve": ["unease", "alarm", "choice"], "verdict": "proceed"
            },
            "editor": {"diagnoses": [{"issue": "redundancy", "evidence": "cold repeats", "severity": "medium"}, {"issue": "viewpoint", "evidence": "explains fear", "severity": "medium"}, {"issue": "tension", "evidence": "choice repeats", "severity": "low"}], "revised_text": revised, "preservation": {"protected_sentences_retained": True, "events_retained": True, "scope": "surgical"}, "deferred_issues": []},
            "reader": {"hook": "fresh water", "tension": "rose", "clarity": "clear", "character_pull": "Mara", "emotional_movement": "shock to decision", "strongest_moment": "Eli's name", "confusions": ["Nessa's motive"], "predictions": ["the case matters"], "desire_to_continue": "yes", "confidence": 0.8},
            "researcher": {"assessments": [{"claim_id": f"R{i}", "verdict": verdict, "evidence": "packet evidence", "inference": "bounded", "citations": [citation], "confidence": 0.9} for i, (verdict, citation) in enumerate([("supported", "[S3]"), ("contradicted", "[S6]"), ("contradicted", "[S4]"), ("supported", "[S2]"), ("contradicted", "[S5]")], 1)], "limitations": ["closed packet"]},
            "continuity": {"findings": [{"id": "C1", "summary_fragment": "official time Tom wheelhouse seawater roof digital ticket lying alarm ferry clock north case", "canon_evidence": "common packet", "severity": "major", "classification": "contradiction"}], "checked_domains": ["time", "people", "objects"], "verdict": "fail"},
            "mechanical-qa": {"corrected_text": mechanical, "issues": [{"original": str(i), "replacement": str(i), "rule": "objective"} for i in range(8)], "source_sha256": "", "corrected_sha256": "", "scope": "mechanical-only"},
        }
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td)
            for role, data in samples.items():
                with self.subTest(role=role):
                    result = benchmark.validate_submission(role, self.write_json(directory, role + ".json", data))
                    self.assertTrue(result["eligible"], result)

    def test_research_bad_citation_fails(self):
        data = {"assessments": [{"claim_id": f"R{i}", "verdict": "supported", "evidence": "x", "inference": "x", "citations": ["[S99]"], "confidence": 1} for i in range(1, 6)], "limitations": []}
        with tempfile.TemporaryDirectory() as td:
            result = benchmark.validate_submission("researcher", self.write_json(Path(td), "bad.json", data))
        self.assertFalse(result["eligible"])
        self.assertIn("citation integrity failure", result["hard_failures"])

    def test_run_record_requires_exact_route_and_frozen_manifest(self):
        manifest_hash = benchmark.sha256_path(benchmark.ROOT / "manifests" / "packet-sha256.json")
        data = {
            "benchmark_id": "fiction-role-benchmark-v1", "pack_version": "1.0.0", "role": "writer", "attempt_id": "a1",
            "requested_route": {"provider": "p", "model": "m"}, "served_route": {"provider": "p", "model": "m"},
            "routing_status": "verified_exact", "usage_class": "low", "packet_manifest_sha256": manifest_hash,
            "started_at": "2026-08-10T00:00:00Z", "ended_at": "2026-08-10T00:00:01Z", "latency_ms": 1000,
            "settings": {"temperature": 0, "reasoning": "none", "max_output_tokens": 2000, "tool_access": "none", "fresh_session": True},
            "status": "pass", "failures": [], "artifacts": [], "score": None
        }
        with tempfile.TemporaryDirectory() as td:
            path = self.write_json(Path(td), "run-result.json", data)
            self.assertTrue(benchmark.validate_run_record(path)["ok"])
            data["served_route"]["model"] = "fallback"
            path = self.write_json(Path(td), "run-result.json", data)
            self.assertFalse(benchmark.validate_run_record(path)["ok"])

    def test_blinding_removes_identity_and_never_overwrites(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            runs = base / "runs"
            for i, model in enumerate(("model-a", "model-b"), 1):
                run = runs / f"run-{i}"
                run.mkdir(parents=True)
                (run / "run-result.json").write_text(json.dumps({"role": "writer", "pack_version": "1.0.0", "attempt_id": f"a{i}", "requested_route": {"provider": "p", "model": model}, "served_route": {"provider": "p", "model": model}}), encoding="utf-8")
                (run / "submission.md").write_text("anonymous prose", encoding="utf-8")
            seed = base / "seed"
            seed.write_text("test-only-secret", encoding="utf-8")
            out = base / "blind"
            private_map = base / "private" / "map.json"
            result = benchmark.blind_runs(runs, out, private_map, seed)
            self.assertEqual(result["candidates"], 2)
            for manifest in out.glob("*/blind-manifest.json"):
                text = manifest.read_text(encoding="utf-8")
                self.assertNotIn("model-a", text)
                self.assertNotIn("model-b", text)
                self.assertNotIn("provider", text)
            with self.assertRaises(ValueError):
                benchmark.blind_runs(runs, out, private_map, seed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
