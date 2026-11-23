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

## Log

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
