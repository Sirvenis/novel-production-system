# Skill: Voice Audit

**Purpose:** Verify that the manuscript's voice is consistent, authentic, and free of prose-level tics. This is a guardrail check, not an editorial assessment.

**When to use:** After Line Edit (Stage 6), before Copy Edit (Stage 7). Also useful after any revision pass to catch tics that intensified during rewriting.

**When NOT to use:** During drafting — voice is still forming. Before the editorial pipeline — structural issues take priority.

**Who runs this:** Editor profile.

---

## What It Does

The Voice Audit checks three dimensions:

1. **Voice consistency** — Does the narrator's voice remain stable across all chapters?
2. **Vernacular authenticity** — Is regional/class dialect earned and consistent, not performative?
3. **Tic detection** — Are any words or phrases repeated mechanically beyond their dramatic purpose?

---

## Execution Steps

### Step 1: Establish the Voice Baseline

Read the Voice Guardrails file for the series (e.g., `VOICE_GUARDRAILS.md` in the project repo).

Extract:
- The golden rule (e.g., "Voice is not costume. Voice is consequence.")
- Prohibited phrases list
- Dramatic-purpose dialect rule
- The Confidence Test questions

Read 3 representative chapters (opening, middle, ending) to establish what the voice sounds like at its best.

### Step 2: Per-Chapter Voice Sample

For each chapter, read:
- First 3 paragraphs
- A middle section (random selection)
- Last 3 paragraphs

Check:
- Does the voice match the baseline?
- Has the POV contract been maintained? (first-person stays first-person, etc.)
- Does the vernacular level match the guardrails? (not over-dialect, not under-textured)

### Step 3: Prose Tic Detection

Run automated frequency analysis:

```bash
# Top 20 most frequent non-dialogue words across the manuscript
grep -oh '\b[a-z]\{4,\}\b' BOOK<N>_COMPLETE.md | sort | uniq -c | sort -rn | head -20
```

Then check series-specific tic patterns:

| Pattern | Why It's a Tic | Threshold |
|---------|---------------|-----------|
| "pulse/pulsing/pulses" | Rhythmic threat vocabulary becomes a crutch | > 3 per chapter |
| "I tell myself" | Self-rationalization motif repeats mechanically | > 2 per chapter |
| "I do not run" | Coping mechanism becomes a refrain | > 1 per chapter |
| "I do not sleep" | Insomnia motif becomes heavy | > 1 per chapter |
| Identical line echoes | Lines repeated across chapters without variation | Any exact match |
| Character's signature phrase | Becomes a catchphrase instead of a character beat | > 2 per chapter |

**Rule:** A word/phrase becomes a tic when its frequency exceeds its dramatic function. A character who says "right" three times in a chapter is voice. A narrator who uses "pulse" eight times is a tic.

### Step 4: Prohibited Phrase Check

Run the prohibited phrases list from the Voice Guardrails against every chapter:

```bash
for phrase in "prohibited phrase 1" "prohibited phrase 2"; do
    echo "=== $phrase ==="
    grep -in "$phrase" chapter-*.md
done
```

### Step 5: The Confidence Test

For any passage where voice feels off, apply the Confidence Test from the Voice Guardrails:

1. Does this sound like something [protagonist] would actually think?
2. Would [protagonist] use this word in this situation?
3. Does this sentence advance the reader's understanding of power, threat, or intimacy?
4. Would a reader from [region] recognise this as authentic, not performative?
5. Does this sentence survive removal from context?
6. If I remove the dialect from this sentence, does anything meaningful change?

### Step 6: Output

Write the audit as `revisions/BOOK<N>_VOICE_AUDIT.md` containing:

1. Voice baseline summary (what the voice sounds like at its best)
2. Per-chapter voice assessment (consistent / drift detected / breakdown)
3. Tic detection results (word/phrase, frequency, chapters affected, severity)
4. Prohibited phrase findings (any matches flagged)
5. Confidence test results (any passages that failed)
6. Summary: PASS (voice is clean) / FLAG (specific issues to address before copy edit)

**The audit does NOT prescribe fixes.** It identifies problems. The editor decides whether to fix in line edit revision or flag for the writer.

---

## Verification

- [ ] Voice Guardrails file was read before sampling chapters
- [ ] Every chapter was sampled (first/middle/last)
- [ ] Automated tic detection was run across the full manuscript
- [ ] Prohibited phrase check covered all items in the guardrails
- [ ] No fixes were applied during the audit — this is detection only

---

## Common Failure Modes

| Failure | Cause | Fix |
|---------|-------|-----|
| Tics not detected | Only read chapters, didn't grep | Run automated frequency analysis on the full manuscript |
| Over-flagging | Flagged every repeated word as a tic | Apply the dramatic-function test: does the repetition serve a purpose? |
| Voice drift missed | Only read openings | Always sample middle and ending paragraphs too |
| Fixing instead of auditing | Editor drifted to revision | This is detection only. Note the issue and move on. |

---

## Tools

- `read_file` — read chapter sections
- `search_files` / `grep` — frequency analysis and prohibited phrase detection
- `execute_code` — batch frequency counting and table generation
- `write_file` — write the audit report

---

*Skill created for the novel-production-system. Aligns with VOICE_GUARDRAILS_TEMPLATE.md and the prose-level tic detection pattern from the pre-pipeline revision reference.*