# Minutes — 2026-04-12 08:10–09:02
## Home Manifest + Archon Backup Hardening + Documentation Security Pass

**Attendees:** Serge, Codex
**Duration:** ~52 minutes
**Workspace:** `~/Dev/Synapse/` + `~/Documents/Documentation/`
**Branch:** main (local working tree)

---

## Session Summary

**Built a workspace-level documentation entry point, hardened Archon backup redundancy, added human-readable recovery guidance, linked all new docs into the main repo navigation, and created a repeatable documentation secret scan.**

The session started as a project-summary request and expanded into workspace information architecture and operational resilience. The key outcomes were: a new `HOME_MANIFEST.md` for navigating the broader `~/` workspace, a safer multi-copy Archon backup strategy, plain-language backup docs for non-technical users, explicit links from Synapse entry docs to all new materials, and a reusable docs secret-scan script that currently reports no likely live secrets in the scanned documentation paths.

---

## Phase 1: Project Resume and Ecosystem Summary

Created a consolidated Synapse project summary and then expanded it after reviewing adjacent workspace material.

### Output created
- `~/Dev/Synapse/PROJECT_RESUME.md`

### What it now covers
- Synapse goals, architecture, features, and current maturity
- integration of `~/Documents/Documentation/` context
- integration of `~/Dev/FactoriesProjects/` as an external but real dependency of the Synapse boardroom/factory model
- clarification that `mempalace` is adjacent and potentially useful, while `Attention-Residuals` is not part of Synapse runtime

### Key conclusion
`FactoriesProjects` materially belongs in the effective Synapse ecosystem. `mempalace` is a candidate for selective integration. `Attention-Residuals` remains research-only.

---

## Phase 2: Workspace-Level Manifest

Created a home-level manifest to serve as the entry point for the broader workspace instead of forcing users to guess which repo or documentation root to start from.

### Output created
- `~/Documents/Documentation/HOME_MANIFEST.md`

### What it includes
- major roots under `~/`
- “start by task” navigation
- critical systems section
- safety and recovery entry points
- pointers to repo-level manifests, READMEs, and documentation indexes

### Linked from
- `~/Documents/Documentation/Readme.md`
- `~/Documents/Documentation/DOCUMENTATION_INDEX.md`
- `~/Dev/Synapse/README.md`
- `~/Dev/Synapse/MANIFEST.md`

### Additional improvement
Minutes were promoted from indirect inclusion to a first-class navigation target in the workspace documentation structure.

---

## Phase 3: MemPalace Fit Assessment

Evaluated whether `mempalace` and `Attention-Residuals` should influence Synapse.

### Conclusion
- `mempalace`: good fit as a **complementary long-term memory layer**, not a replacement for Archon
- `Attention-Residuals`: not a product fit for Synapse at this stage

### Output created
- `~/Dev/Synapse/docs/MEMPALACE_INTEGRATION_PROPOSAL.md`

### Recommended architecture split
- Archon remains live operational truth
- MemPalace would hold durable historical/session memory

---

## Phase 4: Archon Backup Hardening

This was the most operationally critical part of the session.

### Problem statement
Serge explicitly stated that losing the Archon knowledge base again is unacceptable.

### File modified
- `~/Dev/Synapse/ai-supervisor/archon-backup.sh`

### What changed
The backup process no longer relies on a single dump in a single place.

New behavior:
- creates **three backup artifacts** per run:
  - custom dump
  - plain SQL gzip
  - globals export
- writes a manifest with checksums
- copies to multiple backup target roots
- verifies each target by checksum
- writes `latest.*` copies for quick restore
- fails hard if the required number of verified backup targets is not reached

### Default verified target policy now
- primary: `~/Documents/Archive/archon-backups`
- secondary: `~/.codex/memories/archon-backups`
- minimum required verified targets: `2`

### Validation
- shell syntax check passed with `bash -n`
- live backup / restore was not run in this session

---

## Phase 5: Backup Documentation

Created both technical and non-technical documentation for the new backup policy.

