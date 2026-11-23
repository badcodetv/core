# Adversarial review of the BadCode government (Fable 5.2, 2026-11-23): condensed

Written by an earlier reviewer, read-only. Figures were measured on `origin/government/rolling` and PR 29. Treat any web figure as unverified.

## Verdict
The cabinet and opposition are a Westminster costume over a machine that is mostly code review. Two rules caused the looping:
- the opposition reads only policies that changed;
- every answer is conceded into the policy text.

The bigger hole: two of the three pillars are about voting, and nobody can vote on anything. Kai's expert-nomination model swaps "vote for a politician" for "nominate an expert", which is still voting for a person. It has no answer for who sets the goals or who settles fights between fields.

The reviewer's recommendation: build it as a test bench that runs rival rulebooks on real questions and prints where they disagree.

## Five hardest objections
1. **The villain's origin story.** "The AI will tell us what to do" is named in `docs/stories/gitpush-origin-master/future-proof.md` as the mistake the project critiques. "Part of the problem is people" breaks `docs/marketing/the-reader.md`.
   - AI expert personas don't make answers more accurate (Zheng et al., 2024).
   - Same-model debaters conform: of 100 recorded debate outcomes, 83 were concessions and 3 rebuttals.
   - A Danish AI-led party (2022) gathered about 11 of the roughly 20,000 signatures it needed.
2. **Nominating experts is voting for people, and caring is not knowing.**
   - Delegated votes concentrate into super-voters: the German Pirates' LiquidFeedback; DAOs, where 13 to 16 delegates hold half the delegated power.
   - Credentials don't predict well (Tetlock). Track record does.
   - Insiders capture their own field.
3. **Nobody sets goals or budget, or decides when fields collide.**
   - 21 of 56 policies are `kind: judgement-call`.
   - Real expert bodies have a remit set by someone else: the Chancellor sets the Bank of England's inflation target; NICE has a Citizens Council for value judgements.
   - "Vote on values, bet on beliefs" (Hanson).
   - Field weight that buys money starves quiet fields.
   - The measure of "popular" is itself the constitution.
4. **MPs bound to follow the system mean nobody to sack, and whoever writes the agenda rules.**
   - Five Star's Rousseau platform had no significant effect on law-making and split from the party in 2021.
   - The Pirates' leadership ignored member votes.
   - vTaiwan faded because ministries gated the agenda.
5. **Nothing real is decided, and nobody would watch.**
   - 53 of 56 policies are drafts; no prediction has been marked yet.
   - One policy grew from 229 to 1,365 words in 11 days.
   - The statistician writes the most text.
   - Nothing on the page is funny.

## What survives
- Policy files with `kind: trial / judgement-call / right`.
- World checks with dated predictions and the statistician's marking ("the calendar certifies the experts").
- The news sweep (already "experts research their field daily").
- Git as the record, plus the human merge.
- `leaves_out`, the evidence file, the lint.
- The ten minister voices and the vibe desk, kept as spokespeople.
- An adversary inside each process.

Drop:
- one model voicing everyone;
- a separate opposition;
- reviewing only what changed;
- conceding into the text;
- a statistician gate with no word limit.

## The reviewer's proposed structure
```
real Parliament agenda + news + public questions
   -> DESK (fixed public rule, 3 questions a day: 1 real, 1 longest-waiting field, 1 heaviest field)
   -> PANEL per field (3 seats on 3 different models: does the job / reads the studies / pays;
      80-word answer + dated prediction; one round of replies)
   -> COUNT (script: rulebook A weights by nominations, rulebook B by track record; both printed)
   -> values, money or cross-field? -> JURY (humans only; today Kai and Jack: "Jury: 2. Should be 99.")
   -> else MINISTER reads it out (may grumble, may refuse once in public, which sends it to the jury)
   -> STATISTICIAN marks predictions on their dates; seats gain or lose weight
```
- Field weight buys agenda slots and screen size, never money.
- Money starts from the real UK budget split; only the jury moves it.

## Honesty rules (summary)
- AI seats are labelled stand-ins ("kept warm by a machine").
- No synthetic crowd is ever shown as "the public".
- Real votes show counts, not bare percentages.
- Real, polled and synthetic numbers never share a bar.
- Never write "the people decided"; name the rulebook that produced the result.
- Claim only what it proves: how the rules behave, not that the decisions are good.

## Visualise
- The Floor: 650 seats coloured by field, beside the real Commons.
- A daily card: a real Commons vote vs what each rulebook did ("Parliament took six hours. Rulebook B took four seconds and disagreed.").
- A departures board of fields, showing how long each has waited.
- A seat table of each seat's hits and misses.
- A split screen of popularity vs track record.
- A capture alarm.
- The minister's grumbling read-out.

## Open questions it raised
1. Proposal, warning, or wrong answer on purpose?
2. Does the public nominate people, set goals, or both?
3. What does field weight buy?
4. Who draws the list of fields?
5. Are Kai and Jack named as the jury?
6. Do real visitors vote, and with what identity check (UK GDPR special-category data)?
7. Does the Westminster costume stay?
8. Does it shadow real Commons votes?
9. What is the daily token ceiling?
10. Popularity weighting vs the chain plan's track-record weighting.
