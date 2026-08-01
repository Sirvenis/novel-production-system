---
name: controlled-fiction-revision-and-expansion
description: Use for approved prose-changing fiction revision, expansion, deepening, dramatization, line/cadence cleanup, and micro-polish.
version: 0.1.0-draft
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [fiction, novel-production, draft-skill, skill-split]
    related_skills: [longform-fiction-series-drafting]
---

# Controlled Fiction Revision And Expansion

## Purpose

Execute approved prose-changing passes safely. This skill covers Pass 1/Pass 2 workspaces, targeted developmental fixes, skeleton expansion, dialogue/monologue dramatization, line/cadence cleanup, and micro-polish.

## When to Use

- User approves a specific revision plan.
- A chapter or set of chapters needs targeted expansion/deepening.
- Dialogue desert or monologue-dominant scenes require dramatization.
- Late-stage cadence/consistency/micro-polish is authorized.
- Interrupted revision pass must be resumed without corrupting uncommitted work.

## Required Preflight

1. Read approved revision plan and current status/handoff.
2. Verify git state and identify dirty files.
3. Create/use a revision workspace when required.
4. Identify protected source files/chapters.
5. Define exact chapter/file scope and stop boundary.
6. Use safe mechanical insertion/replacement methods for long prose.

## Revision Procedure

1. Work one bounded unit at a time.
2. Preserve backups or source parity where required.
3. Make targeted edits only within approved scope.
4. Verify word count, chapter headings, duplicate paragraphs, scene markers, and protected-file diffs.
5. Reassemble only with explicit ordered loops, never fragile globs.
6. Write change report/completion note.
7. Update status/handoff/tracker.
8. Commit/push and stop at the boundary.

## Expansion Principle

Expansion should add reader value: dramatized pressure, atmosphere, relationship texture, or consequence. Do not pad word count mechanically.

## Linked References

- `references/legacy-generalized-lessons-20260801.md` — compact cross-series lessons distilled from legacy global references for this task class.

## Pitfalls

- Asking an LLM to rewrite a whole chapter and receiving a summary.
- Patch failures on Unicode-heavy prose.
- Duplicate insertion/orphaned sentence artifacts.
- Beautiful expansion moving reveals too early.
- Paragraph trimming for a chapter-level structural problem.

## Verification Checklist

- [ ] Revision plan approved and read.
- [ ] Scope limited to named files/chapters.
- [ ] Protected files verified unchanged.
- [ ] Word counts and duplicate/artifact scans run.
- [ ] Report/status/handoff updated.
- [ ] Commit pushed and tree clean.
