---
name: solana-toolchain-initiative
description: "Solana toolchain + Emperor's New Coin — plan at design/2026-08-06-solana-toolchain-and-emperors-new-coin.md; key oracle/economy decisions and the research that forced them"
metadata: 
  node_type: memory
  type: project
  originSessionId: 11d2f141-7886-4a3c-81f2-9ebdea6adf7f
  modified: 2026-08-11T12:03:46.553Z
---

**PROGRESS 2026-08-11: the toolchain is DONE and proven. Next is T7 (ENC
program state + math).** T24-T27 shipped: Docker toolchain (no host Rust/Solana/
Anchor), the `counter` demo program + `/dev/counter` page as a portability
harness, and **`./stack`** at the repo root as the ONLY local entry point
(`badcode` and `chain` are node_modules/.bin symlinks, NOT on PATH — never write
them in docs or UI copy). **Copied into the forum repo and committed there**
(/home/kai/projects/forum/forum, commit 28940ab, branch verification-manifest):
chain/ self-contained with the CLI at chain/cli, client libs at
frontend/src/solana/{kit,react}, verbs prefixed `chain_`. Forum's frontend is
yarn + router5 + MUI, no root package.json — that shaped the layout.

**The full loop is verified end to end, not assumed** (CDP browser, real
transactions): edit Rust -> `./stack redeploy counter` (~90s) -> generated types
change -> Vite **hot-swaps the component** (no page reload; React Fast Refresh) ->
deleting a Rust field fails `tsc` at the exact line. Only unverified link:
Phantom's own connect/sign click (needs a real extension).

**Five bugs found by attacking it, all fixed — do not reintroduce:**
- **`Buffer` does not exist in browsers** and Vite does not polyfill it; PDA
  derivation threw on first wallet connect. chain-kit imports it explicitly.
- **Anchor emits two disagreeing IDLs**: `.json` = Rust names (`updated_at`),
  `.ts` = camelCase (`updatedAt`). A bare `BorshAccountsCoder` does NOT convert,
  so fields read `undefined` while TS says otherwise. Decode via
  **`useProgramReader`** (wallet-free Program).
- **Docker seccomp blocks io_uring**, which Agave 3.x asserts on -> fresh ledger
  dies with a trace never mentioning Docker. `seccomp:unconfined` on the
  validator service only.
- **Solana allocates the program's EXACT length**, and growing it later fails
  ("ExtendProgram was superseded by ExtendProgramChecked") — so any struct change
  was undeployable. First localnet deploys reserve 500KB, and that step
  **bypasses Anchor because `anchor deploy -- --max-len N` silently DROPS
  everything after `--`** despite documenting the opposite.
- **chain-cli assumed an npm workspace root**; now finds Anchor.toml (CHAIN_DIR
  overrides).

**Do NOT add @types/react overrides/resolutions pre-emptively** — badcode (npm)
needs them because wallet-adapters pull v19; adding them to the forum (yarn)
CREATED a duplicate and broke an unrelated file. Add only against a real error.
Set **CHAIN_PROJECT** per repo (badcode-chain / forum-chain): both publish 8899,
only one validator can run at a time.

**PROGRESS 2026-08-10: T1-T6 + T16 DONE and committed** (toolchain track
complete). Packages built: `@badcode/chain-cli` (doctor/up/down/status/build/
deploy/test/idl/airdrop, own bin, portable), `@badcode/chain-kit` (clusters,
registry, PDA), `@badcode/chain-react` (provider, useProgram(idl,programId),
useAccount, useSendTransaction, ClusterBadge). `chain/` Anchor workspace builds+
deploys+tests. `/coins/enc` route live (lazy, 508kB chunk). Next: T7 (program
state + math). **Pinned toolchain, hard-won — see chain/versions.json:** Rust
1.97.1 (NOT the advertised 1.89 MSRV; avm needs 1.91+), Agave 3.1.10 (NOT 4.x —
`avm install` picks it and overwrites yours; install Anchor BEFORE Solana),
Anchor CLI 1.1.2 built `--from-source` (prebuilts need glibc 2.39, Ubuntu 22.04
has 2.35), `@coral-xyz/anchor` TS client 0.32.1 (versions independently of the
CLI). **`anchor test` needs `--validator legacy`** — Anchor 1.x defaults to
surfpool, which isn't installed. `anchor test -- --grep X` does NOT filter; use
`--script`.

2026-08-06: BadCode is releasing Solana coins. Plan written (Kai-approved,
23 tickets): `design/2026-08-06-solana-toolchain-and-emperors-new-coin.md`.
Two tracks — a reusable in-monorepo toolchain (`chain/` Anchor workspace,
`packages/solana-kit`, `packages/solana-react`, `badcode chain` CLI commands,
coin pages at `/coins/:slug` in the single existing web app) and **Emperor's
New Coin** as its first consumer. Finish line is **devnet**, not mainnet.

