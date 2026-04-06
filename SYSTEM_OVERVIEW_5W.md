# System Overview — The 5W
**Created:** 2026-03-18
**Author:** Claude (synthesized from full project inventory + UNIFIED_SYSTEM_VISION.md)
**Purpose:** Read this to understand everything you're building — in one place.

---

## WHY — The Vision

You are building a **personal AI operating layer**.

> Every intention — write code, control the house, capture an idea, execute a task — passes through an agent team that validates it, executes it, and logs it permanently. Every action is explainable. Every action is reversible. The system knows what needs to be done without you telling it every time.

The system has five conceptual pillars:

| Pillar | What It Is | Progress |
|--------|-----------|----------|
| **Archon** | The brain — shared memory, task management, agent registry, audit log | 85% |
| **Alfred** | The butler — Home Assistant AI, pattern recognition, proactive suggestions | 40% |
| **Claude Orchestration** | The execution protocol — parallel tasks, validation, synthesis | Spec only (no enforcement) |
| **Agent Work Orders** | The job queue — Claude CLI execution, SSE streaming, dry-run mode | 60% |
| **AuraOS** | The full vision — multi-agent council, zero-trust sandbox, radical transparency | Concept only |

**The insight:** AuraOS is not a separate project. It is Archon + Alfred + Agent Work Orders + Orchestration, assembled correctly. You've been building it piece by piece without naming what the pieces add up to.

**The three things missing:**
1. **Situation Agent** — reads all tasks, plans, sessions → "here are your top 3 priorities today"
2. **Validation Council** — three agents run before any work order executes (logic, impact, coherence)
3. **Unified Audit Log** — one timeline across all systems

Build those three and the rest becomes a working system instead of a collection of promising parts.

---

## WHO — The Team

### Builder
**Serge Villeneuve** — macOS zsh, `~/Documents/` workspace. Architects the system, approves stories, reviews output.

### BMAD Agent Team (Development)
| Agent | Role | Trigger |
|-------|------|---------|
| **Bob** | Scrum Master — creates stories, runs sprint ceremonies | `/bmad sm` |
| **Amelia** | Developer — implements features, fixes bugs | `/bmad dev` |
| **Quinn** | QA Engineer — tests, validates, tracks defects | `/bmad qa` |
| **Winston** | Architect — system design, ADRs, API contracts | `/bmad arch` |
| **UX Designer** | Interface design, accessibility, layout | `/bmad ux` |
| **PM** | Product requirements, feasibility, stakeholders | `/bmad pm` |

### AI Systems (Deployed)
| Agent | Where It Runs | What It Does |
|-------|-------------|-------------|
| **Alfred** | Docker container, port 8052 | Talks to Home Assistant, controls devices, memory via SQLite + vectors |
| **Claude Code** | CLI, this session | Parallel execution engine, BMAD workflow runner |
| **Archon MCP** | Docker container, port 8051 | Tools for Claude: tasks, sessions, knowledge base, shared context |

---

## WHAT — Every Project

### Core Infrastructure (Always On — Docker)

| Project | Port(s) | What It Does | Status |
|---------|--------|-------------|--------|
| **Archon Server** | 8181 | REST API for tasks, projects, sessions, shared context. Single source of truth for agent coordination | Active — 85% |
| **Archon UI** | 3737 | Web dashboard: projects, tasks, sessions, sprint war room, agent work orders | Active |
| **Archon MCP** | 8051 | MCP server — exposes all Archon tools to Claude Code, Cursor, Windsurf | Active |
| **Alfred Agent** | 8052 | Home AI butler — HA device control, TTS (Kokoro), conversation memory | Active — 40% |
| **Home Assistant** | 8123 | Home automation platform — devices, automations, recorder database | Active |
| **LLM Streamer** | 8000 | AI event bus gateway — cross-agent context sharing (paused, security design needed) | Paused |
| **Neural Interface** | 3005 | Proxy / interface layer | Active |
| **HVAC Stack** | 3010 / 8010 / 1883 / 8880 | Full HVAC AI system: React frontend, Python backend, MQTT broker, Kokoro TTS | Active |
| **Ollama** | 11434 | Local LLM serving (llama3.2 3B) — Homebrew native, Apple Silicon MLX. Fallback when OpenAI budget exhausted. | Active (Homebrew, NOT Docker — since 2026-04-03) |

