import importlib.util, json, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("gate_benchmark", ROOT / "validators/benchmark.py")
benchmark = importlib.util.module_from_spec(spec); spec.loader.exec_module(benchmark)


def valid_submission():
    beat = lambda i: {"id": f"G{i}", "purpose": "p", "visible_action": "a", "reader_effect": "r", "evidence_boundary": "e", "continuity_risk": "c", "exit_condition": "x"}
    return {
        "beats": [beat(i) for i in range(1,9)],
        "decision": "Tamsin checks the culvert camera first.",
        "protected_non_actions": ["one", "two", "three", "four"],
        "future_book_risks": ["equipment malfunction", "staged human interference", "unknown ecological event"],
        "escalation_curve": ["one", "two", "three", "four"],
        "writer_handoff": {
            "required_inclusions": ["saltwater footprints at dry threshold", "deactivated blue token", "evidence locker five years", "04:46", "LOT 6 / RETURN UNOPENED", "upper gantry", "missing signature delivery manifest", "culvert camera before confronting Esme"],
            "prohibited_conclusions": ["Cal alive", "person entered", "case opened", "Esme lied", "salinity solved"],
            "scene_boundary": "decision"
        },
        "verdict": "proceed"
    }

class GateTests(unittest.TestCase):
    def validate_obj(self, obj, wrapper=lambda s:s):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"submission.json"; p.write_text(wrapper(json.dumps(obj)), encoding="utf-8")
            return benchmark.validate_submission(p)
    def test_valid_structure_passes(self):
        self.assertTrue(self.validate_obj(valid_submission())["eligible"])
    def test_dollar_schema_is_deterministic_failure(self):
        obj=valid_submission(); obj["$schema"]="https://json-schema.org/draft/2020-12/schema"
        result=self.validate_obj(obj)
        self.assertFalse(result["eligible"]); self.assertTrue(any("schema validation failed" in x for x in result["hard_failures"]))
    def test_fence_is_not_repaired(self):
        result=self.validate_obj(valid_submission(), lambda s: "```json\n"+s+"\n```\n")
        self.assertFalse(result["eligible"]); self.assertTrue(result["checks"]["markdown_fence_present"])
    def test_preamble_is_not_repaired(self):
        result=self.validate_obj(valid_submission(), lambda s: "Here is the JSON:\n"+s)
        self.assertFalse(result["eligible"])
    def test_trailing_commentary_is_not_repaired(self):
        result=self.validate_obj(valid_submission(), lambda s: s+"\nDone.")
        self.assertFalse(result["eligible"]); self.assertTrue(result["checks"]["non_whitespace_trailing_content"])
    def test_freshness_has_no_prior_overlap_or_markers(self):
        result=benchmark.freshness_validation(); self.assertTrue(result["ok"], result)
    def test_example_run_record_schema(self):
        launcher_spec=importlib.util.spec_from_file_location("gate_launcher", ROOT/"launchers/no_tool_runner.py")
        launcher=importlib.util.module_from_spec(launcher_spec); launcher_spec.loader.exec_module(launcher)
        from jsonschema import Draft202012Validator
        errors=list(Draft202012Validator(json.loads((ROOT/"schemas/run-result.schema.json").read_text())).iter_errors(launcher.example_run_record()))
        self.assertEqual(errors, [])

if __name__ == "__main__": unittest.main()
