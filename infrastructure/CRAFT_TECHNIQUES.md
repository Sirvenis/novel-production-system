# Craft Techniques — Genre-Agnostic Rules

These techniques were discovered during production and are reusable across genres.

---

## 1. Job-Based Word Ranges

Replace fixed per-chapter targets with ranges determined by narrative complexity.

| Chapter Type | Range | When to Use |
|--------------|-------|-------------|
| Setup / Introduction | 2,000–3,500 | Establishing ordinary world, new POV, slow burn |
| Escalation / Investigation | 3,000–5,500 | Core plot movement, discoveries, crew assembly |
| Action / Confrontation | 4,000–6,500 | High stakes, multiple locations, complex logistics |
| Emotional / Revelation | 2,500–4,500 | Character beats, secrets, aftermath |
| Finale / Epilogue | 2,000–4,000 | Resolution, sequel hooks, breathing room |

**Rules:**
- A chapter is done when its narrative job is complete — not when it hits a word count, and not when it runs out of steam.
- If a chapter is lean because its job was small, that is correct.
- If it feels thin because we rushed a beat, expand.
- Kill the "Target: ~70,000" line in architecture docs. Replace with "Estimated total based on chapter mandates: X–Y words."

---

## 2. Tier-Based Expansion Priority

After the Discovery Pass, classify chapters into expansion tiers:

**Tier 1 (Critical — expand before or during editorial):**
- Chapters whose job is NOT earned at current length
- Core revelation chapters
- Major action chapters
- Emotional climax chapters

**Tier 2 (High — expand during editorial if capacity):**
- Chapters that are lean but their job is present
- Science-heavy chapters that need more process/detail
- Strategy/planning chapters that need more debate

**Tier 3 (Medium — expand if time/capacity):**
- Transition chapters that could use more character moments
- Secondary action chapters that need more physical stakes
- Setup chapters that could deepen the ordinary world

**Execution:** Expand by weaving new material into existing scenes, not by appending. Verify with `read_file` tail checks (not `wc`).

---

## 3. Discovery Pass Workflow

**When:** Before Pass 3 Editorial. Always.

**Purpose:** Pure inventory. No recommendations. No plans. Just "what exists?"

**Steps:**
1. **Extract actual word counts** per chapter from compiled manuscript. Use line-range extraction, NOT inline markers (which may be stale) and NOT `wc` on the whole file (which caches).
2. **Inventory architecture alignment** — does each chapter deliver its mandated job?
3. **List contradictions** with series bible, character bible, previous books.
4. **List TK placeholders** — are there any?
5. **Record actual vs target** in a discovery table. Classify each chapter: Adequate / Lean / Underweight.
6. **Output:** `tracking/BOOK<N>_DISCOVERY_PASS.md`

**Critical:** The Discovery Pass output must NOT include recommendations. It is raw data. The editorial pass (Pass 3) uses this data as input.

---

## 4. Thread-Continuity Gap Detection

An important narrative thread can drop out during chapters where it should be present. This is invisible until the reader notices something missing.

**Detection:** Run grep counts of key terms across all chapters. Look for chapters with 0 refs that should have some.

**Fix:** Add 2-3 references, not a full explanation. A line of dialogue, a monitor reading, a character noticing the absence.

**Prevention:** When designing a chapter, check what threads are active at that point in the story. Ensure at least one reference survives, even if the chapter's focus is elsewhere.

---

## 5. Cadence Fatigue Detection

When consecutive chapters end with the same structural pattern, readers notice. It becomes predictable and deflates tension.

**Detection:** Read the last 5 lines of the final 3-4 chapters. If they all follow the same shape, flag it.

**Fix:** Vary at least half of them:
- Action-oriented ending (characters doing something concrete)
- Dialogue ending (final line is spoken, not narrated)
- Concrete-not-poetic (specific detail instead of abstraction)
- Subvert the pattern (the aphorism turns out to be wrong)

---

## 6. Broken Transition Repair

When a scene ends with characters in danger and the next scene opens in safety with no explanation, don't use "Three hours later..." summaries.

**Better:** Write a transition paragraph in the same narrative voice showing the actual journey — what they did, what they saw, what they felt — ending with arrival at the new location.

**Example:** "We drove back to Innisfail in silence. Maya kept the camera pointed out the back window... By the time we reached Sharon's bakery, the sun was setting and the ordinary world felt like a costume we'd outgrown." (Then open the new scene.)

---

## 7. Thematic Seeding Through Physical Imagery

When a philosophical concept pays off late in the book, seed it early through concrete physical imagery rather than abstract statements.

**Example:** Instead of having the narrator think "I guard the boundary," show them driving past fence wire and noticing the jungle pressing against cane fields. The physical boundary foreshadows the philosophical one.

**Rule:** The seed should appear 10–15 chapters before the payoff, in a scene where the reader doesn't yet know it's thematic.

---

## 8. Humor-Horror Rhythm (Genre-Specific Example)

