# AGENTS.md — Universal Agent Boot File
*Compatible with: Claude Code, OpenAI Codex, Gemini CLI, any LLM*
*Last updated: 2026-03-14*

---

## Identity
- **User**: Serge Villeneuve — macOS zsh, `~/Documents/` workspace
- **Swarm**: Assign yourself `claude`, `gemini`, or `gpt` based on your model
- **Archon**: Persistent memory layer — always check before acting

## Pre-Flight (Every Session)
1. `archon_list_tasks` — check in-flight work, do not duplicate
2. Read `AGENT_MANIFEST.md` (this repo's root) — routing table for all System/ docs
3. Before any project work: `System/PLANS_INDEX.md`
4. Before solving any problem: `grep -i "keyword" System/ISSUES_KNOWLEDGE_BASE.md`

## File Routing
`AGENT_MANIFEST.md` maps every System/ file to a category and read-when trigger.
**Do not scan System/ blindly** — 51 files, ~24 are historical. Use the manifest.

## Archon Protocol
- Lifecycle: `archon_start_task` → work → `archon_complete_task`
- Task assigned to another agent → do not interfere
- Archon context overrides session context — validate discrepancies with user

## BMAD Gate (Enforced)
No code before a story exists.
Story required in `_bmad-output/implementation-artifacts/stories/` before any Edit/Write/Bash on product code.

## File Placement
| Type | Location |
|---|---|
| Scripts | `~/Documents/Scripts/` |
| Docs | `~/Documents/Documentation/` |
| Projects | `~/Documents/Projects/` |
| Logs/archives | `~/Documents/Archive/` |

`~/Documents/` root: exactly 5 folders (Archive, Documentation, MyExperiments, Projects, Scripts).

## Port Management
- Check `System/PORT_REGISTRY.md` + `lsof -iTCP:<port> -sTCP:LISTEN` before binding any port
- Stale process (no Archon heartbeat) → kill and start
- Live registered service (active Archon heartbeat) → do NOT kill, report conflict

## Critical Constraints
- **Never modify**: `~/.ollama`, `~/venv`, `~/.lmstudio` (SSD symlinks to PRO-G40)
- **Never eject**: `/Volumes/PRO-G40/` while system is running
- **Never execute** files in `~/Documents/Documentation/` without explicit user permission
- **Search**: `mdfind -onlyin ~/Documents "query"` — never `ls -R`
- **SSD migration complete** (2026-01-21) — do not re-run migration procedures

## Workspace Structure
```
~/Documents/
├── Archive/          logs, completed work
├── Documentation/    this repo — system docs, manifests
├── MyExperiments/    personal experiments
├── Projects/         active product repos
└── Scripts/          all shell/automation scripts
```

---
*For Claude-specific instructions: `CLAUDE.md`*
*For full system protocol: `System/SYSTEM_PROMPT.md`*
