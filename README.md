# Novel Production System

A reference implementation of a mature, multi-stage editorial pipeline for multi-book novel series, developed and battle-tested across three complete books.

## What This Is

This repository preserves the **reusable production infrastructure** — not the creative content. It is designed to be cloned, adapted, and deployed for any new novel or series.

## What This Is NOT

- A manuscript archive (manuscripts live in their own creative repositories)
- A writing guide for beginners (this assumes you can write; it helps you produce)
- A one-size-fits-all template (every project adapts this system)

## Repository Map

```
novel-production-system/
├── README.md                    # This file
├── docs/
│   ├── GETTING_STARTED.md       # Clone, adapt, and deploy for a new project
│   ├── REPO_ORGANISATION.md     # How this repo is structured and why
│   └── ADAPTATION_GUIDE.md      # How to customise the pipeline for different genres
├── infrastructure/
│   ├── PRODUCTION_PIPELINE.md   # The pipeline: Stage 0 (Voice Test) + 9-Stage system
│   ├── EDITORIAL_STAGES.md      # Each stage: purpose, inputs, outputs, verdicts
│   ├── MULTI_PROFILE_WORKFLOW.md # Hermes profile-based agent pipeline
│   ├── CRAFT_TECHNIQUES.md      # Reusable craft rules (genre-agnostic)
│   ├── TRACKING_SYSTEM.md       # Dashboards, trackers, decision logs
│   ├── HANDOFF_SYSTEM.md        # Cross-session state preservation
│   ├── GIT_WORKFLOW.md          # Commit discipline and branch strategy
│   └── EVOLUTION.md             # How the pipeline developed, what failed, what changed
├── templates/
│   ├── ARCHITECTURE_TEMPLATE.md
│   ├── CHAPTER_JOB_STATEMENT.md
│   ├── EDITORIAL_REPORT.md
│   ├── READER_AUDIT_TEMPLATE.md
│   ├── TRACKER_TEMPLATE.md
│   ├── HANDOFF_TEMPLATE.md
│   ├── DECISION_LOG_ENTRY.md
│   ├── VOICE_GUARDRAILS_TEMPLATE.md
│   ├── CHAPTER_1_VOICE_TEST_REVIEW_TEMPLATE.md
│   └── CHAPTER_1_REVIEW_PACKAGE_TEMPLATE.md
├── case-studies/
│   └── horror-series-production/
│       ├── OVERVIEW.md          # Anonymised summary of 3-book production
│       ├── BOOK1_LESSONS.md     # What the first book taught us
│       ├── BOOK2_LESSONS.md     # Pipeline evolution, autonomy grants
│       ├── BOOK3_LESSONS.md     # Seductive entity, reader audit, shrinkage
│       └── PIPELINE_EVOLUTION.md # Stage-by-stage how the system grew
└── references/
    ├── READER_AUDIT_FIVE_QUESTIONS.md
    ├── DEVELOPMENTAL_STRUCTURAL_FOUR_QUESTIONS.md
    ├── TIER_BASED_EXPANSION.md
    ├── DISCOVERY_PASS_WORKFLOW.md
    ├── LINE_EDIT_EXECUTION.md
    ├── COPY_EDIT_EXECUTION.md
    ├── ASSEMBLY_FINAL_QA.md
    ├── SCOPE_DISCIPLINE.md
    └── VERIFICATION_RULE.md
```

## Quick Start

```bash
# 1. Clone this repository as your production backbone
git clone https://github.com/Sirvenis/novel-production-system.git

# 2. Create your creative repository (manuscripts live here)
gh repo create my-new-novel --private --clone

# 3. Copy the templates into your creative repo
mkdir -p my-new-novel/{drafts,tracking,handoff,manuscript}
cp novel-production-system/templates/* my-new-novel/templates/

# 4. Read PRODUCTION_PIPELINE.md and adapt for your genre
# 5. Create your first ARCHITECTURE.md in your creative repo
# 6. Begin drafting
```

**Important:** This repository contains reusable infrastructure only. Unpublished creative material (manuscripts, project-specific architecture, character designs, voice guardrails) belongs in a dedicated private creative repository. See `docs/REPO_ORGANISATION.md` for the repository governance model.

## The 9 Stages at a Glance

| Stage | Name | Purpose | Who |
|-------|------|---------|-----|
| 1 | Architecture | Blueprint before prose | Showrunner |
| 2 | Drafting | Words on page | Writer |
| 3 | Expansion | Lean chapters to weight | Writer + Editor |
| 4 | Developmental Editorial | Structural assessment | Editor |
| 5 | Targeted Fixes | Priority 1 blockers only | Writer |
| 6 | Line Edit | Prose rhythm, voice | Editor |
| 7 | Copy Edit | Mechanical correctness | Editor |
| 8 | Assembly | Compile + verify | Showrunner |
| 9 | Final QA | Continuity, foreshadowing | Showrunner |
| — | Reader Audit | Fresh-eye experiential read | Reader |
| — | Freeze | Lock the manuscript | Showrunner |

## Core Principles

1. **The manuscript is the ground truth.** Trackers, dashboards, and reports are aspirational. Verify against source files.
2. **Never trust a report that says "fixes applied."** Always spot-check the actual source.
3. **Autonomy triples velocity.** Grant tactical autonomy to the writer; the showrunner only intervenes for blockers.
4. **Handoffs before reports.** Update state files before presenting session summaries.
5. **Discovery before editorial.** Run a pure-inventory Discovery Pass before any editorial assessment.
6. **Copy edit is mechanical only.** No stylistic improvements during Stage 7.
7. **Every book teaches the pipeline.** After completion, update this repository with new lessons.

## Origin

Developed during the production of a three-book cosmic horror-comedy series (2026). The pipeline evolved from a loose 4-pass system to a disciplined 9-stage machine with profile-based agent delegation, comprehensive tracking, and verification protocols. Every rule in this repository exists because something broke first.

## Repository Governance Note

In July 2026, the Arden Studios horror project *The Better Version* was created and its creative material (manuscripts, series architecture, voice guardrails, decision records) was moved to its own private creative repository: `Sirvenis/the-better-version`. This repository now contains only reusable infrastructure. The repository governance model is documented in `docs/REPO_ORGANISATION.md`.

## Licence

MIT — use, adapt, improve. If this helps you produce better novels, the system has done its job.
