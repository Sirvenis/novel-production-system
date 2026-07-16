# Arden Studios Repository Governance Model

## A Constitutional Document

**Version:** 1.0.0
**Established:** 2026-07-16
**Authority:** Derived from the migration of *The Better Version* from `novel-production-system` to its own canonical creative repository.

---

## I. First Principle

> Every repository exists to preserve **one constitutional purpose**.
>
> Repository classes are expressions of that principle, not exceptions to it.

This principle is older than any specific repository. It is the reason the separation works. When a repository forgets its purpose, it begins to accumulate material that belongs elsewhere. That accumulation is not merely untidy. It is a privacy risk, a maintenance burden, and a source of confusion about where the ground truth lives.

The constitutional purpose of a repository is not its *description*. It is the single reason the repository would still deserve to exist if every file inside it had to be justified individually.

---

## II. Why This Model Exists

### The Failure It Prevents

Before this model, Arden Studios maintained creative material and reusable infrastructure in the same public repository. The result was predictable:

1. **Unpublished manuscripts lived in public commit history.** A chapter draft, a series bible containing full endings and sequel hooks, and character backstories were all technically public. The repository was not marketed, but public is public.

2. **Infrastructure became project-contaminated.** Templates, case studies, and reusable pipelines were interleaved with project-specific voice guardrails, setting decisions, and candidate comparisons. A new project cloning the system would inherit material from an unrelated series.

3. **Version history lost meaning.** Commits that changed craft rules were mixed with commits that changed chapter prose. The history of the pipeline became unreadable.

4. **Decision trails were hard to recover.** A setting decision made in the context of one series was buried in a general-purpose repository. Future projects could not learn from it because it was not where they expected to find it.

### What Experience Taught Us

The migration of *The Better Version* (July 2026) proved that the boundary between infrastructure and creative material is not a matter of preference. It is a matter of safety and clarity.

The migration took one project-specific file after another out of `novel-production-system` and placed it in a dedicated private repository. Each move revealed the same pattern: the file had been convenient where it was, but it had never belonged there. The convenience was a local optimum. The boundary was a global one.

The verification table that confirmed the migration's success was simple:

| Repository | Constitutional Purpose | Unpublished Manuscripts? | Series Architecture? | Character Voice Rules? | Reusable Templates? | Production Pipeline Docs? |
|---|---|---|---|---|---|---|
| `novel-production-system` | Reusable infrastructure | No | No | No | Yes | Yes |
| `the-better-version` | Canonical creative project | Yes | Yes | Yes | No | No |

That table is the operational proof of the First Principle.

---

## III. Repository Classes

Repository classes are named patterns that arise from applying the First Principle to the actual work of producing novels. They are not prescriptive categories invented in advance. They are descriptive patterns extracted from repeated experience.

The current Arden Studios ecosystem recognises four classes.

---

### Class A: Infrastructure Repositories

**Constitutional purpose:** To preserve reusable production systems, templates, and institutional knowledge.

**What this means in practice:**

An infrastructure repository contains everything a new project needs to set up its own production pipeline, and nothing that belongs to any specific project. It is the workshop, not the work.

**Contents:**
- Production stage definitions and editorial criteria
- Blank templates (architecture, trackers, handoffs, reports)
- Generic craft techniques and genre-agnostic rules
- Anonymised case studies from past production
- Cross-project references and execution patterns
- Getting-started and adaptation guides

**Exclusions:**
- No manuscripts, drafts, or unpublished creative material
- No project-specific architecture, bibles, or character designs
- No voice guardrails tied to a specific protagonist or setting
- No decision logs from individual projects (unless fully anonymised and framed as pattern illustration)

**Visibility:** Typically public. The system is a contribution to craft, not a secret.

**Current example:** `Sirvenis/novel-production-system`

