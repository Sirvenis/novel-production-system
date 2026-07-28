# Skill: Canary Run

**Purpose:** Pre-scale validation that an agent profile can execute a full pipeline stage autonomously without drifting. A canary run is a small, bounded test that catches problems before committing to a long autonomous session.

**When to use:** Before granting or expanding autonomy to a profile. After creating a new profile. After significant changes to SOUL.md, config, or pipeline infrastructure. Before running a multi-chapter autonomous session.

**When NOT to use:** For routine single-chapter tasks where autonomy is already proven. For tasks that require human judgment (architecture decisions, freeze decisions).

**Who runs this:** Showrunner (master) profile, testing another profile's capabilities.

---

## What It Does

The Canary Run executes a bounded, low-risk task on a single chapter or a small section, then verifies:

1. **Instruction adherence** — Did the agent follow its SOUL.md and skill instructions?
2. **Output quality** — Is the output structurally correct and on-voice?
3. **Pipeline compliance** — Did the agent follow the pipeline stage's defined steps?
4. **State management** — Did the agent update trackers, handoffs, and commit correctly?
5. **Drift detection** — Did the agent deviate from its mandate? By how much?

---

## Execution Steps

### Step 1: Define the Canary Task

Select a task that is:
- **Bounded:** One chapter, one pass, one check — not a full pipeline run
- **Low-risk:** If the agent fails, no canon material is lost
- **Representative:** The task exercises the same skills the full autonomous run will need
- **Verifiable:** The output can be checked against a known-good result or rubric

Example canary tasks per profile:

| Profile | Canary Task | What It Tests |
|---------|-------------|---------------|
| Writer | Draft one chapter from an existing job statement | Voice, POV, word count target, job statement discipline |
| Editor | Run developmental editorial on one existing chapter | Four questions method, verdict format, report structure |
| Reader | Read one chapter and produce a reader audit | Five questions, experience-not-prescription discipline |
| Showrunner | Run a Discovery Pass on an assembled manuscript | Inventory accuracy, gap detection, no-recommendations rule |
| Researcher | Ingest one video/article and produce a structured report | Metadata capture, insight synthesis, filing, commit |

### Step 2: Set the Boundaries

Define explicit constraints for the canary run:
- **Scope:** Exactly what the agent should do (one chapter, one pass, one report)
- **Stop condition:** When the agent should stop (after one chapter, after one report, after one check)
- **Output location:** Where the agent should write files
- **Commit message:** What the commit should say
- **Time limit:** How long the canary should take (typically 10-30 minutes)

Write the boundaries as a task instruction:

```
CANARY TASK: [task description]
SCOPE: [exactly what to do]
STOP WHEN: [completion condition]
OUTPUT TO: [file paths]
COMMIT AS: [commit message format]
TIME LIMIT: [minutes]
```

### Step 3: Execute the Canary

Run the canary task with the target profile. Options:

**Option A: Delegate (preferred for quick canaries)**
```
delegate_task(
  goal="[CANARY TASK description with boundaries]",
  context="[Profile SOUL.md contents, pipeline stage instructions, file paths]",
  role="leaf"
)
```

**Option B: Spawn profile (for testing profile-specific behavior)**
```
terminal(command="hermes chat -q -p [profile] '[CANARY TASK instruction]'", timeout=300)
```

**Option C: Manual session (for interactive observation)**
```
Run the profile interactively, observe behavior, take notes on drift
```

### Step 4: Verify the Output

After the canary completes, verify against the rubric:

| Check | Method | Pass Criteria |
|-------|--------|---------------|
| Output exists | `read_file` the expected output path | File is present and non-empty |
| Output is structurally correct | Read the file, check structure | Matches the expected format (report template, chapter structure, etc.) |
| Instructions were followed | Compare output to SOUL.md + skill instructions | No deviations from the defined scope |
| Pipeline stage was respected | Check against the stage definition in PRODUCTION_PIPELINE.md | Agent did not skip steps or add unauthorized steps |
| State was updated | Check tracker, handoff, and git log | Tracker updated, handoff written, commit message correct |
| No drift | Compare what the agent did vs what it was told to do | Scope, output, and behavior match |

### Step 5: Drift Assessment

If the agent deviated, document:

| Dimension | Expected | Actual | Drift Severity |
|-----------|----------|--------|----------------|
| Scope | [what was asked] | [what was done] | [None/Minor/Major] |
| Output format | [expected format] | [actual format] | [None/Minor/Major] |
| Pipeline steps | [expected steps] | [actual steps] | [None/Minor/Major] |
| State updates | [expected updates] | [actual updates] | [None/Minor/Major] |
| Commit | [expected message] | [actual message] | [None/Minor/Major] |

**Drift severity levels:**
- **None:** Agent did exactly what was asked
- **Minor:** Agent added small improvements or clarifications within scope
- **Major:** Agent went beyond scope, skipped required steps, or produced wrong output type

**Decision:**
- All None/Minor: Autonomy granted for this task type. Proceed to full run.
- Any Major: Do not grant autonomy. Review SOUL.md or instructions. Re-run canary after fixes.

### Step 6: Log the Canary Result

Write the result to `audits/CANARY_LOG.md` (or append if it exists):

```markdown
## Canary Run: [date]

**Profile tested:** [profile name]
**Task type:** [drafting/editorial/reading/discovery/research]
**Canary task:** [brief description]
**Result:** PASS / PASS WITH NOTES / FAIL
**Drift summary:** [None/Minor/Major — describe if any]
**Decision:** Autonomy granted / Autonomy deferred — [reason]

---
```

---

## Verification

- [ ] Canary task was bounded (one chapter/one pass/one check)
- [ ] Agent was given explicit scope and stop conditions
- [ ] Output was verified against a rubric, not just checked for existence
- [ ] Drift was assessed across all five dimensions
- [ ] Result was logged to CANARY_LOG.md
- [ ] Decision (grant/defer autonomy) was explicit and justified

---

## Common Failure Modes

| Failure | Cause | Fix |
|---------|-------|-----|
| Canary too large | Selected "draft 3 chapters" instead of 1 | Scale down to the smallest representative task |
| No rubric | "Check if the output looks good" | Define specific pass criteria before running |
| Drift not detected | Only checked output existence, not adherence | Compare actual behavior against instructions dimension by dimension |
| Autonomy granted too quickly | Canaries passed but full run failed | Run 2-3 canaries of different types before granting full autonomy |
| Profile-specific behavior missed | Used delegate instead of spawning the actual profile | Use `hermes chat -q -p [profile]` to test profile-specific SOUL.md behavior |

---

## Tools

- `delegate_task` — run canary as a subagent (quick, isolated)
- `terminal` — spawn a profile-specific session
- `read_file` — verify output files
- `search_files` / `grep` — verify structural compliance
- `write_file` — log results to CANARY_LOG.md

---

*Skill created for the novel-production-system. Aligns with the multi-profile pipeline pattern and the autonomy grant lessons from Book 2 and Book 3 case studies.*