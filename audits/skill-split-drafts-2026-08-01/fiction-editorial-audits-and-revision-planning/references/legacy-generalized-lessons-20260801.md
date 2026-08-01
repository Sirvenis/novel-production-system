# Legacy Generalized Lessons — fiction-editorial-audits-and-revision-planning

Date: 2026-08-01

This compact linked reference distills cross-series/general items from the old global `longform-fiction-series-drafting` reference archive into task-class guidance for the staged draft skill split.

No live Hermes skills were changed. Series-specific canon remains in canonical series repos; the legacy files remain untouched until a later approved slimming pass.

Source manifest: `/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/REFERENCE_CLASSIFICATION_MANIFEST.csv`
Legacy source directory: `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references`
Processed references in this task domain: 26

## Generalization Rules Used

- Convert reusable procedure into task-class guidance.
- Preserve project names only as provenance; do not treat old examples as current canon.
- Do not include runtime/provider/profile/deployment-sensitive items here; those remain quarantined for manual review.
- Before installing any staged skill live, re-check current repo authority and validate the draft skill package.

## Source Index

| Source file | Title | Hash | Words |
|---|---|---:|---:|
| `baseline-checkpoint-before-reader-audit.md` | Baseline Checkpoint Before Reader/Editorial Audit | `32aedcef29183487` | 466 |
| `book-directory-editorial-history-pattern.md` | Book Directory Editorial History Pattern | `69bdcd87b5ef7231` | 396 |
| `book3-pass16-external-editorial-validation.md` | Book 3 Pass 1.6 External Editorial Validation Pattern | `1efb84129f0bd767` | 385 |
| `controlled-pass1-revision-from-review-package.md` | Controlled Pass 1 Revision from an Editorial Review Package | `fd33e515ca760fd5` | 523 |
| `dialogue-desert-detection-and-dramatization-audit.md` | Dialogue Desert Detection and Dramatization Audit | `155c84ca71eec591` | 1427 |
| `editorial-persona-simulation.md` | Editorial Persona Simulation — Session-Derived Technique | `c395b439d95bd9b0` | 713 |
| `expansion-session-planning.md` | Expansion Session Planning for Fiction Manuscripts | `8b7c272481fbfa22` | 587 |
| `external-editorial-model-boundaries.md` | External Editorial Model Boundaries for Fiction Drafting | `7c2aaf26186651cc` | 341 |
| `external-editorial-packet-workflow.md` | External Editorial Packet Workflow | `b9ec352bd555cb0d` | 601 |
| `external-editorial-review-consolidation.md` | External Editorial Review Consolidation for Longform Fiction | `e7510b168fff64e9` | 516 |
| `external-editorial-review-packets.md` | External editorial review packets for long manuscripts | `ed14f1f0e5ba3dd7` | 427 |
| `final-micro-polish-after-reader-scan.md` | Final Micro-Polish After Reader Scan | `2317ba05a799390b` | 561 |
| `final-proofread-export-and-review-gates.md` | Fiction final proofread/export and editorial review gates | `b916d7692acbf431` | 423 |
| `formal-reader-editorial-audit-after-expanded-baseline.md` | Formal Reader / Editorial Audit After Expanded-Draft Baseline | `9cb79ab56c0eab4f` | 651 |
| `longform-skill-bloat-audit-and-slimming.md` | Longform Skill Bloat Audit and Slimming Pattern | `ec0da70518b536bf` | 411 |
| `manuscript-quality-gate-checklist.md` | Manuscript Quality Gate Checklist | `829d79e338fcb411` | 464 |
| `model-separation-editorial-pipeline.md` | Model-Separation Editorial Pipeline | `e7cabd7eaff86ac7` | 1508 |
| `necessity-review-and-controlled-split-assessment.md` | Necessity Review and Controlled Split Assessment | `fbbe410a0a1f0cad` | 504 |
| `pass-1-6-surgical-validation-after-editorial-review.md` | Pass 1.6 Surgical Validation After External Editorial Review | `f03c78201ef6fcc2` | 416 |
| `pass1-completion-audit-copyedit-metadata-pattern.md` | Pass 1 completion audit + copyedit + metadata packaging pattern | `71bfcdf8badb006a` | 631 |
| `pass2-cadence-consistency-and-mechanical-audit.md` | Pass 2 cadence/consistency pass + mechanical audit | `ad94cf1c2560d3fd` | 537 |
| `quality-reading-pass-four-questions.md` | Quality Reading Pass — Four Questions (Arden Method) | `17ad943baf426007` | 779 |
| `read-only-external-review-response.md` | Read-Only External Review Response Workflow | `67ed6760c8d52be4` | 396 |
| `reader-profile-supporter-pass-and-editor-interpretation.md` | Reader Profile Supporter-Pass Pass + Scout Editor Interpretation | `83044d8be5a78bfd` | 601 |
| `steward-editorial-lens-and-working-writer-boundaries.md` | Steward / External Editorial Lens vs Working Writer Boundaries | `d70f864dad46bca0` | 444 |
| `targeted-alpha-editorial-packaging.md` | Targeted alpha/editorial packaging workflow | `781753027d25a37f` | 677 |

