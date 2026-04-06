# HVAC AI Assistant — MVP Spec
*Status: Draft | Date: 2026-03-25 | Owner: Serge Villeneuve*

---

## 1. Product Summary

A local-first AI assistant packaged for HVAC companies to deploy for their non-technical customers. Answers HVAC-related questions, captures voice input, maintains an encrypted user profile, and escalates to a human agent when it can't help.

**Core promise:** Works offline. Doesn't require the customer to understand AI. Hands off gracefully.

---

## 2. Architecture

```
┌─────────────────────────────────────┐
│           Customer Device            │
│                                      │
│  ┌──────────┐   ┌─────────────────┐ │
│  │  Voice   │──▶│  STT (Whisper)  │ │
│  │  Input   │   └────────┬────────┘ │
│  └──────────┘            │          │
│                          ▼          │
│  ┌──────────────────────────────┐   │
│  │      Local RAG Engine        │   │
│  │  (scoped HVAC knowledge)     │   │
│  │  Chroma / SQLite-vec         │   │
│  └──────────┬───────────────────┘   │
│             │                        │
│  ┌──────────▼───────────────────┐   │
│  │  Claude API (primary LLM)    │   │
│  │  Rules engine (guardrails)   │   │
│  └──────────┬───────────────────┘   │
│             │                        │
│  ┌──────────▼───────────────────┐   │
│  │  Encrypted User Profile      │   │
│  │  (AES-256, local keychain)   │   │
│  └──────────────────────────────┘   │
│                                      │
│  ┌──────────────────────────────┐   │
│  │  Handoff Trigger Layer       │   │
│  │  → SMS / webhook / ticket    │   │
│  └──────────────────────────────┘   │
└─────────────────────────────────────┘
```

---

## 3. Knowledge Layer (Scoped RAG)

**What goes in:**
- HVAC equipment manuals (uploaded by the company at setup)
- Common troubleshooting FAQs
- Maintenance schedules by unit model
- Local building codes (optional, company-provided)

**What stays out:**
- General web knowledge
- Non-HVAC topics
- Any PII not explicitly provided by the user

**Implementation:**
- `ChromaDB` or `sqlite-vec` embedded locally
- Chunked documents at setup time (one-time ingestion)
- Similarity threshold: reject if confidence < 0.65 (triggers handoff consideration)

---

## 4. Voice Input Flow

```
User speaks
    → Whisper (local, distil-whisper-small or medium)
    → Transcript displayed + editable
    → Submitted to RAG + LLM pipeline
    → Response spoken via system TTS (macOS/iOS Speech, or pyttsx3 on desktop)
```

**Constraints:**
- STT runs fully offline
- No audio stored after transcription
- Push-to-talk UI (no always-on mic)

---

## 5. Encrypted User Profile

**Schema:**
```json
{
  "customer_id": "uuid-v4",
  "name": "string",
  "unit_models": ["string"],
  "service_history": [{ "date": "ISO-8601", "type": "string", "notes": "string" }],
  "preferences": { "language": "en", "voice_enabled": true },
  "handoff_contact": { "method": "sms|email|webhook", "value": "string" }
}
```

**Encryption:**
- AES-256-GCM, key stored in OS keychain (Keychain on macOS/iOS, Credential Manager on Windows)
- Profile decrypted in-memory only; never written to disk in plaintext
- No cloud sync in MVP

---

## 6. Human Handoff Rules

Trigger escalation when ANY of these are true:

| Condition | Threshold |
|-----------|-----------|
| RAG confidence below minimum | < 0.65 |
| User frustration signals | "I don't understand", "not helpful", 2+ rephrases |
| Safety-critical keyword detected | "gas leak", "carbon monoxide", "fire", "electrical burning" |
| Explicit request | "talk to someone", "call agent", "human" |
| LLM uncertainty flagged | model returns "I'm not sure" or equivalent |

**Handoff actions (configurable by company):**
1. Send SMS to on-call technician (Twilio)
2. POST to company webhook (ticket system)
3. Display phone number + open-hours message

**Handoff message includes:** customer name, unit model, conversation summary (last 5 turns), trigger reason.

---

## 7. Modular Add-ons (Post-MVP)

| Module | Description |
|--------|-------------|
| Predictive maintenance | alert based on service history + manufacturer schedule |
| Photo diagnosis | snap photo of unit, AI identifies issue |
| Parts lookup | match symptom to part number + supplier |
| Multi-language | localized STT + TTS |

---

## 8. MVP Scope (Build vs. Defer)

**Build:**
- Voice input (Whisper local)
- Scoped RAG (ChromaDB)
- Claude API integration
- Encrypted local profile
- Handoff trigger (SMS + webhook)
- Simple chat UI (web or Electron)

**Defer:**
- Cloud sync
- Mobile app
- Photo diagnosis
- Multi-tenant admin dashboard

---

## 9. Tech Stack

| Layer | Choice | Rationale |
|-------|--------|-----------|
| LLM | Claude API (Sonnet) | Best quality, Serge has access |
| STT | Whisper (distil-small) | Local, no audio leaves device |
| RAG | ChromaDB + LangChain | Simple, local, Python-native |
| Encryption | AES-256-GCM + OS keychain | Industry standard, no custom crypto |
| UI | Electron (desktop MVP) | Cross-platform, ships as app |
| Handoff | Twilio SMS + webhook | Proven, easy to configure |

---

## 10. Success Criteria (MVP)

- [ ] Customer can ask an HVAC question via voice and get a correct answer
- [ ] System refuses to answer out-of-scope questions (returns "I don't know, let me connect you")
- [ ] Profile persists across sessions, decrypts correctly
- [ ] Handoff triggers within 2 seconds of threshold hit
- [ ] Zero PII written to disk unencrypted
- [ ] Cold start < 10 seconds on a 2020 MacBook

---

## 11. Next Steps

1. Validate spec with HVAC company stakeholder (or proxy)
2. Create BMAD story for Electron shell + RAG ingestion pipeline
3. Source 2–3 HVAC manuals for test corpus
4. Build handoff webhook receiver (mock company endpoint)
5. Use this spec as the NRC-IRAP 2-page project brief (with sections 1, 2, 6, 10)
