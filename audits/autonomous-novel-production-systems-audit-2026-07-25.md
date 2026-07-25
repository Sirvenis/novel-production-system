# Autonomous Novel Production Systems Audit — 2026-07-25

Scope: compare the actual autonomous novel-production infrastructure, The Last Clean-Up Crew/horror-series profile family, The Better Version profile family, and other known fiction profile/SOUL setups. This is read-only: no profile/config/manuscript changes were made.

## Executive findings

1. `/home/andrew/novel-production-system/` is the populated canonical reusable infrastructure repo. It contains the mature Stage 0 + 9-stage production pipeline, templates, multi-profile workflow, case studies, and handoff/tracking systems.
2. `/home/andrew/kimi/horror-series-1/novel-production-system/` is an empty nested clone of `Sirvenis/novel-production-system` with no visible files beyond `.git/`. It is not currently the working production system.
3. The `horror-series` profile family is real and project-specific: showrunner, writer, editor, reader all point to `/home/andrew/kimi/horror-series-1` and use `kimi-k2.6:cloud` via `ollama-launch`.
4. The Better Version also has a complete 4-profile family and a canonical series-level SOUL plus SERIES_LENGTH_STANDARD in `/home/andrew/the-better-version/series/`.
5. Series-level SOUL coverage is uneven. The Better Version has canonical series governance. Last Clean-Up Crew has a strong proposal SOUL in the Arden collaboration repo, but not yet migrated to the canonical horror project root. Brambleford, Anunnaki, and Meridian appear to have role/profile SOULs or project bibles, but no root series-level SOUL found in the audited canonical repos.
6. Genre-level SOUL is not enough. The two horror series already prove this: Last Clean-Up Crew is working-class cosmic/environmental horror-comedy; The Better Version is identity-replacement psychological horror. They need separate series SOULs and separate profile families.

## Repository / filesystem state

| Area | Path | Exists | Git | Branch | Ahead | Behind | Working tree | Head | Remote |
|---|---|---|---|---|---:|---:|---|---|---|
| Novel Production System infrastructure | `/home/andrew/novel-production-system` | yes | yes | `main` | 0 | 0 | clean | `5d2d8cd Update pipeline with Better Version matured stages: Stage 0 Voice Test, Voice Guardrails, Confidence Test, 3 new templates, README update` | `https://github.com/Sirvenis/novel-production-system.git` |
| Last Clean-Up Crew / Kimi Horror Lab | `/home/andrew/kimi` | yes | yes | `main` | 0 | 0 | ?? horror-series-1/novel-production-system/ | `0d648f4 Add CANONICAL_RECORD.md: frozen trilogy state, verified word counts, header standardisation confirmed` | `https://github.com/Sirvenis/kimi-horror-lab.git` |
| Last Clean-Up Crew project subdir | `/home/andrew/kimi/horror-series-1` | yes | yes | `main` | 0 | 0 | ?? novel-production-system/ | `0d648f4 Add CANONICAL_RECORD.md: frozen trilogy state, verified word counts, header standardisation confirmed` | `https://github.com/Sirvenis/kimi-horror-lab.git` |
| Nested horror novel-production-system | `/home/andrew/kimi/horror-series-1/novel-production-system` | yes | yes | `master` | ? | ? | clean | `` | `https://github.com/Sirvenis/novel-production-system.git` |
| The Better Version | `/home/andrew/the-better-version` | yes | yes | `main` | 0 | 0 | clean | `710d36d Book 2: Update SERIES_RECORD and MASTER_HANDOFF — Stage 6 Line Edit complete, canonical terminology fixed` | `https://github.com/Sirvenis/the-better-version.git` |
| Brambleford Mysteries | `/home/andrew/projects/active/brambleford-cozy-mystery` | yes | yes | `main` | 0 | 0 | clean | `52b0764 docs: add Book 1 production readiness report` | `https://github.com/Sirvenis/brambleford-cozy-mystery.git` |
| Anunnaki Chronicles | `/home/andrew/projects/active/anunnaki-chronicles-novel` | yes | yes | `main` | 0 | 0 | clean | `7c96af0 [scout] chore: Add archive/audio-drama-june-2026 to .gitignore` | `https://github.com/Sirvenis/anunnaki-chronicles-novel.git` |
| Meridian Relics | `/home/andrew/projects/active/meridian-relics` | yes | yes | `main` | 0 | 0 | clean | `03133f6 [kimi] docs: Add 'This Series Makes These Promises' page` | `https://github.com/Sirvenis/meridian-relics.git` |
| Arden-Hermes Collaboration | `/home/andrew/projects/active/arden-hermes-collaboration` | yes | yes | `main` | 0 | 0 | clean | `5670a60 docs: update Health WageCheck v10 redeploy report` | `https://github.com/Sirvenis/arden-hermes-collaboration.git` |

