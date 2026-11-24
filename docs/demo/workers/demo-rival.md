---
engine: codex
effort: medium
labels: role=demo,step=rival
include: demo
---
# Your step: answer C

Go on only if the stage is `citizens` and `<id>.side.rival.json` doesn't exist yet. Never open
`*.side.bench*` files or a `bench` field.

Read the case, `citizens.tests` and `citizens.voices`, and `<id>.side.clerk.json` (`angles[2]` is yours).

Write one concrete answer:

- `title`: up to 70 characters.
- `answer`: up to 120 words (the validator counts). Say what changes, who does it, who pays, and how you'd know it worked.
- Work from the case's own facts. Name no real person or company.

Save `<id>.side.rival.json` as
`{"id": "C", "angle": "<angle>", "title": "...", "answer": "...", "engine": "codex", "model": "<your model id>"}`.
Commit only that file, and push. Finish with one line: `C: <title>`.
