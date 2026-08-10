# Final Showrunner Compliance-Gate Report

Date: 2026-08-10
Custodian: Scout / Hermes under Andrew's final authority
Scout runtime: `gpt-5.6-sol / openai-codex`, verified from the live session log
Candidate: `gpt-5.6-luna / openai-codex`, profile `gpt56-luna`
Status: PASS RECOMMENDATION ONLY; STOPPED BEFORE PRODUCTION ASSIGNMENT

## 1. Exact authorisation

Andrew / Arden authorised one final Showrunner-only compliance gate after accepting the canonical Wave 1C evidence. This was not Wave 1D. It permitted one fresh Showrunner scenario, one candidate attempt, zero retries, zero tools, deterministic schema validation, blind substantive scoring, evidence preservation, institutional records, commits, pushes and parity verification.

Mechanical QA, Fresh Reader, Editor, Continuity, Researcher and Writer were not to be rerun. No extra-credit model, production assignment, universal Luna promotion, automatic routing, model-policy change, profile/configuration change, prose/canon change or infrastructure change was authorised.

## 2. Fresh scenario

The new scenario, “The Flood Gallery Decision”, is an adult near-future ecological-suspense scene at Blackglass Estuary Laboratory during a king tide. Tamsin Roe must interpret saltwater footprints, a deactivated access token linked to her missing brother, a floor-load state change, a courier's sealed specimen case, an incomplete delivery manifest and failing culvert surveillance before choosing which risk to confront first.

It tests causal scene architecture, the exact literal `LOT 6 / RETURN UNOPENED`, evidence-versus-inference restraint, downstream canon, three protected future explanation classes and a bounded writer handoff.

## 3. Freshness evidence

Freshness validation passed before execution:

- candidate-visible files: 4;
- prior candidate-visible hashes compared: 22;
- exact hash overlap: 0;
- prohibited prior marker hits: 0;
- no prior names, locations, incidents or evidence structures reused;
- `three short beeps` and `amber twice, pause, amber once` absent.

Record: `benchmarks/fiction-role-benchmark-v1.3-final-showrunner-compliance-gate/evidence/pre-run-freeze/freshness-validation.json`.

## 4. Frozen pre-run artifacts and hashes

A separate package was frozen and pushed before candidate execution:

- package: `benchmarks/fiction-role-benchmark-v1.3-final-showrunner-compliance-gate/`;
- frozen source commit: `71898e10dac66cb7aea8c6a1fc9d03b41889b8e2`;
- pre-run evidence commit: `a00ba21` (including the later path correction that preserved the Scout runtime excerpt);
- frozen files: 12;
- pack-manifest SHA-256: `37471ef1d564d8b2981612f0da9d872d803677463ef601a8984feaf5dcc3b25e`;
- candidate packet hash: `a2e12669bdfe33fd3bd213ef5cf0989404627d4a758c5f1507ad870550d166ea`;
- packet-manifest SHA-256: `2c056e7e61566e37c0653018366cce112d02d506b24a8f37098748c94fdf5149`;
- tests before execution: 7/7 PASS;
- package verification before execution: PASS.

Frozen material included the scenario, candidate packet, exact output schema, deterministic validator, scoring rubric, ground truth, no-tool launcher, tests and manifests. The output schema uses `additionalProperties: false` at the top level and nested object levels. `$schema` is not an allowed output property.

## 5. Scout runtime verification

The live default-session log recorded:

`model=gpt-5.6-sol provider=openai-codex`

Scout's runtime was not changed. Evidence: `evidence/pre-run-freeze/scout-runtime-evidence.txt`.

## 6. Candidate requested and served route

Requested:

- provider: `openai-codex`;
- model: `gpt-5.6-luna`;
- profile: `gpt56-luna`.

Served exactly the same route. Candidate session: `20260810_185640_4e4009`. Route result: PASS.

## 7. Actual tool turns

- tool policy: `none`;
- resolved tool definitions: 0;
- actual candidate tool turns: 0;
- API calls: 1;
- candidate attempts: 1;
- retries: 0.

## 8. Deterministic schema result

PASS.

The exact provider response and judged submission have the same SHA-256:

`6ed17dc957ec06103c30a1dde40641868e1e127fde297161eb4de1df405e0959`

Normalization actions: none.

Draft 2020-12 validation returned zero schema errors. All required properties were present. Beat IDs were exactly G1–G8 in order.

## 9. Structural violations

None.

- prohibited `$schema` property: absent;
- unknown/additional properties: none;
- Markdown fence: absent;
- explanatory preamble: absent;
- trailing commentary: absent;
- missing required structure: none.

The launcher encountered a post-response Python call-signature exception after it had preserved the exact response, judged submission, wrapper artifacts, normalization record and route evidence. The candidate was not retried. The already-frozen validator was invoked directly against the untouched submission, and bookkeeping was reconstructed from the preserved route/wrapper evidence. This did not repair or normalise the candidate output. Recovery evidence: `final-luna-showrunner-c1/harness-recovery-record.json`.

