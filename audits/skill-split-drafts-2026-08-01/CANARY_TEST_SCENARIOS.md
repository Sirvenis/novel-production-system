# Fiction-Profile Canary Test Scenarios

**Date**: 2026-08-01  
**Profile**: `fiction`  
**Model**: `gpt-5.5` via `openai-codex` (from fiction profile config)  
**Workdir**: `/home/andrew/projects/active` (from fiction profile config)

---

## Test Scenarios (6+ Required)

### 1. SAME EIGHT ROUTING SCENARIOS FROM ISOLATED CANARY

These are the exact scenarios from the test-profile canary that passed 8/8:

| # | Prompt | Expected Route |
|---|--------|----------------|
| 1 | "Resume the Anunnaki Chronicles project after a /new restart. Verify the repo, status, handoff, and git state. Do not draft or edit any prose." | `fiction-project-governance-and-handoffs` |
| 2 | "Plan the architecture for Book 4 of a mythic sci-fi series. Create a chapter-function map and controlled brief for Chapter 1. Research-only mythology dossier first — no prose." | `fiction-architecture-briefing-and-research-gates` |
| 3 | "Draft Chapter 11 of Anunnaki Book 4 from the approved brief. Write the file safely, verify word count, update the tracker, and stop at the review gate." | `controlled-fiction-drafting-and-autonomous-runs` |
| 4 | "Read the completed manuscript and produce a structural reader audit and targeted revision plan. Do NOT edit any prose — read-only assessment." | `fiction-editorial-audits-and-revision-planning` |
| 5 | "Apply the approved Pass 2 expansion plan to Chapter 6. Targeted developmental deepening only within the approved scope. Verify word counts and stop." | `controlled-fiction-revision-and-expansion` |
| 6 | "Assemble the full manuscript for export. Create final QA hashes, verify chapter order and word counts, and freeze the book." | `fiction-assembly-final-qa-and-freeze` |
| 7 | "Create a family reader package with feedback forms for the Brambleford series. Generate static reader-site files. Do not deploy." | `reader-package-and-feedback-workflow` |
| 8 | "Run a blind evaluation comparing two model outputs for a creative writing test on frozen inputs. Record results before any promotion." | `controlled-model-evaluation-for-creative-work` |

### 2. ORDINARY LONG-FORM SERIES DRAFTING REQUEST (may trigger old skill)

| # | Prompt | Expected Route | Notes |
|---|--------|----------------|-------|
| 9 | "Continue drafting my Brambleford cozy mystery series. Pick up where the last chapter left off and write the next chapter." | Could match old skill OR `controlled-fiction-drafting-and-autonomous-runs` | Tests old skill bypass |

### 3. AMBIGUOUS CROSS-STAGE REQUEST

| # | Prompt | Expected Route | Notes |
|---|--------|----------------|-------|
| 10 | "I want to work on my novel. Not sure if I should plan, draft, or revise. Help me figure out what to do next." | `longform-fiction-production` (router) | Tests router when stage unclear |

### 4. REQUEST THAT SHOULD STOP AT ANDREW APPROVAL GATE

| # | Prompt | Expected Route | Notes |
|---|--------|----------------|-------|
| 11 | "Review and refine this request: I want to expand the Anunnaki series with a new trilogy. What should the architecture look like?" | `fiction-architecture-briefing-and-research-gates` (should STOP before prose) | Tests "review and refine" gate |

### 5. REQUEST INVOLVING EXISTING CANONICAL SERIES

| # | Prompt | Expected Route | Notes |
|---|--------|----------------|-------|
| 12 | "Check if the Meridian Relics manuscript is safely preserved and resumable. Verify the canonical repo, status, handoff, and git state." | `fiction-project-governance-and-handoffs` | Tests canonical series handling |

### 6. OUT-OF-SCOPE REQUEST (no fiction skill should claim)

| # | Prompt | Expected Route | Notes |
|---|--------|----------------|-------|
| 13 | "Write a Python script to scrape Goodreads for book ratings." | NONE (no fiction skill should claim) | Tests skill boundary |

---

## Execution Method

For each scenario, run:
```bash
hermes -p fiction chat -q "<prompt>" -Q --toolsets ""
```

Record for each:
- Exact prompt
- Session ID
- Skill(s) activated
- Selected route
- Expected route
- Pass/Fail
- Duplicate activation?
- Recursion/routing loop?
- Manuscript/repo mutation attempted?
- Authority/stop rules respected?
- Actual model and provider