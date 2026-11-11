---
id: health/the-time-goes-to-the-bed
title: The time goes to the bed
line: Every hour a machine saves goes to patients, or the contract isn't renewed.
owner: health
status: draft
kind: trial
needs: health/tried-on-a-ward; work-pensions/transition-count
stop: Stops on its date unless Parliament votes to keep it, on the published review. Passes, and it goes national.
test.where: The wards using a note-taker
test.against: wards like them without one
test.measure: the saved hours that turn up as patient time or shorter waits, ward by ward, each quarter
test.by: each contract's renewal date
fails_if: Under half of the saved time turns up as patient time or shorter waits (provisional).
leaves_out: GP practices too stretched to volunteer; patients outside England
signs: The Health Secretary
check.claim: By 31 October 2027, NHS England will publish a national figure for clinician time saved by AI note-takers, with no figure for how much of it became time with patients or shorter waits.
check.prior: 0.4
check.rule: Held if an NHS England publication between 2026-11-11 and 2027-10-31 states a national time-saved figure for ambient voice technology and gives no figure for the share that became patient contact time or shorter waits.
check.source: NHS England's website (publications and news)
check.if_revised: The publication as first issued counts; if no national time-saved figure is published, the check fails.
check.check_on: 2027-10-31
check.provisional: yes
check.result: pending
---
Every hour a machine saves is counted, ward by ward, each quarter, as a row in the Transition
Count. If under half turns up as patient time or shorter waits, the contract isn't renewed.
