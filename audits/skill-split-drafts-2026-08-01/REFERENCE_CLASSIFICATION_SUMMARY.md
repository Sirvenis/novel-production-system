# Reference Classification Manifest Summary

Date: 2026-08-01T11:48:12

Scope: classification of all 252 markdown references under `longform-fiction-series-drafting/references/`. No live Hermes skills changed; no references moved or deleted.

CSV manifest: `/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/REFERENCE_CLASSIFICATION_MANIFEST.csv`

## Disposition counts

- generalize-into-draft-task-skill-or-linked-reference: 132
- copy-to-canonical-series-repo-before-global-slim: 76
- manual-review-before-disposition: 18
- manual-review-before-live-skill-install: 17
- copy-to-series-or-adjacent-domain-reference-before-global-slim: 9

## Series/project bucket counts

- cross-series/general: 167
- meridian-relics: 29
- elias-library: 19
- anunnaki: 17
- brambleford: 8
- stories-for-the-road: 6
- last-clean-up-crew: 4
- better-version: 2

## Task-domain bucket counts

- controlled-fiction-drafting-and-autonomous-runs: 62
- manual-review: 39
- fiction-editorial-audits-and-revision-planning: 33
- fiction-architecture-briefing-and-research-gates: 26
- controlled-fiction-revision-and-expansion: 26
- reader-package-and-feedback-workflow: 23
- fiction-project-governance-and-handoffs: 22
- controlled-model-evaluation-for-creative-work: 20
- fiction-assembly-final-qa-and-freeze: 1

## Risk counts

- normal: 235
- manual-review/high-impact: 17

## High-impact/manual-review items

- `automatic-model-switching-policy.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `codebase-memory-mcp-fiction-continuity.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `codebase-memory-mcp-for-fiction-projects.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `deploy-scout-versions-reader-site.md` → deployment/server-coupled — route to reader package + deployment skill with explicit approval
- `fallback-model-canon-reset.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `fallback-model-incident-chapter-19-20-case-study.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `fallback-model-work-classification.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `gpt-55-only-canon-reset.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `hermes-v017-reach-features-for-novel-agents.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `mcp-first-after-session-recall.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `ollama-cloud-fiction-model-lanes.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `profile-provider-definition-fix-pattern.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `profile-suite-to-executable-production-pipeline.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `publishing-infrastructure-audit-pattern.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `reader-site-feedback-deployment-pitfalls.md` → deployment/server-coupled — route to reader package + deployment skill with explicit approval
- `token-efficient-fiction-profile-continuation.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse
- `token-management-for-fiction-sessions.md` → runtime/profile/config-sensitive — keep out of drafting skill; review manually before reuse

## Recommended next action

Use this manifest to do a preservation pass before live skill installation: copy series-specific case studies to canonical repos with provenance indexes; convert cross-series methods into linked references under the staged task skills; quarantine high-impact runtime/deployment utilities for manual review.
