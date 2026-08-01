# Legacy Generalized Lessons — controlled-model-evaluation-for-creative-work

Date: 2026-08-01

This compact linked reference distills cross-series/general items from the old global `longform-fiction-series-drafting` reference archive into task-class guidance for the staged draft skill split.

No live Hermes skills were changed. Series-specific canon remains in canonical series repos; the legacy files remain untouched until a later approved slimming pass.

Source manifest: `/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/REFERENCE_CLASSIFICATION_MANIFEST.csv`
Legacy source directory: `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references`
Processed references in this task domain: 12

## Generalization Rules Used

- Convert reusable procedure into task-class guidance.
- Preserve project names only as provenance; do not treat old examples as current canon.
- Do not include runtime/provider/profile/deployment-sensitive items here; those remain quarantined for manual review.
- Before installing any staged skill live, re-check current repo authority and validate the draft skill package.

## Source Index

| Source file | Title | Hash | Words |
|---|---|---:|---:|
| `blind-model-evaluation-layer-repair.md` | Blind Model Evaluation Layer Repair | `a6696211ef9304d2` | 682 |
| `controlled-blind-evaluation-sequence.md` | Controlled Blind Evaluation Sequence for Multi-Model Fiction Experiments | `96ddd22b3a3adecb` | 687 |
| `controlled-experiment-candidate-canonical-promotion.md` | Controlled Experiment Candidate Canonical Promotion | `d8ded00a94f93ad1` | 488 |
| `controlled-multi-model-chapter1-experiment.md` | Controlled Multi-Model Chapter 1 Experiment | `ded6c128efcaefac` | 738 |
| `editorial-reader-model-testing.md` | Editorial Reader Model Testing — Session Findings | `8b85db6ee7f9a60f` | 445 |
| `fallback-drift-prevention-pass1-expansion.md` | Fallback Drift Prevention During Pass 1 Expansion | `ec926ec6bb21b895` | 540 |
| `multi-model-fiction-pipeline.md` | Multi-Model Fiction Pipeline | `da656c0c8bb53026` | 333 |
| `multi-model-orchestration-pattern.md` | Multi-Model Orchestration Pattern (Ollama Cloud) | `730c963fb852ca0b` | 352 |
| `nemotron-3-ultra-fiction-subagent-benchmark.md` | Nemotron 3 Ultra fiction subagent benchmark pattern | `1de1c1af0fd22f2d` | 467 |
| `post-blind-identity-reveal-and-synthesis.md` | Post-blind identity reveal and synthesis workflow | `c1a464896eafba2f` | 433 |
| `post-blind-model-experiment-synthesis-and-revision-gate.md` | Post-Blind Model Experiment Synthesis and Revision Gate | `7979f9e9e008469d` | 539 |
| `shelved-model-experiment-gate-before-prose.md` | Shelved Model Experiment Gate Before Prose | `dd033a75079b0b12` | 443 |

## Distilled Operational Lessons

### Blind Model Evaluation Layer Repair

Provenance: `blind-model-evaluation-layer-repair.md` (`a6696211ef9304d2`), 682 words.

- Topic: Blind Model Evaluation Layer Repair
- Topic: Core rule
- Topic: Procedure
- Verify the current runtime only if model-sensitive work is being done, but do not generate prose.
- Confirm the immutable artifacts before editing:
- Generate a fresh random deranged mapping from preserved raw drafts to Version A-D. Deranged means no version keeps the same raw draft as the compromised mapping.

### Controlled Blind Evaluation Sequence for Multi-Model Fiction Experiments

Provenance: `controlled-blind-evaluation-sequence.md` (`96ddd22b3a3adecb`), 687 words.

- Topic: Controlled Blind Evaluation Sequence for Multi-Model Fiction Experiments
- Topic: Core rule
- Topic: Evaluation order pattern
- Use the isolated `reader/` workspace only.
- Reader lens: commercial reader effect, desire for next chapter, character interest, clarity, emotion, atmosphere, tension.
- Do not over-prioritize canon/architecture compliance unless it disrupts the reading experience.

### Controlled Experiment Candidate Canonical Promotion

Provenance: `controlled-experiment-candidate-canonical-promotion.md` (`d8ded00a94f93ad1`), 488 words.

- Topic: Controlled Experiment Candidate Canonical Promotion
- A controlled model/prose experiment produced one or more non-canonical candidates.
- A winner/base candidate has passed reader/editor/showrunner or similar evaluation.
- Revision and final micro-polish are complete.
- Andrew separately approves canonical promotion for a specific chapter/file.
- Topic: Pre-promotion checks

### Controlled Multi-Model Chapter 1 Experiment

