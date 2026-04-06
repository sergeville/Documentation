# idea-0022 — Manufacturing Vertical Pivot Brief
*Decision date: 2026-03-28*

---

## Decision

**Selected vertical: Manufacturing (hands-free factory/warehouse floor control)**

Vertical scoring analysis complete. Manufacturing wins on all four decisive axes: MVP feasibility, path to named customer, defensible moat, willingness to pay.

Ruled out:
- **Retail** — commodity space, Alexa/Google own it, no differentiation path
- **Accessibility** — monetization is structurally hard, regulatory overhead disproportionate to early-stage capacity

---

## Problem Statement

Workers on the factory or warehouse floor operate with gloved hands and both hands occupied at all times. Current systems (scanners, tablets, terminals) require manual interaction — a direct conflict with task continuity and OSHA distraction guidelines. The cost is real: workflow interruptions, data entry lag, mislogged units, and supervisors who can't get floor status without walking the line.

Voice is the obvious input modality. The gap is a system that understands factory-floor vocabulary, integrates with existing ops workflows, and satisfies safety constraints without requiring workers to hold a device.

---

## Target Customer Profile

**Primary buyer:** Mid-size manufacturing or warehouse operations manager (50–500 floor workers)

**Profile:**
- Running a line or fulfillment operation with existing WMS/ERP (SAP, NetSuite, Fishbowl, or homegrown)
- Measured on throughput, defect rate, and downtime
- Skeptical of "AI" but will move fast for a floor efficiency tool with a clear ROI
- Has authority to run a pilot without enterprise procurement sign-off
- Pain is daily and visible — not a latent problem

**Geography:** North America, light/medium manufacturing or 3PL warehouse

---

## MVP Scope

**Core principle:** Narrow command set, push-to-activate, local processing preferred.

### Command vocabulary (v1)

| Command | Action |
|---|---|
| "Log unit" | Increment unit count for current task/station |
| "Flag defect" | Open defect log entry (type prompted or defaulted) |
| "Call supervisor" | Push alert to supervisor dashboard with worker ID + station |
| "Next task" | Pull next task assignment from queue |
| "Status" | Read back current task, unit count, time on station |

### Activation model

Push-to-activate (hardware button or wearable trigger). Worker initiates — system does not listen passively. This is the OSHA-compliant pattern and eliminates false-positive anxiety on the floor.

### Processing

Local inference preferred (edge device or on-prem server). Cloud fallback acceptable for v1 pilot if latency is under 400ms. Data sovereignty is a real concern for ops managers — do not require cloud-only.

### Out of scope for MVP

- ERP write-back (logged locally, exported manually in v1)
- Multi-language support
- Custom wake words
- Mobile app

---

## Moat

**Layer 1 — Industry command vocabulary**
General-purpose voice assistants don't know what "flag a Class 2 defect at station 7" means. We build and own the factory-floor command ontology. This compounds with each customer and vertical sub-segment (automotive, pharma, food & bev each have distinct vocabularies).

**Layer 2 — Workflow integration**
ERP/WMS hooks are the stickiness mechanism. Once we're writing to their task queue or defect log, we are embedded in their ops system. Switching cost is high.

**Layer 3 — Edge deployment**
On-prem/local processing builds trust with ops managers who won't send production data to the cloud. This is a real barrier for cloud-native competitors.

---

## First Customer Hypothesis

One plant or warehouse ops manager as a **design partner**, not a paying customer in round one.

Target: someone running a 50–200 person operation who is personally responsible for floor efficiency. They get the MVP free for 60 days in exchange for weekly feedback sessions and permission to use anonymized workflow data.

Success condition for this relationship: they can point to one measurable change in their operation (defect log accuracy, supervisor response time, unit count speed) that they attribute to the pilot.

---

## Regulatory Note

**OSHA push-to-activate pattern** is the safe design decision. Passive always-on listening raises two concerns: (1) worker monitoring/surveillance objections under NLRB interpretations, (2) distraction risk in high-noise/high-hazard environments. Push-to-activate sidesteps both. It is also the pattern workers intuitively trust — they control when the system hears them.

Document this design choice explicitly in any customer-facing materials.

---

## Next Steps — 3 Concrete Actions

### 1. Draft outreach template for design partner recruitment
Write a 200-word cold email targeting ops managers at mid-size manufacturers. Lead with the problem (gloved hands, manual data entry lag), offer a free 60-day pilot, ask for a 20-minute discovery call. Target 10 sends in week 1.

### 2. Define the complete MVP feature list
Expand the 5-command vocabulary into a full feature spec: exact command grammar, confirmation audio patterns, error handling ("didn't catch that"), station/worker ID binding, local log format, and supervisor alert schema. This becomes the build brief for the MVP sprint.

### 3. Define pilot success criteria
Before outreach, define what "pilot worked" means in measurable terms:
- Defect log entries per shift (baseline vs. pilot)
- Supervisor alert response time
- Worker adoption rate (% of eligible workers using the system by week 4)
- Net Promoter Score from ops manager at 60-day close

These criteria go into the design partner agreement upfront.

---

## Reference

- Vertical scoring analysis: completed 2026-03-28 (session context)
- Follow-up sprint task: `[idea-0022] Define manufacturing voice MVP — command set + pilot customer outreach`
- idea-0022 status: `decided`

---

## Sprint Deliverables
*Produced: 2026-03-28*

The three next-step actions defined above have been executed. Deliverables:

| Track | Document | What it contains |
|---|---|---|
| A — MVP Feature Spec | [idea-0022-mvp-feature-spec.md](idea-0022-mvp-feature-spec.md) | 14-command vocabulary table (4 categories), activation model comparison, tech stack recommendation (Whisper local vs. cloud, platform options, integration point), v1 scope boundary, and per-component build estimates (4–6 weeks to pilot-ready) |
| B — Pilot Customer Outreach | [idea-0022-outreach-template.md](idea-0022-outreach-template.md) | Cold LinkedIn message (<300 chars), cold email (subject + body, <200 words), target persona definition, industry sub-vertical prioritization, LinkedIn search strings, week-1 outreach cadence |
| C — Pilot Success Criteria | [idea-0022-pilot-success-criteria.md](idea-0022-pilot-success-criteria.md) | Quantitative metrics (accuracy, adoption, time saved), qualitative green/red signals, hard-stop failure conditions, 4-week pilot structure, go/no-go decision framework, minimum design partner agreement terms |

**Critical path for next session:** hardware procurement lead time is the build bottleneck — order edge server and BT headsets before the sprint starts. Outreach can run in parallel with the build.
