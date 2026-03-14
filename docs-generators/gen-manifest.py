#!/usr/bin/env python3
"""
gen-manifest.py — Generates AGENT_MANIFEST.md from System/ contents.
Curate metadata below. New System/ files not in metadata appear as uncategorized.
"""

import os
import sys
from datetime import datetime

REPO_ROOT = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
SYSTEM_DIR = os.path.join(REPO_ROOT, "System")
OUTPUT = os.path.join(REPO_ROOT, "AGENT_MANIFEST.md")

# ── Metadata ──────────────────────────────────────────────────────────────────
# (filename, category, purpose, read_when)
# Categories: core | ops | reference | archive
META = [
    # CORE
    ("SYSTEM_PROMPT.md",           "core", "Master cognitive protocol — identity, Archon rules, BMAD gate",              "every session"),
    ("CLAUDE_ORCHESTRATION.md",    "core", "Claude executor protocol — delegation, swarm, handoff schema",               "every session"),
    ("CLAUDE_WORKFLOW.md",         "core", "Archon-BMAD integration package for Claude",                                 "every session"),
    ("MASTER_VISION_2026.md",      "core", "Strategic vision — what you're building and why",                            "every session"),

    # OPS
    ("PORT_REGISTRY.md",           "ops",  "Source of truth for all local service port assignments",      "before any port change"),
    ("SCRIPTS_REGISTRY.md",        "ops",  "Registry of all scripts in ~/Documents/Scripts/",             "before creating/running scripts"),
    ("PLANS_INDEX.md",             "ops",  "Index of all active plans across ~/Documents",                "before any project work"),
    ("ISSUES_KNOWLEDGE_BASE.md",   "ops",  "Known issues + solutions registry",                           "before solving any problem"),
    ("SEARCH_PROTOCOL.md",         "ops",  "Fastest macOS search path (Spotlight first)",                 "when searching filesystem"),
    ("CREDENTIAL_ROTATION_GUIDE.md","ops", "How to rotate Supabase and other credentials",                "auth/credentials work"),
    ("SHELL_FUNCTIONS.md",         "ops",  "Custom zsh aliases and shell functions",                      "when using custom shell commands"),
    ("CRON-INSTRUCTIONS.md",       "ops",  "Migration status cron job reference",                         "cron job changes"),
    ("SECURITY.md",                "ops",  "Active vulnerabilities and remediation status",               "any security-relevant changes"),
    ("MANUAL_PROJECT_SETUP.md",    "ops",  "Manual Archon project creation steps",                        "setting up new Archon project"),
    ("IDEA_DATA_ARCHITECTURE.md",  "ops",  "Single source of truth for idea data flow",                   "idea-capture system work"),

    # REFERENCE
    ("AI-SYSTEM-ORIENTATION.md",   "reference", "Big picture overview of the AI-augmented dev system",          "onboarding/orientation"),
    ("AGENT_ORCHESTRATION.md",     "reference", "Gemini conductor protocol for multi-agent coordination",       "multi-agent work"),
    ("UNIFIED_SYSTEM_VISION.md",   "reference", "Plain-language system overview",                               "understanding the system"),
    ("MASTER_TODO.md",             "reference", "Single-view of all ideas, plans, tasks",                       "planning sessions"),
    ("EXPERTISE_DEVELOPMENT_PLAN.md","reference","Learning and skills roadmap",                                  "career/skill planning"),
    ("ACTION_PLAN.md",             "reference", "Current weekly action items",                                  "weekly review"),
    ("LEARNING_LOG.md",            "reference", "Daily learning log",                                           "knowledge capture"),
    ("SESSION_LOGGER.md",          "reference", "Session logging system docs",                                  "understanding logging"),
    ("FIXED_INSTRUCTIONS.md",      "reference", "Project loading fix for Archon DB issue",                      "Archon DB problems"),
    ("System Meta-Prompt and Technical Specification.md",
                                   "reference", "Legacy meta-prompt for Alfred/Archon agents",                  "Alfred agent setup"),

    # ARCHIVE
    ("PHASE_1_COMPLETION_SUMMARY.md",   "archive", "Completed: Issue tracking implementation phase 1"),
    ("PHASE_2_COMPLETION_SUMMARY.md",   "archive", "Completed: Knowledge base structure enhancement"),
    ("PHASE_3_COMPLETION_SUMMARY.md",   "archive", "Completed: CLAUDE.md automation"),
    ("PHASE_4_1_COMPLETION_SUMMARY.md", "archive", "Completed: Session logger auto-detection"),
    ("PHASE_4_2_COMPLETION_SUMMARY.md", "archive", "Completed: Test auto-detection + add-issue.sh"),
    ("PHASE_4_3_COMPLETION_SUMMARY.md", "archive", "Completed: Session logger → knowledge base link"),
    ("PHASE_4_COMPLETION_SUMMARY.md",   "archive", "Completed: Session logger enhancements"),
    ("PHASE_5_1_COMPLETION_SUMMARY.md", "archive", "Completed: search-issues.sh tool"),
    ("PHASE_5_2_COMPLETION_SUMMARY.md", "archive", "Completed: issue-stats.sh analytics"),
    ("PHASE_5_3_COMPLETION_SUMMARY.md", "archive", "Completed: validate-knowledge-base.sh"),
    ("PHASE_5_COMPLETION_SUMMARY.md",   "archive", "Completed: Maintenance tools suite"),
    ("SESSION_SUMMARY_2026-02-18.md",   "archive", "Historical: 2026-02-18 session summary"),
    ("System_Hang_Investigation_and_Refactoring_2025-07-17.md", "archive", "Historical: 2025 system hang investigation"),
    ("TERMINAL_RECOVERY_STATE.md",      "archive", "Historical: 2026-01-21 SSD migration recovery"),
    ("ARCHON_MCP_FIX_SUMMARY.md",       "archive", "Historical: Archon MCP config fix (resolved)"),
    ("ARCHON_PROJECT_CREATION_ISSUE.md","archive", "Historical: Archon project creation MCP issue"),
    ("ARCHON_RAG_VALIDATION.md",        "archive", "Historical: Archon RAG tools validation"),
    ("CLAUDE_INTEGRATION_REPORT.md",    "archive", "Historical: Claude-Archon integration report"),
    ("SECURITY_AUDIT_FINAL_REPORT.md",  "archive", "Historical: Security audit final report 2026-02-18"),
    ("MD_FILES_ORGANIZATIONAL_PLAN.md", "archive", "Historical: MD files organization plan 2026-02-18"),
    ("ORCHESTRATION_ELABORATION_PLAN.md","archive","Historical: Orchestration spec elaboration plan"),
    ("Starlink-TV-WiFi-Fix.md",         "archive", "Historical: Starlink TV WiFi fix (resolved)"),
    ("Schedule Supabase Rotation for Later.md", "archive", "Historical: Supabase rotation deferred task"),
    ("ISSUES_AND_FIXES_LOG.md",         "archive", "Superseded by ISSUES_KNOWLEDGE_BASE.md"),
    ("workflow_state.md",               "archive", "Duplicate of CLAUDE_WORKFLOW.md"),
    ("BMAD_V6_INSTALL_PLAN.md",         "archive", "Historical: BMAD V6 install plan (completed)"),
    ("AGENT_MANIFEST.md",               "archive", "This file — skip"),
]

