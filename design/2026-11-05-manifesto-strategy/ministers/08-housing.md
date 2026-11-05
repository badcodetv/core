# Housing: manifesto strategy

> **Revised 2026-11-05 (closing pass).** The §6 draft page has been rewritten to apply the red team's fixes; the change list sits above the new draft, and the old draft is kept under it. Sections 1-5 and 7 onward are unchanged, so where they still say "unless the data says keep", read "unless Parliament votes to keep it" (see `../README.md` §2).

2026-11-05. Strategy for post 08 (homes, rents, planning, local government). Not a ruling and not
copy for `docs/government/`: that changes only through the cabinet's rolling PR or a human PR.
Built on `spine.md` (the thesis, the eleven-field contract, row 4 of the arc, §4 Stage 2) and the
absorb pack (FP-A, MACH, GUARD, LAND). Confidence marks are LAND's: [H] [M] [L] [?] [K]. **[K]
means background knowledge, not re-checked today: it must get a source URL and a grade before it
goes in public copy (X12, the fact gate).** The cabinet's own rule is stricter still: a figure can
go on the page only if it sits in a `kind=news` memory with a URL.

---

## 1. Mission

**The line (frontmatter):** *Count the roofs, not the promises, and put homes ahead of servers in
the queue.* (79 characters, no colon.) Fallback if Kai and Jack want AI kept out of the headline
entirely: keep today's *Count the roofs, not the promises.* and carry "homes before servers" as
the second commitment.

**The problem this post exists to prevent.** Two links in the bad-branch chain land on the ground
here, and Housing is the minister who owns the ground:

- **Row 4 of the arc, the places half: the machines get the land, the power and the water first.**
  The bad branch said it flat: the biggest data centre brings "forty new jobs, six of which are for
  humans", and "the hosepipe ban does not apply to the data centre" (F7). Energy and Climate owns
  the bill; Housing owns the *planning decision* and the *host town*. Today's sign: AI Growth Zones
  in Culham, the North East, North and South Wales and Lanarkshire, about £28bn mostly pledged,
  with electricity the binding constraint [M]; a £20bn Drax/Brookfield/Radiant data-centre
  proposal at a North Yorkshire power station this week [M]; OpenAI writing its own "community
  compact" for host towns because the state hasn't [M]. The warning already happened once: in
  2022 the GLA said new housing in parts of west London could wait years for grid connections
  because data centres had taken the capacity [K, needs source].
- **Row 5, growth nobody received, where it settles.** When the gains from AI go to people who
  already own assets, the asset they buy most is land. Rising land value is where "the economy
  grew and nobody it happened to" becomes a rent rise. Today's sign: Bank Rate up to 4.00%, 8–1
  [H], with CPI above 3% and rising [M], landing on the next remortgage and the next rent review;
  1.5m-homes target at about 437,900 net additions by September 2026, about 29% of the target at
  44% of the time, now called a "stretch target" [H, Full Fact, BCIS, Construction News].
- **Row 3 in a letting agent's office: the computer says no to a tenancy.** Tenant referencing and
  rent-setting are moving onto software. In the US, pooled rent-setting software became an
  antitrust case (DOJ v RealPage, 2024) and several cities banned it [K]. Whether it is happening
  at scale in the UK is **unknown**; nobody measures it. That gap is the policy.

In one sentence: **this post exists so that the decade AI arrives is not the decade the young lose
the last route to a secure home, while the land, the grid and the rise in value go to whoever got
there first.** Shortage is a decision. So is the queue.

---

## 2. The flagships

Four, each using a different Future Proof mechanism so the page also demonstrates the method:
council building (data-driven, plant into idle capacity), homes before servers (continuous
integration: a check before a big load lands), a human on your tenancy (the right to a human),
and street votes (composition: decide one thing at a time, locally). A fifth, the roof count, is
the instrument under all four rather than a policy of its own.

### F0 (the instrument): the Roof Count

**In one sentence:** the department publishes, monthly, homes *completed* (not permitted, not
"delivered"), net of demolitions, split by tenure with social rent on its own line, against the
promise, by council.

This is MICRO's worked example made real (D1: "rents: average rent as a share of local take-home
pay; within three years"). It costs almost nothing, it is what the foreman would do first, and it
makes every other flagship falsifiable. It also kills a common trick: counting conversions and
permissions as "homes". The headline measure for the whole post is **median private rent as a
share of local take-home pay**, published per council, so the reader can see whether anything we
do touches the thing they feel. Status: *Kept* from day one (it is a measure, not a trial).

