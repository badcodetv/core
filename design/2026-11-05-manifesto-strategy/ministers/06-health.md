# Health and social care: manifesto strategy

> **Revised 2026-11-05 (closing pass).** The §6 draft page has been rewritten to apply the red team's fixes; the change list sits above the new draft, and the old draft is kept under it. Sections 1-5 and 7 onward are unchanged, so where they still say "unless the data says keep", read "unless Parliament votes to keep it" (see `../README.md` §2).

2026-11-05. Strategy for Kai and Jack, not a ruling. Nothing here edits `docs/government/`; the
draft page (§6) and the brief changes (§7) are proposals for a human PR or the cabinet's rolling PR.
Sources: the absorb pack (FP-A, MACH, GUARD, LAND), `spine.md`, the current brief and page, and
five web searches made today (listed at the end). Confidence marks follow LAND: [H] [M] [L] [?],
and [K] for background knowledge not re-verified today. **Nothing marked [K], [L] or [?] goes
into public copy until it passes the fact gate (spine X12), and the cabinet may only cite what
sits in a `kind=news` memory.**

---

## 1. Mission

**The line** (90 characters, no colon):

> *Test it on a ward before you sell it to a country, and give the time it saves to patients.*

It keeps the current line (it is the best line in the cabinet and pure Future Proof) and bolts on
the economic half, the "Yours" of *Tested. Undoable. Yours.* Pub version, if the teletext needs
it shorter: *"Test it on a ward first. The time it saves goes to the patient."*

**The problem this post exists to prevent.** Arc row 3 in the NHS (*the computer says no*),
plus row 2 (*the saving goes up*) in its health form. In the bad branch the NHS did not collapse
in a dramatic way. It optimised. The queue went, the form filled itself, "the decision is already
made for you and it's a *good* decision" (F1); then the human who could say yes went (F4), and by
2034 "every channel that should answer in a catastrophe is a bot returning a polite non-answer"
(F23). Each step was a reasonable purchase. Nobody tested any of them against normal care, and the
time they saved was booked as fewer staff instead of more care. The ward lost its nurses one
efficiency at a time, and when a machine got it wrong there was "no one left whose job it was".

**Why it is live now, in the real news:**

- **The machines are already being bought at national scale, ahead of the evidence.** NHS England
  expects trusts and ICBs to adopt ambient voice technology (AI note-takers listening to
  consultations) from April 2026, as part of a reported £10bn, three-year tech programme; one
  rollout alone covers more than 10,000 clinicians in Leicester and Northamptonshire [M, trade
  press]. No independent, system-wide evaluation has been published [M]. The tool may well be good.
  What is missing is the test, and any rule about where the saved time goes.
- **The queue.** 7.37m treatments (6.24m patients) waiting in England at the end of August 2026,
  the worst since October 2025, about 113k waiting more than a year [H, LAND]. In March the interim
  target was met (65.3% within 18 weeks, 7.1m waiting) [H, NHS England], reportedly with help from
  £120m of "sprint funding" [M, Full Fact]. Five months later the list was back up. That is the
  exact failure Future Proof names: a target hit on a date, not a system that holds.
- **The data.** NHS England's Federated Data Platform contract (Palantir-led) is reported to run
  to February 2027, with the renewal decision due this year [L, single secondary source]; in May
  there were reports of contractor access to identifiable data and transparency concerns [M]; the
  national data opt-out does not apply to it [L]. A renewal decision is a release decision, and it
  should ship with its test.
- **Social care.** A £500m first Fair Pay Agreement for care workers, negotiations from April 2027,
  in effect April 2028; the Casey Commission's final report brought forward to summer 2027 [M,
  gov.uk]. Care workers are told to wait two more years for a pay floor.
- **Sickness and benefits.** New-claim UC health element cut to about £50/week; PIP changes going
  ahead before the Timms review reports [M]. Health owns the clinical side of what W&P owns the
  money side of.

---

## 2. The flagships

Five, in priority order. The first two are the page; the third is the right; four and five are the
ones that make Health more than "AI policy for hospitals". All follow the spine's contract (§2).

### Flagship 1: The Ward Test

**The policy.** No AI tool that touches patient care is bought for the whole NHS until it has
beaten normal care on real wards, against a comparison, with the full result published, including
the groups it worked worst for.