# ── Build lookup ───────────────────────────────────────────────────────────────
meta_map = {row[0]: row for row in META}

# ── Scan System/ ──────────────────────────────────────────────────────────────
buckets = {"core": [], "ops": [], "reference": [], "archive": [], "unknown": []}

if os.path.isdir(SYSTEM_DIR):
    for fname in sorted(os.listdir(SYSTEM_DIR)):
        if not fname.endswith(".md") or fname == "AGENT_MANIFEST.md":
            continue
        row = meta_map.get(fname)
        cat = row[1] if row else "unknown"
        buckets[cat].append(fname)

# ── Write manifest ─────────────────────────────────────────────────────────────
now = datetime.now().strftime("%Y-%m-%d %H:%M")
today = datetime.now().strftime("%Y-%m-%d")

active = len(buckets["core"]) + len(buckets["ops"]) + len(buckets["reference"])
archived = len(buckets["archive"])
unknown = len(buckets["unknown"])

lines = []
lines.append(f"# AGENT MANIFEST — System/")
lines.append(f"*Auto-generated {now} by docs-generators/gen-manifest.py*")
lines.append(f"*Do not edit manually — overwritten on every commit.*")
lines.append("")
lines.append("## How to use")
lines.append("Read this file first. Match your task to a category. Open **only** the listed file(s).")
lines.append("Files marked **archive** are historical — skip unless investigating past work.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 🔴 Core — Read on every session start")
lines.append("")
lines.append("| File | Purpose |")
lines.append("|---|---|")
for f in buckets["core"]:
    row = meta_map[f]
    lines.append(f"| `{f}` | {row[2]} |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## 🟡 Operations — Read when task matches")
lines.append("")
lines.append("| File | Read when | Purpose |")
lines.append("|---|---|---|")
for f in buckets["ops"]:
    row = meta_map[f]
    lines.append(f"| `{f}` | {row[3]} | {row[2]} |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## 🔵 Reference — Background context")
lines.append("")
lines.append("| File | Purpose | Read when |")
lines.append("|---|---|---|")
for f in buckets["reference"]:
    row = meta_map[f]
    lines.append(f"| `{f}` | {row[2]} | {row[3]} |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## ⚪ Archive — Historical, completed, or superseded")
lines.append("")
lines.append("Do not read. Safe to move to `~/Documents/Archive/` if noise is an issue.")
lines.append("")
lines.append("| File | Notes |")
lines.append("|---|---|")
for f in buckets["archive"]:
    row = meta_map.get(f)
    note = row[2] if row else "—"
    lines.append(f"| `{f}` | {note} |")

if buckets["unknown"]:
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## ❓ Uncategorized — Add to docs-generators/gen-manifest.py")
    lines.append("")
    lines.append("| File |")
    lines.append("|---|")
    for f in buckets["unknown"]:
        lines.append(f"| `{f}` |")

lines.append("")
lines.append(f"_Updated: {today} — {active} active files, {archived} archived, {unknown} uncategorized_")
lines.append("")

with open(OUTPUT, "w") as fh:
    fh.write("\n".join(lines))

print(f"  → AGENT_MANIFEST.md written ({active} active, {archived} archived, {unknown} uncategorized)")
