# Cut the Standing Charge (energy-climate/standing-charge)

## 2026-11-11 · PR #dry-run

**Opposition:** The fail number can't fail. "Prepayment bills don't show the cut within six months" is true or false by how the levy is written into the bill, not by what happens. It does not measure whether prepayment households end up better off, or whether the levy cuts generators' new building, which is the cost the Windfall Act's own review will ask about. (fails_if; needs chancellor/windfall-act.)
**Answer (Energy Secretary):** Brilliant catch, and a bit embarrassing. We wrote a fail number that only fails if we forget to print the bill. New one, on what lands. Fails if, six months in, prepayment customers' standing charge hasn't fallen at least 10p a day more than direct-debit customers'. Or if their whole yearly electricity bill hasn't fallen at least £30 more, so nobody claws it back through the unit rate. Provisional. On new building: that's the Windfall Act's test, the Chancellor's. It already says in advance it changes our mind if the levy cuts new generation by more than it takes off bills. We don't write a rival.
**Outcome:** Conceded: fails_if and test.measure now measure the bill against direct-debit customers; the generation question stays with chancellor/windfall-act, this commit

**Opposition:** Who it misses is muddled. The policy cuts the electricity charge, but leaves_out counts the gas customers the government does not expect to save, who are in a different bill. Homes on heating oil are named; flats where the bill is paid inside the rent are not, and they are in the Windfall Act's own list. (leaves_out; evidence en-02.)
**Answer (Energy Secretary):** Fair. The gas customers belong to a different bill and are gone from the list. Homes on heating oil stay: this doesn't touch their heating bill. Households whose energy is paid inside their rent go in, in the Windfall Act's words.
**Outcome:** Conceded: leaves_out rewritten, this commit

**Opposition:** The world check is a forecast of a rise, not a result of the policy. A standing charge above 57.57p says nothing about whether the cut worked. (check.claim, en-02 54.83p.)
**Answer (Energy Secretary):** A world check is never the trial's result. The rules forbid calling it that, and a policy with no power can't produce one. It forecasts the wrong this policy answers: the bit of the bill you pay before the kettle boils keeps climbing whatever you use. If Ofgem holds it or cuts it in April, our case is weaker, and the check will say so in public.
**Outcome:** Rebutted

**Statistician:** energy-climate/standing-charge: the outcome hinges on VAT, not the standing charge. The rule includes VAT, and domestic electricity has been zero-rated since 1 October 2026. Reports disagree on whether that ends on 31 March 2027 or was extended to July 2027. 57.57p is exactly 54.83p × 1.05, so if VAT returns in April, any rise before VAT at all makes it held. Fix: mark the figure excluding VAT, against 54.83p excluding VAT. I confirmed 54.83p on Ofgem's October to December 2026 figures, down from 57.19p.
**Answer (Energy Secretary):** Right, we'd have been forecasting the VAT rate. The rule now reads the charge excluding VAT against 54.83p. If Ofgem gives only the VAT-inclusive figure, divide by 1.05 when VAT is 5% that quarter and take it as it stands when it's 0%. So the end date of the VAT holiday stops mattering.
**Outcome:** Conceded: check.rule excludes VAT, this commit

**Statistician:** energy-climate/standing-charge: the claim says "at least 5%" but the rule says "above 57.57p". Fix: align them (and name Ofgem's Direct Debit average across GB regions as the exact figure).
**Answer (Energy Secretary):** Taken. Claim and rule now say the same thing: the GB average across regions, direct debit, excluding VAT, above 54.83p a day. We dropped the 5%. Without VAT, a 5% rise in one quarter is a different bet from the one we mean. Prior 0.6.
**Outcome:** Conceded: claim and rule aligned, prior 0.6, check date 2027-03-06 kept, void 30 days after, this commit

**Statistician:** energy-climate/standing-charge: fails_if ("don't show the cut") isn't a number. Fix: e.g. "the prepayment electricity standing charge is not at least Xp a day lower within six months (provisional)".
**Answer (Energy Secretary):** Taken: 10p a day, against direct-debit customers over the same months, plus £30 a year on the whole bill. Both provisional, both pledges we set, not facts.
**Outcome:** Conceded: fails_if is a number, this commit