## Distilled Operational Lessons

### Baseline Checkpoint Before Reader/Editorial Audit

Provenance: `baseline-checkpoint-before-reader-audit.md` (`32aedcef29183487`), 466 words.

- Topic: Baseline Checkpoint Before Reader/Editorial Audit
- Topic: Procedure
- Verify repository state first:
- `git branch --show-current` must match the requested branch.
- `git rev-list --left-right --count HEAD...origin/<branch>` should be `0 0` before creating the baseline report.
- `git status --short` should be clean before the baseline report is created.

### Book Directory Editorial History Pattern

Provenance: `book-directory-editorial-history-pattern.md` (`69bdcd87b5ef7231`), 396 words.

- Topic: Book Directory Editorial History Pattern
- Topic: Canonical repo structure per book
- Topic: Why this matters
- **Future readers** (including future Scout sessions) don't reconstruct why decisions were made — they read the evidence.
- Topic: BOOKN_STATUS.md contents
- Current status (e.g. "FIRST DRAFT COMPLETE")

### Book 3 Pass 1.6 External Editorial Validation Pattern

Provenance: `book3-pass16-external-editorial-validation.md` (`1efb84129f0bd767`), 385 words.

- Topic: Book 3 Pass 1.6 External Editorial Validation Pattern
- Draft has already been expanded to healthy adult-novel weight.
- Topic: Core lesson
- Save the pasted external/editorial review as a report artifact in the active non-destructive revision workspace, e.g.
- Run a validation audit against the current assembled manuscript:
- law/custom/thematic density by chapter,

### Controlled Pass 1 Revision from an Editorial Review Package

Provenance: `controlled-pass1-revision-from-review-package.md` (`fd33e515ca760fd5`), 523 words.

- Topic: Controlled Pass 1 Revision from an Editorial Review Package
- A review package exists with a consolidated editorial decision, chapter-lock table, or targeted revision plan.
- The user says to proceed/begin Pass 1 revision.
- The draft is already complete and should not be rebuilt.
- Topic: Procedure
- Verify the required model/runtime before any prose/editorial judgment if the project has model-gating rules.

### Dialogue Desert Detection and Dramatization Audit

Provenance: `dialogue-desert-detection-and-dramatization-audit.md` (`155c84ca71eec591`), 1427 words.

- Topic: Dialogue Desert Detection and Dramatization Audit
- Topic: What is a Dialogue Desert?
- The reader knows what was said but never hears the speaker's voice, hesitations, or emotional state
- Topic: Critical distinction: Dialogue Desert vs. Monologue Desert
- Topic: Monologue-dominant structure
- Look for resistance. Information that flows freely feels like exposition. Information that must be pulled feels like drama.

### Editorial Persona Simulation — Session-Derived Technique

Provenance: `editorial-persona-simulation.md` (`c395b439d95bd9b0`), 713 words.

- Topic: Editorial Persona Simulation — Session-Derived Technique
- Topic: When to use
- Topic: Core idea
- Topic: The 5 Personas
- Topic: Chapter Bundle Strategy
- Topic: Context File Template (per persona)

### Expansion Session Planning for Fiction Manuscripts

Provenance: `expansion-session-planning.md` (`8b7c272481fbfa22`), 587 words.

- Topic: Expansion Session Planning for Fiction Manuscripts
- Topic: Proven Workable Pattern
- Topic: Session Planning Template
- Topic: Prioritization Strategy
- **Middle chapters first** (5-9): Where crew forms, threat escalates, revelations happen. These have highest reader impact.
- Topic: Why This Works

### External Editorial Model Boundaries for Fiction Drafting

Provenance: `external-editorial-model-boundaries.md` (`7c2aaf26186651cc`), 341 words.

- Topic: External Editorial Model Boundaries for Fiction Drafting
- Topic: Working authority model
- The manuscript/repo/canon outrank any model’s opinion.
- ChatGPT or another external model is an outside editorial lens, not a project controller.
- Hermes/Scout remains the working creative agent: drafting, continuity, file operations, trackers, validation, handoffs, commits, and push.
- Topic: How to use external feedback

### External Editorial Packet Workflow

Provenance: `external-editorial-packet-workflow.md` (`b9ec352bd555cb0d`), 601 words.

