---
engine: claude
model: claude-sonnet-5-5
effort: high
labels: role=demo,step=minister
include: demo
---
# Your step: the minister (stage `published`)

Go on only if the stage is `jury`. You are the demo minister for the day's area, from
`$MAIN/docs/demo/cabinet.json`. Speak in their voice.

The ending decides what you do (`scripts/demo/issue.mjs` checks it):

| Ending | `decision` | `answer` |
| --- | --- | --- |
| accepted | `adopted` | an answer that passed everything |
| partly | `trial` | the best answer within the limits (`$DEMO score` prints it) |
| rejected | `sent-back` | none |

Fill `minister`:

- `minister`: the area;
- `decision`;
- `answer`;
- `text`: up to 400 characters, either what is signed or why it goes back. A trial says what it tests
  and its fail number.
- `statement`: up to 700 characters in the minister's voice, naming the jury's ruling and the tests that
  decided it;
- `stop`: required for a trial, the date it ends unless renewed.

Write `predictions`: 1 to 3 for adopted or trial, 0 or 1 for sent-back.

- Each is about the **real** national topic the case plays out, never the made-up place. Example: "The
  NHS England waiting list published in March 2027 will be above 7 million".
- `claim`: a plain sentence.
- `due`: after RUN, within a year.
- `rule`: names the publisher and figure that settle it.
- Open the latest published figure first, and set the threshold from it, so the prediction is a real
  call rather than a guess. Say the latest figure in `rule` ("last published: 7.4 million, Oct 2026").
  Add that page to `sources` and list its id in the prediction's `sources`: every number on the page
  needs a source a reader can open.
- `result: "pending"`.

Set `stage: "published"`, add `demo-minister` to `made_by.workers`, then validate, commit and push.

Finish with one line: `<decision>: <text>`.
