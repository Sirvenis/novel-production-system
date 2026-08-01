# Preservation Pass Report — Project-Specific Fiction Skill References

Date: 2026-08-01

## Scope

Copied all references classified as project-specific or adjacent-domain/project-specific from the legacy Hermes skill:

`/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references/`

into canonical project repositories before any future slimming of the global skill.

No live Hermes skills were changed. No original reference files were moved or deleted.

## Source manifest

`/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/REFERENCE_CLASSIFICATION_MANIFEST.csv`

## Destinations and commits

| Repository | Local destination | Files copied | Commit |
|---|---|---:|---|
| `Sirvenis/anunnaki-chronicles-novel` | `docs/skill-reference-migration/` | 17 references + README | `7dfbc80` |
| `Sirvenis/meridian-relics` | `docs/skill-reference-migration/` | 29 references + README | `1a29457` |
| `Sirvenis/elias-silver-library` | `docs/skill-reference-migration/` plus `short-stories/` | 25 references + 2 README files | `368d84b` |
| `Sirvenis/brambleford-cozy-mystery` | `docs/skill-reference-migration/` | 8 references + README | `8dda89c` |
| `Sirvenis/last-clean-up-crew` | `docs/skill-reference-migration/` | 4 references + README | `86b021c` |
| `Sirvenis/the-better-version` | `docs/skill-reference-migration/` | 2 references + README | `b590809` |

Total preserved reference files: 85.

## Notes

Each destination folder includes a `README.md` index explaining provenance, the source skill path, the migration manifest, and a table with task-domain classification plus source hash for every copied file.

The copied files are archival/provenance references. Current repo status, handoff, authority files, and manuscript files remain the live authority.

## Next step

The project-specific preservation prerequisite is complete. The next safe step is to process the 132 cross-series/general references from the manifest into compact linked references under the staged task skills, while keeping the 17 high-impact runtime/deployment items quarantined for manual review.
