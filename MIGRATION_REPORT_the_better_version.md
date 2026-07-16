# Migration Report: The Better Version — Canonical Repository Establishment

## Discovery and Migration Planning Pass

**Date:** 2026-07-16
**Requested by:** Arden (Priority 1 of GitHub Review)
**Scope:** Establish correct canonical home for *The Better Version* creative material
**Constraint:** No moves, deletes, rewrites, or repo creation during this pass

---

## 1. LOCAL REPOSITORY STATE

### Discovered Paths

| Path | Status |
|------|--------|
| `/home/andrew/novel-production-system` | Active local clone, main branch, clean working tree |
| `/home/andrew/kimi/horror-series-1/novel-production-system` | Empty git repo (no commits), NOT the active working copy |

### Git State (primary clone)

| Property | Value |
|----------|-------|
| Branch | `main` |
| Working tree | Clean |
| Total commits | 17 |
| Latest commit | `1130273` — "Session handoff: Phase Six complete, paused for housekeeping" |
| Remote | `https://github.com/Sirvenis/novel-production-system.git` |
| Tag | `v1.0.0` |

### GitHub State

| Property | Value |
|----------|-------|
| `gh auth status` | Authenticated as `Sirvenis` |
| Token scopes | `gist`, `read:org`, `repo`, `workflow` |
| Target repo exists? | **NO** — `Sirvenis/the-better-version` returned "Could not resolve to a Repository" |
| Naming conflict? | **NONE** — `the-better-version` is not in the 20-repo list |

---

## 2. FILE INVENTORY AND CLASSIFICATION

### Classification Key

| Code | Meaning |
|------|---------|
| **MOVE** | Move to new creative repository; remove from `novel-production-system` |
| **COPY** | Copy to new repository; retain anonymised/generic version in `novel-production-system` |
| **REMAIN** | Keep in `novel-production-system` as reusable infrastructure |
| **REVIEW** | Requires human judgment before classification |

---

### 2A. The Better Version Project-Specific Files (MOVE)

| # | File | Lines | Classification | Reason |
|---|------|-------|--------------|--------|
| 1 | `docs/THE_BETTER_VERSION_ARCHITECTURE.md` | 581 | **MOVE** | Series bible: protagonist design, 5-book architecture, setting decision, South Yorkshire details, fear escalation model, commercial positioning. Purely creative. |
| 2 | `docs/CANDIDATES_PHASE_THREE.md` | 661 | **MOVE** | Candidate generation material for this project. 10 fear-driven horror candidates with evaluations. Project-specific creative origin. |
| 3 | `docs/SEMI_FINALIST_COMPARISON.md` | 296 | **MOVE** | Semi-finalist comparison (Candidates 1, 2, 10) with Arden fit scores, commercial analysis, and Phase Four verdict. Project-specific decision record. |
| 4 | `docs/VOICE_GUARDRAILS_SOUTH_YORKSHIRE.md` | 171 | **MOVE** | Voice guardrails for Diana "Di" Calloway. Contains character-specific rules, prohibited constructions, Confidence Test. Belongs to this series. |
| 5 | `docs/BOOK_1_CHAPTER_ARCHITECTURE.md` | 568 | **MOVE** | Book 1 chapter-level architecture: 18 chapter Job Statements, escalation map, replacement-rule progression, emotional arc, cast function map, mystery/withholding plan. Purely creative. |
| 6 | `drafts/THE_BETTER_VERSION_CHAPTER_1.md` | 368 | **MOVE** | Chapter 1 manuscript (3,612 words). Unpublished creative material. Must leave public repo. |
| 7 | `reviews/CHAPTER_1_REVIEW_PACKAGE.md` | 423 | **MOVE** | Chapter 1 review package containing full draft text, review questions, flagged passage. Contains unpublished manuscript. |
| 8 | `reviews/CHAPTER_1_VOICE_TEST_REVIEW.md` | 179 | **MOVE** | Voice test review report with line-by-line dialect density check, class texture analysis, setting authenticity assessment. Project-specific. |
| 9 | `handoff/MASTER-HANDOFF.md` | 149 | **MOVE** | Current handoff is entirely The Better Version state (Phases 1-6, candidate status, next tasks). Must become project-local. |
| 10 | `handoffs/SESSION_HANDOFF_2026-07-16.md` | 125 | **MOVE** | Session handoff for The Better Version Phase Six. Contains project decisions, file inventory, next tasks. Project-specific. |

