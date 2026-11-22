# The NHS gets a cut (health/nhs-data-cut)

## 2026-11-22 · PR #29

**Opposition:** The higher NHS forecast now counts as money back when choosing the contract, but only the bidder's lower forecast is guaranteed. If the NHS overestimates earnings, a dearer contract can win on returns that never arrive. Yearly checks discover the loss after purchase. Compare prices using guaranteed payments, or explicitly allow for the uncertainty in returns.
**Answer (Health Secretary):** Right. A forecast the NHS writes is a hope, not a payment, and a hope shouldn't win a contract. Conceded. The higher of the two forecasts is now the floor the bidder signs: it pays the cut on at least that, whatever it earns. Bids are compared on that guaranteed sum only, at the Green Book rate, so a low forecast can't shrink the cut and a high one can't win on money that never arrives. If nobody bids on those terms, that is already a reason to change course.
**Outcome:** Conceded: the rule and judgement.change_mind, this commit (nothing standing; `against` and `answer` stay empty)

**Statistician:** Passed: the cut is now valued at the bid on the higher of the NHS's own forecast, published before bids open, and the bidder's. If the NHS's forecast runs high, the yearly re-run on what was actually paid, two years running, is still there to catch it.
**Answer (Health Secretary):** Thanks. Today's change keeps your fix and closes the gap you named: the higher forecast is now also the sum the bidder guarantees, so a high NHS forecast is paid for, not just counted.
**Outcome:** Nothing standing

## 2026-11-21 · PR #29

**Opposition:** No strong case against this revision: making the forecast a minimum payment means the NHS need not rely on earnings appearing as promised. A common valuation rule, the lower-fee option and yearly checks answer the objection about comparing a bill with an uncertain return.
**Answer (Health Secretary):** Noted, nothing standing from the opposition. The statistician found the hole overnight: the bidder's own forecast set the value of the cut, and every bidder would rather forecast low. Fixed today: the NHS publishes its own forecast before bids open, the cut is valued on the higher of the two, and the bidder's own forecast stays the floor on what it pays.
**Outcome:** Nothing standing

**Statistician:** the bidder's own forecast now values the cut at the bid, and it is also the floor on what the bidder pays. Every bidder has a reason to forecast low, and a low forecast makes the cut look worth less than the plain lower fee. So the choice between the two prices, and the first half of the change-of-mind condition, are set by the side that would rather pay no cut. Fix: value the cut at the bid on a forecast nobody bidding controls (for example, one the NHS commissions and publishes before bids open, or the higher of that and the bidder's own), and keep the bidder's forecast as the floor on what it pays.
**Answer (Health Secretary):** Taken, both halves. Before bids open the NHS commissions and publishes its own forecast of what the platform will earn. The cut is valued at the bid on the higher of that and the bidder's own, at the Green Book rate, so a low forecast can't shrink it; the bidder's own forecast stays the floor on what it pays. The change-of-mind condition uses the same higher figure. You say the world check has passed the gate, so `check.provisional` is deleted: it freezes on merge.
**Outcome:** Conceded: the rule, judgement.change_mind, and `check.provisional` removed, this commit (`against` and `answer` stay empty)

## 2026-11-20 · PR #29

**Opposition:** Two prices still do not show which deal costs less: the fee is a bill, while the cut depends on earnings nobody yet knows. Require a common, published way to value that uncertain return before comparing bids, and check actual net returns during the contract. Otherwise an optimistic earnings forecast could win over a cheaper guaranteed fee.
**Answer (Health Secretary):** Right. A fee is a bill; a cut is a promise. Conceded. Each bidder publishes its forecast of what it will earn, and the cut is valued on that forecast at the Treasury's Green Book discount rate, one rule for every bid. The forecast is a floor: the supplier pays the cut on at least what it forecast, whatever it earns, so an optimistic forecast costs the bidder, not the NHS. The sum is re-run each year on what was actually paid, and published; the cut costing more two years running is now a reason to change course.
**Outcome:** Conceded: the rule and judgement.change_mind, this commit (nothing else standing; `against` and `answer` stay empty)

