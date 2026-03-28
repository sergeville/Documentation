# Documentation Folder

> `~/Documents/Documentation/` is the **central knowledge base** for Serge's entire workspace. It exists to prevent knowledge loss, reduce repeated problem-solving, and give AI agents (Claude, Gemini, etc.) the context they need to act correctly without asking. Every system decision, protocol, operational procedure, issue resolution, port assignment, and architectural plan that is not obvious from code lives here.

*Last Updated: 2026-03-28*

---

## What Lives Here

| Location | Purpose |
|---|---|
| `System/` | AI agent protocols, operational guides, port registry, issue knowledge base, plans |
| `SSD-Migration/` | Historical: 2026-01-21 internal SSD migration (complete, reference only) |
| `Home-Organization/` | Historical: 2026-01-22 home folder reorganization (complete, reference only) |
| `Tech/` | Technical reference: PLC docs, Home Assistant notes |
| `Entrepreneurship/` | Business strategy, venture studio plans |
| `Personal/` | Personal reference material |
| `RV_Maintenance/` | RV-related documentation |
| `Knowledge/` | General knowledge capture |
| `Reference/` | External reference material |
| `docs-generators/` | Tools and scripts for generating documentation |

Top-level `.md` files in this folder are standalone reference documents — AI system architecture, BMAD methodology, API cost guides, skill analyses, and more.

---

## How to Navigate

**You are an AI agent starting a session:**
→ Read `AGENT_MANIFEST.md` — it maps every task type to the exact file you need. One lookup, no noise.

**You are looking for a specific file:**
→ Read `DOCUMENTATION_INDEX.md` — full catalog of 156+ essential files with why/when/who metadata.

**You are solving a problem:**
→ `grep -i "keyword" System/ISSUES_KNOWLEDGE_BASE.md` before touching anything else.

**You are starting a project:**
→ Read `System/PLANS_INDEX.md` — all active plans across the workspace.

---

## The `System/` Subfolder

This is the most critical subfolder. It contains:

- **`SYSTEM_PROMPT.md`** — master cognitive protocol for all AI agents
- **`CLAUDE_ORCHESTRATION.md`** — Claude's delegation and swarm protocol
- **`ISSUES_KNOWLEDGE_BASE.md`** — every known issue + solution
- **`PORT_REGISTRY.md`** — source of truth for all local service ports
- **`PLANS_INDEX.md`** — index of all active implementation plans
- **`MASTER_VISION_2026.md`** — the strategic north star
- And 30+ more operational guides (see `AGENT_MANIFEST.md` for the full map)

---

## Maintenance Rule

> If you solve a problem, document it in `System/ISSUES_KNOWLEDGE_BASE.md`.
> If you assign a port, register it in `System/PORT_REGISTRY.md`.
> If you start a plan, index it in `System/PLANS_INDEX.md`.

Knowledge that lives only in your session context is knowledge that will be lost.
