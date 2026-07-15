# `wc -w` Word-Count Caching Pitfall

## Symptom

After `write_file` successfully writes an expanded chapter draft (new byte count confirmed in tool output), `wc -w <file>` continues to report the OLD word count from before the rewrite.

## Reproduction

```bash
# File chapter-07.md is 2,829 words (lean)
write_file(path="chapter-07.md", content="<expanded 4,756-word version>")
# Tool reports success, new byte count ~16,855

wc -w chapter-07.md
# Output: 2829  (stale — the old count)
```

`read_file` confirms the new content is on disk. The file IS correct. `wc` is wrong.

## Root Cause

The `wc` command on this system appears to cache file metadata and not invalidate the cache when the file is overwritten by `write_file`. This may be a filesystem-level caching behavior in the WSL environment.

## Workaround / Verification Method

**Do not trust `wc -w` for word-count verification immediately after `write_file`.**

Use one of these alternatives:

1. **`read_file` tail check** — Read the last few lines of the file (where the word-count annotation lives). This bypasses the cache and reads actual disk content.
2. **`cat | wc`** — `cat chapter-07.md | wc -w` sometimes bypasses the file-metadata cache, though this is not guaranteed.
3. **Re-read after delay** — In practice, the cache invalidates within a few minutes, but this is too slow for iterative drafting.
4. **Trust `write_file` output + `read_file` spot-check** — The most reliable method: confirm `write_file` reported success with the expected byte count, then spot-check the file content with `read_file` (offset near end) to verify the expected closing text is present.

## Why This Matters

In Pass 2 expansion workflows, the agent iteratively writes expanded chapters and needs to confirm they hit target word count before committing. A false "still lean" reading from `wc` can cause:
- Unnecessary second rewrites
- Over-expansion beyond target
- Wrong tracker updates
- Commits with incorrect metadata

## Session Reference

Discovered during Book 2 Pass 2 expansion (Chapters 7, 8, 16, 17). The agent wrote expanded versions, `write_file` reported correct byte counts, but `wc -w` returned old counts for all four files. `read_file` tail checks confirmed the files were correct on disk.
