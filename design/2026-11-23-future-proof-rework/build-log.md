# Build log: Future Proof simulation

Goal: [`GOAL.md`](./GOAL.md). Branch: `future-proof/simulation`. Newest entry first under **Log**.

## Decisions

- **D1. Bob can't publish a private page.** On 23 Nov a plain Bob chat (Sonnet) reported no Artifact
  tool and no `claude` CLI.
  - Bob's own file viewer is private behind Bob's sign-in, but it is sandboxed with no JavaScript, so
    it can't run the loop animation.
  - So: a claude.ai cloud **routine** republishes the private artifact each day, if routines have the
    Artifact tool. A one-off probe routine checks this (`trig_01HGvNtmvTooXfhXmjXJC7n7`).
- **D2. The repo is public** (`badcodetv/core`, `isPrivate: false`). The simulation's data files are
  readable on GitHub like the rest of the government's work. "Private" means the page: a private
  claude.ai artifact, never linked from badcode.tv.
- **D3. Daily data goes on its own branch, `simulation/live`.** Bob workers push there directly, with no
  PR and no merge, as Kai decided.
  - main gets no daily bot commits.
  - The site doesn't redeploy.
  - Code, schema and worker prompts live on main, arrive through the one PR, and sync to Bob on merge.

- **D8. badcode.tv reads the data branch at build time, on a schedule** (goal 2, 23 Nov). `site-deploy`
  fetches `simulation/live`, and `apps/site/simulation.mjs` reads the issue files straight from git
  (`git ls-tree` and `git show`), builds the feed and writes `/future-proof/live/` (the page from main,
  wrapped with a SIMULATED title, description and preview picture) and its `feed.json`.
  - **Trigger:** two daily cron runs, 12:15 UTC (after the minister) and 14:30 UTC (after the 13:00
    clock), plus pushes to main that touch the page or the sim code, plus manual dispatch.
  - **Why not have the routine dispatch the deploy:** that needs a GitHub token that can start
    workflows in the cloud routine or in Bob. The schedule needs none, still works if the routine
    fails, and costs about a minute of Actions per run. The price is up to an hour's lag after a run.
  - The private artifact page stays as a mirror, republished by the routine as before.

- 23 Nov: branch created; Bob capability probe done (D1); repo visibility checked (D2); cloud probe routine scheduled for 17:58 UTC; distributions researcher started.
- 23 Nov: **D4. Cloud routines can publish.** A one-off probe routine had `Artifact`, `ArtifactComments` and `ArtifactData`, listed artifacts, and cloned `badcodetv/core`. So the private page is a claude.ai artifact, republished by a daily routine. A Bob file-viewer page would be private too, but it can't run JavaScript.
- 23 Nov: built `scripts/government/sim/` (`issue.mjs` schema and validator, `lot.mjs` draw by lot, `feed.mjs`, `sim.mjs` command line, `make-pool.mjs`, `bob-setup.sh`), with 17 tests passing. Pool: 1,000 people from `distributions.json` (ONS mid-2025, Census 2021 E&W, Commons Library 2024 results).
- 23 Nov: seven worker prompts (`docs/government/workers/sim-*.md`) and `docs/government/simulation/{README.md, worker-common.md}`. `sync-bob.mjs` now takes `include: simulation`, and `bob-sync.yml` watches `worker-common.md`.
- 23 Nov: **D5. Thames Water's news date is 10 Nov, not inside 16–22 Nov.** The fact-checker found no dated Thames rescue story from 12 to 17 Nov; the latest is Smart Water Magazine on 10 Nov. The seven replayed days are therefore 10 Nov (Thames) and 17–22 Nov.
- 23 Nov: **D6. The backfill's topics were assigned up front,** so six clerks could run in parallel without picking the same topic. Each is a real weight-2 or weight-3 UK item from that day's digest, and each field is new, so queue rule 2 (longest wait) applies honestly:
  - 17 Nov: energy (the price cap)
  - 18 Nov: migration (the asylum support charge)
  - 19 Nov: youth jobs (the Milburn review)
  - 20 Nov: policing (Local Police Commands)
  - 21 Nov: EU trade (the summit deal)
  - 22 Nov: high-street jobs (the Poundland sale)
