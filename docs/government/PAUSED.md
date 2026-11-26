# The BadCode government: paused (26 Nov 2026)

**Kai, 26 Nov 2026:** "I think we've overcomplicated this... I want to stop spending tokens on this, and I
want to completely reconsider this." Everything that ran by itself is switched off. Nothing is deleted.
GOVT on badcode.tv is now just Future Proof: the three questions. This file is the record: what we built,
why, how it ran, what it cost, what we learned, and how to bring any of it back.

## What the government was for

To show Future Proof working: a government built on its three tenets, run in the open.

1. **Choose issue by issue** (why can I only vote red or blue?).
2. **Change it small, keep the undo** (why is it only once every five years?).
3. **No policy without its test** (why don't we ask the experts?).

The canon is [`docs/stories/gitpush-origin-master/future-proof.md`](../stories/gitpush-origin-master/future-proof.md).
Why the government was built the way it was: [`future-proof-government.md`](./future-proof-government.md).

## What we built: three experiments in three weeks

### 1. The AI cabinet (5 to 11 Nov, ran until 26 Nov)

- **What:** one Opus agent played ten ministers. Every morning it read the news and rewrote a manifesto
  of 55 policy files. An opposition on another AI model (Codex) attacked each change. A statistician
  agent refused anything that couldn't be measured, and set dated predictions about the real UK.
- **Daily, in Bob:**
  - 05:00 news sweep (24 researchers);
  - 06:00 cabinet;
  - 07:30 opposition;
  - 08:00 statistician;
  - Sundays 20:00 the cabinet secretary rewrote the ministers' briefs.
- **On the site:** GOVT 1 to 5 (the manifesto, Live, The floor, The record, Replay), a page per minister
  and per policy, and a scoreboard.
- **Where it is:**
  - this folder: `ministers/`, `manifesto/`, `policies/`, `debates/`, `statements/`, `workers/`,
    `workflows/`, `shared.md`;
  - design: [`design/2026-11-05-badcode-government.md`](../../design/2026-11-05-badcode-government.md),
    [`design/2026-11-11-future-proof-government/`](../../design/2026-11-11-future-proof-government/README.md).
- **Left open:** PR #29 (`government/rolling`, "Government: since 2026-11-12").
  - It holds 49 commits, 66 files and 81 comments of cabinet work from 12 to 26 Nov.
  - It was never merged, so the live policy pages stayed at their 12 Nov state.
  - PR #22 (cut the news sweep to save tokens) is also open, untouched since 11 Nov.
- **Why it stopped working (23 Nov review):**
  - The debate looped on three policies, and 47 of 56 were never challenged.
  - "A cabinet arguing with an opposition is still Westminster with better policies."
  - [`design/2026-11-23-future-proof-rework/adversarial-review-2026-11-23.md`](../../design/2026-11-23-future-proof-rework/adversarial-review-2026-11-23.md)

### 2. Future Proof Live, SIMULATED (23 Nov, ran until 26 Nov)

- **What:** one real news issue a day, run through seven AI stations:
  - a clerk picks the issue;
  - 100 simulated citizens, drawn by lot, set the tests;
  - three rival answers are written blind (one on Codex);
  - a gate marks every answer against every test;
  - 12 simulated jurors vote;
  - a minister signs a small trial with dated predictions.
- **Results:**
  - 17 issues: 9 to 22 Nov backfilled, then 23, 25 and 26 Nov live.
  - The 24 Nov issue (money lessons in maths) stopped at the bench stage and was never published.
  - It was public at `/future-proof/live/` from 23 Nov.
- **Where it is:**
  - the data: branch `simulation/live`;
  - the code: [`simulation/`](./simulation/README.md) and `scripts/government/sim/`;
  - the design, goals and full build log: [`design/2026-11-23-future-proof-rework/`](../../design/2026-11-23-future-proof-rework/README.md);
  - a copy of the private mirror page: `private-mirror/` in that folder;
  - the explainer: https://claude.ai/artifact/8JJXdfsxM8PBzCBH3iWCQo;
  - the private mirror: https://claude.ai/artifact/GArjgzYRpi2Hc7C2ZjTi7V.
- **Kai, 26 Nov:** "it's just pages of text that nobody's going to look at."

### 3. The Future Proof Demo (24 Nov, ran until 25 Nov)

- **What:** made-up towns hung on real news, with each day's ending chosen in advance (accepted, partly
  or rejected). Seven demo ministers grew manifestos only from adopted days.
