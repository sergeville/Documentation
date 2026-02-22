# Getting Started with Your Knowledge Management System

**Complete step-by-step guide with real examples**

---

## Table of Contents

1. [First Time Setup](#first-time-setup)
2. [Daily Workflow](#daily-workflow)
3. [Building Quick References](#building-quick-references)
4. [Weekly Review Process](#weekly-review-process)
5. [Searching Your Knowledge](#searching-your-knowledge)
6. [Real-World Examples](#real-world-examples)
7. [Tips & Best Practices](#tips--best-practices)

---

## First Time Setup

### Step 1: Reload Your Shell

Open a terminal and run:

```bash
source ~/.zshrc
```

**What this does:** Loads all the new knowledge management commands.

### Step 2: Verify Installation

```bash
til
```

**Expected output:**
```
💡 TIL - Today I Learned

Usage:
  til "what you learned"     # Capture learning
  til --show [days]          # View recent (default: 7 days)

📖 Recent entries:
No entries yet today.
```

**If you see this, you're ready to go!**

---

## Daily Workflow

### Morning: Start Your Day

**Step 1: Check what you're working on**

```bash
tasks
```

This shows you Archon tasks (ask Claude "show me task list" for full details).

**Step 2: Check workflow state**

```bash
workflow
# or shorter:
wf
```

### During Work: Capture Learnings

**Every time you learn something, capture it immediately.**

#### Example 1: Learning Docker

```bash
til "Docker containers share the host kernel, VMs have their own kernel"
```

**Output:**
```
✅ Captured to: ~/Documents/Knowledge/TIL/2026-02.md
   "Docker containers share the host kernel, VMs have their own kernel"
```

#### Example 2: Learning Python

```bash
til "Python list comprehensions: [x*2 for x in range(10)] is faster than loops"
```

#### Example 3: Learning Git

```bash
til "git stash saves uncommitted changes temporarily, git stash pop restores them"
```

#### Example 4: Terminal Commands

```bash
til "macOS mdfind command searches faster than find because it uses Spotlight index"
```

### End of Day: Review What You Learned

```bash
til-show
```

**Example output:**
```
📚 Last 7 days of learning:

**2026-02-14 09:15**
- Docker containers share the host kernel, VMs have their own kernel

**2026-02-14 11:30**
- Python list comprehensions: [x*2 for x in range(10)] is faster than loops

**2026-02-14 14:22**
- git stash saves uncommitted changes temporarily, git stash pop restores them

**2026-02-14 16:45**
- macOS mdfind command searches faster than find because it uses Spotlight index
```

---

## Building Quick References

Quick references are your personal cheat sheets for topics you use frequently.

### When to Create a Quick Reference

Create one when you find yourself:
- Looking up the same commands repeatedly
- Googling the same thing multiple times
- Asking Claude the same questions
- Learning a new tool/language/framework

### Step-by-Step: Create Your First Quick Reference

#### Example: Creating a Docker Quick Reference

**Step 1: Create the guide**

```bash
quickref --create Docker
```

**What happens:**
1. Creates `~/Documents/Knowledge/QuickRef/Docker.md`
2. Opens it in your default editor (vim/nano/VSCode)

**Step 2: Fill in the template**

The template looks like this:

```markdown
# Docker Quick Reference

**Category:** Containers
**Last Updated:** 2026-02-14

---

## Common Commands

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Run a container
docker run -d -p 8080:80 nginx

# Stop a container
docker stop container_id

# Remove a container
docker rm container_id

# View logs
docker logs container_id
```

---

## Key Concepts

- **Image**: Template for containers (like a class)
- **Container**: Running instance of an image (like an object)
- **Volume**: Persistent storage for containers
- **Network**: How containers communicate

---

## Best Practices

1. Use .dockerignore to exclude unnecessary files
2. Multi-stage builds reduce image size
3. Don't run containers as root in production
4. Use specific image tags, not 'latest'

---

## Common Pitfalls

❌ **Don't do this**
```bash
docker run myapp  # Loses data when container stops
```

✅ **Do this instead**
```bash
docker run -v $(pwd)/data:/app/data myapp  # Data persists
```

---

## Examples

### Run PostgreSQL locally
```bash
docker run -d \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=mypassword \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15
```

### Build and run your app
```bash
docker build -t myapp:v1 .
docker run -d -p 3000:3000 myapp:v1
```

---

## Related Resources

- [Official Docker Docs](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)

---
```

**Step 3: Save and view it**

```bash
# List all quick refs
quickref --list

# View your Docker guide
quickref Docker
# or shorter:
qr Docker
```

### More Quick Reference Examples

#### Python Async

```bash
quickref --create Python-Async
```

Then fill with your learnings:

```markdown
## Common Patterns

```python
# Run multiple async tasks concurrently
import asyncio

async def fetch_data():
    # Concurrent execution
    results = await asyncio.gather(
        fetch_user(),
        fetch_posts(),
        fetch_comments()
    )
    return results

# Always use await inside async functions
async def main():
    data = await fetch_data()
```
```

#### Kubernetes Basics

```bash
quickref --create Kubernetes
```

Fill with commands you use:

```markdown
## Common kubectl Commands

```bash
# Get all pods
kubectl get pods

# Get pod details
kubectl describe pod pod-name

# View logs
kubectl logs pod-name

# Execute command in pod
kubectl exec -it pod-name -- /bin/bash
```
```

---

## Weekly Review Process

Every Friday afternoon or Sunday evening (your choice).

### Step 1: Start the Review

```bash
review
```

**What happens:**
1. Script creates `~/Documents/Knowledge/Reviews/2026-W07.md`
2. Auto-fills with this week's TIL entries
3. Opens in your editor

### Step 2: Fill in the Template

The review template looks like this:

```markdown
# Weekly Review - Week 2026-W07
**Period:** 2026-02-08 to 2026-02-14
**Created:** 2026-02-14

---

## 🎯 This Week's Focus

Alfred HVAC automation, Docker migration, Learning Kubernetes

---

## 💡 Key Learnings (TIL)

**2026-02-14 09:15**
- Docker containers share the host kernel, VMs have their own kernel

**2026-02-14 11:30**
- Python list comprehensions: [x*2 for x in range(10)] is faster than loops

**2026-02-14 14:22**
- git stash saves uncommitted changes temporarily, git stash pop restores them

**2026-02-14 16:45**
- macOS mdfind command searches faster than find because it uses Spotlight index

---

## ✅ Accomplishments

- Completed SSD migration and cleanup
- Set up knowledge management system
- Created 3 quick reference guides
- Learned Docker networking basics

---

## 🚧 Challenges & Blockers

- Docker network configuration was confusing initially
- Resolved by reading official docs and experimenting
- Created QuickRef guide to remember patterns

---

## 🧠 Concepts Deepened

- Docker networking: bridge vs host mode
- Python async: concurrency vs parallelism
- Git workflow: stashing for context switching

---

## 🔄 Patterns Noticed

- I learn best by doing, then documenting
- Creating QuickRef guides after 3+ lookups saves time
- Daily TIL captures are easier than weekly brain dump

---

## 📝 Actions for Next Week

1. Complete Kubernetes QuickRef guide
2. Review and consolidate Docker learnings
3. Start weekly review habit on Fridays

---
```

### Step 3: Keep It Brief

**Time limit: 10-15 minutes max**

Focus on:
- What did you accomplish?
- What did you learn?
- What patterns emerged?
- What's next?

---

## Searching Your Knowledge

### Basic Search

```bash
learn "docker"
```

**Output:**
```
🔍 Searching knowledge base for: "docker"

📄 Docker.md
## Common Commands

```bash
# List running containers
docker ps
```

📄 2026-02.md
**2026-02-14 09:15**
- Docker containers share the host kernel, VMs have their own kernel
```

### Search Multiple Terms

```bash
learn "python async"
```

### View Knowledge Stats

```bash
learn
```

**Output:**
```
📊 Your Knowledge Stats:
  TIL entries: 12
  Quick refs:  5
  Reviews:     2
  Concepts:    1
```

### Direct File Access

```bash
# View TIL file directly
cat ~/Documents/Knowledge/TIL/2026-02.md

# Search with grep
grep -r "docker" ~/Documents/Knowledge/

# Use macOS Spotlight
mdfind -onlyin ~/Documents/Knowledge "kubernetes"
```

---

## Real-World Examples

### Scenario 1: Learning a New Framework

**Day 1: First Exposure**

```bash
til "Next.js uses file-based routing: pages/index.js becomes /"
til "Next.js getServerSideProps runs on server, getStaticProps at build time"
```

**Day 3: After Some Practice**

```bash
til "Next.js API routes: create pages/api/hello.js for /api/hello endpoint"
til "Next.js Image component auto-optimizes images and lazy loads"
```

**End of Week: Create Reference**

```bash
quickref --create Next.js
```

Fill with your accumulated knowledge from TIL entries.

**Weekly Review**

```bash
review
```

Note: "Learned Next.js basics this week. Ready to build first project."

---

### Scenario 2: Debugging a Complex Issue

**During Investigation**

```bash
til "Docker port binding fails if host port already in use - check with lsof -i :8080"
til "Docker inspect shows full container config including network settings"
til "Docker logs -f streams logs in real-time, useful for debugging"
```

**After Resolution**

```bash
til "Solved port conflict by changing docker-compose.yml port mapping to 8081:8080"
```

**Update QuickRef**

```bash
quickref Docker
# Add debugging section with these commands
```

---

### Scenario 3: Daily Development

**Morning:**
```bash
tasks          # Check Archon tasks
wf             # View workflow state
```

**During work:**
```bash
# Found useful command
til "jq '.data[] | {name, value}' extracts specific fields from JSON"

# Need reference
qr Git-Basics  # Quick lookup

# Learn something
til "Python pathlib.Path.glob('**/*.py') recursively finds all .py files"
```

**Need to remember something:**
```bash
learn "docker port"  # Find that note about port binding
```

**End of day:**
```bash
til-show  # Review what you learned
```

**End of week:**
```bash
review  # Reflect and consolidate
```

---

## Tips & Best Practices

### TIL Best Practices

✅ **Good TIL Entries:**
- Specific and actionable
- Include concrete examples
- Capture insights, not just facts

```bash
til "Docker COPY in Dockerfile copies files at build time, volumes mount at runtime"
til "Python f-strings: f'{value=}' prints 'value=42' for debugging"
til "Git rebase -i HEAD~3 lets you edit last 3 commits interactively"
```

❌ **Avoid:**
- Too vague: "Learned about Docker"
- Too obvious: "Python is a programming language"
- No context: "Used grep today"

### Quick Reference Best Practices

**1. One topic per guide**
- ✅ Docker.md, Kubernetes.md, Git-Advanced.md
- ❌ DevOps-Everything.md

**2. Focus on what you forget**
- Commands you look up repeatedly
- Syntax you mix up
- Concepts that confuse you

**3. Real examples**
- Use code from your actual projects
- Include the context of when to use it

**4. Keep it updated**
- Add new learnings when you discover them
- Remove outdated information

### Weekly Review Best Practices

**1. Same time every week**
- Friday afternoon before weekend
- Sunday evening before week starts

**2. Keep it brief**
- 10-15 minutes maximum
- Bullet points are fine

**3. Focus on insights**
- Not just "what I did"
- But "what I learned"

**4. Note patterns**
- What keeps coming up?
- Where are you spending time?
- What should you focus on?

---

## Quick Command Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `til "..."` | Capture learning | `til "Docker uses layered filesystem"` |
| `til-show` | View recent (7 days) | `til-show` |
| `til-show 30` | View last 30 days | `til-show 30` |
| `learn "topic"` | Search knowledge | `learn "docker"` |
| `learn` | View stats | `learn` |
| `quickref --list` | List all guides | `quickref --list` |
| `quickref Topic` | View guide | `quickref Docker` |
| `qr Topic` | View guide (short) | `qr Docker` |
| `quickref --create Topic` | Create new guide | `quickref --create Python` |
| `review` | Weekly review | `review` |
| `knowledge` | Go to directory | `knowledge` |
| `workflow` | View state | `workflow` or `wf` |
| `tasks` | View Archon tasks | `tasks` |

---

## Your First 7 Days

### Day 1 (Today)
1. Reload shell: `source ~/.zshrc`
2. Capture first learning: `til "Set up knowledge management system"`
3. View it: `til-show`

### Day 2-6
1. Capture learnings as you work (aim for 3-5 per day)
2. When you look something up 3 times, create a QuickRef
3. Use `learn` to find old learnings instead of Googling

### Day 7 (End of Week)
1. Run: `review`
2. Reflect on the week (10 minutes)
3. Note patterns and plan next week

### After 30 Days

You'll have:
- ~100 TIL entries (your learning log)
- 3-5 QuickRef guides (your cheat sheets)
- 4 weekly reviews (your progress journal)
- Searchable knowledge base (your external brain)

**You're building your second brain.**

---

## Next Steps

1. **Start now**: `til "Read the knowledge system guide"`
2. **Capture daily**: Add TIL entries as you work
3. **Build references**: Create QuickRef for your most-used tools
4. **Review weekly**: Make it a habit
5. **Search first**: Before asking Claude, search your knowledge

---

## Getting Help

### Ask Claude for Analysis

```
"Analyze my TIL entries from last month and identify patterns"
"What have I been learning about most?"
"Create a QuickRef guide from my Docker TIL entries"
"Suggest topics for my next QuickRef based on my TILs"
```

### View Documentation

```bash
# Full system overview
cat ~/Documents/Knowledge/README.md

# This guide
cat ~/Documents/Knowledge/GETTING_STARTED.md

# System guide QuickRef
quickref Knowledge-System
```

### Explore Files

```bash
# Go to knowledge directory
knowledge

# Or manually
cd ~/Documents/Knowledge
ls -la
```

---

## Remember

**Your brain is for thinking, not storing.**

This system is your external memory. The more you use it, the more valuable it becomes.

**Capture → Organize → Review → Apply**

---

*Last Updated: 2026-02-14*
*Questions? Ask Claude: "How do I use the knowledge system for..."*
