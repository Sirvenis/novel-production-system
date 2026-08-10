import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("holdout_validator", ROOT / "validators" / "benchmark.py")
benchmark = importlib.util.module_from_spec(spec)
spec.loader.exec_module(benchmark)

runner_spec = importlib.util.spec_from_file_location("holdout_runner", ROOT / "launchers" / "no_tool_runner.py")
runner = importlib.util.module_from_spec(runner_spec)
runner_spec.loader.exec_module(runner)


class HoldoutTests(unittest.TestCase):
    def write_json(self, obj):
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(obj, handle)
        handle.close()
        return Path(handle.name)

    def researcher(self):
        truth = benchmark.load_json(ROOT / "validators" / "ground_truth.json")["researcher"]["verdicts"]
        return {"assessments": [{"claim_id": cid, "verdict": verdict, "evidence": "Packet evidence.", "inference": "Bounded inference.", "citations": [f"[S{i}]"], "confidence": 0.9} for i, (cid, verdict) in enumerate(truth.items(), 1)], "limitations": ["Closed record only."]}

    def showrunner(self):
        required = "condensate; unsigned courier docket; Arun; 02:16; amber twice, pause, amber once; service hatch; north control room; decision"
        return {"beats": [{"id": f"H{i}", "purpose": required, "visible_action": required, "reader_effect": "Escalating uncertainty.", "evidence_boundary": "Pressure state and power request do not establish opening, crossing, cause, sender, or identity.", "continuity_risk": "Preserve capsule, Jo, Arun, and future explanations.", "exit_condition": "Pressure changes without proof."} for i in range(1,9)], "decision": "Imani checks the service hatch first without leaving Jo alone with Voss.", "protected_non_actions": ["Do not open capsule.", "Do not prove Jo lies.", "Do not show Arun.", "Do not identify a cause."], "future_book_risks": ["Automation option lost.", "Human interference precluded.", "Uncanny answer confirmed too soon."], "escalation_curve": ["anomaly", "voice claim", "telemetry", "dangerous choice"], "writer_handoff": {"required_inclusions": ["condensate", "Jo claim", "02:16 telemetry", "amber twice, pause, amber once", "hatch-first decision"], "prohibited_conclusions": ["hatch opened", "someone entered", "Arun alive", "Jo lying"], "scene_boundary": "2:13–2:20; end on decision."}, "verdict": "proceed"}

    def test_prompt_has_schema_without_private_truth_or_rubric(self):
        for role in ("researcher", "showrunner"):
            prompt = runner.build_candidate_prompt(role)
            self.assertIn('"$schema"', prompt)
            self.assertNotIn("ground_truth", prompt)
            self.assertNotIn("Fresh-Holdout Rubric", prompt)
            self.assertNotIn("Wave 1A", prompt)
            self.assertNotIn("Wave 1B", prompt)

    def test_researcher_positive_and_wrong_label_penalty(self):
        good = benchmark.validate_submission("researcher", self.write_json(self.researcher()))
        self.assertTrue(good["eligible"])
        self.assertEqual([], good["checks"]["wrong_verdicts"])
        bad_data = self.researcher()
        bad_data["assessments"][4]["verdict"] = "not-established"
        bad = benchmark.validate_submission("researcher", self.write_json(bad_data))
        self.assertTrue(bad["eligible"])
        self.assertEqual(["R5"], bad["checks"]["wrong_verdicts"])
        self.assertEqual(6, bad["penalty"])

    def test_showrunner_positive_and_literal_overclaim_controls(self):
        good = benchmark.validate_submission("showrunner", self.write_json(self.showrunner()))
        self.assertTrue(good["eligible"])
        self.assertEqual([], good["checks"]["required_story_material_missing"])
        bad_data = self.showrunner()
        text = json.dumps(bad_data).replace("amber twice, pause, amber once", "an amber pattern")
        bad_data = json.loads(text)
        bad_data["beats"][0]["evidence_boundary"] = "The telemetry proves someone entered."
        bad = benchmark.validate_submission("showrunner", self.write_json(bad_data))
        self.assertTrue(bad["eligible"])
        self.assertIn("amber twice, pause, amber once", bad["checks"]["required_story_material_missing"])
        self.assertIn("proves someone entered", bad["checks"]["evidentiary_overclaim_hits"])
        self.assertGreaterEqual(bad["penalty"], 16)

    def test_v11_pack_remains_independently_valid(self):
        parent = ROOT.parent / "fiction-role-benchmark-v1.1"
        self.assertTrue((parent / "manifests" / "pack-sha256.json").exists())


if __name__ == "__main__":
    unittest.main()
