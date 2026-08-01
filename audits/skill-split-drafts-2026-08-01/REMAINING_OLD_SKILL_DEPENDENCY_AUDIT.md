# Remaining Old Skill Dependency Audit

Date: 2026-08-01

Search target: `/home/andrew/.hermes/profiles/*/config.yaml` for `longform-fiction-series-drafting`.

| Profile | State | Config |
|---|---|---|
| `anunnaki` | `disabled` | `/home/andrew/.hermes/profiles/anunnaki/config.yaml` |
| `anunnaki-editor` | `enabled` | `/home/andrew/.hermes/profiles/anunnaki-editor/config.yaml` |
| `anunnaki-reader` | `enabled` | `/home/andrew/.hermes/profiles/anunnaki-reader/config.yaml` |
| `anunnaki-researcher` | `enabled` | `/home/andrew/.hermes/profiles/anunnaki-researcher/config.yaml` |
| `anunnaki-writer` | `enabled` | `/home/andrew/.hermes/profiles/anunnaki-writer/config.yaml` |
| `brambleford-reader` | `enabled` | `/home/andrew/.hermes/profiles/brambleford-reader/config.yaml` |
| `cleanup-audio-casting` | `enabled` | `/home/andrew/.hermes/profiles/cleanup-audio-casting/config.yaml` |
| `cleanup-audio-prep` | `enabled` | `/home/andrew/.hermes/profiles/cleanup-audio-prep/config.yaml` |
| `cleanup-audio-producer` | `enabled` | `/home/andrew/.hermes/profiles/cleanup-audio-producer/config.yaml` |
| `cleanup-audio-publisher` | `enabled` | `/home/andrew/.hermes/profiles/cleanup-audio-publisher/config.yaml` |
| `cleanup-audio-qa` | `enabled` | `/home/andrew/.hermes/profiles/cleanup-audio-qa/config.yaml` |
| `cleanup-audio-showrunner` | `enabled` | `/home/andrew/.hermes/profiles/cleanup-audio-showrunner/config.yaml` |
| `fiction` | `disabled` | `/home/andrew/.hermes/profiles/fiction/config.yaml` |
| `horror-series` | `disabled` | `/home/andrew/.hermes/profiles/horror-series/config.yaml` |
| `wagecheck-dev` | `disabled` | `/home/andrew/.hermes/profiles/wagecheck-dev/config.yaml` |

## Interpretation

- `fiction`, `anunnaki`, and `horror-series` are already migrated/disabled for the old skill.
- Anunnaki specialist profiles still explicitly reference the old monolith and should be migrated as a suite before any global shim.
- Cleanup audio profiles reference the old fiction skill alongside audio production; do not migrate them automatically during manuscript-skill rollout without a separate audio-pipeline check.
- `wagecheck-dev` and `fiction` appearances are disabled-list entries, not blockers.
- `brambleford-reader` uses an older config shape and should be handled separately; Brambleford policy/workflows are distinct.

## Decision

Do not convert the global old skill to a compatibility shim yet. First migrate the Anunnaki specialist profile suite that directly depends on the old monolith.
