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

`benchmarks/fiction-role-benchmark-v1/` was built and deterministically verified as the first reusable noncanonical role-evaluation pack. Wave 0 then ran one ordinary-account comparison route across all seven roles: `gpt-5.6-luna` via `openai-codex`.

Wave 0 preserved fourteen attempts: seven invalid launcher attempts with unintended tool availability and seven controlled no-tool attempts. Exact routing passed 7/7 controlled cells, but deterministic eligibility was 0/7. The principal defect is the execution contract: the documented no-tool workflow gives structured roles task prompts that reference schemas by path without supplying the schema contents, forcing candidates to guess strict field names and enums. The writer also exceeded its word range and beat-order contract.

Blind craft scores were compressed at 90–94 even though every run was hard-gate ineligible. This confirms that human craft scoring and deterministic compliance measure different things, but the current single-scorer spread is not discriminating enough for model selection. Full evidence and route corrections are recorded in `reports/FICTION_ROLE_BENCHMARK_WAVE0_CALIBRATION_2026-08-10.md`.

No canonical prose, live profile configuration, series model policy, deployment, payment infrastructure, or extra-credit model was changed.

## Immediate next gate

Wave 0 is complete. Stop before Wave 1 for evidence review. The next proposed gate is a bounded benchmark-pack revision under a new version/hash: make the no-tool launcher explicit, supply each strict output contract without exposing rubrics or ground truth, preserve raw provider output separately from CLI wrapper text, correct scorer-route capture, strengthen pre-reveal score locking/hashing, and recalibrate writer length/beat compliance. Do not start that revision or any Wave 1 model screen until Andrew authorises the next phase. Kimi K3 and all other extra-credit use remain separately cost-gated.