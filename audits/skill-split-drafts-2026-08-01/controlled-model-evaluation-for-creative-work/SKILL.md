---
name: controlled-model-evaluation-for-creative-work
description: Use for blind or multi-model creative experiments with frozen inputs, isolated outputs, identity reveal, synthesis, and promotion gates.
version: 0.1.0-draft
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [fiction, novel-production, draft-skill, skill-split]
    related_skills: [longform-fiction-series-drafting]
---

# Controlled Model Evaluation For Creative Work

## Purpose

Govern controlled creative model experiments. This is separate from routine drafting. It covers frozen inputs, isolated raw outputs, blind evaluation, identity reveal, synthesis, revision gates, and canonical-promotion gates.

## When to Use

- User approves a blind or multi-model prose experiment.
- Comparing model outputs for creative quality.
- Running reader/editor/showrunner evaluations without identity leakage.
- Promoting an approved experiment candidate to canonical manuscript.

## Non-Triggers

Do not use for normal chapter drafting. Do not run experiments just because a model is available. Do not promote a candidate without explicit gate approval.

## Procedure

1. Confirm experiment is explicitly authorized.
2. Freeze and hash the shared input package.
3. Verify exact runtime/profile/model routes.
4. Generate raw outputs in isolated non-canonical locations.
5. Commit raw outputs before evaluation.
6. Create blind mapping and keep identity key private/outside repo when required.
7. Run reader/editor/showrunner evaluations in the approved order.
8. Reveal identities only when authorized.
9. Synthesize results without confusing winner, base candidate, revised candidate, and canonical promotion.
10. Promote only the explicitly approved candidate and verify prose preservation.

## Linked References

- `references/legacy-generalized-lessons-20260801.md` — compact cross-series lessons distilled from legacy global references for this task class.

## Pitfalls

- Letting identity leak into blind evaluation.
- Regenerating outputs after the blind layer is compromised instead of repairing mapping when raw outputs remain valid.
- Treating winning draft as automatically canonical.
- Mixing model capability, provider runtime behavior, and editorial judgement.

## Verification Checklist

- [ ] User authorization recorded.
- [ ] Input package frozen and hashed.
- [ ] Runtime/model evidence recorded.
- [ ] Outputs isolated and committed.
- [ ] Identity mapping protected.
- [ ] Evaluation/reveal/promotion gates separated.
- [ ] Canonical manuscript unchanged unless promotion approved.
