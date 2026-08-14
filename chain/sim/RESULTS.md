# The genesis parameters, and why they are those

**T15, 2026-08-12.** Every number in [`chain/params.genesis.json`](../params.genesis.json)
that is not fixed by arithmetic was chosen here, from the output of
[`sweep.ts`](./sweep.ts). Re-run it:

```bash
npx tsx chain/sim/sweep.ts          # the sweep these came from
npx tsx chain/sim/index.ts --report # the three legs, at the chosen values
```

The second exits non-zero if the peg ever deadlocks, the vault ever goes
negative, or an epoch pays out more than one pot plus its capped grants. It
exits 0.

## The rule this was decided under

Ruling A is absolute: **no economic parameter may be justified or tuned by
engagement, retention or turnover.** That is precisely how rent came to invert
the thesis — it was hired to force turnover, and at a rate that could do that it
made owning an asset a catastrophic loss.

So what is a parameter allowed to be chosen *for*? **Legibility.** Whether the
sentence it produces is true, short, and says something about money. Plus
exactly one pass/fail, which comes from Ruling C making the faucet the only
route in that BadCode controls: **a patient claimant must be able to reach the
cheapest tenancy.** If that fails the loop does not close and the piece is a
shop window.

The sweep's most useful finding is that this is a narrow question. **Every
combination tried keeps the peg alive** — 49 trials across four floors, five
alphas and five price ladders, zero deadlocks, zero bound breaches. Nothing here
is a safety decision. It is all about what the machine *says*.

## What was chosen

| Parameter | Value | The sentence it buys |
| --- | --- | --- |
| `vault.floorBps` | **5000** | The Emperor keeps **half** of all the money, forever. Only the other half can ever circulate. |
| `faucet.alphaBps` | **1000** | The genesis hoard is handed out over about **two months**; after that the faucet hands out **half of everything the Fed prints**, and the Emperor keeps the other half. |
| `faucet.epochSeconds` | **86400** | Register today, collect tomorrow. |
| `faucet.welcomeGrant` | **1000 ENC** | At the peg that is exactly **one million dollars** of the money supply, and it buys you nothing. |
| `faucet.grantsPerEpoch` | **100** | Caps aggregate grants at about 5% of a day's pot in the steady state. |
| `sanity.maxChangeBps` | **1000** | Clears the largest month in 67 years (**+6.42%, April 2020**) with room. |
| `tenancy.termSeconds` | **2592000** | A month — matching the price-travel window, and the Gazette's monthly front page. |
| `retirement.silenceSeconds` | **31536000** | A year of nobody mentioning money. |
| `assets.genesisPricePpm` | **100 → 10000** | The cheapest column costs **one basis point of all the money there is**; the masthead costs a hundred times that. |

### The floor: half

The sweep found the floor changes almost nothing measurable — 25%, 40%, 50% and
60% all keep the peg alive and all settle the same way, a fraction of a
percentage point above whatever the floor is. So the argument for it is entirely
what it says, and *half* needs no footnote and is checkable in one RPC call.

**Rejected: 4000 bps.** Tempting because it is citable — the Bank of England's
own 2012 analysis found the top 5% of households held 40% of QE's
financial-asset gains. It was rejected because it needs a paragraph of
explanation to land, and a number that needs explaining is a worse number.

### Alpha: 10% of the surplus per epoch

This one has a real consequence, and the sweep measures it: how long the
Emperor's opening hoard — half the money supply — takes to distribute.

| α per epoch | hoard reaches the floor | settles at (floor 50%) |
| --- | --- | --- |
| 1.00% | never (in 50 years) | 50.97% |
| 2.50% | never | 50.48% |
| 5.00% | 145 epochs (4.8 months) | 50.32% |
| **10.00%** | **54 epochs (1.8 months)** | **50.26%** |
| 20.00% | 21 epochs (0.7 months) | 50.25% |

The argument for 10% is legibility, not speed: **a visitor should be looking at
the machine's permanent behaviour, not at a launch giveaway.** At 1% the opening
hand-out never really ends inside a human attention span, so every number a
visitor reads in the first years is unrepresentative of what the thing actually
does. At 10% the machine settles into its steady state inside two months, and
stays there for as long as it runs.

**What the steady state actually is — corrected 2026-08-13.** This section used
to say the faucet then distributed *precisely* the money the Fed prints and not
one token more. It does not. **It distributes half of it.**

