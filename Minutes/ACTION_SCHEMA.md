# Minutes Action Schema

This is the canonical schema for machine-readable action items in Synapse session minutes.

Archon reads this archive as a source of operational memory. Keep action items structured so unresolved work can be surfaced without scraping prose.

## Action Section Format

Each minutes file may include:

```markdown
## Open Actions  <!-- use this exact heading in real session minutes only -->

- [open] Short operator-readable action.
  - action_id: stable-kebab-case-id
  - owner: codex
  - next_step: concrete next action
  - story_id: 59-6
  - task_id: archon-task-id
  - epic_id: 59
  - sprint_id: 49
```

## Status Marker

Put the lifecycle status in the action line:

- `[open]`: unresolved work that should appear in Archon open loops
- `[carried]`: unresolved work carried forward from an earlier session
- `[blocked]`: unresolved work blocked on a decision, dependency, or human action
- `[done]`: resolved work that should suppress earlier open entries with the same `action_id`

## Required Fields

- `action_id`: stable loop identity. Use the same value when carrying or closing the loop.
- `owner`: accountable operator or agent.
- `next_step`: concrete next action, not a broad goal.

## Traceability Fields

Use these whenever the action maps to canonical delivery state:

- `story_id`: BMAD story id, for example `77-2`
- `task_id`: Archon task id
- `epic_id`: BMAD epic id
- `sprint_id`: BMAD sprint id

If an id does not exist yet, omit it rather than inventing a placeholder. Add it when the object is created.

## Optional Resolution Fields

Resolved actions may include:

- `closed_at`: closure date in `YYYY-MM-DD`
- `resolution`: short explanation of what closed the loop
- `evidence`: links or paths to PRs, validation notes, story files, or runtime probes

Example:

```markdown
- [done] Restore agent-work-orders visibility.
  - action_id: agent-work-orders-visibility
  - owner: codex
  - next_step: closed by Story 77-2
  - closed_at: 2026-04-24
  - resolution: Direct AWO health and Archon proxy list both returned 200.
  - evidence:
    - https://github.com/sergeville/Synapse/pull/28
```

## Parser Contract

Archon currently parses these metadata fields:

- `action_id`
- `owner`
- `status`
- `next_step`
- `story_id`
- `task_id`
- `epic_id`
- `sprint_id`
- `carried_from`

Additional bullet details are preserved as human-readable `details` and `detail_text`.
