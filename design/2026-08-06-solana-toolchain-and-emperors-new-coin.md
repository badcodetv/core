# Solana Toolchain & Emperor's New Coin — Design & Implementation Plan

> **EXECUTION RULES (for agents):** Work ONE ticket at a time, in order unless
> dependencies say otherwise. Only the orchestrator changes ticket Status;
> workers may only append to Notes and the Discovered Issues Log. A ticket's
> checkbox is checked only after its Validation commands have been re-run by
> the orchestrator and pass. Do not expand scope; log surprises in the
> Discovered Issues Log instead.

Status: in progress — **15 of 27 done, T11 code complete. Next: T12, after the T11 delegate ruling.**
Date: 2026-08-06
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
| ✅ | T16 · Switchboard feed authored, immutability **proven live** | oracle |
| ✅ | T7 · program state, `math.rs`, placeholder genesis params | program |
| ✅ | T8 · `initialize` + `init_asset` ×10 | program |
| ✅ | T9 · oracle trait + MockOracle behind a Cargo feature | program |
| ✅ | T10 · `sync_m2` — supply targeting, the core | program |
| 🟡 | T11 · rent accrual, `settle_rent`, `foreclose` — code done, 7 tests need T12 | program |
| ⬜ | **T12 · `buy_asset` — the forced sale** ← **you are here** (needs the T11 ruling) | program |
| ⬜ | T13 · the faucet — register-now, collect-next-epoch | program |
| ⬜ | T14 · economic simulation harness | economics |
| ⬜ | T15 · choose the genesis parameters | economics |
| ⬜ | T17 · stand the M2SL feed up on devnet | oracle |
| ⬜ | T18 · Switchboard on-chain read + crank (**wall-clock stall: budget a day**) | oracle |
| ⬜ | T19 · ENC page, read-only state | web |
| ⬜ | T20 · ENC page, wallet actions + the melting balance | web |
| ⬜ | T21 · documentation | docs |
| ⬜ | T22 · devnet deploy + **burn the upgrade authority** | ship |
| ⬜ | T23 · end-to-end verification | ship |

**T7–T13 are one continuous run** — each builds on the last, all in Rust, all
validated by `./stack cargo test …` and `./stack test test-…`. Nothing in that
stretch needs devnet, Switchboard, or a browser.

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
| `chain/programs/emperors-new-coin/src/state.rs` | `Config`, `Printer`, `Asset`, `FaucetEpoch`, `Player` |
| `chain/programs/emperors-new-coin/src/errors.rs` | `ErrorCode` enum |
| `chain/programs/emperors-new-coin/src/math.rs` | Supply targeting, rent accrual, price interpolation (unit-tested) |
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

| Instruction | Signer | Effect |
|---|---|---|
| `initialize(params)` | deployer, once | ENC mint (6dp, mint authority = vault PDA, **freeze authority None**), vault, `Config` (immutable), `Printer`; bootstrap supply from a hardcoded genesis M2 the first `sync_m2` corrects |
| `init_asset(index)` | deployer, once each | One `Asset` PDA + its Token-2022 NFT (permanent delegate + metadata), held by the vault. Gated by `Config.initialized_assets` |
| `sync_m2()` | **anyone** | Validate quote → retarget supply → mint to / burn from vault → rescale prices. Rejected until all 10 assets exist |
| `claim()` | anyone | Pay share of `pot(N−1)`; pay welcome grant if new and grants remain; register for epoch `N` |
| `buy_asset(index)` | anyone | Settle seller rent, pay 100% of price to seller, move NFT, reassign |
| `settle_rent(index)` | **anyone** | Push accrued rent from holder to vault |
| `foreclose(index)` | **anyone** | If rent debt > holder balance and grace elapsed: asset → vault, caller gets bounty |
| `close_epoch(n)` | **anyone** | Reclaim rent-exemption from a settled `FaucetEpoch` (n ≤ current−2) to the closer |
| `set_mock_m2(v, d)` | anyone | **Compiled only under `--features mock`** |

`Config` is written once at `initialize` and has no mutating instruction. The
upgrade authority is burned at T22.

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

