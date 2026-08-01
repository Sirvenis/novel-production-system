# Fiction Skill Split Phase Closure Report

Date: 2026-08-01

## Decision

This phase is complete.

The new split fiction skill system is production-ready for migrated profiles, while the old `longform-fiction-series-drafting` monolith remains preserved as an archive/fallback. Do not shim, delete, or slim the old global monolith yet.

## Completed rollout scope

- Project-specific legacy references preserved in canonical project repos.
- Cross-series/general references condensed into task-class linked references.
- High-impact runtime/deployment/model/profile references quarantined.
- Test-only `fiction-skill-canary` profile installed and passed routing canary.
- `fiction` profile migrated and old monolith disabled there.
- Limited production trial on copied/non-canonical sandbox material passed.
- `anunnaki` showrunner profile migrated and passed routing/governance canaries.
- `horror-series` showrunner profile migrated and passed routing/governance canaries.
- Global split skills installed alongside old monolith.
- Anunnaki specialist suite migrated: writer/editor/reader/researcher.

## Global skill state

Old monolith:

- Path: `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/SKILL.md`
- SHA-256 prefix: `bbd5fd26ec5747a8`
- Preserved unchanged: yes
- Deleted: no
- Shimmed: no

New global split skills:

| Skill | Present | SHA-256 prefix |
|---|---:|---:|
| `longform-fiction-production` | True | `31165fdd86004239` |
| `fiction-project-governance-and-handoffs` | True | `00cd93443cf83ec1` |
| `fiction-architecture-briefing-and-research-gates` | True | `6148ccb435deee7b` |
| `controlled-fiction-drafting-and-autonomous-runs` | True | `dd79fd3786fc9eb0` |
| `fiction-editorial-audits-and-revision-planning` | True | `868d62cac2f0b2e7` |
| `controlled-fiction-revision-and-expansion` | True | `08c5f1830439184e` |
| `fiction-assembly-final-qa-and-freeze` | True | `2ddc4783da1d47b8` |
| `reader-package-and-feedback-workflow` | True | `3c382b419483500e` |
| `controlled-model-evaluation-for-creative-work` | True | `c10d517de93bd948` |

## Migrated profile state

| Profile | Old skill enabled? | Old skill disabled? | New split skills enabled |
|---|---:|---:|---:|
| `fiction` | False | True | 0 |
| `anunnaki` | False | True | 9 |
| `anunnaki-writer` | False | True | 9 |
| `anunnaki-editor` | False | True | 9 |
| `anunnaki-reader` | False | True | 9 |
| `anunnaki-researcher` | False | True | 9 |
| `horror-series` | False | True | 9 |

Note: `fiction` uses a broad disabled-list profile pattern and consumes globally installed split skills; its `new split skills enabled` count here reflects explicit config entries only, not global availability.

## Remaining old-skill consumers intentionally left alone

See: `REMAINING_OLD_SKILL_DEPENDENCY_AUDIT.md`

- cleanup-audio profiles still explicitly enable the old monolith. Leave these for a separate audiobook workflow review.
- `brambleford-reader` uses an older config shape and should receive a separate reader-profile review, not a blind production-skill swap.
- Disabled-list references in migrated profiles are expected and harmless.

## Operational recommendation

Use the new split skills going forward in:

- `fiction`
- `anunnaki`
- `anunnaki-writer`
- `anunnaki-editor`
- `anunnaki-reader`
- `anunnaki-researcher`
- `horror-series`
- default/global when explicitly loading `longform-fiction-production`

Keep old `longform-fiction-series-drafting` available as preserved fallback/archive until real usage across several sessions shows no regressions.

## Stop condition

Stop skill-system migration work here unless Andrew specifically asks to review cleanup-audio, Brambleford reader, or old-monolith shim/deletion.

Recommended return to normal work: actual fiction/library/audio production using the new migrated profiles.