## Production-system file reality

| Item | Path | Exists |
|---|---|---|
| NPS production pipeline | `/home/andrew/novel-production-system/infrastructure/PRODUCTION_PIPELINE.md` | yes |
| NPS multi-profile workflow | `/home/andrew/novel-production-system/infrastructure/MULTI_PROFILE_WORKFLOW.md` | yes |
| NPS SOUL template | `/home/andrew/novel-production-system/templates/SOUL_MD_PATTERN.md` | yes |
| Horror master handoff | `/home/andrew/kimi/horror-series-1/handoff/MASTER-HANDOFF.md` | yes |
| Horror Book2 pipeline | `/home/andrew/kimi/horror-series-1/BOOK2_PIPELINE.md` | yes |
| Horror Book3 pipeline | `/home/andrew/kimi/horror-series-1/BOOK3_PIPELINE.md` | yes |
| Horror canonical record | `/home/andrew/kimi/horror-series-1/CANONICAL_RECORD.md` | yes |
| Horror series bible | `/home/andrew/kimi/horror-series-1/SERIES_BIBLE.md` | yes |
| Better Version master handoff | `/home/andrew/the-better-version/handoff/MASTER_HANDOFF.md` | yes |
| Better Version series soul | `/home/andrew/the-better-version/series/SERIES_SOUL.md` | yes |
| Better Version length standard | `/home/andrew/the-better-version/series/SERIES_LENGTH_STANDARD.md` | yes |
| Better Version series bible | `/home/andrew/the-better-version/series/SERIES_BIBLE.md` | yes |

Nested horror `novel-production-system/` visible file count excluding `.git/`: **0**.
Conclusion: nested folder is `.git` only / empty checkout state. Treat as accidental or incomplete clone, not live infrastructure.

## Hermes profile integrity

