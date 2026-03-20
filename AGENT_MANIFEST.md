# AGENT MANIFEST — System/
*Last updated: 2026-03-20 (manual)*

## How to use
Read this file first. Match your task to a category. Open **only** the listed file(s).
Files marked **archive** are historical — skip unless investigating past work.

---

## 🔴 Core — Read on every session start

| File | Purpose |
|---|---|
| `CLAUDE_ORCHESTRATION.md` | Claude executor protocol — delegation, swarm, handoff schema |
| `CLAUDE_WORKFLOW.md` | Archon-BMAD integration package for Claude |
| `MASTER_VISION_2026.md` | Strategic vision — what you're building and why |
| `SYSTEM_PROMPT.md` | Master cognitive protocol — identity, Archon rules, BMAD gate |

---

## 🟡 Operations — Read when task matches

| File | Read when | Purpose |
|---|---|---|
| `CREDENTIAL_ROTATION_GUIDE.md` | auth/credentials work | How to rotate Supabase and other credentials |
| `CRON-INSTRUCTIONS.md` | cron job changes | Migration status cron job reference |
| `IDEA_DATA_ARCHITECTURE.md` | idea-capture system work | Single source of truth for idea data flow |
| `ISSUES_KNOWLEDGE_BASE.md` | before solving any problem | Known issues + solutions registry |
| `launch-agents.md` | LaunchAgent / plist changes | Personal LaunchAgents registry |
| `MANUAL_PROJECT_SETUP.md` | setting up new Archon project | Manual Archon project creation steps |
| `PLANS_INDEX.md` | before any project work | Index of all active plans across ~/Documents |
| `PORT_REGISTRY.md` | before any port change | Source of truth for all local service port assignments |
| `SCRIPTS_REGISTRY.md` | before creating/running scripts | Registry of all scripts in ~/Documents/Scripts/ |
| `SEARCH_PROTOCOL.md` | when searching filesystem | Fastest macOS search path (Spotlight first) |
| `SECURITY.md` | any security-relevant changes | Active vulnerabilities and remediation status |
| `SHELL_FUNCTIONS.md` | when using custom shell commands | Custom zsh aliases and shell functions |

---

## 🔵 Reference — Background context

| File | Purpose | Read when |
|---|---|---|
| `ACTION_PLAN.md` | Current weekly action items | weekly review |
| `AGENT_ORCHESTRATION.md` | Gemini conductor protocol for multi-agent coordination | multi-agent work |
| `AI-SYSTEM-ORIENTATION.md` | Big picture overview of the AI-augmented dev system | onboarding/orientation |
| `SYSTEM-MANIFEST.md` | **Complete replication guide** — all services, ports, setup, startup sequence | sharing system / onboarding someone new |
| `bmad-cmd.md` | BMAD slash command quick reference | BMAD session startup |
| `claude-manifest.yaml` | Claude Code installation manifest | Claude Code config troubleshooting |
| `EXPERTISE_DEVELOPMENT_PLAN.md` | Learning and skills roadmap | career/skill planning |
| `FIXED_INSTRUCTIONS.md` | Project loading fix for Archon DB issue | Archon DB problems |
| `LEARNING_LOG.md` | Daily learning log | knowledge capture |
| `MASTER_TODO.md` | Single-view of all ideas, plans, tasks | planning sessions |
| `PLAN_REMAINING_SHORTFALLS.md` | Active plan: known system shortfalls to address | system improvement work |
| `PLAN_RULES_AND_MEMORY_CONSOLIDATION.md` | Active plan: reduce context noise, unify rule sources | memory/rules cleanup |
| `PLAN_THREE_GAPS.md` | Active plan: three identified system gaps | gap closure work |
| `SESSION_LOGGER.md` | Session logging system docs | understanding logging |
| `System Meta-Prompt and Technical Specification.md` | Legacy meta-prompt for Alfred/Archon agents | Alfred agent setup |
| `UI_DESIGNER_PROMPT.md` | UX design brief for visual-inventory project | visual-inventory UX work |
| `UNIFIED_SYSTEM_VISION.md` | Plain-language system overview | understanding the system |

---

## ⚪ Archive — Historical, completed, or superseded

Do not read. Safe to move to `~/Documents/Archive/` if noise is an issue.

