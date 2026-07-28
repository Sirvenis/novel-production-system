# Video Research Report: Build An AI Second Brain Knowledge Base (Step-By-Step)

**Source:** Matt Wolfe / @mreflow — https://www.youtube.com/watch?v=yke4fLQUsh4
**Scanned:** 2026-07-28
**Runtime:** 38m58s
**Transcript length:** ~7,400 words
**Relevance to novel production:** MEDIUM-HIGH — Knowledge management infrastructure, content ingestion, cross-referencing

---

## Executive Summary

Matt Wolfe built a personal "second brain" knowledge management system with three pillars: a wiki/knowledge base, a CRM, and a journal — all queryable via natural-language chat. The core insight is that most second-brain systems are "information graveyards" because they lack active retrieval. His system solves this by embedding an AI layer that surfaces relevant knowledge automatically during chat and journaling.

For novel production, the most relevant elements are:
1. **Structured content ingestion** (transcripts, articles, podcasts → queryable corpus)
2. **Cross-referenced journaling** (daily notes linked to stored knowledge)
3. **Unified chat interface** (one place to query everything)

---

## Tools Deep-Dive

### 1. Notion (Structured Database Layer)

**What he uses it for:**
- CRM: people, conversations, contact details, meeting notes
- Structured knowledge: tables of tools, resources, saved content with metadata
- Linking: relations between people, topics, projects

**How it connects to the chat layer:** Notion data is exposed to Capable (the AI overlay), so queries like "What did I discuss with [person] last month?" return structured CRM results.

**Our equivalent:** We use GitHub repos + markdown + Codebase Memory MCP for structured project data. Our "CRM" is scattered across project handoffs, decision logs, and the Arden Knowledge Base. We don't have a unified people/conversation tracker.

### 2. Obsidian (Linked Notes / Wiki Layer)

**What he uses it for:**
- Markdown notes with bidirectional linking (`[[note name]]`)
- Graph view of connections between ideas
- Daily journal entries as separate files
- Long-form writing and thought capture

**How it connects:** All Obsidian notes are indexed by Capable. Journal entries can reference wiki pages, and wiki pages link to each other.

**Our equivalent:** Our markdown infrastructure (PROJECT_STATUS.yml, handoffs, trackers, decision logs) functions similarly but is project-scattered. Obsidian's graph view is more advanced than our flat-file approach.

### 3. Capable (AI Overlay / Retrieval Layer)

**What it does:**
- Sits on top of Notion + Obsidian
- Provides a chat interface to query ALL stored knowledge
- Automatically pulls relevant context when journaling
- Can answer questions using ingested content ("What did I save about [topic]?")
- Maintains conversation context across sessions

**Key workflow:** Journaling → AI reads journal → AI queries wiki for related content → AI surfaces relevant past notes → User gets insights they wouldn't have found manually.

**Our equivalent:** Hermes profiles + Codebase Memory MCP. Capable is a consumer product; our system is more powerful for code/manuscript context but lacks the unified "chat with your entire knowledge base" simplicity.

### 4. Make / Zapier (Automation / Ingestion Layer)

**What he uses it for:**
- Auto-save YouTube transcripts → Notion/Obsidian
- Auto-save tweets, articles, podcast transcripts
- RSS feed ingestion
- Content tagging and categorization

**Our equivalent:** Our yt-dlp + manual transcript processing. We don't have automated ingestion pipelines for research content.

---

## Workflows Extracted

### Workflow 1: The Ingestion Pipeline
```
Content discovery (YouTube, web, podcast)
    → Automation extracts transcript/summary
    → Stored in Notion (structured) or Obsidian (notes)
    → Tagged and linked
    → Becomes queryable by Capable
```

**Novel production application:** We could build a "research ingestion pipeline" for each series — saving setting research, historical references, folklore, technical details into a unified, queryable corpus. Currently, research is scattered in project folders, Arden KB, and ad-hoc notes.

### Workflow 2: The Journal Cross-Reference
```
User writes journal entry
    → Capable reads entry
    → Capable queries wiki for related stored knowledge
    → Capable surfaces connections: "You wrote about anxiety — here are 3 past entries + 2 saved articles on the topic"
```

**Novel production application:** A "writer's journal" that cross-references character bibles, series lore, and previous books. "I'm writing Chapter 7 about Enki's doubt — show me all previous mentions of Enki's confidence and all series bible entries about Anunnaki emotional rules."

### Workflow 3: The Unified Query
```
User asks question in chat
    → Capable searches Notion (structured data) + Obsidian (notes/wiki)
    → Returns synthesized answer with source links
    → User can drill down to original content
```

