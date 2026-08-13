# Solana Toolchain & Emperor's New Coin — Design & Implementation Plan

> **EXECUTION RULES (for agents):** Work ONE ticket at a time, in order unless
> dependencies say otherwise. Only the orchestrator changes ticket Status;
> workers may only append to Notes and the Discovered Issues Log. A ticket's
> checkbox is checked only after its Validation commands have been re-run by
> the orchestrator and pass. Do not expand scope; log surprises in the
> Discovered Issues Log instead.

Status: in progress — **26 of 31 done** (T31, T19, T20 and T21 landed 2026-08-13). The autonomous track is complete; everything left needs devnet, keys, or a human decision. T11 SUPERSEDED by the 2026-08-12
architecture ruling and its code deleted by T30. The tenancy auction (T12), the
faucet (T13), `retire` (T28) and the proportional caps (T29) are built and
green; the simulation (T14) runs the full M2 record plus a forward projection,
and the genesis parameters (T15) are chosen from its output and recorded in
[`chain/sim/RESULTS.md`](../chain/sim/RESULTS.md). **The Rust program is now
code-complete** — T31's Gazette landed on 2026-08-13 and every suite is green
under the `mock` feature (39 Rust unit tests; init 12, sync 14, auction 12,
faucet 10, gazette 16, retire 7). The remaining track is the oracle (T16–T18),
the page (T19–T20) and shipping (T21–T23).

> **⚠ Corrected 2026-08-13 (ticket audit) — "feature-complete" was overstated.**
> `oracle::read_quote`'s non-mock body is a stub that unconditionally returns
> `OracleUnavailable`, and the crate has **no Switchboard dependency at all**.
> So **a default build cannot sync, ever** — every green test to date runs under
> the `mock` feature, which is legitimate and by design, but it means **T18 is
> not an integration polish step: it is the difference between a deployed
> program that works and one whose core instruction always fails.** Deploying to
> devnet before T18 would put up a coin that cannot track M2. `Config.expected_
> feed_id` is likewise written at genesis and validated by nothing until T18.

**Three things want a human before T22.** (1) Jack's Gazette slot sheet.
**Corrected 2026-08-13: this does not block T31.** Slot personalities are
genesis naming and frontend presentation over one mechanism that serves all ten
(Ruling D), and `params.genesis.json` already fixes the price ladder — so T31
builds now with placeholder names and the sheet is due at **T22**, where
`init_asset` makes the names permanent. (2) Ratification of one creative call
made on the documented recommendation: retirement keeps the auctions trading
rather than freezing them (T28's Notes). (3) A read of the peg-horizon finding —
the coin can only count to $18,446.7 trillion of M2, about 107 years out, and
T15 ruled *state it, don't postpone it* (T15's Notes and the Discovered Issues
Log).
Date: 2026-08-06 · **architecture revised 2026-08-12 · adversarial review folded in 2026-08-12**

> **Read [`2026-08-12-enc-architecture-decision.md`](./2026-08-12-enc-architecture-decision.md)
> before touching T11–T13.** Three rulings from Kai landed on 2026-08-12 and they
> change the shape of the economy:
> **(A) No holding cost at all** — rent, the standing SPL delegate, the
> Token-2022 permanent delegate and foreclosure are all removed. Holding ENC
> already loses truthfully, because the balance sits still while asset prices
> rise. Assets change hands by **scheduled auction** instead of forced sale.
> **(B) It runs forever**, with one exception it can prove for itself: a
> permissionless `retire` that any caller may trigger once the oracle has been
> silent long enough (new **T28**).
> **(C) Closed loop by posture** — BadCode seeds no liquidity pool and sells no
> ENC, ever. ENC stays a plain SPL token that anyone else may pool if they wish;
> we neither prevent it nor point at it. The faucet is therefore the only route
> in that we control, which makes T13's parameters a pass/fail test at T14.
>
> The evidence behind all three is at
> [`research/2026-08-12-enc-tokenomics/`](./research/2026-08-12-enc-tokenomics/README.md).
>
> **An adversarial review (2026-08-12, same day) then attacked the rulings and
> the tickets.** The rulings held — the arithmetic was re-verified from a fresh
> FRED pull and the auction shape survived. The tickets did not, quite: **T12**
> gained three spec fixes (stale-bid release, settlement that never needs the
> outgoing holder's cooperation, the invariant restated in signature form),
> **T28**'s rationale was rewritten (oracle silence ≠ Fed silence, and its
> correctness now explicitly depends on T16/T18's release-date sourcing), and
> **T29** was added — as built, the sync caps guarantee eventual forced
> retirement. Claims corrections landed in the decision doc §4.
Relates: `docs/stories/magic-money-tree/emperors-new-coin.md` (canon — the coin
is a cryptocurrency folded into the Magic Money Tree story, cross-promoted with
it). Upstream reference repo: https://github.com/emperorsnewcoin/coin (design
docs only; it never got as far as contracts).

## Progress board

Full detail per ticket under **Tickets**, below. The checkbox there is the record;
this table is the map.

| | Ticket | Track |
|---|---|---|
| ✅ | T1–T6 · toolchain, Anchor workspace, chain-kit / chain-react / chain-cli, `/coins/:slug` | toolchain |
| ✅ | T24–T27 · Docker toolchain, counter harness, copy-out proof, `./stack` | toolchain |
| 🟡 | T16 · Switchboard feed authored, immutability **proven live** — but the **date feed is still missing**, and T18/T28 depend on it (2026-08-13 audit) | oracle |
| ✅ | T7 · program state, `math.rs`, placeholder genesis params | program |
| ✅ | T8 · `initialize` + `init_asset` ×10 | program |
| ✅ | T9 · oracle trait + MockOracle behind a Cargo feature | program |
| ✅ | T10 · `sync_m2` — supply targeting, the core | program |
| ⛔ | T11 · rent, `settle_rent`, `foreclose` — **SUPERSEDED 2026-08-12**, built, still in the tree until T30 removes it | program |
| ✅ | T30 · remove the rent machinery (the deletion Ruling A implies) | program |
| ✅ | T12 · the tenancy auction — `place_bid` · `withdraw_bid` · `settle_auction` · `roll_term` · `mint_certificate` | program |
| ✅ | T13 · the faucet — `claim` · `close_epoch` (Ruling C made it the only way in) | program |
| ✅ | T28 · `retire` — the coin notices its own end (ending ruled: **keep trading**) | program |
| ✅ | T29 · proportional sync caps + the catch-up walk (2026-08-12 review) | program |
| ✅ | T31 · the Imperial Gazette — tenant copy + the editor's pen. `Asset` is now **414 bytes and boxed everywhere**; that size is permanent after T22 | program |
| ✅ | T14 · economic simulation harness (+ `@badcode/enc`, the math mirror) | economics |
| ✅ | T15 · the genesis parameters, chosen and recorded in `chain/sim/RESULTS.md` | economics |
| ⬜ | T17 · stand the M2SL feed up on devnet | oracle |
| ⬜ | T18 · Switchboard on-chain read + crank (**wall-clock stall: budget a day**) | oracle |
| ✅ | T19 · ENC page, read-only state — the printer + the Imperial Gazette front page, live on localnet | web |
| ✅ | T20 · ENC page, wallet actions + the melting balance — **one gap: the two-wallet Phantom run-through is still owed a human** | web |
| ✅ | T21 · documentation — `docs/coins/emperors-new-coin.md` + the **claim ledger**, every figure re-derived from the FRED record | docs |
| ⬜ | T22 · devnet deploy + **burn the upgrade authority** | ship |
| ⬜ | T23 · end-to-end verification | ship |

**T30, T12, T13, T28, T29 are one continuous run** — each builds on the last,
all in Rust, all validated by `./stack cargo test …` and `./stack test test-…`.
Nothing in that stretch needs devnet, Switchboard, or a browser. (T7–T11 were
the same kind of run and are done, T11 having been superseded.)

**Two schedule facts worth knowing before you start.** T18 needs a Switchboard
quote that has genuinely *aged* on devnet, so it stalls a calendar day no matter
how fast the code goes — start it the moment the read path compiles. And T15
picks the real economic parameters, so T7's `params.genesis.json` values are
deliberately placeholders; don't tune them by hand on the way past.

---

## Context

BadCode is going to release Solana projects as part of the BadCode universe.
The first is **Emperor's New Coin (ENC)**: a satirical token whose supply is
programmatically pegged to the US Federal Reserve's M2 money supply. When the
Fed prints, ENC prints.

Two things are being built here, and the order matters:

1. **A reusable Solana toolchain inside this monorepo.** Not a standalone crypto
   repo — libraries and build tooling that multiple coin projects can be spawned
   from, with all their frontends served by the single existing BadCode web app
   (`apps/web`). ENC is the first consumer and therefore the forcing function.
2. **The ENC program and page itself.**

The repo today has **zero** Solana/crypto code — verified: no `solana`,
`@coral-xyz`, `web3.js`, or wallet-adapter entries anywhere in
`package-lock.json`, no `.rs` files, no `Anchor.toml`, no `chain/` directory.
Everything here is greenfield. The only existing crypto artifact is narrative:
canon at `docs/stories/magic-money-tree/emperors-new-coin.md:151` flags "what
the cryptocurrency actually is" as the open question this plan answers, and
`apps/web/src/home/timeline.ts:107-117` reserves a `coming-soon` node pointing
at `/comics/emperors-coin` from when ENC was going to be a comic.

### What the research established

Four deep-research passes were run before this design (Switchboard; the wider
oracle landscape; trust-minimisation patterns; engagement economics). The
findings that shaped the design, with the ones that **changed** it marked:

- **★ There is no M2 feed on any oracle, on any chain.** The US Department of
  Commerce publishes CPI and GDP on-chain via Chainlink, but M2 is a *Federal
  Reserve Board* statistic and the Fed is not in that partnership. We are first.
- **★ Switchboard On-Demand has no feed authority.** A feed *is* its job
  definition: the feed ID is a commitment to the canonical protobuf bytes of the
  job, and the on-chain account is a PDA derived from `(queue, feed IDs)`.
  Changing one character of the job produces a different feed ID at a different
  address — you have not edited the feed, you have created an unrelated one. The
  `verified_update` instruction has **no authority account and no owner check**.
  There is a separate product called *Authority-Updated Feeds* which is exactly
  the backdoor we are designing out; we never touch it.
- **★ M2 needs no API key.** `api.stlouisfed.org` requires one, but the Fed's own
  Data Download Program and FRED's `fredgraph.csv` both serve M2 keyless as CSV.
  Since Switchboard's hosted secrets service has been shut down and its
  replacement (`variableOverrides`) means *only the key-holder can crank the
  feed*, going keyless is what keeps the feed permissionless.
- **★ Cadence is monthly, not weekly.** The Fed's H.6 release has been monthly
  since 23 Feb 2021 — fourth Tuesday, 1:00pm ET, ~1 month data lag. Verified
  live against the current H.6 release.
- **★ Use `M2SL`, not `WM2NS`.** The weekly series is *non-seasonally-adjusted*
  and rises every December on holiday cash demand. A program pegged to it would
  mint on Christmas shopping rather than Fed policy.
- **★ Harberger without a carrying cost is inert.** The self-assessed price is a
  truth-telling device; the *tax* is the turnover engine. Replacing self-assessment
  with an oracle price is fine, but deleting the tax means ten wallets take the
  ten assets in the first hour and nothing happens again. A decade of Harberger
  art experiments has no published evidence of frequent turnover.
- **★ Token-2022's interest-bearing extension is cosmetic.** Official docs:
  *"No new tokens are ever created… The feature is entirely cosmetic."* The rate
  can be negative (`i16` basis points) but it only changes the displayed UI
  amount. There is no drop-in decaying token on Solana.
- **UMA / the Polymarket pattern does not port.** UMA is EVM-only across 12
  chains with its DVM on Ethereum mainnet. Its token-weighted dispute vote is
  our exact threat model (whale-swung resolutions; >half of votes in disputed
  markets from the ten largest wallets). Every Solana prediction market resolves
  via an admin multisig or council.
- **Signature verification is cheap.** ed25519 strict verify is 2,400 compute
  units. Cryptography is not the constraint; operations are.
- **The real operational adversary is bot protection.** FRED sits behind Akamai;
  blocks manifest as *hangs, not errors*, and a spoofed Chrome User-Agent is
  blocked while `python-requests` passes. Expect to chase this at least once.

### The claim we can honestly make

> "The supply rule is a hash. The program will only accept a number that a
> hardware-attested oracle network signed after running *that exact job
> definition* — fetching M2 from the Federal Reserve. We can't change the job,
> because changing it doesn't edit the feed, it creates a different feed our
> program won't read. There is no admin key. There is no pause button. There
> isn't even an owner field."

**Amended by T31 (2026-08-12):** once the Gazette lands, "there is no admin key"
may never again be said unqualified — one key will exist, and the claim must
always be stated in its two-part form: **no key over the money; one editorial
pen over the words, and it can only strike, once per column per edition.** See
T31's claims-surgery checklist.

Every clause is defensible. The claim we must **not** make is "nobody can affect
this but the Fed" — Switchboard's queue authority governs which attested oracles
may sign. The honest framing is *"we removed ourselves from the loop,"* which is
also checkable, and a satire about monetary control whose reality-feed depends on
a small consortium deciding who may sign for reality is on-theme. State it loudly.

Separately and independently: **our own program ships non-upgradeable** (BPF
upgrade authority burned to `None`, mint and freeze authority handled as below).
That is what makes "not even we can change the rule" literally true, costs
nothing, and is verifiable by any skeptic with one RPC call.

---

## Architecture

### Repo layout

```
badcode/
│
├─ chain/                        ★ NEW — Anchor workspace (Rust + its own package.json)
│   ├─ package.json              added to the root workspaces glob
│   ├─ Anchor.toml
│   ├─ Cargo.toml                (Cargo workspace)
│   ├─ programs/
│   │   └─ emperors-new-coin/
│   ├─ tests/                    Anchor integration tests (TS, vs localnet)
│   ├─ sim/                      economic simulation harness
│   └─ target/idl/*.json         generated
│
├─ packages/
│   ├─ chain-kit/                ★ NEW — framework-agnostic TS client
│   ├─ chain-react/              ★ NEW — React layer (web only)
│   └─ cli/                      EXISTING — gains `badcode chain <cmd>`
│
└─ apps/web/src/coins/enc/       ★ NEW — the /coins/enc page
```

`chain/` **is** an npm workspace member. An Anchor workspace ships a
`package.json` (that is how `anchor test` runs ts-mocha), so it must be added to
the root `workspaces` glob at `package.json:6-9` — otherwise npm never links
`node_modules` there and neither the Anchor tests nor the simulation harness can
resolve `@coral-xyz/anchor`, mocha, vitest, or `@badcode/chain-kit`.

Package names avoid `@badcode/solana-*` because Anza ships `@solana/kit` (the v2
successor to web3.js) and the collision would be actively confusing. **We use
web3.js v1 types** (`PublicKey`, `TransactionInstruction`) because that is what
Anchor still requires; pin `@solana/web3.js@^1.95`.

`chain-kit` is pure TypeScript — no React, no Node-only APIs — because
`apps/web` consumes workspace packages as **unbuilt source**: `tsc` resolves via
the `@badcode/*` → `packages/*/src` path mapping (`tsconfig.base.json:19-22`)
while **Vite** resolves through the npm workspace symlink and the package's
`exports` field (`apps/web/vite.config.ts` declares no `resolve.alias` — verified).
Anything Node-only would therefore break the browser build. The CLI and the
browser share one source of truth for program IDs, PDA seeds, and instruction
encoding.

**The toolchain's success test:** coin #2 writes a Rust program and a page
component, and writes no plumbing.

### Portability contract — the toolchain must survive leaving this repo

A second, unrelated BadCode project (nothing to do with coins or tokens) will
want to write a Solana program, test it, and build a frontend against it. So the
generic layer must be liftable by copying folders, **without dragging any of
ENC's strong opinions along**. That constrains the design now:

```
PORTABLE — zero ENC references, copy-paste to any project
  chain/{Anchor.toml,Cargo.toml,rust-toolchain.toml,versions.json,scripts/install.sh}
  packages/chain-kit/      clusters · RPC · explorer URLs · generic program
                           registry · generic PDA derive
  packages/chain-react/    provider · useProgram(idl, programId) · useAccount
                           · useSendTransaction · ConnectWallet · ClusterBadge
  packages/chain-cli/      doctor · up · down · build · deploy · idl · airdrop
                           — its OWN package with its own bin, NOT a subfolder
                           of packages/cli (which drags in sharp + GCS + comic
                           tooling and cannot be lifted)

ENC-SPECIFIC — delete freely when lifting
  chain/programs/emperors-new-coin/    the program
  chain/feeds/ · chain/sim/            M2 feed + economic simulation
  packages/enc/                        ENC accounts · instruction builders
                                       · math mirror · IDL · program ID
  packages/cli/src/enc.ts              the `chain enc` sub-group
  apps/web/src/coins/enc/              the page
```

Two rules that make this real, and both are testable:

1. **No file under `packages/chain-kit`, `packages/chain-react`, or
   `packages/chain-cli` may reference ENC** — not by import, not by name, not by
   a string literal like `'emperors-new-coin'`. The program registry is a generic
   `name → address` map loaded from JSON; the `chain` commands take a program
   name as an argument. ENC's `chain enc` sub-group lives in `packages/cli`
   (BadCode's own CLI), which *depends on* `chain-cli` — never the reverse.
   `./stack` reaches both: it calls `chain-cli`'s bin by path, and ENC verbs
   forward to `packages/cli`. The other project lifts `chain-cli` whole and runs
   its bin directly, with `./stack` verbs of its own — proven in the forum repo.
2. **`chain-react` is generic over the IDL.** `useProgram(idl, programId)` takes
   them as parameters rather than looking up a hardcoded program, so the React
   layer never imports a specific program's types. (This also removes any build
   ordering coupling to a generated IDL.)

T23 verifies this by grep, not by good intentions.

### The ENC machine

> **⚠ SUPERSEDED IN PART (2026-08-12).** The diagram and several paragraphs in
> this section describe the **rent-era architecture** — force-buy, rent,
> foreclosure, the Token-2022 permanent delegate, Invariant M. Ruling A removed
> all of it; they stand here as the record of what was designed and why. The
> live architecture is: **no holding cost; the ten flags stay in program
> custody; tenancy auctions (T12); a tenancy certificate in the holder's
> wallet; no token leaves any wallet without its owner's signature.** Where a
> paragraph below disagrees with the decision doc or with T12/T28/T29, the
> tickets win.

```
   ┌─────────────────────────────────────────────────────┐
   │  Federal Reserve H.6 — M2SL                         │
   │  monthly · 4th Tuesday · 1:00pm ET · keyless CSV    │
   └───────────────────────┬─────────────────────────────┘
                           │  Switchboard On-Demand
                           │  feed ID = hash of the fetch job
                           │  no authority · no API key
                           │  anyone may crank (~$0.0015)
                           ▼
   ┌─────────────────────────────────────────────────────┐
   │  sync_m2()   ← permissionless, anyone may call      │
   │  guards: feed_id matches · release date advanced    │
   │          · Δ within sanity cap · single-mint cap    │
   └───────────────────────┬─────────────────────────────┘
                           │  target_supply = k × M2_latest
              ┌────────────┴────────────┐
              ▼                         ▼
        M2 rose                    M2 fell
     mint Δ → VAULT            burn Δ ← VAULT
              └────────────┬────────────┘
                           ▼
        all 10 asset prices × (M2_new / M2_old),
        interpolated over 30 days ⇒ prices tick EVERY SLOT


   THE CIRCULAR ECONOMY  (total supply untouched by all of this)

        ┌──────────────── EMPEROR'S VAULT ────────────────┐
        │                                                  │
        │  faucet: register in epoch N,                    │
        │          collect share of pot(N) in epoch N+1     │
        │          pot(N) = α × max(0, V − floor·S)         │
        ▼          snapshotted when epoch N opens           │
   ┌─────────┐   force-buy at fixed price, 100% to seller  │
   │ PLAYERS │ ◄──────────────────────────────────────►    │
   │         │        no refusal · no cooldown              │
   └────┬────┘                                             │
        │  rent ρ%/day of current price ──────────────────►│
        │  foreclosure if unpaid ────────────────────────►│
        └──────────────────────────────────────────────────┘
```

**Two flows that must never be confused.** The oracle alone changes total
supply. Rent, foreclosure and purchases only move *existing* tokens between the
vault and players.

### Key decisions and rejected alternatives

**Supply targets a level, not a delta.** `supply = k × latest published M2`, and
each sync mints or burns `target − current_supply`. Every release simply
retargets. *Rejected:* a ratchet on `max(M2_seen)`, proposed to dodge M2's
retroactive revisions (verified: the same observation restated downward ~0.16%
between vintages). The dodge is unnecessary — we burn from the vault, so a
downward revision uses the identical code path as quantitative tightening.
*Also rejected:* a `burn_deficit` field tracking burns the vault couldn't cover.
Under level-targeting the excess self-corrects at the next sync; tracking it as
well would apply the correction twice and undershoot permanently. Consequence to
state honestly: the true invariant is **`supply ≥ k × M2`**, with equality
whenever the vault was solvent enough to absorb the last burn.

**Exact units — these must not be guessed.**
- M2SL is published in **billions of USD** (e.g. `22176.1`). On-chain
  `m2_value` is that number in **fixed-point with 6 decimals**:
  `22176.1 → 22_176_100_000`.
- **ENC has 6 decimals.** Nine would overflow: ~2.21e10 whole ENC at 9 decimals
  is 2.21e19 base units, past u64 max (1.845e19). Six gives 2.21e16 — ~830×
  headroom.
- **`k = 1_000_000`**, so `supply_base_units = m2_value × k`. This yields
  1 ENC per $1,000 of M2 (M2 ≈ $22.18T → ≈ 22.18 billion ENC).
- All targeting arithmetic is computed in **`u128`** and narrowed to `u64` with
  a checked conversion that errors rather than wrapping.

**The 50% floor governs the faucet, not the burn.** Burning from the vault
*lowers the vault's share of supply* (S=100/V=50, burn 10 → S=90/V=40 = 44%), so
the floor cannot be a hard invariant enforced by refusing to burn — the burn must
always happen. Instead the faucet pot is `α × max(0, V − floor·S)`, which is zero
below the floor while rent refills it. The story: *the Fed tightens, and your
pocket money stops entirely until rent rebuilds the Emperor's coffers.* Genesis
vault is **100%** — at `initialize` there is nobody else to hold anything, and
BadCode takes no allocation.

