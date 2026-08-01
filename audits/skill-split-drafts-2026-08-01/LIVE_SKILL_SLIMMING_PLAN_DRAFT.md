# Live Skill Slimming Plan Draft — Fiction Production Skill Split

Date: 2026-08-01

Status: draft plan only. Do not execute without Andrew's explicit live-install/slimming approval.

## Current evidence

Completed gates:

- Reference inventory/classification complete: 252 legacy references.
- Project-specific/adjacent preservation complete: 85 references copied to canonical repos.
- Cross-series condensation complete: 132 references condensed into linked task-skill references.
- High-impact quarantine complete: 17 references held out.
- Test profile canary install complete: `fiction-skill-canary`.
- Fresh routing canary passed: 8/8 routes correct.

Latest reports:

- `PRESERVATION_PASS_REPORT.md`
- `CROSS_SERIES_CONDENSATION_REPORT.md`
- `CANARY_REVIEW_REPORT.md`
- `TEST_PROFILE_CANARY_INSTALL_REPORT.md`

## Proposed live install shape

Install these as separate user-local creative skills under `~/.hermes/skills/creative/`:

- `creative/controlled-fiction-drafting-and-autonomous-runs/`
- `creative/controlled-fiction-revision-and-expansion/`
- `creative/controlled-model-evaluation-for-creative-work/`
- `creative/fiction-architecture-briefing-and-research-gates/`
- `creative/fiction-assembly-final-qa-and-freeze/`
- `creative/fiction-editorial-audits-and-revision-planning/`
- `creative/fiction-project-governance-and-handoffs/`
- `creative/longform-fiction-production/`
- `creative/reader-package-and-feedback-workflow/`

The intended primary entry point is:

- `longform-fiction-production` — lean router.

The other eight skills are task-class specialists loaded only when their production phase is known.

## What happens to the existing live skill

Do not delete `~/.hermes/skills/creative/longform-fiction-series-drafting` during the first live install.

Recommended first live phase:

1. Install new split skills alongside the old skill.
2. Keep the old skill present as an archive/compatibility fallback.
3. Patch the old skill lightly, if approved, to say it has been superseded by `longform-fiction-production` for new work.
4. Disable the old skill only in selected lean fiction profiles after successful canary, not globally on day one.
5. Delete/archive old references only in a later cleanup pass after Andrew review.

## Profile impact proposal

First profile to change after live install:

- `fiction` profile only, because it is the token-saving fiction profile and already intended for lean fiction workflows.

Do not change immediately:

- `default`
- series-specific showrunners/writers/editors/readers
- audio profiles
- wagecheck/dev profiles
- visual profiles

Proposed `fiction` profile change after live install:

1. Enable/load `longform-fiction-production` and the eight task-class skills.
2. Disable or stop auto-loading the old `longform-fiction-series-drafting` only after a successful live canary.
3. Verify with `hermes -p fiction skills list` and a dry-run routing prompt.
4. Update profile SOUL/handoff only if needed to point to the router.

## Quarantine handling

Do not promote the following class of references automatically:

- runtime/model/provider fallback rules;
- profile/provider config repair patterns;
- Codebase Memory MCP/token strategy rules;
- reader-site/VPS/deployment procedures;
- Telegram/delivery behavior;
- any item listed in `_manual-review-quarantine/HIGH_IMPACT_RUNTIME_DEPLOYMENT_REFERENCES_20260801.md`.

Those should become separate references only after manual review, likely under these existing or future skills:

- Hermes/profile/runtime items → `hermes-agent`, `hermes-provider-fallback`, or a future fiction-profile-operations skill.
- Deployment items → `static-site-vps-deployment` or `reader-package-and-feedback-workflow` with explicit deployment gate.
- Codebase Memory/token items → MCP/governance skill after verifying current tooling.

## Live install checklist if Andrew approves later

1. Snapshot current live skill tree metadata:
   - file list;
   - SHA-256 hashes for `longform-fiction-series-drafting`;
   - current `hermes skills list` output;
   - current `fiction` profile config skill section.
2. Copy staged skill directories from the approved package into `~/.hermes/skills/creative/`.
3. Validate all copied `SKILL.md` frontmatter and linked references in the live tree.
4. Run `hermes skills list` in default and `fiction` profile.
5. Start a fresh `fiction` profile dry-run routing canary.
6. If successful, optionally update only the `fiction` profile skill disables/enables.
7. Record report and commit it to `novel-production-system` plus update `scout-handoffs`.

## Rollback plan

If live install fails before profile changes:

1. Remove only the newly copied split skill directories from `~/.hermes/skills/creative/`.
2. Leave `longform-fiction-series-drafting` untouched.
3. Clear any generated test cache/session files only if necessary.
4. Re-run `hermes skills list` to verify the old state is visible.

If a profile change fails:

1. Restore the saved profile `config.yaml` from the snapshot.
2. Do not touch manuscript repos.
3. Re-run `hermes -p fiction skills list` and a one-line test prompt.

## Explicit approval wording required

Do not execute this plan unless Andrew gives a clear instruction equivalent to:

"Proceed with the live fiction skill split install/slimming plan. Install alongside first; do not delete the old skill yet."

If Andrew only says "keep going" or "prepare the next step", continue with planning/review only.
