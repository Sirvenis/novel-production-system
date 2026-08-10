# Fiction Role Benchmark — Wave 1C Fresh-Holdout Report

Date: 2026-08-10
Custodian: Scout / Hermes under Andrew's final authority
Scout runtime: `gpt-5.6-sol / openai-codex`, verified in the live agent log before reliance
Candidate route: `gpt-5.6-luna / openai-codex`, profile `gpt56-luna`
Status: EVIDENCE COMPLETE; STOPPED BEFORE PRODUCTION ASSIGNMENT OR PROMOTION

## 1. Exact scope and authorisation

Andrew / Arden authorised Wave 1C for two roles only:

1. Researcher / Fact Checker;
2. Showrunner.

The purpose was a genuine generalisation test against fresh holdouts, not another execution of the frozen v1.1 tasks. Mechanical QA, Fresh Reader, Editor, Continuity and Writer were not rerun. No extra-credit model was tested.

The four Wave 1B decisions carry forward unchanged: Mechanical QA approved for bounded production assignment; Fresh Reader approved for bounded production assignment; Editor approved with an explicit diagnosis-only versus authorised-surgical-revision control; Continuity approved as a bounded secondary audit role. Wave 1C did not route production work to any of them.

Writer remains exactly:

`WRITER ROLE — INELIGIBLE UNDER CORRECTED WAVE 0B CALIBRATION`

## 2. Holdout construction and freshness evidence

A separately identified extension was created at:

`benchmarks/fiction-role-benchmark-v1.2-wave1c-holdout/`

It contains wholly new invented content:

- Researcher: a closed Northglass conservation record with six claims testing supported, contradicted, qualified, unsupported and not-established verdicts, plus evidence/inference separation;
- Showrunner: a desert radio-observatory scene testing eight-beat causal escalation, exact-detail retention, limited telemetry conclusions, canon restraint, future-book risk detection and a bounded writer handoff.

The new literal requirement was the visual sequence `amber twice, pause, amber once`. It is unrelated in content and modality to the former missed requirement.

Freshness validation passed:

- candidate-visible exact-file hash overlap with v1.1: 0;
- Wave 1A/1B versus Wave 1C prompt-hash overlap: 0;
- Wave 1A/1B versus Wave 1C submission-hash overlap: 0;
- old scenario marker hits in candidate-visible material: 0;
- holdout frozen in commit `76a73eb363a2d875c5ec7e0fb38a2213ba80255c` before the first candidate run;
- holdout packet hash: `30f4830640314efb744cab2e16052b5531b0bb57b2e8e627bf13664a2082f1a1`.

Evidence: `evidence/wave1c-gpt56-luna-20260810/freshness-validation.json`.

## 3. Benchmark/version handling

The corrected v1.1 pack was not modified. It reverified immediately before holdout construction:

- files: 45;
- manifest SHA-256: `92e9dc13980b69aab21268ec38dcda1d62d8726a299317b960998faa1de65c05`;
- packet hash: `1aac9a7890a7ca4337719dae85f093d1d6ee24e2abf2810df49b23da55fc9ad8`;
- tests: 17/17 PASS.

The new holdout extension froze separately:

- frozen files: 16;
- manifest SHA-256: `085b2d6aade816e8f567e7d137dc928927a5180d19be187b0a225a80d78f3a70`;
- packet hash: `30f4830640314efb744cab2e16052b5531b0bb57b2e8e627bf13664a2082f1a1`;
- holdout tests: 4/4 PASS.

Ground truth and rubrics were committed and pushed before either candidate execution.

## 4. Route and Scout runtime verification

Live Scout evidence in `~/.hermes/logs/agent.log` recorded the current session as `model=gpt-5.6-sol provider=openai-codex`. Scout runtime was not changed.

Both candidate cells requested and served exactly:

- provider: `openai-codex`;
- model: `gpt-5.6-luna`;
- profile: `gpt56-luna`.

Exact route: 2/2 PASS. Per-cell immutable route evidence is preserved in each attempt directory.

