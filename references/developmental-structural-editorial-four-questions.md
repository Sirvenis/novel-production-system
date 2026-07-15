# Developmental Structural Editorial — The Four Questions Method

**Use case:** After Tier 1 expansion (or any major draft revision), before proceeding to targeted fixes. This method was validated on Book 3 (The Signal) and confirmed by user as the correct way to assess whether a manuscript is ready for the next pipeline stage.

**When NOT to use:** Do not run this before a Discovery Pass. The Discovery Pass inventories actual state; this editorial asks interpretive questions about that state.

---

## The Four Questions (User-Validated)

These four questions target the four dimensions that determine whether a manuscript has moved from "compressed" to "breathing":

### Q1: Does tension continually escalate from opening to closing?

**What to check:**
- Stakes trajectory per chapter (local → team → physical → conceptual → emotional → global)
- Identify "dip" chapters that pause for information, planning, or character
- Verify each dip earns its place (does it serve a function the climax needs?)
- Check that the two longest chapters are the climax pair (emotional + physical)

**Tooling:** Read chapter summaries, plot stakes per chapter in a table. Flag chapters where stakes do not rise from previous chapter.

**Acceptable finding:** Yes, with necessary breathing-room dips. Each dip serves the climax (Raj's analysis in Ch 6 → Ch 9's revelation; tourist subplot in Ch 8 → shows individual threat; planning in Ch 10-12 → makes Ch 13-15 desperate).

**Unacceptable finding:** Flat middle, or climax chapters shorter than setup chapters.

---

### Q2: Does the key character arc feel inevitable rather than abrupt?

**What to check:**
- Trace the character's state through every chapter they appear in
- Count references to their defining condition (compulsion, grief, resolve, etc.)
- Verify the pre-climax chapters show progressive degradation/change
- Check that the expanded chapters (if any) contribute to this progression

**Example from Book 3 (Marco):**
- Ch 1: Observer (35 wrongness refs)
- Ch 2: Recruiter (pattern recognition)
- Ch 4: Participant (physical ownership)
- Ch 5: First victim (11 compulsion refs — EXPANDED)
- Ch 11: Fully compromised (15 compulsion refs — midnight disappearance)
- Ch 14: Excluded (6 refs — accepts fate)
- Ch 15: Sacrifice (64 refs — poisoned blood, death)

**Critical technique:** The expanded chapter (Ch 5) was essential. Before expansion, the compulsion was summary-level. After expansion, readers experienced the drift, the glassy eyes, the physical struggle. This made Ch 11 inevitable.

**Gap to watch:** Passive states between active moments. If a character is "recovering" for multiple chapters, give them one active-failure beat so their passivity feels like struggle, not absence.

---

### Q3: Does the central entity/mechanism become progressively more understandable without losing mystery?

**What to check:**
- Map "understanding layers" — what does the reader learn in each chapter?
- Track frequency/entity mentions per chapter (grep count)
- Verify the signal thread does not drop out during personal-crisis chapters
- Check that the final understanding is satisfying but leaves room for sequel

**Understanding layer template (Book 3):**
| Layer | Chapter | What Reader Learns | Mystery Preserved |
|-------|---------|--------------------|-------------------|
| Beauty trap | Ch 1 | Patches are "wrong" | What ARE they? |
| Pattern connection | Ch 2 | 0.95 Hz detected | Why this frequency? |
| Confirmed signal | Ch 3 | Mark IV detects | What does it want? |
| Compulsion mechanism | Ch 5 | Physical welcome | Why does it feel like home? |
| Biological mechanism | Ch 7 | Filter-feeder network | Where is the core? |
| Intelligence | Ch 9 | Distributed brain | How does it think? |
| Human effect | Ch 11 | Claims people | What happens to the emptied? |
| Adaptation | Ch 13-14 | Incorporates tech, goes pelagic | Can it be stopped? |
| Consumption | Ch 15 | Processes human DNA | Did sacrifice work? |
| Pattern context | Ch 17 | Part of global network | What is the full Pattern? |