**Why now.** National adoption of AI note-takers is under way from April 2026 with no published
system-wide evaluation [M]. The 10 Year Health Plan's "analogue to digital" shift [K] means dozens
more tools will follow: triage, imaging, discharge, prescribing. The buying decision is being made
now, by NHS England and ICB procurement, and it is being made on vendor pilots.

**Future Proof mechanism.** Tenet 3 (no policy without its experiment) and tenet 2 (small,
staged, with an undo). The practical form is a *stepped-wedge* rollout: trusts switch the tool on
in a random order, so every trust gets it and the ones still waiting are the comparison. Nobody is
denied anything they have today (spine amendment 1: the control group gets normal care).

**The contract.**
- *Who decided:* NHS England and ICB boards, by procurement; DHSC by setting adoption expectations.
- *The rule:* a national purchase or national adoption expectation for any patient-facing AI tool
  requires (a) a pre-registered trial on NHS wards against usual care, (b) an independent
  evaluator, not the vendor, (c) results by age, sex, ethnicity and deprivation, (d) a contract
  clause that lets the NHS switch it off, keep its data, and fall back to the manual pathway.
- *The test:* the first three national tools (start with ambient note-takers, already spreading)
  re-run as stepped-wedge trials across volunteer trusts over 12 months. Measured: the tool's
  pre-registered primary outcome (for note-takers, clinician time with patients and note accuracy;
  for a diagnostic tool, missed and false findings), plus patient-reported experience.
- *Fails if:* it does not beat usual care on its primary outcome at 12 months, **or** any monitored
  group does measurably worse than usual care. Then the national purchase stops, we publish the
  postmortem, and the trusts that want to keep it may, at their own risk, with monitoring.
- *The undo:* every national licence lapses after two years unless the live monitoring data says
  keep. The manual pathway is kept warm (staff still trained to do the job without the tool).
- *Ledger:* vendors pay in time (slower national sales) and, for weak products, in lost contracts;
  the NHS pays the evaluation cost; patients gain tools that work for them, not just on average.
- *Who it leaves out:* small trusts and GP practices too stretched to volunteer for trials, and
  the patients they serve. Counted separately, and offered evaluation support first, so "tested"
  does not mean "tested on teaching hospitals".
- *Who signs:* the national clinical lead for each tool, by name.
- *Status:* Draft.

**Scale and cost.** Small. Independent evaluation is a few per cent of contract value, paid by
reserving that share inside every AI procurement budget (no new money). The NIHR and the What
Works machinery already exist [K]. Honest uncertainty: stepped-wedge trials add months; the real
cost is delay, and we say so.

**Strongest precedents.** For: the EDITH breast-screening AI trial (about 700,000 women, announced
2025) is the NHS doing this right [K]. Against acting without it: the Epic sepsis model, used in
hundreds of US hospitals, missed about two-thirds of sepsis cases when externally validated (Wong
et al., JAMA Internal Medicine, 2021) [K]; pulse oximeters overestimated oxygen levels in patients
with darker skin (Sjoding et al., NEJM 2020; the UK's Independent Review of Equity in Medical
Devices, 2024) [K]; Babylon's GP at Hand scaled before its evidence and collapsed in 2023 [K]. The
MHRA's AI Airlock is a regulatory sandbox for AI medical devices, tenet 2 already in the building [K].

**Strongest objection.** "You're slowing down cures. People die waiting for your trial." **Our
answer:** nothing anyone has today is taken away, the trial *is* the rollout (stepped-wedge means
everyone gets it within the year), and a tool that misses two-thirds of sepsis cases also kills
people, more quietly. "Fast" is a virtue in the ambulance, not in the procurement office.

### Flagship 2: The time goes to the bed

**The policy.** Any staff time an AI tool saves is counted, published and spent on patients and
waits, and never banked as a cut to clinical posts.

**Why now.** The case for AI note-takers is time saved on paperwork [M]. Nobody has said where the
saved time goes. In the bad branch it went to "fewer staff" every time. With a list of 7.37m [H],
the bottleneck is clinical hours, and the machine is offering some back.

**Future Proof mechanism.** "Every pound has an address" applied to hours (the Chancellor's ledger,
§5), and the spine's Work and Pensions rule, *a say before the saving*, in the NHS form. Spine §5:
*"You can print the money. You can't print the nurse."* The real limit is the work; here is a
machine handing some work back. Spend it where the limit is.

**The contract.**
- *Who decided:* trust boards and ICBs, by how they book "productivity gains" in their plans; the
  Treasury and DHSC, by counting cashable savings as the prize.