- **Results:** 16 days and 11 manifesto lines. It was public at `/demo/`.
- **Where it is:**
  - the data: branch `demo/live`;
  - the code: `docs/demo/` and `scripts/demo/`;
  - the design: [`design/2026-11-24-future-proof-demo/`](../../design/2026-11-24-future-proof-demo/GOAL-3.md).

## What it cost

Bob doesn't count tokens, so these are estimates from the build logs.

| Experiment | Per day | Models |
| --- | --- | --- |
| The AI cabinet | about 1.5M to 2M tokens (a guess) | Opus, Codex |
| Future Proof Live | about 330k to 430k tokens (measured from subagents) | Sonnet, Haiku, Codex |
| The Demo | about 100k tokens (from the backfill; daily not measured) | Sonnet, Haiku, Codex |

All three together came to roughly 2M to 2.5M tokens a day, for output that Kai and Jack had no time to
read.

## What we learned

- **Showing beats simulating.** The three questions page made the point in seconds. Every layer of
  simulation added text and cost, and took away clarity.
- **Nobody reads a machine's daily output, including us.** The rolling PR went two weeks unread. A loop
  that needs humans to review it each day fails quietly when they're busy.
- **Imitating the process brings back the thing we're criticising.** The cabinet and opposition
  re-created Westminster. The simulation's stations re-created bureaucracy.
- **The honesty rules worked:** the SIMULATED stamps, no safe bets, misses printed, and humans holding
  the pen. Keep them for whatever comes next.
- **The automation was reliable.** Every scheduled run reported "ok". The one failure (24 Nov) was a
  stage that didn't hand on. The problem was never whether it ran. It was whether it was worth running.

## What changed on 26 Nov (the pause)

- **Bob:** all 22 schedules are disabled: 5 for the cabinet, 7 for the simulation, 10 for the demo.
  - `docs/government/schedules.json` and `docs/demo/schedules.json` now say `"enabled": false`, so the
    next `bob-sync` doesn't switch them back on.
  - The workers still exist in Bob, unused.
- **claude.ai:** the cloud task "Future Proof simulation: clock and page (daily)"
  (`trig_012kXE2KMjrHYuber7bJBmev`) is disabled.
- **GitHub:** `site-deploy`'s three daily rebuilds are commented out. A push to main still deploys.
- **badcode.tv:**
  - **GOVT** is Future Proof: the three questions, which used to be NEWS 1.
  - **NEWS** is the shorts. Until the first short is in `apps/site/src/content.json` under `news.shorts`,
    the TV has two channels (Kai, 26 Nov): the NEWS button is gone and NEWS addresses open GOVT. Adding
    the first short (`{title, line, youtube}`) brings NEWS back by itself.
  - **The Storyverse** moved back to STORIES 9.
  - The minister, policy and scoreboard pages, GOVT 2 to 5, `/future-proof/live/` and `/demo/` are no
    longer built.
  - Old government addresses open Future Proof.
  - Setting `PAUSED = false` in `apps/site/build.mjs` brings the pages back exactly as they were (the TV
    routing in `tv.js` would need its GOVT tabs restored too).
- **Archive tags,** so nothing is lost even if a branch is deleted:
  - `archive/government-rolling-2026-11-26` (PR #29's work);
  - `archive/simulation-live-2026-11-26`;
  - `archive/demo-live-2026-11-26`.

## To bring something back

1. Set `"enabled": true` on the schedules you want, in `schedules.json`, and merge. `bob-sync` turns
   them on in Bob. A schedule turned back on never runs what it missed.
2. For the simulation's marking, re-enable the cloud task at
   https://claude.ai/code/routines/trig_012kXE2KMjrHYuber7bJBmev.
3. For the pages, set `PAUSED = false` in `apps/site/build.mjs`, and uncomment the schedule in
   `.github/workflows/site-deploy.yml` if the data changes daily.

## What next

The rethink starts from one question: what is the simplest thing that makes people see that government
could work differently? The ideas for it are in
[`design/2026-11-26-government-rethink/`](../../design/2026-11-26-government-rethink/).
