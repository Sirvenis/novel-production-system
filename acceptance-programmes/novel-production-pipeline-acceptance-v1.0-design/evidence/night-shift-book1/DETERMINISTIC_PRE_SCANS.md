# Night Shift Book 1 — Deterministic Pre-Scan Results

**Date:** 2026-08-11
**Method:** Script-based deterministic checks (no LLM involvement)
**Manuscript:** /home/andrew/projects/active/nurse-fiction-series/night-shift/book1/MANUSCRIPT_ASSEMBLED.md

## 1. File/Manuscript Integrity

- File exists at canonical path: YES
- File readable: YES
- File size: 256,999 bytes
- SHA-256: 91642840cbc8cb9656d26b46bb3dcaf1a8a05905ae0a48b75de4c0f59666bef7
- Encoding: UTF-8 (contains non-ASCII: em dashes, smart quotes)
- No binary corruption detected
- No placeholder text found ([INSERT, [TODO, [PLACEHOLDER, TBD, XXX)

## 2. Chapter Ordering

- Chapter count: 16 (Chapters 1-16)
- All chapters sequentially numbered: YES
- No missing chapter numbers: YES
- No duplicate chapter numbers: YES
- All 16 chapter headings present and correctly formatted as "# Chapter N: Title"

## 3. Chapter Word-Count Distribution

| Chapter | Title | Words | % of Total |
|---------|-------|-------|------------|
| 1 | The First Night | 4,922 | 10.4% |
| 2 | The Rhythm | 4,442 | 9.4% |
| 3 | Aunty Dot | 2,865 | 6.1% |
| 4 | Room 14 | 3,849 | 8.1% |
| 5 | The Full Moon | 2,472 | 5.2% |
| 6 | The History | 3,567 | 7.5% |
| 7 | The Surge | 2,532 | 5.4% |
| 8 | The Break | 2,205 | 4.7% |
| 9 | Liam | 2,755 | 5.8% |
| 10 | Room 14 Again | 2,117 | 4.5% |
| 11 | The Choice | 2,789 | 5.9% |
| 12 | The Basement | 2,964 | 6.3% |
| 13 | The Long Night | 5,254 | 11.1% |
| 14 | After | 1,403 | 3.0% |
| 15 | The Next Night | 1,638 | 3.5% |
| 16 | The Drive Home | 1,537 | 3.2% |

Total: 47,311 words

Distribution finding: ABNORMAL — Chapters 14, 15, and 16 are notably short (1,403, 1,638, 1,537 words respectively). The combined total of Ch 14-16 (4,578 words, 9.7%) is less than Chapter 1 alone (4,922 words). The climax chapter (13) is the longest at 5,254 words, which is structurally appropriate. However, the severe brevity of the final three chapters creates an asymmetric falling action/epilogue structure that may indicate truncation, rushed generation, or deliberate compression. This requires model-based diagnosis to determine if intentional.

## 4. Duplicate/Repeated Headings

- Total markdown headings: 16 (one per chapter, all unique)
- No duplicate chapter headings
- No sub-headings found within chapters (manuscript uses scene breaks "---" rather than sub-headings)

## 5. Duplicate Paragraphs and Lines

### Cross-chapter duplications (DETERMINISTIC HIGH SEVERITY)

17 duplicate substantive lines (>30 chars) were detected. These cluster into two patterns:

**Pattern A: Chapters 13 and 16 near-identical endings**
Chapters 13 and 16 contain near-identical sequences of text covering:
- The day shift arrival ("At 06:00, the day shift arrived. Patricia, with her ponytail and her tired eyes...")
- The handover description
- Mara gathering things, stethoscope in bag
- "Same time tonight" / "Same time"
- The fire door, stairwell, main entrance exit
- The drive home (22 minutes, traffic lights, truck, sprinkler, jogger on Greenhill Road)
- Getting home, parking, sitting in car, silence of the street
- Setting alarm for 3:00 PM
- "She lay down. She closed her eyes."

This represents approximately 300-400 words of near-verbatim duplicated text between the two chapters.

**Pattern B: Chapters 12/13 and 15 duplicated roof/breathing scene**
"She stood on the roof and she breathed. She breathed the way you breathe when you've been holding something..." appears in both Ch 12/13 context and Ch 15 context.

**Pattern C: Within-Chapter 1 duplicate**
"Every year. It's in the maintenance log. They'll get to it." appears twice within Chapter 1 (lines 160 and 214). This appears to be the same dialogue repeated in two different contexts — possibly intentional (Gwen says it twice across two shifts) or a generation artifact.

### Assessment

The cross-chapter duplications between Ch 13 and Ch 16 are the most concerning. They could be:
1. Intentional structural rhyme (the novel ends the way the crisis night ends — cyclical, "she would be there")
2. GLM-5.2 generation artifact (the model repeated itself when generating similar ending scenes)
3. A combination — some structural echo intended, but the verbatim repetition is an artifact

This finding is flagged for the developmental diagnosis to assess. The deterministic scan can only establish that duplication exists; it cannot determine intent.

## 6. Scene Breaks

- Scene breaks ("---"): 47 total
- Distribution appears normal across chapters
- No malformed or missing scene breaks detected

## 7. Metadata Consistency

- Manuscript word count (47,311) vs test plan stated count (45,555): DISCREPANCY of +1,756 words
- Git log shows post-draft developmental revision commits for Ch 1, 9, and 14-16, which likely accounts for the difference
- Chapter count matches test plan (16)
- No front matter or back matter detected (manuscript is pure chapter content)

## 8. Formatting Defects

- Smart quotes used consistently throughout (not mixed with straight quotes)
- Em dashes used throughout (not hyphens)
- No markdown rendering issues detected
- No broken links, images, or formatting artifacts
- No encoding defects beyond expected UTF-8 content

## 9. Known Generated Artifacts

- No [IMAGE] or [FIGURE] placeholders
- No "As an AI" or model-identity leakage
- No "Certainly!" or "I'd be happy to" preamble
- No obvious generation-metadata in the prose

## Summary of Deterministic Findings

| # | Finding | Severity | Type | Chapter(s) |
|---|---------|----------|------|------------|
| D1 | Cross-chapter verbatim text duplication Ch 13 ↔ Ch 16 | HIGH | Duplication | 13, 16 |
| D2 | Cross-chapter near-duplicate roof/breathing scene | MEDIUM | Duplication | 12/13, 15 |
| D3 | Within-Ch 1 duplicate dialogue line | LOW | Duplication | 1 |
| D4 | Abnormally short final three chapters (Ch 14-16) | MEDIUM | Structure | 14, 15, 16 |
| D5 | Word count discrepancy with test plan (+1,756) | INFO | Metadata | — |

No truncation detected. No missing chapters. No placeholder text. No encoding defects. No formatting corruption.