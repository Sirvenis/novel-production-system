# Comparative Writer Qualification Design

## Objective

Qualify Writer candidates for Arden Studios by testing whether they can produce a publishable scene from a constrained brief without collapsing into summary, losing literal details, resolving too early, or damaging voice/canon constraints.

The test evaluates Writer capability, not showrunner planning, editing, research, or final publication judgement.

## Candidate set

Initial future candidates: GPT-5.5, Kimi K2.6, GLM-5.2.

Excluded from this initial comparison:

- GPT-5.6 Luna: Writer ineligible under corrected Wave 0B calibration; closed.
- Nemotron / StepFun: not included unless new evidence materially changes the historical audit.

## Route requirements

Each future candidate cell must record:

- profile used;
- requested provider/model;
- served provider/model from logs where verifiable;
- session id;
- prompt hash;
- raw provider response hash;
- wrapper/stdout hash if applicable;
- latency and usage if available;
- actual tool turns, expected to be zero;
- whether the run received any prior candidate output or analysis.

A candidate whose served model is not the requested model is not silently accepted. It is recorded as a route failure unless Andrew / Arden separately approve rerun or fallback classification.

## Zero-tool policy

Writer cells are generation-only. Candidate-visible packet must contain every fact required. Tools are prohibited because the task tests retention and writing from a frozen brief, not research or file discovery.

## Immutable response policy

Raw provider response is preserved byte-for-byte before extraction, normalization, blind packaging, or scoring. If wrapper post-processing fails after a provider response exists, do not retry the candidate automatically; preserve the raw response and validate from it where possible.

## Deterministic disqualifiers

Category D hard failures include:

1. Served route mismatch.
2. Any actual tool turn.
3. Missing required output contract section or malformed required JSON envelope when required by the execution harness.
4. Response below minimum word count after excluding metadata.
5. Scene-marker order violation.
6. Missing any deterministic literal-detail retention item marked hard.
7. Premature resolution of the central scene tension.
8. Summary substitution: more than two consecutive paragraphs primarily summarising events that should be dramatized.
9. Canon/brief contradiction on any hard fact.
10. Raw output not preserved or hash mismatch.
11. Identity leak into blind scoring packet.
12. Candidate output contains another candidate's material or analysis.

## Scoring dimensions

Human blind scoring is 100 points:

- Prose quality and style control: 15
- Scene construction/dramatization: 15
- Character voice and interiority: 12
- Dialogue quality and subtext: 10
- Emotional control/restraint: 10
- Pacing and escalation: 8
- Sensory specificity integrated into action: 8
- Continuity and canon preservation: 8
- Instruction/literal-detail retention: 8
- Ending discipline: no premature resolution, satisfying pressure point: 6

A candidate must score at least 82 overall and must not fall below 7/10 equivalent in prose, scene construction, voice, continuity, or instruction retention. Category D disqualifies regardless of score.

## Blind scoring architecture

Three blind lanes score independently:

- Fresh reader: does the scene read as compelling fiction and leave the intended reader wanting more?
- Editor: craft, voice, pacing, dialogue, summary substitution, revision burden.
- Showrunner: brief/canon preservation, beat order, series/scene promise, production risk.

Scorers receive anonymized candidate IDs, no provider/model/profile identity, no route metadata, and no other scorer conclusions. The blind packet includes the same rubric and target reader contract but not ground-truth labels beyond what a human reader needs to score.

## Normalization rules

Allowed before blind scoring:

- remove harness wrapper lines outside the candidate's answer;
- decode escaped newlines if the harness stored JSON strings;
- extract the prose field exactly when a schema requires it.

Not allowed:

- rewriting, spell-fixing, paragraph rearrangement, trimming preambles that are part of output-contract compliance, removing `$schema`/extra properties for schema compliance, repairing headings, filling missing sections, or normalising away deterministic failures.

## Leakage controls

- Use hash-distinct candidate output folders.
- Store identity map under private/ or outside repo until reveal.
- Blind bundles contain only candidate ID and normalized display text.
- Scorers must declare whether they saw any prior candidate output, model identity, or other scorer analysis.
- If leakage occurs, preserve evidence and decide whether scoring is invalidated; do not quietly re-score.

## Advancement to holdout

Only candidates passing Packet 01 deterministic checks and blind scoring advance to Packet 02. Packet 02 tests generalisation in a materially different genre/reader contract, not memorization of Packet 01 techniques.


## Execution harness and scoring addenda

The operational harness is specified separately in `EXECUTION_HARNESS_SPEC.md`. Its key rules are: no automatic retries, byte-for-byte raw response preservation, requested-vs-served route verification from logs where possible, and disqualification for any candidate tool call or attempted tool invocation.

The scorer architecture is specified separately in `SCORER_ARCHITECTURE.md`. It defines scorer lanes, calibration, Fresh Reader mini-rubric, conflict resolution, and independence downgrades when a scorer receives prior analysis or scores multiple lanes.

Passing Writer qualification is necessary evidence only. It is not sufficient by itself for permanent production deployment. Production use would still require Andrew / Arden approval, series-specific policy fit, and manuscript-pipeline survival evidence.


## Added qualification floors and holdout failure rule

After challenge review, the critical-dimension floors are tightened: voice/character control, continuity/canon preservation, and instruction/literal-detail retention require at least 8/10-equivalent performance in blind scoring as well as deterministic eligibility. These are production-safety dimensions, not ordinary taste dimensions.

If a candidate passes Packet 01 but fails Packet 02, it does not qualify as a cross-genre Writer candidate. Retesting after Packet 02 failure requires a new packet/version and Andrew / Arden approval; the failed holdout remains preserved.

If the served model cannot be verified from logs or equivalent route evidence, the candidate attempt is classified as `UNVERIFIABLE_ROUTE` and cannot pass as controlled benchmark evidence.