### Outputs created
- `~/Dev/Synapse/docs/ARCHON_BACKUP_AND_RECOVERY.md`
- `~/Dev/Synapse/docs/ARCHON_BACKUP_GUIDE_FOR_HUMANS.md`

### Purpose split
- `ARCHON_BACKUP_AND_RECOVERY.md` explains the technical strategy, artifact types, target roots, verification, and restore logic
- `ARCHON_BACKUP_GUIDE_FOR_HUMANS.md` explains in plain language why multiple backups matter and how a non-technical user can confirm the system is healthy

### Key message preserved in plain English
**One copy is not a backup.**

---

## Phase 6: Documentation Linking and Discoverability

One concern raised during the session was that newly created docs can become orphaned if they are not linked from the main entry points.

### Files updated
- `~/Dev/Synapse/README.md`
- `~/Dev/Synapse/MANIFEST.md`
- `~/Dev/Synapse/docs/SYNAPSE_MASTER_DOCUMENT.md`
- `~/Documents/Documentation/Readme.md`
- `~/Documents/Documentation/DOCUMENTATION_INDEX.md`

### Result
New documents are now discoverable from:
- Synapse repo root docs
- Synapse master narrative docs
- Documentation folder entry points
- the new workspace-level manifest

---

## Phase 7: Documentation Secret Scan

Added a repeatable scan so documentation safety is not dependent on a one-time manual review.

### Outputs created
- `~/Dev/Synapse/scripts/scan-docs-secrets.sh`
- `~/Dev/Synapse/docs/DOCS_SECRET_SCAN.md`

### What it does
Scans documentation-heavy paths for likely real secrets such as:
- API keys
- GitHub tokens
- AWS keys
- private key blocks
- database URLs with embedded credentials

### Important behavior
It allows:
- env var names like `OPENAI_API_KEY`
- placeholders like `sk-proj-...`
- example text like `your-key-here`

### Validation result
The scan was run after tightening false-positive handling and finished with:

> No likely live secrets found in the scanned documentation paths.

### Caveat noted
This is a heuristic scan, not a complete security audit of every file type.

---

## Key Decisions

1. **Keep `Synapse/MANIFEST.md` scoped to the Synapse repo.**
   Use `HOME_MANIFEST.md` for workspace-wide navigation instead of turning the Synapse manifest into a home-directory dump.

2. **Treat `FactoriesProjects` as part of the effective Synapse ecosystem.**
   It influences boardrooms, playbooks, and multi-agent design enough to deserve explicit inclusion.

3. **Do not put `Attention-Residuals` on the Synapse app roadmap.**
   It remains adjacent research, not runtime product infrastructure.

4. **Harden backups around multiple verified copies.**
   Backup success now means more than “a file exists.”

5. **Make new documentation discoverable immediately.**
   No more orphan operational docs.

6. **Make docs safety repeatable.**
   Secret scanning now has a script and a runbook.

---

## Files Created This Session

### In `~/Dev/Synapse/`
- `PROJECT_RESUME.md`
- `docs/MEMPALACE_INTEGRATION_PROPOSAL.md`
- `docs/ARCHON_BACKUP_AND_RECOVERY.md`
- `docs/ARCHON_BACKUP_GUIDE_FOR_HUMANS.md`
- `docs/DOCS_SECRET_SCAN.md`
- `scripts/scan-docs-secrets.sh`

### In `~/Documents/Documentation/`
- `HOME_MANIFEST.md`
- `Minutes/minutes-2026-04-12-0902-home-manifest-backup-hardening-and-doc-security.md`

---

## Files Modified This Session

### Synapse repo
- `README.md`
- `MANIFEST.md`
- `docs/SYNAPSE_MASTER_DOCUMENT.md`
- `ai-supervisor/archon-backup.sh`

### Documentation root
- `Readme.md`
- `DOCUMENTATION_INDEX.md`
- `HOME_MANIFEST.md`
- `Minutes/INDEX.md` (updated after this file creation)

---

## Outstanding / Follow-Up

### Recommended next operational step
Run a real backup and a non-destructive restore test against the live Archon database to validate the new backup path end-to-end.