Provenance: `controlled-multi-model-chapter1-experiment.md` (`ded6c128efcaefac`), 738 words.

- Topic: Controlled Multi-Model Chapter 1 Experiment
- A chapter brief is approved.
- The output must remain non-canonical until blind evaluation and Andrew's later decision.
- Topic: Core rule
- Topic: Required sequence
- **Update project gates first.** Update status, handoff, and decision log to record:

### Editorial Reader Model Testing — Session Findings

Provenance: `editorial-reader-model-testing.md` (`8b85db6ee7f9a60f`), 445 words.

- Topic: Editorial Reader Model Testing — Session Findings
- Topic: OpenRouter Free Model Landscape (June 2026)
- Topic: Reliably Working Models
- Topic: Practice Recommendation
- **Hermes delegation with primary model** — Spawn subagents using `delegate_task` (uses your Codex primary). Prompt each with distinct editorial personas. No model switching needed.
- **Cronjob with model override** — If you want a specific model (e.g., Nemotron), use `cronjob` with `model` override for each agent run.

### Fallback Drift Prevention During Pass 1 Expansion

Provenance: `fallback-drift-prevention-pass1-expansion.md` (`ec926ec6bb21b895`), 540 words.

- Topic: Fallback Drift Prevention During Pass 1 Expansion
- Topic: What went wrong
- On the next "ok please proceed", the agent (running on fallback) failed to re-read `handoff/next-actions.md` which explicitly specified Chapter 14 expansion
- Topic: Root cause
- Topic: Prevention checklist
- Topic: Before continuing after any rate limit / fallback event:

### Multi-Model Fiction Pipeline

Provenance: `multi-model-fiction-pipeline.md` (`da656c0c8bb53026`), 333 words.

- Topic: Multi-Model Fiction Pipeline
- Topic: Orchestration Roles
- **Orchestrator drafts** — Chapter by chapter with tracker updates
- **Every 5 chapters: Reader Audit** — Orchestrator pauses and asks momentum questions:
- Would I still be eager to read the next chapter?
- Topic: Critical Rules

### Multi-Model Orchestration Pattern (Ollama Cloud)

Provenance: `multi-model-orchestration-pattern.md` (`730c963fb852ca0b`), 352 words.

- Topic: Multi-Model Orchestration Pattern (Ollama Cloud)
- Topic: Pattern Overview
- Topic: Model Roles
- Topic: Workflow Pipeline
- **Logic Audit:** deepseek-v3.2:cloud reviews threat escalation, continuity, mystery fairness
- Topic: Orchestrator vs Writer Split

### Nemotron 3 Ultra fiction subagent benchmark pattern

Provenance: `nemotron-3-ultra-fiction-subagent-benchmark.md` (`1de1c1af0fd22f2d`), 467 words.

- Topic: Nemotron 3 Ultra fiction subagent benchmark pattern
- Topic: Session-derived lesson
- Topic: What worked
- Commercial reader audit: produced useful reader-facing reactions and satisfaction/pacing notes.
- Subagent coordination: produced reasonable agent roles and stop gates.
- Current-state verification: when given only current tracker + current chapter files, it correctly identified that previously flagged Arden blockers in Chapters 13, 15, and 16 had been fixed.

### Post-blind identity reveal and synthesis workflow

Provenance: `post-blind-identity-reveal-and-synthesis.md` (`c1a464896eafba2f`), 433 words.

- Topic: Post-blind identity reveal and synthesis workflow
- The task is synthesis/status/governance only, not prose revision.
- Topic: Required sequence
- Verify the protected key before reading it:
- If the hash does not match, stop and report. Do not use the key.
- If the hash matches, read the key only for the minimum mapping needed.

### Post-Blind Model Experiment Synthesis and Revision Gate

Provenance: `post-blind-model-experiment-synthesis-and-revision-gate.md` (`7979f9e9e008469d`), 539 words.

- Topic: Post-Blind Model Experiment Synthesis and Revision Gate
- The task asks for synthesis, status updates, validation, commit/push, and strict stop boundaries.
- Later, Andrew may approve a non-canonical base draft, a controlled revision pass, or a focused editor audit.
- Topic: Procedure
- Verify private identity key before reading it:
- if hash differs, STOP and report.

### Shelved Model Experiment Gate Before Prose

Provenance: `shelved-model-experiment-gate-before-prose.md` (`dd033a75079b0b12`), 443 words.

- Topic: Shelved Model Experiment Gate Before Prose
- A research dossier and a model-experiment framework share the same PR or development stage.
- The next active task is architecture, not Chapter 1 prose.
- Topic: Required sequence
- Verify live runtime before architecture/canon work if the series has a model gate.
- Make the merge/commit record explicitly say the experiment specification was added without authorising generation.
