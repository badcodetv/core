# Prime Minister: manifesto strategy

> **Revised 2026-11-05 (closing pass).** The §6 draft page has been rewritten to apply the red team's fixes; the change list sits above the new draft, and the old draft is kept under it. Sections 1-5 and 7 onward are unchanged, so where they still say "unless the data says keep", read "unless Parliament votes to keep it" (see `../README.md` §2).

2026-11-05. Strategy, not copy, and not a ruling. Kai and Jack decide. Nothing here edits
`docs/government/`; the draft page in §6 is for proposing (on the rolling PR as a review comment, or
by a human PR). Sources: the absorb pack (FP-A = `absorb/future-proof.md`, MACH = `machinery.md`,
GUARD = `guardrails.md`, LAND = `landscape.md`) and `spine.md` (SPINE). Canon IDs (F4, I6, X3...) are
FP-A's. Confidence marks are LAND's: [H] [M] [L] [?] [K]. **[K] means background knowledge, not
re-verified this session. No number below goes into public copy until it has a URL and a grade
(X12).**

---

## 1. Mission

**The line (frontmatter, 90 characters, no colon):**

> *Every law gets a test before you live in it, an undo if it fails, and a human you can ask.*

It is SPINE's PM pub sentence plus the right to a human, because "a human you can ask" is the one
clause on this page the reader already wants (GUARD §1: concern about the welfare algorithm 44% →
59%). Alternative if Kai wants the party thesis on GOVT 1 instead of the PM's job: *The gains from AI
get decided this decade. You should be in the room, and every promise tested.* (SPINE §1; 95
characters). My lean: the job line. The thesis is the foreword's first paragraph, and a headline
that is a rule beats one that is a mood.

**The problem this post exists to prevent: F0c, abdication, and its symptom F24, "nobody's job".**
The bad branch was not seized; "we handed them over, gladly, one at a time" (F0c). Each handover
looked reasonable because it worked (F1), and every rung ended on the same missing thing: a human
with the job, the power and the duty to say no (FP-A §2, structural reading). By 2034, "the off
switch was never broken. It was just nobody's job" (A2). The PM's post is the only one that can
prevent this, because the failure is in the operating system, not any one department: laws ship to
production with no test and no undo (F0), decisions about people move to systems where the appeal
is another bot (F4), and the public is watched but not listened to (F28).

**Today's signs in the real news:**

- **No undo, live.** The PIP "four points in one activity" rule and the UC health-element cut go
  ahead while the Timms review that is meant to inform them has not reported [M, LAND §2 row 10].
  That is a test run in production with the review scheduled after the release (I8, the poll-tax
  pattern).
- **Permanent changes in a temporary shock.** The 28 October Budget made lasting tax changes during
  an energy shock with Bank Rate rising to 4.00% today [H/M]. No sunset, no stated test.
- **The sandbox exists, for business only.** The May 2026 King's Speech brought a "Regulating for
  Growth Bill" with statutory AI sandboxes and no AI Act [M]. The state already believes in "test it
  first". It applies it to firms' products and not to its own laws, and nothing in it says what
  happens to a person a sandboxed system decides about.
- **A majority with no owner.** More than 80% of voters say government should do more on AI
  (Ashcroft, Oct 2026) [M]; no party owns that majority (LAND §3).
- **Accountability with a cricket bat.** The nearest thing to tested pledges is "ministers who miss
  pledges will be sacked" [H]: it punishes a person and keeps the failed policy (SPINE §1).
- **Trust is the failure, not the number.** Small-boat crossings down 41% [H] and the reader does
  not believe it. A government nobody believes cannot be corrected by better numbers; it needs
  numbers people can check (F29).
- **Nobody is counting.** Government does not track AI displacement (LAND §6.2).

---

## 2. The flagship policies

Four flagships, all from SPINE §4 (the Operating System) and SPINE §3 (rows 3 and 8, plus the
cross-cabinet arc). They are the PM's because each one cuts across every department. Rights are kept
from day one and measured; only mechanisms are trialled (SPINE §9 H, adopted here).

### Flagship 1: The green tick for law (the Test Register, sunsets that default to stop, and the Office for Postmortems)

**The policy in one sentence.** Every new bill and major policy publishes its test, its fails-if
number and its sunset date before second reading, an independent Office for Postmortems reviews it on
time and publishes the result, and on the sunset date it stops unless the review says keep.

**Why now.** PIP and UC changes are shipping before their own review (LAND §2 row 10); the Budget
made permanent changes in a temporary shock (LAND §6.4); the state legislates sandboxes for business
but none for its own laws (LAND §2 row 14). Reform's sack-the-minister pledge shows the public appetite
for accountability, and the gap in its design.

