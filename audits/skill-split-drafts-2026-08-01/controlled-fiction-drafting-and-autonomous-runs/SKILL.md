---
name: controlled-fiction-drafting-and-autonomous-runs
description: Use when drafting approved fiction chapters or running bounded autonomous fiction drafting with repo-local reports and stop gates.
version: 0.1.0-draft
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [fiction, novel-production, draft-skill, skill-split]
    related_skills: [longform-fiction-series-drafting]
---

# Controlled Fiction Drafting And Autonomous Runs

## Purpose

Draft fiction only after approval gates are satisfied. Covers one approved chapter, bounded pilots, autonomous continuation, canary runs, runtime checks, and honest completion reporting.

## When to Use

- User approves one chapter from a prepared brief.
- User approves a bounded multi-chapter pilot.
- A showrunner launches or verifies a writer profile canary.
- Autonomous run needs repo-local reports, commits, and stop gates.
- Resuming interrupted drafting where the next chapter is clearly authorized.

## Required Preflight

1. Verify runtime if the repo/user has a model gate.
2. Verify git state.
3. Read current status/handoff/tracker and approved brief/map.
4. Confirm exactly what prose is authorized.
5. Hash/check protected prior chapters if required.
6. Use reliable file I/O for long chapters; avoid large-fiction `write_file` truncation.

## Drafting Procedure

1. Draft exactly the authorized unit.
2. Write to the canonical path using safe file I/O.
3. Verify word count from actual file content.
4. Update tracker/status/handoff/completion note.
5. Assemble or validate only if that is part of the gate.
6. Commit and push.
7. Stop at the authorized boundary.

## Autonomous Run Rules

- Use canary runs before scaling a profile.
- Worker reports go into the repo, not raw Telegram chatter.
- Commit/push at defined checkpoints.
- If output becomes a lean skeleton or falls below target gate, label it honestly and stop/expand only if authorized.
- Do not continue past checkpoint just because the model recommends it.

## Canary Requirements

A canary must be small, representative, verifiable, and logged. Assess instruction adherence, output quality, pipeline compliance, state management, and drift before granting autonomy.

## Linked References

- `references/legacy-generalized-lessons-20260801.md` — compact cross-series lessons distilled from legacy global references for this task class.

## Pitfalls

- Continuing on fallback when the project requires a specific model.
- Drafting more chapters than approved.
- Calling a skeleton a complete draft.
- Trusting end markers instead of actual word counts.
- Letting a worker’s final message substitute for file verification.

## Verification Checklist

- [ ] Runtime/model gate checked if relevant.
- [ ] Scope and stop condition explicit.
- [ ] File exists and word count verified.
- [ ] Tracker/status/handoff/report updated.
- [ ] Git commit pushed and clean.
- [ ] No unauthorized next chapter started.
