# Pass 3 Editorial Review — Pattern and Report Template

## When to Use

After Pass 2 (expansion) is complete, before any Reader Audit (Pass 4). This is the structural gate: does the manuscript hold together across the full arc?

## Workflow

### 1. Sample Strategy

Do NOT read every chapter. Read a representative sample that covers:
- **Opening:** Ch 1 (voice calibration) + Ch 2-3 (early beats)
- **Bridge/Setup:** The chapter that introduces the core mechanic (e.g., Ch 5 for frequency analysis)
- **Midpoint escalation:** The chapter that escalates stakes (e.g., Ch 9 for carriers, Ch 10 for spore cloud)
- **Climax machinery:** The planning chapter (Ch 12) + the climax chapter (Ch 14)
- **Finale:** The last 2 chapters (Ch 16-17) for payoff, seeding, and cadence
- **Any lean chapter** flagged from Pass 2

### 2. What to Evaluate

| Dimension | How to Check |
|-----------|-------------|
| **Continuity** | Follow motifs across chapters: toothbrush, boots, frequency, swollen hands, maps. Does each thread have setup, development, and payoff? |
| **Architecture alignment** | Does each chapter deliver ONLY its mandate? Check for scope creep (beats stolen from later chapters). |
| **Cadence fatigue** | Read the last 5 lines of the final 3-4 chapters. Same structural pattern? Flag it. |
| **Dropped threads** | Search for setups that lack payoffs: green switch, blog references, character disappearances, dog behaviors. |
| **Word count reality** | Compare actual vs target. Are chapters underweight AND thin, or underweight but complete? |
| **Prose cadence** | Look for repeated sentence openers, dialogue attribution patterns, poetic-ending overuse. |
| **Emotional arc** | Does the relationship between protagonist and key characters evolve across the manuscript? |

### 3. Report Structure

Write `BOOK<N>_EDITORIAL_REPORT.md` in `revisions/`:

```markdown
# BOOK<N> EDITORIAL REPORT
## Pass 3 — Structural, Continuity, and Cadence Review

## EXECUTIVE VERDICT
Status: [READY FOR READER AUDIT / NEEDS TARGETED FIXES / NEEDS MAJOR REWRITE]

## PRIORITY 1: BLOCKERS
### 1. [Chapter X: Issue title]
Location: `book<N>-drafts/chapter-XX.md`
Issue: [What and why]
What to add/fix: [Specific direction]

## PRIORITY 2: SIGNIFICANT CONCERNS
[Same format, less critical]

## PRIORITY 3: NICE-TO-HAVES
[Polish items]

## CONTINUITY AUDIT: PASSED / FAILED
Table: Element | Status | Notes

## STRUCTURAL ASSESSMENT
Table: Act | Chapters | Assessment

## PROSE CADENCE ASSESSMENT
Strengths + Concerns

## WORD COUNT ANALYSIS
Table: Chapter | Actual | Target | Delta
Note: Do NOT force chapters to arbitrary targets. Expand only if thematically underweight.

## RECOMMENDED REVISION PLAN
Phase A: Blockers
Phase B: Significant
Phase C: Polish

## FINAL ASSESSMENT
Release-readiness: [NOT YET / READY]
Confidence after fixes: [LOW / MEDIUM / HIGH]
Estimated fix time: [N sessions]
Risk level: [LOW / MEDIUM / HIGH]
```

### 4. Verdict Rules

- **READY FOR READER AUDIT:** No Priority 1 blockers. Minor concerns acceptable.
- **NEEDS TARGETED FIXES:** Has 1-4 Priority 1 blockers. Fixable in one session. Proceed to Pass 3.5.
- **NEEDS MAJOR REWRITE:** Structural problems (acts broken, scope creep, continuity collapse). Requires re-architecture.

### 5. Handoff File

Write `book<N>-editorial-handoff.md` in `handoff/` with:
- What was read and what was found
- Priority queue (must/should/could do)
- Continuity locks to preserve during fixes
- Next steps (Pass 3.5 or Pass 4)

## Verification Rule

**Never trust a report that says "fixes applied." Always spot-check the actual source files.**

After Pass 3.5 fixes:
1. `read_file` tail-check each fixed chapter
2. `git diff --stat` to confirm changes are in the commit
3. Update tracker
4. Commit
5. Write session handoff

## Real-World Example

**Book 2, Pass 3 (this session):**
- Read 9 chapters across full manuscript
- Verdict: NEEDS TARGETED FIXES (2 blockers: Ch 2, Ch 17 underweight; 4 significant concerns; 5 polish items)
- Applied in Pass 3.5: Ch 2 expanded (+1,063 words), Ch 17 expanded (+1,115 words), cadence variation in 2 endings, green switch resolved, Margaret reaction added
- Tracker updated from 64,390 → ~66,830 words
- Status: READY FOR READER AUDIT
