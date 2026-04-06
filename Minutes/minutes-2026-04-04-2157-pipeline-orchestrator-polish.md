# Session Minutes — 2026-04-04 21:57 → 22:10
## Idea Pipeline Filter + Orchestrator Stuckness Guards

**Agent:** Claude (orchestrator, Opus 4.6)
**Duration:** ~13min
**Sub-agents spawned:** none

---

## Decisions Made

1. **Orchestrator reconciliation strategy** — existing code already prunes `active_orders` when tasks leave "doing", but that misses the stuck-in-doing failure mode (worker crashed, task never moves). Added age-based slot eviction (30min default) at the orchestrator side, plus supervisor-side watchdog as defense in depth.
2. **Watchdog signals** — three independent detectors chosen:
   - Tick-stall (30min) — orchestrator process alive but loop hung
   - Frozen active_orders (45min) — workers silent / dispatched but no churn
   - LLM fail streak (3 consecutive) — credential/rate-limit problem
3. **Severity routing** — tick-stall + LLM-fail → HIGH (macOS notification), frozen-slots → MEDIUM (dashboard only).

---

## Shipped (4 commits)

| Commit | Description |
|---|---|
| `464396c` | `fix(idea-flow)`: idea-0096 — `[Idea]` prefix filter applied to backlog/doing/shipped (was only on backlog) — dev stories no longer leak into executing slot or shipped column |
| `faba358` | `feat(orchestrator)`: release work-order slots after 30min (MAX_ORDER_AGE_SEC). Shape change: `active_orders[tid] = {oid, dispatched_at}`. 52/52 tests pass. |
| `5b07020` | `feat(supervisor)`: `check_orchestrator_health()` — 30min tick stall + 45min frozen-slots anomalies, auto-resolve on recovery |
| `7fbaa74` | `feat(supervisor)`: extend watchdog with LLM-fail-streak detector (3 consecutive) → HIGH anomaly pointing at `ANTHROPIC_API_KEY` |

---

## Issues Discovered

- **`ANTHROPIC_API_KEY` in macOS Keychain is invalid** (401 from Anthropic since ~22:03). Orchestrator has been skipping every tick with "LLM routing failed". New watchdog caught it and fired a HIGH macOS notification within 3 scans as designed. **Action pending:** Serge renews key, updates Keychain, restarts orchestrator.

---

## Rejected Ideas / Non-Goals

- Did NOT auto-restart the orchestrator on LLM-fail-streak — credential renewal is a human action; auto-restart would just re-hit 401.
- Did NOT add rate-limit backoff to orchestrator's LLM caller — out of scope for this session; current 60s tick cadence is already gentle.

---

## Carry-forward (remaining priorities from `project_next_session_priorities.md`)

4. JSONL watcher agent detection (offset restart issue)
5. BMAD panel name mapping (PM → Nina, UX → Karen)
6. Sam's stale escalation bubble
7. Extract TEAM_ROSTER to shared source
8. Remove `[AI Agents]` debug console.log

---

*Logged 2026-04-04 22:10*
