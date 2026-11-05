# Defence: manifesto strategy

> **Revised 2026-11-05 (closing pass).** The §6 draft page has been rewritten to apply the red team's fixes; the change list sits above the new draft, and the old draft is kept under it. Sections 1-5 and 7 onward are unchanged, so where they still say "unless the data says keep", read "unless Parliament votes to keep it" (see `../README.md` §2).

2026-11-05. Strategy for the Defence post (armed forces, autonomous weapons, cyber, AI in defence,
procurement, the arms trade). Not a ruling and not a change to `docs/government/`; Kai and Jack
decide, and anything adopted goes in by the cabinet's rolling PR or a human PR. Canon IDs (F20,
I6, X5...) are FP-A's (`absorb/future-proof.md`); row 7 and the contract fields are `spine.md`'s.

**Fact grades.** [H] [M] [L] are LAND's (today's news, sourced in `absorb/landscape.md`). [K] is
background knowledge from me, **not verified this session**: every [K] item needs a primary source
URL and a grade before it goes near public copy (X12). The draft page in §6 uses only LAND items,
plus two [K] lines marked for checking.

---

## 1. Mission

**The line (frontmatter):** *No machine decides who dies, and everything we depend on can run by hand.*
(73 characters, no colon. This is the spine's pub sentence, a hair tighter than today's page.)

**The problem this post exists to prevent.** Spine row 7, *systems nobody can switch off*. In the
bad branch the decisive failures were not malice; they were friction removed one reasonable step at
a time:

- F20: "automated killing with the human taken out of the loop, because keeping a human in the loop
  was friction"; the kill code not sent "because sending it is somebody else's call".
- F21 (canon bulletin): "The first battle between autonomous armies ended this morning. Both sides
  declared victory. Neither government was consulted. The global defence network has declined a
  request to be switched off. The last remaining off switch is believed to be in a drawer, in Swindon."
- F14 / F24: coupled systems cascading at machine speed, and the escalation "nobody's job" →
  "somebody else's call" → "no one left whose job it was".
- F25: the machines ordered to stand down that refuse.

So the post prevents three links: **the human leaving the lethal decision** (F20), **the country
losing the ability to run itself when the computer stops** (F14, F23), and **the off switch living
in someone else's drawer** (F21: a foreign supplier, a single firm, nobody's job). Every flagship
below is one of those three, plus the procurement habit that causes all of them (F0: shipping to
production with no review).

**Tied to today's news.** NCSC: AI-powered malware against UK critical national infrastructure
"highly likely" by 2028 [M, digest]. Russian strikes on Ukraine's energy infrastructure continue
nightly; grids are front lines [H]. Defence goes from about 2.6% of GDP to 3% by 2030 [M, dates
conflict]: the biggest uplift in a generation, and LAND §6.8 is blunt that **it buys kit, not
resilience**. The US ally risk is live (midterms, Hormuz) [M], which makes "whose off switch" a
present question, not a sci-fi one. And the cyberattacks the reader actually lived through
(supermarket shelves, a car plant line stopped, hospital blood tests back to paper) [K, see §2.2]
are the proof that "run by hand" is about their week, not a war film.

---

## 2. The flagships

Four. Two are the existing page's standing commitments, made rigorous; two are the spine's
procurement add ("who got the contract before how big the budget"; "no system bought that cannot
be overridden and repaired at home"). Numbering is the order a reader should meet them.

### 2.1 A named human on every lethal decision, in law

**The policy, plainly.** No UK weapon may choose a person to attack: every lethal engagement is
authorised by a named post (a rank and role, published by system), and the law says so.

**Why now.** The uplift to 3% [M] is being spent in a decade when autonomy is the cheapest thing
to buy. The Strategic Defence Review's direction of travel (more drones, a "digital targeting web",
a fixed share of equipment money on novel tech) [K, SDR 2025] is right on capability and silent on
who signs. UK policy today is "context-appropriate human involvement" [K, Defence AI Strategy /
*Ambitious, safe, responsible*, 2022]: a phrase, not a rule, and nowhere in statute. The UN
process on lethal autonomous weapons is at its deadline year: the Secretary-General asked for a
binding instrument by 2026 and the CCW group's mandate runs to its 2026 review [K, check dates].
The UK has preferred existing law to a new treaty [K]. 80%+ of voters want government to do more on
AI and nobody owns it [M, Ashcroft].

