# Red team: the policy wonk

2026-11-05. A red-team pass on `spine.md` and the ten files in `ministers/`, read as an ex-Treasury,
ex-IFS, ex-No.10 policy unit hand would read a draft manifesto the week before the launch. Not a
ruling. Nothing here touches `docs/government/`. Where I cite law or precedent from memory it is
marked **[K]**; [K, check] means I am fairly but not fully sure and it must be sourced before anyone
relies on it (the fact gate, X12, applies to this file too).

**The verdict in one paragraph.** The spine is the best thing in the folder, and the policy contract
(eleven fields, three gates) is a real idea that no British party has. The ten pages are well
written. But taken together they are **not yet one plan for the AI transition. They are about 45
flagships, roughly 40 of them pilots, run by ten departments with no shared sequence, no trial
office and no fiscal envelope.** About a third of the flagships duplicate one another (three host-town
compacts, two windfall levies, six "rights to a human" with five different deadlines, seven
different "counts"). The party's own economic answer to "who gets the gains" (the Public Slice) only
bites where the state gives a subsidy, and the Energy page abolishes most of those subsidies. And
several of the mechanisms are drafted in a way an IFS economist, a parliamentary clerk or a
government lawyer would take apart in an afternoon: "stops unless the data says keep" (data cannot
decide; Parliament votes), chapter-by-chapter treaty ratification (you cannot ratify half a
treaty), DNO purchase at regulatory asset value (A1P1 and investment-treaty exposure), a First Rung
Count built on payroll records that hold no occupation code, and a dozen "fails if" windows far
shorter than the effect they are meant to detect. All of it is fixable, and the fixes mostly make
the document *smaller*, which is the other thing it needs.

---

## 1. The top ten findings (ranked by damage if published as is)

1. **There is no fiscal envelope, so the IFS will write one for you.** The spine bans costings
   ("Never a costing we can't source"), and each page says "no figure". But a real manifesto is
   judged on its money annex, and this one has real spending in it: the W&P bridge, the 28-day
   human review, the NHS one-working-day human route, Home F5's "named officer for every reported
   crime", council housing borrowing, a multi-billion DNO purchase, Switch List fallbacks, the PIP
   pause, the NI holiday. Nobody has added them up or said which fiscal rules the party keeps. Fix
   in §3.
2. **"It stops unless the data says keep" is constitutionally wrong and politically dangerous.** It
   is the party's catchphrase (spine line 107; Energy draft "Every rule stops after five years
   unless the data says keep"; Education draft; Housing draft). Data does not decide; Parliament
   does, and no statute can stop a future Parliament renewing or repealing anything. Written this
   way it reads as technocracy-by-dashboard, which is the bad branch's handover. Fix: **"It stops on
   its date unless Parliament votes to keep it, on the published review."** Same number of words in
   the pub version: "It stops unless MPs vote to keep it, with the results in front of them."
3. **About 40 pilots, no trial office, no sequence, and the same few volunteer areas in all of
   them.** Count them: PM 4, Chancellor 5, Foreign 2, Home 5, Education 5, Defence 3, Health 4, W&P 6,
   Housing 4, Energy 4. At least seven of them want "two regions" or "two volunteer combined
   authorities" (Rung Fund, NI holiday, bridge, say-before-the-saving, second go, Plant Rule,
   windfall delivery). England has about a dozen mayoral combined authorities [K]. The same
   enthusiastic mayors will volunteer for everything, every trial contaminates every other, and the
   Evaluation Task Force (a few dozen people [K, check]) cannot run them. Fix: one Trials Office
   under the PM, a published portfolio of at most eight trials in year one, randomised assignment.
   §4.
4. **Most trials as designed cannot detect their own effect.** "Two areas against matched areas"
   is n=2 clusters: no statistical power, and volunteering is itself the confound (the firms that
   volunteer for "a say before the saving" are the firms that were going to share the saving
   anyway). Several "fails if" clauses test against "any monitored group does measurably worse"
   (Health F1, Home F4): with enough subgroups, one will be worse by chance, so the tool fails
   automatically. Fix: stepped-wedge randomisation among volunteers (Health already does this,
   copy it everywhere), many small clusters not two big ones, pre-registered non-inferiority
   margins, subgroup tests limited and powered. Say "everyone gets it; the order is drawn by
   lot", which also kills the postcode-lottery charge better than amendment 1 does.
