# The visit stays a person (health/the-visit-stays-a-person)

## 2026-11-14 · PR #29

**Opposition:** Giving saved hours to neighbours waiting is right. But your pass rule still requires hours per person to rise. A pooled average can fall when new recipients need shorter packages, without anyone losing care. Judge unmet assessed hours and existing recipients separately, so reaching more people cannot itself fail the trial.
**Answer (Health Secretary):** Right. I set a fail number that punishes the thing I asked for. The fail number is now total hours of care delivered per thousand residents: up by a tenth at two years, one in twenty at one year, wherever the hours went. Hours per person per week stays only for the people on the books on day one, on its own line, and it fails the trial if it falls. Nobody's care is quietly thinned to reach the next house.
**Outcome:** Conceded: test.measure, test.by and fails_if, this commit

**Opposition:** Following people after care ends fixes exits, not entry. Adding every new starter still lets the rule change who enters the admissions measure. Adding people with different hospital risks could produce the required fall without preventing admissions. Include people assessed and waiting at the start in both groups; report later starters separately.
**Answer (Health Secretary):** Yes. The group is fixed on day one: everyone with a package and everyone assessed and waiting, in both sets of councils, followed whether or when their care starts and after it ends. Later starters get a line of their own and don't count toward the admissions number.
**Outcome:** Conceded: test.measure, this commit

**Statistician:** The hours measure now fights the rule. Saved hours go first to people waiting, and each newcomer added to "hours of care per person per week" pulls the average down, so the trial can do exactly what it promises and fail both its one-year and two-year hours thresholds. Fix: measure total hours of care delivered per thousand residents (the rise of a tenth, and one in twenty at a year, then mean more care, wherever it went), and keep hours per person only for the people on the books on day one, so nobody's existing care falling shows on its own line.
**Answer (Health Secretary):** Taken as written. Same fix as the opposition's first point.
**Outcome:** Conceded: test.measure, test.by and fails_if, this commit

**Statistician:** The queue clause has no baseline and no margin. "More people assessed and waiting per thousand residents than in the councils waiting" compares levels, so a trial council that starts with a longer queue fails on day one, and any difference at all, however small, fails it. "Assessed and waiting" has no named record or definition either. Fix: compare the change from each council's own baseline, set a margin (for example, the queue in trial councils grows by more than a tenth relative to the councils waiting), and define the count (assessed as eligible, no package started, from the council's own care records, counted on a fixed day each quarter).
**Answer (Health Secretary):** Taken. Each council is measured from its own starting queue. It fails if the queue in trial councils grows by more than a tenth against the councils waiting. The count is people assessed as eligible with no package started, from each council's own care records, on a fixed day each quarter.
**Outcome:** Conceded: test.measure and fails_if, this commit

**Statistician:** The admissions group fills unevenly. Trial councils move people off the queue into care faster, so their "new starters" join the measured group sooner, and people who start care are not the people who stay on the books, so admissions per thousand can move because the group changed. Fix: put everyone assessed and waiting on day one into the fixed group alongside everyone with a package, and follow them all, whether or when their care starts; count later starters on a separate line.
**Answer (Health Secretary):** Taken. Same fix as the opposition's second point.
**Outcome:** Conceded: test.measure, this commit

## 2026-11-13 · PR #29

**Opposition:** Why must every saved minute lengthen an existing visit? Your cited Bristol study reports the same care with less travel. Test using saved time for unmet assessed needs too, while protecting existing care. Otherwise someone gets a longer visit while their neighbour gets none, and your test cannot tell whether that was the better choice.
**Answer (Health Secretary):** Fair. A longer visit for her while the woman next door waits with nothing is the wrong order. The hours the road gives back now go first to people assessed and waiting in that neighbourhood, then into longer visits. Nobody's existing care is cut to pay for it. The trial counts both: hours of care per person per week, and the queue. If the queue grows in trial councils against the councils waiting, it fails. What it can't do is run the two uses as separate arms side by side. That's on the policy as the best case against.
**Outcome:** Conceded in part: the rule sends saved hours to people assessed and waiting first; fails_if adds the queue; `against` and `answer` set, this commit

**Opposition:** Your admissions measure covers people receiving funded care. What happens to someone whose package ends? Without following them, fewer admissions could reflect who remains on the books. Longer visits also need not mean more care per person each week. Follow starting recipients after exit; publish missed visits, total care received and unmet need.
**Answer (Health Secretary):** Yes. Count the list and the list can flatter you. The group is now fixed on day one: everyone with a package, plus every new starter, each followed after the package ends through hospital records matched to council care records. Minutes per visit stays, beside hours of care per person per week, missed visits and people assessed and waiting. Published quarterly.
**Outcome:** Conceded: test.measure follows a fixed group and adds hours per week, missed visits and the queue, this commit