**Total project-specific lines:** **~3,521 lines** of creative/project material currently in a public infrastructure repository.

---

### 2B. Files to COPY (retain anonymised version in infrastructure)

| # | File | Classification | Reason |
|---|------|---------------|--------|
| 11 | `docs/ARDEN_SIGNATURE.md` | **COPY** | Arden Studios horror philosophy (6 pillars, voice rules, reader experience). This is institutional knowledge that should remain in `novel-production-system` as reusable reference. The new repo should also have a copy as project context. |

---

### 2C. Files that REMAIN in `novel-production-system`

| Category | Files | Reason |
|----------|-------|--------|
| **Repository definition** | `README.md`, `.gitignore` | Infrastructure identity |
| **Getting-started docs** | `docs/GETTING_STARTED.md`, `docs/REPO_ORGANISATION.md`, `docs/ADAPTATION_GUIDE.md` | Reusable deployment instructions |
| **General horror research** | `docs/HORROR_LANDSCAPE_SURVEY.md` (400 lines), `docs/WHAT_CREATES_FEAR.md` (100 lines), `docs/WHAT_DESTROYED_MONSTERS.md` (184 lines) | Genre-agnostic research applicable to any horror project |
| **Production pipeline** | `infrastructure/PRODUCTION_PIPELINE.md`, `EDITORIAL_STAGES.md`, `MULTI_PROFILE_WORKFLOW.md`, `CRAFT_TECHNIQUES.md`, `TRACKING_SYSTEM.md`, `HANDOFF_SYSTEM.md`, `GIT_WORKFLOW.md`, `EVOLUTION.md` | Reusable infrastructure |
| **Templates** | `templates/ARCHITECTURE_TEMPLATE.md`, `CHAPTER_JOB_STATEMENT.md`, `DECISION_LOG_ENTRY.md`, `EDITORIAL_REPORT.md`, `HANDOFF_TEMPLATE.md`, `READER_AUDIT_TEMPLATE.md`, `SOUL_MD_PATTERN.md`, `TRACKER_TEMPLATE.md` | Reusable blanks for any new project |
| **Case studies** | `case-studies/horror-series-production/OVERVIEW.md`, `BOOK1_LESSONS.md`, `BOOK2_LESSONS.md`, `BOOK3_LESSONS.md`, `PIPELINE_EVOLUTION.md` | Anonymised lessons from prior production |
| **References** | All 21 files in `references/` | Reusable craft patterns, execution workflows, verification rules |

**Total remaining lines:** ~7,400+ lines of reusable infrastructure.

---

### 2D. UNCERTAIN — Requires Review

| # | File | Uncertainty | Recommendation |
|---|------|-------------|----------------|
| 12 | `handoff/MASTER-HANDOFF.md` | This file is referenced in `infrastructure/HANDOFF_SYSTEM.md` as the canonical primary handoff. Moving it breaks the infrastructure's self-documentation. | **Option A:** Move the current content to the new repo as its MASTER_HANDOFF.md, then replace the original with a generic template/example handoff. **Option B:** Keep a generic MASTER_HANDOFF.md template in `novel-production-system` and move the populated version to the new repo. |

**Resolution:** Prefer Option A. The populated handoff is project-specific. The infrastructure doc should reference a template, not a live project file.

---

## 3. PRIVACY RISK ASSESSMENT

### Critical Finding

The following **unpublished creative material** is currently in a **public** GitHub repository (`Sirvenis/novel-production-system` is public):

| Material | Location | Risk |
|----------|----------|------|
| Complete Chapter 1 draft (3,612 words) | `drafts/THE_BETTER_VERSION_CHAPTER_1.md` | **HIGH** — Unpublished manuscript in public repo |
| Full 5-book series architecture | `docs/THE_BETTER_VERSION_ARCHITECTURE.md` | **HIGH** — Complete series spoilers, endings, sequel hooks |
| Book 1 chapter-by-chapter plan | `docs/BOOK_1_CHAPTER_ARCHITECTURE.md` | **HIGH** — Detailed plot beats for entire book |
| Character design (Di Calloway, replacement, cast) | `docs/THE_BETTER_VERSION_ARCHITECTURE.md` | **MEDIUM** — Character details, backstories |
| Voice guardrails (character voice rules) | `docs/VOICE_GUARDRAILS_SOUTH_YORKSHIRE.md` | **LOW** — Craft rules, not story content |
| Review package (contains full Chapter 1) | `reviews/CHAPTER_1_REVIEW_PACKAGE.md` | **HIGH** — Duplicate of manuscript text |

