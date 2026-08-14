# Elastic supply, rebasing, and where new supply goes

**Question:** What happened to algorithmic elastic-supply tokens (Ampleforth, OlympusDAO, Terra/LUNA, Frax, RAI, the Basis lineage, Lido stETH, Solana attempts), and what does that imply for ENC minting new supply to a treasury instead of distributing it to holders?

## What I found

1. **Ampleforth (AMPL) rebases proportionally and non-dilutively.** A daily 2AM UTC rebase updates one global scalar applied to every wallet — if you owned X% of supply before, you own X% after. No treasury capture, no relative dilution. Target is the CPI-adjusted 2019 dollar; changes fire only outside a 5% deadband, sigmoid-capped at ±10%/day. [Ampleforth docs](https://docs.ampleforth.org/learn/about-the-ampleforth-protocol)

2. **AMPL never reliably held its price target.** The protocol can move supply, not demand/sentiment; once the market doubts the peg, contraction/expansion doesn't restore it. AMPL has spent long stretches materially off $1 in both directions. [Finematics](https://finematics.com/ampleforth-explained/), [CMC AMPL analysis](https://coinmarketcap.com/cmc-ai/ampleforth/price-analysis/)

3. **OlympusDAO (OHM) did not rebase proportionally — it minted mostly to stakers.** sOHM balances grew every 8h from new mint; non-stakers and pOHM holders were diluted in percentage terms. Advertised APYs ran into the thousands of percent; the DAO later walked staking rate toward 0%, and a leader's ~$11M dump triggered a cascade across "rebase DAO" forks. [Postmortem](https://medium.com/@juicyarbol/olympus-has-fallen-a-postmortem-on-the-3-3-experiment-87c316791612), [Messari](https://messari.io/report/governor-note-olympus-says-goodbye-to-staking-apy), [Protos](https://protos.com/rebase-daos-olympus-ohm-leader-dump-cascade-crypto/)

4. **Terra/LUNA had no treasury backstop, and its mint-burn arb died in a textbook death spiral.** Burn $1 LUNA to mint 1 UST and vice versa. When UST depegged (May 7–10, 2022), the protocol minted LUNA exponentially to absorb excess UST, crashing LUNA's price, forcing more minting. LUNA went to near-zero in days; UST fell to ~$0.23 by May 11. [Forbes](https://www.forbes.com/sites/rahulrai/2022/05/17/the-death-spiral-how-terras-algorithmic-stablecoin-came-crashing-down/), [ecos.am](https://ecos.am/en/blog/terra-luna-crash-complete-breakdown-of-the-luna-and-ust-algorithmic-stablecoin-implosion)

5. **RAI (Reflexer) deliberately avoided both a peg and holder dilution** — a fully ETH-collateralized "reflex bond" with a floating redemption price, no treasury seigniorage capture. Widely praised as the honest design in this category. It still didn't reach lasting adoption: Reflexer Labs wound down active development (contracts remain live, unmaintained). Exact wind-down date **unverified**, but the quiet-obsolescence outcome is corroborated across sources. [Reflexer FAQ](https://reflexer.finance/faq/), [Dankrad Feist, 2023-01-31](https://dankradfeist.de/ethereum/2023/01/31/rai-crypto-experiment.html)

6. **Frax started fractional-algorithmic and retreated to full collateral under pressure.** Launched Dec 2020 at 100% USDC-backed; by 2022 collateral ratio drifted to ~82%, the gap backed only by mintable FXS. In 2023, governance (FXIP-188) voted back to 100% collateralization. Even a sophisticated, audited team backed away from partial-algorithmic backing at scale. [Messari](https://messari.io/report/frax-a-fractional-algorithmic-stablecoin), [Bankless](https://www.bankless.com/the-bankless-guide-to-the-frax-stablecoin)

7. **The seigniorage-shares lineage (Basis → Empty Set Dollar → Basis Cash) is a graveyard.** Basis (Basecoin), best-funded of the group ($133M, a16z/Bain/GV), pre-emptively shut down in Dec 2018 and returned funds, self-concluding its bond/share tokens would need securities-style KYC restrictions — no SEC order, a self-shutdown. [CoinDesk](https://www.coindesk.com/markets/2018/12/13/basis-stablecoin-confirms-shutdown-blaming-regulatory-constraints) Heir Basis Cash fell from $1 to ~$0.30 across January 2021 off a ~$30.74M peak market cap. [Fast Company](https://www.fastcompany.com/90751716/panics-and-death-spirals-a-history-of-failed-stablecoins)

8. **Lido stETH is the clean, benign proportional-rebase example running at real scale.** A daily ~12:00 UTC rebase grows every holder's balance pro-rata to reflect real ETH staking rewards, no separate reward transaction: 90% to stakers, 5% node operators, 5% DAO treasury (a small cut, not full capture). Works because the underlying yield is real and the story is simple. [Lido blog](https://blog.lido.fi/steth-the-mechanics-of-steth/), [Lido docs](https://lido.fi/how-lido-works/rewards-and-penalties)

9. **Solana-native elastic-supply attempts exist but are obscure and unverified** — e.g. $REBASE, targeting a CPI-adjusted price. Found only via secondary listicles and the project's own site; no independent data on adoption or outcome. **Low confidence, essentially untested.** [rebasesol.com](https://rebasesol.com/)

10. **Rebase mechanics reliably confuse ordinary users and break tooling, regardless of design honesty.** Balances changing with no accompanying transaction breaks wallet UIs, cost-basis tracking, and tax logic — in the US, every rebase is a live open question about taxable-event status even with zero sale and zero dollar-value change. This happens even to AMPL's clean, non-dilutive design — it's a symptom of *any* balance-without-transaction mechanic, not of bad mechanism design. [OnChain Accounting](https://onchainaccounting.com/articles/how-are-rebase-tokens-like-ampleforth-taxed), [CoinTracker](https://support.cointracker.com/hc/en-us/articles/25712623483409-Understand-rebase-tokens)

## Precedents

| Project | Mechanism | What happened | Lesson |
| --- | --- | --- | --- |
| Ampleforth (AMPL) | Proportional rebase, no capture | Never reliably held target; still trades, niche | Clean design ≠ price stability |
| OlympusDAO (OHM) | Mint-to-stakers, RFV narrative | Unsustainable APY, non-staker dilution, dump, cascade collapse | Routing new supply to a subset is a wealth transfer dressed as yield |
| Terra/LUNA | Uncollateralized mint-burn peg arb | Death spiral, ~$60B wipeout, May 2022 | No backing + reflexive minting = worst case |
| RAI (Reflexer) | Floating, collateralized, no dilution/peg | Technically sound, never scaled, team wound down | Soundness doesn't guarantee adoption |
| Frax | Fractional-algorithmic → full collateral | Market/governance forced retreat | Even strong teams retreat from partial-algo backing under stress |
| Basis / Basis Cash / ESD | Seigniorage shares (bond/share absorb changes) | Basis self-shut down (2018, securities risk); Basis Cash collapsed ~70% in a month (2021) | Multi-token seigniorage risks securities law AND death spirals |
| Lido stETH | Proportional rebase, real yield, small treasury cut | Works at massive scale, trusted | Rebase reads cleanly only when paying out something real and simple |

## What this means for ENC

**→ ENC's mint-to-treasury has no real precedent in this category — it's closer to central-bank seigniorage than to any DeFi rebase design.** AMPL/stETH keep everyone's *percentage* ownership constant; OHM/Terra route new supply to *participants*. ENC routes 100% to itself, diluting every non-vault holder's percentage ownership every month, by design. That's a genuinely novel choice worth naming internally, not something borrowed from a working precedent.

**→ The joke depends on "your balance never moves" reading as elegant, not sinister — the evidence cuts both ways.** Even AMPL's honest, visibly-changing balance confuses users. A design where the balance never moves but your %-of-supply silently shrinks is more legible in one sense (nothing visibly happens to you) and more suspicious in another (no on-chain signal is exactly the pattern people call "stealth mint" or "hidden inflation"). Don't assume this resolves in ENC's favor by default.

**→ Every survivor here kept the treasury/algorithm role separate from any actor who could plausibly be blamed for taking your money.** RAI and Lido avoid a capturable delta; OHM and Basis both had one and both drew "who's getting rich" scrutiny. ENC's non-upgradeable, keyless-oracle, no-admin design is the strongest defense against this exact failure mode and should lead any public explanation.

**→ "Supply that only goes up, held by a treasury nobody controls" is close to what killed trust in OHM's RFV narrative — the metric people watched was "how fast is the treasury growing relative to me."** Even with no admin key, a permissionless mint that always flows to one address invites "so who benefits." ENC needs a crisp, unavoidable answer before launch — the OHM/Terra failures weren't really about bad mechanisms, they were about mechanisms getting interrogated and the answer not holding up.

**→ Nothing here shows elastic supply successfully teaching a lay audience an economic idea on its own.** AMPL is the purest pedagogical attempt and it hasn't become a widely understood reference point outside DeFi natives — mostly it generates "why did my balance change" support tickets. If the goal is the joke landing with non-crypto people, the UI/copy layer has to carry nearly all the explanatory weight; the mechanism can't be relied on to speak for itself.

**→ ENC genuinely dodges the rebase-specific UX tax.** Holder balances are static (mint goes to treasury, not pro-rata), so ENC avoids AMPL/Lido's "why did my balance change" support burden and the associated tax/cost-basis mess. Worth stating as a real advantage, not just implying it.

**→ The 2018 Basis precedent is a securities-law flag more than a mechanism flag.** A structure that looks like it routes seigniorage to a privileged class (bond tokens, share tokens, insiders) invited a pre-emptive shutdown even absent enforcement. ENC's "everything flows to the vault, no one personally profits from the mint" shape is right — but only holds if the vault is verifiably undrainable to insiders, a claim that needs to survive the same scrutiny Basis's bond holders got.

## Open questions

- Is there a public-facing explanation for "why does the vault keep new supply instead of holders" that survives a skeptical first read? OHM/RFV precedent says this question will be asked.
- What does the vault actually do with accumulated ENC over time (fund the assets/faucet mechanics, sit idle)? Precedent shows treasury *purpose* is where trust is won or lost.
- Given RAI's fate (technically clean, quietly died), is "reads correctly to a crypto-critical audience" enough, or does the satire need mainstream legibility to work?

## Confidence

**High:** AMPL's rebase mechanics, OHM's staker-dilution structure and 2022 unraveling, Terra/LUNA's death-spiral sequence, stETH's daily proportional rebase, Basis's 2018 shutdown and Basis Cash's 2021 collapse, Frax's collateral-ratio history — all corroborated by protocol docs, Messari, or contemporaneous reporting.

**Medium:** RAI's exact wind-down date (outcome is corroborated, date isn't); framing ENC's design as precedent-less is my analysis, following directly from the sourced mechanics above, not itself a sourced claim.

**Low / flagged unverified:** the Solana-native $REBASE project's real adoption or track record — only the project's own site and generic listicles found, no independent verification possible.
