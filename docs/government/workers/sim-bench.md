---
engine: claude
model: claude-sonnet-5-5
effort: high
labels: role=simulation,step=bench
include: simulation
---
# Your step: the bench, answers A and B (stage `bench`)

Two rival answers, each written blind, joined to answer C from the other AI model. You are the
organiser, not a writer: the writing happens in two subagents that never see each other or C.

## 1. Check the stage

Run `find` for NEWS. Go on only if the stage is `citizens` AND `<id>.side.rival.json` exists. If C is
missing, stop with one line: the bench needs two engines, so it won't run without C.

## 2. Write A and B blind

Start two subagents (the Agent tool) **in one message, in parallel**. Give each the same packet:

- the issue's `issue`, `poll` and `sources` blocks;
- `citizens.tests` and `citizens.voices`;
- the clerk's `angles`, `facts_for_writers` and `extra_sources`;
- the README's rules 1 to 5.

Give each one its own angle:

- **A, fix what exists:** keep today's owners and institutions, and change the rules, the referee, the
  money or the penalties.
- **B, change who runs it:** a structural change in who owns, runs or decides. This is the bolder one.

Ask each for JSON: `{title (≤70 chars), answer (≤120 words, plain), sources: [ids from the packet],
new_sources: [{title, publisher, date, url}] for pages it opened}`.

Don't tell either subagent about the other or about C. Don't edit their answers beyond trimming to the
length limits.

## 3. Join the bench

- Read `<id>.side.rival.json` for C.
- Any `extra_sources` an answer cites keep their ids and join `sources`. Give every new source (from A, B and C) the next free `sN` id, add it to `sources`, and swap the ids
  into the answers' `sources`.
- Set `bench` to `[A, B, C]`:
  - A and B: `engine: "claude"`, `model: "claude-sonnet-5-5"`, `blind: true`.
  - C: exactly as the rival wrote it.
- Write `<id>.side.bench.json` with the two subagents' raw replies, for the record.
- Set `stage: "bench"` and add `sim-bench` to `made_by.workers`.

## 4. Validate, commit, push

Finish with one line: `A: <title> / B: <title> / C: <title>`.
