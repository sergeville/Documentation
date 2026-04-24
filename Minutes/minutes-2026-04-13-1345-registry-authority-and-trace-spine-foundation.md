# Minutes — 2026-04-13 12:52–13:45
## Registry Authority + Trace Spine Foundation

**Attendees:** Serge, Codex
**Duration:** ~53 minutes
**Workspace:** `~/Dev/Synapse/`
**Branch:** main (local working tree)

---

## Session Summary

**Completed the decision-grade Synapse architecture package, approved and materialized the ADR/epic/story planning artifacts, implemented the first two foundation stories, and established the exact next execution order for runtime adoption.**

The session moved in three phases:
- architecture clarification and canonical surface decisions
- planning artifact creation for Epic 59
- implementation of Story 59-1 and Story 59-3 foundations

No runtime producer wiring or cockpit trace UI was started yet. Launcher/nav derivation work was identified as the next active implementation step.

---

## Phase 1: Architecture Decision Package

### Outputs created
- `~/Dev/Synapse/docs/architecture-package-2026-04-13.md`

### Hard decisions captured
- `tool-registry.json` becomes the single source of truth for surface inventory, lifecycle state, retired markers, and operator navigation eligibility
- canonical active operator surfaces are `launcher`, `claude-cockpit`, and `idea-flow`
- canonical active runtime authorities are `Archon`, `ai-orchestrator`, and `ai-supervisor`
- `claude-dashboard` and `claude-inbox` should merge into `claude-cockpit`
- `ai-dev-dashboard`, `workflow-panel`, and `workspace-hub` are retired/legacy and should not remain first-class destinations
- a unified trace spine is required so cockpit can show one operator narrative from idea through execution result

---

## Phase 2: ADRs, Epic, and Stories Approved

### Outputs created
- `~/Dev/Synapse/docs/adr/ADR-001-registry-authority.md`
- `~/Dev/Synapse/docs/adr/ADR-002-trace-spine-schema.md`
- `~/Dev/Synapse/_bmad-output/implementation-artifacts/epic-59-registry-authority-and-trace-spine.md`
- `~/Dev/Synapse/_bmad-output/implementation-artifacts/stories/59-1-registry-authority-schema.md`
- `~/Dev/Synapse/_bmad-output/implementation-artifacts/stories/59-2-launcher-and-nav-derive-from-registry.md`
- `~/Dev/Synapse/_bmad-output/implementation-artifacts/stories/59-3-trace-spine-schema.md`
- `~/Dev/Synapse/_bmad-output/implementation-artifacts/stories/59-4-trace-aware-audit-and-read-contract.md`

### Execution order approved
1. Story `59-1` — registry authority schema
2. Story `59-3` — trace spine schema (parallel-safe foundation)
3. Story `59-2` — launcher + nav derive from registry
4. Story `59-4` — trace-aware audit/read contract

---

## Phase 3: Story 59-1 Implemented

### Files changed
- `~/Dev/Synapse/tool-registry.json`
- `~/Dev/Synapse/scripts/validate_tool_registry.py`
- `~/Dev/Synapse/docs/TOOL_REGISTRY_SCHEMA.md`

### What changed
- `tool-registry.json` was upgraded to `registry-authority-v1`
- every registry entry now carries explicit authority fields:
  - `owner`
  - `canonical`
  - `operator_visible`
  - `lifecycle`
  - `replacement`
  - `nav_group`
  - `managed_by_launcher`
- missing core surfaces were added to the registry:
  - `idea-flow`
  - `ai-idea-analyst`
  - `synapse-docs`
  - `neural-map`
  - `archon-ui`
- a validation script now checks lifecycle integrity, replacement integrity, and required core coverage

### Validation completed
- `python3 scripts/validate_tool_registry.py`
- `python3 -m json.tool tool-registry.json >/dev/null`
- `python3 -m py_compile scripts/validate_tool_registry.py`

All passed.

---

## Phase 4: Story 59-3 Implemented

### Files changed
- `~/Dev/Synapse/archon/migrations/0005_epic_59_trace_spine.sql`
- `~/Dev/Synapse/docs/TRACE_SPINE_SCHEMA.md`

### What changed
Added the first canonical trace-spine schema for idea-to-execution delivery branches.

### Table introduced
- `public.archon_work_item_traces`

### Core fields included
- `trace_id`
- `root_trace_id`
- `parent_trace_id`
- `idea_id`
- `plan_id`
- `story_id`
- `file_path`
- `archon_task_id`
- `decision_id`
- `assigned_agent`
- `agent_run_id`
- `workflow_stage`
- `status`
- `created_at`
- `updated_at`
- `started_at`
- `completed_at`
- `terminal_result`
- `error_summary`
- `links_to_artifacts`

