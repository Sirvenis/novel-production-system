# Comprehensive Session Handoff Pattern

**Context:** Developed during Book 2 pipeline session when user said "We have had to compress this conversation a couple of times now, could you please update the Handoff Repo... so we can start a new session."

**The Problem:**

Context compression means the next session will lose conversation history. The handoff must become the single source of truth for all state that the next agent needs.

**The Solution:**

A comprehensive handoff file that includes everything the next agent needs to continue without asking questions.

---

## Handoff File: `handoff/<series>-session-comprehensive-handoff.md`

### Required Sections

1. **Header** — Date, session ended, next session plan, current totals, agent, model, git commit, working directory

2. **CRITICAL: What the Next Agent Must Know** — A numbered list of the most important facts. This section is designed to be read first and fast. Include:
   - Pipeline status (profiles created? SOUL.md written?)
   - Book status (which book, what phase)
   - Chapter status (which are committed, which are drafted, which need revision)
   - Any reviews completed and their verdicts
   - Any blockers or decisions pending

3. **Priority Fixes / Next Actions** — If there are specific tasks the next session must do, list them with file references and what needs to change. This prevents the next agent from having to re-read reports to extract actionable items.

4. **What Works (Preserve)** — List specific beats, lines, or techniques that the next agent should NOT change. This prevents well-meaning rewrites that destroy good material.

5. **Next Session Plan** — Numbered list of what to do, in order, with file references for each step.

6. **Critical Files** — Table of every file the next agent needs to read, with its purpose. Absolute paths.

7. **User Preferences** — Any user preferences that are relevant to this work. This is especially important because the next agent won't have conversation history.

8. **Git Status** — Repo, branch, latest commit, files changed, whether working tree is clean.

---

## Additional Files to Create

When a session involves subagent reviews (editor, reader), save their full reports as files in the project repo:

- `book2-drafts/editorial-report-ch02-ch03.md`
- `book2-drafts/reader-audit-ch02-ch03.md`

This allows the next agent to read the full reports without re-running the reviews.

---

## Commit Pattern

After creating the comprehensive handoff and any review reports:

```bash
git add -A
git commit -m "Session handoff: comprehensive state snapshot + [editorial/reader] report for [chapters]"
```

This ensures the handoff is versioned and the next session can check it out from git.

---

## Real Example

**File:** `handoff/book2-session-comprehensive-handoff.md` (The Last Clean-Up Crew — Book 2)

**What it contained:**
- 4 profiles created with paths to their SOUL.md and config.yaml
- Book 1 locked at commit 4007ec2, 63,128 words
- Book 2 architecture approved (The Deep Root, Tully/Mission Beach)
- Chapter 1 committed (2,847 words)
- Chapters 2-3 drafted but need revision (flagged with "NEEDS REVISION per editorial report")
- 10 specific fixes listed with "Why" for each
- "What Works" list of 8 specific beats to preserve
- Next session plan: read handoff → read reports → revise Ch 2 → revise Ch 3 → commit → draft Ch 4
- Table of 11 critical files with absolute paths
- User preference reminder: "User explicitly prefers pipeline setup BEFORE drafting"
- Git status: clean, commit e399272

**Result:** Next session can start immediately with `read_file` on the handoff, without needing to ask "what's the status?"

---

## When to Use This Pattern

- When context compression has occurred or is likely
- When the user explicitly asks for a handoff update
- When a session ends with unresolved work that the next session must continue
- When subagent reviews have produced findings that must survive across sessions
- When the project has moved from one phase to another (e.g., from drafting to revision)

---

*Reference: created 2026-07-15 during Book 2 pipeline session.*
