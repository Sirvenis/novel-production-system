# Pipeline Validation Current Handoff

Updated: 2026-08-11
Custodian: Scout / Hermes under Andrew's final authority
Status: WRITER + PIPELINE ACCEPTANCE DESIGN PACKAGE COMPLETE; STOPPED AT EXECUTION GATES

## Canonical lane

- Repository: `/home/andrew/novel-production-system`
- Branch: `main`
- Controlling status: `PIPELINE_VALIDATION_STATUS.md`
- Current planning-phase report: `reports/NOVEL_PRODUCTION_SYSTEM_PLANNING_PHASE_DESIGN_2026-08-11.md`
- Validation report: `reports/NOVEL_PRODUCTION_SYSTEM_DESIGN_VALIDATION_2026-08-11.md`

## Completed in this phase

Andrew / Arden authorised design only for two workstreams and explicit background-profile orchestration. Scout verified repo state and runtime, preserved Codex capacity where possible, used non-Codex background challenge lanes, and completed the design package.

### Workstream A — Comparative Writer Qualification, design only

Package: `benchmarks/comparative-writer-qualification-v1.0-design/`

Includes:

- `COMPARATIVE_WRITER_QUALIFICATION_DESIGN.md`
- Packet 01 frozen candidate packet: `packet-01-genre-neutral/candidate_packet.md`
- Packet 02 frozen cross-genre holdout: `packet-02-cross-genre-holdout/candidate_packet.md`
- ground truth files for both packets
- deterministic validator and fixtures under `validators/`
- `SCORING_RUBRIC.md`
- `BLIND_SCORING_ARCHITECTURE.md`
- `SCORER_ARCHITECTURE.md`
- `EXECUTION_HARNESS_SPEC.md`
- `WRITER_DESIGN_SHA256.json`

Controls included: route requirements, zero-tool/no-attempt policy, immutable raw-response rules, deterministic disqualifiers, no automatic retry, blind reader/editor/showrunner procedures, leakage controls, critical 8/10-equivalent floors for voice/continuity/instruction, and route-unverifiable cannot pass.

Do not execute GPT-5.5, Kimi K2.6, GLM-5.2, Packet 01, or Packet 02 until Andrew / Arden approve. Luna Writer remains closed/ineligible.

### Workstream B — Novel Production Pipeline Acceptance Programme, design only

Package: `acceptance-programmes/novel-production-pipeline-acceptance-v1.0-design/`

Includes:

- acceptance programme README
- creation-pipeline bridge definitions
- manuscript-production stage definitions
- conditional stage trigger rules
- Night Shift acceptance-test plan
- Anunnaki Book 4 acceptance-test plan
- 16-novel retrospective regression-audit plan
- acceptance metrics and thresholds
- stage-to-defect mapping
- known-defect register spec
- evidence/provenance architecture
- usage estimate
- background-profile/model usage record
- design challenge synthesis
- explicit execution gates
- `PIPELINE_ACCEPTANCE_DESIGN_SHA256.json`

Controls included: source lock, deterministic scans before expensive diagnosis, preservation lists, confidence/intentionality flags, canon/voice citations, research triggers, no automatic all-stage processing, fresh source-lock before intervention, and no prose changes without Andrew / Arden approval.

## Independent challenge review

Completed review lanes:

- `glm` / `glm-5.2:cloud`: pipeline architecture challenge, APPROVE WITH CHANGES.
- `scout-cloud-creative` / `kimi-k2.6:cloud`: benchmark fairness/bias challenge, APPROVE WITH CHANGES.
- `scout-cloud-research` / `qwen3.5:cloud`: preservation/anti-overediting challenge, APPROVE WITH CHANGES.

Failed lane:

- `scout-cloud-audit` / `deepseek-v3.2:cloud`: failed HTTP 410 retired model; preserved as provenance only.

Material challenge findings were incorporated into the frozen design package and recorded in `DESIGN_CHALLENGE_SYNTHESIS.md`. Background conclusions are design-review evidence, not controlled benchmark evidence or production assignments.

## Validation

- Writer validator pass fixture: exit 0, deterministic eligible.
- Writer validator fail fixture: exit 2 as expected, deterministic disqualifier.
- Python compile: 0 errors.
- JSON parse: 0 errors.
- Hash manifests generated for Writer and pipeline packages.

## Boundaries preserved

No Writer candidate was executed. No holdout was executed. Night Shift was not processed. Anunnaki Book 4 was not processed. The 16 Library-ready novels were not audited or revised. No canonical prose, production role assignment, model policy, Hermes config, web work, deployment, payment, or VPS infrastructure changed.

## Exact next action

STOP for Andrew / Arden review of:

1. `benchmarks/comparative-writer-qualification-v1.0-design/`
2. `acceptance-programmes/novel-production-pipeline-acceptance-v1.0-design/`

Do not cross any execution gate until Andrew / Arden explicitly approve the next run.
