# Editorial Stages — Detailed Execution Guide

## Stage 1: Architecture

### What It Is
The blueprint. Before any prose, every chapter has a Job Statement, a word range, and declared beats.

### Inputs
- Series bible (if applicable)
- Concept brief
- Author's intent

### Process
1. Write the concept brief (1 page: premise, tone, central fear, protagonist)
2. Define the series promise (what the reader is guaranteed)
3. Break down chapters 1–N:
   - Chapter number and title
   - Job Statement: "This chapter exists to make the reader believe [X]"
   - Word range (job-based, not fixed)
   - Key beats (3–5 bullet points)
   - Characters present
   - Emotional register
   - Sequel hook (if applicable)
4. Character positions: where is everyone at the start and end?
5. Thematic through-lines: what ideas recur?

### Outputs
- `BOOK<N>_ARCHITECTURE.md`
- `tracking/BOOK<N>_TRACKER.md` (blank, with status PENDING for all chapters)

### Verdict
APPROVED / NEEDS REVISION. No prose until approved.

### Common Pitfalls
- **Architecture conflation:** Combining multiple chapters' worth of story into one chapter mandate. This collapses pacing.
- **Title mismatch:** A chapter title like "The Crew Assembles" signals content the architecture doesn't mandate until later.
- **Fixed word targets:** "~4,000 words per chapter" creates pressure to pad or rush. Use job-based ranges.

---

## Stage 2: Drafting

### What It Is
First-pass prose. The goal is completion, not perfection.

### Inputs
- Architecture document
- Tracker
- Handoff with current state

### Process
1. Write the Job Statement at the top of each chapter draft
2. Draft the chapter
3. Self-edit for obvious contradictions and missing beats
4. Commit
5. Update tracker

### Outputs
- `drafts/chapter-NN.md`
- Git commits
- Updated tracker

### Verdict
COMPLETE when all chapters are drafted.

### Common Pitfalls
- **Drafting without pipeline confirmation:** If you haven't confirmed pipeline approach, chapters are "guilty until proven innocent."
- **Compressing chapters:** When a draft exceeds its mandate, stop and split rather than compressing.
- **Procedural verbosity under autonomy:** If autonomy is granted, silent execution. Announce blockers only.

---

## Stage 3: Expansion

### What It Is
Identifying and fixing lean chapters.

### Inputs
- Complete draft set
- Architecture document

### Process
1. **Discovery Pass:** Pure inventory
   - Extract actual word counts per chapter
   - Compare to architecture mandates
   - List contradictions with series bible
   - List TK placeholders
   - Classify: Adequate / Lean / Underweight
2. **Tier-Based Expansion:**
   - Tier 1: Core revelation, major action, emotional climax
   - Tier 2: Lean but job-present
   - Tier 3: Transitions, secondary action
3. **Expansion execution:**
   - Read the lean chapter
   - Identify specific targets (sensory depth, emotional beats, transitions)
   - Weave new material into existing scenes
   - Do NOT append — integrate

### Outputs
- Expanded drafts
- `tracking/BOOK<N>_DISCOVERY_PASS.md`
- Updated tracker

### Verdict
Tier 1 complete. Tier 2/3 optional based on time and capacity.

### Common Pitfalls
- **Using `wc` for word counts:** `wc -w` caches stale output after `write_file`. Use line-range extraction or `read_file` tail checks.
- **Expanding by appending:** Appended material disrupts pacing. Weave inline.
- **Expanding thin chapters that don't need it:** A chapter at 75% of target is not automatically underweight if its beats are fully delivered.

---

## Stage 4: Developmental Editorial

### What It Is
Structural assessment. Does the story work? Not: is the prose good?

### Inputs
- Expanded draft set
- Discovery Pass report
- Series bible

### Process
1. Sample chapters across the manuscript (opening, middle, climax, finale)
2. Run the Four Questions:
   - Q1: Does tension continually escalate from opening to closing?
   - Q2: Does the key character arc feel inevitable rather than abrupt?
   - Q3: Does the central mechanism become progressively more understandable without losing mystery?
   - Q4: Does the ending create anticipation for the sequel thread rather than simply introducing it?
3. Check thread continuity (frequency mentions, character conditions, thematic elements)
4. Check cadence fatigue (do consecutive chapters end the same way?)
5. Check escalation dip (any mid-book sag?)

### Outputs
- `revisions/BOOK<N>_EDITORIAL_REPORT.md`
- Verdict: READY / NEEDS TARGETED FIXES / NEEDS MAJOR REWRITE

### Verdict
READY or NEEDS TARGETED FIXES. Major rewrite returns to architecture.

### Common Pitfalls
- **Editorial missing architecture alignment:** The editor must check whether each chapter delivers ONLY its mandated job, or whether it steals beats from later chapters.
- **Grading prose during developmental:** This is not a prose review. It's a story review.
- **Over-generous verdict:** "It's fine" when there are clear structural gaps. The editor must be ruthless.

---

## Stage 5: Targeted Fixes (Pass 3.5)

### What It Is
Applying ONLY Priority 1 blockers from the editorial report.

### Inputs
- Editorial report
- Draft set

### Process
1. Select ONLY Priority 1 blockers
2. For each: determine the least invasive fix
3. Apply fix inline (patch or rewrite the specific section)
4. Verify in source file
5. Document: fix applied, deferred, or rejected
6. Update tracker

