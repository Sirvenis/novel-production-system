# Design Challenge Synthesis

Three background challenge lanes were attempted during the design phase.

## Completed reviews

1. `pipeline-architect.glm.review.md`
   - Profile/model: `glm`, reported `glm-5.2:cloud`.
   - Independence: received draft design paths but no prior review notes.
   - Verdict: APPROVE WITH CHANGES.
   - Main findings: creation pipeline was named but underspecified; Writer/pipeline bridge missing; harness spec missing; scorer architecture underspecified; Stage 11 vs retrospective unclear; acceptance metrics needed measurement instruments.

2. `benchmark-bias-risk.scout-cloud-creative.review.md`
   - Profile/model: `scout-cloud-creative`, reported `kimi-k2.6:cloud`.
   - Independence: received draft design paths; no other scorer output.
   - Verdict: APPROVE WITH CHANGES.
   - Main findings: Fresh Reader rubric needed; inter-scorer calibration needed; zero-tool should include attempted tool calls; retry policy needed; budget caps desirable; pre-intervention re-lock should be explicit; literal-detail gate weight should be clearer.

## Failed / replaced review

- `preservation-anti-overediting.scout-cloud-audit.review.md` failed because `deepseek-v3.2:cloud` returned HTTP 410 retired. This was recorded as a provenance/access failure, not a substantive review.
- A replacement preservation review completed on `scout-cloud-research` / `qwen3.5:cloud`.

## Material changes applied

- Added `CREATION_PIPELINE_STAGE_DEFINITIONS.md`.
- Added Writer `EXECUTION_HARNESS_SPEC.md`.
- Added Writer `SCORER_ARCHITECTURE.md`.
- Added `STAGE_TO_DEFECT_TYPE_MAPPING.md`.
- Added `KNOWN_DEFECT_REGISTER_SPEC.md`.
- Clarified Stage 11 dual mode.
- Added measurement-instrument notes for metrics.
- Added fresh source-lock before any approved intervention to Night Shift and Anunnaki plans.
- Clarified no automatic Writer retries and tool-attempt disqualification.

## Disagreements preserved

- GLM reviewer argued Packet 02 is more accurately a cross-genre transfer holdout than deep generalisation because it tests many of the same axes in a different genre. Scout accepts this as a useful limitation note but preserves the holdout because the user explicitly requested materially different genre/reader contract generalisation. Future Packet 03 could test a different structural skill axis if Andrew / Arden want another stage.
- Kimi reviewer argued Fresh Reader scoring without a rubric is not measurement. Scout accepted and added a mini-rubric.


3. `preservation-anti-overediting.scout-cloud-research.review.md`
   - Profile/model: `scout-cloud-research`, reported `qwen3.5:cloud`.
   - Independence: received draft design paths; no other scorer output.
   - Verdict: APPROVE WITH CHANGES.
   - Main findings: diagnosis should include Preservation List and confidence/intentionality flags; deterministic scans should precede expensive LLM diagnosis; route-unverifiable Writer runs should not pass; critical Writer floors for voice/continuity/instruction should be higher.

## Additional changes applied after replacement preservation review

- Added pre-diagnosis deterministic scan rule.
- Added developmental diagnosis output contract with confidence, could-be-intentional flag, canon/voice citation, proposed action, and Preservation List.
- Added anti-overediting rule that low-confidence/taste findings become watch items, not revision triggers.
- Added separate false-positive accounting for known vs new regression findings.
- Tightened Writer critical-dimension floors for voice, continuity/canon, and instruction/literal-detail retention to 8/10-equivalent.
- Added route-unverifiable classification cannot pass as controlled benchmark evidence.
