# Handoff System

## Purpose

Preserve state across sessions so that:
- The next session knows where to resume
- The showrunner can recover from context compression
- Multiple profiles can coordinate without conversation history

**Golden rule:** Handoff before report. Update state files before presenting session summaries to the user.

---

## Handoff Files

### `handoff/MASTER-HANDOFF.md`

The primary handoff document. Updated after every autonomous stage.

**Structure:**
```markdown
# Project Handoff — [Series Name] Book [N]

## Current Status
- Stage: [current pipeline stage]
- Word count: [actual total]
- Chapters complete: [N of total]
- Blockers: [none / list]

## Last Completed Work
- [Brief description of what was done]
- [Files modified]
- [Commits made]

## Next Task
- [What the next session should do]
- [Priority: HIGH / MEDIUM / LOW]
- [Expected output]

## Critical Files to Read
1. [file path] — [why]
2. [file path] — [why]

## Tone / Voice Reminders
- [Any specific reminders for the writer]

## Verification Checklist
- [ ] Read this handoff
- [ ] Read the tracker
- [ ] Read the specific chapter/file being worked on
- [ ] Read adjacent chapters for continuity (one before, one after)
- [ ] Confirm the named next task matches the tracker
- [ ] Proceed silently without asking for confirmation (autonomy mode)

## Session Boundary Notes
- [Any compression warnings, context limits, etc.]
```

### `handoff/sessionN-handoff.md` (Optional)

When a single session produces significant work, create a dated handoff:

```markdown
# Session Handoff — [Date]

## Accomplished
- [List]

## Current Totals
- Words: [N]
- Chapters: [N of total]
- Status: [stage]

## Next Steps
- [List]

## Files
- [List of created/modified files]
```

---

## Handoff Discipline

### After Every Autonomous Stage

1. Complete work
2. Update `handoff/MASTER-HANDOFF.md`
3. Update `tracking/BOOK<N>_DASHBOARD.md`
4. Commit with descriptive message
5. Present report to user

### When User Signals Context Compression

The user may say "we have to compress this conversation" or "update the handoff repo." This means:
- Create a comprehensive handoff immediately
- Include ALL state the next session needs
- Do not rely on the next session having conversation history

The handoff becomes the source of truth.

### Session-Start Protocol

When a session starts with "New session started" and a REPORT block:

1. Read `handoff/MASTER-HANDOFF.md`
2. Read `tracking/BOOK<N>_DASHBOARD.md`
3. Read the specific chapter/file being worked on
4. Read adjacent chapters for continuity (one before, one after)
5. Confirm the named next task matches the tracker
6. Proceed silently without asking for confirmation

**Do not ask "What would you like to work on?" or "Where did we leave off?"** The handoff and tracker contain this information. Use them.

---

## Cross-Profile Handoffs

When handing off from one profile to another:

### Showrunner → Writer
- Architecture document
- Tracker with current status
- Job Statements for chapters to draft
- Voice reminders
- Autonomy constraints (if any)

### Writer → Editor
- Complete draft set
- Architecture document
- Tracker
- Discovery Pass report (if done)
- Specific concerns from writer

### Editor → Reader
- Fixed manuscript (after Pass 3.5)
- Editorial report (for showrunner only, NOT for reader)
- Tracker
- Reader audit template

### Reader → Showrunner
- Reader audit report
- Classification table
- Recommendations (not prescriptions)

---

## Comprehensive Handoff Pattern

For long sessions or major milestones, create a comprehensive handoff:

```markdown
# Comprehensive Handoff — [Milestone]

## Project State
- Book: [N]
- Stage: [current]
- Words: [total]
- Commits since last handoff: [N]

## What Changed
- [Detailed list of changes]

## What Remains
- [Detailed list of remaining work]

## Decisions Made
- [List of decisions with DEC- IDs]

## Risks
- [Known blockers, unresolved questions]

## Next Session Task
- [Specific, actionable task]
- [Expected output]
- [Decision points where human judgment is needed]

## Files to Read (Priority Order)
1. handoff/MASTER-HANDOFF.md
2. tracking/BOOK<N>_DASHBOARD.md
3. [specific working file]
4. [adjacent chapter for continuity]
```

---

## Common Pitfalls

- **Handoff after report:** Presenting the session report to the user BEFORE updating the handoff. The user may close the session before the handoff is written.
- **Stale handoffs:** Handoffs that describe work done two sessions ago. Update after EVERY autonomous stage.
- **Missing critical files:** Not listing the specific files the next session must read.
- **Vague next tasks:** "Continue drafting" is not specific. "Draft Chapter 7, which covers [beats], estimated [range] words" is specific.
- **Autonomy confusion:** If autonomy is granted, the handoff should say so explicitly. If not, the handoff should specify approval gates.
