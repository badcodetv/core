# Emperor's New Coin

*When they print, we print.*

**Status: being built in the open.** Nothing is deployed and nothing is for
sale — that second part is permanent, and most of this page is about why.
Until mainnet, the present tense below describes the program as designed and
tested; at launch, every sentence of it becomes checkable with one RPC call.

## What this is

ENC is a Solana token whose supply is pegged to **M2** — the headline measure
of how many US dollars exist. When the Federal Reserve reports more dollars,
anyone on Earth can press a button and this coin mints by the same percentage.
When the Fed reports fewer, it burns. At today's M2 that is about 23 billion
ENC: **one ENC for every $1,000 of America's money.** The rule is
`supply = k × M2`, and there is no second rule.

We are BadCode, an art collective. We make comics, drum & bass, and — now —
economic machinery. ENC is an artwork about money printing, built out of the
thing it is about. It is not an investment. Everyone says that; we went
further and engineered it: **there is no way to give us money.** No sale, no
presale, no allocation, no fee, no pool. The coin comes free from a faucet,
and the joke is the product.

## The joke

Here is the arrangement the last century settled into, compressed:

1. New money is created — trillions, when needed.
2. It lands in asset prices first: houses, equities, everything already owned.
3. Wages get there last, or not at all.
4. You are told there is no magic money tree, usually by someone standing
   under one.

ENC runs that arrangement in miniature, in public, with the numbers showing:

- **Your ENC balance is the wage.** It sits still. Nobody takes anything from
  it — no rent, no fee, no decay. It just… sits there. While —
- **Ten parody assets** — the Emperor's treasures — reprice by exactly the
  percentage M2 moved. Automatically. Forever. Upward, historically, about
  94% of the time. The moment the Fed publishes, the assets glide away from
  your balance at precisely the printed rate.
- So holding the coin loses to holding the asset — not because we tax you,
  but because that is what a peg to the printer *means*. We did not build the
  cruelty in. We removed everything that usually hides it.

Don't hold the coin. Hold the asset. You have been living in this demo your
whole life; ours is just small enough to see all at once.

## The machine, in one breath

The Fed publishes M2 monthly. A hardware-attested oracle network fetches it —
the feed is the cryptographic hash of its own fetch job, so no key exists
that could point it somewhere else. Anyone may call `sync_m2` for a fraction
of a cent: supply moves to `k × M2`, minted to (or burned from) the Emperor's
vault, and all ten asset prices rescale by the same ratio, gliding to their
new levels over thirty days so they tick every slot. There is one speed
limit — the peg will not move more than 10% of itself in a single call, so a
figure wilder than that arrives in instalments rather than all at once. A
real month is a fraction of a percent, so you will never see it. A daily faucet drips ENC
from the vault to whoever shows up. The ten assets re-auction on a published
clock, roughly monthly: the winner takes the tenancy and a certificate, and
the outgoing holder is paid the entire winning bid. That is the whole
machine.

## Questions you are already asking

### Is this a scam?

A scam needs a route from your pocket to ours, and we declined to build one.
BadCode sells no ENC, holds no allocation, seeds no liquidity, charges no
fee, and takes nothing from the auctions — the full winning bid goes to the
outgoing holder. The only source of ENC is a faucet that pays *you*. If you
gave someone money for ENC, you invented that part yourself, and we would
gently ask what you were thinking.

### Then why does the risk scanner say DANGER?

RugCheck will report **"Mint Authority still enabled" — danger, weight
50,000, its heaviest** — because the mint authority is alive and always will
be. The scanner is correct. This coin is arbitrarily inflatable… **by the
Federal Reserve.** The authority is an address owned by a non-upgradeable
program that takes orders only from the published M2 number; no human hand
can sign for it — which a person can verify and an automated scanner cannot.
A coin about money printing, flagged by the machines as a money-printing
risk: we could not have bought advertising that good, so we quote it here
before anyone else can.

### Can I make money on this?

We have gone to unusual lengths to make that difficult. ENC has no price from
us — no pool, no chart, no roadmap with an arrow on it. The assets appreciate
*measured in ENC*, and ENC is given away. If a market for it appears
somewhere, that is someone else's decision and someone else's risk; we
neither prevent it nor point at it. What we sell is nothing. What we promise
is the rule.

### How do I get ENC?

The faucet. Register today; come back tomorrow and split yesterday's pot with
everyone who registered beside you. The pot does not grow when the crowd
does, so a thousand-wallet bot farm mostly dilutes itself — and you. Welcome
to scarcity. Every wallet is owed one small welcome grant, paid on the first
visit where the day's allotment has not run out and the Emperor's vault sits
above its floor; refused, it is not lost, and you can come back for it. When
the Fed tightens hard enough, the faucet stops entirely — no share, no grant.
Arrive during the tightening and there is nothing for you. That is not a bug.
That is austerity, reproduced faithfully.

### What do I actually own?

Careful with that word — it is the theme. **The coin is yours:** a plain SPL
token in your wallet, and no instruction in this entire program can move a
token out of any wallet without its owner's signature. Not ours, not
anyone's. **The assets are never yours.** You win a *tenancy* at auction,
hold it for a published term of about a month, and then it re-auctions. If
someone outbids the reserve, the flag passes to them and you are paid their
entire bid — the current price, whatever M2 says it is. What stays in your
wallet forever is a numbered, dated **tenancy certificate**: never revoked,
never altered, never worth the asset. The magnificent thing was never yours.
The receipt always will be.

