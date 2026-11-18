---
name: enc-program-build
description: "ENC on-chain program: 26/31 tickets, Rust CODE-COMPLETE + page built on feat/enc-program; ceiling law is 1/2C not 1/C; the mock-binary deploy hazard; peg horizon; Anchor/browser gotchas worth not rediscovering"
metadata: 
  node_type: memory
  type: project
  originSessionId: 11d2f141-7886-4a3c-81f2-9ebdea6adf7f
  modified: 2026-08-13T21:32:42.462Z
---

**Branch `feat/enc-program`.** Plan and per-ticket notes:
`design/2026-08-06-solana-toolchain-and-emperors-new-coin.md` — progress board
at the top, Discovered Issues Log at the bottom, self-contained (no thread
context needed). See [[solana-toolchain-initiative]] for the toolchain before
it and [[enc-architecture-rulings]] for the rulings it implements.

**2026-08-13: 26 of 31 tickets done. The Rust program is CODE-COMPLETE** and the
page is built. T31 (Gazette), T19 (read-only page), T20 (wallet actions +
melting balance) and T21 (docs + claim ledger) all landed, each validated by the
orchestrator re-running its gates rather than trusting the executor. Remaining:
the oracle (T16–T18), shipping (T22–T23). T11's rent code is superseded and
deleted; history only, at `9a94fa3`.

**Everything left needs devnet, keys, or a human decision** — there is no more
autonomous work on this branch. Note all green suites run under the `mock`
cargo feature: `oracle::read_quote`'s real path is still a stub returning
`OracleUnavailable` and the crate has no Switchboard dependency, so **a default
build cannot sync at all until T18.**

**T31 was NEVER blocked on Jack** — the plan said so and it was wrong. Ruling D
makes slot personalities genesis naming + frontend presentation over one shared
mechanism, so the program was built with placeholder names; the sheet is
consumed at T22.

**Four things owed a human before T22:**
1. Jack's Gazette slot sheet — and it must now reach **two places**: `init_asset`
   (on-chain NFT metadata) and `AssetGrid.tsx`'s `FURNITURE` array. Better fix:
   have the grid read the name from metadata and delete the array.
2. **The tenancy certificate URI.** `mint_certificate` mints with an **empty
   URI** and sets update authority to `None` in the same instruction, so the one
   object a human actually receives renders as nothing in every wallet, forever.
   Any HTTPS URI instead binds the artwork to one domain staying alive — the
   operational dependency the whole design exists to avoid. **Genuinely Kai's
   call; no agent should invent a host.**
3. Ratification of one creative call made on the documented recommendation:
   **retirement keeps the auctions trading** rather than freezing them. Chosen
   because a freeze would have had to keep every escrow exit alive anyway or
   strand live bids, so "keep trading" is the safe option as well as the better
   one, and it costs no code.
4. A read of the **peg-horizon finding**, below.