### Lineage support included
- `root`
- `supersedes`
- `replaces`
- `parallel`
- `derived_from`

### Important note
The migration file was created and reviewed, but **not applied to a live database in this session**.

---

## Phase 5: Current Start on Story 59-2

Story `59-2` was identified as the next active work item.

### First seam chosen
Start with launcher-derived registry/navigation APIs, then move the shared navigation bar to consume that authority instead of relying on hardcoded surface lists.

### Constraint observed
`launcher/server.py` and `launcher/packages/design-system/synapse-nav.js` already had uncommitted changes in the working tree, so the next implementation step must extend those edits carefully rather than overwrite them.

---

## Key Decisions

1. **Do cleanup before new capability.**
   Registry authority and trace schema foundations come before cockpit UI or producer wiring.

2. **Keep one source of truth for topology.**
   `tool-registry.json` owns inventory truth; runtime health belongs elsewhere.

3. **Keep one source of truth for current trace state.**
   `archon_work_item_traces` should become the operator read model; `unified_audit_log` stays append-only history.

4. **Do not merge timelines across branches.**
   One idea may produce multiple trace branches; cockpit must show lineage instead of silently blending them.

5. **Treat Story 59-2 as the next safest active implementation step.**
   The data contract now exists; launcher and nav should start consuming it before deeper producer wiring.

---

## Files Created This Session

### Planning and architecture
- `~/Dev/Synapse/docs/architecture-package-2026-04-13.md`
- `~/Dev/Synapse/docs/adr/ADR-001-registry-authority.md`
- `~/Dev/Synapse/docs/adr/ADR-002-trace-spine-schema.md`
- `~/Dev/Synapse/_bmad-output/implementation-artifacts/epic-59-registry-authority-and-trace-spine.md`
- `~/Dev/Synapse/_bmad-output/implementation-artifacts/stories/59-1-registry-authority-schema.md`
- `~/Dev/Synapse/_bmad-output/implementation-artifacts/stories/59-2-launcher-and-nav-derive-from-registry.md`
- `~/Dev/Synapse/_bmad-output/implementation-artifacts/stories/59-3-trace-spine-schema.md`
- `~/Dev/Synapse/_bmad-output/implementation-artifacts/stories/59-4-trace-aware-audit-and-read-contract.md`

### Foundation implementation
- `~/Dev/Synapse/scripts/validate_tool_registry.py`
- `~/Dev/Synapse/docs/TOOL_REGISTRY_SCHEMA.md`
- `~/Dev/Synapse/archon/migrations/0005_epic_59_trace_spine.sql`
- `~/Dev/Synapse/docs/TRACE_SPINE_SCHEMA.md`

---

## Next Session Priorities

1. Finish Story `59-2`
   - make launcher inventory derive from `tool-registry.json`
   - add a registry-derived navigation API
   - move shared nav to consume registry-driven operator-visible surfaces

2. Apply and verify migration `0005_epic_59_trace_spine.sql`
   - run Archon migration status/apply
   - verify the new table and indexes exist cleanly

3. Start Story `59-4`
   - add trace-aware read contract in Archon
   - define how audit rows carry `trace_id` metadata without breaking existing consumers

4. After that, wire producer writes
   - `idea-capture-web`
   - `idea-flow`
   - validation council
   - orchestrator
   - agent work orders

5. Only then build the cockpit unified trace view

---


## Addendum — 2026-04-13 13:45–14:20

### Story 59-2 progress
- launcher inventory, launch resolution, `/api/tools`, `/api/navigation`, and `/api/status` metadata now derive from `tool-registry.json`
- shared nav now fetches launcher-provided navigation instead of relying only on hardcoded surface entries
- launcher UI now renders lifecycle and canonical registry state instead of a one-off retired dashboard filter

### Migration 0005 status
- `0005_epic_59_trace_spine.sql` was applied inside `archon-archon-server-1`
- migration runner now reports `applied: 5`, `pending: 0`
- database verification confirmed:
  - schema migration row exists for `0005_epic_59_trace_spine`
  - `public.archon_work_item_traces` exists with the expected 22 columns

### Story 59-4 started
- `POST /api/audit` now accepts optional trace-related fields and copies them into audit metadata
- `GET /api/traces` added for trace lookup
- `GET /api/traces/{trace_id}` added for canonical trace + lineage reads
- Archon main app now includes the trace router
- live verification passed after Archon restart:
  - `GET /api/traces?limit=1` returns `200`
  - `GET /api/audit?trace_id=...` returns `200`
  - invalid trace ids now return `422` instead of `500`

### Updated next order
1. browser-verify and close Story `59-2`
2. restart/verify Archon live routes for Story `59-4`
3. wire trace producers
4. build cockpit unified trace view
5. consolidate legacy surface exposure after parity is proven

