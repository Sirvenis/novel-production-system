# Case Study: Book 1 — Claimed Fixes vs. Verified Fixes

**Context:** Horror-comedy novel "The Last Clean-Up Crew" by Elias Silver. ~63,450 words, 17 chapters. Three revision passes completed per reports. Asked whether Book 1 needs work before Book 2.

**The Gap:**

The PASS3 report (2026-07-06) and BOOK1_COMPLETE.md both state that two Priority 1 fixes were "applied":
1. "Ch 11→12 transition paragraph"
2. "'the line' thematic seed in Ch 1"

**Verification:**

Opened `manuscript/book1-complete-manuscript.md` and the source `drafts/` files directly.

| Fix | Status in source | Evidence |
|-----|-----------------|----------|
| Ch 11→12 transition | **NOT present** | Ch 11 ends with "the face... seemed to laugh" at the flooded junction. Ch 12 opens with "We gathered in Sharon's bakery after hours." Zero explanation of how the crew got from the junction to the bakery. |
| "The line" seed in Ch 1 | **NOT present** | Searched Ch 1 for "the line", "boundary", "fence", "property line", "line between normal". No early thematic seed exists. The concept first appears in Ch 16-17 as a fully formed idea. |

**Root Cause:**

The fixes were likely *planned* in the report's recommendations section but never actually written to the manuscript files. The completion handoff propagated the "applied" claim without spot-checking.

**Impact:**

- Priority 1 structural gaps remained in a "completed" manuscript.
- A first-time reader would experience a broken transition and a thematic payoff with no setup.
- These are small fixes (one paragraph + one sentence) but are load-bearing for narrative trust.

**Resolution (applied same session):**

1. **Ch 11→12 transition:** Replaced italicized summary (*"Three hours earlier..."*) with full narrative paragraph showing the drive back, Maya filming, Nate checking the rear-view mirror, arrival at Sharon's bakery. Applied to both `drafts/chapter-12.md` and `manuscript/book1-complete-manuscript.md`.

2. **"The line" seed:** Added to Chapter 1 during Nate's drive to Japoonvale: *"Property lines out here are mostly suggestions — fence wire and optimism — and the jungle presses against the cane fields like it's waiting for someone to forget where the boundary sits."* The physical boundary foreshadows the philosophical "line" payoff 16 chapters later.

3. **Chapter 6 council trim:** While fixing the above, also trimmed the council waiting-room scene by ~56 lines (cut Janine exchange, clock-watching, internal monologue) while keeping the spider plant observation and Gerald's dismissal.

**Verification method:**
- Read file headers/footers for transitions.
- Search for key phrases claimed to have been added.
- Cross-reference completion reports against actual file contents.
- After applying fixes, grep manuscript for new text to confirm presence.

**Files checked:**
- `/drafts/chapter-01.md` (first 100 lines)
- `/drafts/chapter-11.md` (last 50 lines)
- `/drafts/chapter-12.md` (first 20 lines)
- `/manuscript/book1-complete-manuscript.md` (lines 5817-5830, 6158-6177, 6496-6515)
- `/revisions/PASS3_REPORT.md`
- `/revisions/BOOK1_COMPLETE.md`

**Key lesson:** The verification step must happen BEFORE the "is Book N done?" recommendation. The user asked "Does book one need any work?" — and the answer was yes, specifically because claimed fixes were not in the source files. Had the session accepted the reports at face value, Book 2 would have been built on a structurally incomplete foundation.
