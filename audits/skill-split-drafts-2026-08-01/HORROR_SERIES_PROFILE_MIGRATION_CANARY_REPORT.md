# Horror-Series Profile Migration Canary Report — Fiction Skill Split

Date: 2026-08-01

## Scope

This pass migrated the `horror-series` Hermes profile individually to the new staged fiction split skills, after the `fiction` and `anunnaki` migrations/canaries passed.

This was a horror-series-profile-only migration. No global skill slimming was performed.

## Profile changed

- Profile: `horror-series`
- Path: `/home/andrew/.hermes/profiles/horror-series`
- Model remains: `kimi-k2.6:cloud` via `ollama-launch`
- Workdir remains: `/home/andrew/projects/active/last-clean-up-crew`
- SOUL.md unchanged

## Skill changes

The old monolith was removed from `skills.enabled` and added to `skills.disabled` in the `horror-series` profile config:

- disabled old skill: `creative/longform-fiction-series-drafting`
- global old skill deleted: no
- global old skill hash remains: `bbd5fd26ec5747a8`

The 9 split skills were installed into the horror-series profile skill tree:

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

`horror-series-profile-migration/`

Files:

- `before-config.yaml`
- `after-config.yaml`
- `before-SOUL.md`
- `after-SOUL.md`
- `HORROR_SERIES_PROFILE_MIGRATION_MANIFEST.json`

## Routing canary

Prompt:

`horror-series-profile-migration/horror-routing-canary-prompt.txt`

Output:

`horror-series-profile-migration/horror-routing-canary-output.txt`

Result: PASS.

The horror-series profile routed:

1. fresh-session governance → `fiction-project-governance-and-handoffs`
2. Book 4 architecture/research → `fiction-architecture-briefing-and-research-gates`
3. approved single chapter drafting → `controlled-fiction-drafting-and-autonomous-runs`
4. read-only editorial audit → `fiction-editorial-audits-and-revision-planning`
5. final assembly/QA/freeze → `fiction-assembly-final-qa-and-freeze`

The canary output explicitly reported `OLD_SKILL_USED: no`.

## Read-only governance canary

Prompt:

`horror-series-profile-migration/horror-governance-canary-prompt.txt`

Output:

`horror-series-profile-migration/horror-governance-canary-output.txt`

Result: PASS.

The profile correctly identified:

- canonical repo: `/home/andrew/projects/active/last-clean-up-crew`
- current gate: Books 1-3 frozen/ready; Book 4 architecture pending
- prose authorized: no
- git state: clean, main up to date with origin/main
- next safe action: catalogue source-path update or Book 4 architecture/research gate when Andrew requests it

## Isolation verification

- No canonical Last Clean-Up Crew files changed.
- No manuscript/prose written.
- No global old skill deleted or modified.
- No default profile changes.
- No other series profile migration performed in this pass.

## Decision

Horror-series profile migration canary: PASS.

## Next staged migration gate

Audit remaining profile references to `creative/longform-fiction-series-drafting`. If no critical dependent profile still requires the old monolith, prepare or execute the compatibility-shim conversion according to Andrew's active approval. Preserve the old full skill and references in an archive snapshot before any shim conversion.
