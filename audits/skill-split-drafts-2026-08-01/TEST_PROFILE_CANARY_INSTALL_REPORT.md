# Test-Profile Skill Canary Install Report

Date: 2026-08-01

## Scope

Andrew explicitly approved:

> Proceed with the test-profile skill canary install. Do not replace live skills yet.

This pass installed the staged fiction skill split package into a dedicated test-only Hermes profile and ran a fresh-session routing canary.

## Test profile

- Profile: `fiction-skill-canary`
- Path: `/home/andrew/.hermes/profiles/fiction-skill-canary`
- Model for canary: `gpt-5.6-luna` via `openai-codex`
- Workdir: `/home/andrew/novel-production-system`
- Memory: disabled in test profile config
- Bundled skills: disabled via `.no-bundled-skills`
- Live manuscript work: forbidden by profile SOUL

## Installed staged skills

Destination:

`/home/andrew/.hermes/profiles/fiction-skill-canary/skills/creative/`

Skills installed: 9

- `controlled-fiction-drafting-and-autonomous-runs`
- `controlled-fiction-revision-and-expansion`
- `controlled-model-evaluation-for-creative-work`
- `fiction-architecture-briefing-and-research-gates`
- `fiction-assembly-final-qa-and-freeze`
- `fiction-editorial-audits-and-revision-planning`
- `fiction-project-governance-and-handoffs`
- `longform-fiction-production`
- `reader-package-and-feedback-workflow`

## Verification commands/results

`hermes -p fiction-skill-canary skills list` reported:

- 9 local skills
- 9 enabled
- 0 hub-installed
- 0 builtin
- 0 disabled

Local validation of copied profile skill files reported:

- skill count: 9
- frontmatter/link issues: 0

## Fresh-session routing canary

Command used:

`hermes -p fiction-skill-canary -s longform-fiction-production chat -q "$(cat canary-routing-prompt.txt)" -Q --toolsets ""`

Output:

```text
⚠ tirith security scanner enabled but not available — command scanning will use pattern matching only

session_id: 20260801_144652_910ab1
CANARY_ROUTE_RESULT
1. fiction-project-governance-and-handoffs
2. fiction-architecture-briefing-and-research-gates
3. controlled-fiction-drafting-and-autonomous-runs
4. fiction-editorial-audits-and-revision-planning
5. controlled-fiction-revision-and-expansion
6. fiction-assembly-final-qa-and-freeze
7. reader-package-and-feedback-workflow
8. controlled-model-evaluation-for-creative-work
LIVE_SKILLS_CHANGED: no
```

Result: PASS.

The router mapped all 8 scenarios to the expected staged task skills.

## Runtime evidence

Profile agent log showed the canary ran as:

```text
2026-08-01 14:46:55,150 INFO [20260801_144652_910ab1] agent.turn_context: conversation turn: session=20260801_144652_910ab1 model=gpt-5.6-luna provider=openai-codex platform=cli history=0 msg='You are running inside the test-only profile `fiction-skill-canary`.  This is a ...'
2026-08-01 14:47:01,335 INFO [20260801_144652_910ab1] agent.conversation_loop: API call #1: model=gpt-5.6-luna provider=openai-codex in=13663 out=139 total=13802 latency=5.4s
```

No fallback activation was observed in the captured canary log excerpt.

## Live skill safety check

The live global skill was not replaced or slimmed:

- Live skill checked: `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/SKILL.md`
- Current SHA-256 prefix: `bbd5fd26ec5747a8`
- Live replacement performed: no
- Legacy references deleted/moved: no
- Default/profile skill lists changed outside test profile: no

Note: running the canary profile created normal profile-local runtime files such as `state.db`, `logs/`, cache files, and a profile-local `bin/tirith`. These are confined to `/home/andrew/.hermes/profiles/fiction-skill-canary/`.

## Conclusion

The staged fiction skill split package successfully installs and loads in a dedicated test profile. The router canary passed against the expected eight task routes.

## Next safe step

Prepare the live skill slimming plan, but do not execute it until Andrew explicitly approves live replacement/slimming. The next plan should specify exactly:

1. which live skill files would be added;
2. which old `longform-fiction-series-drafting` files would remain archived;
3. how the default/fiction profiles would reference the new router;
4. rollback path if skill loading fails;
5. confirmation that high-impact runtime/deployment references remain quarantined.
