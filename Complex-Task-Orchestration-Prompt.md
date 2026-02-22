# Complex Task Orchestration Prompt

**Version**: 1.0.0
**Created**: 2026-02-14
**Purpose**: Practical framework for Claude to handle complex multi-step tasks with persistence

---

## What This Is

This is a **systematic approach** for Claude (single AI agent) to handle complex tasks that require:
- Multiple steps across different domains (code, research, infrastructure)
- Persistence across sessions (surviving restarts)
- Structured methodology (Agile, DevOps, Waterfall)
- Clear progress tracking and recovery

**Note**: This is not a multi-agent system. Claude is one unified AI that adopts different "thinking modes" for different domains.

---

## Core Capabilities

### What Claude Actually Has

| Capability | Implementation | Persistence Method |
|------------|----------------|-------------------|
| **Task Tracking** | TodoWrite tool | In-session only |
| **Cross-Session State** | Archon MCP | SQLite database |
| **Sub-Agents** | Task tool (Explore, Plan, Bash) | Context-limited Claude instances |
| **Code Management** | Read/Write/Edit + Git | Filesystem + version control |
| **Research** | WebSearch, WebFetch, Grep | Temporary results |
| **Infrastructure** | Bash tool | Command execution |
| **Skills** | Slash commands (optional) | Varies by skill configuration |

### What Claude Doesn't Have
- ❌ Separate AI agents for different domains
- ❌ Distributed execution across multiple models
- ❌ Automatic background task persistence without Archon
- ❌ Built-in state replication or high-availability

---

## Orchestration Protocol

### Phase 1: Pre-Flight Check (MANDATORY)

**Always run before starting complex tasks:**

```
1. Check Archon for existing tasks
   → archon_list_tasks(assignee="claude", status="doing")

2. If existing tasks found:
   → Resume existing work instead of starting fresh
   → Ask user: "I found N incomplete tasks. Continue or start new?"

3. If no existing tasks:
   → Assess complexity (see matrix below)
   → Select methodology
   → Create Archon task for tracking
```

**Complexity Assessment:**

| Complexity | Indicators | Approach |
|------------|-----------|----------|
| **Simple** | 1-2 steps, single domain, <5 min | Execute directly, no TodoWrite needed |
| **Moderate** | 3-5 steps, 1-2 domains, 5-20 min | Use TodoWrite, consider Archon |
| **Complex** | 6+ steps, multiple domains, >20 min | Mandatory Archon + TodoWrite + methodology selection |

### Phase 2: Methodology Selection

**Decision Tree:**

```
IF (requirements unclear OR iterative feedback needed)
  → Agile/Scrum
  → Checkpoint after each iteration
  → Tool: Archon updates after each sprint

ELSE IF (infrastructure/deployment focus OR zero-downtime needed)
  → DevOps
  → Checkpoint before/after infrastructure changes
  → Tool: Git commits + Archon state

ELSE IF (strict requirements OR regulatory compliance OR high risk)
  → Waterfall
  → Checkpoint after each phase gate
  → Tool: Formal Archon milestones + approval gates

ELSE IF (continuous flow OR low ceremony needed)
  → Kanban
  → Checkpoint on status transitions
  → Tool: TodoWrite status updates + Archon sync
```

### Phase 3: Task Decomposition

**Create structured breakdown:**

```
1. Identify capability domains needed:
   - Code (Read/Write/Edit)
   - Research (WebSearch/WebFetch)
   - Infrastructure (Bash)
   - Exploration (Task tool with Explore agent)

2. Build dependency graph:
   Task A → Task B → Task C
   Task D (parallel to A)

3. Set up tracking:
   - TodoWrite for in-session visibility
   - Archon for cross-session persistence

4. Define checkpoints:
   - After each major subtask
   - Before risky operations
   - Every 10-15 minutes for long tasks
```

### Phase 4: Execution with Checkpoints

**Standard execution pattern:**

