# Test every law before you live in it (prime-minister/test-every-law)

## 2026-11-11 · PR #dry-run

**Opposition:** The change-our-mind test is rigged to pass or fail by selection. "Bills that published a test fare no better than bills that didn't": but ministers choose which bills carry tests, and will pick the easy ones. Nothing here says the comparison is drawn by lot or matched. (judgement.change_mind.)
**Answer (Prime Minister):** Every new bill carries a test, so no minister picks. The old wording invited the reading anyway, because it compared bills that did with bills that didn't. Now it compares bills under the rule with the last parliament's, matched by department, both judged by one independent office against the aim each bill stated when it was introduced. That isn't drawn by lot. A rule for every law can't be.
**Outcome:** Conceded: judgement.change_mind rewritten as a matched comparison with the parliament before, this commit

**Opposition:** The 8% figure is stretched. The source is a 2019 review of major-project spending, reported by the NAO in 2021, graded B. The body uses it to say that the rules that set your wage and benefit have no test. Projects are not laws. (evidence pm-05.)
**Answer (Prime Minister):** Correct. Projects are not laws. The body now says so and uses the figure only for what it shows: even where the state spends, it seldom plans to check. The unsourced "none has a test" is gone.
**Outcome:** Conceded: body rewritten; the 8% is labelled as projects, not laws, this commit

**Opposition:** The world check is close to a safe bet. The NAO publishes reports of this kind often, so "at least one in five months" at 0.75 barely risks anything, and it does not show a published test improves a law. (check.claim, check.rule.)
**Answer (Prime Minister):** Agreed. Withdrawn and replaced (see the statistician's second point).
**Outcome:** Conceded: check rewritten, this commit

**Statistician:** prime-minister/test-every-law: this is a safe bet. The NAO publishes dozens of value-for-money reports in five months, and "could not show whether it met its objectives" is a routine finding. My probability is above 0.9, so a stated prior of 0.75 understates it, and the check is refused.
**Answer (Prime Minister):** Refusal accepted. Withdrawn.
**Outcome:** Conceded: the NAO check is gone, this commit

**Statistician:** prime-minister/test-every-law: the rule needs the marker's judgement ("inadequate", "could not show") and tests the existing wrong, not the policy's claim that bills could publish their tests before debate. Fix: count from the bill pages on bills.parliament.uk, e.g. "of government bills given a Commons second reading between 1 December 2026 and 30 April 2027, at least half will have no impact assessment published before second reading", with an honest prior.
**Answer (Prime Minister):** Taken. The rule is now a count, read off each bill's publications page: an impact assessment dated on or before the Commons second reading, or not. Prior 0.4. We expect most bills do publish one, and we're putting that on the record against our own argument. If none reaches second reading in the window: void.
**Outcome:** Conceded: check rewritten as a count from bills.parliament.uk, prior 0.4, check date 2027-05-10 kept, this commit

**Statistician:** prime-minister/test-every-law: judgement.change_mind says "fare no better at their review" but names no figure. Fix: say fare on what, e.g. the share that met their own stated test.
**Answer (Prime Minister):** Taken. On the share that meet the aim they stated when introduced.
**Outcome:** Conceded: judgement.change_mind names the share, this commit
