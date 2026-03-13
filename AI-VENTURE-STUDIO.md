# AI Venture Studio
*The vision: one person, full company — AI as the operating brain for every step of product creation.*

**Created:** 2026-03-11
**Author:** Serge Villeneuve
**Status:** Vision / Architecture Design

---

## The Core Idea

You are not just building products. You are building **the machine that builds products**.

A solo founder backed by a full AI team that covers every company function — from raw idea all the way to shipped product and market feedback. AI handles execution. You handle vision and final calls.

The blood pressure app is not the product. The machine that decides whether to build it — and then builds it — is the product.

---

## Full Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      YOU (Human CEO)                        │
│                 Vision · Final call · Values                │
└──────────────────────────┬──────────────────────────────────┘
                           │
              ┌────────────▼─────────────┐
              │    IDEA INTELLIGENCE      │   ✅ BUILT
              │                          │
              │  · idea-capture (web)    │
              │  · rating / ranking      │
              │  · priority scoring      │
              │  · idea-chain (Archon)   │
              └────────────┬─────────────┘
                           │
              ┌────────────▼─────────────┐
              │    VALIDATION GATE        │   ❌ MISSING ← BUILD THIS
              │    (The CEO Brain)        │
              │                          │
              │  [Market Agent]          │
              │   → TAM estimate         │
              │   → competition scan     │
              │   → pricing signals      │
              │                          │
              │  [Devil's Advocate]      │
              │   → why this fails       │
              │   → risks & blockers     │
              │   → what kills it        │
              │                          │
              │  [Business Model Agent]  │
              │   → 2-3 revenue options  │
              │   → rough unit economics │
              │   → B2C vs B2B angle     │
              │                          │
              │  [Risk Agent]            │
              │   → regulatory exposure  │
              │   → legal / IP risks     │
              │   → competitive moat     │
              │                          │
              │  [CEO Synthesis Agent]   │
              │   → weighs all above     │
              │   → GO / NO-GO / PIVOT   │
              │   → conditions & brief   │
              └────────────┬─────────────┘
                           │
               ┌───────────┴──────────┐
               │                      │
            NO-GO                    GO
               │                      │
          ← archive            ┌──────▼──────────────┐
                               │   BUILD PIPELINE     │   ✅ BUILT
                               │                      │
                               │  BMAD Workflow:      │
                               │  · bmm-analyst       │
                               │  · bmm-pm (PRD)      │
                               │  · bmm-architect     │
                               │  · bmm-ux            │
                               │  · bmm-sm (epics)    │
                               │  · bmm-dev (code)    │
                               │  · bmm-qa (tests)    │
                               └──────┬───────────────┘
                                      │
                               ┌──────▼───────────────┐
                               │   SHIPPED PRODUCT     │   ✅ BUILT
                               │                       │
                               │  · running service    │
                               │  · Archon heartbeat   │
                               │  · port registered    │
                               └──────┬────────────────┘
                                      │
                               ┌──────▼───────────────┐
                               │   FEEDBACK LOOP       │   ❌ MISSING
                               │                       │
                               │  · usage metrics      │
                               │  · AI reads traction  │
                               │  · pivot / scale      │
                               │    recommendation     │
                               │  → feeds back into    │
                               │    idea-capture       │
                               └───────────────────────┘
```

---

## What You've Already Built (Supply Side)

| Component | Status | Where |
|---|---|---|
| Idea capture & ranking | ✅ Done | `idea-capture-web` :3001 |
| Rating system | ✅ Done | idea-capture-web |
| Priority & backlog | ✅ Done | idea-capture-web |
| Idea dispatch to agent | ✅ Done | idea-capture-web |
| PRD generation (bmm-pm) | ✅ Done | BMAD workflow |
| Architecture design (bmm-architect) | ✅ Done | BMAD workflow |
| Epic/story breakdown (bmm-sm) | ✅ Done | BMAD workflow |
| Code implementation (bmm-dev) | ✅ Done | BMAD workflow |
| QA & testing (bmm-qa) | ✅ Done | BMAD workflow |
| Orchestration (Archon) | ✅ Done | :8181 / :3737 |
| Voice boardroom (multi-agent debate) | ✅ Done | voice-boardroom :3007 |
| Sprint tracking & dashboards | ✅ Done | ai-dev-dashboard :3004 |

**You are ~70% complete.** The execution engine is real and proven.

---

## What's Missing (The CEO Brain)

### 1. The Validation Gate (`bmm-validator`)

The gate that sits between "idea" and "build." Runs 4 agents in parallel, synthesizes to a verdict.

**Trigger:** idea reaches a certain rating/priority threshold in idea-capture
**Output:** one-page brief + GO / NO-GO / PIVOT verdict

```
Input: idea title + description + category
   ↓
   ├── Market Agent      → web search → TAM, competitors, pricing
   ├── Devil's Advocate  → top 5 reasons this fails
   ├── Business Model    → 2-3 revenue paths + rough numbers
   └── Risk Agent        → regulatory, legal, moat assessment
   ↓
   CEO Synthesis Agent
   ↓
   Output: verdict + conditions + one-page brief
```

### 2. The Feedback Loop (`bmm-traction`)

After ship, closes the loop. Currently: you ship → silence.

- Reads usage metrics, logs, error rates
- Compares against original hypothesis in the validation brief
- Produces: "Scale / Pivot / Kill" recommendation
- Feeds a new idea back into idea-capture if pivot

---

## The AI Agent Roster (Full Company)

```
STRATEGY LAYER
  bmm-validator    → Validation Gate (CEO Brain)      ← BUILD NEXT
  bmm-traction     → Feedback & pivot signal          ← BUILD LATER

PRODUCT LAYER (existing BMAD)
  bmm-analyst      → Domain & market research
  bmm-pm           → PRD, requirements
  bmm-ux           → UX design, user flows
  bmm-architect    → Technical architecture

EXECUTION LAYER (existing BMAD)
  bmm-sm           → Sprint planning, epics, stories
  bmm-dev (Amelia) → Code implementation
  bmm-qa (Quinn)   → Testing & quality

OPERATIONS LAYER (existing)
  Archon           → State, context, task management
  Alfred           → Home assistant integration
  Voice Boardroom  → Multi-agent live debate
```

---

## The Blood Pressure App — Run Through the Full System

**Idea:** photo of BP monitor → extract reading → save data → trend analysis

### Validation Gate Output (manual run):

**Market Agent:**
- Hypertension affects ~30% of Canadians, ~1.3B people globally
- Most home monitors: no app, or bad app with forced account creation
- Existing: Apple Health (no photo capture), Google Fit (same gap), brand apps (device-locked)
- Gap: device-agnostic, zero-friction logging for any monitor
- TAM: real and large

**Devil's Advocate:**
- Do people who own cheap monitors actually want an app?
- Apple/Google could add this tomorrow
- Health data privacy regulations (PIPEDA in Canada, HIPAA if US)
- Liability if someone acts on wrong extracted reading

**Business Model:**
- B2C: free app + $7/mo AI insights (trend analysis, anomaly alerts)
- B2B: clinic dashboard — patient logs at home, doctor sees 6 months of trends. Worth $50-200/clinic/mo
- Data licensing (de-identified, opt-in) — pharmaceutical / research interest

**Risk Agent:**
- Not a medical device (logging only, no diagnosis) — lower regulatory bar
- Privacy: on-device processing option removes cloud risk
- Moat: dataset of BP readings over time is hard to replicate

**CEO Verdict: GO — with one condition**
> Validate that people with dumb BP monitors actually want this before building the trend layer. Build the photo-extraction MVP first. Get 10 people using it. Then decide on the intelligence layer.

### Build Plan (BMAD pipeline):
1. `bmm-analyst` — competitive deep-dive, user research
2. `bmm-pm` — PRD (photo capture → extraction → storage → basic trend view)
3. `bmm-architect` — Claude Vision API for extraction, local SQLite, PWA
4. `bmm-ux` — mobile-first, 2-tap flow: open → photo → confirm → saved
5. `bmm-sm` — epics & stories
6. `bmm-dev` — build
7. `bmm-qa` — test with real monitors

---

## The Bigger Picture: This IS the Product

The AI Venture Studio is not just your personal tooling. It is a sellable product.

**Who needs it:**
- Solo founders who can code but can't afford a team
- Non-technical founders who need execution without hiring
- Small studios running multiple products

**What makes it different from existing tools:**
- Cursor / Copilot → helps you write code faster
- This → decides WHAT to build, WHY, WHETHER to build it, and then builds it

**The grant story:**
> "An AI-powered venture studio platform that enables solo entrepreneurs to take ideas from concept to shipped product using a multi-agent AI team — covering market validation, product planning, development, and traction analysis."

That's IRAP-eligible. That's Canadian AI innovation. That's a real pitch.

---

## Next Steps

| Priority | Action |
|---|---|
| 1 | Design `bmm-validator` agent spec |
| 2 | Build Validation Gate as BMAD workflow |
| 3 | Run all 18 ideas in idea-capture through it |
| 4 | Take BP app through full pipeline as proof of concept |
| 5 | Design `bmm-traction` feedback loop |
| 6 | Write IRAP grant application using this architecture |

---

*This document was created from a strategic conversation on 2026-03-11.*
*Connected projects: idea-capture-web · voice-boardroom · BMAD · Archon*