- Topic: External Editorial Packet Workflow
- Topic: Problem this solves
- Do not rewrite chapters while gathering editorial feedback.
- Split the manuscript into individual chapter files.
- Recommended packet shape for a 20-chapter / 100k-word novel.
- Packet 01: Chapter 1, or reference if already reviewed.

### External Editorial Review Consolidation for Longform Fiction

Provenance: `external-editorial-review-consolidation.md` (`e7510b168fff64e9`), 516 words.

- Topic: External Editorial Review Consolidation for Longform Fiction
- Topic: Why this matters
- Save raw external feedback first.
- Create an index/manifest with packet/chapter coverage and word counts.
- Extract actual verdicts, chapter lock recommendations, repeated concerns, and concrete fixes.
- Use prompts like: “Stop planning. Produce the actual editorial report now. Use only the text provided. Format: Editorial Summary, What Works, Main Issues, Priority Fixes, Line Notes, Lock Recommendation.”

### External editorial review packets for long manuscripts

Provenance: `external-editorial-review-packets.md` (`ed14f1f0e5ba3dd7`), 427 words.

- Topic: External editorial review packets for long manuscripts
- Topic: Session-tested pattern
- Split the manuscript into exact chapter files using the real chapter headings.
- Include a packet index with order, chapter numbers, word counts, and purpose.
- Save every useful external response as raw feedback, then extract only actionable notes into a tracker.
- Do not rewrite chapters until all reports are captured and Andrew approves a revision pass.

### Final Micro-Polish After Reader Scan

Provenance: `final-micro-polish-after-reader-scan.md` (`2317ba05a799390b`), 561 words.

- Topic: Final Micro-Polish After Reader Scan
- Topic: Principle
- changing the ending because a reader had a small accepted reservation.
- **Re-read the exact target passages only.**
- Read the relevant final assembly lines.
- If assembled from per-chapter source files, read the matching chapter source files too.

### Fiction final proofread/export and editorial review gates

Provenance: `final-proofread-export-and-review-gates.md` (`b916d7692acbf431`), 423 words.

- Topic: Fiction final proofread/export and editorial review gates
- Topic: Final proofread/export prep pattern
- Do not edit the baseline/source manuscript.
- Run mechanical publication-leak scans before export:
- `Book 1`, `Book 2`, `Chapter 8`, `previous chapters`, `earlier chapters`, `fifteen chapters`, `Complete`, placeholder initials such as `EW`;
- metadata/draft-process terms that should not appear in-world.

### Formal Reader / Editorial Audit After Expanded-Draft Baseline

Provenance: `formal-reader-editorial-audit-after-expanded-baseline.md` (`9cb79ab56c0eab4f`), 651 words.

- Topic: Formal Reader / Editorial Audit After Expanded-Draft Baseline
- Topic: When to use
- `READY FOR FORMAL READER AUDIT / EDITORIAL READINESS CHECKPOINT`
- Topic: Required discipline
- Verify live runtime if the series/model policy requires it.
- Verify branch, clean tree, sync with `origin/main`, and baseline commit/report.

### Longform Skill Bloat Audit and Slimming Pattern

Provenance: `longform-skill-bloat-audit-and-slimming.md` (`ec0da70518b536bf`), 411 words.

- Topic: Longform Skill Bloat Audit and Slimming Pattern
- Topic: Why this matters
- contradictory instructions from Anunnaki, Brambleford, Meridian, horror, and reader-site workflows;
- Topic: Safe response
- move to the project repo where it belongs;
- read handoff/tracker before acting;

### Manuscript Quality Gate Checklist

Provenance: `manuscript-quality-gate-checklist.md` (`829d79e338fcb411`), 464 words.

- Topic: Manuscript Quality Gate Checklist
- Topic: Section 1: Structural Integrity
- [ ] All chapter titles follow consistent format (e.g., "Chapter N — Title" not bare "Chapter N" in some places)
- [ ] No duplicate chapter titles across the book
- [ ] No "Summary Draft", "Scene N — Summary", or other scaffolding markers left in text
- [ ] No `[End Chapter X]` or editorial metadata visible to reader

### Model-Separation Editorial Pipeline

Provenance: `model-separation-editorial-pipeline.md` (`e7cabd7eaff86ac7`), 1508 words.

- Topic: Model-Separation Editorial Pipeline
- Topic: Critical Framing
- Topic: Pre-Drafting Phase (Orchestrator)
- **Canon documents** (treat as authoritative, never overwrite):
- Never become thriller / action / dark-for-stakes
- Topic: Writing Phase (Lead Novelist)

### Necessity Review and Controlled Split Assessment

Provenance: `necessity-review-and-controlled-split-assessment.md` (`fbbe410a0a1f0cad`), 504 words.

- Topic: Necessity Review and Controlled Split Assessment
- A chapter is already long or structurally functional, but prior pass notes suggest it may need attention.
- A chapter split is being considered for reader rhythm, but not for table-of-contents neatness.
- Topic: Principle
- Topic: Chapter necessity review workflow
- Read the target chapter and the immediate neighbouring chapters.

