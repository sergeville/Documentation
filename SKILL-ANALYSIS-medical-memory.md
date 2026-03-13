# SKILL Analysis Report — Medical-memory
**File Analyzed:** `~/Documents/Projects/medical-diagnostic/skills/Medical-memory/SKILL.md`
**Role Applied:** Data · Memory · Logic Agent
**Date:** 2026-03-11
**Analyst:** Claude (Sonnet 4.6)

---

## Executive Summary

The `Medical-memory` skill manages persistent storage of medical diagnostic conversations using MCP tools.
It contains **9 security issues**, **8 efficiency issues**, and **8 logic issues** — several are high severity given the PHI (Protected Health Information) nature of the data.
The skill is functional for low-volume, single-user, non-regulated use but **must not be deployed in any HIPAA or production medical environment without the fixes below.**

---

## 1. Security Issues

### CRITICAL

| # | Issue | Location | Risk |
| - | ----- | -------- | ---- |
| S1 | **PHI stored in `.tmp/`** — temp dir is world-readable on macOS, subject to OS cleanup, accessible by other processes | `Storage Structure` section | Data leakage, loss |
| S2 | **No encryption at rest** — all conversations stored as plaintext JSON including patient_id, symptoms, diagnoses | `file_path` field | PHI exposure |
| S3 | **No access control** — no authentication or authorization check before save/load/delete operations | entire skill | Unauthorized access |
| S4 | **Insecure deletion** — `delete_conversation()` likely just removes the file; on macOS/HFS+/APFS, data persists until overwritten | `delete_conversation` section | PHI recovery after delete |

### HIGH

| # | Issue | Location | Risk |
| - | ----- | -------- | ---- |
| S5 | **Predictable, enumerable session_id** — `conversation_20260130_123456` format leaks timestamp and is trivially enumerable | `session_id` field | Session enumeration attack |
| S6 | **Unvalidated metadata dict** — arbitrary key/value pairs accepted with no sanitization; if metadata is later queried or indexed, path-traversal or injection possible | `metadata` parameter | Injection, unexpected behavior |
| S7 | **keyword search unsanitized** — `keywords=["appendicitis"]` fed directly to matcher; no regex escaping shown | `search_conversations` | Regex injection if implemented as regex |
| S8 | **No audit log** — no record of who accessed, modified, or deleted a conversation | entire skill | HIPAA audit trail requirement |

### MEDIUM

| # | Issue | Location | Risk |
| - | ----- | -------- | ---- |
| S9 | **`patient_id` embedded in plain metadata** — PII should be hashed or referenced by opaque token, not stored in clear in searchable fields | `metadata.patient_id` | PII exposure in logs/indexes |

---

## 2. Efficiency Issues

| # | Issue | Impact | Fix |
| - | ----- | ------ | --- |
| E1 | **File-per-conversation flat storage** — search requires opening every file; does not scale past ~1000 sessions | O(n) reads on every search | Use SQLite index or append-only log with separate index file |
| E2 | **`search_conversations` is O(n) full scan** — no inverted index, no pre-built keyword→session lookup | High latency at scale | Build a `keywords_index.json` on save; query the index instead |
| E3 | **`list_conversations(limit=50)` hardcoded default** — no offset/cursor parameter for pagination | UI will miss sessions > 50 | Add `offset` or `after_id` cursor parameter |
| E4 | **No compression** — medical conversation files can be large (hundreds of turns); stored uncompressed | 3–5× unnecessary disk use | Store as `.json.gz`; decompress on load |
| E5 | **Naive `match_score` (keyword count only)** — no TF-IDF, no field weighting (title vs. body), no semantic distance | Poor relevance ranking | Weight `primary_symptom` matches higher; use simple frequency normalization |
| E6 | **`first_message` preview unspecified** — no defined truncation length or strategy; could cut mid-word or mid-sentence | Bad UX in session list | Truncate to 80 chars at word boundary |
| E7 | **No caching layer** — `list_conversations` re-reads all file metadata on every call | Repeated I/O for UI refreshes | Cache list in memory; invalidate on save/delete |
| E8 | **Context window overflow on `load_conversation`** — restoring full message history for long sessions (200+ turns) can exceed Claude's context budget | Silent truncation or error | Add `max_messages` parameter + auto-summarize older turns |

