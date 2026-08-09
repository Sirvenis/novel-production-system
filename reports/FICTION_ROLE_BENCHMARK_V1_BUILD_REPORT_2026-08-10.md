# Fiction Role Benchmark v1 — Build and Verification Report

Date: 2026-08-10
Custodian: Scout / Hermes under Andrew's final authority
Runtime used for pack construction: `gpt-5.6-sol` via `openai-codex`, verified in `~/.hermes/logs/agent.log`
Status: PACK BUILT AND VERIFIED; MODEL RUNS NOT STARTED

## Scope completed

Built `benchmarks/fiction-role-benchmark-v1/` as a noncanonical reusable evaluation pack for:

- showrunner;
- writer;
- editor;
- fresh reader;
- researcher/fact checker;
- continuity/canon auditor;
- mechanical QA.

The pack uses the invented scenario *The Last Ferry from Bellwether*. It contains no canonical series prose.

## Controls implemented

- 21 model-visible packet/task/schema files frozen with SHA-256 hashes;
- packet-manifest SHA-256: `bd30312a7fa23ff226cbe06c32992d7b7de982c2a1741e4cfe7543f95777e282`;
- seven isolated role packets, prompts, and 100-point role-specific rubrics;
- exact requested/served provider and model fields, usage class, settings, latency, token/cost fields, route evidence, failures, and immutable artifact hashes;
- random blind aliases generated from an evaluator-held seed;
- identity mapping stored separately from blind bundles and protected from overwrite;
- deterministic checks for required beats/order, forbidden expressions/events, surgical preservation, source-event retention, packet-local citation integrity, known-answer research claims, continuity traps, exact mechanical correction, structure, and exact-route run records;
- explicit contamination, retry, truncation, promotion, cross-genre, and extra-credit stop rules;
- candidate test order that screens low/medium-usage models before high/extra-high candidates and keeps Kimi K3 behind Andrew's separate cost approval.

## Verification executed

Commands:

```text
python3 validators/benchmark.py verify-pack
python3 -m unittest -v tests/test_benchmark.py
python3 -m py_compile validators/benchmark.py tests/test_benchmark.py
jsonschema.Draft202012Validator.check_schema(...) for all eight schemas
git diff --check
```

Results:

- frozen files checked: 21;
- role packet/task/rubric triplets checked: 7;
- JSON Schemas checked: 8/8 valid Draft 2020-12 schemas;
- unit tests: 6/6 passed, including positive and negative submissions, citation failure, route mismatch, blinding leakage, and overwrite protection;
- Python compile: PASS;
- role/schema reference audit: PASS;
- Git whitespace check: PASS.

## Boundaries preserved

- model runs performed: 0;
- extra-credit use: 0;
- profile/core Hermes configuration changes: 0;
- canonical manuscript changes or promotions: 0;
- live deployment/payment changes: 0.

## Next gate

Present `benchmarks/fiction-role-benchmark-v1/CANDIDATE_TEST_ORDER.md` to Andrew. Do not start the run phase until Andrew authorises it. Extra-credit candidates remain separately cost-gated.
