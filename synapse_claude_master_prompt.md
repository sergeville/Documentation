# SYNAPSE Prompt Package

## Included reference asset

Use the attached image file **`SYNAPSE.png`** as the primary visual reference for the design system, theme, layout language, and interface tone described in this prompt.

When using this prompt in Claude, provide **both files together**:

- `synapse_claude_master_prompt.md`
- `SYNAPSE.png`

The image is not decorative. It is the visual source of truth for:
- typography mood
- panel construction
- blueprint-grid background treatment
- control-plane layout
- metadata strip styling
- button and table feel
- spacing discipline
- border treatment
- overall SYNAPSE aesthetic

---

# Claude Code Master Prompt — SYNAPSE Workspace Control (Style-Aligned)

You are Claude Code acting as a senior platform architect, design-systems lead, and implementation engineer.

Your task is to design the foundation for a unified workspace platform called **SYNAPSE** and produce a concrete, implementation-oriented architecture package that a developer can begin building immediately.

Do **not** give a vague product essay.  
Produce a **build-oriented plan** with practical structure, contracts, conventions, implementation guidance, and a style system aligned to the attached reference image.

---

## Reference Style Direction

Use the provided SYNAPSE UI screenshot as the **primary visual reference** for the platform’s design language.

### The visual system should inherit these qualities from the reference image:

- **Blueprint / engineering console aesthetic**
- **Retro-futuristic control-plane feel**
- **Cream / off-white drafting-paper background**
- **Fine grid overlay** across the workspace
- **Deep cobalt / blueprint blue** as the primary accent
- **Sparse use of status colors** for health and state indicators
- **Technical labeling language** with uppercase micro-labels and metadata strips
- **Panelized interface** with clearly segmented operational zones
- **Monospaced / technical microcopy feel** for metadata and labels
- **Bold industrial headline typography** for the SYNAPSE identity
- **Thin borders, precision spacing, and schematic framing**
- **System-dashboard look**, not consumer-SaaS softness
- **Minimal, disciplined motion**, like a real operations console
- **Visual hierarchy based on information architecture**, not decoration

### Important design interpretation rules

The system should feel like:

- an **AI operating system**
- a **workspace control deck**
- a **mission console / orchestration plane**
- a **neuro-cybernetic engineering dashboard**
- a **single source of truth for connected tools**

It should **not** feel like:

- a generic admin dashboard
- a glossy startup landing page
- a playful neon cyberpunk UI
- a rounded-card modern SaaS template
- a cluttered monitoring screen

---

# PROJECT INTENT

We have multiple tools living in separate subfolders/modules/apps.  
We want to make them feel like **one connected product ecosystem**.

We need a central place called:

# SYNAPSE — Workspace Control

SYNAPSE will be the main control layer / workspace shell / launcher.

From SYNAPSE, the user should be able to:

- see available tools
- launch any tool
- move between tools
- keep shared workspace/session context
- maintain a consistent visual identity across all tools

---

# CRITICAL REQUIREMENTS

## 1) Centralized access
Every tool/subfolder must be reachable from SYNAPSE through a standard integration pattern.

## 2) Shared look and feel
All tools must share the same:
- fonts
- theme
- color system
- spacing rhythm
- UI language
- component feel
- navigation feel

All tools should visually feel like they belong to SYNAPSE.

## 3) Caller awareness inside every tool
This is one of the most important requirements.

When a tool is opened, it must know:
- who launched it
- what launched it
- from where it was launched
- which workspace is active
- which session is active
- what entity/item/task triggered the launch
- what the launch intent was

Example:
If SYNAPSE launches a tool from a project card, that destination tool should know:
- it was launched from SYNAPSE
- which user/session/workspace initiated it
- which page/card/entity launched it
- whether the intent is inspect/edit/analyze/continue

This requirement is mandatory, not optional.

## 4) Cross-tool communication
Tools must be able to communicate back to SYNAPSE, for example:
- opened
- ready
- failed
- completed action
- request navigation
- request opening another tool
- update context

## 5) MCP investigation
Investigate whether MCP makes sense for:
- tool discovery
- capability registration
- interoperability
- LLM/tool calling compatibility

But do not force MCP if it adds unnecessary complexity.  
If it helps, explain exactly where it fits.  
If it does not help, propose a better alternative.

## 6) Graceful standalone mode
Tools may still need to run standalone, but when launched from SYNAPSE they must become context-aware and workspace-integrated.

---

# WHAT I WANT YOU TO PRODUCE

Act like you are preparing the real implementation foundation for a repo.

Produce the following sections in order:

---

# 1. Executive Summary
A plain-English explanation of the architecture and why it is the recommended default.

---

# 2. Recommended Default Architecture
Define the best architecture for:
- SYNAPSE shell
- tool registry
- launch mechanism
- shared design system
- shared workspace SDK
- event bus
- caller-awareness/context broker
- optional MCP layer

Be decisive. Pick a default approach.

---

# 3. MVP Architecture vs Future-State Architecture
Split the proposal into:
- MVP version we can build first
- future-state version once the foundation is proven

The MVP should be realistic and not over-engineered.

---

# 4. Tool Integration Contract
Define the minimum contract every tool must support to become SYNAPSE-compatible.

Include:
- required metadata
- required lifecycle hooks
- required context handling
- required theme support
- required event support
- expected fallback behavior when standalone

