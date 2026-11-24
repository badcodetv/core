---
engine: claude
model: claude-haiku-5-5
effort: medium
labels: role=demo,step=jury
include: demo
---
# Your step: the jury (stage `jury`)

Go on only if the stage is `gate` and `ending` equals `plan.ending`. If they differ, stop with one line:
the day waits for `demo-redo`.

1. Run `$DEMO draw <id>`. Take `jurySeed` and `jury` (12 ids). Read them with `$DEMO people`.
2. Write one values question the marks can't settle (who pays, whose need comes first, what matters
   more), with 2 to 4 options a person could honestly choose.
   - **accepted:** the question can be about how to carry out the adopted answer.
   - **rejected:** which red line, if any, the town should be asked to rethink.
3. Go through the 12 jurors one by one: from each one's age, work, place and politics, decide how they
   would vote and why in a few words (keep these notes in `<id>.side.jury.json`). Then add up the votes.
4. Fill `jury`: `{seed, size: 12, ids, model, question, options, votes, ruling, reasons}`.
   - `ruling`: one sentence with the count, e.g. "The town pays, 8 to 4."
   - `reasons`: 2 to 4 jurors in their own words.
5. Set `stage: "jury"`, add `demo-jury` to `made_by.workers`, then validate, commit and push.

Finish with one line: `<ruling>`.
