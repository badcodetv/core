# ENC token economics — research base, 2026-08-12

Ten parallel research briefs commissioned by Kai to answer one question before
any more of the ENC program gets built: **what token economics let the joke land,
rather than triggering the fear and doubt that stops people getting it?**

The joke, stated by Kai: *when the Fed prints, asset prices rise and wages don't.
So don't buy ENC as a speculative bet — hold ENC in order to buy the assets,
because the assets are guaranteed to rise measured in ENC.* ENC does not need
real-world value. It needs an envelope that doesn't crumble when you look at it.

Nothing here is committed to canon. These are inputs to a design decision, and
several of them argue against what is already built on `feat/enc-program`.

| # | Brief | The one thing in it |
| --- | --- | --- |
| 01 | [Elastic supply and rebase](./01-elastic-supply-and-rebase.md) | Mint-100%-to-treasury has no working precedent; survivors keep holders' % share constant |
| 02 | [Harberger and forced sale](./02-harberger-and-forced-sale.md) | Highest rate ever deployed was 100%/yr as a stress test; ENS evaluated forced sale and walked away |
| 03 | [Custody, clawback, delegation](./03-custody-clawback-and-delegation.md) | Our two custody powers are the two things Solana scanners flag hardest; Streamflow escrow is the live alternative |
| 04 | [Distribution, liquidity, price](./04-distribution-liquidity-and-price.md) | No launch mechanism exists that is compatible with "the treasury never sells" |
| 05 | [Faucets, sinks, game economies](./05-faucets-sinks-and-game-economies.md) | No game economy anywhere runs anything near 5%/day; dormancy is the evidence-consistent outcome |
| 06 | [MEV, front-running, bots](./06-mev-frontrunning-and-bots.md) | Every input is public and computable; the ten assets get bot-owned within days |
| 07 | [Regulatory and platform](./07-regulatory-and-platform-landscape.md) | The coin is close to the safe pattern; the **NFTs** are the exposed part. UK promotion rules already apply |
| 08 | [Art coins, mechanism as artwork](./08-art-coins-and-mechanism-as-artwork.md) | Nobody is called a rug for a *disclosed* harsh mechanism — only for a false factual claim |
| 09 | [Cantillon and the real numbers](./09-cantillon-and-the-real-numbers.md) | 2021–24 is the empirical embarrassment; root the copy in the long run and the BoE's own admission |
| 10 | [Alternative architectures](./10-alternative-architectures.md) | Demurrage + Nouns-style auctions carry the joke with zero custody powers |

## The finding that reframes the design

None of the ten briefs states this outright; it falls out of putting 02, 05 and
06 next to the actual numbers.

**The rent inverts the thesis it is supposed to demonstrate.**

- Asset prices rise with M2. M2 grows on the order of **5% per year**, so an asset
  appreciates ~**0.4% per month**.
  > **The 5% here is an order of magnitude, not a measurement** (noted
  > 2026-08-13). It is doing an order-of-magnitude job — the comparison below is
  > against *150% a month*, where a point either way changes nothing, and the
  > argument is unaffected. **Do not quote it as what M2 actually does.**
  > Compounded from the Fed's own series it is **6.73% since 1959**, and above
  > **5.6%** on every multi-decade window. T20 imported this line into copy on
  > the page and it had to be corrected; see `MELT_ANNUAL_BPS` in
  > `packages/enc/src/actions.ts`.
- Rent is **5% per day** — ~**150% per month**.
- An asset holder therefore nets roughly *minus 150% a month*. Holding ENC and
  buying nothing is, by a wide margin, the better trade.

That is the exact opposite of the joke. Write it as a condition:

> For "holding assets beats holding cash" to be **true on-chain**, rent must be
> strictly **less than the M2 growth rate** — i.e. under about **5% per year**.

Which is, by coincidence, exactly the rate the founding Harberger art project
used in 2019 (see 02).

**The consequence is structural, not a tuning fix.** At a rate low enough for the
joke to be true, rent is far too small to function as the turnover engine it was
introduced to be. Rent cannot do both jobs. If turnover matters, it has to come
from somewhere else — a scheduled auction (10) rather than a continuous tax.

## Where the research points

**Demurrage on the coin, auctions for the assets.**

- ENC's balance visibly shrinks. Token-2022's `InterestBearingMint` takes a
  negative rate natively, built for exactly this; the stored balance is untouched
  and nothing ever leaves a wallet (10).
- The ten assets re-auction on a clock, Nouns-style — five years live, zero
  custody drama (10).
- Removes: rent, the standing SPL delegate, the permanent delegate, foreclosure.
  Keeps: the M2 peg, the price ratchet, the whole joke.

It is also the **more accurate satire**. In the real economy nobody seizes your
wages. They quietly become worth less while you hold them. Demurrage is that,
literally. Rent on the asset is a tax on *owning*, which is the opposite of the
world we're describing, where owning is nearly free and holding cash is what
bleeds you.

## Constraints any redesign must respect

**→ Claims, not cruelty, are what get you called a rug** (08). The mechanism may
be harsh if it is disclosed and true. So the sentence to be careful with is
"assets are **guaranteed** to rise" — it silently depends on M2 continuing
upward, and M2 fell ~4.7% in 2022–23 (09). A sustained decline makes a correctly
functioning mechanism feel like a broken promise.

**→ Decide whether ENC has a market price at all** (04). Currently ducked. The
closed-loop option (no pool, no chart, spend-only) is a real and arguably safer
choice, not a failure.

**→ The NFTs carry the legal exposure, not the coin** (07). Guaranteed
appreciation plus issuer-collected rent is the shape that has drawn SEC
settlements. Removing rent helps here too.

**→ Bots will win the asset layer** (06). Fine, and arguably a better joke — but
then the copy must stop implying humans can hold one.

**→ Don't call it a Harberger tax** (02). We removed self-assessment, which is
the mechanism's whole justification.

## Corrections applied to these briefs

- **03** dated the Token-2022 permanent-delegate scam story to September 2026. It
  is September **2024** ([Binance Square, 2024-09-04](https://www.binance.com/en/square/post/2024-09-04-scammers-exploit-solana-token-extension-to-burn-users-crypto-13074543469010)).
  Verified and corrected in the file. The substance survives: the scanner flags
  are two years established and routine rather than a live news cycle.

Each brief carries its own confidence section and flags what it could not verify.
Several could not reach primary sources (SEC.gov and FRED both refused fetches),
and those cells are marked — check them before anything goes into public copy.
