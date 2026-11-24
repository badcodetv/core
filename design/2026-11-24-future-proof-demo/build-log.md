# Future Proof Demo: build log

The goal is [`GOAL-3.md`](./GOAL-3.md) (Kai, 24 Nov 2026). Newest entries at the bottom.

## Decisions

- **E1. A fresh start, beside the simulation.**
  - New code in `scripts/demo/`, new rules in `docs/demo/`, new data branch `demo/live`, new workers
    `demo-*`, new page `/demo/`.
  - Copied from the simulation: the lot drawer and the citizen pool (with recipe cards pointing at the
    originals).
  - Nothing in `scripts/government/sim/`, `docs/government/simulation/`, `simulation/live` or the
    `sim-*` workers was changed.
- **E2. The rotation is code** (`plan()` in `scripts/demo/issue.mjs`).
  - Areas go round weekly (housing, health, education, work, energy, transport, crime).
  - Area k in week w gets ending `[accepted, partly, rejected][(k + w) % 3]`.
  - That gives 5, 5 and 4 in the first fortnight, as the goal asks. Over three weeks every area meets
    every ending once.
  - A 14-day cycle would have locked each area to two endings forever.
- **E3. The endings are worked out from the marks, never set by hand.**
  - accepted: an answer passes every test and limit.
  - rejected: every answer fails a limit (a red line).
  - partly: anything in between.
  - The validator refuses a published day whose marks don't reach its planned ending. So "steer the
    inputs, never fake the marks" is enforced, not just asked for.
  - Why "rejected" means crossing red lines rather than "no test passed": it gives each sent-back day
    a concrete reason to show ("A crossed t3, B crossed t4"). And a fair checker will usually pass an
    answer on something.
- **E4. One redo, then a second marking round.**
  - When the marks miss the plan, `demo-redo` changes the inputs and the gate marks again. Inputs means
    the case, the tests or the answers, never the marks.
  - Daily: at most two rounds (two gate schedules).
  - Backfill: two days were given a third round by hand (14 and 18 Nov). The validator allows up to
    three.
  - Days that needed another try say so on the page (`gate.rounds`, `made_by.note`).
- **E5. The gate marks blind to the plan.**
  - In the backfill, the gate is a separate subagent given the day without `plan` and without the
    clerk's design notes.
  - In Bob, the worker is told never to open them.
- **E6. Predictions are about the real topic,** never the made-up place, so the clock can still mark
  them against a named publisher's figure.
- **E7. The government is folded from day files** (`scripts/demo/government.mjs`).
  - One `docs/demo/government/<date>.json` per day holds the debate and the changes.
  - A line is born only from an adopted or trialled day, in that minister's area. Only its own
    minister changes or drops it.
  - Folding in date order gives each line's history, so the page can show the manifestos growing.
- **E8. Bob reads the demo's own folder.**
  - `sync-bob.mjs` now also loads `docs/demo/workers/*.md` and `docs/demo/schedules.json`, and the
    `include: demo` common ground (`docs/demo/worker-common.md`).
  - The chain runs 12:00 to 14:25 London, after the simulation's morning chain.
- **E9. The site reads `demo/live` at build time,** the same way it reads `simulation/live` (simulation
  D8), with one more scheduled rebuild at 15:00 UTC.
- **E10. Labels:** one "This is a demo" banner, "Demo" in the title, and a link preview saying THIS IS
  A DEMO. Place names carry "(made up)". There are no per-card stamps (Kai, 24 Nov).
- **E11. The backfill writes answer C with Claude,** like A and B, in a separate blind subagent. The
  daily run uses Codex for C (`demo-rival`). Codex through a Bob chat was the slowest part of the
  simulation's replays.

## Log

### 24 Nov, morning

- Code, rules, nine workers, ten schedules, site wiring and preview written on branch `demo/build`.
- Tests: `scripts/demo` 9 passed; `scripts/government` all passed, with a new sync test for the demo
  workers.
- One pilot day (10 Nov) launched to test the brief before the other thirteen run in parallel.

### 24 Nov, midday: the backfill

- **Pilot (10 Nov):** valid first time, but all three answers passed every test, which shows nothing.
  - Fixed: citizens' tests must be demanding, the jury goes juror by juror, predictions start from the
    latest real figure, and the validator refuses answers over 130 words.
  - The pilot day was discarded and rerun with the others.
- **14 days run in parallel** (one Sonnet orchestrator per day, with blind subagents for A, B, C and the
  gate).
  - Three days stopped at the session's limit of 20 subagents at once, then were resumed as others
    finished.
  - Cost per day: about 80k to 150k subagent tokens, typically about 100k (from the subagent totals,
    which include cached reads). That's roughly a quarter of a simulation day.
- **Result:** 14 valid days, 5 accepted, 5 partly and 4 rejected, each reaching its planned ending.
  - Rounds: 7 days in one, 5 in two, 2 in three.
- **What missed, and the fix (now in the worker files):**
  - **partly → accepted:** a careful answer could meet everything. Fix: the clerk builds the tension in
    as hard numbers (e.g. the money covers 1,200 of 1,500 homes) and the citizens ask for the thing
    those numbers rule out.
  - **rejected → partly:** an answer kept every red line by leaving the bind unsolved. Fix: the bind
    itself ("the books must balance") is a red line, not just a test.
