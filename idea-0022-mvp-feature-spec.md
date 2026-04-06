# idea-0022 — Manufacturing Voice MVP: Feature Spec
*Version: 0.1 — 2026-03-28*

---

## 1. Command Vocabulary

Push-to-activate model. Worker holds button, speaks command, releases. System responds with short audio confirmation. Commands are discrete intents — no chained sentences.

### Production Logging

| Command | Canonical Phrase | Variants | Action | Audio Response |
|---|---|---|---|---|
| Log unit | "Log unit" | "Unit done", "Count one" | Increment unit counter for current station/task | "Unit logged. [N] total." |
| Log batch | "Log batch [N]" | "Batch of [N]" | Increment unit counter by N | "Batch logged. [N] total." |
| Undo last log | "Undo" | "Cancel last" | Decrement last logged count, mark corrected | "Undone." |
| Start timer | "Start task" | "Begin task" | Timestamp task start for cycle time tracking | "Timer started." |
| End timer | "End task" | "Task complete" | Timestamp task end, write cycle time to local log | "Task closed." |

### Quality Control

| Command | Canonical Phrase | Variants | Action | Audio Response |
|---|---|---|---|---|
| Flag defect | "Flag defect" | "Defect", "Bad unit" | Open defect entry; log station, timestamp, worker ID | "Defect flagged." |
| Log defect type | "Defect: [type]" | "Scratch", "Misalign", "Leak" | Attach defect category to last open entry | "Type recorded." |
| Pass inspection | "Pass" | "Good unit", "Clear" | Mark unit as inspected-pass in QC log | "Passed." |
| Hold unit | "Hold" | "Quarantine", "Set aside" | Mark unit as hold-pending-review in QC log | "Unit on hold." |

### Communication

| Command | Canonical Phrase | Variants | Action | Audio Response |
|---|---|---|---|---|
| Call supervisor | "Call supervisor" | "Get supervisor", "Need help" | Push alert to supervisor dashboard: worker ID, station, timestamp | "Supervisor alerted." |
| Request material | "Need material" | "Request supplies" | Push material request: station, worker ID, current task | "Request sent." |
| Report hazard | "Safety issue" | "Hazard", "Report hazard" | Push HIGH-priority alert to supervisor; logged separately | "Safety alert sent." |

### Navigation / Status

| Command | Canonical Phrase | Variants | Action | Audio Response |
|---|---|---|---|---|
| Next task | "Next task" | "What's next" | Pull next assignment from local task queue | "Next: [task name]." |
| Read status | "Status" | "Where am I", "My count" | Read back: current task, unit count, time on station | "[Task]. [N] units. [T] minutes." |

**Total: 14 commands.** All commands are single-intent. The system never requires a follow-up question to complete an action — if a field is missing (e.g., defect type), the action logs what it has and prompts once: "Defect type?"

---

## 2. Activation Model

| Approach | Pros | Cons | Verdict |
|---|---|---|---|
| Push-to-activate (PTT button) | OSHA-compliant, zero false positives, worker-controlled, no background noise ingestion, low compute cost | Requires one hand free for 1-2 seconds | **Recommended for v1** |
| Wake word (always-on) | Fully hands-free | False positives in noisy environments, surveillance perception risk, NLRB concern, higher compute load, worker trust issues | Defer to v3+ |
| Tap-on-wearable trigger | Hands-free, glove-compatible | Requires wearable hardware, higher BOM cost | Consider for v2 wearable variant |

**Recommendation: Push-to-activate via a physical button on a chest-mounted device or clip-on badge.**

OSHA compliance note: passive always-on listening in a workplace environment raises two risks — (1) distraction in high-noise/high-hazard zones, and (2) worker monitoring concerns under NLRB interpretations. Push-to-activate sidesteps both. It is also the pattern workers intuitively trust because they control when the microphone opens. Document this design choice in all customer-facing materials and the design partner agreement.

---

## 3. Tech Stack Recommendation

### Speech-to-Text Engine

| Option | Latency | Cost | Privacy | Noise Accuracy | Verdict |
|---|---|---|---|---|---|
| Whisper.cpp (local, small/medium model) | 200–600ms on modest hardware | Free (compute only) | Full — audio never leaves site | Good with fine-tuning; weaker on factory vocabulary out of the box | **Recommended** |
| Azure Cognitive Speech | 150–300ms | ~$1/hr streaming | Cloud-dependent; data leaves premises | Excellent general accuracy; supports custom acoustic models | Acceptable cloud fallback |
| Deepgram Nova | 100–200ms | ~$0.008/min | Cloud-dependent | Strong in noise; custom vocabulary support | Best cloud option if privacy waived |

