# Writer Execution Harness Specification

Status: DESIGN SPECIFICATION — not an execution script

The future harness must enforce controls that policy alone cannot prove.

## Required functions

1. Build candidate prompt from frozen packet without mutation.
2. Record prompt file hash before execution.
3. Launch exactly one candidate route: profile, requested provider, requested model.
4. Disable resolved tools where Hermes/profile supports it; in any case record zero actual tool calls and zero attempted tool invocations from logs/output.
5. Preserve raw provider response byte-for-byte before extraction.
6. Preserve wrapper stdout/stderr separately.
7. Extract required output without repairing compliance failures.
8. Run deterministic validator.
9. Build blind bundle only from immutable output.
10. Record run-result JSON with route, hashes, session id, usage/latency where available, and failure class.

## Retry policy

No automatic candidate retries. A failed route, malformed output, tool attempt, or deterministic failure is preserved as the candidate attempt. Any rerun requires Andrew / Arden authority and receives a new attempt ID; it must not overwrite the failed attempt.

## Tool policy wording

For Writer qualification, any tool call, attempted tool invocation, resolved tool turn, or hidden harness-side candidate assistance is disqualifying for that attempt. Deterministic validators and blind-pack builders may run after the candidate response, but they are not candidate tools and must be recorded as harness tools.

## Served route verification

The harness should prefer live Hermes logs over profile config. Config proves request intent; logs prove what served. If logs are unavailable, served route is marked unverified and the attempt cannot be promoted as controlled benchmark evidence.
