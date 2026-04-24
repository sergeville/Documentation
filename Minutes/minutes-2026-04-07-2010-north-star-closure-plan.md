# Minutes — 2026-04-07 20:10–20:32
## North Star Closure Plan — Autonomous AI Venture Studio

**Attendees:** Serge, Claude (Opus 4.6)
**Duration:** ~25 minutes
**Archon Project:** "North Star Closure Plan" (`d097b6cf-778e-49eb-836c-7ef25bf8cd21`)

---

## Agenda & Outcomes

### 1. Goal Assessment
- Serge asked: is Synapse ready to achieve its goal?
- Reviewed VISION.md — north star: "fully autonomous AI venture studio that operates while you sleep"
- **Finding:** Infrastructure is production-grade (heartbeats, self-healing, voice, cost control). But the autonomy loop is incomplete — 5 gaps prevent end-to-end autonomous operation.

### 2. Gap Analysis (5 Gaps Identified)

| Gap | What's Missing | Impact |
|-----|---------------|--------|
| **1. PLAN Stage UI** | No way to auto-generate BMAD stories from scored ideas | Biggest pipeline break |
| **2. Dashboard Consolidation** | 11 dashboards → should be 5-6 | Cognitive overload |
| **3. Autonomous Work Dispatch** | Orchestrator can't assign work to agents without human trigger | Core autonomy gap |
| **4. Degraded Mode** | No Normal/Degraded/Recovery state machine | No resilience posture |
| **5. Validation Council Wiring** | Council exists but agents don't call it autonomously | Safety gap |

### 3. Sprint State Audit (SCOUT Agent)
- **157 stories** across 44+ epics — Epics 1-40 all complete
- **4 stale "in-progress" epics** need closing (41, 41-hygiene, 43, 44)
- **5 gaps have NO stories** — confirmed the plan scope
- Sprint 35 mostly done — ready for Sprint 36 planning
- Duplicate epic-41 numbering flagged

### 4. Master Plan (NEXUS Agent)
- **21 stories across 5 epics, ~16 sessions, 4 phases**
- Critical path: Council Wiring → Degraded Mode → Autonomous Dispatch → Dashboard Consolidation
- PLAN Stage UI runs in parallel with Council Wiring (independent workstreams)
- North Star Test: idea spoken → AI scores SHARP → story auto-drafted → human approves → Council gates → Amelia codes → reconciler closes loop → cockpit shows it all. **Only "approve" remains human-gated.**

### 5. External Research (2 SCOUT Agents)

#### Frameworks Research
| Gap | Best Tool Found | Action |
|-----|----------------|--------|
| Degraded Mode | **pytransitions** + **pybreaker** | INTEGRATE — 20-line FSM, zero risk |
| Autonomous Dispatch | **Aider** (`--yes` mode, git-native) + **LangGraph** | INTEGRATE as "Amelia" engine |
| Validation Council | **Galileo Agent Control** (Apache 2.0, March 2026) | EVALUATE — exact Council concept |
| PLAN Stage UI | No good tool exists | BUILD — custom 200-line service + Claude prompt |
| Dashboard Consolidation | **Builderz Mission Control** (inspiration) | BUILD — study SPA shell pattern |

#### AI Venture Studio Landscape
- **No one does the full pipeline.** Devin/Factory handle coding. MetaGPT handles generation. CrewAI handles orchestration. None combines idea capture + scoring + sprint + autonomous coding + monitoring + self-healing. **Synapse's ambition is genuinely novel.**
- **AutoAgent/Meta-Harness** (MIT, March 2026): AI that optimizes its own agent harness overnight. Hit #1 on multiple benchmarks beating all human-engineered entries. Future epic for self-improving Synapse.
- **Key insight:** Factory.ai's multi-Droid architecture (CodeDroid, ReviewDroid, QA Droid) is the closest structural parallel to Synapse's BMAD agents.
- **Market signal:** Dario Amodei: 70-80% probability of one-person billion-dollar company in 2026.

### 6. Revised 4-Sprint Plan

**Sprint 36 — Quick Wins (2-3 sessions)**
- Install pytransitions + pybreaker → Degraded Mode FSM (G-1 to G-4)
- Close 4 stale epics, clean up stale Archon tasks

**Sprint 37 — Pipeline Bridge (4-5 sessions)**
- PLAN Stage UI: story template engine + draft UI + approval flow (P-1 to P-4)
- Evaluate Galileo Agent Control vs. build Council client (C-1, C-2)

**Sprint 38 — Autonomy (5 sessions, highest risk)**
- Prototype Aider `--yes` on a simple story in a git worktree
- Agent runner bridge + trigger conditions (A-1 to A-5, C-3)

**Sprint 39 — Polish (3 sessions)**
- Dashboard consolidation: cockpit absorbs ai-dev-dashboard (D-1 to D-4)

### 7. Archon Project Created
- Project: **"North Star Closure Plan"**
- ID: `d097b6cf-778e-49eb-836c-7ef25bf8cd21`
- 7 tasks created covering all 4 sprints
- Status: Planning phase

---

## Key Tools Discovered

| Tool | Repo | Why It Matters |
|------|------|---------------|
| pytransitions | github.com/pytransitions/transitions (5.6K stars) | Lightweight FSM for Normal/Degraded/Recovery |
| pybreaker | github.com/danielfm/pybreaker | Circuit breaker per-service calls |
| Aider | github.com/Aider-AI/aider | Git-native headless coding with `--yes` flag |
| Galileo Agent Control | galileo.ai (Apache 2.0) | Policy-as-code for AI agents = Validation Council |
| LangGraph Deep Agents | langchain.com/langgraph | Durable long-running agent workflows |
| AutoAgent/Meta-Harness | github.com/aiming-lab/AutoHarness (MIT) | Self-optimizing agent harness |
| Builderz Mission Control | github.com/builderz-labs/mission-control | SPA shell for AI agent dashboards |
| OpenHands | github.com/OpenHands/OpenHands (68.6K stars) | Sandboxed autonomous coding agent |
| MetaGPT/MGX | github.com/FoundationAgents/MetaGPT (34.4K stars) | Multi-agent role-based code generation |
| CrewAI | github.com/crewAIInc/crewAI (45.9K stars) | Role-based agent orchestration with MCP |

---

## Decisions Made

1. **Plan saved as Archon project** — "North Star Closure Plan" with 7 tracked tasks
2. **Sprint 36 starts next session** — degraded mode FSM + epic cleanup
3. **Aider preferred over OpenHands** for autonomous coding — lighter weight, git-native
4. **Galileo Agent Control to be evaluated** before building custom Council client
5. **AutoAgent deferred** to future epic — powerful but not immediate priority

---

## Next Actions

- [ ] Start Sprint 36: `pip install transitions pybreaker` → build FSM
- [ ] Close stale epics 41, 41-hygiene, 43, 44 in sprint-status.yaml
- [ ] Resolve stale "BMAD PM: Create PRDs" Archon task
- [ ] Create BMAD story files for Sprint 36 stories (G-1 to G-4)

---

*Session conducted at ~/Dev/Synapse (git worktree context)*
*4 sub-agents deployed: SCOUT (sprint), NEXUS (plan), SCOUT (frameworks), SCOUT (studios)*