### T11: Rent accrual, `settle_rent`, `foreclose`   [Status: code DONE 2026-08-11, tests part-blocked on T12 | Model: opus]
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

### T12: `buy_asset` — the forced sale   [Status: pending | Model: opus]
- **Scope:** Anyone buys any asset at the current interpolated price. Atomically:
  settle the seller's rent, pay 100% of the price to the seller (or the vault if
  the Emperor holds it), move the NFT via the permanent delegate, reassign the
  `Asset`, reset `last_touched`. **Create the seller's ENC ATA if absent**
  (idempotent create, buyer pays) — otherwise a seller without an ATA could block
  their own forced sale, defeating the no-refusal guarantee. No cooldown. Emit an
  event with buyer, seller, index, price, slot.
- **Files:** `chain/programs/emperors-new-coin/src/instructions/buy_asset.rs`,
  `chain/tests/buy_asset.ts`.
- **Acceptance criteria:** Seller receives exactly price minus rent owed; the NFT
  lands in the buyer's token account; the holder cannot block the sale **even with
  no ENC token account**; buying from the vault routes payment to the vault;
  supply unchanged; rapid back-and-forth buying succeeds with rent correctly
  settled each way.
- **TDD:** yes
- **Validation:** `./stack test test-buy`.
- **Depends on:** T11
- [ ] done
- Notes:

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
- [ ] done
- Notes:

### T14: Economic simulation harness   [Status: pending | Model: opus]
- **Scope:** A TypeScript harness replaying real historical M2SL (including the
  2022–23 contraction — the first sustained decline since the 1930s) through the
  program's math, with synthetic player populations including a sybil-farm
  cohort. Reports vault share, asset turnover, time-to-first-asset, and whether
  Invariant M holds. Depends only on `math.rs`'s TS mirror, **not** on the
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
- [ ] done
- Notes:

### T15: Choose the genesis parameters   [Status: pending | Model: opus]
- **Scope:** Sweep parameters with the T14 harness and commit the chosen values
  to `chain/params.genesis.json`, replacing T7's placeholders. Record the
  rationale and the rejected settings in `chain/sim/RESULTS.md`.
- **Files:** `chain/params.genesis.json`, `chain/sim/RESULTS.md`.
- **Acceptance criteria:** Over the full historical replay: the vault never goes
  negative; **Invariant M holds in every epoch in which all ten assets are held by
  players**; a new player can afford the cheapest asset on day one via the welcome
  grant; assets turn over at least once per week on average under a moderate
  population. Values are produced by the harness, not hand-written.
- **TDD:** no (parameter selection); the invariants are asserted by T14's harness.
- **Validation:** `npx tsx chain/sim/index.ts --report --params chain/params.genesis.json`
  exits 0 with all invariants green.
- **Depends on:** T14
- [ ] done
- Notes:

### T16: Switchboard feed — author it and prove immutability   [Status: mostly done 2026-08-10 | Model: opus]

> **DONE:** immutability proven live against Crossbar (one character → different
> feed hash; re-store → identical hash), production job authored and stored, both
> keyless sources verified to agree. Evidence and job committed at
> `chain/feeds/README.md` + `chain/feeds/m2sl.job.json`. **The hard gate is
> cleared — the artistic claim is safe to publish.**
> **REMAINING:** add DBnomics as a median-aggregated second source (needs the
> JSONPath-to-last-element shape tested; its `observations=1` does not limit the
> response), and mint the mainnet-queue feed at launch.
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
  **Schedule note:** one acceptance criterion needs a quote that genuinely aged
  on devnet, so budget a **calendar day** between cranking and asserting. T19–T23
  sit behind this — it is a wall-clock stall in the critical path, not a work
  estimate. Start the aging clock as soon as the read path compiles.
- **Files:** `chain/programs/emperors-new-coin/src/oracle.rs` (real impl),
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

### T19: ENC page — read-only state   [Status: pending | Model: sonnet]
- **Scope:** Live M2 readout, total supply, vault balance and share with the floor
  marked, next H.6 release countdown (fourth Tuesday, 1:00pm ET), and the ten
  assets with prices interpolating every slot. Works with no wallet connected.
  Add the account decoders and `currentPrice`/`rentOwed` to chain-kit.