### Useful next improvements
- add the docs secret scan to a maintenance checklist or single-command validation flow
- surface the new docs inside `synapse-docs/index.html` if web-doc discoverability is important
- add at least one independent external/off-machine Archon backup target and raise the required verified copy count beyond 2

---

## Final State At Session End

At the end of the session:
- workspace documentation navigation is materially better
- new operational docs are linked and discoverable
- Archon backup strategy is stronger than before
- there is now a plain-language explanation for backup safety
- documentation secret scanning exists and currently passes on the checked docs surface


## Next Actions

1. Install or restore Docker Desktop so the `docker` CLI resolves to a real binary again.
2. Start Docker Desktop and confirm `docker ps` works from the terminal.
3. From `~/Dev/Synapse/archon/`, run `docker compose up -d`.
4. Verify Archon health on `http://localhost:8181/health` and the UI on `http://localhost:3737`.
5. Run the hardened backup once before relying on the knowledge base.

---

## Follow-Up: Archon Startup Check (2026-04-12)

A later startup attempt for Archon stopped immediately because Docker is not currently installed in a usable location on this machine.

### Findings
- `/usr/local/bin/docker` exists, but it is a symlink to `/Applications/Docker.app/Contents/Resources/bin/docker`
- `/Applications/Docker.app` is not present
- no Docker app was found under `/Applications` or `~/Applications`
- an old `Docker.app` exists only in `~/.Trash/`, which means the machine currently has a broken Docker CLI path rather than a working Docker installation

### Impact
Archon was **not started** in this session. The blocker is host setup, not Synapse configuration.

### Decision
Do not attempt to bring up the Archon stack again until Docker Desktop is restored and the CLI works normally.

---

## Follow-Up: Archon Startup Attempt After Docker Restore (2026-04-12)

Docker was later restored successfully enough for the CLI to work (`docker ps` and `docker compose version` both returned normally), but the Archon stack still did not start.

### Findings
- `docker compose up -d` was run from `~/Dev/Synapse/archon/`
- startup failed on image pull: `archon-archon-server` does not exist locally and is not available from a registry
- the current `docker-compose.yml` references image names only and does not define `build:` entries for the backend services
- the repo contains an `archon-ui-main/Dockerfile`, but no backend Dockerfiles were found in the current checkout
- repo documentation says `docker compose up -d` or `docker compose up --build -d`, but the current compose file is not sufficient for a first-time local boot on a clean machine

### Security Finding
During startup validation, `~/Dev/Synapse/archon/.env` was found to contain live plaintext credentials rather than placeholders. This is a separate security risk and should be cleaned up after Archon boot is stabilized.

### Impact
Archon remains **not running**. The blocker has shifted from missing Docker to missing or unbuildable Archon backend images in the current repo state.

### Recommended Next Step
Reconstruct or restore the missing Archon backend build path, or replace the compose image-only definitions with valid local `build:` targets before attempting another startup.
## Archon Recovery

- Docker was brought online and the Archon compose stack was rebuilt to use local Dockerfiles instead of missing image-only references.
- A missing local Supabase project was recreated at `~/Dev/Synapse/archon-knowledge-local/supabase/config.toml` with the expected local ports:
  - API `54321`
  - DB `54322`
- Existing backup found and used for recovery:
  - `~/Documents/Archive/archon-backups/archon-db-2026-04-11-070251.dump`
- Full-database restore into fresh Supabase produced expected ownership conflicts on Supabase internal schemas, so recovery was validated against the restored Archon `public` tables instead.
- Verified restored Archon data in local DB:
  - `4` projects
  - `56` epics
  - `125` tasks
- Verified Archon stack health after recovery:
  - Backend healthy on `http://localhost:8181/health`
  - MCP healthy on `http://localhost:8051/health`
  - Agents healthy on `http://localhost:8052/health`
  - UI serving on `http://localhost:3737`
- Verified live hierarchy endpoints after recovery:
  - `/api/projects`
  - `/api/projects/{project_id}/epics`
  - `/api/projects/{project_id}/hierarchy`