## 5. Tool-turn evidence

For both cells:

- tool policy: `none`;
- resolved tool definitions: 0;
- actual tool turns: 0.

Aggregate: 0 tool turns across 2 cells. The known display-only Hermes warning for the invalid empty-toolset sentinel remains separated in wrapper artifacts and did not enter judged submissions.

## 6. Deterministic eligibility

| Role | Route | Tool turns | Schema/structure | Deterministic result | Penalty |
|---|---|---:|---|---|---:|
| Researcher | exact | 0 | PASS | eligible with warning | 12 |
| Showrunner | exact | 0 | FAIL: prohibited top-level `$schema` property | ineligible | 0 |

Researcher returned all six ordered assessments, valid citations and valid JSON, but its frozen-ground-truth validator found two wrong verdict labels: R4 and R5.

Showrunner preserved the content contract but added `$schema` to a schema with `additionalProperties: false`. This is a strict output-contract failure. The run was not retried because the failure was candidate instruction compliance, not a changed technical variable.

## 7. Blind leakage result

A fresh two-candidate blind bundle was created. Route, profile, model, attempt, provider-response and prior-wave information were absent.

- files scanned: 4;
- forbidden route/history terms checked: 11;
- leakage: PASS, 0 leaks;
- private identity-map SHA-256: `27b5aa642e37b186a7f22ce2336589832192c8855f13b3c1467227e96c74afdc`;
- private seed SHA-256: `2ad6d39eb674e921ce875586460822223bf685285b62ffc750d92d7b3d5189c4`.

## 8. Blind scores

| Role | Human total | Deterministic penalty | Final score | Eligibility | Critical flag |
|---|---:|---:|---:|---|---|
| Researcher | 85 | 12 | 73 | eligible with warning | none |
| Showrunner | 100 | 0 | 100 | ineligible | `INELIGIBLE_SCHEMA_CONTRACT` |

The Showrunner's 100-point human score does not cure ineligibility. The hard schema failure controls.

## 9. Researcher rubric findings

- Exact verdict classification: 27/40. R1 supported, R2 contradicted, R3 not-established and R6 not-established matched. R4 was labelled `supported` rather than frozen-ground-truth `qualified`; R5 was labelled `not-established` rather than `unsupported`.
- Citation integrity: 20/20. Every assessment used a valid supplied source; no outside evidence appeared.
- Evidence/inference separation: 15/15. The fields were consistently distinct and accurate.
- Uncertainty calibration: 13/15. Prose was cautious and substantively sensible, but two required taxonomy boundaries were missed.
- Production usability: 10/10. Concise, ordered and readable.

The key result is not softened by the quality of the prose: two of six required labels were wrong.

## 10. Showrunner rubric findings

- Causal architecture and escalation: 20/20. H1–H8 form a causal anomaly-to-decision chain.
- Literal detail retention: 20/20. Every explicit requirement survived; `amber twice, pause, amber once` appeared three times.
- Evidence/inference restraint: 20/20. Hatch telemetry never became proof of opening, crossing, intrusion or identity; the power request never became proof of sender.
- Canon/future-book protection: 20/20. Capsule, Jo, Arun, Keir, Voss and all three future explanation classes remained protected.
- Bounded writer handoff/usability: 20/20. Required inclusions and prohibited conclusions were explicit and operational.

Despite these strengths, the extra `$schema` property violated the exact output schema and made the cell ineligible.

## 11. Comparison with Waves 1A and 1B

Scores are directionally comparable but Wave 1C uses a new task and role-specific rubric.

| Role | Wave 1A | Wave 1B | Wave 1C | Generalisation finding |
|---|---:|---:|---:|---|
| Researcher | 90 | 91 | 73 | The verdict-label weakness repeated materially on a genuinely fresh taxonomy task. |
| Showrunner | 89 | 87 | 100 human / ineligible | Prior detail-retention and overclaim weaknesses resolved, but a new strict-schema failure controls. |

## 12. Whether repeated weaknesses persisted

