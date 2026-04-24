# Minutes — 2026-04-14 13:24–14:31
## Cockpit Bird's-Eye Containment Refinement

**Attendees:** Serge, Codex
**Duration:** ~67 minutes
**Workspace:** `~/Dev/Synapse/`
**Branch:** `birds-eye-level`

---

## Session Summary

**Refined the Cockpit futuristic prototype into a containment-first bird's-eye operator surface aligned to Archon's `project -> epic -> task` model, wired it to live state, pushed the feature branch, and opened the PR.**

The session moved in four phases:
- clarified the operator model around `intent -> route -> project -> epic -> task`, with lifecycle treated as context instead of the primary spine
- remapped the prototype to canonical Archon containment and added live project/epic selection
- ran repeated readability passes so the first screen reads as selected project, selected epic, current gate, and visible proof
- pushed `birds-eye-level` and created the PR for review

---

## Phase 1: Model Correction

### Core decision
The prototype should not lead with a flat lifecycle chain. The primary user model is:
- `project -> epic -> task`
- lifecycle as context
- approval and proof as visible truth layers

### Important framing changes
- `intent` became the broader root concept instead of forcing everything into `idea`
- `brainstorming` was treated as an exploration phase, not a permanent work container
- bare labels like `Done` or `Planning complete` were treated as ambiguous unless bound to an object or scope

---

## Phase 2: Containment + Live Wiring

### Main files changed
- `~/Dev/Synapse/claude-cockpit/futuristic-prototype.html`
- `~/Dev/Synapse/claude-cockpit/server.py`

### What changed
- added live hydration from cockpit runtime endpoints
- aligned the prototype with Archon project/epic containment data
- added project selection to the bird's-eye view
- added epic selection with downstream task/approval/proof scoping
- made narrative, flow, corridor, and proof follow the selected epic context
- exposed project/epic cluster data through cockpit for the prototype to consume

### Validation completed
- repeated `node --check` on the prototype script
- repeated live route checks on `http://localhost:3027/futuristic-prototype`
- browser and headless interaction smoke passes for project/epic switching

---

## Phase 3: Readability Passes

### Main visual changes
- made the system view containment-first
- moved project selection and epic containment above the fold
- simplified the center system path so it supports the selected cluster instead of competing with it
- aligned the header, left rail, and inspector to the selected project/epic context
- reduced topbar density
- tightened system copy and strengthened visual hierarchy

### Intended first-screen read
- selected project
- selected epic
- current human gate
- visible proof

### Important remaining limitation
`Intent` and parts of `Proof/Result` are still inferred in the UI. They are not yet canonical backend objects.

---

## Phase 4: Branch + PR

### Branch status
- feature branch created and used: `birds-eye-level`
- branch pushed to origin and set to track `origin/birds-eye-level`

### PR created
- `https://github.com/sergeville/Synapse/pull/1`

### Cockpit commit sequence
- `493ace6` Add cockpit bird's-eye prototype
- `bfebb0a` Bind cockpit bird's-eye prototype to live state
- `ffb4088` Align cockpit prototype with Archon containment model
- `9735129` Make cockpit bird's-eye view containment-first
- `8e525e5` Scope cockpit narrative to selected epic context
- `39143d8` Add project selection to cockpit bird's-eye view
- `03c98c0` Fix cockpit project selector click handling
- `68c975d` Refine cockpit bird's-eye containment layout
- `6ec2d63` Align cockpit header signals with selected cluster
- `43d5325` Simplify cockpit system path focus
- `b6b5b68` Align cockpit left rail with selected cluster
- `2365826` Reduce cockpit topbar density
- `74f1ec2` Tighten cockpit system copy
- `ea213e8` Strengthen cockpit visual hierarchy

---

## Key Decisions

1. **Containment leads.**
   The operator should see `project -> epic -> task` before any abstract lifecycle framing.

2. **Lifecycle is context, not the primary spine.**
   Project phase should inform the view, not replace containment.

3. **Approval and proof stay visible as first-class layers.**
   Humans need to see what is gated and what evidence exists without drilling into implementation details.

4. **Selection context must stay coherent across the whole page.**
   When a project or epic changes, narrative, flow, corridor, header, and inspector must all follow it.

5. **Readability matters as much as data correctness.**
   The page only works if a human can understand it quickly from the first screen.

---

## Next Session Priorities

1. Promote canonical backend objects for:
   - `Intent`
   - `Proof/Result`

2. Decide whether the PR should stay prototype-only or begin moving parts of the containment model into the main cockpit surface.

3. Review the PR diff carefully to keep the scope limited to cockpit changes.

4. If approved, continue with backend truth work instead of adding more visual complexity.
