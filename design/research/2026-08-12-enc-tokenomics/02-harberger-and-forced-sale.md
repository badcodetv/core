# Harberger Taxes and Forced Sale in Practice

**Question:** What happens when Harberger-tax systems (perpetual rent on a self-assessed price, anyone may force-buy, non-payment triggers foreclosure) meet real users — and what changes when the price is protocol-set rather than self-assessed, as in ENC?

## What I found

1. **The founding art project ran at 5%/year, not 5%/day.** Simon de la Rouviere's *This Artwork Is Always On Sale* (TAIAOS), launched March 2019, charged a **5% annual** patronage fee on the owner's self-assessed price, flowing to the artist. [Medium, 2019](https://medium.com/@simondlr/this-artwork-is-always-on-sale-92a7d0c67f43). ENC's placeholder of ~5%/day compounds to roughly **18,000%/year** — several orders of magnitude past anything found in the wild.

2. **De la Rouviere later tried raising the rate to 100%/year in a v2 — deliberately, as an experiment, and it's presented as a stress test, not a norm.** V1 turned over 3 times in its life, generated ~18.4 ETH for the artist, then sat with one holder (final valuation ~240 ETH) who said they held for patronage/support of the artist's open-source work, not speculation. V2 raised the rate specifically to test whether higher tax forces more turnover. [simondlr.com, TAIAOS v2](https://home.simondlr.com/posts/this-artwork-is-always-on-sale-v2). Takeaway: **even the most tax-tolerant art experiment in the space treated 100%/year as an extreme worth studying**, not a baseline.

3. **Wildcards (2020) is the "first scalable Harberger tax contract" live on Ethereum mainnet**, tokenizing endangered species as always-for-sale NFTs, tax flowing to conservation charities. It raised over $130,000 for conservation partners. [BitcoinKE, 2020](https://bitcoinke.io/2020/01/the-wildcards-project/); [Wildcards blog](https://blog.wildcards.world/). I could not verify their specific rate or turnover/dormancy numbers — their blog is now unreachable (DNS failure) and secondary sources don't state the number. Mark rate/outcome data **unverified**.

4. **ENS explicitly evaluated and rejected Harberger tax for domain names — this is the single most relevant precedent for ENC**, because it's a real team, with real users, reasoning in public about *why forced sale on a valuable digital asset backfires*. Vitalik Buterin's 2022 post lays out the case: domain owners are typically unsophisticated (unlike the industrial-property users Harberger theory assumes), switching costs are high, and a forced sale of a name like `coinbase.eth` to the highest bidder could mean a scammer buys it and runs a fake-charity/ICO scam under a trusted name — a catastrophic externality forced-sale advocates don't price in. [vitalik.eth.limo, 2022](https://vitalik.eth.limo/general/2022/09/09/ens.html). ENS's proposed alternative drops forced sale entirely: bidders (not owners) drive price signals, fees rise toward open bids but are **capped**, and owners can prepay to lock a rate — trading efficiency for owner security.

5. **The self-assessment mechanism is the entire efficiency argument in Posner & Weyl's original COST proposal, and it's a real tension even when working as designed**: self-assessment creates opposing incentives — under-declare to pay less tax, over-declare to avoid losing an asset to a bidder you don't want to lose to. [Wikipedia, Harberger Tax](https://en.wikipedia.org/wiki/Harberger_Tax); [Flight from Perfection](https://www.flightfromperfection.com/the-common-ownership-self-assessed-tax.html) (states the theory's own claims, not independent critique — flagged). UChicago Law Review's symposium on *Radical Markets* raised a deeper, autonomy-based objection: the book's mechanisms subordinate self-determination to aggregate welfare. [UChicago Law Review](https://lawreview.uchicago.edu/book-symposium-posner-and-weyls-radical-markets), 2018 — stale (8 years) but the standard academic anchor; nothing newer found that supersedes it.

6. **Solana precedent exists but is thin and still self-assessed.** LEMS ("Limited Editions Market-based Subscriptions") is a Solana Harberger-tax primitive where the creator sets the tax rate and the buyer self-assesses resale price; its flagship app, SolarSaloon, was described by its own builder as devnet-only and "full of bugs and issues," no adoption data disclosed. [Medium, dodecahedr0x](https://dodecahedr0x.medium.com/partial-digital-ownership-with-limited-editions-market-based-subscriptions-5f585f04060e) — undated, likely 2021-22, appears never to have shipped past prototype. Closest same-chain analogue to ENC's asset layer, and it never reached real users.

7. **No real-world Harberger-style system found — art, land, domains, or otherwise — has a protocol-set price rather than a self-assessed one.** TAIAOS, Wildcards, radical.domains, and LEMS all put price-setting in the holder's hands. ENC's design (protocol sets the price, moving it with M2) has no direct precedent here; it's closer in spirit to a fixed forced-sale strike price than to Harberger taxation, which is *defined* by the self-assessment step. That's a structural difference, not a tuning knob, and worth naming plainly.

8. **Zora's "hyperstructure" work (perpetual auctions, finder's fees, embedded royalties) is a different mechanism family** — auction/royalty value capture, not continuous rent-and-forfeiture — and isn't a Harberger precedent. Doesn't inform the forced-sale question; dropped from further consideration.

## Precedents

| Project | Mechanism | What happened | Lesson |
| --- | --- | --- | --- |
| TAIAOS (2019, v2 later) | Self-assessed price, 5%/yr → 100%/yr patronage to artist, forced sale | 3 turnovers, then 1 long-term holder; ~18.4 ETH raised in v1; v2 rate hike was a deliberate stress test | Even the field's own extreme test topped out at 100%/yr — ENC's placeholder is ~180x that |
| Wildcards (2020) | Self-assessed price, monthly tax to conservation charities, forced sale | $130k+ raised for charity; rate/turnover/dormancy unverified (source unreachable) | Charity-framed Harberger can attract capital even if game mechanics are murky to outsiders |
| ENS (evaluated, rejected) | Considered Harberger tax for domain names; adopted bid-driven capped fees instead | Never shipped Harberger for ENS; shipped an alternative with no forced sale | A real team with real, non-speculative users concluded forced sale creates catastrophic externalities and rejected it outright |
| radical.domains | Harberger tax for ENS domains, self-assessed | Testnet only (Rinkeby), never reached mainnet | A direct attempt to Harberger-ize naming never got traction past demo |
| LEMS / SolarSaloon (Solana) | Creator sets tax rate, buyer self-assesses price, forced sale | Devnet only, builder describes it as buggy, no adoption data | Closest same-chain precedent to ENC's asset layer; it never left prototype |

## What this means for ENC

**→ The rate is the headline problem.** 5%/day is roughly two orders of magnitude past the most aggressive real experiment found (TAIAOS v2's 100%/year, itself treated as an extreme stress test). At 5%/day an asset's rent consumes its full price roughly every 20 days — nobody in the precedent set has tested anything close, so there's no evidence this produces "the joke" rather than immediate, universal foreclosure.

**→ ENC removes the one thing that makes Harberger tax an efficiency argument: self-assessment.** Every precedent has the holder set the price and live with the under/over-declare tension. ENC's protocol sets the price and moves it with M2 — closer to a fixed forced-sale strike price with rent attached than to Harberger taxation, which is *defined* by self-assessment. Fine for satire, but don't market it as "a Harberger tax" — that invites informed critics to point out ENC skipped the hard, legitimizing part.

**→ ENS's rejection is the most on-point cautionary tale.** Vitalik's reasoning (unsophisticated holders, high switching costs, forced sale handing power to a bad actor) maps onto ENC's ten legible, ownable assets more than onto TAIAOS's or Wildcards' fungible collectibles. A holder losing an asset to a snipe-buy at a price they never set, inside a satire about the powerless getting fleeced by structural rules, risks the mechanism doing the thing it satirizes, to the player, for real.

**→ No precedent survives long-term active play.** TAIAOS ended with one long-term holder; Wildcards' outcomes are unverifiable at this remove; LEMS never left devnet. If ENC's rent-and-foreclosure loop is meant to stay lively rather than collapse to "the vault owns everything," that needs an explicit design answer — nothing here demonstrates sustained churn at any rate, let alone one two orders of magnitude past anything tried.

**→ A different fairness question replaces self-assessment.** Holders can't hedge by mispricing since ENC sets the price. The open question becomes whether a M2-linked price can outrun what a holder can afford in rent, and whether losing the asset then reads as "the game working" or "bad luck." No precedent has this structure, so none answers it.

**→ Charity framing (Wildcards) reads better than pure-satire framing (TAIAOS) for softening forced-sale discomfort**, unverified but suggestive: Wildcards ties the tax to a legible outside good, versus TAIAOS's artist admitting ambivalence about whether it's still art or a subscription. ENC's "joke" is the outside good, but it's a joke about being fleeced — a harder frame to make forced sale feel *fair* under than "your money helps rhinos."

## Open questions

**→ What decay rate actually produces the intended feel** — churn and contest, not instant universal foreclosure? Nothing here validates 5%/day or offers a substitute; that's a design decision needing its own model, not a literature lookup.

**→ Should ENC's mechanism be marketed as "Harberger tax"** given it drops self-assessment, or is a more accurate name ("protocol-priced forced sale with rent") safer against a false-precedent critique?

**→ Does force-buy on ENC's ten assets need any owner protection** (grace period, cooldown, minimum hold) echoing why ENS backed off pure forced sale — or is "no protection" load-bearing for the satire?

**→ What happens to engagement after the first foreclosure wave** — does play continue, or collapse to "the vault owns everything," as every precedent here trends toward eventually?

## Confidence

**High:** TAIAOS's 5%/yr → 100%/yr rate history and turnover/holder facts (multiple sources); Wildcards' mainnet status and $130k figure; Vitalik's ENS reasoning and the alternative ENS shipped (primary source); the self-assessment definition of Harberger/COST tax (multiple agreeing sources).

**Medium:** That no found precedent uses protocol-set (vs self-assessed) pricing — searched specifically, found none, but coverage of a decade of experiments isn't exhaustive.

**Low / unverified, flagged in text:** Wildcards' specific rate and dormancy/turnover numbers (source unreachable); LEMS/SolarSaloon's status today (source undated, likely 2021-22); whether the 2018 UChicago symposium has been superseded by newer academic treatment — found nothing fresher.
