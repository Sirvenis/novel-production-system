# Legacy Generalized Lessons — controlled-fiction-drafting-and-autonomous-runs

Date: 2026-08-01

This compact linked reference distills cross-series/general items from the old global `longform-fiction-series-drafting` reference archive into task-class guidance for the staged draft skill split.

No live Hermes skills were changed. Series-specific canon remains in canonical series repos; the legacy files remain untouched until a later approved slimming pass.

Source manifest: `/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/REFERENCE_CLASSIFICATION_MANIFEST.csv`
Legacy source directory: `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references`
Processed references in this task domain: 28

## Generalization Rules Used

- Convert reusable procedure into task-class guidance.
- Preserve project names only as provenance; do not treat old examples as current canon.
- Do not include runtime/provider/profile/deployment-sensitive items here; those remain quarantined for manual review.
- Before installing any staged skill live, re-check current repo authority and validate the draft skill package.

## Source Index

| Source file | Title | Hash | Words |
|---|---|---:|---:|
| `autonomous-book-completion-run.md` | Autonomous Book Completion Run | `b5c2f22dbcf42c2f` | 521 |
| `autonomous-completion-lean-skeleton-guard.md` | Autonomous Completion Lean-Skeleton Guard | `5adb0c9a9a7054ff` | 422 |
| `autonomous-completion-workflow-diagnosis-pattern.md` | Autonomous Completion Workflow Diagnosis Pattern | `77894429a6e18b7d` | 801 |
| `autonomous-creative-worker-monitor-cron.md` | Autonomous creative worker plus monitor cron pattern | `077043f4b682cff7` | 289 |
| `autonomous-pipeline-audit-and-maintenance.md` | Autonomous Pipeline Audit and Maintenance Workflow | `44cfa56fb57a0477` | 941 |
| `autonomous-series-continuation-pipeline-pattern.md` | Autonomous Series Continuation Pipeline Pattern | `f88026b7d9bf5f81` | 962 |
| `book3-first-draft-completion-cron.md` | Book 3 first-draft completion from scheduled drafting cron | `2a8e093a4d9c87f0` | 429 |
| `book3-pass15-autonomous-expansion-insert.md` | Book 3 Pass 1.5 Autonomous Expansion Insert Pattern | `64036929fd0227e2` | 416 |
| `book3-pass15-bounded-cron-expansion-sync.md` | Book 3 Pass 1.5 bounded cron expansion + dashboard sync | `43762ab795d158ac` | 436 |
| `chapter-expansion-by-incremental-insertion.md` | Chapter Expansion by Incremental Insertion | `4703847471136f51` | 362 |
| `chapter-renumbering-after-insertion.md` | Chapter Renumbering After New Chapter Insertion | `3ce01088b2210607` | 573 |
| `cron-tracker-ahead-sequential-drafting.md` | Cron tracker-ahead sequential drafting pattern | `f9ce7956d1f46f99` | 222 |
| `durable-cron-continuation-after-initial-chapters.md` | Durable Cron Continuation After Initial Fiction Chapters | `845a2bd5dfda0ffa` | 576 |
| `expanded-draft-structural-reader-readiness-audit.md` | Expanded Draft Structural Reader / Readiness Audit Pattern | `c8bf23601edf0743` | 624 |
| `first-draft-review-to-pass1-start.md` | First-draft review to Pass 1 start | `57d9a8816ae094bb` | 406 |
| `full-draft-review-pass-workflow.md` | Full-draft review and Pass 1 expansion workflow | `6d37d143f67ef1b3` | 378 |
| `milestone-drafting-workflow.md` | Milestone-Based Sequential Novel Drafting | `71255f4e2fb486b6` | 352 |
| `no-chapter-headers-in-scene-transitions.md` | No Chapter Headers in Scene Transitions | `98e66ab834dc0254` | 463 |
| `pass-1-expansion-from-thin-draft.md` | Pass 1 Expansion: From Thin Draft to Commercial Length | `32414230921ebfcb` | 963 |
| `pass15-validation-stop-expansion-cron.md` | Pass 1.5 Validation / Stop-Expansion Cron Pattern | `eea25ab990a6111d` | 420 |
| `pass2-chapter-expansion-validation-notes.md` | Pass 2 chapter expansion validation notes | `babf24c93ca5ecba` | 321 |
| `post-draft-editorial-audit-workflow.md` | Post-Draft Editorial Review & Reader Audit Workflow | `bb59603f600e8001` | 1208 |
| `procedural-antagonist-chapter-drafting.md` | Procedural Antagonist Chapter Drafting | `393710616b48b325` | 460 |
| `python-incremental-chapter-expansion-technique.md` | Python Incremental Chapter Expansion Technique | `8145f60d36d63258` | 721 |
| `sequential-novel-drafting-milestones.md` | Sequential Novel Drafting with Milestone Mini-Checks | `f69e87f5765b3a8d` | 363 |
| `session-opening-stale-status-pitfall.md` | Session Opening Stale-Status Pitfall | `f3a8d35bb1525898` | 378 |
| `single-agent-draft-shortfall-case-study.md` | Case Study: Single-Agent Draft Shortfall | `65b33221133cd5b6` | 154 |
| `solo-writer-thin-draft-failure-mode.md` | Solo Writer Thin Draft Failure Mode | `512f6ac12fef1625` | 565 |

