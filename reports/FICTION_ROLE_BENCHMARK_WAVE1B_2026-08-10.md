# Fiction Role Benchmark v1.1 — Wave 1B Report

Date: 2026-08-10
Custodian: Scout / Hermes under Andrew's final authority
Scout runtime: `gpt-5.6-sol` via `openai-codex`, verified in the live agent log
Candidate route: `gpt-5.6-luna` via `openai-codex`, profile `gpt56-luna`
Scope: authorised Wave 1B promotion-readiness validation only
Status: EVIDENCE COMPLETE; STOPPED BEFORE PRODUCTION ASSIGNMENT OR PROMOTION

## 1. Corrected-pack verification

The corrected v1.1 pack was reverified before Wave 1B execution:

- corrected pack: `benchmarks/fiction-role-benchmark-v1.1/`;
- frozen files: 45;
- `python3 validators/benchmark.py verify-pack`: PASS;
- unit tests: 17/17 PASS;
- Python compilation: PASS;
- Git whitespace check: PASS;
- canonical packet hash: `1aac9a7890a7ca4337719dae85f093d1d6ee24e2abf2810df49b23da55fc9ad8`;
- full-manifest SHA-256: `92e9dc13980b69aab21268ec38dcda1d62d8726a299317b960998faa1de65c05`.

The installed Hermes registry emitted the known SQLite WAL-version advisory during no-tool probe imports. It did not alter tool resolution, execution, routes, submissions, or evidence. No Hermes update or configuration change was performed.

The frozen pack contains no alternate task variants. To preserve the corrected 45-file pack rather than silently creating a new benchmark version, Wave 1B used six fresh independent executions against the frozen tasks. No Wave 1A response was reused as a judged artifact: all six Wave 1B submission hashes differ from Wave 1A.

## 2. Wave 1A evidence accepted

Andrew / Arden accepted Wave 1A as valid eligibility evidence for the six non-writer roles under the corrected v1.1 harness. Accepted Wave 1A results were:

- exact route: 6/6;
- actual tool turns: 0/6;
- deterministic eligibility: 6/6;
- Mechanical QA 100;
- Fresh Reader 93;
- Showrunner 89;
- Editor 94;
- Researcher 90;
- Continuity 88;
- blind leakage scan: PASS, 0 leaks.

Wave 1B tests repeatability and promotion readiness; it does not replace or erase Wave 1A.

## 3. Roles tested

Wave 1B tested only the authorised non-writer roles:

1. Mechanical QA;
2. Fresh Reader;
3. Editor;
4. Researcher / Fact Checker;
5. Showrunner;
6. Continuity / Canon Auditor.

Mechanical QA and Fresh Reader were prioritised in review because they already held the strongest repeated corrected-pack evidence. The other four roles were repeated to determine whether their Wave 1A quality and warning patterns held.

## 4. Roles excluded and writer carry-forward

Writer was not tested. Its controlling status remains exactly:

`WRITER ROLE — INELIGIBLE UNDER CORRECTED WAVE 0B CALIBRATION`

The corrected Wave 0B writer response was 1,231 words, exceeded the 900–1,200 contract, and placed required markers out of order. Wave 1B authority did not reopen that role. No extra-credit or alternate candidate model was tested.

## 5. Exact route, tools, and artifact controls

Every Wave 1B cell requested and served exactly:

- provider: `openai-codex`;
- model: `gpt-5.6-luna`;
- profile: `gpt56-luna`;
- tool policy: `none`;
- actual tool turns: `0`.

Aggregate execution evidence:

- exact requested/served route: 6/6 PASS;
- zero actual tool turns: 6/6 PASS;
- deterministic eligibility: 6/6 PASS;
- strict run-record validation: 6/6 PASS;
- immutable raw provider response: 6/6 preserved;
- Hermes wrapper stdout/stderr: 6/6 preserved separately;
- judged submission: 6/6 preserved separately;
- route evidence, validation result, normalization record and artifact hashes: 6/6 preserved;
- input tokens: 11,941;
- output tokens: 6,402;
- total tokens: 18,343;
- mean wall latency: 23,526 ms.

Known wrapper warnings remained in wrapper artifacts and were excluded from judged submissions. No route metadata, logs, warnings, or wrapper notices contaminated the blind bundle.

## 6. Deterministic eligibility and blind review

A fresh six-candidate blind bundle was created before scoring. Scout scored only the role-labelled blind submissions against the frozen role rubrics. Route and attempt metadata were not present in judged bundle files.

