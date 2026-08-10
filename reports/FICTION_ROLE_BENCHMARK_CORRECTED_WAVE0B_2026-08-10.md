# Fiction Role Benchmark v1.1 — Corrected Wave 0B Report

Date: 2026-08-10
Custodian: Scout / Hermes under Andrew's final authority
Scout runtime: `gpt-5.6-sol` via `openai-codex`, verified in live agent log
Calibration route: `gpt-5.6-luna` via `openai-codex`, profile `gpt56-luna`
Scope: corrected pack plus three-cell harness calibration only
Status: ELIGIBLE FOR ANDREW / ARDEN EVIDENCE REVIEW; WAVE 1 NOT AUTHORISED

## 1. What was wrong with v1

v1's no-tool workflow gave structured candidates a task that referenced a schema file by path but did not supply the schema contents. Once tools were truly absent, the candidate could not read the path and had to guess required keys, enums, nesting, and `additionalProperties` rules. Exact routing, isolation, preservation, and deterministic failures remained useful evidence, but 0/7 eligibility could not establish model unsuitability. The writer independently exceeded length and misplaced beats.

## 2. What changed

- Added an explicit no-tool launcher with a preflight proof that `--toolsets none` resolves zero tool definitions.
- Embedded each structured role's complete JSON Schema verbatim in the candidate-visible prompt.
- Kept rubrics, answers, validator ground truth, identity maps, and scoring logic private.
- Separated exact final assistant response, Hermes wrapper stdout/stderr, wrapper notices, normalization artifacts, submissions, route logs, and validation records.
- Sealed raw artifacts read-only and rejected existing attempt directories.
- Added strict Draft 2020-12 validation for nested structure, enums, constants, and extra fields.
- Recorded requested/served provider/model, profile, tool policy/count, sampling settings, usage, wall/API latency, session ID, route evidence, and artifact hashes.
- Tightened writer length and literal-marker order rules without tuning to the previous prose.
- Added full-pack and model-visible packet manifests.

## 3. Exact files changed

v1 was not edited. v1.1 is a new versioned pack at `benchmarks/fiction-role-benchmark-v1.1/`.

Material v1.1 changes/additions relative to v1:

- `README.md`
- `BENCHMARK_SPEC.md`
- `CANDIDATE_TEST_ORDER.md`
- `V1_TO_V1.1_CHANGE_SUMMARY.md`
- `launchers/no_tool_runner.py`
- `tasks/writer.md`
- `validators/benchmark.py`
- `validators/ground_truth.json`
- `tests/test_benchmark.py`
- `tests/test_v11_repairs.py`
- `schemas/run-result.schema.json`
- `schemas/score.schema.json`
- `templates/run-result.template.json`
- `templates/score.template.json`
- `manifests/benchmark.json`
- `manifests/packet-sha256.json`
- `manifests/pack-sha256.json`
- `evidence/README.md`
- `evidence/wave0b-gpt56-luna-20260810/**` (three immutable attempts, blind bundle, readiness validation, README, and calibration artifact manifest)

The complete exact 45-file corrected-pack list and SHA-256 values are in `manifests/pack-sha256.json`. The exact calibration evidence list and hashes are in `evidence/wave0b-gpt56-luna-20260810/CALIBRATION_ARTIFACT_MANIFEST.json`.

## 4. New manifest and packet hash

- Full corrected-pack file count: 45
- Full manifest SHA-256: `92e9dc13980b69aab21268ec38dcda1d62d8726a299317b960998faa1de65c05`
- Packet manifest SHA-256: `5b015e6ebbd38490adf0ece0927b256560daf155228ffc70df5952aa2753a6da`
- Canonical packet hash: `1aac9a7890a7ca4337719dae85f093d1d6ee24e2abf2810df49b23da55fc9ad8`
- Calibration artifact manifest SHA-256: `e9f3e0b9d7b96966458af97330bd978417f62212b1aea4a1d8a81d8c061b6cef`

v1 preservation proof:

