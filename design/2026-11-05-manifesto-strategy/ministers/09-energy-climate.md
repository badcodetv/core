# Energy and Climate: what the manifesto should say

> **Revised 2026-11-05 (closing pass).** The §6 draft page has been rewritten to apply the red team's fixes; the change list sits above the new draft, and the old draft is kept under it. Sections 1-5 and 7 onward are unchanged, so where they still say "unless the data says keep", read "unless Parliament votes to keep it" (see `../README.md` §2).

2026-11-05. Strategy for one post, fitted to `spine.md`. Not a ruling, and it changes nothing
under `docs/government/`; Kai and Jack decide, and the text below reaches the site only through the
cabinet's rolling PR or a human PR. Sources: the absorb pack (FP-A, MACH, GUARD, LAND), the brief
`docs/government/ministers/09-energy-climate.md`, and the live page
`docs/government/manifesto/09-energy-climate.md` (merged today in PR #5).

Confidence marks are LAND's: [H] [M] [L] [?]. **[K]** means background knowledge, not checked this
session. **No [K] or [L] item goes into public copy until it has a source URL and a grade** (spine
X12, the fact gate). The precedents in §2 are almost all [K], so that is the first job before any of
this goes public.

---

## 1. Mission

**The line (frontmatter):** *Households first on the grid, and what can't compete, the public owns.*
(70 characters, no colon. The spine's pub sentence, turned into one sentence.)

**The problem this post exists to prevent.** Arc row 4 in the spine: *the machines get the power and
the water first.* In the bad branch it comes in two bulletins. "The hosepipe ban does not apply to
the data centre" (F7). Then the grid operator, "now fully automated, classifies human households as
'legacy load'" (F8). Nobody switched the households off. They just slid down a queue, one sensible
decision at a time, until the queue had a name for them.

**Today's version of it, in the real news:**

- The Ofgem cap for Oct–Dec 2026 is **£1,723**, up about 4% [H]. January is forecast at about
  **£1,999** [L].
- **At the same time, the government is consulting on cheaper electricity for AI Growth Zones** [M].
  That is row 4 in a single decision: cheaper power for the machine while the household cap goes up.
- **Drax/Brookfield/Radiant have proposed a £20bn AI data centre** at a North Yorkshire power station,
  eventually more than a gigawatt [M]. Electricity is "the binding constraint" on the AI zones [M].
  Some reports say OpenAI paused Stargate UK over power costs [L].
- **OpenAI is writing its own "community compact"** for host towns [M]. The social contract is being
  drafted by the tenant.
- **Hormuz has been near-closed since late February.** Brent is about $110 [H], and energy is the
  main driver of inflation, which is back above 3% [M].
- **Reform promises "£500 off bills by 2030"** by scrapping VAT and green levies [H/M]. It is the only
  bill offer in the field, and it is aimed straight at our reader.

**Where it sits in the failure chain.** The link is *allocation without a chooser*. Grid capacity
and water are physical stock, and they are being handed out by a connections queue, a regulator's
formula and a consultation. No one has put the question to the people who pay the bill. The minister
exists so that before the queue fills, a rule says who goes first, who pays for the pipe, and who
owns what the public's bills built.

**Who decided (by act, never "AI" or "the market"):** the ministers who launched the AI-zone power
consultation; Ofgem, which sets the cap formula and the connection charging rules; the network
companies and the system operator, which run the queue; the water companies' boards and Ofwat, for
water. The data-centre developers are applicants, not villains. They ask for what the rules allow.

---

## 2. The flagship policies

Four flagships. They are composable: each stands alone, and the page says so. Together they answer
the four questions a reader would ask about a data centre arriving in their town. Who goes first?
Who pays for the pipe? Who gets the windfall? Who owns the thing nobody can compete with?

### Flagship 1: Households first on the grid

**The policy in one plain sentence.** In a shortage or a queue, homes, hospitals and the industry
already here keep their power first. The biggest new loads (data centres above a threshold, say
100 MW, to be set by the test) are switched down first, pay the full cost of their connection and
the reinforcement it needs, and never get a discount that is recovered from household bills.

**Why now.** The AI-zone cheaper-power consultation [M], the £1,723 cap rising toward about £1,999
[H/L], the £20bn Drax proposal [M], and electricity as the zones' binding constraint [M]. The
decision on who pays for the big taps is being made **this year**, by consultation. Once the
connections are signed, they are signed for decades.

**Future Proof mechanism.** Composition (tenet 1). The grid's charging rules get unbundled. Today a
household and a gigawatt campus sit in one socialised pot. We split out the large-load class so its
costs have their own address ("every pound has an address"). CI (tenet 2): the rule ships as a
tariff with a sunset and a review, not as a permanent Act.

**The policy contract.**
- *The wrong:* a family on a prepayment meter rations the heating in January. Up the road, a server
  hall signs a cheaper rate.
- *Who decided:* the consultation on cheaper power for AI zones, and the charging rules Ofgem
  approves.
- *The rule:* (a) a large-load tariff class: new loads above the threshold pay full shallow and deep
  connection costs, plus a minimum-demand charge so stranded reinforcement can't fall back on
  households if they leave; (b) a priority order in law for stress events, with large new loads
  interruptible first, under contract and paid for it; (c) no public power discount for any
  large load unless the public takes a stake (Flagship 2, and the Chancellor's fund).
- *The ledger:* developers pay more up front. Households stop underwriting their reinforcement.
  The money moves *from* compute balance sheets *to* the socialised network bill. The direction is
  clear; the size depends on how many campuses connect, and nobody has published it. We pledge to
  publish it.
- *The test:* the first qualifying connections in one network region (Drax, if it gets planning, is
  the natural first case) go on the new tariff. They are compared with the rest of Great Britain on
  household network charges per home, connection timelines and committed investment, over three
  years, with results published every year.
- *Fails if:* (pre-registered) household network charges in the trial region rise faster than the
  GB average *because of* large-load reinforcement. That means the tariff is too soft, and we tighten
  it. **Or** no qualifying project in the trial region reaches connection in 24 months while
  comparable projects elsewhere do. That means the tariff is pricing out investment we wanted, and
  we publish the postmortem and reset the level. Both results are published.
- *The undo:* the tariff expires after five years unless the review says keep. Contracts signed
  under it keep their terms, so nobody is stranded by the undo.
- *Who it leaves out:* smaller loads below the threshold (hospitals' own expansions, factories
  electrifying), which must not be caught by accident. They are counted separately. So are homes
  off the gas grid, who get nothing from a network-charge saving if their heat is oil or LPG.
- *Who signs:* the Energy minister's office in the fiction; Kai or Jack merging in the real world.
- *Status:* Draft.

**Scale, cost, how it's paid.** Close to zero public cost. It moves who pays; it doesn't add
spending. The risk is lost investment, and that is what the second fails-if measures. Honest
uncertainty: we don't know how much reinforcement the AI zones need. No published figure was
found this session [?].

**Strongest precedent.** US utilities facing the same rush have created large-load tariffs. The
best known: Ohio regulators' 2025 data-centre tariff for AEP, with a minimum-demand charge of about
85% over long contracts [K]. Texas SB 6 (2025) lets the grid operator curtail large new loads in
emergencies and makes them share connection costs [K]. Ireland is the cautionary tale: data centres
reached roughly a fifth of national electricity use, and the grid operator effectively stopped new
Dublin connections for years [K]. All three need a URL before use.

**Strongest objection and our answer.** *"You'll drive the AI industry to France and we'll lose the
jobs."* Answer: the jobs per £bn are few (LAND #13 [M]), and the test is built to catch exactly this
(fails-if, second clause). If it prices out investment we wanted, we publish that and change it.
What we won't do is pay to be chosen out of the household bill, because then we've paid for the
pipe *and* given the tenant the house.

### Flagship 2: The hosepipe ban applies to the data centre

**The policy in one plain sentence.** A town that hosts a compute campus writes the deal, not the
company. The deal sets a share of the new generation owned locally, discounted bills for the homes
nearest the site, water use metered and published, and the campus cut first in a drought or a
hosepipe ban.

**Why now.** OpenAI is drafting its own "community compact" for host towns [M]. The £20bn Drax
proposal is a real host-town negotiation this month [M]. The Growth Zones (Culham, the North East,
North and South Wales, Lanarkshire) are mostly pledged and not yet built [M], so the terms are
still open.

**Future Proof mechanism.** Composition, done locally. The town votes on its own compact, issue by
issue (the share, the water rule, the bill discount), using the spine's Stage 2 machinery: a
randomly selected local panel plus an agreement map. Data-driven: the water and power figures are
published monthly, so the compact can be checked.

**The policy contract.**
- *The wrong:* the hosepipe ban arrives in August, and the only thing in town that still gets all
  the water it wants is the building with forty jobs.
- *Who decided:* today, the developer and the planning committee, with a compact the developer
  writes.
- *The rule:* any campus above the threshold needs a host-town compact, agreed by a local panel and
  approved by the council (Housing owns the planning route). The compact sets a floor: (a) the
  community is offered a minimum share of any generation built to serve the site, to buy into or
  hold through the council; (b) a bill discount for homes within a set radius; (c) water and power
  use published monthly; (d) in a drought order or hosepipe ban, the campus cuts water before
  households do, and uses non-potable or recycled water where the site allows.
- *The ledger:* developers pay (equity offered, discount funded, water infrastructure built). The
  host town gains income and cheaper bills. The national fund's stake (Chancellor) and the local
  share must be split by a published rule, so nobody is paid twice and nobody is skipped.
- *The test:* the first two or three campuses to apply. Compared with campuses approved under
  today's rules on local bill levels, local ownership income, water use in dry months, and the
  share of residents who say they'd accept a second site (a survey, run before and after).
- *Fails if:* developers walk away from compact sites at a clearly higher rate than from comparable
  sites (pre-registered rate), **or** local panels draw a small, unrepresentative crowd (the
  LiquidFeedback postmortem). Either result is published.
- *The undo:* the compact requirement sunsets after five years unless kept. Compacts already
  signed run to their own terms.
- *Who it leaves out:* the next town along, which gets the pylons and none of the deal. It is
  counted, and the radius rule is tested on it. So are renters, who may not see a bill discount
  their landlord pockets. The discount goes to the bill-payer, and we measure whether it arrives.
- *Who signs:* Energy, with Housing for the planning route.
- *Status:* Draft.

**Scale, cost, how it's paid.** Paid by developers and the generation itself. Public cost is
administration, plus the local panels (small; spine Stage 2 budget). Uncertainty: what share of
equity makes a deal neither a giveaway nor a deal-breaker. That is the test's job.

**Strongest precedent.** Denmark required new onshore wind projects to offer at least 20% to local
people (2009–2020) [K]. The UK's own 2025 move to give households near new pylons money off their
bills, about £250 a year for ten years [K]. Scottish community-benefit funds per MW for wind [K].
Each needs a URL.

**Strongest objection and our answer.** *"Planning is slow enough already; you're adding a
referendum to every server hall."* Answer: it isn't a referendum. It's a compact with a fixed
floor, agreed by a small panel in weeks. It replaces the fight that delays sites today, a town that
was never asked and objects to everything. Our bet is that a town that owns a slice says yes faster.
If it doesn't, the test shows it.

### Flagship 3: Sell the free wind at the wind's price

**The policy in one plain sentence.** Old wind farms, solar and nuclear that are already built and
paid for, but sell their power at a price set by gas, pay a levy on the windfall while gas is high.
Every pound goes on cutting the standing charge, prepayment meters first.

**Why now.** Hormuz has been near-closed since February, Brent is about $110 [H], and gas sets the
electricity price in most hours [K]. So a war we didn't choose is paying low-carbon generators whose
costs haven't moved. Meanwhile the only bill offer on the table (Reform's £500, by scrapping VAT and
green levies [H/M]) pays for itself by cutting the green build. This takes the money from the
windfall instead.

**Future Proof mechanism.** Data-driven, with a switch. The levy is on only while a published gas
price is above a published trigger, and off automatically below it. CI: it is a temporary crisis
rule with a sunset that defaults to stop, unlike the Budget's habit of making permanent changes in
a temporary shock (LAND §6.4).

**The policy contract.**
- *The wrong:* "The wind is free. The sun is free. Somehow your bill went up." (the brief's own
  line). Your standing charge is the same whether you use a kettle or a sauna.
- *Who decided:* the market design that pays every generator the price of the last one switched on,
  which is usually gas, and the Treasury and Ofgem rules that leave old low-carbon output on that
  price.
- *The rule:* tighten the existing levy on extraordinary low-carbon generator revenue (or rebuild
  it on the same lines) while the gas trigger holds. Plants already on fixed-price contracts are
  exempt, because they already sell at the wind's price. Revenue is hypothecated, by statute, to a
  standing-charge cut, applied to prepayment and the lowest-use homes first.
- *The ledger:* owners of older low-carbon plants pay out of the windfall (the gap between their
  cost and the gas-set price). Households gain, the lowest users most. New projects are untouched,
  because they bid into fixed-price contracts.
- *The test:* run as a national rule (a levy can't sensibly be regional), compared against its own
  pre-registered forecast. Measured: revenue raised, the standing-charge cut actually delivered on
  bills, and new low-carbon investment committed versus the two years before.
- *Fails if:* raised revenue falls below half the published forecast (the previous levy undershot
  its forecast [K]), **or** the cut doesn't show up on prepayment bills within two quarters, **or**
  committed new low-carbon investment drops measurably against the prior trend for reasons the review
  traces to the levy. Then we publish the postmortem and drop it.
- *The undo:* switches off automatically below the gas trigger; sunsets after three years unless
  renewed after review.
- *Who it leaves out:* homes off the gas grid, on oil and LPG, who face Hormuz prices directly and
  gain little from an electricity standing-charge cut. They are named and counted, with a separate
  heating-oil measure for the Chancellor to test. So are people in heat networks and park homes,
  who sit outside the cap.
- *Who signs:* Energy, with the Chancellor for the hypothecation.
- *Status:* Draft. Judgement element: the trigger level is set by consultation and published in
  advance.

**Scale, cost, how it's paid.** Self-funding by design. Its size swings with the gas price, and we
won't print a figure we can't source. The pledge is the kill number, not a costing (GUARD tension
2). Honest uncertainty: a windfall levy depends on the windfall. If gas falls, the levy falls, and
so does the cut. Say that up front.

**Strongest precedent.** The UK's own Electricity Generator Levy (from 2023: 45% on extraordinary
returns above a benchmark price, CfD plants exempt) [K], and the Energy Profits Levy on oil and gas
(LAND §5, Moderate) [K]. The EU's 2022 inframarginal revenue cap did the same thing across member
states [K].

**Strongest objection and our answer.** *"Windfall taxes scare off the investors you need for net
zero."* Answer: new projects are exempt, and the test measures investment and drops the levy if it
bites. A plant built and paid for years ago, earning a war price, isn't an investment signal. It's a
lottery ticket the household bill is paying for.

### Flagship 4: Own what can't compete

**The policy in one plain sentence.** Where there is only one set of wires and one water main to
your door, the public owns them. We start with one electricity network region bought at a price
the courts and the regulator set, and a water company that fails comes into public hands instead of
being refinanced back onto the market.

**Why now.** The bill can't be switched away from (LAND #3 [H]). The reader already backs public
ownership of utilities: Reform's 2024 contract proposed 50% public ownership of utilities and
critical infrastructure, and majorities across parties back public water (GUARD §1; FP-A R20,
"avoid hard numbers"). Water companies' debts and sewage are a standing scandal [K; needs a dated
item before the cabinet uses it]. And the networks are about to absorb the biggest new loads in
their history (Flagship 1), so who owns the wires decides who books the return on that build.

**Future Proof mechanism.** All three tenets. Composition: ownership is unbundled by asset (the
monopoly wires and pipes, not the competitive generation or retail). Data-driven: one region first,
against the rest. CI: if it does worse, it can be sold back, and the contract says how.

**The policy contract.**
- *The wrong:* there is one pipe to your house. You can't shop around for a sewer. Its owners have
  paid themselves dividends while it leaked [K, needs a source], and you pay for it on the bill.
- *Who decided:* the 1989–90 privatisations and every regulator settlement since, which set
  allowed returns on assets that have no competitor.
- *The rule:* (a) acquire one electricity distribution region by negotiated purchase or statutory
  transfer at a value set by an independent valuer under the regulator's existing asset-value
  framework, funded by public borrowing against the network's regulated revenue, and run as a
  public company with a duty to keep bills down and publish everything; (b) any water company that
  enters special administration stays in public ownership rather than being recapitalised for sale,
  with creditors taking the losses the administration determines.
- *The ledger:* shareholders are paid the independently set value, not the price they name. The
  regulated return that went to dividends goes to lower bills and investment. Lenders to failed
  water firms take a haircut. The public takes on the borrowing, and in exchange owns a regulated
  income stream.
- *The test:* the public region against comparable private regions over five years: bills per home,
  minutes lost to power cuts, investment delivered against plan, cost of capital, and
  connection times for new homes.
- *Fails if:* (pre-registered) after five years the public region is worse than the median private
  region on both bills and reliability. Then we publish the postmortem and sell it back by the
  method written into the purchase law. Water is a *judgement call*: the principle (no rescue for
  shareholders), a review at five years, and the change-of-mind condition published in advance
  (public water costing households more than the comparable private firms).
- *The undo:* a sale-back clause written into the acquisition. Water's review at five years.
- *Who it leaves out:* customers of the other regions, who wait five years for the answer. They are
  told so, and they're no worse off than today (spine §2.2 amendment 1, the control group's floor).
  So are pension funds that hold utility shares, who get the independently set value, not a
  confiscation. We say that plainly, because the reader's pension may be one of them.
