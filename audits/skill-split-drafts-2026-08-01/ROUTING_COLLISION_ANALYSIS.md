# Routing Collision Analysis — Live Coexistence Canary

**Date**: 2026-08-01  
**Phase**: Live Coexistence Canary — Fiction Profile Only  
**Scope**: Compare trigger boundaries of new split skills vs old live skill

---

## Skill Descriptions and Trigger Boundaries

### NEW SKILLS (installed in fiction profile)

| Skill | Description | When to Use (Trigger) |
|-------|-------------|----------------------|
| **longform-fiction-production** (router) | Lean router for longform fiction work | "Use when the user asks for fiction work and the current stage is unclear, or when resuming a novel project before deciding whether the task is architecture, drafting, audit, revision, assembly, packaging, or model experiment." |
| **fiction-project-governance-and-handoffs** | Maintain fiction project continuity and repository authority | "New session/resumption for a fiction project. User asks whether work is preserved, canonical, pushed, or resumable. Migrating/splitting series repos or repairing authority documents. Updating PROJECT_STATUS.yml, handoff, tracker, decision log, completion notes, or closure reports. Preparing a repo for background/showrunner profile work." |
| **fiction-architecture-briefing-and-research-gates** | Control pre-prose creative planning | "User says 'review and refine this request'. Creating or revising a book/series architecture. Building a chapter-function map or tracker. Writing a controlled chapter brief. Running research-only mythology/history/market/technical realism dossiers. Deciding what can enter canon from research." |
| **controlled-fiction-drafting-and-autonomous-runs** | Draft fiction only after approval gates | "User approves one chapter from a prepared brief. User approves a bounded multi-chapter pilot. A showrunner launches or verifies a writer profile canary. Autonomous run needs repo-local reports, commits, and stop gates. Resuming interrupted drafting where the next chapter is clearly authorized." |
| **fiction-editorial-audits-and-revision-planning** | Separate inventory, judgement, and planning from prose changes | "A draft/pass is complete and needs read-only assessment. User authorizes audit but not prose changes. External/reader/steward feedback must be archived and interpreted. Need Discovery Pass inventory before editorial judgement. Need continuity, timeline, motif, voice, or tic detection. Need a targeted revision plan before edits." |
| **controlled-fiction-revision-and-expansion** | Execute approved prose-changing passes safely | "User approves a specific revision plan. A chapter or set of chapters needs targeted expansion/deepening. Dialogue desert or monologue-dominant scenes require dramatization. Late-stage cadence/consistency/micro-polish is authorized. Interrupted revision pass must be resumed without corrupting uncommitted work." |
| **fiction-assembly-final-qa-and-freeze** | Handle final mechanical manuscript operations | "Assembling chapters into a full manuscript. Creating baseline/checkpoint before reader audit. Final QA after revision/line/copy/proofread. Preparing release candidates/exports. Freezing a book or closing a project phase." |
| **reader-package-and-feedback-workflow** | Prepare reader-facing packages and feedback workflows | "Building a family/beta/supporter reader package. Creating or updating feedback forms. Generating static reader-site files from manuscripts. Archiving reader feedback into the canonical repo. Checking free/locked library packaging rules." |
| **controlled-model-evaluation-for-creative-work** | Govern controlled creative model experiments | "User approves a blind or multi-model prose experiment. Comparing model outputs for creative quality. Running reader/editor/showrunner evaluations without identity leakage. Promoting an approved experiment candidate to canonical manuscript." |

### OLD LIVE SKILL (global, unchanged)

| Skill | Description | When to Use (Trigger) |
|-------|-------------|----------------------|
| **longform-fiction-series-drafting** | Draft, revise, review, and hand off longform fiction series | "Use for novel/series drafting, chapter continuation, manuscript revision/review, packets, trackers, completion notes, and handoffs." |

---

## Identified Routing Collisions

