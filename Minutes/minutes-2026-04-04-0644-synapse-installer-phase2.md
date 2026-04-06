# Session Minutes — Synapse Installer Phase 2 + Platform Polish + BMAD Consolidation

**Date:** 2026-04-04, ~06:44–09:15 EDT
**Agent:** Claude Opus 4.6 (1M context) via Claude Code CLI
**Topic:** Installer Phase 2, Minutes Dashboard, Dashboard Polish, BMAD Migration

---

## What was done

### Synapse Installer Phase 2 (06:44–07:26)
- Built **Task 2.4 — Update Mechanism** (`UpdateManager.swift` + `UpdateView.swift`)
  - Full lifecycle: stop services → git pull (Synapse + Archon) → detect changed deps → reinstall → restart → health check
  - Background auto-check every 6 hours
  - Update window with progress states + collapsible detail log
  - Menu bar shows version + "Update Available (N new)" when commits pending
- Built **Task 2.6 — Dynamic Menu Bar Icons** (replaced text badge approach)
- Fixed `UNUserNotificationCenter` crash when running outside `.app` bundle
- Bumped to **v1.7.0**, updated CHANGELOG, story, memory
- Committed and pushed `5f23cdb`

### Session Minutes System (07:26–08:21)
- Established **session minutes pattern** — feedback memory saved
- Created `Documentation/Minutes/` directory
- Built **Session Minutes dashboard** (`Minutes/index.html`):
  - Cobalt Blueprint theme with full design system tokens (IBM Plex Mono 12px, grid background)
  - Inline markdown renderer (tables, code, bold, lists — no raw `.md` in browser)
  - List view (cards) + detail view (rendered content) — like cockpit inbox
  - Synapse-nav bar included + `body.has-synapse-nav` padding fix
  - Responsive: iPhone / iPad / desktop
- Added **"Minutes"** to shared `synapse-nav.js` (port 8899, temp server)
- Saved feedback: **all web pages must use Cobalt Blueprint + synapse-nav + responsive**
- Bumped to **v1.7.1**, committed `30b5e41`

### Dashboard Polish (08:21–09:00)
- **Speech bubble markdown formatting** — added `fmtBubble()` to both `ai-dev-dashboard` and `claude-cockpit`
  - Renders **bold**, `code`, bullet lists, numbered lists, line breaks in comic balloons
  - Previously showed raw `**text**` and `- items`
- **Wider speech bubbles** — `max-width: 220px` → `min(500px, 50vw)` so text fits
- **Idle agent bubbles removed** — no more "Ready: capabilities" balloons cluttering the team panel
- **Thought dots fixed** — `display: none` by default, only `display: flex` with `.visible` class when agent has active Archon task
- Saved feedback: **AI Assistant on BMAD team is Sam; Orchestrator stays Claude**

### BMAD Consolidation (08:48–09:10)
- Found upstream: **`bmad-code-org/BMAD-METHOD`** (v6.2.2, 43K stars)
- **Cloned fresh** into `Synapse/_bmad/` (30 skill files across 4 lifecycle phases)
- **Moved `_bmad-output/`** (162 files) into `Synapse/_bmad-output/`
- **Removed corrupted** `~/Documents/_bmad/` (APFS damage, no recoverable content)
- **Agent roster comparison**: upstream has Analyst, Tech Writer, PM, UX, Architect, Dev. Local adds Quinn (QA) and Bob (SM) as custom extensions.
- Updated **BMAD_DISPLAY_NAMES** — `claude` → "Sam" in team panel, "Claude" in orchestrators

### Dashboard Identity Fix (09:00–09:15)
- **Sam** = AI Assistant agent on BMAD Team panel
- **Claude** = Orchestrator in the Orchestrators panel (the session talking to Serge)
- Fixed both display contexts to show the correct name

## Decisions made

| Decision | Why |
|----------|-----|
| SF Symbol variants instead of colored dot overlay | macOS renders menu bar icons as monochrome templates — colored SwiftUI overlays are invisible |
| `brain` → `brain.fill` → `brain.head.profile` → `exclamationmark.triangle` | Each is visually distinct even in monochrome; matches severity escalation |
| Guard `UNUserNotificationCenter` on `bundleIdentifier != nil` | `swift run` doesn't create a proper `.app` bundle, causing crash |
| Session minutes at end of every session | Conversation context is lost between sessions — minutes preserve decisions, issues, rejected ideas |
| All web pages must use Cobalt Blueprint + synapse-nav | Serge accesses dashboards from iPhone/iPad/desktop — consistent look matters |
| BMAD consolidated into Synapse repo | Was scattered in `~/Documents/_bmad` (corrupted) and `_bmad-output` — violates 6-folder rule, now version-controlled together |
| Sam vs Claude naming | Sam is the AI developer agent on the team; Claude is the orchestrator session — different roles |
| Idle agents: no bubble | Thought dots and "Ready:" balloons cluttered the UI — only show bubbles when there's actual activity |
| Thought bubble `display:none` by default | CSS guard ensures no phantom dots even if JS generates stale HTML |

## Issues encountered

1. **"Phase 2" was ambiguous** — appeared in 4 different project contexts. Serge clarified: option 3 (Synapse Installer).
2. **Colored dot overlay invisible in menu bar** — macOS menu bar icons are template images (monochrome). Pivoted to SF Symbol names.
3. **`swift run` crash** — `UNUserNotificationCenter` needs proper `.app` bundle. Fixed with bundleIdentifier guard.
4. **Menu bar icon not visible** — first attempt silently died; had to run without `&>/dev/null` to see the exception.
5. **Nav bar overlapped header** — `body.has-synapse-nav` padding wasn't in the minutes page CSS initially.
6. **Raw markdown in browser** — `.md` files served as plain text by `python3 -m http.server`. Built inline renderer instead.
7. **Speech bubbles showed raw markdown** — `escHtml()` escaped everything. Added `fmtBubble()` for inline markdown rendering.
8. **BMAD agent files lost** — `~/Documents/_bmad/` directory structure intact but all content wiped by APFS corruption. Git also corrupted (no HEAD). Re-cloned from upstream `bmad-code-org/BMAD-METHOD`.
9. **Phantom thought dots** — CSS `::before`/`::after` pseudo-elements on `.ua-thought-bubble` rendered even when the div was empty. Fixed with `display:none` default + `.visible` class.
10. **Sam vs Claude confusion** — initially renamed Claude to Sam everywhere; Serge clarified they're different roles.

## What was tried and rejected

- **Colored Circle overlay on brain icon** — macOS strips colors from menu bar template images
- **Text badge suffix** ("!" and "✕") — visually weak; replaced with symbol-switching
- **Idle agent speech bubbles** ("Ready: architecture, system-design") — cluttered the team panel; removed entirely

## Open questions / next steps

- **Phase 3 (Distribution)** blocked on security audit: 2 CRITICAL + 4 HIGH
- **`.dmg` rebuild** pending with Phase 2 code
- **Minutes service** on port 8899 is temp `python3 -m http.server` — needs proper service
- **PM PRD creation** — BMAD PM agent should create PRDs for all major product areas (delegation pattern, not Claude doing it)
- **Dashboard-to-BMAD sync** — team roster currently hardcoded, should eventually read from BMAD framework files
- **CLAUDE.md references** need updating for new `Synapse/_bmad` and `Synapse/_bmad-output` paths
