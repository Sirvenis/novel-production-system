# Pre-Pipeline Revision Execution Pattern

**Context:** The Last Clean-Up Crew — Book 2: The Deep Root. Pipeline was being established (4 profiles). Chapters 2 and 3 had been drafted before the pipeline was approved. Editor and reader both returned REVISE verdicts.

**The Situation:**

After deploying `horror-series-editor` and `horror-series-reader` profiles to review Chapters 2–3, both returned "REVISE — do not discard." The user explicitly said "(A) proceed with this revision plan, revise in-place."

**What Was Done:**

1. **Read all current drafts** — Chapters 1, 2, and 3, plus the architecture, plus both review reports, plus the handoff
2. **Composed revised Chapter 1** — Made Jack a denialist who dismisses Lena's data ("Queensland cane doesn't read German textbooks"). Removed Jack's admission that the cane is wrong. The "Not fear. Hope" beat became Lena's observation of Jack's *refusal* to see, not his acceptance.
3. **Composed revised Chapter 2** — Five structural fixes applied simultaneously:
   - Margaret became **kindly dismissive** (offered tea, suggested electrolytes, compared Lena to a previous backpacker who thought banana trees talked) instead of cryptic/conspiratorial
   - **Cut Professor Hartmann email scene entirely** — Lena writes a draft, realizes it sounds insane, closes laptop unsent
   - **Added humour** — Klaus asks if the professor romance; Lena deadpans about his beard
   - **Fixed nocturnal conclusion** — "Hypothesis: nocturnal activity cycle. Requires multiple observations for confirmation. n=1."
   - **Set up Margaret as caller** — New closing scene: Margaret dials Nate at 6:30 AM, explains Lena isn't the panicky type, Jack doesn't know she called
4. **Composed revised Chapter 3** — Six structural fixes applied:
   - **Margaret calls, not Jack** — Opens with Margaret's phone call; Jack is hostile when Nate arrives ("Don't touch my crop")
   - **Lena knows only vague pub rumors** — "Something happened in Innisfail. The farmers talk about it in the pub... The Mitchells' farm — people say it was destroyed"
   - **Lena-Nate meeting has friction** — Lena opens aggressively: "If you are here to tell me it is a good season, save your breath"; challenges his credentials before softening
   - **Cane moves when unwatched** — Nate places stalk on tray, turns away, leaves reorient toward him; shared horror moment
   - **Raised stakes ending** — The cane does its "worship" gesture at **dusk**, not 10 PM. It broke its own rule. "Either it doesn't care if we see it anymore, or it's in a hurry. Neither option is good."
   - **Cut "cosmic pest"** — Nate says "something that doesn't belong here. Something old and patient and hungry."
5. **Ran second editorial + reader review** — Deployed both profiles again to verify fixes and catch new problems

**Key Execution Principles:**

### Revise In-Place, Not Side-by-Side

The user explicitly chose in-place revision (overwrite `chapter-02.md`, not create `chapter-02-revised.md`). This keeps the repo clean and prevents the confusion of "which is the canonical version?"

When the user doesn't specify, ask: "Should I revise in-place or save revised versions alongside?"

### Fix Structure Before Voice

Apply Priority 1 structural fixes (arc-breaking continuity errors) before Priority 2 voice/pacing fixes. A chapter with perfect prose but a broken Jack arc is useless. A chapter with clunky prose but a correct Jack arc can be polished later.

In this session, all 5 Priority 1 structural fixes were applied before any Priority 2 considerations.

### Preserve What Works

Both the editor and reader identified specific beats that must be preserved. Before rewriting, list them:

- Lena's voice: "I am documenting something that does not fit current agricultural theory"
- Canal junction fungal structure: "connected to the channel by something that looked like roots. Or veins. Or the nervous system of something that has no business being on Earth"
- Nate's opening: "Some days, it's rats. Or cockroaches. Or the occasional carpet python that turns out to be a piece of garden hose"
- Maya's fear: "I'm scared that the person I love only exists when the world is ending"
- Lena's closing: "It is wearing cane like a costume, and I want to know what is underneath"
- Frequency comparison: "The Wet was higher. Faster. This is lower. Slower. More patient"

When composing revisions, consciously weave these preserved beats back into the new structure. Do not assume they'll survive by accident.

### Track Fixes Against the Report

Use a todo list to track each fix. Do not rely on memory. The revision pass is complex enough that items will be missed without explicit tracking.

