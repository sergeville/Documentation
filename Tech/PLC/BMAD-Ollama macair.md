# Setting Up Ollama with Docker and BMAD Method on MacBook Air

This guide provides a complete, step-by-step process to run Ollama in Docker and integrate it with the BMAD Method (Breakthrough Method of Agile AI-Driven Development) on a MacBook Air. It assumes you're starting from scratch but includes checks for pre-installed software. 

**Important Notes:**
- MacBook Air (Apple Silicon, M1/M2/M3) works great with Ollama and Docker, as both support ARM architecture.
- BMAD is a Node.js-based framework for AI-driven development using prompt-based agents. It primarily integrates with chat-based AI interfaces (e.g., custom GPTs or local LLMs). For Ollama, we'll use a local web interface like Open WebUI to simulate agent interactions.
- Total time: ~30-60 minutes, depending on downloads.
- If you encounter issues (e.g., due to hardware limits—MacBook Air has limited RAM), start with smaller models like `phi3` (3B parameters) instead of `llama3` (8B+).

## Prerequisites and Checks

Before starting, verify if key software is already installed. Open Terminal (Cmd + Space, type "Terminal") and run these commands:

1. **Check Docker**:
   ```
   docker --version
   ```
   - **If installed** (e.g., shows "Docker version 27.x"): Skip to Ollama setup. Ensure Docker Desktop is running (check the menu bar whale icon).
   - **If not**: Install Docker Desktop for Mac from [docker.com](https://www.docker.com/products/docker-desktop/). Download the Apple Silicon version, install, and launch it. Sign in if prompted (free tier is fine). Restart Terminal.

2. **Check Node.js** (required for BMAD):
   ```
   node --version
   ```
   - **If installed** (v20 or higher, e.g., "v20.10.0"): Proceed.
   - **If not or outdated**: Install via Homebrew (if you have it) or directly.
     - Install Homebrew if needed: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
     - Then: `brew install node` (ensures v20+).
     - Verify: `node --version` should now show v20+.

3. **Check for Existing BMAD**:
   - In a project folder (or create one: `mkdir my-bmad-project && cd my-bmad-project`), run:
     ```
     npx bmad-method --help
     ```
   - **If it works** (shows commands): BMAD is installed globally or via npx cache. Update it later in the BMAD section.
   - **If not**: Proceed to install.

## Section 1: Running Ollama in Docker

Ollama runs as a lightweight server for local LLMs. We'll use Docker for isolation and persistence.

### Step 1: Pull the Ollama Image
```
docker pull ollama/ollama:latest
```
- This downloads ~500MB. If already pulled (check with `docker images | grep ollama`), skip.

### Step 2: Create a Persistent Volume
This stores models (~5-20GB per model) outside the container:
```
docker volume create ollama
```

### Step 3: Run the Ollama Container
Start the server:
```
docker run -d \
  --init \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama \
  --platform linux/arm64 \
  ollama/ollama serve
```
- `--platform linux/arm64`: Ensures Apple Silicon compatibility.
- Verify: `docker ps` (should show "ollama" running). Test API: `curl http://localhost:11434/api/tags` (returns JSON, possibly empty).

### Step 4: Pull and Test a Model
Exec into the container to download a model:
```
docker exec -it ollama ollama pull llama3.1:8b
```
- This downloads ~4.7GB (quantized). Use `phi3:mini` (~2GB) if RAM is tight (<16GB).
- Test interactively:
  ```
  docker exec -it ollama ollama run llama3.1:8b "Hello, world!"
  ```
- Exit with `/bye`. Models persist in the volume.

### Step 5: Install a Web UI for Easier Interaction (Recommended for BMAD)
BMAD relies on chat interfaces, so use Open WebUI for a browser-based Ollama frontend:
1. Pull the image:
   ```
   docker pull ghcr.io/open-webui/open-webui:main
   ```
2. Run it (links to Ollama):
   ```
   docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
   ```
3. Open http://localhost:3000 in your browser. Sign up (admin user), select your model (llama3.1:8b), and chat to test.

**Management Commands**:
- Stop: `docker stop ollama open-webui`
- Start: `docker start ollama open-webui`
- Logs: `docker logs ollama`
- Remove (if needed): `docker rm -v ollama open-webui` (deletes data—backup first).

## Section 2: Installing and Setting Up BMAD Method

BMAD uses AI agents for roles like Analyst and Developer. Installation is via npm/npx.

### Step 1: Install BMAD
In your project folder (`cd my-bmad-project`):
```
npx bmad-method install
```
- This sets up files like `core-config.yaml`, team prompts, and scripts. It detects upgrades if BMAD exists.
- If errors (e.g., permissions), add `sudo` or fix npm config.
- Verify: `ls` should show new folders like `bmad/`, `docs/`, and Markdown files (e.g., `PRD.md`).

### Step 2: Update BMAD (If Already Installed)
```
npx bmad-method install --upgrade
```
- Backs up custom changes.

### Step 3: Quick Start BMAD Workflow
1. Review the generated files (e.g., open `bmad/team-fullstack.txt` in VS Code—install if needed: `brew install --cask visual-studio-code`).
2. For a new project:
   - Edit `project-brief.md` with your idea.
   - Run agents via chat (see integration below) or CLI: `npx bmad-method analyst --brief "Build a todo app"`.

For full details, see the [BMAD User Guide](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/user-guide.md) or run `npx bmad-method help`.

## Section 3: Integrating BMAD with Ollama

BMAD is LLM-agnostic but designed for chat-based agents. Use Open WebUI (from Section 1) as your "custom agent" interface:

### Step 1: Prepare BMAD Team File
- Download or copy `team-fullstack.txt` from [GitHub](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/dist/teams/team-fullstack.txt).
- This defines agents (e.g., Analyst, Architect) with prompts.

### Step 2: Configure in Open WebUI
1. Go to http://localhost:3000 > Settings > Models > Select `llama3.1:8b`.
2. Create a new "Chat" or "Agent":
   - Paste the contents of `team-fullstack.txt` into the system prompt.
   - Add instruction: "You are the BMAD Orchestrator. Your critical operating instructions are in the attached team file—do not break character. Use *help for commands."
3. Save and start chatting:
   - Type `*help` to list commands (e.g., `*analyst` to generate briefs).
   - Follow the workflow: Analyst → Product Manager → Architect → Developer.
   - Reference your project files by copying/pasting (or use WebUI's file upload if available).

### Step 3: Advanced API Integration (Optional)
If you want scripted automation (e.g., via Node.js in BMAD):
- Edit `core-config.yaml` (if present) or create a custom script to call Ollama's API:
  ```javascript
  // Example in a BMAD script (add to package.json scripts)
  const ollama = require('ollama').default;
  async function queryAgent(prompt) {
    const response = await ollama.chat({
      model: 'llama3.1:8b',
      messages: [{ role: 'system', content: 'BMAD Team Instructions...' }, { role: 'user', content: prompt }]
    });
    return response.message.content;
  }
  ```
- Install Ollama JS client: `npm install ollama`.
- Run: `node your-script.js`.
- This routes BMAD prompts to `http://host.docker.internal:11434`.

For non-code workflows, stick to the WebUI method—it's simplest for MacBook Air.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Docker won't start | Restart Mac, check Virtualization in System Settings > General > About (should be enabled). |
| Ollama pull fails (out of memory) | Use smaller model: `ollama pull phi3`. Close apps to free RAM. |
| Node.js install errors | Run `brew doctor` and fix warnings. |
| BMAD install fails | Clear npx cache: `npx clear-npx-cache`. Ensure project is Git repo: `git init`. |
| Slow responses | MacBook Air limits: Use 8B models max; add swap if <8GB RAM. |
| WebUI not connecting to Ollama | Ensure both containers run; use `host.docker.internal:11434` in WebUI settings. |

## Next Steps
- Start a sample project: Use `*analyst` in WebUI with "Create a simple weather app."
- Explore BMAD expansions: `npx bmad-method expansion --list`.
- Resources: [BMAD GitHub](https://github.com/bmad-code-org/BMAD-METHOD), [Ollama Docs](https://ollama.com/docs), [Open WebUI](https://openwebui.com).

Enjoy your local AI dev setup! If stuck, share error logs. 🚀