- **Discarded and rerun:** the first 23 Nov.
  - Its real-news hook was a specific child-exploitation sentencing (real victims): never again.
  - Its case also echoed 16 Nov's records theme.
  - The rerun uses the early-release policy story.
- **Hand review fixes:**
  - **14 Nov:** made-up phone numbers swapped for Ofcom's drama ranges (`0808 157 0xxx`,
    `03069 990xxx`).
  - **20 Nov:** a stock-data site replaced by the ONS bulletin of 17 Nov, with the figures checked on
    the page.
- **Known weak spots, left as they are:**
  - **15 and 22 Nov (transport):** both hang on the £2 bus fare cap (a DfT statement of 22 Jul),
    because neither day's digest had a transport story. It shows one topic reaching two endings.
  - **16 Nov (crime):** its predictions are national crime figures, not its pardoned-records topic.
  - **18 Nov:** its prediction is "the next Hospice UK count", whose timing is loose.

### 24 Nov, afternoon: the marketing gatekeeper

- **Round 1: REVISE, no FAIL.** What it asked for, and what changed:
  - **AI disclosure.** The banner now says every town, citizen, vote, answer, mark and minister is made
    up and written by AI, and links to how we use AI. Answers say "Written by AI (Claude Sonnet)".
  - **"The citizens set the tests" was contradicted by the second tries, which changed tests.** We took
    the honest route: the banner says each day's ending is picked in advance, and that the case, and
    sometimes the tests, are rewritten until the honest marks reach it. Every second-try note is now
    in plain words.
  - **"In the news that day" wasn't true for 15, 22 and 23 Nov.** Those days now say so, and the
    record says "a real topic from the UK news".
  - **Baselines.** Predictions can now cite sources (schema change). Every baseline figure was opened
    and confirmed, or reworded where it couldn't be.
  - **Gresmoor (16 Nov).** The crime-statistics predictions are replaced by one about the pardon
    guidance, the title says "delete", and the record count is lower.
  - **Ministers.** Titles are now "Demo minister for …", and "Joe Kettering" is renamed "Joe Mallin"
    (Kettering is a real constituency).
  - **Copy.** Garbled lines and self-introductions fixed, two minister lines reworded (one implied
    citizens were fooled, one tied teenagers to crime), real village names replaced, and citizen ids
    removed from labels.
- **Round 2: REVISE, six small items.** All were fixed:
  - a leftover sentence on Corvenhall that tied young people to crime;
  - Rennowick's predictions, rewritten without a guessed bulletin date;
  - the banner, which now says "the figures the predictions will be checked against" are real, not the
    predictions;
  - one of the two unemployment predictions made strict, so both can't hit;
  - two made-by lists;
  - Gresmoor's finish date moved to the real guidance's one month.
- **Round 3:** see the report.

## Report (goal 3)

### What runs when (after the merge)

| When | What |
| --- | --- |
| 12:00 to 14:25 London | Bob: `demo-clerk` → `demo-citizens` → `demo-rival` (Codex) → `demo-bench` → `demo-gate` → `demo-redo` (only if the marks missed) → `demo-gate` (second round, only after a redo) → `demo-jury` → `demo-minister` → `demo-cabinet`. Each pushes to `demo/live` |
| 15:00 UTC | `site-deploy` rebuilds badcode.tv, which reads `demo/live` and publishes `/demo/` |
| Any push to main touching the demo page or code | `site-deploy` too |
| On merge, and on any change to `docs/demo/workers` or `docs/demo/schedules.json` | `bob-sync` puts the workers and schedules into Bob |

The demo chain runs after the simulation's morning chain (09:00 to about 11:30). Bob runs a project's
schedules one at a time, so they never overlap.

### The cost of one day

- **Backfill:** about 80k to 150k subagent tokens a day, typically about 100k (cached reads included).
  That's about a quarter of a simulation day.
  - Days needing a second or third round cost about 120k to 150k.
  - The ministers' debate for all 14 days together was about 100k.
- **Daily in Bob:** cheaper. The citizens and jury run on Haiku, answer C on Codex, and only the clerk,
  bench, gate, minister and cabinet run on Sonnet. Not measured yet: Bob doesn't count tokens. The first
  live day will tell.

### What failed

- **Reaching the planned ending.** 7 of 14 days needed more than one round.
  - Two kinds of miss: "partly" cases that were too easy, and "rejected" cases where an answer dodged
    the bind.
  - Both lessons are now in the clerk and redo worker files.
- **Subagent limit.** Three days stopped at the session's limit of 20 subagents at once and were
  resumed.
- **One day discarded (23 Nov):** its real-news hook was a specific child-exploitation case. It was
  rerun on early release.
- **Not every day had its area in the news.** 15 and 22 Nov share the £2 bus cap from July; 23 Nov's
  story is from 10 Nov. The page says so.
- **The gatekeeper.** Rounds 1 and 2 were REVISE: AI disclosure, honesty about rewritten tests,
  unsourced baselines, and copy fixes. All were fixed.

### Still to check

- **The first daily run,** the first day after the merge: does the chain publish a day and a debate,
  and does the 15:00 UTC rebuild show it?
- **Whether the daily chain fits its slots.** A redo plus a second gate round needs both to land before
  the 13:55 jury.