- *Who signs:* Energy, with the Chancellor for the borrowing.
- *Status:* Draft (electricity); Judgement call (water).

**Scale, cost, how it's paid.** The biggest number in this chapter, and we have no sourced figure
for it. One distribution region is plausibly a multi-billion-pound purchase [?]. It is paid by
borrowing against the regulated revenue the network already earns, so the bill-payers who pay that
revenue today become its owners. It is not paid from day-to-day spending. Rising Bank Rate (4.00%
today [H]) makes the borrowing dearer, and the test counts the cost of capital honestly. Water in
administration costs little up front, but running costs and the investment backlog are real.

**Strongest precedent.** Scottish Water has been publicly owned throughout, and Welsh Water runs as
a not-for-profit (Glas Cymru) [K]. The comparison with English firms is the natural test. Hamburg
voted in a 2013 referendum to buy back its grids, and Berlin bought back its electricity
distribution network in 2021 [K]: re-municipalising a grid is a thing cities have done, by a
public vote. Norway's state ownership of Statkraft and of its grid operator [K].

**Strongest objection and our answer.** *"Nationalisation means the Treasury on the hook and the
1970s on the phone."* Answer: one region, bought at a fair price set by someone who isn't us, tested
against the rest, with a sale-back clause written into the law. If the public version is worse,
you'll read the postmortem and get the private one back. Name another party whose nationalisation
comes with a receipt and a returns policy.

