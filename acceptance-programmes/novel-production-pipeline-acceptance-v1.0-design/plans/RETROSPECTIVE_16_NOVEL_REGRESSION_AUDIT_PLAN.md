# 16-Novel Retrospective Regression-Audit Plan

Status: DESIGN ONLY — DO NOT RUN INITIAL REGRESSION AUDIT YET
Mode: diagnosis/audit only; no canonical prose changes.

## Corpus

The verified Library-ready regression corpus comprises 16 novels:

- Anunnaki Chronicles: Books 1–3
- Brambleford Mysteries: Books 1–4
- Meridian Relics: Books 1–3
- Last Clean-Up Crew: Books 1–3
- The Better Version: Books 1–3

Exact source paths, hashes, and catalogue IDs must be verified at run time from each canonical series repo and Elias Silver Library catalogue. Older counts are stale unless reverified.

## Purpose

Determine whether the new production pipeline:

- rediscovers historically known defects;
- detects credible previously missed defects;
- produces false positives;
- misunderstands intentional stylistic choices;
- invents continuity/canon problems;
- over-edits established voice;
- proposes unnecessary structural intervention;
- behaves consistently across genres/series;
- preserves series-specific identity;
- distinguishes genuine defects from preference.

## Initial phases

1. Corpus source lock: repo/path/branch/handoff/catalogue/hash verification for all 16.
2. Known-defect register: compile existing historical findings per series before audit scoring.
3. Deterministic scans: duplicate paragraphs, chapter numbering, missing headings, abrupt file truncation, repeated placeholder text, export/markdown issues.
4. Diagnosis-only LLM audit: bounded packets, series-specific context, no revision suggestions beyond proposed findings.
5. False-positive review: Scout compares findings to intentional style/canon and existing project records.
6. Proposed finding log: credible new defects go to Andrew / Arden review.

## Protection rules

- Never edit the canonical manuscripts during regression phase.
- Do not let a model re-litigate completed publication readiness without evidence.
- Do not compare series voices as if one house style should dominate.
- Do not over-sample one genre and generalize to all.
- Do not treat catalogue metadata as manuscript truth.


## False-positive accounting

Known historical defects and newly proposed findings must be scored separately. Rediscovering a known defect is true-positive evidence; proposing a new defect requires separate Scout/Andrew/Arden review. A model preference against intentional series voice is a false positive, not a defect.
