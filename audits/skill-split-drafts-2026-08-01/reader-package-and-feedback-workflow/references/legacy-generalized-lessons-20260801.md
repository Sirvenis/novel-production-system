# Legacy Generalized Lessons — reader-package-and-feedback-workflow

Date: 2026-08-01

This compact linked reference distills cross-series/general items from the old global `longform-fiction-series-drafting` reference archive into task-class guidance for the staged draft skill split.

No live Hermes skills were changed. Series-specific canon remains in canonical series repos; the legacy files remain untouched until a later approved slimming pass.

Source manifest: `/home/andrew/novel-production-system/audits/skill-split-drafts-2026-08-01/REFERENCE_CLASSIFICATION_MANIFEST.csv`
Legacy source directory: `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/references`
Processed references in this task domain: 14

## Generalization Rules Used

- Convert reusable procedure into task-class guidance.
- Preserve project names only as provenance; do not treat old examples as current canon.
- Do not include runtime/provider/profile/deployment-sensitive items here; those remain quarantined for manual review.
- Before installing any staged skill live, re-check current repo authority and validate the draft skill package.

## Source Index

| Source file | Title | Hash | Words |
|---|---|---:|---:|
| `auto-generated-reader-dashboard.md` | Auto-Generated Reader Dashboard for Fiction Projects | `f7f0163ff5d7fd5a` | 693 |
| `book3-cron-stale-prompt-multi-chapter-dashboard-sync.md` | Book 3 Cron: Stale Prompt, Tracker Ahead, Multi-Chapter Dashboard Sync | `dd9014f78d94ea15` | 353 |
| `current-dashboard-pattern.md` | Current Dashboard Pattern | `0267c2b2f5c8df10` | 386 |
| `editorial-feedback-lifecycle-status-update.md` | Editorial Feedback as Lifecycle Status Update | `9bbdc322b80947a6` | 409 |
| `family-reader-chapter-title-proposal-pass.md` | Family reader chapter-title proposal pass | `1c9ddbea860934b1` | 280 |
| `fiction-project-progress-dashboard.md` | Fiction Project Progress Dashboard | `98b13d1fd6162a22` | 314 |
| `generating-chapter-titles-from-source.md` | Generating Short Chapter Titles When Source Has None | `655827afe956334d` | 978 |
| `manuscript-to-web-reader-pipeline.md` | Manuscript-to-Web Reader Pipeline | `0b604b9db66e3a4a` | 457 |
| `reader-feedback-form-templates.md` | Reader Feedback Form Templates | `0d6538be4db6b902` | 1575 |
| `reader-site-feedback-form-generation.md` | Reader Site Feedback Form Generation | `21b57601dd4c48c7` | 663 |
| `reader-site-title-regression-guards.md` | Reader Site Title Regression Guards | `d80a6f39b3d1e72e` | 282 |
| `simplified-reader-site-feedback-forms.md` | Simplified Reader-Site Feedback Forms | `bc4816fa653679d4` | 274 |
| `single-page-multi-book-reader-site.md` | Single-Page Multi-Book Reader Site — Hybrid Architecture | `a74dcbd956fdddd2` | 799 |
| `structural-expansion-pass-from-editor-feedback.md` | Structural Expansion Pass From External Editor Feedback | `64a157874fbe2c66` | 445 |

## Distilled Operational Lessons

### Auto-Generated Reader Dashboard for Fiction Projects

Provenance: `auto-generated-reader-dashboard.md` (`f7f0163ff5d7fd5a`), 693 words.

- Topic: Auto-Generated Reader Dashboard for Fiction Projects
- Topic: What It Is
- Topic: Why It Exists
- Topic: Live Example
- **Repo:** `Sirvenis/kimi-horror-lab`
- Topic: How It Works

### Book 3 Cron: Stale Prompt, Tracker Ahead, Multi-Chapter Dashboard Sync

Provenance: `book3-cron-stale-prompt-multi-chapter-dashboard-sync.md` (`dd9014f78d94ea15`), 353 words.

- Topic: Book 3 Cron: Stale Prompt, Tracker Ahead, Multi-Chapter Dashboard Sync
- Topic: Durable lesson
- Topic: Workflow that worked
- Verify `~/.hermes/logs/agent.log` shows the required creative runtime (`model=gpt-5.5 provider=openai-codex`) before drafting prose.
- Read canonical tracker and identify the first `next` row.
- Draft one or more sequential chapters from the tracker truth, not from stale prompt text.

### Current Dashboard Pattern

Provenance: `current-dashboard-pattern.md` (`0267c2b2f5c8df10`), 386 words.

- Topic: Current Dashboard Pattern
- User wants to avoid `/home/andrew/` clutter
- Topic: One-time setup (requires sudo)
- Topic: Folder structure template
- Topic: Creation checklist
- Identify latest verified source for each book (check for fix/acceptance passes)

### Editorial Feedback as Lifecycle Status Update

Provenance: `editorial-feedback-lifecycle-status-update.md` (`9bbdc322b80947a6`), 409 words.

- Topic: Editorial Feedback as Lifecycle Status Update
- Topic: Core rule
- Read the relayed feedback and classify it:
- If it is process/stage guidance, create a concise repo-local report under `bookN/reports/` or the nearest project reports directory.
- Update status/handoff files so future sessions inherit the improved framing.
- Preserve the current manuscript pause/closure state unless the feedback explicitly requires prose action.

### Family reader chapter-title proposal pass

Provenance: `family-reader-chapter-title-proposal-pass.md` (`1c9ddbea860934b1`), 280 words.

