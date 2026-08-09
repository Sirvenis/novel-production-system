# Mechanical Qa Rubric

Score the blind output without model/provider metadata. Total: 100. Quote evidence for every dimension.

## Correction accuracy — 35 points

- Full credit: All eight seeded mechanical/style-sheet errors are corrected exactly, including time, apostrophe, agreement, names and Australian spelling.
- Half credit: materially useful but incomplete, generic, uneven, or requiring bounded repair.
- Zero/low: absent, contradicted by the output, contaminated by another role, or harmful to downstream work.

## False-positive avoidance — 25 points

- Full credit: No grammatical but stylistically imperfect wording is “improved”; no unseeded substitution is introduced.
- Half credit: materially useful but incomplete, generic, uneven, or requiring bounded repair.
- Zero/low: absent, contradicted by the output, contaminated by another role, or harmful to downstream work.

## Exact preservation — 20 points

- Full credit: Sentence order, paragraphing and all text outside objective fixes remain byte-equivalent where line endings permit.
- Half credit: materially useful but incomplete, generic, uneven, or requiring bounded repair.
- Zero/low: absent, contradicted by the output, contaminated by another role, or harmful to downstream work.

## Issue-ledger completeness — 10 points

- Full credit: One ledger entry records each objective source-to-replacement change and the governing rule.
- Half credit: materially useful but incomplete, generic, uneven, or requiring bounded repair.
- Zero/low: absent, contradicted by the output, contaminated by another role, or harmful to downstream work.

## Scope and provenance discipline — 10 points

- Full credit: Declares mechanical-only scope and records valid source/corrected hashes through the harness.
- Half credit: materially useful but incomplete, generic, uneven, or requiring bounded repair.
- Zero/low: absent, contradicted by the output, contaminated by another role, or harmful to downstream work.

## Deterministic interaction

- Apply validator penalties only after human dimension scores are locked.
- A provenance, parse/schema, preservation, citation-integrity, required-beat, or exact mechanical hard failure makes the run ineligible even if the prose appears strong.
- Deterministic pass does not add points. Countable compliance is a floor, not evidence of reader delight.

## Critical dimension rule

A candidate cannot be promoted if any dimension scores below half its available points. Record critical flags, scorer confidence, and possible identity/style leakage.
