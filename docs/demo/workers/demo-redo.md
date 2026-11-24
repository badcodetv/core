---
engine: claude
model: claude-sonnet-5-5
effort: high
labels: role=demo,step=redo
include: demo
---
# Your step: the second try (only when the marks missed)

Go on only if the stage is `gate` and `ending` differs from `plan.ending`. Otherwise say
`no redo needed` and stop. If `<id>.side.redo.json` already says `rounds: 2`, the day has had its
second try: say `<id> missed after two rounds` and stop. The day is not published.

You change inputs, never marks. Read the gate's notes and `<id>.side.clerk.json`, then:

- **Plan accepted, marks fell short:** rewrite the best answer so it does what the failing and unclear
  tests ask, within the case's facts. A minister's adviser fixing a draft.
- **Plan partly, marks gave accepted:** the case was too easy. Make the tension hard numbers in
  `case.story` that rule out one thing the citizens ask for, and add or sharpen that test, so a careful
  answer can keep every limit but not pass every test. Then bring each answer into line with the new
  facts without changing its approach.
- **Plan partly, marks gave rejected:** rewrite the best answer to keep within every limit.
- **Plan rejected, marks gave something else:** the case wasn't a hard enough bind. Tighten
  `case.story` so the bind is real (a fixed budget, a deadline, a rule), then bring each answer into
  line with the new facts.
  The bind only bites if it is a red line. If the citizens' must-have ("closes the whole gap", "no
  debt", "ready by the deadline") is only a `test`, make it a `limit`, so an answer that dodges the
  bind crosses a red line instead of just missing a test. Say so in `changed`.

Then:

- Write `<id>.side.redo.json`: `{rounds: <gate.rounds>, changed: "<one plain sentence>"}`.
- Add to `made_by.note`: `Round <n+1>: <what changed>.`
- Delete `gate` and `ending`, set `stage: "bench"`, add `demo-redo` to `made_by.workers`.
- Validate, commit, push. The gate's second round marks it again.

Finish with one line: `redo: <what changed>`.
