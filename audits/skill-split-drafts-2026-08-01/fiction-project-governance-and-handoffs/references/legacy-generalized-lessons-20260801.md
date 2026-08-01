# Legacy Generalized Lessons — fiction-project-governance-and-handoffs

Date: 2026-08-01

This compact linked reference distills cross-series/general items from the old global `longform-fiction-series-drafting` reference archive into task-class guidance for the staged draft skill split.

No live Hermes skills were changed. Series-specific canon remains in canonical series repos; the legacy files remain untouched until a later approved slimming pass.

Source manifest: `/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/REFERENCE_CLASSIFICATION_MANIFEST.csv`
Legacy source directory: `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references`
Processed references in this task domain: 18

## Generalization Rules Used

- Convert reusable procedure into task-class guidance.
- Preserve project names only as provenance; do not treat old examples as current canon.
- Do not include runtime/provider/profile/deployment-sensitive items here; those remain quarantined for manual review.
- Before installing any staged skill live, re-check current repo authority and validate the draft skill package.

## Source Index

| Source file | Title | Hash | Words |
|---|---|---:|---:|
| `author-imprint-and-profile-governance.md` | Author / Imprint / Profile Governance Pattern | `561412edd4e6163c` | 554 |
| `branch-manuscript-assembly-pattern.md` | Assembling a Manuscript from Scattered Branch Files | `f7abefd858717410` | 649 |
| `context-threshold-fiction-handoff.md` | Context-threshold handoff for fiction sessions | `1f1011a23e803f64` | 274 |
| `continuity-preservation-audit-before-next-gate.md` | Continuity Preservation Audit Before Next Gate | `61f414b40a75a901` | 860 |
| `cross-session-github-handoff-repo.md` | Cross-session GitHub handoff repo pattern | `99cb816c49d24814` | 434 |
| `curator-of-series-memory-pattern.md` | Curator of Series Memory — Building Series Ecosystems | `1215a057809fc2ce` | 668 |
| `direct-writer-editor-repo-handoff.md` | Direct writer → editor repo handoff | `255a680ec3abd279` | 407 |
| `fiction-project-clean-pause-and-polish-readiness.md` | Fiction Project Clean Pause + Polish Readiness Pattern | `804a5274ca6d299a` | 716 |
| `fresh-session-pass-expansion-handoff-cycle.md` | Fresh-session Pass expansion handoff cycle | `ba3a9c859243c71f` | 420 |
| `git-audit-before-creative-work.md` | Git Audit and Cleanup Before New Creative Work | `3015ac2e60507488` | 381 |
| `light-continuity-scan-after-reader-pass.md` | Light Continuity Scan After Reader Pass | `c949a15b29d52068` | 374 |
| `model-agnostic-repo-with-caretaker.md` | Model-Agnostic Repository with Caretaker Designation | `905e8af28f2f4678` | 768 |
| `non-destructive-branch-manuscript-audit.md` | Non-Destructive Branch Manuscript Audit | `ac521f7d9a36cf0a` | 404 |
| `project-phase-closure-before-switching.md` | Project Phase Closure Before Switching Projects | `3e47132a94a9e0b2` | 397 |
| `repo-local-worker-handoff-and-assembly-validation.md` | Repo-local worker handoff and assembly validation | `58eec6ffa1c79a48` | 479 |
| `repo-local-writer-handoff-and-editorial-gates.md` | Repo-local writer handoff and editorial gates | `a797186c1be395d7` | 663 |
| `sequential-chapter-drafting-handoff-pattern.md` | Sequential Chapter Drafting + Handoff Pattern | `595faddd25ed86fc` | 371 |
| `structural-reader-audit-and-readiness-report.md` | Structural reader audit and first-draft readiness report | `d08383a35e26e290` | 659 |

## Distilled Operational Lessons

### Author / Imprint / Profile Governance Pattern

Provenance: `author-imprint-and-profile-governance.md` (`561412edd4e6163c`), 554 words.

- Topic: Author / Imprint / Profile Governance Pattern
- Topic: Core rule
- Topic: Layer model
- Cross-project orchestration, repo governance, routing, handoffs, quality gates.
- Assigns bounded work to profiles and verifies repo-local reports before summarising to Andrew.
- Series showrunner profile = series lead

### Assembling a Manuscript from Scattered Branch Files

Provenance: `branch-manuscript-assembly-pattern.md` (`f7abefd858717410`), 649 words.