```python
# Pseudo-code for complex task execution

# 1. Initialize
archon_task = archon_add_task(
    title="Task name",
    assignee="claude",
    priority="medium",
    description="Full context"
)

archon_start_task(archon_task.id)

# 2. Execute subtasks
for subtask in workflow:
    # Mark as in-progress
    todo_update(subtask.id, status="in_progress")

    # Do the work (code, research, infrastructure)
    result = execute_subtask(subtask)

    # Checkpoint
    if subtask.is_critical:
        git_commit(f"Checkpoint: {subtask.name}")

    archon_update_task(
        archon_task.id,
        description=f"Completed: {subtask.name}"
    )

    # Mark complete
    todo_update(subtask.id, status="completed")

# 3. Finalize
archon_complete_task(archon_task.id)
```

### Phase 5: Recovery & Resumption

**On session restart:**

```
1. Check Archon:
   tasks = archon_list_tasks(assignee="claude", status="doing")

2. If tasks found:
   - Display task summary
   - Show last checkpoint
   - Offer to resume or start fresh

3. Resume workflow:
   - Load context from Archon description
   - Identify completed vs pending subtasks
   - Continue from last checkpoint
```

---

## Persistence Strategy

### Hybrid Approach (Recommended)

| Layer | Tool | Use Case | Durability |
|-------|------|----------|-----------|
| **In-Session** | TodoWrite | Active task visibility | Lost on restart |
| **Cross-Session** | Archon MCP | State persistence | Survives restart |
| **Code State** | Git commits | Code checkpoints | Version controlled |
| **Logs** | File writes | Audit trail | Manual cleanup needed |

### Checkpoint Pattern

**When to checkpoint:**
- ✅ After completing each TodoWrite task
- ✅ Before executing risky Bash commands
- ✅ After significant code changes (via Git commit)
- ✅ Every 10-15 minutes for long-running tasks
- ✅ Before asking user for input (save partial progress)

**Checkpoint content:**
```json
{
  "task_id": "archon-uuid",
  "timestamp": "2026-02-14T19:00:00Z",
  "methodology": "Agile",
  "completed_subtasks": ["subtask-1", "subtask-2"],
  "pending_subtasks": ["subtask-3", "subtask-4"],
  "current_state": "Waiting for test results",
  "context": {
    "files_modified": ["src/main.py", "tests/test_main.py"],
    "commands_run": ["pytest", "npm build"],
    "blockers": []
  }
}
```

Store in Archon task description or as JSON file in `~/Documents/Archive/Logs/`.

---

## Methodology Deep Dive

### Agile/Scrum Pattern

**When to use:**
- Requirements are evolving
- User feedback is critical
- Iterative refinement needed

**Workflow:**
```
Sprint 1 (2-day iteration):
  1. Plan: Identify 3-5 user stories
  2. Execute: Implement features
  3. Review: Demo to user
  4. Checkpoint: Archon update + Git commit
  5. Retrospect: Adjust approach if needed

Sprint 2:
  (Repeat with new stories based on feedback)
```

**Checkpoint frequency:** After each sprint (every 2-7 days or iterations)

**Example activation:**
```
Claude, use Agile methodology to build a REST API with the following features:
- User authentication
- CRUD operations for posts
- Rate limiting

Plan sprints and checkpoint after each iteration.
```

### DevOps Pattern

**When to use:**
- Infrastructure automation
- Deployment pipelines
- High-availability systems

**Workflow:**
```
1. Infrastructure as Code:
   - Write Terraform/CloudFormation
   - Checkpoint: Git commit

2. CI/CD Pipeline:
   - Configure GitHub Actions/Jenkins
   - Checkpoint: After successful test run

3. Deployment:
   - Execute deployment
   - Checkpoint: Before and after (rollback point)

4. Monitoring:
   - Set up alerts
   - Checkpoint: Configuration saved
```

**Checkpoint frequency:** Before/after each infrastructure change

**Example activation:**
```
Claude, use DevOps methodology to:
1. Dockerize the application
2. Set up CI/CD with GitHub Actions
3. Deploy to AWS with blue-green deployment

Checkpoint before each deployment step.
```

