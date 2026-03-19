# Session Notes — 2026-03-13

## Context Recovery (Post Power Outage)

Services restored via `startidea`. All 10/10 online.

---

## Changes Made This Session

### Workspace Launcher (`Projects/launcher/`)

**`server.py`**
- Added `docker_running()` and `docker_container_count()` helpers
- Added `GET /api/docker/health` endpoint
- Added `POST /api/docker/start` endpoint
- Modified `POST /api/start-all` to wait for Docker (up to 30s) before calling `startidea`
- Removed dead `git-habit-tracker` service from SERVICES list

**`index.html`**
- Added `⬡ DOCKER:Nc` chip in header — green if running, red if not
- Added `fetchDockerHealth()` function
- Rewrote `runBoot()`: check Docker → start if offline → wait 30s → run startidea
- Added `on-hold` badge style (orange: `#ff9f43`)

### AI Dev Dashboard (`Projects/ai-dev-dashboard/index.html`)
- Added `on-hold` CSS badge style (orange `#ff9f43`)

### Sprint Status (`_bmad-output/implementation-artifacts/sprint-status.yaml`)
- Added `on-hold` to Story Status definitions
- Changed `avs-5-1-stripe-payment-integration` → `on-hold`
- Added `avs-arch-v2-update: in-progress` → now `done`

### Port Registry (`Documentation/System/PORT_REGISTRY.md`)
- Removed dead `3009 | git-habit-tracker` entry

---

## ADR Update — avs-arch-v2-update — COMPLETE ✓

### Files Written
- **NEW:** `_bmad-output/planning-artifacts/ai-venture-studio/architecture-v2.md`
- **UPDATED:** Original `architecture.md` — superseded notice prepended

### Quinn — Drift Report (completed earlier)

| Area | ADR v1 Said | Reality | Status |
|---|---|---|---|
| Core validation | ThreadPoolExecutor, Haiku/Sonnet split, TypedDicts | Same | VALID |
| Storage | Archon context keys, no new DB | Supabase primary (5 tables) | OUTDATED |
| Cache | SHA-256 + Archon storage | Supabase `val_cache` table | OUTDATED |
| Auth | Single user, local only | Supabase magic-link JWT | OUTDATED |
| Traction | Phase 3, out of scope | SHIPPED — SPK, 7 endpoints, dashboard | NEW |
| Enrichment pipeline | Not mentioned | Auto-enrich before 4-agent jury | NEW |
| Freemium | Not mentioned | FREE_VALIDATION_LIMIT=3, `_is_pro()`, UpgradeModal | NEW |
| Privacy NFR | All-local, private | Data in Supabase cloud | OUTDATED |

### Winston — Key Findings (verified against running code)

**Storage:**
- 5 Supabase tables confirmed in code: `ideas`, `val_cache`, `val_enrichment`, `traction_log`, `traction_recommendations`
- `validation_cache.db` still exists on disk but is now a no-op stub — not actively used
- All DB access goes through `lib/supabase_client.py` (6 helper functions)
- Archon context is a secondary best-effort mirror only

**Traction:**
- 7 endpoints total (was "out of scope" in v1)
- SPK Haiku agent, 24h background daemon, Pivot auto-creation, portfolio dashboard
- ⚠ Column name mismatch: Supabase stores `verdict`/`pivot_hint`; API returns `recommendation`/`pivot_suggestion` via backward-compat mapping

**Auth:**
- Magic-link OTP via `LoginView.jsx` → Supabase JS client
- JWT validated in `lib/auth.py` with dev pass-through when `SUPABASE_JWT_SECRET` not set
- ⚠ Only 4 routes currently protected (`@require_auth`); traction/enrichment/roadmap routes are NOT

**New agents since v1:**
- Enrichment agent (Haiku, auto-runs before validation)
- Pivot Planner (Sonnet, Archon-cached)
- GO Roadmap (Sonnet, val_cache-stored)
- SPK traction agent (Haiku — hardcoded string, should use `HAIKU_MODEL` constant)

**Not yet verified / gaps:**
- `user_profiles` table — referenced in project memory (AVS-5.2) but NOT found in any Python file
- RLS policy definitions — described in Supabase PRD but **no migration files exist** in repository

### Moira — Scope Summary

**AVS is:** Solo-founder operating brain. Idea → 4-agent validation gate → GO/NO-GO/PIVOT → BMAD build pipeline → traction feedback loop (Scale/Pivot/Kill).

**Key open question:** Multi-tenant SaaS (one Supabase project + RLS) vs. single-tenant (one Docker per founder)? Current implementation assumes **multi-tenant**. ADR v2 makes this explicit.

---

## AVS-5.6 — Auth Route Hardening — COMPLETE ✓

- `@require_auth` added to 10 previously unprotected routes in `api_server.py` + `api_server_validator.py`
- Hardcoded model strings replaced with `CLAUDE_HAIKU_MODEL` constant
- API server restarted

## AVS-5.7 — RLS Migrations — COMPLETE ✓

- `supabase/migrations/` created from scratch
- 5 migration files written and pushed via `supabase db push`
- Tables with RLS enabled: `ideas`, `val_cache`, `val_enrichment`, `traction_log`, `traction_recommendations`
- `validation_usage` table does not exist — usage tracked via local JSONL (no-op migration added)
- **Schema reality**: tables have no `user_id` column (single-tenant). RLS blocks anon-key access; service role key bypasses RLS (backend unaffected).
- `architecture-v2.md` updated to reflect RLS applied + schema gap noted

## Sprint 16 — Epic 6.1: Multi-Tenant Foundation — COMPLETE ✓ (2026-03-13)

### AVS-6.4 — Remove legacy cache
- `validation_cache.db` deleted (815KB)
- Dead constants removed from `api_server.py`, `api_server_validator.py`, `Dockerfile.backend`, `docker-compose.yml`

### AVS-6.5 — Anthropic retry policy
- `_call_claude()` helper added with 3-retry exponential backoff (1s/2s/4s)
- 8 call sites replaced across `api_server_validator.py`
- `httpx.Timeout(60.0)` applied to Anthropic client
- Catches: RateLimitError, APIConnectionError, InternalServerError

### AVS-6.1 — user_id schema
- `user_id TEXT` column added to all 5 tables: `ideas`, `val_cache`, `val_enrichment`, `traction_log`, `traction_recommendations`
- RLS policies updated: `auth.uid()::text = user_id`
- `get_current_user_id()` added to `lib/auth.py`
- 8 write operations in `api_server.py` + `api_server_validator.py` inject `user_id`
- 4 migrations pushed via `supabase db push`

### AVS-6.2 — user_profiles
- `user_profiles` table created: `user_id, plan, validations_this_month, month_reset_at`
- Freemium gate (`_count_validations_this_month`, `_is_pro`) migrated from JSONL to Supabase
- JSONL fallback retained for dev pass-through
- `_increment_validation_count()` called after each real (non-cached) validation run
- `POST /api/admin/set-pro` endpoint added (requires `X-Service-Key` header)

### Remaining open items
- [ ] AVS-6.3 Stripe integration (on-hold — waiting for keys)
- [ ] API server restart required after these changes (done: `api_server.py` restarted 2026-03-13)
