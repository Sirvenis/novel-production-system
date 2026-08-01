# Rollback Plan — Live Coexistence Canary

**Date**: 2026-08-01  
**Phase**: Live Coexistence Canary — Fiction Profile Only  
**Objective**: Install nine split fiction skills alongside existing live skill in fiction profile, verify routing and detect conflicts

---

## Pre-Change State Snapshots

### 1. Fiction Profile Configuration
- **File**: `/home/andrew/.hermes/profiles/fiction/config.yaml`
- **SHA-256**: `c3f1eb3e305db8b2ef964957fcc2c67b065ea2f2b39089b945e0860b78e1daec`
- **Backup**: `/home/andrew/.hermes/profiles/fiction.backup.20260801_*/config.yaml`

### 2. Global Live Skill (unchanged during this phase)
- **File**: `/home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/SKILL.md`
- **SHA-256**: `bbd5fd26ec5747a8f95837756ff028420f08c10e4e59773399d39a375479531a`
- **Must remain unchanged**: This phase does NOT authorize slimming, replacing, disabling, moving, or deleting the old live skill

### 3. Fiction Profile Skills Directory (before install)
- **Path**: `/home/andrew/.hermes/profiles/fiction/skills/creative/`
- **Contents**: 17 builtin creative skills only (no local fiction skills)
- **No `longform-fiction-series-drafting` installed locally in fiction profile**

### 4. Test Profile (isolated, must remain unchanged)
- **Path**: `/home/andrew/.hermes/profiles/fiction-skill-canary/`
- **Contains**: 9 staged skills from test-profile canary
- **Must not be modified** during this phase

### 5. Default Profile (must remain unchanged)
- **Path**: `/home/andrew/.hermes/profiles/default/`
- **Minimal config only (.env)**

### 6. Series Profiles (must remain unchanged)
- `anunnaki`, `horror-series`, `meridian-master`, `brambleford-showrunner`, etc.
- These explicitly enable `creative/longform-fiction-series-drafting` in their enabled skills list

---

## Files This Phase May Change

### Primary Changes
1. **Nine new skill directories** under `/home/andrew/.hermes/profiles/fiction/skills/creative/`:
   - `controlled-fiction-drafting-and-autonomous-runs/`
   - `controlled-fiction-revision-and-expansion/`
   - `controlled-model-evaluation-for-creative-work/`
   - `fiction-architecture-briefing-and-research-gates/`
   - `fiction-assembly-final-qa-and-freeze/`
   - `fiction-editorial-audits-and-revision-planning/`
   - `fiction-project-governance-and-handoffs/`
   - `longform-fiction-production/`
   - `reader-package-and-feedback-workflow/`

2. **No profile config changes** in this phase — skill enablement tested via explicit `-s` flag

---

## Rollback Procedure

### If Installation Fails or Canary Fails

#### Option A: Remove Only New Skills (if profile config unchanged)
```bash
# Remove the nine newly installed skill directories
rm -rf /home/andrew/.hermes/profiles/fiction/skills/creative/controlled-fiction-drafting-and-autonomous-runs
rm -rf /home/andrew/.hermes/profiles/fiction/skills/creative/controlled-fiction-revision-and-expansion
rm -rf /home/andrew/.hermes/profiles/fiction/skills/creative/controlled-model-evaluation-for-creative-work
rm -rf /home/andrew/.hermes/profiles/fiction/skills/creative/fiction-architecture-briefing-and-research-gates
rm -rf /home/andrew/.hermes/profiles/fiction/skills/creative/fiction-assembly-final-qa-and-freeze
rm -rf /home/andrew/.hermes/profiles/fiction/skills/creative/fiction-editorial-audits-and-revision-planning
rm -rf /home/andrew/.hermes/profiles/fiction/skills/creative/fiction-project-governance-and-handoffs
rm -rf /home/andrew/.hermes/profiles/fiction/skills/creative/longform-fiction-production
rm -rf /home/andrew/.hermes/profiles/fiction/skills/creative/reader-package-and-feedback-workflow

# Verify rollback
hermes -p fiction skills list
```

#### Option B: Full Profile Restore (if profile config was modified)
```bash
# Restore entire fiction profile from backup
BACKUP_DIR=$(ls -dt /home/andrew/.hermes/profiles/fiction.backup.* | head -1)
rm -rf /home/andrew/.hermes/profiles/fiction
cp -r "$BACKUP_DIR" /home/andrew/.hermes/profiles/fiction

# Verify
hermes -p fiction skills list
cat /home/andrew/.hermes/profiles/fiction/config.yaml | sha256sum
# Should match: c3f1eb3e305db8b2ef964957fcc2c67b065ea2f2b39089b945e0860b78e1daec
```

### Verification After Rollback
1. `hermes -p fiction skills list` — should show only builtin skills, no local fiction skills
2. Global live skill unchanged: `sha256sum /home/andrew/.hermes/skills/creative/longform-fiction-series-drafting/SKILL.md` → `bbd5fd26...`
3. Test profile intact: `ls /home/andrew/.hermes/profiles/fiction-skill-canary/skills/creative/` → 9 skills
4. Default profile intact
5. Series profiles intact (e.g., `anunnaki` still has `creative/longform-fiction-series-drafting` enabled)

---

## What This Phase Does NOT Change
- ❌ Global `longform-fiction-series-drafting` skill (remains at `/home/andrew/.hermes/skills/creative/`)
- ❌ Default profile
- ❌ Any series profile (`anunnaki`, `horror-series`, `meridian-*`, `brambleford-*`, etc.)
- ❌ Test profile (`fiction-skill-canary`)
- ❌ Any manuscript repository
- ❌ Any canonical series repo
- ❌ Any SOUL files, memory policy, model policy, toolsets, or workdir

---

## Canary Failure Criteria (Triggering Rollback)
- Routing collisions causing duplicate activation or infinite recursion
- Manuscript or repository mutation attempted during canary
- Authority/stop gates not respected
- Old skill bypasses new routing unexpectedly
- Any profile other than `fiction` shows changes
- Test profile shows changes