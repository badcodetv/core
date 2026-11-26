# Goal 2: two weeks of Future Proof, public on badcode.tv

Kai, 23 Nov 2026, evening. This replaces `GOAL.md` (goal 1, where items 1 to 5 are done and PR #30 is
merged). Work autonomously. Read `build-log.md` in this folder first: it holds every decision so far
(D1 to D7), the measured costs and the IDs.

## What Kai wants now

1. **Backfill two full weeks.** One replayed issue for every day from 9 Nov to 22 Nov 2026, as fast as
   possible. Seven exist already: 10 Nov, and 17 to 22 Nov. Missing: **9, 11, 12, 13, 14, 15 and 16 Nov**.
2. **Put it on the live website,** badcode.tv, so people see two weeks of decisions at once: "a truly
   future-proof network effect".
   - **This reverses an earlier decision.** Goal 1 kept the simulation private for its first two weeks.
     Kai now wants it public.
   - The private artifact page can stay as a mirror.
3. **Keep it running itself every day after that,** including the site.
4. **Finish goal 1's leftover:** verify the live run.
   - Tonight's manual run for 23 Nov started with the `sim-clerk` chat `d84b5673-4d15-45f6-b5a2-a04758967547`
     (issue: the EDITH AI breast-screening trial). Carry it on through citizens, rival, bench, gate, jury
     and minister, using `chat_create` on each worker with its schedule message.
   - Then confirm the first fully scheduled day, 24 Nov: Bob from 09:00 London time, then the routine at
     13:00 UTC.

## Done means

1. Fourteen valid published issues (9 to 22 Nov) plus the live days are on `simulation/live`.
   - Every replay is stamped `Replayed on <run date> from the news of <news date>`.
   - Every prediction falls due after its run date.
2. **badcode.tv shows the simulation:**
   - a feed, newest first;
   - each issue with its loop animation and its full record;
   - the scoreboard.
   - It's built from `simulation/live` at deploy time, and it reaches the site with no human step after
     each daily run. One option: the 13:00 routine triggers `site-deploy` (`workflow_dispatch`). Another:
     the site build fetches the branch. Choose one and write down why.
3. Before the first public deploy, the `marketing-gatekeeper` subagent has checked the public page and
   copy against the reader rules, the AI-disclosure rules and the legal lines on real people and
   companies. Its FAILs are fixed.
4. The 23 Nov manual live run, and the 24 Nov scheduled one, are each verified as published.
5. `build-log.md` is up to date, and ends with a short report:
   - what runs when;
   - the cost of one day;
   - what failed;
   - how to go from one issue a day to five.

## Hard rules (still binding, and stricter now that it's public)

- Every card, page, image and social preview says **SIMULATED**.
- Simulated citizens are never "the public". A real poll sits beside them where one exists.
- No claim about a real person or company without a published source. Never put words in a real
  person's mouth.
- No hindsight scoring.
- Never edit `docs/government/policies/` (the manifesto).
- Never touch PRs #29 or #22.
- The site follows `docs/using-ai.md` and `docs/marketing/the-reader.md`.
- No social posts or YouTube. The website is the only public surface.

## How to go fast (what worked on 23 Nov)

- **Replay kit:** `design/2026-11-23-future-proof-rework/replay-kit/`, holding `orchestrate.md`,
  `packet.py` and `join_bench.py`. Set run_date to the actual date you run on; the kit says 2026-11-23.
- **Clerks first, in parallel,** one per day, each given a topic chosen up front so no field repeats:
  - Read each day's `kind=news-digest` memory in Bob.
  - Pick distinct values-laden UK items.
  - Avoid fields already used: water, energy, migration, youth-jobs, policing, eu-trade, high-street-jobs,
    and nhs-ai for 23 Nov.
- **Then citizens (Haiku), one subagent per day.**
- **Then one Sonnet orchestrator per day** running `orchestrate.md` steps A to F:
  - C goes to Codex through a Bob plain chat;
  - A and B come from two blind nested subagents;
  - then gate, jury, minister.
  - About 330k to 430k tokens a day.
- **Then:**
  1. review every file by hand against the hard rules;
  2. validate;
  3. push to `simulation/live`;
  4. rebuild the feed;
  5. republish https://claude.ai/artifact/GArjgzYRpi2Hc7C2ZjTi7V (read it and `feed.json` first).
- **Site code:** `apps/site/` (see `manifesto.mjs` and `debates.mjs` for how government data is read at
  build time). The page to port is `docs/government/simulation/page/index.html`. `site-deploy.yml` deploys
  on pushes to main that touch `apps/site/**`, the manifesto, the policies or the debates, or on manual
  dispatch.
- **The daily routine:** `trig_012kXE2KMjrHYuber7bJBmev`, following `docs/government/simulation/routine.md`.

## Merging

Kai merged PR #30 by asking for it on 23 Nov ("please merge and deploy everything we have"). For this
goal, open one PR for the site work.

- Merge it yourself only if Kai has confirmed that in this goal's message.
- Otherwise stop and ask, and say exactly what the merge makes public.

## Stop and ask Kai only if

- a hard rule can't be met;
- the gatekeeper FAILs something you can't fix;
- a merge needs his yes;
- a day costs over three times today's government run.