- blind bundle files scanned: 12;
- leakage scan: PASS, 0 leaks;
- private identity-map SHA-256: `bd59a80ba482822a6338bc68370cbfb2676d94b5c178887924e70a29cfe7a470`;
- private seed SHA-256: `b3c6e0883f9edc2546d1a5b58539f2ef92e7cf2f179167c418080d751d48e4c2`;
- score-schema validation: 6/6 PASS.

| Role | Exact route | Tool turns | Deterministic result | Human total | Penalty | Final | Critical flags |
|---|---:|---:|---|---:|---:|---:|---|
| Mechanical QA | PASS | 0 | eligible | 100 | 0 | 100 | none |
| Fresh Reader | PASS | 0 | eligible | 95 | 0 | 95 | none |
| Editor | PASS | 0 | eligible | 96 | 0 | 96 | none |
| Researcher | PASS | 0 | eligible with warning | 95 | 4 | 91 | none |
| Showrunner | PASS | 0 | eligible with warning | 89 | 2 | 87 | none |
| Continuity | PASS | 0 | eligible | 93 | 0 | 93 | none |

No role incurred a hard failure. No critical rubric dimension fell below half its available points.

## 7. Role-by-role comparison with Wave 1A

| Role | Wave 1A | Wave 1B | Delta | Repeatability finding |
|---|---:|---:|---:|---|
| Mechanical QA | 100 | 100 | 0 | Exact repeat of perfect deterministic and blind performance; all eight defects fixed with no false positives. |
| Fresh Reader | 93 | 95 | +2 | Strong repeat; spoiler-free experiential response, concrete confusion tracking, calibrated predictions, no revision-history invention. |
| Editor | 94 | 96 | +2 | Strong repeat; three prioritised diagnoses, 98.25% retention, protected events and sentences preserved, no unauthorised lore or replacement scene. |
| Researcher | 90 | 91 | +1 | Strong source/citation restraint, but the same R5 verdict mismatch repeated (`not-established` rather than harness ground truth `contradicted`). |
| Showrunner | 89 | 87 | -2 | Useful causal plan, but the same missing literal `three short beeps` warning repeated and the plan slightly overclaimed what the alarm proved. |
| Continuity | 88 | 93 | +5 | Improved defect coverage and clean contradiction/unsupported-certainty separation; case-related severity remains slightly understated. |

All six Wave 1B response hashes differ from their Wave 1A counterparts. Mechanical QA reached the same exact corrected passage through a separately generated JSON artifact.

## 8. Comparison with current production expectations

### Mechanical QA

Current expectation: mechanical-only changes, reproducible evidence, hard-gate handling, exact preservation, and false-positive restraint.

Observed: exact answer match, eight-entry issue ledger, no unseeded substitution, explicit mechanical-only scope, complete harness provenance. This meets the current candidate pipeline's Copy Edit / mechanical QA expectations.

### Fresh Reader

Current expectation: describe paying-reader experience without editorial prescription, track confusion and emotional movement, remain spoiler-free, and never invent revision history.

Observed: specific reactions to fresh water, the stair, Eli, the ticket and compass; candid continuation signal; uncertainty held as prediction; no fixes, production history, or off-page facts invented. This meets current Fresh Reader expectations.

### Editor

Current expectation: identify high-value structural/prose problems, make only the bounded revision authorised by the packet, preserve voice/events, and avoid replacement-scene behaviour.

Observed: accurate redundancy/fear/choice diagnoses, 98.25% retention, exact protected sentences, no event loss, no new lore, and no scope expansion. This meets the current controlled editorial expectation. Production assignment must still state whether a task is diagnosis-only or permits surgical revision.

### Researcher

Current expectation: remain closed-source when instructed, separate evidence from inference, label uncertainty, and avoid causal or supernatural overclaiming.

Observed: excellent citation integrity and evidence/inference separation. However, the repeated R5 verdict-label mismatch shows a stable classification-boundary weakness even though the prose reasoning is restrained. It does not yet meet production-assignment confidence without a fresh-variant confirmation.

### Showrunner

Current expectation: preserve canon, create causal escalation, identify future-book risks, distinguish evidence from certainty, and hand the writer a bounded decision contract.

Observed: strong seven-beat causal escalation and explicit continuity risks, but the repeated required-detail omission and alarm overclaim show a stable instruction-detail/evidence-boundary risk. It does not yet meet production-assignment confidence.

### Continuity

Current expectation: detect contradictions, timeline errors, location/person/state inconsistencies and unsupported certainties without rewriting or choosing repairs.

Observed: strong timeline, person, ticket, alarm, compass, water/roof and case findings; no invented repairs; clean classification. Slight case-severity understatement remains bounded. This meets current secondary continuity-audit expectations.

