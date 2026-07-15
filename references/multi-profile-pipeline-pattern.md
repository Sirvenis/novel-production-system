# Multi-Profile Pipeline Pattern (from Elias Silver / Meridian / Mystery Projects)

**Context:** Discovered during Book 2 pipeline planning. User asked: "do you have a pipeline working in the background, using various profiles, writing, editing, etc?" and "Maybe have a look at some of the other repos and see what we are doing there."

---

## What I Found

The user runs multi-book series across several projects with a consistent profile-based pipeline:

### Profile Roles

| Role | Typical Name Pattern | SOUL.md Purpose |
|------|---------------------|-----------------|
| **Master / Showrunner** | `<series>-master` | Coordinates, manages handoffs, talks to user, delegates |
| **Writer** | `<series>-writer` | Drafts chapters, voice consistency, word counts |
| **Editor** | `<series>-editor` | Structural reviews, continuity, prose cadence |
| **Reader** | `<series>-reader` | Engagement audit, pacing, release-readiness verdict |
| **Researcher** | `<series>-researcher` | Factual/technical research for the writer |

### Examples Found

- **Elias Silver / Anunnaki:** `elias-master`, `elias-writer`, `elias-editor`, `elias-reader`, `elias-researcher`
- **Meridian Relics:** `meridian-master`, `meridian-writer`, `meridian-editor`, `meridian-reader`, `meridian-researcher`
- **Brambleford / Mystery:** `mystery-editor`, `mystery-characters`, `mystery-dialogue`, `brambleford-reader`, `anunnaki-reader`

### Handoff Pattern

- `handoff/sessionN-handoff.md` — created after each session, includes status, next steps, verification checklist
- `handoff/snapshots/` — timestamped copies of current handoff (some projects have `save-current-handoff.sh`)
- Handoffs include: what was accomplished, current totals, next decision point, critical files, tone reminders, verification checklist

### 4-Pass Pipeline (Universal)

1. **Pass 1: Expansion/Drafting** — Writer profile, session by session
2. **Pass 2: Editorial Review** — Editor profile, continuity + structure
3. **Pass 3: Reader Audit** — Reader profile, "would I keep reading?"
4. **Pass 4: Final Polish + Assembly** — Master profile, compile, release

### SOUL.md Constraints

- Master: "Use gpt-5.5 / OpenAI Codex as primary model for canon/prose decisions"
- Writer: "Never use fallback models — only gpt-5.5 output is canon"
- Reader: "Internal gate — not outside reader packaging"
- Editor: "Never expand manuscripts after review says they have enough body"

### Session Work Pattern

- User checks in, asks for status
- Master reports progress, asks for direction
- User approves next step (or asks for options)
- Master delegates to writer/editor/reader as appropriate
- After work completes, master creates handoff, reports to user

---

## Profile Implementation (Hermes)

Profiles live in `~/.hermes/profiles/<profile-name>/`.

Each profile needs three files:

| File | Purpose |
|------|---------|
| `SOUL.md` | Role definition, constraints, project paths, what the agent owns |
| `profile.yaml` | Short description for Hermes UI |
| `config.yaml` | Model, provider, toolsets, terminal cwd, max turns |

### SOUL.md Structure
- Role identity ("You are the X agent for...")
- Core principles (what the agent must do)
- What it owns (specific deliverables)
- Project paths (absolute paths to repo, drafts, handoffs)
- Style conventions (if writer)
- Key constraints (never use fallback, never expand, etc.)

### config.yaml Key Settings
- `model.model` and `model.provider` — primary model for canon work
- `fallback_providers` — ordered list if primary fails
- `toolsets` — what tools the profile can use (writer gets terminal+file; reader gets file only)
- `agent.max_turns` — writer gets 80; editor 60; reader 50; master 120
- `terminal.cwd` — repo root

### Creating a New Profile

```bash
mkdir -p ~/.hermes/profiles/<profile-name>
```

Then create the three files. No registration needed — Hermes discovers profiles at startup.

## Application to The Last Clean-Up Crew

**Current state:** Book 1 used single `horror-series` profile for everything. User's other projects use multi-profile.

**Decision needed:** Does user want multi-profile for Book 2, or is single-profile acceptable?

**If multi-profile:** Create `horror-series-writer`, `horror-series-editor`, `horror-series-reader` profiles with SOUL.md files matching the Elias/Meridian pattern.

**If single-profile:** Still follow the 4-pass pipeline and handoff pattern, just within the one profile.

---

*Reference: discovered 2026-07-15 during Book 2 pipeline planning session.*
