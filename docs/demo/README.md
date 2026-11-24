# The Future Proof Demo

A demo, not a simulation. Every day one made-up case, on a topic that is really in the news, goes round
the Future Proof loop and ends in a clear, chosen way: **accepted**, **partly** or **rejected**. A demo
government of seven invented ministers sits on top. Every line in their manifestos comes from a demo day.

It's like fixture data in a test: the case is written to show the process working, not to settle the
real question. It sits beside the Future Proof simulation (`docs/government/simulation/`) and shares
nothing with it except a copy of the citizen pool.

- **Why:** [`design/2026-11-24-future-proof-demo/GOAL-3.md`](../../design/2026-11-24-future-proof-demo/GOAL-3.md).
- **The data shape and its rules:** [`scripts/demo/issue.mjs`](../../scripts/demo/issue.mjs) (a day) and
  [`scripts/demo/government.mjs`](../../scripts/demo/government.mjs) (the government).
- **The command line:** `node scripts/demo/demo.mjs`, whose usage is listed at the top of the file.

Every demo worker reads this file before it starts. The rules below are the whole contract.

## Where things are

| What | Where |
| --- | --- |
| Code, the pool, the cabinet, these rules | `main`. In Bob: `/project/work/.demo/main` (read-only) |
| The days | Branch `demo/live`, `docs/demo/days/<news date>/<id>.json`. In Bob: `/project/work/.demo/live` |
| A step's working notes | Next to the day, as `<id>.side.<step>.json`. The feed ignores them |
| The government | Branch `demo/live`, `docs/demo/government/<news date>.json` |
| The page | https://www.badcode.tv/demo/, built from `demo/live` each time the site deploys |

## A day, step by step (Europe/London)

| Time | Worker | Engine | Does | Stage after |
| --- | --- | --- | --- | --- |
| 12:00 | `demo-clerk` | Claude Sonnet | today's area and ending from the rotation; a real news topic in that area; a made-up case built for the ending | `case` |
| 12:15 | `demo-citizens` | Claude Haiku | 100 citizens drawn by lot set 3 to 6 tests, at least one a limit (a red line) | `citizens` |
| 12:30 | `demo-rival` | Codex | answer C (side file) | `citizens` |
| 12:45 | `demo-bench` | Claude Sonnet | answers A and B; merges C | `bench` |
| 13:05 | `demo-gate` | Claude Sonnet | marks every answer on every test, honestly; works out the ending reached | `gate` |
| 13:25 | `demo-redo` | Claude Sonnet | only if the ending missed the plan: rewrites the case or the answers, never a mark | `bench` |
| 13:40 | `demo-gate` | Claude Sonnet | the second round, only if `demo-redo` sent it back | `gate` |
| 13:55 | `demo-jury` | Claude Haiku | 12 jurors drawn by lot settle the values question | `jury` |
| 14:10 | `demo-minister` | Claude Sonnet | adopts, trials or sends back; writes predictions | `published` |
| 14:25 | `demo-cabinet` | Claude Sonnet | the ministers debate the day and change the manifestos | (government file) |

Bob runs a project's schedules one at a time, so each step waits for the one before it. Each step reads
today's file, checks it is at the stage before its own, adds its part, validates, commits and pushes to
`demo/live`. A step that finds the file missing or at the wrong stage writes one line saying so and stops.

## The three endings (worked out by `scripts/demo/issue.mjs`, never by hand)

- **Accepted:** at least one answer passes every test and limit. The minister adopts it as written, and
  it becomes a **policy** line in that minister's manifesto.
- **Partly:** no answer passes everything, but at least one keeps within every limit. The minister signs
  a small **trial** of the best such answer, with a stop date. It becomes a **trial** line.
- **Rejected:** every answer breaks at least one limit. Nothing is signed. The day is **sent back**, and
  the page says which red lines each answer crossed.

The rotation (`demo.mjs plan <date>`) gives each date its area and ending. Over three weeks every area
meets every ending once.

## Rules for every step (never broken)

1. **Steer the inputs, never fake the marks.**
   - The clerk builds the case, and the citizens set the tests, so that the chosen ending can be
     reached.
   - The gate marks only what each answer says, and never opens the clerk's design notes.
   - If the marks miss the plan, `demo-redo` rewrites the case, the tests or the answers, and the gate
     marks again. A mark is never edited. The page shows how many rounds a day took.
2. **Real topic, made-up case.**
   - The topic must really be in that day's UK news, with a source you opened.
   - The case (the town, the people, the proposal, the numbers) is invented and says so in
     `case.place` (e.g. "Fernbridge (made up)").
   - Name no real person or company in a case. Never put words in a real person's mouth.
   - A real statistic may appear in `case.facts`, with its source.
3. **The citizens are made up.** They are "the citizens" or "the town's citizens". Never "the public",
   "people decided" or "Britain thinks".
4. **Predictions are about the real world.** The case is invented, so a prediction is about the real
   national topic it plays out: a published figure or decision that can be checked on its due date, by
   a named publisher. Each one falls due after the run date.
5. **Plain words.** Short sentences, no software words, no jargon. Follow `docs/voice.md` and
   `docs/marketing/the-reader.md`. Swear words are written in full if used.
6. **Fixed by lot.** Citizens and jurors come only from `demo.mjs draw <id>`, never hand-picked.
7. **Validate before you push:** `node <MAIN>/scripts/demo/demo.mjs validate <file>`. Never push a file
   that fails.

## Commit and push (every step)

```bash
cd /project/work/.demo/live
git add docs/demo/
git -c user.name="BadCode demo" -c user.email="demo@badcode.tv" commit -m "Demo <news date>: <stage> (<worker>)"
bob-push
```

## Backfill

A backfill runs the same steps for an older news date, with `run.mode: "backfill"` and `run_date` the
day it was really run. The message that starts a step says so, e.g.
`Backfill: news_date=2026-11-17 run_date=2026-11-24`. Without that, the step is daily: the news date and
run date are both today.
