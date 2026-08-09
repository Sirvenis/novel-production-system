# Fiction Role Benchmark v1

Status: noncanonical reusable evaluation pack; no benchmark model outputs have been run or promoted.

Purpose: compare models by fiction-production role using identical frozen packets, exact route evidence, blind scoring, deterministic checks, and role-specific human judgement. This pack is evidence for Arden Studios pipeline validation; it is not a manuscript, series bible, model assignment, or final pipeline decision.

## Roles

1. showrunner — architecture and decision discipline
2. writer — voice-stable scene execution
3. editor — developmental diagnosis plus surgical revision
4. reader — uncontaminated reading experience
5. researcher — bounded evidence synthesis with packet-local citations
6. continuity — canon and timeline defect detection
7. mechanical-QA — exact, scope-limited correction and assembly checks

## Directory map

- `packets/`: model-visible frozen inputs
- `tasks/`: model-visible task prompts
- `rubrics/`: evaluator-visible scoring guides
- `schemas/`: JSON Schemas for run records and structured outputs
- `validators/`: deterministic pack/submission/blinding tools and private ground truth
- `manifests/`: frozen SHA-256 manifest and benchmark metadata
- `templates/`: run, score, failure, and adjudication records
- `tests/`: standard-library validator tests
- `runs/`: ignored local outputs; never place model output in canonical manuscript paths

## Reproducible workflow

1. Verify the pack: `python3 validators/benchmark.py verify-pack`
2. Create one fresh isolated run directory per exact provider/model/role.
3. Give the model only `packets/common.md`, its role packet, and its matching task prompt. Do not expose rubrics, ground truth, other role outputs, or identity mappings.
4. Record route evidence and timings in a run record conforming to `schemas/run-result.schema.json`. A requested route is not a verified route. Keep `score` null until blind score records are locked, then populate the post-reveal score summary.
5. Validate the run record: `python3 validators/benchmark.py validate-run --run-record RUN/run-result.json`
6. Validate the output: `python3 validators/benchmark.py validate-submission --role ROLE --submission PATH`
7. Blind outputs: `python3 validators/benchmark.py blind --runs-dir RUNS --out-dir BLIND --map-out PRIVATE_MAP.json --seed-file SECRET_SEED_FILE`
8. Score blind aliases independently with the role rubric. Deterministic checks are gates and penalties, not substitutes for reader delight or craft judgement.
9. Reveal identities only after score files are locked and hashed. Record adjudication and any rerun reason.

## Contamination controls

- Fresh session per run; no conversation carryover.
- Same packet hashes and task version for every candidate in a comparison cell.
- Writer, editor, and reader outputs are isolated. Reader never sees editorial reports; editor never sees reader scores; later candidates never see prior outputs.
- Model/provider identities are removed from blind bundles. Scorers use random aliases and must declare conflicts or recognisable style leakage.
- Temperature, reasoning mode, system prompt, tool access, retries, and truncation are recorded. A rerun is a new attempt, never an overwrite.
- No external web access for packet-local research; this tests evidence discipline, not browsing coverage.
- No candidate is selected from one sample. v1 is a calibration pack; later cross-genre packets must test replication.

## Hard boundaries

- No extra-credit model runs without Andrew's approval.
- No profile/core Hermes reconfiguration.
- No canonical prose or benchmark output promotion.
- No hidden fallback counted as the requested model.
- Pack changes after first scored run require a new semantic version and fresh hashes.