**Why this class exists:**
When Arden Studios began producing multiple series in parallel, it became clear that each series was reinventing the same tracking systems, the same editorial stages, and the same handoff patterns. The infrastructure repository centralises that learning so that each new series can begin with tested methods rather than naive experiments.

**Failure this prevents:**
Without this class, every new project begins from zero. With it, each project begins from the best understanding the studio has accumulated.

**What experience taught us:**
The 9-stage pipeline, the Four Questions of developmental editorial, the Verification Rule, and the handoff system all emerged from producing three complete books. None of them would have been preserved if each project had kept its own private notes. The infrastructure repository is institutional memory made explicit.

---

### Class B: Canonical Creative Repositories

**Constitutional purpose:** To preserve the definitive version of a single creative project.

**What this means in practice:**

A canonical creative repository is the ground truth for one novel or one series. It contains the manuscripts, the architecture, the decision trail, the reviews, and the handoffs for that project and no other. If the repository were lost, the project would have to be reconstructed from memory and scattered files.

**Contents:**
- Series bible and book-level architecture
- Chapter drafts and revision history
- Voice guardrails and character bibles
- Decision logs (candidates, comparisons, setting choices)
- Editorial reviews and reader audits
- Session handoffs and project tracking
- References copied from the infrastructure repository for local convenience

**Exclusions:**
- No reusable templates (use the infrastructure repository; copy blanks into the project)
- No production pipeline definitions (reference the infrastructure repository)
- No case studies from other projects
- No cross-project infrastructure

**Visibility:** Private. Unpublished manuscripts, plot spoilers, and character endings must not be public.

**Naming convention:** The repository name should identify the project, not the genre or the author. `the-better-version`, not `horror-novel-2026` or `elias-silver-book`.

**Current example:** `Sirvenis/the-better-version`

**Why this class exists:**
Creative material needs a single canonical home. When a draft exists in a chat log, a local file, a cloud drive, and a repository simultaneously, no version is authoritative. The canonical repository resolves that ambiguity. Its HEAD is the current truth. Its history is the project's memory.

**Failure this prevents:**
Without this class, drafts proliferate across channels. A chapter revised in a chat session may never be written back to the file. A setting decision made in a handoff may never reach the architecture document. The canonical repository is the single place where the project converges.

**What experience taught us:**
The `kimi-horror-lab` repository (now `Sirvenis/kimi-horror-lab`) for *The Last Clean-Up Crew* demonstrated that a dedicated creative repository enables continuous drafting with confidence. The writer knows where the manuscript lives. The editor knows where to find the latest version. The showrunner knows the decision trail is intact. That confidence is impossible when creative material is mixed with infrastructure.

---

### Class C: Working Repositories

**Constitutional purpose:** To preserve experimental or transitional material that may or may not become canonical.

**What this means in practice:**

A working repository is a scratchpad. It holds experiments, alternative versions, tool-specific outputs, and material that is being evaluated before it is promoted to a canonical repository. It is where the messy work happens.

**Contents:**
- Experimental drafts or alternative chapters
- Tool outputs (AI-assisted rewrites, summarisation, analysis)
- Scout or agent-specific working forks
- Prototypes, tests, and evaluation material
- Material that may be discarded without loss to the canonical project

**Exclusions:**
- No material that is the current ground truth for the project
- No irreversible decisions (working repos are expendable)

**Visibility:** Typically private. Working material is often rough and may contain material that will not survive editorial review.

**Naming convention:** The repository name should signal its subordinate status. Append `-work`, `-test`, `-scout-work`, or `-lab` to the canonical project name.

**Current examples:**
- `Sirvenis/brambleford-scout-work` (Scout working fork of *Brambleford*)
- `Sirvenis/meridian-scout-work` (Scout experiments on *The Meridian Relics*)
- `Sirvenis/cozy-mystery-lab` (local Ollama competitive author lab)