### Git History Risk

Even after files are removed from the working tree, **Git history retains all content**. The Chapter 1 draft, series architecture, and all creative material will remain in the commit history of `novel-production-system` unless history is rewritten.

**Mitigation options:**
1. **Accept:** Leave history intact. The repo is public but not marketed. Risk is low unless someone actively digs through history.
2. **Filter-branch:** Use `git filter-branch` or `git-filter-repo` to remove creative files from all commits. **Risk:** Rewrites history, invalidates existing clones, requires force-push. Dangerous for a repo that may have other users.
3. **Archive and replace:** Create a new `novel-production-system` repo (or force-push a cleaned history), archive the old one. **Risk:** Breaks external references.

**Recommendation:** Accept Option 1 for now. The repo is public but not indexed or marketed. The creative files will be removed from HEAD, which is sufficient practical protection. History cleanup can be a separate Priority 6 task if desired.

---

## 4. PROPOSED NEW REPOSITORY STRUCTURE

**Repository:** `Sirvenis/the-better-version` (private)
**Purpose:** Canonical creative repository for the series

```
the-better-version/
├── README.md                              # Project-specific README
│
├── series/
│   └── SERIES_BIBLE.md                    # From THE_BETTER_VERSION_ARCHITECTURE.md
│                                          # (5-book architecture, core wound, rules, risks)
│
├── book-1/
│   ├── ARCHITECTURE.md                    # From BOOK_1_CHAPTER_ARCHITECTURE.md
│   │                                      # (18 chapter Job Statements, escalation, arcs)
│   ├── drafts/
│   │   └── chapter-1-the-regular-customer.md   # From THE_BETTER_VERSION_CHAPTER_1.md
│   └── ... (future chapters)
│
├── voice/
│   └── VOICE_GUARDRAILS.md                # From VOICE_GUARDRAILS_SOUTH_YORKSHIRE.md
│
├── decisions/
│   ├── CANDIDATES.md                      # From CANDIDATES_PHASE_THREE.md
│   ├── SEMI_FINALIST_COMPARISON.md        # From SEMI_FINALIST_COMPARISON.md
│   └── SETTING_DECISION.md                # (extracted or referenced from series bible)
│
├── reviews/
│   ├── chapter-1-review-package.md        # From CHAPTER_1_REVIEW_PACKAGE.md
│   └── chapter-1-voice-test.md            # From CHAPTER_1_VOICE_TEST_REVIEW.md
│
├── handoff/
│   ├── MASTER_HANDOFF.md                  # Populated from current MASTER-HANDOFF.md
│   └── archive/
│       └── session-handoff-2026-07-16.md  # From SESSION_HANDOFF_2026-07-16.md
│
└── references/
    └── ARDEN_SIGNATURE.md                 # Copy of institutional philosophy (for local context)
```

**Rationale:**
- Flat enough for quick navigation; nested enough for 5-book series growth
- `series/` holds cross-book material; `book-N/` holds per-book material
- `decisions/` preserves the creative decision trail
- `handoff/` follows the infrastructure pattern but is project-local
- `references/` includes a copy of `ARDEN_SIGNATURE.md` for convenience

---

## 5. PROPOSED MIGRATION SEQUENCE

### Step 1: Create the new repository
```bash
gh repo create the-better-version --private --description \
  "The Better Version — canonical creative repository for the 5-book horror series by Arden Studios"
```

### Step 2: Clone locally
```bash
cd /home/andrew
git clone https://github.com/Sirvenis/the-better-version.git
cd the-better-version
```

### Step 3: Populate with project files
Copy all MOVE-classified files into the proposed structure above.

### Step 4: Initial commit
```bash
git add .
git commit -m "Initial commit: The Better Version series bible, Book 1 architecture, Chapter 1 draft, voice guardrails, and decision records"
git push origin main
```

