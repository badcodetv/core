---
name: marketing-initiative
description: Continuous-release marketing plan + Agent Orange worker-fleet manifestation; docs/marketing/ is the source of truth
metadata: 
  node_type: memory
  type: project
  originSessionId: ad243c81-baec-4292-8ae6-d2249dc3f213
---

Decided 2026-07-16 (Kai + Jack): stop album-drop thinking, **release continuously** and
automate marketing. Camping (comic + song + Jack's music video, all ~finished) is campaign #1;
its moral core for the funnel: don't judge the homeless — homelessness as wealth-gap symptom.

Source of truth: `docs/marketing/` — `README.md` (strategy portfolio: funnel, slice,
serialization, narrator-in-residence, making-of, music-first, engagement, owned-channel,
collab, evergreen-search; cadence calendar; metric hierarchy = badcode.tv funnel clicks >
followers > engagement > views), `agent-orange.md` (worker fleet + schedules + requirements
back to Agent Orange), `marketing-manager-prompt.md` (the seed system prompt — the ONLY
hand-created worker; idempotent daily reconcile + weekly self-critique), `badcode-image.md`
(worker Docker image spec), `platform-playbooks.md` (deep-research-grounded growth mechanics).

**Why:** they were over-engineering and under-releasing; social algorithms reward cadence.

**How to apply:** marketing work goes through `docs/marketing/`; the marketing-manager prompt
is a seed — once live in Agent Orange, the system owns it (don't hand-sync). Key decisions:
stage-1 autonomy = every public post human-approved via the core `request_human_attention`
tool (spec P6 — staged autonomy is purely a prompt edit, NO approval queues/UI built);
Agent Orange worker layer is spec-only (`agent-orange/docs/17-product-spec.md`) — gaps we
require: `request_human_attention` implementation, worker_create/update/delete + schedule
MCP tools. Flow/Suno generation stays human-attended. Related: [[agent-orange-initiative]],
[[team-kai-and-jack]], [[camping-karen-rework-initiative]].