**Why this shape:** Kai explicitly refuses a standalone crypto repo, and
refuses any coin whose supply BadCode can change ("the joke is that not even
we can change what the Fed decides"). Coin #2 must write only a Rust program
and a page component — no plumbing. That's the toolchain's success test.

**Four deep-research passes** drove the design (Switchboard; oracle landscape;
trust-minimization; engagement economics). Load-bearing findings, because they
are non-obvious and expensive to rediscover:

- **Switchboard On-Demand has no feed authority** — a feed *is* the hash of its
  fetch job, so no key can repoint it. Avoid their "Authority-Updated Feeds"
  product; that IS the backdoor. **PROVEN LIVE 2026-08-10** (T16 done): one
  character changed → completely different feedHash; re-store unchanged →
  identical hash. Evidence + production job committed at `chain/feeds/`. The
  hard gate is cleared; the artistic claim is safe to publish.
- **The feed job is static forever** (bytes = identity), so no rolling date
  param. It fetches the whole M2SL series and the regex MUST be end-anchored —
  a first-match pattern returns 286.6, i.e. M2 in **January 1959**. Against an
  immutable program that is unrecoverable.
- **M2 is available keyless** (Fed Data Download Program + fredgraph.csv, CSV
  not JSON). `api.stlouisfed.org` needs a key; going keyless is what keeps the
  feed permissionless, since Switchboard's secrets service was shut down.
- **Use M2SL (monthly, seasonally adjusted), not WM2NS** — the weekly series
  isn't seasonally adjusted and spikes every December on holiday cash.
- **H.6 is monthly since Feb 2021** — fourth Tuesday, 1pm ET.
- **zkTLS on Solana is dead** — Reclaim's verifier is an abandoned 2024 demo
  (1 witness, expired validity). Shipping it would be *less* trustworthy than
  a quorum while sounding more trustless.
- **UMA/Polymarket doesn't port** (EVM-only; whale-swung dispute votes).
- **Token-2022 interest-bearing is cosmetic only** — display-only decay.
- **Harberger without a carrying cost is inert** — the tax, not the forced
  sale, is the turnover engine.

**Decisions Kai made (don't relitigate):** level-targeting supply
(`supply = k × latest M2`, so revisions and QT use the same burn path — Kai's
own correction, replacing a proposed ratchet); the 50% vault floor governs the
*faucet*, not the burn (burning lowers the vault's share, so it can't be a hard
invariant); rent from day one (~5%/day) with permissionless foreclosure; no
identity system (fixed-per-epoch faucet pot + Invariant M make sybils harmless
— the faucet is **register in epoch N, collect your share of pot(N) in N+1**,
because dividing a *current* pot by a *previous* headcount lets a farm drain
100× the pot; that bug was caught in adversarial review, don't reintroduce it);
classic SPL for ENC (DEX-listable) but Token-2022 permanent delegate for the
ten asset NFTs (that's what makes force-buy work); cosmetic decay lives in the
*website*, not the chain.

**The honest claim** — say "we removed ourselves from the loop", never "nobody
can affect this but the Fed" (Switchboard's queue authority governs which
oracles may sign). Our own program ships non-upgradeable, which is what makes
"not even we can change the rule" literally true.

**Below the floor, NOTHING pays out** — not the epoch share and not the welcome
grant. Floor-gating only the pot would let fresh wallets drain a depleted vault
forever via grants. "Arrive during the tightening and there's nothing for you"
is the intended austerity beat, not a gap.

**Environment split (Kai, confirmed):** localnet = mock oracle only, never
Switchboard; **devnet = staging**, where the real oracle integration is proven
before mainnet. No local Switchboard clone — cloned oracle accounts are frozen
snapshots nothing re-signs, so they can only prove stale-quote decoding.

**Token authorities:** freeze authority MUST be `None` (else BadCode holds a key
over holders' coins). Mint authority stays forever — so risk scanners will
permanently flag ENC as arbitrarily inflatable. Kai's call: that is a **feature,
quote it in our own copy** — a money-printing coin flagged by the machines as a
money-printing risk is the joke landing for free. Never try to suppress it.

Canon lives at `docs/stories/magic-money-tree/emperors-new-coin.md`; ENC is a
cryptocurrency cross-promoted with [[magic-money-tree-refounding]], not a comic.
Kai's asset-NFT layer (ten parody assets, printer-set always-for-sale prices,
forced sales) is his own invention on top of the original ENC concept.