### Active Dev Projects (On-Demand)

| Project | Port(s) | What It Does | Sprint Status |
|---------|--------|-------------|--------------|
| **workspace-launcher** | 3000 | Control plane entry — start/stop all dev services, see system health | Stable |
| **idea-capture-web** | 3001 (UI) / 3002 (API) | Cyberpunk idea capture + AI enrichment + dependency analysis DAG. Smart Auto-Intake pipeline | **Sprint 21 — Epic 16 active** |
| **visual-inventory / Vault OS** | 3003 | File inventory with glassmorphic Vault OS UI, blueprint toggle, circle pins | Phase 2 complete |
| **ai-dev-dashboard** | 3004 | Passive service health monitor — polls 11 services every 6s, shows up/down status | Stable |
| **projects-viewer** | 3006 | Browse all projects, status overview | Stable |
| **voice-boardroom** | 3007 | Voice interface + Virtual Whiteboard Agent (VWA at `/vwa`) | Active |
| **archon-telemetry** | 3008 | Telemetry stub for Archon monitoring (rebuilt 2026-03-15) | Stub |
| **maverick-command-core** | 3009 | Ford Maverick ECU/OBD dashboard — vehicle data display | Active |
| **claude-dashboard** | 3011 | Claude activity monitor | Stable |
| **bp-monitor** | 3012 / 3013 | Blood pressure tracker — React PWA + Express/SQLite API | Active |
| **hvac-simulator** | 3014 / 3015 | HVAC simulation — React frontend + Express/SQLite API | Active |
| **archon-client** | 3016 | Archon client interface | Active |
| **obd-flux-app** | 3017 | OBD BLE dashboard — Next.js + Capacitor-ready, connects to Maverick via Bluetooth | Active |
| **skills-mindmap** | 8765 | Visual mindmap of all skills/capabilities | On-demand |

### Projects In Planning / Partially Built

| Project | Path | What It Is | Status |
|---------|------|-----------|--------|
| **claude-phone** | `Projects/claude-phone` | Claude deployment on Raspberry Pi / SBC — unified installer with prerequisite checks | Active plans, not started |
| **AuraOS / brainstorming** | `Projects/brainstorming` | Multi-agent council vision — zero-trust sandbox, radical transparency, one-click undo | Concept |
| **RLM** | `MyExperiments/RLM_PROJECT_PLAN.md` | Recursive Language Model — agents reason over 100K+ word knowledge bases without losing context | 10-week plan ready, not started |
| **Validation Council** | Port 8054 (reserved) | Three-agent pre-execution gate: logic validator + impact analyzer + coherence guard | Spec only |
| **Agent Work Orders** | Port 8053 (reserved) | Claude CLI in git worktrees, SSE live output, dry-run mode | 60% built |

### Key Data Stores

| Store | Where | What It Holds |
|-------|-------|--------------|
| Archon PostgreSQL | Docker | Tasks, projects, sessions, agent registry, shared context, knowledge base |
| Alfred SQLite | Docker (`alfred-agent`) | 25 tables — conversation history, device patterns, energy data, battery tracking |
| idea-capture `ideas.db` | `Projects/idea-capture-web/` | Captured ideas, enrichment data, dependency links |
| bp-monitor SQLite | `Projects/bp-monitor/server/` | Blood pressure readings |
| hvac-simulator SQLite | `Projects/hvac-simulator/server/` | Simulation state |
| HVAC Docker volumes | Docker | HVAC sensor data, MQTT messages |
| Issues Knowledge Base | `Documentation/System/ISSUES_KNOWLEDGE_BASE.md` | 22,000+ lines of known issues and solutions |

---

## WHERE — Paths and Ports

