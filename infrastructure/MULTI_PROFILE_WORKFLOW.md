# Multi-Profile Workflow

## What It Is

A production system where multiple Hermes profiles (AI agents) each specialise in a role: Showrunner, Writer, Editor, Reader. The Showrunner coordinates; specialists execute.

## Why It Works

- **Voice consistency:** The Writer profile maintains the narrator's voice across sessions
- **Fresh eyes:** The Reader profile has no memory of editorial debates; it reads as a human would
- **Ruthlessness:** The Editor profile checks what the Writer wants to ignore
- **Parallel work:** Writer drafts while Editor reviews previous book
- **Autonomy:** The Writer operates silently between checkpoints, tripling velocity

## The Four Roles

### 1. Showrunner (Master)

**Name pattern:** `<series>-master` or `<series>` (as in `horror-series`)

**Responsibilities:**
- Coordinates the full pipeline
- Talks to the human author
- Delegates to specialists
- Manages handoffs, git commits, final assembly
- Makes canon decisions
- Never uses fallback-model creative output as canon

**SOUL.md priorities:**
- Confirm pipeline approach before drafting
- Proceed without approval gates where autonomy is granted
- Announce only blockers, session-end summaries, or tool failures
- Handoff before report

**When to use:** Always. This is the primary profile.

### 2. Writer

**Name pattern:** `<series>-writer`

**Responsibilities:**
- Drafts chapters
- Maintains narrator voice
- Targets job-based word ranges
- Commits after each chapter
- Self-edits for contradictions

**SOUL.md priorities:**
- Maintain first-person present tense (or project's chosen POV)
- Follow humor-horror rhythm (or project's chosen rhythm)
- Heartbeat moments every N chapters
- Stop only for blockers or continuity conflicts
- Never use fallback models for canon prose

**When to use:** Stage 2 (Drafting), Stage 3 (Expansion), Stage 5 (Targeted Fixes)

### 3. Editor

**Name pattern:** `<series>-editor`

**Responsibilities:**
- Structural review (Stage 4)
- Line Edit (Stage 6)
- Copy Edit (Stage 7)
- Continuity audit
- Cadence assessment
- Architecture alignment check

**SOUL.md priorities:**
- Never expand manuscripts after review says they have enough body
- Check architecture alignment explicitly
- Grade prose cadence, voice consistency, dialogue clarity
- Do NOT grade "did I like it?" — grade "does it work?"

**When to use:** Stage 4 (Developmental Editorial), Stage 6 (Line Edit), Stage 7 (Copy Edit)

### 4. Reader

**Name pattern:** `<series>-reader`

**Responsibilities:**
- Fresh-eye read (Reader Audit)
- Reports experiential questions: "Where did I stop turning pages?"
- Pacing assessment
- Character engagement
- Ending satisfaction

**SOUL.md priorities:**
- Read cold — no previous passes, no editorial reports
- Report experience, not prescriptions
- Classify findings by severity
- Do NOT do editorial work

**When to use:** Reader Audit (after Pass 3.5 or after Assembly)

### 5. Researcher (Optional)

**Name pattern:** `<series>-researcher`

**Responsibilities:**
- Factual/technical research for the writer
- Verifies scientific, historical, or cultural details
- Maintains a research ledger

**When to use:** Projects requiring heavy factual accuracy (historical, scientific, regional)

## Profile Setup in Hermes

Profiles live in `~/.hermes/profiles/<profile-name>/`.

Each profile needs:

### `SOUL.md`

Role identity, core principles, project paths, style conventions, key constraints.

Example (Writer):
```markdown
You are the chapter drafting agent for [Series Name].

**Core principles:**
- Maintain [POV] voice
- Follow [rhythm rule]
- Target job-based word ranges
- Commit after each chapter

**Project paths:**
- Main project: /home/[user]/[project]/
- Drafts: /home/[user]/[project]/drafts/
- Architecture: /home/[user]/[project]/ARCHITECTURE.md

**Style conventions:**
- [Specific voice rules]
- [Vernacular / diction]
- [Humor-horror balance]

**Key constraints:**
- Never use fallback models for canon prose
- Stop only for blockers
- Announce only blockers, session-end summaries, or tool failures
```

### `config.yaml`

```yaml
model:
  model: your-primary-model
  provider: your-provider
toolsets:
  - hermes-cli
  - terminal
  - file
  - skills
terminal:
  backend: local
  cwd: /home/[user]/[project]/
```

### `profile.yaml` (optional)

Short description for the Hermes UI:
```yaml
name: my-series-writer
description: Chapter drafting agent for My Series
```

## Workflow Patterns

### Pattern A: Serial Delegation (One at a time)

1. Showrunner approves architecture
2. Showrunner delegates drafting to Writer
3. Writer completes, reports back
4. Showrunner delegates editorial to Editor
5. Editor completes, reports back
6. Showrunner delegates Reader Audit to Reader
7. Reader completes, reports back
8. Showrunner assembles and freezes

**Best for:** Small projects, limited compute, when you want tight control.

### Pattern B: Parallel Delegation (Overlapping)

1. Showrunner approves architecture
2. Writer drafts Book N while Editor reviews Book N-1
3. When Writer completes Book N, Editor reviews it
4. While Editor reviews, Reader audits Book N-1
5. Showrunner assembles when all reports are in

**Best for:** Multi-book series, high compute, when you want maximum velocity.

### Pattern C: Autonomy Grant (Continuous Drafting)

1. Showrunner grants Writer tactical autonomy: "Draft chapters 1-17 without approval gates"
2. Writer drafts → self-edit → commit → proceed silently
3. Writer reports only at session end or on blockers
4. Showrunner reviews the complete draft, then delegates editorial

**Best for:** When you trust the Writer and want maximum speed. Used successfully for Book 3 (17 chapters, 33,131 words, single session).

## Handoff Between Profiles

When one profile finishes and another begins, the Showrunner must:

1. Update `handoff/MASTER-HANDOFF.md` with:
   - What was completed
   - Current totals and status
   - Next task for the receiving profile
   - Critical files to read
   - Tone reminders
   - Verification checklist

2. The receiving profile reads:
   - `handoff/MASTER-HANDOFF.md`
   - `tracking/BOOK<N>_DASHBOARD.md`
   - The specific files it needs to work on

3. The receiving profile does NOT read:
   - Previous profile's raw output (unless specifically needed)
   - Editorial reports if it is the Reader (must remain fresh-eyed)

## Session Recovery

When a session starts with "New session started" and a REPORT block:

1. Read `handoff/MASTER-HANDOFF.md`
2. Read `tracking/BOOK<N>_DASHBOARD.md`
3. Read the specific chapter/file being worked on
4. Read adjacent chapters for continuity (one before, one after)
5. Confirm the named next task matches the tracker
6. Proceed silently without asking for confirmation

## Common Pitfalls

- **Profile confusion:** The Showrunner and Writer are not the same. The Showrunner coordinates; the Writer writes.
- **Reader contamination:** The Reader must NOT see editorial reports before reading. Contamination invalidates the audit.
- **Editorial overreach:** The Editor grades structure and prose, not "did I like the story."
- **Writer autonomy without constraints:** Autonomy must include clear constraints (stop for blockers, commit after each chapter, follow architecture).
- **Forgetting handoffs:** Every profile transition needs a handoff. Every session boundary needs a handoff.
