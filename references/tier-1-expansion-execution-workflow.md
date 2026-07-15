# Tier 1 Expansion Execution Workflow

## When

After the Discovery Pass has classified chapters into tiers, and the user has approved Tier 1 targets. Before any developmental editorial begins.

## What Tier 1 Expansion Actually Means

Tier 1 chapters are critical: revelation chapters, action chapters, emotional climax chapters. The user has approved deepening them. The expansion brief identifies specific focuses per chapter (sensory immersion, scientific reasoning, emotional weight, etc.).

**Core philosophy (DEC-008):** Deepen existing material. No new subplots, reveals, or mythology. Add sensory immersion, relationship conversations, investigative reasoning, atmosphere, emotional aftermath, slower tension, clearer transitions.

## Execution Steps

### 1. Pre-flight: Read Context Surrounding the Chapter

Before expanding any chapter, read the **previous chapter** and the **next chapter** in full. Tier 1 expansion adds material — you must know:
- What state characters are in when they enter this chapter
- What state they must be in when they leave
- What plot beats must not be duplicated or contradicted
- What emotional temperature must be maintained across the boundary

**Do not skip this.** Expansion that ignores surrounding context creates continuity gaps that are harder to fix later.

### 2. Read the Expansion Brief

The brief lives in `tracking/BOOK<N>_TIER1_BRIEFS.md`. Each chapter has:
- Current word count (from Discovery Pass — actual, not architecture estimate)
- Target range (job-based, not fixed)
- Specific expansion focuses numbered 1–6
- "Deepen, Don't Add" constraints

### 3. Write the Expanded Chapter as a Complete Replacement

**Do not patch the existing chapter line-by-line.** Write the new chapter from scratch, incorporating all original material and weaving in new material inline.

**Why complete replacement:**
- Ensures pacing coherence — new material is distributed, not appended
- Prevents Frankenstein seams where old and new prose meet jarringly
- Forces you to re-read every sentence, catching continuity errors
- Easier to verify with `wc -w` and `read_file` tail checks

**The replacement trap (CRITICAL):** When writing a "complete replacement" that incorporates the original text, it is extremely easy to subconsciously reproduce the original draft almost verbatim — especially if you just re-read it. You think you're expanding, but the output is the same length. 

**Detection:** After writing the replacement, run `wc -w` on the new file immediately. If the count is within ~5% of the original, you fell into the trap. The expanded version must be measurably larger.

**Fix:** If the count hasn't grown, re-read the expansion brief's specific focuses, pick the three largest, and explicitly write new paragraphs for each before the next self-edit pass. Do not trust your intuition about "I added stuff" — verify with numbers.

**Weaving technique:**
- Identify 3–5 specific expansion targets from the brief
- For each target, locate the corresponding section in the original draft
- Write new paragraphs that fit the surrounding voice and POV
- Extend existing scenes rather than adding new scenes
- Add sensory detail to moments that were previously summarized
- Add character reactions to moments that were previously narrated
- Add transitional paragraphs between scenes that jumped

### 4. Self-Edit Checklist

Before updating the manuscript:
- [ ] No character name errors (search for old names, e.g. "Henderson")
- [ ] No duplicate words adjacent (regex `(\b\w+\b)\s+\1`)
- [ ] POV consistency maintained (Nate first-person present, etc.)
- [ ] All original dialogue and beats preserved
- [ ] No new subplots or reveals added
- [ ] Word count within target range (**verify with `wc -w chapter-XX.md` — must be measurably larger than original**)
- [ ] Ending transitions smoothly to next chapter's opening

**Note on `wc` usage:** `wc -w` on an individual chapter file is safe and accurate. The caching/stale-output issue applies only to `wc` on the compiled manuscript (`BOOK<N>_COMPLETE.md`) after it has been rewritten via `write_file` or `patch` — the filesystem timestamp may not update immediately, and `wc` can return the old count. For chapter files, `wc` is fine.

### 5. Replace Chapter in Compiled Manuscript

The compiled manuscript (`BOOK<N>_COMPLETE.md`) is assembled from individual chapters. When one chapter expands, the compiled manuscript must be rebuilt.

**Primary technique — Python raw-text replacement (recommended):**

Read the compiled manuscript as raw text (not with line-number prefixes, which `read_file` injects). Use Python to find the exact character positions of the chapter start and the next chapter's start, then splice the new chapter in between.