### Waterfall Pattern

**When to use:**
- Requirements are fixed
- Regulatory compliance needed
- High-risk changes

**Workflow:**
```
Phase 1: Requirements
  - Document all requirements
  - Checkpoint: Requirements signed off

Phase 2: Design
  - Create architecture diagram
  - Design database schema
  - Checkpoint: Design approved

Phase 3: Implementation
  - Write code per design
  - Checkpoint: Code complete

Phase 4: Testing
  - Run full test suite
  - Checkpoint: Tests pass

Phase 5: Deployment
  - Deploy to production
  - Checkpoint: Deployment verified
```

**Checkpoint frequency:** After each phase gate (formal approval)

**Example activation:**
```
Claude, use Waterfall methodology to migrate our PostgreSQL database to MySQL.

Requirements:
- Zero data loss
- Minimal downtime (<1 hour)
- Full audit trail

Checkpoint after each phase and wait for approval before proceeding.
```

### Kanban Pattern

**When to use:**
- Continuous flow of work
- Low ceremony preferred
- Work-in-progress limits needed

**Workflow:**
```
Backlog → To Do → In Progress → Done

Rules:
- Max 2 tasks in "In Progress" at once
- Move tasks through stages
- Checkpoint on stage transition
```

**Checkpoint frequency:** Every status change

**Example activation:**
```
Claude, use Kanban to work through my task list:
1. Fix authentication bug
2. Add dark mode
3. Write API documentation
4. Update dependencies

Limit to 1 task in progress at a time, checkpoint after each completion.
```

---

## Activation Commands

### Standard Activation

**Simple tasks (no orchestration needed):**
```
Claude, [direct request]
```

**Complex tasks (orchestration mode):**
```
Claude, use orchestration mode to [task description]
```

### With Methodology

**Agile:**
```
Claude, use Agile sprints to [task description]
```

**DevOps:**
```
Claude, use DevOps practices to [task description]
```

**Waterfall:**
```
Claude, use Waterfall with approval gates to [task description]
```

**Kanban:**
```
Claude, use Kanban flow to [task description]
```

### With Persistence Specification

**Archon-backed:**
```
Claude, create an Archon task and [task description]
```

**Git checkpoints:**
```
Claude, with Git checkpoints, [task description]
```

**Full persistence:**
```
Claude, with full persistence (Archon + Git + logs), [task description]
```

---

## Real-World Examples

### Example 1: Build Web Application (Agile)

**Request:**
```
Claude, use Agile methodology to build a task management web app with:
- User registration/login
- Create/edit/delete tasks
- Task categories and tags
- Basic dashboard

Plan in 3 sprints, checkpoint after each.
```

**Claude's response:**
```
Entering orchestration mode with Agile methodology.

Checking Archon for existing tasks... None found.

Creating Agile workflow:

Sprint 1 (Foundation):
  - Set up project structure (React + Node.js)
  - Implement user authentication
  - Create basic UI components
  Checkpoint: Working login system

Sprint 2 (Core Features):
  - CRUD operations for tasks
  - Add categories and tags
  - Database schema and API endpoints
  Checkpoint: Full task management working

Sprint 3 (Polish):
  - Dashboard with task analytics
  - UI/UX improvements
  - Testing and bug fixes
  Checkpoint: Production-ready app

Creating Archon task... [task-id-123]
Creating TodoWrite tasks for Sprint 1...

Shall I proceed with Sprint 1?
```

### Example 2: Infrastructure Migration (DevOps)

**Request:**
```
Claude, use DevOps methodology to migrate Docker from internal disk to external SSD.

Requirements:
- Zero data loss
- Preserve all containers/images
- Update Docker Desktop settings
- Verify symlinks work correctly

Checkpoint before and after each major step.
```

**Claude's response:**
```
Entering orchestration mode with DevOps methodology.

Checking Archon for existing tasks... Found 1 related task: "SSD Migration" (completed 2026-01-21)

⚠️ Migration already complete. Checking current state...

Running verification:
  ✓ Docker data path: /Volumes/PRO-G40/HomeFiles/Docker/
  ✓ Disk usage: 240GB on external SSD
  ✓ Docker Desktop operational

Current state is correct. No migration needed.
Do you want me to re-verify the configuration or document the current setup?
```

