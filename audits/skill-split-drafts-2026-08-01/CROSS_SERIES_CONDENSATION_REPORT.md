# Cross-Series Reference Condensation Report

Date: 2026-08-01

## Scope

Processed the 132 cross-series/general legacy references marked `generalize-into-draft-task-skill-or-linked-reference` in `REFERENCE_CLASSIFICATION_MANIFEST.csv`.

No live Hermes skills were changed. No files were removed from the legacy `longform-fiction-series-drafting` skill archive.

## Output

Each staged task skill now has a linked `references/legacy-generalized-lessons-20260801.md` file containing:

- source index with filename, title, hash, and word count;
- compact distilled operational lessons;
- explicit rule that project-specific canon remains in canonical repos;
- explicit exclusion of runtime/provider/profile/deployment-sensitive material.

The staged `SKILL.md` files were updated only to point at their linked reference file.

## Processed counts by task skill

| Task skill | References processed | Linked reference |
|---|---:|---|
| `controlled-fiction-drafting-and-autonomous-runs` | 28 | `controlled-fiction-drafting-and-autonomous-runs/references/legacy-generalized-lessons-20260801.md` |
| `controlled-fiction-revision-and-expansion` | 21 | `controlled-fiction-revision-and-expansion/references/legacy-generalized-lessons-20260801.md` |
| `controlled-model-evaluation-for-creative-work` | 12 | `controlled-model-evaluation-for-creative-work/references/legacy-generalized-lessons-20260801.md` |
| `fiction-architecture-briefing-and-research-gates` | 12 | `fiction-architecture-briefing-and-research-gates/references/legacy-generalized-lessons-20260801.md` |
| `fiction-assembly-final-qa-and-freeze` | 1 | `fiction-assembly-final-qa-and-freeze/references/legacy-generalized-lessons-20260801.md` |
| `fiction-editorial-audits-and-revision-planning` | 26 | `fiction-editorial-audits-and-revision-planning/references/legacy-generalized-lessons-20260801.md` |
| `fiction-project-governance-and-handoffs` | 18 | `fiction-project-governance-and-handoffs/references/legacy-generalized-lessons-20260801.md` |
| `reader-package-and-feedback-workflow` | 14 | `reader-package-and-feedback-workflow/references/legacy-generalized-lessons-20260801.md` |

Total processed: 132.

## Manual-review quarantine

The 17 high-impact runtime/deployment references were not condensed into task skills. They are listed at:

`_manual-review-quarantine/HIGH_IMPACT_RUNTIME_DEPLOYMENT_REFERENCES_20260801.md`

These require manual review before any live skill install because they involve runtime/profile/provider behavior, MCP/token strategy, or deployment/server-coupled operations.

## Validation

- Staged `SKILL.md` files validated: 9
- Linked reference files created: 8
- Skill frontmatter/errors: 0 errors
- Live Hermes skills changed: no

Validation details: `VALIDATION_SUMMARY.json`.

## Next safe step

Review/canary the staged skill package. Do not install or replace live skills yet. After Andrew approves, install into a test profile first, verify skill loading and routing behavior, then plan the live `longform-fiction-series-drafting` slimming/deprecation pass.
