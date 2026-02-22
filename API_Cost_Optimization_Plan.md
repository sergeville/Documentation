# Claude API Cost Optimization Plan

**Created:** 2026-02-21
**Owner:** Serge Villeneuve
**Reference:** `~/Documents/Claude_API_Cost_Optimization_Guide.md`

---

## System Readiness Check (2026-02-21)
- ✅ Archon: 10 tasks, all `done` — clean slate
- ✅ No blocking issues
- ✅ Guide file exists and is well-structured

---

## Phase 1 — Audit (find the money)
Locate every API call in the system (Alfred service, scripts, automations):
- Search for `anthropic`, `model=`, `client.messages.create` across `~/Documents/Projects/`
- Inventory: which model, `max_tokens` set or not, system prompt size, caching enabled or not

**Status:** ✅ Complete (2026-02-21)

---

## Phase 2 — Quick Wins (high impact, low effort)

**Status:** ✅ Complete (2026-02-21)

| File | Change Made | Expected Saving |
|---|---|---|
| `HVAC_ideas/ai_tank1_diagnostic.py` | Added prompt caching on system prompt + conversation history | Up to 90% off cached turns in multi-turn sessions |
| `idea-capture-web/api_server.py` | Removed hardcoded Gemini key → env-only via `.env` | Security fix |
| `idea-capture-web/api_server.py` | Added `max_output_tokens=1024` to Gemini model config | Prevents runaway output |
| `idea-capture-web/api_server.py` | Added `python-dotenv` load at startup | `.env` auto-loaded |

**Not applied — `situation_agent.py`:** System prompt is ~10 tokens (below 1024-token cache minimum). User message (Archon state JSON) changes every run. No caching opportunity. Already has `max_tokens=1024`. No changes needed.

**Not applied — Archon internals:** Already well-optimized. Session summarizer and pattern extractor use local Ollama (free). Multi-provider abstraction handles model selection via DB config.

**Gemini key rotation:** Old key `AIzaSyB1...` deleted from Google AI Studio. New key stored in `.env` only (single clean line, no duplicates). API test pending Gemini outage resolution (Google AI Studio reported active incident 2026-02-21).

---

## Phase 3 — Structural (bigger, one-time work)
- Route batch/offline Alfred jobs through the **Batch API** (50% off everything)
- Add a context chunker to keep inputs under **200K tokens** (avoid 2x surcharge)

**Status:** ⏳ Ready to start

---

## Phase 4 — Track & Document
- Archon task to baseline current monthly API spend before changes
- Document patterns in Issues KB so future agents don't regress

**Status:** ⏳ Pending Phase 3

---

## Audit Log

### Phase 1 Results — Complete (2026-02-21)

#### 🚨 URGENT: Security Issue
- **`idea-capture-web/api_server.py` line 75**: Gemini API key hardcoded in source. **Rotate immediately.**

#### Claude/Anthropic API Consumers

| File | Model | max_tokens | Caching | System Prompt | Priority |
|---|---|---|---|---|---|
| `Scripts/situation_agent.py` | claude-sonnet-4-6 | 1024 ✅ | NO ⚠️ | ~10 tokens | Add caching → 90% off reads |
| `HVAC_ideas/ai_tank1_diagnostic.py` | claude-3-haiku-20240307 | 2000 ✅ | NO ⚠️ | ~1200 tokens | Compress prompt + cache |
| `ottomator-agents/ai-agent-fundamentals/agent.py` | claude-haiku-4.5 (OpenRouter) | NOT SET ⚠️ | NO | ~300 tokens | Add max_tokens cap |
| `MemEvolve/mini-swe-agent` | LiteLLM (dynamic) | NOT SET | YES ✅ | — | Already optimized |

#### Other LLM Consumers (Non-Claude)

| File | Provider | Model | max_tokens | Issue |
|---|---|---|---|---|
| `Alfred/core/agent.py` | Gemini + Ollama | Config-based | NOT SET ⚠️ | Unbounded Gemini output |
| `Alfred/custom_components/alfred/conversation.py` | Gemini + OpenAI | Config-based | 500 (OAI only) ⚠️ | OAI cap too low; Gemini uncapped |
| `idea-capture-web/api_server.py` | Gemini | gemini-2.0-flash | NOT SET | 🔑 Key exposed |
| `ottomator-agents/ask-reddit-agent/ai_agent.py` | OpenAI | gpt-4o-mini | NOT SET | XML prompt ~700 tok |
| `ottomator-agents/pydantic-ai-mcp-agent` | OpenAI | gpt-4o-mini | NOT SET | — |

#### Phase 1 Summary
- **Total files with API calls**: 9
- **Claude/Anthropic API**: 4 files
- **Caching enabled**: 1/4 (MemEvolve only)
- **max_tokens uncapped**: 3/4 Claude consumers
- **Security issue**: 1 (urgent)

---

---

## Token Pricing Reference (early 2026)

| Model | Input /1M | Output /1M |
|---|---|---|
| Haiku 4.5 | $1 | $5 |
| Sonnet 4.5 | $3 | $15 |
| **Sonnet 4.6** | **$3** | **$15** |
| Opus 4.6 | $5 | $25 |

> ⚠️ Inputs over 200K tokens: billed at **$6/$22.50** per 1M (entire request, not just overage) — Sonnet & Opus
> ⚠️ Prompt cache writes: 1.25x (5-min) or 2x (1-hr); cache reads: **0.1x** (90% off)