**Why this class exists:**
Not every experiment deserves to live in the canonical repository. A working repository gives agents and tools a place to iterate without polluting the project's ground truth. If an experiment fails, the working repository can be archived or deleted. If it succeeds, its results are merged into the canonical repository through a deliberate editorial decision.

**Failure this prevents:**
Without this class, experimental material accumulates in the canonical repository. Commits become noisy. History becomes cluttered with attempts that did not survive. The canonical repository loses its authority because it contains too much that is not authoritative.

**What experience taught us:**
The `brambleford-scout-work` repository exists because Scout (an alternative agent) needed a place to experiment with commercial edits and alternative phrasings without risking the main *Brambleford* manuscript. The separation allows the human editor to compare Scout output against the canonical version and decide what to promote. That decision is only possible because the two repositories are distinct.

---

### Class D: Publication Repositories

**Constitutional purpose:** To preserve publication-ready artifacts and their distribution infrastructure.

**What this means in practice:**

A publication repository holds the material that reaches readers: websites, e-book builds, audio files, cover images, and marketing copy. It is the interface between the studio and the audience.

**Contents:**
- Website source code and assets
- E-book generation scripts and outputs
- Cover designs and promotional material
- Reader-facing metadata (blurbs, series descriptions)
- Distribution configuration (RSS feeds, store listings, newsletter templates)

**Exclusions:**
- No manuscripts or drafts (those live in the canonical creative repository)
- No editorial reviews or decision logs (those live in the canonical creative repository)
- No production pipeline definitions (those live in the infrastructure repository)

**Visibility:** Typically public or selectively shared. A reader-facing website is public by definition.

**Naming convention:** Append `-website`, `-reader-site`, or `-publication` to the canonical project or series name.

**Current examples:**
- `Sirvenis/elias-silver-library` (reader site and fiction production studio)
- `Sirvenis/elias-silver-library-website` (local development copy)
- `Sirvenis/meridian-relics-website`
- `Sirvenis/brambleford-mysteries-website`
- `Sirvenis/last-clean-up-crew-website`

**Why this class exists:**
Publication requires different tooling, different review cycles, and different collaborators than writing. A website developer does not need access to unrevised chapter drafts. A cover designer does not need the series bible. The publication repository gives each role exactly what it needs and nothing more.

**Failure this prevents:**
Without this class, publication assets are mixed with manuscripts. A website deployment might accidentally include a draft chapter. A build script might reference a file that has since been revised. The separation ensures that what reaches readers is deliberately chosen, not incidentally exposed.

**What experience taught us:**
The Elias Silver Library (`elias-silver-library`) and its associated website repositories demonstrated that reader-facing material needs its own lifecycle. A book launch does not happen at the same pace as a chapter revision. The publication repository allows marketing material to be prepared, reviewed, and deployed independently of the writing schedule.

---

## IV. Boundary Rules

Repository classes are only meaningful if the boundaries between them are respected. The following rules govern how material moves across boundaries.

### Rule 1: One Direction of Authority

**The canonical creative repository is the ground truth for creative material.**

No other repository may claim to hold the current version of a manuscript, a character design, or a series architecture. Working repositories may propose alternatives. Publication repositories may display extracts. Infrastructure repositories may quote anonymised passages as case studies. But the canonical repository decides what is true.

**Why this rule exists:**
Without a single ground truth, every repository becomes a competing claimant. An editor reviews a draft from the working repository while the writer revises the canonical version. The result is divergence and confusion.

**What experience taught us:**
During *The Last Clean-Up Crew* production, the `kimi-horror-lab` repository became the de facto ground truth because it was the only place where the complete manuscript, the series bible, and the character bible were all maintained together. Every other copy was a derivative. That concentration of authority was discovered, not designed. This rule makes it explicit.

### Rule 2: Templates Cross; Content Does Not

**Reusable templates move from infrastructure to creative repositories. Creative material never moves from creative to infrastructure.**

