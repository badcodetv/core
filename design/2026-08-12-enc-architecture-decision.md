# ENC — the architecture decision

**Status: RULED 2026-08-12 by Kai.** All three decisions below are settled and
have been written into the implementation plan (T11 superseded, T12 rewritten as
the tenancy auction, T13 annotated, T28 added).

| Ruling | Decision |
| --- | --- |
| **A — architecture** | **No holding cost at all.** No rent, no demurrage. Assets change hands by scheduled auction. |
| **B — sunset** | **Forever**, with a self-proving exception: a permissionless `retire` once the oracle has been silent long enough (T28). |
| **C — market** | **Closed loop by posture.** BadCode seeds no pool and sells no ENC. Anyone else may pool it; we neither prevent it nor point at it. |

**Follow-up ruled the same day:** the ten flags stay in program custody and the
holder receives a **tenancy certificate** NFT of their own, which is never taken
back. Putting the flag itself in the holder's wallet would require the permanent
delegate to pull it at settlement — the exact power Ruling A removed — and there
is no third option, since wallet residency and permissionless settlement are
mutually exclusive. The certificate is also the better joke: *you never really
owned the asset; all you keep is the receipt.* Net effect: **no path in the
program touches anyone's wallet without their signature.** Detail in T12.

One creative call remains open, and it is small: **what retirement does to the
auctions** — freeze as a final exhibit, or keep trading forever at the last
prices the Fed ever reported. See T28.

**Why this exists.** The research base at
[`design/research/2026-08-12-enc-tokenomics/`](./research/2026-08-12-enc-tokenomics/README.md)
found a defect in the built design that is not a tuning problem. This document
states it, sets out the two ways forward as concretely as they can be stated
before a ruling, and asks for three decisions. Everything here is reversible
until T22 burns the upgrade authority.

**The frame this is decided inside** (Kai, 2026-08-12): ENC is an **artwork in a
frame, not an ecosystem**. It succeeds if the joke exists and makes sense when
someone looks at it. It does not need players, volume, a market price or a
living economy. *It is okay if it dies and nobody cares.* Consequently: **no
mechanism may be justified by "it keeps people playing."** Legibility is the
whole job.

---

## 1. The defect

The joke: *when the Fed prints, asset prices rise and wages don't — so don't hold
the coin, hold the asset.*

The built mechanism charges asset holders **5% per day** in rent. Asset prices
rise with M2. Here is what M2 actually does, computed from the full FRED M2SL
series, 1959-01 to 2026-06, 810 observations
([`m2-backtest.mjs`](./research/2026-08-12-enc-tokenomics/m2-backtest.mjs),
re-runnable):

| Measure | Value |
| --- | --- |
| Median month-on-month M2 change | **+0.522%** |
| CAGR, trailing 20 years | **+6.28%** |
| CAGR, since 1959 | +6.73% |
| Largest single month | +6.42% (Apr 2020) |
| Largest monthly fall | −1.40% (Mar 2023) |
| Months where M2 fell | 49 of 809 (**6.1%**) |
| 2022 peak → trough | 21,787.2 → 20,737.5 = **−4.82%** ($1.05T) |

So an ENC asset appreciates at a median of **~0.52% per month**, or about
**0.017% per day**.

**Rent is set at 5% per day. That is roughly 290× the rate at which the asset
gains.** An asset holder nets about −150% per month. Holding ENC and buying
nothing beats owning the asset by an enormous margin.

That is the precise inverse of the thesis the coin exists to demonstrate. Stated
as a condition:

> For "holding assets beats holding cash" to be **true on chain**, the cost of
> holding an asset must be **strictly below the M2 growth rate** — under about
> **0.017%/day**, i.e. **~6%/year**.

**This is not a number to tune, it is a structural conflict.** Rent was
introduced to force turnover. At a rate low enough for the joke to be true, rent
is far too small to force anything. Rent cannot do both jobs. And under the
artwork framing, turnover was never a requirement in the first place — so the
job it was hired for no longer exists.

**Why this still matters when nobody is playing.** It is not an economic failure,
it is a **legibility** failure. A visitor who works out the arithmetic sees a
machine that contradicts its own caption, while looking at it. That is the one
failure mode the artwork framing does not forgive.

---

## 2. The three rulings

### Ruling A — the architecture

**Option A1: keep rent, fix the rate.** Set rent below M2 growth (~5%/year), keep
`buy_asset`, `settle_rent` and `foreclose` broadly as built.

- **Keeps:** the code already written and tested at T11.
- **Costs:** still needs the standing SPL delegate over holders' ENC (the program
  cannot debit a wallet otherwise), still needs the permanent delegate on the
  NFTs for foreclosure. Both are the primitives Solana scanners flag hardest, and
  at ~5%/year a foreclosure now takes *years* to trigger, so the mechanism exists
  in the code and essentially never fires. We would carry the maximum
  reputational cost for a mechanism that does nothing.