### Outputs
- Fixed drafts
- `revisions/BOOK<N>_FIXES_APPLIED.md`
- Updated tracker

### Verdict
All Priority 1 fixes verified.

### Common Pitfalls
- **Fixing Priority 2/3 during Pass 3.5:** Priority 2/3 are for Reader Audit or next revision, not now.
- **Structural fix masquerading as surgical:** If a fix requires reordering chapters or adding new mythology, it's not surgical.
- **Not verifying in source:** Always check the actual file after claiming a fix is applied.

---

## Stage 6: Line Edit

### What It Is
Prose-level cleanup: repetition, dialogue tags, throat-clearing, POV.

### Inputs
- Fixed drafts (after Pass 3.5)
- Editorial report (for context, not for new fixes)

### Process
1. Pattern audit across all chapters:
   - Repetition tics (echo phrases, structural patterns)
   - Dialogue tags → action beats
   - Throat-clearing phrases
   - POV consistency
   - Showing vs. telling
2. Phased fix execution:
   - Phase 1: Repetition (most visible)
   - Phase 2: Dialogue tags
   - Phase 3: Throat-clearing
   - Phase 4: POV and showing
3. Re-assemble after each phase
4. Commit each phase separately

### Outputs
- Line-edited drafts
- `revisions/BOOK<N>_LINE_EDIT_REPORT.md`

### Verdict
Complete when all phases pass.

### Common Pitfalls
- **Line Edit scope creep into structural revision:** If a fix requires adding, removing, or reordering scenes, it is outside Stage 6 scope.
- **Changing sentence rhythm during Line Edit:** Line Edit can tighten but should not fundamentally alter voice rhythm.

---

## Stage 7: Copy Edit

### What It Is
Mechanical correctness only.

### Inputs
- Line-edited drafts
- Style sheet (British/Australian spelling, terminology capitalisation)

### Process
1. Systematic scan:
   - Spelling ( British: centre, colour, organisation)
   - Punctuation (em-dashes, quotation marks, apostrophes)
   - Grammar
   - Capitalisation of series terms (Pattern, Signal, Wet, Root)
   - Name consistency
   - Frequency / technical terms
   - Timeline consistency
2. Verification table: each check, result, chapter

### Outputs
- Copy-edited drafts
- `revisions/BOOK<N>_COPY_EDIT_REPORT.md`

### Verdict
0–5 genuine issues found. If 20+, re-run with tighter filters.

### Common Pitfalls
- **Copy Edit inventing issues:** A clean manuscript should have very few mechanical issues. Do not change text just to feel productive.
- **Stylistic improvements during Copy Edit:** The user's directive is explicit: resist the temptation to make stylistic improvements. Copy edit = correctness, not creativity.

---

## Stage 8: Assembly

### What It Is
Compiling individual chapters into a single manuscript.

### Inputs
- Copy-edited chapter drafts

### Process
1. Determine order and boundaries
2. Extract each chapter (line-range, not inline markers)
3. Concatenate with front matter
4. Verify chapter count and order
5. Clean trailing whitespace

### Outputs
- `manuscript/BOOK<N>_COMPLETE.md` or `BOOK<N>_COMPLETE.md`

### Verdict
All chapters present, in order, clean.

### Common Pitfalls
- **Patching the middle of a large file:** A compiled manuscript can be 5,000+ lines. Do not patch the middle. Use boundary extraction.
- **Forgetting individual drafts:** Maintain both the compiled manuscript AND individual chapter drafts.

---

## Stage 9: Final QA

### What It Is
The last check before freeze.

### Inputs
- Compiled manuscript
- Series bible
- Tracker

### Checklist
- [ ] Structural: act transitions, escalation arcs
- [ ] Emotional: payoff moments land
- [ ] Continuity: foreshadowing pays off, threads don't drop
- [ ] Character: arcs complete and earned
- [ ] Sequel hooks: planted and functional
- [ ] Technical: no TK placeholders, no trailing whitespace
- [ ] Word count: matches tracker
- [ ] Formatting: consistent

### Outputs
- `tracking/BOOK<N>_DASHBOARD.md` updated
- Final handoff: "Book N frozen"

### Verdict
All checks pass. Declare FROZEN.

### Common Pitfalls
- **Skipping QA because "it already passed editorial":** Editorial assesses story. QA assesses completeness. They are complementary.

---

## Reader Audit (Interleaved Stage)

### What It Is
Fresh-eye experiential read. NOT an editorial read.

### When
After Pass 3.5 (targeted fixes), before Line Edit. OR after full assembly.

### Who
A reader who has NOT read previous passes or editorial reports.

### Process
1. Read the manuscript cold
2. Answer the Five Focus Questions (see `references/READER_AUDIT_FIVE_QUESTIONS.md`)
3. Classify findings by severity
4. Present classification table to showrunner/author
5. Showrunner classifies: MUST FIX / INVESTIGATE FIRST / SHOULD FIX / COULD FIX / NOT A FIX

### Outputs
- `revisions/BOOK<N>_READER_AUDIT.md`
- Classification table with showrunner verdicts

### Common Pitfalls
- **Treating all "Must Address" as MUST FIX:** The reader identifies issues; the author decides priority.
- **Reader doing editorial work:** The reader should report experience, not prescribe fixes.