When a new project begins, it copies templates from the infrastructure repository into its own canonical repository and fills them in. The filled-in templates become project-specific documents and remain in the creative repository. They do not get merged back into the infrastructure repository.

Exception: If a project discovers a genuinely new pattern that should be available to all future projects, that pattern is extracted, anonymised, and added to the infrastructure repository as a new template or case study. The project-specific document stays where it is.

**Why this rule exists:**
The infrastructure repository must remain generic. If every project's filled-in architecture were merged back, the templates would become contaminated with specific examples and would no longer be blank.

**What experience taught us:**
The `ARCHITECTURE_TEMPLATE.md` in `novel-production-system` is a blank shell with annotations. The filled-in `BOOK_1_CHAPTER_ARCHITECTURE.md` for *The Better Version* is 568 lines of specific plot beats, character functions, and escalation maps. Those 568 lines would ruin the template for the next project. The boundary protects the template's reusability.

### Rule 3: Working Repositories Are Ephemeral

**A working repository may be archived or deleted without notice.**

No material that would be lost to the project should live exclusively in a working repository. Working repositories are scratchpads. Their purpose is to hold material that might be useful, not material that must be preserved.

**Why this rule exists:**
Working repositories accumulate quickly. If they are treated as permanent, they become a second layer of canonical material and the boundary collapses.

**What experience taught us:**
The `meridian-scout-work` repository was created for Scout to experiment with *The Meridian Relics*. Its contents are valuable only while the experiment is active. Once the human editor has extracted the useful insights and merged them into the canonical repository, the working repository has served its purpose. Treating it as permanent would create an unmaintained shadow copy.

### Rule 4: Publication Repositories Derive from Canonical

**Publication repositories receive material from canonical creative repositories through an explicit editorial gate.**

A chapter does not appear on a website because it was drafted. It appears because it has passed through the pipeline, been approved for publication, and been explicitly promoted. The promotion is a deliberate act, not an automatic sync.

**Why this rule exists:**
Readers should not see drafts. A website that automatically reflects the latest commit in a creative repository would expose unfinished work, rejected alternatives, and potential spoilers.

**What experience taught us:**
The Elias Silver Library website (`elias-silver-library`) displays completed, edited books. It does not display works in progress. That separation is maintained by manual promotion: when a book is frozen and approved for publication, its material is copied to the website repository. The manual step is the gate.

---

## V. The Migration Principle

When material is discovered to be in the wrong repository, it should be migrated according to these steps:

1. **Classify the material.** Determine its constitutional purpose. Which repository class should hold it?

2. **Create the destination if it does not exist.** A new canonical creative repository should be private, named for the project, and given a single initial commit explaining its purpose.

3. **Move the material with restructure.** Do not blindly copy the old directory tree. Reorganise the material to reflect the project's actual life: series bibles belong in `series/`, book architectures in `book-N/`, voice guardrails in `voice/`, decisions in `decisions/`, reviews in `reviews/`, handoffs in `handoff/`.

4. **Remove from the source.** Delete the material from the original repository's HEAD. Do not rewrite history unless there is a specific, authorised reason to do so.

5. **Update cross-references.** Any document in the infrastructure repository that referenced the moved material should be updated to reference the new location or replaced with a generic template.

6. **Verify the boundary.** Produce a verification table showing that each repository now holds only material consistent with its constitutional purpose.

**Why this principle exists:**
Migration is not merely file movement. It is the enforcement of constitutional boundaries. A sloppy migration leaves material behind, creates broken references, and fails to teach the system what went wrong.

**What experience taught us:**
The migration of *The Better Version* followed this principle. The material was not merely copied; it was reorganised into a structure (`series/`, `book-1/`, `voice/`, `decisions/`, `reviews/`, `handoff/`, `references/`) that reflected the project's actual life. The old `handoff/MASTER-HANDOFF.md` was replaced with a generic template. The verification table confirmed the boundary. The result was not two copies of the same files. It was two correctly constituted repositories.

---