The floor is why, and the reason is exact rather than approximate. The floor is
half of a supply that is itself growing, so every token minted raises the floor
by half a token: the vault has to retain half of each release simply to stay
level with its own floor, and only the other half is ever above the floor for the
pot to be a fraction of. With `f` the floor as a share of supply, `α` the fraction
of the surplus paid per epoch and `g` the per-epoch growth in supply, the surplus
settles at `g(1−f)/(g+α)` of supply and therefore

```
pot / newly minted  =  α(1−f) / (g+α)   →   1 − f   as g gets small
```

At the shipped `f = 5000 bps` that is **one half**, and `g` here is small enough
to make it exact to three figures: **0.4991** at the historical median month,
**0.4992** at the trailing-20-year CAGR. Measured rather than derived, across
years ten to fifty of a fifty-year forward run at the chosen parameters:
**0.497**. Over the *whole* run it reads 0.52, because the genesis hoard is still
going out — which is the same trap as the two-epochs-to-a-column number below.

So the sentence that survives is the sharper one anyway: **the Emperor keeps half
of everything printed and hands out half.** Every ENC that reaches a wallet still
came from a Federal Reserve release; half of every release simply never leaves.
The vault does not sit at a flat fraction above its floor — it jumps to about
26 bps above it on the day of a release and decays back toward the floor over the
month, which is the 50.26% / 50.00% pair in the sweep above.

### The ladder: one basis point to one percent

Prices are stored as **parts per million of the money supply**, never as a fixed
number of tokens. That distinction is the whole lesson of T29: a price in tokens
would be a constant measured against an exponentially growing M2, which is
exactly the shape that had to be deleted from the sanity caps. As a fraction it
holds forever, because every sync rescales all ten by the same factor — so the
masthead is always the masthead.

| slot | ppm | bps | at genesis | claimants it can support |
| --- | --- | --- | --- | --- |
| 0 (cheapest) | 100 | 1.00 | 2,217,610 ENC | 5,000 |
| 1 | 170 | 1.70 | 3,769,937 ENC | 2,941 |
| 2 | 280 | 2.80 | 6,209,308 ENC | 1,785 |
| 3 | 460 | 4.60 | 10,201,006 ENC | 1,086 |
| 4 | 770 | 7.70 | 17,075,597 ENC | 649 |
| 5 | 1300 | 13.00 | 28,828,930 ENC | 384 |
| 6 | 2200 | 22.00 | 48,787,420 ENC | 227 |
| 7 | 3600 | 36.00 | 79,833,960 ENC | 138 |
| 8 | 6000 | 60.00 | 133,056,600 ENC | 83 |
| 9 (dearest) | 10000 | 100.00 | 221,761,000 ENC | 50 |

**The ceiling law — corrected 2026-08-13, and it was out by a factor of two.**
This section derived the law from "the faucet pays out what the Fed printed",
which is the error fixed above: the faucet pays out **half** of what the Fed
printed, because the floor takes the other half. Every figure in it was therefore
twice what the arithmetic supports, and the wrong ones had already reached
`params.genesis.json` and the published design document.

Corrected: a slot's price is a fixed fraction of supply, and `C` claimants who
all claim every epoch split each pot `C` ways forever, so each accumulates in the
limit a **`1/2C`** share of everything ever printed — and can therefore afford a
slot costing **up to `1/2C` of the total supply, and never more.** Turned around,
which is the useful direction: a slot priced at a fraction `p` of supply is
reachable by at most **`1/2p`** claimants.

That is not a soft trend. Tested against the harness, whose cells were right all
along and are what caught the derivation:

| slot | predicted max crowd | 200 claiming | 500 claiming | 2000 claiming |
| --- | --- | --- | --- | --- |
| 10 bps | 500 | 6 epochs | 64 epochs | never |
| 25 bps | 200 | 64 epochs | never | never |
| 50 bps | 100 | never | never | never |

The bottom row is the one that gives the old law away: at 50 bps the old formula
predicted 200 claimants could get in, and the harness had already measured that
200 never do. The crowds that *do* get in at exactly the predicted ceiling — 500
at 10 bps, 200 at 25 bps — get there off the genesis hoard, which is half the
money supply handed out in the first two months, and not off the steady state.
The clean measurement is the latecomer table below, where the hoard is gone: a
cohort of 4,000 reaches the cheapest column after 309 months, and a cohort of
4,990 stalls at 97.8% of the price forever.

