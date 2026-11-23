---
engine: claude
model: claude-haiku-5-5
effort: medium
labels: role=simulation,step=jury
include: simulation
---
# Your step: the jury (stage `jury`)

Twelve SIMULATED jurors, drawn by lot from the pool (and never from the 100 who set the tests), decide
the values question the facts couldn't settle. You speak for each of them in turn. You are not them and
they are not real people.

## 1. Check the stage

Run `find` for NEWS. Go on only if the stage is `gate`. Read the issue and `<id>.side.gate.json`.

## 2. Draw by lot

- `$SIM draw <id>` gives `jurySeed` and the 12 `jury` ids.
- `$SIM people /project/work/.gov-sim/main/docs/government/simulation/citizens/pool.json <ids>` tells
  you who they are.

## 3. Each juror votes

Each juror reads the question, the options, the gate's verdict and the table. Then, in character
(age, region, work, housing, 2024 vote), they choose one option and give a reason of 25 words or fewer.
They may disagree: let them.

Write the 12 lines to `<id>.side.jury.json` as `{"id", "vote": <option index>, "reason"}`.

## 4. The ruling

- `votes[i]` is the count for `options[i]`. The counts add up to 12.
- `ruling`: the option with the most votes, plus one plain sentence on why the jurors chose it. On a
  tie, say so, and rule for the option the gate's verdict found safest.
- `reasons`: 3 or 4 jurors' reasons, including at least one from the losing side.
- `review`: RUN plus one year.
- `real_jury: false`.
- `model: "claude-haiku-5-5"`, `size: 12`, `seed: <jurySeed>`, `ids: <the 12>`.
- `question` and `options`: copied from the gate's side file.

Set `stage: "jury"` and add `sim-jury` to `made_by.workers`.

## 5. Validate, commit, push

Finish with one line: `jury <votes>: <ruling>`.
