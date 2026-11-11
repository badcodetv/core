---
id: chancellor/your-pension-votes
title: Your pension votes for you
line: Your pension owns the firms swapping jobs for machines. You should choose how it votes.
owner: chancellor
status: draft
kind: trial
needs: none
band: small
stop: Stops after two voting seasons unless Parliament votes to keep it, on the published review. Passes, and it goes national.
test.where: Nest, the state's own pension scheme
test.against: Nest members not drawn, whose votes are cast as today
test.measure: The share of members drawn by lot who choose how their votes are cast, and the cost to the fund
test.by: Two voting seasons
fails_if: Under 1 in 20 choose in two seasons, or it costs over 0.01% of the fund a year (provisional).
leaves_out: Anyone with no workplace pension; savers in other schemes until it goes national
signs: The Chancellor
check.claim: HMRC's first estimate of UK payrolled employees for April 2027 will be lower than its estimate for April 2026.
check.prior: 0.6
check.rule: The seasonally adjusted UK payrolled employees series in the ONS labour market release that first carries April 2027: April 2027 against April 2026 as printed in that same release. Lower: held.
check.source: ONS Labour market overview, UK (HMRC PAYE Real Time Information, payrolled employees)
check.if_revised: The release that first carries April 2027 counts; later revisions change nothing. If it is not published by the check date, the check is void.
check.check_on: 2027-05-31
check.result: pending
---
Your pension owns shares in firms swapping jobs for machines; someone else casts its votes.

Who decided. The schemes and the fund managers they hire, who vote your shares at every annual
meeting without asking you.

The rule. Nest, the state's own scheme, goes first: job-cutting votes published within a month,
and members drawn by lot choose how theirs are cast.

The ledger. Small: the cost of publishing the votes and asking the members. Members gain a say over
the firms their savings own.