**THE PEG HAS A LAST NUMBER (T15, 2026-08-12).** `supply = k × M2` and an SPL
token's supply is a `u64`, so the largest M2 ENC can represent is
**$18,446.7 trillion — 797× today's, about 107 years out** at the historical
median month. Past it `sync_m2` fails the overflow check and, because the
baseline only advances on success, fails **forever after**. It is the same shape
as the bug T29 deleted and the one instance that **cannot be designed away** —
the token standard picks the integer width. **Ruled: state it, don't postpone
it.** Dropping `k` by 1,000 buys another century and costs the headline ("one
ENC per $1,000 of America's money"); T28's ending already covers it gracefully.
Pinned as a test in `chain/sim/sim.test.ts` and stated in the program README,
which no longer claims the coin ends "ideally never".

**Parameters are chosen and recorded** — `chain/sim/RESULTS.md` is the record,
`chain/sim/sweep.ts` reproduces it. The load-bearing results: every combination
tried keeps the peg alive (so every choice is about legibility, never safety);
the **price ladder is parts per million of supply, never tokens** (a price in
tokens is the T29 time-bomb shape again); and the **ceiling law**.

**⚠ THE CEILING LAW IS `1/2C`, NOT `1/C` — corrected 2026-08-13.** `C` diligent
claimants each reach a `1/2C` share of everything ever printed, so a slot
costing `1/2C` of supply is out of reach for `C` of them. **The faucet passes
through only HALF of each release**, because the floor is half of a *growing*
supply: every token minted raises the floor by half a token, so the vault must
retain half of each release simply to stay level with itself, and only the
other half is ever above the floor for the pot to be a fraction of. Pass-through
is `1 − floorBps`, and the floor is a half. The cheapest column therefore
supports about **five thousand** diligent claimants and the masthead about
**fifty** — published as ten thousand and a hundred until this was re-derived.
The sweep's own table had already refuted it, in the cell beside the claim, and
nobody read it that way. **T15 still stands**: its pass/fail was a measurement,
not the law, and the error ran in the safe direction.

**The ladder is now load-bearing twice.** `params.genesis.json`'s
`genesisPricePpm` is mirrored in the program as `GENESIS_PRICE_PPM`, and
`init_asset` recomputes the expected base units and refuses anything else
(`WrongGenesisPrice`). Editing one without the other fails deployment at asset 0
with both figures logged — deliberately, because the by-hand multiplication it
replaced lived only in a test file.

**Design decisions NOT in the ticket text** (all in the plan's Notes, all cheap
to revisit before T22):
- Bootstrap gates on the loader's own **ProgramData upgrade authority**, not a
  hardcoded key — otherwise a stranger could `initialize` between deploy and our
  first transaction and pick every parameter forever. `claim` gates on all ten
  assets existing for the same window.
- The ENC mint and the ten NFT mints are **PDAs**; no deployer keypair ever
  holds a mint.
- **Three parameters are `Config` fields purely so tests can reach the
  behaviour**: `term_seconds`, `epoch_seconds`, `retirement_silence_seconds`.
  The harness runs 12s / 15s / 25s; `params.genesis.json` keeps the shipped
  values, and `initialize.ts` asserts the substitution so it is visible.
- The welcome grant keys on `welcome_grant_taken`, not "is this wallet new", so
  arriving below the floor or after the day's allotment does not cost you it.

**Gotchas found 2026-08-13, the expensive half:**
- **A validation or dev-loop command must not mutate tracked files.** `./stack
  check`, `test`, `reset` and `start` all rewrote the committed `chain/idl` —
  so test-under-mock then check then commit shipped an interface for a build we
  never release. Fixed in two places (a `syncIdl` unit test pointed at the real
  repo root, and `BuildOptions.publishIdl`). **Prove it by diffing `chain/idl`
  either side of a full suite run**, not by reading the code.
- **🔴 `./stack test` leaves the MOCK `.so` in `target/deploy`, and `deploy`
  never rebuilds.** `set_mock_m2` is unauthenticated by design and `mock_fund`
  drains the vault to any named wallet, so a mock build burned at T22 would hand
  the money supply to any passer-by, permanently. Now guarded: builds write a
  feature marker beside the artifact (cleared by the next default build) and
  `assertDefaultBuild` refuses a feature build on any non-localnet cluster.
- **`Buffer` does not exist in browsers and Anchor needs it.** `chain-kit`
  imports it for PDA derivation, so the *read* half of a page works and the
  first button throws. Every unit test and the typecheck pass with the bug in.
  The app must put `Buffer` on the global itself.
- **`ConnectionProvider` with no commitment defaults to `finalized`**, so
  `onAccountChange` waits ~32 slots — measured 12.5s — while
  `useSendTransaction` confirms at `confirmed`. The two halves of one click
  disagree about when it happened.
- **Anchor types every `u64`/`i64` as `any`**, so a `BN` reaching a `bigint`
  compiles, builds, and throws only in the browser. Convert at one boundary.
- **Anchor's two IDLs disagree about ERROR names as well as field names**, and
  `errorCode.code` carries the *Rust* name. A table typed off the generated view
  matches nothing and degrades silently to hex codes.
- **Growing an account can break an instruction that never touched it.** `Asset`
  at 414 bytes overflowed Anchor's 4KB BPF stack frame in `place_bid`; the only
  symptom is "Access violation in stack frame 5…", naming neither the account
  nor Anchor. Box the account.
- **The research briefs are argument-grade, not copy-grade.** A "5% M2 growth"
  used for an order-of-magnitude comparison got printed as fact; the real figure
  is 6.73%/yr since 1959. Likewise "M2 fell 13 months in a row" — it is **nine**,
  and the wrong number had already spread into code comments. **Re-derive from
  `chain/sim/m2-history.csv`; never quote a table.**

**Gotchas found the hard way, do not rediscover:**
- **Anchor 1.x `CpiContext::new` takes a `Pubkey`**, not an `AccountInfo`.
- **Anchor runs `init` BEFORE bare `constraint =`**, so an authority gate does
  not short-circuit account creation. A test must aim at a *fresh* account.
- **Anchor rejects `.signers([x])` on an instruction with no Signer account**
  ("unknown signer") — handy as proof of signerlessness, useless for running it
  as somebody else. Build the ix and send a raw `Transaction` with them as fee
  payer.
- **`program.idl` is camelCase; the committed `chain/idl/*.json` is snake_case.**
  An IDL shape test looking for `place_bid` fails while `claim` passes. Better
  still: assert behaviour, not shape.
- **`anchor build -- --features x` DOES forward** (unlike `anchor deploy`). But
  features are per-package — build that program alone. A `--features` build must
  not publish the IDL, and a default build can publish a *stale* one, so run the
  `! grep -q set_mock_m2 chain/idl/*.json` check every time before committing.
- **ts-mocha cannot resolve TS-importing-TS as ESM**; suites run on mocha + tsx.
- **chai's ordering assertions reject BigInt** ("expected N to be a number or a
  date") and fail like a broken program. Compare as booleans, print both sides.
- **Test time must come from the validator** (`getBlockTime(getSlot())`), never
  `Date.now()` — the local validator drifts behind wall time.
- **Never edit `chain/` while `./stack test` is building.** It compiles whatever
  is on disk; a mid-flight edit kills the run and the failure looks unrelated.
- A struct change needs `./stack reset` or existing accounts fail to decode.

**Testing conventions:** suites are re-runnable against a persistent ledger and
`this.skip()` rather than pass when a case needs a fresh chain. **`retire.ts` is
TERMINAL** — it ends the ledger's peg, so it is excluded from the
run-everything script and lives behind `./stack test test-retire`; reset after.
`mock_fund` (mock builds only) stays deliberately: it is the only way to reach a
vault below its floor or too small to cover a burn, states the real economy
takes years to produce.

**When a simulation reports the exact failure it was built to detect, suspect
the harness first.** Three plausible-but-wrong figures came out of `chain/sim`
before the numbers were trustworthy — see the plan's Discovered Issues Log.