**The faucet is register-now, collect-next-epoch.** A pot cannot be divided
fairly among a set that is still growing. So `claim()` does two things in one
transaction: pays your share of the **previous** epoch's pot (`pot(N−1) /
registrants(N−1)`), and registers you for the current one. `pot(N)` is
snapshotted when `FaucetEpoch(N)` is created by its first claimer — computed from
the vault balance *before* that caller's own payout — so outflow during any epoch
is **at most** one pot (registrants who never return simply leave their share
behind). *Rejected:* dividing the current pot by the previous epoch's headcount —
10 registrants one day and 1,000 the next would drain 100× the pot, inverting
the very property the design depends on.

**The welcome grant is floor-gated too.** It is separately capped at
`grants_per_epoch`, first-come, so aggregate outflow stays bounded against
unlimited fresh wallets; but it is *also* refused whenever
the vault sits below the floor. Otherwise fresh wallets would keep drawing
`grants_per_epoch × welcome_grant` out of a depleted vault every epoch forever,
which both breaks the floor's whole purpose and contradicts the story beat. Below
the floor **nothing** is paid out: no share, no grant. If you arrive during the
tightening, there is nothing for you until rent rebuilds the coffers — which is
exactly what austerity is, and exactly what the coin is about.

**Rent is the turnover engine.** ~5%/day of the current price, accrued lazily
from a `last_touched` timestamp (computed on read — no crank, no iteration over
accounts). `foreclose` is permissionless so nobody has to run a bot. *Rejected:*
shipping an event-only version first and adding rent later — Kai chose to build
the engine in from day one because dormancy is the predicted steady state, not
a risk.

**No identity system.** The faucet's pot is fixed per epoch, so a sybil farm
running a thousand wallets dilutes itself and everyone else equally and cannot
increase the vault's outflow. Combined with **Invariant M** — *when all ten
assets are held by players, aggregate daily rent exceeds the aggregate daily
faucet pot* — monopolising the assets is arithmetically impossible. (The
invariant is stated conditionally on purpose: while assets sit in the vault the
vault would be paying rent to itself, so there is nothing to monopolise and
nothing to check.) *Rejected:* World ID / proof-of-personhood (investigated or
suspended in 13+ jurisdictions; requiring an iris scan to play a joke about the
Fed is the wrong punchline), wallet-age heuristics (defeated in five minutes),
and gas-as-cost (5,000 lamports per signature is worthless as a deterrent).
Honest consequence, to be stated publicly: ten assets can only fund so much
income, so the game supports on the order of tens-to-low-hundreds of *active*
players. Spectators are unlimited. Scarcity of the flags is the point.

**Token standards.** ENC is a **classic SPL token** with 6 decimals, mint
authority on the vault PDA and **freeze authority `None`** — so Jupiter and every
DEX stay compatible (the coin must be freely listable; BadCode takes no revenue
from it) and there is no account-freezing admin power. The ten assets use
**Token-2022 with the Permanent Delegate extension plus the metadata pointer and
embedded metadata extensions**, so the program can move an NFT out of a holder's
wallet without their signature *and* wallets render it with a name and image.
Permanent delegate is what makes force-buy work; it is literally a rug-pull
primitive, which for this coin is the thesis rather than a smell.

*Freeze authority `None` is not optional.* A freeze authority can freeze any
holder's account, so keeping one would be a live BadCode key over other people's
coins — it contradicts "no admin key," it is flagged by every token risk scanner
as a rug vector, and setting it to `None` at creation is free and irreversible.

**The mint-authority warning is a feature. Do not try to suppress it.** ENC must
keep its mint authority forever, so scanners will permanently report ENC as
arbitrarily inflatable. That report is *correct*, and it is the joke landing
without our help: a coin about money printing, flagged by the machines as a
money-printing risk. Lean into it — quote the warning in our own copy. The
explanation sits beside it: the authority is a PDA of a non-upgradeable program,
so no human can inflate it, which a person can verify in one RPC call and an
automated scanner cannot distinguish from a founder's key. Expect any listing
verification to need a human; specific aggregator criteria belong to the mainnet
launch plan, not this one.

**Environment split — deliberate and absolute.** Localnet runs the **mock oracle
only** and never talks to Switchboard; devnet is the **staging** environment where
the real oracle integration is proven end-to-end. There is no local Switchboard
setup, because cloned oracle accounts are frozen snapshots that no oracle ever
re-signs, so a local clone could only ever prove we can decode a stale quote —
not the failure that would hurt on mainnet. Fast iteration comes from the mock;
truth comes from devnet.

**Cosmetic decay moves to the frontend.** Since ENC stays classic SPL, there is
no interest-bearing extension. The melting balance is rendered by the **website**:
the chain holds the truth, the page shows a number quietly shrinking. A coin
named for a story about seeing what isn't there, whose own website lies to you
about what you have.

**Oracle depth: Switchboard + in-program sanity bounds.** *Rejected for now:* an
optimistic challenge layer (bonded proposals, 7-day window, any challenge
cancels the round with no mint). It is designed-for and cheap to add later — M2
is a cumulative level that never expires, so "tie goes to no-mint" costs us
nothing while being catastrophic for a prediction market, which is the asymmetry
that lets us skip the adjudicator every prior attempt got stuck on. But an
optimistic oracle with no economically-motivated watchers is theatre. *Also
rejected:* zkTLS via Reclaim — its Solana verifier is an abandoned 2024 demo
(last deployed 2024-03-24, **1 witness, minimum 1**, one-day validity window long
expired, upgradeable by Reclaim); shipping it would be *more* centralised than a
quorum while sounding more trustless. *Also rejected:* a K-of-N signer quorum
(good, ~1-2 weeks, but Switchboard's keyless no-authority path is strictly better
and cheaper to operate) and pegging to Pyth's live CPI feed instead of M2 (a real
creative alternative — "we inflate exactly as fast as your savings evaporate" —
but the ENC canon joke is the *printer*, and Pyth's economic feeds move behind a
$2,500/month tier this month with Pythnet retiring).

---

## File Structure

### Create — `chain/`

| Path | Purpose |
|---|---|
| `chain/package.json` | `@badcode/chain`, private; devDeps: `@coral-xyz/anchor`, `@solana/web3.js@^1.95`, `@solana/spl-token`, `ts-mocha`, `mocha`, `chai`, `vitest`; scripts `test`, `typecheck` |
| `chain/Anchor.toml` | Program IDs per cluster; `[scripts]` entries for per-suite test runs |
| `chain/Cargo.toml` | Cargo workspace manifest |
| `chain/rust-toolchain.toml` | Pins the Rust version |
| `chain/versions.json` | Pinned solana/anchor/rust versions, read by `chain doctor` |
| `chain/params.genesis.json` | Genesis economic parameters (placeholders at T7, finalised at T15) |
| `chain/programs/emperors-new-coin/Cargo.toml` | Program manifest |
| `chain/programs/emperors-new-coin/src/lib.rs` | Entrypoint + handlers |
| `chain/programs/emperors-new-coin/src/state.rs` | As built: `Config`, `Printer`, `Asset`, `Bid`, `FaucetEpoch`, `Player` (+ `MockOracle` behind the `mock` feature). Non-data PDAs: vault, escrow, ENC mint, asset mints, certificate mints. |
| `chain/programs/emperors-new-coin/src/errors.rs` | `ErrorCode` enum |
| `chain/programs/emperors-new-coin/src/math.rs` | Supply targeting, price interpolation, auction/faucet arithmetic (unit-tested). **No rent accrual** — Ruling A removed it; T30 deleted the code. |
| `chain/programs/emperors-new-coin/src/oracle.rs` | Oracle read abstraction: Switchboard + mock behind a feature |
| `chain/programs/emperors-new-coin/src/instructions/*.rs` | One file per instruction |
| `chain/tests/*.ts` | Anchor integration tests, one file per suite |
| `chain/sim/*.ts` | Economic simulation harness |
| `chain/scripts/crank.ts` | Standalone published crank anyone can run |
| `chain/feeds/m2sl.job.json` | The raw Switchboard job definition, committed |
| `chain/README.md` | Install → run → deploy → **how to add coin #2** |

### Create — `packages/chain-kit/`

`package.json` (name `@badcode/chain-kit`, private, `type: module`,
`main`/`module`/`types`/`exports` → `./src/index.ts`, scripts `typecheck`:
`tsc --noEmit` and `test`: `vitest run`, devDep `vitest`, dep
`@solana/web3.js@^1.95` — matching the `packages/comic-meta/package.json`
convention), `tsconfig.json`, and:
`src/{index,clusters,registry,pda}.ts`, `src/programs.json`, `src/*.test.ts`.
**Generic only** — no ENC file, no `'emperors-new-coin'` literal.

### Create — `packages/enc/` (created at T14)

`@badcode/enc` — everything ENC-specific that both the CLI and the web app need:
`src/{index,accounts,instructions,math}.ts`, `src/idl/emperors_new_coin.ts`,
`src/*.test.ts`. Depends on `@badcode/chain-kit`; nothing depends on it except
the ENC page, the `chain enc` CLI sub-group, and the simulation harness.

### Create — `packages/chain-react/`

`package.json` (`@badcode/chain-react`, same conventions, React 18.3 peer dep),
`tsconfig.json`, `src/SolanaProvider.tsx`, `src/useProgram.ts`,
`src/useAccount.ts`, `src/useSendTransaction.ts`, `src/ConnectWallet.tsx`,
`src/ClusterBadge.tsx`, `src/*.test.ts`.

### Create — `apps/web/src/coins/`

`coins.ts` (slug → lazy component registry), `enc/EncPage.tsx`,
`enc/Printer.tsx`, `enc/AssetGrid.tsx`, `enc/Wallet.tsx`, `enc/enc.css`.

### Create — docs

`docs/coins/emperors-new-coin.md` — public design + the honest trust statement.

### Modify

| Path | Change |
|---|---|
| `package.json:6-9` | Add `"chain"` to the `workspaces` array |
| `apps/web/src/App.tsx:20-29` | Add `<Route path="/coins/:slug">`, introducing `React.lazy` + `<Suspense>` (the file currently uses neither) |
| `apps/web/src/home/timeline.ts:113` | `route: '/comics/emperors-coin'` → `'/coins/enc'` (note: `:112` is `title`) |
| `apps/web/src/home/timeline.ts:114` | `status` → `'live'` (T22 only) |
| `apps/web/src/home/comics.test.ts:11-15` | Asserts `resolveComic('emperors-coin').kind === 'stub'`; breaks once the node's route leaves `/comics/` |
| `apps/web/src/home/atlas/diorama.test.ts:16` | Asserts `enterTargetFor` is `null` for `emperors-coin`; true only while `status` is `'coming-soon'` |
| `apps/web/src/home/catalog.ts:74` | Comment naming `emperors-coin` as living at a comic route goes stale |
| `apps/web/package.json` | Add `@badcode/chain-kit`, `@badcode/chain-react` as `"*"` deps |
| `packages/cli/package.json` | Add `@badcode/chain-kit` as a `"*"` dep |
| `packages/cli/src/bin.ts` | Register the `chain` command group (existing pattern at `:38-130`) |
| `package.json` | `chain:*` convenience scripts |
| `.gitignore` | `chain/target/`, `chain/.anchor/`, `chain/test-ledger/`, local keypairs |
| `docs/stories/magic-money-tree/emperors-new-coin.md:151` | Resolve the open thread |
| `CLAUDE.md` | Add the toolchain to the repo map |

---

## Interfaces

### PDA seeds — byte-exact, mirrored in Rust

| Account | Seeds |
|---|---|
| `Config` | `b"config"` |
| `Printer` | `b"printer"` |
| `Vault` | `b"vault"` |
| `Asset` | `b"asset"`, `index: u8` (1 byte) |
| `FaucetEpoch` | `b"epoch"`, `epoch: u64` **little-endian** (8 bytes) |
| `Player` | `b"player"`, `wallet: Pubkey` (32 bytes) |

Epoch index is `unix_timestamp / 86_400`.

### `@badcode/chain-kit`

```ts
export type Cluster = 'localnet' | 'devnet' | 'mainnet-beta'
export function rpcEndpoint(cluster: Cluster): string
export function explorerUrl(cluster: Cluster, kind: 'tx'|'address', id: string): string
export function programId(name: string, cluster: Cluster): PublicKey
// generic: reads src/programs.json, a plain { [name]: { [cluster]: address } } map.
// NEVER hardcode a program name here — see the Portability contract.

// ── Everything below this line is ENC-specific and lives in `@badcode/enc`,
//    NOT in chain-kit. chain-kit exports only the generic `derive()` helper.
export const SEEDS: {
  config: readonly [Buffer]
  printer: readonly [Buffer]
  vault: readonly [Buffer]
  asset:  (index: number) => readonly [Buffer, Buffer]   // u8
  epoch:  (n: bigint)     => readonly [Buffer, Buffer]   // u64 LE
  player: (w: PublicKey)  => readonly [Buffer, Buffer]
}
export function derive(seeds: readonly Buffer[], pid: PublicKey): [PublicKey, number]

export interface EncConfig {
  mint: PublicKey; vault: PublicKey; expectedFeedId: Uint8Array
  k: bigint; encDecimals: number
  rentRatePerDayBps: number; faucetAlphaBps: number; floorBps: number
  welcomeGrant: bigint; grantsPerEpoch: number
  graceSeconds: number; forecloseBounty: bigint
  maxChangeBps: number; maxSingleMint: bigint
  initializedAssets: number
}
export interface EncPrinter {
  m2Value: bigint        // billions USD, 6dp fixed-point (22176.1 → 22_176_100_000)
  m2ReleaseDate: number  // unix seconds — the FED RELEASE, not the sync time
  lastSyncSlot: bigint
  targetSupply: bigint   // base units
}
export interface EncAsset {
  index: number
  holder: PublicKey | null   // null iff the on-chain field equals the vault PDA
  priceFrom: bigint; priceTo: bigint
  interpStart: number; interpEnd: number
  rentAccrued: bigint; lastTouched: number
}
export interface EncPlayer {
  wallet: PublicKey
  lastRegisteredEpoch: bigint
  welcomeGrantTaken: boolean
}
export interface EncFaucetEpoch {
  epoch: bigint; pot: bigint; registrants: number; grantsIssued: number
}

export function currentPrice(a: EncAsset, nowUnix: number): bigint
export function rentOwed(a: EncAsset, nowUnix: number, cfg: EncConfig): bigint
export function faucetShare(prev: EncFaucetEpoch | null): bigint
export function decodeConfig(b: Buffer): EncConfig      // …and one per account type

export const ENC_IX: {
  initialize(...): TransactionInstruction
  initAsset(...): TransactionInstruction
  syncM2(...): TransactionInstruction
  setMockM2(...): TransactionInstruction   // mock builds only
  claim(...): TransactionInstruction
  buyAsset(...): TransactionInstruction
  settleRent(...): TransactionInstruction
  foreclose(...): TransactionInstruction
  closeEpoch(...): TransactionInstruction
}
```

### `@badcode/chain-react` — generic, never imports a specific program

```tsx
<SolanaProvider cluster={Cluster}>{children}</SolanaProvider>
function useProgram<T extends Idl>(idl: T, programId: PublicKey): Program<T> | null
function useAccount<T>(pk: PublicKey | null, decode: (b: Buffer) => T):
  { data: T | null; loading: boolean; error: Error | null }
function useSendTransaction():
  { send(ixs: TransactionInstruction[]): Promise<string>; pending: boolean; error: Error | null }
<ConnectWallet />
<ClusterBadge />
```

### CLI

Everything is reached through **`./stack`** at the repo root. Neither `badcode`
nor `chain` is on anyone's PATH — they exist only as `node_modules/.bin` symlinks,
so never write them bare in docs, tickets or UI copy.

```
./stack start                       # image, validator, funded wallet, deploy, web app
./stack stop · status · logs [web|validator]
./stack build [prog] · deploy · redeploy [prog] · reset
./stack test [suite]                # Anchor suites, against the running validator
./stack cargo <args>                # cargo in the container — Rust unit tests
./stack doctor · wallet · shell · image · fund <address>
./stack check                       # typecheck + unit tests, repo-wide

./stack enc init --cluster <c>      # ENC-specific, added from T9 onward
./stack enc crank --cluster <c>     # post a Switchboard update + call sync_m2
./stack enc mock-m2 <value>         # localnet, mock builds only
./stack enc state --cluster <c>
```

### Program instructions

> **Rewritten 2026-08-13 to the as-built surface.** This table previously listed
> `buy_asset`, `settle_rent` and `foreclose` — the rent economy Ruling A deleted
> and T30 removed. What follows is what the program actually exports today.

| Instruction | Signer | Effect |
|---|---|---|
| `initialize(params)` | **upgrade authority**, once ever | ENC mint (6dp, mint authority = vault PDA, **freeze authority None**), vault, `Config` (immutable), `Printer`; bootstrap supply from a hardcoded genesis M2 the first `sync_m2` corrects |
| `init_asset(index, name, symbol, uri, genesis_price)` | **upgrade authority**, once each, in order | One `Asset` PDA + its Token-2022 NFT (metadata pointer, **no permanent delegate**), held by the vault. Gated by `Config.initialized_assets` |
| `sync_m2()` | **nobody — no signer at all** | Validate quote → one `capped_step` toward target → mint to / burn from vault → rescale all ten price curves. Rejected until all 10 assets exist, and after `retire` |
| `claim(epoch)` | claimer | Pay share of `pot(N−1)`; pay welcome grant if new and grants remain; register for epoch `N`. Pays nothing at all below the vault floor |
| `close_epoch(n)` | **anyone** | Reclaim rent-exemption from a settled `FaucetEpoch` (n ≤ current−2) to the closer |
| `place_bid(index, amount)` | bidder | Escrow the bidder's **own** ENC as the standing high bid. Must beat the interpolated price and the current high bid strictly |
| `withdraw_bid(index)` | bidder | Return escrow and close the `Bid`. Refused only while the bid is both standing **and** from the current term |
| `settle_auction(index)` | **anyone** (fee payer only) | After `term_ends_at`: escrow → outgoing holder, tenancy → winner, term increments. Needs no cooperation from the outgoing holder |
| `roll_term(index)` | **nobody — no signer at all** | After `term_ends_at` with no qualifying bid: release the stale high bid, increment the term, holder unchanged |
| `mint_certificate(index, term)` | **anyone** (pays) | Token-2022 certificate minted **to the holder**, never the caller. The Emperor gets no receipt |
| `retire()` | **nobody — no signer at all** | Set `retired` once the oracle has been silent for `retirement_silence_seconds`. One-way. Stops only `sync_m2` |
| `set_mock_m2(v, d)` · `mock_fund(amount)` | anyone | **Compiled only under `--features mock`** |
| `file_copy(index, text)` · `spike(index)` · `pass_the_pen(k)` · `break_the_pen()` | tenant / editor | **T31, not yet built.** The Gazette — see Ruling D |

**Four instructions take no signer whatsoever** (`sync_m2`, `roll_term`,
`retire`, and `settle_auction` bar its fee payer). That is the point: the
machine runs itself, and **no token moves without its owner's signature.**

`Config` is written once at `initialize` and has no mutating instruction — there
is no setter for any economic parameter. The upgrade authority is burned at T22.

---

## Out of Scope

- **Mainnet launch** — deploy, branding, liquidity, launch comms, disclaimers.
- **The optimistic challenge layer** — designed-for above; not built.
- **DAO / governance** (the old repo's "Socialism Coin" concept).
- **Any second coin.** The toolchain is validated by ENC alone.
- **A prediction / "Rumour Board" feature** — a good future addition.
- **Season leaderboards** — computed off-chain from emitted events later.
- **Changing the comics pipeline, story canon prose, or the 3D homepage** beyond
  the ENC timeline node and the tests that assert its old state.

---

## Tickets

### T1: WSL toolchain install + `badcode chain doctor`   [Status: DONE 2026-08-10 | Model: sonnet]
- **Scope:** Install script for the native WSL toolchain (Rust, agave/Solana CLI,
  Anchor via avm) with pinned versions in `chain/versions.json`, plus a `doctor`
  command verifying each and printing actionable remediation per failure.
  **First task — choose and record the versions.** They are deliberately not
  hardcoded here because Anchor/Agave/Rust compatibility moves; the executor must
  resolve the current mutually-compatible set (check Anchor's release notes for
  its required Solana CLI and Rust versions) and write the exact triple into
  `chain/versions.json` before writing any install logic. Do not guess or use
  "latest" — every later ticket builds against this pin.
  **Command shape:** `badcode chain doctor` (and later `badcode chain enc crank`)
  needs **two-level nesting**, which `packages/cli/src/bin.ts` does not currently
  demonstrate — all eight existing commands are flat
  `program.command('x').action(...)` (see `:38-48` for the shape). Build the group
  with `new Command('chain')` + sub-commands + `program.addCommand(chain)`;
  commander `^12.1.0` is already a dependency. Note `packages/cli/src/` is flat
  today, so `src/chain/` is the first subdirectory.
- **Files:** `chain/scripts/install.sh`, `chain/versions.json`,
  **`packages/chain-cli/`** (new package: `package.json` with a `chain` bin,
  `tsconfig.json`, `src/index.ts` exporting a commander `Command` group,
  `src/doctor.ts`), and `packages/cli/src/bin.ts` + `packages/cli/package.json`
  to register that exported group as `badcode chain`.
- **Acceptance criteria:** `install.sh` brings a bare machine to the pinned
  versions. `doctor` exits 0 when correct, non-zero with a named remediation
  otherwise.
- **TDD:** no (environment wiring)
- **Validation:** `npx tsx packages/cli/src/bin.ts chain doctor` exits 0;
  `anchor --version`, `solana --version`, `rustc --version` match `chain/versions.json`.
- **Depends on:** —
- [x] done
- Notes:

### T2: Anchor workspace scaffold + npm workspace membership   [Status: DONE 2026-08-10 | Model: sonnet]
- **Scope:** Create `chain/` as both a Cargo and an npm workspace member: add
  `"chain"` to the root `workspaces` array, write `chain/package.json` with the
  Anchor/mocha/vitest devDeps and `typecheck`/`test` scripts, and a program
  containing only a no-op instruction. Wire `.gitignore`. Add per-suite
  `[scripts]` entries to `Anchor.toml` (see T-validation note below).
- **Files:** `package.json` (modify), `chain/{package.json,Anchor.toml,Cargo.toml,rust-toolchain.toml}`,
  `chain/programs/emperors-new-coin/{Cargo.toml,src/lib.rs}`, `chain/tests/smoke.ts`, `.gitignore`.
- **Acceptance criteria:** `anchor build` emits `.so` + `chain/target/idl/emperors_new_coin.json`.
  `anchor test` deploys and calls the no-op. Root `npm install` links
  `chain/node_modules` and still succeeds. Root `npm run typecheck` and
  `npm run test` include `chain` without failing.
- **TDD:** no (scaffolding)
- **Validation:** `npm install` at root exits 0; `cd chain && anchor build && anchor test`;
  root `npm run typecheck` exits 0.
- **Depends on:** T1
- [x] done
- Notes:

### T3: `@badcode/chain-kit` foundation   [Status: DONE 2026-08-10 | Model: sonnet]
- **Scope:** Clusters, RPC endpoints, explorer URLs, program registry, and PDA
  derivation matching the byte-exact seed table in Interfaces. No React, no
  Node-only APIs. Declare `typecheck`/`test` scripts and the `vitest` devDep —
  root `--if-present` silently skips a missing script rather than failing.
- **Files:** `packages/chain-kit/{package.json,tsconfig.json}`,
  `src/{index,clusters,registry,pda}.ts`, `src/programs.json`, `src/*.test.ts`.
- **Acceptance criteria:** PDA derivation is unit-tested against fixed expected
  addresses for known seeds (so T7's Rust must match these, not the reverse).
  Importing the package pulls in no Node builtins. **`grep -riE "enc|emperor|m2"
  packages/chain-kit/src` finds no ENC reference** — the program registry is a
  generic JSON map and `programId()` takes a `string`. ENC's own seeds, decoders
  and IDL live in `@badcode/enc` (created at T14), never here.
- **TDD:** yes
- **Validation:** `npm run typecheck --workspace @badcode/chain-kit`;
  `npm run test --workspace @badcode/chain-kit`; root `npm run typecheck`.
- **Depends on:** T2
- [x] done
- Notes:

### T4: `badcode chain` lifecycle commands   [Status: DONE 2026-08-10 | Model: sonnet]
- **Scope:** `up`, `down`, `build`, `deploy --cluster`, `idl --out`, `airdrop`.
  `up` runs `solana-test-validator` detached with a gitignored ledger and polls
  until RPC answers. `idl` copies the generated IDL into
  a caller-specified directory (no hardcoded default naming a program — see the
  Portability contract). Add `@badcode/chain-kit` to the CLI's deps.
- **Files:** `packages/chain-cli/src/*.ts` (generic commands), `packages/cli/src/bin.ts`,
  `packages/cli/package.json`, root `package.json` (scripts).
- **Acceptance criteria:** Full lifecycle works from the repo root regardless of
  CWD. Note the pitfall at `.claude/skills/animate-slide/SKILL.md:210-213`:
  `npm run --workspace` sets CWD to `packages/cli/`, so repo paths must not be
  resolved relative to CWD. **There is no existing root-detection helper to
  reuse** — `packages/cli/src/bin.ts` passes raw `process.cwd()` throughout, so
  T4 must *write* one (walk up from `__dirname` until a `package.json` containing
  a `workspaces` key is found) and use it for every repo-relative path.
- **TDD:** yes for path/argument resolution; lifecycle itself is manual.
- **Validation:** `npx tsx packages/cli/src/bin.ts chain up` then
  `solana cluster-version --url http://127.0.0.1:8899` succeeds; `chain down`;
  `npm run test --workspace @badcode/cli`.
- **Depends on:** T3
- [x] done
- Notes:

### T5: `@badcode/chain-react` foundation   [Status: DONE 2026-08-10 | Model: sonnet]
- **Scope:** Provider stack (connection + wallet-adapter with Phantom),
  `useProgram`, `useAccount` (websocket subscription with cleanup),
  `useSendTransaction`, `<ConnectWallet>`, `<ClusterBadge>`. Types against the
  **generic over the IDL** — `useProgram<T extends Idl>(idl, programId)` takes both
  as parameters, so this package never imports a specific program's types and has
  no build-ordering dependency on any generated artifact. Test it against a
  hand-written minimal `Idl` fixture, not a real program's output.
- **Files:** `packages/chain-react/{package.json,tsconfig.json}`, `src/*.tsx`, `src/*.ts`, `src/*.test.ts`.
- **Acceptance criteria:** `useAccount` re-renders on change and unsubscribes on
  unmount (tested with a fake connection). No import of `@badcode/chain-react`
  from the CLI. **`grep -ri "enc\|emperor" packages/chain-react/src` returns no
  ENC reference** — this package must be liftable to an unrelated project.
- **TDD:** yes for subscription lifecycle; no for UI primitives.
- **Validation:** `npm run typecheck --workspace @badcode/chain-react`;
  `npm run test --workspace @badcode/chain-react`.
- **Depends on:** T3
- [x] done
- Notes:

### T6: `/coins/:slug` route, ENC shell, and the tests it breaks   [Status: DONE 2026-08-10 | Model: sonnet]
- **Scope:** Add the lazy-loaded route (introducing `React.lazy` + `<Suspense>`,
  which `App.tsx` does not currently use), a slug registry, an ENC shell mounting
  `<SolanaProvider>` with cluster badge and connect button, and repoint the
  timeline node's `route`. **Fix the two existing tests this breaks** and the
  stale comment.
- **Files:** `apps/web/src/App.tsx`, `apps/web/src/coins/coins.ts`,
  `apps/web/src/coins/enc/EncPage.tsx`, `apps/web/src/home/timeline.ts:113`,
  `apps/web/src/home/comics.test.ts:11-15`, `apps/web/src/home/atlas/diorama.test.ts:16`,
  `apps/web/src/home/catalog.ts:74`, `apps/web/package.json`.
- **Acceptance criteria:** `/coins/enc` renders and connects Phantom against
  localnet; `/coins/nope` → NotFound; wallet libraries land in a separate chunk
  (verified in build output), not the main bundle; the homepage node links to
  `/coins/enc`; **the full web test suite passes**, with `comics.test.ts` updated
  to reflect that `emperors-coin` is no longer a comic slug and `diorama.test.ts`
  still valid for a `coming-soon` node.
- **TDD:** no (wiring), but the two broken tests must be updated deliberately.
- **Validation:** `npm run test --workspace @badcode/web`; `npm run build`
  showing a separate coin chunk; root `npm run typecheck`.
- **Depends on:** T5
- [x] done
- Notes:

### T7: Program state + math module + genesis params   [Status: DONE 2026-08-11 | Model: opus]
- **Scope:** Define `Config`, `Printer`, `Asset`, `FaucetEpoch`, `Player` with
  the byte-exact seeds from Interfaces. Implement `math.rs`: supply targeting
  (`u128` intermediate, checked narrowing), price interpolation, rent accrual,
  faucet share — all pure, all unit-tested. Write `chain/params.genesis.json`
  with **placeholder** values (`k = 1_000_000`, decimals 6, floor 5000 bps, rent
  500 bps/day, α, welcome grant, grants/epoch, grace, bounty, sanity caps),
  clearly marked as replaced by T15.
- **Files:** `chain/programs/emperors-new-coin/src/{state,errors,math}.rs`,
  `chain/params.genesis.json`, `chain/programs/emperors-new-coin/src/lib.rs`.
- **Acceptance criteria:** Math unit tests cover zero, max, and overflow
  boundaries and prove `k × m2` cannot wrap. Rust PDA seed constants match
  T3's fixed expected addresses.
- **TDD:** yes
- **Validation:** `./stack cargo test -p emperors-new-coin --lib`.
- **Depends on:** T3, T2
- [x] done
- Notes: 42 unit tests green. The Rust seed test asserts the same three base58
  literals as `pda.test.ts`, so the two languages fail together or not at all.
  Rent is the **exact integral** of the interpolated price rather than a sample
  of either endpoint — tested by splitting an interval four ways and getting the
  same total, which is what stops rent depending on when someone settles.
  Two small design calls made here, both cheap to revisit: `Asset.holder` is a
  plain `Pubkey` using the vault as the "unowned" sentinel (fixed-size layout,
  both cases cost the same to read) rather than an `Option`; and `Player` carries
  a single `last_registered_epoch` that does two jobs — `== current` rejects a
  second claim, `== current − 1` grants eligibility — so the two facts cannot
  disagree with each other.

### T8: `initialize` + `init_asset`   [Status: DONE 2026-08-11 | Model: opus]
- **Scope:** `initialize` creates the classic-SPL ENC mint (6 decimals, mint
  authority = vault PDA, **freeze authority `None`**), the vault PDA and its ATA,
  `Config` (immutable) and `Printer`, and mints a bootstrap supply from a
  hardcoded genesis M2 value that the first real `sync_m2` corrects.
  `init_asset(index)` — called ten times, one per transaction — creates one
  `Asset` PDA and its Token-2022 NFT with permanent delegate, metadata pointer
  and embedded metadata (name + image URI), held by the vault, incrementing
  `Config.initialized_assets`. **Split deliberately:** doing all of this in one
  instruction is ~40 accounts, past both the 200k CU limit and the 1232-byte
  transaction limit.
- **Files:** `chain/programs/emperors-new-coin/src/instructions/{initialize,init_asset}.rs`,
  `chain/tests/initialize.ts`.
- **Acceptance criteria:** `initialize` callable exactly once; no instruction
  anywhere mutates `Config`; freeze authority is `None`; vault holds **100%** of
  supply at genesis; `init_asset` is idempotent-guarded per index and rejects
  index ≥ 10; all ten NFTs carry metadata a wallet can render; each call fits in
  one transaction under the CU limit.
- **TDD:** yes
- **Validation:** `./stack test test-init` (add the Anchor.toml `[scripts]` entry
  invoking ts-mocha on `tests/initialize.ts`; `./stack test <name>` passes it to
  `anchor test --script`, which reuses the running validator).
- **Depends on:** T7
- [x] done
- Notes: 20 tests green. **Three decisions the ticket did not specify.** (1) Both
  instructions gate on the loader's own `ProgramData` upgrade-authority record —
  the plan said "deployer, once" without saying how, and without a gate a
  stranger could `initialize` between our deploy and our first transaction and
  choose every parameter permanently. No new key: the authority already exists
  and is burned at T22. (2) The ENC mint and the ten NFT mints are **PDAs**
  (`b"mint"`, `b"asset_mint" + index`), so no deployer keypair ever holds a mint.
  (3) Assets must be created **in order**, which makes `initialized_assets`
  exactly "how many exist" for `sync_m2` to trust.
  **Anchor evaluates `init` before bare `constraint =`**, so an authority gate
  does not short-circuit account creation — a stranger aiming at an *existing*
  account gets "already in use" and never reaches the check. Atomicity means the
  gate still holds; it means a test must aim at a *fresh* index to prove it.
  **The ten asset names are still placeholders**, living only in the test —
  naming them is Kai and Jack's call, and costs one bootstrap call, not a
  redeploy.

### T9: Oracle abstraction + MockOracle   [Status: DONE 2026-08-11 | Model: opus]
- **Scope:** A trait returning `(m2_value, release_date)`, with `switchboard`
  (stubbed until T18) and `mock` implementations behind a Cargo feature. Add
  `./stack enc mock-m2`. **Also add `--features <list>` to `chain build`** — it
  currently takes only `--program-name`, and without a way to pass Cargo features
  through to `anchor build` the mock build cannot be produced at all.
- **Files:** `chain/programs/emperors-new-coin/src/oracle.rs`,
  `src/instructions/set_mock_m2.rs`, `packages/chain-cli/src/{anchor,index}.ts`,
  `packages/cli/src/enc.ts`, `stack`, `chain/Anchor.toml`.
- **Acceptance criteria:** A default build does not compile `set_mock_m2` into
  the program at all; a `--features mock` build does. Anchor's `idl-build`
  feature must still be active in both.
- **TDD:** no (plumbing); covered by T10.
- **Validation:** `./stack build && ! grep -q set_mock_m2 chain/idl/emperors_new_coin.json`
  then `./stack build --features mock && grep -q set_mock_m2 chain/idl/emperors_new_coin.json`.
  (Note `grep -c` prints `0` but **exits 1**, so it cannot be used here.)
- **Depends on:** T8
- [x] done
- Notes: Both grep directions verified. `anchor build -- --features x` **does**
  forward (unlike `anchor deploy`, which drops everything after `--`). The `mock`
  feature also scopes `anchor-lang/init-if-needed`, so a default build cannot use
  that pattern anywhere. `./stack enc` routes to the **badcode** CLI, not the
  chain one — ENC commands must never enter `@badcode/chain-cli`. Proven live:
  `./stack enc mock-m2 22176.1`. Note the real Switchboard path is a stub
  returning `OracleUnavailable`, so a default build cannot sync until T18; the
  two things T18 must get right are recorded in `oracle.rs`.

### T10: `sync_m2` — supply targeting and guards   [Status: DONE 2026-08-11 | Model: opus]
- **Scope:** The permissionless core. Read the oracle; **require the release date
  to have strictly advanced** (anti-double-mint); reject a change beyond
  `max_change_bps`; cap any single mint; compute `target = k × m2` in `u128` and
  mint `target − supply` to the vault or burn `supply − target` from it. If the
  vault cannot cover a burn, burn its entire balance and leave supply above
  target — **no deficit is recorded**, because the next sync's level-targeting
  self-corrects. Rescale all ten assets' interpolation endpoints by the same
  ratio over 30 days. Reject until `initialized_assets == 10`.
- **Files:** `chain/programs/emperors-new-coin/src/instructions/sync_m2.rs`,
  `src/math.rs` (extend), `chain/tests/sync_m2.ts`.
- **Acceptance criteria:** A rise mints exactly to target; a fall burns exactly
  to target; a repeat call with an unchanged release date **fails**; a change
  beyond the sanity cap fails; a burn exceeding vault balance zeroes the vault and
  leaves supply above target. The **following** sync then either mints to exact
  target (if M2 rose) or burns as much as the vault then holds (if it fell again)
  — it does **not** guarantee one-step restoration, because a second fall against
  an empty vault cannot correct. The invariant to assert is `supply ≥ k × m2`
  after every successful sync, with equality whenever the vault could absorb the
  move. Prices scale by the same ratio and interpolate over 30 days.
- **TDD:** yes
- **Validation:** `./stack cargo test -p emperors-new-coin --lib && ./stack test test-sync`.
- **Depends on:** T9
- [x] done
- Notes: 12 tests. **Rent is banked before prices rescale** — rent accrues from
  `last_touched` against the curve, so replacing the curve without settling would
  retroactively recompute every unpaid day at the new prices. Not in the ticket;
  it is a correctness requirement the design implies. The ten assets arrive as
  `remaining_accounts` (naming them exceeds the tx size limit) and each is
  **re-derived, not trusted** — without that, ten copies of asset 0 rescale it
  ten times. The uncovered-burn acceptance case is **deliberately pending**: it
  is unreachable while the vault holds every token, so it is enabled at T13.
  Toolchain fallout: suites run through **mocha + tsx** (ts-mocha cannot resolve
  TS-importing-TS as ESM, so a shared harness was impossible), and a
  **`--features` build no longer publishes the IDL**, or the committed interface
  flips with whichever build ran last.

### T11: Rent accrual, `settle_rent`, `foreclose`   [Status: **SUPERSEDED 2026-08-12** — built, then removed by ruling A | Model: opus]

> **Do not build this. It is kept for the record.** The code was written and
> tested (commit `9a94fa3`), then ruled out on 2026-08-12. **Rent inverts the
> thesis:** asset prices rise with M2 at a median of ~0.52%/month, and rent was
> set at 5%/day (~150%/month), so owning an asset was a catastrophic loss and
> holding ENC was the better trade — the exact opposite of the joke. For "assets
> beat cash" to be true on chain, any holding cost must sit *below* the M2 growth
> rate (~6%/year), and at that rate rent cannot also serve as the turnover engine
> it was hired to be. Under the artwork framing (legibility over engagement)
> turnover was never required, so the job no longer exists. **The design now has
> no holding cost at all** — holding ENC already loses truthfully, because the
> balance sits still while asset prices rise. See
> [`2026-08-12-enc-architecture-decision.md`](./2026-08-12-enc-architecture-decision.md).
> Removing it also drops the standing SPL delegate and the Token-2022 permanent
> delegate, which are the two primitives Solana risk scanners weight most heavily.

<details><summary>Original ticket (superseded)</summary>

- **Scope:** Lazy rent from `last_touched` at the configured per-day rate against
  the *current interpolated* price. `settle_rent` (permissionless) moves owed rent
  from holder to vault. `foreclose` (permissionless) returns the asset to the
  vault when rent debt exceeds the holder's balance and grace has elapsed, paying
  the caller a bounty from the vault.
- **Files:** `chain/programs/emperors-new-coin/src/instructions/{settle_rent,foreclose}.rs`,
  `src/math.rs` (extend), `chain/tests/rent.ts`.
- **Acceptance criteria:** Rent accrues continuously and is exact across
  interpolated price changes. `foreclose` fails before grace and succeeds after.
  A holder whose balance covers the debt cannot be foreclosed. Rent moves to the
  vault and **never** changes total supply. Assets held by the vault accrue no rent.
- **TDD:** yes
- **Validation:** `./stack cargo test -p emperors-new-coin --lib && ./stack test test-rent`.
- **Depends on:** T10
- [ ] done — code complete; 7 acceptance cases pending a holder (T12)
- Notes: **OPEN DECISION FOR KAI.** "Permissionless" + "moves tokens from holder
  to vault" cannot both hold for a classic SPL token unless the program is a
  **delegate**. Implemented that way: `buy_asset` will make the vault an
  unlimited delegate over the buyer's ENC, signed by the buyer. The bargain
  becomes "to hold a flag you sign away control of your money" — thematically
  perfect, but it is a real cost to players. A holder can `revoke`, after which
  rent stops being collectable and foreclosure follows. **Alternative:** drop
  "permissionless" from `settle_rent` and collect only at sale and foreclosure.
  Confirm before T12 builds on it.
  Foreclosure needs debt > balance **and** grace — either alone lets a solvent
  holder be evicted by anyone patient, or evicts on the first cent of shortfall.
  Bounty capped at the vault balance so a poor vault cannot block foreclosure.
  Debt dies with the tenancy. **Localnet headroom raised 500KB → 1MB** — the
  program now lands near 530KB and overran the old reservation.

</details>

### T12: The tenancy auction — `place_bid` + `settle_auction`   [Status: pending — replaces the forced sale | Model: opus]
- **Scope:** Each of the ten assets is held for a fixed **term** (placeholder: 30
  days, aligned to the price interpolation window). During a term anyone may
  `place_bid`, transferring ENC into a program-owned escrow — **signed by the
  bidder, so no delegate over anyone's balance is ever required.** A bid must beat
  both the current interpolated price (the reserve — a flag can never change hands
  below what M2 says it is worth) and the standing high bid. A superseded bidder
  may `withdraw_bid` at any time. At term end anyone may call `settle_auction`
  (permissionless): the winner's escrow pays **100% to the outgoing holder** (the
  vault, if the Emperor held it), the `Asset` reassigns to the winner, and a fresh
  term begins. **If no bid cleared the reserve the incumbent keeps it for another
  term** — dormancy is an expected outcome, not a failure.
  Three settlement rules from the 2026-08-12 adversarial review, each closing a
  hole the original spec left open:
  - **The reserve is re-checked at settlement, and a standing bid that no longer
    clears it is released** — `high_bid` clears and the bid becomes withdrawable
    exactly as if superseded. Prices move during a term (~94% of months, upward),
    so a bid that beat the reserve when placed can sit under it at term end;
    without release, the sole bidder in a dormant market is locked into term
    after term while the reserve climbs away from them. That is the stranding
    the acceptance criteria forbid, reached under the design's *expected* state.
  - **Settlement never depends on the outgoing holder's cooperation.** If their
    ENC token account is missing (closed, deliberately or not — the classic
    push-payment veto), `settle_auction` creates it, payer = caller. Otherwise
    an incumbent blocks their own eviction and freezes the winner's escrow by
    closing one account.
  - **The incumbent may bid on their own asset** — they are just another bidder,
    and a winning self-bid simply renews the term (settlement must tolerate
    payer = payee). To take a flag from someone defending it, outbid them; that
    is an auction working, not a loophole.
- **Custody — the ten flags never leave program custody.** Each sits in a
  vault-owned token account; the `Asset` PDA records who holds the tenancy. This
  is what removes the permanent delegate, and it is honest: it *is* a lease, and
  the chain says so.
- **What the holder actually gets in their wallet: a tenancy certificate.**
  Winning mints the holder their own NFT — theirs outright, in Phantom from the
  moment they win. **At term end nothing is taken from them.** It simply stops
  being the current tenancy and becomes a stub: a ticket for a night that already
  happened, kept forever, numbered and dated.
  - *Why this rather than putting the flag itself in the wallet* (asked and ruled
    2026-08-12): a wallet-held flag would have to be pulled back at settlement
    without the holder's signature, which means the **permanent delegate returns**
    — the exact power, and the exact scanner flag, that Ruling A removed. There is
    no third way; wallet residency and permissionless settlement are mutually
    exclusive.
  - *And it is the better joke.* **You never really owned the asset. All you keep
    is the receipt.** That is the Emperor's New Clothes exactly: the magnificent
    thing was never yours, and what you're left with is documentation that you
    were there. The certificate carries the comedy — *"Certificate of Temporary
    Ownership. The bearer held [asset]. It is no longer theirs. Thank you for
    participating in the economy."*
  - *Net effect:* **no path in the entire program touches anyone's wallet without
    their signature.** Not the coin, not the flags, not the certificates.
  - **Correction from the build:** the certificate is *claimable* from the
    moment they win, not already in the wallet — issuing it is a separate
    permissionless `mint_certificate`, and the winner's frontend bundles the
    two instructions. See the Notes for why settlement does not carry it.
  - **Immutable at mint** (2026-08-12 review): no update authority, no freeze
    authority; name, term number and dates written once at issue. Its "stub"
    state is *derived* — the certificate's term number no longer matches the
    `Asset`'s — never written by a later instruction. That makes "never touched
    again" structural rather than a matter of implementer restraint.
- **On forcing the outgoing holder — state this plainly in the copy.** Settlement
  does remove the tenancy whether the incumbent likes it or not. What makes that
  fair rather than a seizure is that it happens **on a clock published at the
  moment they won** (a term, not ownership), and they are **paid the current
  price, whatever M2 says it is** — never say "the new, higher price": M2 falls
  in 6.1% of months (nine consecutively in 2022–23 — corrected from "13 in a
  row" at T21, see the Discovered Issues Log), the reserve falls with it, and an
  incumbent settled out in a contraction is paid *less* than they bid. Never
  describe a tenancy as owning the asset.
- **Why this shape:** the outgoing holder is paid the *new* price having bought at
  the old one, so a term held through an expansion pays out more than it cost — in
  a currency that buys less than it used to. That is the entire joke, executed by
  the machine, with nobody's wallet touched without their signature.
- **Files:** `chain/programs/emperors-new-coin/src/instructions/{place_bid,withdraw_bid,settle_auction}.rs`,
  `src/state.rs` (extend: `term_ends_at`, `high_bid`, `high_bidder`, `term_number`;
  `Bid` PDA), `chain/tests/auction.ts`.
- **Acceptance criteria:** A bid below the reserve or below the standing high bid
  is refused. `settle_auction` before term end is refused. The outgoing holder
  receives exactly the winning bid. A superseded bidder can always recover their
  escrow in full. Settling with no qualifying bid leaves the holder unchanged and
  starts a new term. Total supply is never changed by any path. **Escrowed ENC is
  never strandable** — every route out is reachable by the bidder alone;
  specifically, a stale high bid (placed above the reserve, overtaken by it
  mid-term) is released at a no-winner settlement and recoverable in full.
  `settle_auction` succeeds when the outgoing holder's ENC token account has
  been closed, creating it with the caller as payer. A winning self-bid
  (payer = payee) settles cleanly and renews the term. A
  tenancy certificate is minted to the winner and is **never** moved, burned or
  reclaimed by any later instruction — prove it by settling a subsequent term and
  asserting the previous holder's certificate is untouched, and assert the
  certificate mint carries **no update authority and no freeze authority**.
  **No tokens leave any wallet without that wallet owner's signature.** (The
  earlier caller-form of this sentence — "no instruction can move a token the
  caller does not own" — was unsatisfiable as written: `settle_auction` is
  permissionless and moves the winner's escrow by design, and T13's `claim`
  pays vault tokens to the caller. The signature form is the real invariant;
  found by the 2026-08-12 review.)
- **TDD:** yes
- **Validation:** `./stack test test-auction`.
- **Depends on:** T10 (no longer T11)
- [x] done
- Notes: 12 auction cases green on a fresh ledger; `test-init` and `test-sync`
  still green beside them. Every acceptance criterion is covered, including the
  three the adversarial review added — the stale-bid release, the closed-account
  veto, and the signature-form invariant.
  **Five shape decisions the ticket left open.**
  (1) **`roll_term` is a second instruction**, not a branch inside
  `settle_auction`. The two outcomes need genuinely different accounts — a
  no-winner term has no bid, no winner and no payment — and Anchor optional
  accounts would have been the only way to keep one name. Their guards are
  exact complements, so every ended term is handled by precisely one of the
  two and neither can deny the other's outcome. An explorer also now says which
  of the two happened without decoding anything, which is a legibility win.
  (2) **Escrow pools in its own PDA, deliberately not the vault.** `sync_m2`
  burns from the vault's token account, so pooling bids there would let an
  ordinary monetary contraction destroy bidders' money — stranding reached
  through a path nobody would think to test.
  (3) **The certificate is `mint_certificate`, a separate permissionless
  instruction**, not part of settlement. Atomic issue would drag a mint,
  metadata and an ATA into the no-winner path too, and make a stranger settling
  out of civic duty pay for someone else's souvenir. Consequence for the copy:
  the certificate is *claimable* from the moment they win, not already in the
  wallet — the ticket body's "in Phantom from the moment they win" is corrected
  above. The winner (or their frontend) bundles both instructions in one
  transaction, so in practice it is instant.
  (4) **`Asset.last_touched` became `term_ends_at`** (T30 flagged this here).
  Nothing else read "when was this last written" — the price curve carries its
  own window. Added alongside: `term_number`, `high_bid`, `high_bidder`, a
  `Bid` PDA per (asset, bidder), and `Config.term_seconds`.
  (5) **The permanent delegate is gone from `init_asset`**, which the
  Discovered Issues Log flagged as T12's call. Under program custody it was
  dead weight costing the heaviest scanner flag, and its absence is what makes
  the signature invariant structural. `initialize.ts` now asserts the *absence*
  where it used to assert the presence.
  **Two things worth not rediscovering.** A bid is locked only while it is both
  the standing high bid *and* from the live term, which is what makes a stale
  high bid recoverable without a special case. And raising a bid is a top-up
  (only the difference moves), so a superseded bidder does not have to withdraw
  and re-bid.
  **Test-only affordance, logged below:** `mock_fund` — the vault holds every
  token and the faucet is T13, so without it the auction could not be tested
  against a bidder who owns anything.

### T13: The faucet — register-now, collect-next-epoch   [Status: pending | Model: opus]
- **Scope:** `claim()` in epoch `N`: (1) create `FaucetEpoch(N)` if absent, payer
  = caller, snapshotting `pot(N) = α × max(0, V − floor·S)`; (2) if the caller
  registered in `N−1`, pay `pot(N−1) / registrants(N−1)`; (3) if new, create the
  `Player` PDA and ENC ATA and pay the welcome grant, provided
  `grants_issued(N) < grants_per_epoch` **and the vault is above the floor**;
  (4) register for `N`. Reject a second claim in the same epoch.
  **Snapshot timing:** `pot(N)` is computed from the vault balance at the moment
  `FaucetEpoch(N)` is created, **before** that same caller's `pot(N−1)` payout and
  welcome grant are deducted. Add `close_epoch(n)` (permissionless, `n ≤ current−2`)
  reclaiming the rent-exemption to the closer, so epoch accounts don't accumulate
  forever.
- **Files:** `chain/programs/emperors-new-coin/src/instructions/{claim,close_epoch}.rs`,
  `src/state.rs` (extend), `chain/tests/faucet.ts`.
- **Acceptance criteria:** **Total payout during any epoch `N` is at most
  `pot(N−1)` plus `grants_per_epoch × welcome_grant`, regardless of how many
  wallets claim.** (At most, not exactly — registrants who never return leave
  their share in the vault.) A simulated 1,000-wallet farm arriving in epoch `N+1`
  after 10 claimants in `N` extracts at most `pot(N)` in total, not 100× it.
  Epoch 0 pays no share (nothing registered before it) and does not divide by
  zero. **Below the floor, both the pot and the welcome grant are zero** and
  `claim` still succeeds without reverting. If the vault cannot cover a computed
  share, pay what remains and never underflow. A second claim in one epoch fails.
  `close_epoch` refuses `n > current−2`.
- **TDD:** yes
- **Validation:** `./stack test test-faucet`.
- **Depends on:** T12
- [x] done
- Notes: 10 faucet cases green, and 31 Rust unit tests (the epoch arithmetic
  gained two). **Three decisions the ticket did not spell out.**
  (1) **The epoch length became `Config.epoch_seconds`**, exactly as
  `term_seconds` did at T12 and for exactly the same reason: at the shipped one
  day, *not one* acceptance criterion is reachable — a pot divided among
  yesterday's registrants, a second claim refused inside one epoch, an epoch old
  enough to close, all of them need a boundary crossed. The harness runs 15
  seconds, `params.genesis.json` keeps 86,400, and `initialize.ts` asserts
  `Config` carries the harness value so the substitution is visible rather than
  assumed. The epoch is a **PDA seed input**, so this decides which accounts can
  ever exist — safe only because it is chosen once and has no setter.
  Consequence worth catching: `PRICE_INTERPOLATION_SECONDS` was defined as
  `30 × SECONDS_PER_EPOCH` and is now `30 × SECONDS_PER_DAY`. Left alone, a
  short test epoch would have shrunk every price curve to nothing, leaving all
  ten assets permanently arrived at their targets and quietly disabling the
  reserve the auction bids against.
  (2) **`claim` gates on `initialized_assets == ASSET_COUNT`**, like `place_bid`.
  Not in the ticket, and it closes a real window: between `initialize` and the
  tenth `init_asset` the vault holds every token, so a stranger claiming in that
  gap draws a full pot out of a machine that is not built yet. The window is
  live at T22.
  (3) **The welcome grant is keyed on `welcome_grant_taken`, not on "is this
  wallet new".** Somebody whose first visit landed below the floor, or after the
  day's allotment ran out, is owed theirs when they come back. The field's own
  doc already said "never resets"; this is what that buys, and the program
  README's sentence about the grant was corrected in the same commit to say so.
  **`mock_fund` stays, deliberately.** T13 does give wallets a real route to
  ENC, but funding the auction suite through it would make a bidder's stake
  `pot ÷ registrants` — a number that depends on whether *another suite* claimed
  in the previous epoch, on a ledger all the suites share and which runs them
  alphabetically. That is the cross-suite coupling the log already warns about,
  and it would make every auction case wait out an epoch before it could bid.
  The mock-surface argument does not bite either way: `mock_fund` ships in
  **neither** build, and `initialize.ts` asserts that against the committed IDL,
  so the claim it could threaten is about the shipped interface and is untouched.
  What the faucet proves instead is in its own suite: a claimant's payout clears
  the cheapest asset's live reserve, so the loop closes.
  **Two traps worth not rediscovering.** The epoch index has to be an
  **instruction argument** (a PDA seed cannot read the clock), so the program
  checks it against `Clock::get()` and returns the new `WrongEpoch` when a
  transaction straddles a boundary — correct behaviour, and the suite resubmits
  rather than loosening the check. And **chai's ordering assertions reject a
  BigInt outright** ("expected N to be a number or a date"), which fails five
  tests at once while the program is entirely correct; every amount here is a
  u64 that does not survive a `Number`, so ordering is asserted as a boolean
  with both operands printed.
  The below-floor case drives the vault under its floor with `mock_fund` and
  **puts the money back in a `finally`** — the vault ATA is an ordinary token
  account, so anyone may pay into it. Without the restore, every later run of
  the suite finds an empty Emperor and fails for a reason unrelated to the code.
  **The faucet is now the only way in.** Ruling C (2026-08-12) is that
  BadCode seeds no liquidity and sells nothing, so unless a stranger makes a pool
  there is no route to ENC except this instruction. That turns a tuning
  preference into a **pass/fail test for T14**: a patient claimant must be able to
  accumulate enough to clear an auction reserve within a reasonable number of
  epochs. If they cannot, the loop does not close and the artwork is a shop
  window. The good news is that it self-scales — the pot is a share of the vault,
  and vault and asset prices both move with M2 by the same factor, so the ratio
  holds as M2 grows.

### T14: Economic simulation harness   [Status: pending | Model: opus]
- **Scope:** A TypeScript harness replaying real historical M2SL (including the
  2022–23 contraction — the first sustained decline since the 1930s) through the
  program's math, with synthetic player populations including a sybil-farm
  cohort — **plus a forward projection: ≥50 years at the median M2 growth rate
  (~0.52%/month), asserting `sync_m2` never deadlocks against the caps.** The
  forward leg exists because the cap failure T29 fixes is in the *future* by
  construction; a historical replay alone would have waved it through. Reports
  vault share, time-to-first-asset (a patient claimant reaching the cheapest
  auction reserve — T13's pass/fail). Invariant M was rent-era arithmetic and
  retires with T11; asset-turnover reporting is optional colour, not a
  criterion, per Ruling A. Depends only on `math.rs`'s TS mirror, **not** on the
  oracle integration.
- **Files:** `chain/sim/{index,players,report}.ts`, `chain/sim/m2-history.csv`,
  `chain/sim/*.test.ts`, and **create `packages/enc/`** (`@badcode/enc`:
  `package.json`, `tsconfig.json`, `src/{index,math}.ts`) — the first ENC-specific
  client package, kept out of `chain-kit` per the Portability contract.
- **Acceptance criteria:** The TS math mirror is tested to agree with the Rust
  unit tests on the same fixed vectors. The harness runs the full history and
  emits a report without asserting any particular outcome (T15 judges).
- **TDD:** yes
- **Validation:** `npm test --workspace @badcode/chain` (vitest; the sim is pure
  TypeScript, so it needs no container).
- **Depends on:** T13
- [x] done
- Notes: 30 mirror tests in `@badcode/enc`, 15 simulation tests in
  `chain/sim`, `./stack check` green repo-wide.
  **The mirror is all `bigint`.** Every quantity in this program is a `u64` in
  base units and `Number` silently rounds above 2^53, which the money supply
  passed long ago (~2.2e16 base units today). A mirror that quietly rounded
  would be worse than none, because the parameters that ship are chosen against
  it. `math.test.ts` copies the Rust vectors verbatim, so the two languages fail
  together — the same arrangement `pda.test.ts` already has for the seeds.
  **The finding, and it looked exactly like the bug T29 had just fixed.** The
  first historical run reported **133 deadlocked releases and one 8-step
  catch-up walk**. Neither is real. The program writes `m2_release_date = 0` at
  genesis, on the reasoning that any real Fed release is later than the unix
  epoch — true of a coin deployed in 2026, and **false of a replay that starts
  in 1959, because pre-1970 observations have negative timestamps.** So every
  release from 1959-01 to 1969-12 failed the anti-double-mint guard (133 of
  them), the peg sat frozen for eleven years, and the first release it *did*
  accept was a +110% move it then had to walk in eight steps. A fact about the
  harness, not the program: a historical run now says when the coin was
  notionally deployed. Worth recording because a number that looks like a
  deadlock is exactly the number this harness exists to detect, and it was
  wrong the first time.
  **What is modelled, and what is deliberately not.** The peg (including T29's
  walk), the vault, supply, the ten price curves, and the faucet in full — pots,
  snapshots, registration, grants, the floor. Not modelled: bidding, terms,
  certificates, who wins what. Ruling A removed turnover as a goal, so asset
  turnover is explicitly not a criterion. What *is* modelled is the money moving
  when a purchase happens, because a purchase from the Emperor refills the vault
  and that changes the faucet — the vault is not simply a leak.
  **Deterministic on purpose:** nothing calls `Math.random`, and the M2 history
  is a committed CSV rather than a fetch, so the sweep that picks the parameters
  for a non-upgradeable program gives the same answer twice. The re-fetchable
  version stays at `design/research/2026-08-12-enc-tokenomics/m2-backtest.mjs`
  and the two must agree.
  **The dead state is a first-class run**, not an afterthought: the whole record
  with not one participant. It passes — the vault holds everything, the prices
  go on repricing, and nothing breaks. That is the floor Ruling A set, and now
  it is a test rather than an intention.
  **Left for T15, since T14 judges nothing:** at the shipped genesis M2 the
  placeholder price ladder makes the cheapest tenancy affordable after **two
  epochs**, which is almost certainly too cheap for a thing whose scarcity is
  the point. Note the ladder is *not* a T29-class time bomb even though it is an
  absolute number — every sync rescales all ten by the same factor, so it tracks
  M2 forever. What T15 is choosing is only where it starts, relative to the
  genesis supply.

### T15: Choose the genesis parameters   [Status: pending | Model: opus]
- **Scope:** Sweep parameters with the T14 harness and commit the chosen values
  to `chain/params.genesis.json`, replacing T7's placeholders. Record the
  rationale and the rejected settings in `chain/sim/RESULTS.md`.
- **Files:** `chain/params.genesis.json`, `chain/sim/RESULTS.md`.
- **Acceptance criteria:** Over the full historical replay **and T14's ≥50-year
  forward projection**: the vault never goes negative; `sync_m2` never deadlocks
  against the caps (T29's regression, proven at the parameter values actually
  chosen); a patient claimant can clear the cheapest auction reserve within a
  stated number of epochs — record the number in `RESULTS.md` as a published
  fact about the artwork, not a growth target. Values are produced by the
  harness, not hand-written. *(The old criteria "Invariant M holds" and "assets
  turn over weekly" are removed: the first was rent-era arithmetic, the second
  was an engagement target, and Ruling A forbids justifying mechanisms by
  engagement.)*
- **TDD:** no (parameter selection); the invariants are asserted by T14's harness.
- **Validation:** `npx tsx chain/sim/index.ts --report --params chain/params.genesis.json`
  exits 0 with all invariants green.
- **Depends on:** T14
- [x] done
- Notes: Every value chosen from `chain/sim/sweep.ts` output; the full record,
  the rejects and the published facts are in
  [`chain/sim/RESULTS.md`](../chain/sim/RESULTS.md).
  **The sweep's first finding is that this was a narrow question.** 49 trials
  across four floors, five alphas and five ladders: **zero deadlocks, zero
  bound breaches, zero negative vaults.** Nothing here was a safety decision —
  every combination keeps the peg alive — so every choice is about what the
  machine *says*, which is the only ground Ruling A leaves.
  **The price ladder is stored as parts per million of the money supply, not
  as tokens** (`assets.genesisPricePpm`, 100 → 10000). A price in tokens is a
  constant measured against an exponentially growing M2 — the exact shape T29
  deleted from the sanity caps. As a fraction it holds forever, because every
  sync rescales all ten by the same factor. `init_asset` still takes absolute
  base units, so the multiplication happens once, at deployment, from one
  number; the test harness now derives its ladder the same way rather than
  carrying a second copy.
  **The ceiling law**, found by the sweep and then confirmed exactly: in the
  steady state the faucet pays out what the Fed printed, split among whoever
  registered, and a slot costs a fixed fraction of supply — so `C` diligent
  claimants each reach, in the limit, a `1/C` share of everything ever printed,
  and a slot costing `1/C` of supply is **exactly** out of reach for `C` of
  them. It is the honest replacement for the rent-era Invariant M and it is the
  scarcity the piece is about. The cheapest column supports about ten thousand;
  the masthead about a hundred.
  **A number that would have been a lie.** The harness's first answer to "how
  long to afford a column" was *two epochs* — true only at launch, because the
  Emperor's genesis hoard is half the money supply and goes out over two
  months. Publishing it would have been a false claim for everyone arriving
  later, which is the one bug class this project calls fatal. The harness grew
  a latecomer cohort, and the honest figures are 22 epochs at ten claimants,
  119 at a hundred, 1,290 at a thousand.
  **The finding that was not ticketed at all: the peg has a last number.**
  `supply = k × M2` and an SPL supply is a `u64`, so the largest M2 this coin
  can represent is **$18,446.7 trillion — 797× today's, about 107 years away**
  at the median month. Past it `sync_m2` fails the overflow check and, because
  the baseline only advances on success, fails forever after. **Same shape as
  T29's bug, and the one instance that cannot be designed away**: `k` and the
  six decimals are pinned by the width of a `u64`, and the token standard picks
  the width. Postponing it by a factor of a thousand in `k` buys another
  century and was rejected — it costs the headline ("one ENC for every $1,000
  of America's money"), 107 versus 217 years is not a difference an artwork
  notices, and **the ending is already graceful and already built**: T28's
  `retire` covers it, nothing is stranded, and the auctions go on at the last
  prices. It is now a test, so a future change to `k` cannot quietly shorten
  the life of the artwork, and it is stated plainly in the program README —
  which previously said the coin ends "ideally never", and no longer does.
  **Also worth knowing:** the vault legitimately dips *below* its own floor
  (47.47% in the historical replay). A burn lowers the vault's share as well as
  the supply, so a long enough contraction walks it under. The floor governs
  the faucet, never the burn — and what a visitor sees is the pot going to zero
  and staying there, which is the austerity beat arriving out of the arithmetic
  rather than out of a mechanism.
  **Two harness bugs found on the way, both of which printed plausible
  nonsense.** A cohort's `claimsIn` was being handed the chain's *absolute*
  epoch index (north of twenty thousand), so a latecomer told to arrive at
  "epoch 400" arrived immediately and the measured waits came out negative. And
  a ladder expressed in absolute tokens priced every 1959 slot above the entire
  money supply of the era, so the historical replay reported that nobody could
  ever afford anything. Both are the same lesson as T14's genesis-date artefact:
  **a simulation reports a number whatever you ask it.**

### T16: Switchboard feed — author it and prove immutability   [Status: mostly done 2026-08-10 | Model: opus]

> **DONE:** immutability proven live against Crossbar (one character → different
> feed hash; re-store → identical hash), production job authored and stored, both
> keyless sources verified to agree. Evidence and job committed at
> `chain/feeds/README.md` + `chain/feeds/m2sl.job.json`. **The hard gate is
> cleared — the artistic claim is safe to publish.**
> **REMAINING (expanded by the 2026-08-13 ticket audit — this is more than a
> polish item, and one part of it is load-bearing):**
> 1. **🔴 The date feed does not exist.** The committed `m2sl.job.json` is a
>    single job that extracts the *value* only — its regex matches a date but
>    captures group 1, the number. **T18's `Quote.release_date` therefore has no
>    source, and `retire` (T28) is only correct if that date comes from the
>    Fed's own metadata**: with a crank-time date instead, any bot cranking a
>    dead series keeps the coin alive forever and retirement measures apathy
>    rather than silence. This must be authored and its feed ID committed
>    **before T18 can meet its acceptance criteria.**
>    **Decision owed to Kai, with the groundwork done (2026-08-13).** Tested
>    against a live pull of `fredgraph.csv`, whose last row today is
>    `2026-06-01,23155.2`:
>    - **A Switchboard feed's value is a number**, and `2026-06-01` is not one.
>      A single "date feed" is therefore not possible — the date has to be
>      encoded numerically.
>    - **The CSV's date column is literally named `observation_date`** — the
>      month the figure describes, not the day the Fed published it. Today's
>      last observation is June while the date is August, so it lags the release
>      by about two months. **Calling it a release date in the code would be a
>      lie in the field name**, and the field is permanent.
>    - **Recommended mechanism — two extra feeds, combined on-chain.** Extract
>      the year and the month as separate numeric feeds, both end-anchored like
>      the value feed, then key off `year × 12 + month`. Verified against the
>      live CSV in single-line mode:
>      ```
>      ([0-9]{4})-[0-9]{2}-[0-9]{2},[0-9.]+\s*$   ->  2026   ✓
>      [0-9]{4}-([0-9]{2})-[0-9]{2},[0-9.]+\s*$   ->  06     ✓
>      year × 12 + month                          ->  24318  (next month 24319)
>      ```
>      That key is **monotone, Fed-sourced, and freezes when the series dies** —
>      which is exactly and only what `retire` needs. Rename `Printer.
>      m2_release_date` to something honest (`m2_period` / `m2_observation_key`)
>      if this is chosen.
>    - If a **true H.6 release date** is wanted instead, it needs a second
>      endpoint and its own keyless-source proof. More work, and it buys nothing
>      `retire` actually uses.
>
>    **The job is immutable forever once stored, so decide before storing.**
> 2. Add DBnomics as a median-aggregated second source (needs the
>    JSONPath-to-last-element shape tested; its `observations=1` does not limit
>    the response).
> 3. Mint the mainnet-queue feed **at mainnet launch** — *not* needed for T22,
>    which deploys to devnet against T17's devnet feed.
>
> **Two findings that bind later tickets:**
> 1. The job is **static forever** (its bytes are its identity), so it cannot take
>    a rolling date parameter. It fetches the full series and extracts the last row.
> 2. **The regex must be end-anchored.** A first-match pattern returns `286.6` —
>    M2 in January 1959. Against an immutable program that is unrecoverable.
- **Scope:** Author the keyless M2SL job (Fed Data Download Program CSV primary +
  `fredgraph.csv` as a second job, median-aggregated) using `regexExtractTask` —
  **all keyless government endpoints return CSV, not JSON**. Store via Crossbar to
  obtain the feed ID. Commit the **raw job JSON** so the feed is reconstructible
  from a text file forever (Crossbar's IPFS pin durability is undocumented).
  Encode the release date as a second feed in the same quote. Pin a known-good
  User-Agent and treat a **hang** as the block signature — Akamai blocks manifest
  as timeouts, not errors, and a spoofed Chrome UA is blocked while
  `python-requests` passes.
- **Files:** `chain/feeds/m2sl.job.json`, `chain/feeds/README.md`,
  `chain/scripts/fetch-m2.ts`.
- **Acceptance criteria:** **Prove the immutability claim first-hand** — store
  the job, note the feed ID, change one character, store again, confirm a
  different feed ID at a different PDA. Record the transcript in
  `chain/feeds/README.md`. **Nothing artistic may be published until this is
  verified.** The fetch script retrieves current M2SL and its release date from
  both sources and they agree.
- **TDD:** yes for the CSV parsing / release-date extraction.
- **Validation:** `npx tsx chain/scripts/fetch-m2.ts` prints matching values
  from both sources; `chain/feeds/README.md` records the two distinct feed IDs.
- **Depends on:** T2 — **not** T15. This ticket needs only the `chain/` workspace,
  nothing from the program or the parameter sweep. It carries the plan's hard gate
  ("nothing artistic may be published until the immutability claim is verified"),
  so **pull it forward and run it early**, in parallel with the toolchain track.
  It is listed here only to keep the oracle tickets adjacent.
- [ ] done
- Notes:

### T17: Stand the M2SL feed up on devnet   [Status: pending | Model: opus]
- **Scope:** Create the M2SL feed on **devnet**, where Switchboard runs real
  oracles that actually sign. Confirm it resolves and can be cranked by an
  arbitrary keypair. **No local Switchboard.** Per the environment split in
  Architecture (above), localnet uses the mock oracle exclusively and never talks
  to Switchboard. Ship **`chain enc feed-crank`** here — it posts a Switchboard
  update and stops. (The full `chain enc crank`, which also calls `sync_m2`, needs
  T18's on-chain read path and belongs there.)
- **Files:** `chain/feeds/m2sl.devnet.json`, `packages/cli/src/enc.ts`.
- **Acceptance criteria:** The devnet feed exists, returns the current M2SL value
  and release date, and a freshly generated keypair with airdropped devnet SOL
  can post an update to it — proving the feed is permissionless in practice, not
  just in principle. Never substitute the mock oracle for T18's acceptance.
- **TDD:** no (environment)
- **Validation:** `./stack enc feed-crank --cluster devnet` succeeds using a fresh keypair.
- **Depends on:** T16
- [ ] done
- Notes:

### T18: Switchboard on-chain read + crank   [Status: pending | Model: opus]
- **Scope:** Implement the real oracle path. **`require!` the feed ID explicitly**
  — the canonical-address constraint proves only "this is the canonical account
  for whatever feeds it contains," so an attacker could pass the canonical
  BTC/USD account and pass that check. Use the plain account read with our own
  **timestamp-based** staleness bound, **not** `QuoteVerifier::verify_account`,
  which is hard-capped at ~512 slots (~3.5 min) by the `SlotHashes` sysvar and
  would silently fail for a monthly feed. Check the signature count against our
  own quorum (`min_oracle_samples` may not be enforced by the deployed program).
  Add `chain enc crank` (T17's `feed-crank` plus a `sync_m2` call) and the
  standalone published `crank.ts`.
  **`Quote.release_date` must come from the Fed's own metadata** (the
  release-date feed T16's scope specifies — note the committed
  `m2sl.job.json` currently extracts only the value), **never from the quote's
  crank or signing timestamp** (2026-08-12 review). This is load-bearing for
  T28: with Fed-sourced dates, a discontinued-but-still-served series fails the
  `StaleRelease` guard, the last-successful-sync clock freezes, and `retire`
  fires correctly; with crank-time dates, any bot cranking a dead series keeps
  the coin "alive" forever and retirement measures nothing but apathy in both
  directions.
  **Schedule note:** one acceptance criterion needs a quote that genuinely aged
  on devnet, so budget a **calendar day** between cranking and asserting. T19–T23
  sit behind this — it is a wall-clock stall in the critical path, not a work
  estimate. Start the aging clock as soon as the read path compiles.
  **Scope corrections from the 2026-08-13 ticket audit — this ticket is bigger
  than "wire up a read":**
  1. **There is no Switchboard dependency in `Cargo.toml` yet.** Adding it, and
     whatever it drags in, is part of this ticket and is the most likely source
     of build-toolchain pain (see `chain/README.md`'s Docker notes).
  2. **The current non-mock `read_quote` is a stub returning
     `OracleUnavailable` and discarding both its arguments.** Nothing about the
     real path exists to extend — it is written from scratch here.
  3. **`Quote` currently carries only `m2_value` and `release_date`.** If the
     signature-quorum check needs more (signer count, oracle timestamps), the
     struct grows here and `sync_m2`'s call site grows with it.
  4. **The `mock` feature must keep working unchanged.** It is how every other
     suite runs and how T19/T20 are developed; the environment split is
     deliberate and absolute. Do not let the real path's types leak into the
     mock build.
  5. **T16's date feed is a prerequisite** and does not exist yet — see T16's
     REMAINING block. `Quote.release_date` has no source until it is authored,
     and `retire`'s correctness depends on it being Fed-sourced.
- **Files:** `chain/programs/emperors-new-coin/src/oracle.rs` (real impl),
  `chain/programs/emperors-new-coin/Cargo.toml` (add the Switchboard dep),
  `chain/scripts/crank.ts`, `packages/cli/src/enc.ts`, `chain/tests/switchboard.ts`.
- **Acceptance criteria:** **All of these must be proven against devnet**, where
  real oracles sign real quotes. The real read path executes end-to-end against a
  live devnet quote; a quote for the **wrong feed ID is rejected**; **a quote
  cranked days earlier is still readable** (this is our actual access pattern and
  the one thing the docs did not settle — it needs a quote that genuinely aged on
  devnet, so allow a day between cranking and asserting); a quote below our
  signature quorum is rejected.
- **TDD:** yes
- **Validation:** `./stack test test-switchboard-devnet` (Anchor.toml `[scripts]`
  entry running the suite against devnet — `./stack test` already passes
  `--skip-local-validator`, which matters here because plain `anchor test` spawns
  its own validator and would bypass the cluster entirely).
- **Depends on:** T17
- [ ] done
- Notes:

### T19: ENC page — read-only state   [Status: **DONE 2026-08-13** — validation re-run by the orchestrator, page loaded and read in a real browser | Model: sonnet]
- **Scope:** Live M2 readout, total supply, vault balance and share with the floor
  marked, next H.6 release countdown (fourth Tuesday, 1:00pm ET), and the ten
  assets with prices interpolating every slot. Works with no wallet connected.

  **Rewritten 2026-08-13 (ticket audit).** The original scope said "add the
  account decoders and `currentPrice`/`rentOwed` to chain-kit." Both halves were
  wrong and following it would have broken the build:
  - **🔴 `rentOwed` does not exist.** Ruling A removed rent; T30 deleted the
    code. There is no holding cost to display.
  - **🔴 Decoders must NOT go in `chain-kit`.** The kit is copied wholesale into
    unrelated repos and may not know ENC exists. **T23 enforces this by grep and
    would fail.** Everything ENC-specific belongs in **`packages/enc`**, which
    already documents exactly this in its `src/index.ts`. `chain-kit` stays
    generic; only its `programs.json` name→address map may mention the coin.

  **What to actually build.** Add to `packages/enc`: the IDL
  (`src/idl/emperors_new_coin.ts`), account decoders (`src/accounts.ts`), and
  PDA derivations. `math.ts` **already exists** and mirrors the program — reuse
  it; do not rewrite the arithmetic. Mirror in BigInt with the same truncating
  integer division.
  - **Accounts to read:** `Config` (`[b"config"]`), `Printer` (`[b"printer"]`),
    the ENC mint (`[b"mint"]`, for `supply`), the vault ATA (owner `[b"vault"]`,
    `allowOwnerOffCurve`) for the vault balance, the ten `Asset` PDAs
    (`[b"asset", [i]]` — one `getMultipleAccounts`), the escrow ATA (owner
    `[b"escrow"]`) for total ENC locked in bids, and `FaucetEpoch`
    (`[b"epoch", u64le]`) for epochs N and N−1. **Treat a missing `FaucetEpoch`
    as pot 0 / registrants 0** — it is created lazily by the first claimer.
  - **Derived per asset:** current price from
    `PriceCurve{price_from, price_to, interp_start, interp_end}.price_at(now)` —
    this is both the displayed price *and* the auction reserve. `holder == vault
    PDA` renders as "the Emperor holds it", not as an address.
    `high_bidder == PublicKey.default` means no bids. Show time remaining to
    `term_ends_at`, and once past it, which of `settle_auction` or `roll_term`
    applies (`high_bid > 0 && high_bid >= price_at(now)`).
  - **Derived globally:** `floor_amount(supply, floor_bps)` with the vault's
    share against it; `faucet_pot(...)` for a not-yet-open epoch;
    `epoch_of(now, epoch_seconds)` and the next boundary; the honest supply
    drift `mint.supply − printer.target_supply` (invariant is `supply ≥ k × M2`,
    never `=`); and the retirement clock `now − printer.last_sync_at` against
    `retirement_silence_seconds`.
  - **Render the Gazette front page** (Ruling D / T31): the ten slots as
    newspaper columns with their filed copy, spiked columns as redaction bars.
    The page **must state that the "only the last word is visible" serial
    framing is presentation, not secrecy** — the chain is public. Same
    disclosure family as the melting balance.
  - **Only `Synced`, `Claimed` and `Retired` emit events.** The auction
    instructions emit `msg!` logs only, so auction history needs account-state
    diffing or log parsing — do not design a UI that assumes an event feed.
- **Files:** `apps/web/src/coins/enc/{Printer,AssetGrid}.tsx`, `enc.css`,
  `packages/enc/src/accounts.ts`, `packages/enc/src/idl/emperors_new_coin.ts`.
  **Not `packages/chain-kit`.**
- **Acceptance criteria:** Prices visibly tick without a refresh; account changes
  push through the websocket subscription; the page renders with no wallet; the
  countdown is correct across a DST boundary; and
  `grep -riE "enc|emperor|m2" packages/chain-kit/src packages/chain-react/src`
  still returns nothing but `programs.json` and false-positive substrings.
- **TDD:** yes for countdown and price math; no for presentation.
- **Validation:** `npm run test --workspace @badcode/enc`; `npm run build`;
  manual check at `/coins/enc` against localnet.
- **Depends on:** T6, and **T31** (the `Asset` layout must be final before the
  frontend decodes it). **Not blocked on T18** — build and demo against
  localnet with the `mock` feature, where `set_mock_m2` drives the peg. T18 only
  changes where the numbers come from, not what the page renders.
- [x] done — 2026-08-13. Orchestrator re-ran the validation independently:
  `npm run test --workspace @badcode/enc` **79 passing** (including a five-year
  H.6 sweep asserting every release still reads 1pm Tuesday in New York, across
  both DST boundaries), `npm run build` green, `./stack check` green across
  every workspace, and the portability grep over `chain-kit`/`chain-react`
  returning nothing but the generic `programs.json` entry. **Loaded
  `/coins/enc` in a real browser over CDP and read the rendered page**: the
  printer, the `supply ≥ k × M2` drift line, the vault's 77.61% against its 50%
  floor, the faucet correctly explaining that no epoch account exists yet
  *because nobody has claimed*, the retirement clock, and all ten Gazette
  columns — a filed column, a spiked one rendering as redaction bars, an
  under-reserve standing bid, and the Emperor's default copy on the rest.
  Console clean apart from a missing `favicon.ico`. Both required disclosures
  are present and in voice. **Review finding logged against T22:** slot names
  now exist both on-chain and in `AssetGrid`'s `FURNITURE` array, and Jack's
  sheet must reach both or the page will caption a column the chain does not
  carry.
- Notes (executor, 2026-08-13 — built and verified in a real browser against
  localnet with the `mock` build; validation run: `npm run test --workspace
  @badcode/enc` **79 passing**, `./stack check` green, `npm run build` green,
  the T23 grep clean. **Judgement calls the ticket did not settle:**
  1. **`packages/enc` gained four modules, not two.** `accounts.ts` (addresses,
     Anchor decoders, the two SPL decoders) and `idl/emperors_new_coin.ts` as
     specified, plus `view.ts` (decoded accounts + a timestamp → what a
     component renders), `format.ts` (base units, M2, shares, countdowns) and
     `h6.ts` (the release calendar). The rule they enforce: **no arithmetic and
     no date logic in a component**, so all of it is testable without a browser.
     `math.ts` was reused unchanged and nothing re-derives it.
  2. **The IDL module is a re-export, imported by relative path rather than the
     `@chain/*` alias.** That alias is a tsconfig path and therefore has to be
     declared twice per consumer; `@badcode/enc` is now compiled by four
     toolchains (the web app's tsc + vite, its own vitest, `chain`'s tsc, the
     simulation's vitest) and a relative path is understood by all four with
     nothing to keep in step. Nothing is hand-written — `./stack build` still
     owns the file.
  3. **`chain/tsconfig.json`'s `module` moved es2022 → esnext.** The simulation
     imports `@badcode/enc`, which now reaches `@badcode/chain-kit`, whose
     `registry.ts` loads JSON with an import attribute — syntax es2022 rejects
     and every runtime here already accepts. One line, commented in place.
  4. **The mint and the two token accounts are decoded by fixed offset in
     `accounts.ts`**, rather than adding `@solana/spl-token` to the browser
     bundle. `getTokenSupply`/`getTokenAccountBalance` were rejected for a
     different reason: they are RPC calls, not subscriptions, and the page has
     to move when the chain moves.
  5. **The page runs on the validator's clock, not the browser's.** A local
     validator's unix time drifts behind wall time, and every price and epoch
     index is derived from `Clock::get()`; `useChainClock` reads the chain's
     time, keeps the offset and ticks locally. Same trap the test harness
     documents, one layer up.
  6. **Slot names are frontend furniture and provisional** — Masthead, Leader,
     Editorial … Classified, dearest to cheapest. Only the two ends are settled
     by Ruling D; the eight between are presentation and cost nothing to change
     when Jack's sheet lands at T22. The page says the names arrive later and
     that the ladder is already fixed.
  7. **The Emperor's default copy (`copy_len == 0`) is written in the
     frontend**, not on-chain, and reads as a standing notice rather than an
     empty column. A column with copy from an earlier tenant is labelled
     "standing from an earlier edition", which is the distinction `copy_filed`
     exists to make.
  8. **Gazette prices render at two decimal places with the exact figure on
     hover.** At this scale the price moves by whole ENC a second, so the tick
     is visible without setting a headline in micro-units.
  9. **Shares of the money supply are printed to four decimal places.** Two
     rendered the cheapest column — one basis point of everything — as `0%`,
     which deletes the joke rather than rounding it.
  10. **T31's judgement call #2 asked whether a spiked column the Emperor holds
      renders oddly. It does not.** Slot 08 is exactly that on the test ledger:
      redaction bars, "struck by the editor, this edition", holder "The
      Emperor". Nothing to fix.
  11. **A missing escrow ATA or `FaucetEpoch` reads as zero, never as an
      error** — both are created lazily, so absence is the normal state and the
      page says so in words ("no epoch account exists yet today … it is created
      by whoever claims first").
  12. The wallet button stays but does nothing yet; the page states plainly that
      everything on it is readable without connecting. T20 fills it in.
- Notes (verification, same run): prices tick every second in the browser with
  no refresh (all ten columns move); an account change pushes through the
  websocket subscription — `roll_term` sent from a script moved a slot's term
  number and standing-bid state in the open page without a reload. Zero console
  errors at 1440px and at 390px. The front page rendered from the state the
  suites leave behind: filed copy on one slot, a spiked column on another, live
  bids, and one slot whose standing bid had fallen **under the reserve** since
  it was placed — which is the coin's whole thesis rendering itself.

### T20: ENC page — wallet actions and the melting balance   [Status: **DONE 2026-08-13** — validation re-run by the orchestrator; **the Phantom two-wallet run-through is still owed a human**, see the checkbox | Model: sonnet]
- **Scope:** Connect, claim (showing whether it's the welcome grant, a share of
  yesterday's pot, or zero — and why), and the auction actions. Errors surface a
  human cause, successes an explorer link. Plus the melting balance: the
  displayed ENC decays continuously while the chain holds the true number, with a
  quiet discoverable tell (hover/tap reveals the truth). Copy per `docs/voice.md`.

  **Rewritten 2026-08-13 (ticket audit).** The original scope listed
  "force-buy, rent owed, settle rent" — the rent/foreclosure machinery Ruling A
  deleted and T30 removed from the tree. **None of those instructions exist.**
  The actions to wire are the ones the program actually has:
  - **`claim(epoch)`** — the faucet. The UI must explain the *register today,
    collect tomorrow* shape, because it is the single most confusing thing here:
    a first-ever claim registers you and pays only the welcome grant; the share
    of the pot arrives on the *next* claim. Read `Player.last_registered_epoch`
    to say which case the user is in, and say plainly when the vault is below
    its floor and the faucet pays nothing at all.
  - **`place_bid(index, amount)`** — escrows the bidder's own ENC. Must beat both
    the current price (the reserve) and the standing high bid strictly. Topping
    up an existing bid transfers only the difference.
  - **`withdraw_bid(index)`** — refused only while the bid is both the standing
    high bid *and* from the current term; a bid from any earlier term is always
    withdrawable. Surface that distinction, because "my money is stuck" is the
    obvious support question and the answer is usually "it isn't."
  - **`settle_auction(index)` / `roll_term(index)`** — both permissionless and
    callable by anyone once `term_ends_at` passes. Offer whichever the asset
    state qualifies for; `roll_term` needs **no signer at all**.
  - **`mint_certificate(index, term)`** — anyone may pay for it, and it always
    lands in the holder's wallet, never the caller's. The Emperor gets no
    receipt (`holder == vault` is refused).
  - **`file_copy(index, text)`** (T31) — the tenant writes their column. **Once
    per term**, so the UI must make the finality obvious *before* submission,
    not after. Show the redaction marker for a spiked column.
  - **Do not build a "buy" button.** There is no purchase instruction — the only
    routes to ENC are the faucet and whatever secondary market strangers make.
    Ruling C is a posture the page states, not a feature it offers.
- **The melting balance survives Ruling A unchanged**, and its explanation
  changes: nothing decays on-chain, and there is no demurrage. The balance sits
  still while everything priced against the money supply rises, so the *real*
  loss is in purchasing power. The page renders the fall; the chain holds the
  truth; a hover reveals it. Cosmetic only, no on-chain state, and disclosed.
- **Files:** `apps/web/src/coins/enc/Wallet.tsx`, `AssetGrid.tsx` (extend), `enc.css`.
- **Acceptance criteria:** Full loop against localnet with Phantom, two wallets:
  claim in epoch N → claim again in N+1 and receive a share → `place_bid` →
  second wallet outbids → first wallet withdraws its escrow **in full** → term
  ends → `settle_auction` from a third, uninvolved wallet → certificate lands in
  the winner's wallet → tenant files copy once and is refused twice.
  Rejected transactions show a readable cause, not a raw program error code —
  map at minimum `BidBelowReserve`, `BidNotHighEnough`, `BidIsStanding`,
  `StaleBidOutstanding`, `TermNotEnded`, `NoQualifyingBid`,
  `AlreadyClaimedThisEpoch` and `WrongEpoch`. The melting number is always one
  interaction away from the truth and involves no on-chain state.
- **TDD:** no (UI wiring; logic is tested in the program and `@badcode/enc`)
- **Validation:** `npm run build`; manual two-wallet run-through on localnet.
  **Epoch and term lengths are `Config` fields** — a test ledger can be
  initialised with short ones to reach these cases without waiting a month.
- **Depends on:** T19
- [x] done — 2026-08-13, **with one criterion explicitly outstanding.**
  Orchestrator re-ran the validation independently: `npm run test --workspace
  @badcode/enc` **133 passing**, `./stack test test-actions` **15 passing** on a
  fresh ledger, `./stack check` green across every workspace and **leaving the
  working tree clean**, `npm run build` green, the portability grep still
  returning nothing but `programs.json`, and the page loaded over CDP with a
  **clean console** and correctly showing no buttons before a wallet connects.
  - **🔴 STILL OWED A HUMAN: the two-wallet Phantom run-through.** A browser
    extension cannot be driven from here. The executor proved every instruction
    from a real browser through an injected Phantom-shaped provider holding a
    throwaway key, which establishes the wiring, the account maps, the amounts
    and the error mapping — but **not Phantom itself**. That is a genuine gap in
    this ticket's acceptance, carried forward to **T23**, not quietly closed.
  - **Corrected by the orchestrator:** the melt rate was 5%/yr and is now 6%.
    See the Discovered Issues Log — the research's 5% is an order of magnitude,
    and M2 has actually grown 6.73%/yr since 1959.
- Notes (built 2026-08-13):
  - **The logic is in `packages/enc/src/actions.ts`, not in components.** Three
    things live there: every instruction's account map, every `require!` a
    person can trip by clicking mirrored so a button can grey itself out and say
    why, and the program's refusals in English. `Counter.tsx` and `Wallet.tsx`
    decide nothing; they render what those functions return. 49 unit cases.
  - **`chain/tests/actions.ts` (`./stack test test-actions`) is the substitute
    for the Phantom run-through**, and it exists because the acceptance criteria
    describe something no automation here can drive. It sends every instruction
    against a live validator through the *same* account maps and checks them
    against the *same* predictions the page uses, so a derivation that drifts
    fails a suite rather than a user's transaction. 15 cases, the ticket's whole
    loop in order.
  - ~~**The melt rate is 5% a year**, sourced to
    `research/2026-08-12-enc-tokenomics/README.md` — the long-run growth of
    M2.~~ **Corrected to 6% by the orchestrator, 2026-08-13.** The research's
    5% is an order-of-magnitude figure in a comparison against 150%/month rent;
    M2 has actually compounded at **6.73%/yr since 1959** and above 5.6% on
    every multi-decade window. See the Discovered Issues Log. The rest of this
    note stands: every price on the page is a fixed share of the money supply,
    so that is honestly what a balance sitting still loses, and it is stated on
    the page rather than buried.
  - **The melt clock starts when the page first sees the balance**, and
    re-anchors whenever the balance changes. The chain does not record when a
    wallet acquired anything and neither do we, so any other anchor would be an
    invention. Six decimals are rendered because the last two are what visibly
    fall — about two micro-ENC a second on a thousand ENC.
  - **Hover and tap are separate states.** A mouse user who hovers and then
    clicks was toggling the reveal straight back off; the click now pins it.
  - **Two-step filing.** Once per term is the design, so the button says
    "File it" and then "Yes — file it, finally", with the finality spelled out
    *before* submission rather than explained afterwards. Byte count, not
    character count, is shown live.
  - **No buy button, stated twice** — once to a visitor who has not connected
    and once to one who has. Ruling C is a posture the page says out loud.
  - **Certificates are subscribed to, not discovered by failing.** A second
    `mint_certificate` fails with "account already in use", a raw system-program
    error with no good sentence, so the page reads the cert PDA's existence
    instead. Those ten subscriptions are wallet-gated: T19's read-only page must
    not pay for T20's buttons.
  - **`roll_term` needs no signer but still needs a wallet to pay the fee.** The
    page says the instruction asks nothing of anyone; it does not pretend the
    transaction is free.
  - **What a human still has to click.** Every instruction was driven from a
    real browser against localnet — claim, place_bid, withdraw_bid,
    settle_auction, roll_term, mint_certificate, file_copy, plus a refusal
    rendering its mapped sentence — but through an injected Phantom-shaped
    provider holding a throwaway localnet key, because a browser extension
    cannot be automated here. **What is unverified is Phantom itself**: its
    approve/reject dialogs, its own error surfaces, and the reconnect/account-
    change paths its adapter emits. That is the residual for T23.
  - **The 12-second test-ledger term is nearly unbiddable from a browser** and
    that is the ledger's fault, not the page's: notification lag plus a term
    shorter than it leaves a window of a few seconds. Irrelevant at the shipped
    30-day term, but it is why the browser bid needed a script keeping a slot on
    a fresh term.

### T21: Documentation — toolchain, coin, canon   [Status: **DONE 2026-08-13** — validation re-run by the orchestrator; every claim-ledger figure independently recomputed from the FRED series | Model: sonnet]
- **Scope:** `chain/README.md` (install → run → deploy → **how to add coin #2**).
  `docs/coins/emperors-new-coin.md` — the public design including the honest trust
  statement: what we can say ("we removed ourselves from the loop") and what we
  must not ("nobody can affect this but the Fed"), naming the Switchboard
  queue-authority residual explicitly, stating the true supply invariant as
  `supply ≥ k × M2`, and **quoting the scanner warning as a selling point** —
  ENC genuinely is arbitrarily inflatable, that is the entire coin, and the
  PDA/non-upgradeable explanation sits beside it rather than apologising for it.
  Resolve the open thread at
  `docs/stories/magic-money-tree/emperors-new-coin.md:151`.

  **Post-rulings requirements (2026-08-13 ticket audit) — the docs describe the
  coin as it is now, not as first designed:**
  - **The trust statement is two-part, never one.** *No key over the money; one
    pen over the words.* T31 puts an editor key on the chain, so **"no admin
    key" unqualified is now false and must not appear anywhere in the docs.**
    State the pen's blast radius plainly: it can redact ten columns a month and
    cannot move a token. If T31 has landed, this is the same claims surgery its
    scope names — do not undo it here.
  - **No rent, no foreclosure, no holding cost, no permanent delegate**
    anywhere in the docs. Assets change hands by scheduled auction (Ruling A).
    The old rent-era architecture diagram in this plan is marked SUPERSEDED and
    is a historical record — do not narrate it as live.
  - **It runs forever**, with the one self-proving exception: a permissionless
    `retire` after `retirement.silenceSeconds` of oracle silence (Ruling B).
  - **Closed loop by posture** (Ruling C): BadCode seeds no liquidity and sells
    no ENC, ever. The faucet is the only route in that we control. Say the
    posture; do not claim ENC *cannot* be traded — anyone may pool a plain SPL
    token and we neither prevent it nor point at it.
  - **State the peg horizon rather than burying it** (T15's ruling): the peg
    can count to $18,446.7 trillion of M2, roughly 107 years out. It is a
    better sentence than a silence.
  - Document the economic parameters by *what they say*, sourcing
    `chain/sim/RESULTS.md` — the Emperor keeps half the money forever; a
    thousand ENC is a million dollars of the money supply and buys you nothing;
    the cheapest column is one basis point of all the money there is.
- **Already done — do not redo:** the toolchain is in `CLAUDE.md`'s repo map,
  and `chain/README.md` already carries the portability contract and the
  Docker/`io_uring`/dual-IDL gotchas. Extend both; do not rewrite from scratch.
- **Files:** `chain/README.md`, `docs/coins/emperors-new-coin.md`,
  `docs/stories/magic-money-tree/emperors-new-coin.md`, `CLAUDE.md`.
- **Acceptance criteria:** A reader goes from clean WSL to a running localnet ENC
  using only `chain/README.md`. **No claim in the docs is unsupported by code** —
  in particular the supply invariant and the trust statement.
- **TDD:** no (docs)
- **Validation:** Follow `chain/README.md` from a clean shell; every command runs.
- **Depends on:** T20
- [x] done — 2026-08-13. Orchestrator re-ran the validation and, because this
  is the claims ticket, **independently recomputed every figure in the claim
  ledger straight from the FRED M2SL series** rather than reading the table.
  All of them hold: 810 observations / 809 steps, rose 758 · fell 49 ·
  unchanged 2; median month **+0.522%**; biggest rise **+6.42%** (Apr 2020);
  biggest fall **−1.40%** (Mar 2023); the 2022–23 contraction **−4.82%**,
  **$1,049.7bn**, Mar 2022 → Oct 2023; the longest run of consecutive falls
  **nine**, Aug 2022 → Apr 2023; and the peg horizon **$18,446.7 trillion**,
  **796.7×** today, **106.9 years** at the median month. `./stack check` green
  across every workspace and leaving the tree clean, `npm run build` green.
  - **🔴 One claim in this repo did not survive the ticket, and it had spread.**
    The claims standard in the decision doc said M2 fell "13 in a row in
    2022–23". It did not — the longest run in the entire 1959–2026 record is
    **nine**. The wrong figure had already reached `settle_auction.rs` and the
    plan's T12 notes. Corrected in all three, visibly rather than quietly.
    Independently confirmed here.
  - **Orchestrator fix on top:** T21 removed `--features mock` from `./stack
    help`'s `test` line but left it on `build`, where the advertised
    `./stack build [<program>] [--features mock]` is precisely the form that
    fails — cargo features are per-package and `counter` has no `mock`. Ran it;
    it dies. The help now states that naming the program is required, and why.
- Notes:
  - **Built 2026-08-13.** `docs/coins/emperors-new-coin.md` is new and is now the
    public design of record: the machine instruction by instruction, the
    parameters by what they *say*, the two-part trust statement, the Switchboard
    queue-authority residual, the scanner warning quoted as a selling point, the
    peg horizon stated rather than buried, and a **claim ledger** — every factual
    figure with the thing that proves it. `chain/README.md` gained a clean-shell
    install path, a tests section with the real suite names, a deploy section and
    a **how to add coin #2** walkthrough. Both existing READMEs were extended,
    not rewritten.
  - **Every M2 figure was re-derived at this ticket** from
    `chain/sim/m2-history.csv` rather than quoted from a brief. Confirmed exactly:
    median month +0.522%; rose 758/809 (93.7%), fell 49 (6.1%), 2 unchanged;
    largest month +6.42% (2020-04); largest fall −1.40% (2023-03); CAGR 6.73%
    since 1959 and 6.28% trailing 20y; 770 of 774 three-year windows up, worst
    −0.54%, median 1.222×; 2022–23 drawdown −4.82% / $1,049.7bn; peg ceiling
    $18,446.7tn = 797× today = **107 years** at the median month; genesis 22.176bn
    ENC; cheapest column 100 ppm = 1.00 bps = 2,217,610 ENC; welcome grant
    1,000 ENC = $1,000,000 of M2. **One figure did not survive** — see the
    Discovered Issues Log entry on "thirteen in a row".
  - **`MELT_ANNUAL_BPS = 600` is confirmed correct.** All five CAGR windows in its
    justification comment reproduce exactly (6.73 / 5.62 / 6.25 / 6.32 / 6.08%).
    One precision note recorded in the log: "every multi-decade window is above
    5%" is true of those five windows and of every 30-year and 40-year window,
    but **not** of every 20-year window — 28 of 570 fall below 5%, the weakest
    being 4.88% (1987-01 → 2007-01). The constant is unaffected; the sentence
    should not be generalised past the table it sits under.
  - **Two documented commands did not work and were fixed** — see the log.
  - **Claim surgery applied** to the program README (`supply ≥ k × M2` now stated
    where the `=` headline was; "the Emperor's treasures" and "the flag passes to
    them" replaced with Gazette vocabulary per Ruling D; the 2022–23 sentence
    re-derived; an explicit "the oracle is not built and the authority is not
    burned" note added at the top where the blanket disclaimer sat 160 lines
    away), to `CLAUDE.md` (which stated the trust claim in the forbidden one-part
    form and did not link the rulings), to `chain/feeds/README.md` (present tense
    on an unwired feed), and to `packages/cli/src/enc.ts` (an error string
    pointing at `./stack enc crank`, a command that has never existed).
  - **Left for T22/T23, deliberately:** the "flags" vocabulary still in Rust doc
    comments (`state.rs`, `math.rs`, `place_bid.rs`, `retire.rs`, `errors.rs`) and
    the `supply = k × M2` form in `state.rs:141` / `lib.rs:9` — **those two reach
    the IDL**, so changing them republishes a committed artifact, which is T22's
    territory and not a docs ticket's. Also left: the plan's own §"Key decisions"
    (~L373–475) and §"Interfaces" (~L620–680), which still narrate rent, `Invariant
    M` and the permanent delegate as live design without the SUPERSEDED banner the
    §"The ENC machine" section carries.

### T22: Devnet deploy + burn the upgrade authority   [Status: pending | Model: opus]
- **Scope:** Deploy to devnet against the feed T17 already created, run
  `initialize` + ten `init_asset` calls with the T15 parameters, then **burn the BPF upgrade
  authority to `None`**. Publish the feed hash, the raw job JSON, and the
  standalone crank script. Flip the timeline node to `live` and update
  `diorama.test.ts` accordingly.

  **What becomes permanent here (2026-08-13 ticket audit).** This is the point
  of no return, so the things the burn freezes are listed explicitly:
  1. **The ten slot names and image URIs — Jack's Gazette slot sheet.** T31
     builds the mechanism with placeholder names; *this* ticket is where the
     real ones are set, and after the burn they cannot be changed. **Do not run
     `init_asset` on devnet-as-mainnet-rehearsal without Jack's sheet in hand.**
     **🔴 The names now live in two places (noted at T19's review,
     2026-08-13).** `init_asset` writes a name into each asset's Token-2022 NFT
     metadata, *and* `apps/web/src/coins/enc/AssetGrid.tsx` carries a
     `FURNITURE` array of ten presentation names (currently Classified →
     Masthead, cheapest first, and clearly marked provisional in place).
     **Jack's sheet must land in both, in the same commit**, or the page will
     confidently caption a column with a name the chain does not carry — and
     after the burn only the page can be corrected. Either sync the two
     deliberately at this ticket, or make `AssetGrid` read the name from the
     NFT metadata and delete the array. The second is better and is a small
     job; decide before deploying, not after.
  2. **The editor key** (`Config.editor`, set at `initialize`). Rotatable via
     `pass_the_pen` afterwards, so key loss is survivable — but the initial
     holder is a decision, not a default. Do not use a throwaway keypair.
  3. **The genesis price ladder**, as absolute base units: multiply
     `assets.genesisPricePpm` by the bootstrap supply (`GENESIS_M2_VALUE × k`),
     cheapest slot first. The *ratios* are what hold forever — every sync
     rescales all ten by the same factor.
  4. **`retirement.silenceSeconds` and the sanity cap** — both `Config` fields,
     both unchangeable after the burn.
- **Split permitted (recommended).** Deploying and burning need not be one act.
  An **upgradeable devnet deploy** to exercise T23's loop for real, followed by
  the burn once everything is proven, is strictly safer and costs nothing but a
  second deploy. **The burn is irreversible and must be a human decision** — an
  agent may prepare and verify it, and must not execute it unprompted.
- **Files:** `packages/chain-kit/src/programs.json`, `chain/feeds/m2sl.devnet.json`,
  `apps/web/src/home/timeline.ts:114`, `apps/web/src/home/atlas/diorama.test.ts:16`,
  `docs/coins/emperors-new-coin.md` (addresses).
- **Acceptance criteria:** `solana program show <id> --url devnet` reports
  **Authority: none**. The mint authority is the vault PDA and the freeze
  authority is `None`. A stranger running only the published crank script from a
  clean checkout with a fresh keypair can advance the feed and call `sync_m2`.
  Every published claim is verified by RPC, not assumed.
- **TDD:** no (deployment) — but re-verify every claim by RPC.
- **Validation:** `solana program show <id> --url devnet`;
  `spl-token display <mint> --url devnet`;
  `npx tsx chain/scripts/crank.ts --cluster devnet` from a clean checkout;
  `npm run test --workspace @badcode/web`.
- **Depends on:** T21
- [ ] done
- Notes:

### T23: End-to-end verification   [Status: pending | Model: opus]
- **Scope:** Prove the whole feature works on devnet through the real UI, and that
  the toolchain is genuinely reusable.
- **Files:** none (verification only); append findings to the Discovered Issues Log.
- **Acceptance criteria:**
  1. Full gates green: `./stack check` (typecheck + unit tests) and `npm run build`
     at repo root; `./stack cargo test -p emperors-new-coin --lib`; and every
     `./stack test test-*` suite.
  2. Against **devnet**, through `/coins/enc` in a browser with Phantom, the
     **auction** loop (rewritten 2026-08-13 — the original text described the
     rent/foreclosure machinery Ruling A deleted): connect → claim from the
     faucet in epoch N → collect in epoch N+1 → `place_bid` on a slot → a second
     wallet outbids → the first wallet `withdraw_bid`s its escrow back in full →
     the term ends → anyone (a third wallet, not the winner) calls
     `settle_auction` → the winner receives the tenancy and `mint_certificate`
     puts the press clipping in their wallet → the tenant calls `file_copy`
     once and is refused a second time → the editor `spike`s that column and is
     refused a second spike in the same term → the term rolls.
     **The signature invariant is the thing being proven: no token leaves any
     wallet without its owner's signature, at any point in that sequence.**
  3. A real `sync_m2` executes against the live devnet Switchboard feed and the
     resulting supply equals `k × M2` for the current published figure.
  4. **Toolchain reuse check:** scaffold a throwaway second program and page from
     `chain/README.md`'s "add coin #2" section and confirm no plumbing had to be
     written — only a Rust program and a page component. Delete it afterwards.
  5. **Portability check — enforce the contract by grep, not good intentions:**
     `grep -riE "enc|emperor|m2" packages/chain-kit/src packages/chain-react/src`
     and `grep -riE "enc|emperor|m2" packages/chain-cli/src`
     return **no ENC references** (allow for false positives on substrings like
     "encode"/"encrypt" — review, don't just count). Then prove it for real:
     copy `chain/`'s scaffold files, `packages/chain-kit`, `packages/chain-react`
     and `packages/chain-cli` into a scratch directory
     outside this repo, delete every ENC-specific path listed in the Portability
     contract, and confirm the remainder typechecks with no dangling imports.
     A second, non-token BadCode project will lift exactly this set.
- **TDD:** no (verification)
- **Validation:** All commands above pass; the browser walkthrough is completed and
  transaction signatures recorded in the Notes.
- **Depends on:** T22
- [ ] done
- Notes:

---

### T24: Containerise the toolchain   [Status: DONE 2026-08-11 | Model: opus]

Kai's call: no hard dependency on host binaries. `chain/docker/Dockerfile` +
`chain/docker-compose.yml` build a pinned image (asserting all four versions at
build time) and run a two-service stack: a long-lived `validator` publishing
8899/8900 to the host, and a throwaway `toolchain` sharing its network namespace
so `127.0.0.1:8899` means the same thing inside and out.

`packages/chain-cli/src/runner.ts` is the whole seam — `runInChain` dispatches to
`docker compose run` or the host, and `CHAIN_RUNNER` forces either. Nothing else
in the CLI branches on it. `docker/.env` is regenerated from versions.json before
every docker command, so the image cannot drift from the pins unseen.

Findings, all now pinned or asserted:
- **Docker's seccomp profile blocks io_uring, which Agave 3.x asserts on.** A
  fresh ledger dies with `assertion failed: io_uring_supported()` and a trace
  that never mentions Docker. `seccomp:unconfined` on the validator service only.
- Ubuntu 24.04 (glibc 2.39) means Anchor's **prebuilt** binary works — no source
  build, which is why the image takes ~10 minutes once rather than ~40.
- `anchor test` starts a second validator on the running one's port. `chain test`
  now passes `--skip-local-validator`; tests must assert on movement, not values.
- Switching runners changes the deploy wallet, so existing programs refuse to
  upgrade ("Upgrade authority mismatch"). `chain reset` is the fix.
- `chain reset` wiped the ledger *and* the wallet's balance, so the next deploy
  failed with "no record of a prior credit". Reset now refunds and redeploys.

### T25: The counter program — a harness for the whole loop   [Status: DONE 2026-08-11 | Model: opus]

`chain/programs/counter` (PDA per wallet, `initialize`/`increment`/`reset`),
`chain/tests/counter.ts` (5 tests), and `apps/web/src/chain-demo/CounterPage.tsx`
at `/dev/counter`. Deliberately not a coin: it is the only thing that can prove a
copy-out landed in a project that has nothing to do with tokens.

The type pipeline is the point. `chain build` publishes IDL **and** generated
TypeScript into committed `chain/idl/`; the app imports both through the new
`@chain/*` alias (declared in tsconfig.base.json *and* vite.config.ts, because
Vite does not read tsconfig paths). Since the IDL carries `address`, **nothing
hardcodes a program address**.

Verified live, not asserted:
- `STEP` 1 → 2, rebuild, redeploy → the on-chain delta changed 1 → 2, same
  address, state preserved.
- Added `updated_at: i64` → it appeared in the generated types as `updatedAt`,
  carrying the Rust doc comments; the app now reads it.
- **Deleted the field → `tsc` failed** at the exact line. That is the workflow
  Kai asked for: a backend struct change fails the frontend build.
- A pre-existing account then fails to decode with a raw `ERR_OUT_OF_RANGE`; the
  page catches it and names `chain reset` as the fix, since the error does not.
- Browser (real Chrome, CDP) at `/dev/counter`: renders, 0 console errors,
  cross-origin RPC to the container reaches the validator, program confirmed
  executable.
- **Not verified**: the Phantom connect/sign click path. It needs a real
  extension, which cannot be driven headlessly.

Program keypairs moved to committed `chain/keys/` (dev identities only), because
Anchor generates them into `target/` — so cleaning the build silently changed
every program's address and broke its own `declare_id!`.

### T26: Prove the copy-out   [Status: DONE 2026-08-11 | Model: opus]

The portable set was copied into an empty directory with a minimal root
`package.json`, and the loop run there: doctor, dev (build + deploy), test.
Counter's 5 tests passed under **both** runners. `chain/README.md` documents the
procedure and the two things that bit.

It found a real bug: `packages/chain-cli/src/bin.ts` mounted the command group on
a program of the same name, so a project without a host CLI had to type `chain
chain doctor`. Fixed via `standaloneProgram()`, with a test.

### T27: `./stack` — one entry point for local services   [Status: DONE 2026-08-11 | Model: opus]

Kai spotted that every documented command started with `badcode`, a binary he
could not find. It exists — `packages/cli` declares `"bin": {"badcode": ...}` —
but npm only symlinks it into `node_modules/.bin`, which is not on anyone's PATH.
So every command in the README and on the demo page was uncopyable as written.

Fixed by adopting Agent Orange's `./stack` convention: one executable at the repo
root, self-documenting header, verbs for everything local (`start`, `stop`,
`status`, `logs`, `redeploy`, `reset`, `test`, `fund`, `check`, `shell`,
`doctor`, `image`). It shells out to `node_modules/.bin/chain` **by path**, never
`npx chain` — npx would silently fetch an unrelated package from the registry if
the workspace were not installed. No tmux, unlike Agent Orange: there are two
services here, not five, so `./stack logs` is enough.

`chain` stays the portable CLI; `./stack` is this project's wrapper, and a
project that copies the toolchain writes its own. All references in
`chain/README.md`, `CounterPage.tsx` and `CLAUDE.md` were corrected.

Also adds `chain/TESTING.md`: the manual Phantom walkthrough, whose load-bearing
point is that **Phantom sends transactions over its own selected network, not the
page's** — so leaving it on Mainnet fails every click with a blockhash error
while the page correctly reports localnet.

### T28: `retire` — the coin notices its own end   [Status: pending | Model: opus]
- **Scope:** ENC runs **forever** (Ruling B, 2026-08-12) — with one exception it
  can prove for itself. Add a permissionless `retire` instruction that any caller
  may invoke and that the *program* validates: if the last successful `sync_m2`
  is older than `RETIREMENT_SILENCE`, set `config.retired = true`, irreversibly,
  and emit a `Retired` event. Once retired, `sync_m2` refuses forever. Nobody can
  retire it early; nobody can prevent it once the condition is true. **No key, no
  discretion, no announcement — anyone can walk up and observe that it ended.**
- **Why time, not "the value stopped changing":** the program has no clock of its
  own and only runs when someone sends a transaction. A staleness *counter* needs
  somebody to keep poking it; an elapsed-time test is true whether or not anyone
  is watching, and the first visitor years later can flip the bit.
- **`RETIREMENT_SILENCE` = 365 days** (placeholder for T15, but the reasoning is
  fixed): M2 publishes monthly, and this flag is **irreversible on a
  non-upgradeable program**, so a Switchboard outage or a bad month must never be
  able to end the artwork.
- **What a year of silence actually means (2026-08-12 review — the copy must not
  overclaim).** The trigger measures one thing: *no new M2 figure reached this
  program for a year.* The program cannot know why. The causes, roughly in order
  of likelihood over a forever horizon: the oracle stack rotted (Switchboard
  sunsets the feed's runtime — near-certain eventually, against a pinned feed
  hash on a non-upgradeable program); nobody left who cares to crank; the sync
  caps deadlocked (T29 removes this cause); FRED stopped serving; the Fed went
  dark. Do **not** write "a one-year gap in US money-supply publication means
  something genuinely happened" — oracle silence is not Fed silence. Write what
  is true, which is also the better joke: **the coin ends when nobody has told
  it about money for a year — whether because the dollar ended or because
  everyone stopped looking, and from where it sits those are the same event.**
  That is the most Emperor's-New-Clothes ending available.
- **Correctness dependency:** the silence clock only freezes when the *data*
  stops advancing if `release_date` is Fed-sourced and `sync_m2` refuses
  repeats — see the requirement added to T18. Without it, `retire` can never
  fire while any bot cranks a dead series.
- **Open creative call (Kai/Jack) — what retirement DOES to the auctions.**
  Either everything freezes and the final state stands as the exhibit, or *the
  auctions keep running forever at the last prices the Fed ever reported* — the
  machine grinding on, trading flags at the valuations of a vanished world,
  because nobody noticed the numbers stopped meaning anything. The second is the
  better ending and costs nothing extra; it needs a ruling before this is built.
  **Constraint from the 2026-08-12 review:** the freeze ending must keep
  `withdraw_bid` and every other escrow exit alive after retirement, or it
  strands live bids permanently — the exact harm T12's criteria forbid. "Keep
  trading" has no such edge and is mechanically free: price interpolation
  already flattens at `price_to`, so after the final sync the machine holds the
  last prices with no extra code.
- **Files:** `chain/programs/emperors-new-coin/src/instructions/retire.rs`,
  `src/state.rs` (extend `Config`), `chain/tests/retire.ts`.
- **Acceptance criteria:** `retire` fails while syncs are current and succeeds
  once the silence threshold has elapsed. Calling it twice is harmless. After
  retirement `sync_m2` always fails. No signer is required and no authority is
  consulted. Clock manipulation in tests uses the mock oracle's timestamps, not a
  writable state field.
- **TDD:** yes
- **Validation:** `./stack test test-retire`.
- **Depends on:** T10
- [x] done
- Notes: 7 cases green, including a stranger with no relationship to the program
  ending it, and money still leaving escrow afterwards.
  **The open creative call is answered: keep trading.** Both this ticket and the
  decision doc recommended it, it is mechanically free (`PriceCurve` already
  flattens at `price_to`, so after the final sync the machine simply holds), and
  it is the *safe* option rather than merely the better one — a freeze would
  have had to keep `withdraw_bid` and every escrow exit alive anyway or it would
  strand live bids permanently. `retire` therefore touches exactly one thing:
  `config.retired`, which only `sync_m2` reads. **Reversible until T22 and owed
  Kai/Jack's ratification**; the program README now states it as built, since
  the code does it.
  **Three shape decisions.** (1) **`Printer` gained `last_sync_at`** — a unix
  timestamp beside the existing `last_sync_slot`, because a program cannot
  convert a slot into a date, so the slot could never answer "how long has it
  been". It is **seeded at `initialize`**, not left at zero: at zero the coin
  would be decades overdue for retirement the instant it was born and the first
  stranger to look could end it before the first sync. It advances only on a
  *successful* sync, which is the mechanism T18's Fed-sourced `release_date`
  requirement protects — a feed still serving a dead series fails the
  release-date guard, never reaches that line, and the clock keeps running.
  (2) **`RETIREMENT_SILENCE` is `Config.retirement_silence_seconds`**, shipped
  at 365 days and 25 seconds on the test ledger — the third parameter to make
  that trade, after `term_seconds` and `epoch_seconds`. Marked
  `placeholder: false`: the length is reasoned, not swept.
  (3) **`Config` now documents two one-way latches** rather than one. Neither
  `initialized_assets` nor `retired` has a key on it, and `retired` is not
  anyone's decision — it is a condition the program checks about itself. The
  economic parameters still have no setter at all.
  **The suite is TERMINAL and is excluded from the run-everything script.**
  Retirement is irreversible by design, so once `retire.ts` passes, `sync_m2`
  refuses on that ledger forever and the auction and sync suites have nothing
  to sync. `Anchor.toml`'s `test` now carries `--ignore 'tests/retire.ts'` with
  the reason written next to it; `./stack test test-retire` runs it, and the
  ledger wants `./stack reset` after. Nothing is lost from coverage: T23's
  gate is "every `./stack test test-*` suite", which names them individually.
  **Two traps worth not rediscovering.** Anchor **rejects `.signers([x])` on an
  instruction with no signer account** — "unknown signer", because the extra key
  is not in the account list. That refusal is itself proof of signerlessness,
  but to actually *execute* as a stranger you must build the instruction and
  send a raw `Transaction` with them as fee payer. And **`h.program.idl`
  presents camelCase names**: an IDL shape assertion looking for `place_bid`
  fails while `claim` passes, which reads as "the auction vanished". That is
  `chain/README.md`'s "two IDLs that disagree" surfacing somewhere new — the
  `initialize.ts` allowlist already carries both spellings for this reason. The
  fix here was better than the assertion: the case now **places two bids and
  withdraws one on a retired chain**, which proves what actually matters — that
  no escrow is stranded by the end of the world.

### T29: Proportional sync caps — remove the built-in doomsday constants   [Status: pending — from the 2026-08-12 adversarial review | Model: opus]

- **Why this exists.** As built at T7/T10, `Config.max_single_mint` is an
  **absolute number of base units**, fixed at `initialize`, forever, on a
  non-upgradeable program — while the median monthly mint grows with M2, which
  doubles roughly every 11 years. Any finite value is therefore exceeded by an
  ordinary month eventually. When that happens `sync_m2` fails, and because
  level-targeting only updates `previous_m2` on success, **every later sync
  fails too**, and T28 retires the coin 365 days later. "Forever" as built is
  "until M2 outgrows a constant chosen in 2026." The same deadlock hits
  `max_change_bps` on a single genuine hyperinflation-scale release: a real
  move past the cap can never be believed, the gap never closes, and the coin
  dies at the exact moment its thesis is most vindicated. T15's historical
  replay could never catch either — the breach is in the future by construction
  (hence the forward projection now required in T14/T15).
- **Scope:** (1) Replace `max_single_mint: u64` with a proportional bound or
  delete it outright — `max_change_bps` already caps the move as a ratio, so
  the absolute cap adds nothing but the time bomb. (2) Give an oversized *real*
  move a **catch-up walk** instead of a permanent refusal: when a release's
  delta exceeds `max_change_bps`, move `m2_value` toward the quote by at most
  the cap and do **not** store the release date; repeated permissionless calls
  walk supply to the target over several transactions, each rescaling prices by
  its own step ratio (the steps telescope), and the final in-cap step commits
  the release date. A bad oracle print still moves at most one cap-step before
  the next genuine release retargets it — level-targeting self-heals, exactly
  as it already does for uncovered burns.
- **Files:** `chain/programs/emperors-new-coin/src/{state.rs,math.rs}`,
  `src/instructions/sync_m2.rs`, `chain/tests/sync.ts` (extend).
- **Acceptance criteria:** An ordinary month's mint at 10× today's M2 level
  succeeds with the shipped parameters. A single release 5× over the cap is
  absorbed over multiple `sync_m2` calls, each within cap, with the release
  date committed exactly once, supply landing exactly on target, and prices
  rescaled by the same total ratio as a single-step sync would have applied
  (up to truncation). A bad print followed by a corrected release converges
  back to the true target. `previous_m2 = 0` still fails rather than walking
  from zero. The T14 forward projection passes at the T15 parameter values.
- **TDD:** yes
- **Validation:** `./stack cargo test -p emperors-new-coin --lib && ./stack test test-sync`.
- **Depends on:** T10. **Must land before T22** — the authority burn makes it
  permanent, and this is the one class of bug (works now, fails by arithmetic
  certainty later) that non-upgradeability turns fatal.
- [x] done
- Notes: 34 Rust unit tests (7 new, all on the walk) and the sync suite rewritten
  around the new behaviour.
  **`max_single_mint` was deleted rather than made proportional.** The ticket
  offered either; `max_change_bps` already bounds the move as a ratio, so a
  second cap in absolute base units bounded nothing that was not already bounded
  and carried the whole time bomb by itself. Out with it went the `Config` field,
  the `InitializeParams` field, the `sanity.maxSingleMint` parameter and the
  `MintTooLarge` error.
  **`ChangeTooLarge` went too, and that is the real shape of this ticket.** Once
  an oversized move is *walked* rather than refused, no move is ever refused, so
  the error had no remaining path to it. `NoBaselineM2` replaces it for the one
  thing still refused — a walk from zero, which has no ratio to walk along.
  `change_bps` was deleted with them: nothing calls it now, which is the standard
  T30 applied to `rent_owed`. Error renumbering was free again, as T30 predicted,
  because no suite matches on a numeric `60xx` code.
  **Two floors the walk needed that the ticket did not specify, both of which
  would have re-created the exact deadlock it exists to remove.**
  (1) **A step is never zero.** The proportional step is `from × cap ÷ 10000`,
  which truncates to nothing for a small enough `from` — and a walk that cannot
  move is the same permanent refusal in a friendlier costume.
  (2) **A downward walk never reaches zero.** This one is not theoretical:
  repeated 10% cuts with integer truncation *do* reach zero, and from zero every
  later sync has no baseline, so a program that could get there could never
  leave. The walk floors at one unit. A real M2 of zero is not a reading, it is
  the end of money.
  Also: the ceiling at the top of `u64` **saturates rather than erroring**. A
  ceiling above `u64::MAX` means "no ceiling in range", and refusing a step that
  is perfectly representable would have been the deadlock in a third costume.
  **The honest trade, recorded because T22 makes it permanent.** A bad oracle
  print is no longer refused outright — it is merely slow and expensive, and
  anyone willing to send enough transactions can walk supply all the way to a
  wrong number. What makes that survivable is that level-targeting self-heals:
  the next genuine release retargets absolutely, exactly as it already does for
  an uncovered burn, and the suite proves it. A permanent deadlock does not
  self-heal. This is the better of two failure modes, not a free lunch, and the
  ticket's own sentence *"a bad print still moves at most one cap-step before
  the next genuine release retargets it"* is true of a caller who stops and not
  of one who does not. **No time gate was added**, deliberately: the ticket
  specifies a per-transaction walk, and a clock that must be waited on is a new
  deadlock class rather than a fix for the old one.
  Two smaller things. `Synced` gained `release_committed`, so an indexer can
  tell "still catching up" from "done" without diffing the printer. And T28's
  retirement clock **does** advance on a partial step — the program genuinely
  heard about money — which cannot be used to keep a dead coin alive, because a
  walk always terminates and the release date then commits.

### T30: Remove the rent machinery   [Status: pending — the deletion Ruling A implies | Model: sonnet]

- **Why this exists.** Ruling A deleted rent on 2026-08-12, and the decision
  doc's cost table says "T11 → delete" — but **no ticket ever owned the
  deletion, so the code is still live in the tree**: `settle_rent` and
  `foreclose` are wired into `lib.rs`, `Config` still carries three rent
  parameters, `sync_m2` still banks rent before every rescale, and `lib.rs`'s
  own module docs still describe force-buy and rent as the machine. T12 extends
  the same files, so shipping this first is what stops the auction being built
  on top of a contradiction. Found by the 2026-08-12 adversarial review.
- **Scope:** Delete the rent/foreclosure machinery and every reference to it,
  leaving the peg (T7–T10) untouched.
  - **Delete:** `instructions/settle_rent.rs`, `instructions/foreclose.rs`,
    `chain/tests/rent.ts`, and the `test-rent` script in `Anchor.toml [scripts]`.
  - **`lib.rs`:** drop both `#[program]` entrypoints, and **rewrite the module
    doc comment** — it currently describes assets "always for sale at a
    published price with no right of refusal" whose "holders pay rent to the
    vault", which is now the opposite of the design. Replace with the tenancy
    model (auctions, certificate, no holding cost).
  - **`instructions/mod.rs`:** drop both modules and their re-exports.
  - **`state.rs`:** remove `Config.rent_rate_per_day_bps`, `Config.grace_seconds`,
    `Config.foreclose_bounty`, and `Asset.rent_accrued`. **Leave
    `Asset.last_touched` in place and flag it to T12** — it is currently "when
    rent was last settled or the holder last changed"; T12 decides whether it
    becomes the term anchor or is replaced by `term_ends_at`. Deciding it here
    would be guessing at T12's shape.
  - **`math.rs`:** remove `rent_owed` and `PriceCurve::integral` (the integral
    exists only to charge rent against a moving price; nothing else calls it)
    plus their unit tests. Keep `price_at` — the auction reserve needs it.
  - **`instructions/initialize.rs`:** remove the three fields from
    `InitializeParams`, their assignments, and their `InvalidRate` validation.
  - **`sync_m2.rs`:** remove the rent-banking block and the `rent_rate` local
    from `rescale_assets`, and the comment explaining bank-before-rescale. The
    Emperor-charges-himself-nothing branch goes with it. *(T10's Notes keep the
    original explanation as history — do not edit past tickets' Notes.)*
  - **`errors.rs`:** remove `NotForeclosable` and `VaultHoldsAsset`. **Keep
    `WrongHolderAccount`** — T12 needs exactly that check when paying the
    outgoing holder. Note that Anchor numbers error codes by declaration order
    (6000 + index), so removing variants **renumbers every later code**; that is
    free now and impossible after T22, which is another reason this lands here.
  - **`chain/params.genesis.json`:** delete the `rent` block. Leave `sanity`
    alone — T29 reworks it.
  - **`chain/tests/{enc-harness,initialize}.ts`:** drop the rent params from the
    harness type and the `initialize` call, and the `rentRatePerDayBps`
    assertion.
  - **`chain/tests/initialize.ts` "exposes no instruction that could rewrite the
    rules":** remove `settle_rent`/`settleRent`/`foreclose` from the allowlist,
    **and add a positive assertion that the IDL does not contain them** — the
    removal should be provable, not merely untested.
- **Files:** as enumerated above.
- **Acceptance criteria:** The program builds and every existing suite passes.
  `grep -rnE 'rent_owed|rent_accrued|rent_rate|settle_rent|settleRent|foreclos'
  chain/programs chain/tests chain/params.genesis.json` returns nothing outside
  historical comments. **Do not grep for the bare word `rent`** — Solana's own
  account-rent exemption and the `Rent` sysvar (`initialize.rs` holds a
  `Sysvar<'info, Rent>`) legitimately use it, and conflating the two is how this
  ticket breaks `initialize`. The published IDL contains neither `settleRent`
  nor `foreclose`. `sync_m2` still rescales all ten assets correctly and its
  suite passes unchanged.
- **TDD:** no (deletion; the existing suites are the regression).
- **Validation:** `./stack cargo test -p emperors-new-coin --lib && ./stack test test-init && ./stack test test-sync`.
- **Depends on:** T10. **Blocks T12** — same files.
- [x] done
- Notes: Rust unit tests 42 → **30** (the 12 removed were `integral` and
  `rent_owed`); `test-init` 14 green on a fresh ledger, `test-sync` 12 green +
  the 1 deliberately-pending uncovered-burn case. `./stack check` clean.
  **Run on opus though the header says sonnet** — Kai's call, made rather than
  switching models twice for a mechanical deletion.
  **Four references the enumeration missed**, all forced by the deletion rather
  than scope creep: `init_asset.rs` zeroed `rent_accrued`; `Cargo.toml`
  justified the `init-if-needed` feature by naming `foreclose` (the feature
  **stays** — `set_mock_m2` uses it now and T12's create-the-holder's-account
  rule needs it, so the comment was repointed at that); `errors.rs` had a
  section header `── Assets, rent, sales ──`; and `math.rs`'s `faucet_pot` doc
  said the pot stays at zero "until rent rebuilds the Emperor's coffers", which
  is now a claim about a mechanism that does not exist — rewritten to the two
  ways the vault actually refills (M2 rises, or a flag the Emperor holds is won
  at auction).
  **Two build facts worth not rediscovering.** The published IDL only refreshes
  from a **default** build (T9/T10's note), so removing an instruction needs
  `./stack build` before the mock build the suites do for themselves — otherwise
  the committed interface still advertises `settleRent`. And `Config` losing
  three fields is a layout change, so `./stack reset` is required or every
  pre-existing account fails to decode.
  Error renumbering was free as predicted: no suite matched on a numeric
  `60xx` code, only on names. `Asset.last_touched` kept and flagged to T12 in
  its doc comment; `sync_m2.ts`'s "banks the rent clock" test renamed to
  "restarts every asset clock at the sync" and kept, so the field cannot
  quietly stop being maintained before T12 picks it up.
  The IDL-shape test asked for is in `initialize.ts` as *"has no rent or
  foreclosure instruction, and no rent parameters"* — it also asserts the
  `Config` fields are gone from the published types, since a parameter with no
  instruction behind it is a rule the coin cannot enforce.

### T31: The Imperial Gazette — tenant copy + the editor's pen   [Status: **DONE 2026-08-13** — validation re-run by the orchestrator; slot names still placeholders, Jack's sheet consumed at T22 | Model: opus]

- **What the ten assets are (decided 2026-08-12, replacing the placeholder
  "flags").** The ten slots of a newspaper front page — the asset layer is **a
  newspaper about money, whose column-inches are auctioned monthly.** When the
  Fed prints, the price of speech rises by exactly the printed rate. Candidate
  slot sheet, Jack's pass owed: the masthead (the paper's *name* is for sale),
  the main headline, the lead story, an opinion column, letters, a cartoon
  caption, the weather ("outlook: inflationary"), obituaries (for dead coins),
  the serial, a classified ad. **Slot personalities are genesis naming +
  frontend presentation only — one program mechanism serves all ten.** The
  serial is the worked example: consequences/exquisite-corpse, one sentence per
  term, is pure presentation — the chain is public, so "you can only see the
  last word" is theatre the site performs, not a secret the chain keeps, and
  the page must say so (same disclosure family as the melting balance).
- **Scope:**
  1. `Asset` gains a fixed-size `copy` field (~280 bytes, decided at build)
     plus `copy_filed` / `copy_spiked` flags, reset at every settlement. Copy
     *persists* across settlement until the new tenant files — yesterday's news
     stands until today's edition.
  2. `file_copy(index, text)` — current tenant only, **once per term**.
     Write-once is what makes the pen decisive; unlimited rewrites turn
     moderation into a war that requires BadCode to run a bot forever, which
     re-inserts us as an operational dependency.
  3. `spike(index)` — editor key only, **once per term per column**; replaces
     the copy with a fixed redaction marker. **The pen strikes words; it never
     authors them** — BadCode must not write into a slot someone paid for, and
     a fixed marker is also the better joke (redaction bars).
  4. `Config.editor` set at `initialize`, plus `pass_the_pen(new_editor)` —
     rotation is the one thing that must survive key loss/theft — and
     `break_the_pen()` (set to `None`, irrevocably: the paper goes feral).
     Whether the pen breaks at retirement is part of T28's open creative call.
  5. Shape tests: the editor key appears in **no** instruction that moves
     tokens, asserted against the IDL like the T30 removal test; the
     `initialize.ts` allowlist gains the three names deliberately.
  6. **Claims surgery, same commit** — the sentences the pen falsifies, fixed
     where they live: the program README's "Who can change the rules? Nobody"
     and "no admin key, no pause button"; `lib.rs`'s module doc; this plan's
     claim block (amended above). The replacement is always the two-part form:
     *no key over the money; one pen over the words.* State the blast radius
     plainly: a stolen pen can vandalise ten columns per month; it cannot move
     a token. This is not a decentralisation play and never was — the trustless
     surface is the money, and every one of those claims is untouched.
- **Files:** `chain/programs/emperors-new-coin/src/instructions/{file_copy,spike,pass_the_pen}.rs`,
  `src/state.rs` (extend `Asset`, `Config`), `chain/tests/gazette.ts`,
  `chain/programs/emperors-new-coin/README.md`, `src/lib.rs`.
- **Acceptance criteria:** The tenant can file once per term and not twice; a
  stranger cannot file; the vault-held (Emperor's) slots show default copy. The
  editor can spike once per term per column and not twice; spike writes the
  marker, never caller-supplied text; a spiked slot cannot be re-filed until
  the next term. `pass_the_pen` transfers the power; `break_the_pen` ends it
  forever. **No new instruction moves any token** (shape test against the
  IDL). Total supply and every balance are untouched by every new path — the
  signature invariant survives verbatim.
- **TDD:** yes
- **Validation:** `./stack test test-gazette`; the T9 IDL grep discipline
  (default `./stack build` + `! grep -q set_mock_m2 chain/idl/emperors_new_coin.json`).
- **Depends on:** T12 (term lifecycle + settlement reset). **Must land before
  T22** — the editor key, the copy field size, and the slot names/genesis
  prices all become permanent at the authority burn — and **before T19**, which
  decodes `Asset` and renders the front page, so the account layout must be
  final before the frontend is written against it.
- **NOT blocked on Jack (clarified 2026-08-13 ticket audit).** The plan header
  previously said this ticket was blocked on the slot sheet; it is not. Ruling D
  is explicit that slot personalities are *genesis naming and frontend
  presentation over one mechanism serving all ten*, and the price ladder is
  already fixed in `params.genesis.json`. **Build the mechanism now with
  placeholder slot names** (`slot_00` … `slot_09` or the candidate sheet in the
  scope above, clearly marked provisional). Jack's sheet is consumed at **T22**,
  where `init_asset` writes the real names and the burn makes them permanent.
  Nothing in the program logic branches on a slot's name.
- [x] done — 2026-08-13. Orchestrator re-ran the validation independently:
  `./stack test test-gazette` **16 passing** on a fresh ledger, `./stack cargo
  test -p emperors-new-coin --lib` **39 passing**, the shipped IDL carries the
  four new instructions and no mock one, and every pre-existing suite is still
  green (init 12, sync 14, auction 12, faucet 10, retire 7 — run last, then
  `./stack reset`). Slot names remain
  placeholders by design; Jack's sheet is consumed at T22.
- Notes (executor, 2026-08-13 — **six judgement calls the ticket did not
  settle**, all reversible until T22 and all flagged rather than buried):
  1. **`copy` is 280 bytes plus an explicit `copy_len: u16`.** The ticket named
     the field and the flags but not how a client finds the end of a shorter
     string. NUL-termination was rejected: nothing stops a tenant filing a zero
     byte, so scanning for one would silently truncate their column. `copy_len
     == 0` doubles as "never written", which is what the front page renders the
     Emperor's default copy from.
  2. **The editor may spike a vault-held column.** Nothing in `spike` branches
     on the holder — the pen is aimed at a column, not a tenant. Striking one
     the Emperor holds writes the marker over nothing. Harmless, left
     permitted, and cheaper than a rule; say so if T19 renders it oddly.
  3. **`pass_the_pen` refuses the all-zero key**, and `initialize` refuses
     `Some(Pubkey::default())`. Either would leave `editor.is_some()` true while
     no hand could sign — an account claiming an editor exists when none does.
     `break_the_pen` says that honestly; these refuse to say it by accident.
  4. **`InitializeParams.editor` is `Option<Pubkey>`, and is *not* in
     `params.genesis.json`.** That file holds economic parameters chosen by the
     simulation; the pen is a key chosen at deployment. `None` is accepted, so a
     paper can be feral from birth. **T22 must supply the real key** — the test
     harness uses the deploy wallet, which is the only key every suite has and
     the only one that survives a re-run.
  5. **`chain/tests/gazette.ts` is one-way, cheaply.** Its last case breaks the
     pen, which is irrevocable, so a re-run marks the seven pen cases pending
     instead of passing for the wrong reason (verified: 15 passing fresh, 9
     passing + 7 pending on a re-run). Unlike `retire.ts` it stays in the
     run-everything script, because nothing outside the suite uses the pen.
     `./stack reset` restores full coverage.
  6. **Placeholder slot names unchanged.** `assetSpec` still writes
     `Placeholder Asset N`; no program logic anywhere branches on a slot's name.
     Jack's sheet is still consumed at T22 as planned.
- Notes: Genesis prices differ per slot (`init_asset` already takes one per
  index): masthead dearest, classified cheapest. **The cheapest reserve is
  T14/T15's faucet-reachability target**, which turns the pass/fail criterion
  into a sentence: *anyone patient can afford a small ad.* Price ratios freeze
  at genesis — every sync rescales all ten by the same factor — so the masthead
  is always the masthead, deliberately. Frontend (T19/T20) renders the front
  page and the site curates what it hangs: the chain records, the gallery
  chooses — declared on the page, same as the melting balance.

## Discovered Issues Log

_(appended by executors during implementation)_

- **2026-08-13 · T21 · 🔴 "thirteen in a row" is not true of the record, and it
  had already propagated into three files.** The claims standard itself
  (`2026-08-12-enc-architecture-decision.md` §4) carried *"M2 falls in 6.1% of
  months — 13 in a row in 2022–23"*, and from there it reached
  `settle_auction.rs`'s module doc and this plan's T12 notes. Re-derived from
  `chain/sim/m2-history.csv`: **the longest run of consecutive monthly falls in
  the entire 1959–2026 series is nine, August 2022 to April 2023.** The
  contraction ran nineteen months peak (2022-03, 21787.2) to trough (2023-10,
  20737.5) and seventeen of those months fell — but across *three* runs of 3, 9
  and 5, which is the likeliest origin of the wrong number. Corrected in all
  three places, visibly rather than silently in §4, because that section is what
  other copy is written against. Everything else in §4 re-verified and holds.
  **The lesson is the T20 one arriving a second time**: a figure that is only
  ever quoted, never re-derived, drifts and then hardens. The claim ledger in
  `docs/coins/emperors-new-coin.md` now lists each figure next to the operation
  that reproduces it, so the next person can check rather than copy.

- **2026-08-13 · T21 · 🔴 two documented `./stack` commands did not work.**
  Found by running the docs rather than reading them.
  1. **`./stack test <suite> --features mock`** — the form printed by
     `./stack help` and by the script's own inline comment — fails with *"the
     package 'counter' does not contain this feature: mock"*. Cargo features are
     per-package and `anchor test` rebuilds the whole workspace, so the flag
     reaches `counter`, which has no such feature. The dispatch already builds ENC
     with `--features mock` automatically; passing the flag takes the *other*
     branch and breaks it. **There is nothing to ask for, so the help text now
     says `./stack test [suite]`** and the comment explains the trap.
  2. **`./stack build --features mock`**, also advertised in the help, fails the
     same way for the same reason. The working form names the program:
     **`./stack build emperors_new_coin --features mock`**. Help corrected.
  Both were verified failing and then verified fixed. `./stack build
  emperors_new_coin --features mock` also prints *"committed IDL left
  unchanged"*, so the mock-IDL hazard is now guarded at the build as well as in
  the test that used to trip it.

- **2026-08-13 · T21 · `test-init` fails rather than skips on a played ledger.**
  On the shared localnet after T19/T20's runs, `./stack test test-init` is 12
  passing / 3 pending / **1 failing**, and the failure is *"puts 100% of the
  genesis supply in the vault"* comparing 20,680,992,104,074,290 against the
  genesis 22,176,100,000,000,000. That is the ledger, not the program — the
  supply has since been synced. The T12 log already recorded the general rule
  ("any assertion about pristine state needs the same treatment") and fixed the
  auction suite's equivalent case to **skip** on a played ledger; this one was
  missed. Documented as the remedy (`./stack reset` first) in `chain/README.md`
  rather than fixed, because changing a test's pass condition is not a docs
  ticket's call — but it is three lines and belongs to whoever next opens
  `initialize.ts`. Everything else run at T21 is green on the played ledger:
  39 Rust unit tests, `test-gazette` 16 passing, `test-faucet` 10 passing,
  `./stack check`, `npm run build`.

- **2026-08-13 · T21 · "every multi-decade window is above 5%" is true of the
  table it sits under and false if generalised.** `MELT_ANNUAL_BPS = 600` is
  **correct and its evidence reproduces exactly** — all five CAGRs in its comment
  (6.73 / 5.62 / 6.25 / 6.32 / 6.08%) re-derive to the digit. But those are five
  windows that all *end at 2026-06*. Across every 20-year window in the series,
  **28 of 570 come in below 5%**, the weakest being **4.88% (1987-01 → 2007-01)**.
  Every 30-year window (min 5.36%) and every 40-year window (min 5.61%) clears 5%.
  So the honest generalisation is *"every thirty-year window"*, not *"every
  multi-decade window"*. Nothing needs changing in the code; recorded so the
  looser sentence is not the one that gets printed later. Not a defect — a
  reminder that the failure mode being guarded against is a claim widening
  quietly as it is re-quoted.

- **2026-08-13 · T21 · `docs/coins/emperors-new-coin.md` was linked from four
  files before it existed.** `chain/feeds/README.md:21` and this plan (four
  places) pointed at it as though it were the authority on the honest oracle
  sentence. It now exists and is that authority. Worth noting because a dangling
  link to a claims document reads, to anyone auditing, exactly like a claim with
  no backing — which is what it was.

- **2026-08-13 · PRE-BURN REVIEW · 16 agents, five lenses, adversarial
  verification.** Twenty raw findings → **seven confirmed**, four refuted with
  corrections, nine below the verification threshold. Confirmed, worst first:
  1. **🔴 CRITICAL · nothing checks that the deployed `.so` is a default
     build.** `./stack test` builds the mock last, so `chain/target/deploy/
     emperors_new_coin.so` is the **mock binary** after any test run, and
     `deploy`/`deployProgram` never rebuild — they upload what is on disk. The
     only mock guard anywhere inspects the *published IDL*, a different artifact
     from a different step. `set_mock_m2` is unauthenticated by design and
     `mock_fund` moves vault ENC to any named wallet, so a mock build that
     reaches a real cluster and is then burned hands every stranger the money
     supply, permanently. *Verifier's correction, fairly made:* the documented
     recipe does start with `./stack build`, and a mock build would fail T23's
     live-Switchboard criterion — so this is a missing belt to an existing
     brace rather than a live break. It is still the one artifact the burn makes
     permanent and it has no mechanical provenance check.
  2. **🔴 CRITICAL · the published "ceiling law" is wrong by a factor of two.**
     `docs/coins/emperors-new-coin.md` derives that the cheapest column supports
     about ten thousand diligent claimants; the arithmetic beside it gives
     ~5,000. Published as a derived law with a re-runnable proof that does not
     support it — precisely the failure the project names as the only fatal one.
  3. **🔴 HIGH · `init_asset` does not validate `genesis_price`.** Zero is an
     absorbing state (`rescale(0, ..) == 0` forever, so the slot is winnable for
     one base unit for all time), and a mis-scaled ladder stays internally
     consistent while being permanently wrong against M2. The ppm → base-units
     conversion exists in exactly one place in the repo — `assetSpec()` in a
     **test file** — and T22 asks the operator to redo that multiplication by
     hand, once, at the only moment it can never be corrected.
  4. **🔴 HIGH · every tenancy certificate is minted with an empty URI** and its
     update authority set to `None` in the same instruction. The certificate is
     the one piece of the artwork that lands in a human's wallet, and it will
     render as nothing, forever.
  5. **🔴 HIGH · `./stack test`, `reset` and `start` all rewrite the committed
     `chain/idl`.** The same class as the `syncIdl` unit-test bug fixed earlier
     today, one level up in the CLI itself — and the log's entry for that fix
     reads as a broader exoneration than it earned.
  6. **🔴 HIGH · the prefilled bid is the reserve at render time**, and the
     reserve climbs every second, so the *default* bid transaction on any column
     is guaranteed to be refused. The first bid — the primary interaction the
     auction exists for — costs a fee and returns an error.
  7. **🔴 HIGH · "the faucet pays out roughly what the Fed printed, and not one
     token more" — it pays about half.**
  Below the verification threshold but worth naming, because **two independent
  lenses found it**: the Gazette masthead prints *"a currency that only goes
  up"* — the single claim §4 pre-commits never to make — and `EncPage` serves
  "Nobody here can change that, including us" unqualified while the program is
  undeployed with a live upgrade authority.
  Full output: the workflow result for run `wf_bdfdf6bc-ff2`.

- **2026-08-13 · T20 · 🔴 an order-of-magnitude figure became a claim on the
  page.** The melting balance shipped falling at **5% a year**, described in
  code as "the rate the money supply grows at in the long run" and on the page
  as "roughly how fast they print", citing
  `design/research/2026-08-12-enc-tokenomics/README.md`. That research does say
  "on the order of 5% per year" — but it is comparing against rent at *150% a
  month*, where a point either way changes nothing. **Compounded from the Fed's
  own series, M2 has grown 6.73% a year since 1959, and above 5.6% on every
  multi-decade window since 1990 — every window is above 5%.**
  **Fixed by the orchestrator: `MELT_ANNUAL_BPS` is now 600**, the conservative
  round number rather than a flattering one, with the measured windows recorded
  at the constant and a caveat added to the research file so the loose figure is
  not imported again. Artistically it is also the better number: the truth is
  worse than 5%, which is the joke landing harder. **Kai may reasonably prefer a
  different rate** — it is one constant and one test line.
  The general lesson for T21, which has to state claims for real: **the research
  briefs are argument-grade, not copy-grade.** A number good enough to win an
  internal argument is not automatically good enough to print.

- **2026-08-13 · T19 · 🔴 `./stack check` overwrites the committed IDL with
  whatever was last built — including the mock one.** Two steps, and the second
  is the surprising one. `./stack test` builds with `--features mock`, which
  leaves `chain/target/idl/emperors_new_coin.json` carrying `set_mock_m2` and
  `mock_fund`. Then **`packages/chain-cli/src/anchor.test.ts`'s `syncIdl` case
  calls `syncIdl()` against the real repo root**, so running the unit tests
  copies that build output over the committed `chain/idl/`. The validation
  command mutates tracked files, and the natural workflow — run the suites, run
  check, commit — ships an interface describing a build we never release. Hit
  twice in this ticket and reverted by hand both times
  (`git checkout -- chain/idl/`); T9's grep discipline catches it only if
  somebody remembers to run the grep.
  **The fix is three lines and belongs to whoever owns `chain-cli`:** give that
  test a temporary root with a fixture `target/idl`, the way `restoreKeys`'s
  cases already do two describes above it, rather than pointing a
  file-copying function at the working tree. Left unfixed here because it is
  outside this ticket and inside the portable package. Worth doing before T22,
  where the deployed IDL becomes permanent.
  **✅ FIXED by the orchestrator, 2026-08-13**, exactly as described — the case
  now builds a `mkdtempSync` root with fixture `target/idl` and `target/types`
  and passes it to `syncIdl(root)`. Verified by planting a sentinel file in
  `chain/target/idl/` and confirming the suite neither publishes it nor dirties
  `chain/idl/`; `./stack check` now leaves the working tree clean. Fixed rather
  than deferred because every remaining ticket runs `./stack check`, so the
  hazard was live for the rest of the build, and T22 makes the published IDL
  permanent.

- **2026-08-13 · T19 · Anchor types every `u64` as `any`, so the compiler does
  not catch a `BN` reaching a `bigint`.** `IdlAccounts<EmperorsNewCoin>` gives
  precise types for `pubkey`, `bool`, `u8`/`u16`/`u32` and arrays, but `u64` and
  `i64` land as `any` in this build. Passing `printer.m2Value` straight to a
  formatter that takes `bigint` therefore typechecks, builds, and throws
  "Cannot mix BigInt and other types" in the browser — which is exactly how the
  page first failed to render. Fixed structurally rather than locally: every
  `BN` is converted at one boundary (`view.ts`), components never see one, and
  `view.test.ts` asserts the view hands out `bigint`. Worth knowing at T20,
  which will touch far more `u64` fields than this ticket did.

- **2026-08-13 · T31 · 🔴 growing `Asset` overflowed the BPF stack, and the
  error names nothing.** The Gazette's 284 extra bytes took `Asset` to 414, and
  `place_bid` — untouched by this ticket — began failing every transaction with
  `Access violation in stack frame 5 at address 0x200005ff8 of size 8`. That is
  a 4KB stack-frame overflow in Anchor's generated account deserialisation, and
  the message mentions neither the account, nor the size, nor Anchor. Fixed by
  `Box<Account<'info, Asset>>` in every instruction context that carries one,
  applied as a uniform rule rather than per-instruction so nothing has to be
  re-measured when an account list next grows. **Recorded in
  [`chain/README.md`](../chain/README.md)'s "Things that will bite you"** — it
  is exactly the class of thing that file exists for, and the next person to
  widen an account struct will hit it. Worth knowing at T19/T22: `Asset` is now
  414 bytes on the ledger and that number is permanent.

- **2026-08-13 · T31 · README vocabulary drift, not fixed.** The program README
  still calls the assets "flags" and "the Emperor's treasures" in the joke
  section and in "What do I actually own?", which predates Ruling D's newspaper
  framing. Nothing there is *false* — they are the same ten things — so it was
  left alone rather than expanding this ticket into a rewrite of the page.
  Worth one pass at T21/T23, when the copy is being read end-to-end anyway.

- **2026-08-13 · ticket audit before the remaining-work run (no code changed).**
  Every unfinished ticket was read against the as-built program and the
  2026-08-12 rulings. The 08-12 review's step 4 — *"rewrite tickets T12 onward
  to match"* — had been applied to T12/T13/T28/T29 but **not** to T19/T20/T23,
  which still specified the deleted rent economy. Findings:
  1. **🔴 The oracle's real path is a stub.** `read_quote` (non-mock) returns
     `OracleUnavailable` unconditionally and discards both arguments; the crate
     has no Switchboard dependency. **A default build can never sync.** Every
     green suite runs under the `mock` feature. The plan's "feature-complete"
     status line was corrected, and T18's scope expanded — it is a from-scratch
     build, not an integration step.
  2. **🔴 T19 directed ENC decoders into `packages/chain-kit`**, which the
     portability contract forbids and **T23's own grep would have failed**.
     Redirected to `packages/enc`, which already documents the rule.
  3. **🔴 T19 specified a `rentOwed` display and T20 specified "force-buy, rent
     owed, settle rent"** — none of which exist. Both rewritten against the real
     instruction set (`claim`, `place_bid`, `withdraw_bid`, `settle_auction`,
     `roll_term`, `mint_certificate`, `file_copy`).
  4. **🔴 T23's end-to-end criterion walked a rent/foreclosure loop.** Rewritten
     as the auction loop, with the signature invariant as the thing being proven.
  5. **🔴 T16's date feed does not exist.** The committed `m2sl.job.json`
     extracts the value only, so `Quote.release_date` has no source — and
     `retire` is only correct if that date is Fed-sourced. T16's board status
     dropped from ✅ to 🟡. A decision is owed on observation-month versus true
     release date **before** the job is stored, because it is immutable after.
  6. **T31 was wrongly described as blocked on Jack's slot sheet.** Ruling D
     makes slot personalities naming and presentation over one shared
     mechanism, and the price ladder is already fixed in `params.genesis.json`.
     T31 builds now with placeholder names; the sheet is due at T22.
  7. **T21's "add the toolchain to `CLAUDE.md`" was already done**, and its
     trust statement predated the editor's pen. Rewritten to the two-part form:
     *no key over the money; one pen over the words.*
  8. **T22 gained an explicit list of what the burn makes permanent**, and an
     endorsed split: deploy upgradeable, prove it, then burn as a separate human
     act.
  9. Minor: the file map still described `math.rs` as carrying rent accrual and
     omitted `Bid` from `state.rs`. Both corrected.
  10. Not fixed, recorded only — small dead code in the program: unused error
      variants `InvalidInterpolationWindow` and `AssetAlreadyInitialized`, and
      unused `rent: Sysvar` fields on `Initialize` and `InitAsset`. Harmless;
      worth a sweep at T23 rather than a ticket of its own.

- **2026-08-12 · adversarial review (Fable), findings folded into tickets:**
  (1) `max_single_mint` / `max_change_bps` deadlock guarantees eventual forced
  retirement → **T29**, and T14/T15 gained a ≥50-year forward projection since
  historical replay cannot see it. (2) T12 as first specced could strand escrow
  (stale high bid at a no-winner rollover) and let an incumbent veto eviction
  (closed token account) — both closed in the ticket. (3) The acceptance
  invariant "no instruction can move a token the caller does not own" was
  unsatisfiable (permissionless `settle_auction` moves the winner's escrow by
  design); restated in signature form. (4) T28's rationale confused oracle
  silence with Fed silence; the committed feed job extracts only the value, so
  Fed-sourced `release_date` is now an explicit T18 requirement T28 depends on.
  (5) Claims corrections in the decision doc §4: the EPI wage figure's window
  and population, "paid the new, higher price," the rug-accusation universal,
  and the forward-looking debasement line as incentive-not-prophecy.
  (6) `m2-backtest.mjs` now self-fetches its CSV and its genesis-supply line
  was off by 10⁶ (printed 23,155 whole ENC; correct is ~23.16 billion).
  (7) Verified clean in the same review: the M2 arithmetic against a fresh FRED
  pull, `PriceCurve` flattening at `price_to` (makes "keep trading at last
  prices" free), rent banked-before-rescale, and the sybil-dilution faucet
  bound.
  (8) **Ruling A's deletion was never ticketed** — T11's rent code is still live
  in the tree (wired into `lib.rs`, `Config`, `sync_m2`), so a builder starting
  at T12 would extend files that contradict the design → **T30**, which now
  precedes T12.

- **2026-08-12 · T30 · the permanent delegate is still on all ten NFTs, and a
  published sentence says it isn't.** T30 deleted the rent machinery, but
  `init_asset` still creates each asset mint with the Token-2022
  **PermanentDelegate** extension, and `initialize.ts` still asserts it
  (*"gives the vault permanent delegate over every asset"*, passing). Left in
  place: T30's scope is the rent machinery, and asset custody belongs to T12.
  **Why it matters.** The decision doc's §3 cost table lists the permanent
  delegate as **dropped** under Ruling A, and §5 states plainly *"Under A2 the
  permanent-delegate flag never applies, since the extension is dropped."* That
  sentence is currently false about the built code — and §4's rule is that the
  mechanism may be harsh but the claims must be exactly true. It is also the
  heavier of the two scanner flags the ruling was partly chosen to shed
  (RugCheck: `"Permanent Control Enabled"`, danger, weight 50000).
  **Not yet a live danger**, which is why it is logged rather than hot-fixed:
  the extension can only be exercised against a wallet holding a flag, and
  under T12 no wallet ever does — the flags stay in program custody and holders
  get a certificate. So the program README's "no instruction can move a token
  out of any wallet without its owner's signature" survives intact today.
  **The decision T12 must make, and the deadline.** Extensions are fixed at
  mint creation, so this is changeable only until T22 runs the real
  `init_asset` calls — after that it is permanent on a non-upgradeable program.
  T12 should either drop the extension (recommended: it is unused under
  program custody, and it buys back the claim) or keep it deliberately and fix
  §3/§5 in the same commit. Do not let it arrive at T22 undecided.
  **RESOLVED at T12 (2026-08-12): dropped.** `init_asset` no longer sets the
  extension, and `initialize.ts` asserts its *absence* where it used to assert
  its presence. The decision doc's §3 and §5 are true again.

- **2026-08-12 · T12 · the auction needed a way to own money, so `mock_fund`
  exists.** The vault holds every token at genesis and its authority is a PDA,
  so the only route from the vault to a wallet is an instruction — and that
  instruction is the faucet, which is **T13, and T13 depends on T12**. Without
  a stand-in, not one acceptance case involving a real bidder could be written.
  Added `mock_fund` behind `--features mock`, exactly as `set_mock_m2` already
  is: a default build contains no instruction that can move vault ENC to a
  chosen wallet, and `initialize.ts` asserts that against the **committed**
  IDL. It *moves* tokens rather than minting them, so `supply = k × M2` holds
  across every test — which is what the faucet will do too. Retire it if T13
  ever makes it redundant; there is no other reason to keep it.
  **RESOLVED at T13 (2026-08-12): kept, and it earned two more jobs.** The
  faucet does give wallets a real route to ENC, but funding the auction suite
  through it would make a bidder's stake `pot ÷ registrants` — a number set by
  whether *another suite* claimed in the previous epoch, on the one ledger they
  all share and which runs them alphabetically. That is the cross-suite coupling
  logged above, and it would make every auction case wait out an epoch before
  bidding. Nothing about the shipped claim changes either way: `mock_fund` is in
  **neither** build and `initialize.ts` proves it against the committed IDL.
  Meanwhile it turned out to be the only way to reach two states the real
  economy takes years to produce — a vault below its floor, and a vault too
  small to cover a burn — so both of those acceptance cases now run on it, each
  putting the money back in a `finally`.

- **2026-08-12 · T12 · `h.program.idl` is the build output, not the artifact
  that ships.** A test asserting "no mock instruction in the interface" against
  `h.program.idl` fails under `./stack test`, because Anchor loads the IDL from
  `target/` — which that command deliberately fills with a **mock** build. The
  shipped interface is the committed `chain/idl/*.json`, and only a default
  build publishes there. Any test about what *ships* must read the file. (The
  T30 rent test happens to pass either way, since rent is absent from both
  builds — so this only bites tests about the mock/default split itself.)

- **2026-08-12 · T12 · suites share one ledger, and `tests/**/*.ts` runs them
  alphabetically — so `auction` runs before `initialize`.** "All ten assets are
  held by the Emperor" is a statement about genesis that the auction exists to
  falsify, so it now skips on a played ledger rather than asserting something
  the design deliberately breaks. Worth knowing before writing T13's suite: any
  assertion about pristine state needs the same treatment, and `./stack reset`
  is what makes those cases run.

- **2026-08-12 · T12 · a parallel session committed this ticket's code inside
  its own commit.** Another session was working the Flow track in the *same
  working tree* on the same branch, and its `1021159` ("plan: revise Wave C")
  swept up every mid-flight T12 file — all five new instructions, `state.rs`,
  `errors.rs`, `lib.rs`, the IDL, `params.genesis.json` and the suites. The
  content is correct and the tests pass against it; only the history is
  mislabelled, and two later commits sit on top, so **it was not rewritten** —
  rewriting shared history under a live session is a worse bug than a wrong
  commit message. T12's own commit therefore carries the tests and the plan
  only, and says so.
  **The lesson is about `git add -A`, not about that session.** One checkout,
  two agents, and a stage-everything commit takes whatever the other one has
  half-written. If two sessions must share a tree, stage explicit paths; if they
  can, use separate worktrees.

- **2026-08-12 · T12 · test time must come from the validator, never
  `Date.now()`.** A local validator's `Clock::get()` drifts behind wall time as
  slots slip, so a suite that decides "the term has ended" from the host clock
  gets `TermNotEnded` back from a chain that has not caught up — which reads
  exactly like a program bug and is not one. Cost an hour. `auction.ts` reads
  `getBlockTime(getSlot())` and loops until the chain agrees. The same trap is
  waiting in T13 (epochs) and T28 (the retirement clock).

- **2026-08-12 · T13 · the faucet can never drain the vault, so T10's pending
  case needed a different key.** T10 left "leaves supply above target when the
  vault cannot cover a burn" pending and pointed at T13, on the reasoning that
  the faucet would move tokens out of the vault. It does — but it **stops paying
  at the floor**, so it can never take the vault below 50% of supply, while the
  case needs the vault holding less than one burn. What actually reaches that
  state is **sustained contraction**: a burn lowers the vault's share as well as
  the supply (50/100 → burn 10 → 40/90 = 44%), so a long enough tightening walks
  the vault down until a burn outruns it. That is years of real M2 history, so
  the case is now driven by `mock_fund` — the same stand-in the auction uses —
  and the suite has no pending cases left. Worth generalising: *"the faucet will
  make this reachable"* was an assumption about a mechanism that had not been
  built yet, and the floor is exactly the feature that makes it false.

- **2026-08-12 · T13 · chai's ordering assertions reject a BigInt, and fail
  like a broken program.** `expect(x).to.be.greaterThan(y)` / `.at.most` /
  `.at.least` throw *"expected 887046740000000 to be a number or a date"* when
  handed a BigInt — which fails the test with a message that reads like the
  arithmetic was wrong, while the arithmetic is fine. Five faucet cases failed
  this way at once. Every amount in this program is a u64 that does not survive
  a `Number`, so ordering is asserted as a boolean with both operands in the
  message (`atLeast`/`atMost`/`above` at the top of `faucet.ts`). `sync_m2.ts`
  had already hit this and worked around it inline; the same trap waits in T28,
  T29 and T14.

- **2026-08-12 · T15 · the peg has a last number, and nothing had ticketed it.**
  `supply = k × M2` and an SPL token's supply is a `u64`, so the largest M2 this
  coin can represent is `u64::MAX / k` = **18,446,744,073,709 — $18,446.7
  trillion, 797× today's.** Past it `sync_m2` fails the overflow check in
  `target_supply`, and because `previous_m2` only advances on success it fails
  **forever after**. At the historical median month that is **107 years away**.
  Found by accident: a 150-year probe threw `MathOverflow` out of the
  simulation.
  **It is the same shape as the bug T29 deleted** — an absolute constant
  measured against an exponentially growing M2 — and it is the one instance
  that cannot be designed away, because the token standard picks the width.
  Ruled at T15: **do not postpone it.** Dropping `k` by 1,000 buys another
  century and costs the headline; 107 versus 217 years is not a difference an
  artwork notices; and T28's ending already covers it gracefully (the peg
  stops, a year of silence passes, anyone may `retire`, nothing is stranded and
  the auctions go on at the last prices). Now pinned as a test so a future `k`
  cannot shorten the artwork's life quietly, and stated in the program README,
  which previously claimed the coin ends "ideally never".
  **The general lesson for anything still unbuilt:** T29 removed the *tunable*
  constants that were timers. The untunable one is the width of the integers,
  and it is worth checking any new field against that before T22 makes it
  permanent.

- **2026-08-12 · T15 · a simulation reports a number whatever you ask it.**
  Three separate times the harness printed a confident, plausible, wrong
  figure, and each looked like a program bug rather than a harness bug: (1)
  133 "deadlocked releases" in the historical replay, which was the program's
  genesis release date of zero meeting the *negative* unix timestamps of
  pre-1970 observations (T14); (2) "nobody can ever afford anything" across the
  whole record, which was a price ladder expressed in absolute tokens being
  applied to a 1959 money supply seventy-seven times smaller than the one it
  was derived from; (3) *negative* waiting times, because a cohort's
  `claimsIn` receives the chain's **absolute** epoch index (north of twenty
  thousand today), so a latecomer told to arrive at "epoch 400" arrived
  immediately. All three now have their reasoning written next to the code.
  The habit that caught all of them was the same: **when the harness reports
  the exact failure it was built to detect, suspect the harness first.**

- **2026-08-12 · T28 · `program.idl` is camelCase, so an IDL shape test can
  claim the auction vanished.** `h.program.idl.instructions` presents
  **camelCase** names, so a test asserting the interface still contains
  `place_bid` fails while the same test's `claim` passes — it reads as "half the
  program is gone". This is `chain/README.md`'s "Anchor emits two IDLs that
  disagree" turning up somewhere new: the committed `chain/idl/*.json` is
  snake_case, the in-memory `Program.idl` is not. `initialize.ts`'s allowlist
  already carries both spellings for exactly this reason and is the pattern to
  copy. The better fix, where it is available, is to stop asserting shape and
  assert behaviour — the case now places two bids and withdraws one on a retired
  chain, which proves the thing the shape test was only gesturing at.

- **2026-08-12 · T28 · Anchor refuses an extra signer, which is how you prove
  an instruction has none.** `.signers([stranger])` on an instruction whose
  account list contains no `Signer` fails with `unknown signer: <key>` — the key
  is not in the account list, so web3.js will not attach it. Convenient as a
  proof, useless as a way to *run* the thing as somebody else: for that, build
  it with `.instruction()` and send a raw `Transaction` with the stranger as fee
  payer. Both forms appear in `retire.ts`, doing different jobs.

- **2026-08-12 · T30 · a default build can publish a stale IDL, so run T9's
  grep every time.** After deleting the two instructions, `./stack build`
  (default) published an IDL that no longer contained `settleRent` or
  `foreclose` — but *still* contained `set_mock_m2`, which a default build must
  never carry. An identical second `./stack build` later produced the correct
  file. Verified in isolation, so the obvious suspects are cleared: **neither
  `./stack test <suite>` nor `./stack reset` republishes the IDL**, despite both
  building. Root cause not pinned further (incremental-build reuse is the
  likely candidate) and not chased, because the guard is cheap and already
  specified: **T9's validation grep is the check, and it has to be run rather
  than assumed.** The staged commit was briefly wrong in exactly this way and
  the grep is what caught it. Practical rule for T12 onward: a default
  `./stack build` plus `! grep -q set_mock_m2 chain/idl/emperors_new_coin.json`
  immediately before `git add`, every time the instruction set changes.

- **2026-08-13 · T20 · 🔴 Anchor needs `Buffer` on the global, and the read half
  of a page hides it.** `chain/README.md` said `chain-kit` imports `buffer`
  explicitly "so a consuming app needs no polyfill setup". That is true of every
  PDA this toolchain derives and **false of every instruction Anchor encodes**:
  `BorshInstructionCoder.encode` calls `Buffer.alloc` against the global, inside
  a dependency nobody here can edit. So T19's page — all reads — worked
  perfectly, and the first T20 button threw `Buffer is not defined` with a stack
  naming none of it. Every unit test, the typecheck and `npm run build` passed
  with the bug in place, because nothing but a browser has this gap. Fixed in
  the **app** (`apps/web/src/buffer-global.ts`, imported first in `main.tsx`)
  rather than in `chain-kit`/`chain-react`: a library that silently mutates
  `globalThis` on import is a worse neighbour than an app that says what it is
  installing. README corrected.

- **2026-08-13 · T20 · 🔴 Every account subscription was waiting for
  finalisation.** `ConnectionProvider` was given a `wsEndpoint` and no
  commitment, so web3.js defaulted the connection to `finalized` and every
  `onAccountChange` inherited it. **Measured: 12.5 seconds** between a
  `roll_term` landing and the open page showing the new term — long enough that
  a term shorter than that (the test ledger's twelve seconds) can never be seen
  live at all, and long enough on any ledger to read as a broken page rather
  than as a commitment level. Worse, it disagreed with `useSendTransaction`,
  which has always confirmed at `confirmed`: the two halves of one click
  believed different things about when it happened. Fixed in `SolanaProvider`
  (`commitment: 'confirmed'`), which is generic and names no program. Lag on the
  same measurement afterwards: under seven seconds, the remainder being local
  validator and headless browser.

- **2026-08-13 · T20 · 🔴 A generic error humaniser destroys the specific one
  downstream.** `useSendTransaction` caught the failure, rewrote it as "The
  program rejected this (error 0x1780)" and rethrew a **new** `Error` — so the
  page's own mapping had nothing left to read and rendered the hex code to the
  user. Caught only by clicking a button that fails in a real browser; the unit
  tests passed because they fed `encErrorMessage` the shapes it expected. Fixed
  on both sides: `useSendTransaction` now carries the original as `cause`
  (generic, and strictly better for any consumer), and `encErrorName` follows
  `cause` *and* recognises the humanised wording. Both cases are now regression
  tests.

- **2026-08-13 · T20 · Anchor's two IDLs disagree about error names too.** The
  documented gotcha was about *field* names; it applies to the error table as
  well. `chain/idl/emperors_new_coin.json` carries `MathOverflow`, the generated
  `.ts` carries `mathOverflow`, `ENC_IDL` is the JSON wearing the `.ts` file's
  types, and what a running program logs — and puts in `errorCode.code` — is the
  Rust one. A lookup table typed off the compiler's view compiles cleanly,
  matches nothing, and degrades silently to hex codes in front of users. Noted
  in `chain/README.md`.

- **2026-08-13 · T20 · The test ledger's twelve-second term is effectively
  unbiddable from a browser**, and it is the ledger's fault rather than the
  page's. Between notification lag and a term shorter than a minute there is a
  window of a few seconds in which the bid form exists at all. Nothing to fix —
  the shipped term is thirty days — but anyone verifying the auction by hand on
  localnet should expect to need a script holding a slot on a fresh term, or a
  ledger initialised with a longer one. Recorded because it will otherwise look
  like a page bug to whoever tries it next.
