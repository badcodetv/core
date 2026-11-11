# A say before the saving (work-pensions/a-say-before-the-saving)

## 2026-11-11 · PR #dry-run

**Opposition:** The measure counts the survivors. "Workers' pay and hours" in trial firms: anyone who is let go is no longer a worker in the trial, so a firm that cuts forty jobs and pays the rest 5% more passes. Displaced workers are not in leaves_out either. Count everyone who was in the firm on day one. (test.measure, fails_if, leaves_out.)
**Answer (Secretary of State for Work and Pensions):** Yes. That's the exact trick this policy exists to stop, and we nearly built it into our own scoreboard. Now we count everyone on the payroll the day the firm joins. We follow them wherever they work after, through HMRC's records, and count nought for anyone out of work. The forty count. People let go before their firm signs up get no say, so they go on the leaves-out list by name.
**Outcome:** Conceded: test.measure and fails_if count everyone on day one; leaves_out adds people let go before their firm signs up, this commit

**Opposition:** A volunteer firm is not a typical one. Firms that agree to share the saving with their workers, even drawn by lot among volunteers, are the ones least likely to automate hard. The trial may show a rule works for firms that didn't need it. (test.where.)
**Answer (Secretary of State for Work and Pensions):** Both sides of the trial are volunteers, drawn by lot, so the comparison inside it is fair. Volunteers against volunteers, matched on sector, size and their automation plans. And the policy is binding only where employers sign up. The trial measures it as it would actually run. Whether it holds for the firm that would never sign is a real question. It's the one Parliament weighs before this becomes law, and the review has to say so out loud. We've put it on the policy as the best case against.
**Outcome:** Rebutted

**Opposition:** The world check follows the economy, not the policy. Payrolled employees were already down 111,000 on the year to August 2026; employer National Insurance (15% above £5,000) and the oil price move that figure as much as any say over automation. (evidence wp-01, ch-06, A.)
**Answer (Secretary of State for Work and Pensions):** Agreed. The payroll count goes up and down with the economy, whatever any board decides. Withdrawn. The new check asks firms what their own AI did to their headcount.
**Outcome:** Conceded: check rewritten (see the statistician's first point), this commit

**Statistician:** work-pensions/a-say-before-the-saving: the forecast is a bystander fact. The UK payroll count moves with the cycle, employer NICs and the minimum wage, so a fall can't be tied to automation or to whether workers had a say, and a rise argues nothing against the policy. Fix: forecast automation's effect on staff directly, e.g. the share of firms using AI that report it cut their headcount, in a named ONS Business Insights and Conditions Survey wave (confirm the question runs in that wave before writing it). The current rule is otherwise well frozen; if kept, say the flash estimate counts.
**Answer (Secretary of State for Work and Pensions):** Taken. The survey asks firms what AI did to their overall workforce headcount; we checked it is on the questionnaire. The claim: among AI-using firms with ten or more staff, the share saying AI reduced their headcount is higher in the last wave asked by March 2027 than in the last wave asked by March 2026. Both are read on the same day, to the decimal place the ONS gives. Equal or lower: failed. Prior 0.5. If neither window has the question, void. Check date 2027-05-14. We can't promise the question runs in a given wave months ahead, so the rule takes the latest wave asking it before each date, not a wave number.
**Outcome:** Conceded: check rewritten, this commit

**Statistician:** work-pensions/a-say-before-the-saving: test.against "firms like them" doesn't say how they are alike, test.measure names no figure for pay, hours or investment, and test.by "two years" has no start. Fix: matched on sector, size band and automation plans in the Transition Count. Use pay and hours from HMRC RTI for those firms and capital spending from their accounts, two years from the first firm's start.
**Answer (Secretary of State for Work and Pensions):** Taken as written. Pay and hours from HMRC's records follow the people, not the firm (see the opposition's first point).
**Outcome:** Conceded: test.against, test.measure and test.by filled, this commit

**Statistician:** work-pensions/a-say-before-the-saving: there is no band field, and the lint passes it because policy-lint.mjs never checks band (the README treats band as required for every policy). Fix: add a band, and make the lint require it.
**Answer (Secretary of State for Work and Pensions):** Band added: small. The public pays for running the trial, and the saving moves from the firm to its people. The body now carries the ledger. The lint is not ours to touch: it changes by a human PR, and we've flagged it for Kai and Jack.
**Outcome:** Conceded: band: small and a ledger paragraph; the lint change is left for a human PR, this commit
