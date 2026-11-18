---
name: enc-tokenomics-research
description: 10 cited tokenomics briefs for ENC (2026-08-12) in design/research/; the rent-inverts-the-thesis finding and where the research points
metadata: 
  node_type: memory
  type: project
  originSessionId: 11d2f141-7886-4a3c-81f2-9ebdea6adf7f
  modified: 2026-08-12T09:50:44.938Z
---

**2026-08-12: ten parallel research briefs on ENC token economics**, written to
`design/research/2026-08-12-enc-tokenomics/` with a README index that carries the
synthesis. Commissioned by Kai before building further on `feat/enc-program`.
Uncommitted at time of writing.

**The finding none of the briefs stated, which falls out of combining them:**
**the rent inverts the thesis.** Asset prices rise with M2 (~5%/yr, ~0.4%/month);
rent is 5%/day (~150%/month). So owning the asset is a catastrophic loss and
holding ENC is the better trade — the exact opposite of the joke. For "assets
beat cash" to be *true on chain*, **rent must be below the M2 growth rate**,
under ~5%/year. At that rate rent cannot also serve as a turnover engine, so the
two jobs it was given are incompatible. This survives the
[[enc-artwork-not-ecosystem]] ruling and gets *more* important under it: a
mechanism that doesn't compute on inspection is a legibility failure.

**Where it lands (revised same day after verification):** **no holding cost at
all** — no rent, no demurrage — plus Nouns-style periodic auctions for the
assets. **Holding ENC already loses truthfully from the peg alone:** the balance
sits still while asset prices rise, so the money buys less of what matters, which
is exactly what happens to a wage. A holding cost was about to be built to
demonstrate a loss the design already produces for free. Removes rent, the
standing SPL delegate, the permanent delegate and foreclosure; deletes code and
adds almost none.

**Do not reach for Token-2022 `InterestBearingMint` as the holding cost.**
Verified: negative rates are real (i16 bps, annual continuous compounding,
`rate_authority` can be None or a PDA) but the decay is **purely cosmetic**
(Neodyme's review says so), nothing realises it, transfers move the full
undecayed amount, and **no production token uses it**. Shipping it as a real cost
would have made the shrinking balance false on any explorer. It survives only as
*declared display* — "the number shrinks, the tokens don't."

**Constraints that survive regardless of architecture:**
- **Claims, not cruelty, get you called a rug.** No project was ever accused over
  a *disclosed* harsh mechanism; every real accusation traced to a false factual
  claim. So "assets are **guaranteed** to rise" is the dangerous sentence — it
  depends on M2 rising, and M2 fell ~4.7% in 2022–23.
- **The NFTs carry the legal exposure, not the coin.** Guaranteed appreciation +
  issuer-collected rent is the shape that drew SEC settlements (Stoner Cats,
  Impact Theory). UK financial-promotion rules already apply to promoting ENC to
  a UK audience.
- **Don't call it a Harberger tax** — self-assessment was removed, and that is
  the mechanism's whole justification.
- **2021–24 is the empirical embarrassment**: fastest M2 growth in modern history
  *and* bottom-half real wages rose 15.3%. Root public copy in the long-run
  divergence and the BoE's own 2012 admission (top 5% took 40% of QE's asset
  gains), never a year-by-year causal claim.

**Quality caveat:** Sonnet agents, ~5 minutes each. Several figures flagged
unverified; SEC.gov and FRED refused fetches; **one brief was two years wrong on
its key source date** (the Token-2022 permanent-delegate scam story is Sept
**2024**, not 2026) — caught and corrected in the file. Good enough to decide the
architecture on, not good enough to quote from.

**Prior art:** no cryptocurrency with supply contractually pegged to M2 appears
to exist — everything found is Bitcoin-vs-M2 *correlation* commentary. One search
only, so a weak signal, but the idea looks unclaimed.