### 1. OVERLAPPING TRIGGER LANGUAGE

**Old skill trigger**: "novel/series drafting, chapter continuation, manuscript revision/review, packets, trackers, completion notes, and handoffs"

**This directly overlaps with ALL new task skills**:

| Old Skill Phrase | Overlaps With New Skill |
|-----------------|------------------------|
| "novel/series drafting" | controlled-fiction-drafting-and-autonomous-runs |
| "chapter continuation" | controlled-fiction-drafting-and-autonomous-runs |
| "manuscript revision/review" | controlled-fiction-revision-and-expansion, fiction-editorial-audits-and-revision-planning |
| "packets, trackers, completion notes" | fiction-project-governance-and-handoffs |
| "handoffs" | fiction-project-governance-and-handoffs |

**Additionally**, the old skill's body contains explicit references to:
- Architecture/briefing → fiction-architecture-briefing-and-research-gates
- Reader packages → reader-package-and-feedback-workflow
- Model experiments → controlled-model-evaluation-for-creative-work
- Assembly/QA → fiction-assembly-final-qa-and-freeze

### 2. AMBIGUOUS OWNERSHIP

**Requests that could match BOTH old and new skills**:

| Request | Could Match Old Skill | Could Match New Skill(s) |
|---------|----------------------|-------------------------|
| "Continue drafting my novel" | ✓ (chapter continuation) | ✓ (controlled-fiction-drafting-and-autonomous-runs) |
| "Review this manuscript" | ✓ (manuscript revision/review) | ✓ (fiction-editorial-audits-and-revision-planning) |
| "Revise chapter 5" | ✓ (manuscript revision) | ✓ (controlled-fiction-revision-and-expansion) |
| "Update my tracker/handoff" | ✓ (trackers, completion notes, handoffs) | ✓ (fiction-project-governance-and-handoffs) |
| "Create a chapter brief" | ✓ (implied in drafting) | ✓ (fiction-architecture-briefing-and-research-gates) |
| "Assemble the manuscript" | ✓ (implied in handoffs) | ✓ (fiction-assembly-final-qa-and-freeze) |
| "Build a reader package" | ✓ (implied in series work) | ✓ (reader-package-and-feedback-workflow) |
| "Run a model experiment" | ✓ (referenced in body) | ✓ (controlled-model-evaluation-for-creative-work) |

### 3. RECURSIVE DELEGATION RISKS

**Risk**: The old skill contains explicit delegation patterns that could bypass the new router:

From old skill body:
- "When Andrew approves an audit verdict... use `references/first-draft-map-tracker-before-autonomous-pilot.md`"
- "When Andrew authorises only a baseline/checkpoint... use `references/baseline-checkpoint-before-reader-audit.md`"
- "For the model-separation editorial pipeline... see `references/model-separation-editorial-pipeline.md`"
- "When the fiction catalogue grows... use `references/author-imprint-and-profile-governance.md`"

These reference-based delegations in the old skill could route to specific workflows WITHOUT going through the new `longform-fiction-production` router, creating a parallel routing path.

### 4. SITUATIONS WHERE NO SKILL CLEARLY OWNS THE REQUEST

**Gap scenarios** (may fall through cracks):

| Request | Old Skill Match? | New Router Match? | New Task Skill Match? |
|---------|-----------------|-------------------|----------------------|
| "Set up a new fiction project workspace" | Partial (workspace-population-template.md in body) | Partial (router expects existing project) | None explicitly |
| "Check if my manuscript is canonical" | Partial (SOURCE_OF_TRUTH in body) | ✓ (router: governance) | ✓ (governance skill) |
| "Migrate my series to a new repo" | Partial (repository authority in body) | ✓ (router: governance) | ✓ (governance skill) |
| General fiction question without specific phase | ✓ (broad trigger) | ✓ (router: unclear stage) | None (requires routing) |

### 5. OLD SKILL BYPASSING NEW TASK-SPECIFIC ROUTING