## Post-Recovery Backup Validation

- Ran a fresh backup from the repaired local Archon database after recovery.
- Verified artifacts created for `2026-04-12 10:14:48 EDT`:
  - custom dump
  - plain SQL gzip
  - globals SQL
  - manifest
- Verified backup succeeded to both targets:
  - `~/Documents/Archive/archon-backups`
  - `~/.codex/memories/archon-backups`
- Confirmed `latest.*` files were refreshed.
- Confirmed `archon/.env` is permissioned `600` and ignored by git.

## Secret Hardening

- Removed live provider and Supabase secrets from repo-managed `archon/.env`.
- Created local-only secret file:
  - `~/.codex/memories/archon-secrets.env`
- Locked secret file permissions to `600`.
- Updated `archon/docker-compose.yml` to load runtime secrets from the external secret file instead of the repo file.
- Recreated Archon services and verified health after the change:
  - backend healthy
  - MCP healthy
  - agents healthy
  - UI serving
- Residual issue still present but unrelated to secret storage:
  - fixed afterward: `document` agent had failed initialization with `Unknown keyword arguments: result_type`
  - root cause: installed `pydantic_ai` uses `output_type`, not `result_type`
  - fix applied in:
    - `archon/python/src/agents/document_agent.py`
    - `archon/python/src/agents/features/session_summarizer.py`
    - `archon/python/src/agents/features/pattern_extractor.py`
  - rebuilt `archon-agents` image and verified both `document` and `rag` agents initialize successfully


## Follow-Up: Archon Knowledge Empty-State Investigation and Repair (2026-04-12)

Later in the day, the Archon Knowledge UI on `http://localhost:3737/knowledge` appeared empty even though the stack was running.

### Problem
- Archon UI loaded, but the Knowledge page showed `No Knowledge Items`.
- Direct verification showed the current local Archon database had no knowledge rows:
  - `archon_sources = 0`
  - `archon_crawled_pages = 0`
  - `archon_code_examples = 0`

### Root Causes Found
1. The current Archon instance is pointed at the **local Supabase** stack on `host.docker.internal:54321`, not a cloud database.
2. The `GET /api/knowledge-items/sources` endpoint in `knowledge_api.py` was stubbed and always returned `[]`.
3. Normal document uploads were failing because Archon credential lookup only read DB-stored credentials and did **not** fall back to environment-backed provider keys, so embedding creation could not authenticate.
4. The progress endpoint incorrectly converted missing progress IDs from `404` into `500`.

### Fixes Applied
- Fixed `archon/python/src/server/api_routes/knowledge_api.py` so `/api/knowledge-items/sources` now returns real DB-backed sources.
- Fixed `archon/python/src/server/services/credential_service.py` so `get_credential()` falls back to environment variables when a value is not present in `archon_settings`.
- Fixed `archon/python/src/server/api_routes/knowledge_api.py` so the progress route re-raises `HTTPException` correctly instead of converting a missing progress ID into `500`.
- Restarted `archon-server` after each verified backend fix.

### Validation
- Verified a normal Archon document upload succeeded again through `/api/documents/upload`.
- Verified the uploaded document was chunked and stored successfully.
- Verified both live endpoints now return real data:
  - `/api/knowledge-items/summary`
  - `/api/knowledge-items/sources`
- Verified missing/completed progress IDs now return `404` instead of `500`.
- Verified the browser Knowledge page became populated again.

### Data State After Repair
Curated Synapse repo docs were ingested into the current local Archon knowledge base and now appear in the UI, including:
- `README.md`
- `SYNAPSE_MASTER_DOCUMENT.md`
- `SERVICE_SPECIFICATIONS.md`
- `LLM_PROVIDER_ARCHITECTURE.md`
- `SECURITY.md`
- additional Synapse technical reference documents

### Conclusion
The empty Knowledge page was a real backend/data-path issue, not a stale browser state issue. The local Archon knowledge workflow is functioning again and is ready for review.

### Code Result
Verified fixes were committed and pushed on `main`:
- `a7573c6` — `fix(archon): restore knowledge uploads and source listing`