## Distilled Operational Lessons

### Autonomous Book Completion Run

Provenance: `autonomous-book-completion-run.md` (`b5c2f22dbcf42c2f`), 521 words.

- Topic: Autonomous Book Completion Run
- "no replying after every chapter"
- Verify the live prose runtime first if the project is model-gated.
- For Meridian/Book 3-style gated work, inspect `~/.hermes/logs/agent.log` and confirm provider/model exactly before prose edits.
- If runtime is wrong or switches/fallbacks during prose drafting, stop prose work, commit/push any clean completed work if possible, and report the blocker.
- Pull and validate the repository before drafting.

### Autonomous Completion Lean-Skeleton Guard

Provenance: `autonomous-completion-lean-skeleton-guard.md` (`5adb0c9a9a7054ff`), 422 words.

- Topic: Autonomous Completion Lean-Skeleton Guard
- Topic: Required checks during autonomous completion
- Per-chapter default: use the prompt’s stated range.
- If a chapter is below the thinness threshold, run a real thinness check before continuing.
- One short procedural chapter can be acceptable; a run of short chapters is a systemic failure.
- If multiple consecutive chapters fall below target, stop or expand before proceeding.

### Autonomous Completion Workflow Diagnosis Pattern

Provenance: `autonomous-completion-workflow-diagnosis-pattern.md` (`77894429a6e18b7d`), 801 words.

- Topic: Autonomous Completion Workflow Diagnosis Pattern
- A durable/background/autonomous job completed and pushed a first draft.
- User asks why it happened and whether the durable handoff caused it.
- Topic: Required boundary
- Do not line edit, copyedit, proofread, package, publish, or update reader sites.
- Treat the output as workflow/root-cause analysis plus status/handoff updates only.

### Autonomous creative worker plus monitor cron pattern

Provenance: `autonomous-creative-worker-monitor-cron.md` (`077043f4b682cff7`), 289 words.

- Topic: Autonomous creative worker plus monitor cron pattern
- Uses the approved high-quality model for canon/prose.
- Checks the worker job ID, cron state, last status, STOP files, assembled draft word/chapter counts, and state file.
- Topic: Prompt guardrails
- do not schedule further cron jobs,
- verify assembled manuscript after each chunk,

### Autonomous Pipeline Audit and Maintenance Workflow

Provenance: `autonomous-pipeline-audit-and-maintenance.md` (`44cfa56fb57a0477`), 941 words.

- Topic: Autonomous Pipeline Audit and Maintenance Workflow
- "Research the current autonomous pipeline for profile X"
- Any request to audit profiles, repos, or pipeline state after a break.
- Topic: Step 1: Locate the Profile(s)
- Topic: Step 2: Verify Profile Integrity
- Topic: Step 3: Verify the Repo

