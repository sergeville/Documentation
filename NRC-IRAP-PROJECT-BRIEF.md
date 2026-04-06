# NRC-IRAP Project Brief
**Applicant:** Serge Villeneuve
**Date:** 2026-03-25
**Program:** NRC Industrial Research Assistance Program (IRAP)
**Project Title:** Local-First AI Assistant for HVAC Service Delivery

---

## 1. Project Summary

We are developing a packaged, local-first AI assistant that HVAC companies can deploy directly for their non-technical customers. The system answers HVAC-specific questions via voice, maintains an encrypted customer profile, and escalates to a human technician when it cannot help — all without requiring internet connectivity or customer technical knowledge.

This is a B2B product: HVAC companies license the software and configure it for their customer base. The AI is scoped strictly to HVAC knowledge provided by the company (manuals, FAQs, maintenance schedules), ensuring safe and accurate responses.

**Innovation:** Combining local RAG (retrieval-augmented generation), offline voice transcription, and rule-bound escalation in a single deployable package for non-technical end users — a capability gap that currently has no commercial equivalent for trades industries.

---

## 2. Technical Approach

The system runs entirely on the customer's device (desktop or tablet):

- **Voice Input:** OpenAI Whisper (local, distil-small variant) transcribes speech without sending audio to any server
- **Knowledge Layer:** ChromaDB vector store, pre-loaded with company-provided HVAC documents at setup. Similarity threshold (0.65) gates what the AI can answer
- **LLM:** Claude API (Anthropic Sonnet) as the reasoning layer, constrained by the scoped knowledge base
- **Encrypted Profile:** Customer equipment history, preferences, and contact info stored with AES-256-GCM encryption; key held in OS keychain — never written to disk in plaintext
- **Human Handoff:** Rule-based escalation triggers (safety keywords, confidence threshold, explicit request, frustration signals) that route to SMS/webhook/ticket within 2 seconds

No audio is retained. No PII leaves the device. No cloud sync in MVP.

---

## 3. Market Opportunity

HVAC service is a $140B+ industry in North America. The customer service bottleneck — technicians fielding basic questions by phone — is a known cost center. Existing AI chatbot solutions require cloud connectivity, are not scoped to domain knowledge, and are not designed for non-technical users.

**Primary customers:** Independent HVAC companies (1–50 technicians), who cannot afford enterprise AI solutions but need to reduce inbound support volume and improve customer self-service.

**Revenue model:** Annual SaaS license per company, tiered by number of customer deployments.

---

## 4. Escalation & Safety Design

Safety is a first-class requirement. The system escalates immediately on detection of:

| Trigger | Example |
|---------|---------|
| Safety-critical keyword | "gas leak", "carbon monoxide", "burning smell" |
| Low confidence RAG | Score < 0.65 — system doesn't guess |
| User frustration signals | Repeated rephrasing, "not helpful" |
| Explicit human request | "talk to someone", "call agent" |

Handoff delivers: customer name, unit model, last 5 conversation turns, trigger reason — to on-call technician via SMS or company ticket system.

---

## 5. R&D Activities Requiring IRAP Support

| Activity | Description |
|----------|-------------|
| Domain-scoped RAG tuning | Optimize chunking, embedding, and threshold for HVAC technical documents |
| Offline STT integration | Validate Whisper variants for accuracy on HVAC terminology and accented speech |
| Handoff protocol design | Define and test escalation rules across edge cases (conflicting signals, no-answer loops) |
| Encryption + keychain integration | Cross-platform (macOS, Windows) secure profile storage without user-facing complexity |
| Field validation | Deploy pilot with 1–2 HVAC companies, measure self-service resolution rate vs. baseline |

---

## 6. Expected Outcomes (12 months)

- Functional MVP deployable to 2–3 pilot HVAC companies
- Validated self-service resolution rate > 60% for common HVAC questions
- Zero data breach incidents (privacy-by-design architecture)
- NRC-IRAP technical report documenting RAG scoping and escalation design patterns
- Foundation for Phase 2: mobile app + predictive maintenance module

---

*Full technical specification:* `~/Documents/Documentation/HVAC-AI-ASSISTANT-MVP-SPEC.md`
*Contact for ITA meeting:* https://nrc.canada.ca/en/support-technology-innovation/nrc-irap/contact-irap
