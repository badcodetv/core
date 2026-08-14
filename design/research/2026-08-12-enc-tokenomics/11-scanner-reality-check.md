# Scanner reality check: what RugCheck/Solscan/Jupiter/GoPlus actually show for PermanentDelegate and mint-authority tokens

**Question:** Do public Solana risk scanners really name and flag the `PermanentDelegate` Token-2022 extension and an active mint authority, as earlier (secondary-source) research claimed? What exact wording/severity, and do they distinguish a mint-level permanent delegate from a token-account-level `approve` delegate?

All checks run live 2026-08-12 via WebFetch against public JSON APIs (no browser/JS rendering available in this environment).

## What I actually observed

**Test tokens** — both real, live, mainnet Token-2022 stablecoins that carry `PermanentDelegate` (confirmed by both RugCheck and GoPlus responses below):
- **PYUSD** (PayPal USD) — mint `2b1kV6DkPAnxd5ixfnxCpjxmKwqjjaYmCZfHsFu24GXo`
- **USDG** (Paxos Global Dollar) — mint `2u1tszSeqZ3qBWF3uNGPFc8TzMk2tdiwknnRMWGWjGWH`

**RugCheck does name the risk explicitly — confirmed on USDG.** `GET https://api.rugcheck.xyz/v1/tokens/2u1tszSeqZ3qBWF3uNGPFc8TzMk2tdiwknnRMWGWjGWH/report` returned a `risks` array including, verbatim:

```json
{ "name": "Mint Authority still enabled",
  "description": "More tokens can be minted by the owner",
  "score": 50000, "level": "danger" },
{ "name": "Permanent Control Enabled",
  "description": "The token creator can permanently control all tokens",
  "score": 50000, "level": "danger" },
{ "name": "Freeze Authority still enabled",
  "description": "Tokens can be frozen and prevented from trading",
  "score": 25000, "level": "danger" }
```
Overall `score_normalised: 81` (out of 100, higher = riskier). Mint authority and permanent delegate carry equal, maximal weight (50000 each) — the two heaviest danger flags RugCheck has. This directly answers the question: RugCheck's name for the PermanentDelegate extension is **"Permanent Control Enabled,"** severity **"danger."** Confirmed with the exact same wording on `/report/summary` too.

**But PYUSD — same extension, same authority address — got a clean bill.** `GET .../2b1kV6DkPAnxd5ixfnxCpjxmKwqjjaYmCZfHsFu24GXo/report` (and `/report/summary`) both returned `"risks": [], "score": 1, "score_normalised": 1`, despite PYUSD's own data (visible in the same response) showing an active `mintAuthority` and an active `permanentDelegate` field, both non-null. The GoPlus data for the same mint (below) confirms these authorities are genuinely live. **So RugCheck's risk engine is overridden for tokens on its own trusted/verified registry** — the extension is present, but the danger flags don't fire. This is a real finding, not a guess: it's the literal API output.

**GoPlus (`api.gopluslabs.io/api/v1/solana/token_security`) has no risk-name field at all — it's raw structured data, not a verdict.** For PYUSD I dumped the full JSON: it has `mintable.status: "1"` (authority `8Jornc27...`), `freezable.status: "1"`, and a field called **`balance_mutable_authority`** (`status: "1"`, authority `2apBGMsS...` — the same address as PYUSD's permanent delegate). GoPlus's schema has no key literally called `permanent_delegate`; `balance_mutable_authority` is almost certainly their name for it (moving a holder's balance without their signature), but GoPlus itself emits no severity label or description string — that's left entirely to whatever frontend consumes the API. The response also carries `"trusted_token": 1` for PYUSD.