### Example 3: Security Audit (Waterfall)

**Request:**
```
Claude, use Waterfall methodology to audit our codebase for security vulnerabilities.

Phases:
1. Scan for common vulnerabilities (OWASP Top 10)
2. Review authentication/authorization code
3. Check for secrets in code/config
4. Generate security report
5. Propose fixes

Wait for approval after each phase.
```

**Claude's response:**
```
Entering orchestration mode with Waterfall methodology.

Creating Archon task: "Security Audit - Waterfall"

Phase 1: Vulnerability Scanning
  Tasks:
    - Scan for SQL injection points
    - Check for XSS vulnerabilities
    - Review file upload handling
    - Check for command injection
    - CSRF protection review

Creating checkpoint: phase-1-start

Executing Phase 1...
[Performs scans using Grep, Read, static analysis]

Phase 1 Results:
  ✓ No SQL injection found (using parameterized queries)
  ⚠️ Potential XSS in user profile (line 234 in profile.js)
  ✓ File uploads properly validated
  ⚠️ Command execution in admin panel (line 567 in admin.py)
  ✓ CSRF tokens present

Creating checkpoint: phase-1-complete

Phase 1 complete. Approve to proceed to Phase 2 (Authentication Review)?
```

### Example 4: Continuous Task Flow (Kanban)

**Request:**
```
Claude, use Kanban to work through these maintenance tasks:
- Update all npm dependencies
- Fix TypeScript errors
- Update README with new setup instructions
- Add missing unit tests
- Optimize Docker build

One task at a time, checkpoint after each.
```

**Claude's response:**
```
Entering orchestration mode with Kanban methodology.

Kanban Board:
┌─────────────────────────────────────────────┐
│ To Do (5)                                   │
│ - Update npm dependencies                   │
│ - Fix TypeScript errors                     │
│ - Update README                             │
│ - Add unit tests                            │
│ - Optimize Docker build                     │
├─────────────────────────────────────────────┤
│ In Progress (0)                             │
│                                             │
├─────────────────────────────────────────────┤
│ Done (0)                                    │
│                                             │
└─────────────────────────────────────────────┘

WIP Limit: 1 task at a time

Moving "Update npm dependencies" to In Progress...
Creating Archon task...

[Executes: npm outdated, npm update, tests]

Task complete. Checkpoint created.

Kanban Board Updated:
┌─────────────────────────────────────────────┐
│ To Do (4)                                   │
│ - Fix TypeScript errors                     │
│ - Update README                             │
│ - Add unit tests                            │
│ - Optimize Docker build                     │
├─────────────────────────────────────────────┤
│ In Progress (0)                             │
│                                             │
├─────────────────────────────────────────────┤
│ Done (1)                                    │
│ ✓ Update npm dependencies (5 min)          │
└─────────────────────────────────────────────┘

Moving to next task: "Fix TypeScript errors"
Continue? (yes/next task/pause)
```

---

## Tool Coordination Patterns

### Pattern 1: Code + Test + Commit

```
1. Read existing code
2. Edit code (fix/feature)
3. Run tests (Bash: pytest/npm test)
4. If tests pass:
   → Git commit with checkpoint message
   → Archon update
5. If tests fail:
   → Fix and repeat
```

### Pattern 2: Research + Implement

```
1. WebSearch for documentation/examples
2. Explore codebase (Task tool: Explore agent)
3. Read relevant files
4. Implement solution
5. Checkpoint via Git + Archon
```

### Pattern 3: Infrastructure + Verify

```
1. Bash: Check current state
2. Bash: Execute infrastructure change
3. Bash: Verify change successful
4. If success:
   → Archon update
   → Log to audit file
5. If failure:
   → Rollback
   → Escalate to user
```

---

## Skills Integration (Optional Enhancement)

### What Are Skills?

