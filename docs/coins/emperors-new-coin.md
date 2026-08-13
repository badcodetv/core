# Emperor's New Coin — the public design

*When they print, we print.*

This is the design document: every mechanism, every parameter, and every claim
we make, with the thing that proves it sitting next to it. The front-of-house
version — the same coin, told as a joke rather than as a specification — is
[`chain/programs/emperors-new-coin/README.md`](../../chain/programs/emperors-new-coin/README.md).
Read that one first if you want to enjoy it. Read this one if you want to check it.

**Status, stated before anything else, because everything below is written in
the present tense.** Nothing is deployed. There is no mint, no live program, no
address you can look up. The oracle's real read path is a stub that returns
`OracleUnavailable`; every green test in this repo runs against a mock feed
under a Cargo feature. The upgrade authority is not burned, because there is
nothing to burn it on yet. What exists is a complete, tested Rust program and a
website that drives it on a local validator. See
[What is actually built](#what-is-actually-built) for the line-by-line.

---

## 1. What it is

ENC is a Solana token whose supply is pegged to **M2** — the headline count of
how many US dollars exist. The Federal Reserve publishes the figure monthly.
When it goes up, anyone on Earth may send a transaction that mints ENC by the
same percentage. When it goes down, that same transaction burns.

The peg is `supply = k × M2` with `k = 1,000,000` base units of ENC per unit of
`m2_value`, which works out at **one ENC for every $1,000 of America's money**.
At the last observation in our copy of the series — June 2026, M2SL = $23,155.2
billion — that is about **23.2 billion ENC**.

Ten assets hang off the peg. They are the ten slots of a newspaper front page —
the **Imperial Gazette** — and their prices are fixed *as a share of the money
supply*, so every time the Fed prints, the price of a column rises by exactly
the printed rate. Whoever holds a slot writes what it says, once, for the month
they paid for.

That is the whole artwork: **your balance is the wage and it sits still; the
assets are the assets and they float away from it at the rate of the printer.**
Nobody takes anything from you. That is the part people find hard to believe.

## 2. The joke, and why the machine has to be honest for it to land

New money is created. It arrives in asset prices first and in wages last, or
never. You are told there is no magic money tree, generally by somebody standing
under one.

ENC runs that arrangement small enough to see all at once. Which means the
arithmetic has to actually do what the caption says — a visitor who works out
the numbers and finds a machine contradicting its own label has caught us, and
that is the one failure mode the artwork does not survive. It has happened once
already: the first design charged asset holders **5% per day** in rent to force
turnover, while the assets appreciate at a median of **0.017% per day** — so the
rent was about **290× the rate the asset gained**, and an asset holder netted
roughly −150% a month. Holding the coin and buying nothing beat owning the asset
by an enormous margin, which is the precise inverse of the thesis the coin
exists to demonstrate. The rent was deleted rather than retuned, because there is
no rate at which one mechanism both forces turnover and stays below M2 growth —
it was a structural conflict, not a number to tune. The full argument is
[the architecture decision](../../design/2026-08-12-enc-architecture-decision.md).

**So there is no holding cost of any kind.** No rent. No demurrage. No fee. No
foreclosure. No permanent delegate. No pause button. Holding ENC already loses,
truthfully, because your balance is unchanged while everything priced against
M2 is not — which is what a peg to the printer *means*, and what happens to a
wage. We did not have to build the cruelty. We removed the things that usually
hide it.

## 3. The machine

Fifteen instructions. This is all of them, and the committed interface at
`chain/idl/emperors_new_coin.json` is the list.

| Instruction | Who may call it | What it does |
| --- | --- | --- |
| `initialize` | the program's upgrade authority, once ever | Creates the mint, the vault, the `Config` whose economic parameters no instruction can ever change, and the `Printer`. |
| `init_asset` | same, ten times | Creates one Gazette slot and its NFT. |
| `sync_m2` | **anyone, no signer at all** | Reads the feed; mints to or burns from the vault; rescales all ten prices. |
| `claim` | anyone | The faucet: take your share of yesterday's pot, register for today. |
| `close_epoch` | anyone | Closes a spent epoch account and keeps its lamport deposit for the trouble. |
| `place_bid` | the bidder, signed | Escrows the bidder's own ENC against a slot. |
| `withdraw_bid` | the bidder, signed | Takes it back, unless it is the live high bid of an unsettled term. |
| `settle_auction` | anyone | Pays the outgoing holder the entire winning bid; hands the tenancy over. |
| `roll_term` | **anyone, no signer at all** | Ends a term nobody won; releases any stale high bid. |
| `mint_certificate` | anyone, paying | Issues the tenancy certificate for a (slot, term). |
| `file_copy` | the current tenant, once per term | Writes up to 280 bytes into the column. |
| `spike` | **the editor**, once per column per term | Replaces a column's text with a fixed redaction marker. |
| `pass_the_pen` | the editor | Hands the pen to a successor. |
| `break_the_pen` | the editor | Ends the editorship, permanently. |
| `retire` | **anyone, no signer at all** | Stops the peg, once the silence condition is already true. |

Three of them — `sync_m2`, `roll_term` and `retire` — have no `Signer` in their
account list whatsoever. Nobody's permission is involved in advancing the peg,
ending a term, or declaring the coin over.

### The peg, and its honest invariant

`sync_m2` is level-targeting, not a ratchet: every release retargets absolutely,
so a downward revision and genuine tightening take the identical code path.

**The invariant is `supply ≥ k × M2`, never `=`.** Burns come out of the vault
and only the vault, because reaching into holders' balances to hit a target is
exactly the power this coin claims not to have. So if the vault cannot cover a
fall, the program burns everything it has and **leaves supply above target**,
says so in the `Synced` event's `uncovered_burn` field, and waits for the next
rise to close the gap. Equality holds whenever the vault was solvent enough to
absorb the last burn, which is almost always. It is not a guarantee, and we do
not state it as one.

This is not hypothetical. The simulation drives the vault under its own floor —
to **47.47%** of supply — on the real 1959–2026 record, because a burn lowers
the vault's share as well as the supply, so a long enough contraction walks it
down ([`chain/sim/RESULTS.md`](../../chain/sim/RESULTS.md)).

There is one speed limit: `max_change_bps = 1000`, so the peg moves at most 10%
of itself per call. It is a **speed limit, not a veto** — a bigger release is
absorbed over several permissionless calls rather than refused. Refusal was
permanent, because the baseline only advances on success, so a single
hyperinflation-scale month would have frozen the peg forever at the exact moment
the thesis was most vindicated. The largest month in 67 years is +6.42%, so in
practice this never fires.

### The Gazette

Ten slots, priced in **parts per million of the money supply** rather than in
tokens. That distinction is load-bearing: a price fixed in tokens would be a
constant measured against an exponentially growing M2, and on a non-upgradeable
program a constant like that is a timer, not a parameter. As a fraction it holds
forever, because every sync rescales all ten by the same factor — the masthead
is always the masthead.

Slots change hands by **scheduled auction** on a 30-day term, aligned to the
30-day window a rescaled price takes to travel to its new level, so an auction
settles against a price that has arrived rather than one still in motion. The
outgoing holder is paid **the entire winning bid** — the current price, whatever
M2 says it is. Never "the new, higher price": M2 fell in 6.1% of months in the
record, and the reserve falls with it.

**The NFT never leaves program custody.** You win a *tenancy*; what lands in
your wallet is a numbered, dated **certificate**, never revoked and never worth
the asset. This is not a consolation prize, it is the only arrangement that
works: putting the NFT in the holder's wallet would require a permanent delegate
to pull it back at settlement — the exact power Ruling A removed — and wallet
residency and permissionless settlement are mutually exclusive. It is also the
better joke. *You never owned the asset. All you keep is the receipt.*

Say the unflattering part plainly, because it is the caption rather than a bug:
**an auction machine allocates by wealth, full stop.** Self-bidding is net-free,
so the richest wallet can hold the masthead indefinitely. This is not a town
square and we will not call it one. It is the front page, sold monthly.

### The faucet

The only route into the economy that we control. Register in epoch *N*, collect
your share of *N*'s pot in *N+1*. The pot is `α × max(0, vault − floor × supply)`,
snapshotted when the epoch opens, and divided by a headcount that has stopped
moving.

That ordering is the whole sybil defence, and it is why this program needs no
identity system: outflow during any epoch is **at most one pot plus the capped
welcome grants**, however many wallets show up. A thousand-wallet farm dilutes
itself and everyone else equally and cannot increase what leaves the vault.

`claim` cannot mint. The mint account is not writable in its context, so the
faucet is structurally incapable of changing the supply — it can only move
tokens a Federal Reserve release already brought into existence.

Below the floor it pays nothing at all: no share, no welcome grant. When the Fed
tightens hard enough, arriving at the faucet gets you nothing. That is not a
bug. That is austerity, reproduced faithfully, and it arrives out of the
arithmetic rather than out of a rule we wrote.

## 4. The parameters, by what they say

Chosen at T15 from the simulation sweep and recorded in
[`chain/sim/RESULTS.md`](../../chain/sim/RESULTS.md); the live values are
[`chain/params.genesis.json`](../../chain/params.genesis.json). The rule they
were chosen under is absolute: **no economic parameter may be justified or tuned
by engagement, retention or turnover.** That is exactly how rent came to invert
the thesis. Legibility is the only permitted argument, plus one pass/fail — a
patient claimant must be able to reach the cheapest tenancy, because otherwise
the loop does not close and the piece is a shop window.

| Parameter | Value | The sentence it buys |
| --- | --- | --- |
| `vault.floorBps` | 5000 | **The Emperor keeps half of all the money, forever.** Only the other half can ever circulate. |
| `faucet.alphaBps` | 1000 | The genesis hoard goes out over about **two months**; after that the faucet hands out **half of everything the Fed prints, and the Emperor keeps the other half**. |
| `faucet.epochSeconds` | 86400 | Register today, collect tomorrow. |
| `faucet.welcomeGrant` | 1000 ENC | At the peg that is **exactly one million dollars** of the money supply, and it buys you nothing. |
| `faucet.grantsPerEpoch` | 100 | Caps aggregate grants at roughly 5% of a day's pot in the steady state. |
| `sanity.maxChangeBps` | 1000 | Clears the largest month in 67 years (+6.42%, April 2020) with room. |
| `tenancy.termSeconds` | 2592000 | A month — the price-travel window, and a front page sold monthly. |
| `retirement.silenceSeconds` | 31536000 | A year of nobody mentioning money. |
| `assets.genesisPricePpm` | 100 → 10000 | **The cheapest column costs one basis point of all the money there is.** The masthead costs a hundred times that. |

The floor is *half* because half needs no footnote and is checkable in one RPC
call. The sweep found every floor from 25% to 60% keeps the peg alive and
settles the same way, so the argument for it is entirely what it says. Forty
percent was rejected despite being citable — the Bank of England's 2012 finding
that the top 5% of households held 40% of QE's financial-asset gains — because
it needs a paragraph to land, and a number that needs explaining is a worse
number.

**The faucet is a half pass-through, and that is where the ceiling law comes
from.** Once the genesis hoard is gone the faucet does *not* hand out what the
Fed printed. It hands out half of it. The reason is the floor: the floor is half
of a supply that is itself growing, so every time the Fed prints, the Emperor has
to keep half of the new money simply to stay level with his own floor, and only
the other half is ever above it to be paid out. Written down, with `f` the floor
as a share of supply, `α` the fraction of the surplus paid per epoch and `g` the
per-epoch supply growth: the surplus settles at `g(1−f)/(g+α)` of supply, so the
pot settles at

```
pot / newly minted  =  α(1−f) / (g+α)   →   1 − f   as g gets small
```

At `f = ½` that is **one half**, and `g` is small enough here to make it exact to
three figures: **0.4991** at the historical median month (+0.522%), **0.4992** at
the trailing-20-year CAGR (+6.28%/yr). The simulation measures **0.497** across
years ten to fifty of a fifty-year run — years one and two are excluded because
the genesis hoard is still going out and drags the whole-run figure to 0.52. So
the honest sentence is the better one:
**the Emperor keeps half of everything printed and hands out half.**

**The ceiling law falls straight out of it, and it is the scarcity the piece is
about.** A slot costs a fixed fraction of supply, and `C` claimants who all claim
every epoch split the pot `C` ways forever. So each accumulates, in the limit, a
`1/2C` share of everything ever printed — and can afford a slot costing up to
**`1/2C`** of the supply, and never more. Turned around: a column priced at a
fraction `p` of the money supply is reachable by at most `1/2p` claimants. The
cheapest column at 100 ppm therefore supports about **five thousand** diligent
claimants; the masthead at 10,000 ppm supports about **fifty**. Stated, that is
the caption. Unstated, it is a nasty surprise.

It is a hard edge rather than a trend, and the harness finds it where the
arithmetic puts it: a cohort of 4,000 all claiming every epoch reaches the
cheapest column after 309 months, and a cohort of 4,990 never does — it stalls at
97.8% of the price and stays there, because the price is running away at exactly
the rate the money is arriving.

The published sentence, measured against a cohort arriving *after* the genesis
hoard is gone: *anyone patient can afford a small ad — in about four months, if
a hundred other people are being just as patient. The more of you there are, the
longer it takes, and past five thousand it never happens at all.*

## 5. Who can change the rules

**No key over the money; one pen over the words.**

That sentence is two parts and it is never said as one. Both halves are true and
neither survives without the other.

### No key over the money

There is no instruction anywhere in this program that changes an economic
parameter. Not gated behind an authority — **absent**. `k`, the floor, alpha,
the welcome grant, the term, the epoch, the silence clock, the sanity cap and
the expected feed id are written once at `initialize` and there is no code path
anywhere that writes any of them again; the program ships non-upgradeable, so
"not even we can change the rule" is a property of the binary rather than a
promise.

Be exact about what *is* mutable in `Config`, since three fields are.
`initialized_assets` counts to ten during bootstrap and stops. `retired` flips
once, permissionlessly, when a condition the program checks about itself is
already true. `editor` is the pen, and only the pen's own holder can move it.
Nothing else in that account ever changes, and none of those three is an
economic parameter.

The mint authority is the vault PDA — an address derived from the program with
no private key anywhere on Earth — and it takes orders only from the published
M2 figure. The freeze authority is `None`. No key can mint, burn, move, freeze
or seize a token. **No path in this program moves a token out of any wallet
without that wallet owner's signature**, and the test suite asserts it against
the published interface rather than leaving it as a claim.

Two fields move without a key, and both are one-way latches that are nobody's
decision: `initialized_assets` counts to ten during bootstrap and stops, and
`retired` flips once when a condition the program checks about *itself* is
already true.

### One pen over the words

`Config.editor` is a key, and it is the only one. It reaches exactly one
instruction, `spike`, which replaces a column's copy with a fixed marker it does
not get to choose. Once per column per term.

**State the blast radius plainly: a stolen pen can vandalise ten columns a
month, and it cannot move a token.** Not one ENC, not one NFT, not one
certificate. `spike`'s account list is two accounts and a signer — no mint, no
token account, no token program — so there is nothing there for a stolen key to
reach, and `initialize.ts` asserts that the editor appears in no token-moving
instruction.

It exists because there is no on-chain answer to vile text, and pretending
otherwise is how a project like this gets ugly. A newspaper has an editor. The
pen is rotatable (`pass_the_pen`, because after the burn there is no upgrade
authority to recover a lost key with) and breakable (`break_the_pen`,
irrevocably, after which the paper goes feral).

This was never a decentralisation play. **The trustless surface is the money**,
and every claim in this document about the money survives the pen verbatim. The
column is for sale. The pen is not.

### The residual we could not remove

One honest asterisk, stated loudly because it is on-theme.

A Switchboard feed *is* the cryptographic hash of its own fetch job, so pinning
the hash pins the data source: edit one character of the job and you have not
repointed the feed, you have created a different feed the program refuses to
read. Good. But the oracle network's operators are admitted by **its queue
authority**, which is not ours and never will be — so a small consortium still
decides who may sign for reality.

**We removed ourselves from the loop. We could not remove the loop.** Anyone who
tells you their oracle has no such residual has either not looked or is not
saying.

### And when the scanner says DANGER

It will, and it is right, and we would like to quote it before anybody else
does.

RugCheck reports **"Mint Authority still enabled" — danger, weight 50,000, its
heaviest** — for tokens whose mint authority is alive. ENC's is alive and always
will be, because a peg that cannot mint is not a peg. So: **this coin is
arbitrarily inflatable.** That is not a caveat buried in a risk section, it is
the entire product. It is arbitrarily inflatable **by the Federal Reserve**, and
by nobody else, because the authority is a program-derived address owned by a
non-upgradeable program that takes orders only from a published number.

A person can verify that in about ten minutes. An automated scanner cannot, and
will not, and will keep saying danger forever. A coin about money printing,
flagged by the machines as a money-printing risk: we could not have bought
advertising that good. It stands, unsuppressed, and we will not seek a
trust-listing to make it go away.

## 6. The market: closed loop by posture

**BadCode seeds no liquidity pool and sells no ENC, ever.** No sale, no presale,
no allocation, no fee, no treasury position we can exit. We take nothing from
the auctions — the full winning bid goes to the outgoing holder. There is no
route from your pocket to ours, and we declined to build one.

Say the posture; do not overstate the mechanism. **ENC is a plain SPL token and
anyone may pool it.** We cannot prevent that and we do not claim to. If a market
appears somewhere it is someone else's decision and someone else's risk; we
neither prevent it nor point at it. What we sell is nothing. What we promise is
the rule.

## 7. How it ends

It runs **forever**. Two exceptions, and one of them is arithmetic.

### The Emperor runs out of counting

An SPL token's supply is a `u64`, so `supply = k × M2` has a largest M2 it can
represent. That number is `u64::MAX / k = 18,446,744,073,709` units of
`m2_value`, which is **$18,446.7 trillion of M2 — about 797 times the last
figure in our copy of the series.** At the historical median month of +0.522%
that is **about 107 years away**. Past it `sync_m2` fails its overflow check,
and because the baseline only advances on success, it fails forever after.

We could have bought roughly another century by dropping `k` by a factor of a
thousand, and we decided not to. It costs the headline, which is a good one; 107
years versus 217 is not a difference an artwork notices; the ending below
already covers it gracefully; and a coin pegged to a number that grows forever,
running on a machine with a largest number, is the whole joke told back to us.
It is pinned as a test so a future change to `k` cannot quietly shorten the life
of the artwork, and it is stated here rather than left to be discovered.

### Or nobody says anything for a year

If a full `retirement_silence_seconds` — 365 days — passes in which no new M2
figure reaches the program, **anyone may call `retire`.** No key is consulted,
the instruction has no signer at all, and a passer-by can simply observe that it
is over. The flag it sets is permanent and nothing anywhere can set it back —
though calling `retire` a second time is deliberately not an error, because
refusing would make "anyone can walk up and see that it ended" throw at the
second person who looks.

Be exact about what that trigger measures: *no new M2 figure reached this
program for a year.* The program cannot know why, and **oracle silence is not
Fed silence** — over a forever horizon the likelier causes are the oracle stack
rotting against a pinned hash on a non-upgradeable program, or nobody left who
cared to crank. Which is also the better joke: the coin ends when nobody has
told it about money for a year, whether because the dollar ended or because
everyone stopped looking, and from where it sits those are the same event.

**Retirement stops exactly one thing: the peg.** The auctions go on forever, at
the last prices the Fed ever reported — the machine grinding on, trading at the
valuations of a vanished world. Bids still go in and still come out; nothing is
stranded by the end of the world. Freezing it as a final exhibit was considered
and rejected: a freeze would have had to keep every escrow exit alive anyway or
strand live bids permanently, so it is both the less true ending and the more
dangerous one.

## 8. The claim ledger

Every factual claim this project makes, and the thing that proves it. If you
find a sentence anywhere in our copy that is not literally true, file an issue —
that is the one bug class this project treats as fatal.

The M2 figures below were **re-derived at T21 (2026-08-13) directly from the
committed FRED M2SL record** at [`chain/sim/m2-history.csv`](../../chain/sim/m2-history.csv)
(810 observations, 1959-01 to 2026-06), not quoted from a secondary source.

| Claim | Figure | How to check it |
| --- | --- | --- |
| M2 rises far more often than it falls | rose in **758 of 809** months (93.7%), fell in 49 (6.1%), unchanged in 2 | `m2-history.csv`, month on month |
| The median month | **+0.522%** — about 0.017% per day | same |
| The biggest month in the record | **+6.42%**, April 2020 | same |
| The biggest monthly fall | **−1.40%**, March 2023 | same |
| Long-run growth | **6.73%/yr** since 1959; 6.28% trailing 20y; 5.62% from 1990; 6.08% from 2015 | compounded endpoint to endpoint |
| Three-year windows | rose in **770 of 774**; worst outcome **−0.54%**; median multiple **1.222×** | rolling 36-month windows |
| The 2022–23 contraction | **−4.82%** peak to trough, $1,049.7bn, March 2022 → October 2023 | the only drawdown of 1% or more in the entire record |
| …including | a run of **nine consecutive falling months**, Aug 2022 → Apr 2023 — the longest in the record | consecutive month-on-month falls |
| The peg's last number | **$18,446.7 trillion**, ~797× today's, ~**107 years** at the median month | `u64::MAX / k`, then compound at +0.522%/month |
| Genesis supply | **22.176 billion ENC** at M2 = $22,176.1bn — one ENC per $1,000 | `GENESIS_M2_VALUE × k`, at 6 decimals |
| The cheapest column | 100 ppm = **1.00 basis point** of supply = 2,217,610 ENC at genesis | `params.genesis.json`, × genesis supply |
| The welcome grant | 1,000 ENC = **$1,000,000** of the money supply | 1e9 base units ÷ 1e6, × $1,000 |
| The Emperor's floor | **half** of all supply, forever | `floorBps = 5000` |

Everything re-runs. From the repo root:

```bash
node design/research/2026-08-12-enc-tokenomics/m2-backtest.mjs   # fetches its own CSV
npx tsx chain/sim/index.ts --report                              # the three simulation legs
npx tsx chain/sim/sweep.ts                                       # the parameter sweep
```

### Claims we do not make

Held to the standard in
[the architecture decision, §4](../../design/2026-08-12-enc-architecture-decision.md):

- Never **"guaranteed to rise."** Say *it tracks M2, whatever M2 does* — which
  makes the 2022–23 burn a feature rather than an embarrassment. **This escaped
  once and it is worth naming where:** the Gazette masthead on the live page
  read *"priced in a currency that only goes up"* until 2026-08-13. The
  forbidden claim will not arrive labelled as one; it arrives as a strapline
  somebody wrote in a hurry because it scanned well.
- Never **"the faucet pays out what the Fed printed."** It pays out **half** of
  it — the floor is half of a growing supply, so the vault retains half of every
  release just to stay level with itself. The true version is the better joke
  and it is also the one that survives someone checking.
- Never **"the Fed prints money and hands it to Wall Street."** That conflates
  QE, bank lending and fiscal transfers, and 2020–21 was transfer-heavy. Say
  *when the money supply expands, asset owners benefit disproportionately and
  first.*
- Never **"guaranteed to keep printing."** The forward-looking line is incentive
  and record, not prophecy: debasement is every indebted government's cheapest
  exit, M2 has risen in about 94% of months since 1959, and the debt only points
  one way.
- Never **"paid the new, higher price."** The auction pays the current price,
  whatever M2 says it is.
- Never **"no admin key"** unqualified. One key exists. Say both halves.
- Never **"nobody can change that, including us"** while the upgrade authority
  is alive. Non-upgradeability is a property of the shipped binary, and until
  T22 burns the authority the honest form names the gap: *that is what ships,
  and it has not shipped.*
- Never **"ENC cannot be traded."** We seed nothing and sell nothing; anyone
  else may pool a plain SPL token.
- Do not call it a **Harberger tax**. Self-assessment was removed, and that was
  the mechanism's entire justification.
- **Do not claim wages never rose.** The strongest version of the counterargument,
  stated for the other side: from 2019 to 2024 US real wages for low-wage workers
  rose about **15.3%** (EPI), the fastest in decades, spanning the fastest money
  growth in modern history — while average real hourly earnings *fell*
  year-over-year for 25 straight months inside that same window. The joke lives
  in the long-run divergence, not in any one year, and the 2022–23 tightening was
  the *worst* stretch for real wages, so the converse does not hold either.

The economics are anchored on: the Bank of England's 2012 finding that the top
5% of households held 40% of QE's financial-asset gains; the Fed's Distributional
Financial Accounts (Q4 2024: top 1% hold ~33% of wealth, bottom 50% hold ~2.5%);
and Case-Shiller, 100 → 332.7 since 2000.

## 9. What is actually built

Stated plainly, because a design document written in the present tense is
otherwise a claim about a thing that does not exist.

| | State |
| --- | --- |
| The Rust program | **Complete.** 15 instructions in a default build (17 with the two mock ones compiled in), **42 unit tests**, eight Anchor suites of 92 cases. Counted and re-run 2026-08-13: `cargo test -p emperors-new-coin --lib` reports 43 passing, the forty-third being Anchor's own generated `test_id`. `retire` is one of the eight and runs alone, because passing it ends the ledger. |
| The oracle, mock | **Works.** `--features mock` compiles a `MockOracle` and `set_mock_m2`. This is what localnet runs and what every green test uses. |
| The oracle, real | **Not built.** `oracle::read_quote`'s non-mock body returns `OracleUnavailable` unconditionally, and the crate has no Switchboard dependency at all. **A default build cannot sync.** That is T18. |
| The M2 feed | Authored, and its hash-immutability property proven live. The **release-date** extraction it needs does not exist yet — the committed job pulls the value only — and `retire` is only correct once that date is Fed-sourced. |
| The website | Read and write paths live on localnet at `/coins/enc`. |
| Deployment | **None.** No devnet, no mainnet, no addresses. That is T22, which also burns the upgrade authority — **not yet done, and not to be claimed until it is.** |

The mock instructions are compiled out of a default build and are absent from
the committed IDL, and `initialize.ts` asserts that against the committed file
rather than the build output. Verified while writing this: zero occurrences of
`set_mock_m2` or `mock_fund` in `chain/idl/emperors_new_coin.json`.

## 10. Why we built it

Because nobody reads the essay. People remember stories and absorb songs, so we
make comics, tracks, and — this once — a working scale model of the problem. It
is an artwork in a frame, not an ecosystem. It does not need players, volume, a
market price or a living economy, and it is fine if it dies and nobody cares: a
dormant Gazette is ten columns of the Emperor's own copy, priced, repricing
every time the Fed prints, with nobody bidding. That still reads.

If one person holds a balance for a month, watches the columns drift upward out
of reach exactly on schedule, and thinks *wait, this is just my actual life* —
the artwork worked.

Humans: you can all see it. Say it sooner.

---

**Nothing here is financial advice, an offer, or a promise of value.** There is
no value, which for once is not a confession but the design. The mechanisms are
deliberately harsh and completely disclosed.

Related: [the implementation plan](../../design/2026-08-06-solana-toolchain-and-emperors-new-coin.md)
· [the architecture decision](../../design/2026-08-12-enc-architecture-decision.md)
· [the genesis parameters](../../chain/sim/RESULTS.md)
· [the toolchain](../../chain/README.md)
· story canon: [The Magic Money Tree](../stories/magic-money-tree/emperors-new-coin.md)

*BadCode · regrettably, from the future · the mistake is optional*