### Autonomous Series Continuation Pipeline Pattern

Provenance: `autonomous-series-continuation-pipeline-pattern.md` (`f88026b7d9bf5f81`), 962 words.

- Topic: Autonomous Series Continuation Pipeline Pattern
- Topic: Pattern summary
- **Canon drift** — changing killers, motives, or series facts because the worker didn't re-read canonical state.
- **Thin-content shortfall** — producing a structurally complete draft at 40–50% of target word count because single-agent drafting lacks editorial distance.
- Topic: Stage 0 — Source validation and targets
- `CANONICAL_FEEDBACK_ARCHIVE.md` (feedback from prior books)

### Book 3 first-draft completion from scheduled drafting cron

Provenance: `book3-first-draft-completion-cron.md` (`2a8e093a4d9c87f0`), 429 words.

- Topic: Book 3 first-draft completion from scheduled drafting cron
- Topic: Durable workflow lesson
- Verify live runtime/model before creative prose if canon quality matters.
- Read the canonical tracker and continue from the first `next` row, even if the prompt/handoff is stale.
- For each remaining chapter:
- read previous chapter ending, current brief, and following brief/final brief;

### Book 3 Pass 1.5 Autonomous Expansion Insert Pattern

Provenance: `book3-pass15-autonomous-expansion-insert.md` (`64036929fd0227e2`), 416 words.

- Topic: Book 3 Pass 1.5 Autonomous Expansion Insert Pattern
- Active plan/state files define the next expansion zone and STOP condition.
- Old fixed chapter scaffold is deprecated; chapter count must follow story rhythm.
- Creative/canon prose must come only from the approved primary model/runtime.
- Topic: Successful workflow
- Read the expansion plan, autonomous state, scene map, and adjacent chapters around the next unfinished zone.

### Book 3 Pass 1.5 bounded cron expansion + dashboard sync

Provenance: `book3-pass15-bounded-cron-expansion-sync.md` (`43762ab795d158ac`), 436 words.

- Topic: Book 3 Pass 1.5 bounded cron expansion + dashboard sync
- Topic: Pattern captured
- Verified live runtime from `~/.hermes/logs/agent.log` as `model=gpt-5.5 provider=openai-codex` before canon prose.
- Checked both STOP paths before editing:
- Trusted the Pass 1.5 state files and assembled draft before choosing the next queue item.
- Inserted a new chapter in the Alalu/Kharak consequence zone:

### Chapter Expansion by Incremental Insertion

Provenance: `chapter-expansion-by-incremental-insertion.md` (`4703847471136f51`), 362 words.

- Topic: Chapter Expansion by Incremental Insertion
- Topic: Technique
- Topic: Repeat until target reached
- Topic: Advantages
- Easier to verify — only changed sections need review
- `replace()` requires exact string matching — use enough context lines to ensure uniqueness

### Chapter Renumbering After New Chapter Insertion

Provenance: `chapter-renumbering-after-insertion.md` (`3ce01088b2210607`), 573 words.

- Topic: Chapter Renumbering After New Chapter Insertion
- Inserted: Ch 12.5 (night before battle), Ch 14.5 (morning after)
- Topic: Solution: Full Renumbering
- Topic: Example: The Last Clean-Up Crew Book 1
- Topic: Before (broken):
- Topic: Problem: Ch 14.5 (next morning) comes AFTER Ch 14 (6 weeks later). Two chapters titled "The Line."

### Cron tracker-ahead sequential drafting pattern

Provenance: `cron-tracker-ahead-sequential-drafting.md` (`f9ce7956d1f46f99`), 222 words.

- Topic: Cron tracker-ahead sequential drafting pattern
- Verify the live runtime/model first when canon/prose quality is constrained.
- Read the canonical chapter tracker and treat the first row marked `next` as the active source of truth, even if the cron prompt says an earlier chapter is next.
- Do not roll tracker metadata backward to match the prompt.
- If the tracker already shows the prompt's target chapter as `drafted`, inspect the tracker note and continue from the current `next` row.
- For each chapter drafted in the cron run:

### Durable Cron Continuation After Initial Fiction Chapters

