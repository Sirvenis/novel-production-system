# Reader Audit Workflow: The Five Focus Questions

## When

After Developmental Structural Editorial (Stage 4) and its fixes (Stage 4.5), before Line Edit (Stage 6). The Reader Audit is a cold-eye validation pass that answers: "Does the story, as currently written, produce the intended experience?"

## Purpose

Reader Audit is NOT looking for new ideas. It validates whether the existing story achieves its emotional and structural goals.

Developmental Editorial asks: "Does the novel work as a whole?"
Reader Audit asks: "Does the novel produce the intended experience for a first-time reader?"

These are distinct questions. Neither duplicates the other.

## The Five Focus Questions

The Reader Audit should focus on five specific experiential questions, chosen to match the book's known risk areas:

1. **Does the tension feel continuous from beginning to end?**
   - Detects: mid-act drag, repetitive rhythm, escalation dips
   - Fix: vary structure, add stakes variation, remove redundant beats

2. **Does the key character's sacrifice/arc feel earned emotionally?**
   - Detects: absence in middle act, passive witness syndrome, insufficient active contribution
   - Fix: add one meaningful active moment before climax, deepen aftermath

3. **Does the antagonist remain a coherent, evolving threat throughout?**
   - Detects: over-adaptation (plot armor), under-explanation, inconsistent rules
   - Fix: bound adaptation to established mechanisms, clarify limitations

4. **Does the sequel hook feel like an inevitable next mystery rather than a teaser?**
   - Detects: too few touchpoints, abrupt appearance in final chapter, no structural work in present story
   - Fix: seed 3-4 meaningful references before the final chapter; make it shadow the present plot

5. **Does the climactic revelation land emotionally, or does the reader need more time with it?**
   - Detects: under-seeded breadcrumbs, tonal competition from adjacent scenes, insufficient processing time
   - Fix: add subtle foreshadowing throughout, create breathing room in the revelation scene

**Customization:** The five questions should be tailored per book. Book 3's questions targeted: tension continuity, Marco's sacrifice, Signal coherence, Simpson Desert inevitability, Maya's revelation weight. Book 4 might target: rotating backpacker integration, new entity mechanic clarity, series memory payoff, Pattern escalation logic, crew dynamic after member loss.

## Execution: Sub-Agent Dispatch Pattern

The Reader Audit is best performed by a cold-eye sub-agent with NO prior knowledge of the manuscript.

### Context for Sub-Agent

```
You are performing a Stage 5 Reader Audit for Book N of [Series].
You have NO prior knowledge of this manuscript — you are a cold-eye reader.
Read the full manuscript at [path].

Focus on these FIVE questions: [list]

Structure your report:
- EXECUTIVE VERDICT (PASS with grade, or FLAG for fixes)
- READER REACTION SUMMARY (understand? care? horror? humor? ending?)
- THE FIVE FOCUSED QUESTIONS (each with detailed answer)
- WHAT WORKED EXCEPTIONALLY WELL
- CONFUSION POINTS
- BOREDOM/DRAG POINTS
- CHARACTER ASSESSMENT
- HORROR EFFECTIVENESS (chapter-by-chapter)
- PACING ASSESSMENT
- DIALOGUE ASSESSMENT
- RECOMMENDATIONS (Must Address / Should Address / Could Address)

Be honest. If something doesn't work, say so. This is a validation audit.
```

### Report Format

The sub-agent should save its report to `revisions/BOOK<N>_READER_AUDIT.md`.

The report must NOT be cheerleading. A grade of B/B- with specific fixes is more valuable than an A with vague praise.

## User Classification of Findings

After receiving the Reader Audit, the user classifies findings:

| Classification | Action |
|----------------|--------|
| **MUST FIX** | Genuine structural issues. Implement immediately. |
| **INVESTIGATE FIRST** | Timing/compression concerns. Attempt least invasive fix first. Only escalate if problem survives. |
| **SHOULD FIX** | Real issues deserving individual judgment. Evaluate cost vs. benefit per issue. |
| **COULD FIX** | Polish. Address if time permits, or defer to Line Edit. |
| **NOT A FIX** | Preference/misread. Respectfully decline. |

**Example from Book 3 (validated):**
- MUST: Maya under-seeded, Dr. Thorne ambiguity, Simpson Desert abruptness
- INVESTIGATE FIRST: Ch 16 compression — solved with breathing room, not new chapter
- SHOULD: Plan→fail repetition, Marco passive middle act, Signal adaptation speed
- COULD: Raj rounding, possum payoff, toothbrush motif weight

## Post-Audit Decision Point

After fixes are applied (Stage 5.5):

**Option A:** Re-run Reader Audit to validate fixes (recommended if grade was B- or lower)
**Option B:** Proceed directly to Line Edit (Stage 6) if fixes were surgical and confidence is high

The user's standard: "If the Reader Audit comes back with only modest notes, we have evidence the pipeline has matured."

## Reference Data

**Book 3 Reader Audit (July 2026):**
- Sub-agent: cold-eye reader, kimi-k2.6:cloud
- Verdict: FLAG for fixes — Grade B/B-
- Must Address: 4 items (Maya breadcrumbs, Thorne name, Simpson Desert, Ch 16 compression)
- Should Address: 4 items (plan→fail, Marco active moment, Signal adaptation, exposition)
- Could Address: 4 items (Raj rounding, possum, toothbrush, Ch 17 as epilogue)
- Fixes applied in single session: +757 words (39,808 → 40,565)
- Commit: `ed1dbe8`
- User classification: all MUST implemented, INVESTIGATE FIRST solved without new chapter

*Validated: Book 3, 2026-07-16*
