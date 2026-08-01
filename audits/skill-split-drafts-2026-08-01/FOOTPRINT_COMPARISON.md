# Draft Skill Split Footprint Comparison

Date: 2026-08-01

## Scope

Comparison between the existing installed `longform-fiction-series-drafting` skill tree and the staged draft split under:

`/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/`

No live Hermes skills were changed.

## Existing installed skill

| Metric | Value |
|---|---:|
| Total files under skill tree | 266 |
| `SKILL.md` bytes | 53,621 |
| Markdown references | 252 |
| Total tree bytes | 1,096,860 |

## Draft split package

| Metric | Value |
|---|---:|
| Draft skill count | 9 |
| Total draft `SKILL.md` bytes | 24,134 |
| Average draft skill bytes | 2,682 |
| Validation status | All draft frontmatter passed local YAML/size validation |

## Raw byte comparison

If these drafts became the active routing layer, their combined `SKILL.md` footprint would be about 45.0% of the current monolithic `SKILL.md`, before deciding which references to preserve as linked support files.

Compared with the full current skill tree, the draft `SKILL.md` set is about 2.2% of the current total bytes.

This does not mean all old material should be deleted. It means the always-loaded procedural surface can be much smaller while project-specific case studies are preserved in repos or linked reference archives.

## Draft skills created

- `controlled-fiction-drafting-and-autonomous-runs/SKILL.md` — 2,783 bytes
- `controlled-fiction-revision-and-expansion/SKILL.md` — 2,528 bytes
- `controlled-model-evaluation-for-creative-work/SKILL.md` — 2,411 bytes
- `fiction-architecture-briefing-and-research-gates/SKILL.md` — 2,678 bytes
- `fiction-assembly-final-qa-and-freeze/SKILL.md` — 2,354 bytes
- `fiction-editorial-audits-and-revision-planning/SKILL.md` — 2,608 bytes
- `fiction-project-governance-and-handoffs/SKILL.md` — 2,964 bytes
- `longform-fiction-production/SKILL.md` — 3,276 bytes
- `reader-package-and-feedback-workflow/SKILL.md` — 2,532 bytes

## Recommended next validation before live install

1. Andrew/Scout review the staged draft skill boundaries.
2. Create a classification manifest for all 252 existing references with destination and disposition.
3. Copy series-specific references into canonical repos before any deletion.
4. Run canaries against at least three series repos:
   - one governance/handoff task;
   - one architecture/brief-only task;
   - one read-only audit;
   - one controlled revision or assembly validation.
5. Only then install the new skills and slim/deprecate `longform-fiction-series-drafting`.