```python
# Read the compiled manuscript as raw text
with open('BOOK<N>_COMPLETE.md', 'r') as f:
    full_text = f.read()

# Read the new chapter file
with open('book<N>-drafts/chapter-XX.md', 'r') as f:
    new_ch = f.read()

# Find boundaries — exact markers, not line numbers
ch_marker = "# Chapter XX: Title\n"
next_marker = "# Chapter XX+1: Title\n"

start_idx = full_text.find(ch_marker)
end_idx = full_text.find(next_marker)

# The old chapter text includes everything from ch_marker
# through the separator line (---\n\n) before next_marker.
# Extract the old slice first to verify:
old_slice = full_text[start_idx:end_idx]

# Prepare the new chapter — ensure trailing separator
new_ch_prepared = new_ch.rstrip() + "\n\n---\n\n"

# Build and write
new_full = full_text[:start_idx] + new_ch_prepared + full_text[end_idx:]

with open('BOOK<N>_COMPLETE.md', 'w') as f:
    f.write(new_full)
```

**Why this works:** `read_file()` injects line numbers (`1234|content`) into its output. If you use that output for replacement, every line in the manuscript gets corrupted with line-number prefixes. The Python script reads raw bytes, avoiding this entirely.

**Why not patch with `patch` tool:** `patch` (the `replace` action) requires unique `old_string` matches. In a 5,000+ line compiled manuscript, many paragraphs are not unique. It is faster and more reliable to do a positional splice than to fight with uniqueness requirements.

**Why not the line-number technique from the original version of this doc:** Enumerating lines with `enumerate(lines)` and searching for `# Chapter X:` is fragile — chapter titles can vary, separator lines can shift, and the script can silently fail if the next chapter marker is not found. Raw-text `find()` on exact markers is deterministic.

**Legacy technique — line-based replacement (discouraged but documented):**

```python
with open('BOOK<N>_COMPLETE.md', 'r') as f:
    lines = f.read().split('\n')

start_idx = None
next_ch = None
for i, line in enumerate(lines):
    if '# Chapter X: Title' in line:
        start_idx = i
    if start_idx and '# Chapter X+1:' in line:
        next_ch = i
        break

# ...read new chapter lines, splice...
```

This approach has two failure modes: (a) chapter titles with colons or variations may not match, (b) missing the `break` causes the loop to overwrite `next_ch` with a later match. Use the raw-text technique instead.

**Critical:** After writing `new_full`, always verify with `read_file` around the splice point — check that the next chapter header is at the expected position and no corruption occurred.

### 6. Verify the Assembly

After replacement:
- `wc -w BOOK<N>_COMPLETE.md` — confirm total word count changed
- `grep -n "# Chapter X+1:"` — confirm next chapter header is at expected line
- `sed -n 'N,N+5p'` — spot-check the transition between expanded chapter and next chapter
- `grep -n "End Chapter X"` — confirm end marker present

### 7. Update Tracking Files

- `tracking/BOOK<N>_DASHBOARD.md` — update word count, mark chapter ✅ Expanded
- `tracking/BOOK<N>_TIER1_BRIEFS.md` — mark chapter done, note actual word count, update next action
- `handoff/MASTER-HANDOFF.md` — update chapter word counts, total, next session brief

### 8. Commit

```bash
git add -A
git commit -m "Book N: Expand Chapter X — <Title>

- chapter-XX.md: Currentw → Neww (+delta)
- Expansion focuses addressed: (list)
- BOOK<N>_COMPLETE.md rebuilt with expanded chapter
- Dashboard, Tier1 briefs, handoff updated
- Word count: OldTotal → NewTotal"
```

**Include the delta and the list of focuses in the commit message.** This is the primary audit trail.

## Execution Order

The brief specifies order. Follow it. Typically:
1. Most impactful revelation chapter first (establishes understanding for reader)
2. Emotional template chapter second (sets underwater/physical horror tone)
3. Emotional climax third
4. Physical climax fourth

## Common Pitfalls

- **Appending instead of weaving:** Adding new scenes at the end rather than distributing depth through existing scenes. This bloats the chapter without improving its core job.
- **Forgetting the brief's constraints:** Adding a new subplot because "it would be cool." The user's philosophy is "deepen, don't add." Respect it.
- **Not reading surrounding chapters:** Creating continuity errors with adjacent chapters because you only read the one being expanded.
- **Stale tracking:** Updating the source chapter but not the dashboard, handoff, or compiled manuscript. All four must stay in sync.
- **Skipping verification:** Trusting the replacement script without spot-checking the assembly. Always verify.

