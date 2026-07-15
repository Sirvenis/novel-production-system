# Pipeline Evolution — Stage-by-Stage History

## How the System Grew

This document tracks the addition, modification, and removal of pipeline stages across the three-book production cycle.

---

## Pre-Book 1: The Naive Pipeline

```
Draft → Review → Done
```

**Stages:** 2
**Profiles:** 1 (default)
**Tracking:** None
**Handoffs:** None
**Result:** Complete manuscript with structural gaps, prose issues, and pacing problems discovered too late.

---

## Book 1: The 4-Pass System

```
Draft → Editorial → Reader Audit → Assembly
```

**Stages:** 4
**Profiles:** 2 (Showrunner, combined Writer/Editor)
**New additions:**
- Architecture document (basic)
- Tracker (simple list)
- Reader Audit (fresh-eye read)
- Series Bible (for cross-book continuity)

**What worked:**
- Architecture prevented worst wandering
- Reader Audit caught problems writer couldn't see
- Individual chapter files made revision easier

**What failed:**
- Editorial too gentle (said "good" when gaps existed)
- No Discovery Pass (editor assumed draft contained things it didn't)
- No expansion pass (lean chapters stayed lean)
- No Line/Copy Edit (prose issues accumulated)
- No handoff system ("where did we leave off?")
- No decision log ("why did we do that?")

**Key discovery:** The middle act sags. Chapters 6-9 dragged because they only advanced plot, not character/theme/threat.

---

## Book 1 → Book 2: Adding Discipline

```
Architecture → Draft → Discovery Pass → Expansion →
Editorial → Fixes → Reader Audit → Assembly
```

**Stages:** 8 (counting Discovery Pass and Fixes as separate)
**Profiles:** 3 (Showrunner, Writer, Editor)
**New additions:**
- Job Statements (what each chapter must make the reader believe)
- Discovery Pass (pure inventory)
- Tier-Based Expansion Priority
- Targeted Fixes (Pass 3.5, surgical only)
- Handoff system (`handoff/MASTER-HANDOFF.md`)
- Decision Log (`tracking/BOOK[N]_DECISIONS.md`)
- Character Bible (`CHARACTER_BIBLE.md`)
- Autonomy grant for continuous drafting

**What worked:**
- Discovery Pass prevented editorial assumptions
- Tier-Based Expansion prioritised effectively
- Handoff system eliminated session-start confusion
- Decision Log prevented repeated questions
- Autonomy tripled drafting velocity

**What failed:**
- Chapter architecture conflation (Chapter 4 stole beats from 5-6)
- Scope creep (secondary frontier tried to become primary)
- Word count shrinkage invisible at draft stage
- Reader contamination (saw editorial reports)
- Still no Line Edit or Copy Edit

**Key discovery:** Autonomy requires explicit constraints. Without them, it's chaos.

---

## Book 2: The Refinement Phase

During Book 2 production, several refinements were added mid-stream:

**Added mid-Book 2:**
- Scope Discipline rules (single frontier per book)
- Architecture alignment check (editor must verify each chapter stays within mandate)
- Reader isolation (Reader must NOT see editorial reports)

**Discovered during Book 2 revision:**
- Report drift (fixes claimed but not written to source)
- The Verification Rule: always check source files

---

## Book 2 → Book 3: The 9-Stage System

```
Architecture → Draft → Discovery Pass → Expansion →
Developmental Editorial → Targeted Fixes → Line Edit →
Copy Edit → Assembly → Final QA → Reader Audit → Freeze
```

**Stages:** 9 (plus Reader Audit and Freeze)
**Profiles:** 4 (Showrunner, Writer, Editor, Reader)
**New additions:**
- Line Edit (Stage 6): prose rhythm, voice, repetition
- Copy Edit (Stage 7): mechanical correctness
- Final QA (Stage 9): comprehensive checklist
- Reader Audit classification framework (MUST/INVESTIGATE/SHOULD/COULD/NOT)
- Verification Rule (codified)
- Thread-Continuity Gap Detection
- Cadence Fatigue Detection
- Word Count Shrinkage Detection
- Comprehensive handoff pattern (for context compression)
- SOUL.md constraint system (role-specific rules)

**What worked:**
- Full 9-stage pipeline executed cleanly
- Line Edit caught repetition and cadence issues
- Copy Edit caught mechanical errors (only 3 fixes needed)
- Reader Audit classification refined prioritisation
- Verification Rule caught every instance of report drift
- Thread-continuity detection found a zero-mention chapter
- Cadence detection improved ending variety

**What failed:**
- Word count shrinkage accelerated (33k for Book 3 vs. 42k for Book 2)
- Seductive entity harder to maintain than aggressive entities
- Some copy-edit scope creep (caught early, corrected)

**Key discovery:** Each entity should target a different human weakness. The horror is deepest when the compulsion feels like something the victim genuinely wants.

---

## Post-Book 3: Systematisation

**Current state:**
- All stages defined with inputs, outputs, and verdicts
- All profiles defined with SOUL.md constraints
- All templates created
- All case studies documented
- All failure patterns captured
- All seven non-negotiable rules codified

**This repository** is the preservation of that systematisation.

---

## Stage Addition Timeline

| Stage | Added When | Why It Was Added |
|-------|-----------|------------------|
| Architecture | Pre-Book 1 | Wandering narrative needed blueprint |
| Drafting | Pre-Book 1 | Core production |
| Discovery Pass | Book 1→2 | Editor assumed draft contained things it didn't |
| Expansion | Book 1→2 | Lean chapters stayed lean; needed prioritisation |
| Developmental Editorial | Pre-Book 1 (but weak) | Structural assessment |
| Targeted Fixes (3.5) | Book 1→2 | Prevented scope creep during revision |
| Line Edit | Book 2→3 | Prose issues accumulated; needed dedicated stage |
| Copy Edit | Book 2→3 | Mechanical errors needed systematic review |
| Assembly | Pre-Book 1 | Compile individual chapters |
| Final QA | Book 2→3 | Verification checklist before freeze |
| Reader Audit | Book 1 | Fresh-eye read; classification added Book 2→3 |
| Freeze | Book 1 | Lock the manuscript |

---

## Profile Addition Timeline

| Profile | Added When | Why It Was Added |
|---------|-----------|------------------|
| Showrunner (Master) | Pre-Book 1 | Coordinate production |
| Writer | Book 1→2 | Separate drafting from editing for voice consistency |
| Editor | Book 1→2 | Ruthless structural assessment |
| Reader | Book 1 (but contaminated) | Fresh-eye experiential read; isolated Book 2→3 |
| Researcher | Not used | Reserved for future projects needing heavy research |

---

## Rules Added by Book

| Rule | Added | Book | Why |
|------|-------|------|-----|
| Job Statement | Architecture | 1 | Prevent wandering |
| Word ranges job-based | Architecture | 2 | Prevent padding/rushing |
| Discovery Pass | Pre-editorial | 2 | Prevent editorial assumptions |
| Tier-Based Expansion | Expansion | 2 | Prioritise effectively |
| Targeted Fixes (surgical) | Post-editorial | 2 | Prevent scope creep |
| Verification Rule | Post-fixes | 2 | Prevent report drift |
| Line Edit | Stage 6 | 3 | Prose rhythm |
| Copy Edit | Stage 7 | 3 | Mechanical correctness |
| Reader Classification | Reader Audit | 3 | Refine prioritisation |
| Thread-Continuity Detection | QA | 3 | Find dropped threads |
| Cadence Fatigue Detection | Line Edit | 3 | Prevent predictable endings |
| Shrinkage Detection | Discovery Pass | 3 | Flag shortening trends |
| Scope Discipline | Architecture | 2 | Prevent parallel frontiers |
| Handoff before report | Workflow | 2 | Prevent stale state |
| Autonomy constraints | Workflow | 2 | Prevent chaos |

---

## What the Next Project Gets

The next project using this system gets:
- All 9 stages defined and documented
- All 4 profiles configured
- All templates ready to copy
- All failure patterns known in advance
- All detection methods (shrinkage, cadence, continuity) built-in
- All non-negotiable rules codified

**The next project does NOT have to discover these things the hard way.**
