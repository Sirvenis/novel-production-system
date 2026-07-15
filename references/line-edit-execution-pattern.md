# Line Edit Execution Pattern (Stage 6)

**When:** After Reader Audit fixes (Stage 5.5) complete and approved. Before Copy Edit (Stage 7).

**Purpose:** Polish prose at the sentence and paragraph level. Trim repetition, tighten dialogue, fix rhythm, catch POV slips. Preserve every structural and emotional beat already established. This is NOT a structural rewrite — it is surgical prose cleanup.

**Model:** Autonomous execution under autonomy grant. The user should NOT be asked to review individual line changes.

---

## Pre-Execution: Audit

Before touching any prose, run a pattern-audit across all chapter source files. This identifies the specific tics that have accumulated across the manuscript.

**Search patterns (run via `search_files`):**

| Pattern | Regex | Why It Matters |
|---------|-------|----------------|
| "That's worse" echo | `That's worse` | Characters repeating the same phrase back-to-back reads as lazy. Only the first instance should stand; the second needs replacement or deletion. |
| "Not X. Not X. But Y." | `Not [A-Za-z]+\. Not [A-Za-z]+\. But` | Identical triple-beat rhythm across chapters becomes predictable. Vary the phrasing: "A slight shift, barely perceptible, but measurable." |
| "The thing about..." | `[Tt]he thing about` | Paragraph-opening filler. If the context already signals reflection, cut the throat-clearing. |
| Throat-clearing openers | `^I think |I know |I feel ` at para start | "I think about this." before a reflection the reader can already see is redundant. The sentence stands on its own. |
| POV slips | `knows what |knows that |thinks that |is thinking|is feeling` (not Nate's own thoughts) | Nate never knows what others think. He observes behaviour. Flag lines that violate this. |
| Dialogue tag audit | `"[^"]{20,80}"\s*,?\s*(he says\|she says\|I say)` | Tag every line that ends with "X says" after a quote of 20-80 chars. These are candidates for replacement with action beats. |

**Audit output:** A table with chapter, line number, text snippet, and proposed fix. This is for internal use — the user does not need to see it.

---

## Phase 1: High-Impact Repetition Fixes

Apply first. These have the highest reader-visible impact.

### "That's worse" echo

When two characters repeat "That's worse" in succession, remove or replace the second instance.

- **Option A:** Replace second with an action beat: "Maya nods, her jaw tight. The boat cuts through dark water..."
- **Option B:** Replace with a physical reaction: "I nod. The room feels smaller."
- **Option C:** Delete entirely if the scene carries without it.

**Do NOT:** Keep both. The echo is unintentional and reads as the author running out of ideas.

### "Not X. Not X. But Y." rhythm

Replace with varied phrasing that preserves the meaning but breaks the identical cadence:

| Original | Replacement |
|----------|-------------|
| "Not dramatically. Not obviously. But measurably." | "A slight shift, barely perceptible, but measurable." |
| "Not dead. Not destroyed. But wounded." | "Not dead. Not destroyed. Wounded. Grieving." (drop the "But" entirely) |
| "Not loud. Not obvious. But when I..." | "Not loud. Not urgent. But when I..." (vary the second adjective) |

**Rule:** Preserve the content (the change IS slight/perceptible). Kill the cadence duplication.

### "I think about this" throat-clearing

Cut the opener. The sentence that follows is already a reflection.

| Before | After |
|--------|-------|
| "I think about this. I think about the six months of checking..." | "I think about the six months of checking..." |
| "I think about this. The Root had a single frequency..." | "The Root had a single frequency..." |

**Exception:** Keep when it serves as a deliberate pause or transition between unrelated thoughts. But 90% of instances are filler.

---

## Phase 2: Dialogue Tag Trimming

Replace unnecessary "X says" tags with action beats, physical descriptions, or silent attribution.

### When to trim

Trim when:
- The speaker is obvious from context (only two people in the scene)
- The line immediately before or after is already attributed
- The tag adds no information ("he says" after a line of dialogue)

### When to keep

Keep when:
- The speaker would be ambiguous (3+ people in scene, all talking)
- The tag carries emotional weight ("she says, her voice flat")
- The tag is part of a question/answer rhythm

### Replacement techniques

| Technique | Example |
|-----------|---------|
| Action beat | `"It's not just a frequency anymore." Raj's fingers drum the table. "It's a signal."` |
| Physical description | `"It's not your fault." Maya examines him — checking his pupils with a penlight...` |
| Silent attribution | `"We test it on Patch One. From a distance. If it works, we move to Patch Two."` (no tag needed — speaker established) |
| Voice quality | `"I think the entity offers something we all want." Maya's voice is careful, measured.` |

**Rule:** Every dialogue tag you remove should be replaced by either (a) nothing, if context is clear, or (b) an action beat that deepens the scene. Never leave the reader guessing who spoke.

---

## Phase 3: POV and Showing-vs-Telling Verification

### POV slip detection

Nate is first-person present. He never knows what others think, feel, or intend. He observes behaviour.

| POV Slip | Fix |
|----------|-----|
| "Marco knows what the patch does." | "Marco has seen what the patch does." or "Marco's jaw tightens — he knows." |
| "She is thinking about the Pattern." | "She stares at the water, her jaw tight. She is thinking about something she won't name." |

**Verification:** After all fixes, grep for `knows what|knows that|thinks that|is thinking|is feeling` in Nate-POV chapters. Every hit should be either (a) Nate's own thought about himself, or (b) Nate speculating based on observed behaviour.

### Showing vs telling

The audit (Stage 6) rarely finds gross telling because earlier passes already caught it. But verify:

| Telling | Showing |
|---------|---------|
| "He was angry." | "His hands shake. He won't meet my eyes." |
| "She was scared." | "She backs toward the door, her fingers white on the handle." |

---

## Phase 4: Re-Assembly and Verification

After all source chapter files are edited:

1. **Re-assemble `BOOK<N>_COMPLETE.md`** by concatenating all chapter files in order.
2. **Verify net word delta:** Should be near-zero (±50 words). A line edit is not an expansion or compression pass.
3. **Spot-check 3 chapters:** Opening, middle, climax. Read 20 lines each to confirm rhythm is clean and no broken sentences remain.

---

## Commit Format

```
Book N: Line Edit (Stage 6) — <summary of fixes>. Preserve all structural/emotional beats.
```

Example:
```
Book 3: Line Edit (Stage 6) — trim 'That's worse' echo, 'Not X Not X But Y' repetition,
throat-clearing 'I think about this', unnecessary dialogue tags (says→action beats).
Preserve all structural/emotional beats. Net -4 lines, +6 words. 15 chapters touched.
```

---

## What Gets Deferred (Correctly)

Not every issue found in audit should be fixed in Line Edit. Defer to Copy Edit or later:

| Issue | Why Deferred |
|-------|--------------|
| British/Australian spelling inconsistency | Copy Edit (Stage 7) |
| Major exposition interleaving (Ch 6-7) | Risk of structural damage > benefit of prose polish. Flag for user decision. |
| Thin chapter expansion | Not a line-edit task. Expansion belongs in Tier 1 (if before line edit) or next book's architecture. |

---

## Output

After Line Edit completes, update:

- `handoff/MASTER-HANDOFF.md` — add Line Edit fix summary section
- `tracking/BOOK<N>_DASHBOARD.md` — move pipeline stage to 7 (Copy Edit pending)
- `BOOK<N>_COMPLETE.md` — re-assembled from fixed chapters

**Do NOT ask the user for re-audit.** Line Edit is autonomous by design. Present the fix summary and proceed.

---

## Real Data (Book 3, Stage 6)

**Commit:** `316f3fb`
**Files changed:** 15 (of 17 chapters)
**Insertions/deletions:** +74 / -78
**Net delta:** +6 words (40,565 → 40,571)
**Chapters untouched:** Ch 10, Ch 12 (clean in audit)

**Fixes by category:**
- "That's worse" echo: 2 instances (Ch 6, Ch 8)
- "Not X. Not X. But Y.": 6 instances (Ch 2, 5, 6, 9, 13, 15)
- "I think about this": 5 instances (Ch 3, 4, 8, 9, 17)
- Dialogue tags: 20+ replaced with action beats (Ch 1, 3, 4, 5, 6, 7, 9, 11, 13, 16)
- "The thing about": 2 instances (Ch 3, 7)

**Preserved:** All structural beats, Maya breadcrumbs x4, Simpson Desert seeds x3, Marco's copper sulfate moment, Mark V partial-success → camouflage, POV consistency, showing-vs-telling.

---

*Reference: created 2026-07-16 during Book 3 Line Edit (Stage 6).*