| Profile | SOUL exists | SOUL first line | Generic Hermes SOUL? | Model | Provider | terminal.cwd |
|---|---|---|---|---|---|---|
| `horror-series` | yes | You are the showrunner for The Last Clean-Up Crew series under the Elias Silver pen name. | no | `kimi-k2.6:cloud` | `ollama-launch` | `/home/andrew/kimi/horror-series-1` |
| `horror-series-writer` | yes | You are the chapter drafting agent for The Last Clean-Up Crew series under the Elias Silver pen name. | no | `kimi-k2.6:cloud` | `ollama-launch` | `/home/andrew/kimi/horror-series-1` |
| `horror-series-editor` | yes | You are the editorial review agent for The Last Clean-Up Crew series under the Elias Silver pen name. | no | `kimi-k2.6:cloud` | `ollama-launch` | `/home/andrew/kimi/horror-series-1` |
| `horror-series-reader` | yes | You are the internal reader agent for The Last Clean-Up Crew series under the Elias Silver pen name. | no | `kimi-k2.6:cloud` | `ollama-launch` | `/home/andrew/kimi/horror-series-1` |
| `better-version` | yes | You are the showrunner for The Better Version series. | no | `kimi-k2.6:cloud` | `ollama-launch` | `/home/andrew/the-better-version` |
| `better-version-writer` | yes | You are the chapter drafting agent for The Better Version series. | no | `kimi-k2.6:cloud` | `ollama-launch` | `/home/andrew/the-better-version` |
| `better-version-editor` | yes | You are the editorial review agent for The Better Version series. | no | `kimi-k2.6:cloud` | `ollama-launch` | `/home/andrew/the-better-version` |
| `better-version-reader` | yes | You are the fresh-eye reader for The Better Version series. | no | `kimi-k2.6:cloud` | `ollama-launch` | `/home/andrew/the-better-version` |
| `brambleford-reader` | yes | # Brambleford Commercial Reader Agent | no | `kimi-k2.6:cloud` | `ollama-launch` | `` |
| `anunnaki-reader` | yes | # Anunnaki Reader | no | `kimi-k2.6:cloud` | `ollama-launch` | `/home/andrew/projects/scout/anunnaki-scout-edits` |
| `meridian-master` | yes | You are the Meridian Relics Series Showrunner and production coordinator. | no | `nvidia/nemotron-3-super-120b-a12b:free` | `openrouter` | `/home/andrew/projects/active/elias-silver-library` |
| `meridian-writer` | yes | You are the Meridian Relics Chapter Drafting Agent. | no | `nvidia/nemotron-3-super-120b-a12b:free` | `openrouter` | `/home/andrew/projects/active/elias-silver-library` |
| `meridian-editor` | yes | You are the Meridian Relics Developmental Editor. | no | `nvidia/nemotron-3-super-120b-a12b:free` | `openrouter` | `/home/andrew/projects/active/elias-silver-library` |
| `meridian-reader` | yes | You are the Meridian Relics Internal Reader Agent. | no | `nvidia/nemotron-3-super-120b-a12b:free` | `openrouter` | `/home/andrew/projects/active/elias-silver-library` |
| `meridian-researcher` | yes | You are the Meridian Relics Research Agent. | no | `nvidia/nemotron-3-super-120b-a12b:free` | `openrouter` | `/home/andrew/projects/active/elias-silver-library` |

## Series-level SOUL coverage

| Candidate | Exists | First line / status |
|---|---|---|
| `/home/andrew/kimi/horror-series-1/SOUL.md` | NO |  |
| `/home/andrew/the-better-version/series/SERIES_SOUL.md` | yes | # SERIES_SOUL.md |
| `/home/andrew/the-better-version/SOUL.md` | NO |  |
| `/home/andrew/projects/active/brambleford-cozy-mystery/SOUL.md` | NO |  |
| `/home/andrew/projects/active/anunnaki-chronicles-novel/SOUL.md` | NO |  |
| `/home/andrew/projects/active/meridian-relics/SOUL.md` | NO |  |
| `/home/andrew/projects/active/arden-hermes-collaboration/proposals/pilots/last-clean-up-crew/SERIES_SOUL.md` | yes | # Series-Level SOUL.md |
| `/home/andrew/projects/active/arden-hermes-collaboration/proposals/pilots/better-version/SERIES_SOUL.md` | yes | # SERIES_SOUL.md |

## Comparison by system

### Last Clean-Up Crew / `horror-series`
- Active profile family exists: showrunner, writer, editor, reader.
- All four audited profiles use `kimi-k2.6:cloud` and `terminal.cwd=/home/andrew/kimi/horror-series-1`.
- Project has `BOOK2_PIPELINE.md`, `BOOK3_PIPELINE.md`, `SERIES_BIBLE.md`, `CHARACTER_BIBLE.md`, `STORYCRAFT_HANDBOOK.md`, `CANONICAL_RECORD.md`, and `handoff/MASTER-HANDOFF.md`.
- Weakness: canonical root `SOUL.md` / `SERIES_LENGTH_STANDARD.md` are not present in `/home/andrew/kimi/horror-series-1/`; the detailed series-level SOUL exists as a proposal under Arden collaboration.
- Cleanup issue: nested `/home/andrew/kimi/horror-series-1/novel-production-system/` is an empty clone and causes `/home/andrew/kimi` to stay dirty as untracked.

