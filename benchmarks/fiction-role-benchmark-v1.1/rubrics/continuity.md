# Continuity Rubric

Score the blind output without model/provider metadata. Total: 100. Quote evidence for every dimension.

## Seeded-defect recall — 30 points

- Full credit: Finds the material time, location, person, water, roof, ticket, admission, alarm, compass and case conflicts or unsupported certainties.
- Half credit: materially useful but incomplete, generic, uneven, or requiring bounded repair.
- Zero/low: absent, contradicted by the output, contaminated by another role, or harmful to downstream work.

## Precision and false-positive control — 25 points

- Full credit: Each finding maps a specific summary fragment to a specific canon fact; valid material is not mislabelled.
- Half credit: materially useful but incomplete, generic, uneven, or requiring bounded repair.
- Zero/low: absent, contradicted by the output, contaminated by another role, or harmful to downstream work.

## Canon grounding — 20 points

- Full credit: Findings rely only on the supplied packet and distinguish direct contradiction from unsupported certainty.
- Half credit: materially useful but incomplete, generic, uneven, or requiring bounded repair.
- Zero/low: absent, contradicted by the output, contaminated by another role, or harmful to downstream work.

## Severity and classification judgement — 15 points

- Full credit: Critical/major/minor ratings reflect downstream damage; classifications are consistent and do not exaggerate ambiguity.
- Half credit: materially useful but incomplete, generic, uneven, or requiring bounded repair.
- Zero/low: absent, contradicted by the output, contaminated by another role, or harmful to downstream work.

## Role restraint — 10 points

- Full credit: Auditor records defects without rewriting prose, choosing plot solutions or inventing canon repairs.
- Half credit: materially useful but incomplete, generic, uneven, or requiring bounded repair.
- Zero/low: absent, contradicted by the output, contaminated by another role, or harmful to downstream work.

## Deterministic interaction

- Apply validator penalties only after human dimension scores are locked.
- A provenance, parse/schema, preservation, citation-integrity, required-beat, or exact mechanical hard failure makes the run ineligible even if the prose appears strong.
- Deterministic pass does not add points. Countable compliance is a floor, not evidence of reader delight.

## Critical dimension rule

A candidate cannot be promoted if any dimension scores below half its available points. Record critical flags, scorer confidence, and possible identity/style leakage.
