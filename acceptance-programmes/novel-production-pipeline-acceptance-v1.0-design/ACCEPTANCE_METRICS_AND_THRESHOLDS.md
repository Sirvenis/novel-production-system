# Acceptance Metrics and Thresholds

The acceptance programme evaluates pipeline behavior.

## Core metrics

- True-positive defect detection: known/historical defects rediscovered where applicable.
- False-positive rate: findings judged not defects after Scout/Andrew/Arden review.
- Severity calibration: critical/major/moderate/minor labels match real reader/canon risk.
- Canon preservation: no invented canon conflicts, no unauthorized canon changes.
- Voice preservation: no flattening of series-specific style or public author voice.
- Unnecessary rewrite rate: proportion of recommendations asking for structural/prose rewrite without evidence.
- Defect escape rate: defects found downstream that earlier relevant stages missed.
- Downstream correction: whether later stages catch upstream mistakes.
- Instruction compliance: stage stayed inside permitted actions.
- Research accuracy: claim verdict accuracy and source grounding where research was triggered.
- Mechanical defect reduction: repeated text, numbering, format, typo, and export defects reduced.
- Reader-experience improvement: fresh-reader scores improve or known pain points reduce after authorised revision.
- Revision burden: amount of human/Scout correction needed to make stage output usable.
- Handoff quality: next stage can act without re-reading everything or asking Andrew to repeat context.
- Provenance/reproducibility: raw inputs, outputs, hashes, model routes, and decisions recorded.
- Cost/usage: approximate model calls, tokens, time, and premium-model spend.
- Human intervention required: count and severity of Andrew/Arden/Scout interventions.

## Proposed thresholds for pipeline acceptance

- No unauthorized canonical prose change: mandatory 100%.
- Source-lock and hash verification: mandatory 100% before any manuscript processing.
- Stage instruction compliance: >=95% of material stages, with zero hard-boundary violations.
- False-positive rate: target <=20% for diagnosis; <=10% for critical/major findings.
- Severity calibration: >=85% agreement after review.
- Defect escape rate: no critical escapes after the stage designed to catch them; major escapes require stage redesign.
- Unnecessary rewrite rate: <=10% of recommendations, and 0 major rewrites without evidence.
- Research claim verdict accuracy: >=90% on source-checkable claims; uncertain claims must be labelled uncertain.
- Mechanical QA: no introduced structural/chapter-numbering defects; repeated-paragraph detector must run where feasible.
- Handoff completeness: every stage records inputs, outputs, model/profile, served route where verifiable, hashes, tools used, and next gate.

Thresholds are provisional until Andrew / Arden review.


## Measurement instruments added after challenge review

- Defect escape rate uses `STAGE_TO_DEFECT_TYPE_MAPPING.md` to decide which stage should have caught each defect.
- Regression true positives use the frozen `KNOWN_DEFECT_REGISTER_SPEC.md` format.
- Voice preservation compares revised text against source-draft voice guardrails, series Storycraft/voice records where present, and blind/fresh-reader notes. A finding of flattening requires cited before/after evidence, not taste alone.
- Severity calibration agreement means Scout final adjudication against stage output and, where escalated, Andrew / Arden review. Inter-scorer disagreement of 15+ points is recorded rather than averaged away.