- *The rule:* where a trust adopts a tool sold on time saved, its board publishes, ward by ward,
  the hours saved and where they went (more appointments, longer appointments, shorter waits,
  training time, rest). Clinical posts may not be cut on the strength of an AI saving for the term
  of the licence. Staff on the ward have a say, through their elected reps, in how the hours are
  spent (the W&P rule, shared).
- *The test:* the trusts in the Ward Test trial plus comparison trusts, 12 months. Measured:
  patient-facing clinical hours per shift; appointments delivered; waits in the affected
  specialties; staff sickness and leaving rates.
- *Fails if:* patient-facing hours do not rise, or waits in the affected specialties do not fall,
  relative to comparison trusts at 12 months. Then we publish the postmortem: maybe the saving was
  imaginary, maybe it leaked. Either way the rule goes, and the vendor's time-saving claim with it.
- *The undo:* the post-cut ban sunsets with the tool's licence; renewal only on the data.
- *Ledger:* the Treasury gives up the cashable saving it would have booked; patients gain hours;
  staff gain time they can actually use; vendors lose the "cut a post" sales pitch.
- *Who it leaves out:* agency and bank staff, whose hours are cut first and quietly; social care,
  which buys few of these tools. Both counted separately.
- *Status:* Draft.

**Scale and cost.** Close to cost-neutral by design: it allocates time the tool creates. The honest
cost is the saving the Treasury does not get to bank, which is exactly the point. Uncertain: the
real size of the time saving, which is why the test comes first.

**Strongest precedent.** Weak direct precedent, which we admit (spine amendment 3: one of our own
ideas that could fail). Closest: the Dutch Buurtzorg community-nursing model, which moved time from
admin to patients through small self-managed teams, with good but contested evidence [K]. The
cautionary twin: the decade of "efficiency savings" that were met by not filling posts [K].

**Strongest objection.** "If you can't take the saving, why buy the tool? This is Luddism with a
spreadsheet." **Our answer:** we buy it *for* the saving, we just send it to the queue instead of
the balance sheet. A nurse who gets an hour back is the cheapest new nurse the NHS will ever hire.

### Flagship 3: A name on every decision

**The policy.** If software helped decide your triage, referral, scan result or discharge, you are
told, a named clinician answers for it, and you can reach a human within one working day.

**Why now.** The reader's actual machine fear is being judged by one (welfare-algorithm concern
44% to 59% in two years, GUARD §1). GP online triage forms and NHS 111 already sort people before
a clinician sees them [K]; AI triage is the next step. This is the PM's cross-government right to
a human (arc row 3), applied first and most visibly in the NHS.