| File | Notes |
|---|---|
| `ARCHON_MCP_FIX_SUMMARY.md` | Historical: Archon MCP config fix (resolved) |
| `ARCHON_PROJECT_CREATION_ISSUE.md` | Historical: Archon project creation MCP issue |
| `ARCHON_RAG_VALIDATION.md` | Historical: Archon RAG tools validation |
| `BMAD_V6_INSTALL_PLAN.md` | Historical: BMAD V6 install plan (completed) |
| `CLAUDE_INTEGRATION_REPORT.md` | Historical: Claude-Archon integration report |
| `ISSUES_AND_FIXES_LOG.md` | Superseded by ISSUES_KNOWLEDGE_BASE.md |
| `MD_FILES_ORGANIZATIONAL_PLAN.md` | Historical: MD files organization plan 2026-02-18 |
| `ORCHESTRATION_ELABORATION_PLAN.md` | Historical: Orchestration spec elaboration plan |
| `PHASE_1_COMPLETION_SUMMARY.md` | Completed: Issue tracking implementation phase 1 |
| `PHASE_2_COMPLETION_SUMMARY.md` | Completed: Knowledge base structure enhancement |
| `PHASE_3_COMPLETION_SUMMARY.md` | Completed: CLAUDE.md automation |
| `PHASE_4_1_COMPLETION_SUMMARY.md` | Completed: Session logger auto-detection |
| `PHASE_4_2_COMPLETION_SUMMARY.md` | Completed: Test auto-detection + add-issue.sh |
| `PHASE_4_3_COMPLETION_SUMMARY.md` | Completed: Session logger → knowledge base link |
| `PHASE_4_COMPLETION_SUMMARY.md` | Completed: Session logger enhancements |
| `PHASE_5_1_COMPLETION_SUMMARY.md` | Completed: search-issues.sh tool |
| `PHASE_5_2_COMPLETION_SUMMARY.md` | Completed: issue-stats.sh analytics |
| `PHASE_5_3_COMPLETION_SUMMARY.md` | Completed: validate-knowledge-base.sh |
| `PHASE_5_COMPLETION_SUMMARY.md` | Completed: Maintenance tools suite |
| `SECURITY_AUDIT_FINAL_REPORT.md` | Historical: Security audit final report 2026-02-18 |
| `SESSION_SUMMARY_2026-02-18.md` | Historical: 2026-02-18 session summary |
| `Schedule Supabase Rotation for Later.md` | Historical: Supabase rotation deferred task |
| `Starlink-TV-WiFi-Fix.md` | Historical: Starlink TV WiFi fix (resolved) |
| `System_Hang_Investigation_and_Refactoring_2025-07-17.md` | Historical: 2025 system hang investigation |
| `TERMINAL_RECOVERY_STATE.md` | Historical: 2026-01-21 SSD migration recovery |
| `workflow_state.md` | Duplicate of CLAUDE_WORKFLOW.md |

---

---

## 🗂 Key Projects — ~/Documents/Projects/

| Project | Port | Purpose |
|---|---|---|
| `ai-dev-dashboard` | 3004 | Central ops dashboard — sprint board, team assignments, workflow status, Claude activity |
| `voice-boardroom` | 3007 | Live multi-agent voice session — TTS (Kokoro), team cards, speech bubbles |
| `idea-capture-web` | 3000 | Idea capture + validation pipeline (Supabase backend) |
| `capture-api` | 3002 | REST API — single source of truth for idea data |
| `Archon` | 8181 | Task/context store — Archon API + UI |
| `projects-viewer` | 3006 | Projects overview viewer |
| `claude-dashboard` | 3011 | Claude activity monitor |
| `workspace-watchdog` | 3005 | Service watchdog + health monitor |
| `workflow-panel` | 3019 | Universe map / workflow panel |
| `visual-inventory` | — | Visual asset inventory app |
| `HomeAssistant` | — | Home automation integration |
| `Control-Plane` | — | Agent runner orchestration service (Docker) |
| `hvac-simulator` | — | HVAC control simulator |
| `icloud-menubar` | — | macOS Swift menu bar app — iCloud sync status |
| `Idea-to-Sprint` | — | Agile flow simulator / idea pipeline UI |
| `RecordMinutes` | — | Meeting minutes recording + BMAD integration |
| `shared` | — | Shared design tokens CSS across dashboards |
| `archon-telemetry` | 3008 | Archon metrics/telemetry UI |
| `bp-monitor` | 3012/3013 | Blood pressure monitor UI + API |
| `maverick-command-core` | 3009 | Maverick ECU control app |
| `auto-video` | — | Experimental Python video assembly scripts |
| `issue-tracking-system` | — | Legacy issue tracking (see ISSUES_KNOWLEDGE_BASE.md) |

_Updated: 2026-03-20 — Projects cleanup: 7 stray files + 3 folders archived, all remaining projects documented_
