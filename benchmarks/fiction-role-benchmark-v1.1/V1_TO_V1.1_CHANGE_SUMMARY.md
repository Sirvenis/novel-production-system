# v1 to v1.1 Change Summary

Version: `fiction-role-benchmark-v1.1` / `1.1.0`
Base: frozen `fiction-role-benchmark-v1` / `1.0.0`
Scope: harness correction and bounded calibration only

## Defect corrected

v1's documented no-tool workflow supplied `common.md`, a role packet, and a task that merely referenced a schema path. A no-tool candidate could not read that path, so six structured roles had to guess exact keys, enums, nesting, and `additionalProperties` rules. The resulting deterministic failures were real submissions but invalid model-comparison evidence.

## Changes

1. Added `launchers/no_tool_runner.py` with an explicit zero-definition toolset probe, immutable attempt directories, wrapper/provider separation, extraction records, route/session/usage capture, artifact hashes, and overwrite protection.
2. Embedded each structured role's complete JSON Schema verbatim in candidate-visible prompt material at launch time without exposing rubrics, answers, validators, ground truth, identity maps, or scoring logic.
3. Added full Draft 2020-12 JSON Schema validation for structured outputs and run records.
4. Tightened the writer contract: 900–1,200 inclusive, headings count, any overrun/underrun is automatic hard-gate failure, literal marker definition, and mandatory first-occurrence beat order.
5. Expanded run metadata to requested/served provider and model, profile, tool policy, actual tool-turn count, sampling settings, token usage, wall/API latency, session identifier, route-evidence path, and artifact hashes.
6. Added positive/negative tests for structured submissions, launcher behavior, schema visibility, provider/wrapper separation, raw preservation, writer boundaries/order, route mismatch, tool turns, leakage, overwrite protection, and immutable artifacts.
7. Replaced the model-visible-only freeze with two records: packet manifest/hash plus full pack file/SHA-256 manifest.
8. Kept v1 and all Wave 0 evidence unmodified.

## v1 preservation proof before v1.1 calibration

- Git tree at current base commit for `benchmarks/fiction-role-benchmark-v1`: `d3091510478a99da36fb5ef8fb9e9af63858ba9c`
- Git tree for v1 Wave 0 evidence: `724844b748fa76f08d30c83c976023c4464bf234`
- v1 packet-manifest SHA-256: `bd30312a7fa23ff226cbe06c32992d7b7de982c2a1741e4cfe7543f95777e282`
- Working-tree changes under v1 at snapshot time: `0`

Future verification command:

```bash
git diff --exit-code -- benchmarks/fiction-role-benchmark-v1
```