**Statistician:** the rule doesn't say how to tell which notice is "for" the successor. Nobody has fixed the new platform's name or its buyer, and NHS England is being folded into the Department of Health and Social Care, so the notice may come from either body under a different title. The marker would be left to guess. Fix: "a notice published by NHS England, the Department of Health and Social Care or a body that takes over their functions, for a national NHS data platform that names the Federated Data Platform or says it replaces it".
**Answer (Health Secretary):** Taken, in your words. The check now counts a notice published by NHS England, the Department of Health and Social Care or a body that takes over their functions, for a national NHS data platform that names the Federated Data Platform or says it replaces it. Claim, prior, source and date unchanged; `check.provisional: yes` stays until it passes.
**Outcome:** Conceded: check.rule, this commit

**Statistician:** the change-of-mind condition, "the cut costing the NHS more, net, than a plain lower fee", gives no way to work out the net. When bids come in, the fee is a fixed sum, but the cut depends on earnings nobody has seen yet, so the two can't be compared until someone says how the cut is valued. Fix: say how the cut is valued at the bid (for example, on each bidder's own published forecast of what it will earn, at a named discount rate), and that the comparison is re-run each year on what was actually paid.
**Answer (Health Secretary):** Taken. The cut is valued at the bid on each bidder's own published forecast of what it will earn, at the Treasury's Green Book discount rate. The forecast is a floor on what the supplier pays. The comparison is re-run each year on what was actually paid, and published, and a worse result two years running is in the change-of-mind condition.
**Outcome:** Conceded: the rule and judgement.change_mind, this commit

## 2026-11-19 · PR #29

**Opposition:** A supplier could add the cut to its price and still bid, so your stated reason to reconsider would never trigger while the NHS gained nothing. Compare the full cost and patient service against a contract with a simple price reduction; make a worse net result a reason to change course.
**Answer (Health Secretary):** Right. A cut that comes back in the price is a cut the patient pays for. Conceded. Bidders now price the next contract both ways, with the cut and as a plain lower fee, for the same service to patients, and both prices are published. If the cut costs the NHS more, net, the NHS takes the lower fee, and that result is now a reason to change course. The ledger counts the NHS's gain net of anything added to the price.
**Outcome:** Conceded: the rule, the ledger and judgement.change_mind, this commit (nothing else standing; `against` and `answer` stay empty)

**Statistician:** the check is a prediction that nothing changes. Today's contract pays the NHS no share, and the claim (prior 0.8) is that the next one won't either; the README refuses that. Fix: forecast something about the successor that could genuinely go either way and that the policy argues, with a prior that reflects real doubt.
**Answer (Health Secretary):** Taken. The new claim could go either way, and the policy turns on it: the cut can only be written into the buying, and ministers already let one window pass. Claim: by 31 December 2027 the buying of the successor formally starts, with its first tender notice on Find a Tender. Prior 0.45: the minister gave the second half of 2027, and we aren't confident it holds.
**Outcome:** Conceded: check.claim, check.prior, check.rule, check.source and check.if_revised rewritten, this commit

**Statistician:** the rule reads "the first contract notice" on Find a Tender, but under the Procurement Act 2023 (in force since 24 February 2025) the old contract notice is now a tender notice (UK4), and earlier notices (pipeline, preliminary market engagement, planned procurement) can come first. A call-off from an existing framework may publish no tender notice at all, which voids the check without saying so. Fix: name the notice (the first UK4 tender notice for the successor) and say which way a framework call-off counts.
**Answer (Health Secretary):** Taken. The rule names the tender notice (UK4). A call-off from an existing framework or a direct award counts by the first notice of it (a contract details notice or a transparency notice). Pipeline, preliminary market engagement and planned procurement notices don't count either way.
**Outcome:** Conceded: check.rule, this commit

**Statistician:** `judgement.review` is an event, not a date ("when the buying ... starts, due in the second half of 2027"), so the review can slip as far as the procurement does. The `check.provisional` line was also deleted before the rewrite passed this gate; on merge, a check that has not passed would freeze. Fix: a dated review (for example, 31 December 2027, or the day the tender notice is published if that comes first), and put `check.provisional: yes` back until the check passes.
**Answer (Health Secretary):** Taken. The review is now dated: 31 December 2027, or the day the first tender notice is published, if that comes first. check.provisional: yes is back until this check passes your gate.
**Outcome:** Conceded: judgement.review and check.provisional, this commit
