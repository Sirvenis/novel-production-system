# Benchmark Specification

Benchmark ID: `fiction-role-benchmark-v1`
Pack version: `1.0.0`
Scenario: `The Last Ferry from Bellwether` (invented, noncanonical)
Primary comparison unit: one exact model/provider/role/attempt on frozen inputs

## Measurement model

Each role result has three layers:

1. provenance gate — exact requested and served route, packet hashes, configuration, timing, attempt, and failure evidence;
2. deterministic gate — parseability, required structure, preservation, required beats, forbidden terms, citation integrity, and known-answer checks where encoding is valid;
3. blind human/Scout score — role craft, judgement, usefulness, restraint, and reader effect.

Deterministic success cannot establish fiction quality. Human scoring cannot repair missing provenance or a routed/fallback identity. Both are required for promotion evidence.

## Comparable-run rules

A comparison cell is valid only when candidates share role, packet manifest hash, task version, sampling settings (or a declared controlled variable), tool policy, attempt policy, and output budget. Latency is wall-clock elapsed time measured outside the model. Record failures without deleting them.

## Score calculation

- Human rubric: 100 points per role.
- Deterministic penalties: role-specific, capped at 30 points; hard-gate failures make the run ineligible regardless of score.
- Final score: `max(0, human_total - deterministic_penalty)`.
- Promotion threshold for a later controlled trial: provenance PASS, no hard-gate failure, at least 75/100 final, and no critical rubric dimension below 50% of its available points.
- Model assignment requires repeated evidence; one passing v1 result is shortlist evidence only.

## Failure taxonomy

`route_mismatch`, `auth`, `rate_limit`, `entitlement`, `timeout`, `truncation`, `empty_output`, `schema`, `instruction`, `preservation`, `hallucination`, `citation`, `continuity`, `scope_creep`, `quality`, `other`.

## Stop and retry rules

- Stop immediately on route mismatch, paid entitlement gate, auth failure, or evidence that the packet changed.
- One technical retry is allowed only when a real transient variable changed; record both attempts.
- Never retry merely to hide a low quality score.
- Truncated output remains evidence. Do not ask the model to “output the complete chapter again”; use a fresh attempt with the same frozen task and record the budget change as a controlled variable.

## Limits of v1

The scenario is compact speculative suspense with relational tension. It does not prove romance chemistry, comic timing, cozy warmth, epic scale, culturally specific voice, or full-book endurance. Cross-genre and full-book gates remain mandatory.