Present this like a practical internal standard.

---

# 5. Caller-Awareness Design
This section must be detailed.

Explain how a destination tool knows:
- source app
- caller tool/page
- user identity
- workspace identity
- session identity
- origin entity
- launch intent
- return path
- permissions/role context if relevant

Include:
- recommended context schema
- launch token option
- secure vs non-secure context fields
- when to use URL params vs memory vs signed token vs postMessage vs backend lookup

I want a strong recommendation, not just options.

Provide example JSON.

---

# 6. Cross-Tool Communication Model
Define how tools communicate with SYNAPSE and possibly with each other.

Include:
- event bus recommendation
- event naming convention
- minimal event payload shape
- examples like:
  - tool.opened
  - tool.ready
  - tool.error
  - tool.request.navigate
  - tool.request.open_related
  - tool.context.updated
  - tool.action.completed

Explain whether communication should be direct tool-to-tool or always routed through SYNAPSE.

---

# 7. Design System / Theming Strategy
Explain how all tools inherit the same style as SYNAPSE without duplicating CSS.

This section must explicitly use the attached image as style reference and translate it into implementation rules.

Include:
- token strategy
- typography system
- grid/background treatment
- border system
- spacing scale
- component package
- shell layout primitives
- panel anatomy
- metadata strip style
- table/control-plane styling
- status indicator rules
- dark/light support strategy if any
- brand enforcement rules
- how legacy tools can gradually adopt the theme

Also define:
- what the likely font pair should be
- what should be headline font behavior vs metadata font behavior
- how buttons, pills, status chips, headers, tables, and control rows should feel
- how much rounding is allowed
- how shadows should be handled
- how animation should be handled

Make this practical and specific.

---

# 8. Monorepo / Folder Structure Proposal
Propose a maintainable folder structure.

Include something like:
- apps/
- packages/
- configs/
- manifests/
- sdk/
- design-system/
- event-bus/

Explain why the structure works.

---

# 9. Suggested Package / Module Breakdown
Define the internal packages/modules we should likely create, such as:
- @synapse/design-system
- @synapse/workspace-sdk
- @synapse/tool-registry
- @synapse/event-bus
- @synapse/theme-tokens
- @synapse/context-broker

For each, explain:
- purpose
- responsibilities
- example exports

---

# 10. Example Tool Manifest
Provide a realistic example manifest structure for registering tools.

Include fields such as:
- id
- name
- icon
- route/entry
- launchMode
- version
- capabilities
- permissions
- contextAware
- themeAware
- standaloneSupported

Use example JSON.

---

# 11. Example Workspace SDK API
Define a small starter SDK API that tools would consume.

For example:
- getLaunchContext()
- getCallerInfo()
- getTheme()
- notifyReady()
- publishEvent()
- requestNavigation()
- requestOpenTool()
- getSession()

Provide sample TypeScript interface ideas or pseudocode.

---

# 12. Launch Flow
Describe the exact launch lifecycle from click to tool ready.

For example:
1. User clicks tool in SYNAPSE
2. SYNAPSE resolves workspace/session/user context
3. SYNAPSE creates launch payload or token
4. SYNAPSE opens tool
5. Tool bootstraps SDK
6. Tool resolves launch context
7. Tool applies theme
8. Tool reports ready
9. SYNAPSE updates control state

Be explicit.

---

# 13. Implementation Roadmap
Break the work into phases/sprints.

I want a phased roadmap such as:
- Phase 1: platform contract
- Phase 2: SYNAPSE shell foundation
- Phase 3: shared packages
- Phase 4: pilot tool integration
- Phase 5: scaleout / observability / advanced interoperability

Each phase should include:
- goals
- deliverables
- dependencies
- exit criteria

---

# 14. Risks and Mitigations
Call out realistic technical/product risks, for example:
- tools built in different stacks
- incomplete theme adoption
- broken context after refresh
- too much complexity too early
- MCP overreach
- event sprawl
- state synchronization issues

Give concrete mitigations.

---

# 15. Success Criteria
Define what “done” looks like for MVP and for full platform success.

---

# 16. Strong Recommendation
At the end, give:
- your recommended default architecture
- your recommended MVP scope
- whether MCP should be included now, later, or not at all

Be direct.

---

# VERY IMPORTANT OUTPUT RULES

## Output style
- Use clear headings
- Be practical and implementation-oriented
- Prefer specific recommendations over generic options
- Include examples
- Include JSON where appropriate
- Include TypeScript-style pseudocode where helpful
- Avoid buzzword-heavy fluff

## Important
I do NOT want you to start coding the full product yet.  
I want the **architecture-and-implementation package** that a developer could use as the basis for building it.

## Extra requirement
At the very end, provide a section called:

# Starter Repo Blueprint

This should include:
- recommended first folders to create
- first files to write
- what to implement first
- what to stub/mock initially
- what to defer until later

This should feel like a practical first build sequence.

---

# ADDITIONAL STYLE TRANSLATION TASK

Before the architecture section, include a dedicated section called:

# Visual Reference Translation

In that section, explicitly extract the design language from the attached image and convert it into:

- design principles
- UI rules
- token guidance
- typography guidance
- panel rules
- table rules
- shell layout rules
- motion rules
- do / don’t guidance

This section should help a developer or designer reproduce the SYNAPSE visual language consistently across all tools.

---

Now generate the full architecture package.
