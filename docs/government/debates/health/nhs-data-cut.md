# The NHS gets a cut (health/nhs-data-cut)

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