**Critical gap discovered in Book 3:** Ch 11 (Marco's disappearance) had **ZERO frequency mentions.** The signal thread dropped out during the most personal crisis. Fix: add Raj's monitor showing a spike as Marco goes under.

**Detection method:** Run `grep -ic "0\.9\|Hz\|frequency\|signal" chapter-*.md` across all chapters. Look for chapters with 0 refs that should have some.

---

### Q4: Does the ending create anticipation for the sequel thread rather than simply introducing it?

**What to check:**
- Count foreshadowing mentions of the sequel element BEFORE the ending chapter
- Verify at least 2-3 seeds exist in earlier chapters (even if subtle)
- Check that the sequel element connects to existing canon (Old Bill's notes, Dr. Chen's move, etc.)
- Ensure the final line is a pivot, not just a statement

**Example from Book 3:**
- **Strength:** Baltic Sea contact creates global scope BEFORE Simpson Desert appears. Old Bill's "dry wrong" notes give canonical weight. Dr. Chen's move to Alice Springs provides geographic setup.
- **Weakness:** Zero "Simpson/desert/0.47" mentions in Chapters 3-15. The desert is introduced as a twist, not earned as confirmation.
- **Fix:** Add 1-2 subtle seeds in Ch 7 or Ch 9 — Dr. Thorne mentioning "other environments" or "lower frequencies."

**Rule of thumb:** If a sequel element appears ONLY in the final chapter, it needs 2-3 seeds in the middle. If it appears with seeds, it needs 1-2 seeds in the opening.

---

## Thread-Continuity Gap Detection (Technical Method)

A common structural flaw: an important thread (frequency, character condition, thematic element) drops out during chapters where it should be present.

**Detection:**
```bash
# Count mentions of key term per chapter
for ch in chapter-*.md; do
    num=$(echo "$ch" | sed 's/chapter-//' | sed 's/.md//')
    hits=$(grep -ic "TERM" "$ch")
    echo "Ch $num: $hits refs"
done
```

**Interpretation:**
- Zero refs in a chapter ABOUT that topic = gap
- High refs in setup chapters, zero in crisis chapters = thread drop
- Sudden spike in a chapter = possible overcorrection

**Fix pattern:** Add 2-3 references, not a full explanation. A line of dialogue, a monitor reading, a character noticing the absence.

---

## Escalation Dip Assessment

Not all flat or lower-stakes chapters are problems. Use this framework:

| Dip Type | Function | Example | Verdict |
|----------|----------|---------|---------|
| Information delivery | Sets up later understanding | Raj's frequency analysis | Keep |
| Character pause | Shows threat beyond crew | Tourist subplot | Keep |
| Strategic planning | Makes later desperation earned | Fish blood plan | Keep |
| Emotional aftermath | Processes cost | Ch 16 (if expanded) | Keep |
| Repetitive setup | Same beat as previous chapter | — | Cut/merge |
| Unconnected subplot | Does not serve climax or character | — | Cut |

**If a dip chapter does not serve the climax, it is a problem.**

---

## Verdict Framework

The editorial must end with one of three verdicts:

| Verdict | Meaning | Next Action |
|---------|---------|-------------|
| **PROCEED** | Four questions answered positively. Minor fixes only. | Stage 4: Structural Fixes (targeted) → Reader Audit |
| **PROCEED WITH FIXES** | Three questions positive, one needs work. Specific fixes identified. | Apply fixes → verify → Reader Audit |
| **NOT READY** | Two or more questions negative. Structural problems remain. | Return to expansion or rewrite before editorial |

**Book 3 result:** PROCEED WITH FIXES. Four specific fixes identified (frequency gap, foreshadowing seeds, transition clarity, optional revelation weight).

---

## Reporting Format

Write the report as `revisions/BOOK<N>_DEVELOPMENTAL_REPORT.md` with:

1. Executive summary (verdict)
2. Question-by-question analysis (with data)
3. Additional structural findings (continuity, pacing, voice)
4. Recommended fixes table (priority, file, effort)
5. Pipeline status update

**Commit the report before applying fixes.** The report is the audit trail.

---

## Post-Report Fix Execution

After the report is committed, the user will select which fixes to implement immediately and which to defer. **Implement approved fixes in the same session** — do not end the session after the report.

| Category | Implement Now? | Examples |
|----------|---------------|----------|
| Dropped thread / continuity gap | ✅ Yes | Frequency mentions missing, transition unclear |
| Foreshadowing seed missing | ✅ Yes | Sequel element introduced without earlier seed |
| Emotional weight insufficient | ⏸️ Defer | Revelation needs more processing time — wait for Reader Audit |

See `references/structural-fixes-execution-pattern.md` for the full workflow: reading target chapters, applying patches, updating assembly, verifying with `grep`, updating tracking, committing, and presenting the final report.

**Sequence:** (1) user selects fixes → (2) implement each fix in source chapter → (3) update compiled manuscript → (4) update tracking + handoff → (5) commit → (6) present summary.

*Validated: Book 3, 2026-07-15*

---

*Method validated: Book 3, 2026-07-15*
*User assessment: "The manuscript has crossed the threshold from 'structurally complete but emotionally compressed' to 'structurally complete and emotionally breathing.'"*