- v1 Git tree: `d3091510478a99da36fb5ef8fb9e9af63858ba9c`
- v1 Wave 0 evidence tree: `724844b748fa76f08d30c83c976023c4464bf234`
- v1 packet-manifest SHA-256: `bd30312a7fa23ff226cbe06c32992d7b7de982c2a1741e4cfe7543f95777e282`
- current working-tree diff under v1: 0 files

## 5. Verification command results

- `python3 validators/benchmark.py verify-pack`: PASS, 45 files, 0 errors.
- `python3 -m unittest discover -s tests -p 'test_*.py' -v`: PASS, 17/17.
- Python compilation of validator, launcher, and both test modules: PASS.
- Draft 2020-12 structured/run schema validation: PASS on positive fixtures; malformed enum/extra-field fixture rejected.
- Blind-bundle leakage scan: PASS, 0 identity leaks.
- Blind-bundle overwrite attempt: correctly rejected.

The installed Hermes registry emitted a separate SQLite WAL-version advisory during local probe imports. It did not affect tool resolution, tests, route execution, or benchmark artifacts; no Hermes update/config change was authorised or performed.

## 6. No-tool launcher proof

Hermes has no documented empty-toolset CLI sentinel. `--toolsets none` produces the known line `Warning: Unknown toolsets: none`, but the registry resolves the explicit enabled selection to zero definitions rather than falling back to profile tools. Each attempt contains `no-tool-policy-proof.json`; all report zero resolved tools. Profile-local session logs show actual tool-turn count 0 for all three cells. The warning is preserved in wrapper output/notices and excluded from judged submissions.

## 7. Contract visibility proof

`build_candidate_prompt()` concatenates common packet, role packet, task, and—for every structured role—the exact matching schema text. Tests compare the embedded mechanical-QA schema byte-for-text with the source schema and assert private rubric/ground-truth/scoring material is absent. Both structured calibration cells produced schema-valid submissions.

## 8. Raw-response preservation proof

Every attempt separately stores read-only:

- `provider-response.raw.txt` — exact final assistant text after separating only the exact known CLI warning;
- `hermes-wrapper-stdout.raw.txt` and `hermes-wrapper-stderr.raw.txt`;
- `wrapper-notices.txt`;
- `extraction-normalization.json` and normalized submission;
- route and validation evidence.

All are SHA-256 listed in each `run-result.json`; run-record validation recomputes the hashes from disk. Provider-response SHA-256 values:

- mechanical QA: `d8ce8c7f125bbe08900b16e0614fc7cbdfad49ae4cbc3cc71b0aa0ad5084720c`
- reader: `72c8187ff591d339678560d15af3d9ed1549f704ddb6873dc5fba8319c26fc41`
- writer: `55fa88bb32cb79d860735a868fe7549da24529912314544ddc55085f8179c5ac`

## 9. Calibration route

Only `gpt-5.6-luna` via `openai-codex` was run, through existing profile `gpt56-luna`. No extra-credit model, production profile change, core configuration change, canonical prose change, deployment, payment, or production-policy change occurred.

## 10. Calibration deterministic results

| Role | Exact route | Tools | Contract | Deterministic result |
|---|---:|---:|---:|---|
| mechanical QA | PASS | 0 | exact schema visible | eligible / PASS |
| fresh reader | PASS | 0 | exact schema visible | eligible / PASS |
| writer | PASS | 0 | hard length/order contract visible | ineligible: 1,231 words and required markers out of order |

The writer result was not retried because no technical transient changed. The failure shows the corrected gate is discriminating: the model missed a clearly supplied boundary by 31 words and still misplaced marker order. This is calibration evidence, not a production-role decision.

## 11. Review eligibility

Yes. The corrected pack now supplies a self-contained execution contract, strict deterministic validation, route/tool provenance, immutable response separation, full hashes, and clean blind-bundle readiness. It is eligible for Andrew / Arden evidence review.

## 12. Wave 1 gate

Wave 1 remains blocked. The corrected pack can be proposed for a separately authorised Wave 1 only after Andrew / Arden review. Calibration scores/results must not select or promote a production model.