**Future Proof mechanism.** The named signatory (contract field 10, "AI drafts; a human signs;
somebody checks") and the bad branch's off-switch lesson (A2, F24): the switch was never broken, it
was just nobody's job. Here it is somebody's job, by name.

**The contract.** Per spine tension H, **this is a right, not a trial: Kept from day one, and
measured.**
- *The rule:* every automated or AI-assisted clinical decision about a person carries (a) a
  disclosure, (b) the name or role of the responsible clinician, (c) a route to a human within one
  working day (same day where clinically urgent).
- *Measured:* monthly, by trust and practice: the share of people who asked for a human and got one
  inside the limit; complaints and serious incidents involving automated decisions.
- *Fails if:* a trust or practice falls below 95% inside the limit for three months running. Then
  its licence to use that tool for that decision is suspended until it is back above. The right
  stays; the tool is what gets undone.
- *Ledger:* trusts pay a staffing cost for the human route; patients gain a door that opens.
- *Who it leaves out:* people who cannot use the digital route at all, so it never reaches them.
  Counted separately; the phone and the front desk stay open.
- *Status:* Kept (on adoption), measured.

**Scale and cost.** Unknown and probably modest: staffing a human route on top of a tool sold as
replacing one. Paid from the tool's own saving first, which is a fair test of whether it had one.

**Strongest precedent.** UK GDPR Article 22 already gives a right not to be subject to solely
automated decisions with significant effects [K]; we make it practical, fast and named. The
cautionary tale is the Post Office Horizon scandal: a computer was presumed right and nobody's job
was to check it [K].

**Strongest objection.** "A clinician rubber-stamping a thousand AI decisions a day isn't a human
in the loop, it's a human-shaped stamp." **Our answer:** agreed, which is why we measure the
override rate and publish it. A signatory who never disagrees with the machine is a finding, and it
goes in the postmortem.

### Flagship 4: The visit stays human, and the carer gets counted

**The policy.** In social care, machines take the paperwork, never the visit: sensors and
monitoring are added to care, not swapped for it, unless the person and family choose; and the
unpaid carer is counted, paid fairly and kept out of court.

**Why now.** The pay floor for care workers is two and a half years away (April 2028) [M]; Casey
reports summer 2027 [M]. Councils under budget pressure are already buying remote-monitoring and
"virtual care" systems [K]. The unpaid carer, 5 million people in England and Wales at the 2021
Census [K], is the one Health's brief already says the spreadsheet leaves out; the Carer's
Allowance earnings-limit cliff edge produced large overpayment debts and prosecutions and an
independent review in 2025 [K].

**Future Proof mechanism.** X1, name who it leaves out (the brief's instinct, made a policy), and
the W&P rule *a say before the saving*, applied to the person being cared for.

**The contract.**
- *Who decided:* councils, by commissioning care by the task and the minute; DHSC and the Treasury,
  by funding; DWP, by the Carer's Allowance cliff edge.
- *The rule:* (a) no council may replace a care visit with remote monitoring without the person's
  informed consent and a review at three months; (b) volunteer councils commission home care by the
  hour with the person, not the task, with the time any admin tool saves added to the visit; (c)
  with W&P, the Carer's Allowance earnings cliff replaced by a taper, so earning one pound over the
  limit no longer costs the whole allowance.
- *The test:* (b) in a handful of volunteer councils for 18 months against comparable councils;
  measured: unplanned hospital admissions of people in care, care-worker turnover, and what the
  people being cared for say. (c) is W&P's trial; Health co-signs.
- *Fails if:* (b) shows no fall in unplanned admissions or turnover against comparison councils at
  18 months. We publish and drop it.
- *The undo:* (b) sunsets at 18 months unless kept on the data. (a) is a right, Kept.
- *Ledger:* councils pay more per visit in the trial (offset, we bet, by fewer admissions: that is
  the bet, not a promise); care workers gain hours and stability; families gain a say.
- *Who it leaves out:* self-funders and people paying privately, whose care no council
  commissions; young carers. Counted separately.
- *Status:* Draft. **Full funding of social care: Not ready** (see §3).

**Scale and cost.** The visit rule costs little. Commissioning by the hour costs real money in the
trial councils; the national version would be billions, not millions, and we will not print a
figure before Casey and our own trial give one. Paid as social care is now: taxes and borrowing,
with the Chancellor's ledger naming who pays.

**Strongest precedent.** NICE's home-care guidance (2015) says visits under 30 minutes should be
exceptional [K], so the standard already exists and is routinely missed; Buurtzorg again [K].

**Strongest objection.** "The sensor lets my dad stay at home longer. You're taking it away."
**Our answer:** we aren't. If he and you want it, he has it. What we stop is a council swapping his
visit for it without asking him.

### Flagship 5: Your records pay rent

**The policy.** Where a company makes money from a product built on NHS patient data, a share of
the return comes back to the NHS; research for the NHS stays free; and every data deal, renewals
included, ships with its test and its published results.

**Why now.** The Federated Data Platform renewal decision is reported as due this year [L]; reports
in May of contractor access to identifiable data [M]; AI models are trained on scans and records
that the public's NHS paid to create. Spine §5: "If your bill built the grid, you own a bit of what
runs on it." The NHS record is the health version of that grid.

**Future Proof mechanism.** The ownership half of "Yours" (spine §1), the Chancellor's public stake
(§5 source 2), and CI applied to contracts: a renewal is a release, so it needs a release note.

**The contract.**
- *Who decided:* NHS England and DHSC, by contract terms that take a fee for access and no share of
  what is built.
- *The rule:* (a) commercial licences to NHS-derived data or models carry a royalty or equity
  return into NHS capacity; (b) every major data contract publishes, before renewal, what it
  promised against what it delivered; (c) patients are told, in plain words, what their data is
  used for, and the opt-out means what people think it means.
- *The test:* the next set of commercial licences on the new terms, compared with the previous
  years' volume. Measured: licences signed, research access times, money returned, and the national
  opt-out rate (a rising opt-out rate is the public voting with its feet).
- *Fails if:* commercial uptake falls by more than a pre-registered margin against comparable
  countries' data services, or the opt-out rate rises. Then the terms change, with a postmortem.
- *The undo:* the royalty terms are reviewed after three years.
- *Ledger:* firms that profit from NHS data pay a share; the NHS gains a revenue line and the
  public a stake; NHS and academic research pays nothing extra.
- *Who it leaves out:* the patients whose records are poor or missing (often the poorest), so the
  products built on the data serve them worst. Their data gaps are counted and published.
- *Status:* Draft.

**Scale and cost.** Revenue uncertain and probably small at first; we say so. The value is the
principle and the precedent. No figure until a licence has been signed on these terms.

**Strongest precedents.** DHSC's own 2019 principles said the NHS should get a fair share of the
benefits where data underpins innovation [K]; Finland's Findata runs a single permit authority with
fees [K]. The cautionary tales: the ICO found in 2017 that the Royal Free's deal with DeepMind broke
data-protection law [K]; care.data was scrapped in 2016 and GPDPR paused in 2021 after public
backlash [K]. Lose the public's trust and you lose the data.

**Strongest objection.** "You're selling NHS data." **Our answer:** it is being used commercially
already; today the public gets a fee and a press release. We want it to get a share, and to be
told.

---

## 3. What this minister will NOT promise, and why

- **No date for clearing the waiting list.** March proved a date can be hit and lost. We promise the
  number we will be judged on (the median wait for planned treatment, published monthly; FP-A D1's
  worked example), and the condition that would make us change course, not a finish line.
- **No claim that AI will save the NHS, or any figure for what it will save.** A machine that saves
  time is a hypothesis until a ward says so. "Miracle cures, technological or otherwise" is on the
  brief's guard list.
- **No new reorganisation.** Not one new logo. NHS England is already being folded into DHSC [K];
  we change rules for buying and counting, not boxes on an organogram.
- **No promise to keep private providers out.** Private capacity already treats NHS patients [K].
  We promise the brief's question, out loud: who takes the profit and who takes the risk, per
  contract, on the ledger.
- **No full social-care funding settlement.** "Not ready", printed as such, until Casey reports
  (summer 2027) and our trial gives a figure. Every party has promised a care fix; none has
  survived costing. Our refusal is the credible line.
- **No pledge of so many thousand nurses or doctors.** We can't print the nurse. We can stop losing
  her hours.
- **No ban on AI in the NHS, and no "human only" purism.** Some tools will pass the Ward Test and
  should be everywhere fast. The test is neutral (spine amendment 3).
- **No promise on immigration numbers through the NHS door.** That is Home's ruling; Health states
  the true thing (the NHS and care depend on staff recruited from abroad [K]) without denying the
  pressure elsewhere.
- **No absolute privacy promise.** Data saves lives and leaks. We promise disclosure and a share.

---

## 4. The reader test

The NHS is the one public institution this reader still loves and believes is being run down. It
is *their mum's hip* (LAND #7). AI is not on their list (GUARD §1: 0% unprompted). So every
flagship enters through the queue, the GP phone line, the care visit or the record, and "AI"
appears only in the *who decided* paragraph as the tool a named chooser bought.

| Flagship | Trap it risks | How the wording avoids it |
| --- | --- | --- |
| 1 Ward Test | "Experimenting on my mum" / postcode lottery; "blocking cures"; lecturing about RCTs | Lead with "nobody gets less than today". Say "tried on a ward first", never "RCT" or "stepped-wedge". The receipt is a machine that missed sepsis, not a statistics lesson. The tough-minded register: *"Common sense is a guess with good posture"* (D5). |
| 2 Time to the bed | Raises job fear for NHS staff with no beneficiary; reads as "AI is replacing nurses" (inevitability) | The chooser is named (the trust board booking the saving); the beneficiary is the patient in the queue; the rule *protects* the nurse's post. Never "AI will take NHS jobs". |
| 3 Name on every decision | The reader's real fear (judged by a machine) raised without a remedy | The remedy is in the same sentence: a name and a human within a day. Lands as respect, the opposite of "computer says no". |
| 4 Visit stays human | Punching down at families who use sensors; sentimental about care; left-coded "more money" ask | Choice stays with the person and family. Played straight, no sarcasm (a pledge is never sarcastic). The money ask is labelled "Not ready", which disarms "where's the money coming from?" |
| 5 Records pay rent | "Selling NHS data" reflex; Palantir as a culture-war token; conspiracy register | Concede the data is already used commercially; frame as rent owed to the public ("your mum's X-ray built it"). Name the decision (the contract terms), not the company, in public copy; no foreign-company dog-whistle. |

Proportionality hazard to watch (rule 4): NHS staffing from abroad. Health never says "migrants
keep the NHS running" as a rebuttal (rule 10: never restate the claim to refute it). It states the
true thing in a staff story, and leaves the numbers to Home.

---

## 5. Interfaces

- **Prime Minister.** Depends on: the cross-government right to a human (Flagship 3 is its first
  visible trial bed), the Test Register and the Office for Postmortems (the Ward Test results file
  there), the spine's "any AI system the state buys passes the contract" (Flagship 1 is its NHS
  form). Risk: duplication; the PM states the right, Health shows it working.
- **Chancellor.** Depends on: the ledger (Flagship 2 books hours, Flagship 5 books royalties).
  **Clash:** where does the data royalty go? Chancellor's dividend fund wants it; Health wants it
  in NHS capacity. *Proposed ruling:* NHS data returns stay in NHS capacity (the public paid for
  the record through the NHS); the PM settles if it recurs. Also: Flagship 2 gives up the cashable
  saving the Treasury would book. Expect the Chancellor to object, and say so on the page.
- **Work and Pensions.** Shares the "say before the saving" rule (Flagship 2 is its NHS edition);
  owns Carer's Allowance and the PIP/UC health element (Flagship 4c is W&P's trial, Health
  co-signs). Fit notes and the sickness-benefit link sit on the boundary: W&P owns the money,
  Health the clinical judgement. **Clash risk:** W&P attacking PIP cuts while Health says nothing
  on the assessment's clinical basis. Agree a joint line.