### Step 5: Clean `novel-production-system` HEAD
```bash
cd /home/andrew/novel-production-system
git rm docs/THE_BETTER_VERSION_ARCHITECTURE.md \
       docs/CANDIDATES_PHASE_THREE.md \
       docs/SEMI_FINALIST_COMPARISON.md \
       docs/VOICE_GUARDRAILS_SOUTH_YORKSHIRE.md \
       docs/BOOK_1_CHAPTER_ARCHITECTURE.md \
       drafts/THE_BETTER_VERSION_CHAPTER_1.md \
       reviews/CHAPTER_1_REVIEW_PACKAGE.md \
       reviews/CHAPTER_1_VOICE_TEST_REVIEW.md \
       handoffs/SESSION_HANDOFF_2026-07-16.md
# MASTER-HANDOFF.md: see Step 6
git commit -m "Remove The Better Version creative material to dedicated repo"
git push origin main
```

### Step 6: Replace `handoff/MASTER-HANDOFF.md`
Replace the populated project handoff with a generic template/example that matches the HANDOFF_SYSTEM.md specification. Commit separately.

### Step 7: Update `novel-production-system/README.md`
Add a note in the README pointing to the new creative repository pattern, confirming that creative content has been moved to dedicated project repos.

### Step 8: Verify
- Confirm `Sirvenis/the-better-version` is private
- Confirm `Sirvenis/novel-production-system` no longer contains creative files at HEAD
- Spot-check GitHub web view of both repos

---

## 6. HISTORY-PRESERVATION APPROACH

### For `the-better-version` (new repo)

**Option A: Squash import (recommended)**
- Copy files as-is, single initial commit
- Loss: granular commit history from `novel-production-system`
- Gain: clean start, no infrastructure commits mixed in

**Option B: Filtered history export (advanced)**
- Use `git filter-repo` to extract only The Better Version commits from `novel-production-system`
- Loss: complex, may include mixed commits that touched both infrastructure and creative files
- Gain: preserves developmental commit history

**Recommendation:** Option A. The creative files were developed rapidly across a single session. The commit history is not semantically meaningful for a creative repository. The important history is the decision trail (candidates, comparisons, setting choice), which is captured in the document contents, not the commit messages.

### For `novel-production-system` (existing repo)

**Do NOT rewrite history.** The repo is public and may have forks/clones. Removing files from HEAD is sufficient. The commit history showing how the pipeline developed is valuable institutional memory.

---

## 7. BLOCKERS AND RISKS

| # | Blocker/Risk | Severity | Mitigation |
|---|-------------|----------|------------|
| 1 | **Git history contains unpublished manuscript** | Medium | Accept for now; remove from HEAD. History cleanup is a separate optional task. |
| 2 | **MASTER-HANDOFF.md is referenced by infrastructure docs** | Low | Replace with generic template after moving populated version. |
| 3 | **Other projects may have cloned `novel-production-system`** | Low | HEAD cleanup is non-breaking. History rewrite would be breaking — avoid. |
| 4 | **Case studies in `novel-production-system` reference The Better Version indirectly?** | Very Low | Case studies are anonymised horror-series production. No Better Version references detected. |
| 5 | **References folder contains Better Version-specific patterns?** | Low | All 21 reference files are generic execution patterns. None mention Di Calloway, South Yorkshire, or replacement horror. |
| 6 | **User approval required** | **BLOCKING** | This report requires explicit approval before any implementation. |

---

## 8. SUMMARY TABLE

| Category | Files | Lines | Disposition |
|----------|-------|-------|-------------|
| Project-specific creative | 10 | ~3,521 | **MOVE** to `the-better-version` |
| Institutional philosophy | 1 | ~141 | **COPY** to new repo, retain original |
| Reusable infrastructure | ~40 | ~7,400+ | **REMAIN** in `novel-production-system` |
| Uncertain | 1 | ~149 | **RESOLVE** as part of Step 6 |

---

## 9. APPROVAL CHECKLIST

Before implementation, confirm:

- [ ] Approve the proposed new repository name: `Sirvenis/the-better-version`
- [ ] Approve the proposed directory structure
- [ ] Approve the privacy risk mitigation (remove from HEAD, accept history)
- [ ] Approve the history-preservation approach (squash import, single initial commit)
- [ ] Approve the migration sequence (8 steps)
- [ ] Confirm no other active projects depend on The Better Version files in `novel-production-system`

---

**Report prepared by:** Hermes  
**Status:** Awaiting approval before implementation  
**Next step:** Upon approval, execute Steps 1-8 as a single controlled migration session.
