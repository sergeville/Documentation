# Knowledge Management System

Your personal knowledge base for continuous learning and productivity.

## Directory Structure

```
Knowledge/
├── TIL/              # Today I Learned - daily discoveries
├── QuickRef/         # Quick reference guides and cheat sheets
├── Reviews/          # Weekly/monthly learning reviews
├── Concepts/         # Deep dives on specific topics
└── README.md         # This file
```

## Quick Access

```bash
# Terminal shortcuts (added to ~/.zshrc)
til              # Capture what you learned today
til-show         # View recent learnings
quickref         # List quick reference guides
review           # Start weekly review
learn            # Search your knowledge base
```

## Usage Patterns

### Daily Learning Capture
```bash
# At end of day
til "Learned how Docker networks work with bridge mode"
til "Python asyncio: use asyncio.gather() for concurrent tasks"
```

### Weekly Reviews
```bash
# Friday or Sunday
review           # Opens template, auto-fills week's TILs
```

### Quick References
```bash
# Create cheat sheets for topics you use frequently
# Example: Docker commands, Git workflows, Python patterns
```

### Concept Deep Dives
```bash
# When you deeply research a topic, document it
# Example: "Understanding Kubernetes Pods.md"
```

## Integration with Archon

All learning entries are timestamped and searchable. Use:
- `mdfind` for fast macOS searches
- Archon MCP for task-related knowledge
- Claude Code for analysis and insights

## Philosophy

**Capture > Organize > Review > Apply**

1. **Capture**: Record learnings immediately (TIL)
2. **Organize**: Weekly reviews consolidate knowledge
3. **Review**: Monthly summaries identify patterns
4. **Apply**: Use QuickRef guides in real work

---

*Created: 2026-02-14*
*System: Archon-BMAD Integration*