**Mechanism**: The old skill's body contains 250+ specific reference files with explicit "when X, use reference Y" patterns. These are essentially hardcoded routing rules that operate at the PROCEDURE level, not the skill-selection level.

**Example**: User asks "draft Chapter 11 with special brief" → Old skill matches "controlled chapter drafting" → Uses `anunnaki-book4-controlled-ch11-prose-after-special-brief.md` directly, NEVER invokes `controlled-fiction-drafting-and-autonomous-runs` skill.

**Result**: The old skill acts as a self-contained routing-and-execution engine. The new router only gets invoked if the user explicitly loads `longform-fiction-production` OR if the old skill is not loaded.

### 6. ORCHESTRATOR ROUTING DETERMINISM

**Current state**: 
- Old skill is GLOBAL (`~/.hermes/skills/creative/longform-fiction-series-drafting/`)
- New skills are LOCAL to fiction profile (`~/.hermes/profiles/fiction/skills/creative/`)

**Hermes skill loading priority**: Local profile skills typically override global skills with same name, but these have DIFFERENT names.

**Routing behavior**: 
- If both old and new skills are available, the agent must choose based on trigger matching
- Old skill trigger is extremely broad ("novel/series drafting...") — matches almost any fiction request
- New router trigger is narrower ("when stage is unclear...") — but could match the same requests
- New task skills have specific triggers that ALSO match the same requests as old skill

**Determinism**: LOW. Multiple skills can legitimately claim the same request. The agent's choice depends on:
1. Skill description similarity scoring
2. Order of skill loading
3. Model's interpretation of "best match"

---

## Collision Summary Table

| Collision Type | Severity | Count | Mitigation in This Phase |
|----------------|----------|-------|--------------------------|
| Direct trigger overlap | HIGH | 9/9 new skills overlap with old | Document only; old skill preserved |
| Ambiguous ownership | HIGH | ~8 common request patterns | Document; test in canary |
| Recursive delegation bypass | MEDIUM | Multiple reference-based routes | Document; old skill unchanged |
| No clear owner (gaps) | LOW | ~4 request types | Document; may need catch-all |
| Old skill bypasses new routing | HIGH | Old skill is self-contained execution engine | **Critical finding** |
| Orchestrator determinism | MEDIUM | Non-deterministic with both loaded | Test in canary |

---

## Critical Finding: Old Skill Is a Parallel Execution Engine

The old `longform-fiction-series-drafting` skill is NOT just a procedural skill — it contains:
- 252 reference files with explicit "when X, do Y using reference Z" patterns
- Hardcoded project-specific workflows (Anunnaki Book 4, Meridian Book 3, Brambleford, etc.)
- Model/runtime gating rules embedded in references
- Deployment, reader-site, cron, and profile maintenance procedures

**It functions as a complete fiction production operating system within a single skill.**

The new split skills are designed to REPLACE this by separating concerns, but as long as the old skill remains available and enabled (in series profiles), it will:
1. Match most fiction requests first (broader trigger)
2. Execute its own internal routing via reference files
3. Never delegate to the new task skills
4. Create a dual-system where behavior depends on which skill the agent happens to load

---

## Recommendation for This Phase

**Do NOT correct collisions** — this phase is for detection only. The collisions are EXPECTED because:
- The old skill was designed as a monolithic umbrella
- The new skills are designed to decompose it
- Coexistence inherently creates overlap

**The canary test will reveal**:
1. Which skill the agent actually loads for each scenario
2. Whether duplicate activation occurs
3. Whether the old skill bypasses new routing in practice
4. Whether any requests fall through cracks

**The slimming phase (later, if approved) must address**:
1. Either disable old skill in fiction profile, or
2. Slim old skill to ONLY series-specific case studies (not procedures), or
3. Make old skill explicitly delegate to new router

But for NOW: document collisions, run canary, report findings.