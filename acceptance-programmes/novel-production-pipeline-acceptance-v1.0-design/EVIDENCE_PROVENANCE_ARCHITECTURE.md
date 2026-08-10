# Evidence and Provenance Architecture

Every material workstream records:

- profile used;
- requested model/provider;
- served model/provider where verifiable;
- role/task;
- input artifact paths and hashes;
- output artifact paths and hashes;
- whether independent or received prior analysis;
- tools materially used;
- session id/log evidence where available;
- human/Scout verification status;
- execution gate status.

## Directory pattern for future manuscript tests

acceptance-runs/YYYYMMDD-manuscript-slug/
  source-lock/
  stage-01-integrity/
  stage-02-context-map/
  stage-03-developmental-diagnosis/
  stage-04-research-if-triggered/
  stage-05-continuity-canon/
  stage-06-editorial-plan/
  stage-07-authorised-revisions/
  stage-08-mechanical-qa/
  stage-09-fresh-reader/
  stage-10-revision-verification/
  provenance/
  final-gate/

Canonical manuscript repos remain the source of prose truth. Acceptance runs may point to source files and hashes but must not duplicate unpublished manuscripts unnecessarily.