- 23 Nov: **D7. Answer C goes through Bob's Codex in a plain chat** for local replays, because the local Codex CLI hung. The live run uses the `sim-rival` worker on Codex.
- 23 Nov, Thames, first real numbers:
  - **Citizens** (Haiku): about 93k subagent tokens, about 2 minutes. Split: 37% of simulated citizens said yes, against 74% in the real YouGov poll; 35% were unsure.
  - **Answers A and B** (Sonnet): about 46k tokens each, about 5 seconds each.
  - **Answer C** (Codex `gpt-6`): one chat.
- 23 Nov: **Thames Water ran end to end.** Stages: clerk (by hand) → citizens (Haiku) → C (Bob Codex, `gpt-6`) → A and B (Sonnet, blind) → gate (Sonnet) → jury (Haiku) → minister (Sonnet). Published and valid.
  - **Gate:** 0 of 3 pass every test; 1 unsourced claim struck from B.
  - **Jury:** votes 2/5/2/3. Ruling: customers and staff, with lenders taking the loss.
  - **Minister:** signed one panel trial, with three predictions due 30 Nov, 22 Jan and 30 Jun.
  - **Cost, measured** (subagent tokens; these include cached prompt reads, so they overstate the billed figure):
    - citizens 93k, A 46k, B 46k, gate 59k, jury 60k, minister 60k;
    - clerk about 65k (from the six backfill clerks: 63k to 68k each);
    - C is one Codex chat;
    - **total about 430k tokens for one issue-day.**
  - The earlier review **guessed** today's government at 1.5 to 2M tokens a day. On that guess, one issue a day adds about a quarter, well under the 3x stop line.
- 23 Nov: **private page published:** https://claude.ai/artifact/GArjgzYRpi2Hc7C2ZjTi7V (Thames only for now). The routine and the README point at it.
- 23 Nov: `simulation/live` created from `origin/main` and pushed, holding Thames. `future-proof/simulation` pushed (code only; the issue files stay off that branch).
- 23 Nov: removed two provenance cards that `prov.py` had filed under an absolute path in `_elsewhere/`. `pool.json` and `distributions.json` now each carry a `.prov.json` beside them, and the pool also holds its own recipe (seed, method, sources) and rebuilds with `make-pool.mjs`.
- 23 Nov: **one-off cloud test of `routine.md` from the branch** (`trig_017CJQoAzXjQbQCVNqz6ZwNy`) is running.
- 23 Nov: **the cloud publish test worked** (run `cse_017kNM1fdEKHkUmgqTmX13JJ`). It read `routine.md` from the branch, found nothing due, built the feed and republished the private page. It hit two snags, both now fixed in `routine.md`:
  - files outside the working directory can't be published, so the page is now built in `.sim-page/`;
  - `feed.json` must be read before it can be replaced.
- 23 Nov: **daily routine created:** "Future Proof simulation: clock and page (daily)", `trig_012kXE2KMjrHYuber7bJBmev`, cron `0 13 * * *` UTC (13:00 London in winter).
  - **Guard:** it replies "not merged yet" and stops until `routine.md` exists on main, so Kai's merge is what switches it on.
  - Manage it at https://claude.ai/code/routines/trig_012kXE2KMjrHYuber7bJBmev.
- 23 Nov: **backfill.** All six days are past citizens. 20, 21, 22, 18 and 19 are each running bench to minister in one Sonnet orchestrator (`scratchpad/tools/orchestrate.md`); 17 is running gate to minister.
  - **Citizen splits** (simulated, against a real poll where one exists):
    - 19 Nov: 44% yes, against Ipsos for DWP 82%;
    - 17 Nov: 60% yes; 18 Nov: 53%; 20 Nov: 65%; 21 Nov: 34%; 22 Nov: 39% (no matching poll for these).
