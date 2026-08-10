# Fiction Role Benchmark v1.1

Status: corrected noncanonical harness; bounded calibration only. Wave 1 is not authorised.

Purpose: preserve v1's fiction-role comparison intent while repairing the execution contract exposed by Wave 0. This pack is harness evidence only. It cannot promote a production model, alter model policy, or modify canonical prose.

## Roles

Showrunner, writer, editor, fresh reader, researcher, continuity auditor, and mechanical QA.

## Candidate-visible input contract

`launchers/no_tool_runner.py` constructs every prompt from:

1. `packets/common.md`;
2. the matching role packet;
3. the matching task;
4. for structured roles, the complete matching JSON Schema embedded verbatim.

Candidates never receive rubrics, validator ground truth, score logic, identity maps, prior outputs, or route/scoring records.

## Genuine no-tool mode

Hermes currently has no documented empty-toolset CLI sentinel. The launcher passes `--toolsets none`, then independently resolves that selection through Hermes' installed tool registry before launch. `none` is not a registered toolset, so the enabled-toolset filter resolves to exactly zero tool definitions; a nonzero probe aborts the run.

The current CLI prints `Warning: Unknown toolsets: none`. This is a display warning, not fallback to profile tools. The launcher:

- preserves complete Hermes wrapper stdout/stderr;
- separates only that exact known warning;
- proves zero resolved tool definitions before launch;
- counts actual tool turns from the isolated session log;
- makes any nonzero tool-turn count ineligible.

This avoids modifying Hermes core/profile configuration while proving the intended no-tool contract.

## Artifact separation

Each immutable attempt directory preserves separately:

- `provider-response.raw.txt`: exact final assistant text emitted by Hermes after removing only the exact known wrapper warning;
- `hermes-wrapper-stdout.raw.txt` and `hermes-wrapper-stderr.raw.txt`;
- `wrapper-notices.txt`;
- `submission.json` or `submission.md`;
- `extraction-normalization.json`;
- `route-evidence.log`;
- `validation-result.json` and `run-record-validation.json`;
- `run-result.json` with requested/served route, profile, tool policy/count, sampling settings, usage, latency, session ID, route evidence, and artifact hashes.

Raw/wrapper/submission/validation artifacts are sealed read-only. Existing attempt directories are never overwritten.

## Verification

From this directory:

```bash
python3 validators/benchmark.py verify-pack
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m py_compile validators/benchmark.py launchers/no_tool_runner.py tests/test_benchmark.py tests/test_v11_repairs.py
```

All JSON Schemas must also parse and validate as Draft 2020-12.

## Bounded calibration command

Example only; calibration remains limited to Andrew's corrected Wave 0B authorization:

```bash
python3 launchers/no_tool_runner.py \
  --role mechanical-qa \
  --profile gpt56-luna \
  --provider openai-codex \
  --model gpt-5.6-luna \
  --attempt-id wave0b-luna-mechanical-qa-a1 \
  --out-dir evidence/wave0b-gpt56-luna-20260810/wave0b-luna-mechanical-qa-a1
```

## Boundaries

- No Wave 1 without separate authorization.
- No extra-credit model testing.
- No production model promotion from calibration scores.
- No profile/core configuration changes.
- No canonical prose, deployment, payment, or production-policy changes.
- Any pack change after calibration begins requires a new version and hashes.
