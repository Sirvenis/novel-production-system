# Production Pipeline — The 9-Stage System

## Overview

This document describes the complete production pipeline for a multi-book novel series, from architecture through freeze. Each stage has defined inputs, outputs, criteria, and verdicts.

**Origin:** Developed and refined across three complete books of a working-class cosmic horror series (2026). Every rule exists because something broke.

**Assumption:** You have already confirmed your pipeline approach (see `GETTING_STARTED.md`).

---

## Stage 1: Architecture

**Purpose:** Blueprint before prose. Every chapter declares what it must make the reader believe or feel.

**Inputs:**
- Series bible (if series book N+1)
- Concept brief (1-page premise)
- Decision to proceed

**Outputs:**
- `BOOK<N>_ARCHITECTURE.md`
  - Chapter-by-chapter breakdown
  - Each chapter: Job Statement + word range + key beats
  - Character positions at start and end
  - Thematic through-lines
  - Sequel hooks / series seeds
- `BOOK<N>_PIPELINE.md` (if multi-profile)
- `tracking/BOOK<N>_TRACKER.md`

**Key Rules:**
- Job Statement = one sentence: "This chapter exists to make the reader believe [X]."
- Word ranges are job-based, not fixed. See `CRAFT_TECHNIQUES.md` for the range table.
- Architecture is a contract, not a suggestion. Deviations must be tracked.

**Verdict to proceed:** Architecture approved by showrunner (and author, if human). No prose until approved.

---

## Stage 2: Drafting

**Purpose:** Words on page. First pass. Do not polish.

**Inputs:**
- Architecture document
- Tracker with status column
- Handoff with current state

**Outputs:**
- `drafts/chapter-NN.md` for each chapter
- Git commits after each chapter (or each session)
- Updated tracker

**Key Rules:**
- Write the chapter's Job Statement at the top of every draft as a constraint.
- When a draft exceeds its mandate, stop and split — do not compress.
- Autonomy mode: if granted tactical autonomy, draft → self-edit → commit → proceed silently. Announce only blockers.
- Procedural verbosity is noise under autonomy. Announce: blockers, session-end summary, tool failures.

**Verdict to proceed:** All chapters drafted. Tracker shows COMPLETE for all.

---

## Stage 3: Expansion (Pass 2)

**Purpose:** Lean chapters to weight. Identify which chapters are thin and expand them.

**Inputs:**
- Complete draft set
- Architecture document (for comparison)

**Process:**
1. **Discovery Pass** (CRITICAL): Pure inventory. No recommendations.
   - Extract actual word counts per chapter (line-range extraction, not `wc` on whole file)
   - List what exists, what contradicts series bible, TK placeholders
   - Classify each chapter: Adequate / Lean / Underweight
   - Output: `tracking/BOOK<N>_DISCOVERY_PASS.md`
2. **Tier-Based Expansion Priority:**
   - Tier 1 (Critical): Core revelation, major action, emotional climax chapters
   - Tier 2 (High): Lean but job-present chapters
   - Tier 3 (Medium): Transitions, secondary action
3. **Expansion execution:** Weave new material into existing scenes, do not append.

**Outputs:**
- Expanded chapter drafts
- Updated tracker
- Discovery Pass report

**Verdict to proceed:** All Tier 1 chapters expanded. Tier 2/3 may remain lean if job is complete.

---

## Stage 4: Developmental Editorial (Pass 3)

**Purpose:** Structural assessment. Does the story work?

**Inputs:**
- Expanded draft set
- Discovery Pass report
- Series bible (for continuity)

**Process:**
1. Sample chapters across the manuscript (opening, middle, climax, finale)
2. Run the **Four Questions** (see `references/DEVELOPMENTAL_STRUCTURAL_FOUR_QUESTIONS.md`):
   - Q1: Does tension continually escalate?
   - Q2: Does the key character arc feel inevitable?
   - Q3: Does the central mechanism become more understandable without losing mystery?
   - Q4: Does the ending create anticipation for the sequel?
3. Write `BOOK<N>_EDITORIAL_REPORT.md`:
   - Executive verdict: READY / NEEDS TARGETED FIXES / NEEDS MAJOR REWRITE
   - Priority 1 blockers (must fix)
   - Priority 2 significant concerns
   - Priority 3 polish items
   - Continuity audit table
   - Structural assessment by act
   - Prose cadence assessment
   - Word count analysis

**Verdict to proceed:** Verdict = READY or NEEDS TARGETED FIXES. Major rewrite returns to architecture.

---

## Stage 5: Targeted Fixes (Pass 3.5)

**Purpose:** Apply ONLY Priority 1 blockers identified by developmental editorial.

**Key Rules:**
- Surgical only: thread-continuity gaps, foreshadowing seeds, transition clarity
- NOT structural: no reordering chapters, no new mythology, no major rewrites
- Verify each fix in the actual source file
- Document deferred fixes explicitly ("deferred to Reader Audit")
- Some fixes can be deferred to Reader Audit if verdict is uncertain

