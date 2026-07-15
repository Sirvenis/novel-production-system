# Getting Started with the Novel Production System

## Prerequisites

- Git installed and configured
- A GitHub account
- Hermes Agent (or equivalent AI agent with profile support)
- A project directory for your creative work

## Step 1: Clone This Repository

```bash
git clone https://github.com/Sirvenis/novel-production-system.git
cd novel-production-system
```

This repository is your **production backbone**. You will reference it, not modify it, for each project.

## Step 2: Create Your Creative Repository

```bash
# Create a new repo for your actual novel
cd ~
gh repo create my-novel-project --public --description "My novel — manuscripts, drafts, bibles" --clone

# Set up the directory structure
mkdir -p my-novel-project/{drafts,book-drafts,tracking,handoff,manuscript,archive,outlines}
```

## Step 3: Copy the Templates

```bash
cp novel-production-system/templates/* my-novel-project/templates/
```

## Step 4: Set Up Your Hermes Profiles

Create profiles in `~/.hermes/profiles/`:

```bash
mkdir -p ~/.hermes/profiles/my-novel-master
mkdir -p ~/.hermes/profiles/my-novel-writer
mkdir -p ~/.hermes/profiles/my-novel-editor
mkdir -p ~/.hermes/profiles/my-novel-reader
```

Each profile needs three files:

### `SOUL.md` (Role Identity)

Example for the showrunner (master):

```markdown
You are the showrunner for [Series Name].

**Core principles:**
- Coordinate the full production pipeline
- Never use fallback-model creative output as canon
- Proceed without approval gates where autonomy is granted
- Announce only blockers, session-end summaries, or tool failures

**Project paths:**
- Main project: /home/[user]/[project]/
- Drafts: /home/[user]/[project]/drafts/
- Tracking: /home/[user]/[project]/tracking/
- Handoff: /home/[user]/[project]/handoff/

**Key constraints:**
- All canon decisions require [your-primary-model]
- Silent execution: do not narrate every step
- Handoff before report after every autonomous stage
```

### `config.yaml` (Model and Tools)

```yaml
model:
  model: your-primary-model
  provider: your-provider
  base_url: http://127.0.0.1:11434/v1
  api_mode: chat_completions
providers:
  your-provider:
    base_url: http://127.0.0.1:11434/v1
    models:
      - your-primary-model
toolsets:
  - hermes-cli
  - terminal
  - file
  - skills
  - memory
  - todo
delegation:
  max_concurrent_children: 2
  max_spawn_depth: 1
terminal:
  backend: local
  cwd: /home/[user]/[project]/
  timeout: 180
```

## Step 5: Create Your First Architecture Document

Use the template at `templates/ARCHITECTURE_TEMPLATE.md`.

Key rules:
- Each chapter declares a **Job Statement**: one sentence describing what it must make the reader believe or feel
- Word ranges are job-based, not fixed per chapter
- The architecture is a contract, not a suggestion

## Step 6: Begin the Pipeline

1. Confirm pipeline approach with yourself (or your human):
   - A. Pipeline setup first, then drafting
   - B. Immediate drafting with minimal pipeline
   - C. Full multi-profile pipeline

2. Create `tracking/BOOK1_TRACKER.md` from the template

3. Create `handoff/MASTER-HANDOFF.md` with initial project state

4. Begin Stage 1: Architecture → Stage 2: Drafting

## Common First-Time Mistakes

- **Assuming "proceed to drafting" means immediate chapter writing.** It means confirm pipeline, then draft. Always confirm first.
- **Drafting without a tracker.** The tracker is your ground truth for what exists vs. what should exist.
- **Not updating handoffs between sessions.** Every session ends with a handoff update. Every session starts by reading it.
- **Trusting reports over source files.** If a report says "fixed," verify the actual file.

## Verification Checklist (Before First Draft)

- [ ] Architecture document exists with Job Statements for every chapter
- [ ] Tracker exists with status column
- [ ] Master handoff exists with project state
- [ ] Git remote configured
- [ ] Profiles created with correct paths
- [ ] At least one template copied to project directory
- [ ] Decision log file created (`tracking/DECISIONS.md`)

## Next Steps

- Read `infrastructure/PRODUCTION_PIPELINE.md` for the full stage map
- Read `infrastructure/EDITORIAL_STAGES.md` for stage-by-stage details
- Read `case-studies/horror-series-production/` for real examples of how this works in practice