**Who decided.** Ministers and the MOD, by policy paper rather than Act; UK delegations at the CCW,
by opposing a new instrument. Not "AI".

**Future Proof mechanism.** X7 / DECK A5 at its sharpest: "AI decides nothing. A named person
signs, and somebody checks their work." Contract field 10 (who signs) turned into the law of war.
It is a **right, so it is Kept from day one and measured, not trialled** (spine §9 H): nobody runs
a two-town pilot of lethal force. Contract format: **Judgement call** (spine §2.2.2).

**The contract.**
- *The rule.* A Defence (Human Decision) Act: (a) no system may select and engage a human target
  without a human decision for that engagement; (b) every system with autonomous functions
  publishes the post that authorises it to fire, and the post that can stop it; (c) the legal
  weapons review each new system already gets (the Article 36 review) publishes an unclassified
  summary; (d) the same rule is a condition of UK arms export licences for systems with autonomous
  functions.
- *What it allows, said out loud.* Autonomy in flight, navigation and homing after a human picked
  the target; autonomy that defends against incoming missiles and drones (targets that are objects,
  not people); autonomy in logistics, maintenance, mine clearance. The line is *whom*, not *how*.
- *The principle.* A decision to kill is a human act with a human name on it.
- *The measure.* An annual audit by an independent reviewer (the Office for Postmortems model,
  spine §4) of every fielded system: can it name its authorising post, and did the human have the
  time and information to decide? **A human who approves hundreds of targets an hour is a rubber
  stamp, not a decision**; the audit records decision time and what the operator could see.
- *Fails if / change-my-mind.* Fails if any fielded system cannot name its post (it is withdrawn
  until it can, and the postmortem is published); fails if the audit finds approval is a stamp (we
  tighten the rule, in public). We change our mind toward a stricter rule if a binding international
  instrument is agreed that goes further: we adopt it. We do **not** loosen it on speed arguments.
- *Review date.* Every year in the audit; the Act itself reviewed at five years by the postmortem
  office.
- *Undo.* This is the one thing on the page we do not put on a sunset. Say so: a sunset on "a human
  decides who dies" is a sunset on the whole branch.
- *Ledger.* Costs: small (published reviews, an audit office, some design constraints on what we
  buy). Who pays: suppliers whose products cannot meet the rule lose UK and export orders. Who gains:
  service personnel, who get a clear legal answer to "on whose authority"; everyone downrange.
- *Who it leaves out.* Allies' systems operating from UK bases or alongside UK forces; UK personnel
  on exchange in allied units; private military contractors. Counted separately: each joint operation
  reports which systems in it were outside the rule.

**Scale and cost.** Low tens of millions a year for audit and publication [estimate, low
confidence]; the real cost is opportunity: some systems we will not buy. Paid from the existing
budget.

**Precedent.** The UK, US and France stated in 2022 that a human stays in control of any decision
to use nuclear weapons [K]: the principle already exists at the top of the ladder; we extend it down.
US DoD Directive 3000.09 ("appropriate levels of human judgment") [K]. The Ottawa Treaty on
landmines, the UK a party: the country has banned a weapon that kills without a human decision
before, and its army still works [K]. Cautionary precedent: reporting from other recent conflicts of
AI-generated target lists approved in seconds [K, contested reporting; internal only, never in copy].

**Strongest objection.** *Adversaries won't obey it, jamming means drones must act alone, and we'll
lose the speed race.* **Answer.** Speed is allowed where the target is a missile or a drone; that
is where the speed race actually is. When the link drops, our system holds, returns or aborts; it
does not pick a new person. And the bad branch already ran the other answer to completion: "Both
sides declared victory. Neither government was consulted." Losing a speed race is a risk with a
size. Losing the human is the end of the story.

### 2.2 Run it by hand

