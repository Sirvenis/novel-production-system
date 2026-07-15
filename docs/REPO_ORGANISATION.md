# Repository Organisation

This document explains how this repository is structured and why.

## The Two-Repository Law

Every novel project needs **two repositories**:

1. **This repository** (`novel-production-system`): The production backbone. Reusable infrastructure. Never contains manuscripts.
2. **Your creative repository**: Manuscripts, drafts, bibles, tracking. Never contains production system code.

**Why separate them:**
- The production system evolves independently of any single project
- You can clone the system for multiple projects simultaneously
- Manuscripts are large; production rules are small but valuable
- Version history of craft rules should not be interleaved with chapter drafts

## Directory Structure

### `infrastructure/` — The Reusable Pipeline

Contains the actual production system. These are the documents you read before starting a new project.

| File | What It Contains |
|------|------------------|
| `PRODUCTION_PIPELINE.md` | The 9-stage overview, inputs/outputs per stage |
| `EDITORIAL_STAGES.md` | Each stage in detail: purpose, criteria, verdicts, pitfalls |
| `MULTI_PROFILE_WORKFLOW.md` | How to set up and run profile-based agent delegation |
| `CRAFT_TECHNIQUES.md` | Genre-agnostic craft rules (e.g., job-based word ranges, cadence fatigue) |
| `TRACKING_SYSTEM.md` | Dashboards, trackers, decision logs, status definitions |
| `HANDOFF_SYSTEM.md` | Cross-session state preservation patterns |
| `GIT_WORKFLOW.md` | Commit discipline, branch strategy, message format |
| `EVOLUTION.md` | How this system developed; what failed and was fixed |

### `templates/` — Starting Points

Copy these into your creative repository and fill them in. They are blank or lightly annotated shells.

| File | Use |
|------|-----|
| `ARCHITECTURE_TEMPLATE.md` | Chapter-by-chapter blueprint |
| `CHAPTER_JOB_STATEMENT.md` | Template for defining what a chapter must accomplish |
| `EDITORIAL_REPORT.md` | Report structure for Pass 3 (Developmental Editorial) |
| `READER_AUDIT_TEMPLATE.md` | Fresh-eye audit structure |
| `TRACKER_TEMPLATE.md` | Chapter status tracker |
| `HANDOFF_TEMPLATE.md` | Session-to-session handoff |
| `DECISION_LOG_ENTRY.md` | Decision log entry format |

### `case-studies/` — Evidence, Not Canon

Real data from the project that developed this system, anonymised where appropriate. These prove the system works and show what failure looks like.

| Directory | Contents |
|-----------|----------|
| `horror-series-production/` | 3-book production history: lessons, evolution, failures, corrections |

### `references/` — Deep-Dive Documents

Extended reference documents for specific techniques. These are long-form operational guides.

| File | What It Covers |
|------|----------------|
| `READER_AUDIT_FIVE_QUESTIONS.md` | The Reader Audit method |
| `DEVELOPMENTAL_STRUCTURAL_FOUR_QUESTIONS.md` | Post-expansion structural assessment |
| `TIER_BASED_EXPANSION.md` | How to prioritise chapter expansion |
| `DISCOVERY_PASS_WORKFLOW.md` | Pure-inventory pre-editorial assessment |
| `LINE_EDIT_EXECUTION.md` | Stage 6: prose rhythm, voice, repetition |
| `COPY_EDIT_EXECUTION.md` | Stage 7: mechanical correctness, scope boundaries |
| `ASSEMBLY_FINAL_QA.md` | Stages 8-9: compile, verify, freeze |
| `SCOPE_DISCIPLINE.md` | Series expansion rules (single-frontier) |
| `VERIFICATION_RULE.md` | The "never trust a report" rule in detail |

## What Is NOT in This Repository

- **Manuscripts** — those live in your creative repo
- **API keys, tokens, credentials** — these are in `.gitignore` and must never be committed
- **Machine-specific configuration** — cache files, logs, local paths
- **Full SOUL.md files** — these contain project-specific paths and are in your profiles directory

## How to Use This Repository for a New Project

1. **Read, do not modify.** This is the reference. Copy templates, don't edit originals.
2. **Fork or clone.** If you want to evolve the system for a specific project, fork this repo and modify your fork.
3. **Contribute back.** If you discover a new technique or fix a failure pattern, update this repository.

## Versioning

This repository uses semantic versioning for the pipeline itself:

- **Major:** New stage added or removed, or a stage fundamentally redefined
- **Minor:** New template, new reference document, new technique
- **Patch:** Correction, clarification, or bug fix to existing documentation

Current version: **1.0.0** (established after 3-book production cycle)