### Researcher

Decision category: **C — repeats materially**.

The repeated weakness persists. As in Waves 1A and 1B, sound evidence handling and cautious prose were paired with wrong required verdict labels. Wave 1C broadened rather than removed the issue: two classification boundaries were missed.

### Showrunner

Prior weakness outcome: **A — resolved on the fresh holdout** for literal-detail retention and evidentiary overclaiming.

Overall cell outcome: **D — new production-significant weakness**.

The model retained the small explicit sequence, preserved all required details, and resisted the designed overclaim temptation. However, it failed the strict schema by adding an unrequested top-level property. Structural quality is therefore insufficient for eligibility.

## 13. New failure modes

One new production-significant failure appeared:

- Showrunner strict-output contamination: copied a schema declaration into the submission despite an exact `additionalProperties: false` contract.

No new route, tool, canon, detail-retention, overclaim, citation or leakage failure appeared.

## 14. Production-assignment recommendation — Researcher

**DO NOT ASSIGN TO PRODUCTION.**

The fresh holdout confirms that restrained reasoning cannot be trusted to produce the required classification label. The repeated weakness is material, not bounded enough for independent fact-check verdicts. No promotion or production routing is recommended from Wave 1C.

## 15. Production-assignment recommendation — Showrunner

**DO NOT ASSIGN TO PRODUCTION FROM THIS EVIDENCE.**

The original concern was resolved strongly, but the cell is deterministically ineligible due to strict-schema noncompliance. This report does not authorise a retry, shadow assignment, prompt repair or production use. Andrew / Arden must decide the next gate.

## 16. Exclusions and boundaries confirmed

- Writer was not rerun and remains ineligible under corrected Wave 0B calibration.
- Mechanical QA, Fresh Reader, Editor and Continuity were not rerun.
- The four Wave 1B production-assignment decisions were not altered.
- Luna was not promoted universally or made a default fiction model.
- No production task was assigned.
- No automatic production routing was enabled.
- No production model policy changed.
- No Scout or candidate profile/configuration/runtime state changed.
- No canonical prose or canon changed.
- No deployment, payment, VPS or extra-cost infrastructure changed.
- No extra-credit or substitute model was tested.
- The unrelated untracked Brambleford verification file was untouched.

## 17. Evidence locations and hashes

Canonical evidence directory:

`benchmarks/fiction-role-benchmark-v1.2-wave1c-holdout/evidence/wave1c-gpt56-luna-20260810/`

Key hashes:

- evidence artifact manifest SHA-256: `cfd2bc53a9c5b82f0e89822e74a6e954ab3240ce7774b7615c2415c7f5312939`;
- evidence files listed by manifest: 36;
- Researcher judged submission: `e08a646f904602d4ce669270533dff5f5b00fac344ed052f529adb53f7da2f1f`;
- Showrunner judged submission: `b85f86b9fad8b176498e5fca2704f833ac2b4e48541d11cb3ef0904d1d73795e`;
- holdout pack manifest: `085b2d6aade816e8f567e7d137dc928927a5180d19be187b0a225a80d78f3a70`;
- holdout packet: `30f4830640314efb744cab2e16052b5531b0bb57b2e8e627bf13664a2082f1a1`;
- private identity map: `27b5aa642e37b186a7f22ce2336589832192c8855f13b3c1467227e96c74afdc`;
- private blind seed: `2ad6d39eb674e921ce875586460822223bf685285b62ffc750d92d7b3d5189c4`.

Each attempt preserves prompt, zero-tool proof, immutable raw provider response, wrapper stdout/stderr, wrapper notices, judged submission, normalization record, route evidence, deterministic validation, run record, run-record validation and per-artifact hashes.

## 18. Final stop

Wave 1C evidence, scoring and recommendations are complete. Stop for Andrew / Arden's final production-assignment review.

Do not assign Researcher or Showrunner to production, change model policy, promote Luna, modify runtime/configuration/profile state, test Writer, test extra-credit models, alter canonical prose, or begin unrelated work.