### What happens when the Fed prints?

Supply mints — into the Emperor's vault, because new money arriving at the
top first is not our invention; we are merely publishing the plumbing. All
ten asset prices rise by the same percentage over the following month, and
your balance performs the traditional role of a wage: it holds very still.

### And when the Fed tightens?

The coin burns — from the vault, never from a wallet. If the vault ever
cannot cover a fall, supply sits above target until the next rise catches
up, and the chain says so plainly. This is not hypothetical: M2 fell 4.8%
peak-to-trough in 2022–23, the first sustained decline since the 1930s, and
the program handles a repeat by design. **It tracks M2, whatever M2 does.**
For scale, from the full 1959–2026 record: M2 rose in about 94% of months,
and in 770 of 774 rolling three-year windows; the worst three-year outcome
in 67 years was −0.5%. We like those odds; we do not sell them. As for
direction — a government that owes tens of trillions has exactly one
comfortable exit, and the exit is the loom. That is an incentive, not a
prophecy. The debt only points one way.

### Didn't wages actually rise during the big print?

Some did — and here is the strongest version of your own argument, free of
charge: from 2019 to 2024, US real wages for low-wage workers rose about
15.3% (EPI's figure), the fastest in decades, largely because a tight labour
market made employers compete for people. The joke does not live in one
year; it lives in the long run. Since 2000, US house prices have roughly
tripled (Case-Shiller). The Bank of England's own 2012 analysis found the
top 5% of households held 40% of the financial-asset gains from QE. The
Fed's own distribution data puts about a third of US wealth with the top 1%
and 2.5% with the bottom half. The machine exaggerates — instant,
one-to-one, no mercy — because that is what satire is for. The numbers
printed beside it are exact.

### Who can change the rules?

Nobody — and the nobody provably includes us. The program ships with its
upgrade authority burned. The economic parameters have no update
instruction: not gated behind an authority — *absent*. The oracle feed is
the hash of its own fetch job: edit one character and you have not changed
the feed, you have created a different feed the program refuses to read. No
admin key, no pause button, no owner field. One honest asterisk, stated
loudly because it is on-theme: the oracle network's operators are admitted
by its queue authority, so a small consortium still decides who may sign
for reality. We removed ourselves from the loop. We could not remove the
loop.

### How does it end?

Two ways, and one of them is arithmetic.

**The Emperor runs out of counting.** A token's supply is a 64-bit number, so
`supply = k × M2` has a largest M2 it can represent: **$18,446.7 trillion**,
about 797 times today's. At the median month of the last 67 years that is
roughly **107 years away**. Past it the peg simply cannot do the sum, stops,
and never starts again. We could have bought another century by pricing the
coin differently and we decided not to hide it: a coin pegged to a number
that grows forever, running on a machine with a largest number, is the whole
joke told back to us. You can check the figure yourself — it is one division.

**Or nobody says anything for a year.** If a full year passes in which no new
M2 figure reaches the program, anyone — you, a stranger, a bot with a cent —
may call `retire`. Once, permanently. No key is consulted and no announcement is
made; the instruction takes no signer at all, so a passer-by can simply
observe that it is over. The program cannot tell whether the Fed went dark
or everyone stopped looking, and from where it sits those are the same
event.

And then it keeps going. Retirement stops exactly one thing — the peg. The
ten columns go on auctioning, forever, at the last prices the Fed ever
reported: the machine grinding on, trading at the valuations of a vanished
world, because nobody told it the numbers had stopped meaning anything. Your
bids still go in and still come out; nothing is stranded by the end of the
world. We considered freezing it all as a final exhibit and decided this was
truer, and it costs no extra code — the prices were always going to stop
moving on their own.

### Why ten assets, and what are they?

Ten because scarcity is the point — the joke needs things there are not
enough of. What they are, exactly, is a creative decision still being fought
over in the other room. They will be magnificent, and you will not own them.

### Why did you build this?

Because nobody reads the essay. People remember stories and absorb songs, so
we make comics, tracks, and — this once — a working scale model of the
problem. If one person holds their balance for a month, watches the assets
drift upward out of reach exactly on schedule, and thinks *"wait, this is
just my actual life"* — the artwork worked. Humans: you can all see it. Say
it sooner.

## Check our arithmetic

Every number above re-derives from the full FRED M2SL series on demand — from
the repo root:

```
node design/research/2026-08-12-enc-tokenomics/m2-backtest.mjs
```

(it fetches the CSV itself on first run). Design and decision history:
[the implementation plan](../../../design/2026-08-06-solana-toolchain-and-emperors-new-coin.md)
and [the architecture decision](../../../design/2026-08-12-enc-architecture-decision.md).
Story canon: [The Magic Money Tree](../../../docs/stories/magic-money-tree/emperors-new-coin.md).

## The fine print

This is an artwork. Nothing on this page is financial advice, an offer, or a
promise of value — there is no value, which for once is not a confession but
the design. The mechanisms are deliberately harsh and completely disclosed.
If you find a sentence here that is not literally true, file an issue: that
is the one bug class this project treats as fatal.

---

*BadCode · regrettably, from the future · the mistake is optional*