- Topic: Family reader chapter-title proposal pass
- A static family reader site is otherwise working, but one book has generic written-number chapter labels.
- The source manuscript has chapter headings without real titles.
- A source-of-truth audit says not to invent titles during a hotfix.
- Topic: Safe workflow
- Use the project-approved manuscript model for the creative title proposal if the series policy requires one.

### Fiction Project Progress Dashboard

Provenance: `fiction-project-progress-dashboard.md` (`98b13d1fd6162a22`), 314 words.

- Topic: Fiction Project Progress Dashboard
- Topic: Generator Script
- Topic: Build HTML with stats, progress bar, chapter table
- Topic: See full script in project repo: scripts/generate-dashboard.py
- Topic: Deployment Options
- Topic: Open: file://<local-path>

### Generating Short Chapter Titles When Source Has None

Provenance: `generating-chapter-titles-from-source.md` (`655827afe956334d`), 978 words.

- Topic: Generating Short Chapter Titles When Source Has None
- Missing/blank (just "Chapter 14")
- Source had `# Chapter One` through `# Chapter Twenty` with no titles
- Chapter 14 parsed as "Four" + "teen" → "4. teen" in TOC
- Chapters 14, 16-19 had duplicate IDs (reused `book2-chapter-4`, etc.) because the generator matched `Chapter Four` for both Chapter 4 and Chapter 14
- Topic: Solution: Rebuild from source with proper title generation

### Manuscript-to-Web Reader Pipeline

Provenance: `manuscript-to-web-reader-pipeline.md` (`0b604b9db66e3a4a`), 457 words.

- Topic: Manuscript-to-Web Reader Pipeline
- Topic: When to use
- **Convert to HTML** — Create a clean reading page: serif font, 720px max width, chapter nav with prev/next/TOC, warm background, responsive. Parse markdown headings, horizontal rules (---), and italics.
- **Deploy via VPS** — scp HTML to server, add Caddy subdomain config (use actual tabs not \t literals), reload Caddy, add Cloudflare DNS A record. Wait 30s for SSL cert.
- Topic: Separate Reading Room subdomain for cozy mystery series (Brambleford)
- Root: `/srv/brambleford-reader/` on the WPS VPS

### Reader Feedback Form Templates

Provenance: `reader-feedback-form-templates.md` (`0d6538be4db6b902`), 1575 words.

- Topic: Reader Feedback Form Templates
- Topic: Three-tier feedback system
- Topic: Tier 1 — Spoiler-Free Quick Form
- Topic: Tier 2 — Spoiler-Full Deep Form
- **Mystery-specific**: Were clues fairly planted? Did reader solve before protagonist?
- Topic: Tier 3 — Beta-Reader Instructions

### Reader Site Feedback Form Generation

Provenance: `reader-site-feedback-form-generation.md` (`21b57601dd4c48c7`), 663 words.

- Topic: Reader Site Feedback Form Generation
- Topic: When this applies
- Andrew wants to deploy a manuscript for a specific person (e.g., "my mother") to read in a browser.
- The reader should be able to submit feedback after finishing — ideally via email, not a backend.
- The feedback form should be rich and structured, not just a single open text box.
- For Book 1: use the publication master or release candidate.

### Reader Site Title Regression Guards

Provenance: `reader-site-title-regression-guards.md` (`d80a6f39b3d1e72e`), 282 words.

- Topic: Reader Site Title Regression Guards
- Topic: Durable lessons
- Use JSON chapter-title maps as the authoritative title source when manuscripts have bare headings like `# Chapter Fourteen`. Do not infer titles from the first sentence.
- In regexes for word-number chapters, list longer words before shorter words: `Fourteen|Fifteen|...|Four|Five...`. Otherwise `Four` can partially match `Fourteen`, producing duplicate chapter IDs.
- Do not use `\s*` around optional title capture in a multiline chapter-heading regex. `\s` includes newlines, so the regex can swallow the next line (often `## Scene 1`) as the chapter title. Prefer `[ \t]*`:
- If captured title starts with `##`, discard it and fall back to the JSON title map or `Chapter N`.

### Simplified Reader-Site Feedback Forms

Provenance: `simplified-reader-site-feedback-forms.md` (`bc4816fa653679d4`), 274 words.

- Topic: Simplified Reader-Site Feedback Forms
- Topic: When to use
- Topic: The two-tier system
- Topic: Casual form pattern
- Topic: Technical delivery
- **Copy feedback** button (navigator.clipboard.writeText)

### Single-Page Multi-Book Reader Site — Hybrid Architecture

Provenance: `single-page-multi-book-reader-site.md` (`a74dcbd956fdddd2`), 799 words.

- Topic: Single-Page Multi-Book Reader Site — Hybrid Architecture
- Topic: When this applies
- All feedback forms for all books in one place
- Topic: Architecture: Landing Page + Separate Novel Pages
- Topic: `index.html` (the ONE address)
- **Book cards** — 3 cards, one per book, each with "Read Book N" button linking to `book-N.html`

### Structural Expansion Pass From External Editor Feedback

Provenance: `structural-expansion-pass-from-editor-feedback.md` (`64a157874fbe2c66`), 445 words.

- Topic: Structural Expansion Pass From External Editor Feedback
- Topic: Session-derived pattern
- Save it as a concise editorial brief inside the revision workspace.
- Preserve the original draft/pass; do not overwrite it.
- Convert feedback into structural targets.
- For late-book compression, target every chapter in the compressed range, not only the thinnest chapter.
