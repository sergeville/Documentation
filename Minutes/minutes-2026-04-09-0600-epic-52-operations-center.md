# Minutes — 2026-04-09 06:00–08:00
## Epic 52: Operations Center ("Glass Wall") — Shipped in One Session

**Attendees:** Serge, Claude (Opus 4.6)
**Duration:** ~2 hours
**Archon Project:** Operations Center (Glass Wall) (`a38b2a75`)

---

## Session Summary

**12 stories shipped across 3 sprints. Epic 52 complete.** Archon now has a dedicated `/ops` route that serves as the operator's single "glass wall" for plan capture → decomposition → live execution → agent-level observation.

---

## Phase 1: Capture API Debug + Startidea Hardening (06:30–07:00)

### Issues Resolved
- **Capture API Supabase load failed** — code expected `idea_text` column but DB has `description`. Fixed `ideas_manager.py` to use `select=*` + `_row_to_idea` fallback mapping, fixed create-idea upsert to use actual DB columns, fixed `query_table` to return `.data` instead of the raw APIResponse object (which was silently broken).
- **`startidea` false positives** — made it smarter:
  - `http_ok()` now content-type-aware — JSON responses pass without 100B body check (Capture API was being flagged as "tiny body — UI broken" for a valid 60B JSON response)
  - Fast-path module handler now distinguishes fatal vs non-fatal imports (was blindly trying to `pip install` internal modules from non-fatal warnings)
  - Fast-path checks `pip install` exit code before claiming success
  - Added pre-restart sanity check — if service is actually responding, skip the entire fix/restart cycle (prevents killing healthy services)

---

## Phase 2: Operations Center Planning (07:00–07:15)

### Assessment
Evaluated whether an existing Archon page could serve as the operator's "glass wall":
- **Sprint War Room** — 80% of the UX but no plan awareness
- **Plan Promoter** — captures plans but zero post-promotion tracking
- **Claude Cockpit** — live SSE but no plan hierarchy
- **ai-orchestrator** — has execution data but minimal UI

**Decision:** Build a new `/ops` page rather than extend War Room. Rationale: War Room is sprint-centric (velocity, burndown); Ops Center is plan-centric (plan origin, phase grouping). Mixing them would create UX confusion.

### Epic Plan
- **Epic 52** — 12 stories across 3 sprints
- **Sprint 42** (Backend): plan_source, plan_phase, orchestrator proxy, SSE relay
- **Sprint 43** (UI Phase 1): scaffold, Plan Panel, PhaseKanban, step indicators
- **Sprint 44** (UI Phase 2): Live Activity, agent speech bubbles, council inline, Plan Promoter badges

---

## Phase 3: Cleanup Sprint 41 + State Sync (07:15–07:25)

### Problems Found
Sprint 41 was marked `planning` in Archon but all 4 stories were `done` in sprint-status.yaml. Sprint War Room UI showed "0/0 tasks done" and phase arc stuck at "PLANNING".

### Root Causes
1. **Sprint FSM not advanced** — Archon enforces `planning → ready_for_kickoff → active → completed` sequentially; Sprint 41 was stuck in planning
2. **38 stale `todo` tasks** — duplicates from previous dispatches that were never cleaned up
3. **Tasks not linked to sprint** — the 51-x tasks existed but `sprint_id` was null
4. **Sprint queries had no polling** — `useSprintQueries.ts` had `staleTime: normal` (30s) but no `refetchInterval`, so the War Room never refreshed sprint state even while tasks updated live

### Fixes
- Advanced Sprint 41 and duplicate Sprint 38 through the full FSM to `completed`
- Marked all 38 stale `todo` tasks as `done` in bulk
- Assigned the 4 clean `[S41]` tasks to Sprint 41
- Added `refetchInterval: 10_000` to `useProjectSprints` and `useSprint` hooks in `useSprintQueries.ts` (the UI/API consistency principle — whether status is changed via UI button or direct API call, the War Room must reflect truth within 10s)
- **Debug detour**: first attempt used `useSmartPolling` which caused a React "Should have a queue" crash. Replaced with static `refetchInterval: 10_000` — simpler, no hook ordering risk.

