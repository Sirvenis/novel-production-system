# Case Study: Book 2 — Revision Decision with Editorial + Reader Review

**Context:** The Last Clean-Up Crew — Book 2: The Deep Root. Pipeline was being established (4 profiles). Chapters 2 and 3 had been drafted before the pipeline was approved.

**The Situation:**

User asked: "Maybe have your editor and reader profiles go over the two chapters and then you can make a recommendation based upon the findings as to whether we discard or keep those two chapters?"

**What Was Done:**

1. **Read Chapter 1** (committed baseline) — to understand voice and what comes before
2. **Read Chapter 2** (draft) — Lena investigates, nobody believes her, network revealed
3. **Read Chapter 3** (draft) — Nate arrives, meets Lena, recognizes new threat
4. **Read Book 2 architecture** — to check alignment with planned structure
5. **Deployed two subagents in parallel:**
   - `horror-series-editor` — structural, continuity, prose cadence review
   - `horror-series-reader` — engagement, pacing, release-readiness verdict

**The Process:**

Both subagents received:
- Full chapter files to read
- Book 2 architecture for structural context
- Chapter 1 as voice baseline
- Specific assessment criteria
- Structured output format requirements

They ran in parallel via `delegate_task` with `tasks` array. Results returned as single consolidated message when both completed.

**The Findings (Both Agreed):**

| Aspect | Editor Verdict | Reader Verdict |
|--------|---------------|----------------|
| Overall | REVISE | NEEDS TARGETED FIXES |
| Discard? | No — voice and horror too good | No — bones are good |
| Priority 1 | 5 structural issues | 3 engagement issues |
| Priority 2 | 4 craft issues | 2 momentum issues |
| What works | 8 specific beats | 6 specific beats |

**Key Priority 1 Issues Identified:**

1. **Jack Henderson's arc broken** — In Ch 1 he admits the cane is wrong, then in Ch 3 he calls Nate because he's scared. This makes him *believing*, not *denying*, which breaks his Ch 10 arc where he refuses treatment.
2. **Margaret too knowing** — "Some things are better left unexplained" shifts horror from cosmic isolation to small-town conspiracy.
3. **Lena knows too much about the Wet** — Quotes Book 1 specifics that a random farmer shouldn't know.
4. **Professor Hartmann email creates dangling thread** — Conflicts with Toby's planned pipeline for German connection.
5. **"Organism is nocturnal" premature** — n=1 observation stated as categorical fact.

**Key Reader Findings:**

1. **Chapter 2 middle is a flatline** — ~1,500 words of water testing + email writing bury the genuinely creepy dusk walk and 10 PM "worship" beat.
2. **Zero humour in Chapter 2** — For a humour-horror series, this is a broken promise.
3. **Lena-Nate meeting too smooth** — Two competent people competently assessing. Needs friction or spark.
4. **Chapter 3 ends on logistics** — Crew assembly is fine but not a cliffhanger. Needs raised stakes.

**The Recommendation:**

**REVISE — do not discard.**

The chapters are not fundamentally flawed. The prose, voices, and horror beats are solid. The problems are editorial (structural alignment, momentum, engagement) not creative (voice, concept, character).

**Next Steps:**

1. Apply all 5 Priority 1 structural fixes
2. Apply Priority 2 momentum and engagement fixes
3. Commit revised versions
4. Then proceed with Chapter 4

**What Would Have Happened Without Review:**

If the chapters had been committed as-is and drafting continued, the Jack Henderson arc would have been permanently broken, making Chapter 10 impossible to write. The email to Professor Hartmann would have created a dangling thread that either needed awkward retconning or would have been forgotten. The reader would have experienced Chapter 2 as a slog and potentially abandoned the book.

**Verification of Review Quality:**

Both profiles found the same core problems independently (Jack's arc, Margaret's knowingness, Lena's Wet knowledge). The reader found engagement issues the editor didn't flag, and the editor found structural issues the reader didn't catch. This demonstrates the value of running both reviews in parallel.

**Files:**
- `book2-drafts/chapter-02.md` — Chapter 2 draft
- `book2-drafts/chapter-03.md` — Chapter 3 draft
- `book2-drafts/editorial-report-ch02-ch03.md` — Full editorial report
- `book2-drafts/reader-audit-ch02-ch03.md` — Full reader audit
- `handoff/book2-session-comprehensive-handoff.md` — Session handoff with all findings

**Key Lesson:**

When early chapters exist before the pipeline is established, treat them as provisional. Deploy editor and reader profiles before deciding their fate. The user's "discard or keep?" question is a request for data-driven decision-making, not a guess. Both profiles must review, findings must be synthesized, and the recommendation must cite specific evidence from both reports.