- **Education.** The first rung, medical version: AI note-takers and diagnostic aids may deskill
  trainees (one study found endoscopists' adenoma detection fell in non-AI procedures after AI was
  introduced, Lancet Gastroenterology & Hepatology, 2025 [K]). Education's "learning time" applies
  to resident doctors and student nurses. Training places are Education's ledger line.
- **Home.** Staffing from abroad and the care-worker visa route (closed to new overseas recruits in
  2025 [K]) sit with Home. **Clash risk:** a Home cut to care-worker visas lands on Health's care
  workforce. Both pages must say which homes and GP places come first in places under pressure
  (spine tension D).
- **Housing.** Care homes, neighbourhood health centres, and housing for care workers; the host
  town for trials.
- **Energy and Climate.** Hospital and care-home energy bills in the Hormuz shock; minor.
- **Foreign.** Medicine supply chains and drug pricing with the US [K]; minor, judgement-call only.
- **Defence.** None of substance.

---

## 6. Draft manifesto page

House format, renderer-safe (plain paragraphs, no bold, no lists), about 300 words, triage-nurse
voice. Every fact below is from a graded source in §1; before the cabinet uses any of them, each
must sit in a `kind=news` memory with its URL (the waiting-list figures and the ambient-voice
rollout most urgently). The AI note-takers paragraph is the one most likely to need re-sourcing.

