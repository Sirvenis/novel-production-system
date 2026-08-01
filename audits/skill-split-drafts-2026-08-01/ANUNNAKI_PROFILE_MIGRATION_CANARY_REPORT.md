# Anunnaki Profile Migration Canary Report — Fiction Skill Split

Date: 2026-08-01

## Scope

This pass migrated the `anunnaki` Hermes profile individually to the new staged fiction split skills, following the staged rollout after the `fiction` profile limited production trial passed.

This was an Anunnaki-profile-only migration. No global skill slimming was performed.

## Profile changed

- Profile: `anunnaki`
- Path: `/home/andrew/.hermes/profiles/anunnaki`
- Model remains: `gpt-5.5` via `openai-codex`
- Workdir remains: `/home/andrew/projects/active/anunnaki-chronicles-novel`
- SOUL.md unchanged

## Skill changes

The old monolith was removed from `skills.enabled` and added to `skills.disabled` in the `anunnaki` profile config:

- disabled old skill: `creative/longform-fiction-series-drafting`
- global old skill deleted: no
- global old skill hash remains: `bbd5fd26ec5747a8`

The 9 split skills were installed into the Anunnaki profile skill tree:

| Skill | Installed | SHA-256 prefix |
|---|---:|---:|
| `controlled-fiction-drafting-and-autonomous-runs` | yes | `dd79fd3786fc9eb0` |
| `controlled-fiction-revision-and-expansion` | yes | `08c5f1830439184e` |
| `controlled-model-evaluation-for-creative-work` | yes | `c10d517de93bd948` |
| `fiction-architecture-briefing-and-research-gates` | yes | `6148ccb435deee7b` |
| `fiction-assembly-final-qa-and-freeze` | yes | `2ddc4783da1d47b8` |
| `fiction-editorial-audits-and-revision-planning` | yes | `868d62cac2f0b2e7` |
| `fiction-project-governance-and-handoffs` | yes | `00cd93443cf83ec1` |
| `longform-fiction-production` | yes | `31165fdd86004239` |
| `reader-package-and-feedback-workflow` | yes | `3c382b419483500e` |

## Config snapshot

Snapshots stored under:

`anunnaki-profile-migration/`

Files:

- `before-config.yaml`
- `after-config.yaml`
- `before-SOUL.md`
- `after-SOUL.md`
- `ANUNNAKI_PROFILE_MIGRATION_MANIFEST.json`

## Routing canary

Prompt:

`anunnaki-profile-migration/anunnaki-routing-canary-prompt.txt`

Output:

`anunnaki-profile-migration/anunnaki-routing-canary-output.txt`

Result: PASS.

The Anunnaki profile routed:

1. fresh-session governance → `fiction-project-governance-and-handoffs`
2. Book 4 architecture/research → `fiction-architecture-briefing-and-research-gates`
3. approved single chapter drafting → `controlled-fiction-drafting-and-autonomous-runs`
4. read-only editorial audit → `fiction-editorial-audits-and-revision-planning`
5. final assembly/QA/freeze → `fiction-assembly-final-qa-and-freeze`

The canary output explicitly reported `OLD_SKILL_USED: no`.

## Read-only governance canary

Prompt:

`anunnaki-profile-migration/anunnaki-governance-canary-prompt.txt`

Output:

`anunnaki-profile-migration/anunnaki-governance-canary-output.txt`

Result: PASS.

The profile correctly identified:

- canonical repo: `/home/andrew/projects/active/anunnaki-chronicles-novel`
- current gate: Book 4 targeted developmental revision plan complete, awaiting Andrew review
- prose authorized: no
- git state: clean, main tracking origin/main
- next safe action: Andrew read-only review/discussion of `book4/reports/book4-targeted-developmental-revision-plan.md`

## Isolation verification

- No canonical Anunnaki files changed.
- No manuscript/prose written.
- No global old skill deleted or modified.
- No default profile changes.
- No other series profile migration performed in this pass.

## Decision

Anunnaki profile migration canary: PASS.

## Next staged migration gate

Migrate `horror-series` individually to the new split-skill model, then run horror-specific routing/governance canaries. Do not globally slim or shim the old skill until dependent profiles pass.