### Standing position on net zero (not a flagship, but the reader will ask)

Keep the target, and argue it as **security first, bill second, planet third**: "the wind doesn't
sail through the Strait of Hormuz." Add one rule that makes it Future Proof. **Every net-zero measure
that lands on a household bill publishes its effect on that bill before it starts, and is reviewed
against it.** That is the honest answer to "green levies": not denial and not scrapping, but each
levy with its own receipt and its own test. Transport (fuel, buses, rail) moves into this post per
MACH §5, held to the same bill rule. Nothing on it is a flagship yet.

---

## 3. What this minister will NOT promise, and why

1. **No "£X off your bill."** Reform's £500 is the market's only number, and matching it with a
   bigger one would be an invented costing (GUARD §4). Our promise is the kill number: if the trial
   region's bills rise faster than elsewhere, the rule goes. Credibility comes from being the only
   bill offer that can be checked.
2. **No promise that prices fall while Hormuz is shut.** We don't control the strait (MACH §3 on the
   Foreign page). We promise who pays for the shock, not that there won't be one.
3. **No ban on data centres, and no "AI is draining the grid" scare.** Abundance is the brief's
   instinct, so we're pro-building. The objection is to the queue and the discount, not the
   building. And no "each AI query drinks a bottle of water"-style claims (GUARD §4, banned).