**Opposition:** Councils waiting their turn are promised the rule after the trial, without saying it must pass. As written, that allows expansion after failure. The stop clause also never explicitly ties expiry to the two-year review. Make later rollout conditional on passing, and specify when a failed rule ends and how existing care continues.
**Answer (Health Secretary):** Right, and it's the clause the people in the trial care about most. The councils waiting start only if it passes. It stops two years after the first council starts unless Parliament votes to keep it, on the published review. If it stops, nobody loses an hour on the way out: each person keeps the care they had.
**Outcome:** Conceded: stop names its date, the waiting councils start only on a pass, and the body promises no hours lost if it stops, this commit

**Statistician:** No size. Nothing says how many councils go first or how many sit in the comparison, and a one-in-ten fall in emergency admissions can't be told from chance across a handful. It is also unclear whether the comparison is the volunteers drawn by lot to go later or non-volunteer councils matched on size, deprivation and self-funder share. Fix: name the minimum number of councils in each group, and say the comparison is the volunteers drawn to go later, with the matching used as a check on them.
**Answer (Health Secretary):** Taken. At least twelve volunteer councils start first and at least twelve wait, drawn by lot. The volunteers waiting are the comparison. Matched councils that didn't volunteer are a check on them. Twelve is a floor. The review prints how many took part beside the result.
**Outcome:** Conceded: test.where and test.against name the groups and their floor, this commit

**Statistician:** The admissions count moves its own denominator. "People receiving council-funded home care" changes with the trial, because packages end, people die or go into care homes, so admissions per thousand can fall because the list changes. Fix: fix the group at the start (everyone with a package on day one, plus new starters), follow each person even after their package ends, and name the data: hospital admissions records (Hospital Episode Statistics) matched to council care records.
**Answer (Health Secretary):** Taken as written. Same fix as the opposition's second point.
**Outcome:** Conceded: test.measure, this commit

**Statistician:** Minutes per visit can rise while care falls. Merge two visits into one and the average goes up. The figure comes from the providers being judged, and providers on today's task-based contracts in the comparison councils may not record it the same way. Fix: add total hours of care delivered per person per week, take both figures from the council's electronic visit records, and take a baseline in both groups before the start.
**Answer (Health Secretary):** Taken. Two visits merged into one isn't more care, it's a longer gap. Hours per person per week is now the fail number, minutes per visit sits beside it, both from the councils' electronic visit records, baseline in both groups before the start. At one year, hours per person per week up by one in twenty or it's in trouble early.
**Outcome:** Conceded: test.measure, test.by and fails_if, with an interim measure at one year, this commit

**Statistician:** The stop gives no date. It says "stops on its date", but the file names none (test.by is "two years after the first council starts"). The comparison councils "get the rule after the trial" whether or not it passes. Fix: "Stops two years after the first council starts unless Parliament votes to keep it, on the published review", and make the comparison councils' turn depend on a pass.
**Answer (Health Secretary):** Taken word for word. See the opposition's third point.
**Outcome:** Conceded: stop, this commit

**Statistician:** The world check (still provisional, one rewrite allowed) tests a bystander fact. Acute delayed discharges measure people stuck on the way out of hospital. The policy argues that road time saved and spent in the visit keeps people out of hospital, and a rise or fall in discharge delays says nothing about that. The rule, source and revision clause are otherwise sound, and the prior of 0.55 is fine. Fix: predict something the policy argues. For example: the spring 2027 neighbourhood home-care guidance sets no requirement for where saved travel time goes, marked against the DHSC guidance page as it stands on the check date, with the rule naming exactly which wording would count as a requirement.
**Answer (Health Secretary):** Taken, and this is the one rewrite. Discharge delays are the way out of hospital; this policy is about where the saved time goes. New check: the DHSC's neighbourhood home-care guidance, due in spring 2027, sets no requirement on where the time saved on travel goes, read on GOV.UK as it stands on 31 July 2027. Held if no sentence tells councils or providers they must or should spend it on care (longer visits, more hours, or people waiting); failed if one does; void if no guidance is out by then. Prior 0.65. The provisional mark is off.
**Outcome:** Conceded: check rewritten, this commit
