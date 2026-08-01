# Staged Fiction Skill Package Canary Review

Date: 2026-08-01

## Scope

Non-invasive review/canary of the staged fiction skill split package after project-specific preservation and cross-series condensation.

No live Hermes skills were installed, replaced, or slimmed. No Hermes profile/config files were modified.

## Package under review

- Draft package: `/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01`
- Router skill: `longform-fiction-production`
- Task-class skills: 8 staged specialist skills
- Linked condensed references: 8
- Cross-series/general references condensed: 132
- High-impact runtime/deployment references still quarantined: 17

## Static validation

- Staged `SKILL.md` files checked: 9
- Frontmatter/link/size errors: 0
- Blocking absolute path leftovers outside provenance lines: 0
- Benign absolute-path mention reviewed: 1 (`avoid /home/andrew/ clutter` user preference)

Result: PASS — all staged skill files have valid frontmatter, descriptions within limits, existing linked references, and no blocking path leakage.

## Routing canary scenarios

| Scenario | Expected primary skill | Result |
|---|---|---|
| Resuming a fiction project after /new; verify repo, status, handoff, git state; no prose work. | `fiction-project-governance-and-handoffs` | PASS |
| Planning a book/act/chapter map or research dossier before prose is approved. | `fiction-architecture-briefing-and-research-gates` | PASS |
| Draft one approved chapter, write file safely, verify word count, update tracker, stop. | `controlled-fiction-drafting-and-autonomous-runs` | PASS |
| Read a completed manuscript and produce a revision plan without editing prose. | `fiction-editorial-audits-and-revision-planning` | PASS |
| Apply an approved prose-changing expansion or line/cadence pass. | `controlled-fiction-revision-and-expansion` | PASS |
| Assemble/freeze/export a complete manuscript and create final QA hashes. | `fiction-assembly-final-qa-and-freeze` | PASS |
| Create a reader package or feedback forms; deployment remains out of scope unless separately approved. | `reader-package-and-feedback-workflow` | PASS |
| Run a blind/multi-model creative test on frozen inputs and record results before promotion. | `controlled-model-evaluation-for-creative-work` | PASS |

## Condensed reference coverage

| Task domain | Condensed source references |
|---|---:|
| `controlled-fiction-drafting-and-autonomous-runs` | 28 |
| `controlled-fiction-revision-and-expansion` | 21 |
| `controlled-model-evaluation-for-creative-work` | 12 |
| `fiction-architecture-briefing-and-research-gates` | 12 |
| `fiction-assembly-final-qa-and-freeze` | 1 |
| `fiction-editorial-audits-and-revision-planning` | 26 |
| `fiction-project-governance-and-handoffs` | 18 |
| `reader-package-and-feedback-workflow` | 14 |

## Quarantine check

The high-impact/runtime/deployment list remains outside the staged task skills:

`_manual-review-quarantine/HIGH_IMPACT_RUNTIME_DEPLOYMENT_REFERENCES_20260801.md`

This is intentional. Those items include model/provider fallback rules, profile/runtime configuration, MCP/token strategy, and deployment/server-coupled procedures. They should not be silently folded into live fiction drafting skills.

## Canary conclusion

The staged package is ready for a controlled test-profile install/canary, but it should still not replace the live `longform-fiction-series-drafting` skill yet.

Recommended next gate:

1. Create a temporary/test-only Hermes profile or local test skill tree for this package.
2. Load only the router plus one scenario-specific task skill in a fresh session.
3. Run the eight routing scenarios above against real project handoffs without editing manuscripts.
4. If the canary behaves cleanly, prepare an explicit live-install/slimming approval checklist for Andrew.

## Explicit do-not-do-yet list

- Do not delete legacy references.
- Do not slim or replace the live `longform-fiction-series-drafting` skill.
- Do not modify default/profile skill lists.
- Do not fold quarantined runtime/deployment items into live skills without manual review.

## Reviewed benign path mention

- `reader-package-and-feedback-workflow/references/legacy-generalized-lessons-20260801.md:68` — user preference to avoid `/home/andrew/` clutter. This is not a project-specific canon leak or live deployment instruction.
