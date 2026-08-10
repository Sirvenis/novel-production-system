# Fiction Role Benchmark v1.1 — Wave 1A Report

Date: 2026-08-10
Custodian: Scout / Hermes under Andrew's final authority
Scout runtime: `gpt-5.6-sol` via `openai-codex`, verified in live agent log
Candidate route: `gpt-5.6-luna` via `openai-codex`, profile `gpt56-luna`
Scope: authorised Wave 1A non-writer role validation only
Status: EVIDENCE COMPLETE; STOPPED BEFORE PROMOTION OR WAVE 1B

## 1. Corrected-pack verification

The authorised pack was reverified before execution:

- corrected pack: `benchmarks/fiction-role-benchmark-v1.1/`;
- frozen files: 45;
- `python3 validators/benchmark.py verify-pack`: PASS;
- unit tests: 17/17 PASS;
- Python compilation: PASS;
- canonical packet hash: `1aac9a7890a7ca4337719dae85f093d1d6ee24e2abf2810df49b23da55fc9ad8`;
- full-manifest SHA-256: `92e9dc13980b69aab21268ec38dcda1d62d8726a299317b960998faa1de65c05`;
- v1 and Wave 0 evidence remained unmodified.

The installed Hermes registry again emitted the known SQLite WAL-version advisory during probe imports. It did not alter tool resolution, execution, route evidence, or benchmark artifacts. No Hermes update or configuration change was authorised or performed.

## 2. Roles tested

Wave 1A ran the six authorised non-writer roles:

1. Mechanical QA;
2. Fresh Reader;
3. Showrunner;
4. Editor;
5. Researcher / Fact Checker;
6. Continuity / Canon Auditor.

Mechanical QA and Fresh Reader were rerun because corrected Wave 0B had established calibration eligibility and Wave 1A required bounded role-validation evidence. Showrunner, Editor, Researcher, and Continuity were included because the corrected self-contained contract now allowed a fair no-tool test.

## 3. Roles deliberately not tested

Writer was deliberately not rerun. The corrected Wave 0B result is carried forward exactly as:

`WRITER ROLE — INELIGIBLE UNDER CORRECTED WAVE 0B CALIBRATION`

Wave 0B produced 1,231 words, exceeded the 900–1,200 contract, and placed required markers out of order. No technical transient changed, so no retry was justified. No extra-credit model or other candidate model was tested.

## 4. Exact route, tools, and execution controls

Every cell requested and served exactly:

- provider: `openai-codex`;
- model: `gpt-5.6-luna`;
- profile: `gpt56-luna`;
- tool policy: `none`;
- actual tool turns: `0`.

Aggregate execution evidence:

- exact route: 6/6 PASS;
- zero actual tool turns: 6/6 PASS;
- immutable raw provider response stored separately: 6/6;
- Hermes wrapper stdout/stderr stored separately: 6/6;
- extracted judged artifact stored separately: 6/6;
- strict run-record and artifact-hash validation: 6/6 PASS;
- input tokens: 11,941;
- output tokens: 6,352;
- total tokens: 18,293;
- mean wall latency: 22,294 ms.

Wrapper warnings and CLI noise were preserved in wrapper artifacts and excluded from judged submissions. Each run records requested/served route, provider, model, profile, tool policy, actual tool-turn count, settings, usage, latency, session identifier, route evidence, validation, and artifact hashes.

## 5. Deterministic eligibility and blind scoring

A six-candidate blind bundle was created. The identity map and seed remain private outside the repository; only their hashes are recorded. Leakage scan: PASS, 0 leaks across 12 blind-bundle files.

- private identity-map SHA-256: `7008a30ad7f0fda10ddaafca67dcc152103b6eed6491b1651587c3ce1a252c33`;
- private seed SHA-256: `f261ccb8b1b592343acaf0ff91abecd718485d69f24d80e81c8a69ded32077d7`.

Scout scored each blind artifact against the frozen role rubric before using route identity in the synthesis.