It is the honest replacement for the rent-era "Invariant M", and it is the
scarcity the piece is about. **Stated, it is the caption. Unstated, it is a
nasty surprise.**

### Time to a column — and the number that would have been a lie

The obvious figure to publish is what the harness reports first: at the chosen
parameters a patient claimant affords the cheapest column after **two epochs**.

**That number is true only at launch, and publishing it would have been a false
claim** for everybody who arrives afterwards — the one bug class this project
treats as fatal. It is an artefact of the Emperor's genesis hoard, which is half
the money supply and goes out over the first two months.

So the harness grew a cohort whose measured claimant arrives *after* the hoard
is gone and competes for new printing like everyone else. These are the numbers
that stay true:

| claimants | wait for the cheapest column |
| --- | --- |
| 10 | 22 epochs (0.7 months) |
| 100 | 119 epochs (4.0 months) |
| 1,000 | 1,290 epochs (43 months) |
| 4,000 | 9,271 epochs (309 months) |
| 5,000 | never — and this is the ceiling, not the horizon |

The last row was previously read as "longer than the horizon measured". It is
not: 5,000 is the ceiling itself. Extending the run and walking the crowd size
puts the edge between 4,000, which arrives in 309 months, and 4,990, which peaks
at 97.8% of the price and stays there forever. `1/2p` at 100 ppm is 4,991.

**The published fact, as a sentence:** *anyone patient can afford a small ad —
in about four months, if a hundred other people are being just as patient. The
more of you there are, the longer it takes, and past five thousand it never
happens at all.*

## When the Emperor runs out of counting

The sweep turned up one thing nobody had ticketed, and it is the same shape as
the bug T29 deleted.

`supply = k × M2`, and an SPL token's supply is a `u64`. So there is a largest
M2 this coin can represent: **18,446,744,073,709 — $18,446.7 trillion, about 797
times today's.** Past it `sync_m2` fails the overflow check, and because the
baseline only advances on success it fails forever after. At the historical
median month that is **about 107 years away.**

Unlike `max_single_mint`, this one **cannot be designed away.** `k` and the six
decimals are pinned by the width of a `u64` and the token standard picks the
width. It could be *postponed* — dropping `k` by a factor of a thousand buys
roughly another century — and that was rejected:

- It costs the headline, which is a genuinely good one: **one ENC for every
  $1,000 of America's money.**
- 107 years versus 217 is not a difference an artwork notices.
- **The ending is already graceful, and already built.** The peg stops, nobody
  tells the program about money for a year, and any passer-by may `retire` it.
  Nothing is stranded: escrow still leaves, and the auctions go on at the last
  prices anyone reported. T28 built that for the oracle rotting; it turns out to
  cover this too.
- And it is on-thesis. A coin pegged to a number that grows forever, running on
  a machine with a largest number, is the joke told back to us.

It is pinned as a test (`the peg horizon` in `sim.test.ts`) so that a future
change to `k` cannot quietly shorten the life of the artwork, and stated plainly
in the program's README rather than left for someone to discover.

## What the chosen values do, in full

At the committed parameters, `npx tsx chain/sim/index.ts --report`:

| | the record, 1959–2026 | 50 years forward | the dead state |
| --- | --- | --- | --- |
| releases replayed | 810 | 600 | 810 |
| deadlocked releases | **0** | **0** | **0** |
| catch-up walks needed | 0 | 0 | 0 |
| vault ever negative | no | no | no |
| worst breach of the payout bound | 0 | 0 | 0 |
| vault share, min / final | 47.47% / 50.23% | 50.00% / 50.26% | 100% / 100% |
| hoard reaches the floor | 57 epochs | 60 epochs | never |

The vault dipping to **47.47%** — below its own floor — is not a bug and is
worth understanding: a burn lowers the vault's *share* as well as the supply, so
a long enough contraction walks it under. The floor governs the faucet, never
the burn. What a visitor sees during a tightening is the pot going to zero and
staying there. That is the austerity beat, arriving on its own, out of the
arithmetic.

And the third column is the one that matters most under Ruling A: **the whole
record, with not one participant, and nothing breaks.** The Emperor holds
everything, the ten columns reprice every time the Fed prints, and no one is
watching. It still reads.