**Jupiter shows verification/organic-score metadata, not a named permanent-delegate warning.** `GET https://api.jup.ag/tokens/v2/search?query=<mint>` for both tokens returned `isVerified: true`, `organicScore` ~88 ("high"), and `tags` including `"token-2022"`, `"verified"`, `"stable"`, `"community"` (PYUSD additionally tagged `"strict"`, `"moonshot-verified"`; USDG is not `"strict"`, matching RugCheck's own "Jupiter Strict: No" note for USDG). **No tag or field names PermanentDelegate or flags it as a risk anywhere in this payload.** Jupiter lets both trade freely — nothing here suggests either token is restricted or gated at the aggregator level.

**Solscan's web page is not fetchable this way.** `https://solscan.io/token/<mint>` returned a flat **HTTP 403** — it's behind bot protection / requires a browser, confirming this is a JS-heavy page, not a scriptable API. I did not find a working unauthenticated Solscan public API endpoint in the time available (their public API now requires a key); I did not fabricate what its page shows.

**Birdeye is not reachable without an API key.** `public-api.birdeye.so/defi/token_security` returned a flat **HTTP 401**. I could not observe Birdeye's UI wording at all — reporting this as unverified, not guessed.

## What I could not observe and why

- **Solscan's actual on-page wording/severity** — blocked by bot protection (403), no working keyless API found. Not verified either way.
- **Birdeye's actual UI/labels** — blocked by auth requirement (401). Not verified.
- **Jupiter/Raydium/Orca actually *restricting* (vs. merely tagging) a permanent-delegate token at the swap-execution level** — both test tokens swap freely on Jupiter today (they're liquid, verified stablecoins), so I have no case where restriction would even be visible. I found no documentation or announcement of Jupiter blocking swaps specifically for PermanentDelegate; absence of evidence, not evidence of absence — I did not test an actual swap transaction.
- **A live example of an active token-account `approve` delegate being flagged by a scanner** — this is a per-wallet, per-account state (not a mint-wide property), and I have no way to construct or find one via read-only API calls. Documentation search (Solana docs, wallet-security guides) is consistent in describing this as a *separate* mechanic surfaced by wallet-side "revoke approvals" tools (e.g., Famous Fox Federation Revoker), not by mint scanners like RugCheck/Solscan — but I did not directly observe a scanner's response to a live delegated token account, so treat the distinction as corroborated-by-documentation, not directly observed.

## What this means for ENC

The earlier secondary-source claim holds for RugCheck **as a mechanism** (it does compute and can display a "Permanent Control Enabled" danger flag, tied for the highest score weight alongside mint authority) — but the PYUSD case shows the real gate is **RugCheck's own verified-token registry, not the raw extension set**. A token can carry PermanentDelegate and an active mint authority and still show `risks: []` if RugCheck has separately trust-listed it. That's the actionable lever: getting ENC onto RugCheck's (and Jupiter's) verified list matters more than the underlying extension choice. Absent that listing, expect the same "danger" pair USDG shows — mint authority *and* permanent delegate each contributing 50000 points, pushing the normalized score into the 80s (risky-looking) even though USDG is a reputable Paxos stablecoin trading normally on Jupiter/Orca/Raydium with no execution-level restriction observed. Jupiter itself doesn't appear to gate on this at all — verification/organic-score there is a separate, coarser signal that doesn't name the extension.

## Confidence

- RugCheck exact wording/severity for permanent delegate and mint authority: **high** — directly quoted from two independent live API calls (report + report/summary) against a real token that shows the flag.
- RugCheck suppressing risks for trust-listed tokens: **high** — directly observed contrast between PYUSD (suppressed) and USDG (shown), same extension, same authority pattern.
- GoPlus having no named permanent-delegate risk string, only raw authority fields: **high** — full JSON dumped and inspected.
- Jupiter not surfacing a permanent-delegate-specific tag: **medium-high** — confirmed for two tokens' API payloads; can't rule out a differently-worded flag existing elsewhere in Jupiter's UI I didn't fetch.
- Solscan and Birdeye UI wording: **not verified** — both blocked (403/401). Do not treat any prior claim about their exact wording as confirmed by this pass.
- Token-account `approve` delegate being a distinct, wallet-side-only concern: **medium** — well-documented, but not directly observed against a live scanner response.
