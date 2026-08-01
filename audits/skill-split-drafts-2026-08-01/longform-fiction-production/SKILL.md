---
name: longform-fiction-production
description: Use when routing longform fiction work to the right production-stage skill without loading series canon into the skill.
version: 0.1.0-draft
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [fiction, novel-production, draft-skill, skill-split]
    related_skills: [longform-fiction-series-drafting]
---

# Longform Fiction Production

## Purpose

Lean router for longform fiction work. It identifies the current production phase, verifies the repository authority stack, and routes to one task-class procedure. It must remain short: no series lore, no live chapter gate, no deployment recipe, and no historical case archive.

## When to Use

Use when the user asks for fiction work and the current stage is unclear, or when resuming a novel project before deciding whether the task is architecture, drafting, audit, revision, assembly, packaging, or model experiment.

Do not use this as the primary procedure once the stage is known. Load the stage-specific draft skill instead.

## Authority Order

1. Current user instruction in this chat.
2. Canonical series repo authority files: SOURCE_OF_TRUTH, REPOSITORY_AUTHORITY, PROJECT_STATUS, handoff, series SOUL, bible, book status/tracker/decision log.
3. Current git state and actual files.
4. Task-class Hermes skill.
5. Historical examples/case studies.

If repo authority conflicts with a historical skill reference, repo authority wins.

## Routing Map

| Situation | Route to |
|---|---|
| Canonical repo, status, handoff, profile boundary, git state | `fiction-project-governance-and-handoffs` |
| Concept, architecture, chapter map, research-only gate, controlled brief | `fiction-architecture-briefing-and-research-gates` |
| Approved chapter drafting, bounded pilot, autonomous run, canary | `controlled-fiction-drafting-and-autonomous-runs` |
| Read-only discovery, reader/editorial audit, revision plan, continuity/voice audit | `fiction-editorial-audits-and-revision-planning` |
| Prose-changing pass, expansion, line/cadence/micro-polish | `controlled-fiction-revision-and-expansion` |
| Full manuscript assembly, final QA, export/freeze, phase closure | `fiction-assembly-final-qa-and-freeze` |
| Reader package, feedback forms, reader-site generation | `reader-package-and-feedback-workflow` |
| Blind/multi-model creative experiment | `controlled-model-evaluation-for-creative-work` |

## Required Opening Checks

1. Identify the canonical series repo from handoff/status, not memory.
2. Verify git state before edits.
3. Read current project status and handoff.
4. Determine whether prose changes are allowed.
5. Determine whether model/runtime is gated.
6. Route to exactly one primary task skill.
7. Stop and report if authority files are missing or contradictory.

## Pitfalls

- Letting the router become another archive.
- Treating series-specific examples as current canon.
- Loading reader-site/deployment procedures for manuscript drafting.
- Mixing read-only audits with prose-changing revision.

## Verification Checklist

- [ ] Current canonical repo identified from files.
- [ ] Current gate/status read.
- [ ] Git state checked.
- [ ] One task-class route selected.
- [ ] No live skill/config/profile changes made by the router.
