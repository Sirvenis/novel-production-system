---
name: fiction-editorial-audits-and-revision-planning
description: Use for read-only fiction discovery, reader/editorial audits, continuity/voice checks, and revision planning before prose changes.
version: 0.1.0-draft
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [fiction, novel-production, draft-skill, skill-split]
    related_skills: [longform-fiction-series-drafting]
---

# Fiction Editorial Audits And Revision Planning

## Purpose

Separate inventory, judgement, and planning from prose changes. This skill covers Discovery Pass, reader/editorial audits, continuity/voice checks, external review consolidation, and targeted revision-plan synthesis.

## When to Use

- A draft/pass is complete and needs read-only assessment.
- User authorizes audit but not prose changes.
- External/reader/steward feedback must be archived and interpreted.
- Need Discovery Pass inventory before editorial judgement.
- Need continuity, timeline, motif, voice, or tic detection.
- Need a targeted revision plan before edits.

## Stage Separation

| Stage | Allowed Output | Prose Changes? |
|---|---|---|
| Discovery Pass | factual inventory only | No |
| Reader reaction | customer/editorial experience report | No |
| Editorial audit | verdict + issues | No |
| Revision planning | targeted plan and scope | No |
| Revision execution | handled by revision skill | Yes, if approved |

## Procedure

1. Read the full required source stack for the audit scope.
2. Preserve raw external/reader feedback in repo-local reports if provided.
3. If running Discovery Pass, report only facts: files, counts, POV, timeline markers, anomalies.
4. If running editorial audit, state verdict and evidence, not fixes unless planning is authorized.
5. If planning revision, define exact scope, protected material, order, and stop gates.
6. Update governance files only to record the audit/plan and next gate.
7. Verify manuscript hash/diff unchanged for read-only work.
8. Commit/push reports.

## Continuity / Voice Checks

Use actual file reads and search counts. Flag issues with evidence. Do not repair during the check.

## Pitfalls

- Combining audit with immediate rewriting.
- Letting a reader report become automatic rewrite orders.
- Inventing fixes without reading the full relevant manuscript span.
- Treating current repo status as stale because an old case study says otherwise.

## Verification Checklist

- [ ] Audit scope and no-prose boundary explicit.
- [ ] Required files read.
- [ ] Report written to repo.
- [ ] Manuscript unchanged for read-only tasks.
- [ ] Next gate clearly recorded.