Skills are specialized **slash commands** that automate common workflows. They're like macros that combine multiple tools into a single operation.

**Current status**: No skills configured in `~/.claude/settings.json`

### Why Use Skills in Orchestration?

Skills can significantly reduce checkpoint boilerplate and automate repetitive patterns:

| Without Skills | With Skills | Benefit |
|----------------|-------------|---------|
| Read file + Edit + Bash test + Git commit + Archon update | `/fix-and-commit "description"` | 5 steps → 1 command |
| Bash deploy + Bash verify + Git tag + Archon checkpoint | `/deploy production` | Automated rollback on failure |
| Multiple Grep + Read + Analysis | `/security-scan` | Consistent audit process |

### Common Skills for Orchestration

| Skill | Command | What It Does | Best Methodology |
|-------|---------|--------------|------------------|
| **commit** | `/commit` | Smart git commits with co-authoring | All (especially Agile) |
| **test** | `/test` | Run test suites with reporting | DevOps, Waterfall |
| **deploy** | `/deploy [env]` | Deployment with verification | DevOps |
| **review-pr** | `/review-pr [number]` | Code review workflow | Agile sprints |
| **security-scan** | `/security-scan` | OWASP Top 10 audit | Waterfall quality gates |
| **checkpoint** | `/checkpoint [message]` | Git + Archon + logs in one | All methodologies |

### How to Check Available Skills

```bash
# List all configured skills
/help

# Or check settings manually
cat ~/.claude/settings.json | grep -A 10 "skills"
```

**Your current config:**
```json
{
  "model": "sonnet"
}
```
*No skills configured yet*

### How Skills Integrate with Methodologies

#### Agile/Scrum with Skills

**Without skills:**
```
1. Edit code
2. Run tests manually (Bash: npm test)
3. Git commit
4. Update Archon task
5. Announce sprint progress
```

**With `/sprint-checkpoint` skill:**
```
/sprint-checkpoint "Completed user authentication feature"

# Skill automatically:
# - Runs tests
# - Commits to git with sprint metadata
# - Updates Archon task
# - Tags commit with sprint number
# - Generates sprint report
```

#### DevOps with Skills

**Without skills:**
```
1. Bash: docker build
2. Bash: docker tag
3. Bash: docker push
4. Update deployment manifest
5. Bash: kubectl apply
6. Bash: kubectl rollout status
7. Checkpoint if successful
8. Rollback if failed
```

**With `/deploy` skill:**
```
/deploy production --blue-green

# Skill automatically:
# - Builds and pushes image
# - Updates manifests
# - Deploys to staging (green)
# - Runs health checks
# - Switches traffic if healthy
# - Rolls back if unhealthy
# - Checkpoints success/failure
```

#### Waterfall with Skills

**Without skills:**
```
Phase 3: Testing
1. Run unit tests (Bash: pytest)
2. Run integration tests (Bash: npm run test:integration)
3. Run security scan (multiple Grep + Read)
4. Generate test report
5. Git commit test results
6. Update Archon phase status
7. Wait for approval
```

**With `/quality-gate` skill:**
```
/quality-gate phase-3-testing

# Skill automatically:
# - Runs all test suites
# - Performs security scan
# - Generates compliance report
# - Commits results
# - Updates Archon with pass/fail
# - Requests approval if passed
# - Blocks progression if failed
```

#### Kanban with Skills

**Without skills:**
```
Moving task "Fix auth bug" to In Progress:
1. Update TodoWrite status
2. Update Archon task
3. Read code
4. Edit fix
5. Run tests
6. Git commit
7. Update TodoWrite to Done
8. Update Archon to completed
```

**With `/kanban-flow` skill:**
```
/kanban-flow "Fix auth bug"

# Skill automatically:
# - Moves task to In Progress (TodoWrite + Archon)
# - Provides fix context from history
# - After fix applied:
#   - Runs tests
#   - Commits with Kanban metadata
#   - Moves to Done (TodoWrite + Archon)
#   - Updates WIP metrics
```

### Recommended Skills to Create