- Topic: Assembling a Manuscript from Scattered Branch Files
- Topic: When to use
- Topic: 1. Discover what's on the branch (without switching)
- Topic: List all relevant files on the remote branch
- Topic: Check for a complete assembled manuscript already
- Topic: 2. Fetch the branch locally (read-only)

### Context-threshold handoff for fiction sessions

Provenance: `context-threshold-fiction-handoff.md` (`1f1011a23e803f64`), 274 words.

- Topic: Context-threshold handoff for fiction sessions
- A chapter/major planning step was just completed and pushed.
- Stop before another prose step.
- Verify the active repo state: clean/dirty status, latest commit, latest chapter files, and word count if relevant.
- Write a project-local handoff file, preferably under `handoff/CURRENT_SESSION_HANDOFF.md`.
- active project and repo path;

### Continuity Preservation Audit Before Next Gate

Provenance: `continuity-preservation-audit-before-next-gate.md` (`61f414b40a75a901`), 860 words.

- Topic: Continuity Preservation Audit Before Next Gate
- inspect repo files, handoffs, reports, trackers, status, decision logs, validation scripts, manuscript presence/parity;
- create a continuity audit report under `bookN/reports/`;
- make minor documentation synchronization fixes to status/handoff/tracker/decision-log/README;
- package, publish, update reader sites;
- run model experiments or fallback/alternate models;

### Cross-session GitHub handoff repo pattern

Provenance: `cross-session-github-handoff-repo.md` (`99cb816c49d24814`), 434 words.

- Topic: Cross-session GitHub handoff repo pattern
- Topic: Session-derived lesson
- Private GitHub repo: `Sirvenis/scout-handoffs`
- Topic: When to update
- A project-local handoff changes.
- Runtime/model guardrails or next-step gates change.

### Curator of Series Memory — Building Series Ecosystems

Provenance: `curator-of-series-memory-pattern.md` (`1215a057809fc2ce`), 668 words.

- Topic: Curator of Series Memory — Building Series Ecosystems
- Topic: Role Definition
- Topic: The Three-Layer Hierarchy
- Topic: Layer 1: Knowledge Base (Institutional)
- Topic: Layer 2: Series Storycraft (Per-Series)
- Lessons Earned — raw discoveries from the current/recent book, before they've earned promotion

### Direct writer → editor repo handoff

Provenance: `direct-writer-editor-repo-handoff.md` (`255a680ec3abd279`), 407 words.

- Topic: Direct writer → editor repo handoff
- Topic: Problem this prevents
- Topic: Required pattern
- The writer worker runs directly against the project repo/worktree.
- Do not include messaging/Telegram toolsets for repo handoffs.
- Do not send long Kimi production/cleanup reports to Telegram.

### Fiction Project Clean Pause + Polish Readiness Pattern

Provenance: `fiction-project-clean-pause-and-polish-readiness.md` (`804a5274ca6d299a`), 716 words.

- Topic: Fiction Project Clean Pause + Polish Readiness Pattern
- Topic: Core principle
- **ready to return later for copy-edit / formatting / reader pass / canon promotion**
- Topic: 1. Close the current book package first
- Verify word counts and checksums match.
- Write a closure report for that book.

### Fresh-session Pass expansion handoff cycle

Provenance: `fresh-session-pass-expansion-handoff-cycle.md` (`ba3a9c859243c71f`), 420 words.

- Topic: Fresh-session Pass expansion handoff cycle
- Start from a fresh-session handoff for the specific chapter target, not the whole prior conversation.
- Verify live creative runtime before prose/canon work when model purity matters.
- Read only the exact continuity files needed:
- Make targeted edits only in the non-destructive pass workspace, never the preserved first-draft folder.
- Reassemble the pass manuscript immediately after the chapter edit.

### Git Audit and Cleanup Before New Creative Work

Provenance: `git-audit-before-creative-work.md` (`3015ac2e60507488`), 381 words.

- Topic: Git Audit and Cleanup Before New Creative Work
- Topic: The Problem
- Deleted chapter files from old expansion passes
- **Audit the dirty state.**
- Deleted chapter files from old passes → stale
- Unsaved handoff documents → may contain useful notes; archive, don't discard

### Light Continuity Scan After Reader Pass

Provenance: `light-continuity-scan-after-reader-pass.md` (`c949a15b29d52068`), 374 words.