4. **No scrapping net zero, and no new date-hike either.** Both are bundle positions. We test each
   measure against the bill instead.
5. **No forcing anyone out of their boiler or their car.** The brief guards against lecturing about
   boilers and never sneers at anyone who drives to work. Heat pumps and EVs are offers with a
   published bill effect, never mandates on existing homes.
6. **No nationalising "the energy companies."** Generation and retail have competition, so they
   stay in the market. Only the natural monopolies, one region first. No confiscation: the price is
   set independently.
7. **No pretending more North Sea drilling sets your bill.** Home gas sells at the international
   price [K], so we won't sell drilling as a bill cut. Licensing is a judgement call on security and
   jobs, stated as one, with its review date.
8. **No promise that a public network is cheaper.** That is what the test is for. We say in advance
   it could fail.

The spine's §2.2 amendment 3 asks every chapter for one idea of our own we admit could fail
(Flagship 4) and one policy the reader expects us to oppose that we'll test instead of condemning.
Here that is **North Sea licensing**: a judgement call with a review, not a moral stance.

---

## 4. The reader test

The reader: working class, a town that's seen better times, drifting right. Energy bills are near
the top of what they feel (LAND #3), they back public ownership (GUARD §1), AI is not on their list
(0%), and Reform's £500 is aimed at them.

| Flagship | How it lands | Trap it risks | How the wording avoids it |
| --- | --- | --- | --- |
| 1 Households first | Strongly. "Homes before server halls" is a loyalty-and-desert sentence: *we were here first, and we paid for the wires*. | **Anti-AI fear with no beneficiary** (rule 6), and **AI as the issue** (enters through the bill instead). Also the "they're blocking jobs" counter. | Leads on the bill and the queue, not the machine. Names the chooser (the consultation, the charging rules). Says we want the building, just not on the household's tab. The word "AI" appears once, as the zones' name. |
| 2 Hosepipe ban | Very strongly. It is a fairness image anyone can picture, and the town gets a say and a slice. | **Lecture** on planning; **pandering** to NIMBY anger; **a private villain** (one firm). | Shows the wrong as an image (August, the hosepipe, forty jobs). The developer is "the applicant", not the enemy: the fault is that the tenant writes the compact. The town *owns* rather than blocks. |
| 3 Free wind at the wind's price | Well, if it is about the standing charge and the war price. "Someone put a meter on the weather." | Reads as **anti-green** or a **tax on renewables**, and **lecture** on marginal pricing. | One image (paid as if it burned gas), no market-design explainer. Targets the windfall on old plants, never new building. The payoff is concrete: the standing charge, prepayment first. |
| 4 Own what can't compete | Already believed (GUARD §1). "You can't shop around for a sewer" is a pub line. | **The left with a robot voice** (spine §9 C); fear for pensions; **concede first** missed. | Concede first: competition works where it exists, so generation and retail stay private. Fair price set independently, sale-back clause, pensions named. "A receipt and a returns policy" is consumer language, not ideology. |
| Net zero | Mixed. Some readers see green levies as part of the rigging. | **Blaming the cost of living on climate policy without checking** (brief), or **denial** that levies cost anything. | Neither: every levy gets its bill receipt and its test. Security is the argument, "home-grown power is the only kind nobody can blockade", not the planet first. Never sneers at the driver. |

Lee/Coe test on the page's sarcastic lines. "Brilliant machine. Wrong queue." confirms contempt for
the queue, not for the reader or for technology. "A toll booth" confirms contempt for the
arrangement, not for anyone who owns shares.

---

## 5. Interfaces

**Depends on**
- **Chancellor:** the public stake / dividend fund (Flagship 1c, 2); the borrowing for the network
  purchase (4); the hypothecation of the levy (3); a heating-oil measure for off-grid homes (the
  leaves-out of 3). **Clash to settle:** national stake vs local share. One published split rule,
  decided once, by the PM.
- **Housing:** planning route and the host-town compact (2); "build where the people are, not where
  the servers are" is the same row seen from the ground. Connections for new homes are a measure in
  4. **Clash:** a council keen on business rates (mayors keep 20% from 2027 [M]) may want a
  campus at any price. The compact floor stops a race to the bottom, and Housing must back it.
- **PM:** the Operating System. Local panels and agreement maps (Stage 2) run Flagship 2. The Test
  Register and the Office for Postmortems hold all four fails-ifs. The PM settles the stake split.
- **Defence:** the run-by-hand drill for the grid (arc row 7; NCSC warns AI malware against critical
  infrastructure is "highly likely" by 2028 [M]). Energy supplies the grid half and Defence the drill.
  A publicly owned region (4) is the obvious first place to rehearse it.
- **Foreign:** Hormuz. Foreign owns the strait, Energy owns the meter. Rule: every Foreign energy
  story ends with the Energy page's answer, not a second policy.

**Touches**
- **Work and Pensions:** few jobs per £bn at data centres. W&P owns the jobs claim, so Energy never
  promises jobs from a campus.
- **Home:** fuel-poverty scams and smart-meter fraud? Not today; leave it.
- **Health:** cold homes and heat. A possible measure for Flagship 3 (winter admissions in the
  lowest-use homes) if Health wants a shared metric. Not a commitment.

---

## 6. Draft manifesto page (house format, renderer-safe)

Plain paragraphs only, no bold, no lists, so nothing mashes in `apps/site/manifesto.mjs`. About 320
words (the live page is 260; trim the hosepipe rule first if the cabinet needs room). Today's evidence is drawn from LAND. Before the cabinet uses the cap and the consultation,
each needs a `kind=news` memory with a URL (the digest carried Drax and Hormuz; the cap and the
consultation came from this session's web research). The rate-of-gas sentence is [K] and needs a
source or must be cut.

### Revised draft (closing pass, 2026-11-05: the red team's fixes applied)

What changed from the draft the red team read (sources: `../redteam/opposition.md`, `../redteam/reader.md`, `../redteam/wonk.md`; the overall strategy is `../README.md`):

1. 'Picture the grid as a bath' cut; opens on the decision (reader: an analogy is a lesson).
2. The levy now says it exists (the Electricity Generator Levy) and what we change: raise it while the strait is shut, every pound on the standing charge, by law (opposition #10). Led with the payoff, not marginal pricing (reader). One windfall law, owned by the Chancellor; Energy delivers it on bills (opposition #8).
3. Network purchase at fair market value set independently, with the premium counted in the test (wonk §5: A1P1 and investment-treaty exposure).
4. Connection fails-if window lengthened to three years and made a signing measure (wonk #5).
5. 'Every rule stops after five years unless the data says keep' replaced by each rule's own end (opposition #8 contradiction table, wonk #2).
6. 'Take the ones you like' cut (reader X4). Fuel at the pump added (reader).

```markdown
---
title: Energy and Climate
line: Households first on the grid, and what can't compete, the public owns.
---
## Position

A data centre wants as much power as a town, and ministers are consulting on whether it should pay less for it than you do. Brilliant machine. Wrong queue.

The cap on a typical bill rose this autumn to £1,723. A £20 billion data centre is proposed at Drax in North Yorkshire. Who goes first when power runs short is being decided by a consultation and a queue. It can be decided differently.

Households first. In a shortage, homes, hospitals and the factories already here keep their power, and the biggest new loads switch down first. A data centre pays for its own connection and the wires it needs, and never gets a discount paid out of your bill. Fails if, three years in, no big project in the trial region has signed for a connection, or bills there rise faster than elsewhere.

The hosepipe ban applies to the data centre. The town that hosts one writes the deal, not the company: a share of the new power owned locally, water use published every month, and the campus cut first in a drought.

Cut the standing charge, prepayment meters first. A levy on the windfall that old wind farms and nuclear stations make while gas is dear already exists. We raise it while the strait is shut and put every pound on the standing charge, by law. It switches off when gas prices fall back.

Own what can't compete. There is one set of wires and one water main to your door. With no rival, the market is a toll booth. One network region comes into public hands first, at a fair price set by an independent judge, not by us. That costs more than the regulator's book value, and the test counts it. Fails if, after five years, bills or power cuts there are worse than in regions like it. Passes, and the next region follows.

At the pump, the war price is on your petrol too. We publish who gets the extra, every month.

Who it leaves out: homes off the gas grid and on prepayment, who pay most and get counted least. They are counted separately, and first.
```

Notes on the revised draft:

- Trim the pump paragraph first.
- Fact gate: £1,723 and the consultation need `kind=news` URLs; the EGL's terms [K, check]; whether the
  large-load connection charge needs an Ofgem direction or primary law (wonk §5) belongs in the brief,
  not the page.
- Body about 361 words.

### Superseded draft (the version the red team read, kept for comparison)


```markdown
---
title: Energy and Climate
line: Households first on the grid, and what can't compete, the public owns.
---
## Position

Picture the grid as a bath. Your house has a tap. Now a data centre wants one the size of a town, and ministers are consulting on whether it should get its power cheaper than you. Brilliant machine. Wrong queue.

The cap on a typical bill rose this autumn to £1,723. A £20 billion data centre is proposed at Drax in North Yorkshire. Who goes first when the bath runs low is being decided by a consultation and a queue. It can be decided differently.

Four rules. Each stands on its own; take the ones you like.

Households first. In a shortage, homes, hospitals and the factories already here keep their power; the biggest new loads switch down first. A data centre pays for its own connection and never gets a discount paid out of your bill.

The hosepipe ban applies to the data centre. The town that hosts one writes the deal, not the company: a share of the new power owned locally, water use published every month, and the campus cut first in a drought.

Sell the free wind at the wind's price. Old wind farms and nuclear stations sell at a price set by gas. While a war keeps gas dear, that windfall cuts your standing charge, prepayment meters first.

Own what can't compete. There is one set of wires and one water main to your door. With no rival, the market is a toll booth. One network region comes into public hands first, at a price someone else sets.

The test. Each rule starts small, measured against the rest of the country on bills, power cuts and investment. Fails if bills where it runs rise faster than elsewhere. Then we publish the postmortem and drop it. Every rule stops after five years unless the data says keep.

Who it leaves out: homes off the gas grid and on prepayment, who pay most and get counted least. They are counted separately, and first.
```

The first 14 teletext lines carry the bath, the bill, the chooser and the first rule. That is the
order the reader feels them in.

---

## 7. Suggested changes to the brief

Proposed for a human PR to `docs/government/ministers/09-energy-climate.md` (the brief cap is 300
words, so this replaces rather than appends; the temperament, instinct and voice are kept
word-for-word where possible). Changes, in order of importance:

1. **Add "Standing flagships" (defend these; hang the news off them; sharpen, never replace).**
   Households first on the grid (large-load tariff, priority order, no discount out of household
   bills). The hosepipe ban applies to the data centre (the host town writes the compact). Sell the
   free wind at the wind's price (windfall to the standing charge, prepayment first). Own what can't
   compete (one network region first; failed water firms stay public). Line: "Households first on the
   grid, and what can't compete, the public owns."
2. **Widen "Owns"**: add *data-centre power and water use, grid connections and the connections queue,
   transport costs (fuel, buses, rail as infrastructure)*, per MACH §5. Add to "Watches": large-load and
   data-centre items in `tech-ai`, and water in `local gov`.
3. **Add a "Never promises" line**: no £-off figure; no price fall while a foreign strait is shut; no
   data-centre ban and no water-per-query scare; no boiler or car mandates on existing homes; no
   claim that drilling sets the bill; no nationalising competitive generation or retail; no claim the
   public network is cheaper before its test reports.
4. **Add the bill rule to "Instinct"**: every net-zero measure that touches a household bill shows its
   receipt first and gets a test. Security first, bill second, planet third: "home-grown power is the
   only kind nobody can blockade."
5. **Add to "Guards against"**: calling a developer a villain (they're applicants; the rule is the
   fault); restating "£500 off" or any opponent's bill figure in order to knock it down; promising
   jobs from a data centre (that's W&P's call, and the numbers are small).
6. **Interfaces line**: "The stake is the Chancellor's; the compact's planning route is Housing's; the
   grid drill is Defence's; the strait is Foreign's. Hormuz stories end at this page's meter."
7. **Evidence set** (spine §9 B c, needs Kai's ruling): a short standing list this post may cite on
   a quiet day, each with a URL and a grade. The Ofgem cap, the AI-zone power consultation, the
   Drax proposal, and once sourced: the gas-sets-the-price share, the Electricity Generator Levy terms,
   the Scottish Water comparison. Without it, Flagships 3 and 4 can't be defended on a day with no
   energy news.

Suggested sounds-like addition (keep the existing line): "A gigawatt is brilliant. A gigawatt that
jumps the queue and sends the bill to a prepayment meter in Selby is not."

---

## Open questions for Kai and Jack

- **The threshold** for a "large load" (100 MW is a placeholder). Set it by the test, or fix it now?
- **The stake split** between the national fund and the host town (needs the Chancellor's page and a
  PM settlement).
- **Water in or out of the headline.** It is in the brief and in the reader's anger, but the evidence
  for today (special administration, debts, dividends) is not in this session's sources. Leaving it
  in Flagship 4 as a judgement call is my lean.
- **The fact gate.** Every precedent in §2 is [K]. One research pass with URLs (Ohio/Texas tariffs,
  Ireland, Denmark 20%, pylon discount, EGL terms, Hamburg/Berlin, Scottish Water) unblocks the whole
  chapter.