Provenance: `durable-cron-continuation-after-initial-chapters.md` (`845a2bd5dfda0ffa`), 576 words.

- Topic: Durable Cron Continuation After Initial Fiction Chapters
- Verify runtime from live Hermes logs if the project is model-gated.
- Verify git branch, clean tree, sync with origin, required files, and validation baseline.
- Read the authority stack and immediate prior chapters from repo files.
- Draft at least the first authorised next chapter if practical, so the handoff is grounded in real progress rather than just a scheduled promise.
- Commit and push the completed chapter package before handing off.

### Expanded Draft Structural Reader / Readiness Audit Pattern

Provenance: `expanded-draft-structural-reader-readiness-audit.md` (`c8bf23601edf0743`), 624 words.

- Topic: Expanded Draft Structural Reader / Readiness Audit Pattern
- Topic: When to use
- Topic: Required source stack
- `handoff/CURRENT_PROJECT_HANDOFF.md`
- first-draft tracker / chapter map
- chapter files for any suspicious short/thin range

### First-draft review to Pass 1 start

Provenance: `first-draft-review-to-pass1-start.md` (`57d9a8816ae094bb`), 406 words.

- Topic: First-draft review to Pass 1 start
- Topic: Session-derived pattern
- Verify the runtime/model if canon/prose quality matters.
- Preserve the first draft untouched.
- Write a full-draft structural review before line polish:
- `revisions/pass-1/chapters/` copied from first-draft chapters,

### Full-draft review and Pass 1 expansion workflow

Provenance: `full-draft-review-pass-workflow.md` (`6d37d143f67ef1b3`), 378 words.

- Topic: Full-draft review and Pass 1 expansion workflow
- Do not overwrite `drafts/` or the first-draft tracker.
- Create a non-destructive revision workspace such as:
- Structure/pacing: act turns, chapter lengths, compressed sections, expansion needs.
- `workflow/book-X-pass-1-revision-plan.md`
- If later chapters are compressed, expand those before polishing early prose.

### Milestone-Based Sequential Novel Drafting

Provenance: `milestone-drafting-workflow.md` (`71255f4e2fb486b6`), 352 words.

- Topic: Milestone-Based Sequential Novel Drafting
- Example: draft Chapters 9–12 one at a time, then do the Chapter 12 midpoint check.
- read previous chapter ending,
- read current chapter brief,
- optionally read following chapter brief for hook direction,
- draft only the current chapter,

### No Chapter Headers in Scene Transitions

Provenance: `no-chapter-headers-in-scene-transitions.md` (`98e66ab834dc0254`), 463 words.

- Topic: No Chapter Headers in Scene Transitions
- Topic: The Problem
- **Scene headers inside chapters:** Book 3 had 47 `## Scene 1`, `## Scene 2`, etc. headers inside chapters. These looked like draft scaffolding and broke immersion.
- **Duplicate chapter titles:** Book 1 had `# Chapter Fifteen — The Water Level` followed immediately by `## The Water Level`, creating a double heading.
- **Chapter title inside body text:** Chapter headings were sometimes copied into the first paragraph of the chapter as plain text.
- Topic: Detection Script

### Pass 1 Expansion: From Thin Draft to Commercial Length

Provenance: `pass-1-expansion-from-thin-draft.md` (`32414230921ebfcb`), 963 words.

- Topic: Pass 1 Expansion: From Thin Draft to Commercial Length
- Topic: When to Use
- Topic: Prerequisites
- Complete first draft exists and reads well end-to-end
- Primary model/runtime is verified (for horror: kimi-k2.6:cloud authorized)
- Topic: Expansion Workflow

### Pass 1.5 Validation / Stop-Expansion Cron Pattern

Provenance: `pass15-validation-stop-expansion-cron.md` (`eea25ab990a6111d`), 420 words.

- Topic: Pass 1.5 Validation / Stop-Expansion Cron Pattern
- The prompt or stale job setup says to draft the next expansion insert.
- Check STOP files first. If present, stop without prose changes and report the blocker through the configured delivery path.
- sequential chapter numbering,
- assembled draft matches chapter files if applicable,
- Read enough of the inserted chapters and finale to judge whether the expanded joints are functioning.

