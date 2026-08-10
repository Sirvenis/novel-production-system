# Night Shift Book 1 — Source Lock Record

**Acceptance Test:** Night Shift Book 1 — Development/Recovery Pipeline Acceptance Test
**Mode:** DIAGNOSIS ONLY — NO PROSE CHANGES
**Date:** 2026-08-11

## Runtime/Model Record

**Intended Scout runtime:** GPT-5.5 / OpenAI Codex
**Actual runtime at session start:** GPT-5.5 / OpenAI Codex
**Transition:** At 02:31:59 (session timestamp), OpenAI Codex returned HTTP 429 (usage limit reached). Hermes auto-fell-back to ollama-cloud/glm-5.2:cloud. This transition is recorded per authorization: "If Codex reaches its usage limit during this work, do not silently alter evidence provenance."
**Current operating model:** GLM-5.2:cloud via ollama-cloud
**Authorization for continued work on GLM-5.2:** Per Andrew/Arden authorization — "Andrew has an existing GLM-5.2 backup Hermes profile that may be used for appropriate continuation/background work under the existing orchestration authority."
**Provenance note:** All diagnostic findings in this acceptance test were produced by GLM-5.2:cloud unless otherwise noted in the model provenance section. No model silently impersonated another.

## Repository State

- **Canonical repo:** Sirvenis/nurse-fiction-series
- **Remote URL:** https://github.com/Sirvenis/nurse-fiction-series.git
- **Local path:** /home/andrew/projects/active/nurse-fiction-series
- **Branch:** main
- **Commit at lock:** 7f34ac3 — "governance: add standard series authority packet"
- **Dirty state:** clean (no uncommitted changes)
- **Divergence from origin:** 0 ahead, 0 behind (verified via fetch + rev-list)

## Manuscript File

- **Path:** /home/andrew/projects/active/nurse-fiction-series/night-shift/book1/MANUSCRIPT_ASSEMBLED.md
- **File size:** 256,999 bytes
- **SHA-256:** 91642840cbc8cb9656d26b46bb3dcaf1a8a05905ae0a48b75de4c0f59666bef7
- **Total words:** 47,311
- **Total lines:** 3,073
- **Encoding:** UTF-8 (contains non-ASCII characters — em dashes, etc.)

## Chapter Inventory

| Ch | Title | Words | Start Line |
|----|-------|-------|------------|
| 1 | The First Night | 4,922 | 1 |
| 2 | The Rhythm | 4,442 | 280 |
| 3 | Aunty Dot | 2,865 | 618 |
| 4 | Room 14 | 3,849 | 816 |
| 5 | The Full Moon | 2,472 | 1095 |
| 6 | The History | 3,567 | 1227 |
| 7 | The Surge | 2,532 | 1435 |
| 8 | The Break | 2,205 | 1597 |
| 9 | Liam | 2,755 | 1737 |
| 10 | Room 14 Again | 2,117 | 1951 |
| 11 | The Choice | 2,789 | 2117 |
| 12 | The Basement | 2,964 | 2289 |
| 13 | The Long Night | 5,254 | 2441 |
| 14 | After | 1,403 | 2761 |
| 15 | The Next Night | 1,638 | 2855 |
| 16 | The Drive Home | 1,537 | 2949 |

## Discrepancy from Test Plan

The Night Shift Acceptance Test Plan states "45,555 words; 16 chapters." Actual manuscript is 47,311 words; 16 chapters. The word count discrepancy (+1,756 words) likely reflects post-draft revisions already applied (commit history shows developmental revision commits for Ch 1, 9, 14-16). Chapter count matches.

## Working Copy Verification

No working copy found outside the canonical repo. The only manuscript file is at the canonical path above. No fork, branch, or alternate directory contains a competing manuscript.

## No-Modification Boundary

This acceptance test does NOT modify the authoritative manuscript. All evidence is written to the isolated evidence directory at:
/home/andrew/novel-production-system/acceptance-programmes/novel-production-pipeline-acceptance-v1.0-design/evidence/night-shift-book1/

The manuscript hash will be re-verified at the end of this test to confirm no modification occurred.