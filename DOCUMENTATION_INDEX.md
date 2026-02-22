# Documentation Index
## Central Registry of Essential Markdown Files in ~/Documents/

**Last Updated**: 2026-02-22 (Root cleanup — moved stray files/folders to correct locations)
**Maintainer**: Serge Villeneuve
**Purpose**: Single source of truth for all critical documentation
**Total Files Indexed**: 153 essential files (out of 2,559 user-created files)

---

## How to Use This Index

**Quick Navigation**:
1. Find your category ([Projects](#projects), [System](#system-documentation), [Experiments](#myexperiments), [Archive](#archive))
2. Use Cmd+F to search for file names or keywords
3. Click section headings to jump to detailed documentation

**File Status Legend**:
- **Active** - Currently maintained, up-to-date
- **Reference** - Historical but valuable reference
- **Archived** - Completed project, kept for record
- **Deprecated** - Superseded by newer documentation

---

## Top-Level Documents (Root of ~/Documents/)

Root contains exactly: `CLAUDE.md`, `GEMINI.md`, and the 5 standard folders.
All other files have been moved to their correct locations (cleanup 2026-02-22).

### CLAUDE.md
**Location**: `~/Documents/CLAUDE.md`
**Why**: Master AI assistant instructions for entire ~/Documents/ workspace
**When**: Created 2026-01-22 (home reorganization)
**Who**: Serge Villeneuve (author), Claude (AI assistant)
**What**: Defines workspace structure, clean root policy, Archon integration, macOS best practices
**Status**: Active

### GEMINI.md
**Location**: `~/Documents/GEMINI.md`
**Why**: Gemini-specific AI assistant instructions
**When**: Created ~2026-01-22
**Who**: Serge Villeneuve
**What**: Similar to CLAUDE.md but adapted for Gemini interface
**Status**: Active

### DOCUMENTATION_INDEX.md (This File)
**Location**: `~/Documents/Documentation/DOCUMENTATION_INDEX.md`
**Why**: Central index of all essential markdown files
**When**: Created 2026-02-18, moved to Documentation/ 2026-02-22
**Who**: Claude (Archon assignee)
**What**: Why/when/where/who metadata for all critical documentation
**Status**: Active

### Relocated Files (moved 2026-02-22)
Previously at `~/Documents/` root, now properly placed:
- `Documentation/AI Agent Systems_ Shared Memory.md` - Multi-agent memory architecture
- `Documentation/AI Credits, Tokens, and Actions Explained.md` - AI cost/usage explanation
- `Documentation/AI System Architecture and Strategy.md` - System architecture overview
- `Documentation/BMAD Method Explained_ AI Development.md` - BMAD methodology overview
- `Documentation/Claude_API_Cost_Optimization_Guide.md` - Claude API cost guide
- `Documentation/QUICK_START_SHARED_MEMORY.md` - Shared memory quick start
- `Documentation/SHARED_MEMORY_ARCHON_PROJECT_SUMMARY.md` - Archon shared memory summary
- `Documentation/START_HERE.md` - Workspace entry point
- `Documentation/Why.md` - Project rationale
- `Documentation/System/CLAUDE_WORKFLOW.md` - Claude workflow guide
- `Documentation/System/FIXED_INSTRUCTIONS.md` - Fixed instructions reference
- `Documentation/System/MANUAL_PROJECT_SETUP.md` - Manual setup guide
- `Documentation/System/System Meta-Prompt and Technical Specification.md` - System spec
- `Archive/mem.md` - Memory systems architecture (archived)
- `Archive/GIT_COMMIT_REPORT.md` - Git commit report (archived)

---

## System Documentation

### Documentation/System/

#### SYSTEM_PROMPT.md
**Location**: `~/Documents/Documentation/System/SYSTEM_PROMPT.md`
**Why**: Master system prompt for all AI agents
**When**: Created ~2026-02-13, Updated 2026-02-18 (Issue Resolution Protocol added)
**Who**: Serge Villeneuve
**What**: Core AI agent behavior specifications, Archon integration, mandatory issue tracking protocol
**Status**: Active

#### ISSUES_KNOWLEDGE_BASE.md
**Location**: `~/Documents/Documentation/System/ISSUES_KNOWLEDGE_BASE.md`
**Why**: Centralized registry of all issues and solutions for knowledge retention
**When**: Created 2026-02-18, Enhanced 2026-02-18 (Phase 2)
**Who**: Claude (Archon assignee)
**What**: Comprehensive knowledge base with 6 issues, 5-state lifecycle, 34 tags across 5 categories, search patterns, cross-referencing guidelines
**Status**: Active

#### ISSUE_TRACKING_IMPLEMENTATION_PLAN.md
**Location**: `~/Documents/Documentation/System/ISSUE_TRACKING_IMPLEMENTATION_PLAN.md`
**Why**: 5-phase plan to make issue tracking automatic and mandatory across all agents
**When**: Created 2026-02-18
**Who**: Claude (Archon assignee)
**What**: Implementation strategy for system-wide issue tracking, enforcement mechanisms
**Status**: Active (Phase 3 complete - 7/13 tasks done)

#### PHASE_1_COMPLETION_SUMMARY.md
**Location**: `~/Documents/Documentation/System/PHASE_1_COMPLETION_SUMMARY.md`
**Why**: Audit trail for Phase 1 completion (system prompt updates, knowledge base creation)
**When**: Created 2026-02-18
**Who**: Claude (Archon assignee)
**What**: Documents all Phase 1 changes, validation results, files modified
**Status**: Reference

#### PHASE_2_COMPLETION_SUMMARY.md
**Location**: `~/Documents/Documentation/System/PHASE_2_COMPLETION_SUMMARY.md`
**Why**: Audit trail for Phase 2 completion (knowledge base structure enhancement)
**When**: Created 2026-02-18
**Who**: Claude (Archon assignee)
**What**: Documents tagging system, lifecycle, search patterns, 177-line enhancement
**Status**: Reference

#### PHASE_3_COMPLETION_SUMMARY.md
**Location**: `~/Documents/Documentation/System/PHASE_3_COMPLETION_SUMMARY.md`
**Why**: Audit trail for Phase 3 completion (CLAUDE.md automation)
**When**: Created 2026-02-18
**Who**: Claude (Archon assignee)
**What**: Documents script creation, execution results (23 files updated), 100% project coverage
**Status**: Reference

#### AGENT_ORCHESTRATION.md
**Location**: `~/Documents/Documentation/System/AGENT_ORCHESTRATION.md`
**Why**: Multi-agent coordination patterns
**When**: Created ~2026-02-13
**Who**: Serge Villeneuve
**What**: Agent coordination, task delegation, conflict resolution
**Status**: Active

#### MD_FILES_MANIFEST.md
**Location**: `~/Documents/Documentation/System/MD_FILES_MANIFEST.md`
**Why**: Complete catalog of all MD files
**When**: Created 2026-02-18
**Who**: Claude (Archon assignee)
**What**: 15,222 total files, 2,559 user-created, comprehensive categories
**Status**: Active

#### MD_FILES_ORGANIZATIONAL_PLAN.md
**Location**: `~/Documents/Documentation/System/MD_FILES_ORGANIZATIONAL_PLAN.md`
**Why**: Strategy for organizing MD files
**When**: Created 2026-02-18
**Who**: Claude (Archon assignee)
**What**: 6-phase plan for filtering, indexing, maintaining documentation
**Status**: Active

---

## Projects

### Archon (Knowledge Management Platform)
**Location**: `~/Documents/Projects/Archon/`
**Tech Stack**: React + TypeScript + FastAPI + Supabase
**Status**: Active development

**Key Files**:
- `CLAUDE.md` - Development instructions
- `CONTRIBUTING.md` - Contribution guidelines
- `PRPs/ai_docs/ARCHITECTURE.md` - System architecture
- `PRPs/ai_docs/DATA_FETCHING_ARCHITECTURE.md` - TanStack Query patterns
- `PRPs/ai_docs/API_NAMING_CONVENTIONS.md` - Naming standards
- `docs/PROJECT_MANIFEST.md` - Project overview
- `docs/PHASE_2_ACTUAL_STATUS.md` - Current phase status

### Alfred (Home Automation Agent)
**Location**: `~/Documents/Projects/Alfred/`
**Tech Stack**: Python + FastAPI + Home Assistant
**Status**: Active development

**Key Files**:
- `.claude/CLAUDE.md` - AI integration instructions (Archon-first rule)
- `validation/README.md` - Validation documentation
- `tests/security/README.md` - Security testing

### BMAD-METHOD (AI Development Framework)
**Location**: `~/Documents/Projects/BMAD-METHOD/`
**Tech Stack**: YAML agents + Node.js CLI
**Status**: Active (v6 alpha)

**Key Files**:
- `CLAUDE.md` - Framework development guide
- `bmad/bmb/README.md` - Builder module
- `v6-open-items.md` - Development roadmap

### RecordMinutes (BMad Instance)
**Location**: `~/Documents/Projects/RecordMinutes/`
**Status**: Active

**Key Files**:
- `CLAUDE.md` - BMad Method v6a configuration

---

## MyExperiments

### Workspace Documentation
**Location**: `~/Documents/MyExperiments/`

**Key Files**:
- `CLAUDE.md` - Experimental workspace guidance
- `EXPERIMENTS.md` - Central experiment tracker (⭐ Check first!)
- `EXPERIMENTS_MINDMAP.md` - Visual overview

### HVAC_ideas (Production Agent)
**Location**: `~/Documents/MyExperiments/HVAC_ideas/`
**Status**: Production

**Key Files**:
- `CLAUDE.md` - 3-layer architecture instructions
- `docs/sessions/` - Historical development sessions
- `HVAC_Docs/Technical_Guides/` - HVAC technical documentation

### brainstorming (AuraOS Concept)
**Location**: `~/Documents/MyExperiments/brainstorming/`
**Status**: Planning phase

**Key Files**:
- `CLAUDE.md` - AuraOS concept documentation
- `README.md` - Project overview

### simcity-threejs-clone (Game Research)
**Location**: `~/Documents/MyExperiments/Research/simcity-threejs-clone/`
**Status**: Active

**Key Files**:
- `CLAUDE.md` - Game engine architecture
- `docs/features/` - Game mechanics
- `docs/architecture/` - Technical architecture
- `scripts/IMPLEMENTATION_GUIDE.md` - Implementation guide

---

## Archive (Historical Materials)

### Archive/DesktopOld/
**Location**: `~/Documents/Archive/DesktopOld/`
**Purpose**: Historical files from desktop cleanup
**Status**: Reference only

**Key Subdirectories**:
- `Grok/` - AI interaction transcripts
- `simulators/` - Chess and tic-tac-toe projects
- `ottomator-agents/` - Agent collection READMEs
- `jc-logo/` - Logo voting platform docs
- `LightRAG/` - RAG system documentation

---

## Documentation (Reference)

### SSD-Migration/
**Location**: `~/Documents/Documentation/SSD-Migration/`
**Status**: Reference (migration completed 2026-01-21)

**Key Files**:
- `MIGRATION_COMPLETE_SUMMARY.md` - Final status
- `SSD_Migration_Plan.md` - Original plan

### Home-Organization/
**Location**: `~/Documents/Documentation/Home-Organization/`
**Status**: Reference (reorganization completed 2026-01-22)

**Key Files**:
- `HOME_FOLDER_REORGANIZATION_PLAN.md` - Strategy
- `macOS Home Directory Reorganization Plan.md` - macOS guidance

### Tech/
**Location**: `~/Documents/Documentation/Tech/`

**Key Subdirectories**:
- `PLC/` - PLC programming documentation (5 files)
- `HA-add-todo.md` - Home Assistant notes

---

## Maintenance Instructions

### Update This Index When:

**Immediately**:
- Creating new system-level documentation
- Adding major project documentation
- Creating CLAUDE.md files

**Within Week**:
- Adding new MyExperiments projects
- Major documentation reorganization

**Monthly**:
- Review Active status files
- Archive completed projects
- Add newly discovered essential files

---

## Related Documentation

- `~/Documents/Documentation/System/MD_FILES_MANIFEST.md` - Complete file catalog
- `~/Documents/Documentation/System/MD_FILES_ORGANIZATIONAL_PLAN.md` - Organization strategy
- `~/Documents/CLAUDE.md` - Workspace AI instructions (root, kept for CLI)
- `~/Documents/Documentation/DOCUMENTATION_INDEX.md` - This file (moved from root 2026-02-22)
- `~/Documents/MyExperiments/EXPERIMENTS.md` - Experiment tracker

---

*Maintained by Serge Villeneuve*
*Created by Claude (Archon assignee) - 2026-02-18*
*Next review: 2026-03-18*
