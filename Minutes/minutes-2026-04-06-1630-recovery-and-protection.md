# Session Minutes — 2026-04-06 16:30 → 18:07
## Recovery, Audit, and Data Protection Plan

**Agent:** Claude (orchestrator, Opus 4.6)
**Duration:** ~1h 37min
**Sub-agents spawned:** Scout (3x), Nexus (2x)
**Commits:** 3 across 3 repos

---

## What Happened

Session started as a self-diagnostic after Serge noticed the iCloud Documents folder was affected. Evolved into a full infrastructure recovery, multi-agent audit, and data protection plan.

---

## Decisions Made

1. **Synapse git repo repaired** — .git was broken (missing HEAD/objects/refs). Re-init + fetch + force checkout to origin/main.
2. **Archon server restored** — source code was wiped from Archon/python/src/ (Docker data loss). Copied 218 files from Archon-fresh/. Container healthy.
3. **archon-fs-bridge fixed** — venv corrupted (Python 3.14 pip broken), kqueue hanging on large trees. Rebuilt venv, switched to PollingObserver, moved HTTP server start before observer.start().
4. **iCloud eviction diagnosed** — "Optimize Mac Storage" silently evicted 1,389+ files from Documentation/, Scripts/, Projects/. Synapse/ survived because services held files open.
5. **Time Machine was OFF** — AutoBackup = 0, last backup April 4.
6. **Data protection plan designed** — 7-layer plan: move to ~/Dev/, re-enable TM, git discipline, local backups, disk management, supervisor watchdogs, architecture decision.
7. **Git restructure plan created** — .gitignore uses whitelist pattern (only 341/500+ files tracked). Plan to flip to blacklist, remove 15 embedded .git dirs, consolidate 3 Archon copies.

## Issues Encountered

- Archon/python/src/ was empty — Docker bind mount had no source code
- archon-fs-bridge venv had broken pip (Python 3.14 compatibility)
- kqueue observer hangs on ~/Documents/Synapse/ (too many files)
- Documentation git repo had corrupt objects from iCloud eviction
- iCloud created 50+ duplicate files with " 2" suffix
- Orchestrator spamming "Network outage" escalations every 60s (false positive)
- CPU spiked to 55.5 (iCloud daemons), settled to 7.8

## Code Changes

| Repo | Commit | Description |
| --- | --- | --- |
| Synapse | `3f15ffa` | fix(archon-fs-bridge): PollingObserver + HTTP-first startup |
| Scripts | `8900db6` | chore: safety commit — startidea, stopidea, archon-backup, smart-rename |
| Documentation | `1ba52e2` | chore: safety commit — 28 files including roster.json, Minutes/, specs |

## Files Created

- `Synapse/docs/REPO_RESTRUCTURE_PLAN.md` — git restructure plan (Nexus)
- `.claude/projects/.../memory/project_icloud_eviction_2026-04-06.md` — incident memory

## Disk Space

- Reclaimed ~13.4 GB: .claude/debug/ (10 GB) + Docker build cache (3.4 GB) + telemetry (39 MB)
- Free space: 12 GB → 18 GB

## Service Health at End of Session

- 15/15 Synapse services healthy (all ports responding 200)
- Archon API healthy (3ms)
- CPU load normal (7.8)
- 0 open anomalies from supervisor (down from 13 at start)
- archon-fs-bridge: healthy (was down for 66 recurrences)

## Team Audit Results

**Scout-TimeMachine:** Files are evicted (dataless stubs), not deleted. iCloud has the content. TM AutoBackup OFF. "Documents - Serge's MacBook" is normal iCloud folder.

**Scout-Minutes:** All 341 committed files present. Zero missing. Archon directory duplication is a landmine (3 copies, one with space in name). ~/Documents has 10 items not 6.

**Scout-GitHub:** All committed code safe on GitHub. 87 uncommitted changes across 3 repos (now committed). 2 corrupted .git dirs (claude-dashboard, ai-dev-dashboard). 21 of 50 GitHub repos not cloned locally.

**Nexus-Protection:** 7-layer plan — move to ~/Dev/, TM monitoring, git discipline, local backups, disk management, supervisor watchdogs.

**Nexus-Git-Restructure:** .gitignore whitelist pattern blocking 160+ files. Plan to flip to blacklist, remove embedded .git dirs, consolidate Archon, clean duplicates. 4-phase migration with rollback.

## Late Session (18:07 → 18:31)

### Git restructure plan designed (Nexus)
- Nexus audited .gitignore, directory structure, embedded repos
- Found: whitelist .gitignore pattern blocking 160+ files from tracking (only 341/500+ tracked)
- Found: 15 embedded .git dirs (71 MB), 3 Archon copies, 53 iCloud duplicate files
- Plan written to `docs/REPO_RESTRUCTURE_PLAN.md` — 4-phase migration with rollback

### 8 design questions answered by Serge
1. Rename "Archon 2" → `archon/` — YES
2. `_bmad/` — delete .git, track as reference
3. `workflow-panel/` — keep skeleton
4. `workspace-hub/` — archive
5. `Idea-to-Sprint/` — keep but clean
6. `issue-tracking-system/` — archive
7. Keep `synapse_base/` (underscore), delete `synapse-base/` (dash) — YES
8. Git LFS — not now, files small enough

### GitHub strategy decided
- **Monorepo**: Synapse stays as single repo, all services tracked as folders
- Individual GitHub repos (claude-dashboard, ai-dev-dashboard, etc.) stay as archived read-only references — NOT deleted (preserves history)
- Archon stays independent (separate product)
- Remove 15 embedded .git dirs locally so parent repo can track those files

### iCloud "Optimize Mac Storage" — can't disable
- macOS Tahoe re-enables the toggle when disk is low (18 GB free)
- Decision: don't fight it — the ~/Dev/ move solves this permanently
- Files outside ~/Documents/ are never touched by iCloud

### Time Machine re-enabled
- Serge confirmed TM is running (done in System Settings)
- Last backup gap closed

## Pending for Next Session

1. **Git restructure** — execute 4-phase plan (junk → .git dirs → rename → .gitignore rewrite)
2. **Move to ~/Dev/** — relocate Synapse/, Documentation/, Scripts/ out of iCloud
3. **Fix orchestrator network outage false positive** — supervisor says net_ok but orchestrator keeps escalating
4. **Diff "Documents - Serge's MacBook"** against Documentation/ before deleting
5. **Phase 2 protection** — synapse-backup.sh, supervisor watchdogs (dataless, TM, git dirty)

---

*Logged 2026-04-06 18:31. Full recovery session: infrastructure repair, 5-agent audit, 7-layer protection plan, git restructure designed, all at-risk files committed.*
