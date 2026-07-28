# Skill: Discovery Pass

**Purpose:** Pure inventory of manuscript state — what exists, what's missing, what's broken. No recommendations, no interpretation, no editorial assessment.

**When to use:** Before any editorial pass (Stage 4+). After drafting or expansion is complete (Stages 2-3). The Discovery Pass is the prerequisite for all downstream pipeline stages.

**When NOT to use:** Do not run this instead of an editorial pass. The Discovery Pass inventories; the editorial pass interprets. Do not run this before drafting exists.

**Who runs this:** Showrunner (master) or editor profile.

---

## What It Does

The Discovery Pass reads every chapter file and produces a structured inventory:

1. Chapter count and file list
2. Word count per chapter
3. POV per chapter
4. Timeline markers per chapter
5. Key entity/term mentions per chapter (grep counts)
6. Continuity lock status (recurring motifs present/absent)
7. Missing or duplicate chapters
8. Formatting anomalies (missing end markers, unexpected headings)

---

## Execution Steps

### Step 1: Gather Files

```
Read all chapter-NN.md files from the drafts/ or manuscript/ directory.
Read BOOK<N>_ARCHITECTURE.md for the expected chapter count and structure.
```

### Step 2: Per-Chapter Inventory

For each chapter file, extract:

| Field | Method |
|-------|--------|
| Chapter number | Parse from filename or `# Chapter N:` heading |
| Word count | Count words in the file (exclude markdown formatting) |
| POV | Read first 3 paragraphs; identify first-person/limited-third/omniscient |
| Timeline markers | grep for time references: "days", "weeks", "months", "hours", "ago", "yesterday", "tomorrow" |
| Entity mentions | grep -ic for key entities (series-specific: character names, threat name, frequency values, locations) |
| End marker | Check for `**[End Chapter` or equivalent |
| Structural headings | List all `#` and `##` headings in the file |

### Step 3: Cross-Chapter Inventory

Produce a table:

| Ch | Words | POV | End Marker | Key Entity A | Key Entity B | Timeline Refs | Notes |
|----|-------|-----|------------|-------------|-------------|---------------|-------|

Where Key Entity columns are grep counts for series-specific terms (e.g., character names, threat name, frequency values).

### Step 4: Gap Detection

Flag:
- Chapters with zero word count (empty or missing content)
- Chapters with no end marker
- Duplicate chapter numbers
- POV shifts mid-chapter (read opening + closing paragraphs; compare)
- Entity mentions that drop to zero in chapters where they should appear (based on architecture)
- Timeline markers that contradict earlier chapters

### Step 5: Output

Write the inventory as `revisions/BOOK<N>_DISCOVERY_PASS.md` containing:

1. File inventory table
2. Per-chapter metrics table
3. Gap/anomaly list (factual, no recommendations)
4. Architecture alignment check (expected vs actual chapter count)

**Critical:** The Discovery Pass output must NOT include recommendations. It is raw data. The editorial pass (Stage 4) uses this data as input.

---

## Verification

After producing the inventory:
- [ ] Every chapter file was read
- [ ] Word counts are from actual file content, not `wc` (which caches stale output)
- [ ] Architecture chapter count matches actual file count (or discrepancy is flagged)
- [ ] No editorial language in the output ("should", "needs to", "consider")
- [ ] All grep counts verified against actual file content

---

## Common Failure Modes

| Failure | Cause | Fix |
|---------|-------|-----|
| Word count wrong | Used `wc` instead of reading file | Use `read_file` and count in Python |
| Missing chapter not flagged | Only checked filenames, not content | Verify each file has non-zero content |
| Recommendations leaked in | Agent drifted to editorial | Strip all interpretive language from output |
| Entity gaps not detected | Only checked architecture, not grep | Run grep -ic for each key term across all chapters |

---

## Tools

- `read_file` — read chapter files
- `search_files` / `grep` — count entity mentions per chapter
- `execute_code` — batch process word counts and produce tables
- `write_file` — write the discovery pass report

---

*Skill created for the novel-production-system. Validated against the Discovery Pass Workflow pattern in STORYCRAFT_HANDBOOK.md.*