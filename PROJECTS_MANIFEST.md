# Projects Manifest
<!-- AUTO-MAINTAINED by Claude. Update when: project created, status changes, port changes, stack changes. -->
<!-- Location: ~/Documents/Documentation/PROJECTS_MANIFEST.md -->
<!-- Last updated: 2026-02-24 -->

## Legend
🚀 Production | 🔄 Active Dev | 🧪 Prototype | 🛠️ Tool | 📦 Stale/Archive

---

## Running Services (Docker / local processes)

| Container / Process | Port | Status | Notes |
|---|---|---|---|
| Studio Frontend (idea-capture-web) | 3000 | 🚀 | `startidea` |
| Capture API | 3001 | 🚀 | `startidea` |
| Cost Dashboard (claude-dashboard) | 3002 | 🚀 | `startidea` |
| AI Dev Dashboard | 3004 | 🚀 | `startidea` |
| Neural Interface (nginx → alfred-agent) | 3005 | 🚀 | Docker |
| Archon UI | 3737 | 🚀 | Docker |
| Archon MCP | 8051 | 🚀 | Docker SSE |
| Alfred Agent | 8052 | 🚀 | Docker |
| Archon API | 8181 | 🚀 | Docker |
| LLM Gateway | 8000 | 🚀 | Docker |
| Home Assistant | 8123 | 🚀 | Docker |
| Ollama | 11434 | 🚀 | Docker |

---

## Projects

### AI & Agents

| Project | Status | Stack | Git | Last Active | Notes |
|---|---|---|---|---|---|
| idea-capture-web | 🚀 | Node/React | ✅ | 2026-02-24 | Idea studio :3000 + API :3001 |
| ai-dev-dashboard | 🚀 | Python/Flask | ✅ | 2026-02-24 | Dev env dashboard :3004 |
| Archon | 🚀 | Python/Docker | ✅ | 2026-02-24 | Task/context system |
| ai-assistant | 🚀 | Docker | ❌ | 2026-02-24 | alfred-agent + neural-interface |
| Alfred | 🔄 | Python | ✅ | 2026-02-22 | Alfred agent service (source) |
| HVAC_ideas | 🚀 | Python | ✅ | 2026-02-21 | Multi-agent HVAC assistant |
| LLM_streamer | 🚀 | Python/Docker | ✅ | 2026-02-22 | LLM streaming gateway |
| axiom | 🔄 | Python | ❌ | 2026-02-23 | iMessage watcher + Claude Vision — blocked on Apple ID |
| MemEvolve | 🔄 | unknown | ✅ | 2026-02-23 | Meta-evolution of agent memory |
| hvac-technician-specialist | 🧪 | Node/Docker | ✅ | 2026-02-22 | HVAC specialist agent |
| legal-assistant | 🧪 | Python | ✅ | 2026-02-16 | HVAC pattern → legal domain |
| medical-diagnostic | 🧪 | Python | ✅ | 2026-02-21 | Agent scaffolding test |
| ai_avatar_it_support_agent | 🧪 | unknown | ✅ | 2026-01-10 | IT support avatar agent |
| recursive-llm | 🧪 | Python | ✅ | 2026-02-18 | Recursive LLM experiment |
| ai-in-the-terminal | 🔄 | unknown | ✅ | 2026-02-18 | Terminal AI assistant |

### Frontend & Web

| Project | Status | Stack | Git | Last Active | Notes |
|---|---|---|---|---|---|
| visual-inventory | 🔄 | Node/Docker | ✅ | 2026-02-23 | Inventory system + Axiom inbox |
| bp-monitor | 🔄 | Node | ✅ | 2026-02-21 | Blood pressure monitor (OCR) |
| diplomat-dream-display | 🔄 | Node | ✅ | 2026-02-19 | Display dashboard |
| carparts | 🧪 | Node (Next.js) | ✅ | 2026-02-22 | Interactive car parts diagram |
| simcity-threejs-clone | 🧪 | Node (Three.js) | ✅ | 2026-02-18 | SimCity clone |
| weatherAppDemo | 🧪 | Node (React) | ✅ | 2026-02-20 | Weather app demo |
| claude-dashboard | 🚀 | Python/Flask | ✅ | 2026-02-24 | Claude Code cost dashboard :3002 |