## VI. Governance of This Document

### Amendment Process

This document is intentionally provisional.

It records the current best understanding of repository governance within Arden Studios. Amendments should be driven by repeated experience rather than theoretical preference.

**Stability is desirable. Correctness is essential.**

A proposed amendment must satisfy three tests:

1. **Experience test.** The amendment must be grounded in at least one specific incident where the current rule produced a failure or a near-failure.

2. **Generality test.** The amendment must apply to more than one project. A rule that serves only a single series is a project decision, not a governance rule.

3. **Compatibility test.** The amendment must not contradict the First Principle. Repository classes may evolve, but the principle that each repository preserves one constitutional purpose is foundational.

Amendments are made by pull request to this document in the `novel-production-system` repository, accompanied by a case study or incident report explaining the need for the change.

### Versioning

This document follows semantic versioning:

- **Major:** New repository class added or removed, or a class fundamentally redefined
- **Minor:** New boundary rule, new migration step, or new amendment process detail
- **Patch:** Correction, clarification, or correction of an error in the document

Current version: **1.0.0**

---

## VII. Evolution

This section records how this document itself changes.

### 1.0.0 — 2026-07-16

**Established after:** The migration of *The Better Version* from `novel-production-system` to `Sirvenis/the-better-version`.

**What happened:**
Arden Studios discovered that its infrastructure repository had accumulated 3,521 lines of project-specific creative material across ten files. The material included an unpublished chapter draft, a complete 5-book series architecture, character voice guardrails, and project-specific decision logs. The repository was public, making the unpublished material technically accessible.

**What was done:**
A new private repository was created. The material was moved, restructured, and committed with a single initial commit. The infrastructure repository's HEAD was cleaned of creative material. A generic handoff template replaced the project-specific master handoff. The README was updated to explain the two-repository pattern.

**What was learned:**
The separation of infrastructure and creative material is not a matter of tidiness. It is a matter of privacy, clarity, and institutional memory. The infrastructure repository is the workshop; the creative repository is the work. The boundary between them must be maintained deliberately, not assumed.

**Result:**
This document. Four repository classes. Six boundary rules. One migration principle. An amendment process. And the understanding that the model will evolve as Arden Studios encounters new failures and corrects them.

---

## Appendix: Current Arden Studios Repository Map

| Repository | Class | Purpose | Visibility |
|---|---|---|---|
| `novel-production-system` | Infrastructure | Reusable production pipeline, templates, case studies | Public |
| `the-better-version` | Canonical Creative | *The Better Version* (5-book horror series) | Private |
| `kimi-horror-lab` | Canonical Creative | *The Last Clean-Up Crew* (cosmic horror-comedy) | Private |
| `meridian-relics` | Canonical Creative | *The Meridian Relics* series | Private |
| `anunnaki-chronicles-novel` | Canonical Creative | *The Anunnaki Chronicles* prose novel | Private |
| `brambleford-mysteries` | Canonical Creative | *Brambleford Cozy Mystery* series | Private |
| `brambleford-scout-work` | Working | Scout experiments on *Brambleford* | Private |
| `meridian-scout-work` | Working | Scout experiments on *Meridian Relics* | Private |
| `anunnaki-scout-work` | Working | Scout experiments on *Anunnaki Chronicles* | Private |
| `cozy-mystery-lab` | Working | Local Ollama competitive author lab | Private |
| `elias-silver-library` | Publication | Reader site and fiction production studio | Private |
| `elias-silver-library-website` | Publication | Local dev for Elias Silver Library | Private |
| `meridian-relics-website` | Publication | *The Meridian Relics* web presence | Private |
| `brambleford-mysteries-website` | Publication | *Brambleford* web presence | Private |
| `arden-studios-website` | Publication | Arden Studios main website | Private |

---

*This document is part of the `novel-production-system` repository. It is licensed under the same terms as the rest of the repository. It is a living document. Treat it as one.*
