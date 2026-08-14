# MEV, Front-Running, and Bot Dominance

**Question:** Given that ENC's price path is fully public and deterministic (published Fed calendar, permissionless sync, linear 30-day interpolation) and force-buy/foreclosure have no cooldowns, what will automated actors do to this market, and does it complete or ruin the joke?

## What I found

1. **Solana has no public mempool by design** — transactions go straight to the next leader on a known schedule, so "front-running" here means winning the *block-builder auction*, not sniping a mempool. (Helius, "Solana MEV: An Introduction," https://www.helius.dev/blog/solana-mev-an-introduction)

2. **Jito is the de facto ordering layer and dominates validator share.** Mid-2026 reporting puts the Jito-Solana client on roughly 78–95%+ of active stake (sources disagree on the exact figure), Jito tips over 60% of priority-fee volume, MEV-routed bundles 24%+ of validator non-base-fee revenue, and $480M+ cumulative searcher profit through Q2 2026. These are industry-blog figures, not audited data — treat as directional. (Chainstack, "Jito Explained: Bundles, Tips, and How MEV Works on Solana in 2026," https://chainstack.com/jito-explained-bundles-tips-mev-solana/)

3. **Jito deliberately shut down its public mempool in March 2024** because sandwich attacks were hurting ordinary users, forfeiting fee revenue to do it. Bundles (atomic groups routed straight to the leader) remain the main MEV surface today. This is a precedent of a Solana infra operator actively blunting bot extraction at a cost — ENC has no equivalent lever, being non-upgradeable with no admin. (CoinDesk, "Solana Client Developer Jito Ends 'Mempool' Function," Mar 8 2024, https://www.coindesk.com/business/2024/03/08/solana-client-developer-jito-announces-end-of-mempool-function)

4. **The Fed's H.6 (M2) release is on a fixed, years-ahead-published schedule: 4th Tuesday, ~1:00 p.m. ET.** Every future `sync_m2` opportunity is knowable to the minute, before it happens — strictly more predictable than Ampleforth's daily rebase. (Federal Reserve, "Money Stock Measures - H.6," https://www.federalreserve.gov/releases/h6/default.htm)

5. **Ampleforth's rebase is the closest real precedent for a scheduled, public, price-triggered supply change, and traders openly arbitrage it.** Rebase runs daily around 1pm EST, closing only 1/30th of the gap to target price per day — the same structure as ENC's 30-day linear interpolation. Sources describe systematic pre/post-rebase positioning as a known, persistent strategy, not a one-off exploit. (Amber Group, "Ampleforth (AMPL) — Trading Opportunities," https://medium.com/amber-group/trading-ampls-6841ecc09ccd)

6. **Oracle-triggered value ("Oracle Extractable Value," OEV) is a named, actively engineered-around problem.** Chainlink built "Smart Value Recapture" so protocols capture (rather than lose to searchers) the value released the instant an oracle updates; lending protocols on Ethereum alone have historically paid liquidators/searchers $180M+ in incentives. `sync_m2` is structurally an OEV event: the asset repricing is released atomically and is free to whoever lands the next transaction. (Chainlink, "Oracle Extractable Value (OEV) Explained," https://chain.link/article/oracle-extractable-value)

7. **Permissionless liquidation is bot-dominated in practice.** Aave liquidators earned ~7.5% average profit per liquidation in Q2 2024, and one academic dataset shows ~28% of liquidations routed through private Flashbots bundles specifically to beat rival bots — bots front-run other bots. Solend on Solana pays a 5–20% liquidation bonus; in January 2022 its liquidation bots flooded the network with duplicate transactions during a crash, degrading service for everyone — a direct precedent for ENC's foreclosure bounty. ("Demystifying DeFi MEV Activities in Flashbots Bundle," ACM CCS 2023, https://dl.acm.org/doi/10.1145/3576915.3616590; Fortune, "Solana DeFi platform votes to control whale account," https://fortune.com/2022/06/19/solana-defi-platform-votes-to-control-whale-account-via-emergency-powers-in-bid-to-avoid-liquidation-chaos)

8. **Cost-of-carry is the right frame for "buy an asset, hold through a guaranteed rise, pay rent."** The standard no-arbitrage forward price is F = S·e^{(r−y)(T−t)} — spot grown by (rate minus convenience yield) net of carrying costs. ENC's asset-plus-rent structure is a synthetic long futures position with a published forward curve (the 30-day path) and an explicit carrying cost (~5%/day rent) instead of an interest cost. Because the path is publicly computable, this is close to textbook cash-and-carry, not a speculative bet — exactly what the design brief means by "the joke." (Wikipedia, "Convenience yield," https://en.wikipedia.org/wiki/Convenience_yield)

9. **Bot takeover of a scarce game/NFT economy is a documented failure mode.** Ni No Kuni Cross Worlds' NFT layer was reported "totally ruined by bots," automated minting draining value and driving away human players; surveys report 71–74% of gamers say bots reduce enjoyment of multiplayer systems. Common thread across all precedents: when the payoff is fully mechanical and computable, human participation collapses and only automation remains. (Sportskeeda, "Ni No Kuni Cross Worlds gets infested with bots/NFTs," https://www.sportskeeda.com/esports/news-as-ni-no-kuni-cross-worlds-gets-infested-bots-nfts-netmarble-s-solution-make-players-spend-real-life-money)

## Precedents

| Project/case | Mechanism | What happened | Lesson |
| --- | --- | --- | --- |
| Ampleforth (AMPL) | Daily rebase, 1/30-of-gap linear adjustment, public time | Traders systematically position pre/post-rebase; known, persistent strategy | A public, scheduled, formulaic supply change gets traded mechanically, every cycle |
| Jito / Solana MEV | Off-chain bundle auctions, no public mempool since Mar 2024 | Sandwich attacks persisted until Jito voluntarily killed its mempool, forfeiting fees | Even the operator with the most leverage needed an active, costly fix — passive design doesn't self-correct |
| Aave / Flashbots liquidations | Permissionless bonus (~7.5% avg profit) | ~28% of liquidations routed through private bundles to beat rival bots | Liquidation races are bot-vs-bot, not bot-vs-human; humans priced out almost instantly |
| Solend (Solana, Jan 2022) | Permissionless liquidation, 5–20% bonus | Bot flooding during a crash degraded the whole network | An uncapped, no-cooldown bounty race can harm the platform beyond the market itself |
| Ni No Kuni Cross Worlds | NFT layer on a game economy | Bots farmed the reward loop; "totally ruined," players left | A frictionless, fully computable reward loop converts a human system into a bot-only one |

## What this means for ENC

**→ The ten-asset market will likely be bot-owned within days of real liquidity, not weeks.** Every input a searcher needs — sync trigger, multiplier, 30-day price path, force-buy price, foreclosure bounty — is public and computable in advance. This is an easier automation target than Ampleforth or Aave liquidations, both already bot-dominated.

**→ Force-buy with zero cooldown makes ownership a pure latency race with no defensive value.** A bot can force-buy an asset back the instant it's profitable, faster than any human can react. There's currently no reason for a human to hold an asset once bots are watching the chain.

**→ The rent-and-appreciation structure is a legible cash-and-carry trade — good for the satire, bad for engagement.** It maps cleanly onto textbook futures pricing (finding 8), so a bot prices it exactly and acts mechanically: no edge for cleverness, only for speed. Thematically perfect (machines capture the printed money), but it leaves no game for a person to play.

**→ Foreclosure bounties are a known bot-flooding vector, and ENC has no rate limit against it.** The Solend Jan-2022 precedent shows an uncapped bounty inviting duplicate-transaction flooding — worth stress-testing before mainnet, regardless of whether bot dominance is intended.

**→ This completes rather than ruins the satire, but only if the project drops the pretense that humans compete for the assets.** ENC prints tokens machines immediately convert into guaranteed appreciation; humans who "hold ENC to buy the assets" (the brief's own stated thesis) are structurally too slow to ever hold one. If the assets are spectacle/lore objects, bot capture is airtight. If a human fan is meant to realistically win or hold one, the current design guarantees they can't.

**→ Cutting bot dominance without an admin key means changing the auction, not adding a gatekeeper.** Untrusted-by-design options: a minimum hold time before an asset can be force-bought (kills the pure-latency edge, no approval needed); a randomized or commit-reveal delay on `sync_m2` execution (breaks exact-slot predictability); a Dutch-auction-style force-buy price starting above list and decaying (gives a human an economic reaction window).

**→ No one has published data on Solana force-buy/Harberger markets specifically.** The closest analogues (Ampleforth, Aave/Solend) are strong directional evidence, not a direct precedent for this exact mechanic combination — "days not weeks" is an inference, not an observed fact about ENC.

## Open questions

- Is human participation in the ten-asset market a real design goal, or is total bot/machine capture the point (an art statement, not a product)? Decides whether findings 2–4 are bugs or the thesis.
- Should `sync_m2` or force-buy get friction (minimum hold, decay window, randomized delay) without reintroducing anything that smells like an admin key?
- Is the foreclosure bounty capped, or rate-limited per account, to blunt the Solend-style flooding risk?
- Should the lore/docs explicitly state the assets are *expected* to be bot-held — turning findings 4/9 into a stated feature rather than a discovered flaw?

## Confidence

**High confidence:** Solana has no public mempool and Jito's bundle auction is the real ordering layer; Jito shut its mempool in March 2024 over sandwich attacks; the Fed's H.6/M2 release is fixed at 4th-Tuesday ~1pm ET; Ampleforth's rebase produces systematic trader positioning; permissionless liquidation is competitive and largely automated on Aave and Solend, including the 2022 Solend flooding incident; the cost-of-carry framing is standard finance.

**Lower confidence / directional:** exact 2026 percentages for Jito's stake/tip share and searcher profit (industry blogs, not audited, and they disagree with each other); "bot-owned within days" for ENC specifically (inference from comparables, not a measurement — ENC hasn't launched); the Ni No Kuni Cross Worlds narrative (single gaming-press article, not a formal post-mortem).
