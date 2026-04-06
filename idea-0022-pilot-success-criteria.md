# idea-0022 — Pilot Success Criteria
*Version: 0.1 — 2026-03-28*

---

## Pilot Structure

| Parameter | Value | Rationale |
|---|---|---|
| Duration | 4 weeks active use + 1 week setup/onboarding | 4 weeks is long enough to observe adoption decay or growth; short enough to hold a busy ops manager's attention |
| Workers | 5–10 floor workers at one station or line | Small enough to manage personally; large enough to get statistically meaningful usage data |
| Data collection | Automated (local log) + weekly 30-min check-in call | Ops data is captured silently; qualitative signal comes from the human conversation |
| Check-in cadence | End of week 1, 2, 3, 4 | Week 1 = friction report; week 2 = habit formation check; week 3 = value confirmation; week 4 = go/no-go data |
| Baseline requirement | 2 weeks of pre-pilot manual log data from the same station | Cannot measure time saved without a baseline. Make this a condition of starting. |

---

## Quantitative Metrics

### Primary (must have at week 4)

| Metric | Baseline method | Target (pilot worked) | Concern threshold |
|---|---|---|---|
| Time per log event | Observe or estimate from pre-pilot manual entry (avg seconds to walk to terminal or pick up scanner) | 40%+ reduction in time-to-log vs. baseline | Less than 20% reduction |
| Command accuracy rate | % of spoken commands correctly interpreted (from local error log) | >= 90% accuracy by end of week 2 | Below 80% at any week |
| Worker adoption rate, week 1 | % of eligible workers who used the system at least once in week 1 | >= 70% | Below 50% |
| Worker adoption rate, week 4 | % of eligible workers still using the system in week 4 | >= 60% (some drop-off expected; retention > acquisition matters) | Below 40% — indicates the system didn't stick |
| Defect log completeness | # defect entries per shift vs. pre-pilot estimate | Same or higher count (voice should remove the friction that causes underreporting) | Fewer defect entries than baseline — suggests workers stopped using QC commands |

### Secondary (good to have)

| Metric | What it tells you |
|---|---|
| Supervisor alert response time | If supervisors are responding faster, the alert push is working and creating floor value |
| Session start rate | % of shifts where a worker actually activates the system at shift start — proxy for habit adoption |
| Retry rate ("didn't catch that") | High retry rate signals vocabulary mismatch or audio environment problems; feeds fine-tuning backlog |
| Commands per shift per worker | Tracks engagement depth — are workers using 2 commands or 10? |

---

## Qualitative Signals

### Green signals (pilot is working)

- A worker uses the system on a day you're not watching (unprompted use)
- A worker explains the system to a new coworker without being asked
- The ops manager mentions the pilot in a meeting you weren't in
- Workers start suggesting new commands they want ("can it do X?")
- Ops manager asks "what would it take to roll this out to the other line?"

### Red signals (pilot is failing)

- Workers stop using the system after day 3 and revert to manual entry
- The ops manager stops joining weekly check-in calls
- Workers describe the system as "extra work" rather than time saved
- You hear "it doesn't understand us" more than twice in week 1
- No defect entries logged via voice after week 1

---

## Failure Signals — Hard Stops

These indicate a fundamental problem that cannot be fixed by iteration within the pilot:

| Signal | Interpretation | Action |
|---|---|---|
| Command accuracy below 70% at end of week 2 | Audio environment or vocabulary mismatch is too severe for the current engine | Stop pilot. Invest in fine-tuning before restarting. |
| Zero adoption after week 1 (0 workers using system) | Onboarding failed, or value proposition is not landing on the floor | Pause pilot. Conduct worker interviews before week 2. |
| Ops manager withdraws participation | Design partner relationship has broken down | Exit gracefully. Ask for a 30-min debrief call. Do not re-pitch. |

---

## Go / No-Go Decision Framework

At end of week 4, score the pilot against these criteria:

| Criterion | Weight | Go signal | No-go signal |
|---|---|---|---|
| Command accuracy >= 90% | High | Yes | Below 85% at week 4 |
| Week 4 adoption >= 60% | High | Yes | Below 40% |
| Ops manager can name one measurable change | High | Yes — this is the design partner success condition | "I can't point to anything specific" |
| At least one green qualitative signal observed | Medium | Yes | None observed |
| Time-to-log reduction >= 40% | Medium | Yes | Below 20% |
| Worker NPS (informal: "would you keep using this?") | Medium | 60%+ say yes | Below 40% |

**Go = 4 or more criteria met, including all 3 High-weight criteria.**
**Conditional go = 3 criteria met, at least 2 High-weight. Ship with known gaps documented.**
**No-go = fewer than 3 criteria met, or any Hard Stop signal triggered.**

### If Go
- Lock the design partner into a paid agreement (even $1/user/month — establishes commercial relationship)
- Use week 4 data as the case study for the next 5 outreach targets
- Begin v2 scoping: ERP write-back + second customer vertical

### If No-Go
- Conduct a structured debrief with the ops manager and 2–3 workers
- Identify whether the failure is: (a) speech accuracy, (b) command vocabulary mismatch, (c) workflow integration gap, (d) onboarding/training failure
- Each failure mode has a different fix. Do not pivot the whole product — fix the specific layer.

---

## Design Partner Agreement — Minimum Terms

Before week 1 begins, the ops manager signs a one-page agreement covering:

1. Duration and scope (4 weeks, N workers, one station/line)
2. Data use: anonymized workflow data may be used for product improvement
3. Feedback commitment: 4 weekly 30-min check-in calls
4. Success condition: ops manager will identify one measurable change at close, or report "no measurable change" — both outcomes are valid
5. No commercial obligation — this is a free pilot

The agreement is a filter. If an ops manager won't sign a one-pager, they are not a serious design partner.
