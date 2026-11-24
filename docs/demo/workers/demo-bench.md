---
engine: claude
model: claude-sonnet-5-5
effort: high
labels: role=demo,step=bench
include: demo
---
# Your step: answers A and B (stage `bench`)

Go on only if the stage is `citizens` and `<id>.side.rival.json` exists. Don't read answer C until A and
B are written.

Read the case, `citizens.tests` and `citizens.voices`, and `<id>.side.clerk.json` (`angles[0]` is A's,
`angles[1]` is B's). Write each answer on its own, from its own angle:

- `title`: up to 70 characters;
- `answer`: up to 120 words (the validator counts), saying what changes, who does it, who pays, and how you'd know it worked;
- work from the case's own facts, and name no real person or company.

When the plan's ending is **accepted**, write answer A to meet every test and keep within every limit,
plainly and point by point, as a careful minister's adviser would. Otherwise, write each answer as its
angle honestly leads. Don't aim to fail.

Then merge C from the side file. Set `bench` to the three answers, each with `id`, `angle`, `title`,
`answer`, `engine` and `model`. Set `stage: "bench"`, add `demo-bench` (and `demo-rival`) to
`made_by.workers`, then validate, commit and push.

Finish with one line: `A: <title> | B: <title> | C: <title>`.
