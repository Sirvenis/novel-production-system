# Fiction Role Benchmark v1 — Wave 0 Calibration Report

Date: 2026-08-10
Custodian: Scout / Hermes under Andrew's final authority
Scope: Wave 0 only; no Wave 1, extra-credit, canonical prose, profile configuration, deployment, or payment work
Status: WAVE 0 COMPLETE; STOPPED BEFORE WAVE 1 FOR EVIDENCE REVIEW

## Runtime and repository preflight

- Scout runtime was verified from `~/.hermes/logs/agent.log` as `gpt-5.6-sol` via `openai-codex`.
- The comparison route was `gpt-5.6-luna` via `openai-codex`, using the existing lean `gpt56-luna` profile and ordinary ChatGPT Pro/Codex allowance.
- Exact served route evidence was captured from `/home/andrew/.hermes/profiles/gpt56-luna/logs/agent.log` for every attempt.
- `scout-handoffs`, `arden-studios`, and `novel-production-system` were fetched and verified clean, synchronized, and on `main` before the run.

## Deterministic preflight result

Re-executed before any model run:

- frozen pack verification: PASS, 21/21 model-visible files;
- packet-manifest SHA-256: `bd30312a7fa23ff226cbe06c32992d7b7de982c2a1741e4cfe7543f95777e282`;
- unit tests: 6/6 PASS;
- JSON Schemas: 8/8 valid Draft 2020-12 schemas;
- Python compilation: PASS;
- `git diff --check`: PASS.

## Attempts preserved

### Attempt set a1 — launcher/tool-isolation failure

The first seven role attempts used an empty `--toolsets` override. Hermes ignored the empty override and loaded profile tools. Three structured roles used one tool turn before the one-turn cap triggered Hermes' maximum-iteration summary path. All seven a1 attempts were preserved and marked invalid rather than deleted or silently replaced.

Observed cost of the contaminated launcher path:

- attempts: 7;
- input tokens: 86,255;
- output tokens: 5,681;
- mean wall latency: 29,243 ms;
- tool policy: unintentionally available.

### Attempt set a2 — controlled no-tool calibration route

The real transient variable was corrected by using an effective no-tool invocation. Hermes emitted a known `Warning: Unknown toolsets: none` CLI line, but profile-local route logs confirmed zero tool turns for all seven cells. The warning remains preserved in raw stdout and was removed only from the extracted submission artifact.

Observed route and usage:

- exact route: `openai-codex / gpt-5.6-luna`, verified for 7/7 cells;
- fresh isolated sessions: 7/7;
- tool turns: 0/7;
- input tokens: 11,005;
- output tokens: 9,640;
- mean wall latency: 31,200 ms;
- eligible deterministic submissions: 0/7.

Removing tool schemas reduced input use from 86,255 to 11,005 tokens across the seven-role route, an operationally material calibration finding.

## Deterministic findings by role

| Role | Route | Result | Main hard-gate finding |
|---|---|---|---|
| mechanical-QA | exact | fail | Output guessed `corrected_passage` and incompatible issue fields instead of the strict schema; exact mechanical validation failed. |
| continuity | exact | fail | Output used incompatible top-level/enum field names; strict schema failed. |
| researcher | exact | fail | Output omitted required `citations` arrays and `limitations`; citation-integrity gate failed. |
| reader | exact | fail | `desire_to_continue` was prose rather than the required `yes/maybe/no` enum. |
| editor | exact | fail | Output used guessed field names, did not retain protected sentences exactly, fell below the 85% preservation floor, and failed the required diagnosis contract. |
| showrunner | exact | fail | Output used extra/renamed fields and omitted exact `decision` and `protected_non_actions` fields. |
| writer | exact | fail | 1,561 words exceeded the 900–1,200 contract and required markers were out of order. |

## Principal calibration conclusion

The v1 execution instructions are not self-contained enough for a no-tool benchmark route. `README.md` says candidates receive only `common.md`, the role packet, and the task prompt, while six structured task prompts merely reference a schema by path instead of embedding or supplying its contract. With tools correctly disabled, the candidate had to guess key names and enums. The resulting 0/7 eligibility rate therefore measures a harness/input-contract defect as well as model instruction compliance; it cannot support model-role selection.

The writer failure separately shows that output-budget/length enforcement needs calibration even when no JSON schema is involved.

## Blinding calibration

- A seven-alias blind bundle was generated from the a2 submissions.
- Search found no model/provider identity leakage in the blind bundle.
- The identity seed and map are stored outside Git under `/home/andrew/.hermes/private-benchmark/fiction-role-benchmark-v1/wave0/` with mode `600`.
- An overwrite attempt failed as designed because the blind bundle already existed.
- Identity-visible raw evidence was committed before blind human scoring.

## Blind scoring and reveal calibration

- Seven blind human score records were created without evaluator access to model/provider identity, run records, deterministic validation, or the private mapping.
- Human totals were tightly compressed from 90 to 94 despite every run being deterministically ineligible: editor 90, reader 94, researcher 93, showrunner 94, mechanical-QA 91, writer 92, and continuity 91.
- After deterministic penalties, the numeric totals were editor 80, reader 94, researcher 93, showrunner 92, mechanical-QA 91, writer 92, and continuity 91. Every result remains ineligible because hard-gate failure overrides the numeric total.
- This proves the human rubric layer can recognise useful craft in malformed outputs, but its current single-scorer spread is too compressed to separate strong candidates reliably. Wave 1 should not use these totals as winner evidence.
- The delegated scorer sessions were configured to begin on Kimi K2.6 but activated fallback and were actually served by `gpt-5.5 / openai-codex`. The original score files incorrectly labelled the scorer `terra`; originals were preserved, and adjudicated copies correct the actual route without changing human scores.
- The seven score files existed and passed JSON Schema validation before Scout read the private identity map. The score hash manifest was written immediately after reveal rather than before it; this sequencing deviation is preserved as a calibration finding.
- Score evidence is under `benchmarks/fiction-role-benchmark-v1/evidence/wave0-gpt56-luna-20260810/blind-scoring/`.

## Required next gate

Do not begin Wave 1. Wave 0 evidence supports a bounded benchmark-pack revision/review gate first:

1. define a real no-tool launcher mode without a contaminating CLI warning;
2. supply the exact structured output contract to each structured role without exposing rubrics or ground truth;
3. preserve immutable raw provider response separately from CLI wrapper output;
4. record explicit execution-wrapper and sampling metadata;
5. tighten writer length/beat-order instructions without tuning to this one output;
6. rerun deterministic positive/negative tests and a single calibration route under a new pack version/hash;
7. review evidence before authorising Wave 1.

No frozen v1 packet, task, schema, rubric, validator, or canonical series file was changed during this Wave 0 run.
