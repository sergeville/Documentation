# Knowledge Management System Quick Start

**Last Updated:** 2026-02-14

---

## Daily Workflow

```bash
# Morning: Check what you're working on
tasks              # View Archon task list (via Claude)
workflow           # View workflow state

# During work: Capture learnings as you go
til "Learned X about Y"
til "Docker networks use bridge mode by default"
til "Python async: await inside async def only"

# End of day: Review what you learned
til-show           # View today's learnings

# End of week: Reflect and consolidate
review             # Start weekly review
```

---

## Quick Reference Guides

```bash
# List all quick refs
quickref --list
qr --list          # Same (shorter alias)

# View a specific guide
quickref Docker
qr Python-Async

# Create new guide
quickref --create Kubernetes
qr --create Git-Advanced

# Search across all knowledge
learn "docker networking"
learn "async patterns"
```

---

## Key Commands

| Command | Purpose |
|---------|---------|
| `til "..."` | Capture what you learned |
| `til-show` | View recent learnings (7 days) |
| `learn "topic"` | Search knowledge base |
| `quickref --list` | List all quick refs |
| `quickref Topic` | View quick ref |
| `review` | Start weekly review |
| `knowledge` | Go to knowledge directory |

---

## Directory Structure

```
~/Documents/Knowledge/
├── TIL/              # Today I Learned (monthly files)
├── QuickRef/         # Quick reference guides
├── Reviews/          # Weekly reviews
├── Concepts/         # Deep dive documents
└── README.md         # System overview
```

---

## Best Practices

### TIL Entries
✅ **Good**: Specific, actionable insights
```bash
til "Docker: Use --network=host to access localhost from container"
til "Python: asyncio.gather() runs tasks concurrently, returns list"
```

❌ **Avoid**: Vague or obvious statements
```bash
til "Worked on Docker stuff"  # Too vague
til "Python is a language"     # Too obvious
```

### Quick References
- One guide per major topic
- Focus on commands you forget
- Include examples, not just syntax
- Update when you learn new patterns

### Weekly Reviews
- Friday afternoon or Sunday evening
- 10-15 minutes max
- Focus on insights, not just activities
- Note patterns and recurring themes

---

## Integration with Archon

Your knowledge system works alongside Archon:

- **Archon**: Task tracking, project coordination
- **TIL**: Personal learning capture
- **Reviews**: Reflection and consolidation
- **QuickRef**: Just-in-time reference

Together they form your **external brain**.

---

## Examples

### Research Session
```bash
# Start
tasks                              # Check what to work on

# During research
til "K8s: Pods are smallest deployable units"
til "K8s: Services provide stable networking"
til "K8s: ConfigMaps for configuration data"

# After research
quickref --create Kubernetes       # Create reference guide
learn kubernetes                   # Verify it's captured
```

### Weekly Workflow
```bash
# Friday or Sunday
review                             # Start weekly review
# Review opens template with this week's TILs auto-filled
# Add reflections, patterns, next week's focus

# View past reviews
ls ~/Documents/Knowledge/Reviews/
```

---

## Productivity Tips

1. **Capture immediately**: Don't wait - TIL when you learn it
2. **Review weekly**: Consolidate knowledge, spot patterns
3. **Build quick refs**: For topics you reference often
4. **Search first**: Before asking Claude, search your knowledge
5. **Share with AI**: Claude can analyze your TILs for patterns

---

## Advanced Usage

### Ask Claude to Analyze Your Learning
```
"Analyze my TIL entries from the past month and identify patterns"
"What topics have I been learning about most?"
"Create a quick reference guide from my TIL entries about Docker"
```

### Export for Obsidian/Notion
All files are markdown - compatible with:
- Obsidian
- Notion
- Logseq
- Any markdown editor

### Search with mdfind (macOS Spotlight)
```bash
mdfind -onlyin ~/Documents/Knowledge "docker networking"
```

---

## Next Steps

1. Try it out: `til "Learned about the knowledge system"`
2. Create your first quick ref: `quickref --create YourTopic`
3. At end of week: `review`
4. Ask Claude to help analyze your learnings

---

*This is YOUR knowledge base. Make it work for you.*
