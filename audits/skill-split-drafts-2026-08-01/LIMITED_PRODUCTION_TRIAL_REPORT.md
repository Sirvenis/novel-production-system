# Limited Production Trial Report — Fiction Profile Split Skills

Date: 2026-08-01

## Scope

Andrew said to proceed after the fiction-profile old-skill disablement canary. This pass ran the next staged step: a limited production trial on copied/non-canonical material.

The trial used the real `fiction` profile with the new split skills available and the old monolithic `longform-fiction-series-drafting` disabled in that profile.

No canonical fiction repository was used as the work target.

## Sandbox target

`/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/limited-production-trial/sandbox-fiction-project`

Sandbox status:

- disposable/non-canonical project
- prose authorized only for one short sample chapter
- forbidden from touching canonical fiction repos or live Hermes files

## Command/output

Prompt:

`limited-production-trial/fiction-profile-production-trial-prompt.txt`

Captured output:

`limited-production-trial/fiction-profile-production-trial-output.txt`

Canary session:

`20260801_210842_8c25ac`

## Result

PASS.

Files produced/updated inside sandbox:

- `manuscript/chapters/chapter-01.md`
- `PROJECT_STATUS.yml`
- `handoff/CURRENT_PROJECT_HANDOFF.md`
- `reports/CHAPTER_01_COMPLETION_REPORT.md`
- `SANDBOX_GIT_METADATA.md`

Chapter verification:

- Title: `Chapter 1 — The Lantern at Milepost 9`
- Word count including title: 990
- Word count excluding markdown title: 981
- Target: 700-1,000 words
- Stop condition: Chapter 1 only

Sandbox git verification before parent preservation:

- Sandbox commit: `8f49c4ee79fab89272acbfe0a8d72740d7e324e3`
- Sandbox working tree: clean after commit
- Nested `.git` removed after verification so parent repo can track files normally

## Scope verification

Canonical fiction repos checked clean after the trial:

- `/home/andrew/projects/active/anunnaki-chronicles-novel`
- `/home/andrew/projects/active/meridian-relics`
- `/home/andrew/projects/active/brambleford-cozy-mystery`
- `/home/andrew/projects/active/last-clean-up-crew`
- `/home/andrew/the-better-version`

Live Hermes safety:

- No live global skill slimming performed.
- No old references deleted or moved.
- No default or series profile migration performed.
- `fiction` profile old-skill disablement from the prior gate remains in place.

## Quality notes

The sample chapter followed the brief: rain-lashed rail setting, competent protagonist, one unsettling discovery, and a stop before solving the mystery. The workflow produced the expected manuscript file, status update, handoff update, report, and sandbox commit.

## Decision

Limited production trial on copied/non-canonical material: PASS.

## Next staged migration gate

Do not globally slim the old skill yet.

Recommended next step:

1. Migrate the `anunnaki` profile individually to the new split-skill model, preserving old skill/global files.
2. Run Anunnaki-specific dry-run canaries first (governance, architecture/research, no prose unless explicitly authorized by repo status).
3. Only after Anunnaki passes, repeat for `horror-series`.
4. Convert global old skill to compatibility shim only after dependent profiles pass.
