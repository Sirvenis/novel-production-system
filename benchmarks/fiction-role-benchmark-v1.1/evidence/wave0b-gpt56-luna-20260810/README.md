# Corrected Wave 0B Calibration Evidence

Benchmark: `fiction-role-benchmark-v1.1` / `1.1.0`
Route: `gpt-5.6-luna` via `openai-codex`
Profile: `gpt56-luna`
Purpose: harness calibration only; no production model selection

## Results

| Role | Exact route | Tool turns | Contract visible | Deterministic result |
|---|---:|---:|---:|---|
| mechanical QA | yes | 0 | exact JSON Schema | eligible / pass |
| reader | yes | 0 | exact JSON Schema | eligible / pass |
| writer | yes | 0 | explicit hard boundary/order | ineligible: 1,231 words and markers out of order |

The writer failure is retained as evidence and was not retried because no technical transient variable changed. It proves the repaired writer gate detects a real 31-word overrun and order violation; it is not grounds for production-model promotion or rejection by itself.

Every attempt directory separately preserves the exact final assistant text, Hermes wrapper stdout/stderr, wrapper notice, normalized submission, extraction record, route log, validation output, run-record validation, hashes, session ID, usage, latency, and zero-tool proof. Raw artifacts are read-only and attempt paths reject overwrite.

Blind-bundle readiness passed for all three submissions: no requested/served/profile identity leakage and overwrite protection triggered on a second bundle attempt. The private identity map and seed remain outside Git under `/home/andrew/.hermes/private-benchmark/fiction-role-benchmark-v1.1/wave0b/`.

Exact evidence file hashes are in `CALIBRATION_ARTIFACT_MANIFEST.json`.
