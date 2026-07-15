# Copy Edit Execution Pattern (Stage 7)

**When:** After Line Edit (Stage 6) complete and approved. Before Assembly (Stage 8).

**Purpose:** Mechanical correctness only. Spelling, punctuation, grammar, capitalization, italics/quotes, character names, timeline, numerical formats, terminology continuity. **This is NOT a line edit.** Do not touch rhythm, repetition, dialogue style, or showing-vs-telling. Do not make prose "better." Make it correct.

**Model:** Autonomous execution under autonomy grant. The user should NOT be asked to review individual mechanical changes.

---

## Scope Boundary (Critical)

Copy Edit is most effective when it stays focused on correctness rather than creativity. The user's directive: **"Resist the temptation to make stylistic improvements during the copy edit."**

| IN SCOPE | OUT OF SCOPE |
|----------|--------------|
| Spelling (British/Australian consistency) | Sentence rhythm |
| Punctuation (commas, apostrophes, quotes) | Repetition trimming |
| Grammar (its/it's, subject-verb, tense) | Dialogue tightening |
| Capitalization (entity names, proper nouns) | POV slip fixes |
| Italics and quotation consistency | Showing-vs-telling |
| Character name consistency | Exposition interleaving |
| Timeline coherence | Scene restructuring |
| Numerical format consistency | Word count changes |
| Terminology continuity (frequencies, Mark devices, scientific terms) | Emotional beat changes |

**If you find an issue outside scope:** Flag it in notes, do NOT fix it. It belongs in Line Edit (already past) or as a user decision for next revision.

---

## Pre-Execution: Systematic Scan

Run a targeted scan across all chapter source files before fixing anything. This prevents over-correction and identifies genuine issues amid false positives.

### Category 1: British/Australian Spelling

Search for Americanisms in narrative text (not inside dialogue — characters may speak American).

| American | British | Notes |
|----------|---------|-------|
| center | centre | Always check |
| color | colour | |
| organize | organise | |
| realize | realise | |
| recognize | recognise | |
| analyze | analyse | |
| behavior | behaviour | |
| traveling | travelling | |
| canceled | cancelled | |
| program | programme | Skip if "computer program" |
| tumor | tumour | |
| armor | armour | |
| flavor | flavour | |
| favor | favour | |
| harbor | harbour | |
| labor | labour | |
| neighbor | neighbour | |
| savior | saviour | |
| meter (unit) | metre | "meters" (plural) is American; "metre" is unit |
| synchronize | synchronise | |
| specialize | specialise | |
| civilize | civilise | |
| vaporize | vaporise | |

**Script pattern:** `search_files` with regex `\bamerican_word\b`, then verify each hit is in narrative (not inside quotes) before fixing.

### Category 2: Entity Capitalization

Entities (The Wet, The Root, The Signal, The Pattern) must be capitalized consistently in narrative.

- First mention in a book: "The Wet" (capital T)
- Subsequent narrative mentions: "the Wet" (lowercase t, capital W) — this is acceptable
- **Check for:** "the wet" (lowercase w), "the root" (lowercase r) in narrative — these are errors
- Inside dialogue: characters may say "the wet" informally — do not change dialogue

**Exception:** Chapter titles and end markers (`# Chapter 3: The Signal`, `**[End Chapter 17 — The Pattern]**`) are structural, not narrative. They don't need fixing.

### Category 3: Character Names

| Name | Canonical Form | Variants to Flag |
|------|---------------|------------------|
| Living marine biologist | Dr. Thorne | Must be "Dr. Thorne" or "Theodore Thorne" |
| Maya's converted mentor | Dr. Aris Thorne | Must include "Aris" to disambiguate |
| Tourist victim | Mrs. Brennan | Was "Mrs. Henderson" in early drafts — verify cleaned |
| Student in Germany | Toby | Not "Tobias" or "Tobey" |
| Skipper | Jono | Not "Jonno" or "John" |

**Ambiguity rule:** "Dr. Thorne" without a first name must always refer to the living scientist (Theodore). If Aris is meant, the text must say "Dr. Aris Thorne."

### Category 4: Frequency Notation

| Frequency | Notation | Count in Book 3 |
|-----------|----------|-----------------|
| Reef base | 0.95 Hz | 19 |
| Post-disruptor | 0.94 Hz | 1 |
| Pre-spike | 0.93 Hz | 6 |
| Simpson Desert | 0.47 Hz | 1 |
| Root (Book 2) | 2.1 Hz | 3 |

**Rules:**
- Always digit + space + Hz: `0.95 Hz`, NOT `0.95Hz`
- Spoken frequencies may use words: "point nine five Hz" — acceptable in dialogue
- No frequency should appear with inconsistent notation within the same book

### Category 5: Mark Device Naming

- Roman numerals: `Mark IV`, `Mark V`, `Mark I`, `Mark II`, `Mark III`
- Never lowercase: NOT `mark iv` or `mark v`
- Never Arabic numerals: NOT `Mark 4` or `Mark 5`
- Never combined: NOT `MarkIV` or `MarkV`

### Category 6: Terminology Continuity

| Term | Canonical Form | Variants to Flag |
|------|-------------|------------------|
| Disruptor device | disruptor | NOT "disrupter" |
| Filter-feeder organism | filter-feeder | hyphenated; NOT "filter feeder" or "filterfeeder" |
| Hydrophone | hydrophone | NOT "hydrofon" |
| Bioluminescence | bioluminescent (adj), bioluminescence (noun) | |
| Ascidians | ascidians | NOT "acidians" |

### Category 7: Grammar Patterns

| Error | Search Pattern | Fix |
|-------|---------------|-----|
| could of / should of / would of | `\b(could\|should\|would)\s+of\b` | → ... have |
| different than | `\bdifferent\s+than\b` | → different from |
| try and (narrative) | `\btry\s+and\b` | → try to |
| its / it's confusion | `its\s+(the\|a\|not\|own)` | → it's |
| missing apostrophe (possessive) | `Marcos\s+`, `Nates\s+` | → Marco's, Nate's |

**Skip dialogue** — characters make grammatical errors. Only fix narrative.

### Category 8: Punctuation

| Check | Pattern |
|-------|---------|
| Smart quotes | `\u201c`, `\u201d`, `\u2018`, `\u2019` | Replace with straight `"` and `'` |
| Double spaces | `  ` in prose | Replace with single space |
| Trailing whitespace | line ends with ` ` | Strip |
| Unclosed italics | unmatched `*` on a line | Verify and close |

---

## Execution: Fix Only Verified Issues

### Fix criteria

1. **Genuine** — not a false positive from regex (e.g., "program" inside "computer program")
2. **In scope** — not a prose-style issue (rhythm, repetition, showing-vs-telling)
3. **Isolated** — small surgical change, not a structural rewrite
4. **Verified** — read the exact line before and after to confirm context

### Typical fix count

A clean manuscript that has already passed Line Edit should have **0–5** genuine mechanical issues. If you find 20+, something went wrong in earlier stages — escalate to the user.

| Book | Stage | Genuine Issues Found | Chapters Touched |
|------|-------|---------------------|------------------|
| Book 3 | Stage 7 | 3 | 3 of 17 |

### Fix priority

1. **British spelling** (1 fix): `center` → `centre`
2. **Entity capitalization** (2 fixes): `the pattern` → `the Pattern`, `the signal` → `the Signal`
3. **Everything else verified clean** — do NOT invent issues

### What NOT to fix

| Not an Issue | Why |
|-------------|-----|
| "synchronized" in Book 2 canon | Already verified; not in Book 3 |
| "The Wet" vs "the Wet" | First mention = "The"; subsequent narrative = "the" — both correct |
| Chapter titles with "The Signal" | Structural, not narrative capitalization |
| Dialogue with American spellings | Characters may speak American English |
| "try and" inside dialogue | Character speech, not narrator error |

---

## Verification Results Table

After fixes, produce a verification table for the handoff:

| Category | Scan Result |
|----------|-------------|
| Spelling | Americanisms: [N found / CLEAN] |
| Character names | Ambiguities: [N found / NONE] |
| Frequencies | Notation consistency: [PASS / FAIL] |
| Mark devices | Naming consistency: [PASS / FAIL] |
| Terminology | Variant spellings: [N found / NONE] |
| Punctuation | Smart quotes: [N found / NONE]. Double spaces: [N found / NONE]. Trailing whitespace: [CLEANED / NONE] |
| Grammar | Errors: [N found / NONE] |
| Timeline | Contradictions: [N found / NONE] |
| Numerical formats | Mixed formats: [N found / NONE] |

**If all categories are CLEAN, say so explicitly.** A clean scan is a positive result, not a missed opportunity.

---

## Re-Assembly

After fixing source chapter files, re-assemble `BOOK<N>_COMPLETE.md` by concatenating all chapters in order. Net word delta should be **±0** (or very close — mechanical fixes swap one word for another).

**Verify:**
- 17 chapters present and parse correctly
- End markers present (17x)
- No unexpected headings
- Trailing whitespace cleaned

---

## Commit Format

```
Book N: Copy Edit (Stage 7) — N mechanical fixes: <list>. All other terminology,
spelling, names, frequencies verified clean. X files, Y changes, net ±0 words.
```

Example:
```
Book 3: Copy Edit (Stage 7) — 3 mechanical fixes: 'center'→'centre' (Ch 7),
'the pattern'→'the Pattern' (Ch 2), 'the signal'→'the Signal' (Ch 6).
All other terminology, spelling, names, frequencies verified clean.
4 files, 6 changes, net ±0 words.
```

---

## Output

After Copy Edit completes, update:

- `handoff/MASTER-HANDOFF.md` — add Copy Edit fix summary and verification table
- `tracking/BOOK<N>_DASHBOARD.md` — move pipeline stage to 8 (Assembly pending)
- `BOOK<N>_COMPLETE.md` — re-assembled from fixed chapters

**Do NOT ask the user for re-review.** Copy Edit is autonomous by design. Present the verification table and proceed to Assembly.

---

## Real Data (Book 3, Stage 7)

**Commit:** `3bc6c13`
**Files changed:** 4 (chapter source files + assembled manuscript)
**Insertions/deletions:** +6 / -6
**Net delta:** ±0 words (40,571 unchanged)
**Chapters touched:** 3 of 17 (Ch 2, Ch 6, Ch 7)

**Fixes:**
1. `center` → `centre` (Ch 7, narrative)
2. `the pattern` → `the Pattern` (Ch 2, quoted email text)
3. `the signal` → `the Signal` (Ch 6, narrative)

**Verification (all clean):**
- Spelling: No Americanisms in narrative
- Character names: `Dr. Thorne` (96x, Theodore), `Dr. Aris Thorne` (2x), `Mrs. Brennan` (1x) — zero ambiguity
- Frequencies: 0.95 Hz (19x), 0.93 Hz (6x), 0.94 Hz (1x), 0.47 Hz (1x), 2.1 Hz (3x) — consistent notation
- Mark devices: `Mark IV` (40x), `Mark V` (23x) — Roman numerals, zero lowercase
- Terminology: `disruptor` (14x), `filter-feeder` (4x), `Innisfail` (18x), `Port Douglas` (37x), `Lizard Island` (7x), `Simpson Desert` (5x) — all consistent
- Punctuation: Straight quotes, no double spaces, no unclosed italics
- Grammar: No "could of," "different than," "try and" in narrative
- Timeline: Eight months (4x), six months (9x), three days (6x), two weeks (6x) — coherent
- Numerical formats: Consistent (digit + space + Hz)

---

*Reference: created 2026-07-16 during Book 3 Copy Edit (Stage 7).*
