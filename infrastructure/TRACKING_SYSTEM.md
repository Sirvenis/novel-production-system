# Tracking System

## Overview

The tracking system maintains the ground truth of what exists, what stage each component is at, and what decisions have been made. It is the showrunner's dashboard.

**Critical rule:** The manuscript is the ground truth. Trackers are aspirational. Verify against source files.

---

## Core Tracking Files

### `tracking/BOOK<N>_TRACKER.md`

The chapter-by-chapter status board.

**Columns:**
| Column | Meaning |
|--------|---------|
| Chapter | Number and title |
| Status | PENDING / DRAFTED / EXPANDED / EDITORIAL / FIXES / LINE_EDIT / COPY_EDIT / COMPLETE |
| Word Count | Actual (from source, not target) |
| Job Statement | One-sentence mandate |
| Notes | Blockers, deferred items, decisions |

**Status Definitions:**
- **PENDING:** Not yet drafted
- **DRAFTED:** First pass complete
- **EXPANDED:** Tier 1 expansion complete
- **EDITORIAL:** Under developmental review
- **FIXES:** Priority 1 fixes applied, awaiting verification
- **LINE_EDIT:** Stage 6 complete
- **COPY_EDIT:** Stage 7 complete
- **COMPLETE:** Passed final QA

### `tracking/BOOK<N>_DASHBOARD.md`

The project-level status summary.

**Sections:**
- Current stage
- Total word count (actual, not target)
- Chapters complete / total
- Blockers (active)
- Next task
- Last updated
- Pipeline phase checklist

### `tracking/BOOK<N>_DECISIONS.md`

Every production decision with rationale and impact.

**Format:**
```
DEC-YYYYMMDD-NNN: [Title]
**Decision:** [What was decided]
**Rationale:** [Why, based on what evidence]
**Evidence:** [File references, data points]
**Impact:** [What changes downstream]
**Status:** ACTIVE | PENDING | SUPERSEDED | REVOKED
**Recorded by:** [Role]
```

### `tracking/BOOK<N>_DISCOVERY_PASS.md`

Pure inventory from the Discovery Pass.

**Sections:**
- Actual word counts per chapter
- Architecture alignment check
- Contradictions with series bible
- TK placeholders
- Classification table: Adequate / Lean / Underweight

**Rule:** No recommendations. No plans. Just raw data.

---

## Status Definitions (Full Set)

```
PENDING → DRAFTED → EXPANDED → EDITORIAL → FIXES → LINE_EDIT → COPY_EDIT → COMPLETE → FROZEN
```

**Special states:**
- **CONTRADICTION:** Multiple audits disagree on status. Document and resolve.
- **PARKED:** Active work paused indefinitely.
- **CANCELLED:** Will not be completed.
- **REVISION_NEEDED:** Returns to earlier stage.

---

## Handoff Integration

The tracking system feeds into the handoff system:

1. After every session, update the tracker
2. Update `handoff/MASTER-HANDOFF.md` with tracker summary
3. The next session reads the handoff, then the tracker, then the source files

**Never rely on the tracker as the sole source of truth.** Always verify against the manuscript.

---

## Decision Log Discipline

Every production decision gets logged. This prevents the "why did we do that?" problem when revisiting a book months later.

**When to log:**
- Pipeline changes (adding a new stage, modifying a rule)
- Architecture changes (adding/removing chapters, changing beats)
- Editorial verdicts (READY / NEEDS FIXES / NOT READY)
- Reader Audit classifications (MUST FIX / INVESTIGATE / etc.)
- Fix deferrals ("deferred to Reader Audit")
- Scope decisions ("Baltic Sea remains secondary seed")

**When NOT to log:**
- Routine tracker updates
- Commit messages (these are in git history)
- Session summaries (these are in handoffs)

---

## Common Pitfalls

- **Tracker neglect:** The tracker often becomes stale. Treat it as aspirational, not ground truth.
- **Status inflation:** Marking chapters COMPLETE before they have actually passed QA.
- **Decision amnesia:** Not logging why a decision was made, forcing future sessions to re-derive the rationale.
- **Word count caching:** Using `wc -w` on a file after `write_file` — the output is stale. Use line-range extraction or `read_file` verification.
- **Tracker as report:** The tracker is for status, not for narrative. Keep decisions in DECISIONS.md, narratives in handoffs.
