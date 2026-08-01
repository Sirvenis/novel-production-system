# Live Install / Slimming Approval Checklist — Staged Fiction Skill Split

Date: 2026-08-01

## Current status

The staged fiction skill split package has passed non-invasive validation and routing canary review.

Already complete:

- project-specific preservation pass;
- cross-series/general condensation pass;
- high-impact runtime/deployment quarantine;
- static skill validation;
- router scenario canary.

Live Hermes skills have not been changed.

## Package proposed for eventual test install

Draft source:

`/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/`

Staged skills:

- `longform-fiction-production`
- `fiction-project-governance-and-handoffs`
- `fiction-architecture-briefing-and-research-gates`
- `controlled-fiction-drafting-and-autonomous-runs`
- `fiction-editorial-audits-and-revision-planning`
- `controlled-fiction-revision-and-expansion`
- `fiction-assembly-final-qa-and-freeze`
- `reader-package-and-feedback-workflow`
- `controlled-model-evaluation-for-creative-work`

## What approval would allow

A safe approval would allow only a test install/canary, not live default replacement:

1. Copy the staged skills into a temporary/test-only local skill area or dedicated test profile.
2. Run a fresh Hermes session/profile canary that loads the router and task-specific skills.
3. Use dry-run prompts against real project handoffs without editing manuscripts.
4. Record load behavior, routing behavior, token footprint, and any missing procedure gaps.
5. Commit the canary report to `novel-production-system`.

## What approval would NOT allow yet

Even after test-canary approval, do not automatically:

- delete original `longform-fiction-series-drafting` references;
- slim or replace the live `~/.hermes/skills/creative/longform-fiction-series-drafting` skill;
- change default/profile skill lists;
- fold quarantined runtime/deployment references into live skills;
- change Hermes runtime model/provider/fallback configuration.

Those need a separate explicit live-install/slimming approval gate.

## High-impact quarantine remains manual

The following file must be reviewed before any runtime/profile/deployment-sensitive instructions are promoted:

`_manual-review-quarantine/HIGH_IMPACT_RUNTIME_DEPLOYMENT_REFERENCES_20260801.md`

Reason: it covers model/provider fallback rules, profile/runtime behavior, Codebase Memory/token strategy, and reader-site deployment pitfalls.

## Recommended next command/state for a fresh session

If Andrew approves test-canary installation, fresh-session Scout should start by reading:

1. `/home/andrew/projects/active/scout-handoffs/CURRENT_HANDOFF.md`
2. `/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/CANARY_REVIEW_REPORT.md`
3. this checklist

Then perform a test-only install/canary and stop with a report. No live replacement.

## Approval wording to look for

Proceed only if Andrew gives a clear instruction equivalent to:

"Proceed with the test-profile skill canary install. Do not replace live skills yet."

If Andrew says only "continue the audit" or "prepare the next step", keep work non-invasive and do not touch live Hermes skill/profile files.
