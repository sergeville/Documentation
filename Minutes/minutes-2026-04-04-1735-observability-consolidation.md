# Session Minutes — 2026-04-04 17:35 → 18:47
## Observability Layer Consolidation + Promote Flow Restoration

**Agent:** Claude (orchestrator, Opus 4.6)
**Duration:** ~1h 12min
**Sub-agents spawned:** Scout (observability inventory), Sentinel (QA review), Nexus/Plan (merge architecture)

---

## Decisions Made

1. **Observability layer approach**: Scope set to the dashboard/cockpit layer (option b), not the broader idea pipeline. Target = 11 → 5-6 dashboards.
2. **workflow-panel fate**: FROZEN. Source files lost in APFS 2026-03-27 corruption; Docker image has pre-built bundle; `restart: unless-stopped` keeps container alive. Do NOT rebuild image. Status documented in `Synapse/workflow-panel/SOURCE_LOST.md`.
3. **Dashboard merge architecture**: HYBRID — tab shell in cockpit `index.html` for small panels + separate HTML files (`/boardroom.html`, `/console.html`) for heavy ones. Keeps projected cockpit index.html under 3000L.
4. **Debates tab**: candidate for RETIRE (not migrate) — `debates/` dir is empty, Boardroom supersedes. Serge to confirm.
5. **Heartbeat schema extension**: `current_activity` + `activity_started_at` + `activity_ttl_seconds` added as live-balloon layer over existing `current_task` session field.

---

## Shipped (7 changesets)

1. **Story ic-0006 — Promote idea to Archon task (inline)**
   - Replaced PromotionManager dependency (APFS loss) with inline `create_archon_task` call
   - Added `archon_task_id` write-back + `workflow_step='Promoted'`
   - Idempotent; per-idea `threading.Lock` prevents concurrent duplicates
   - Frontend modal: shows Archon task id + "Open in Archon" button (was CLI command)
   - Archon task `3a5009df` closed, sprint-status.yaml updated

2. **Task 409346e3 — BMAD path updates**
   - Replaced `~/Documents/_bmad*` → `~/Documents/Synapse/_bmad*` across 13 refs in 11 files
   - Files: CLAUDE.md, .claude/skills/, .claude/agents/, Documentation/System/, AI-SYSTEM-ORIENTATION, CLAUDE_ORCHESTRATION, SYSTEM-MANIFEST, PLAN_THREE_GAPS, PLAN_REMAINING_SHORTFALLS, UI_DESIGNER_PROMPT, AI_ORCHESTRATOR_ARCHITECTURE
   - Historical BMAD_V6_INSTALL_PLAN.md left intact (install record)

3. **ai-dev-dashboard stale-data cleanup (4 DOWN → 0 DOWN)**
   - Removed Visual Inventory :3003 (decommissioned)
   - Fixed AI Dev Dashboard port :3004 → :3025 (self-reference bug)
   - Removed LLM Gateway :8000 (source lost to APFS)
   - Started workspace-watchdog :3018
   - Updated SPRINT_STATUS + STORIES_DIR to Synapse/_bmad-output/

4. **Orchestrator port fix**
   - `ORCHESTRATOR_API` :3027 → :3028 in ai-dev-dashboard/server.py
   - Work tab's orchestrator metrics now working (was silently broken)

5. **Live activity balloons (NEW FEATURE)**
   - Schema: `current_activity` (≤120 chars) + `activity_started_at` + `activity_ttl_seconds` (default 60) on `workflow:<name>` heartbeat
   - Backend: cockpit `/api/team-activity` + ai-dev-dashboard `/api/bmad` TTL-check + expose
   - Frontend: `_bmadSpeechData` prioritizes live activity over Archon doing tasks
   - Protocol documented in CLAUDE.md: Claude writes `current_activity` when spawning Task sub-agents
   - Demo'd successfully with Scout, Sentinel, Nexus — balloons visible on :3025

6. **Sentinel fixes (post-QA)**
   - MED: Promote race condition → per-idea threading.Lock added. Verified 3 concurrent POSTs → 1 fresh + 2 idempotent, same task_id
   - LOW: `int()` placement → moved inside inner try in both dashboard + cockpit (one malformed heartbeat no longer wipes all activity)

7. **Speech bubble wrapper filter (BUG FIX)**
   - Cockpit was emitting raw `<task-notification>`, `<system-reminder>`, `<user-prompt-submit-hook>`, `<command-*>` XML from Claude's .jsonl as "Serge said..." text
   - Added `_strip_system_wrappers()` regex filter in cockpit server.py
   - Covers 10 wrapper tag types; unit-tested

---

## Sub-agent Work

**Scout (observability inventory)** — catalogued all 11 dashboards (cockpit, ai-dev-dashboard, claude-dashboard, workflow-panel, ai-supervisor, synapse-brain, neural-map, idea-flow, launcher, projects-viewer, minutes-dashboard). Produced duplication matrix, unique-contributions list, navigation graph, 4 data-source conflicts, 7 blind spots. Saved to `memory/project_dashboard_consolidation.md`.

**Sentinel (QA review)** — reviewed all 7 session changesets. 0 CRITICAL. 1 MED (race condition — fixed). 2 LOW (int() placement — fixed). 1 LOW (create_archon_task error masking — deferred as pre-existing).

**Nexus/Plan (merge architecture)** — designed 10-stage migration plan from ai-dev-dashboard :3025 → claude-cockpit :3027. Saved to `memory/project_dashboard_merge_plan.md`.

---

## Open Questions (for next session)

1. Debates tab: retire or migrate?
2. Tab bar placement in cockpit: under header or collapsed into chips?
3. Keep Ops as one tab or pre-split Sprint + Activity?
4. Shared-code extraction scope: cockpit-only or broader (ai-orchestrator, ai-supervisor, archon-client)?

---

## Rejected Ideas

- **Rebuilding workflow-panel Docker image** — rejected because src/ is empty. Rebuild would fail. Frozen container is the correct state.
- **Extracting minified JS bundle to recover src** — high effort, low fidelity. If container dies, rewrite from scratch is better.

---

## Next Session Priorities

1. **Stage 1 + 2** (tab shell + orchestrator metrics strip) — ~3-4h, zero risk
2. **Capture-api Supabase schema fix** — `public.ideas` table missing in local Supabase, blocks cross-restart idempotency
3. **Skip-candidate validation** — confirm debates/alert/agent-respond retire decisions before Stage 6

---

## Memory Updates

New memory files:
- `heartbeat_activity_schema.md` (reference)
- `project_dashboard_consolidation.md` (project — Scout's inventory)
- `project_workflow_panel_source_lost.md` (project)
- `project_dashboard_merge_plan.md` (project — Nexus's 10-stage plan)

Updated: `MEMORY.md` index + `CLAUDE.md` (heartbeat activity protocol).

---

*Session concluded 2026-04-04 18:47 — stop point agreed by Serge.*
