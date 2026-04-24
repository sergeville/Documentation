# Session Minutes — 2026-04-07 07:00 — Repo Hygiene & Documentation

**Agent:** Claude (Opus 4.6)
**Duration:** ~40 min
**Focus:** Synapse repo inventory — .git audit + README documentation for archived/frozen subprojects

## Decisions

1. **`idea-capture-web 2/`** — confirmed as iCloud duplicate junk. Already gitignored. Has its own `.git`. Safe to delete.
2. **`workflow-panel/`** — created 5W README documenting frozen/source-lost status. Source destroyed by APFS corruption (2026-03-27), never committed. Only Docker image survives. Candidate for absorption into claude-cockpit.
3. **`workspace-hub/`** — created 5W README documenting archived status. Source is fully intact (Express API :3022 + React client :3021, 6 tabs). Superseded by launcher (:3000) + cockpit (:3027). Never committed to git, gitignored under "Archived".

## Artifacts Created

- `Synapse/workflow-panel/README.md` — 5W summary, architecture, do-not-build warnings
- `Synapse/workspace-hub/README.md` — 5W summary, architecture diagram, tech stack table

## Findings

- Only 2 `.git` entries in Synapse (depth 2): root repo + `idea-capture-web 2/` (junk)
- `.gitignore` "not Synapse source" section covers: `archon-knowledge-local/`, iCloud dupes, `workflow-panel/`, `workspace-hub/`, `.git.nosync/`, `.claude/worktrees/`, build artifacts

## Open Items

- `idea-capture-web 2/` can be deleted (awaiting Serge's go-ahead)
- Several services down during session: archon-fs-bridge, workspace-launcher, capture-api (supervisor auto-restarting)

---

# Session Minutes — 2026-04-07 09:30 — Post-iCloud Cleanup: Docker & Path Fixes

**Agent:** Claude (Opus 4.6)
**Duration:** ~25 min
**Focus:** Docker validation, path normalization, SYNAPSE_ROOT env var introduction across all services

## Decisions

1. **`Archon` → `archon`** — renamed in `~/Dev/Synapse/` to match `~/Documents/Synapse/archon/` (lowercase). Two-step rename for case-insensitive APFS.
2. **SYNAPSE_ROOT pattern** — all hardcoded `~/Documents/Synapse/` paths replaced with `SYNAPSE_ROOT` env var, defaulting to `~/Documents/Synapse`. Same for `DOCUMENTS_ROOT` (defaults to `~/Documents`).
3. **Docker volume mounts** — `archon/docker-compose.yml` updated to use `${SYNAPSE_ROOT}` and `${DOCUMENTS_ROOT}` with same defaults.
4. **`~/Synapse`** — identified as dead empty directory (created 2026-03-22, never populated). Still mounted as Docker volume `/synapse:ro`. Now replaced by `${SYNAPSE_ROOT}` default.

## Code Changes

### SYNAPSE_ROOT refactored (7 files):
- **`launcher/server.py`** — 25+ paths converted. Added `SYNAPSE_ROOT` and `DOCUMENTS_ROOT` at top. All service `cwd`, `log`, `cmd` paths use them. Also fixed `Archon/archon-ui-main` → `archon/archon-ui-main` (case).
- **`claude-cockpit/server.py`** — 2 Kokoro TTS paths (`venv-kokoro`, `kokoro_daemon.py`) → `SYNAPSE_ROOT`.
- **`ai-dev-dashboard/server.py`** — `SPRINT_STATUS_PATH` and `STORIES_PATH` defaults → `SYNAPSE_ROOT` fallback inside existing `os.getenv()`.
- **`projects-viewer/server.py`** — `README_PATH` and `MANIFEST_PATH` → `DOCUMENTS_ROOT`.
- **`neural-map/server.py`** — `ALLOWED_ROOTS` → `DOCUMENTS_ROOT`.
- **`ai-supervisor/archon-backup.sh`** — `LOCAL_DIR` → `${DOCUMENTS_ROOT:-$HOME/Documents}`.
- **`archon/docker-compose.yml`** — volume mounts → `${DOCUMENTS_ROOT}` / `${SYNAPSE_ROOT}`.

### Files synced from Documents → Dev:
- `archon/python/src/` — 272 files (full Archon backend source)
- `archon/archon-ui-main/` — 1,454 files (frontend + node_modules)
- `archon/docker-compose.yml` — copied
- `archon/.env` — copied (9 lines, Supabase credentials)

## Docker Status

| Container | Status | Notes |
|---|---|---|
| archon-server | Healthy | Was unhealthy at session start, self-recovered |
| archon-mcp | Up | OK |
| archon-agent-work-orders | Healthy | OK |
| archon-frontend | **Missing** | Not running, container absent |
| voice-boardroom | **Not running** | 6/7 COPY sources missing (APFS casualty) |
| 13× Supabase | Healthy | Local stack OK |
| home-assistant | Exited | Stopped 14h ago |

## .env Validation

| File | Status |
|---|---|
| `ai-orchestrator/.env` | 1 line |
| `voice-boardroom/.env` | 19 lines |
| `archon/.env` | 9 lines (copied from Documents) |
| `ANTHROPIC_API_KEY` | Set in shell |
| `OPENAI_API_KEY` | Set in shell |
| `SUPABASE_URL/KEY` | In archon/.env |

## Findings

- **voice-boardroom Dockerfile** references 6 source files missing from both Dev and Documents: `boardroom.html`, `vwa.html`, `strategy-room.html`, `hvac_client.py`, `hvac_intent.py`, `vwa_audit.py`. Likely lost to APFS corruption. Only `server.py` survives. Existing Docker image has them baked in.
- **`~/Synapse`** is an empty directory from March 22 — mounted by Docker but serves nothing.
- **archon-server** recovered to healthy during the session without intervention.

## Open Items

- `~/Synapse` empty dir — can be deleted (stale)
- voice-boardroom source recovery — extract from running Docker image or accept loss
- archon-frontend container not running — investigate if intentional (Docker-only service vs Vite dev)
- To run from Dev: `SYNAPSE_ROOT=~/Dev/Synapse python3 launcher/server.py`