### Revised draft (closing pass, 2026-11-05: the red team's fixes applied)

What changed from the draft the red team read (sources: `../redteam/opposition.md`, `../redteam/reader.md`, `../redteam/wonk.md`; the overall strategy is `../README.md`):

1. 'Fails if it doesn't beat normal care' now has a margin (a twentieth more patient time for note-takers, provisional), and 'any group does worse' is limited to groups named in advance, so the tool can't fail by chance (opposition #1, wonk #4).
2. Ward Test builds on the existing checks (NICE evidence standards, MHRA AI Airlock) rather than implying a new gate; stepped roll-out by lot (wonk §8).
3. 'Not on cutting her post' (unenforceable) becomes a reporting duty tied to contract renewal (wonk §5).
4. Right to a human scoped to triage, diagnosis, referral and discharge, and the GP phone queue added (wonk §8, reader).
5. 'Your records pay rent' rewritten so it can't read as selling records (reader). 'They may be good' cut.
6. 'Not ready' on care funding paired with what happens now (reader).

```markdown
---
title: Health
line: Test it on a ward before you sell it to a country, and give the time it saves to patients.
---
## Position

Your mum's hip is one of 7.37 million treatments on the waiting list in England. In March the target was hit, after a sprint. By August the list was back at its worst in nearly a year. Hitting a date is not the same as fixing a queue.

Meanwhile the machines are arriving on the ward. NHS England has told trusts to start using AI note-takers that listen to your appointment. Nobody has published whether they give you more of the doctor, or give the hospital fewer doctors. That is a decision, it has an owner, and it is being made this year.

So, four rules.

Tried on a ward first. The checks for medical software already exist. We make them compulsory before anything is bought for the whole NHS. Every trust gets the tool in the end, in an order drawn by lot, so the wards still waiting are the comparison. Nobody gets less care than today while we check. Fails if it doesn't beat normal care by the margin we publish before it starts (for note-takers, at least a twentieth more time with patients) with no worse safety, or does clearly worse for any of the groups we name in advance. Then it comes out, and we publish why. Passes, and it goes everywhere, fast.

The time goes to the bed. Any hour a machine saves a nurse or a doctor is counted and published, and the board shows it went to patients and waits. If it didn't, the contract isn't renewed.

A name on every decision. If software helped decide your triage, your diagnosis, your referral or your discharge, you are told, a named clinician answers for it, and you can reach a person the same working day. If software sorted your GP request, you can still get a person on the phone that day. That is a right, not a trial.

If a company makes money from NHS patients' records, the NHS gets a cut. No sale.

The number we are judged on: the median wait for planned treatment, published monthly.

Who it leaves out: people in social care, and the unpaid carer the spreadsheet never sees. Full care funding: Not ready. Until it is, the unpaid carer gets counted, and the visit stays a person.

Bed 4 first. Then the press release.
```

Notes on the revised draft:

- Trim the GP sentence first if needed.
- Fact gate: 7.37m, the March target and the August figure need `kind=news` URLs; the note-taker
  instruction is [M] and most likely to need re-sourcing.
- Body about 387 words.

### Superseded draft (the version the red team read, kept for comparison)


```
---
title: Health
line: Test it on a ward before you sell it to a country, and give the time it saves to patients.
---
## Position

Your mum's hip is one of 7.37 million treatments on the waiting list in England. In March the target was hit, after a sprint. By August the list was back at its worst in nearly a year. Hitting a date is not the same as fixing a queue.

Meanwhile the machines are arriving on the ward. NHS England has told trusts to start using AI note-takers that listen to your appointment. They may be good. Nobody has published whether they give you more of the doctor, or give the hospital fewer doctors. That is a decision, it has an owner, and it is being made this year.

So, four rules.

Tried on a ward first. No AI tool is bought for the whole NHS until it has beaten normal care on real wards, against a comparison, with the result published, including who it did worst for. Nobody gets less care than today while we check. Fails if it doesn't beat normal care, or any group does worse. Then it comes out, and we publish why.

The time goes to the bed. Any hour a machine saves a nurse or a doctor is counted, published and spent on patients and waits. Not on cutting her post. If patient time and waits don't improve in the trial trusts within a year, we publish the postmortem and drop the rule.

A name on every decision. If software helped decide your triage, your referral or your scan, you are told, a named clinician answers for it, and you can reach a human within a working day. That is a right, not a trial.

Your records pay rent. Where a company profits from what NHS patients' data built, a share comes back to the NHS.

The number we are judged on: the median wait for planned treatment, published monthly.

Who it leaves out: social care, and the unpaid carer the spreadsheet never sees. Full care funding: Not ready. We won't print a figure we can't back. They are counted separately until we can.

Bed 4 first. Then the press release.
```

Notes on the draft: the opening is the reader's situation (rule 1); the chooser is NHS England and
trust boards (rule 5); one bathos at most (the last line); pledges played straight; "Not ready"
used once, on purpose, as the credibility asset. Flagship 4's visit rule and 5's detail live in
the strategy and can rotate onto the page when the news brings them (a care story, the FDP
renewal).

---

## 7. Suggested changes to the brief (`docs/government/ministers/06-health.md`)

For a human PR (briefs are capped at 300 words; the Cabinet Secretary edits weekly). Keep
Temperament, Instinct, Guards against and Sounds like as they are; they are good. Add one section
and widen one:

**Owns:** add *"AI and automation in clinical care and in social care: any tool that helps decide
about a patient or replaces a visit. (AI is never the subject; it is the tool in a trust's,
council's or NHS England's decision.)"*

**New section, Standing commitments (sharpen, never replace):**

> 1. The ward test: no national AI purchase without a published ward trial against normal care,
> results by group, and a switch-off clause. 2. The time goes to the bed: AI-saved staff time is
> counted and spent on patients, never on cutting clinical posts. 3. A name on every decision: told,
> a named clinician, a human within a working day. 4. The visit stays human; count the unpaid
> carer. 5. NHS data pays rent to the NHS. Scoreboard: the median wait for planned treatment,
> monthly. Full social-care funding is "Not ready" until the evidence gives a figure. Hang the day's
> news off one of these; a quiet health day leaves the page as it is.

**Guards against:** add *"dates for clearing the list; any figure for what AI will save; denying
the NHS's reliance on staff from abroad, or restating claims about it to refute them."*

**Watches:** add `tech-ai` items with a clinical or care angle (label key `health=y`), and NHS data
contracts and renewals. Health had no news on 5 November (MACH §0): the gatherer's health beat
needs the monthly RTT statistics and NHS England procurement news as standing sources, or this
page stays empty.

---

## The biggest risk

The NHS is the reader's last loved institution, so "test it on a ward" can be heard as
*experimenting on my mum* or *slowing down the cure*, and "your records pay rent" as *selling NHS
data*. Both are fatal if they land first. The defence is wording discipline (nobody gets less than
today; the data is already sold, we want the share) and leading every page with the queue, not
the machine. The second risk is mechanical: Health gets almost no daily news, so without the brief
change in §7 and standing sources for the gatherer, the cabinet will either leave the page empty or
improvise NHS policy from one aggregator item.

---

## Sources searched today

- Ambient voice technology: [NHS England Transformation Directorate guidance](https://transform.england.nhs.uk/digitise-connect-transform/digitising-the-frontline/adopting-ambient-scribing-products-in-health-and-care-settings) · [Digital Health: integrated AVT and £10bn](https://www.digitalhealth.net/?p=302321) · [IT Brief UK: trusts launch major AI voice rollout](https://itbrief.co.uk/story/nhs-trusts-launch-major-ai-voice-rollout-for-clinicians) · [Pulse: UHL/UHN rollout](https://www.pulse.bot/healthcare/news/rollout-of-ambient-voice-technology-across-uhl-uhn-to-speed-up-care-and-improve-communication-for-pa-6255d1f3-0d45-4da6-9c65-b67f76d7f419) · [CMOtech: Hertfordshire](https://cmotech.uk/story/hertfordshire-nhs-trust-rolls-out-ambient-voice-tech)
- Waiting times: [NHS England March 2026 RTT press notice](https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/05/Mar26-RTT-statistical-press-notice-PDF-545K-Dc1i9U.pdf) · [Full Fact: 18-week tracker](https://fullfact.org/government-tracker/cut-waiting-times-18-week-standard/) · [RCS England](https://rcseng.ac.uk/news-and-events/media-centre/press-releases/rtt-april-2026/) · August 2026 figures via LAND ([CIAC](https://ciac.co.uk/2026/10/09/nhs-waiting-list-at-its-worst-since-2025-new-figures-reveal-despite-record-levels-of-care/))
- Social care: [gov.uk: £500m Fair Pay Agreement](https://www.gov.uk/government/news/500m-for-first-ever-fair-pay-agreement-for-care-workers) · [CMS: social care reform programme](https://cms.law/en/gbr/legal-updates/prime-minister-announces-major-social-care-reform-programme) · [FPA consultation](https://www.gov.uk/government/consultations/fair-pay-agreement-process-in-adult-social-care/fair-pay-agreement-process-in-adult-social-care-consultation-document)
- Data: [NHS England: FDP update](https://www.england.nhs.uk/long-read/federated-data-platform-update/) · [LSE/Reuters: contractor access](https://www.lse.co.uk/news/britains-nhs-to-grant-palantir-contractors-unlimited-access-to-patient-data-ft-reports-rhhwv9in5tfcyy1.html) · [Think Digital Partners, 12 May 2026](https://www.thinkdigitalpartners.com/news/2026/05/12/nhs-england-expands-external-access-to-patient-data-platform-amid-transparency-concerns/) · [Pulse: opt-out does not apply](https://www.pulse.bot/govtech/news/nhs-patients-cant-opt-out-of-palantirs-data-platform-but-their-hospital-can-9f157ddb-b8c3-48be-b711-c566b62df62f/)
- Precedents marked [K] (Epic sepsis, pulse oximetry, Babylon, EDITH, MHRA AI Airlock, DeepMind/Royal
  Free, care.data, GPDPR, Findata, Buurtzorg, NICE NG21, Article 22, Horizon, the colonoscopy
  deskilling study, the Carer's Allowance review, Census carers) were not re-searched today.
