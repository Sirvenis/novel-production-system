# Arden Studios Novel Production Pipeline Validation Status

Updated: 2026-08-10
Authority: Andrew is Founder and final authority; Scout / Hermes is Master Architect and validation custodian
Status: FINAL PIPELINE NOT YET SELECTED

## Controlling correction

Everything produced so far is evidence from testing. The current Stage 0 plus staged drafting/editorial framework is the strongest candidate baseline, but it is not the final universal Arden Studios novel-production pipeline.

The institutional goal is to discover the pipeline that produces the best repeatable novels, then apply that pipeline across every canonical novel series. Each series will receive its own role profiles, model assignments, SOUL, canon, voice rules, handoffs, and repository boundaries while conforming to the validated shared production framework.

## What remains provisional

- stage count, names, order, and gates;
- whether expansion is a universal stage or a diagnosis-triggered branch;
- where reader audits occur;
- profile roster and role boundaries;
- autonomy/checkpoint cadence;
- model assignment by role and series;
- context packaging and contamination controls;
- model-switch, fallback, and stop rules;
- quality measurements and final freeze criteria.

## Evidence already earned

- Last Clean-Up Crew demonstrated rapid autonomous drafting, multi-profile separation, staged editorial work, and the need for verification.
- The Better Version strengthened voice-first testing, guardrails, discovery passes, job statements, and surgical-edit discipline.
- Anunnaki, Brambleford, Meridian Relics, Nurse Fiction, and Yuga Cycle provide different genre, voice, research, continuity, and reader-contract pressures that the final pipeline must survive.

These are case studies, not proof that one current variant is universally optimal.

## Validation programme

### Gate 1 — Define measurable roles and outputs

For every candidate stage, specify:

- required inputs;
- permitted and prohibited actions;
- expected artifact;
- objective checks;
- human/Scout quality rubric;
- stop, retry, escalation, and promotion rules.

### Gate 2 — Model-role benchmark

Benchmark currently accessible cloud models on frozen, noncanonical packets for:

- showrunner/architecture;
- writer/voice and scene execution;
- developmental editor;
- line editor;
- copy/mechanical editor;
- fresh reader;
- researcher/fact checker;
- continuity/canon auditor;
- assembly/QA automation.

Models are selected by role and series. No provider or model is the universal author by default.

### Gate 3 — Pipeline variant comparison

Compare at least these candidate structures:

1. current Stage 0 plus staged drafting/editorial baseline;
2. diagnosis-driven branching, where expansion and extra editorial passes occur only when evidence triggers them;
3. checkpointed drafting with early voice/reader calibration and fewer late repair passes.

Use the same controlled creative brief and evaluation rubric. Keep outputs noncanonical.

### Gate 4 — Cross-genre replication

The preferred pipeline must work across at least two materially different genres/reader contracts, not only horror. It must preserve voice, produce adequate narrative abundance without padding, keep continuity, avoid editorial shrinkage, and remain operational across session boundaries.

### Gate 5 — Full-book production trial

Run one approved new book through the preferred pipeline from voice test to freeze. Record actual time, model usage, interventions, defects found by stage, reader outcome, rework, and repository/handoff integrity.

### Gate 6 — Institutional approval

Scout produces the final evidence synthesis. Andrew approves or rejects the proposed standard. Only after approval may the framework be labelled the final Arden Studios novel-production pipeline and rolled out across every series suite.

## Gate 2 benchmark-pack state

`benchmarks/fiction-role-benchmark-v1/` remains preserved as the original calibration/audit pack. Wave 0 proved exact routing and isolation but exposed a defective no-tool input contract: structured candidates saw schema paths without schema contents. Its 0/7 eligibility therefore cannot support model comparison.

Andrew authorised a corrected successor, `benchmarks/fiction-role-benchmark-v1.1/`. v1.1 embeds exact structured-output schemas in candidate-visible prompts, proves zero resolved tools and zero actual tool turns, separates immutable provider response from Hermes wrapper output and normalization, records explicit route/profile/settings/usage/latency/session metadata, validates full nested schemas, tightens writer length/order rules, rejects overwrite/leakage, and freezes a 45-file full manifest plus packet hash.

A bounded three-cell calibration used only `gpt-5.6-luna / openai-codex`: mechanical QA and fresh reader were deterministically eligible; writer remained ineligible at 1,231 words with markers out of order. Exact route passed 3/3 and tool turns were 0/3. These results validate the repaired harness and do not select or reject a production model. Full report: `reports/FICTION_ROLE_BENCHMARK_CORRECTED_WAVE0B_2026-08-10.md`.

No canonical prose, live profile configuration, series model policy, deployment, payment infrastructure, or extra-credit model was changed.

## Wave 1A evidence

Andrew / Arden accepted the corrected pack for bounded Wave 1A testing. Wave 1A ran `gpt-5.6-luna / openai-codex` through the existing `gpt56-luna` profile on all six non-writer roles. Exact route passed 6/6, actual tool turns were 0/6, and deterministic eligibility passed 6/6. Blind final scores were Mechanical QA 100, Fresh Reader 93, Showrunner 89, Editor 94, Researcher 90, and Continuity 88. Showrunner carried a 2-point required-phrase penalty; Researcher carried a 4-point verdict penalty. No hard failures or critical-dimension failures occurred.

Writer was deliberately not rerun and remains: `WRITER ROLE — INELIGIBLE UNDER CORRECTED WAVE 0B CALIBRATION`.

Full report: `reports/FICTION_ROLE_BENCHMARK_WAVE1A_2026-08-10.md`. Canonical evidence: `benchmarks/fiction-role-benchmark-v1.1/evidence/wave1a-gpt56-luna-20260810/`.

## Wave 1B promotion-readiness evidence

Andrew / Arden accepted Wave 1A eligibility evidence and authorised Wave 1B only. Six fresh independent non-writer runs used the same frozen corrected v1.1 tasks because the 45-file pack contains no alternate variants and could not be modified without creating a new benchmark version. All six Wave 1B submission hashes differ from Wave 1A.

Exact route passed 6/6, actual tool turns were 0/6, deterministic eligibility passed 6/6, and blind leakage scanning passed with 0 leaks. Blind final scores were Mechanical QA 100, Fresh Reader 95, Editor 96, Researcher 91, Showrunner 87, and Continuity 93.

Mechanical QA, Fresh Reader, Editor, and Continuity now have enough repeated corrected-pack evidence for Andrew / Arden production-assignment review. Showrunner and Researcher require Wave 1C because their Wave 1A warning modes repeated: Showrunner again omitted the literal `three short beeps`, while Researcher again classified R5 as `not-established` rather than the harness ground-truth `contradicted`. Writer remains `WRITER ROLE — INELIGIBLE UNDER CORRECTED WAVE 0B CALIBRATION`.

Full report: `reports/FICTION_ROLE_BENCHMARK_WAVE1B_2026-08-10.md`. Canonical evidence: `benchmarks/fiction-role-benchmark-v1.1/evidence/wave1b-gpt56-luna-20260810/`.

## Immediate next gate

Wave 1B evidence is ready for Andrew / Arden production-assignment review. Mechanical QA, Fresh Reader, Editor, and Continuity are proposed for review only; Showrunner and Researcher require Wave 1C; Writer remains ineligible. No model has been promoted or assigned. Stop before production use, Wave 1C, extra-credit testing, production model-policy changes, profile/configuration changes, or canonical prose work.