**Outputs:**
- Fixed chapter drafts
- `revisions/BOOK<N>_FIXES_APPLIED.md`
- Updated tracker: "Pass 3.5 COMPLETE — ready for Reader Audit"

**Verdict to proceed:** All Priority 1 fixes verified in source files.

---

## Stage 6: Line Edit (Pass 4)

**Purpose:** Prose-level cleanup: repetition, dialogue tags, throat-clearing, POV consistency.

**Scope:**
- Repetition tics (echo phrases, structural patterns)
- Dialogue tags → action beats where appropriate
- Throat-clearing ("I think about this," "I realise that")
- POV consistency
- Showing vs. telling
- Prose cadence (sentence length variation)

**NOT in scope:**
- Adding, removing, or reordering scenes
- Structural changes
- New exposition

**Key Rules:**
- Line Edit that changes scene structure is no longer a line edit — it becomes structural revision
- Document deferred structural issues, do not fix them here

**Outputs:**
- Line-edited chapter drafts
- `revisions/BOOK<N>_LINE_EDIT_REPORT.md`
- Updated tracker

---

## Stage 7: Copy Edit (Pass 5)

**Purpose:** Mechanical correctness only.

**Scope:**
- Spelling
- Punctuation
- Grammar
- Capitalisation (terminology, proper nouns)
- Style sheet consistency (British/Australian spelling)
- Timeline consistency
- Name/frequency verification

**NOT in scope:**
- Prose rhythm
- Stylistic improvements
- "This sentence feels flat" — defer to next revision

**Key Rules:**
- A clean manuscript after Line Edit should have 0–5 genuine mechanical issues
- If you find 20+ issues, your regex is too broad or you're in scope creep
- Do NOT change text just to feel productive

**Outputs:**
- Copy-edited chapter drafts
- `revisions/BOOK<N>_COPY_EDIT_REPORT.md`
- Updated tracker

---

## Stage 8: Assembly

**Purpose:** Compile individual chapters into a single manuscript file.

**Process:**
1. Concatenate chapters in order
2. Add front matter (title, word count, date)
3. Verify chapter boundaries
4. Check for formatting consistency

**Outputs:**
- `manuscript/BOOK<N>_COMPLETE.md`
- Or: `BOOK<N>_COMPLETE.md` at project root

**Key Rules:**
- When replacing a chapter in the compiled manuscript, use boundary extraction (before + new + after), not patch on a 5,000+ line file
- The compiled manuscript AND individual chapter drafts must both be maintained

---

## Stage 9: Final QA

**Purpose:** Structural verification, continuity check, freeze decision.

**Checklist:**
- [ ] All chapters present and in order
- [ ] Trailing whitespace cleaned
- [ ] Structural checks: act transitions, escalation arcs
- [ ] Emotional checks: payoff moments land
- [ ] Continuity checks: foreshadowing pays off, threads don't drop
- [ ] Character arc: complete and earned
- [ ] Sequel hooks: planted and functional
- [ ] No TK placeholders remain
- [ ] Word count matches tracker

**Verdict to proceed:** All checks pass. Declare manuscript frozen.

---

## Reader Audit (Between Stage 5 and 6, or after Stage 9)

**Purpose:** Fresh-eye experiential read by someone who has NOT read previous passes or editorial reports.

**When:** After Pass 3.5 (targeted fixes) or after full assembly. Best practice: after Pass 3.5, before Line Edit.

**Focus Questions:**
1. Does tension feel continuous?
2. Does the sacrifice / climax feel earned?
3. Does the antagonist remain coherent?
4. Does the sequel hook feel inevitable?
5. Does the climactic revelation land?

**Classification:**
The reader's "Must Address" findings are NOT automatically MUST FIX. The author/showrunner classifies:
- MUST FIX (implement now)
- INVESTIGATE FIRST (least invasive fix first)
- SHOULD FIX (individual judgment)
- COULD FIX (polish, defer)
- NOT A FIX (decline)

**Outputs:**
- `revisions/BOOK<N>_READER_AUDIT.md`
- Classification table with showrunner verdicts

---

## Freeze

**Purpose:** Lock the manuscript. No further changes.

**Actions:**
1. Final commit with "FROZEN" in message
2. Update series bible with Book N canon
3. Update character bible with arc completions
4. Update expansion strategy with next-book direction
5. Update handoff: "Book N frozen, Book N+1 architecture pending"
6. Tag the commit: `git tag book<N>-frozen`

**After freeze:** Begin Book N+1 architecture, OR pause the series.

---

## The Seven Non-Negotiable Rules

1. **The manuscript is the ground truth.** Trackers and reports are aspirational.
2. **Never trust a report that says "fixes applied."** Verify source files.
3. **Handoff before report.** Update state files before presenting summaries.
4. **Discovery before editorial.** Run pure inventory before any assessment.
5. **Copy edit is mechanical only.** No stylistic improvements in Stage 7.
6. **Autonomy triples velocity.** Grant tactical autonomy; intervene only for blockers.
7. **Every book teaches the pipeline.** Update this system after each production.
