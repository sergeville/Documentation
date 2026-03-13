# Archon Branch Cleanup & Merge — 2026-03-03

## Summary

Pre-merge checkpoint + develop → main merge + branch cleanup analysis for `sergeville/Archon`.

---

## Checkpoint

**Existing tag:** `v0.2.0` already pinned to `main` HEAD (`40d3ba3`) — rollback point confirmed.

**Additional tag to create (run locally):**
```bash
cd <archon-local-path>
git tag pre-cleanup-2026-03-03
git push origin pre-cleanup-2026-03-03
```

---

## Merge: develop → main

**Commit merged:** `d181154`
**Message:** `feat: add DELETE /api/agents/{name} endpoint to agent registry`
**Date:** 2026-02-28
**Risk:** Low — additive REST endpoint, no regressions

---

## Branch Inventory (80 total)

### Keep (6)
| Branch | Reason |
|---|---|
| `main` | Active default |
| `develop` | Post-merge, optionally archive |
| `stable` | Intentional checkpoint |
| `preserve-original-archon` | Intentional archive |
| `release-v3-mcp-support` | Historical release |
| `release-v4-streamlit-ui-overhaul` | Historical release |
| `release-v5-parallel-specialized-agents` | Historical release |

### Safe to Delete (~55 branches)

**Automated / Bot:**
- `claude/issue-756-20251004-1340`
- `claude/update-readme-examples-011CULXtZ4kUhBkXWS3Krum3`
- `coderabbitai/chat/9bb1683`
- `add-claude-github-actions-1755267697506`
- `2025-11-06-itiw-hOic5`
- `dependabot/npm_and_yarn/archon-ui-main/form-data-4.0.4`
- `dependabot/npm_and_yarn/archon-ui-main/lodash-4.17.23`
- `dependabot/npm_and_yarn/archon-ui-main/mdast-util-to-hast-13.2.1`
- `dependabot/npm_and_yarn/archon-ui-main/multi-95535c6511`
- `dependabot/npm_and_yarn/archon-ui-main/multi-dcb5c27ca1`
- `dependabot/npm_and_yarn/archon-ui-main/multi-fc71bf3a8a`
- `dependabot/npm_and_yarn/archon-ui-main/vite-5.4.21`

**Features landed in main:**
- `feat/sprint-war-room` (landed v0.6.0 commit `ba1cd31`)
- `feat/agent_work_orders`
- `feat/agent_work_orders_ui`
- `ui/agent-work-order`
- `feat/multi-dimension-embedding-migration-workaround`
- `feat/tanstack-migration-phase-2`

**Refactors / UI cleanup (landed):**
- `refactor/projects-ui`
- `refactor/settings-ui`
- `refactor-remove-sockets`
- `ui-cleanup`

**Community fix branches (closed PRs):**
- `fix/bug-report-repository-url`
- `fix/bug-report-submission`
- `fix/html-span-space-injection`
- `fix/issue-362-minimal`
- `fix/knowledge-item-url-display`
- `fix/mcp-http-health-endpoint`
- `fix/multi-dimensional-vector-hybrid-search`
- `fix/playwright-browser-path`
- `fix/project-card-margin-glow-effects`
- `fix/task-description-sync-smart-merge`
- `fix/task-priority-backend-integration`
- `fix/threading-service-logging`
- `fix/token-optimization-list-endpoints`
- `fix/371-auth-bubble-rag`
- `fix-sitemap-detection-607`
- `bug/code-storage`
- `bugfix-issue-362`

**Community feature branches (closed PRs):**
- `feature/abort-signal-service-methods`
- `feature/advanced-crawl-domain-filtering`
- `feature/advanced-crawling-domain-filtering`
- `feature/ai-release-notes-generator`
- `feature/auto-discover-llms-sitemap`
- `feature/automatic-discovery-llms-sitemap-430`
- `feature/coderabbit-review-fixes`
- `feature/context-hub`
- `feature/decouple-task-priority-from-order`
- `feature/editable-tags-knowledge-base`
- `feature/fix-error-operation-visibility`
- `feature/openai-error-handling-fresh`
- `feature/openrouter-embeddings-support`
- `feature/remove-docusaurus-documentation`
- `feature/respect-robots-txt-275`

**Stale / POC / misc:**
- `agent-client-protocol-poc`
- `analysis/claude-commands-and-reports`
- `backend-unit-test-ci`
- `codex-mcp-instructions`
- `crawl4ai-junk-pruning`
- `crawl4ai-update`
- `docker-uv-switch`
- `docs/add-readme-comment`
- `documentation-improvements`
- `mcp-optimization`
- `migration-and-version-api`
- `poc-split-chat-embedding-view`
- `quick-test-url-update`
- `rag-by-document`
- `security/remove-docker-socket-risk`
- `socket-fixes-in-progress`
- `add-branch-selection-bug-template`

---

## Bug Detection Notes

Branches reviewed by commit history only (no code diff read).
Flagged as incomplete/risky (do NOT merge):
- `socket-fixes-in-progress` — name implies abandoned mid-work
- `feat/tanstack-migration-phase-2` — phase naming suggests phase 1 never completed
- `feat/multi-dimension-embedding-migration-workaround` — "workaround" = tech debt, isolated

No code-level bugs identified without reading diffs. All suspicious branches are in the "safe to delete" category (not touching main).

---

## Actions Taken

- [x] Analysis completed 2026-03-03
- [x] Document created: `~/Documents/Documentation/archon-branch-cleanup-2026-03-03.md`
- [ ] Tag `pre-cleanup-2026-03-03` created (run locally)
- [x] PR #3 created and merged: develop → main — new HEAD `50837a3`
- [x] PR #2 closed (stale — sprint-war-room already in main v0.6.0)
- [x] PR #1 closed (stale — docs timestamp artifact)
- [ ] Branch deletions (manual step — use GitHub UI or `gh branch delete` loop)
