# Assembly and Final QA Execution Pattern (Stages 8-9)

**When:** After Copy Edit (Stage 7) complete. This is the last gate before manuscript freeze.

**Purpose:** Stage 8: Verify the assembled manuscript is structurally intact — all chapters present, markers clean, formatting consistent. Stage 9: Run a structural checklist across the entire manuscript to confirm arcs, continuity, foreshadowing/payoff, and thematic coherence before declaring the book frozen.

**Model:** Autonomous execution under autonomy grant. Present summary + freeze decision. User can override; default is freeze if all checks pass.

---

## Stage 8: Assembly Verification

### Checks

| # | Check | Method | Pass Criteria |
|---|-------|--------|---------------|
| 1 | All chapters present | Count `# Chapter N:` headings in `BOOK<N>_COMPLETE.md` | Matches architecture (e.g., 17) |
| 2 | End markers present | Count `**[End Chapter` markers | Matches chapter count |
| 3 | No unexpected headings | grep for `# ` lines that are not chapter titles or structural | Zero unexpected |
| 4 | Double blank lines acceptable | Count `\n\n\n` sequences | < 20 (some are natural at section breaks) |
| 5 | Trailing whitespace cleaned | Count lines ending with ` ` | Zero |
| 6 | Chapter integrity | Parse each chapter's word count from assembled file | All within expected range, no zero-word chapters |
| 7 | Word count consistency | Total assembled vs sum of individual chapters | Match within ±10 words |

### Execution

1. **Re-assemble `BOOK<N>_COMPLETE.md`** by concatenating all `chapter-NN.md` files in order with double newline separator.
2. **Run the 7 checks** via Python script (see `execute_code` pattern).
3. **Fix any mechanical issues** (trailing whitespace, double blanks).
4. **Commit** with Assembly tag.

### Assembly commit format

```
Book N: Assembly (Stage 8) — <fixes>. 17 chapters verified intact.
```

Example:
```
Book 3: Assembly (Stage 8) — trailing whitespace cleaned, 17 chapters verified intact,
all structural/emotional/continuity checks pass. Manuscript ready for freeze.
```

---

## Stage 9: Final QA — Structural Checklist

Final QA is NOT a prose read-through. It is a verification pass against the series bible, character arcs, and thematic promises made by the architecture.

### Checklist

#### Series Continuity

| Check | Verify |
|-------|--------|
| Previous book references | Wet (Book 1), Root (Book 2), Old Bill memorialized |
| Count thresholds | Wet ≥ 5 refs, Root ≥ 5 refs, Old Bill ≥ 3 refs |
| Technology consistency | Mark devices, disruptors, frequency monitors behave as established |
| Location consistency | Innisfail, Port Douglas, Lizard Island, Simpson Desert names and geography match |

#### Character Arcs

| Character | Arc Check | Verification Method |
|-----------|-----------|---------------------|
| New POV character (backpacker) | Introduced in Ch 1-2, has distinct voice, expertise earns discovery | Read Ch 1-2 opening; grep for name + voice markers |
| Sacrifice character | Active contribution before death, death has weight, aftermath in next chapter | Read Ch 15 (sacrifice) + Ch 16 (aftermath) |
| Secret-keeper | Breadcrumbs seeded across 3+ chapters, revelation lands in designated chapter | grep for breadcrumb phrases; read revelation chapter |
| Protagonist | Chooses the line / commits to Pattern by end | Read final chapter; grep for "line", "choose", "chosen" |

#### Foreshadowing / Payoff

| Seed | Planted In | Pays Off In | Verify |
|------|-----------|-------------|--------|
| Simpson Desert | Ch 7 ("dry wrong"), Ch 9 (sensor reading) | Ch 17 (0.47 Hz confirmed) | grep "Simpson" across all chapters |
| Baltic Sea / Book 4 | Ch 17 (Toby, Germany) | Book 4 architecture | Read Ch 17 ending |
| Maya's secret | Ch 4, Ch 7, Ch 9 (breadcrumbs) | Ch 16 (revelation) | grep breadcrumb phrases + "Aris Thorne" |
| Technology arms race | Ch 5 (Mark IV fails), Ch 13 (Mark V teaches entity) | Ch 14-15 (consequences) | grep "Mark IV|Mark V|camouflage|adapt" |

#### Frequency Progression