Example todo structure:
- Ch1: Jack denialist fix
- Ch1: "Not fear. Hope" reinterpretation
- Ch2: Margaret dismissive not cryptic
- Ch2: Cut email scene
- Ch2: Add humour beat
- Ch2: Nocturnal hypothesis not conclusion
- Ch2: Margaret calls Nate closing
- Ch3: Margaret calls not Jack
- Ch3: Lena vague rumors only
- Ch3: Lena-Nate friction
- Ch3: Cane moves unwatched
- Ch3: Raised stakes ending

### Verify with Second Review

After applying fixes, always run a second editorial + reader review. The first review found problems in the original draft. The second review verifies:
- Did the fixes actually fix the problems?
- Did the fixes introduce new problems?
- Is the chapter now release-ready?

**Never skip the second review.** The most common failure mode is: review → revise → immediately proceed to next chapter → discover in later review that the fixes were partial or wrong.

### Timeline Fix Pattern

When a character's timeline is inconsistent (Nate says "back tomorrow" but stays), fix it at the **earliest mention**. If Nate writes a note saying "back tomorrow night," change the note. Do not add retroactive explanations later. The reader experiences the text linearly — the first mention sets their expectation.

In this session, Nate's note became "Staying overnight. Call you tonight." No ambiguity.

### Terminology Softening

When a character uses on-the-nose terminology that belongs to another character's vocabulary ("cosmic pest" is Dr. Thorne's language, not Nate's), replace with the character's own grounded phrasing.

Nate: "something that doesn't belong here. Something old and patient and hungry."
Dr. Thorne (later, when he arrives): "A botanical cosmic pest of extraordinary sophistication!"

This preserves each character's distinct voice while still conveying the concept.

---

## POV Discipline During Revision

When revising a chapter that has already established a POV contract (e.g., first-person Lena throughout Chapter 2), **never add a new POV section to serve exposition** — even if that exposition is emotionally rich.

**What happened in this session:**

The revision of Chapter 2 added a Margaret close-third POV closing scene (Margaret dials Nate, explains Jack's denial, reflects on the crop). It was beautifully written and architecturally useful — but it broke the chapter's first-person contract with the reader. The editor flagged it as a **structural violation**.

**How to fix without losing the beat:**

- **Option A (preferred):** Keep the POV pure. Move the Margaret call beat to the *next* chapter's opening (where Nate's third-person is already established), or have Lena *discover* that Margaret called Nate when Nate arrives and mentions it.
- **Option B:** If multi-POV chapters are architecturally intended, clearly demarcate the break with `---` and a subheading. But this must be a series-wide decision, not a one-off convenience.

**Rule:** POV is a contract with the reader. Once signed, it cannot be renegotiated mid-chapter without clear signal.

---

## Prose-Level Tic Detection (Second-Review Quality Gate)

After structural fixes are applied, a second editorial review often reveals prose-level tics that intensified rather than resolved. Treat these as a **quality gate** before the chapter is declared done.

**Common tics to grep for after revision:**

| Pattern | Why It Intensifies | Fix |
|---------|---------------------|-----|
| "Pulse/pulsing/pulses" | You're writing about a rhythmic threat; the word becomes a crutch | Vary: *thrummed, beat, throb, rhythm, oscillation, vibration, hum* |
| "I tell myself" | Self-rationalization is a valid motif but repeats mechanically | Vary: *I decide, I insist, I formulate a working theory, I count to ten* |
| "I do not run" | Character's coping mechanism becomes a refrain | Vary the action: *I count steps, I walk quickly, my legs refuse to cooperate* |
| "I do not sleep" | Insomnia motif becomes heavy through repetition | Vary: *Sleep does not come, I lie awake, the darkness is longer than the night* |
| Identical line echoes | e.g., "It is not innocent" in Ch 1 and Ch 2 | Either earn it as a deliberate motif (vary slightly: *"It is not innocent. It has never been innocent."*) or cut the echo |
| Duplicate lines / copy-paste survivors | Chapter assembled from multiple revision passes | Search for duplicate action descriptions (e.g., "Lena gets in the passenger side" appearing twice 25 lines apart) |

**Verification:** After revision, run a `grep` pass on the chapter for the top 3 most frequent non-dialogue phrases. If any appears more than twice, flag for variation.

---

## Humour Injection During Revision (Not Just Drafting)

When a chapter is flagged as "zero humour" or "humour underweight," the fix is often not rewriting the whole chapter but adding **one precise comic beat** that breaks tension without breaking tone.

**Two effective insertion points:**

### 1. The Competence Shield (Lena)

Lena's German scientific detachment is her comedy engine. Insert a deadpan exchange where her rationality collides with someone else's irrationality.

**Example:**
> Klaus: "Is it a romance?"
> Lena: "He is sixty-three and has a beard like a neglected garden. It is not a romance."

**Rule:** The joke must come from Lena's refusal to be anything other than literal. She doesn't *try* to be funny — she tries to be accurate, and the accuracy is funny.

