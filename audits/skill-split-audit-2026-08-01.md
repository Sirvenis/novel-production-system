# Skill Split Audit — longform-fiction-series-drafting

Date: 2026-08-01T10:03:15+1000
Scope: read-only audit of the current Hermes fiction/novel-production skill state. No live skills were rewritten, split, deleted, or installed.

## Summary verdict

`longform-fiction-series-drafting` has not yet been truly split into installed novel-production task skills.

It remains the main oversized fiction umbrella skill:

- Skill file: `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/SKILL.md`
- `SKILL.md` size: 53,621 bytes
- Reference markdown files: 252
- Templates: 9
- Scripts: 4

There are useful task-level skill templates in `/home/andrew/novel-production-system/templates/skills/`, but they are templates inside the infrastructure repo, not installed Hermes skills visible in `skills_list`.

The best next structure is not “one Hermes skill per series.” Use task/class-level Hermes skills for reusable production methods, and keep series-specific knowledge in each canonical series repo unless a series has a recurring procedure that genuinely needs a Hermes skill.

## Verified inputs

Read/checked:

- `/home/andrew/projects/active/scout-handoffs/CURRENT_HANDOFF.md`
- `/home/andrew/novel-production-system/audits/autonomous-novel-production-systems-audit-2026-07-25.md`
- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/SKILL.md`
- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references/`
- `/home/andrew/novel-production-system/templates/skills/`
- Current runtime from `~/.hermes/logs/agent.log`: `model=gpt-5.5 provider=openai-codex`
- `scout-handoffs` git state: clean at `99fc1f0`
- `novel-production-system` git state before this report: clean at `653e760`

Generated inventory:

- `/home/andrew/novel-production-system/audits/longform-fiction-reference-inventory-2026-08-01.csv`

## Installed / visible skill state

Relevant installed skills found in `~/.hermes/skills`:

| Skill | Role | Current concern |
|---|---|---|
| `creative/longform-fiction-series-drafting` | Main fiction umbrella | Oversized mixed archive: 252 references, many series-specific case studies |
| `creative/manuscript-editorial-review` | Editorial review class skill | Useful adjacent class skill, not the novel-production pipeline split |
| `github/fiction-repository-governance` | Fiction repo/source-of-truth governance | Covers repo structure, not drafting/revision/reader/audit pipeline |
| `productivity/skill-library-maintenance` | Skill bloat/splitting workflow | Correct maintenance procedure |
| `software-development/hermes-agent-skill-authoring` | Skill creation/validation conventions | Needed only when we start creating or editing installed skills |

No obvious installed Hermes skills were found for active series names such as Brambleford, Anunnaki, Meridian, Last Clean-Up Crew, The Better Version, or Nurse Fiction.

## Novel-production-system task templates

The repo `/home/andrew/novel-production-system` contains five task-level skill templates:

| Template | Purpose | My recommendation |
|---|---|---|
| `skill-discovery-pass.md` | Pure factual inventory before editorial interpretation | Promote to installed task skill after cleanup pass |
| `skill-voice-audit.md` | Voice consistency / prose-tic detection | Promote to installed task skill, probably under fiction revision/QA |
| `skill-continuity-check.md` | Thread/timeline/motif continuity verification | Promote to installed task skill, probably under fiction QA |
| `skill-research-ingest.md` | Convert external research into structured repo knowledge | Promote to installed cross-project research-ingest skill or merge with an existing research/video-ingest skill |
| `skill-canary-run.md` | Bounded autonomy/profile test before scaling | Promote or merge into fiction-autonomous-workers / profile-governance skill |

These templates are good, but they are not enough to replace the current umbrella yet. They cover specific stages, not the whole mature pipeline.

## Reference inventory by filename bucket

Filename-bucket classification is intentionally conservative. Some cross-series patterns mention project examples internally, but the filename indicates likely ownership/migration target.

### Series / project specificity

| Bucket | Count | Initial treatment |
|---|---:|---|
| Cross-series/general | 167 | Keep/summarize into task/class skills or retain as shared references |
| Meridian/Elias Relics | 29 | Move/copy case studies into `meridian-relics` or Elias Library docs where project-specific |
| Elias Library/Reading Room | 19 | Split between Library catalogue/website docs and web/library packaging skill |
| Anunnaki | 17 | Copy/migrate into `anunnaki-chronicles-novel` docs where project-specific |
| Brambleford/Briarcombe/Cozy | 8 | Move Brambleford/Cozy case studies into canonical Brambleford repo or mystery storycraft docs |
| Stories/Shorts | 6 | Either short-story class reference or Elias Library repo depending on scope |
| Last Clean-Up Crew/Horror | 4 | Move series-specific horror material into `last-clean-up-crew`; keep reusable horror-comedy method only if generalized |
| The Better Version | 2 | Move diagnostic/governance case studies into `the-better-version` or summarize into pipeline lessons |

