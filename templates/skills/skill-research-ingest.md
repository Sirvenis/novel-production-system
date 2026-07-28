# Skill: Research Ingest

**Purpose:** Take web research (articles, video transcripts, papers, notes) and transform it into structured, searchable corpus files that integrate with the project's knowledge base.

**When to use:** When acquiring new external research relevant to a project — craft techniques, market analysis, tool evaluations, genre surveys, competitor analysis.

**When NOT to use:** For creative content (manuscripts, character designs, architecture) — that goes in the creative repo. For project infrastructure — that goes in novel-production-system.

**Who runs this:** Researcher profile or showrunner.

---

## What It Does

The Research Ingest skill takes raw source material and produces a structured markdown report that:
1. Captures source metadata (URL, author, date, type)
2. Extracts key insights relevant to the project
3. Flags actionable items
4. Files the report in the correct location
5. Commits to git with a descriptive message

---

## Execution Steps

### Step 1: Capture Source Metadata

Before processing, record:

| Field | Source |
|-------|--------|
| Title | From the source (video title, article headline, paper title) |
| Author/Creator | From the source |
| Date | Publication date |
| URL | Permanent link |
| Type | video / article / paper / podcast / other |
| Source channel/platform | YouTube, blog, arXiv, etc. |
| Runtime/Length | For videos/podcasts |
| Date ingested | Today's date |

### Step 2: Extract Transcript or Content

**For YouTube videos:**
```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download -o "%(title)s" "URL"
# Clean the VTT/SRT to plain text
```

**For web articles:**
- Use the browser tool or `curl` to fetch the page
- Extract the article body (strip navigation, ads, comments)
- Preserve headings and structure

**For papers:**
- Download PDF
- Extract text with `pymupdf` or `marker-pdf`

### Step 3: Structure the Report

Write the report as a markdown file with this structure:

```markdown
# [Title]

**Source:** [URL]
**Author/Creator:** [Name]
**Published:** [Date]
**Type:** [video/article/paper]
**Ingested:** [Today's date]
**Runtime:** [if applicable]

---

## Summary

[2-3 sentence summary of what this source is about and why it's relevant to the project]

---

## Key Insights

### Insight 1: [Title]
[What the source says, why it matters to the project]

### Insight 2: [Title]
[What the source says, why it matters to the project]

[Continue for each distinct insight...]

---

## Actionable Items

| # | Item | Relevance | Effort | Cost | Priority |
|---|------|-----------|--------|------|----------|
| 1 | [Specific action] | [How it helps] | [Low/Med/High] | [$0/$] | [1-5] |

---

## Notable Quotes

> "[Exact quote from source]"
> — [Attribution], [context]

---

## Cross-References

- Related to: [Other reports/files in the repo]
- Relevant to project: [Which project/series this applies to]

---

*Ingested by [profile name] on [date].*
```

### Step 4: File the Report

Place the report in the correct location:

| Source type | Location | Filename pattern |
|------------|----------|------------------|
| Video scan | `research/video-scans/` | `YYYY-MM-DD-channel-title.md` |
| Article | `research/articles/` | `YYYY-MM-DD-source-title.md` |
| Paper | `research/papers/` | `YYYY-MM-DD-author-title.md` |
| Craft technique | `references/` | `topic-name.md` (if reusable across projects) |

For the `video-insights-library` repo specifically:
- Video reports go in `videos/`
- Implementation plans go in `plans/`
- Scripts go in `scripts/`

### Step 5: Commit

```bash
git add -A
git commit -m "research: ingest [source type] — [short title]"
```

Commit message format: `research: ingest [type] — [title]`

---

## Verification

- [ ] Source metadata is complete (all fields filled)
- [ ] Key insights are extracted (not a raw dump — synthesized)
- [ ] Actionable items are specific (not vague "consider this")
- [ ] File is in the correct location
- [ ] Filename follows the naming convention
- [ ] Git commit is descriptive
- [ ] Report is grep-searchable (key terms will match)

---

## Common Failure Modes

| Failure | Cause | Fix |
|---------|-------|-----|
| Raw dump instead of synthesis | Copied transcript without extracting insights | Rewrite as key insights, not a transcript summary |
| Vague actionables | "Consider looking into X" | Make it specific: "Build scripts/ingest-youtube.sh using yt-dlp" |
| Wrong filing location | Put video scan in references/ instead of research/video-scans/ | Follow the filing table above |
| Missing metadata | Forgot to record URL or date | Always capture metadata first, before processing content |
| Unsearchable report | Used images instead of text for key points | All insights must be text (grep-searchable) |

---

## Tools

- `browser_navigate` / `browser_snapshot` — fetch web articles
- `terminal` — run yt-dlp for video transcripts
- `read_file` — read extracted content
- `write_file` — write the structured report
- `search_files` — verify the report is discoverable via grep

---

*Skill created for the novel-production-system. Validated against the video-insights-library ingestion pattern and the research/video-scans/ directory structure.*