Local Whisper (small model, whisper.cpp) is the default. It runs on a $300 edge server (Raspberry Pi 5 or NUC-class device). For pilot deployments where on-prem hardware procurement is a blocker, Azure Speech with a custom vocabulary model is the cloud fallback. Latency target: under 400ms end-to-end from button release to audio confirmation.

**Fine-tuning note:** Feed the system 50–100 examples of each command spoken by real workers in factory conditions before pilot day 1. This is the single highest-leverage quality action.

### Platform

| Platform | Ruggedization | Battery | Cost (per worker) | Integration | Verdict |
|---|---|---|---|---|---|
| Ruggedized Android wearable (Zebra WT6300, Honeywell CW45) | IP65+, drop-rated | 8–12h shift | $600–$1,200 | Android SDK; BT headset pairing | **Best for production** |
| iPhone in chest mount | Consumer-grade | 8–10h (with case battery) | ~$500 + mount | iOS SDK | Acceptable for pilot |
| Edge server + BT headset (no screen device) | Server in control room; BT headset on worker | N/A (plugged) + headset 8h | $300 server + $80 headset | Any platform | **Recommended for v1 pilot** |

**For the v1 pilot: edge server (NUC or Pi5) in the control room + Bluetooth headset per worker.** This avoids per-worker device procurement, gives full control over the speech engine, and keeps BOM low enough to self-fund a 5-worker pilot. Workers already accept headsets in many factory environments.

### Integration Point

For v1: **standalone app, local log only.** The system writes a structured JSON/CSV log to disk (unit counts, defect entries, supervisor alerts, timestamps). The ops manager pulls the file at end of shift. This eliminates ERP integration complexity from the critical path.

ERP write-back (SAP, NetSuite, Fishbowl) is a v2 deliverable. Designing the local log schema to mirror the ERP's data model from day one reduces the v2 migration cost.

---

## 4. MVP Scope Boundary

| IN scope for v1 | OUT of scope for v1 |
|---|---|
| 14-command vocabulary (4 categories) | ERP / WMS write-back |
| Push-to-activate via PTT button | Custom wake words |
| Local Whisper inference on edge server | Multi-language support |
| Audio confirmation for every command | Mobile app (iOS or Android) |
| Worker ID + station binding at session start | Voice biometric worker authentication |
| Supervisor alert push (local network, dashboard) | Multi-site deployment |
| Local JSON/CSV log with per-shift export | Real-time analytics / reporting UI |
| "Didn't catch that" retry prompt (1 retry, then log failure) | Cloud sync or remote data access |
| Pilot onboarding script (30-min worker training) | Integration with existing badge/RFID systems |
| Session start/end (worker logs in by station) | Custom vocabulary per customer in v1 |

---

## 5. Build Estimate

| Component | Scope | Size | Notes |
|---|---|---|---|
| Speech engine integration | Whisper.cpp on edge server, audio pipeline, PTT trigger | M | 1–2 weeks. whisper.cpp is well-documented; main work is audio capture + latency tuning |
| Command parser / intent engine | Map transcription → intent, handle variants, error path | S | 3–5 days. Rule-based matching on a 14-command set; no ML needed at this scale |
| Audio feedback layer | Text-to-speech responses, pre-recorded fallbacks | S | 2–3 days. Use pre-recorded WAV files for all 14 confirmation phrases — eliminates TTS latency |
| Local log + export | JSON schema, per-shift CSV export, file rotation | S | 2–3 days |
| Supervisor alert push | Local network HTTP push to supervisor dashboard | S | 2–3 days. Simple Flask endpoint + polling dashboard |
| Hardware procurement + setup | Edge server, BT headsets, PTT buttons, mounting | M | 1–2 weeks elapsed (ordering lead time). Setup < 1 day |
| Pilot deployment + worker onboarding | On-site setup, 30-min training per worker, day-1 support | M | 1 week on-site (travel + deployment). Write onboarding script in parallel |

**Total build time (parallel): 4–6 weeks to pilot-ready.**
Critical path is hardware procurement. Order before code is done.

---

*Feed this document directly into the MVP sprint planning session. Each table row is a backlog item.*