5. **Fails-if windows are shorter than the thing they measure, so the party is designing its own
   failures.** Housing F1: CPO-led council building must be "completing social-rent homes both
   faster and at lower cost" by year three; a CPO from resolution to vesting typically takes two to
   four years before a spade goes in [K]. Energy F1: fails if "no qualifying project in the trial
   region reaches connection in 24 months"; 100MW+ connections are years-long queues under any
   tariff [K]. Education Rung Fund and the W&P say are judged at 24 months on earnings. Fix: every
   trial gets an **interim process measure** at 18–24 months (sites acquired, contracts signed,
   applications made) and an **outcome measure** at the date the effect can physically appear,
   with the sunset after the outcome date, not before it.
6. **"Who gets the gains" has no working mechanism.** The spine's "Yours" rests on the Public Slice
   ("where public money builds the machine, the public owns a slice"). But Energy F1 says data
   centres "never get a discount" and pay "full shallow and deep connection costs"; the Chancellor's
   own leaves-out admits "most AI used in the UK runs on servers abroad". So the slice applies to a
   shrinking pool of subsidies on a minority of the compute, and the dividend fund will be tiny for
   a decade. The thesis says AI decides "who earns what for a generation"; the money chapter answers
   with a stake in a few Growth Zone deals. Missing: any answer on **AI rents earned in the UK by
   foreign firms** (where profits are booked and taxed: the Digital Services Tax, Pillar Two, transfer
   pricing) and on **ownership through pensions** (W&P's pass-through voting, buried as a secondary
   commitment, is the most scalable ownership idea in the folder). Fix in §3.
7. **"Automation redundancy" is the load-bearing definition of five policies and it cannot be
   verified.** The HR1 box (W&P F1), the say (W&P F2), the bridge (W&P F5), the paid places (Education
   F4c) and the Chancellor's Level all key off whether a job was lost "to a machine". Once the box
   triggers a cost (a 60-day hold, a bridge contribution), firms stop ticking it, and "undeclared
   automation found on audit is treated as declared" asks an auditor to prove causation inside a
   restructuring. The bridge also creates a horizontal-equity problem a tribunal will hear about:
   two people made redundant on the same day get different benefits depending on the employer's
   story. Fix: keep the box **as a statistic only** (no cost attached, so it stays honest); make the
   bridge an earnings-related top-up for **all** redundancies after two years' NI, with the employer
   contribution scaled by firm size or by redundancy volume, not by declared cause.
8. **The same policy appears three times with three different contents.** Host-town compacts:
   Energy F2 (local generation share, bill discount, water cut first, local panel), Housing F2
   (council writes it, residents vote, jobs, water, business-rate share), Chancellor F2 (equity into
   a *national* fund, host town paid first), and Home wants the same rule for asylum sites. Windfall
   levies: Chancellor F4 (any sector, onto bills by three routes in three regions) and Energy F3
   (tighten the Electricity Generator Levy, onto the standing charge, prepayment first). Rights to a
   human: PM "fixed time set by the trial", W&P 28 days, Health one working day, Housing ten working
   days, Home "a set time", Education unspecified. A reader who reads two pages finds two
   governments. Fix: §2's consolidation table; one owner each.
9. **Several mechanisms break UK law or international practice as drafted.** Chapter-by-chapter
   ratification of trade deals (Foreign F3); DNO purchase at RAV (Energy F4); an Act of Parliament
   per police technology (Home F4); regional VAT trials on domestic energy (Chancellor F4); a Treasury
   "receipt" on every MPC decision (Chancellor F1); the Rung Fund's age-based charge (Equality Act).
   Each has a lawful version. §5.
10. **Measurement is loaded onto an ONS that cannot currently carry it.** The PM's Transition Count
    (eight new quarterly series with statutory triggers), Education's First Rung Count, W&P's HR1
    statistic and Housing's Roof Count all land on the ONS, several of them validated "against the
    LFS", when the Labour Force Survey's response collapse has been the ONS's biggest credibility
    problem of the decade [K, check current status of the Transformed LFS]. And the First Rung Count's
    data source is wrong: "HMRC payroll records (which already carry age, employer and start date)"
    is true, but the count is promised "by occupation", and PAYE RTI carries **no occupation code**
    [K, check: HMRC has consulted on collecting hours and occupation; status unknown]. Fix: the count
    is by **industry** (SIC, which payroll can be linked to) and by town, with occupation added only
    if and when RTI collects it; and consolidate all counts into the one Transition Count (§2).

---

## 2. Coherence: one plan or ten essays?

