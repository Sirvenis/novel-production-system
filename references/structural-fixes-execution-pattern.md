# Structural Fixes Execution Pattern

## When

After a Developmental Structural Editorial report has identified specific fixes and the user has approved which to implement immediately (vs. which to defer).

## Context

This pattern was validated on Book 3 (The Signal), Stage 4. The user approved Fixes 1-3 for immediate implementation and deferred Fix 4 pending Reader Audit evidence. The entire fix cycle — implementation, assembly update, tracking update, commit — happened in the same session as the editorial report.

## Execution Steps

### 1. User Approves Fix Selection

The user may approve all fixes, reject some, or defer some. Record the decision explicitly:

| Fix | Priority | User Verdict |
|-----|----------|--------------|
| Fix 1 (frequency thread gap) | Mandatory | ✅ Implement now |
| Fix 2 (foreshadowing seed) | Mandatory | ✅ Implement now |
| Fix 3 (transition clarity) | Recommended | ✅ Implement now |
| Fix 4 (revelation weight) | Optional | ⏸️ Defer to Reader Audit |

### 2. Implement Each Fix Immediately

**Do not end the session after the editorial report.** The fixes are small (30–150 words each). Implement them now while the context is hot.

**Technique per fix:**
- Open the target chapter file with `read_file`
- Use `patch` (replace mode) for the specific line
- If `patch` fails due to non-unique matches, fall back to `write_file` for the whole chapter (the file is small)
- Verify with `read_file` tail check

### 3. Update the Compiled Manuscript

The compiled manuscript (`BOOK<N>_COMPLETE.md`) must also receive the fixes. Use Python raw-text replacement (not `patch` on the 5,000+ line file):

```python
with open('BOOK<N>_COMPLETE.md', 'r') as f:
    text = f.read()

# Apply each fix as a string replacement
text = text.replace(old_string, new_string)

with open('BOOK<N>_COMPLETE.md', 'w') as f:
    f.write(text)
```

**Verify all three fixes landed:** `grep` for each new string.

### 4. Update Tracking and Handoff

Before presenting the session report:
- `tracking/BOOK<N>_DASHBOARD.md` — update word count, mark structural fixes complete
- `handoff/MASTER-HANDOFF.md` — update status, note which fixes applied, which deferred

### 5. Commit

Single commit for all fixes + tracking updates:

```bash
git add book<N>-drafts/chapter-*.md BOOK<N>_COMPLETE.md tracking/ handoff/
git commit -m "Book N: Structural Fixes (Stage 4) — Fix 1 (desc), Fix 2 (desc), Fix 3 (desc); +Xw

Fix 4 deferred pending Reader Audit."
```

### 6. Present Report

Only after handoff and tracking are updated present the session summary to the user. The summary should include:
- Fixes applied (with line changes)
- Fixes deferred (with trigger condition)
- Pipeline status update
- Next stage ready flag

## The "Defer to Reader Audit" Pattern

Not all fixes need immediate application. When a fix is optional and its value depends on reader reception, defer it. This keeps the pipeline evidence-led:

- **Implement now:** Structural gaps, continuity errors, dropped threads, unclear transitions
- **Defer:** Emotional weight questions, scene-length concerns, character-reaction sufficiency

**Trigger condition for deferred fix:** "If Reader Audit flags [specific issue], then apply [specific fix]. Otherwise, leave as-is."

**Example from Book 3:**
- Fix 4 (Ch 16 Maya revelation weight): "Monitor during Reader Audit. If readers feel emotionally short-changed, add a 500-800 word private Nate/Maya processing scene."

This prevents over-engineering before reader evidence exists.

## Reader Audit Fix Cycle (Stage 5.5) — NEW

A Reader Audit may identify issues that are distinct from Developmental Editorial findings:

| Issue Type | Developmental Editorial | Reader Audit |
|-----------|------------------------|--------------|
| **Scope** | Architecture, structure, thread continuity | Experience, emotional payoff, pacing rhythm |
| **Granularity** | Chapter-level, plot-level | Scene-level, sentence-level feeling |
| **Question asked** | "Does this work as a whole?" | "Did this produce the intended experience?" |
| **Typical findings** | Dropped threads, unclear transitions, scope creep | Repetitive rhythm, under-seeded reveals, character absence, adaptation-credibility |

### User Prioritization Framework (Book 3 validated)

When the Reader Audit returns findings, the user may classify them as:

**MUST FIX** — Genuine structural improvements (under-seeded revelation, confusing name ambiguity, insufficient foreshadowing). Implement immediately.

**INVESTIGATE FIRST** — Compression/timing concerns where a lighter solution may suffice. Attempt the least invasive fix first (e.g., add breathing room within existing chapter before creating a new chapter). Only escalate to structural change if the problem survives.

**SHOULD FIX** — Real issues deserving individual judgment. Evaluate each: does it affect reader experience enough to justify the cost of the fix?

**COULD FIX** — Polish and refinement. Address only if time/capacity permits, or defer to Line Edit.

**NOT A FIX** — Reader audit calls that are actually preferences or misreads (e.g., "I wanted more romance" when the book isn't a romance). Respectfully decline.

### Execution Steps for Reader Audit Fixes

Same as Developmental Editorial fixes, with one addition:

1. **User classifies findings** (MUST / INVESTIGATE / SHOULD / COULD / NOT)
2. **Implement MUST fixes immediately**
3. **Investigate INVESTIGATE-FIRST findings with least invasive solution**
4. **Evaluate SHOULD fixes case by case**
5. **Update assembled manuscript**
6. **Commit with "Stage 5.5" designation**
7. **Decision point:** Re-run Reader Audit OR proceed to Line Edit

**Example from Book 3, Stage 5.5:**
- MUST: Seed Maya's revelation with 4 breadcrumbs, clarify Dr. Thorne name, strengthen Simpson Desert thread
- INVESTIGATE FIRST: Ch 16 compression — added breathing room within existing chapter (Nate's reflection beat). New chapter NOT needed.
- SHOULD: Vary plan→fail cycle, give Marco active moment, bound Signal adaptation
- All applied in single session. Manuscript: 39,808w → 40,565w. Commit: `ed1dbe8`.

## Common Pitfalls

- **Ending the session after the report:** The user said "proceed with Stage 4 immediately." That means implement fixes NOW, not in a future session.
- **Forgetting compiled manuscript:** Source chapters are updated but `BOOK<N>_COMPLETE.md` is not. Future sessions may edit from either source.
- **Not verifying fix landed:** Trusting the replacement without spot-checking. Always `grep` for the new string.
- **Updating handoff AFTER presenting report:** The user's instruction is "update handoffs before presenting report." Sequence matters.

## Reference Data

**Book 3, Stage 4 (July 2026):**
- Fix 1: Ch 11 frequency spike (+23 words) — Raj's monitor shows 0.95 Hz spike as Marco disappears
- Fix 2: Ch 7 Simpson seed (+39 words) — Dr. Thorne mentions Old Bill's "dry wrong" theory
- Fix 3: Ch 17 decision clarity (+50 words) — Nate's "Three days since I decided to stay" reflection
- Total assembly gain: +112 words
- Time: ~15 minutes from user approval to commit

*Validated: Book 3, 2026-07-15*