- **Files:** `apps/web/src/coins/enc/{Printer,AssetGrid}.tsx`, `enc.css`,
  `packages/enc/src/accounts.ts`, `packages/enc/src/idl/emperors_new_coin.ts`.
- **Acceptance criteria:** Prices visibly tick without a refresh; account changes
  push through the websocket subscription; the page renders with no wallet; the
  countdown is correct across a DST boundary.
- **TDD:** yes for countdown and price math; no for presentation.
- **Validation:** `npm run test --workspace @badcode/chain-kit`; `npm run build`;
  manual check at `/coins/enc` against localnet.
- **Depends on:** T18, T6
- [ ] done
- Notes:

### T20: ENC page — wallet actions and the melting balance   [Status: pending | Model: sonnet]
- **Scope:** Connect, claim (showing whether it's the welcome grant, a share of
  yesterday's pot, or zero — and why), force-buy, rent owed, settle rent. Errors
  surface a human cause, successes an explorer link. Plus the melting balance: the
  displayed ENC decays continuously while the chain holds the true number, with a
  quiet discoverable tell (hover/tap reveals the truth). Copy per `docs/voice.md`.
- **Files:** `apps/web/src/coins/enc/Wallet.tsx`, `AssetGrid.tsx` (extend), `enc.css`.
- **Acceptance criteria:** Full loop against localnet with Phantom: claim → buy →
  watch rent accrue → a second wallet force-buys it. Rejected transactions show a
  readable cause, not a raw program error code. The melting number is always one
  interaction away from the truth and involves no on-chain state.
- **TDD:** no (UI wiring; logic is tested in the program and kit)
- **Validation:** `npm run build`; manual two-wallet run-through on localnet.
- **Depends on:** T19
- [ ] done
- Notes:

### T21: Documentation — toolchain, coin, canon   [Status: pending | Model: sonnet]
- **Scope:** `chain/README.md` (install → run → deploy → **how to add coin #2**).
  `docs/coins/emperors-new-coin.md` — the public design including the honest trust
  statement: what we can say ("we removed ourselves from the loop") and what we
  must not ("nobody can affect this but the Fed"), naming the Switchboard
  queue-authority residual explicitly, stating the true supply invariant as
  `supply ≥ k × M2`, and **quoting the scanner warning as a selling point** —
  ENC genuinely is arbitrarily inflatable, that is the entire coin, and the
  PDA/non-upgradeable explanation sits beside it rather than apologising for it.
  Resolve the open thread at
  `docs/stories/magic-money-tree/emperors-new-coin.md:151`. Add the toolchain to
  `CLAUDE.md`'s repo map.
- **Files:** `chain/README.md`, `docs/coins/emperors-new-coin.md`,
  `docs/stories/magic-money-tree/emperors-new-coin.md`, `CLAUDE.md`.
- **Acceptance criteria:** A reader goes from clean WSL to a running localnet ENC
  using only `chain/README.md`. **No claim in the docs is unsupported by code** —
  in particular the supply invariant and the trust statement.
- **TDD:** no (docs)
- **Validation:** Follow `chain/README.md` from a clean shell; every command runs.
- **Depends on:** T20
- [ ] done
- Notes:

### T22: Devnet deploy + burn the upgrade authority   [Status: pending | Model: opus]
- **Scope:** Deploy to devnet against the feed T17 already created, run
  `initialize` + ten `init_asset` calls with the T15 parameters, then **burn the BPF upgrade
  authority to `None`**. Publish the feed hash, the raw job JSON, and the
  standalone crank script. Flip the timeline node to `live` and update
  `diorama.test.ts` accordingly.
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
  2. Against **devnet**, through `/coins/enc` in a browser with Phantom: connect →
     claim → buy an asset → observe rent accruing → a second wallet force-buys it →
     settle rent → a third wallet forecloses a delinquent asset.
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

## Discovered Issues Log

_(appended by executors during implementation)_
