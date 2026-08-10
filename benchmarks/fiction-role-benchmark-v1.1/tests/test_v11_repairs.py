#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


benchmark = load_module("benchmark_v11", ROOT / "validators" / "benchmark.py")
launcher = load_module("no_tool_runner_v11", ROOT / "launchers" / "no_tool_runner.py")


class ContractVisibilityTests(unittest.TestCase):
    def test_structured_prompt_contains_exact_schema_but_not_private_material(self):
        prompt = launcher.build_candidate_prompt("mechanical-qa")
        schema_text = (ROOT / "schemas" / "mechanical-output.schema.json").read_text(encoding="utf-8").strip()
        self.assertIn(schema_text, prompt)
        self.assertIn('"corrected_text"', prompt)
        self.assertNotIn("rubrics/", prompt)
        self.assertNotIn("ground_truth", prompt)
        self.assertNotIn("score", prompt.casefold())

    def test_writer_prompt_has_hard_boundary_and_order_contract(self):
        prompt = launcher.build_candidate_prompt("writer")
        self.assertIn("AUTOMATIC HARD-GATE FAILURE", prompt)
        self.assertIn("headings count toward the word count", prompt)
        self.assertIn("Beat order is mandatory", prompt)
        self.assertIn("900", prompt)
        self.assertIn("1,200", prompt)


class NoToolLauncherTests(unittest.TestCase):
    def test_no_tool_policy_resolves_to_zero_definitions(self):
        probe = launcher.probe_no_tool_policy()
        self.assertEqual(probe["toolset_argument"], "none")
        self.assertEqual(probe["resolved_tool_count"], 0)
        self.assertEqual(probe["resolved_tool_names"], [])

    def test_wrapper_warning_is_separated_without_modifying_provider_text(self):
        raw = "Warning: Unknown toolsets: none\n{\"verdict\":\"pass\"}\n"
        provider, wrapper = launcher.separate_wrapper_output(raw)
        self.assertEqual(provider, '{"verdict":"pass"}\n')
        self.assertEqual(wrapper, "Warning: Unknown toolsets: none\n")

    def test_run_directory_overwrite_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "attempt"
            launcher.create_run_directory(path)
            with self.assertRaises(FileExistsError):
                launcher.create_run_directory(path)


class SchemaAndWriterTests(unittest.TestCase):
    def test_positive_and_malformed_structured_submissions(self):
        valid = {
            "hook": "The fresh water",
            "tension": "rose",
            "clarity": "clear",
            "character_pull": "Mara",
            "emotional_movement": "shock to resolve",
            "strongest_moment": "Eli's name",
            "confusions": [],
            "predictions": ["the case matters"],
            "desire_to_continue": "yes",
            "confidence": 0.8,
        }
        malformed = dict(valid)
        malformed["desire_to_continue"] = "absolutely"
        malformed["extra_field"] = "leak"
        with tempfile.TemporaryDirectory() as td:
            good = Path(td) / "good.json"
            bad = Path(td) / "bad.json"
            good.write_text(json.dumps(valid), encoding="utf-8")
            bad.write_text(json.dumps(malformed), encoding="utf-8")
            self.assertTrue(benchmark.validate_submission("reader", good)["eligible"])
            result = benchmark.validate_submission("reader", bad)
            self.assertFalse(result["eligible"])
            self.assertTrue(any("schema" in item for item in result["hard_failures"]))

    def test_writer_length_overrun_and_beat_order_are_hard_failures(self):
        markers = [
            "fresh water", "ticket", "Eli sent me a message tonight", "11:55",
            "three short beeps", "maintenance stair", "compass",
        ]
        filler = "Mara watched the dark water and held her breath. "
        good = ". ".join(markers) + ". " + filler * 120
        while len(benchmark.words(good)) < 900:
            good += filler
        self.assertLessEqual(len(benchmark.words(good)), 1200)
        over = good + " " + filler * 40
        out_of_order = good.replace("fresh water", "TEMP", 1).replace("compass", "fresh water", 1).replace("TEMP", "compass", 1)
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "writer.md"
            p.write_text(over, encoding="utf-8")
            over_result = benchmark.validate_submission("writer", p)
            self.assertFalse(over_result["eligible"])
            self.assertTrue(any("word count" in item for item in over_result["hard_failures"]))
            p.write_text(out_of_order, encoding="utf-8")
            order_result = benchmark.validate_submission("writer", p)
            self.assertFalse(order_result["eligible"])
            self.assertIn("required beat markers out of order", order_result["hard_failures"])


class ProvenanceAndPreservationTests(unittest.TestCase):
    def test_run_record_rejects_route_mismatch_and_nonzero_tool_turns(self):
        data = launcher.example_run_record()
        data["served_route"]["model"] = "fallback"
        data["actual_tool_turn_count"] = 1
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "run-result.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = benchmark.validate_run_record(path)
        self.assertFalse(result["ok"])
        self.assertTrue(any("route" in item for item in result["errors"]))
        self.assertTrue(any("tool" in item for item in result["errors"]))

    def test_full_pack_manifest_and_packet_hash_are_stable(self):
        report = benchmark.verify_pack()
        self.assertTrue(report["ok"], report)
        self.assertRegex(report["packet_hash"], r"^[0-9a-f]{64}$")
        self.assertGreater(report["files_checked"], 21)

    def test_blinding_leakage_is_detected(self):
        with tempfile.TemporaryDirectory() as td:
            bundle = Path(td)
            (bundle / "submission.md").write_text("served by gpt-5.6-luna via openai-codex", encoding="utf-8")
            leaks = benchmark.scan_blinding_leakage(bundle, ["gpt-5.6-luna", "openai-codex", "gpt56-luna"])
        self.assertEqual(len(leaks), 1)

    def test_immutable_artifact_preserves_bytes_and_hash(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "provider-response.raw.txt"
            path.write_bytes(b"raw provider response\n")
            digest = launcher.seal_artifact(path)
            self.assertEqual(digest, benchmark.sha256_path(path))
            self.assertEqual(path.stat().st_mode & 0o222, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
