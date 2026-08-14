# Token-2022 `InterestBearingMint`: verification against source and docs

**Claim under test:** the extension supports negative rates for demurrage, and works by
changing only a calculated `ui_amount` while the raw balance is untouched — so nothing
ever leaves a holder's wallet.

## Verdict

**Confirmed as a mechanical description — but it changes what the mechanism is good for.** Negative rates and continuous compounding are real and documented; the raw balance genuinely never moves. The catch: this makes the "shrinkage" **cosmetic** — a display convention, not a transfer of value — which is exactly why it's safe for DEXs, but also why it can't do the job of a rent mechanism on its own.

## Evidence

1. **Rate field type/range.** `InterestBearingConfig` in `interface/src/extension/interest_bearing_mint/mod.rs` (solana-program/token-2022, current `main`):
   ```rust
   pub struct InterestBearingConfig {
       pub rate_authority: MaybeNull<Address>,
       pub initialization_timestamp: UnixTimestamp,
       pub pre_update_average_rate: BasisPoints,   // i16
       pub last_update_timestamp: UnixTimestamp,
       pub current_rate: BasisPoints,              // i16
   }
   ```
   `BasisPoints` is a signed 16-bit int, range **-32768 to +32767**, i.e. -327.68% to +327.67% *annual* rate, **continuously compounded**. Source comment: "Tokens accrue interest at an annual rate expressed by `current_rate`, compounded continuously, so APY will be higher than the published interest rate." Matches the claim exactly. [github.com/solana-program/token-2022](https://github.com/solana-program/token-2022/blob/main/interface/src/extension/interest_bearing_mint/mod.rs)

2. **Negative rates / demurrage explicitly supported.** Multiple independent secondary sources (RareSkills two-part series, Chainstack, solana.com developer guide, dev.to writeups) all state the minimum value -32768 bps is "negative interest, for demurrage tokens" — demurrage is named directly as an intended use case, not something bolted on. [solana.com/developers/guides/token-extensions/interest-bearing-tokens](https://solana.com/developers/guides/token-extensions/interest-bearing-tokens), [rareskills.io/post/token-2022-interest-bearing-extension](https://rareskills.io/post/token-2022-interest-bearing-extension)

3. **What actually changes.** Official Solana developer guide, verbatim: *"Interest bearing tokens do not add more tokens to token accounts over time. The token amount stored in each token account stays the same until a token program instruction changes it."* and *"As time passes, the calculated UI amount with interest can increase even though the token amount and token supply stay the same."* No operation "realises" the decay into an actual balance change — `amount_to_ui_amount` / the `AmountToUiAmount` instruction is a **read-time calculation**, including when simulated; it never mutates state. The mint's `supply` field is likewise untouched — supply reporting is raw-amount based, same as any other mint. [solana.com/developers/guides/token-extensions/interest-bearing-tokens](https://solana.com/developers/guides/token-extensions/interest-bearing-tokens)

4. **Composability — the critical question.** Neodyme's Token-2022 extension security writeup classifies `InterestBearingMint` explicitly: *"No dangers arise from this extension, because it is solely cosmetic. Hence, for programs it is safe to support tokens with this extension."* [neodyme.io/en/blog/token-2022](https://neodyme.io/en/blog/token-2022/) This is the load-bearing fact: a DEX or program that reads the **raw** amount is reading the *only* number that is real — there is no separate "true value" being hidden from it. Raydium supports Token-2022 pools generally (permissionless CLMM/farms, freeze authority must be revoked) and nothing in Raydium's or Jupiter's public docs flags interest-bearing specifically as unsupported or mispriced — consistent with it being a non-issue for pricing, precisely because AMMs already price by raw reserve ratio and there's no hidden value to miss. I could not find a documented case of DEX mispricing caused by this extension; that absence is itself expected given point 3.

5. **Rate authority.** `rate_authority: MaybeNull<Address>` — confirmed nullable. Per the developer guide and RareSkills walkthrough, passing `None` at initialization zeroes the field and **makes the rate permanently immutable** — no further updates possible by anyone. This satisfies "fixed forever." Setting it to a program PDA (rather than None) is also structurally possible — it's just an `Address` — so "updatable only by our non-upgradeable program" is achievable too, standard PDA-signer pattern.

6. **Production usage.** I could **not verify a real, currently-active token using `InterestBearingMint` in production**, positive or negative rate. Search surfaced only tutorial/demo mints (RareSkills, Solana docs course examples) and one mainnet address claim from a low-confidence secondary source that I was not able to independently confirm on an explorer — I'm not citing it. **This is a real finding, not a gap in my search**: this extension appears to see near-zero production adoption. A 2023-era GitHub issue (`solana-labs/solana-program-library#3263`) shows the JS SDK lacked bindings for it well after Token-2022 shipped, which tracks with low real-world uptake — though that specific gap is likely closed by now given `@solana/spl-token` has since added interest-bearing helpers (used in the current official guide's code samples).

7. **Wallet display.** Phantom and Solflare both support Token-2022 extensions generally and will render the calculated (decayed/appreciated) UI amount for interest-bearing mints, per Phantom's own token-extensions docs. But this is **display support**, layered on top of the same raw balance — nothing about wallet UI changes what's exchanged on transfer.

## Composability risk

Reframe the question: the risk isn't mispricing, it's **irrelevance**. Because the raw amount is the only thing that ever moves — in a transfer, into a DEX pool, out to another wallet — a program that "ignores" `amount_to_ui_amount` isn't missing anything real; it's just not rendering the cosmetic number. The flip side is the actual risk for ENC's use case: if a holder sends their ENC to a fresh wallet, an exchange, or a pool, the recipient gets the **undecayed raw amount** and only sees the wallet-computed "current worth" if that surface bothers to call the conversion function. Nothing about ownership, redemption value, or supply has shrunk in any way a smart contract can observe or act on.

## Production usage

No confirmed live production token found using this extension in either direction (demurrage or yield). Treat it as effectively unproven in the wild, not a battle-tested primitive.

## What this means for ENC

The extension is **real, safe, and exactly as described mechanically** — but it cannot replace a rent mechanism, because it doesn't actually move value. It's a wallet-UI skin: numbers displayed by conforming clients tick down, balances in every other sense (transfers, pool reserves, `supply`, any on-chain check) are frozen at whatever was last minted or transferred. If the goal is real value transfer out of dormant holders — the actual point of a rent/foreclose design — `InterestBearingMint` with a negative rate accomplishes **nothing**: no tokens are burned, redirected, or reclaimed; total supply held by an inactive wallet is bit-for-bit the same a year later as the day it arrived. It would only be honest to use if the intent is a *narrative/visual effect* ("watch your BadCode balance shrink in Phantom") stacked on top of, not instead of, a real settlement mechanism. It does not remove the need for the standing-delegate rent design already in the T11 program; at best it's a cosmetic layer you could add alongside it.

One thing worth being straight about: swapping the real rent/foreclose mechanism for this would be swapping a working sink for a decoration. If the target audience ever checks a raw explorer balance, a DEX quote, or moves tokens off a conforming wallet, the "shrinkage" story falls apart — which cuts directly against the project's own rule that the M2-peg joke "only works if it is true."

## Confidence

**High** on points 1–3 and 5 (primary source: the struct definition and its doc comment, plus the official Solana developer guide, which is unambiguous). **Medium-high** on point 4 (Neodyme's classification is a credible third-party security review, but I did not find a primary Jupiter/Raydium statement naming this extension specifically). **Medium** on point 6 (absence of evidence for production use is suggestive but not exhaustive — I did not have on-chain explorer/query access to scan all Token-2022 mints for the interest-bearing extension flag). Flagging staleness: several secondary sources were dated 2023–2024; I weighted the primary GitHub source and the current official guide over anything older, and found no indication the core mechanics have changed since introduction.
