# Pipeline Stage Definitions

## 1. Authority / source lock

Purpose: establish the manuscript source of truth before any analysis.
Inputs: canonical repo path, branch, remote, status/handoff, source manuscript path(s), current model policy.
Outputs: source-lock record with commit, file hashes, word/chapter counts, and explicit no-prose-change boundary.
Stop if: repo/path conflicts, dirty unaccounted prose, stale handoff contradiction, missing manuscript, model policy conflict.

## 2. Manuscript integrity verification

Purpose: prove the draft is complete enough to evaluate.
Checks: word count, chapter count, duplicate/missing chapter IDs, obvious truncation, front/back matter separation, encoding, known generated artifacts.
Outputs: integrity report and machine-readable counts.

## 3. Series / canon context loading

Purpose: provide only necessary context for the tested manuscript.
Inputs: series bible, current handoff, canon/status files, prior-book summaries, voice guardrails, project-specific model policy.
Outputs: context map and read-depth declaration.

## 4. Showrunner / developmental diagnosis

Purpose: identify real structural, promise, character, pacing, and reader-contract issues before any fix.
Mode: diagnosis first; no prose rewrite.
Outputs: severity-ranked diagnosis with evidence references and recommended branches.

## 5. Conditional research / fact verification

Purpose: verify factual/procedural/cultural/historical claims only when manuscript content needs it.
Triggers: medical/legal/procedural claims, real culture/history/archaeology, workplace accuracy, geography, science/technical details, harmful stereotype risk, or reader-trust risk.
Outputs: claim register, verdicts, sources, prose-impact recommendations. Researcher role remains unassigned; Luna Researcher excluded.

## 6. Continuity / canon audit

Purpose: detect contradictions within the manuscript and against series canon.
Outputs: contradiction register with severity, evidence, and confidence. No rewrite by default.

## 7. Controlled editorial intervention

Purpose: make only authorised changes targeted to approved findings.
Modes: none; surgical patch; chapter-level revision; structural rewrite. Default is none until Andrew / Arden approve a revision plan.
Outputs: patch plan, changed-file list, before/after hashes, revision notes.

## 8. Mechanical QA

Purpose: reduce deterministic defects cheaply.
Checks: spelling/typos where tooling supports, repeated paragraphs, chapter numbering, missing scene breaks, smart quote/encoding, markdown structure, front/back matter, compile/export readiness.
Outputs: machine report plus human interpretation only where needed.

## 9. Fresh-reader evaluation

Purpose: measure reader experience after diagnosis or approved intervention.
Outputs: enjoyment/confusion/momentum/character-pressure report, not a fix list masquerading as authority.

## 10. Revision verification

Purpose: verify approved changes solved the target defects and introduced no new damage.
Outputs: finding-by-finding verification matrix, regression check, unresolved issues.

## 11. Regression checking

Purpose: test whether the pipeline catches known historical defect types without inventing new ones.
Mode: for the 16 ready novels, diagnosis/audit only initially.
Outputs: true positives, credible new findings, false positives, overediting risk notes.

## 12. Final quality gate

Purpose: decide whether the manuscript is ready for Library/publication processing, needs targeted work, or should stop.
Outputs: quality-gate verdict and evidence pack.

## 13. Andrew / Arden authority gate

Purpose: preserve Founder/steward authority over canon/prose/policy.
Required for: prose changes beyond pre-approved scope, final publication status, model policy changes, production role assignments, rollout of the pipeline as standard.


## Stage 11 clarification

Stage 11 has two modes:

- Per-manuscript regression check: after an approved intervention, verify that the changed manuscript did not reintroduce defects the pipeline already knows how to catch.
- Corpus-level retrospective regression: the separate 16-novel audit programme that diagnoses only, measures known-defect rediscovery and false positives, and never revises canonical ready novels during the initial phase.

Both use the same defect taxonomy, but they are different execution modes.


## Pre-diagnosis deterministic scan rule

Before LLM developmental diagnosis, run cheap deterministic integrity/mechanical scans where feasible: word/chapter counts, duplicate headings, duplicate paragraphs, missing chapter sequence, obvious truncation, placeholder text, encoding/markdown issues, and abnormal chapter-length distribution.

The developmental diagnosis must not claim these script-detectable defects as expensive model discoveries; it may reference the deterministic report and focus on structural, voice, canon, continuity, research, and reader-experience defects that scripts cannot decide.

## Developmental diagnosis output contract addendum

Every material finding should include:

- severity;
- confidence: high / medium / low;
- evidence location;
- defect type from `STAGE_TO_DEFECT_TYPE_MAPPING.md`;
- could-be-intentional flag with explanation;
- canon/voice rule cited if claiming a canon or voice violation;
- proposed action: no change / watch / surgical fix / larger revision;
- preservation risk if acted on.

Every diagnosis must also include a Preservation List: specific strengths, voice traits, pacing choices, character dynamics, or series identity elements that should not be flattened by later intervention.