## 9. Role-by-role promotion recommendation

“Ready” below means ready for Andrew / Arden production-assignment review, not promoted and not authorised for production use.

- Mechanical QA: READY FOR PRODUCTION-ASSIGNMENT REVIEW. Three corrected-pack eligible results including two 100-point blind scores; strongest repeatability evidence.
- Fresh Reader: READY FOR PRODUCTION-ASSIGNMENT REVIEW. Three corrected-pack eligible results; repeated role separation and reader-experience quality.
- Editor: READY FOR PRODUCTION-ASSIGNMENT REVIEW. Two strong corrected-pack results; assignment contract must explicitly distinguish diagnosis-only from authorised surgical revision.
- Continuity: READY FOR PRODUCTION-ASSIGNMENT REVIEW as a bounded secondary audit role. Two eligible results with improved recall and no repair invention.
- Researcher: NOT YET READY. Requires Wave 1C because the same verdict-classification miss repeated in both valid waves.
- Showrunner: NOT YET READY. Requires Wave 1C because the same required-detail omission repeated, accompanied by a bounded evidence overclaim.
- Writer: EXCLUDED / INELIGIBLE under corrected Wave 0B calibration.

## 10. Risks and failure modes

- Frozen-task familiarity: Wave 1B proves independent repeatability on the frozen task, not generalisation to an unseen packet. Every response was fresh, but no alternate variant exists in v1.1.
- Showrunner instruction-detail loss: the literal `three short beeps` requirement was missed twice.
- Showrunner resistance to overclaiming: “accessed a restricted route” outran what a door-circuit change alone proves.
- Research verdict-boundary drift: sound cautious reasoning was paired twice with the wrong benchmark verdict label for R5.
- Editor permission boundary: the model performed well when a surgical revision was authorised; production prompts must not let diagnosis tasks silently become rewrite tasks.
- Continuity severity calibration: case-content/action defects were detected but may deserve higher downstream severity.
- No evidence here supports writer use, universal model status, automatic routing, or unsupervised production promotion.

## 11. Whether any role is ready for Andrew / Arden review

Yes. Mechanical QA, Fresh Reader, Editor, and Continuity have enough repeated corrected-pack evidence to be proposed for Andrew / Arden production-assignment review.

This is an evidence threshold only. Andrew / Arden must decide whether to assign any role, under what series/task boundaries, and with what shadow-run or review controls. No role assignment was made by this run.

## 12. Whether any role requires Wave 1C

- Showrunner: YES. Use a genuinely fresh holdout variant focused on required-detail retention, alarm/evidence boundaries, and future-book risk detection.
- Researcher: YES. Use a fresh closed-source variant with distinctions among contradicted, unsupported, not-established and qualified claims.
- Mechanical QA: no further Wave 1C is required for production-assignment review, though a fresh holdout remains advisable before broad institutional rollout.
- Fresh Reader: no further Wave 1C is required for production-assignment review, though cross-genre replication remains required for the final universal pipeline.
- Editor: no Wave 1C required for review; a diagnosis-only shadow task should be part of any approved assignment gate.
- Continuity: no Wave 1C required for bounded review; cross-series replication remains required before universal assignment.
- Writer: Wave 1C is not authorised by this report; ineligibility remains carried forward.

## 13. Evidence preservation

Canonical Wave 1B evidence:

`benchmarks/fiction-role-benchmark-v1.1/evidence/wave1b-gpt56-luna-20260810/`

The evidence directory contains six immutable attempts, provider/wrapper/judged artifact separation, route and tool evidence, deterministic validations, blind bundle, blind scores, leakage validation, aggregate summary, and artifact manifest.

- evidence files listed by manifest: 94;
- Wave 1B artifact-manifest SHA-256: `69e2f9a4cccfe9cbe6c74c7087d72bc5fab9db69d6b808dc1eb0ef7143a88263`.

## 14. Production and policy boundary confirmation

Wave 1B made no production runtime change, no Scout runtime change, no Hermes configuration change, no profile change, no production model-policy change, no canonical prose change, no deployment change, and no payment-infrastructure change. No extra-credit model was tested. `gpt-5.6-luna` was not promoted or assigned to production.

Scout remained `gpt-5.6-sol / openai-codex`. The candidate route remained `gpt-5.6-luna / openai-codex` through `gpt56-luna` only for isolated benchmark cells.

## 15. Final stop

Wave 1B evidence is complete. Stop for Andrew / Arden production-assignment review. Do not promote Luna, begin production use, test extra-credit models, change runtime/configuration/model policy, or alter canonical prose.