### Pass 2 chapter expansion validation notes

Provenance: `pass2-chapter-expansion-validation-notes.md` (`babf24c93ca5ecba`), 321 words.

- Topic: Pass 2 chapter expansion validation notes
- Verify runtime/model before prose if the project has a model safeguard.
- Verify git state is clean and record the starting commit.
- Read the current handoff, synthesis/plan, tracker, target chapter, and adjacent chapters.
- Expand the target chapter only. Preserve plot outcome and chapter count unless the plan explicitly changes them.
- Reassemble the current Pass 2 manuscript from chapter files, then verify chapter count and word counts with commands.

### Post-Draft Editorial Review & Reader Audit Workflow

Provenance: `post-draft-editorial-audit-workflow.md` (`bb59603f600e8001`), 1208 words.

- Topic: Post-Draft Editorial Review & Reader Audit Workflow
- Topic: When to Use This Workflow
- Topic: PASS 2: EDITORIAL REVIEW (Editor / Structural Eye)
- Topic: Checklist — Pass 2
- Topic: Pass 2 Output
- Critical issues table (must fix before Pass 3)

### Procedural Antagonist Chapter Drafting

Provenance: `procedural-antagonist-chapter-drafting.md` (`393710616b48b325`), 460 words.

- Topic: Procedural Antagonist Chapter Drafting
- Topic: Session pattern proven on Meridian Relics Book 3
- Refuse a phrase before it enters the log.
- Create a renewal mechanism before the opponent defines the missing door.
- Do not let the relic solve the legal/procedural problem. The humans build the procedural floor.
- Use dual records to dramatise power.

### Python Incremental Chapter Expansion Technique

Provenance: `python-incremental-chapter-expansion-technique.md` (`8145f60d36d63258`), 721 words.

- Topic: Python Incremental Chapter Expansion Technique
- Topic: Solution: Python string-replacement insertion
- Read the original chapter file with Python `open()`.
- Use `str.replace(marker, marker + inserted_text, 1)` to insert new paragraphs **after** the marker.
- Write the result back with Python `open(..., 'w')`.
- Verify with `wc -w` and inspect the tail.

### Sequential Novel Drafting with Milestone Mini-Checks

Provenance: `sequential-novel-drafting-milestones.md` (`f69e87f5765b3a8d`), 363 words.

- Topic: Sequential Novel Drafting with Milestone Mini-Checks
- Draft chapters sequentially, one at a time.
- read the previous chapter ending,
- read the current chapter brief,
- optionally read the next brief for the hook,
- draft the chapter at the expected path,

### Session Opening Stale-Status Pitfall

Provenance: `session-opening-stale-status-pitfall.md` (`f3a8d35bb1525898`), 378 words.

- Topic: Session Opening Stale-Status Pitfall
- Topic: Root cause
- Meridian Relics Book 2 (The Burning Bird of Rhodes) Pass 1 revision had just completed
- Topic: Correction applied
- `handoff/current-status.md`
- Topic: Prevention rule

### Case Study: Single-Agent Draft Shortfall

Provenance: `single-agent-draft-shortfall-case-study.md` (`65b33221133cd5b6`), 154 words.

- Topic: Case Study: Single-Agent Draft Shortfall
- Topic: What happened
- Primary model (gpt-5.5 / openai-codex) hit rate limits mid-session.
- Presented the draft as complete.
- **Structural failure:** Climax merged into Chapter 12; Chapters 13-15 became aftermath + sequel hooks instead of sustained escalation.
- Topic: What should have happened

### Solo Writer Thin Draft Failure Mode

Provenance: `solo-writer-thin-draft-failure-mode.md` (`512f6ac12fef1625`), 565 words.

- Topic: Solo Writer Thin Draft Failure Mode
- Topic: What Happened
- An editor reviewing the architecture before drafting
- A reviewer running reader audits every 5 chapters
- Word-count enforcement at the chapter level
- Topic: Thin chapter examples