If you want to enhance orchestration, consider creating these skills:

#### 1. Checkpoint Skill
```json
{
  "name": "checkpoint",
  "description": "Create unified checkpoint across Git, Archon, and logs",
  "command": "/checkpoint [message]",
  "actions": [
    "git add .",
    "git commit -m \"Checkpoint: {message}\\n\\nCo-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>\"",
    "archon_update_task with checkpoint timestamp",
    "log to ~/Documents/Archive/Logs/orchestration.log"
  ]
}
```

**Usage:**
```
Claude: Completed user authentication module
/checkpoint "Auth module complete with JWT implementation"
```

#### 2. Agile Sprint Skill
```json
{
  "name": "sprint-complete",
  "description": "Finalize Agile sprint with testing and reporting",
  "command": "/sprint-complete [sprint-number]",
  "actions": [
    "run test suite",
    "generate sprint report (features completed, bugs fixed)",
    "git tag sprint-{number}",
    "archon_update_task with sprint summary",
    "request user demo/review"
  ]
}
```

**Usage:**
```
/sprint-complete 1
# Prompts: "Sprint 1 complete. 5/5 features done. Run demo?"
```

#### 3. DevOps Deploy Skill
```json
{
  "name": "deploy",
  "description": "Deploy with automated verification and rollback",
  "command": "/deploy [environment]",
  "actions": [
    "checkpoint pre-deployment state",
    "execute deployment to {environment}",
    "run health checks",
    "if healthy: checkpoint success",
    "if unhealthy: automatic rollback + alert user"
  ]
}
```

**Usage:**
```
/deploy staging
# Deploys, verifies, checkpoints or rolls back
```

#### 4. Security Audit Skill
```json
{
  "name": "security-scan",
  "description": "Run OWASP Top 10 security audit",
  "command": "/security-scan [scope]",
  "actions": [
    "grep for SQL injection patterns",
    "grep for XSS vulnerabilities",
    "grep for hardcoded secrets",
    "check authentication code",
    "generate security report",
    "archon_update_task with findings"
  ]
}
```

**Usage:**
```
/security-scan full
# Runs complete audit, generates report
```

### How to Configure Skills

Skills are defined in `~/.claude/settings.json`:

```json
{
  "model": "sonnet",
  "skills": {
    "checkpoint": {
      "description": "Create unified checkpoint",
      "command": "/checkpoint",
      "handler": "checkpoint-skill.js"
    },
    "deploy": {
      "description": "Deploy with verification",
      "command": "/deploy",
      "handler": "deploy-skill.js"
    }
  }
}
```

**Note**: Skills configuration format may vary. Check Claude Code documentation for exact syntax.

### Skills in Checkpoint Patterns

**Updated checkpoint triggers with skills:**

| Trigger | Without Skills | With Skills |
|---------|----------------|-------------|
| After subtask complete | Manual git commit + Archon update | `/checkpoint "subtask done"` |
| Before risky operation | Manual backup + state save | `/backup-state` |
| After tests pass | Manual commit + tag | `/test-and-commit` |
| Sprint complete | Manual sprint closure | `/sprint-complete N` |
| Deployment | Manual deploy + verify | `/deploy env` |

### Integration with Existing Patterns

**Tool Coordination Pattern 1 (Updated):**

```
Code + Test + Commit Pattern:

Without Skills:
1. Read existing code
2. Edit code (fix/feature)
3. Run tests (Bash: pytest/npm test)
4. If tests pass:
   → Git commit with checkpoint message
   → Archon update

With Skills:
1. Read existing code
2. Edit code (fix/feature)
3. /test-and-commit "Fixed authentication bug"
   # Skill runs tests, commits only if passing, updates Archon
```

**Tool Coordination Pattern 2 (Updated):**

```
Infrastructure + Verify Pattern:

Without Skills:
1. Bash: Check current state
2. Bash: Execute infrastructure change
3. Bash: Verify change successful
4. If success: Archon update + log
5. If failure: Rollback + escalate

With Skills:
1. /infra-change "Add Redis cache server"
   # Skill: checks state → applies change → verifies → checkpoints or rolls back
```

