# Blind Skill Split Assessment: `longform-fiction-series-drafting`

Date: 2026-08-01

## Executive verdict

**Split it.** The current skill is not one coherent skill with a large reference library; it is a mixed production archive containing reusable fiction procedures, stage-specific checklists, series/book/session case studies, model/runtime operations, reader-site deployment guidance, templates, and scripts. At 53,621 bytes for `SKILL.md` plus 252 references (about 1.02 MB), its routing surface is too broad and its authority boundaries are unclear.

The correct split axis is **task or production class**, not series. Keep series canon, voice, character rules, reveal order, book state, reports, and handoffs in each canonical series repository. Hermes may still have series-specific **profiles/roles**, but it should not normally have per-series procedural skills. A per-series skill would create a second, stale-prone copy of repository knowledge.

Recommended end state: a small fiction-production router plus six reusable task-class skills, with reader-site/deployment operations and controlled model experiments separated from ordinary drafting. Preserve case studies in canonical repositories or an anonymised production-system case-study library; do not keep them in the always-available procedural layer.

## 1. Runtime identity

- Active profile observed from the environment: `gpt56-sol` (`HERMES_HOME=/home/andrew/.hermes/profiles/gpt56-sol`).
- Model/provider identified by this session's runtime metadata: `gpt-5.6-sol` through `openai-codex`.
- The environment query did not expose a primary-model variable, so the profile observation is independently grounded in the environment while model/provider identification relies on the runtime metadata supplied to this session.

## 2. Scope and source material inspected

This was a source-only assessment. The two excluded audit/inventory files named in the request were not opened, searched, parsed, or used.

### Files read in full

- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/SKILL.md`
- `/home/andrew/novel-production-system/audits/autonomous-novel-production-systems-audit-2026-07-25.md`
- `/home/andrew/novel-production-system/templates/skills/skill-continuity-check.md`
- `/home/andrew/novel-production-system/templates/skills/skill-research-ingest.md`
- `/home/andrew/novel-production-system/templates/skills/skill-voice-audit.md`
- `/home/andrew/novel-production-system/templates/skills/skill-canary-run.md`
- `/home/andrew/novel-production-system/templates/skills/skill-discovery-pass.md`
- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references/novel-production-pipeline-patterns.md`
- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references/anunnaki-book4-controlled-ch11-prose-after-special-brief.md`
- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references/brambleford-book4-skeleton-to-pass2-expansion.md`
- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references/meridian-book3-pass2-model-lane-audit.md`
- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references/reader-site-feedback-deployment-pitfalls.md`
- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/scripts/sync-brambleford-feedback.sh`
- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/scripts/pass-1-reassembly-and-audit.py`
- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/scripts/normalize_typography.py`
- `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/scripts/prune-default-skills.py`

### Directory/file metadata inspected

- Complete filename inventory under `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/`
- Complete filename inventory under its `references/`, `templates/`, and `scripts/` directories
- Complete filename inventory under `/home/andrew/novel-production-system/templates/skills/`
- File sizes and counts for the current skill's components
- Git working-tree status for `/home/andrew/novel-production-system` before report creation

The complete 252-reference directory was inventoried by filename, but only the representative references listed above were read for content. Conclusions about named clusters are therefore filename-level evidence unless tied to a file explicitly listed as read.

## 3. Size and count findings

### Current Hermes skill

| Component | Count | Size/notes |
|---|---:|---|
| `SKILL.md` | 1 | 53,621 bytes; 340 lines; 6,290 whitespace-delimited words |
| Reference files | 252 | 1,023,010 bytes total |
| Template files | 9 | 8,602 bytes total |
| Script files | 4 | 11,627 bytes total |
| Total files in skill | 266 | 1 `SKILL.md` + 252 references + 9 templates + 4 scripts |

### Novel-production-system skill templates

`/home/andrew/novel-production-system/templates/skills/` contains 5 task-oriented templates:

1. continuity check
2. research ingest
3. voice audit
4. canary run
5. discovery pass

These are evidence that narrow, triggerable, verifiable task-class skills are already a natural fit for the production system.

### Filename-level concentration indicators

These groups overlap and must not be summed, but they illustrate the mixture inside one skill:

- 16 reference filenames contain `anunnaki`
- 3 contain `meridian`
- 6 contain `brambleford`, `briarcombe`, or `village-life`
- 43 contain `elias`, `sunken-bell`, or `burning-bird`
- 16 contain reader-site/reading-room/feedback-form/dashboard terms
- 28 contain `cron`
- 22 contain model/runtime-related terms such as model, Ollama, Nemotron, fallback, or provider/profile

This is enough to show that the reference collection spans series cases, infrastructure, publishing operations, runtime orchestration, and craft—not merely longform drafting.

## 4. Why the skill should be split

### 4.1 Trigger ambiguity

The advertised trigger includes drafting, revision, review, packets, trackers, completion notes, and handoffs. The body additionally routes architecture, research-only dossiers, blind model experiments, cron continuation, profile maintenance, reader sites, deployment, publishing infrastructure, final QA, and project closure. An agent cannot infer a narrow procedure from the skill name or top-level trigger.

### 4.2 Mixed authority levels

The collection mixes:

- general production principles;
- stage-specific procedures;
- one-book approval gates;
- exact series reveal restrictions;
- exact model/provider policies from particular sessions;
- hard-coded project paths and operational infrastructure;
- worked examples and postmortems.

A reusable skill should say **how to perform a class of work** and where to load current authority. It should not itself become the authority for a book's canon or live gate state.

### 4.3 Case studies are masquerading as procedures

The Anunnaki Chapter 11 reference is useful evidence for a generic controlled-one-chapter workflow, but its names, withheld revelations, chapter numbers, model requirement, and authority stack belong to that project's recorded history. Likewise, the Brambleford and Meridian references contain reusable lessons wrapped in specific book state. The reusable rule should be extracted; the complete worked case should remain repo-local or in an explicitly labelled, anonymised case-study library.

### 4.4 Non-drafting operations are embedded

Reader-site deployment is a software/deployment task with different prerequisites and safety boundaries from manuscript drafting. The inspected deployment reference includes VPS/API/cache/CSS/source-of-truth concerns. It should not route through a longform drafting skill.

The scripts make the boundary problem especially clear:

- `sync-brambleford-feedback.sh` is project- and server-specific and includes hard-coded infrastructure paths.
- `prune-default-skills.py` modifies the user's Hermes configuration and disables skills/toolsets; it is unrelated to fiction drafting and carries a large blast radius.
- `pass-1-reassembly-and-audit.py` and `normalize_typography.py` are potentially reusable manuscript utilities, but require validation, explicit input/output contracts, tests, and a safer home than an overloaded archive.

### 4.5 Existing templates demonstrate the better unit

The five novel-production-system skill templates have bounded triggers, explicit non-triggers, ordered steps, outputs, verification, and failure modes. That is the appropriate granularity. They also correctly load series-specific values from project files instead of embedding a whole series in the procedure.

## 5. Recommended split structure

Use a two-layer design: one lean router and a small set of task-class skills. Avoid turning every reference into a separate skill.

### A. `longform-fiction-production` — lean router/umbrella

Purpose:

- identify the current production phase;
- require repository, authority-stack, status/handoff, and git checks;
- enforce approval/stop gates;
- route to exactly one primary task-class skill;
- state that repository documents outrank examples and historical notes.

Keep this short. It should contain no series lore, no session-specific model table, no deploy procedure, and only a compact phase map.

### B. `fiction-project-governance-and-handoffs`

Use for:

- canonical-repository discovery and source hierarchy;
- status, tracker, decision log, completion note, and handoff updates;
- cross-session continuity and clean-pause/closure checks;
- git cleanliness, protected-file checks, commit/push verification;
- profile-to-repository role boundaries.

This skill should define the repository contract but load all project paths and current gates from the repository.

### C. `fiction-architecture-briefing-and-research-gates`

Use for:

- concept/architecture work;
- chapter-function maps and job statements;
- controlled chapter briefs;
- research-only dossiers before architecture;
- reveal/withholding gates expressed as repository-loaded inputs;
- review-and-refine requests that must stop before prose.

The existing research-ingest template can remain a separate general research skill if it serves non-fiction projects too; this fiction skill should only define how research is admitted into architecture/canon.

### D. `controlled-fiction-drafting-and-autonomous-runs`

Use for:

- one approved chapter from an approved brief;
- bounded multi-chapter pilots;
- sequential chapter drafting;
- autonomy grants, canaries, checkpoints, resumptions, and durable continuation;
- word-count/skeleton honesty;
- runtime and no-fallback checks when the repository or user requires them.

Keep cron/Hermes scheduling mechanics in a general Hermes automation skill and link to it rather than duplicating commands. This fiction skill defines the creative stop conditions and required artifacts.

### E. `fiction-editorial-audits-and-revision-planning`

Use for read-only or planning work:

- discovery pass;
- structural reader audit/readiness;
- developmental editorial;
- external review packet/consolidation;
- targeted revision-plan synthesis;
- continuity and voice audits;
- necessity reviews;
- model-lane advisory audits where no prose may change.

This skill must preserve the distinction among inventory, judgement, and planning. It should not edit prose.

### F. `controlled-fiction-revision-and-expansion`

Use for prose-changing passes:

- targeted developmental fixes;
- Pass 1/Pass 2 workspaces;
- skeleton-to-full-draft expansion;
- dramatization and dialogue-desert repair;
- line-level cadence/consistency cleanup;
- micro-polish;
- interrupted-pass resumption.

Require per-chapter scope, protected-source checks, actual word-count/assembly verification, and a stop boundary. General methods belong here; series-specific expansion targets remain in repo-local plans.

### G. `fiction-assembly-final-qa-and-freeze`

Use for:

- ordered manuscript assembly;
- chapter/title/heading validation;
- artifact and duplicate checks;
- proofread/export gates;
- baseline/checkpoint creation;
- source parity and hashes;
- final freeze and phase closure.

Reusable assembly scripts can live here only after tests and explicit safeguards. This skill should not include site deployment.

### H. Separate adjacent domains rather than forcing them into fiction drafting

1. **`reader-package-and-feedback-workflow`**: reader packages, feedback forms, feedback archival, reader-facing site generation. If deployment is needed, delegate the deploy step to a general static-site/VPS deployment skill with explicit approval.
2. **`controlled-model-evaluation-for-creative-work`**: frozen inputs, isolated outputs, blind mapping, identity commitment/reveal, evaluation sequence, synthesis, and canonical-promotion gates. This is experimental governance, not routine drafting.

This gives one router plus six core production skills and two adjacent specialist skills. If that initially feels too large, combine B with A during the first migration, but do not combine read-only editorial planning (E) with prose-changing revision (F).

## 6. Per-series Hermes skills versus repo-local series knowledge

### Recommendation

**Do not create per-series Hermes skills as the default architecture.** Keep series-specific knowledge in the canonical series repository.

### Why repo-local knowledge is superior

- It travels with the manuscript, branches, history, reviews, and handoffs.
- Git provides versioning, review, provenance, and rollback.
- All profiles and future agents can read one authority stack.
- It prevents stale duplicates between a skill and the creative repository.
- It avoids leaking one series' voice, characters, reveal order, or paths into another.
- A series can evolve without requiring global Hermes-skill maintenance.

Repo-local series knowledge should include, as applicable:

- `SOUL.md` or `series/SERIES_SOUL.md`
- `SERIES_LENGTH_STANDARD.md`
- series and character bibles
- voice guardrails/style rules
- book architecture and chapter briefs
- reveal/withholding ledger
- status, tracker, decision log, and handoff
- editorial reports and current revision plan
- model/runtime policy only when it is truly a current project gate

### Where Hermes profiles fit

Series-specific profiles can be justified when they supply a stable role, working directory, permission boundary, or fresh-reader separation. A profile's role instructions should remain concise and point into the canonical repository. A profile is not a substitute for a series skill, and neither should duplicate canon.

### Narrow exception

A thin per-series adapter could be tolerated only when tool routing cannot reliably locate the canonical repo. It should contain no lore or duplicated canon—only a stable repository pointer, role, authority-file list, and instruction to stop if those files are missing or contradictory. Even then, a profile configuration or repo-local `AGENTS.md` is usually the better place.

## 7. Concrete migration sequence

This sequence is intentionally non-destructive.

1. **Freeze and inventory.** Record the current 266-file tree, hashes, sizes, inbound links, and references from profiles/prompts. Do not move or delete anything yet.
2. **Create a classification manifest.** Assign every reference/template/script one disposition: reusable procedure, reusable template, reusable utility, repo-local series/book case, infrastructure/deployment, model-experiment governance, duplicate/superseded, or unsafe/out-of-scope. Include destination and canonical authority.
3. **Define repository contracts first.** Standardise the minimum authority stack expected in each creative repo: identity, bible, voice, architecture, status, handoff, tracker, decision log, and reports. Fill missing canonical copies before removing any skill-hosted case material.
4. **Draft candidate skills in a staging area or feature branch.** Build the router and task-class skills outside the live Hermes skill directory. Start from the existing task-oriented templates where suitable.
5. **Extract principles, not stories.** Convert each useful case into a short generic rule/checklist. Preserve the full named case in its canonical repo or an explicit case-study area in `novel-production-system`; link to it only when needed.
6. **Separate adjacent domains.** Move reader-site generation/feedback operations toward reader-package tooling and route deployment to a dedicated deployment skill. Move blind model experiments to their own controlled-evaluation skill. Quarantine unrelated profile/config maintenance from fiction skills.
7. **Review utilities before relocation.** Add fixtures/tests, dry-run behavior, path validation, overwrite protection, and documented contracts for reusable manuscript scripts. Do not migrate hard-coded or configuration-mutating scripts merely because they already exist.
8. **Run representative canaries.** Test at least: one architecture/brief-only gate, one controlled chapter, one read-only audit, one targeted revision, one assembly/final-QA pass, and one resume/handoff scenario. Use different series repos to detect contamination.
9. **Run legacy-versus-new comparisons.** For each canary, compare required files loaded, unauthorized actions, output artifacts, stop behavior, and verification results. Fix routing gaps before changing the live skill.
10. **Introduce a compatibility period.** Keep the legacy skill intact while the proposed router points test users to staged task skills. Add deprecation notices only after canaries pass and inbound references are known.
11. **Install only after explicit approval.** Make live Hermes changes as a separate reviewed operation. Update profile/prompt references atomically and retain a rollback snapshot.
12. **Archive/delete last.** Remove duplicates or old cases only after canonical destination verification, link checking, and a defined retention period. Deletion is not part of the initial split.

## 8. Risks and things not to do

- **Do not split by series.** That multiplies stale canon and procedure copies.
- **Do not split one file into one skill.** Excessive fragmentation creates routing noise; split by stable task class.
- **Do not move series cases until their canonical repo contains the complete authoritative record.** A filename that mentions a series is not proof that the repo has an equivalent copy.
- **Do not let historical examples override current repo gates.** Chapter numbers, reveal rules, model requirements, and paths can expire.
- **Do not preserve exact model/provider assignments as universal fiction rules.** Treat them as current user/repo constraints and verify runtime when required.
- **Do not mix read-only audit, revision planning, and prose editing.** Their permissions and stop conditions differ.
- **Do not keep VPS deployment or server credentials/paths in a drafting skill.** Deployment has separate safety and approval requirements.
- **Do not run or relocate `prune-default-skills.py` as a fiction utility.** It edits Hermes configuration and disables broad skill/tool sets; it is outside this skill's domain and high-impact.
- **Do not treat `sync-brambleford-feedback.sh` as reusable without removing project/server coupling and destructive-sync risk.** Its current `rsync --delete` behavior deserves explicit safeguards.
- **Do not trust the current reassembly script without tests.** Assembly utilities must verify natural chapter order, expected chapter count, output naming, marker scans, and non-destructive behavior.
- **Do not delete the legacy skill immediately.** First classify all files, test replacements, update inbound references, and prove rollback.
- **Do not confuse profiles with skills.** Profiles define roles/runtime/workspaces; skills define reusable procedures; repositories hold canon and live state.
- **Do not make the router another archive.** Its value is concise dispatch and authority rules.

## 9. Concise executive verdict

The skill should be split now in design, then migrated cautiously. Use task/class-level skills around governance, architecture/briefing, controlled drafting/autonomy, read-only editorial/planning, prose revision/expansion, and assembly/final QA. Put reader packaging/deployment and controlled model experiments in adjacent specialist skills. Keep all series identity and live book knowledge in canonical series repositories, optionally accessed by series-specific profiles. Preserve the current skill until every reference is classified, canonical destinations are verified, and staged replacements pass cross-series canaries.