### Task / method buckets

| Bucket | Count | Candidate future skill / home |
|---|---:|---|
| Autonomous workers / models | 65 | `fiction-autonomous-workers` plus model-routing/profile-governance references |
| Drafting / chapter briefs | 43 | `fiction-drafting-core` |
| Revision / expansion / polish | 38 | `fiction-revision-passes` |
| Cross-series core / misc | 24 | Audit manually; some stay in core, some become repo docs |
| Reader/editorial audit | 22 | `fiction-reader-editorial-audits` or merge with `manuscript-editorial-review` |
| Reader-site / web packaging | 17 | `fiction-reader-site-packaging` or Library website skill |
| Repo governance / handoff / memory | 17 | Keep in `fiction-repository-governance` / `session-resumption` / Codebase Memory docs, not drafting skill |
| Case studies / lessons | 11 | Mostly move to project repos after preserving one-line generalized lesson |
| Pipeline architecture / SOUL | 8 | `fiction-production-pipeline` or repo-local series SOUL templates |
| Research / market ingest | 7 | `fiction-research-ingest` / `research-ingest` task skill |

## Proposed split map

### 1. `fiction-drafting-core`

Owns:

- Source-of-truth checks before prose
- Runtime/model stop gates
- One bounded chapter/brief at a time
- Python file I/O for long chapters
- Tracker/handoff/report/commit loop
- Chapter titles and assembly safety that affect drafting sessions

Candidate source references:

- `controlled-chapter-drafting-after-approved-brief.md`
- `chapter-brief-after-architecture-approval.md`
- `sequential-chapter-drafting-handoff-pattern.md`
- `milestone-drafting-workflow.md`
- `write-file-truncation-pitfall.md`
- General parts of Anunnaki/Meridian drafting examples after stripping project-specific canon

### 2. `fiction-revision-passes`

Owns:

- Pass 1 / Pass 2 / line edit / copy edit / proofread boundaries
- Expansion and deepening methods
- Dialogue-desert and monologue-dominant detection
- Incremental Python insertion technique
- Mechanical validation after prose changes

Candidate source references:

- `controlled-pass1-revision-from-review-package.md`
- `controlled-pass2-expansion-and-checkpoint.md`
- `pass2-cadence-consistency-and-mechanical-audit.md`
- `dialogue-desert-detection-and-dramatization-audit.md`
- `dramatization-pass-confrontation-over-monologue.md`
- `targeted-developmental-deepening-pattern.md`
- `python-incremental-chapter-expansion-technique.md`

### 3. `fiction-reader-editorial-audits`

Owns:

- Discovery Pass boundary: inventory only, no recommendations
- Reader profile as paying/customer reader
- Formal reader/editorial audit gates
- External editorial packet workflows
- Readiness reports and verdict discipline

Candidate source references:

- Promote `novel-production-system/templates/skills/skill-discovery-pass.md`
- `post-draft-editorial-audit-workflow.md`
- `structural-reader-audit-and-readiness-report.md`
- `formal-reader-editorial-audit-after-expanded-baseline.md`
- `reader-profile-supporter-pass-and-editor-interpretation.md`
- `external-editorial-packet-workflow.md`

### 4. `fiction-autonomous-workers`

Owns:

- Showrunner/writer/editor/reader profile boundaries
- Canary runs
- Durable cron continuation where appropriate
- Worker writes repo-local reports instead of raw Telegram chatter
- Stale prompt vs tracker truth
- Model/fallback stop gates and traceability

Candidate source references:

- Promote `novel-production-system/templates/skills/skill-canary-run.md`
- `autonomous-book-completion-run.md`
- `durable-cron-continuation-after-initial-chapters.md`
- `repo-local-worker-handoff-and-assembly-validation.md`
- `direct-writer-editor-repo-handoff.md`
- `profile-suite-to-executable-production-pipeline.md`
- `automatic-model-switching-policy.md`

### 5. `fiction-research-ingest`

Owns:

- Research-only gates before architecture/prose
- Source ledgers
- Video/article/paper ingestion
- Market/genre/platform research reports
- Distinguishing raw evidence from canon adoption

Candidate source references:

- Promote `novel-production-system/templates/skills/skill-research-ingest.md`
- `research-only-mythology-dossier-before-architecture.md`
- `fiction-author-monetization-research.md`
- `self-publishing-platform-alternatives.md`
- `elias-library-commercial-genre-strategy.md` after generalizing

### 6. `fiction-reader-site-packaging`

Owns:

