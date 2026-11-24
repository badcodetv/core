---
engine: claude
model: claude-haiku-5-5
effort: medium
labels: role=demo,step=citizens
include: demo
---
# Your step: the citizens (stage `citizens`)

Go on only if the stage is `case`.

1. Run `$DEMO draw <id>`. Take `citizenSeed` and `citizens` (100 ids). Read a sample of 20 of them with
   `$DEMO people <ids…>`, so their ages, jobs and places shape what they ask for.
2. Read the case and `<id>.side.clerk.json` (`tests_hint`).
3. Write `citizens`:
   - `pool: "pool-2026-11-23"`, `seed`, `drawn: 100`, `ids`, `model`.
   - `tests`: 3 to 6 items, ids `t1`, `t2`, …. Each has a `kind`:
     - `test`: something a good answer must do;
     - `limit`: a red line it must not cross.
     At least one of each. Each `text` is under 160 characters and checkable from what an answer says,
     e.g. "Says who pays and how much", not "Makes things better". Make them demanding, as real
     people would: name a number, a date, a person to call, a group that mustn't lose out. On any
     day, a quick or vague answer should miss at least one; only a careful answer passes them all. `backers` is how many of the 100 back
     it (your honest estimate from who they are).
   - `voices`: 2 to 6 short quotes from drawn citizens. `who` is a plain description ("a bus driver,
     50s, Fernbridge"). Each answers the question in their own words, with no claims about groups.
4. Set `stage: "citizens"`, add `demo-citizens` to `made_by.workers`. Validate, commit, push.

Finish with one line: `<n> tests, <m> limits`.
