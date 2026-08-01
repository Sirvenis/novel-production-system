# Global Install + Anunnaki Specialist Suite Migration Report

Date: 2026-08-01

## Scope

Andrew said to proceed. This pass continued the staged fiction skill split rollout after the limited production trial and individual Anunnaki/horror showrunner migrations.

Actions completed:

- Installed the 9 split skills into the global user-local skill tree alongside the old monolith.
- Migrated the Anunnaki specialist profiles (`anunnaki-writer`, `anunnaki-editor`, `anunnaki-reader`, `anunnaki-researcher`) to the split skill set.
- Did not delete, rewrite, slim, or shim the old `longform-fiction-series-drafting` skill.
- Did not migrate cleanup-audio or Brambleford reader profiles.

## Global user-local skill install

Destination: `/home/andrew/.hermes/skills/creative/`

| Skill | SHA-256 prefix |
|---|---:|
| `controlled-fiction-drafting-and-autonomous-runs` | `dd79fd3786fc9eb0` |
| `controlled-fiction-revision-and-expansion` | `08c5f1830439184e` |
| `controlled-model-evaluation-for-creative-work` | `c10d517de93bd948` |
| `fiction-architecture-briefing-and-research-gates` | `6148ccb435deee7b` |
| `fiction-assembly-final-qa-and-freeze` | `2ddc4783da1d47b8` |
| `fiction-editorial-audits-and-revision-planning` | `868d62cac2f0b2e7` |
| `fiction-project-governance-and-handoffs` | `00cd93443cf83ec1` |
| `longform-fiction-production` | `31165fdd86004239` |
| `reader-package-and-feedback-workflow` | `3c382b419483500e` |

Old global skill safety:

- old skill hash before: `bbd5fd26ec5747a8`
- old skill hash after: `bbd5fd26ec5747a8`
- unchanged: True
- deleted: False

Default `hermes skills list` now shows both the new split skills and the old monolith enabled. This is expected for coexistence; default profile was not slimmed.

## Anunnaki specialist suite migration

| Profile | Old skill enabled? | Old skill disabled? | New split skills enabled |
|---|---:|---:|---:|
| `anunnaki-writer` | False | True | 9 |
| `anunnaki-editor` | False | True | 9 |
| `anunnaki-reader` | False | True | 9 |
| `anunnaki-researcher` | False | True | 9 |

Snapshots and manifests are stored under:

`anunnaki-specialist-profile-migration/`

## Remaining old-skill dependency audit

Updated audit:

`REMAINING_OLD_SKILL_DEPENDENCY_AUDIT.md`

Current interpretation:

- Anunnaki showrunner + Anunnaki specialist suite: migrated/old disabled.
- Fiction profile: migrated/old disabled.
- Horror showrunner: migrated/old disabled.
- Cleanup-audio profiles still explicitly enable the old skill and should be handled through the audiobook workflow, not manuscript-skill rollout.
- `brambleford-reader` uses an older config shape and should be handled separately.
- `wagecheck-dev` only has the old skill in disabled list.

## Decision

Global split-skill install and Anunnaki specialist suite migration: PASS.

## Next safe gate

Do not convert the old global skill to a shim yet. First decide how to handle cleanup-audio profile dependencies and the old Brambleford reader profile shape, or explicitly accept that those profiles will keep using the preserved old monolith until their own migration pass.
