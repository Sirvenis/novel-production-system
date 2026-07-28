# Skill: Continuity Check

**Purpose:** Detect thread gaps, timeline inconsistencies, and broken motif chains across a multi-chapter manuscript. This is a mechanical verification pass, not an editorial assessment.

**When to use:** After Assembly (Stage 8), before Final QA (Stage 9). Also useful after any revision pass that modified chapters — revisions can introduce new continuity breaks.

**When NOT to use:** Before the manuscript is fully assembled — partial manuscripts produce false positives for "missing" chapters.

**Who runs this:** Showrunner (master) profile.

---

## What It Does

The Continuity Check verifies five dimensions:

1. **Thread continuity** — Does every key entity/term appear in the chapters where it should?
2. **Timeline coherence** — Do time references (days, weeks, months) agree across chapters?
3. **Motif chain integrity** — Are recurring symbols/objects (continuity locks) present and consistent?
4. **Character presence** — Do characters appear in the chapters the architecture says they should?
5. **Foreshadowing/payoff tracking** — Are seeds planted before they pay off?

---

## Execution Steps

### Step 1: Load the Architecture

Read `BOOK<N>_ARCHITECTURE.md` and extract:
- Expected chapter count
- Character list with first-appearance chapters
- Key entities/terms (threat name, frequency values, locations, devices)
- Timeline framework (what time period, what gaps between books)
- Foreshadowing seeds and their payoff chapters

### Step 2: Thread Continuity Matrix

For each key term, count mentions per chapter:

```bash
for term in "character_name" "threat_name" "frequency_value" "location"; do
    echo "=== $term ==="
    for ch in chapter-*.md; do
        num=$(echo "$ch" | sed 's/chapter-//' | sed 's/.md//')
        hits=$(grep -ic "$term" "$ch")
        echo "Ch $num: $hits"
    done
done
```

Produce a matrix:

| Term | Ch1 | Ch2 | Ch3 | ... | ChN | Gaps |
|------|-----|-----|-----|-----|-----|------|
| Character A | 5 | 3 | 0 | | 2 | Ch3: should appear (architecture says present) |
| Threat Name | 2 | 4 | 1 | | 8 | None |
| 0.95 Hz | 0 | 1 | 0 | | 3 | Ch1, Ch3: thread drop |

**Gap criteria:** Zero mentions in a chapter where the architecture says the entity/term should be present. Not every zero is a gap — only architecturally expected zeros.

### Step 3: Timeline Verification

Extract all time references from every chapter:

```bash
grep -in "day\|week\|month\|hour\|yesterday\|tomorrow\|ago\|since\|until" chapter-*.md
```

For each time reference, record:
- Chapter number
- The reference (e.g., "three days ago", "six months before")
- What it refers to (which event/character)

Check:
- Do references agree across chapters? (If Ch 3 says "six months since Book 2" and Ch 7 says "eight months since Book 2", flag the contradiction.)
- Is the timeline physically possible? (If a character arrives "tomorrow" in Ch 2 but is present in Ch 2, flag.)
- Are gaps between books consistent? (Same gap mentioned in multiple chapters should have the same duration.)

### Step 4: Motif Chain Tracking

Identify continuity locks from the architecture or editorial reports — recurring objects/symbols that anchor the reader's sense of continuity.

Common motif types:
- Personal objects (a toothbrush, a wedding ring, a specific weapon)
- Sensory anchors (a smell, a sound, a color)
- Phrase echoes (a line that recurs or evolves across chapters)

For each motif:
```bash
grep -in "motif_phrase" chapter-*.md
```

Verify:
- The motif appears in the chapters where it should
- It doesn't appear in chapters where it shouldn't (overuse)
- Its description/usage is consistent (a blue toothbrush stays blue)

### Step 5: Character Presence Audit

From the architecture, extract expected character appearances per chapter. Then:

```bash
for char in "Character A" "Character B" "Character C"; do
    echo "=== $char ==="
    for ch in chapter-*.md; do
        num=$(echo "$ch" | sed 's/chapter-//' | sed 's/.md//')
        hits=$(grep -c "$char" "$ch")
        if [ "$hits" -gt 0 ]; then
            echo "Ch $num: present ($hits mentions)"
        fi
    done
done
```

Flag:
- Characters missing from chapters where the architecture says they appear
- Characters appearing in chapters before their introduction
- Characters who vanish for long stretches without explanation

### Step 6: Foreshadowing/Payoff Tracking

From the architecture, extract each foreshadowing seed and its intended payoff chapter.

For each seed-payoff pair:
- Verify the seed exists in the planted chapter (grep for the seed phrase)
- Verify the payoff exists in the target chapter
- Count intermediate references (breadcrumbs) — should be 2-3 between seed and payoff
- Flag any seed with zero breadcrumbs (introduced and then ignored until payoff)

### Step 7: Output

Write the check as `revisions/BOOK<N>_CONTINUITY_CHECK.md` containing:

1. Thread continuity matrix (terms x chapters, gaps flagged)
2. Timeline verification table (reference, chapter, consistency verdict)
3. Motif chain status (motif, chapters present, consistent Y/N)
4. Character presence map (character, chapters present/absent, anomalies)
5. Foreshadowing/payoff tracking table (seed, planted, breadcrumbs, payoff, verdict)
6. Summary: PASS (all checks clear) / FLAG (specific issues to address in Final QA)

**The check is factual.** It does not prescribe fixes. The showrunner decides what to address.

---

## Verification

- [ ] Architecture was read before running any grep commands
- [ ] Thread matrix covers all key terms from the architecture
- [ ] Timeline references were cross-checked between chapters
- [ ] Every motif in the architecture was checked
- [ ] Character presence was checked against architecture expectations
- [ ] Every foreshadowing seed was verified with grep
- [ ] No fixes were applied during the check — this is detection only

---

## Common Failure Modes

| Failure | Cause | Fix |
|---------|-------|-----|
| False positive gap | Flagged zero mentions without checking architecture | Only flag zeros where architecture says the term should appear |
| Timeline contradiction missed | Only read individual chapters | Cross-reference time mentions across all chapters |
| Motif inconsistency not caught | Only checked presence, not description | Verify the motif's attributes are consistent (color, size, condition) |
| Foreshadowing seed missed | Only checked the payoff chapter | Grep for the seed phrase in its planted chapter and all intermediate chapters |

---

## Tools

- `read_file` — read architecture and chapter files
- `search_files` / `grep` — thread counts, timeline extraction, motif tracking, character presence
- `execute_code` — batch process the matrix and produce tables
- `write_file` — write the continuity check report

---

*Skill created for the novel-production-system. Aligns with the thread-continuity gap detection method from the developmental editorial four questions reference, and the Final QA checklist in the assembly-final-qa execution pattern.*