## Example: Chapter 9 — The Network

**Original:** 1,473w | **Target:** 3,500–5,000w | **Delivered:** 3,348w

**Six focuses addressed:**
1. Data accumulation — Raj's 2 AM discovery, false leads rejected
2. Visualization — 200km living circuit board mapped
3. Scale horror — hundreds of growth rings = ancient beyond human history
4. Crew reaction — council of war, individual processing per character
5. Strategic implication — target the "prefrontal cortex," not whole network
6. Entity counter-revelation — tuning confirmed as EEG mind-hacking

**New material woven inline:**
- Pre-dawn Raj scene (before original 7 AM opening)
- Medical/brainwave parallel during dive (Maya explains multiple frequencies = complex cognition)
- Council of war scene (evening, between dive and dream)
- Copper sulfate discarded option
- Foreshadowing for barrier/eddies plan (seeds Ch 10)

**Preserved:** All original dialogue, beats, dream sequence, end marker.

*Created from Book 3 Tier 1 expansion execution, July 2026.*

---

## Example: Chapter 15 — The Sacrifice

**Original:** 2,214w | **Target:** 3,500–5,000w | **Delivered:** 4,195w | **+1,981w**

**The replacement trap caught live:** First draft of the replacement was 3,067w — only +853w from original. The brief demanded 6 specific focuses, but the agent subconsciously reproduced the original draft with minor additions. Detection: `wc -w` showed 3,067 vs target 3,500+. Fix: re-read the brief's 3 largest focuses (argument/debate, preparation detail, deck conversation), wrote new material for each, second pass delivered 4,195w.

**Six focuses addressed:**
1. **The realization** (~400w added): Marco's reasoning about the entity processing his DNA through touch. Chain of deduction made explicit.
2. **The argument** (~600w added): Full crew debate. Alternatives rejected (Mark V, reef demolition, evacuation). Marco's distinction between "dying" and "offering." Nate's reluctant acceptance. Maya's grief, leaving the table.
3. **The preparation** (~400w added): Detailed blood-drawing scene — Maya's steady hands and clenched jaw, dark blood, violence of sealing the bag. Mixture preparation with sensory detail (bruise-colour, chemical smell). Maya and Marco's quiet exchange.
4. **The act** (~500w added): Deck conversation — São Paulo rain, "small in the right way." Boat ride — crew reactions (Maya with useless medical kit, Lena white-knuckled, Dr. Thorne muttering probabilities). Expanded injection sequence with pause before needle.
5. **The death** (~300w added): Nate's dive includes heat through wetsuit, syringe still in hand, polyps wrapping calves "like a child holding a parent's hand."
6. **The aftermath** (~200w added): Sea burial preserved. Individual grief reactions preserved. The silence.

**What made this expansion work (vs. Ch 9):**
- Ch 15 is an emotional climax, not a revelation chapter. The expansion focused on **character interiority** (Marco's calm, Nate's inability to argue, Maya's medical helplessness) rather than **worldbuilding detail**.
- The São Paulo rain conversation is the emotional anchor — it gives Marco a reason beyond abstract justice. He is not sacrificing for the reef. He is sacrificing so that someone else can stand in the rain and feel small in the right way.
- The argument scene makes the sacrifice **earned by the group**, not just by Marco. When the crew exhausts every alternative, Marco's choice becomes inevitable rather than impulsive.

**Technique — reading surrounding chapters for continuity:**
Before writing, read Ch 14 (The Pressure — Marco weak after dive, explosives failed, entity dispersed and more dangerous) and Ch 16 (The Cost — Maya holding Nate's hand since Marco died, the talk, Maya's secret about Dr. Aris Thorne). The expansion had to preserve: Marco's physical weakness entering, Nate's guilt and exhaustion carrying forward, Maya's hand-holding as established in Ch 16's opening.

**Manuscript replacement:** Used Python raw-text `find()` on exact markers (`# Chapter 15: The Sacrifice\n` and `# Chapter 16: The Cost\n`). `read_file` line-number output was avoided. Verified with `grep -n "# Chapter 16:"` and spot-checked transition.

*Book 3 Tier 1 expansion, July 2026.*