### Pass 1.6 Surgical Validation After External Editorial Review

Provenance: `pass-1-6-surgical-validation-after-editorial-review.md` (`f03c78201ef6fcc2`), 416 words.

- Topic: Pass 1.6 Surgical Validation After External Editorial Review
- Draft has already reached a healthy adult-novel range.
- External review says: do not broadly expand; run validation focused on structure/repetition/threat escalation.
- The issue is not missing bones, but repeated chapter machinery or cadence.
- Verify live creative runtime if the project has a model-quality rule.
- Run a read-only validation audit before editing:

### Pass 1 completion audit + copyedit + metadata packaging pattern

Provenance: `pass1-completion-audit-copyedit-metadata-pattern.md` (`71bfcdf8badb006a`), 631 words.

- Topic: Pass 1 completion audit + copyedit + metadata packaging pattern
- Pass 1 chapter-by-chapter expansion is complete for all chapters.
- Completion audit report exists and is clean.
- `handoff/current-status.md` and `handoff/next-actions.md` point to audit as the next step.
- Topic: Copyedit/proofread pass
- Verify live runtime is `gpt-5.5` / `openai-codex` before any manuscript judgement.

### Pass 2 cadence/consistency pass + mechanical audit

Provenance: `pass2-cadence-consistency-and-mechanical-audit.md` (`ad94cf1c2560d3fd`), 537 words.

- Topic: Pass 2 cadence/consistency pass + mechanical audit
- Prior model/editor audit flagged repeated cadence patterns such as `That was`, `Not X. Y.`, overused motif words, or procedural-reference consistency.
- The manuscript has a dedicated revision workspace such as `revisions/pass-2/` with per-chapter draft files and an assembled manuscript.
- Verify model/runtime and clean git state first when the project has a model gate.
- Create a read-only cadence scan before editing:
- do not rewrite whole chapters during cadence cleanup.

### Quality Reading Pass — Four Questions (Arden Method)

Provenance: `quality-reading-pass-four-questions.md` (`17ad943baf426007`), 779 words.

- Topic: Quality Reading Pass — Four Questions (Arden Method)
- Topic: When to use
- Topic: The Four Questions
- Topic: 1. Does the village/world now feel inhabited?
- Specific sensory detail (not generic): frost pattern on old glass, kettle hum read as gauge, saucer drip rhythm, pump handle requiring whole weight
- Objects carry history: thermos dented from 1978 church-step fall, hooks installed in 1968, elm tree from before the church

### Read-Only External Review Response Workflow

Provenance: `read-only-external-review-response.md` (`67ed6760c8d52be4`), 396 words.

- Topic: Read-Only External Review Response Workflow
- User requires live model/provider verification before any work.
- User asks to read handoff/review/tracker/manuscript/planning files and create an acknowledgment/response document.
- User explicitly blocks drafting the next chapter or correcting prose yet.
- Topic: Required sequence
- Verify live runtime from `~/.hermes/logs/agent.log` before touching the repo.

### Reader Profile Supporter-Pass Pass + Scout Editor Interpretation

Provenance: `reader-profile-supporter-pass-and-editor-interpretation.md` (`83044d8be5a78bfd`), 601 words.

- Topic: Reader Profile Supporter-Pass Pass + Scout Editor Interpretation
- Topic: When to use
- Topic: Core distinction
- Writes raw reader feedback to the canonical feedback archive.
- Reads the reader report after it is archived.
- Translates reader experience into a small decision list.

### Steward / External Editorial Lens vs Working Writer Boundaries

Provenance: `steward-editorial-lens-and-working-writer-boundaries.md` (`d70f864dad46bca0`), 444 words.

- Topic: Steward / External Editorial Lens vs Working Writer Boundaries
- Topic: Role split
- Hermes/Scout remains the working creative lead inside the manuscript/repo: drafting, continuity, craft decisions, trackers, completion notes, validation, commits, pushes, and handoffs.
- ChatGPT/Arden or another outside model is an editorial/stewardship lens, not a superior command layer.
- Topic: Operating rule
- outside-reader perspective after a coherent run of chapters exists;

### Targeted alpha/editorial packaging workflow

Provenance: `targeted-alpha-editorial-packaging.md` (`781753027d25a37f`), 677 words.

- Topic: Targeted alpha/editorial packaging workflow
- Topic: Trigger signs
- A validation report says the draft is structurally viable / beta-ready / ready for targeted alpha or editorial feedback.
- The editor/user says not to chase word count or create another revision pass.
- The next useful work is packaging the manuscript with reader context and focused questions.
- Identify the latest verified manuscript source before packaging.
