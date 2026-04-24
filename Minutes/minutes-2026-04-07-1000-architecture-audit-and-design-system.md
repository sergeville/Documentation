# Minutes — 2026-04-07 10:00–19:49
## Architecture Audit & Design System Standardization

**Attendees:** Serge, Claude (Opus 4.6)
**Duration:** ~10 hours
**Commits:** `d947a93` (main audit), `da91ee7` (CSS migration)

---

## Agenda & Outcomes

### 1. System Self-Test & Docker Check
- 15 Docker containers all healthy
- 3 local services down at start (workspace-launcher, capture-api, archon-fs-bridge) — resolved

### 2. Page Header Standardization (Story 45-1)
- Created `PageHeader` + `PageHeaderChip` React primitives
- Migrated all 15 Archon UI views to consistent `ARCHON / PAGE` pattern
- Cockpit sub-header used as reference design

### 3. Full Architecture Audit
Conducted modularity/repetition/separation-of-concerns audit across all 3 layers:

**12 findings identified, all 12 resolved:**

| # | Finding | Resolution |
|---|---------|-----------|
| F1 | synapse_base source lost (.pyc only) | Decompiled & recovered 5 source files |
| F2 | Two 3.5K-line monolith files | Split both into modular packages (17+16 files) |
| F3 | No shared Archon client (46 raw HTTP calls) | ArchonClient added to synapse_base v0.3.0 |
| F4 | 3 services bypass synapse_base | All 9 services now on synapse_base |
| F5 | Duplicated loading/empty states in React | Created LoadingState/EmptyState/ErrorState primitives |
| F6 | Legacy src/components/ui/ (14 orphaned files) | 6 deleted, 3 imports migrated |
| F7 | GlobalTodoPage (603-line monolith) | Refactored into features/global-tasks/ (10 files) |
| F8 | neural-map + synapse-docs bypass design system | Migrated to tokens.css + components.css + nav |
| F9 | 3K+ lines inline JS in HTML pages | Extracted to external app.js files |
| F10 | Ghost port 8899 + package.json gap | Port registered, Minutes added to nav |
| F11 | Hyphenated Flask names crash | Fixed in synapse_base app.py (caller __name__) |
| F12 | synapse_base sys.path missing in services | Added explicit path to all 6 affected services |

### 4. Page Header Compliance
- 10 of 12 user-facing pages now compliant with PAGE_HEADER_SPEC
- Each has: `data-synapse-service`, tokens.css, components.css, synapse-nav.js, dark cobalt `<header>`
- Updated compliance audit in `docs/PAGE_HEADER_SPEC.md`

### 5. Cobalt Blueprint Style Guide
- Added "Cobalt Blueprint" tab to Archon UI StyleGuideView
- 10 sections: Colors, Typography, Page Layout, Panels, Tables, Status Indicators, Chips, Buttons, Animations, Spacing
- Live previews on paper background + CSS code snippets + DO/DON'T rules
- Accessible at http://localhost:5173 → Style Guide → Cobalt Blueprint

### 6. Design System Component Promotion (Phase 1)
- components.css expanded from 314 → 527 lines
- 9 new shared component classes: stat-cards, svc-row, status-badge, agent-card, activity-list, chip-grid, page-content, section-heading, header/hdr-chip

### 7. CSS Migration (Phase 2)
- All 10 HTML pages migrated to use shared components.css classes
- 274 lines of inline CSS removed across 10 files
- Net result: one CSS change = all pages update

### 8. Infrastructure Changes
- `~/Documents/Synapse` → symlink to `~/Dev/Synapse` (canonical location)
- `startidea` + `stopidea` updated to use ~/Dev/Synapse
- `stopidea` alias added to .zshrc
- Per-service venv symlinks created (point to ~/venv)
- Minutes Dashboard (:8899) added to nav bar + PORT_REGISTRY.md
- Git repo initialized, connected to github.com/sergeville/Synapse.git

---

## Decisions Made
1. **~/Dev/Synapse is canonical** — ~/Documents/Synapse is a symlink
2. **synapse_base stays at ~/Dev/Synapse/synapse_base/** — all services import from there
3. **components.css is the single source of truth** for page styling — pages use classes, not inline CSS
4. **Archon UI StyleGuideView** is the visual reference for the design system (not a separate service)

## Action Items (Next Session)
- [ ] Write PAGE_LAYOUT_SPEC.md referencing the style guide
- [ ] Fix voice-boardroom port 3007 squatter alert (update PORT_AUTHORITY to mode=native)
- [ ] Remaining 2 non-compliant pages: Synapse Brain (:5002), AI Orchestrator (:3028)

## Metrics
- **Files changed:** 829+ (across both commits)
- **Lines added:** ~151K (includes new modules from monolith splits)
- **Lines removed:** ~12K (inline CSS, duplicated code)
- **Services:** 19 UP, 0 DOWN at session end
- **Anomalies:** 3 open (all LOW/MEDIUM — port squatter, stale heartbeats)