**Novel production application:** One query interface across ALL series bibles, all character sheets, all previous books, all research notes. Currently, finding a specific detail requires grep across multiple repos.

---

## Cross-Reference with Our Stack

| Matt Wolfe Component | Our Equivalent | Gap / Opportunity |
|---|---|---|
| Notion CRM | Project handoffs, decision logs, Arden KB | No unified people/conversation tracker; no easy "who did we discuss X with?" query |
| Obsidian wiki | Markdown bibles, series docs, character sheets | No graph view; no bidirectional linking across repos; files are siloed per series |
| Capable AI chat | Hermes profiles + Codebase Memory MCP | Our system is more powerful for project context but harder to use for simple "chat with your notes" queries |
| Make/Zapier ingestion | Manual yt-dlp + copy-paste | No automated research pipeline; each video/article is manually processed |
| Journal cross-reference | No direct equivalent | **Biggest gap**: We don't have a journaling layer that AI cross-references with stored knowledge |

---

## Recommendations

### Immediate (No New Infrastructure)

1. **Use Obsidian for series bible graph view**
   - Open the Anunnaki or Brambleford series bible folder in Obsidian
   - Use `[[link]]` syntax to connect character sheets, setting notes, and chapter references
   - The graph view immediately reveals orphaned notes and connection gaps

2. **Add a RESEARCH.md file per series**
   - Currently, research notes are scattered. Create a canonical `research/RESEARCH_CORPUS.md` in each series repo
   - Structure: setting research, historical references, technical details, folklore/mythology, character inspiration
   - Link from the series bible so it becomes discoverable

3. **Journal-as-workflow enhancement**
   - Before each drafting session, the writer profile could read the last 5 journal/handoff entries
   - Then query the series bible for relevant context
   - Present a "pre-flight briefing" to the writer: "You're writing Chapter 7. Here are the threads active at this point, here's what happened in Chapter 6, here are the series bible rules you might need."

### Medium-Term (Lightweight Tooling)

4. **Automated transcript ingestion for research videos**
   - Create a `research/videos/` directory in each series repo
   - Use yt-dlp + a shell script to auto-download transcripts of relevant videos
   - Store as markdown with metadata: source URL, date scanned, key topics, relevance rating
   - This becomes a queryable research corpus

5. **Codebase Memory MCP enhancement**
   - Currently indexed per-repo. Consider creating a "master research index" that spans all series
   - This would let us ask: "Where have we written about unreliable narrators before?" and get results across Brambleford, horror, and Anunnaki

6. **Profile "pre-flight briefing" script**
   - A small Python script that runs before a writer/editor session:
     - Reads the current tracker
     - Reads adjacent chapters for continuity
     - Reads the series bible relevant sections
     - Reads recent handoffs
     - Outputs a 500-word briefing to stdin or a temp file
   - This automates what Matt Wolfe's Capable does manually

### Long-Term (If We Want Unified Knowledge)

7. **Consider a unified knowledge base across ALL series**
   - Currently: Arden KB (institutional), Codebase Memory MCP (code/project graphs), series repos (creative)
   - Opportunity: One markdown-based wiki with graph linking that covers craft techniques, series bibles, character archetypes, research, and editorial lessons
   - Could be a new repo: `Sirvenis/arden-wiki` or integrated into the Arden KB

---

## Specific Tools We Could Adopt

| Tool | Cost | Effort | Novel Production Value |
|------|------|--------|------------------------|
| Obsidian (free) | Free | Low | Graph view of series bibles; bidirectional linking |
| Capable (waitlist) | Unknown | Medium | Unified chat interface — but may overlap with Hermes profiles |
| Make/Zapier | $10-20/mo | Medium | Automated ingestion — low priority for now |
| Custom yt-dlp pipeline | Free | Low | Already feasible; just needs a script template |
| Codebase Memory MCP index expansion | Free | Low | Already installed; just needs config for research repos |

---

## Files Generated from This Scan

- `/tmp/mreflow_secondbrain.txt` — Full cleaned transcript (~39K chars)
- This report — structured analysis and recommendations

---

## Next Actions

1. **Scout decision needed:** Should we create an Obsidian graph for one series as a test? (Recommend: Brambleford, smallest canon)
2. **Scout decision needed:** Should we add a `research/` directory template to the novel-production-system templates?
3. **Scout decision needed:** Should we build the "pre-flight briefing" script as a template or a real tool?

---

*Report prepared by Scout (kimi-k2.6:cloud) for the novel-production-system research archive.*
