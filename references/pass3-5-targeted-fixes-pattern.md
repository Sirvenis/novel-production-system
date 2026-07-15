# Pass 3.5 Targeted Fixes — Pattern and Workflow

**Context:** Bridge pass between Pass 3 Editorial Review and Pass 4 Reader Audit. Applied when editorial verdict is "NEEDS TARGETED FIXES" (1-4 Priority 1 blockers, fixable in one session).

---

## When to Use

- Pass 3 verdict is NEEDS TARGETED FIXES (not READY, not MAJOR REWRITE)
- Blockers are expansion/polish, not structural rewrites
- Typical blockers: underweight chapters, cadence fatigue, dropped threads, missing reactions

## Workflow

### 1. Read the Editorial Report
- Open `revisions/BOOK<N>_EDITORIAL_REPORT.md`
- Extract ONLY Priority 1 (blockers) — ignore Priority 2-3 for this pass
- Note which chapters need work and what type of work

### 2. Identify Fix Type for Each Blocker

| Blocker Type | Fix Strategy | Verification |
|-------------|-------------|------------|
| **Underweight chapter** (below target + thematically thin) | Read chapter, identify 2-3 expansion targets, weave new material inline | `read_file` tail check + line count |
| **Cadence fatigue** (identical endings across finale) | Vary at least half the endings: action, dialogue, concrete detail, subversion | Read last 5 lines of each affected chapter |
| **Dropped thread** (setup without payoff) | Add payoff scene OR cut the setup if payoff isn't possible | Search for setup reference, verify resolution |
| **Missing character reaction** | Add 1-2 paragraph beat showing reaction | `read_file` changed section |

### 3. Execute Fixes Inline

- **DO NOT create `-revised` copies** — overwrite the draft file directly
- **DO NOT append material** — weave new scenes/dialogue into existing structure
- **Preserve voice** — match the chapter's existing tone and POV
- **Preserve continuity locks** — verify motifs (toothbrush, boots, frequency, etc.) still track

### 4. Verify Each Fix

**Critical:** Do NOT rely on `wc` for markdown word counts. After `write_file` or `patch`, verify with `read_file` (check tail or changed section). `wc` caches stale output.

Verification checklist per fix:
- [ ] `read_file` shows the new material is on disk
- [ ] The chapter ending is present and correct
- [ ] No continuity locks were broken

### 5. Commit Batch

After all fixes in a chapter are applied and verified:
```bash
git add -A && git commit -m "Pass 3.5: [chapter] — [fix description]"
```

### 6. Update Tracker

Change status from "Pass 3 COMPLETE — fixes needed" → "Pass 3.5 COMPLETE — ready for Reader Audit"

Update word count (use manual sum of verified chapter word counts, not `wc` on compiled files).

### 7. Write Handoff

Write `handoff/book<N>-pass3-5-handoff.md` with:
- What was fixed in each chapter
- Before/after word counts
- Remaining concerns (if any)
- Status: ready for Pass 4 Reader Audit

---

## Real-World Example: Book 2 Pass 3.5

**Blockers identified:**
1. Ch 2 underweight (2,784w, target ~4,000w)
2. Ch 17 underweight (2,341w, target ~4,000w)
3. Cadence fatigue: Ch 14-17 all end with poetic aphorisms
4. "Green switch" mentioned twice, never explained
5. Margaret has no visible reaction to Old Bill's death

**Fixes applied:**
- Ch 2: Added Jack Henderson confrontation scene, Klaus hostel beat (Swedish girl), first hum-in-teeth for Lena, grandmother photo → 3,847w
- Ch 17: Added Raj's arrival with data, crew kitchen-table reaction, Lena at mill scene, active ending → 3,456w
- Ch 14 ending: Changed from aphorism to action (crew packing up, walking back through broken cane)
- Ch 15 ending: Changed "Waiting for the water" → "Building strength for the day the water returns"
- Ch 12: Added green switch explanation (safety calibration indicator on Mark III)
- Ch 15: Added Margaret reaction beat (tea tray, "He knew the water better than anyone")

**Verification:** Each fix verified with `read_file` tail checks. `wc` reported stale numbers (e.g., showing 2,784w after Ch 2 had been expanded to 3,847w), confirming the caching pitfall.

**Time:** ~1 session. All blockers resolved.

---

## Anti-Patterns to Avoid

- **Creating `-revised` copies:** Creates file proliferation. Future sessions don't know which file is canonical.
- **Expanding by appending:** New material tacked onto the end disrupts pacing. Weave into existing scenes.
- **Fixing Priority 2-3 during Pass 3.5:** Scope creep. Pass 3.5 is for blockers only. Save nice-to-haves for Pass 5 or skip.
- **Trusting `wc`:** After write_file, always verify with read_file.

---

*Reference: created 2026-07-15 during Book 2 Pass 3.5 execution.*