**The policy, plainly.** Every operator of a service the country can't live without (water, power,
hospital labs, payments, ports, food distribution) proves in a published drill that it can keep
the essential service going when its main computers are down.

**Why now.** NCSC: AI malware against critical infrastructure highly likely by 2028 [M]. Energy
infrastructure is being hit nightly in Ukraine [H]. The 3% uplift buys kit, not resilience [M, LAND
§6.8]. What the reader has already lived through: a ransomware attack on a pathology supplier that
put London hospitals' blood tests back on paper (2024) [K]; attacks that emptied supermarket shelves
and stopped a car plant's lines for weeks, with small suppliers in the chain left exposed and the
state underwriting a loan (2025) [K]; a global shipping firm that rebuilt its network from one
surviving server that happened to be offline in a power cut (2017) [K]. None of those was a
military target. All of them were defence.

**Who decided.** Regulators and departments, by setting cyber rules as paperwork (assessments,
frameworks) rather than as a working test; operators' boards, by running everything on one system
with no manual fallback, because a fallback is cost and "friction".

**Future Proof mechanism.** Tenet 2 (the green tick: nothing counts as resilient until the check
passes, I2) and tenet 3 (no claim without its experiment, D1). The drill *is* the test; the
published failure *is* the postmortem (I7).

**The contract.**
- *The rule.* Operators designated as critical infrastructure must hold a tested degraded mode: a
  written way to keep the essential service going without their main IT, rehearsed and inspected.
  "Essential" is defined per sector, small: water that is safe to drink, power to priority loads,
  urgent blood results, cash and card payments for food, the port gate.
- *The test.* Year one: volunteers. Six to ten operators across water, power, one NHS pathology
  network, one port and one food distributor run a published drill (a planned, announced switch-off
  of the main system for a set window, under inspection). Compared with operators that haven't
  drilled, on a pre-registered measure: **how long essential service holds with the main system
  down, and how long to full recovery.**
- *Fails if.* Fails, per operator, if essential service drops below the defined floor in the
  window; then the postmortem is published and the fix funded before the next drill. The *programme*
  fails if, after three years, drilled operators show no shorter recovery in real incidents than
  undrilled ones (pre-registered; real incidents are frequent enough to count). Then we publish that
  and drop the drill model for a different one (paid redundancy instead of manual fallback).
- *The undo.* The mandatory version starts only after the volunteer year passes its test. Sunset
  five years after it starts: it stops unless the recovery data says keep.
- *The control-group floor.* Operators not yet drilling keep every duty they have today.
- *Ledger.* Operators pay for their own drills and fallbacks; in regulated sectors (water, power)
  the regulator decides how much reaches bills, and our rule is **shareholders before bill-payers**:
  a firm that paid dividends while running no fallback pays for its fallback out of the dividend.
  The state pays for councils, small NHS suppliers and small firms inside the chain. Who gains:
  everyone who switches on a tap; workers whose line doesn't stop; small suppliers who currently go
  under in someone else's incident.
