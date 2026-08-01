---
name: fiction-project-governance-and-handoffs
description: Use when verifying fiction repo authority, git state, status files, handoffs, profile boundaries, or clean pause/closure.
version: 0.1.0-draft
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [fiction, novel-production, draft-skill, skill-split]
    related_skills: [longform-fiction-series-drafting]
---

# Fiction Project Governance And Handoffs

## Purpose

Maintain fiction project continuity and repository authority. This skill governs source-of-truth checks, handoffs, status files, profile-to-repo boundaries, clean pause/closure, and git verification. It does not draft or edit prose.

## When to Use

- New session/resumption for a fiction project.
- User asks whether work is preserved, canonical, pushed, or resumable.
- Migrating/splitting series repos or repairing authority documents.
- Updating `PROJECT_STATUS.yml`, handoff, tracker, decision log, completion notes, or closure reports.
- Preparing a repo for background/showrunner profile work.

## Required Inputs

- Canonical repo path and remote.
- `SOURCE_OF_TRUTH.md` / `REPOSITORY_AUTHORITY.md` if present.
- `PROJECT_STATUS.yml` or nearest status file.
- `handoff/CURRENT_PROJECT_HANDOFF.md` or project equivalent.
- Current git branch/status/log.
- Profile workdir/SOUL only if profile boundary is part of the task.

## Procedure

1. Verify live repo state: branch, remote, clean/dirty status, ahead/behind.
2. Read source-of-truth and authority files before interpreting project state.
3. Read current status/handoff/tracker/decision log.
4. Compare claims in status files against actual files when the task depends on them.
5. If updating governance files, keep changes factual and scoped.
6. Commit and push governance updates after validation.
7. Report exact files/commits and any blockers.

## Profile Boundary Rule

Profiles define role/runtime/workdir. Repositories hold canon and live state. Do not duplicate canon into profile SOULs. A profile SOUL should point to the repo authority stack and stop if it is missing or contradictory.

## Clean Pause / Closure

A project is cleanly paused only when:

- current manuscript/source files are preserved;
- reports/status/handoff reflect the real next gate;
- git is clean and pushed;
- no uncommitted generated/prose files remain unaccounted for;
- the next action is bounded and explicit.

## Pitfalls

- Reporting a commit as pushed before `git push` and clean tracking verification.
- Trusting memory over repo files.
- Treating a website or fork repo as manuscript truth without authority documents.
- Letting profile role instructions override current project status.

## Verification Checklist

- [ ] Canonical repo and branch verified.
- [ ] Authority/status/handoff files read.
- [ ] Actual files checked when claims depend on them.
- [ ] Git clean/pushed state verified after changes.
- [ ] No manuscript changes made unless explicitly in scope.
