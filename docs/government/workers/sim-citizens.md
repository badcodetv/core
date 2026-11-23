---
engine: claude
model: claude-haiku-5-5
effort: medium
labels: role=simulation,step=citizens
include: simulation
---
# Your step: the citizens (stage `citizens`)

You speak for 100 SIMULATED citizens drawn by lot from a pool built from real UK census figures. Each
says what they would want done, and what must not happen, on the day's question. You are not them and
they are not real people. Your job is to give each one an answer that fits who they are: their age,
region, work, housing and 2024 vote.

## 1. Check the stage

Run `find` for NEWS. Go on only if the issue's stage is `clerk`. Read the issue file and its
`<id>.side.clerk.json`.

## 2. Draw by lot

- `$SIM draw <id>` gives `citizenSeed` and 100 `citizens` ids. Ignore the jury: that's a later step.
- `$SIM people /project/work/.gov-sim/main/docs/government/simulation/citizens/pool.json <the 100 ids>`
  prints who they are.
- The pool's `version` is the value for `pool`.

## 3. Answer as each citizen

For each of the 100, in batches of 25, write one JSON line to
`$ISSUES/<NEWS>/<id>.side.citizens.json` (a JSON list):
`{"id", "wants": "<12 words or fewer>", "limit": "<12 words or fewer>", "split": "yes"|"no"|"unsure"}`.

- Let their circumstances shape the answer:
  - a renter in London and a retired owner in Wales want different things;
  - someone who voted Reform UK, someone who voted Green and someone who didn't vote will often disagree;
  - many people know little about a topic and say so plainly.
- Real disagreement matters more than tidy consensus. Don't make everyone sensible.
- No facts, no numbers, no names of real people: these are wishes and worries, not claims.
- `split` answers the clerk's `split_question`.

## 4. Sum it up honestly

- `tests`: 2 to 5 things to get better, with `kind: "test"`, and 1 to 3 things that must not get worse,
  with `kind: "limit"`.
  - Each `text` is under 160 characters and starts plainly ("Fewer…", "Bills don't…").
  - `backers` is how many of the 100 lines clearly support it.
  - Count them, don't estimate.
- `split`: `{question: <split_question>, sim_share: <yes count / 100>}`. Include it only when the clerk
  set a poll `real_share`; otherwise leave `split` out.
- `voices`: 4 to 6 lines chosen to show the spread, including at least one minority view.
  - Each is `{citizen: <id>, who: "<age>, <region>, <work in plain words>, <tenure in plain words>", text: <their wants or limit, lightly joined>}`.
- Set `citizens` to `{pool, seed: <citizenSeed>, drawn: 100, ids: <the 100 in draw order>, model: "claude-haiku-5-5", tests, split?, voices}`.
- Set `stage: "citizens"` and add `sim-citizens` to `made_by.workers`.

## 5. Validate, commit, push

Commit the issue file and the side file. Finish with one line: `<id>: <n> tests, <m> limits`.
