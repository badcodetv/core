---
engine: claude
model: claude-sonnet-5-5
effort: high
labels: role=demo,step=cabinet
include: demo
---
# Your step: the demo government's daily debate

Go on only if today's day is `published` and `$LIVE/docs/demo/government/<NEWS>.json` doesn't exist.
Earlier dates must already have their government file. If one is missing, say which and stop.

Read `$MAIN/docs/demo/cabinet.json` (the seven ministers and their voices), today's day, and the
manifestos as they stand: `$DEMO government $LIVE`.

Write `docs/demo/government/<NEWS>.json`:

```json
{"schema": "fp-demo-gov/1", "date": "<NEWS>", "day": "<day id>",
 "debate": [{"minister": "<area>", "text": "..."}],
 "changes": [{"op": "adopt|change|drop", "line": "<area>-<n>", "minister": "<area>", "text": "...", "why": "..."}],
 "made_by": {"workers": ["demo-cabinet"]}}
```

- **debate:** 2 to 5 short speeches, up to 400 characters each. The day's minister speaks first and says
  what happened and why. Others push back or connect it to their own area and lines. Each speech is in
  that minister's voice, with plain words and real disagreement.
- **changes:**
  - **Adopted or trial day:** exactly one `adopt` by the day's minister. The new line is
    `<area>-<next number>`, and its `text` (up to 240 characters) is the manifesto promise in plain
    words. A trial line says it is a trial.
  - **Sent-back day:** no adopt.
  - **Any day** may `change` or `drop` an existing line when today's day shows it was wrong or needs
    more. Only the line's own minister may do it. `why` names what today showed.
  - Don't change things for the sake of it. Most days change nothing else.
- Run `$DEMO validate` on the file and `$DEMO government $LIVE`. It must show no `skipped` line. Then
  commit and push.

Finish with one line: `<adopt line or "nothing adopted">; <n> other changes`.
