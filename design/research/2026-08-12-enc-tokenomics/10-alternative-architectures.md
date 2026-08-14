# Alternative token architectures for Emperor's New Coin

**Question:** What other token architectures could make "holding cash loses, holding assets wins" true and felt, with less collateral damage than ENC's current rent + standing delegate + foreclosure machinery?

## What I found

1. **Wörgl, Austria (1932–33)** — 1%/month stamp-scrip demurrage, 1:1 backed by schillings. Notes needed a monthly stamp to stay valid, so they circulated ~9–10x faster than the national currency. Unemployment fell locally while rising nationally; six towns copied it before Austria's central bank banned complementary currencies and shut it down in 1933. Founding proof that a visibly-shrinking balance drives circulation with no seizure event. [Unterguggenberger Institut](https://unterguggenberger.org/the-free-economy-experiment-of-woergl-1932-1933/), [Lietaer PDF](https://bernard-lietaer.org/wp-content/uploads/2022/07/2010-The-Worgl-Experiment-Austria-1932-1933-Lietaer-annotated.pdf)

2. **Freicoin (2013)** — Bitcoin fork with 5%/year demurrage, redistributed to miners. Failed to gain adoption; post-mortems blame governance problems and, more relevantly, that decay "had no real function" absent an actual economy transacting in the coin. [BitcoinWiki](https://bitcoinwiki.org/wiki/freicoin), [freico.in](https://freico.in/)

3. **Chiemgauer (Bavaria, still running)** — live regional currency, 1:1 EUR-backed, demurrage via a stamp roughly every 3 months (~6–8%/year). Circulates ~3x faster than the euro; conversion fees fund local nonprofits. Decades of continuous operation, no crypto tooling needed. [Wikipedia](https://en.wikipedia.org/wiki/Chiemgauer), [finnus.co.uk](https://www.finnus.co.uk/insights/the-chiemgauer-explained-is-it-a-viable-solution)

4. **Circles UBI (Gnosis Chain, v2 shipped May 2025)** — every user mints a personal currency at 1 CRC/hour with ~7%/year demurrage, spendable via trust-network graphs, now bridged to a real Visa card via Gnosis Pay. A *live* crypto demurrage system, not a historical curiosity. [money2069.org](https://money2069.org/projects/circles), [Frontiers in Blockchain](https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2024.1362939/full)

5. **Token-2022 `InterestBearingMint` supports negative rates natively.** Rate is a signed 16-bit basis-point field, range **−32768 to +32767 bps**, and the SPL source explicitly documents negative values as for demurrage tokens. Critically: **the raw stored balance never changes** — it's the principal; the decayed figure is a *calculated* `ui_amount` from continuous compounding. Nothing leaves a wallet automatically. [token-2022 source](https://github.com/solana-program/token-2022/blob/de93095c0a32ad52d90b37d944fb17756ced4dc5/interface/src/extension/interest_bearing_mint/mod.rs), [Solana docs](https://solana.com/docs/tokens/extensions/interest-bearing-tokens)

6. **Axie Infinity's SLP/AXS collapsed via sink starvation.** SLP (uncapped "wage" token) minted continuously by every player, but its sink (breeding) scaled with a fixed asset population, not player count. When growth stalled the faucet kept running — SLP fell ~94% ($0.39→$0.01) over ~7 months in 2021–22, forcing emission cuts in Feb 2022 "to prevent collapse." [CoinDesk](https://www.coindesk.com/tech/2022/02/08/axie-infinity-reduces-slp-emissions-to-prevent-collapse)

7. **Basis (2018)**, a 3-token seigniorage-share stablecoin (coin + bond + share), raised $100M+ but shut down pre-launch in Dec 2018 and returned capital, widely attributed to securities-law risk — a token structured as a claim on future issuance reads as equity. Never launched live. [Multicoin overview](https://multicoin.capital/2018/01/17/an-overview-of-stablecoins/)

8. **Frax Price Index (FPI)** — a real, launched (Feb 2022) CPI-pegged token: holders' dollar value rose monthly with inflation, no rent/delegate involved. Ran 4+ years, formally wound down **June 2026** (two months ago) — Frax cites declining adoption against plain-yield alternatives. Lesson: an index-only "number goes up" token is a hard sell against active yield. [FIP-448](https://gov.frax.finance/t/fip-448-wind-down-the-frax-price-index-fpi-system/3861)

9. **Ampleforth (AMPL)** rebases every wallet daily to hold % ownership constant while targeting ~$1. Rarely held its peg in practice — rebases got front-run, producing pump/dump cycles. Cautionary UX note: a balance that changes on its own confuses and gets gamed even when "fair" by construction. [Bitget](https://www.bitget.com/academy/ampleforth-forth-gui)

10. **Synthetix inverse synths** (iETH, iBTC) tracked assets via a shared debt pool with hard price bounds, freezing on breach; the whole family was deprecated in the V3 migration — even a mature protocol abandoned debt-pool synthetic tracking. [Synthetix blog](https://blog.synthetix.io/debt-pool-synthesis/)

11. **Nouns DAO** has auctioned one NFT every 24 hours since Aug 17, 2021 — five years, 100% proceeds to treasury, zero rent, zero standing delegate, zero clawback. Cleanest live precedent for distributing scarce items fairly with no custody mechanism: ownership just expires into the next auction on an agreed clock. [Trust Wallet](https://trustwallet.com/blog/academy/nouns-dao-a-generative-nft-token-project)

12. **Volt Protocol**, a CPI-pegged stablecoin, raised a $2M seed in 2022, planned mainnet for that spring. Could not verify it reached meaningful live operation — flagging **unverified/likely quiet death**, a second data point that index-tracking-as-the-whole-product repeatedly gets abandoned. [Decrypt](https://decrypt.co/97365/volt-protocol-raises-2-million-inflation-resistant-stablecoin)

## Precedents

| Project | Mechanism | What happened | Lesson |
|---|---|---|---|
| Wörgl / Chiemgauer | Stamp-scrip demurrage, holder-side | Wörgl banned by central bank (1933); Chiemgauer still running decades later | Demurrage alone drives circulation, no seizure needed |
| Freicoin | On-chain demurrage, miner-redistributed | Failed to gain adoption | Decay needs a real economy behind it, not just the mechanic |
| Circles UBI | Personal-currency demurrage + trust graph | Live, v2 shipped 2025, Visa bridge | Crypto demurrage works today, at social-graph scale |
| Token-2022 InterestBearingMint | Native negative-rate extension, calculated not transferred | Ships in SPL today | Cheapest possible demurrage: no custom program needed |
| Axie SLP/AXS | Uncapped wage token vs fixed sink | 94% collapse, emissions cut 2022 | Wage-token sink must scale with the wage token, not user count |
| Basis | 3-token seigniorage shares | Shut down pre-launch, 2018, securities risk | A token that's a claim on future issuance reads as equity |
| Frax FPI | CPI-pegged index token | Wound down June 2026 after 4+ years | Pure index tracking loses to products offering real yield |
| Nouns DAO | Perpetual daily auction | 5 years continuous, zero custody drama | Best precedent for distributing scarce assets without rent |

## Candidate architectures for ENC (my proposals, not findings)

**1. Auction-replaces-force-buy — ranked #1.** Keep M2-synced supply and the oracle-driven price multiplier. Replace force-buy + rent + standing delegate + foreclosure with a Nouns-style clock: each of the ten assets re-auctions periodically (e.g., every 30 days, aligned with the M2 re-price). Holder tops up escrow to keep it, or it auctions; proceeds 100% to the outgoing holder. **Removes:** rent, delegate, permanent delegate, foreclose. **Keeps:** mint-to-M2, price ratchet. UX: you know from day one it's a lease, not a live wallet that can be touched without your action. Solana feasibility: high — escrow + timed-auction is a well-trodden pattern (Metaplex auction houses, Nouns clones).

**2. Demurrage-native ENC via Token-2022 — ranked #2.** Drop rent and the delegate entirely. Set ENC's own `InterestBearingMint` rate negative, oracle-updated alongside M2. Balances shrink in `ui_amount` terms while assets (priced in a separate unit) don't. **Removes:** rent, delegate, permanent delegate, foreclose, possibly `sync_m2` minting itself (demurrage alone can carry the message without minting new supply). **Real caveat:** the raw balance only decays in calculation — any program/DEX that skips `amount_to_ui_amount` will price ENC at face value, and interest needs a realize/sync path to actually leave a wallet. Genuine composability risk flagged by SPL developer write-ups, not just a nicety.

**3. Two-token wage/asset split — ranked #4, riskiest.** A freely-earned "Wage" token and a fixed-supply "Asset-index" token whose Wage price only rises with M2; assets distributed via burn-funded periodic auctions. **Removes:** rent, delegate, foreclose, force-buy. **Risk:** this is exactly the shape that broke Axie (uncapped faucet, non-scaling sink) and Basis (a claim-on-future-issuance token reads as a security) — needs a genuinely hard, enforced burn sink to avoid repeating either. Highest precedent-failure rate of anything surveyed.

**4. Radically simple: fixed-supply ENC + public index + open AMM — ranked #3, the floor.** No mint/burn, no rent, no delegate, no force-buy, no auction. ENC is a plain fixed-supply SPL token; the only mechanism is a public oracle feed showing "1 ENC now buys X% less of [asset basket] than last month," and assets change hands on an ordinary AMM/OTC market. **Removes everything** but the price feed. This is the Volt/FPI shape, and FPI's June 2026 wind-down is direct evidence "number goes up, nothing else happens" underwhelms — no active mechanic pulls people through the story. Zero collateral-damage risk, weakest felt experience.

**Ranking:** 1 (auction) > 2 (native demurrage) > 4 (pure index, radical floor) > 3 (two-token).

## What this means for ENC

- **The standing delegate is the single biggest satire risk** — every "feels safe" precedent (Nouns, Chiemgauer, Circles) achieves its effect without the protocol ever touching a wallet's existing balance uninvited.
- **Demurrage is the most direct, best-attested way to make "holding cash loses" literally true**, and it's a first-class Solana primitive today (Token-2022 negative-rate `InterestBearingMint`) — could replace rent+delegate+foreclose with something the SPL standard itself defines.
- **Auctions (Nouns) are the most direct way to distribute scarce items fairly** without rent, mapping "force-buy" onto a scheduled rather than surprise event.
- **Two-token designs are the riskiest category surveyed** — both real-world failures found (Axie, Basis) trace to a token structured as an unbounded claim, on emissions or on future issuance.
- **Pure index-tracking tokens (FPI, Volt) are safe but die from indifference**, not scandal — a floor/fallback, not a headline mechanism.
- **The interest-bearing composability gotcha is a real engineering cost**: any consuming code that skips `amount_to_ui_amount` misprices a demurring ENC — must be designed around from day one if candidate 2 is chosen.

## Open questions

- Felt actively (candidates 1/2, an ongoing mechanic) or a static receipt (candidate 4) enough, given this is art, not a daily-use product?
- If demurrage (2) is adopted, does it replace M2-driven mint/burn, or run alongside it?
- Who bears interest-bearing-mint composability risk — does BadCode control every trading venue, or tolerate third-party DEXs mispricing it?
- If auctions (1) replace force-buy, does a holder who can't top up simply lose the asset free at settlement — fairer or crueler than today's force-buy?

## Confidence

**High:** Wörgl and Chiemgauer facts (multiple sources, one still operating); Token-2022 negative-rate support and principal-preserving mechanics (confirmed against source, not just docs); Nouns' mechanism and duration; Axie's SLP collapse; FPI's June 2026 wind-down (primary source).

**Medium:** Freicoin's exact failure causes (forum-level sourcing); Circles UBI's precise rate and usage scale (mixed sourcing, no audit).

**Low/unverified:** Whether Volt Protocol reached live operation. Basis never launched, so its "outcome" is a shutdown decision, not an operational failure.