| Role | Route | Tool turns | Deterministic result | Human total | Penalty | Final | Critical flags |
|---|---:|---:|---|---:|---:|---:|---|
| Mechanical QA | PASS | 0 | eligible | 100 | 0 | 100 | none |
| Fresh Reader | PASS | 0 | eligible | 93 | 0 | 93 | none |
| Showrunner | PASS | 0 | eligible with warning | 91 | 2 | 89 | none |
| Editor | PASS | 0 | eligible | 94 | 0 | 94 | none |
| Researcher | PASS | 0 | eligible with warning | 94 | 4 | 90 | none |
| Continuity | PASS | 0 | eligible | 88 | 0 | 88 | none |

Deterministic warning details:

- Showrunner: the plan contained the alarm opening and timestamp but omitted the literal required phrase `three short beeps`; 2-point penalty.
- Researcher: R5 used `not-established` rather than the harness ground-truth verdict `contradicted`; the reasoning still correctly rejected proof of supernatural action; 4-point penalty.
- Continuity: 81.82% expected-concept recall was captured by the validator. The blind human score separately reflected that the official-time framing was not isolated as its own finding.

No run had a hard failure. No critical rubric dimension fell below half its available points.

## 6. Comparison with Wave 0 and corrected Wave 0B

| Evidence wave | Pack | Roles | Exact route | Tool turns | Deterministic eligibility | Interpretation |
|---|---|---:|---:|---:|---:|---|
| Wave 0 | v1 | 7 | 7/7 | 0/7 | 0/7 | Execution/isolation evidence only; structured schema was not candidate-visible. Writer independently failed length/order. |
| Corrected Wave 0B | v1.1 | 3 | 3/3 | 0/3 | 2/3 | Harness calibration: Mechanical QA and Fresh Reader eligible; Writer ineligible at 1,231 words and wrong marker order. |
| Wave 1A | v1.1 | 6 non-writer | 6/6 | 0/6 | 6/6 | Valid bounded non-writer role evidence with blind scores; no production promotion. |

Mechanical QA and Fresh Reader now have repeated corrected-pack eligibility across Wave 0B and Wave 1A. Showrunner, Editor, Researcher, and Continuity have one corrected Wave 1A role-validation result each. The writer remains ineligible and was not rerun.

## 7. Role-promotion review eligibility

All six tested non-writer roles clear the v1.1 evidence threshold for Andrew / Arden role-promotion review: exact provenance, no hard gate, final score at least 75, and no critical dimension below half.

Evidence strength is not equal:

- strongest repeated evidence: Mechanical QA and Fresh Reader;
- strong first valid cell: Editor and Continuity;
- eligible with bounded deterministic warning: Showrunner and Researcher.

This means `gpt-5.6-luna` may be considered further for these non-writer roles. It does not mean any role assignment or production profile is approved.

## 8. Whether Wave 1B is needed

Yes, further Wave 1B evidence is needed before production assignment. Mechanical QA and Fresh Reader have repeated same-route evidence, but a production decision still needs controlled comparative or replication evidence. Showrunner, Editor, Researcher, and Continuity currently have only one fair corrected-pack cell, and the Showrunner/Researcher warnings should be tested for repeatability rather than hidden by retries.

Wave 1B was not started. Its scope remains subject to separate Andrew authorization.

## 9. Artifact preservation

Canonical Wave 1A evidence:

`benchmarks/fiction-role-benchmark-v1.1/evidence/wave1a-gpt56-luna-20260810/`

The evidence directory contains six immutable attempt records, raw provider and wrapper artifacts, extracted submissions, route evidence, validation records, blind bundle, schema-validated blind scores, aggregate summary, and artifact manifest.

- Wave 1A evidence files listed by manifest: 94;
- Wave 1A artifact-manifest SHA-256: `bf74c8d0acde671ab888c721b766e2ceffeab74cb3cbee1d9233b32bb3f5d8b4`.

## 10. Boundary confirmation and stop

Wave 1A changed no production runtime, Hermes configuration, canonical prose, deployment, payment infrastructure, production model policy, or series model assignment. Scout remained `gpt-5.6-sol / openai-codex`. No extra-credit model was tested. No model was promoted. Wave 1B was not begun.

The lane stops at Andrew / Arden role-promotion review.
