# Git Workflow

## Commit Discipline

Every commit message should tell the next person (including future you) exactly what changed and why.

### Message Format

```
[Book N]: [Stage] — [What changed]

[Optional: Details, word count delta, files touched]
```

**Examples:**
```
Book 3: Ch 14 The Pressure expanded — boat ride, thermocline descent, charge placement detail. 2,261w → 3,808w (+1,547w). Tier 1 complete.
```
```
Book 3: Line Edit (Stage 6) — trim 'That's worse' echo, 'Not X Not X But Y' repetition, throat-clearing 'I think about this', unnecessary dialogue tags. 15 chapters touched. Net +6 words.
```
```
Book 3: Copy Edit (Stage 7) — 3 mechanical fixes: 'center'→'centre' (Ch 7), 'the pattern'→'the Pattern' (Ch 2), 'the signal'→'the Signal' (Ch 6). All terminology verified clean.
```

### Commit Timing

- **After every chapter draft:** Commit before proceeding to next chapter
- **After every expansion:** Commit each expanded chapter separately
- **After every fix batch:** Commit per fix group
- **After line edit phases:** Commit each phase separately
- **After copy edit:** Single commit for all mechanical fixes
- **After assembly:** Commit the compiled manuscript
- **After freeze:** Final commit with "FROZEN" in message + git tag

### Tagging

```bash
git tag book1-frozen
git tag book2-frozen
git tag book3-frozen
git push origin --tags
```

Tags mark the exact commit where a book was frozen. This makes it easy to recover the frozen state even if later commits modify files.

---

## Branch Strategy

### Simple Strategy (Recommended for Solo/Small Projects)

```
main
├── commit: Book 1 architecture
├── commit: Book 1 Ch 1 drafted
├── commit: Book 1 Ch 2 drafted
├── ...
├── commit: Book 1 frozen [tag: book1-frozen]
├── commit: Series bible update
├── commit: Book 2 architecture
├── ...
```

All work on `main`. No feature branches. The commit history IS the revision history.

### Multi-Project Strategy (If Multiple Series in One Repo)

```
main
├── series-a/
│   ├── book-1/
│   ├── book-2/
│   └── book-3/
└── series-b/
    ├── book-1/
    └── book-2/
```

Use directories, not branches. Each series gets its own directory. This keeps the repo simple.

### Feature Branch Strategy (If Multiple Writers/Editors)

```
main
├── draft/book3/ch14-expansion  [branch]
│   └── commits: expansion work
│   └── merge to main
├── edit/book3/line-edit        [branch]
│   └── commits: line edit work
│   └── merge to main
```

Use branches for major revision passes that might be abandoned. Merge when complete.

---

## What NOT to Commit

- `.env` files or any file containing API keys, tokens, or secrets
- Cache files (`*.cache`, `__pycache__/`, `.hermes/cache/`)
- Log files (`*.log`, `logs/`)
- OS-specific files (`.DS_Store`, `Thumbs.db`)
- IDE files (`.vscode/`, `.idea/`)
- Build artifacts (compiled PDFs, generated images — unless they are deliverables)
- Temporary files (`*.tmp`, `*.swp`, `*~`)

**See `.gitignore` in this repository for the complete exclusion list.**

---

## Working Tree Hygiene

Before every commit:

```bash
git status              # See what's changed
git diff --cached       # Review staged changes
git diff                # Review unstaged changes
```

Before presenting a report to the user:

```bash
git status              # Confirm working tree is clean (or staged)
```

The user expects a clean working tree after major work. "Working tree: Clean" is a sign of disciplined production.

---

## Recovery Patterns

### Recovering a Deleted File

```bash
git log --all --full-history -- drafts/chapter-07.md
git show [commit]:drafts/chapter-07.md > drafts/chapter-07.md.recovered
```

### Recovering a Frozen State

```bash
git checkout book1-frozen -- .
git reset --soft HEAD
```

This restores all files to their frozen state while keeping the commit history intact.

### Finding When Something Changed

```bash
git log -S "specific phrase" -- drafts/
git log -p -- drafts/chapter-03.md | less
```

### Comparing Two Versions

```bash
git diff book2-frozen..HEAD -- SERIES_BIBLE.md
```

---

## Common Pitfalls

- **Mega-commits:** Committing 10 chapters at once. Lose granularity, lose recovery precision.
- **Vague messages:** "Update files" tells nobody anything. Be specific.
- **Committing secrets:** Double-check `git status` before committing. Use `.gitignore` aggressively.
- **Dirty working tree:** Presenting a report while there are uncommitted changes. The user sees a dirty tree and assumes work is incomplete.
- **No tags:** Freezing without tagging makes it impossible to recover the exact frozen state.
