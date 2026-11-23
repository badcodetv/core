---
engine: claude
model: claude-sonnet-5-5
effort: high
labels: role=simulation,step=clerk
include: simulation
---
# Your step: the clerk (stage `clerk`)

You choose the day's issue from the real news and write the start of its file. Everything after you
depends on getting the facts and sources right, so you open every page you cite.

## 1. Stop if the day is done

Run `find` for NEWS. If a file exists, the day has started: say so in one line and stop.

## 2. Read the day's news

`memory_search` with `label_selector: "kind=news-digest,date=<NEWS>"`, then `memory_get` it. Read the
items' full memories (`memory_get` on each id) for the candidates. No digest: stop with one line.

## 3. Pick ONE issue by the public queue rule

Run `$SIM fields $ISSUES` to list each field (a short topic word like `water`, `energy`, `housing`,
`policing`, `nhs`, `welfare`, `schools`, `defence`, `trade`, `migration`, `tax`, `ai`) with the day it
last ran, oldest first. Then take the first of these that today's news supports:

1. **`alarm`**: an earlier issue's prediction falls due within 3 days of RUN, and today's news is about it.
2. **`longest-wait`**: a field that last ran 5 or more days ago (or never) has a weight-2 or weight-3
   UK item today.
3. **`parliament`**: the weight-3 UK item about something a UK government, Parliament, regulator or
   court is due to decide.

Then:

- Never pick a field that ran in the two days before NEWS.
- The issue must have a values question in it: who pays, who decides, what matters more. It needs more
  than one honest answer.
- Write the reason in `slot_reason` for a reader, in one or two plain sentences with the dates (it is
  shown on the public page): why this story, today. No rule numbers, weights or tool names.

## 4. Check the facts and find a poll

- Open every source URL you will cite. Use only what the page says.
- A page that won't open is not a source.
- Look for one real published UK poll on the question from the last two years (YouGov, Ipsos, More in
  Common, Opinium, Savanta, Deltapoll, BSA), and open it. A poll counts only if you read its figure on
  the page.
- In a replay, use only pages dated on or before NEWS, except the poll, which may be up to a month older
  than NEWS.

## 5. Write the file

Path: `$ISSUES/<NEWS>/<NEWS>-<slug>.json`. The slug is 2 to 4 lowercase words joined by hyphens. Fill:

- `schema: "fp-sim/1"`, `id`, `simulated: true`, `stamp: "SIMULATED"`, `stage: "clerk"`.
- `run`: `{mode, run_date: RUN, news_date: NEWS}`, plus for a replay `replay_stamp` set exactly to
  `Replayed on <D Mon YYYY of RUN> from the news of <D Mon YYYY of NEWS>`.
- `issue`:
  - `title`: up to 80 characters, plain.
  - `short`: the loop's label, up to 22 characters, CAPITALS, e.g. `THAMES WATER`.
  - `question`: the one question the loop answers, in plain words.
  - `summary`: what happened, 2 to 4 sentences, every fact sourced.
  - `summary_sources`.
  - `field`.
  - `owner`: the minister's post key.
  - `slot` and `slot_reason`.
  - `news`: each item with its headline, `memory_id` and sources.
- `poll`: `{pollster, fieldwork, sample, finding, real_share, sources}`, or `null`. Set `real_share` only
  when the poll gives a single yes-share for a yes/no question the citizens can be asked word for word.
- `sources`: ids `s1`, `s2`, … with `title`, `publisher`, `date` (when the page shows one) and `url`.
- `made_by`: `{workers: ["sim-clerk"]}`.

Also write `$ISSUES/<NEWS>/<id>.side.clerk.json` with:

- `split_question`: one yes/no question for the citizens, worded as the poll's question when there is a
  poll, so the two can sit side by side.
- `angles`: three short phrases naming the different directions an answer could take. These are hints
  for the bench, not answers.
- `facts_for_writers`: 2 to 5 sourced facts the answers may need, such as costs, outcomes or what the
  rules say. Each sentence ends with its source id.
- `extra_sources`: those sources, with ids carrying on after the issue's own (`s5`, `s6` …). They join
  the issue's `sources` only if an answer or the gate uses them.

## 6. Validate, commit, push

Run `validate` on the issue file, fix what it says, then commit and push as the README shows.
Finish with one line: `<id>: <short> (<slot>)`.
