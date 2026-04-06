# Session Minutes — 2026-04-04 10:53
**Agent:** Claude (Opus 4.6)
**Duration:** ~90 min
**Theme:** Housekeeping, cleanup, and pipeline hygiene

## Decisions Made
1. **Supabase cloud account deletion** — submitted via dashboard. Account: villeneuve.serge@gmail.com. Projects: MyArchonKnowledge + Alfred's Project. Awaiting email confirmation (up to 30 days).
2. **Reminders reorganized** — consolidated 14 scattered lists into 5 categories: Shopping, Health, Personal, Tech / Dev, Today. Deleted 7 empty lists via AppleScript. Shared/Exchange lists need manual drag (AppleScript limitation).
3. **Archon task cleanup** — 3 stale "doing" tasks moved back to todo. Supabase revocation task marked done.
4. **Cockpit scrollbar fix** — body/main had `overflow: hidden` preventing page scroll. Fixed to `overflow-y: auto` + `min-height: 100vh`. Sprint board columns got `min-height: 0` for proper flexbox scrolling.
5. **Idea pipeline triage** — 11 auto-captured anomaly "ideas" (idea-0084 through idea-0094) evaluated as NO-GO and discarded. All were resolved infrastructure incidents, not product ideas.

## Issues Found
- **AppleScript + shared Reminders lists** — `move` and property iteration fail on collaborative (shared) lists and Exchange lists. Workaround: copy name/body to new list, delete original. Still unreliable for bulk operations.
- **ai-idea-analyst pollution** — agent auto-captures supervisor anomalies as "ideas" in the pipeline. Root cause: no filter distinguishing incidents from product ideas. Needs fix.
- **ai-orchestrator LLM routing failing** — every tick shows "LLM routing failed — skipping tick" (1500+ ticks). Likely OpenAI budget or config issue. Not blocking but wasting cycles.

## Rejected Ideas
- None explicitly rejected.

## New Feedback Rules
- **Close the idea pipeline loop** — when resolving bugs/incidents, always check for matching idea pipeline entries and close them. Saved to memory.

## Late Session Work (12:00--12:43)
1. **Idea Flow backlog bug fixed** -- `archon_tasks()` only fetched page 1 of 497 tasks (all done). Fixed: 3 targeted API calls with `?status=todo/doing/done`. Backlog now shows 17 tasks. SCOUT diagnosed, FORGE fixed.
2. **Auto-refresh on Idea Flow** -- already had 5s interval, confirmed working at 10s.
3. **Idea pipeline cleaned** -- 11 auto-captured anomaly ideas (idea-0084 to 0094) discarded as NO-GO. 2 test ideas also deleted. Pipeline is clean.
4. **First real idea captured** -- idea-0095: "Make Synapse user-agnostic -- dynamic user identity for new installations" (high priority, blocks distribution).
5. **New behavior rules saved to memory:**
   - Auto-capture user requests as ideas in pipeline
   - Close idea pipeline loop when work is done
   - Delegate to specialist agents in parallel (don't solo everything)
6. **Cockpit scrollbar fix** -- body overflow changed to scrollable, sprint board columns got min-height:0 for proper flexbox scrolling.
7. **Archon task cleanup** -- 3 stale "doing" tasks moved to todo, Supabase revocation marked done.

**Idea Flow / Cockpit relationship clarified:** Idea Flow is the idea funnel (capture, triage, prioritize). Cockpit is the execution dashboard (sprint board, agent activity, escalations). They feed into each other -- ideas graduate from Idea Flow into Cockpit when they become stories/tasks.

## Pending (Manual by Serge)
- Reminders: drag items from Péllules Médicamant → Health, Electrical Shopping → Shopping, Jupette → Personal
- Reminders: review GPT3 list (22 items), delete stale Exchange lists
- Reminders: delete Monaco Diplomat, Docteur, Serge todo list manually