### F1: Councils build again, on land at the field price

**The policy in one sentence.** Councils (and development corporations they set up) build homes for
social rent again, buying the land at close to its value before planning permission, with the rise
in value paying for the roads, school and surgery, and new council homes exempt from Right to Buy.

**Why now.** The national target is at about 29% at 44% of the time [H]; the rate rise today [H]
makes private building slower, because builders build at the speed they can sell (the Letwin
review's "absorption rate", 2018 [K]); private renters and the waiting list carry the gap. Labour's
Budget taxed property income more and devolved business rates [M], but did not touch the price of
land, which is the largest single cost the public pays when it builds.

**The Future Proof mechanism.** Data-driven decision (tenet 3) plus the money story's "plant into
idle capacity" (spine §5.1), with its honest limit built in as the fails-if: if planting pushes
building costs up faster than elsewhere, the builders weren't there and we stop.

**The contract.**

| Field | Filled in |
| --- | --- |
| The wrong | A family on a council waiting list in a town where a field becomes worth many times more the day the council grants permission, and the rise goes to whoever held the field. |
| Who decided | The Land Compensation Act 1961, which pays landowners "hope value" for permission the public hasn't granted yet [K]; Right to Buy without replacement, since 1980 [K]; the borrowing rules that stopped councils building for decades (cap lifted 2018 [K]). Partly reformed by the Levelling-up and Regeneration Act 2023 for some schemes [K]. |
| The rule | Volunteer councils may compulsorily buy named sites at existing-use value plus a fixed, published premium for the owner; the uplift is spent on the site's infrastructure first; the homes are let at social rent; homes built under the rule are exempt from Right to Buy. |
| The ledger | Pays: landowners and land promoters, who lose a windfall the public's permission created (not homeowners selling their house: the rule touches undeveloped land on named sites). Gains: households on waiting lists; councils, whose rent roll repays the borrowing; the taxpayer, who pays less per home. Money moves from land rent to roofs. |
| The test | Five volunteer councils chosen where pressure is highest (longest waiting lists, most overcrowding, most temporary accommodation), compared with five matched councils building the usual way. Measured: social-rent completions, cost per completed home, months from site purchase to first roof, local build-cost inflation. Reported quarterly on the Roof Count. |
| Fails if | By the end of year three, trial councils are not completing social-rent homes both faster and at lower cost per home than the comparison councils; **or** build costs in trial areas rise faster than the regional average for two quarters running (capacity wasn't there). |
| The undo | Sunset at year five: it stops unless the data says keep. Sites already bought finish (a half-built estate is not an undo); new purchases stop. We publish the postmortem and drop it. |
| Who it leaves out | Today's private renters and families in temporary accommodation, who cannot wait for year three; people who don't qualify for the waiting list; places that don't volunteer. Counted separately every month. |
| Who signs | The Housing Secretary's office (fiction); Kai or Jack merging (real). |
| Status | Draft. |

**Scale, cost, how it's paid (honest uncertainty).** The trial is small: a few thousand homes
across ten councils. Councils borrow against future rents (the Housing Revenue Account model) from
the Public Works Loan Board; the land discount is the subsidy. Land is a large share of the cost
of a home in high-pressure areas, often a third or more in the South East [L, needs source], so
buying at existing-use value is where the saving is, but nobody can honestly say how large until
the first compulsory purchases are priced and tested in court. The full-scale ambition if it
passes (the 90,000 social-rent homes a year that Shelter's 2019 commission called for [K]) is a
*consequence of the test*, not a promise. A second source we can name: councils already spend
large sums renting temporary accommodation from private landlords at nightly rates [K, needs a
DLUHC/MHCLG figure]. Stop paying twice (spine §5.3): trial councils may move that budget into buying
or building homes they own and use as temporary accommodation.

**Strongest precedent.** The post-war new towns: development corporations bought land near
agricultural value, built Stevenage to Milton Keynes, and repaid the Treasury from the uplift
[K]. Abroad, Dutch and German municipal land assembly does the same today [K]. The record of
council building itself: councils completed over 100,000 homes a year for much of the 1950s and
60s [K, ONS/MHCLG live tables].

**Strongest objection and our answer.** *"This is confiscation; landowners will sue and stop
selling, and you'll build nothing."* Answer: it is the rule this country built its new towns
under, the owner is paid what the land was worth plus a published premium, and we test it in ten
places before anyone else lives in it. If owners stop selling and the trial councils build slower,
the fails-if catches it in three years and we drop it, in public. Second objection: *"councils
can't build."* Then the comparison group will show it, and we'll say so.

### F2: Homes before servers in the queue

**The policy in one sentence.** No housing scheme is pushed back in the grid or water queue to make
room for a data centre, and where a big new load wants a town's land, power or water, the town
writes the deal, not the company.

**Why now.** The Growth Zones [M], Drax [M], the OpenAI "community compact" [M], the government's
consultation on cheaper power for AI zones while household caps rise [M]. The bad branch: "the
hosepipe ban does not apply to the data centre" (F7).

**The Future Proof mechanism.** Continuous integration: a check before a big change lands (the
green tick, I2), and a published test on the first case. Plus composition at the town level: the
host town votes on its own compact.

**The contract.**

| Field | Filled in |
| --- | --- |
| The wrong | A young couple whose estate is approved but can't be connected for years, in the same district where a server campus got its connection first. |
| Who decided | The grid connection queue's ordering rules (Ofgem and the network operators); planning fast-tracks for data centres as nationally significant infrastructure [K]; Growth Zone designation (DSIT); a company writing its own "compact" [M]. |
| The rule | (1) A Housing Connection Check: before any large new load (a threshold set with Energy, e.g. 100 MW) is granted planning or a connection, the network operator and the council publish whether it delays any allocated housing site's connection; if it does, the load pays for the extra capacity or waits. (2) The Host Town Compact: the council writes it, residents vote on it (participatory, spine §4 Stage 2.4), and it is published before consent, covering jobs to local people, water use, and a share of the site's retained business rates ring-fenced for local homes. |
| The ledger | Pays: the developer of the big load (connection and reinforcement costs it would otherwise push onto the queue or the bill). Gains: households on allocated housing sites; the host town. Money moves from the campus's margin to the town's homes. The retained rates mechanism exists already (mayors keep 20% of business rates growth from 2027 [M]). |
| The test | The first two or three large-load applications after the rule (Drax if it reaches planning, is the obvious first [M]) go through the check in public, compared with housing connection dates in the same distribution area over the previous two years. |
| Fails if | Within two years, any allocated housing site in a checked area is delayed by a big load that passed the check; **or** the check adds more than an agreed time (pre-registered, set with Energy) to consents without moving a single housing connection date. Either result: postmortem, rule changes or goes. |
| The undo | Sunset at three years unless the data says keep. |
| Who it leaves out | Towns that want the jobs badly enough to sign anything (the compact can't protect a town from its own bargain); places without a council plan or allocated sites, which the check can't see. |
| Who signs | Housing Secretary jointly with Energy and Climate. |
| Status | Draft. |

**Scale and cost.** Near-zero public cost: it reallocates who pays for capacity. The real cost is
time added to big-load consents, which is why the second fails-if exists. Uncertain: how many
housing connections are actually being delayed by big loads outside west London; the check is also
the first measurement anyone has made of that.

**Strongest precedent.** The west London grid constraint in 2022 is the warning [K]; Ofgem's
connections reform ("first ready, first connected", 2025) shows the queue can be reordered by rule
[K]. Community benefit funds for onshore wind are the precedent for a host-town share [K].

**Strongest objection and our answer.** *"You'll scare off the investment the country needs."*
Answer: we're pro-building, of servers too (spine §6, pro-abundance). The rule says a data centre
pays for its own pipe and doesn't jump the queue ahead of a house. If the check measurably drives
investment away without freeing a single home, the fails-if says so and we drop it.

### F3: If software turns you down for a home, a human hears you

**The policy in one sentence.** Anyone refused a tenancy, a social-housing priority band or a
homelessness duty where software scored them is told so, given the reason, and gets an appeal heard
by a named human within ten working days; and the competition regulator finds out, within a year,
whether landlords are setting rents with shared software that pools rivals' data, with a ban if it
is.

**Why now.** The reader's sharpest machine fear is being judged by one (welfare algorithm concern
44% to 59% in two years, GUARD §1). The right to a human is the PM's cross-government statute (row
3); Housing is its natural second trial after benefits because the letting agent is where many
renters meet the algorithm.

**The Future Proof mechanism.** The right to a human is a right, so per spine §9 H it is *Kept from
day one and measured*, not trialled. The rent-software half is tenet 3 at its purest: **we don't
know if it's happening here, so we look before we ban.** That is the line that makes the page
credible.

**The contract (abridged).** The wrong: a renter refused for a flat by a referencing score nobody
will explain. Who decided: the agency and landlord that bought the tool; the absence of any rule.
The rule: disclosure, reason, human appeal; CMA market study into pooled rent-setting with a
published finding by month twelve. The ledger: costs agents a reviewer's time; gains renters a
reason and a second look. Measure: share of appeals overturned (if almost none ever are, the appeal
is a rubber stamp and we redesign it; if many are, the scoring was wrong and that is published).
Fails if (rent-software half): the CMA finds pooled tools in material use and a ban is not in force
within a further year. Undo: the right stays; the ban, if any, carries a five-year review. Leaves
out: people refused without any software involved (the old-fashioned no), and lodgers outside
tenancy law.

**Precedent.** UK GDPR Article 22 already restricts solely automated decisions [K] (and Reform
would scrap UK GDPR [M]: we state our rule, we don't name them). DOJ v RealPage (2024) and city
bans on algorithmic rent-setting in San Francisco and elsewhere (2024) [K].

**Objection.** *"Red tape for small landlords."* The duty sits on whoever uses the tool, usually the
agent; a landlord with one flat who reads the application himself is untouched.

### F4: Your street decides (the policy you'd expect us to oppose, tested)

**The policy in one sentence.** Where most residents of a street vote to let their own street add
a storey or replace semis with terraces to an agreed design, the council says yes, tested first in
volunteer councils.

**Why it's here.** Street votes are a right-of-centre idea (Policy Exchange; legislated in the
Levelling-up and Regeneration Act 2023 and never switched on [K]). Spine §2.2.3 requires at least
one policy the reader expects us to oppose that we *test* instead. It is also tenet 1 at its
smallest possible scale: decide one thing, the people it lands on decide it, issue by issue. And
residents keep the uplift on their own house, which is the honest answer to "what's in it for me?"

**The contract (abridged).** Test: switch on the existing powers in three to five volunteer
councils for three years, compared with matched councils. Measured: net extra homes, share of votes
passed, disputes. Fails if fewer than a pre-registered handful of streets ever vote yes, or
neighbours outside the street win more than an agreed share of appeals on harm. Undo: three-year
sunset unless the data says keep; homes built stay built. Leaves out: renters on the street (who
vote? the hard question; trial both versions, owners-only and all-residents, and publish which
builds more), and places with no streets suited to it. Precedent: Auckland's 2016 upzoning,
associated with a large rise in consents [K, research disputes the size]. Cost: almost none to the
public.

**Objection.** *"It's a gift to homeowners."* It's a gift of homes. If it builds none, we'll say so.

---

## 3. What this minister will not promise

The foreman's refusals. Each is a sentence the page can say out loud, because credibility comes
from what we won't sign.

1. **No house-building number we can't count.** We promise a published count and a fails-if, not
   "300,000 a year". A number with no test is the thing this minister mocks.
2. **We won't promise house prices fall.** Most of our readers who own a home own nearly nothing
   else. The aim is that rent stops eating the wage and a first home stops being a lottery, not that
   anyone's house loses value. Promising a crash is promising to hurt the people we're for.
3. **We won't promise to fix your mortgage rate.** The Bank of England sets Bank Rate and stays
   independent (the Chancellor's page says the same). We can publish who pays for each rise
   (Chancellor's ledger); we can't wave it away.
4. **No national rent freeze.** The evidence is mixed: Scotland's emergency cap (2022–25) and
   Berlin's rent lid (2020, struck down) both ran into supply and enforcement problems [K]. We'd
   rather build and measure rent against wages. If someone wants to propose in-tenancy rent
   stabilisation, it goes through the same contract, in one city first.
5. **We won't blame migrants, and we won't pretend pressure isn't real.** Where more people have
   arrived and nothing has been built, the queue is longer and the reader is right. The not-building
   is the bigger story, so the trial councils are picked by pressure, and the homes go there first.
6. **No new Right to Buy on homes we build.** We're not abolishing anyone's existing right in this
   page; we won't sell off the new ones at a discount.
7. **We won't promise to stop the data centre.** Building is good, including servers. The promise is
   who pays for the pipe and who's first in the queue.
8. **No AI planning officer.** Software can sort consultation responses into a map (C7); a named
   planning officer decides, and the decision says so.

---

## 4. The reader test

| Flagship | Trap it risks | How the wording avoids it |
| --- | --- | --- |
| F0 Roof Count | Wage-maths lecture; numbers as the climax (rule 3). | The count is a foreman's joke, not a table ("Count them yourself. I'll wait."). One figure on the page, not ten. |
| F1 Field price | Punching down at the small landlord or the homeowner (rule on punching down; brief's own guard); "the left with a robot voice" (spine §9 C). | Says "the field", "the landowner who held the field", never "landlords". States plainly it touches undeveloped land on named sites, not your house. The concession: this is how the new towns were built, a national achievement the reader's grandparents moved into. Moral vocabulary: a windfall you didn't earn, fair reward. |
| F1 targeting by pressure | Denying immigration's housing cost (rule 4); or restating the scare to refute it (rule 10). | Concedes the pressure where nothing is built in one clause, then re-aims at the not-building. Never quotes a migration claim; never says "immigrants aren't the problem". Picks trial councils by measured pressure, which is the reader's own instinct (homes where the queue is). |
| F2 Homes before servers | Leading with AI (0% unprompted); unaimed automation fear; data-centre imagery as aesthetic. | The headline is the queue and the house, not "AI". The data centre appears as a competitor with a named chooser (the queue rules, the company writing its own compact) and the rule gives the anger an address in the same paragraph. Pro-building, not anti-tech. |
| F3 Human on your tenancy | Lecturing about algorithms; casting the reader as a victim-pupil. | Lands on the reader's own measured fear (being judged by a machine). Written as a right with a deadline, not a warning. "We don't know if it's happening here, so we'll look before we ban" is said straight: the honesty is the credential. |
| F4 Street votes | Reads as a gift to owners against renters; NIMBY-coded. | Framed as "your street, your vote, your extra floor", owner-and-renter versions both trialled. It is the one plank that hands a decision to the people it lands on, which is the reader's anger at "nobody asked us" turned into a rule. |

Overall: the page opens on the reader's situation (the rent, the remortgage, the queue), names the
chooser by act (the 1961 Act, the queue rule, the company's compact), plays every pledge straight,
and keeps one bathos ("I've got a time machine") and one crack of warmth (the last line).

---

## 5. Interfaces

- **Energy and Climate (depends, partly clashes).** F2 is a joint rule: Energy owns the bill and
  "big loads pay their own way"; Housing owns planning and the host town. Clash: Energy's "build the
  power we can't be cut off from" wants new generation and wires sited fast; Housing's check adds a
  step. Settle by one shared threshold and one published check, not two.
- **Chancellor (depends).** F1 needs borrowing headroom for council housing revenue accounts and the
  land discount booked on the Ledger. The Chancellor's dividend-fund stake ("public money builds the
  machine, the public owns a slice") and Housing's land-value capture are the same principle at two
  scales; they must use the same words. Possible clash over whether Growth Zone uplift goes to the
  fund or to local homes: propose a split, decided by the host town's vote.
- **Home (clashes unless settled).** Migration proportionality lives in both. Home owns the numbers
  and asylum accommodation (the Linton-on-Ouse row [M]); Housing owns councils and supply. Rule:
  Home states the real size; Housing states where the homes go. Asylum sites in towns go through the
  same host-town consultation as any big use of local land. Spine §9 D (what Home proposes) needs a
  ruling first.
- **Work and Pensions (depends).** Housing benefit and the UC housing element, Local Housing
  Allowance; arrears caused by automated benefit decisions feed homelessness. The right to a human
  is one rule across both.
- **Prime Minister (depends).** The right-to-a-human statute; the Test Register; Stage 2's
  participatory budgeting and local votes, which spine §4 gives to Housing to run.
- **Education (supports).** Construction skills are the binding constraint beside land. F1's
  fails-if (build costs rising) is the signal; construction apprenticeships for under-25s are the
  first-rung answer. A trowel is a first rung nobody is automating this decade [claim needs care:
  say "work standing ready", not "AI-proof"].
- **Health (supports).** GP surgeries in F1's infrastructure-first rule; cold, damp homes as a
  health cost (Awaab's Law [K]).
- **Devolution (scope, spine §9 J).** Housing and planning are devolved; this page is England-led,
  with Scotland, Wales and Northern Ireland invited to run the same tests.

---

## 6. Draft manifesto page (proposal for `docs/government/manifesto/08-housing.md`)

Renderer-safe: plain paragraphs, no bold, no lists. About 330 words. **Fact gate before it ships:**
the 437,900 / 29% / 44% figure and the 4% rate are [H] in LAND and must sit in a `kind=news`
memory (Full Fact tracker, BoE) on the day the cabinet uses them; "worth many times more" needs a
land-value source (MHCLG land value estimates) or comes out; "a 1961 law" needs its statute link.

### Revised draft (closing pass, 2026-11-05: the red team's fixes applied)

What changed from the draft the red team read (sources: `../redteam/opposition.md`, `../redteam/reader.md`, `../redteam/wonk.md`; the overall strategy is `../README.md`):

1. 'Count them yourself. I'll wait. I've got a time machine.' and 'I've seen how this one ends' cut: sarcasm aimed at the reader, and the fiction leaking (reader, opposition #6).
2. 'Under a 1961 law' statute lesson replaced by plain words, and the page now says councils can already strip hope value on some schemes (LURA 2023) and we make it the default (opposition #10, wonk §8).
3. Led with the new towns; owner-occupied farms below a size exempt (opposition #13).
4. 'The not-building is the bigger story' cut: no ranking of the reader's worries (reader X7).
5. Fails-if window fixed: interim measure at year two (land bought), outcome at year five with a number (15% cheaper per home, provisional); no 'data says keep' (wonk #5, opposition #1).
6. Who gets the homes now answered: local connection alongside need. PENDING RULING, You-decide 6 in README.md.
7. The host-town deal is the single compact Housing owns; residents have the last word (opposition #8).
8. Ends on the receipt, not 'Write a better rule' (reader X2).

```markdown
---
title: Housing
line: Count the roofs, not the promises, and put homes ahead of servers in the queue.
---
## Position

A planning permission is a drawing. A roof is a roof. England was promised one and a half million homes by 2029. By September about 437,900 had been added: 29% of the homes at 44% of the time. Somebody's keeping a different count. We'll keep ours every month, in public: homes finished, not homes permitted.

Shortage is a decision. When the council says yes to houses on a field, the field can be worth many times what it was the day before, and most of that rise goes to whoever held it. Councils were stopped from building, and their homes were sold without replacement. And today's rate rise lands on the next remortgage and the next rent review.

First, councils build again, for social rent, the way the new towns did: on land bought at close to what it was worth before the permission, with the rise paying for the road, the school and the surgery. Councils can already do this on some schemes. We make it the default for social-rent sites. Owner-occupied farms below a set size are left out. The new homes are not sold off at a discount.

Who gets them: people with a connection to the town, who live, work or grew up there, alongside those in the greatest need.

Who pays, who gains. The landowner gives up a windfall the public's permission created. The waiting list gets homes. The council borrows against the rents and pays it back.

The test. Councils where the waiting lists are longest, against councils like them. By year two they must have bought the land; by year five they must be finishing social-rent homes at least 15% cheaper per home than the comparison, without local building costs rising faster than elsewhere. Miss either, and we publish the write-up and drop it. Passes, and every council can do it.

Second, homes before servers. Where a data centre wants the town's grid, land or water, the town writes the deal, not the company, residents have the last word, and no housing site moves back in the queue for it.

Third, if software turned you down for a tenancy, you are told, given the reason, and a named person hears your appeal within ten working days.

Who it leaves out: today's private renters and families in temporary accommodation, who can't wait five years. They're counted every month, on their own line.

Count the roofs. We will.
```

Notes on the revised draft:

- Trim the rate-rise sentence first (it dates fastest).
- Fact gate: 437,900 / 29% / 44% need a `kind=news` URL (Full Fact tracker); 'many times what it was'
  needs MHCLG land value estimates; the LURA 2023 hope-value power [K, check] must be sourced before the
  'can already do this' sentence ships.
- Body about 403 words.

### Superseded draft (the version the red team read, kept for comparison)


```markdown
---
title: Housing
line: Count the roofs, not the promises, and put homes ahead of servers in the queue.
---
## Position

A planning permission is a drawing. A roof is a roof. England was promised one and a half million homes by 2029. By September about 437,900 had been added: 29% of the homes at 44% of the time. Count them yourself. I'll wait. I've got a time machine.

Shortage is a decision. The day a council grants permission, a field can be worth many times what it was, and under a 1961 law the rise goes to whoever held the field. Councils were stopped from building and their homes sold without replacement. Where more people arrived and nothing was built, the queue got longer. The not-building is the bigger story. And today's rate rise lands on the next remortgage and the next rent review.

First, councils build again, for social rent, on land bought at what it was worth before the permission. The rise pays for the road, the school and the surgery. The new homes are not sold off.

Who pays, who gains. The landowner gives up a windfall the public's permission created. The waiting list gets homes. The council borrows against the rents and pays it back.

The test. Five volunteer councils where the waiting lists are longest, against five like them, counting finished homes, cost per home and time to first roof. Fails if, by year three, they aren't building faster and cheaper, or if local building costs climb faster than elsewhere. Then we publish the postmortem and drop it. It stops in year five unless the data says keep.

Second, homes before servers. Where a data centre wants the town's grid, land or water, the town writes the deal, not the company, and no housing site moves back in the queue for it.

Third, if software turned you down for a tenancy, you are told, given the reason, and a named person hears your appeal.

Who it leaves out: today's private renters and families in temporary accommodation, who can't wait three years. They are counted every month, separately, so nobody calls a good pilot a fixed housing market.

I've seen how this one ends. It ends with nobody under a roof they own. Write a better rule.
```

Notes on the draft:

- F4 (street votes) and F0 (the Roof Count as an instrument) are left off the page to keep it
  near the length of its peers; they belong in the brief as standing commitments and can enter
  the page on a news day that calls for them (a planning bill, a street-votes story). If Kai and
  Jack want the "policy you'd expect us to oppose" visible from day one, swap the Third paragraph
  for: "Third, your street decides. Where most residents vote to let their own street build up a
  floor, the council says yes. Tested in volunteer councils first, and dropped if it builds
  nothing."
- The last line is the one crack of warmth and the only time-machine reference beyond the
  brief's own joke. It points at the outcome, not at the reader. If it reads as too bleak, the
  brief's sign-off ("Write a better rule.") alone is fine.
- The opening paragraph is the teletext 14 lines: the wrong and the line land before any policy.

---

## 7. Suggested changes to the minister's brief

For a human PR to `docs/government/ministers/08-housing.md` (brief cap: 300 words). Keep the
temperament, instinct and "Sounds like" exactly as they are; they are working. Add:

**Owns (add):** places as well as homes: councils, high streets, and the town where a trial runs or
a big load lands. With Energy and Climate, the planning side of data centres and AI Growth Zones:
the host town, its land and its queue. Tenant referencing and rent-setting software. Street votes
and local participatory budgeting.

**Standing commitments (new section, defended whatever the news):**
1. The Roof Count: homes completed, net, by tenure, by council, monthly; rent as a share of local
   take-home pay is the measure the post answers to.
2. Councils build again for social rent on land at the field price; new council homes are not sold
   off. Five volunteer councils, five matched; fails-if at year three; sunset at year five.
3. Homes before servers: no housing site moves back in the grid or water queue for a big load; the
   host town writes its own compact.
4. If software turned you down for a home, you're told, given the reason, and a named human hears
   the appeal.
5. Street votes, tested in volunteer councils.

**Rules for the daily page (add):** The standing section is sharpened, never replaced; a quiet news
day changes nothing. Today's news goes in the evidence paragraph. Count completions, never
permissions or "delivered". Never promise a national number, a price fall, a mortgage rate or a
rent freeze. On data centres, the anger goes to the queue rule and the company's deal, never to
"AI".

**Guards against (add):** denying housing pressure where people have arrived and nothing was built,
or restating a migration claim to argue with it. Equating the person selling their house with the
fund holding land.

---

## Open questions for Kai and Jack

1. **The line.** Put "servers" in the headline, or keep *Count the roofs, not the promises.* and
   let "homes before servers" carry the AI link one paragraph down? (Lean: the new line; it is the
   one housing sentence no other party could say.)
2. **Land at the field price** is the boldest plank and the most left-coded. It is also the most
   historically British (the new towns). Lean hard, or soften to "a fair share of the uplift"?
   (Lean: keep it, framed as the new towns' rule.)
3. **Street votes on the page or in the brief only.** (Lean: brief now, page on the first news hook.)