### 2. The Customer-Service Voice (Nate)

Nate's comedy comes from the gap between his mundane professional persona and the impossible thing he's actually dealing with. Insert a moment where he deploys his "nervous homeowner" voice on a cosmic horror.

**Example:**
> "So you've got a... cane problem? Normally I do rats. Termites. The occasional carpet python that turns out to be a garden hose. But I'm flexible."

**Rule:** The humour must escalate the scene, not deflate it. After the joke, the horror must immediately resume — and feel *worse* because the joke made us relax.

---

## The "Moves When Unwatched" Horror Staging

A specific visual horror beat that works across threat types: the observed object behaves normally, but when the observer turns away and looks back, it has changed.

**Staging recipe:**
1. Character places object in a fixed position (stalk on tray, photograph on desk, sample on bench)
2. Character turns away to do something mundane (get clipboard, check phone, write a note)
3. Character turns back — object has reoriented toward them
4. No one else was present. No wind. No vibration. No explanation.

**Why it works:** It violates the safety of "I saw it, therefore I understand it." The observer's turning away creates a gap in certainty, and the object fills that gap with predatory attention.

**In this session:** Nate places a cane stalk on the tray, turns to get his clipboard, turns back — the leaves have reoriented toward the cab. Lena's whispered confirmation *"It moves when nobody's looking"* is the payoff.

---

## Raised Stakes Ending Pattern: Rule-Breaking

When a supernatural entity has established a behavioral rule (e.g., "it only moves at night"), the most effective way to raise stakes at chapter end is to have it **break its own rule in front of witnesses**.

**Why this works:**
- It shows the entity is accelerating / adapting / no longer hiding
- It removes the safety of "we know its pattern"
- It creates a choice: *it doesn't care if we see it, or it's in a hurry*
- Neither choice is good for the protagonists

**In this session:** The cane's "worship" gesture was established as nocturnal (10 PM). In Chapter 3's closing, it happens at **dusk** — still light, still visible. The final line: *"Which means either it doesn't care if we see it anymore, or it's in a hurry. Neither option is good."*

**Variations for future use:**
- Entity that only converts animals → converts a plant while watched
- Entity that avoids water → appears in a rain puddle
- Entity that needs darkness → manifests under fluorescent lights

---

## Humanising the Competent Protagonist (Lena Pattern)

When a scientist protagonist is flagged as "spreadsheet with a backpack" or "90% scientist, 10% tired," the fix is a **non-plot memory** that reveals what they care about outside the anomaly.

**Requirements:**
- Must not be about the current threat
- Must connect to their expertise (so it feels organic, not shoehorned)
- Must carry emotional weight (loss, love, regret, homesickness)
- Must be brief — 3-5 sentences max

**In this session:** Lena looks at her phone's home screen — a photograph of her grandmother's rose garden in Stuttgart. The grandmother grew roses for fifty years, knew every plant by habit. She died last spring, two weeks before Lena bought her ticket. Lena never told her she was leaving. *"I told myself there would be time. There was not time."*

**Why it works:** It connects Lena's scientific plant knowledge to an emotional inheritance. It explains why she *must* understand the cane — because understanding plants is how she honors her grandmother. And it gives the reader something to worry about losing.

---

## Verification Checklist for Pre-Pipeline Revisions

Before declaring a revision pass complete, verify:

| Check | Method |
|-------|--------|
| All Priority 1 fixes applied | Read revised chapter, grep for old problem text |
| Preserved beats still present | Spot-check specific lines identified in first review |
| No new continuity errors introduced | Read revised chapter against architecture |
| Voice consistency maintained | Read 3 paragraphs from beginning, middle, end |
| Timeline consistent | Check all time references in revised chapters |
| Second review completed | Deploy editor + reader profiles, read their reports |
| Tracker updated | Update `BOOK<N>_TRACKER.md` with revised status |

---

## Files

- `book2-drafts/chapter-02.md` — Revised Chapter 2
- `book2-drafts/chapter-03.md` — Revised Chapter 3
- `book2-drafts/editorial-report-ch02-ch03-revised.md` — Second editorial report (post-revision)
- `book2-drafts/reader-audit-ch02-ch03-revised.md` — Second reader audit (post-revision)
- `handoff/book2-session-comprehensive-handoff.md` — Session handoff with revision state

---

**Key Lesson:**

A "REVISE — do not discard" verdict is not a license to continue drafting. It is a mandate to stop, fix, verify, and only then proceed. The pipeline exists to enforce this discipline. When chapters exist before the pipeline, the agent must enforce it manually.

**Reference: created 2026-07-15 during Book 2 revision session.**
