# The Roof Comes with the Arrival (home/the-roof-comes-with-the-arrival)

## 2026-11-11 · PR #dry-run

**Opposition:** The trial tests the wrong half. The headline rule is a cap on work visas tied to homes, GP and school places. The trial only gives volunteer councils the roof money first and measures GP and housing waits against councils like them. Nobody trials the visa link, so a pass says money helps, not that the rule works. (test.where, test.measure, line.)
**Answer (Home Secretary):** The visa number is one national figure. You can't issue Darlington a different one from Doncaster. So it can't be tried in two towns, and we don't pretend it can: MPs vote on it once a year, in public. What can be tried is the roof the link rests on: does money arriving first shorten the queue? If it doesn't, the link ties the number to nothing, and we'll say so. The body now says this plainly.
**Outcome:** Rebutted (the body now says the cap can't be tried in two towns, this commit)

**Opposition:** "Band: none" can't be right. The rule says the roof money is paid first, from the cost of closing asylum hotels. But 16,021 people were in hotels at end June 2026, half the year before: the saving is already shrinking as hotels close. Where does the money come from in year two? (evidence home-08, gov.uk, A.)
**Answer (Home Secretary):** Right on both counts. Homes, GP and school places for every work-visa arrival is not "none". It's large, over £1bn a year once national. That's an order of magnitude, not a costing. And the hotel money is the first payment, not the last. 16,021 at end June, half the year before. After it, MPs vote the roof money together with the number. No money voted, no rise in the number.
**Outcome:** Conceded: band: large; the body says where the money comes from after the hotels, and has a ledger, this commit

**Opposition:** A word dropped. The advisers' 5% and 4% are nominal wages, 1993 to 2017; over the same period real wages at the 5th percentile rose 55%. The body says "pay". (evidence home-10, A.)
**Answer (Home Secretary):** Correct, and it's the proportion we're for. Nominal pay about 5% lower at the bottom. Over the same years, real pay at the bottom rose 55%. Both are now printed.
**Outcome:** Conceded: body says nominal and adds the 55%, this commit

**Statistician:** home/the-roof-comes-with-the-arrival: 171,000 is the ONS's own provisional figure for the year ending December 2025 (published 21 May 2026), so this predicts that the fall since 2023 continues. The release is due within weeks and the Home Office visa figures for that year are already out, so it is close to knowable. That breaks the "status quo continues" rule.
**Answer (Home Secretary):** Accepted. Withdrawn.
**Outcome:** Conceded: the net migration check is gone, this commit

**Statistician:** home/the-roof-comes-with-the-arrival: the forecast doesn't test the policy. The level of net migration doesn't test whether homes, GP places and school places keep pace with arrivals, or the policy's funding source (closing asylum hotels). Fix: forecast the money, e.g. the number of people in asylum hotels in the Home Office's quarterly immigration statistics at the end of March 2027 being below a stated N, or housing completions against work-visa grants.
**Answer (Home Secretary):** Taken, with the date moved. End March 2027 is published after May, too late for this minister's six-month check. So: people in asylum hotels at the end of December 2026, in the quarterly release that first carries it, below 12,016. That's three quarters of the 16,021 at end June 2026. A year-on-year halving would come in under it, and a stall wouldn't. Prior 0.55. Held means the first source of roof money is real and growing. Failed means it's thinner than we say.
**Outcome:** Conceded: check rewritten, check date 2027-03-15, this commit

**Statistician:** home/the-roof-comes-with-the-arrival: if_revised voids only if nothing is published by 2027-03-31, but the marking rule voids 30 days after check_on (2027-01-14). Fix: pick one date in the rule.
**Answer (Home Secretary):** Taken. One date: void if it isn't published 30 days after the check date.
**Outcome:** Conceded: check.if_revised follows the 30-day rule, this commit

**Statistician:** home/the-roof-comes-with-the-arrival: test.against "councils like them" doesn't say how they are alike, and "GP and housing waits" names no figure. Fix: matched on population, deprivation decile and visa arrivals per head. Measure NHS England Appointments in General Practice (share seen within two weeks) and households on the housing register (MHCLG local authority housing statistics).
**Answer (Home Secretary):** Taken as written. The councils not drawn get it after the trial, so none gets less than today. The fail number follows the new figures: a tenth better on each.
**Outcome:** Conceded: test.against, test.measure and fails_if name the match and the figures, this commit