- Manuscript-to-web conversion
- Hybrid one-address reader site architecture
- Feedback forms
- Cache-busting and deployment pitfalls
- Chapter-title and duplicate-ID regression guards
- Library free/locked packaging safety

Candidate source references:

- `reader-site-feedback-form-generation.md`
- `single-page-multi-book-reader-site.md`
- `reader-site-feedback-deployment-pitfalls.md`
- `reader-site-title-regression-guards.md`
- `reader-feedback-form-templates.md`
- `simplified-reader-site-feedback-forms.md`
- `manuscript-to-web-reader-pipeline.md`

### 7. `fiction-production-pipeline`

Possible umbrella / index skill, not a dumping ground.

Owns:

- 12-stage pipeline overview
- Stage order and gates
- Which specialist skill to load for each stage
- Series repo vs profile vs Library vs website responsibility

Candidate source references:

- `novel-production-pipeline-patterns.md`
- `series-level-soul-and-length-standard-pattern.md`
- `curator-of-series-memory-pattern.md`
- `author-imprint-and-profile-governance.md`
- `book-directory-editorial-history-pattern.md`
- `model-separation-editorial-pipeline.md`

This should stay concise. It should route to the specialist skills rather than swallowing all 252 references again.

## What should move to canonical series repos

Series-specific case studies should be preserved before being removed from the global skill. Proposed homes:

| Source type | Destination |
|---|---|
| Anunnaki Book 2/3/4 chapter, audit, cron, canon-reset examples | `/home/andrew/projects/active/anunnaki-chronicles-novel/docs/` or `book4/reports/` as appropriate |
| Meridian / Sunken Bell / Burning Bird run examples | `/home/andrew/projects/active/meridian-relics/docs/` or book-level reports |
| Brambleford/Briarcombe incidents and village/cozy pass examples | `/home/andrew/projects/active/brambleford-cozy-mystery/docs/` or storycraft/editorial reports |
| Better Version diagnostic case studies | `/home/andrew/the-better-version/docs/` or `book2/reports/` |
| Last Clean-Up Crew horror-comedy specifics | `/home/andrew/projects/active/last-clean-up-crew/docs/` or `series/` |
| Elias Library catalogue/access/public-site material | `/home/andrew/projects/active/elias-silver-library/docs/` or `/home/andrew/projects/active/elias-silver-library-website/docs/` |

Keep only a generalized lesson and a pointer in global skills.

## Answer to the key question: do we need per-series Hermes skills?

Not by default.

Recommended rule:

- Series knowledge lives in the series repo: `series/SOUL.md`, `SERIES_BIBLE.md`, `STORYCRAFT_HANDBOOK.md`, handoff, reports, status files.
- Hermes skills should describe reusable procedures: how to draft, audit, revise, package, research, or manage workers.
- Create a per-series Hermes skill only if multiple Hermes profiles repeatedly need the same series-specific operating procedure and repo-local docs are not enough.

Current active series already have profile suites and canonical repos. That is the right place for series voice/canon. A Hermes skill per series would likely recreate bloat and load irrelevant canon into sessions.

## Non-destructive migration sequence

1. Preserve full inventory CSV and this audit in `novel-production-system`.
2. Do not delete source references yet.
3. Create draft skill files under a planning/audit area first, not active `~/.hermes/skills`.
4. Copy project-specific references into destination series repos with provenance indexes.
5. Draft the small `fiction-production-pipeline` router skill and 5-6 task skills.
6. Validate frontmatter and count footprint.
7. Compare old vs new token/byte footprint.
8. Ask Andrew to review the split map before installing/replacing live skills or editing profile skill lists.
9. Only after approval: install new skills, slim `longform-fiction-series-drafting`, and update profile keep-lists.

## Do not do yet

- Do not delete any of the 252 current references.
- Do not rewrite `longform-fiction-series-drafting` in place.
- Do not create one Hermes skill per active fiction series by default.
- Do not change profile skill lists or runtime config during this audit.
- Do not move project-specific files out of the skill until copied into destination repos and indexed.

## Recommended next decision for Andrew

Approve a draft-skill planning pass, not live skill surgery.

The planning pass should create draft files under:

`/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/`

Drafts to create:

1. `fiction-production-pipeline/SKILL.md`
2. `fiction-drafting-core/SKILL.md`
3. `fiction-revision-passes/SKILL.md`
4. `fiction-reader-editorial-audits/SKILL.md`
5. `fiction-autonomous-workers/SKILL.md`
6. `fiction-research-ingest/SKILL.md`
7. `fiction-reader-site-packaging/SKILL.md`

Those drafts should import/generalize the five existing `novel-production-system/templates/skills/` files and selected cross-series references, but stay outside live Hermes skills until reviewed.