### Infrastructure & Tools

| Project | Status | Stack | Git | Last Active | Notes |
|---|---|---|---|---|---|
| Control-Plane | 🚀 | Docker | ❌ | 2026-02-21 | Secure sandbox (renamed from control-plans) |
| HomeAssistant | 🚀 | Docker | ❌ | 2026-02-04 | Smart home — port 8123 |
| mkproject | 🛠️ | Shell | ✅ | 2026-02-21 | Project scaffolding utility |
| superpowers | 🛠️ | unknown | ✅ | 2026-02-21 | Dev tooling |
| brainstorming | 🔄 | unknown | ✅ | 2026-02-18 | AuraOS AI-native macOS concept |
| issue-tracking-system | 🔄 | unknown | ✅ | 2026-02-18 | Issue tracking |
| NoteTaking | 🧪 | Docker | ✅ | 2026-02-21 | Note taking app |
| MacCleanup | 🛠️ | unknown | ❌ | 2025-03-15 | Mac maintenance scripts |
| claude-phone | 🧪 | Node/Docker | ✅ | 2026-02-18 | Claude phone integration |

### Stale / Archive

| Project | Status | Stack | Git | Last Active | Notes |
|---|---|---|---|---|---|
| FordMaverick | 📦 | unknown | ✅ | 2026-02-12 | Ford Maverick project |
| Kimi-K2 | 📦 | unknown | ✅ | 2026-02-01 | Kimi K2 experiment |
| Ask Gemini | 📦 | Python | ✅ | 2026-02-03 | Gemini CLI tool |
| aiwithsuryalivedemo | 📦 | unknown | ✅ | 2026-02-05 | Live demo project |
| ha-addon | 📦 | unknown | ✅ | 2025-11-11 | Home Assistant addon |
| SonoffLAN | 📦 | unknown | ✅ | 2025-11-11 | Sonoff LAN control |
| pingpong | 📦 | unknown | ✅ | 2025-11-11 | Ping pong experiment |
| OpenAikit | 📦 | Python | ✅ | 2025-11-22 | OpenAI toolkit |
| DockerNotes | 📦 | unknown | ✅ | 2025-11-08 | Docker notes |
| Arduino CD | 📦 | unknown | ❌ | 2025-03-10 | Arduino project |
| Obsidian Vault | 📦 | unknown | ❌ | 2025-07-01 | Obsidian notes |
| chatGPT myDocs | 📦 | unknown | ❌ | 2024-01-12 | ChatGPT docs experiment |
| Cline | 📦 | unknown | ✅ | unknown | Cline AI assistant |
| theNetworkChuck | 📦 | unknown | ❌ | 2026-02-18 | NetworkChuck tutorial |
| RecordMinutes | 📦 | unknown | ❌ | 2026-02-18 | Meeting recorder |
| _git_test | 📦 | unknown | ✅ | unknown | Git test repo — can delete |

---

## MyExperiments (non-Projects)

| Project | Status | Notes |
|---|---|---|
| ai-assistant | 🚀 | Compose file mirror of ~/Documents/Projects/ai-assistant |
| tools | 🛠️ | Misc tools |

---

## Update Protocol (for Claude)

When any of the following happens, update this file immediately:
- **New project created** → add row in correct category
- **Port changes** → update Running Services table
- **Status changes** (archived, promoted to prod, etc.) → update status icon
- **Project deleted/moved** → remove or move to Stale section
- **Stack identified** → fill in unknown fields

Command to check for new projects not in manifest:
```bash
ls ~/Documents/Projects/ | sort
```