### Filesystem
```
~/Documents/
├── Projects/           → all runnable services + apps
├── Documentation/
│   └── System/         → CLAUDE.md, UNIFIED_SYSTEM_VISION.md, PORT_REGISTRY.md,
│                          PLANS_INDEX.md, ISSUES_KNOWLEDGE_BASE.md
├── _bmad/              → BMAD agent personas, config, workflows
├── _bmad-output/       → sprint-status.yaml, stories/, epics/
├── Scripts/            → startidea, stopidea, utility scripts
├── Archive/            → completed plans, experiments
└── MyExperiments/      → RLM, HVAC AI, Alfred Evolution, brainstorming
```

### Service Map (quick reference)
```
3000  workspace-launcher (control plane)
3001  idea-capture frontend
3002  idea-capture API
3003  visual-inventory / Vault OS
3004  ai-dev-dashboard
3005  neural-interface
3006  projects-viewer
3007  voice-boardroom
3008  archon-telemetry
3009  maverick-command-core
3010  hvac frontend (Docker)
3011  claude-dashboard
3012  bp-monitor frontend
3013  bp-monitor API
3014  hvac-simulator frontend
3015  hvac-simulator API
3016  archon-client
3017  obd-flux-app
3737  Archon UI (Docker)
8000  LLM Streamer (Docker)
8051  Archon MCP (Docker)
8052  Alfred Agent (Docker)
8053  Agent Work Orders (reserved)
8054  Validation Council (reserved)
8055  RLM service (reserved)
8123  Home Assistant (Docker)
8181  Archon API (Docker)
11434 Ollama (Homebrew native — NOT Docker)
```

### Important Config Files
| File | Purpose |
|------|---------|
| `~/.claude.json` | MCP server config (NOT `~/.claude/settings.json`) |
| `~/Documents/_bmad/bmm/config.yaml` | BMAD config — user name, language, project root |
| `~/Documents/Documentation/System/PORT_REGISTRY.md` | Port assignments — source of truth |
| `~/Documents/Documentation/System/PLANS_INDEX.md` | All active plans across the system |
| `~/Documents/_bmad-output/implementation-artifacts/sprint-status.yaml` | Current sprint story tracking |
| `~/Documents/Documentation/System/ISSUES_KNOWLEDGE_BASE.md` | 22K+ line issue database |

---

## WHEN — Timeline and Roadmap

### Now — Sprint 21 (Active)
**Epic 16: Smart Auto-Intake Pipeline** (idea-capture-web)

| Story | What | Status |
|-------|------|--------|
| 16.1 — Auto-rate on capture | AI rates idea immediately on capture | ✅ Done |
| 16.2 — Dep scan on intake | Background dep scan fires after auto-rate; pending badge on AnalysisTrigger | ✅ Done (review) |
| 16.3 — Rating chip on PipelineCard | Show rating visually in card | 📋 Backlog |
| Tags edit UI + Comments/Files | Tags have no edit UI post-creation; comments/files don't exist in data model | 📋 Story not yet created |

### Near Term — Phase A (2–3 weeks)
*Goal: See everything in one place*
- A1. Load real work into Archon (clean up stale January tasks)
- A2. Build Unified Audit Log (one table, all systems write to it, timeline view in UI)
- A3. Build Situation Agent (`/situation` command — reads all plans + tasks → prioritized brief)
- A4. Alfred → Archon bridge (Alfred logs discoveries as Archon session events)

### Medium Term — Phase B (3–4 weeks)
*Goal: Nothing executes without validation*
- B1. Validation Council microservice (port 8054) — 3 agents in parallel
- B2. Wire all work orders through the council
- B3. Dry-run mode (execute in shadow worktree, show diff before committing)
- B4. Human approval queue in Archon UI for destructive actions

### Long Term — Phase C (4–6 weeks)
*Goal: System acts proactively*
- C1. Situation Agent runs automatically (8am daily, creates Archon tasks)
- C2. Gemini Conductor — natural language → structured work orders
- C3. Alfred Phase 2 — pattern recognition, proactive suggestions, HA automation creation
- C4. RLM integration — agents reason over entire 100K+ word knowledge base

