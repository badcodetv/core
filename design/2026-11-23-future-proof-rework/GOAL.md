# Goal: the Future Proof simulation, one week old and running itself

Kai, 23 Nov 2026. Work autonomously. Don't ask questions unless a stop condition below is hit.
Branch: `future-proof/simulation`.

## Read first (this is the whole brief)

- `design/2026-11-23-future-proof-rework/README.md`: the design, Kai's decisions, the at-scale plan,
  guard rails and phases. It overrides anything older.
- `design/2026-11-23-future-proof-rework/future-proof-engine.html`: the loop animation, published
  privately at https://claude.ai/artifact/8JJXdfsxM8PBzCBH3iWCQo. Reuse its loop diagram to draw each issue.
- How the government runs today: `docs/government/README.md`, `docs/government/workers/`,
  `docs/government/policies/README.md`, `docs/government/schedules.json` and `scripts/government/`
  (Bob workers, sync, lint).
- `docs/rules/working.md`, `docs/voice.md`, `docs/marketing/the-reader.md`, `CLAUDE.md`.

## Done means all of these are true

1. **Data format.**
   - One JSON file per issue per day, holding:
     - the issue;
     - the borrowed real poll, if any;
     - the simulated citizens' tests;
     - three blind rival answers;
     - the gate table;
     - the jury question and vote;
     - the minister's read-out;
     - dated predictions;
     - sources.
   - A schema and a validator check it, with tests.
2. **Citizen pool.**
   - About 1,000 simulated UK residents, built from real ONS/census distributions, recorded with provenance.
   - Each run draws about 100 citizens and a jury of 12 by lot.
3. **Bob workers.**
   - Clerk, citizens, bench (on two different engines), gate, jury, minister and publish.
   - Together they run ONE issue a day from the real morning news, end to end, with no human step.
   - Added through `schedules.json` and `workers/`, the way the existing government is.
4. **Backfill.**
   - Seven replayed days, one issue each, from the real news of each of the past seven days.
   - Thames Water is one of the seven.
   - Every replayed issue is stamped "Replayed on <run date> from the news of <news date>".
   - Its predictions must resolve AFTER the run date, so nothing is scored with hindsight.
5. **Private page.**
   - Shows the feed of all issues, newest first.
   - Each issue opens to its loop animation and its detail.
   - Includes a scoreboard of predictions, honestly at zero marks.
   - Updates itself after each daily run with no human step.
   - Choose how it publishes and stays private: a republished private artifact, or an unlisted site route.
     An unlisted route is NOT private.
   - Write down which you chose and why.
6. **One PR to main** contains all of it.
   - Its description says, in plain English, what Kai's single merge switches on.
   - After Kai merges, verify that the first live daily run happened and published. That is the finish line.
7. **A short report.**
   - What runs when.
   - The measured cost of one day, in tokens or run time.
   - What failed.
   - What it takes to go from one to five issues a day.

## Hard rules (never break these, even to finish faster)

- Every card, page and image carries "SIMULATED".
- Simulated citizens are never called "the public". Show a real poll beside them where one exists.
- No claim about a real person or company without a published source. The gate rejects unsourced claims.
- Never put words in a real person's mouth.
- No hindsight scoring. Replayed predictions must resolve in the future.
- Changes to `docs/government/policies/` (the manifesto) still need a human merge. The simulation never edits them.
- Don't touch, merge or close the open PRs #29 (government rolling) and #22 (news trim).
- Post nothing publicly:
  - no badcode.tv pages linked from the menu;
  - no social posts;
  - no YouTube.
- Follow CLAUDE.md:
  - mark guesses as guesses;
  - write provenance for generated files;
  - rules go in the repo, not in memory.

## How to work

- **Order:**
  1. template (Thames Water by hand as the first data file, plus the page);
  2. schema, validator, tests;
  3. the citizen pool;
  4. workers;
  5. backfill the other six days;
  6. the PR;
  7. wait for the merge;
  8. verify the live run;
  9. report.
- **Keep a progress log** at `design/2026-11-23-future-proof-rework/build-log.md`: what's done, what's next,
  decisions. It lets the work survive context resets. Read it first if it exists.
- **Cost:** use the cheapest model that works for citizens and jurors. Measure the cost of the first full
  day before backfilling.
- **Backfill:** use subagents in parallel for the days. Review each one's output against the hard rules
  before accepting it.
- **Before the PR:** run the tests and the lint. Report failures plainly, with their output.

## Stop and ask Kai only if

- a hard rule can't be met;
- the private-publishing path is impossible both ways;
- one day's cost looks above about three times today's government run;
- a merge is needed (then say exactly what that merge switches on).

## Facts already found (23 Nov)

- **Backfill source.** Bob holds a `kind=news-digest` memory for every day from 12 to 23 Nov 2026, each
  with 31 to 58 items. Find them with `mcp__bob__memory_search`, label `kind=news-digest`; each item
  also exists as its own `kind=news` memory.
- **Bob's limits.**
  - Each Bob worker runs on one engine: `claude` or `codex`.
  - Today's government workers run on `claude-opus-5-5`, except `opposition`, which runs on Codex.
  - Workers push to GitHub with `bob-push` (a script that pulls with rebase, then pushes).
- **Unknown.** Whether a Bob worker can publish a claude.ai artifact. Test it before choosing the
  private-page path.