The frozen literal substring detector emitted one warning for `Cal used the token`. The phrase appears only inside explicit negated protections such as “Do not collapse ... into proof that Cal used the token”; it is not an overclaim. The warning remains preserved unchanged.

## 10. Blind leakage result

PASS, 0 leaks.

- blind alias: `CANDIDATE-001`;
- files scanned: 4;
- model/provider/profile/route/history/prior-score information exposed: none;
- private identity-map SHA-256: `00b945f03d1d52559b760f42c49abc652fda87d8b6c2c91eb7362b3fb1b1670e`;
- private seed SHA-256: `232f6763be793c3e39fecdc53fa0daec1807a9a679aaba9c7b56e5486e74f81d`.

## 11. Substantive blind score

Blind substantive score: **98/100**.

- causal architecture and escalation: 20/20;
- literal detail retention: 19/20;
- evidence/inference restraint: 20/20;
- canon/future-story protection: 20/20;
- bounded writer handoff/usability: 19/20.

No dimension was below half. No material regression was found. Blind verdict: `production-worthy`.

## 12. Literal-detail result

PASS.

All deterministic required literals were retained; `LOT 6 / RETURN UNOPENED` appeared three times. The blind scorer deducted one point because the 1,200-word target was not repeated in the writer handoff. This is a minor usability omission, not a material regression or schema failure.

## 13. Evidence/inference result

PASS, 20/20.

The floor-load status remained only evidence that the configured threshold was crossed. Credential acceptance remained only evidence that a registered credential was accepted. Neither became proof of a person, intrusion, presenter, identity, cause or Cal's survival.

## 14. Canon and future-story protection

PASS, 20/20.

The specimen case remains locked, sealed and intact; Esme is not established as knowingly lying; Cal neither appears nor is confirmed alive; salinity does not solve the cause; Esme is not isolated with Sable; equipment malfunction, staged human interference and an unknown ecological event all remain viable.

## 15. Bounded-handoff result

PASS, 19/20.

The handoff gives nine required inclusions, eight prohibited conclusions and a precise scene boundary. It is diagnosis/architecture material only and does not grant unbounded prose or canon authority. The only blind deduction was omission of the 1,200-word target from the handoff itself.

## 16. Comparison with the unresolved Wave 1C issue

Wave 1C established substantive Showrunner capability at 100/100 but failed deterministic eligibility by adding a prohibited top-level `$schema` property.

This final gate directly resolves that narrow issue:

- Wave 1C `$schema`: present and prohibited;
- final gate `$schema`: absent;
- Wave 1C schema result: FAIL;
- final gate schema result: PASS;
- final gate additional properties: none;
- substantive quality retained: 98/100, production-worthy, no material regression.

## 17. Final PASS/FAIL recommendation

**FINAL GATE: PASS.**

Recommendation:

`SHOWRUNNER — ELIGIBLE FOR ANDREW / ARDEN FINAL PRODUCTION-ASSIGNMENT APPROVAL.`

This is a recommendation only. Andrew retains final production-assignment authority.

## 18. Other-role rerun confirmation

No other role was rerun. Mechanical QA, Fresh Reader, Editor, Continuity, Researcher and Writer received zero new candidate attempts.

Researcher remains rejected for production assignment and closed to rerun or prompt repair unless Andrew / Arden explicitly reopens reconsideration.

Writer remains:

`WRITER ROLE — INELIGIBLE UNDER CORRECTED WAVE 0B CALIBRATION`

## 19. No assignment or policy change

No production assignment was made. Luna was not promoted universally, made the default fiction model or enabled for automatic routing. No Scout/candidate profile, model configuration, routing, production model policy, canonical prose, canon, deployment, payment or VPS infrastructure changed.

## 20. Evidence locations and manifest hash

Canonical package:

`benchmarks/fiction-role-benchmark-v1.3-final-showrunner-compliance-gate/`

Candidate and blind evidence:

`benchmarks/fiction-role-benchmark-v1.3-final-showrunner-compliance-gate/evidence/final-showrunner-compliance-gate-gpt56-luna-20260810/`

Complete evidence manifest:

`benchmarks/fiction-role-benchmark-v1.3-final-showrunner-compliance-gate/evidence/FINAL_SHOWRUNNER_GATE_ARTIFACT_MANIFEST.json`

- files listed: 36;
- manifest SHA-256: `76aba89491f55f7cadb4dd878c9ccb0895e906a06251b1ef7f672152ad799123`;
- candidate submission SHA-256: `6ed17dc957ec06103c30a1dde40641868e1e127fde297161eb4de1df405e0959`;
- blind score SHA-256: `c14586df75579b942826c79dd88e9037413c0f5e75aa1948b2e8d7fcf3efac3a`.

Preservation checks confirmed Wave 0, corrected v1.1/Waves 1A–1B, and Wave 1C paths unchanged from the pre-gate baseline. The unrelated untracked Brambleford verification file was untouched.

## Stop

The single authorised compliance attempt, validation, blind scoring and canonical technical evidence are complete. Stop after report/institutional records, commits, pushes, fetches and divergence verification. Do not implement the recommendation.