---

## 3. Logic Issues

| # | Issue | Location | Risk |
| - | ----- | -------- | ---- |
| L1 | **No session_id uniqueness guarantee** — two saves within the same second produce identical IDs; second write silently overwrites first | `session_id` generation | Silent data loss |
| L2 | **No atomic write** — if process dies mid-write, a partial/corrupt JSON file is left on disk | `save_conversation` | Corrupt state; crash on next load |
| L3 | **No schema validation on `metadata`** — required fields like `patient_id`, `outcome` are not enforced | `metadata` parameter | Inconsistent records; failed searches |
| L4 | **`session_type` hardcoded in example** — `"session_type": "medical_sessions"` baked into example code instead of coming from a constant or config | `save_conversation` example | Copy-paste drift; wrong session_type silently stored |
| L5 | **No session TTL/expiry** — old sessions accumulate indefinitely with no lifecycle policy | entire skill | Disk fill, stale PHI retained past need |
| L6 | **No deduplication** — same conversation can be saved multiple times producing multiple IDs; no idempotency key | `save_conversation` | Duplicate records; inflated list |
| L7 | **Non-standard storage path** — `.tmp/user_data/conversations/` is ephemeral on some systems and not clearly documented as project-relative vs. absolute | `Storage Structure` | Path breaks across environments |
| L8 | **`delete_conversation` return value not verifiable** — returns `{"success": True}` but provides no tombstone; a deleted session_id could be re-created silently | `delete_conversation` | Confusion between new and deleted sessions |

---

## 4. Recommended Changes (Priority Order)

### P0 — Do immediately (blockers for any real use)

```text
1. Move storage from .tmp/ to a stable, protected path:
   ~/Documents/Projects/medical-diagnostic/.data/conversations/
   (add to .gitignore)

2. Add write-then-rename atomic save:
   write to conversation_<id>.json.tmp → rename to conversation_<id>.json

3. Generate session_id with UUID4, not timestamp:
   session_id = str(uuid.uuid4())

4. Add required metadata fields validation before save:
   required = ["patient_id", "primary_symptom", "outcome"]
```

### P1 — High priority (security posture)

```text
5. Add filesystem-level access restriction:
   chmod 700 on the conversations directory

6. Implement secure delete (overwrite before unlink):
   import os; open(path, 'wb').write(os.urandom(os.path.getsize(path))); os.unlink(path)

7. Hash patient_id before storing:
   import hashlib; hashed = hashlib.sha256(patient_id.encode()).hexdigest()[:16]

8. Add audit_log.jsonl alongside conversations/:
   append {action, session_id, timestamp} on every save/load/delete
```

### P2 — Efficiency (performance & usability)

```text
9.  Build keywords_index.json updated on every save/delete
10. Add offset parameter to list_conversations
11. Truncate first_message preview at 80 chars (word boundary)
12. Add max_messages=50 parameter to load_conversation
    with auto-summary of older turns
```

### P3 — Logic cleanup

```text
13. Define SESSION_TYPE constant, not inline string
14. Add TTL field to metadata (e.g., retain_until: ISO date)
    with periodic cleanup script
15. Add idempotency_key option to save_conversation
    to prevent duplicate saves of the same session
```

---

## 5. Priority Matrix

| Priority | Count | Issues |
| -------- | ----- | ------ |
| P0 (Blocker) | 4 | S1, S2, L1, L2 |
| P1 (High) | 5 | S3, S4, S5, S8, S9 |
| P2 (Medium) | 7 | E1–E8 (minus E8→P1), S6, S7 |
| P3 (Low) | 5 | L3–L8 |

---

## 6. What Was NOT Changed

The skill's **purpose, MCP tool interface, and domain logic** are sound and should be preserved:
- The 5-tool API (`save`, `load`, `list`, `search`, `delete`) is clean and complete
- MCP Orchestrator pattern (no direct file access from skill) is correct
- Metadata-driven tagging approach is good
- Example code is illustrative and clear

The fixes above are **additive hardening** — they do not change the interface contract.

---

*Report generated by Claude Sonnet 4.6 — 2026-03-11*
*Source skill: `Projects/medical-diagnostic/skills/Medical-memory/SKILL.md`*
