---
name: work-board-2026-09-12
description: "Kai's 2026-09-12 cross-project brain-dump digested into 8 threads (OVH ops, Agent Bob, Agent Wolf, camping cut + listen tools, GPOM stills with variety, MMT footage, GPOM narration, parked Ableton/Serum ideas)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 23bf9342-5511-4372-aced-48bed7291a7c
  modified: 2026-09-12T09:00:40.015Z
---

On 2026-09-12 Kai brain-dumped the season's work across three repos; the digest lives at
`design/2026-09-12-work-board.md` in the badcode repo (uncommitted at time of writing).

Threads: (1) OVH box + move everything off Kubernetes except NoCode and Franchise Cloud
(shut down week of 2026-09-14) — source `../agent-bob/docs/ops.md`; (2) Agent Bob: resume paused
onboarding fleet, then first real workflows for Emperor's New Coin (with Richard, from WhatsApps),
BadCode government, BadCode marketing manager — the user must see the architect's decisions and
its reaction to events quickly; (3) Agent Wolf live so friends can log in; (4) camping music-video
cut, using it to test listen-mcp / music-session against Jack's guidance (he named a reference
band — not in repo); (5) GPOM storyboard stills proposed as a SPREAD of different ideas per beat,
then honed like the Suno loop; (6) MMT stock-footage research for the war + NHS; (7) GPOM
narration track; (8) parked: Ableton/Serum via computer use, extract newsreader voice from Suno.

Ruled the same day: the muted palette sameness is caused by the skills themselves
(badcode-art-direction rule 1 "not a stylistic option"), so variety mode must let one candidate
break the register on purpose. Shortcut for now: music AND narration come out of Suno.

**Why:** Kai explicitly wants coordination across projects in one place, and images are free so
storyboarding hard up front is the strategy.
**How to apply:** open the board first when Kai says "where were we"; see [[claude-can-hear-initiative]],
[[camping-duet-recut]], [[still-approval-gate]], [[agent-orange-initiative]].

**Orchestration protocol that worked (2026-09-12 afternoon):** one planning session named `orchestrator`; each thread launched from `design/2026-09-12-threads/LAUNCH.md` + a two-digit number; threads write `status/<NN>.md` (line 3 = a `NOW:` one-liner on request); the orchestrator runs two Monitors (status files every 45 s, commits every 60 s), relays between threads with SendMessage, never does thread work, and hands Kai ONE next action at a time ranked: deadline → unblocks other threads → cheapest yes that frees free work → credit spends → housekeeping. Sessions cannot be renamed by another session; Kai renames them (`ovh-servers`, `t02-bob-onboarding`, `t03-bob-first-projects`, `t04-wolf-live`, `t05-camping`, `t06-gpom-stills`, `t07-mmt-footage`, `t08-gpom-narration`). Kai said the NOW-line table was "invaluable".