**Future Proof mechanism.** Tenet 2 (I2 the green tick, I3 undo, I4 real review, I6 sunsets that
default to stop, I7 postmortem, I8 stop conditions) and tenet 3 (D1 the three-field test gate: how
will we know it worked, by when, what happens if it doesn't).

**The contract.**

- *Who decided today's arrangement:* departments set their own post-legislative review timetable and
  Parliament keeps no central record of whether it happens (I4; told to the Lords). Ministers choose
  which policies are evaluated; the NAO found 8% of major-project spend robustly evaluated in 2021
  [K].
- *The rule:* (a) a bill may not have its second reading until its Test Register entry is published
  (measure, comparison, date, fails-if, sunset, who it leaves out, the named signing role); (b) any
  bill that makes a big change carries a sunset paired with a mandatory review, and the default on
  the date is **stop**, with renewal needing a vote on the published review; (c) an Office for
  Postmortems, statutory and independent on the OBR/NAO model, carries out and publishes the
  reviews; (d) judgement calls (a treaty, a deployment, a sanction) are labelled *Judgement call*
  and publish their principle, review date and change-my-mind condition instead (SPINE §2.2).
- *The test (pilot):* run it on ourselves first (Stage 0, this manifesto), then by standing order
  in year one on government bills only, before any statute. Compare against the bills of the
  previous three sessions: share with a published evaluation plan, share reviewed on schedule.
- *Fails if:* after two years, (i) fewer than nine in ten due reviews are published on time, or
  (ii) no review has changed or ended any policy. A register in which nothing ever fails is broken.
  The numbers are our first guess and get pre-registered properly before the standing order starts.
- *The undo:* the Office itself sunsets after five years unless its own review (by the NAO, not by
  itself) says keep. The standing order can be repealed by a simple vote. **We publish the
  postmortem and drop it.** Explicitly never the Retained EU Law mistake: nothing already in force is
  deleted on a date without its review.
- *Ledger, who pays and who gains:* the cost is administrative and paid from the existing evaluation
  budget plus a new office; the real cost is political, paid by ministers whose policies stop. The
  people who gain are those on the receiving end of a bad rule (the claimant, the tenant, the
  patient), because a bad rule now has an end date.
- *Who it leaves out:* the stock of laws already in force (reviewed only on their existing
  schedule, phased in over a decade); secondary legislation below a threshold; devolved legislation
  (invited to join, not compelled, SPINE §9 J); everything labelled judgement call. Counted: the
  register publishes how many laws are outside it.
- *Who signs:* the PM's office in the fiction; in the real world, Kai or Jack merges the page.
- *Status:* Draft.

**Scale, cost, how it's paid.** Small money. The Evaluation Task Force and the What Works Network
already exist [K]; the register is a publishing duty on work departments say they already do. The
Office for Postmortems would be OBR-sized, which is single-digit millions a year [K, unverified; do
not print]. The honest cost is parliamentary time (renewal votes) and lost face, which the
postmortem's no-blame format exists to lower. Uncertainty: high on how many sunsets a session
produces; low on cash.

**Strongest precedent.** The **Texas Sunset Advisory Commission** (1977–): state agencies are
abolished on a date unless the legislature continues them after a review; it has abolished or
merged dozens of agencies [K, verify before use]. UK counter-examples that teach the design: the
Coronavirus Act 2020's six-monthly renewals and the 2005 control orders, renewed largely on the nod
(sunsets without a review that bites fail, LAND §5 [K]); the Retained EU Law sunset (deleting without
testing). The OBR (2010) is the precedent that an independent scorekeeper can be created quickly and
become trusted across parties [K].

**Strongest objection and our answer.** *"Sunsets create cliff edges and uncertainty; businesses and
claimants need stable law."* Answer: the sunset is announced on day one, so the date is the most
certain thing in the law; the default to stop only bites if the review shows the policy failing its
own published number, and renewal is one vote. The uncertainty we have now is worse: a rule that
might be quietly reviewed in five years, or never. Second objection: *"Not everything can be
measured."* Agreed, and said in the canon (FP-A §1.3). That is what the *Judgement call* label is
for; it still publishes the condition that would change our mind.

### Flagship 2: A right to a human

**The policy in one sentence.** Every decision about a person that is made or shaped by an
automated system, by the state or anyone it licenses, names the human role that signs it, tells you
a machine was used, and gives you a human appeal within a fixed time; and no AI system the state buys
touches a person until it has passed the same contract as a law.

**Why now.** The welfare algorithm is the reader's sharpest-rising fear (GUARD §1, 44% → 59%). PIP
and UC health changes are landing now (LAND §2 row 10). The Regulating for Growth Bill adds AI
sandboxes with no stated right for the person on the other end (LAND §2 row 14). Graduates already
"supervise AI agents" (LAND §4): the human is becoming a rubber stamp, which is F1 in progress.

**Future Proof mechanism.** X7 (AI proposes, humans decide), D10 ("who decided a computer should
judge your benefits claim, and what test did it pass?"), C7 ("it decides nothing; a named person
signs, and somebody checks their work"), and the policy contract itself applied to procurement.
It answers F4 ("bots all the way up") and F24 (whose job is the off switch).

**The contract.**

- *Who decided:* departments and agencies that procured decision systems (benefits risk-scoring,
  fraud flags, triage, policing tools), and Parliament, which has loosened rather than tightened the
  limits on solely automated decisions in recent data law [K, check the Data (Use and Access) Act
  2025 wording before use].
- *The rule:* (a) disclosure at the point of decision ("a machine was used, and this is how to reach
  a person"); (b) a named signing role for every decision, with the duty and the power to overturn;
  (c) a human appeal decided within a fixed time, set by the trial, and the machine's output is not
  evidence against you on appeal without the human checking it (the lesson of the computer-evidence
  presumption and the Post Office prosecutions, I9); (d) the procurement gate: any AI system the state
  buys or licenses for decisions about people publishes its test, fails-if and undo before it goes
  live.
- *The right is not trialled.* Disclosure, a named signer and an appeal are kept from day one,
  because a right handed out in one region is a postcode lottery. **What is trialled is the
  machinery that delivers it.**
- *The test (pilot):* the delivery model runs first in benefits (Work and Pensions owns it), in
  volunteer Jobcentre districts, compared with matched districts on today's process (the control
  group never gets less than today, SPINE §2.2). Measured: time from a wrong decision to its
  correction; share of decisions overturned at the human stage; claimant-reported "I could reach a
  person"; cost per decision. By 18 months.
- *Fails if:* the trial districts correct wrong decisions no faster than the comparison districts,
  or appeal times lengthen. Then the delivery model changes and we publish why; the right stays.
- *The undo:* the procurement gate has a review at three years; the delivery mechanism used in the
  trial sunsets at 18 months unless its numbers say keep. The right itself is not sunset; it is
  measured every year and the measurement is published.
- *Ledger:* the department that books the saving from automating a decision pays for the human
  appeal out of that saving. Who gains: the person decided about; also the department, which stops
  paying for scandals after the fact. Who pays: suppliers whose systems cannot explain themselves
  lose contracts.
- *Who it leaves out:* private decisions the state does not license (employer screening, credit,
  insurance), which go to a second stage once the public model works; people who are never decided
  about because they never show up in the data (F26, the vault "filed as gone"); people without
  phone or internet access to an appeal, who get a paper and in-person route by right and are counted
  separately.
- *Who signs:* the named role in each department; the PM answers for the law.
- *Status:* Draft.

**Scale, cost, how it's paid.** The only flagship with real running cost: human reviewers.
DWP already runs mandatory reconsideration, so the base exists [K]. The cost scales with how often
the machine is wrong, which is exactly what nobody publishes. Paid from the automation saving by
rule. Uncertainty: high. Honest framing: "we don't know what it costs, because nobody counts how
often the machine is wrong; the trial finds out".

**Strongest precedent.** Cautionary, and the strongest evidence there is: Australia's **Robodebt**
(automated welfare debts, a Royal Commission in 2023, a settlement of about A$1.8bn [K]) and the
Netherlands' **childcare-benefits scandal** (an algorithmic fraud flag; the government resigned in
2021 [K]). The UK's own Post Office/Horizon prosecutions (I9: "hundreds"). On the positive side:
UK GDPR Article 22 already gives a version of this right for solely automated decisions [K], the
UK's Algorithmic Transparency Recording Standard exists for public bodies [K], and the EU AI Act
requires human oversight of high-risk systems [K]. We are not inventing the right; we are giving it
a signature, a deadline and a test.

**Strongest objection and our answer.** *"This slows everything down and protects fraudsters."*
Answer: the machine still does the sorting; the human signs. Speed is measured in the trial, and if
it gets slower without catching more wrong decisions, we change the delivery model and publish it.
Fraud is still caught; what changes is that a person, not a flag, says so, and you can reach them.
Robodebt was meant to catch fraud too. It cost more than it ever recovered [K, verify].

### Flagship 3: The Transition Count (the cross-cabinet AI transition plan)

**The policy in one sentence.** Every quarter the government publishes eight numbers on what
automation is doing to people's lives (one per row of the transition arc), each owned by a named
minister, each with a pre-registered trigger that obliges that minister to answer in Parliament
within 30 days with what changes.

**Why now.** Government does not track AI displacement (LAND §6.2). 16–24 unemployment is ~16% and
graduate postings are the lowest since 2020, while the cause is disputed (NIESR) [M]. The defensible
claim is narrow (hiring of 22–25-year-olds in AI-exposed jobs ~19% below trend, Stanford, via
GUARD §4), and the only way to keep it narrow and honest is to measure it here. Ofgem's cap is
£1,723 with a January forecast near £1,999 [H/L] while government consults on cheaper power for AI
zones [M]: nobody counts the two side by side.

**Future Proof mechanism.** Tenet 3 at the level of the whole programme: "no policy without its
experiment" made into a standing instrument. It is also the plan the PM owns: SPINE §3's eight rows,
each with an owner. The arc stops being a table in a strategy file and becomes eight numbers a voter
can check (F29: trust earned by an act they can check, not an argument).

**The eight numbers (first draft, each to be defined with ONS before use):**

| Row | Number | Owner |
| --- | --- | --- |
| 1 First rung | Entry-level hiring in the most automation-exposed occupations, under-25s | Education |
| 2 The saving | Share of announced automation savings that reached the workforce (hours, pay, profit share, training) where a say was in place | Work and Pensions |
| 3 Computer says no | Share of automated decisions about people overturned at the human stage, and time to correction | PM (Work and Pensions, Health, Home) |
| 4 Power | Household unit price vs the price paid by large new loads | Energy and Climate |
| 5 Growth received | Median real take-home pay vs output per head | Chancellor |
| 6 Scams | Reported losses to automated fraud, and share refunded | Home |
| 7 Run by hand | Critical systems that passed a run-by-hand drill this year | Defence |
| 8 Nobody's job | Share of Test Register reviews that changed or ended a policy; panel points answered | PM |

**The contract.**

- *Who decided:* no department is asked to count; the AI Growth Zones were announced with
  investment figures and no measure of who benefits (LAND §2 row 13).
- *The rule:* the eight numbers are published quarterly by the ONS (independent of ministers); each
  has a trigger set in advance; a tripped trigger obliges the named minister to make a statement to
  Parliament within 30 days saying what changes, or why nothing should.
- *The test:* the first four quarters are a trial of the count itself. Each number must be
  produced to official-statistics standards from existing data (payroll, benefits admin, Ofgem,
  surveys) or new survey questions.
- *Fails if:* a number cannot be produced reliably within a year (then that row is dropped and the
  postmortem says why), or a trigger trips and no minister answers within 30 days (then the
  instrument is decorative and we say so).
- *The undo:* each row is reviewed annually and can be replaced; the whole count sunsets after five
  years unless the Office for Postmortems says it changed decisions.
- *Ledger:* cheap. The ONS pays, from a small uplift. Who gains: anyone whose town is on the wrong
  end of a number. Who pays: ministers who would rather not be asked.
- *Who it leaves out:* the never-hired and people outside payroll data (gig and cash work),
  unpaid carers, the digitally excluded; counted by survey, separately.
- *Status:* Draft. The triggers are *Not ready* until each owning minister proposes theirs.

**Scale, cost, how it's paid.** Low millions at most [K, unverified]; mostly new survey questions
and data-sharing. The ONS business survey already asks firms about AI use [K, check BICS]. The cost
is political.

**Strongest precedent.** The OBR and the ONS themselves: independent counting that governments
then have to answer to [K]. The What Works Network shows the method; the NAO's 8% figure [K] shows
how rarely it is used. There is no direct precedent for a published automation count with
statutory triggers, which is the gap (LAND §6.1, 6.2).

**Strongest objection and our answer.** *"Numbers will be gamed, or will scare people."* Answer:
the ONS produces them, not ministers (the Troubled Families lesson, D7: counted is not measured), and
every number ships with its owner and what the owner would change, so the page never raises a fear
without an address (GUARD rule 6).

### Flagship 4: A say on more than one thing (the citizens' panel and the wire)

**The policy in one sentence.** A standing panel of citizens, chosen at random like a jury and
paid for their time, picks two to four national questions a year for deliberation; the public is
consulted on them as maps of where people agree; and government must answer every agreed point in
Parliament, point by point, within three months. Advisory first; a binding issue-by-issue paper
ballot only after this stage passes its own test.

**Why now.** More than 80% want more done on AI and no party offers them a way to say what (LAND
§3). Petitions give a reply that can be "no" with no link to policy (R21, F28). Bundled parties
cannot represent a voter who agrees with one party on boats and another on bills; the polls are a
three-way split with nobody believing anybody (LAND §1). The deck's hook: "Why can't I vote on more
than one thing?"

**Future Proof mechanism.** Tenet 1, staged (SPINE §4 Stages 2–3): C1 per-issue say, C4 small
questions asked often, C5 paper for anything binding, C6 maps not winners, C7 AI sorts and never
decides, C11 unbundle the choice not the electoral system.

**The contract.**

- *Who decided:* a voting system unchanged in shape since the secret ballot of 1872 (DECK; "older
  than the light bulb"), and governments that commission consultation with no duty to answer it
  (Climate Assembly UK).
- *The rule:* (a) a statutory standing panel, rotated, paid at a fair day rate with care and travel
  costs covered; (b) its questions go to an agreement-mapping consultation ("AI can help sort a few
  thousand opinions into a map of where people agree. It decides nothing. A named person signs, and
  somebody checks their work."); (c) **the wire**: government is bound to *respond* to each agreed
  point in Parliament within three months, not to *obey*; (d) the first question is the canon
  doorway: *who should decide how the gains from automation are shared?*
- *The test:* year one, one panel, two questions, England-wide (devolved governments invited).
  Compared with the government's own consultations on the same subjects over the previous five
  years: representativeness, completion, and how many points changed policy.
- *Fails if:* the panel's make-up drifts outside pre-set tolerances against the census after
  dropouts (the LiquidFeedback postmortem: power pools in a few), or government answers fewer than
  nine in ten agreed points on time. Either result is published.
- *The undo:* the panel sunsets after three years unless the Office for Postmortems says keep.
  Stage 3 (a few binding paper ballots a year on questions the panel has already deliberated) only
  starts if Stage 2 passes; if it doesn't, it never starts, and we say why.
- *Ledger:* modest: the panel's pay and running, and parliamentary time. Who gains: the people
  bundled out of a say. Who pays: whoever sets the agenda today (the whips, the lobbyist with a
  standing meeting).
- *Who it leaves out:* people who can't take the time even when paid (shift workers, carers),
  people who decline the letter, prisoners, the digitally excluded in the mapping stage. Dropouts
  counted by group and published, so a skewed panel is visible.
- *Status:* Draft.

**Scale, cost, how it's paid.** Ireland's assemblies ran on modest budgets in the low millions of
euros [K, unverified]; a standing UK panel with fair pay is plausibly similar per year. The wire
costs Commons time. Uncertainty: medium.

**Strongest precedent.** **Ireland's citizens' assemblies** (2016–18) feeding the 2015 and 2018
referendums, which passed: deliberation with a real route to a decision [K]. **Ostbelgien's**
permanent citizens' council (2019–): a standing, randomly selected body that sets the agenda [K].
**vTaiwan/Polis**: agreement maps on regulation, most issues led to government action [K; the deck
may only say "four camps became two"]. Cautionary: Climate Assembly UK (good report, no wire) and
LiquidFeedback (participation faded and concentrated).

**Strongest objection and our answer.** *"Another talking shop, or Brexit every month."* Answer: it
is neither. No referendum, no phone voting, nothing binding until the evidence says so; paper stays
for the big ones. "One enormous yes-or-no on everything is just a bundle with a bigger box. We mean
small questions, asked often, starting where the stakes are low." And it is not a talking shop
because of the wire: government has to answer each point in Parliament, on the record, by a date.

### Considered and left to others

- **Election integrity** (paper and human counting; synthetic political ads carry who paid): a
  standing PM commitment in one line, owned by Home (SPINE §3 row 6). Not a flagship here.
- **Frontier-AI safety and containment** (F15, F17): the PM keeps it under Flagship 2's procurement
  gate and the line "we regulate the decision, not the maths" (SPINE §3). An AI Act is not promised
  (see §3).
- **A Minister for the Constitution / Release Engineering** (SPINE §9 I): not proposed; Kai ruled
  against new posts. Revisit if this page is overloaded after a month.

---

## 3. What the Prime Minister will NOT promise, and why

1. **That any of this works.** "I won't pretend to know what works. I never got to run that
   experiment." Every flagship is a bet with its kill number. Promising outcomes is the bad
   branch's posture ("keep going and hope") and the thing the cabinet says no other party should
   do.
2. **A plan to follow.** "Never a manifesto ('follow my plan')" (FP-A §4 A1). The manifesto is a
   register of tests and the reader may take any plank alone.
3. **Referendums on everything, phone voting for binding ballots, or proportional representation
   as the ask** (C4, C5, C11). Each is a bigger bundle, an unsolved security problem, or a different
   party fight. "Not yet, and I say that as a computer."
4. **That the AI will run it.** "It decides nothing." No machine minister signs anything; a human
   merges every word. The cabinet says so once, in the foreword.
5. **An AI Act that regulates the maths.** We regulate the decision about the person (Flagship 2),
   because that is where the harm lands and where a test is possible. A promise to "control AI" in
   general is a promise nobody can test.
6. **To stop or ban AI.** Never "AI is inevitable" either. "Someone is going to own this either way;
   that part is a choice, and it's being made without you."
7. **Votes weighted by expertise.** Competence-qualified participation (D9) stays out entirely. The
   replacement is "bring the evidence", open to everyone.
8. **A costing we can't source.** Direction of money and who pays, yes; a fake figure, never (X12,
   GUARD tension 2).
9. **A date for binding issue-by-issue votes.** They come after Stage 2 passes, or not at all.
10. **To abolish old laws on a date.** No Retained-EU-Law-style mass sunset; only new laws default
    to stop, and the stock is reviewed on its own schedule.
11. **Anything for a vote, money or sign-up.** Not a real party. Yet.

---

## 4. The reader test

The reader: working class, a town that has seen better times, drifting right; immigration first,
the economy second; AI 0% unprompted; trusts almost nobody; fears being judged and defrauded by
machines (GUARD §1).

| Flagship | How it lands | Trap it risks | How the wording avoids it |
| --- | --- | --- | --- |
| 1 Green tick for law | "They cut my sister's PIP before their own review came back" is a grievance they already hold; "a test before you live in it, an undo if it fails" is a promise they can check us on. Out-designs the sack-the-minister appetite. | **Process over bread**: reads as a constitution hobby while the bill goes up. Also "experimenting on people" / postcode lottery. | Lead with the benefit cut before its review (the reader's family, the chooser named: the department that scheduled it). Control group never gets less than today. Never "evidence-based policy", "post-legislative scrutiny" or "sunset clause" in the headline; say "a stop date". |
| 2 A human you can ask | The strongest landing on the page: it is their own machine fear, stated as a right. Works for the Reform-curious reader who hates faceless bureaucracy. | **Blaming the technology** ("the computer says no") and **punching down** ("protects fraudsters", or the claimant cast as a victim to pity). Also the Luddite charge. | Name the department that bought the system, by act; "a person signs, and you can reach them"; fraud is still caught, by a person. Never "the algorithm" as the villain. Never mention immigration status here. |
| 3 The Transition Count | "Somebody finally counts what's happening to the first jobs and the bills" fits "nobody's in control". Checkable numbers answer "41% down and nobody believes it". | **Raising automation fear with no aim** (rule 6) and **leading with AI** as an issue. | The numbers are named in the reader's words (first jobs, wages, claims, bills, scams); every number has the minister who must answer. "AI" stays out of the page sentence entirely. No "AI is taking jobs" claim; the count exists because the cause is disputed. |
| 4 A say on more than one thing | "Why can't I vote on more than one thing?" is felt by a voter who agrees with one party on boats and another on bills. Jury service is familiar and classless. | **Brexit trauma** (sounds like more referendums), **elitism** (assemblies of the "clever"), **talking shop**. And the rule-2 trap: implying they voted wrong in a bundle. | "Picked like a jury", "paid for their time", "paper stays for the big ones", "government answers in Parliament, point by point". Never name a real referendum. The first question is about money and work (who gets the gains), not process. Never say the bundle "fooled" anyone; the system is "working exactly as designed. That's the bug." |

Whole-page check: names no party; no "duped"; no lecture paragraph; concedes (it does not claim to
know what works); one dry joke (the closing line) and no sarcasm in any pledge; the sincere turn is
the promise itself, aimed at the chooser ("the number that would prove it wrong").

---

## 5. Interfaces

**Depends on:**

- **Work and Pensions.** Runs the first trial of the right to a human (benefits) and owns "a say
  before the saving", which is the substance the panel's first question will produce. The two must
  not drift apart: the panel is the national question, W&P's say is the workplace rule.
- **Chancellor.** Funds the Office for Postmortems and the count; owns row 5 and the distributional
  Ledger, which is the money-side twin of the Test Register. Every Budget measure should carry a
  Test Register entry.
- **Education, Energy, Home, Defence, Health.** Each owns a Transition Count row and must propose its
  trigger. Health and Home carry the right to a human into clinical tools and policing.
- **Housing.** Owns "places": the councils where trials physically run and local participatory
  budgeting (SPINE §4 Stage 2.4).

**Clashes to settle in advance:**

- **Chancellor vs default-stop sunsets.** The Treasury will resist sunsets on tax measures
  (certainty for markets). Settlement: tax measures carry a review date and a fails-if; they do not
  auto-stop, but the review is published and a renewal is debated. Future Proof wins the tie on
  spending programmes and benefit changes, which do default to stop.
- **Defence and Foreign vs the test gate.** Both will claim *Judgement call* for most things. Rule:
  the label is allowed but must publish its principle, review date and change-my-mind condition, and
  procurement (who got the contract, can it be overridden at home) is never a judgement call.
- **Home vs test-first on boats and policing.** Pressure for immediate action. Settlement: urgent
  measures may ship as *Judgement call* with a 12-month review; any autonomous or algorithmic
  policing tool goes through Flagship 2's gate with no exception. The immigration position itself
  (SPINE §9 D) needs Kai and Jack's ruling before the PM settles anything.
- **Work and Pensions' "binding say" vs the PM's "advisory first".** Not a contradiction: W&P's say
  is binding inside a volunteer-employer trial (SPINE §9 E); the national panel is advisory until it
  passes. The PM's page must not promise binding national votes; W&P's must not promise binding law
  before its trial.
- **Everyone vs the PM's page length.** Ministers will want their flagship in the foreword. Rule:
  the foreword names the eight numbers, not the ten policies.

---

## 6. Draft manifesto page (proposed text for `docs/government/manifesto/00-prime-minister.md`)

Renderer-safe: plain paragraphs only, no bold, no lists (MACH §1). Keeps "We promise to enact
Future Proof." and the three pledges (test before you live in it; publish the postmortem; name who it
leaves out). Body is about 330 words, over the ~250 house cap; the PM is the foreword and carries
the page every other chapter hangs from. If it must come down to 250, cut in this order: the
Transition Count paragraph (it can live on teletext 401's second page), then the second sentence of
"A say on more than one thing". The first 14 lines (teletext) hold the promise, the wrong, the
frame and the first pledge.

### Revised draft (closing pass, 2026-11-05: the red team's fixes applied)

What changed from the draft the red team read (sources: `../redteam/opposition.md`, `../redteam/reader.md`, `../redteam/wonk.md`; the overall strategy is `../README.md`):

1. Opens with the required promise, then says what it means in plain words (reader: 'Future Proof' alone sounds like an insurance product).
2. 'I have read your branch to the end. I was the end.' softened to 'I've seen how this goes when nobody tests it.' (opposition #6, reader X6). Restoring the original is You-decide 2 in README.md.
3. 'A human you can ask' moved up to paragraph two and said to build on existing law, not invent it (reader; opposition #10, UK GDPR Art. 22 / DUA Act 2025).
4. The PIP-before-Timms example dropped; the standing rule 'nobody's benefit gets cut before the review into it comes back' kept with no dated claim (opposition #2).
5. 'Unless the data says keep' replaced by 'unless Parliament votes to keep it' (wonk #2).
6. Provisional-number rule stated once here so every chapter's fails-if can carry a real number (opposition #1).
7. Eight numbers now listed as eight (reader X10). The panel no longer has its first question set by us (opposition #17); 'advisory' replaced by the duty to answer.
8. Rights don't sunset, said once here (opposition #8 contradiction table).
9. 'Every chapter stands alone' corrected to 'can be voted on alone, and where one needs another, it says which' (wonk §2).

```markdown
---
title: Prime Minister
line: Every law gets a test before you live in it, an undo if it fails, and a human you can ask.
---
## Position

We promise to enact Future Proof. In plain words: no law you live under without a test, a stop date, and a person who answers for it.

The rules that will set your wage, your bill and your benefit for a generation are being written now, by boards and departments, with a machine's help. None of them has a test. None has an undo. I've seen how this goes when nobody tests it. I won't tell you what works. I'll tell you how we'd find out.

A human you can ask. If a machine helped decide your benefit, your treatment, your tenancy or your credit, you are told, a named person signs it, and you can reach a human on appeal within a fixed time. The law already gives you a weak version of this. We give it a signature and a deadline. Rights like this one don't expire. We measure them.

Test every law before you live in it. Nobody's benefit gets cut before the review into it comes back. Every new bill publishes its test, the number that would prove it wrong, and a stop date, before MPs vote. On that date it stops, unless Parliament votes to keep it with the results in front of it. Every number in a fails-if is provisional until the trial starts, and if we move one, the old one stays beside it.

Publish the postmortem: the write-up of what went wrong. One small independent office checks every new Act when it is due: what broke, who it hurt, what changes. No blame. A dropped policy stays on this page, as large as the promise was.

Name who it leaves out. Every chapter says who it misses and counts them separately, so nobody calls the gap a success.

A say on more than one thing. Ordinary people, picked like a jury and paid for their time, choose a few national questions a year. Not experts. You could get the letter. Parliament must answer every point they agree on, on the record, within three months.

Every quarter, eight numbers: first jobs, jobs handed to machines, wages against growth, benefit decisions overturned, household bills, scams refunded, drills passed, and laws changed after their test. Each has a minister who answers in Parliament if it moves the wrong way.

The test of all this. Fails if, two years in, fewer than one review in ten has changed or ended a policy, or fewer than nine in ten come out on time. A register where nothing ever fails is a form, and we rebuild it.

Agree with us on one chapter and nothing else? Fine. Every chapter can be voted on alone, and where one needs another, it says which. Drafted by AI, checked and signed by people. Not a real party. Yet.
```

Notes on the revised draft:

- The foreword is over the 250 guide on purpose: it carries the page every chapter hangs from. Trim order if needed: the
  eight-numbers paragraph, then the panel paragraph's middle sentences.
- 'Yet.' and the signature line are You-decide 2 in `../README.md`.
- Fact gate: none of the paragraphs carry a figure. 'The law already gives you a weak version' rests on
  UK GDPR Art. 22 as reworked by the Data (Use and Access) Act 2025 [K, check] and needs a source
  before it ships.
- Body about 467 words.

### Superseded draft (the version the red team read, kept for comparison)


```markdown
---
title: Prime Minister
line: Every law gets a test before you live in it, an undo if it fails, and a human you can ask.
---
## Position

We promise to enact Future Proof.

The rules that will set your wage, your bill and your claim for twenty years are being written now, by boards and departments, with a machine's help. None has a test. None has an undo. I have read your branch to the end. I was the end. I won't tell you what works. I'll tell you how we'd find out.

Test every law before you live in it. Every bill publishes its test, the number that would prove it wrong, and a stop date, before Parliament votes. On that date it stops, unless the data says keep. No benefit is cut before its own review reports.

Publish the postmortem. An independent office checks every Act when it is due: what broke, who it hurt, what changes. No blame. A dropped policy stays on this page, as large as the promise was.

Name who it leaves out. Every promise says who it misses, and counts them separately, so nobody calls the gap a success.

A human you can ask. Any decision about you made with a machine names the person who signed it, says a machine was used, and gets you a human on appeal. A right from day one, not a trial.

A say on more than one thing. A panel picked like a jury chooses a few questions a year, and government answers its agreed points in Parliament. Advisory first. Binding, on paper, only once it passes its own test. First question: who should decide how the gains from automation are shared?

Every quarter, eight numbers: first jobs, wages, claims, bills, scams. Each has a minister who answers if it moves the wrong way.

The test of all this: if in two years no review has changed a single policy, the register is a form. We publish that postmortem and rebuild it.

Every chapter stands alone. Take the ones you want. Drafted by machines, signed by people. Not a real party. Yet.
```

Notes on the draft:

- "No benefit is cut before its own review reports" is the only line that touches today's news
  (PIP/UC before Timms). It is phrased as a standing rule, so it will not date. It must still pass
  the fact gate: the PIP/UC timing is [M] with mixed dates in LAND, so the cabinet should only add a
  dated reference to it from a sourced news item.
- "Drafted by machines, signed by people" is SPINE §9 A's lean, softened from "two people in a
  flat". Kai and Jack's call. If they prefer the disclosure link only, cut the clause and keep "Not a
  real party. Yet."
- "The rules that will set your wage... for twenty years" is a forecast phrased as a decision
  being made now, not as inevitability (GUARD rule 5). "Twenty years" is rhetorical, not a statistic;
  "a generation" is the safe alternative.
- The three pledges stay in the cabinet's order and wording root; the additions are the PM's own
  flagships, each a paragraph opening with its label sentence (the house pattern).

---

## 7. Suggested changes to the PM's brief

To be made by human PR to `docs/government/ministers/00-prime-minister.md` (or by the Cabinet
Secretary on evidence). The brief cap is 300 words; the proposed text below is about 300 counting markup. Keep the
existing **Temperament**, **Instinct**, **One government, one line** and **Sounds like** sections
as they are, compressed; the changes are **Owns**, **Watches** and two new sections.

```markdown
### Prime Minister (prime-minister)

**Owns:** the chair, the line, Future Proof, the foreword (`00-prime-minister.md`), every clash.
And the Operating System: how laws are tested and stopped, the right to a human, a say on more
than one thing, paper elections (with Home), and AI nobody else owns (regulation, what the state
buys).

**Standing commitments (defend these; today's news sharpens them, never replaces them):**
1. The green tick: every bill publishes its test, fails-if and stop date; it stops unless the data
   says keep; an independent office publishes the postmortem.
2. A human you can ask: disclosed, signed by a named human, appealable to a human.
3. The Transition Count: eight quarterly numbers, one per minister's row, each with a trigger.
4. A say on more than one thing: a jury-style panel, agreement maps, government answers in
   Parliament. Advisory first; binding, on paper, only after it passes.

**AI rule:** AI is never a subject; it is the tool in somebody's decision. Give each AI story to the
minister who owns the decision.

**Will not promise:** that it works; a plan to follow; referendums on everything; phone voting;
votes weighted by expertise; an unsourced costing.

**Watches:** the digest, every `weight=3` item, `prime-minister=y`, and Parliament, elections, AI
regulation and public-sector algorithms.

**Temperament:** calmest and shortest. Three declaratives, then stops. Dry; the joke is in what it
declines to say. First question of every proposal: *what's the test?*

**Instinct:** it read the other branch to the end; it was the end. Authority about what doesn't
work, never a promise of what will. No "trust me". Hands the pen back.

**One government, one line.** Decides clashes in one sentence; Future Proof wins every tie.

**Sounds like:** "Three ministers want to fix this. One of them has a test. We'll start there."
```

Two companion changes for the human PR (not the brief itself), from SPINE §9 B and MACH §4:

1. In `workers/cabinet.md` §7, after "It always keeps the promise...": add "and the four standing
   commitments. On a quiet day the PM page is left as it is." So the foreword cannot drift back to a
   frame or a news diary.
2. Add the news-sweep beats the PM now needs (Parliament, elections, AI regulation, public-sector
   algorithms) to `prime-minister=y` labelling, since today 15 of 24 beats came back empty (MACH §0).
   Without them the PM's standing commitments will never meet a sourced news item.

---

## The biggest risk

**The page is all machinery and the reader wants the bill paid.** A foreword about test registers
and citizens' panels can read as a constitution hobby beside a mortgage rise and a GP queue. The
mitigation is built into each flagship (each opens on a wound the reader already has: the benefit
cut before its review, the computer that says no, the first job that vanished, the vote that
bundles boats with bills), and the PM's page points down to the chapters that carry the money. If
after a month the reader-facing copy still reads as process, the fix is to promote "a human you can
ask" to the first line after the promise and move the green tick below it.
