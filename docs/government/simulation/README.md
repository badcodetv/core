# The Future Proof simulation

**SIMULATED.** Every day, one real news story goes round the Future Proof loop. Simulated citizens
set the test, three blind answers compete, the gate checks them, a simulated jury settles the values
question, a minister signs one small trial, and the clock marks it on the date. Nothing here is real
people taking part. The news, the sources and the dates the predictions are marked on are real.

- **Why:** [`design/2026-11-23-future-proof-rework/`](../../../design/2026-11-23-future-proof-rework/README.md)
  (Kai's decisions, 23 Nov 2026).
- **The data shape and its rules:** [`scripts/government/sim/issue.mjs`](../../../scripts/government/sim/issue.mjs).
  Check a file with `node scripts/government/sim/sim.mjs validate <file>`.

Every simulation worker reads this file before it starts. The rules below are the whole contract.

## Where things are

| What | Where |
| --- | --- |
| Code, the citizen pool, these rules | `main`. In Bob: `/project/work/.gov-sim/main` (read-only) |
| The issue files | Branch `simulation/live`, under `docs/government/simulation/issues/<news date>/<id>.json`. In Bob: `/project/work/.gov-sim/live` |
| A stage's working notes | Next to the issue, as `<id>.side.<stage>.json`. The feed ignores them |
| The page | A private claude.ai artifact, https://claude.ai/artifact/GArjgzYRpi2Hc7C2ZjTi7V, republished daily by a cloud routine ([`routine.md`](./routine.md)) |

The simulation never edits `docs/government/policies/` (the manifesto), never opens a PR, and never
touches `/project/work/core` beyond reading `origin/main` with `git show`.

## The daily cycle (Europe/London)

Each step is one Bob worker. Bob runs a project's schedules one at a time, so each step waits for the one
before it. Each step reads today's issue file, checks it is at the stage before its own, adds its part,
validates the file, commits and pushes to `simulation/live`. A step that finds the file missing or at
the wrong stage writes one line saying so and stops. It never guesses and never skips ahead.

| Time | Worker | Engine | Adds | Stage after |
| --- | --- | --- | --- | --- |
| 09:00 | `sim-clerk` | Claude Sonnet | the issue, a real poll if one exists, the news, the sources | `clerk` |
| 09:20 | `sim-citizens` | Claude Haiku | 100 simulated citizens drawn by lot set the tests | `citizens` |
| 09:40 | `sim-rival` | Codex | answer C, written blind (side file) | `citizens` |
| 10:00 | `sim-bench` | Claude Sonnet | answers A and B, each written blind; merges C | `bench` |
| 10:30 | `sim-gate` | Claude Sonnet | checks every answer against every test and limit, with sources | `gate` |
| 11:00 | `sim-jury` | Claude Haiku | 12 simulated jurors drawn by lot vote on the values question | `jury` |
| 11:20 | `sim-minister` | Claude Sonnet | the minister signs or refuses, writes the statement and predictions | `published` |
| 13:00 | cloud routine | Claude | marks predictions that are due, rebuilds the feed, republishes the page | n/a |

## Rules for every step (never broken)

1. **SIMULATED, always.** Every file has `"simulated": true` and `"stamp": "SIMULATED"`.
   - Simulated citizens are "simulated citizens" or "the citizens". Never "the public", "people
     decided" or "Britain thinks".
   - Where a real poll exists, it sits beside them.
2. **Sources or silence.** Every fact about the world must point at a source in the file's `sources`
   list: a URL you opened, with its publisher and date.
   - Claims about a real person or company come only from a published source. Never invent one, never
     round one up, never put words in a real person's mouth.
   - If you can't source it, leave it out. The gate deletes unsourced claims and lists them in
     `rejected_claims`.
   - Simulated citizens' and jurors' own words are opinions, marked as theirs. They're never facts.
3. **No hindsight.** A prediction must fall due after the issue's `run_date`.
   - In a replay (an issue made later from older news), write only what was knowable on the news date.
   - Predict only things still in the future on the run date.
4. **Plain words.** Short sentences, no software words, no jargon. Follow `docs/voice.md` and
   `docs/marketing/the-reader.md`. Never blame the reader. Swear words are written in full if used,
   never asterisked.
5. **Small and testable.** A minister signs one small trial with a fail number and a stop date, never a
   sweeping programme.
6. **Fixed by lot.** Citizens and jurors come only from `sim.mjs draw <issue id>`, never hand-picked.
   The seeds are printed in the file.
7. **Validate before you push.** Run `node <MAIN>/scripts/government/sim/sim.mjs validate <file>`.
   - A failing file is fixed or, if you can't fix it, left uncommitted, with one line saying why.
   - Never push a file that fails.

## Commit and push (every step)

```bash
cd /project/work/.gov-sim/live
git add docs/government/simulation/issues/<news date>/
git -c user.name="BadCode simulation" -c user.email="sim@badcode.tv" commit -m "Simulation <news date>: <stage> (<worker>)"
bob-push
```

`bob-push` pulls with rebase and pushes, retrying a few times. Stage only the issue's own folder.

## Replays

A replay runs the same steps on an older day's news, with `run.mode: "replay"` and the exact stamp
`Replayed on <run date> from the news of <news date>`. The message that starts a step says so, e.g.
`Replay: news_date=2026-11-17 run_date=2026-11-23`. Without that, the step is live: the news date and
run date are both today.