**Option A2: no holding cost at all; assets change hands by scheduled auction.**

*This option was revised on 2026-08-12 after verification (§5). It was originally
"demurrage replaces rent". Demurrage turns out to be cosmetic — and, more
usefully, unnecessary.*

**The insight that simplifies everything: holding ENC already loses, truthfully,
with no mechanism at all.** Your balance sits still while the assets get more
expensive. Nobody takes anything from you; your money simply buys less of what
matters. **That is precisely what happens to a wage**, and it is already
guaranteed by the peg. We were about to build a holding cost to demonstrate a
loss the design already produces for free.

- **No rent. No demurrage. No holding cost.** The purchasing-power loss is
  emergent and real.
- **The assets re-auction on a clock**, Nouns-style, aligned to the M2 sync.
  Proceeds 100% to the outgoing holder. You know from the first screen that it is
  a lease with a published end, not a wallet someone can reach into.
- **Removes entirely:** rent, the standing SPL delegate, the permanent delegate,
  foreclosure, and the "permissionless settle_rent" contradiction that blocked
  T12.
- **Costs:** deletes T11's tested code; `buy_asset` becomes an auction settlement.
- **Optional garnish, not load-bearing:** the shrinking on-screen balance stays a
  *display*, exactly as the original plan already intended ("the chain holds the
  truth, the page shows a number quietly shrinking"). Whether that display lives
  on the frontend or in a Token-2022 negative-rate mint is now a cosmetic
  implementation choice, and either way the copy must say plainly: **the number
  shrinks; the tokens do not.** Declared, it is the joke. Undeclared, it is a
  false claim, and false claims are the one thing that reliably gets a project
  called a rug.

**The argument for A2 beyond the mechanics:** it is the truer satire. In the real
economy nobody seizes your wages. They quietly become worth less while you hold
them. Rent on the asset is a tax on *owning* — which describes the opposite of
the world we are depicting, where owning is nearly free and holding cash is what
bleeds you.

**Recommendation: A2.** It is now also the *smallest* machine on the table: it
deletes code and adds almost none.

### Ruling B — the sunset

Does ENC run **forever**, or as a **bounded experiment** (Kai floated three
years)?

The running cost is not the argument — cranking the oracle is ~$0.0015 and is
permissionless, so it costs us nothing to leave alone. The arguments are:

**For bounding it:**
- **A stated duration is a frame.** "This ran from 2026 to 2029" is a complete
  object with an ending, which is what an artwork wants.
- **It repairs our most dangerous sentence.** "Assets are *guaranteed* to rise"
  silently depends on M2 rising. Over a bounded window the claim becomes
  scoreable rather than a promise that can break — and the data says it is
  nearly bulletproof: **of 774 historical three-year windows, M2 rose in 770.
  The worst three-year outcome in 67 years was −0.5%.** Median three-year
  multiple: **1.222×**.
- **It answers abandonment.** The work does not get abandoned; it **completes**.
- It bounds oracle risk: a feed that dies in year four cannot embarrass a thing
  that already ended.

**Against:** non-upgradeable means the duration is chosen once, now, forever.

**The open question if bounded: what does the ending DO?** Two candidates, and
this must be decided before T12 because it must be coded in:
- **Freeze** — syncs stop, prices stop, the final state stands as the exhibit.
- **Release** — the vault burns its holdings, the assets become plain NFTs their
  holders keep forever. *The empire ends; you keep the flag.*

### Ruling C — the market

**Closed loop** (no liquidity pool, ENC has no external price, spend-only) or
**let a market form**?

The research found no launch mechanism compatible with "the treasury never
sells", and that a thin faucet-fed market is trivially moved and reads as a rug
when it moves. The closed loop has a working precedent at enormous scale (Robux)
and removes the price chart the artwork would otherwise be judged by.

**Recommendation: closed loop.** Under the artwork framing this costs us nothing
we wanted.

---

## 3. What each ruling costs in code

| | A1 (fix the rate) | A2 (demurrage + auction) |
| --- | --- | --- |
| T7–T10 (state, math, oracle, sync) | unchanged | unchanged |
| T11 (rent, settle, foreclose) | keep, retune | **delete** |
| T12 `buy_asset` | as specced + delegate grant | becomes `settle_auction` |
| T13 faucet | unchanged | unchanged |
| Token-2022 permanent delegate | required | **dropped** |
| Standing SPL delegate | required | **dropped** |
| New work | none | interest-bearing mint, auction loop |

T11's code stays in git history on the branch either way. If it goes, the plan's
ticket notes record why — it was correct work against a spec that turned out to
contradict itself.

---

## 4. Claims the artwork may make

Whatever is ruled, these are the constraints on public copy, from the research:

- **Never say "guaranteed to rise."** Say **"it tracks M2, whatever M2 does."**
  True unconditionally, and it makes the 2022–23 burn a feature rather than an
  embarrassment.
- **Never say "the Fed prints money and hands it to Wall Street."** That conflates
  QE, bank lending and fiscal transfers; 2020–21 was transfer-heavy. Say *"when
  the money supply expands, asset owners benefit disproportionately and first."*
- **Do not call it a Harberger tax.** Self-assessment was removed, and that is the
  mechanism's entire justification.
- **Anchor the economics on:** the Bank of England's own 2012 finding that the top
  5% of households held 40% of QE's financial-asset gains; Fed DFA Q4 2024 wealth
  shares (top 1% = 33%, bottom 50% = 2.5%); Case-Shiller 100 → 332.7 since 2000.
- **Pre-empt the strongest attack in one honest line:** 2021–24 was the fastest
  money growth in modern history *and* real wages for the bottom half rose 15.3%.
  Root the joke in the long-run asset-vs-wage divergence, not a year-by-year
  causal claim.
- **The mechanism may be harsh; the claims must be exactly true.** No project has
  been called a rug over a disclosed harsh mechanism. Every real accusation
  traced to a false factual claim.

---

## 5. Verification results

**`InterestBearingMint` — verified, and it demoted itself from the plan.**
([full report](./research/2026-08-12-enc-tokenomics/12-interest-bearing-mint-verification.md))
The mechanics are exactly as claimed: negative rates are real (`i16`, −32768 to
+32767 bps, annual continuous compounding), `rate_authority` can be `None` or a
PDA, and the stored balance and mint `supply` never change. **But the decay is
purely cosmetic** — Neodyme's security review calls it "solely cosmetic"; nothing
ever realises it, and a transfer moves the full undecayed amount. **No confirmed
production token uses it in either direction**, so it is unproven in the wild.

Consequences, and they are good ones:
- It **cannot** substitute for a real holding cost. Had we shipped it as one, the
  shrinking balance would have been false the moment anyone checked an explorer —
  a false claim, which §4 forbids.
- It does not need to. **The peg already makes holding ENC lose, truthfully.**
  This is what collapsed A2 into its simpler form.
- The cosmetic decay remains available as *display*, which is what the original
  plan always intended. Declared as display, it is honest and it is the joke.

**Scanner behaviour — observed directly, not cited.**
([full report](./research/2026-08-12-enc-tokenomics/11-scanner-reality-check.md))
Checked against two real Token-2022 mainnet stablecoins that carry
`PermanentDelegate` — PayPal's **PYUSD** and **USDG** — via public JSON APIs.

- RugCheck names it explicitly. On USDG: **`"Permanent Control Enabled"`**, *"The
  token creator can permanently control all tokens"*, score **50000**, level
  **`danger`** — tied for its heaviest weighting with **`"Mint Authority still
  enabled"`**, also 50000/danger.
- **The lever is trust-listing, not the mechanism.** PYUSD carries the *identical*
  extension and a live mint authority and returns `risks: []`, score 1, because
  it sits on RugCheck's verified registry. Jupiter marks both `isVerified: true`
  with no permanent-delegate tag at all, and both trade freely.
- Could not verify: Solscan (403, bot-protected), Birdeye (401, needs a key), and
  whether any DEX ever *restricts* rather than merely tags such a token.

**What this means for us, under either ruling.** ENC keeps its mint authority
forever by design, so **`"Mint Authority still enabled"` / danger / 50000 is a
permanent, unavoidable readout on ENC** — and we will not get trust-listed. The
existing plan already ruled that this warning is a feature and must not be
suppressed. That stance is now confirmed and, better, **executable: we know the
exact string and can quote it in our own copy before anyone else does.** A coin
about money printing, flagged by the machines as a money-printing risk, in their
words.

Under **A2** the permanent-delegate flag never applies, since the extension is
dropped. Under **A1** we would take a second 50000/danger flag on top, for a
foreclosure mechanism that at a correct rent rate would essentially never fire.

Useful aside: PayPal ships `PermanentDelegate` in production, so the extension
itself is not disreputable — it is unverified projects carrying it that get
marked.

Also under verification: what a risk scanner *actually* displays for a
permanent-delegate token, observed directly rather than cited
([`11-scanner-reality-check.md`](./research/2026-08-12-enc-tokenomics/11-scanner-reality-check.md)).
If A1 is chosen, that finding decides how loudly we have to pre-empt it.

---

## 6. What happens after the rulings

1. Draft the **claim list** — every factual assertion the coin, the page and the
   copy will make — for sign-off.
2. Verify only that list, against primary sources, plus the two empirical checks
   above.
3. Build the **backtest into T14** so the claims become re-runnable
   demonstrations rather than citations, and use it to pick the T15 parameters.
4. Rewrite tickets T12 onward to match, and resume.