- Topic: Light Continuity Scan After Reader Pass
- A final/near-final manuscript has passed a reader or supporter-pass read.
- Reader found only small continuity/rhythm issues, not structural failure.
- Re-read only the relevant manuscript sections and prior reader/editor reports.
- Do not broaden into a full proofread, line edit, chapter expansion, or structural rewrite.
- If the concern is real but small, archive the judgement as a report and stop unless the user explicitly authorizes edits.

### Model-Agnostic Repository with Caretaker Designation

Provenance: `model-agnostic-repo-with-caretaker.md` (`905e8af28f2f4678`), 768 words.

- Topic: Model-Agnostic Repository with Caretaker Designation
- Topic: When to use
- Topic: The problem this solves
- **Single-model lock-in:** A repo tied to one model (e.g., "Predator = GPT-5.5 only") becomes inaccessible when that model hits usage limits.
- **Scout forks diverging:** Alternative versions live in separate forks (`brambleford-scout-work`) that may become more complete than the canonical repo, but are treated as "non-canonical."
- **Lost editorial history:** Reports, audits, and expansion pass documentation accumulate in worker directories or session logs, never reaching the canonical repo.

### Non-Destructive Branch Manuscript Audit

Provenance: `non-destructive-branch-manuscript-audit.md` (`ac521f7d9a36cf0a`), 404 words.

- Topic: Non-Destructive Branch Manuscript Audit
- Confirm the current repo state first:
- Create a detached inspection worktree outside the repo, preferably under Hermes cache:
- combine split scene files where a chapter is stored as multiple `scene*-draft.md` files
- calculate total manuscript word count from draft text only, excluding plans/status/audits
- read the final chapter tail to verify whether it actually ends

### Project Phase Closure Before Switching Projects

Provenance: `project-phase-closure-before-switching.md` (`3e47132a94a9e0b2`), 397 words.

- Topic: Project Phase Closure Before Switching Projects
- Topic: Principle
- Topic: Closure sequence
- Verify the path, word count, chapter count, and latest commit.
- Check `manuscripts/scout-versions/`, release/export folders, status files, and handoffs.
- Verify checksum identity after copying.

### Repo-local worker handoff and assembly validation

Provenance: `repo-local-worker-handoff-and-assembly-validation.md` (`58eec6ffa1c79a48`), 479 words.

- Topic: Repo-local worker handoff and assembly validation
- Topic: When to use
- Topic: Direct worker → editor handoff
- Write its completion report and validation results into the project repository.
- Commit and push manuscript, tracker, architecture, assembled-manuscript, and report changes.
- Return only a short handoff to the launching Hermes/Scout process: report path, commit hash, validation status, and blocker if any.

### Repo-local writer handoff and editorial gates

Provenance: `repo-local-writer-handoff-and-editorial-gates.md` (`a797186c1be395d7`), 663 words.

- Topic: Repo-local writer handoff and editorial gates
- Topic: Problem solved
- Topic: Durable workflow rule
- Do not use Telegram or user-facing messaging as the worker-report handoff channel.
- The writer worker writes its completion report, validation results, changed-file summary, word counts, commit hash, and next requested decision into the project repository.
- The worker final response is only a short machine-checkable handoff: commit, report path, validation status, blocker if any.

### Sequential Chapter Drafting + Handoff Pattern

Provenance: `sequential-chapter-drafting-handoff-pattern.md` (`595faddd25ed86fc`), 371 words.

- Topic: Sequential Chapter Drafting + Handoff Pattern
- Read the current handoff first.
- Verify git status and latest commit.
- Verify live runtime/model if the project is model-gated.
- Read the immediately prior chapter, its completion note, the drafting tracker, and only the planning files needed for the next chapter.
- Use Python file I/O / `execute_code` for large prose writes; do not use tools known to truncate large manuscript files.

### Structural reader audit and first-draft readiness report

Provenance: `structural-reader-audit-and-readiness-report.md` (`d08383a35e26e290`), 659 words.

- Topic: Structural reader audit and first-draft readiness report
- Topic: When to use
- Topic: Structural reader audit
- **Would I keep turning pages?** Does the evidence chain or plot momentum carry the reader from chapter to chapter? Is there a hook that makes me want to know what happens next?
- **Did the middle sag?** Are there chapters that feel like pure atmosphere without advancing mystery or character? Does every chapter change the reader's understanding?
- **Were clues fair?** Does the reader have access to all key evidence before the confession? Can the reader assemble the case alongside the protagonist?
