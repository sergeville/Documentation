# AI Venture Studio — Implementation Plan

**Created:** 2026-03-11
**Ref doc:** `Documentation/AI-VENTURE-STUDIO.md`
**Goal:** Complete the machine that builds products — Validation Gate + Feedback Loop

---

## North Star

> One person. Full company. AI handles every step from idea to traction signal.
> You provide vision and final calls. AI provides everything else.

---

## Current State

```
✅ Idea Intelligence (idea-capture)
✅ Build Pipeline (BMAD)
✅ Orchestration (Archon)
✅ Voice Boardroom (multi-agent debate)

❌ Validation Gate — the CEO Brain  ← Phase 1
❌ Feedback Loop — traction signal   ← Phase 2
❌ Packaged as a product             ← Phase 3
```

---

## Phase 1 — The Validation Gate (CEO Brain)

**Duration:** ~2 weeks
**Outcome:** Any idea in idea-capture can be run through a 4-agent analysis and receive a GO / NO-GO / PIVOT verdict in under 5 minutes.

### Epic 1.1 — Market Research Agent

**What it does:** Given an idea title + description, performs web research and returns a structured market brief.

Stories:

- [ ] **1.1.1** — Create `bmm-validator` agent skeleton in BMAD agents folder
- [ ] **1.1.2** — Implement Market Agent prompt: TAM estimate, top competitors, pricing signals, trend direction
- [ ] **1.1.3** — Connect to web search (WebSearch tool or Perplexity API)
- [ ] **1.1.4** — Output: structured JSON `{tam, competitors[], pricing, trend, summary}`

### Epic 1.2 — Devil's Advocate Agent

**What it does:** Argues hard against the idea. Surfaces the real risks before any work starts.

Stories:

- [ ] **1.2.1** — Implement Devil's Advocate prompt: top 5 failure modes, substitutes, timing risks
- [ ] **1.2.2** — Force contrarian stance — agent must find at least 3 reasons to kill the idea
- [ ] **1.2.3** — Output: structured JSON `{risks[], substitutes[], fatal_flaw, survivable_risks[]}`

### Epic 1.3 — Business Model Agent

**What it does:** Generates 2-3 monetization paths with rough unit economics.

Stories:

- [ ] **1.3.1** — Implement Business Model prompt: B2C / B2B / hybrid options
- [ ] **1.3.2** — For each path: pricing benchmark, rough LTV, acquisition cost estimate
- [ ] **1.3.3** — Output: structured JSON `{options[{model, price, tam_capture, ltv, cac_est}], recommended}`

### Epic 1.4 — Risk Agent

**What it does:** Flags regulatory, legal, IP, and competitive moat risks.

Stories:

- [ ] **1.4.1** — Implement Risk Agent prompt: regulatory exposure (Canada), legal risks, IP landscape
- [ ] **1.4.2** — Include moat assessment: what stops a well-funded competitor from copying this
- [ ] **1.4.3** — Output: structured JSON `{regulatory, legal, ip, moat_strength, moat_description}`

### Epic 1.5 — CEO Synthesis Agent

**What it does:** Reads all 4 agent outputs. Produces a final verdict and one-page brief.

Stories:

- [ ] **1.5.1** — Implement CEO Synthesis prompt: weigh market vs risks vs business model
- [ ] **1.5.2** — Output verdict: `GO` / `NO-GO` / `PIVOT` with confidence score (0-100)
- [ ] **1.5.3** — Output conditions: what must be true for GO to hold
- [ ] **1.5.4** — Generate one-page brief (markdown): summary, verdict, key risks, recommended first step

### Epic 1.6 — Integration with idea-capture

**What it does:** Connect the Validation Gate to the existing idea-capture pipeline.

Stories:

- [ ] **1.6.1** — Add "Validate" button to idea-capture UI per idea
- [ ] **1.6.2** — POST idea to new `/api/validate` endpoint → triggers 4-agent parallel run
- [ ] **1.6.3** — Store validation brief in Archon: `validation:<idea-id>`
- [ ] **1.6.4** — Display verdict badge on idea card (GO green / NO-GO red / PIVOT orange)
- [ ] **1.6.5** — Link to full brief from idea detail view

### Epic 1.7 — Run All Existing Ideas

**What it does:** Validate all 18 ideas currently in idea-capture backlog.

Stories:

- [ ] **1.7.1** — Run BP Monitor through Validation Gate — produce first real brief
- [ ] **1.7.2** — Run all 18 ideas in batch
- [ ] **1.7.3** — Rank ideas by validation score — update idea-capture priority accordingly
- [ ] **1.7.4** — Kill or archive ideas that score NO-GO

---

## Phase 2 — Build the Proof of Concept (BP Monitor)

**Duration:** ~1 week (weekend + polish)
**Outcome:** Working app — photo of any BP monitor → reading extracted → stored → trend visible.
**Purpose:** Prove the full pipeline works end-to-end, from Validation Gate through BMAD to shipped product.

### Epic 2.1 — Run BP Monitor Through BMAD

Stories:

- [ ] **2.1.1** — `bmm-analyst`: competitive research, user persona (hypertension patient, caregiver)
- [ ] **2.1.2** — `bmm-pm`: PRD — photo capture, Claude Vision extraction, local storage, trend chart
- [ ] **2.1.3** — `bmm-architect`: Claude Vision API + SQLite + PWA (mobile-first)
- [ ] **2.1.4** — `bmm-ux`: 2-tap flow — open → photo → confirm reading → saved
- [ ] **2.1.5** — `bmm-sm`: epics + stories breakdown
- [ ] **2.1.6** — `bmm-dev`: implement
- [ ] **2.1.7** — `bmm-qa`: test with real monitors (multiple brands)

### Epic 2.2 — Alfred Integration

Stories:

- [ ] **2.2.1** — "Alfred, log my BP" → prompts for photo → auto-logged
- [ ] **2.2.2** — Alfred can answer "What was my BP last week?" from stored data

---

## Phase 3 — Feedback Loop (Traction Signal)

**Duration:** ~1 week
**Outcome:** After a product ships, an AI agent monitors usage and produces a Scale / Pivot / Kill recommendation.

### Epic 3.1 — Traction Monitor Agent (`bmm-traction`)

Stories:

- [ ] **3.1.1** — Define metrics to track per product (usage frequency, retention, errors)
- [ ] **3.1.2** — Implement traction agent: reads logs/metrics → compares to validation brief hypothesis
- [ ] **3.1.3** — Weekly report: "Hypothesis was X. Reality is Y. Recommendation: Scale / Pivot / Kill"
- [ ] **3.1.4** — If Pivot: generate new idea and push to idea-capture automatically
- [ ] **3.1.5** — Store traction report in Archon: `traction:<product-id>:<week>`

### Epic 3.2 — Dashboard Integration

Stories:

- [ ] **3.2.1** — Add traction panel to ai-dev-dashboard per shipped product
- [ ] **3.2.2** — Show: hypothesis vs reality, current recommendation, trend arrow

---

## Phase 4 — Package as a Product (Optional / Grant Phase)

**Duration:** TBD — only after Phase 1-3 proven
**Outcome:** The AI Venture Studio as a standalone product other solo founders can use.

### Epic 4.1 — Productize

Stories:

- [ ] **4.1.1** — Extract BMAD + Validation Gate + Feedback Loop into a standalone installable
- [ ] **4.1.2** — Remove Serge-specific hardcodes, make fully configurable
- [ ] **4.1.3** — Landing page + onboarding flow
- [ ] **4.1.4** — Pricing: freemium (3 ideas/mo free) + $29/mo unlimited

### Epic 4.2 — Grant Application

Stories:

- [ ] **4.2.1** — Write IRAP application using AI Venture Studio as the product
- [ ] **4.2.2** — Prepare demo: run one idea through the full pipeline live
- [ ] **4.2.3** — Apply to Scale AI acceleration program

---

## Milestones

| # | Milestone | Target | Done when |
|---|---|---|---|
| M1 | Validation Gate live | End of Phase 1 | Any idea can be validated in <5 min |
| M2 | All 18 ideas validated | End of Phase 1 | Backlog is ranked by validation score |
| M3 | BP app shipped | End of Phase 2 | Photo → reading → trend working on phone |
| M4 | Full pipeline proven | End of Phase 2 | Idea → validated → built → shipped in one flow |
| M5 | Feedback loop live | End of Phase 3 | Weekly traction report generated automatically |
| M6 | Grant application filed | Phase 4 | IRAP or Scale AI application submitted |

---

## Agent Build Order

Build in this order — each one enables the next:

```
1. bmm-validator (Market Agent)       → validates ideas exist in a market
2. bmm-validator (Devil's Advocate)   → stops bad ideas before wasted work
3. bmm-validator (Business Model)     → ensures there's a revenue path
4. bmm-validator (Risk Agent)         → surfaces blockers early
5. bmm-validator (CEO Synthesis)      → produces actionable verdict
6. Integration with idea-capture      → closes the loop on the supply side
7. BP Monitor MVP                     → first full end-to-end proof
8. bmm-traction                       → closes the loop on the demand side
```

---

## Technical Decisions

| Decision | Choice | Reason |
|---|---|---|
| Validation agent type | BMAD agent (Claude Sonnet) | Consistent with existing stack |
| Web search in validation | WebSearch tool | Already available in Claude Code |
| Validation storage | Archon context keys | Consistent with existing ops pattern |
| BP photo extraction | Claude Vision API | No new infra, high accuracy |
| BP data storage | SQLite local | Privacy-first, no cloud required |
| BP app type | PWA (mobile-first) | Works on iPhone, no App Store |

---

## Success Definition

The system is complete when:

1. Serge has an idea at 9pm
2. Validation Gate runs overnight — produces GO verdict with conditions
3. BMAD pipeline starts in the morning — PRD, arch, stories ready by noon
4. bmm-dev builds the MVP — shipped by end of day
5. bmm-traction monitors it — weekly report tells Serge if it's working

**One person. Zero team. Full company. AI does everything except deciding.**

---

*Plan created: 2026-03-11*
*Ref: Documentation/AI-VENTURE-STUDIO.md*
