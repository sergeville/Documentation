# Meeting Minutes — Goals Brainstorm Session
**Date:** 2026-03-06
**Facilitator:** Winston (BMAD Architect)
**Attendees:** Serge Villeneuve + BMAD Team (Winston, John/PM, Mary/Analyst, Sally/UX, Bob/SM)
**Format:** Party Mode — open brainstorm with cross-functional feedback

---

## Purpose
Define and document Serge's goals for the AI workspace — starting from a simple question: *"Why are we building all of this?"*

---

## Key Discovery

Serge articulated the core vision unprompted:

> *"It started with an idea. Ideas need to be documented. From a goal we brainstorm — is it good, bad, no sense? Then we follow a method that brings that idea to a plan, a project, and ships it."*

**Team interpretation:** This is not a collection of projects. This is a **single pipeline**, built one stage at a time, that takes any idea from spark to shipped.

---

## The Pipeline (Emerged from Discussion)

| Stage | Name | What happens | Built today |
|---|---|---|---|
| 1 | **Capture** | Idea is spoken or typed and documented | idea-capture-web :3000 |
| 2 | **Enrich** | Related ideas found, patterns surfaced | Idea relationship graph (Epic 12) |
| 3 | **Validate** | Brainstorm — good / bad / no sense? | Voice boardroom + BMAD party mode |
| 3.5 | **Decide** | AI-assisted gate: ship / shelve / merge | ⚠️ Not built — identified as gap |
| 4 | **Plan** | Goals → epics → stories | BMAD (PM + Arch + SM workflows) |
| 5 | **Build** | AI-assisted implementation | bmm-dev (Amelia) + Archon tasks |
| 6 | **Track** | Progress, health, cost monitoring | AI Dev Dashboard + Archon telemetry |

---

## Vision Statement
*(Drafted by team, approved by Serge)*

> **An AI-native platform that takes any idea — from anyone on a team — through a structured pipeline from spark to shipped: capture, validate, plan, build, and track. Agents handle the method. Humans bring the thinking.**

---

## Audience
- **Now:** Serge (sole user, proving the pipeline on himself)
- **Next:** A whole team — shared ideas, shared agents, shared tracking
- **Future:** Any team, any domain — the pipeline is domain-agnostic

---

## Strategic Goals

| # | Goal | Status |
|---|---|---|
| G1 | Pipeline works end-to-end for Serge — zero friction from idea to Epic | ✅ Achieved |
| G2 | Pipeline works for a small team — shared ideas, shared agents, shared tracking | 🔜 Next horizon |
| G3 | Pipeline is domain-agnostic — HVAC, legal, health, home automation all flow through the same system | 🔜 Next horizon |
| G4 | Decision gate (Stage 3.5) exists — AI scores ideas and recommends: ship / shelve / merge | 🔮 Future |
| G5 | Platform is deployable — another team can run this stack | 🔮 Future |

---

## Identified Gap — Epic 13 Candidate

**Stage 3.5: AI Decision Gate**

After brainstorm, before planning — a structured moment to answer: *"Should we build this?"*

Inputs:
- Brainstorm output (nodes, ratings, links)
- Current project load (Archon tasks)
- Alignment with strategic goals (this document)

Output: **Ship / Shelve / Merge** recommendation with reasoning

This is the missing link between the creative phase and the execution phase.

---

## Pros & Cons Raised by Team

**Pros of this vision:**
- Every project already built maps to a pipeline stage — nothing is wasted
- Archon as orchestrator, agents as workers, ideas as data — all scales to multi-user
- Voice interface already bridges physical + digital workspace
- Domain experiments (HVAC, legal, medical) validate the pipeline across verticals

**Cons / Risks raised:**
- Current stack is deeply personal (local paths, local ports, personal `.env`) — multi-user requires auth, tenancy, deployment rethink *(Winston)*
- Goals doc must stay to 1 page max or it gets ignored *(Winston)*
- Some beloved projects may not map to the pipeline — hard but healthy to acknowledge *(Mary)*
- Without Stage 3.5, good ideas and bad ideas get equal effort *(John)*

---

## Decisions Made
1. Vision statement adopted as written above
2. Pipeline stages 1–6 confirmed as the canonical model
3. Stage 3.5 (Decision Gate) identified as next major feature — likely Epic 13
4. Goals document to be saved to `~/Documents/Documentation/` and referenced in `context.md`

---

## Action Items

| # | Action | Owner | When |
|---|---|---|---|
| A1 | Save this goals doc to Documentation/ | Winston | ✅ Done (this file) |
| A2 | Add goals summary to `context.md` for Astra AI | Winston | Next |
| A3 | Plan Epic 13: AI Decision Gate | John + Winston | Next session |
| A4 | Map all 50 existing projects to pipeline stages | Mary | Backlog |
| A5 | Identify what changes are needed for multi-user (auth, tenancy) | Winston | Backlog |

---

## External Inspiration — Claude Telegram Relay

**Source:** https://github.com/godagoo/claude-telegram-relay
**Raised by:** Serge during session

### What it is
An open-source project that turns Telegram into a personal AI assistant interface. It receives Telegram messages, spawns Claude Code CLI to process them, and returns responses. Features: persistent memory (Supabase + semantic search), voice transcription (Whisper/Groq), multimodal input (text, photo, voice, document), proactive morning briefings, always-on daemon (macOS launchd / Linux systemd).

### How it maps to our pipeline

| Relay feature | Pipeline opportunity |
|---|---|
| Telegram → Claude Code → reply | Mobile idea capture — send from anywhere, enters :3001 API |
| Voice transcription | Voice → idea without needing the full voice boardroom |
| Morning briefings | BMAD SM (Bob) sends daily sprint status to Serge via Telegram |
| Always-on daemon | Pipeline never sleeps — capture at 2am from mobile |
| Multi-user whitelist | Shared team capture channel — anyone can submit ideas |

### Team Reaction

**John (PM):** Solves the desktop-only friction. Makes the pipeline ambient — it follows the user. Directly enables Goal G2 (whole team).

**Sally (UX):** This is the mobile front door the pipeline is missing. Idea in a meeting → voice message → transcribed → captured → waiting in the studio.

**Mary (Analyst):** The "whole team" ambition becomes real: anyone Telegrams an idea, it enters the shared pipeline.

**Winston (Architect) — Pros:**
- No new UI — Telegram is already on every device
- Voice transcription maps to voice boardroom concept
- Daemon model fits existing `startidea` stack
- Open source — can fork and wire directly to `:3001` capture API

**Winston (Architect) — Cons:**
- External dependency (Telegram bot token, webhook/polling)
- Supabase memory is separate from Archon — risk of two sources of truth
- Claude Code CLI per message is expensive at team scale
- Security: Telegram userID whitelist must be strict for multi-user use

### Classification
**Epic 14 candidate** — *Telegram as mobile capture + BMAD briefing channel*
*(Epic 13 = Decision Gate first, then Epic 14 = Telegram interface)*

---

## Next Session Suggested Agenda
1. Review this goals doc — any corrections?
2. Kick off Epic 13 planning (Decision Gate)
3. Explore Claude Telegram Relay fork for Epic 14
4. Begin multi-user architecture exploration

---

*Minutes drafted by Winston (BMAD Architect) · Party Mode session · 2026-03-06*
*Participants: Serge, Winston, John (PM), Mary (Analyst), Sally (UX), Bob (SM)*