## Handoff Note

If context gets tight, resume from this order:
1. finish `59-2`
2. apply/verify `0005`
3. implement `59-4`
4. wire producers
5. build cockpit trace UI

## Addendum — 2026-04-13 23:05–23:44

### Trace producer wiring started
- `idea-capture-web/services/archon.py` now creates or updates a canonical Archon trace row for an idea and stores `trace_id` inside `capture-api:idea-state:<idea_id>`
- `idea-capture-web/routes/ideas.py` now returns `trace_id` on idea creation and includes it in the initial `idea.captured` audit metadata
- `idea-flow/server.py` now writes trace transitions for:
  - council pending / blocked states during story approval
  - auto-gated idea-to-task promotion
  - story approval, including story file and Archon task links
- `archon/python/src/agent_work_orders/models.py` now accepts optional `trace_id`, `idea_id`, `plan_id`, `story_id`, and `archon_task_id`
- `archon/python/src/agent_work_orders/api/routes.py` now propagates trace metadata into council requests, AWO audits, and trace status transitions for blocked, pending-human, run-started, run-completed, and run-failed work-order states

### Trace API expanded
- `archon/python/src/server/api_routes/trace_api.py` now supports:
  - `POST /api/traces`
  - `PATCH /api/traces/{trace_id}`
  - existing read routes remain in place
- the initial implementation assumed `uuid.uuid7()` existed everywhere; this failed in the live Archon container
- compatibility fallback was added so trace creation now uses `uuid7` when available and `uuid4` otherwise

### Audit contract repaired
- live verification exposed that `POST /api/audit` was writing `description` and `project` columns that do not exist in `public.unified_audit_log`
- `archon/python/src/server/api_routes/audit_api.py` was corrected to normalize `description` and `project` into `metadata` and to filter `project` from metadata on reads

### Live verification completed
- Archon container restarted successfully after the trace and audit changes
- live API verification passed for:
  - `POST /api/traces`
  - `PATCH /api/traces/{trace_id}`
  - `GET /api/traces/{trace_id}?include_audit=true`
  - `POST /api/audit`
  - `GET /api/audit?trace_id=...`
- synthetic trace verification confirmed:
  - artifact links merge correctly across patch updates
  - lineage reads still work
  - trace-linked audit entries now appear in trace detail reads

### Updated next order
1. browser-verify and close Story `59-2`
2. finish remaining producer gaps in validation council and `ai-orchestrator`
3. build the cockpit unified trace view on top of the now-live trace writer/read contract
4. consolidate legacy surface exposure after parity is proven

## Addendum — 2026-04-13 Current State Snapshot

### Commit split completed
The runtime and architecture work from this session is now preserved as four scoped commits instead of one mixed change:

1. `dec4342` — `Establish launcher execution authority contract`
2. `652fb59` — `Add canonical trace spine and producer wiring`
3. `b55c5c7` — `Align topology views with canonical surfaces`
4. `fd1973b` — `Decouple boardroom standup from retired dashboard`

### What is now true
- launcher inventory, navigation, and control behavior are contract-backed through `tool-registry.json` + `launcher-execution.json`
- CI now validates both registry authority and launcher execution authority
- the canonical trace spine exists in Archon and producer wiring now reaches capture, story approval, agent work orders, and orchestrator story context resolution
- static topology views now reflect the current canonical Synapse surface model instead of retired surfaces
- `voice-boardroom` standup no longer depends on retired `ai-dev-dashboard`

### Validation completed across the session
- `python3 scripts/validate_tool_registry.py`
- `python3 scripts/validate_runtime_contracts.py`
- launcher endpoint smoke tests for `/api/status`, `/api/services`, `/api/tools`, `/api/navigation`, `/api/contracts/validation`
- `python3 -m py_compile` on the touched runtime modules
- `pytest ai-orchestrator/test_orchestrator.py` -> 61 passed
- `pytest idea-capture-web/test_api_server.py` -> 29 passed

### Remaining uncommitted items
The repo work is functionally split and committed. What remains outside git is documentation/planning residue only:
- `docs/adr/ADR-001-registry-authority.md`
- `_bmad-output/implementation-artifacts/stories/59-1-registry-authority-schema.md`
- `_bmad-output/implementation-artifacts/stories/59-2-launcher-and-nav-derive-from-registry.md`
- `docs/architecture-package-2026-04-13.md`
- local prompt / handoff files (`synapse-decision-pass.prompt.md`, `synapse-master-prompt.md`, local `AGENTS.md`)

### Resume point
If work resumes from here, the safest next move is a docs-only commit for the remaining registry-authority architecture records. After that, the workspace is clean enough to either push the Epic 59 foundation chain or start the cockpit trace UI on top of the committed trace/read contracts.

