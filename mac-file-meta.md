# mac-file-meta — macOS File Tagger & Smart Folder Cleaner

**Script location:** `~/Documents/Scripts/mac-file-meta.py`

---

## What It Does

Tags any file with up to 5 Finder tags and a Spotlight comment — both are indexed by macOS Spotlight so they're instantly searchable. The `clean` command does the full sweep automatically: remove `.DS_Store`, convert HEIC screenshots to PNG, organise images into subfolders, and tag every source file by type and context.

---

## Quickstart

### Tag a single file
```bash
python3 ~/Documents/Scripts/mac-file-meta.py tag README.md \
  --tags "readme,docs,project" \
  --desc "Project overview and setup guide"
```

### Show current tags and comment
```bash
python3 ~/Documents/Scripts/mac-file-meta.py show README.md
```

### Clean and tag an entire project (smartest way)
```bash
# Preview first — no changes
python3 ~/Documents/Scripts/mac-file-meta.py clean ~/Documents/Projects/MyProject --dry-run

# Apply for the first time
python3 ~/Documents/Scripts/mac-file-meta.py clean ~/Documents/Projects/MyProject

# Refresh all tags (e.g. after adding new rules)
python3 ~/Documents/Scripts/mac-file-meta.py clean ~/Documents/Projects/MyProject --retag
```

---

## Recommended Workflow

```
New project landed?
  1. Run clean once (no --retag) → tags everything that has no tags yet
  2. Preview with --dry-run first if unsure

Added new files?
  1. Run clean again (no --retag) → only tags the new untagged files, skips the rest

Changed the rules or want fresh tags?
  1. Run clean --retag → re-applies rules to every file, overwrites old tags
```

**Golden rule:** `clean` without `--retag` is safe to re-run any time — it skips already-tagged files.

---

## Make It Accessible From Anywhere

Add a short alias to `~/.zshrc`:

```bash
alias mac-meta="python3 ~/Documents/Scripts/mac-file-meta.py"
```

Then reload:
```bash
source ~/.zshrc
```

Now you can use:
```bash
mac-meta clean ~/Documents/Projects/SomeProject
mac-meta tag myfile.jsx --tags "react,component,ui"
mac-meta show myfile.jsx
```

---

## What Gets Tagged (Built-in Rules)

### Source Code — `file_rules` (tag in-place, any project)

| Files | Tags |
|---|---|
| `README.md` | readme, docs, markdown |
| `MASTER_PROMPT.md` | master-prompt, handoff, agile, sprint |
| `NEXT_STEPS.md` | next-steps, handoff, sprint, todo |
| `TASKLIST.md` | tasklist, backlog, sprint, todo |
| `CHANGELOG.md` | changelog, history, agile |
| `docs/*.md` | docs, markdown, agile |
| `*.md` (fallback) | markdown, docs |
| `src/components/*.jsx/.tsx` | react, component, ui |
| `src/hooks/*.js/.ts` | hook, react, state |
| `src/data/*.js/.ts` | data, canonical, workflow |
| `src/session/*.js/.ts` | session, state, workflow |
| `src/chat/*.js/.ts` | chat, intent, operator |
| `src/agent/*.js/.ts` | agent, contract, validation |
| `src/*.jsx/.tsx` | react, ui, src |
| `src/*.css` | css, styles, ui, design-system |
| `src/*.js/.ts` | javascript, src, frontend |
| `server/*.js/.ts` | server, backend, api |
| `agent/*.js/.ts` | agent, engine, validation |
| `test/*.js/.ts` | test, jest, unit-test |
| `vite.config.*` | config, vite, build |
| `package.json` | config, npm, dependencies |
| `*.json` | json, config |
| `*.yaml/.yml` | yaml, config |
| `*.sh` | shell, script |
| `*.html` | html, markup, frontend |
| Images in `review/agile-ui/` | agile-ui, sprint, screenshot, idea-to-sprint |
| Images in `review/app-obd/` | obd, app, screenshot, testing |
| Images in `review/competitor/` | competitor, research, obd, car-scanner |
| Images in `review/ios-setup/` | ios, setup, provisioning, screenshot |
| Images in `review/references/` | reference, design, agile, inspiration |
| `*.png/.jpg/.gif` (fallback) | image, screenshot, asset |
| `docs/*.pdf` | pdf, docs, reference |
| `*.pdf` (fallback) | pdf, document |

### Screenshots — `subfolders` (move into subdirs, specific to review/ folder)
Patterns like `ios-`, `app-obd-`, `car-scanner-`, `app-agile`, `reference` → moved into `ios-setup/`, `app-obd/`, `competitor/`, `agile-ui/`, `references/` and tagged.

---

## Custom Rules for a Different Project

Create a `rules.json` file, then pass it with `--rules`:

```json
{
  "cleanup": { "convert_heic": true, "remove_ds_store": true },
  "subfolders": {
    "design": {
      "patterns": ["mockup-", "wireframe-", "figma-"],
      "tags": ["design", "mockup", "ux"],
      "desc": "UI design mockup or wireframe"
    }
  },
  "file_rules": [
    {
      "paths": ["src/api/"],
      "extensions": [".ts"],
      "tags": ["api", "backend", "typescript"],
      "desc": "TypeScript API module"
    }
  ]
}
```

```bash
mac-meta clean ~/Documents/Projects/SomeProject --rules ~/path/to/rules.json
```

---

## Spotlight Search — What You Get

After tagging, these searches work instantly in Spotlight (`Cmd+Space`) and Terminal:

```bash
# Find all sprint-related files across all projects
mdfind 'kMDItemUserTags == "sprint"'

# Find all agile-ui screenshots
mdfind 'kMDItemUserTags == "sprint" && kMDItemUserTags == "agile-ui"'

# Find files by comment keyword
mdfind 'kMDItemFinderComment == "*React UI*"cd'

# Scoped to a folder
mdfind -onlyin ~/Documents/Projects 'kMDItemUserTags == "validation"'
```

The Finder sidebar tag filter also works — click any tag in the sidebar to see all matching files across all drives.

---

## Skipped Directories

The walker automatically skips: `node_modules/`, `.git/`, `dist/`, `.claude/`, `__pycache__/`

---

## Flags Reference

| Flag | Effect |
|---|---|
| `--dry-run` | Preview only — print what would happen, change nothing |
| `--retag` | Re-tag files that already have tags (overwrite) |
| `--rules <path>` | Use a custom JSON rules file instead of the built-in defaults |