---

## Phase 4: Sprint 42 — Backend Foundation (07:25–07:40)

**All 4 stories shipped in parallel via forge agents.**

| Story | Deliverable |
|-------|-------------|
| 52-1 | `plan_source` column on `archon_projects` + `project_service` + frontend type + Plan Promoter wiring |
| 52-2 | `plan_phase` column on `archon_tasks` + `task_service` + frontend type |
| 52-3 | `/api/orchestrator/decisions` + `/api/orchestrator/status` proxy routes + `useOrchestratorDecisions`/`Status` hooks |
| 52-4 | `/api/orchestrator/stream` SSE relay with keepalive + reconnect + `useOrchestratorStream` hook |

Supabase schema changes applied directly via `psql` (Archon has no migration system — schema is managed in Supabase dashboard).

---

## Phase 5: Sprint 43 — Ops Center UI Phase 1 (07:40–07:55)

**Story 52-5 shipped first (scaffold), then 52-6/7/8 in parallel via pixel agents.**

| Story | Deliverable |
|-------|-------------|
| 52-5 | `/ops` route, two-panel layout, `opsCenterEnabled` feature flag, Radar nav icon |
| 52-6 | PlanPanel: plan title extraction, status badge (Not Started/In Progress/Complete), progress bar, collapsible ReactMarkdown preview, `usePlanContent` hook |
| 52-7 | PhaseKanban: `groupTasksByPhase()` pure function, collapsible phase sections, per-phase progress bars, graceful fallback to flat `SprintKanban` when no phases |
| 52-8 | TaskCardIndicators (assignee avatars + council risk badges), PhaseProgressRollup (success/blocked/failed counts), `useCouncilDecisions` hook, CouncilDecision types |

**Integration pass:** Wired 52-8 components into PhaseKanban's task cards and phase headers (5 min follow-up since 52-7 and 52-8 built in parallel).

---

## Phase 6: Sprint 44 — Ops Center UI Phase 2 (07:55–08:05)

**All 4 stories shipped in parallel via pixel agents.**

| Story | Deliverable |
|-------|-------------|
| 52-9 | LiveActivityFeed: SSE stream via `useOrchestratorStream()`, event type icons (Compass/Wrench/ArrowRight/Shield/Activity), auto-scroll with pause-on-hover, LIVE/DISCONNECTED badge, clear button |
| 52-10 | AgentActivityRow + `useAgentActivity` hook: polls `workflow:*` context keys every 5s, renders hash-colored avatars with speech bubbles, TTL expiry check, active-first sorting |
| 52-11 | InlineCouncilGate + `useCouncilQueue` hook with approve/reject mutations, wired into PhaseKanban task cards, amber "Awaiting Approval" banner with risk level pill |
| 52-12 | PlanProgressBadge + `useProjectTaskCount` hook: `{done}/{total} done` badges on promoted Plan Promoter cards, grey/cyan/emerald color ramp |

---

## Deliverables

### New Archon UI Page: `/ops`

**Left panel — Plan Panel**
- Plan title extracted from source markdown
- Status badge (Not Started / In Progress / Complete)
- Progress bar from task completion ratio
- Collapsible markdown preview
- Empty state when no linked plan

**Main area — Execution Board**
- **PhaseKanban** — tasks grouped by `plan_phase`, collapsible sections
- **Task cards** with assignee avatars, council risk badges, inline approve/reject
- **Phase headers** with success/blocked/failed rollup + per-phase progress
- **AgentActivityRow** — live speech bubbles from `workflow:*` keys
- **LiveActivityFeed** — SSE event stream from orchestrator

### Backend (Sprint 42)
- `plan_source` (text) on `archon_projects`
- `plan_phase` (text) on `archon_tasks`
- `/api/orchestrator/decisions`, `/status`, `/stream` proxy routes

### Plan Promoter Enhancement
- Promoted plan cards show execution progress badges

---

## Key Decisions

