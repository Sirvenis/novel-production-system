---
name: fiction-assembly-final-qa-and-freeze
description: Use for assembling manuscripts, final mechanical QA, export/freeze gates, source parity, hashes, and phase closure.
version: 0.1.0-draft
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [fiction, novel-production, draft-skill, skill-split]
    related_skills: [longform-fiction-series-drafting]
---

# Fiction Assembly Final Qa And Freeze

## Purpose

Handle final mechanical manuscript operations after drafting/revision: ordered assembly, chapter/title validation, artifact scans, source parity, export/freeze, baseline checkpointing, and phase closure.

## When to Use

- Assembling chapters into a full manuscript.
- Creating baseline/checkpoint before reader audit.
- Final QA after revision/line/copy/proofread.
- Preparing release candidates/exports.
- Freezing a book or closing a project phase.

## Procedure

1. Read current status/handoff and assembly manifest if present.
2. Verify source chapter directory and expected chapter order/count.
3. Assemble with explicit sorted numeric order, not brittle shell globs.
4. Validate headings, duplicate IDs, chapter titles, scene markers, end markers, word counts, and known artifact patterns.
5. Compare source and assembled manuscript parity.
6. Create hashes/manifest when freezing or checkpointing.
7. Update status/handoff/closure report.
8. Commit/push.

## Final QA Checks

- Expected chapter count.
- Sequential chapter headings.
- No duplicate titles unless intentional.
- No `[End Chapter]` production markers in publication export.
- No scaffold notes or model metadata in reader-facing files.
- No Chapters 10+ omitted by `chapter-0*.md` style glob.
- Export/source checksums recorded where needed.

## Freeze Rule

A freeze is a governance act. Do not freeze a manuscript just because final QA passed. Confirm the repo/status says freeze is the current gate.

## Pitfalls

- Silent omission of chapters 10+ from shell globs.
- Treating file size as quality.
- Publishing/exporting stale assembled files.
- Starting new prose work during closure.

## Verification Checklist

- [ ] Expected source files identified.
- [ ] Assembly order verified numerically.
- [ ] Full manuscript word/chapter counts verified.
- [ ] Artifact scans run.
- [ ] Manifest/hash/report created if relevant.
- [ ] Git clean and pushed.