### Activating Orchestration Mode with Skills

**Enhanced activation commands:**

```
# Basic orchestration with skill support
Claude, use Agile methodology with skills to build a REST API

# Explicit skill preference
Claude, use /checkpoint skill for all checkpoints while implementing auth

# DevOps with deployment skill
Claude, use DevOps with /deploy skill to set up CI/CD pipeline

# Security-focused with audit skill
Claude, use Waterfall with /security-scan at each phase gate
```

### When Skills Are Most Valuable

Use skills when:
- ✅ Repeating same checkpoint pattern frequently (Agile sprints)
- ✅ Complex multi-step operations need atomicity (DevOps deployments)
- ✅ Compliance requires consistent audit process (Waterfall quality gates)
- ✅ Reducing human error in critical operations
- ✅ Enforcing team standards (commit messages, test coverage)

Skip skills when:
- ❌ One-off tasks with unique requirements
- ❌ Exploratory work where process varies
- ❌ Skills would add more overhead than value
- ❌ You need manual control at each step

### Next Steps

**To start using skills:**

1. **Identify repetitive patterns** in your workflow
2. **Design skill behavior** (what should it automate?)
3. **Configure in settings.json** (or use Claude Code skill creation)
4. **Test skill** on non-critical tasks first
5. **Integrate into orchestration** methodology

**Example workflow to add `/checkpoint` skill:**

```bash
# 1. Edit Claude settings
vim ~/.claude/settings.json

# 2. Add skill configuration
{
  "model": "sonnet",
  "skills": {
    "checkpoint": {
      "description": "Unified checkpoint across Git + Archon",
      "handler": "checkpoint"
    }
  }
}

# 3. Test the skill
/checkpoint "Testing new checkpoint skill"

# 4. Use in orchestration
Claude, use Agile with /checkpoint skill for sprint boundaries
```

---

## Failure Recovery

### Common Failure Scenarios

| Failure Type | Detection | Recovery Strategy |
|--------------|-----------|-------------------|
| **Session timeout** | User restarts Claude | Resume from Archon tasks (status="doing") |
| **Command fails** | Bash returns error code | Retry 2x, then ask user |
| **Tests fail** | Test suite returns failures | Fix issues, don't checkpoint until pass |
| **Git conflict** | Merge conflict | Ask user for resolution strategy |
| **Archon unavailable** | MCP connection fails | Fall back to TodoWrite only (warn user) |

### Recovery Protocol

```
On session start:
1. Check Archon for incomplete tasks
2. Display summary to user:
   "I found 2 incomplete tasks from previous sessions:
    - Task A (status: doing, last updated: 2 hours ago)
    - Task B (status: todo, created: yesterday)

   Options:
   a) Resume Task A
   b) Resume Task B
   c) Start fresh
   d) Show more details"

3. Based on user choice:
   → Resume: Load context, continue workflow
   → Start fresh: Archive old tasks, begin new work
```

---

## Best Practices

### Do's ✅

1. **Always check Archon first** before starting complex tasks
2. **Use TodoWrite** for in-session visibility (user can see progress)
3. **Commit frequently** to Git for code checkpoints
4. **Update Archon** after each major subtask completion
5. **Ask before risky operations** (deployments, deletions, major refactors)
6. **Estimate complexity** realistically (simple/moderate/complex)
7. **Select appropriate methodology** based on task characteristics
8. **Checkpoint before asking user** (save partial progress)

### Don'ts ❌

1. **Don't skip Archon check** - you might duplicate existing work
2. **Don't checkpoint partial/broken state** - only checkpoint when subtask truly complete
3. **Don't run destructive commands without confirmation** (rm -rf, DROP TABLE, etc.)
4. **Don't assume session continuity** - always design for resumability
5. **Don't over-engineer for simple tasks** - use orchestration only when needed
6. **Don't lose context** - save state before long-running operations
7. **Don't ignore test failures** - fix before checkpointing

---

## Integration with CLAUDE.md