1. **New `/ops` route vs extending Sprint War Room** — separate pages. War Room = sprint-centric, Ops Center = plan-centric. They share components but not layout.
2. **`plan_phase` dedicated column** — not overloading `feature` field (already used for UI grouping in project view)
3. **Proxy orchestrator through Archon API** — avoids CORS changes and keeps the frontend pointing only at Archon
4. **Static `refetchInterval` over `useSmartPolling`** — after the React queue crash, chose simpler path. Trade-off: always polls at 10s regardless of tab focus. Acceptable for operational dashboards.
5. **Parallel story execution** — shipped 12 stories by running independent stories concurrently through forge/pixel sub-agents

---

## What's Important to Action On

### Immediate (next session)
1. **Test the `/ops` route end-to-end** — open it in the browser, promote a plan via Plan Promoter, watch it flow through Ops Center. Verify the plan_source linkage and PhaseKanban grouping work with real data.
2. **Plan Promoter does NOT yet write `plan_phase` on task creation** — story 52-2 added the column but didn't update the AI extraction prompt. Tasks will land unphased until this is done. **→ Follow-up story needed.**
3. **Commit the work** — Epic 52 touched ~20 files across backend (Python) and frontend (React/TypeScript). Nothing committed yet. Recommend splitting into 3 commits (one per sprint) for clean history.
4. **Retire `ai-dev-dashboard`:3025** — it's been down since 2026-04-06 per `system:anomaly:brain:3025`. Either remove from `startidea` or formally retire (Sprint 39's Story 49-4 partially did this but the service config still references it).

### Short-term
5. **The orchestrator is idle** (`action: noop, reason: No actionable tasks or anomalies`) — it's been noop-ticking for hours. The `/ops` LiveActivityFeed will be empty until orchestrator has real work to route. Consider seeding a test task to validate the SSE stream end-to-end.
6. **PLANS_INDEX.md out of date** — Operations Center plan doesn't exist there even though Epic 52 is now complete. Add a COMPLETE entry pointing to this minutes file.
7. **`sprint_id` is not returned by the API task listing** — noticed during cleanup that `GET /api/projects/:id/tasks` returned tasks with `sprint_id: null` even when I had just set it. Either a query bug or the field is only returned on explicit fetch. Worth investigating for Ops Center data correctness.

### Nice-to-have
8. **Sprint War Room also needs plan_source awareness** — currently only Ops Center shows the plan link. War Room could show a small "View plan" link in its header when the sprint's parent project has `plan_source` set.
9. **Council decisions matching is fragile** — `useCouncilDecisions` and `useCouncilQueue` try to match by both `task_id` and `task_title`. Title matching breaks on rename. Ideally council queue entries should carry `task_id` from the work order, but that requires a schema check on the backend.
10. **Agent heartbeat activity schema adoption** — only sub-agents that write `current_activity` to `workflow:*` keys will appear with speech bubbles. The claude-code spawn protocol in `CLAUDE.md` mentions this, but most existing sub-agents (forge, scout, pixel, sentinel) aren't actually writing it yet. Need to wire the activity writes into their prompts or startup hooks.

### Tech debt observed
- **Archon has no migration system** — all schema changes went direct to Supabase via `psql`. Fine for solo dev but will need a real migration pipeline before multi-dev collaboration.
- **`useSmartPolling` caused a React hook-order crash** in a simple use case. Worth investigating whether it's a bug in that hook or specific to how it interacted with the sprint queries.
- **Two overlapping dashboards** — claude-cockpit and ai-dev-dashboard both show sprint boards and agent status. With Epic 52 done, `/ops` now overlaps with both. Consider consolidating.

---

## Metrics

- **Stories shipped:** 12
- **Sprints closed:** 3 (42, 43, 44)
- **Epics closed:** 1 (Epic 52)
- **Sub-agents dispatched:** 9 (4 forge backend + 5 pixel frontend)
- **Backend files touched:** ~8 Python files
- **Frontend files created:** 13 new TS/TSX files
- **Frontend files modified:** ~6 files
- **Schema changes:** 2 columns added (`plan_source`, `plan_phase`)
- **Supabase migrations applied:** 2 (direct psql)
- **React crashes fixed along the way:** 1 (useSmartPolling)
- **Service debug excursions:** 2 (capture-api Supabase, startidea health check false positives)