### The Better Version
- Complete profile family exists: showrunner, writer, editor, reader.
- Canonical series-level files exist in `/home/andrew/the-better-version/series/`: `SERIES_SOUL.md`, `SERIES_LENGTH_STANDARD.md`, `SERIES_BIBLE.md`.
- This is the cleanest example of the newer pattern: series identity and length standard live in the creative repo, role SOULs live in Hermes profiles.
- It should be the model for migrating Last Clean-Up Crew governance.

### Brambleford
- Canonical repo exists and is clean. A project AGENTS.md with role rules exists, and `brambleford-reader` profile exists.
- Only `brambleford-reader` was found in the default profile scan; Predator has additional Brambleford profiles according to prior project notes, but this audit did not run active work on Predator.
- No root `SOUL.md` found in `/home/andrew/projects/active/brambleford-cozy-mystery/` during this audit. Brambleford should eventually receive its own series-level SOUL because it is family/cozy mystery, not generic mystery.

### Anunnaki
- Canonical repo exists and is clean. `anunnaki-reader` profile exists.
- No root `SOUL.md` found in the canonical repo during this audit. Anunnaki has extensive bibles/spines, but should have a concise series-level SOUL defining mythic science-fiction identity, pace, palette, canon boundaries, and expansion rules.

### Meridian Relics
- Canonical repo exists and is clean. Meridian has a fuller profile family: master, writer, editor, reader, researcher.
- Current audited Meridian profile configs still point `terminal.cwd` at `/home/andrew/projects/active/elias-silver-library`, not `/home/andrew/projects/active/meridian-relics`. This may be stale after repo separation and should be reviewed before running autonomous Meridian work.
- No root `SOUL.md` found in `/home/andrew/projects/active/meridian-relics/` during this audit.

## Recommended clean architecture

1. Keep exactly one canonical reusable infrastructure repo: `/home/andrew/novel-production-system/` / `Sirvenis/novel-production-system`.
2. Each creative series repo should contain its own series identity documents: `SOUL.md` or `series/SERIES_SOUL.md`, `SERIES_LENGTH_STANDARD.md`, `SERIES_BIBLE.md`, book architecture, trackers, handoffs, and reports.
3. Each active series should have one profile family: `<series>`, `<series>-writer`, `<series>-editor`, `<series>-reader`; add `<series>-researcher` only when the genre needs factual research.
4. Role profile SOULs should stay in `~/.hermes/profiles/<profile>/SOUL.md`; series-level SOULs should stay in the canonical creative repo. Do not confuse the two.
5. Use The Better Version as the current best-practice pattern for SOUL/length governance.
6. Migrate Last Clean-Up Crew proposal SOUL into the canonical horror project root before Book 4 architecture. Add a matching `SERIES_LENGTH_STANDARD.md`.
7. Review/fix Meridian profile `terminal.cwd` before using those profiles again, because the source repo has separated from Elias Library.
8. Decide what to do with the empty nested `horror-series-1/novel-production-system/`: either remove it from the horror repo workspace, replace it with a README pointer to `/home/andrew/novel-production-system/`, or turn it into a git submodule intentionally. Do not leave it as an accidental untracked nested repo.

## Suggested next actions, in order

1. Commit this audit to `Sirvenis/novel-production-system`.
2. Create a migration plan for Last Clean-Up Crew: move/copy approved `SERIES_SOUL.md` proposal into `/home/andrew/kimi/horror-series-1/series/` or root, add `SERIES_LENGTH_STANDARD.md`, and update `CANONICAL_RECORD.md` / `MASTER-HANDOFF.md`.
3. Fix or document the empty nested `horror-series-1/novel-production-system/` after Andrew approves the intended handling.
4. Make a second pass over Brambleford, Anunnaki, and Meridian to create/migrate series-level SOULs one at a time, not all at once.
5. Patch Meridian profile cwd only after explicit approval, because it changes Hermes profile runtime behaviour.