### Completed (Milestones)
| When | What |
|------|------|
| 2026-01-21 | SSD migration to PRO-G40 complete |
| 2026-01-31 | idea-capture-web MVP launched |
| 2026-02-19 | Archon Phase 3 complete — Sessions Dashboard, Test Runner UI (201 tests, SSE) |
| 2026-02-20 | UNIFIED_SYSTEM_VISION.md written — full architectural synthesis |
| 2026-02-21 | Orchestration Elaboration Plan complete — conductor_log SQL+API+MCP |
| 2026-02-23 | Visual Inventory → Vault OS UI redesign (Phase 2 complete) |
| 2026-03-05 | Sprint War Room shipped — all components, /sprints route, nav item |
| 2026-03-15 | archon-telemetry rebuilt |
| 2026-03-18 | Epic 16.1 done, Epic 16.2 done — Smart Auto-Intake Pipeline underway |

---

## The Architecture in One Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     YOU (Serge)                             │
│         capture idea / write command / make request         │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│               SITUATION AGENT  (Phase A)                    │
│   reads all tasks + plans → "here's what to do today"       │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│             AGENT WORK ORDER created                        │
│   what to do | project | risk level | reversible?           │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│          VALIDATION COUNCIL  (Phase B)  — 3 agents          │
│  Logic Validator + Impact Analyzer + Coherence Guard        │
│              → APPROVED or BLOCKED                          │
└───────────────────────┬─────────────────────────────────────┘
                        │
              ┌─────────┴──────────┐
              ▼                    ▼
        BLOCKED                 APPROVED
    logged + shown           dry-run first
    in UI + audit log        show diff → approve
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────┐
│         EXECUTION  (Claude CLI in git worktree)             │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                ARCHON  (The Brain)                          │
│  task marked done + session event + unified audit log row   │
│  shared context updated + snapshot if destructive           │
└─────────────────────────────────────────────────────────────┘
                        │
              ┌─────────┴──────────┐
              ▼                    ▼
        ALFRED                ai-dev-dashboard
   (home devices)           (service health)
```

---

## Active Plans Index (Quick Reference)

| Plan | Status | Where |
|------|--------|-------|
| Unified System Vision | ACTIVE | `Documentation/System/UNIFIED_SYSTEM_VISION.md` |
| Archon Memory Upgrade | ACTIVE — not started | `Projects/Archon/docs/MEMORY_UPGRADE_PLAN.md` |
| Archon Phase 2 Roadmap | ACTIVE — pending | `Projects/Archon/docs/PHASE_2_ROADMAP.md` |
| Archon Send-to-Agent | ACTIVE | `Projects/Archon/docs/SEND_TO_AGENT_PLAN.md` |
| Alfred Agent Enhancement | ACTIVE — 0/35 tasks | `Projects/Alfred/docs/agent/AGENT_ENHANCEMENT_PLAN.md` |
| Alfred Evolution Plan | ACTIVE — ready to execute | `MyExperiments/PRPs/ALFRED_EVOLUTION_PLAN.md` |
| RLM Project Plan | ACTIVE — planning complete | `MyExperiments/RLM_PROJECT_PLAN.md` |
| claude-phone Installer | ACTIVE — 5 sub-plans | `Projects/claude-phone/src/features/` |
| LLM Streamer Event Bus | PAUSED — security design needed | `Archive/LLM_streamer/IMPORTANT-READ-BEFORE-ANY-WORK.md` |
| Rules/Memory Consolidation | DRAFT | `Documentation/System/PLAN_RULES_AND_MEMORY_CONSOLIDATION.md` |

---

*Generated 2026-03-18. Source: UNIFIED_SYSTEM_VISION.md + PORT_REGISTRY.md + PLANS_INDEX.md + sprint-status.yaml + full project inventory.*
*Update this file at the end of each sprint or when major milestones are reached.*
