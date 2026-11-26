# The review comes first (work-pensions/review-before-it-lowers)

## 2026-11-26 · PR #29

**Opposition:** The test lets DWP choose what counts as success. If its published aim were a lower bill, taking money from disabled people could pass. No number limits unmet needs or wrong refusals. Require a separate test of harm to claimants, fixed before anyone enters. (test.measure and fails_if.)
**Answer (Secretary of State for Work and Pensions):** Conceded. As written, a smaller bill could pass for a better benefit, and the DWP would mark its own homework. Now two harm measures are fixed before anyone enters: the share of decisions changed at reconsideration or appeal, and the share of people an independent reassessment finds with assessed needs their award leaves unmet. Either one a tenth or more higher than in areas like it, and it fails. Two quarters running past that line stop the trial early.
**Outcome:** Conceded: test.measure and fails_if carry the two harm measures and the early stop, edfad799

**Opposition:** The first area's claimants could lose money before the review everyone else is promised. The stop clause does not say their old awards return or lost payments are repaid if the assessment fails. Name these people in leaves_out and state when harm stops the trial and how losses are put right. (rule, stop and leaves_out.)
**Answer (Secretary of State for Work and Pensions):** Conceded. Somebody has to go first or nobody else gets a review, so the people who go first get the cover. If the trial fails or stops early, everyone in the first areas goes back to their old award, and every pound they lost is paid back. They're named in leaves_out, counted on their own line.
**Outcome:** Conceded: the body promises old awards back and losses repaid; leaves_out names the first areas' claimants, edfad799

**Statistician:** work-pensions/review-before-it-lowers: test.where now allows the trial "under ... the same power written into the Bill that replaces PIP", but test.by is still "the limit the pilot power sets", and that Bill hasn't been written yet, so the PIP route has no stated by-when. Fix: set test.by to "three years at most, the limit in section 41, written into the PIP Bill the same". The check is unchanged from origin/main, so the freeze holds, and it still tests what the policy argues.
**Answer (Secretary of State for Work and Pensions):** Taken as written: test.by now reads "three years at most, the limit in section 41, written into the PIP Bill the same". The world check is untouched.
**Outcome:** Conceded: test.by, edfad799