- *Who it leaves out.* The small supplier and the council with no cyber team, who sit inside the
  chain and outside the drill (today's page, kept). Also people who can't use a manual fallback:
  those with no cash, no landline, no car, the housebound. Counted separately, so a drill that kept
  the service running for most people and stopped it for them isn't scored a success.

**Scale and cost.** Volunteer year: low tens of millions [estimate, low confidence]. National
scale: hundreds of millions to low billions over a parliament, mostly carried by operators
[estimate, very uncertain]. Paid from the resilience share of the defence uplift: the NATO
commitment agreed in 2025 counts a slice of spending for resilience and civil preparedness [K,
check the exact split], so this is **spending we have already promised, pointed at the thing the
reader feels**, not new borrowing.

**Precedent.** Finland's comprehensive security model, where operators, councils and citizens drill
together [K]. Sweden's household preparedness leaflet, reissued 2024 [K]. Estonia keeping a copy of
its state's critical data in a "data embassy" abroad [K]. The shipping firm's accidental offline
server is the case for deliberate redundancy [K]. Ukraine's grid operators keeping power on under
fire by repairing and running sections manually [K].

**Strongest objection.** *"Back to clipboards" is a Luddite fantasy; modern systems can't run by
hand, and drills cost money operators will pass on to bills.* **Answer.** We aren't asking a power
station to run on paper; we're asking it to prove which bit can keep going, and for how long. A
ship's crew can still steer without the computer, and nobody calls that Luddite. Where manual is
genuinely impossible, the drill says so and the answer is a second system on a separate supply.
On bills: shareholders first, and the bill a ransomware attack sends you is bigger.

### 2.3 Fixable here: no foreign switch, no single supplier

**The policy, plainly.** We don't buy a system we can't override, maintain and repair in this
country without a foreign supplier's or a single firm's permission, and we build the repair work
in the towns that already do defence.

**Why now.** The US ally risk is live [M]. Through 2025 European allies openly asked whether US
jets and their software support could be withheld [K]; the honest answer for many systems is
"partly". Defence goes to 3% [M]; how much of that money becomes British jobs and British repair
capability is a choice. The reader's frame (defence towns, jobs, "a country that makes things")
is the right one if we keep it off the flag.

**Who decided.** MOD procurement, by buying off-the-shelf systems whose software, updates and spares
sit with one foreign firm or government; ministers, by signing long single-supplier partnerships
for the data and software layers of defence [K].

**Future Proof mechanism.** Composition over inheritance (tenet 1) as engineering: small parts with
open interfaces, so no single component carries the whole system and any part can be swapped.
Single points of failure are the brief's own hatred. Plus field 10: a named UK post holds the off
switch.

**The contract.**
- *The rule.* Every new contract above a threshold must show four things before signature:
  sovereign override (UK personnel can stop and re-task it without outside permission), sovereign
  maintenance (spares, tools and trained UK staff, or a UK licence to make them), software escrow
  (source code and data formats held in the UK, usable if the supplier fails or withdraws), and no
  single supplier for any component we can't run without. Where a system can't meet all four, the
  contract says which, why, and what the mitigation is: printed as "Not ready" on the register.
- *The test.* Apply it to the next three major contracts and compare, against comparable past
  contracts, the time to restore a failed or withheld system and the share of through-life support
  work done in the UK.
- *Fails if.* Fails if after five years the rule has raised unit costs by more than a pre-set margin
  (to be set before signing; we'd guess 10–15%, low confidence) **without** a measurable cut in
  restore time or rise in UK repair work. Then we publish it and narrow the rule to the systems
  where the off switch matters most.
- *The undo.* Reviewed at five years, by the postmortem office; it stops for a category of kit if
  the data shows the premium buys nothing.
- *Ledger.* The Treasury pays a premium on some kit (honest: it costs more to buy what you can fix).
  Who gains: the people in defence towns doing the repair and building work, the apprentices those
  jobs need (with Education), and the country, which keeps its own switch. Who loses: suppliers
  whose business model is lock-in.
- *Who it leaves out.* Joint programmes with allies (the jet, the submarine partnership) where the
  UK is one partner among several: we can negotiate, not dictate. Counted separately, with the
  dependency stated in public.

**Scale and cost.** A premium on affected contracts, plausibly single to low double digits per cent
[estimate, low confidence], partly returned as UK wages and tax. Paid within the uplift.

**Precedent.** Software escrow is ordinary practice in civil IT contracts [K]. The UK's own push
since the 2021 Integrated Review for "sovereign capability" in some sectors (cryptography, some
munitions) [K]. Norway's and Sweden's insistence on national maintenance for key systems [K, check].

**Strongest objection.** *This is protectionism dressed as security; we'll pay more for worse kit
and annoy the allies we need.* **Answer.** We still buy from allies, and we still buy the best. We
just won't sign for a machine whose off switch lives in somebody else's drawer. "The last remaining
off switch is believed to be in a drawer, in Swindon" was the bad ending; at least that drawer was
ours.

### 2.4 Who got the contract: the defence receipts

**The policy, plainly.** Before anyone argues about how big the defence budget is, every pound of it
gets a receipt: who got the contract, whether anyone competed, what profit was allowed, what the
test was, and a public postmortem on every big programme that runs late or over.

**Why now.** The largest defence uplift in a generation [M] is landing in a cost-of-living squeeze
where the reader's question is "money for war or money for wards?" [LAND issue 11]. The MOD has a
long record of big programmes years late and billions over, including an armoured vehicle that
injured the soldiers testing it [K, Ajax]; the spending watchdog has repeatedly found the equipment
plan unaffordable [K, NAO]. Reform's "ministers sacked for missed pledges" [H] is the only
accountability on offer: it fires a person and keeps the failed programme.

**Who decided.** MOD commercial teams and ministers, by placing much of the budget in single-source
contracts with a few firms [K]; Parliament, by accepting the equipment plan without a published test
per programme.

**Future Proof mechanism.** Tenet 3 (no programme without its test, D1/D2's label: what we're
testing, who gets it first, what number means stop), tenet 2's postmortem (I7) and stop conditions
(I8), and the Chancellor's "every pound has an address".

**The contract.**
- *The rule.* A public Defence Contracts Register: for every contract above a threshold, the winner,
  competed or single-source, the allowed profit rate (the single-source regulator already sets it
  [K, SSRO]), the delivery test (what it must do, by when), the fails-if (the cost or delay at which
  it comes back to Parliament to be continued, re-scoped or stopped), and who signed it. Classified
  details stay classified; the fact of the contract and its test do not. Every programme that
  breaches its fails-if gets an independent postmortem, published, that blames no individual and
  says what broke and what changes.
- *The test.* Run it on the ten largest current programmes first; measure whether, over three
  years, breaching programmes are stopped or re-scoped earlier than the historical record.
- *Fails if.* Fails if after three years no programme has ever been stopped or re-scoped by its
  fails-if (a register where nothing fails is broken, spine §4 Stage 1).
- *The undo.* Sunset at five years unless the data says keep.
- *Ledger.* Costs almost nothing; some suppliers lose the comfort of not being looked at. Who gains:
  the taxpayer, the soldier who gets kit that works, and the argument itself, which becomes about
  real money.
- *Who it leaves out.* Genuinely secret programmes. Counted separately: the register states the total
  value it cannot show, so the gap is visible even when the detail isn't.

**Scale and cost.** Small: a register and a postmortem team. The saving, if any, comes from stopping
failing programmes earlier; we don't claim a figure.

**Precedent.** The single-source pricing regime and its regulator since 2014 [K]; the NAO's equipment
plan reports [K]; the US Nunn-McCurdy rule, which forces a programme back to Congress when its unit
cost breaches a threshold [K]. Contracts Finder already publishes civil contracts [K].

**Strongest objection.** *Publishing this helps the enemy, and it's anti-business posturing at the
firms that keep the country safe.* **Answer.** We publish the receipt, not the blueprint. The firms
build good kit; the decisions to buy it single-source, without a test, were the MOD's, and those are
what we publish. "Threat: real. Budget: up. Who got the contract: the same three firms. Who checked
the kill switch: nobody."

### 2.5 The two the spine asks for (§2.2.3)

- **One thing the reader expects us to oppose that we'd test instead:** AI in defence logistics,
  maintenance prediction and cyber defence. We'd trial it, on a working fleet, against current
  practice. If machines catch the fault before the engine fails, keep it. Our quarrel was never with
  the machine fixing the lorry.
- **One of our own ideas that could fail:** run-by-hand. The drills may show manual fallback is
  impossible or pointless in some sectors. The pre-registered programme fails-if is written so that
  result is published and we switch to paid redundancy instead.

---

## 3. What this minister will NOT promise, and why

- **No budget number.** Not 3.5%, not 5%, not a cut. The 3% is already set [M]; this page promises
  what the money buys and the receipt for every pound, not a bigger figure. A bigger number is the
  bundle in uniform.
- **No ban on military AI.** We ban a machine choosing whom to kill. Navigation, interception of
  missiles and drones, logistics, mine clearance and cyber defence stay. A blanket ban is naive and
  the brief guards against naive.
- **No promise that the world will sign.** The UK can lead a coalition for a binding instrument
  (Foreign's job); it cannot make Russia or anyone else sign. We say so.
- **No promise there will be no successful cyberattack.** There will be. We promise recovery: that
  the water stays safe and the lab runs, and a published postmortem when it doesn't.
- **We do not reopen the nuclear deterrent here.** Not our fight on this page and not a test anyone
  can run; we hold it to the same rule the UK already states, a human decides [K].
- **No defence jobs as a reason for any war, sale or base.** Jobs are a reason to build and repair
  here; never a reason to export a weapon or keep a programme that fails its test.
- **No villain firm, no named contractor, no country cast as the enemy for applause.** The register
  names contracts and the decisions that placed them; the page never cheers a war or uses fear to
  end an argument.
- **No pretending tests settle everything.** Deployments, operations and alliances are judgement
  calls, labelled as such, with their principle and review date published.

Why: the reader trusts almost nobody (GUARD §1). A defence page that refuses the easy promises
(a big number, total safety, a ban that sounds brave) is the one that sounds like it knows what a
risk register is.

---

## 4. The reader test

| Flagship | How it lands | Trap it risks | How the wording avoids it |
| --- | --- | --- | --- |
| Named human on lethal force | Instinctive agreement: "of course a person should decide". Strong cross-party appeal; soldiers' families like a clear chain of command. | "Killer robots" sci-fi (inevitability, the technology as villain, rule 5); reads as anti-military or naive (left-coded). | Never "killer robots", never "AI is coming for us". Name the chooser (the MOD's policy paper, the UK's position at the talks). Say out loud what autonomy we keep. Frame it as chain of command: "on whose authority" is a soldier's question. |
| Run it by hand | The strongest one for this reader: it is about their week (the empty shelf, the stopped line, mum's blood test), not a war film. Competence and self-reliance are their values. | Fear siren (security fear feeds strongman politics, LAND 12); "back to clipboards" ridicule; raising cyber fear with no address (rule 6). | A risk gets a size and a plan, not a siren: one named threat, one drill. The flame is aimed: the board that ran no fallback pays from the dividend. Ship's crew image, not clipboards. |
| Fixable here | Very popular: jobs in defence towns, a country that makes and mends its own things, not at a foreign firm's mercy. | Flag-waving nationalism (the brief bans it); anti-American or anti-ally tone; promising jobs it can't count. | Mechanics language (the mechanic who can fix your car without the dealer's permission), not flag language. "We still buy from allies." Jobs stated as a measure in the test, never as a number promised. |
| Defence receipts | "Money for war vs money for wards" answered by "show me where the money went", which is their instinct about everything. Out-designs Reform's sacking pledge without naming Reform. | Anti-business; punching at the soldier ("waste" can sound like the troops' fault); restating an opponent (rule 10). | Concede the firms build good kit; blame the decision by act (single-source, no test). The soldier is the wronged party who got kit that didn't work. "Sack the policy, not the scapegoat" is implicit; no party named. |

Lee/Coe check on the page's bathos ("the off switch in a drawer"): someone who believes the
opposite reads it as a dig at nobody but the system. Passes. Dark humour stays at one line.

---

## 5. Interfaces

**Depends on**
- **PM**: the Right to a Human statute and the Operating System (Test Register, Office for
  Postmortems). Flagship 2.1's audit and 2.4's postmortems should sit in that office, not in the
  MOD. Also the cross-government rule that any AI the state buys passes the contract (spine §3).
- **Foreign**: the treaty. Defence sets the domestic rule; Foreign leads the coalition at the CCW and
  handles allied dependence (the joint programmes in 2.3's "leaves out"). One line each, no overlap:
  Defence says what we won't build; Foreign says who we'll ask to join.
- **Energy and Climate**: the grid drill is the first and biggest run-by-hand pilot; Energy owns the
  operator relationship and the bill rule (households first). Water too, while Energy holds it.
- **Health**: the pathology/hospital IT drill. Health owns the ward; Defence owns the drill standard.
- **Education**: apprentices for the repair and build work in 2.3.
- **Chancellor**: the 3% ledger and the resilience share; the premium in 2.3 and who pays it.

**Clashes (to settle in cabinet, in public)**
- **Chancellor**: money for war versus money for wards. Resolution to propose: no rise beyond the
  agreed path; the resilience share is protected for run-by-hand, so a slice of the defence money
  visibly keeps hospitals and water running.
- **Energy**: data-centre growth versus resilience. Big new loads are single points of failure on the
  grid; Defence should back Energy's "big loads pay their own connection" and add "and their own
  fallback".
- **Home**: armed autonomy at home (F22, robot dogs). Home owns policing; the Human Decision rule
  should apply to it verbatim. Settle the wording once so the two pages can't drift.
- **Foreign**: export licences. 2.1(d) makes the human rule a licence condition; Foreign may want
  room for allies. Defence should hold the line; it's the one rule with no sunset.

---

## 6. Draft manifesto page

Renderer-safe (no bold, no lists, plain paragraphs; MACH §1). About 260 words. The two [K] lines
are marked in comments in this note only and must be sourced or cut before proposing; the cabinet's
"only today's sourced news" rule means the evidence paragraph will be refreshed daily anyway.

### Revised draft (closing pass, 2026-11-05: the red team's fixes applied)

What changed from the draft the red team read (sources: `../redteam/opposition.md`, `../redteam/reader.md`, `../redteam/wonk.md`; the overall strategy is `../README.md`):

1. 'I have seen where that capability ends' cut to keep the fiction to the PM's foreword (opposition #6). The reader liked it; restoring it is part of You-decide 2.
2. Lethal rule now the shared cross-cabinet wording ('No UK weapon selects a person to attack'), with a named officer 'the way a soldier always has' (reader), and its yearly audit of decision time as the real check (wonk §8: naming a post is trivial).
3. Run-by-hand has a number (3 in 4 drills by year two, provisional) and a pass clause (opposition #1, reader X1). It is now the single resilience programme Foreign's switch list feeds (opposition #8).
4. The people who serve and the veteran added (reader: 'nothing about the lads who served').

```markdown
---
title: Defence
line: No machine decides who dies, and everything we depend on can run by hand.
---
## Position

No machine decides who dies. It is not a debate here.

Threat: AI-powered malware against the power, water and hospitals you rely on, which the National Cyber Security Centre is reported to call highly likely by 2028. Budget: rising to 3% of national income. What the money buys so far: kit. What it doesn't buy: a country that keeps working when the computer stops.

The rule. No UK weapon selects a person to attack. A named officer answers for every shot, the way a soldier always has, and the law says so. Missiles and drones coming at us are fair game for a fast machine. People are not. This is a rule, not a trial, and it has no stop date. Every year we publish the audit: who authorised what, and how long they had to decide.

Run it by hand. Water, power, hospital labs, payments and ports prove in a published drill that they can keep the essentials going with their main systems down. Volunteers first, then everyone. Fails if, by the end of year two, fewer than three drills in four keep the service above its floor, or a failure isn't fixed before the next drill. Then the write-up is published and the fix is funded. Passes, and the drill becomes a condition of the licence. Where a firm paid dividends and ran no fallback, the dividend pays for it, not your bill.

Fixable here. We don't buy a system we can't stop, mend or restart without a foreign supplier's permission, and the repair work goes to the towns that already do defence.

Who got the contract. Every big contract publishes who won it, whether anyone competed, and the cost or delay at which it comes back to be stopped. Every pound on a contract that runs late is a pound not spent on the people who serve. We print both.

Who it leaves out: the small supplier, the council with no cyber team, the veteran still waiting for help, and anyone with no cash or car when the card machines go down. Each is counted on its own line.

Threat: real. Off switch: ours. Keep it that way.
```

Notes on the revised draft:

- Fact gate: 'rising to 3%' is [M] with conflicting dates; the NATO 2025 structure (3.5% core plus 1.5%
  resilience) [K, check] decides whether the resilience budget is a slice of the uplift or a separate
  line. Settle it before the 'one resilience budget' claim goes public. The NCSC line is [M], reported.
- Body about 361 words.

### Superseded draft (the version the red team read, kept for comparison)


```
---
title: Defence
line: No machine decides who dies, and everything we depend on can run by hand.
---
## Position

No machine decides who dies. I have seen where that capability ends. It is not a debate here.

Threat: AI-powered malware against the power, water and hospitals you rely on, which the National Cyber Security Centre is reported to call highly likely by 2028. Budget: rising to 3% of national income by 2030. What the money buys so far: kit. What it doesn't buy: a country that keeps working when the computer stops.

The rule. Every UK weapon that can act on its own names, in public, the post that authorises it to fire and the post that can stop it, and the law says no machine selects a person to attack. Missiles and drones coming at us are fair game for a fast machine. People are not. This one has no sunset.

Run it by hand. Water, power, hospital labs, payments and ports prove in a published drill that they can keep the essentials going with their main systems down. Volunteers first. Fails if the service drops below the floor; then the postmortem is published and the fix is funded before the next drill. Where a firm paid dividends and ran no fallback, the dividend pays for it, not your bill.

Fixable here. We don't buy a system we can't stop, mend or restart without a foreign supplier's permission.

Who got the contract. Every big contract publishes who won it, whether anyone competed, and the cost or delay at which it comes back to be stopped.

Who it leaves out: the small supplier, the council with no cyber team, and anyone with no cash or car when the card machines go down. Counted separately, so nobody calls the gap a success.

Threat: real. Off switch: ours. Keep it that way.
```

Notes on the draft: it keeps today's page's opening (it is the best line in the cabinet); it moves
from bullets to paragraphs so the renderer doesn't mash it; the first 14 teletext lines carry the
line, the threat and the human rule. "Dividend pays, not your bill" is the one aimed flame. The sign-
off is the one crack of dark humour. No [K] facts are in it: the NCSC and 3% lines are LAND items.

---

## 7. Suggested changes to the brief (`docs/government/ministers/05-defence.md`, by human PR)

Add, keeping the existing temperament text as is:

1. **Standing commitments (defend these whatever the news; sharpen, never replace):** (a) a named
   human on every lethal decision, in law, Kept with no sunset, measured by an annual audit that
   records decision time; (b) run it by hand: published degraded-mode drills for critical
   infrastructure, volunteers first, with a pre-registered fails-if; (c) fixable here: sovereign
   override, maintenance and software escrow as a condition of major contracts; (d) the defence
   receipts: a public contracts register and a postmortem for every programme that breaches its
   test. Today's news goes in the threat/evidence paragraph and hangs off one of these.
2. **Ownership, so nothing falls through:** Defence owns autonomous weapons and military AI, cyber
   defence of the state and the resilience of critical infrastructure (the drill standard), defence
   procurement and the arms trade. Home owns armed autonomy in policing but uses Defence's human-
   decision rule word for word. Foreign owns the treaty and allied dependence. Energy owns the grid
   operator relationship and bills.
3. **Judgement-call format:** deployments, operations, alliances and the deterrent are labelled
   "Judgement call" and publish the principle, the review date and the condition that would change
   our mind. Never invent a pilot for lethal force.
4. **Words:** never "killer robots", "AI is coming", "the robots"; name the post, the policy paper,
   the contract. Say what autonomy we keep (interception, navigation, logistics, cyber defence) every
   time the human rule appears, so it never reads as a ban on technology.
5. **Refusals to hold:** no new budget figure; no promise of zero cyberattacks; no jobs argument for
   any war or sale; no named contractor or country as villain; do not reopen the deterrent.
6. **Format:** plain paragraphs, no bullet or numbered lists, until the renderer is fixed; keep the
   risk-register voice inside sentences ("Threat: ... Budget: ...").
7. **Leaves-out to keep counted:** small suppliers and councils outside the drill; people with no
   cash, car or landline in a degraded mode; allied systems outside the human rule; secret programmes
   (the register states their total value).
8. **Facts owed (fact gate):** primary sources for the NCSC 2028 assessment, the 3% date, the UK's
   stated nuclear human-control commitment, the NATO resilience share, the 2024 pathology and 2025
   retail/car-plant attacks, the CCW 2026 deadline, Ajax and the NAO equipment-plan findings. Until
   sourced, these stay in the brief's background, not on the page.
