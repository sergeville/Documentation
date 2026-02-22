# Knowledge System - Command Cheat Sheet

**Quick reference for all knowledge management commands**

---

## Daily Commands

```bash
# Capture learning
til "what you learned"

# View recent learnings (last 7 days)
til-show

# View last 30 days
til-show 30
```

---

## Quick Reference Commands

```bash
# List all quick reference guides
quickref --list
qr --list              # shorter alias

# View a guide
quickref Docker
qr Git-Basics          # shorter alias

# Create new guide
quickref --create Kubernetes
qr --create Python-Async
```

---

## Search Commands

```bash
# Search all knowledge
learn "docker networking"
learn "python async"

# View knowledge stats
learn
```

---

## Review Commands

```bash
# Start weekly review (auto-generates template)
review

# View workflow state
workflow
wf                     # shorter alias

# View Archon tasks (requires Claude Code)
tasks
```

---

## Navigation

```bash
# Go to knowledge directory
knowledge

# Direct paths
cd ~/Documents/Knowledge/TIL
cd ~/Documents/Knowledge/QuickRef
cd ~/Documents/Knowledge/Reviews
```

---

## File Locations

| Type | Location |
|------|----------|
| TIL entries | `~/Documents/Knowledge/TIL/2026-02.md` |
| Quick refs | `~/Documents/Knowledge/QuickRef/*.md` |
| Reviews | `~/Documents/Knowledge/Reviews/2026-W07.md` |
| Concepts | `~/Documents/Knowledge/Concepts/` |

---

## Common Workflows

### Morning Routine
```bash
tasks              # Check what to work on
workflow           # View current state
til-show           # Review yesterday's learnings
```

### During Work
```bash
til "learned something"      # Capture immediately
qr Docker                    # Quick lookup
learn "topic"                # Find old note
```

### End of Day
```bash
til-show                     # Review what you learned
```

### End of Week
```bash
review                       # Weekly reflection
```

---

## Tips

- Capture learnings immediately (don't wait)
- Create QuickRef after looking up something 3+ times
- Keep weekly reviews under 15 minutes
- Search your knowledge before asking Claude

---

*Print this and keep it handy until commands are muscle memory*