| Frequency | Expected Mentions | Verify |
|-----------|------------------|--------|
| Previous book frequency | 2.1 Hz (Root) | grep `2\.1\s*Hz` |
| Current book base | 0.95 Hz (Signal) | grep `0\.95\s*Hz` |
| Post-disruptor shift | 0.94 Hz | grep `0\.94\s*Hz` |
| Next book seed | 0.47 Hz (Simpson) | grep `0\.47\s*Hz` |
| Notation | digit + space + Hz consistently | regex `\d+\.\d+\s*Hz` |

#### Emotional Arc Integrity

| Check | Verify |
|-------|--------|
| Sacrifice chapter carries weight | Not through grief-language count, but through action/decision density. Read the chapter: does the character's choice feel inevitable? |
| Aftermath chapter exists | Ch 16+ must process the death — not skip to next plot point |
| Revelation breathing room | After Maya's secret is revealed, Nate needs processing time before next action |
| Finale closure + setup | Ch 17 must: resolve current book's immediate threat AND seed next book's setting |

#### Thematic Consistency

| Theme | Verify |
|-------|--------|
| Understanding as protagonist | grep "understand|understanding" — should appear throughout, not just in climax |
| Technology arms race | Each Mark device teaches the entity — grep "learn|adapt|incorporated" |
| Cost per book | Permanent change, not just victory — check for character deaths, crew changes, knowledge states |
| Entity escalation | Each book uses different horror mechanic (Book 1: aggression, Book 2: infiltration, Book 3: seduction) |

#### Timeline Coherence

| Marker | Verify |
|--------|--------|
| "eight months" | Marco's reef tenure — consistent across Ch 1-2 |
| "six months" | Post-Book 2 gap — consistent across Ch 3-4 |
| "three days" | Post-revelation gap in Ch 17 — consistent with Ch 16 ending |
| "two weeks" | Simpson Desert sensor age — consistent with Ch 9 and Ch 17 |

---

### Final QA Execution

1. **Run the checklist** via `execute_code` with grep/regex across assembled manuscript.
2. **Flag any FAIL items.** If ≥1 check fails:
   - Determine if it's a quick fix (add a line, fix a number) or a structural issue.
   - Quick fix: apply, re-verify, proceed.
   - Structural issue: present to user with recommendation (fix now vs defer vs book not ready).
3. **Produce verification table** for handoff.
4. **Make freeze decision.** Default: FREEZE if all checks pass. User can override.

---

## Freeze Decision

**When all checks pass, declare:**

> **Book N: [Title] is FROZEN.**
>
> No further edits without explicit user approval. The manuscript has passed through the complete pipeline:
> 1. ✅ Architecture
> 2. ✅ Draft
> 3. ✅ Developmental Editorial
> 4. ✅ Structural Fixes
> 5. ✅ Reader Audit
> 6. ✅ Reader Audit Fixes (Stage 5.5)
> 7. ✅ Line Edit
> 8. ✅ Copy Edit
> 9. ✅ Assembly
> 10. ✅ Final QA
> 11. ✅ **FREEZE**

**Update tracking:**
- `handoff/MASTER-HANDOFF.md` — status = FROZEN
- `tracking/BOOK<N>_DASHBOARD.md` — pipeline stage = FROZEN
- Git commit with freeze tag

---

## Real Data (Book 3, Stages 8-9)

**Assembly commit:** `edeedfd`
**Tracking commit:** `fb06045`
**Word delta:** ±0 (40,571 unchanged)

### Assembly checks (all PASS)
- 17 chapters present: PASS
- 17 end markers: PASS
- No unexpected headings: PASS
- Double blank lines: 16 (acceptable)
- Trailing whitespace: CLEANED (2 lines)
- Chapter integrity: All parse correctly
- Word count: 40,571 (consistent)

### Final QA checks (all PASS)
- Series continuity: Wet (35x), Root (39x), Old Bill (19x)
- Character arcs: Marco (intro/sacrifice/aftermath), Maya (4 breadcrumbs + revelation), Nate (chooses the line)
- Foreshadowing: Simpson Desert (5x, 3x before Ch 17 payoff), Baltic Sea seed (Ch 17)
- Frequencies: 2.1 Hz (3x), 0.95 Hz (19x), 0.47 Hz (1x) — consistent notation
- Timeline: Eight months (4x), six months (9x), three days (6x), two weeks (6x) — coherent
- Emotional integrity: Ch 15 weight through action/decision, Ch 16 aftermath present
- Thematic: Mark devices (63x), entity learns/adapts, understanding as protagonist (23x)

**Freeze declared:** 2026-07-16

---

*Reference: created 2026-07-16 during Book 3 Assembly + Final QA (Stages 8-9).*
