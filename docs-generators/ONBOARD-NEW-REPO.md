# How to add doc-generators to a new repo

## Step 1 — Fill in the two blanks

Open the prompt template below. Replace the two `[BRACKETED]` values:

| Placeholder | What to put |
|---|---|
| `[WHAT TO INDEX]` | What files/folders to scan (e.g. `all .md files in docs/`, `all stories in stories/`, `all API routes in src/api/`) |
| `[OUTPUT FILE NAME]` | Name of the generated file (e.g. `AGENT_MANIFEST.md`, `PROJECT_INDEX.md`, `DOCS_INDEX.md`, `SPRINT_MANIFEST.md`) |

## Step 2 — Open a Claude Code session in the target repo

```
cd ~/Documents/Projects/your-repo
claude
```

## Step 3 — Paste the prompt

```
Add the docs-generator framework to this repo.

Index: [WHAT TO INDEX]
Output file: [OUTPUT FILE NAME]

---

Context:
- A global pre-commit hook is already installed at ~/.config/git/hooks/pre-commit
- It calls `docs-generators/run.sh` if present in the repo root — nothing else needed
- The hook chains any existing local hooks — nothing will break

What to build:
1. `docs-generators/run.sh` (executable) — calls the generator + git add the output file
2. `docs-generators/gen-<name>.py` (Python 3, no pip dependencies) — scans the repo,
   produces [OUTPUT FILE NAME], surfaces any new unrecognized files as "uncategorized"
3. [OUTPUT FILE NAME] at repo root — categorized markdown table, agent-optimized
4. `AGENTS.md` at repo root — universal LLM boot file for this project

Rules:
- Use Python 3 (macOS bash is 3.2 — no associative arrays)
- Do NOT modify ~/.config/git/hooks/pre-commit
- Do NOT touch .git/hooks/ — the global hook chains them automatically

Reference implementation: ~/Documents/Documentation/docs-generators/
  gen-manifest.py — generator to follow as model
  run.sh          — runner to follow as model

After building, verify with:
  bash docs-generators/run.sh
Then make a test commit to confirm the hook fires automatically.
```

## Step 4 — Verify

After Claude builds it:

```bash
bash docs-generators/run.sh        # should print: → <output-file> written
git add -A && git commit -m "test" # should print: [docs-generators] Running generators...
```

---

## Examples

### BMAD project (stories + epics)
- `[WHAT TO INDEX]` → `all story files in stories/ and epic files in epics/`
- `[OUTPUT FILE NAME]` → `SPRINT_MANIFEST.md`

### Next.js app (pages + API routes)
- `[WHAT TO INDEX]` → `all pages in app/ and API routes in app/api/`
- `[OUTPUT FILE NAME]` → `PROJECT_INDEX.md`

### Scripts repo
- `[WHAT TO INDEX]` → `all .sh files — use first comment line as description`
- `[OUTPUT FILE NAME]` → `SCRIPTS_INDEX.md`

### Generic docs repo
- `[WHAT TO INDEX]` → `all .md files — categorize by folder`
- `[OUTPUT FILE NAME]` → `DOCS_INDEX.md`