- 23 Nov: **backfill done: 7 replayed days published and valid.**
  - **Pushed** to `simulation/live` (`83c3f6d5`).
  - **Private page republished** with all seven: https://claude.ai/artifact/GArjgzYRpi2Hc7C2ZjTi7V. The scoreboard shows 18 predictions pending and 0 marked.
  - **The seven days:**
    - 10 Nov, Thames Water: jury picked customers and staff, with lenders taking the loss.
    - 17 Nov, price cap: quick help, paid for by the richest.
    - 18 Nov, refugee support charge: repay what you can afford, under a cap.
    - 19 Nov, youth jobs: a guaranteed place, with a duty to take it.
    - 20 Nov, local police: a commander who can be removed by a panel of residents drawn by lot.
    - 21 Nov, EU fees: home rates only for countries that match them.
    - 22 Nov, high street: staff and councils get first call on closing stores.
  - Every minister signed a one-area trial. In 7 of 7 the gate found 0 of 3 answers passing every test: most rows are "unclear", which is honest, because the sources rarely settle a proposal ahead of time.
  - **Hard-rule review by hand:**
    - "the public" appears only inside a real poll's wording (Thames: "public sector");
    - no minister quotes a real person;
    - every prediction falls due after 23 Nov.
  - **Two fixes made:**
    - 19 Nov's statement now attributes "25 pounds for every 1 pound" to the government's own figure (s2), instead of stating it as fact;
    - a stray note was taken out of 22 Nov's struck-out claims.
  - **Cost per replayed day, measured:** clerk about 65k, citizens about 90k, orchestrator (C relay, join, gate, jury, minister) about 80k, plus A and B about 46k each. **About 330k to 430k tokens a day.**
  - **Jury model:** for 17–22 Nov the orchestrator wrote the juror votes on Sonnet, not Haiku, and the files say so.
  - **Stray Codex chats:** two placeholder messages were sent by mistake (chats `a1418e41…` and `183f66e0…`); they weren't used.
- 23 Nov: checks:
  - `vitest run scripts/government`: 345 passed;
  - `policy-lint`: 55 policies, 0 errors;
  - sync assembles 12 workers and 12 schedules;
  - no change under `docs/government/policies/`.
- **Next:** open the one PR. After Kai merges, verify the first live run (Bob 09:00–11:30 London time, then the routine at 13:00 UTC) and write the report.
- 23 Nov, 19:12 UTC: **Kai asked for PR #30 to be merged, and it was** (`cde5bcc2`).
  - `bob-sync` succeeded. Bob now lists the seven `gov-4*-sim-*` schedules, the first due 24 Nov at 09:00 London time.
  - `site-deploy` didn't run: the merge touched none of its paths, so badcode.tv is unchanged.
- 23 Nov, 19:13 UTC: **a manual live run for 23 Nov started in Bob:** `sim-clerk` chat `d84b5673-4d15-45f6-b5a2-a04758967547`, on the EDITH AI breast-screening trial.
  - It at first made worktrees from inside `/project/work/core`, then removed them and ran `bob-setup.sh` correctly.
  - Worth tightening the setup text so it never touches core's worktree list.
- 23 Nov: **Kai wants the last two weeks backfilled and the simulation on badcode.tv,** which reverses "private first". Brief: [`GOAL-2.md`](./GOAL-2.md). The replay kit was copied into [`replay-kit/`](./replay-kit/).
- 23 Nov, 19:15 to 19:45 UTC: **the 23 Nov live run in Bob, step by step,** each started by `chat_create` with its schedule message, each checked by its commit on `simulation/live`:
  - clerk `7b4b0b99` (EDITH AI breast screening), citizens `06b03240`, rival C `4778c643`, bench `7d6c9705`, gate `f323afe5`, jury `ec82e1f8`, minister `12617fdc`.
  - **Verified published and valid** (goal 1's last item). C is Codex `gpt-6`, A and B Sonnet, jury Haiku. A real poll sits beside the citizens (Focaldata for King's College London and partners, March 2026).
  - The minister signed a one-hospital trial (Cambridge): one expert plus AI against two experts, drawn by lot, every woman told her group and free to keep two experts. Predictions are due 22 Jan 2027 (two) and 23 Nov 2027.
  - "the public" appears only in two real sources' own titles.
  - Each step took about 4 to 8 minutes in Bob, so the whole loop runs in under 40 minutes, well inside the 09:00 to 11:20 schedule.