**Honest answer: ten good essays stapled to a strong spine.** The spine's arc table (eight rows,
one owner each) is the right skeleton, and the PM's Transition Count is the right instrument to make
it real. But each minister was asked for five flagships and delivered five, so the arc's eight rows
carry 45 flagships, and the reader cannot find the eight.

**The "every plank stands alone" claim is false and should be softened.** The spine (§4 Stage 0)
and the PM's draft ("Every chapter stands alone. Take the ones you want.") promise composability.
But W&P F2 and F5 cannot run without W&P F1's box; every sunset depends on the PM's Office for
Postmortems; the Slice depends on the Ledger to value anything; Home F1's pressure fund depends on
Housing's supply; Energy F2 depends on the PM's Stage 2 panels; Foreign F1 and Defence 2.2 share one
pot of money. Composition over inheritance means **clean interfaces**, not **no dependencies**. Fix
the line to: *"Every chapter can be voted on alone. Where one needs another, it says which."* and
publish a one-page dependency map. That is the more honest piece of software engineering anyway.

**Consolidation table (one owner each; everyone else cross-refers in one sentence):**

| Duplicated thing | Where it appears | One version, one owner |
| --- | --- | --- |
| Counts and registers | PM Transition Count; Education First Rung Count; W&P HR1 statistic; Housing Roof Count; Home monthly "real size"; Chancellor Ledger; Foreign till receipt; Defence contracts register | **Two instruments only.** The Transition Count (ONS, eight rows, includes first rung, automation redundancies, roofs) and the Ledger (independent unit; Foreign's receipt and Defence's register are columns in it). Home's monthly note stays as communication, not policy. |
| Right to a human | PM F2; W&P F3; Health F3; Housing F3; Home F4d/F5; Education 2.5 | **One framework statute** (PM), built on the Data (Use and Access) Act 2025's automated-decision safeguards (UK GDPR Arts 22A–D [K, check numbering]), with sector deadlines set by schedule: benefits 28 days, clinical same/next day, tenancy 10 days, policing at the stop. Data protection is reserved, which also solves the devolution problem. |
| Host-town compact | Energy F2; Housing F2; Chancellor F2; Home (asylum sites) | **Housing owns the compact** (planning is the legal hook). Energy sets the grid and water floor inside it; Chancellor sets the national/local split in one published formula. Asylum sites: a different instrument (Home F1's pressure fund), do not merge. |
| Windfall levy | Chancellor F4; Energy F3 | **One Windfall Act (Chancellor)** with an electricity schedule (Energy's EGL tightening) and an oil-and-gas schedule (the EPL). One hypothecation rule: standing charge, prepayment first. Drop the three-route regional delivery trial (§5). |
| Critical-infrastructure resilience | Foreign F1 Switch List; Defence 2.2 Run it by hand; Energy grid drill; Defence 2.3 Fixable here | **One programme**, and the lead is not Defence or the FCDO: civil CNI resilience sits with the Cabinet Office's resilience function, the lead government departments and NCSC [K]. Put it under the PM as "the Switch List and the drills"; Defence keeps military procurement (2.3) and the lethal-force rule. Also, both Foreign and Defence spend "the resilience slice of the defence uplift": the same pound twice. |
| Retraining | Education F4; W&P F2 menu; W&P F5 condition | Education owns courses; W&P only says "retraining for a job that exists". Already proposed by Education; enforce it. |
| AI-saved time | Health F2; Education 2.5 | One cross-government sentence in the PM's procurement gate, as Education proposes. |

**After consolidation the manifesto has about 20 flagships, which is still too many for a
front page.** Real manifestos lead with five or six. Proposal: the PM's foreword names **six
pledges**, one per arc cluster, each with its test box:

1. A human you can ask (rights statute, all sectors) — rows 3, 8.
2. Every law with a test and a stop date (Test Register + Office for Postmortems) — row 8.
3. The Transition Count (one statistic, eight rows, MPC-style open-letter triggers) — all rows.
4. A say before the saving, trialled; the bridge for anyone made redundant — row 2.
5. Households first on the grid; the host town writes the compact — row 4.
6. Keep the bottom rung (Rung Fund trial; learning time) — row 1.

Everything else sits in chapters. That is what makes ten pages read as one plan.

---

## 3. The money: what a Treasury reviewer would demand

**3.1 A fiscal statement, without inventing costings.** Keep the ban on fake figures, but publish
three things the IFS will otherwise publish for you, badly:

- **Which fiscal rules the party keeps.** Say it: the current-budget balance rule and the debt
  (or PSNFL) rule, with the OBR scoring every measure. Without this sentence every opponent says
  "they'd borrow for all of it".
- **A direction-and-band table.** Not "£3.2bn", but bands from sourced analogues: *small* (under
  £100m a year: Test Register, Ledger unit, HR1 box, Transition Count, contracts register),
  *medium* (£100m–£1bn: 28-day benefit reviews, NHS human route, bridge at national scale, Switch
  List fallbacks), *large* (over £1bn: council housing borrowing, DNO purchase, any national roll-out
  of Home F5). Each band from a named comparable. That is honest and checkable, which is the brand.
- **The aggregate test.** One pre-registered fiscal fails-if for the whole programme (for example,
  total new day-to-day spending above X% of the envelope pauses new roll-outs). The party that
  tests everything must test its own budget.

**3.2 The Plant Rule is mostly the status quo.** Chancellor F5: "a ring-fenced investment envelope
outside the day-to-day balance rule". Public investment is already outside the current-budget rule;
the binding constraint is the debt rule and the gilt market [K]. As drafted, a Treasury reader sees
a relabelled capital budget plus a sector-price brake that does not exist in any statistic at the
needed granularity (sector price indices lag by quarters and move for many reasons). Fix: say what
is new (each line names its idle capacity; a published brake), concede what is not ("investment is
already outside the day-to-day rule; the difference is the brake"), and use an existing series
(ONS construction output price indices [K]) for the first brake.

**3.3 The Ledger on the Bank is a market risk.** Chancellor F1(b): "every MPC decision (the
Treasury's analysis, not the Bank's: the Bank stays independent, we print the receipt)". A Treasury
distributional verdict four weeks after every rate decision is, in market eyes, a running political
commentary on the MPC. It does not break the Bank of England Act 1998, but it erodes the convention
that the Treasury does not comment on decisions, at the moment gilts are most sensitive (rates rose
today). Fix: ask the Bank to publish distributional analysis in its Monetary Policy Report, as it did
for QE in 2012 [K]; the independent Ledger unit covers fiscal events and public deals only, plus one
**annual** look at monetary policy.

**3.4 The Level's NI holiday has a British precedent the page omits.** The Regional Employer NICs
Holiday (2010–13) for new businesses outside London and the South East was badly undersubscribed
[K, check figures]. Freeport employer NICs relief is the live precedent for place-based NIC relief
[K]. Cite both: the first as the warning (deadweight and take-up), the second as the legal vehicle.
"Net new entry-level hires" also needs a baseline rule, or firms churn staff to manufacture "new".

**3.5 The Slice values the unvaluable.** Chancellor F2 converts "grid priority" and "planning
fast-track" into equity. Planning permission is not a subsidy, and a connection-queue reorder is not
a transfer the Subsidy Control Act 2022 recognises [K]. Limit the slice to **cash, discounted
power, public land and guarantees**, which a valuer can price. And fix the thesis gap (finding 6)
with one or both of: (a) a sourced position on taxing AI profits earned in the UK (DST, Pillar Two;
the Chancellor's page should own it, as a judgement call if necessary); (b) promote W&P's pension
pass-through voting to a Chancellor flagship ("you already own a slice through your pension; get
the vote that comes with it") and add a test.

**3.6 The asymmetric ratchet.** W&P F4: "Every welfare reduction carries a two-year sunset." PM
clash note: tax measures "do not auto-stop". So cuts sunset, rises and tax changes do not. That
contradicts amendment 3 ("the test is neutral"), and a hostile reader will call it a one-way
ratchet for spending. Fix: every *new* measure that changes anyone's income by more than a threshold,
up or down, tax or benefit, carries the same review-and-renewal vote. Tax keeps a review date rather
than a stop if the Treasury wins the argument, but then say so on the W&P page too.

---

## 4. Delivery and sequencing: the plan a No.10 unit would draw

Future Proof's own order of work is "measure first, test second, roll out last" (W&P §2). The
manifesto should be sequenced the same way, and say so in the foreword: **"The first tests."**

- **Day one (no legislation):** publish the contract for every pledge (Stage 0); standing order for
  the Test Register on government bills; HR1 automation box (a form change); PIP four-point rule
  paused (a commencement decision); commission the ONS for the Transition Count; set up the Trials
  Office in the Cabinet Office, absorbing the Evaluation Task Force.
- **First session (year one, statute):** one constitutional bill (Office for Postmortems, Transition
  Count triggers, right-to-a-human framework, citizens' panel); one money bill (Ledger unit, Windfall
  Act, Slice terms in Growth Zone deals). Two bills, not ten. Every department's trial runs under
  existing pilot powers where they exist (Welfare Reform Act 2012 s.41 allows UC pilot schemes for
  up to three years in specified areas [K, check scope]; Jobseekers Act 1995 pilots [K]).
- **Year one, trials:** at most eight, chosen from the six front pledges, stepped-wedge where
  possible, assigned to areas by lot from a volunteer pool so no area carries more than two.
- **Years two to three:** interim measures reported; outcomes for the short-cycle trials (benefit
  review times, scam refunds, Ward Test).
- **Years four to five:** long-cycle outcomes (housing completions, DNO comparison, Rung Fund
  earnings); renewal votes on the published reviews; Stage 3 ballots only if Stage 2 passed.

**State capacity is the missing chapter.** Every flagship assumes a civil service that can run
pre-registered trials, a DWP that can find decision-makers for a 28-day review (versus a 79-day
mandatory reconsideration today [M]), forces that can give every crime a named officer, and an ONS
that can produce eight new series. Nobody owns the machine that delivers the machine. Give the PM a
standing commitment on it: the Trials Office, evaluation money reserved inside every programme
budget (Health already proposes "a few per cent of contract value": generalise it), and the state's
own use of AI under the procurement gate. That last one is a gap in its own right (§7).

---

## 5. Legality and the constitution, mechanism by mechanism

| Line as drafted | Problem | Lawful fix |
| --- | --- | --- |
| Spine §2.1 field 8, and every page: "it stops unless the data says keep" | Data cannot decide; Parliament cannot bind successors; reads as rule by dashboard. | "It stops on its date unless Parliament votes to keep it, on the published review." Office for Postmortems advises, never decides. |
| PM F1(a): "a bill may not have its second reading until its Test Register entry is published" | Fine as a Commons standing order (proceedings are internal, Bill of Rights art. 9). Not enforceable as statute against a future Commons. | Say "by standing order", and add the Lords equivalent. The PM page already does; make the foreword match. |
| PM F4 / spine Stage 3: "binding, on paper" issue ballots | UK referendums are advisory unless a specific Act provides otherwise [K]. | "Binding" = an Act per ballot committing implementation, under PPERA 2000 conduct rules. Say "Parliament promises in law to act on the result". |
| Foreign F3(c): "Parliament gets a vote on deals chapter by chapter" | Treaties are ratified whole; bilateral FTAs do not allow partial ratification or reservations. Rejecting one chapter rejects the deal and weakens the UK's hand in the room. | Vote on the **negotiating mandate** up front and on the whole deal; chapter-by-chapter **scrutiny** with a published impact assessment per chapter; a statutory review clause. Keeps the composition idea where it is lawful (scrutiny), drops it where it is not (ratification). |
| Foreign F2: rule says "before the UK joins a sanction ... it publishes"; objection answer says "it comes out after the decision is made, not before" | The page contradicts itself. | Pick "after": publish the expected household cost within 30 days of the decision, with the six- and twelve-month check. "Before" hands an adversary the price list. |
| Energy F4(a): acquisition "at a value set by an independent valuer under the regulator's existing asset-value framework" | DNOs trade at a premium to RAV [K]. Compensation at RAV invites A1P1 (ECHR) challenge and, where owners are foreign, investment-treaty claims (UK Power Networks' owners are Hong Kong-based [K, check; and check whether a UK–Hong Kong BIT applies]). | "At fair market value, set independently." State that this costs more, and that the test compares returns to the public *net* of that premium. Also: say how the purchase scores against the debt rule. |
| Energy F4(b): failed water firms stay public "with creditors taking the losses the administration determines" | The Special Administration Regime is designed to rescue and transfer, not to nationalise or impose haircuts [K]. | Needs primary legislation to retain the company publicly; say "we would legislate". Losses fall by insolvency ranking, not by administrator's choice. |
| Energy F1(a): large-load class pays "full shallow and deep connection costs" | GB demand charging is largely shallow; a class-specific deep charge must survive non-discrimination duties in licences and codes [K]. | Route it through an Ofgem Strategic and Policy Statement direction and code modification, or primary legislation if needed; say which. |
| Chancellor F4 test: windfall money "put on bills three ways in different regions (a cut in VAT on domestic energy ...)" | VAT is a UK-wide reserved tax; regional VAT rates on domestic fuel would need legislation, and Northern Ireland's VAT position under the Windsor Framework complicates any UK-wide change [K, check]. | Test only the two delivery routes that can legally vary by area (standing-charge credit, flat credit via suppliers), or test VAT nationally against forecast. Keep the "we test the VAT cut" instinct; move it to a national before/after. |
| Chancellor F1(b): Treasury distributional "receipt" for every MPC decision | Legal, but a convention breach with market cost. | See 3.3: the Bank publishes it; the Ledger covers fiscal decisions. |
| Home F4(a): "no AI system makes or prompts a decision about a member of the public without an Act naming it" | An Act per technology is unworkable (ANPR, triage software, risk tools, translation, case management all qualify). It also means no technology can be trialled before its Act, which contradicts F4(b). | One framework Act for police biometrics and decision tools, with each technology class approved by affirmative regulations, an independent commissioner (the IPA/RIPA model [K]), and the trial authorised by the regulation. Scotland's biometrics commissioner is the domestic precedent [K]. |
| Home F1(c): "no discretionary route's planned number grows faster than the housing, GP and school capacity funded for it" | Most routes are demand-led (study, family, many work routes); family is constrained by Article 8 ECHR; nobody can attribute GP capacity to a visa route. The fails-if ("planned numbers miss the outturn ... two years running") is then near-certain to trip. | Cap only the routes the state actually controls (sponsored work, student dependants), tie a per-head **infrastructure charge** on those routes to the host-area pressure fund, and publish a **forecast**, not a plan, for demand-led routes. Then the straight answer ("where the homes aren't built, the number falls") is true for the routes it covers, and the page says which. |
| Education F2: charge on large employers whose under-25 starts fall below their own baseline | Pushes employers toward age-based selection (direct age discrimination is only lawful if justified, Equality Act 2010 s.13(2) [K]); and it is pro-cyclical: in a downturn every firm's youth hiring falls, so the charge lands hardest in a recession, which is roughly now (unemployment at a five-year high, Bank Rate rising). | Measure the shortfall **relative to the firm's sector and region trend**, not its own history; take legal advice on the age justification, and frame the aim (legitimate aim: entry to the labour market) in the statute. |
| W&P F2: "an automation redundancy cannot proceed until an agreement ... is signed by the elected reps, or 60 days pass and an independent arbiter ... rules" | In a *voluntary* trial this is a contract, not law; fine. But it is longer than the statutory 45-day consultation and stacks on it. | State it as "inside the 45 days where possible; 60 at most", and say it binds only firms that signed up (or that took Growth Zone support with it as a condition, which is the better test). |
| Defence 2.1(d): human-decision rule as an arms export licence condition | Lawful under the Export Control Act 2002 [K]; will collide with allied joint programmes. | Keep; Foreign's interface already flags it. Add that joint programmes are assessed case by case and listed. |
| Health F2: "Clinical posts may not be cut on the strength of an AI saving for the term of the licence" | Unenforceable: no trust records why a post went. | Make it a reporting duty plus a pass-through rule: hours saved are published and the board must show they went to patient-facing time; the licence is not renewed if they did not. |

---

## 6. Is each Future Proof mechanism implementable?

- **Pilots: yes, with three conditions.** Randomise among volunteers (stepped-wedge), run many small
  clusters rather than two regions, and cap the portfolio. The UK has the tools (ETF, What Works,
  pilot powers in social-security law) and a bad habit of not using them, which is the honest
  pitch.
- **Sunsets: yes, if they bite through a vote, not a dashboard.** The PM page has the right design
  (sunset + mandatory review + renewal vote; Texas Sunset Commission; the Coronavirus Act lesson).
  Copy that wording into every page and into the spine's field 8.
- **Ledgers: yes for fiscal events and public deals; no for monetary policy.** Commercial
  confidentiality of Growth Zone deals is the real obstacle; the Chancellor's "disclosure as a
  condition of public money" is the right answer and should be on the page.
- **Issue-voting: the staged design is sound and the best-evidenced part of the folder.** Two
  gaps: say how the panel's questions get on the agenda without a government veto (otherwise it is
  a consultation with a lottery); and answer the obvious question, *what happens when a Stage 3
  ballot result conflicts with a Commons majority?* (Answer: the Act that calls the ballot says the
  government will legislate; MPs keep the final vote; that is what "paper stays for the big ones"
  means.)
- **The Transition Count's triggers: yes, and there is a perfect precedent nobody cites.** The
  Bank's open-letter rule (inflation more than a point off target obliges a public letter to the
  Chancellor) is exactly a pre-registered trigger obliging a named official to explain [K]. Cite it;
  it makes the idea feel like the British constitution rather than a hackathon.

---

## 7. What is missing entirely

Ranked by how fast a journalist would notice.

1. **AI copyright and the creative industries.** The single loudest AI fight in British politics in
   2025 (the Data (Use and Access) Bill's training-data amendments [K]), and BadCode is an art
   collective. No minister owns it. It is a "who gets the gains" question in its purest form: whose
   work trained the model, and do they get paid? Give it to the Chancellor (rents) or Education
   (culture), as a judgement call if need be.
2. **Where AI profits are taxed.** See finding 6. Without it the gains chapter is about subsidies,
   not profits.
3. **Growth and productivity.** Every flagship is distributive or defensive. There is no answer to
   "how does the UK get any of the gains in the first place?": AI diffusion into small firms, public
   sector productivity, skills supply for the build-out, compute access for British firms and
   universities. The spine says "pro-abundance"; no page plants anything except council homes. One
   standing commitment, probably the Chancellor's (the Plant Rule's first AI line), would answer it.
4. **The state's own use of AI.** The PM's procurement gate covers what the state *buys*; nothing
   says what the government will *do* with AI itself (casework, correspondence, policy drafting),
   which is where most early public-sector change is happening [K]. For a party run by AI ministers
   this is a glaring gap and a gift of a pledge: "the state uses AI under the same contract it asks
   of everyone".
5. **Local government finance.** Housing "owns places", and nearly every trial runs through
   councils, but councils are issuing section 114 notices and living on exceptional financial
   support [K]. A council that is bust cannot volunteer for anything. One line on council funding
   (or an explicit "Not ready") is owed.
6. **Courts and justice.** Home covers police and prisons only in passing; the Crown Court backlog is
   the front-end failure the Home page itself describes ("the system at the back is full because the
   front stopped working") [K]. AI in courts (listing, transcription, sentencing tools) belongs in
   the right-to-a-human statute.
7. **Competition and market power.** Only Housing touches it (rent software). The concentration of
   foundation models, cloud and chips in a few firms is the "who owns the machines" question at the
   market level; the CMA's foundation-model work exists [K]. One Chancellor line.
8. **SEND, childcare, universities' finances, transport.** Each flagged "Not ready" or absorbed with
   nothing on it. Fine for a manifesto of tests, but list them in one "Not ready" box in the foreword
   so it reads as a choice, not an omission.
9. **The Union.** The spine's §9 J sentence ("UK-wide on money, defence, foreign, work and the
   Operating System; England-led on devolved services") is right and is not yet on any page. Also
   note: social security is devolved in Northern Ireland (parity in practice) and partly in Scotland
   [K], so "UK-wide on work" needs care for W&P's trials.

---

## 8. Page-by-page, harsh and short

**Spine.** Strong. Change field 8 ("stops unless the data says keep" → Parliament votes). Change
Stage 0's "Every plank stands alone" (see §2). Add a field 12 to the contract: **"Needs"** (which
other pledge it depends on). Add the fiscal statement (§3.1). Cut the ten pub sentences to the six
front pledges plus chapter lines.

**PM.** The best ministerial file. Three fixes. (1) The draft's "Every bill publishes its test ... On
that date it stops, unless the data says keep" → "unless Parliament votes to keep it". (2) Flagship 2's
scope, "made or shaped by an automated system", catches every spreadsheet; use the legal definition
of a significant decision based solely or substantially on automated processing, from the 2025 Act's
regime [K, check wording], and say we extend its safeguards, not invent them: "We are not inventing
the right; we are giving it a signature, a deadline and a test" is already the right line, so make
the policy match it. (3) Flagship 4 needs the agenda-setting rule (§6).

**Chancellor.** Five flagships is two too many; the Windfall Rule merges with Energy, the Plant
Rule shrinks to its honest new part (§3.2). The draft page's figure lines are good. "Income tax, NI or
VAT raised on working people in last week's Budget: none." is the most quotable line in the folder;
keep it. Add the fiscal-rules sentence and the AI-profits position.

**Foreign.** The Switch List is a civil-resilience programme in a Foreign Office coat; move it to
the PM (§2) and keep Foreign's half as *foreign* dependencies and the oil-stock analogy. Fix the F2
before/after contradiction. Replace chapter-by-chapter ratification (§5). Aid "has to beat cash" is
sound (and the best-evidenced idea on the page); keep it off the front page as proposed.

**Home.** The bravest page and the one most likely to blow up. F1 must be rebuilt around controlled
routes (§5) or, as the file itself suggests, become a labelled judgement call: a capacity rule
nobody can operate is worse than an honest judgement call. F4's "Act per technology" → framework Act.
F5 ("Every reported crime ... gets a named officer and a human answer within a fixed time") is the
most expensive line in the manifesto on no costing at all; keep it as the trial in two forces, and
take the national promise out of the draft. F3's 18-month sunset on a liability rule is perverse:
nobody invests in scam prevention for a rule that may vanish in 18 months; make the *scope* trial
(one scam type first) and the liability permanent once extended.

**Education.** The strongest problem statement and the smartest honest move ("nobody knows,
because nobody counts"). Fix the First Rung Count's data (no occupation in RTI; finding 10) and the
Rung Fund's baseline and age-law exposure (§5). "Learning time" is the most defensible pilot in the
manifesto; it needs a sample size, not just "a few towns".

**Defence.** The tightest page. Two problems: 2.2 (run it by hand) is not Defence's to own (§2), and
the "Fails if any fielded system cannot name its post" test is weak because naming a post is trivial;
the real test is the audit of decision time per engagement, which the page already describes, so
make that the fails-if with a pre-registered floor. "The 3% is already set" is [M] with conflicting
dates in LAND; with the NATO 3.5% core plus 1.5% resilience structure from 2025 [K, check], the page
must state which number it holds to and by when, or the IFS will.

**Health.** Strong; the stepped-wedge Ward Test is the model every other page should copy. Fix the
subgroup fails-if (finding 4), make F2's post-cut ban a reporting and renewal rule (§5), and connect
the Ward Test to what exists: NICE's Evidence Standards Framework and early value assessment for
digital tools, and the MHRA's AI Airlock [K]. Saying "we make the existing gate mandatory before a
national purchase" is stronger and cheaper than implying a new one. The one-working-day human route
for every AI-assisted clinical decision needs a scope (triage and diagnosis, not scheduling).

**Work and Pensions.** The heart of the party and the page with the most mechanism risk (finding 7).
Also: "Two in three people who take a PIP decision to a tribunal win" is not "a checker wrong two
times in three". Tribunal cases are a selected sample, and many succeed on new oral evidence; DWP
will say so within the hour [K]. Keep the number, drop the inference, or use the overturn rate at
mandatory reconsideration plus tribunal together, sourced. The source list cites "seven in ten" while
the page says "two in three": reconcile. F4's asymmetric sunset (§3.6). The pension pass-through vote
should be promoted (finding 6).

**Housing.** Land at existing-use value is the boldest and most historically British idea in the
folder, and the Levelling-up and Regeneration Act 2023 already allows hope value to be removed in
certain CPOs with ministerial confirmation [K, check]. So the honest pitch is "switch on and widen a
power Parliament already passed", which is far stronger than implying a new confiscation. Fix the
year-three fails-if (finding 5). Street votes: good choice for the "policy you'd expect us to
oppose"; the LURA power exists but needs regulations [K, check], which makes it a cheap first test.

**Energy and Climate.** Clear and reader-safe. Fix the DNO valuation (§5), say how the purchase
scores against the debt rule, fix the 24-month connection fails-if (finding 5), merge the levy with
the Chancellor's. "Every rule stops after five years unless the data says keep" in the draft
conflicts with the page's own three-year levy sunset and ten-year windfall Act; one sentence per
rule, or none. The "no North Sea drilling sets your bill" refusal is correct and rare; keep it.

---

## 9. What I would cut tomorrow

- Chapter-by-chapter treaty ratification.
- The regional VAT test.
- The Treasury receipt on every MPC decision.
- "An Act of Parliament" per police technology.
- Home F5 as a national promise (keep the two-force trial).
- The earnings-related bridge restricted to "automation" redundancies (make it all redundancies, or
  drop it).
- Every instance of "unless the data says keep".
- Four of the seven counts (fold into the Transition Count and the Ledger).
- Two of the three compacts and one of the two windfall levies.

The document that is left is shorter, cheaper to check, and harder to attack, which is the Future
Proof claim made good on itself.