While this rule was developed for cosmic horror-comedy, the principle is universal: alternate the dominant emotional mode to prevent fatigue.

**The Golden Rule:** No three [dominant mode] without a [release mode]. No two [release mode] without a [dominant mode]. Heartbeat moments every 4–5 chapters.

**Adaptation:**
- Gothic horror: No three atmospheric dread scenes without a concrete action or dialogue scene
- Survival horror: No three action scenes without a quiet character moment
- Psychological horror: No three unreliable-narrator scenes without an external confirmation

---

## 9. First-Person Narrator Discipline

The narrator's voice is the series' engine. It is also its greatest risk.

**Voice as coping mechanism:** The worse things get, the more the narrator jokes (or rages, or goes quiet). The voice IS the emotional arc.

**Throat-clearing:** Watch for "I think about this," "I realise that," "I wonder if." These distance the reader. Replace with direct observation or action.

**Filter words:** "I see," "I hear," "I feel" — remove where possible. "The wall screamed" is stronger than "I heard the wall scream."

---

## 10. The "Line" — Boundaries Between Normal and Impossible

A recurring motif that pays off across the series. It works in any genre where the protagonist bridges two worlds.

- The line between farmland and wilderness
- The line between normal and impossible
- The line the protagonist walks between their old life and their new one

**Rule:** If a theme arrives late, seed it early. The reader should feel the payoff as recognition, not surprise.

---

## 11. Rotating Opening Lens

When each book introduces a new character as the opening POV, that character carries the first 2 chapters before the series protagonist takes over.

**Why it works:**
- Fresh perspective makes the horror more credible
- Voice contrasts with the established narrator
- Delays reunion, building anticipation
- The new character's naivety mirrors the first-time reader's experience

**How to execute:**
- Give the new character 2 chapters of POV
- They must have a distinct voice from previous openers
- Their opening scene must establish their expertise
- Their discovery of the anomaly must feel earned through their specific expertise
- The protagonist's arrival should feel like relief

**Verdict:** The risk (returning readers miss the protagonist) pays off if the new voice is strong enough.

---

## 12. Entity Escalation Through Different Mechanics

Each book in a series should use a different mechanic for the threat. This prevents repetition and escalates the series creatively even when the structure remains consistent.

**Pattern:** Each threat targets a different human weakness:
- Book 1 → survival instinct (fear)
- Book 2 → productivity instinct (usefulness)
- Book 3 → belonging instinct (love/acceptance)
- Book 4 → memory/identity (the self)
- Book 5 → time/perception (reality itself)

**Technique:** When designing a new threat, identify the human instinct it weaponises. The horror is deeper when the compulsion feels like something the victim genuinely wants.

---

## 13. Word Count Shrinkage Detection (Critical for Series)

When architecture targets ~70k words but drafts consistently land at 45k, the series is at risk of shrinking novels.

**Root cause:** Chapter-level drafting produces 2.5k–3.5k chapters when the architecture mandates ~4k. The "lean and efficient" style compounds across books.

**Detection:** Compare first-draft totals book-over-book. If Book N drafts shorter than Book N-1, flag it immediately.

**Prevention:** Before drafting Book N+1, review Book N's actual chapter lengths vs architecture targets. If the pattern is "chapters draft 25-30% short," adjust the architecture: add chapters, add a B-plot, or mandate longer scenes.

**Series target decision:** Make the explicit choice early:
- (A) Target 70k and enforce it through architecture
- (B) Accept 45k as the "real" series length and architect accordingly
- (C) Let books vary as the series matures

**Do not let shrinkage happen by accident.**

---

## 14. The Banality of Horror

The most distinctive quality is how ordinary the threat feels.

**The rule:** The horror arrives during the most ordinary moments:
- A routine call
- A breakup argument
- A waiting room
- A bakery at 4 AM

**Why it works:** The contrast between cosmic threat and working-class ordinary creates the voice. The threat doesn't announce itself with thunder. It spreads like mold.

**Lesson:** The more ordinary the entry point, the more disturbing the horror.

---

## 15. Middle Act Sag Prevention

Classic structural problem: the middle act sags.

**The Book 1 pattern:**
- Hook (chapters 1–5): Discovery and escalation — STRONG
- Middle (chapters 6–9): Bureaucracy, grief, exposition — SAGS
- Recovery (chapters 10–13): Action, planning, battle — STRONG
- Resolution (chapters 14–17): Aftermath, signal, sequel hook — STRONG

**The fix:**
- In the middle act, introduce a new threat or complication every 2 chapters
- Use the middle to deepen relationships, not just advance plot
- Every middle-act chapter must move at least two of: plot, character, theme, threat
- The middle is where readers decide whether to finish the book

---

## 16. Verification Rule

**Never trust a report that says "fixes applied." Always spot-check the actual source files.**

- Completion reports can claim fixes that were not actually written to the manuscript.
- When a report says "Fixed X in Chapter Y," open the source file and confirm.
- This is especially important for structural fixes (transition paragraphs, thematic seeds, continuity patches) that are small but load-bearing.