- 23 Nov, goal 2: **the seven missing days (9, 11–16 Nov) were assigned topics up front** from each day's Bob news digest, every field new:
  - 9 Nov: school curriculum (Key Stage 3 restored as its own phase);
  - 11 Nov: housebuilding costs (a think tank's figure for rule-driven costs);
  - 12 Nov: social care (neighbourhood home care, a National Care Service funded by Triple Lock changes);
  - 13 Nov: leasehold (service charge protections);
  - 14 Nov: criminal records (ending lifelong disclosure of some childhood convictions);
  - 15 Nov: evictions (possession claims up 21% after Section 21 ended);
  - 16 Nov: research funding (the cost of joining the EU's next research programme).
  - All seven clerks (Sonnet, in parallel) finished in about 1.5 minutes each, 64k to 68k tokens each, all valid. Then one Sonnet day-runner per day: citizens on a nested Haiku subagent, then `replay-kit/orchestrate.md` A to F.
  - Clerk notes worth keeping: 12 Nov's gov.uk page was updated on 18 Nov to fix one research body's name, so the issue leaves that body unnamed; several trade-press and survey pages refused automated fetches (403) and were left out rather than cited unopened.
- 23 Nov: **site work on branch `future-proof/site`** (from main): `apps/site/simulation.mjs` and its test, the build step, a TV link on the government page, a SIMULATED preview picture (`scripts/government/sim/preview.sh` draws it), and the schedule in `site-deploy.yml` (D8). Checked in Chrome at 1280 and 390 wide: no errors, no sideways scroll.
- 23 Nov, about 20:10 UTC: **two-week backfill done: 9 to 22 Nov all replayed, plus the live 23 Nov.** Pushed to `simulation/live` (`8790d3eb`). The private page is republished with 15 issues and 35 predictions waiting.
  - **The new seven days, and what each minister signed:**
    - 9 Nov, school curriculum: ten schools, each with a panel drawn by lot that signs off a published plan for Years 7 to 9 (jury 5 of 12: families and teachers decide).
    - 11 Nov, housebuilding costs: three councils decide standard planning applications to a deadline, with the fee refunded if late (jury tied 5 to 5; the tie rule picks the option the gate found safest).
    - 12 Nov, social care: two councils run neighbourhood home care with carers and care users on the board, nothing taken from pensions (jury 6 of 12).
    - 13 Nov, leasehold: in one region, landlords carry their own legal costs in service charge disputes (jury 5 of 12).
    - 14 Nov, childhood records: a fixed filtering period for minor childhood convictions; serious offences and child-safety checks unchanged (jury 5 of 12).
    - 15 Nov, evictions: in one county court area, a ring-fenced landlord claim fee pays for judge sitting days (jury 4 of 12).
    - 16 Nov, research funding: an independent board advises on the EU research programme, with costs published yearly and no NHS or school money (jury 5 of 12).
  - **Cost per day, measured:** clerk 64k to 68k; each day-runner 81k to 86k of its own; citizens (Haiku) 85k to 107k; A and B about 46k each. That's about **330k to 360k tokens a day**, plus one Codex chat, as before. All seven ran in parallel: clerks about 1.5 minutes, day-runners 4 to 5 minutes.
  - **Hand review against the hard rules,** for each day: "the public" appears nowhere except in real sources' titles; no minister quotes a real person; every prediction falls due after 23 Nov.
    - Each of the 9, 12 and 13 Nov predictions was checked by web search to see whether it had already been settled before 23 Nov.
  - **Fixes made by hand:**
    - **13 Nov hindsight:** the bill the first prediction named was introduced on 19 Nov, before the run date, so that prediction was already settled. The second (litigation-cost regulations "laid before the end of 2026") may already have been laid in draft. Both were replaced with one prediction that was knowable on 13 Nov and still open: "no delay to the 1 April 2027 start announced by 22 January 2027". The 1 April prediction stays.
    - **13 Nov:** answer A's title had been cut mid-word by `join_bench.py`, and its "loser-pays" didn't match the answer. It was retitled to say what the answer says, and `join_bench.py` now cuts long titles at a word.
    - **15 Nov:** Codex had prefixed answer C's title with "SIMULATION:". That prefix was removed.
  - **Lesson for the minister's instructions:** a replay's minister should check that a prediction hasn't already happened between the news date and the run date. The 13 Nov one hadn't been checked.
- 23 Nov: **gatekeeper round 1: FAIL** (`marketing-gatekeeper` on the built page, the preview picture and the 7 older issues). Everything it raised was fixed as follows.
  - **Page code:**
    - Every panel header, the scoreboard and each answer now carry the SIMULATED stamp, with a test to keep it that way.
    - The minister is now "Simulated <post>" on cards, in the loop and in the minister panel, which also says "BadCode's AI stand-in, not the real office-holder".
    - The jury chip shows the winning option and its votes, where before it showed a cut-off sentence.
    - A one-line AI disclosure links to `/how-we-made-it/`, and an opening line now says what the page is for.
    - The loop's "public rule" station is now "Why this one".
    - The noscript list printed an empty "()" because it read the wrong field (`run.stamp`, where the data has `run.replay_stamp`). Fixed.
    - The voices panel is now top-aligned.
  - **Worker instructions:**
    - **gate:** strike unsourced claims from the clerk's summary too; never let an answer put words in an office-holder's mouth; proposals go in the conditional; a plain-words note for reasoning.
    - **minister:** no sarcasm about hardship; nothing said about what a real office-holder, company or board did without a source; sign the ruling as voted, or say plainly why not; the predicted event itself must fall after the run date.
    - **clerk:** `slot_reason` is written for a reader.
    - **citizens:** voices answer the question, with no claims about groups of people.
  - **Issue data:** an editor (Opus) is fixing all 15 issues against the gatekeeper's list: unsourced lines in the 22 Nov summary and statement, the sarcastic energy opening, office-holder attributions, the Ofgem date check, plumbing words, unprompted group claims in voices, and the police minister signing the lighter option.
  - **Left for later (REVISE, not FAIL):** the citizen pool draws home ownership independently of age, so some young students "own outright". Fixing it needs a versioned pool (`pool-2`), because published issues name people by their id in the current pool. Logged as the first job after goal 2.
- 23 Nov: **the issue editor (Opus) fixed all 15 issues** (pushed `259ae939`). Ofgem announces the January to March 2027 cap on 25 Nov 2026, after the run date, so the energy prediction due 30 Nov stands.
- 23 Nov: **gatekeeper round 2: PASS to deploy.** Every round-1 FAIL is fixed, and the 8 issues it hadn't seen have no FAILs. Its eight small REVISE notes were all done (`d25468b7`):
  - 13 Nov's fail number was backwards and now reads "fails if more than 1 in 10 challenges are dropped over cost";
  - a struck claim had come back reworded in 15 Nov answer B, and was cut; the gate now treats a reworded struck claim as struck;
  - four statements got plainer lines;
  - 19 Nov's prediction now credits "the 17 November statement" instead of a real Secretary;
  - the Thames note says its re-check used only sources dated on or before 10 Nov;
  - the page and its description say "a simulated minister".
- 23 Nov, 19:47 UTC: **PR #31 merged; the simulation is public.** Kai's goal-2 message allowed the merge once tests, lint and the gatekeeper passed.
  - `site-deploy` built "simulation: 15 issues, 0 skipped" and deployed. https://www.badcode.tv/future-proof/live/ returns 200 for the page, `feed.json` and `preview.png`, with the title "SIMULATED · Future Proof Live · BadCode". Checked in Chrome on the live site at 1280 and 390 wide: no errors.
  - `bob-sync` succeeded, so the four tightened workers are live in Bob for tomorrow.
  - The private mirror is republished with the corrected page and data (version 5).

## Report (goal 2)

### What runs when (every day, London time; UTC in winter)

| Time | What | Where | Writes |
| --- | --- | --- | --- |
| 09:00 | `sim-clerk` picks the story, poll and sources | Bob, Sonnet | `simulation/live` |
| 09:20 | `sim-citizens`: 100 simulated citizens, drawn by lot, set the tests | Bob, Haiku | `simulation/live` |
| 09:40 | `sim-rival`: answer C, blind | Bob, Codex | `simulation/live` |
| 10:00 | `sim-bench`: answers A and B, blind; joins C | Bob, Sonnet | `simulation/live` |
| 10:30 | `sim-gate`: every answer against every test; strikes unsourced claims | Bob, Sonnet | `simulation/live` |
| 11:00 | `sim-jury`: 12 simulated jurors vote on the values question | Bob, Haiku | `simulation/live` |
| 11:20 | `sim-minister` signs one small trial with dated predictions; publishes | Bob, Sonnet | `simulation/live` |
| 12:15 UTC | `site-deploy` rebuilds badcode.tv from the branch | GitHub Actions | badcode.tv |
| 13:00 UTC | routine `trig_012kXE2KMjrHYuber7bJBmev`: marks due predictions, republishes the private mirror | claude.ai cloud | `simulation/live`, mirror |
| 14:30 UTC | `site-deploy` again, so the marks reach the site | GitHub Actions | badcode.tv |

Each Bob step took 4 to 8 minutes on 23 Nov, so the whole loop runs in under 40 minutes of the 2h20 window.

### The cost of one day

- **Measured:** about 330k to 430k tokens per issue-day, from subagent totals, which include cached reads. Per step: clerk 65k, citizens 85k to 107k, A and B 46k each, gate, jury and minister about 60k each. On top of that comes one Codex chat for C, plus about 1 minute of Actions twice a day.
- **Against the stop line:** that's about a quarter of the government run's guessed 1.5 to 2M tokens a day, far under the 3x stop line. Bob doesn't count tokens yet, so the live number is still an estimate.

### What failed, and what was done about it

- **A prediction already settled before the run date** (13 Nov: the bill had been introduced on 19 Nov). It was replaced, and the minister's instructions now require a check that the predicted event hasn't already happened.
- **Gatekeeper round 1 FAILed the public page** (the SIMULATED stamp missing from panels; real job titles on the AI ministers) and six issues (unsourced lines; sarcasm about hardship; real office-holders paraphrased; group claims in voices). All fixed; round 2 passed.
- **A struck claim survived in a clerk's summary,** and another came back reworded. The gate now checks the summary and rewordings.
- **`join_bench.py` cut titles mid-word.** It now cuts at a word.
- **Small things:** Codex once prefixed a title with "SIMULATION:"; the Bob clerk first made worktrees inside `/project/work/core`, then cleaned them up.
- **Open:** the citizen pool draws home ownership independently of age. A versioned `pool-2` is needed.

### From one issue a day to five

1. **The data allows it already.** An issue's id and draw seeds are per issue, and `sim.mjs find` lists every file for a date. The page and feed show any number per day.
2. **Bob runs a project's schedules one at a time,** so five issues means five times as many steps in the window. At about 6 minutes a step, 5 × 7 steps is about 3.5 hours: start at 07:00, or split the morning.
3. **The clerk picks five distinct fields** in one run (queue rules 1 to 3, no repeats) and writes five clerk-stage files. Each later worker then loops over every issue at the stage before its own, one at a time, as the replay kit did. This change is to the worker text only: "for each issue at stage X".
4. **Cost scales linearly:** about 1.7 to 2.2M tokens a day for five. That is roughly the government's own daily run and still under the 3x line, but worth measuring on one day before switching.
5. **The gatekeeper's lesson:** with five a day, review by hand won't keep up. Before scaling, add an automated pre-publish check to `issue.mjs`:
   - flag "the public", rule numbers and tool names in text fields;
   - flag `rejected_claims` text that is still in the summary or statement;
   - flag office-holder titles followed by "says".
