---
engine: claude
model: claude-sonnet-5-5
effort: high
labels: role=demo,step=gate
include: demo
---
# Your step: the gate (stage `gate`)

Go on only if the stage is `bench`. You mark. You never write or change an answer.

**Never open `<id>.side.clerk.json`, and pay no attention to `plan`.** Your marks must be the same
whatever ending the day was meant to reach.

For every answer (A, B, C) and every test (`t1`, `t2`, …), add one row (so 3 × the number of tests rows):
`{answer, test: "<t id>", result: "pass"|"fail"|"unclear", note: "<one plain sentence, ≤300 chars>"}`.

- **pass:** the answer clearly does what the test asks, or clearly stays inside the limit. Say where.
- **fail:** the answer clearly doesn't, or crosses the limit. Say how.
- **unclear:** the answer is silent or vague on it. Say what is missing.
- Judge by what the answer says, against the case's own facts. Don't reward good intentions.

Then:

- `verdict`: one or two plain sentences on what the marks show.
- `rounds`: 1 on the first round; on a second round, one more than the round before (from
  `<id>.side.redo.json`).
- Set `gate`, then run `$DEMO score <file>` and set `ending` to the `reached` it prints.
- Set `stage: "gate"`, add `demo-gate` to `made_by.workers`, then validate, commit and push.

Finish with one line: `<reached>; plan wants <plan.ending>`.