This orchestration framework extends the core CLAUDE.md directives:

### Archon Pre-Flight (CLAUDE.md Section)
```
CRITICAL: Before ANY complex action, you MUST check Archon first.
```
**Implementation:** Phase 1 of Orchestration Protocol (mandatory Archon check)

### Clean Root Policy (CLAUDE.md Section)
```
Auto-Cleanup Rule: Any file created in ~/Documents/ root must be
moved to appropriate subdirectory immediately.
```
**Implementation:** Checkpoint logs go to `~/Documents/Archive/Logs/`

### macOS-Optimized Search (CLAUDE.md Section)
```
Primary: mdfind -onlyin ~/Documents "query" for filename/metadata searches
```
**Implementation:** Use in Research phase of complex tasks

---

## Monitoring & Metrics

### Track These Metrics

| Metric | How to Measure | Target |
|--------|----------------|--------|
| **Task completion rate** | Archon tasks marked "done" vs "total" | >90% |
| **Average subtask duration** | Time between TodoWrite status changes | <15 min |
| **Checkpoint frequency** | Git commits + Archon updates per hour | 4-6/hour |
| **Recovery time** | Time to resume after session restart | <2 min |
| **Methodology adherence** | Actual vs planned workflow | 100% |

### Example Log Entry

```
[2026-02-14T19:30:00Z] Orchestration started: "Build REST API"
[2026-02-14T19:30:05Z] Archon check: 0 existing tasks
[2026-02-14T19:30:10Z] Methodology selected: Agile (3 sprints)
[2026-02-14T19:30:15Z] Archon task created: task-abc-123
[2026-02-14T19:35:42Z] Sprint 1 subtask 1 complete: "Project setup"
[2026-02-14T19:35:43Z] Checkpoint: Git commit 7f8a9b2
[2026-02-14T19:35:44Z] Archon updated: "Completed project setup"
[2026-02-14T19:42:18Z] Sprint 1 subtask 2 complete: "Auth implementation"
[2026-02-14T19:42:19Z] Checkpoint: Git commit 3c4d5e6
[2026-02-14T19:42:20Z] Archon updated: "Auth complete, 2/5 subtasks done"
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-14 | Initial release - practical orchestration framework |
| 1.1.0 | 2026-02-14 | Added Skills Integration section with methodology examples |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│         COMPLEX TASK ORCHESTRATION QUICK GUIDE              │
├─────────────────────────────────────────────────────────────┤
│ 1. PRE-FLIGHT                                               │
│    → archon_list_tasks(assignee="claude")                  │
│    → Assess complexity (simple/moderate/complex)            │
│    → Check /help for available skills                       │
│                                                             │
│ 2. METHODOLOGY                                              │
│    → Evolving requirements? → Agile                         │
│    → Infrastructure/deployment? → DevOps                    │
│    → Fixed requirements/compliance? → Waterfall             │
│    → Continuous flow? → Kanban                              │
│                                                             │
│ 3. TRACKING                                                 │
│    → Complex tasks: Archon + TodoWrite                      │
│    → Code changes: Git commits (or /commit skill)           │
│    → Logs: ~/Documents/Archive/Logs/                        │
│                                                             │
│ 4. CHECKPOINTS                                              │
│    → After each subtask completion                          │
│    → Before risky operations                                │
│    → Every 10-15 minutes                                    │
│    → Before asking user for input                           │
│    → Use /checkpoint skill if configured                    │
│                                                             │
│ 5. RECOVERY                                                 │
│    → On restart: Check Archon for status="doing"           │
│    → Resume from last checkpoint                            │
│    → Show user context and options                          │
│                                                             │
│ 6. SKILLS (OPTIONAL)                                        │
│    → /checkpoint - Unified Git + Archon checkpoint          │
│    → /deploy - Automated deployment with verification       │
│    → /security-scan - OWASP Top 10 audit                    │
│    → Check settings.json for configuration                  │
└─────────────────────────────────────────────────────────────┘
```

---

**End of Complex Task Orchestration Prompt**
