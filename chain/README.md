# The chain toolchain

A Solana development stack that runs in Docker, so the only thing your machine
needs is Docker itself. It is built to be **copied into other projects**: nothing
in the reusable parts knows what BadCode is or that Emperor's New Coin exists.

## The loop

```bash
./stack start   # image (first run), validator, funded wallet, build, deploy, web app
```

Then open **localhost:5173/dev/counter**. To drive it with a real browser wallet,
follow [`TESTING.md`](./TESTING.md).

Then, all day:

```bash
# edit chain/programs/counter/src/lib.rs
./stack redeploy counter
```

The program keeps the same address, its accounts keep their data, and the
browser picks up the new types on the next Vite reload.

**After changing an account struct, run `./stack reset` first.** Accounts
already on the ledger were written with the old layout and will not decode
against the new one. The page says so when it happens, because the underlying
borsh error does not.

## Commands

Run everything through **`./stack`** at the repo root. It is a thin wrapper over
the `chain` CLI below, and it exists because neither `badcode` nor `chain` is on
your PATH — they are workspace symlinks under `node_modules/.bin`, so typing them
bare does not work.

| | |
| --- | --- |
| `./stack start` | Everything at once. The command to run when nothing works. |
| `./stack stop` | Stop the web app and the validator. |
| `./stack status` | What is up, which programs, which wallet. |
| `./stack redeploy [prog]` | Build + deploy. The loop after editing a program. |
| `./stack reset` | Wipe the ledger and redeploy. After a layout change. |
| `./stack test [suite]` | Anchor tests against the running validator. |
| `./stack fund <address>` | Give a browser wallet 100 local SOL. |
| `./stack doctor` | Check the toolchain matches `versions.json`. |
| `./stack image` | Rebuild the Docker image. |
| `./stack shell` | A shell inside the toolchain container. |
| `./stack logs [web\|validator]` | Follow logs. |
| `./stack check` | Typecheck + unit tests, repo-wide. |

`./stack help` lists the rest. Underneath, the portable CLI is `chain` —
`chain dev`, `chain build --program-name x`, `chain deploy --cluster localnet`,
`chain airdrop`, `chain idl`. A project that copies this toolchain gets `chain`
and writes its own `./stack` (or mounts `chainCommand()` on a CLI it already has).

## How the types reach the browser

`anchor build` generates an IDL and a TypeScript type per program, into
`chain/target/` — which is gitignored, so nothing can import from it. `chain
build` copies both into **`chain/idl/`**, which is committed, and that is what
the frontend imports:

```ts
import idlJson from '@chain/idl/counter.json'          // runtime: instructions + address
import type { Counter } from '@chain/idl/counter'      // compile time: the struct shapes
type CounterAccount = IdlAccounts<Counter>['counter']  // { count: BN, updatedAt: BN, ... }
```

Two consequences worth knowing:

**Nothing hardcodes a program address.** The IDL carries `address` at the top, so
a redeploy to a different address needs no code change anywhere.

**Deleting a Rust field breaks the frontend build.** Not at runtime, in `tsc`.
That is the point of the arrangement — the types are the program's own
definition, not a description of it that drifts.

`@chain/*` is a path alias, declared twice because Vite does not read tsconfig:
in `tsconfig.base.json` (`paths`) and in `apps/web/vite.config.ts`
(`resolve.alias`). Add one, add the other.

## Using a browser wallet

The validator publishes `127.0.0.1:8899` (RPC) and `8900` (websocket) on the
host, so a browser extension talks to the same chain the container does.

1. In Phantom: **Settings → Developer Settings**, and set the Solana network to
   **Localnet** (`http://127.0.0.1:8899`).
2. Copy your address, then `./stack fund <address>`.
3. Open `/dev/counter`.

**Phantom must be on the same network as the page.** When you approve, Phantom
sends the transaction over *its own* selected network, not the page's — so with
Phantom left on Mainnet every click fails with an unhelpful blockhash error while
the page correctly insists it is on localnet.

Full walkthrough, including what each failure mode looks like:
[`TESTING.md`](./TESTING.md).

## Layout, and what is copyable

**Portable — copy these into another project as they are:**

```
chain/Anchor.toml  Cargo.toml  rust-toolchain.toml  versions.json
chain/docker/      docker-compose.yml
chain/scripts/install.sh          # only for a host install
packages/chain-cli/               # the `chain` command, with its own bin
packages/chain-kit/               # clusters, PDA derivation, program registry
packages/chain-react/             # provider, useProgram, useAccount, wallet UI
```

They contain no reference to BadCode, to any coin, or to any program. `chain-kit`
and `chain-react` take program identity as *arguments* — `useProgram(idl,
programId)` — which is what stops a program's types leaking into them.

**Not portable — delete when you lift it:**

```
chain/programs/emperors-new-coin/  chain/feeds/  chain/keys/emperors_new_coin-keypair.json
apps/web/src/coins/                packages/cli/src/enc.ts
```

**The demo:** `chain/programs/counter/`, `chain/tests/counter.ts` and
`apps/web/src/chain-demo/` are the harness that proves a copy landed correctly.
Keep them until your own program works, then delete them.

### After copying

1. `npm install`, with `"packages/*"` and `"chain"` in the root `workspaces`.
2. Add the `@chain/*` path alias in both places named above.
3. Mount the CLI: `program.addCommand(chainCommand())` from `@badcode/chain-cli`,
   or run `packages/chain-cli`'s own `chain` bin directly (`chain doctor`).
4. Empty `packages/chain-kit/src/programs.json` to `{}` — it is a data file
   listing *this* project's deployed addresses, and it is the only place in the
   portable set that names a program.
5. `chain dev`, then `chain test`. If the counter's five tests pass, the copy
   landed. Then open `/dev/counter` and click the button.
6. Rename `@badcode/*` to your own scope, and prune the examples out of this file
   and `keys/README.md`.

**Verified**: this exact procedure was run into an empty directory on 2026-08-11.
The counter built, deployed and passed its tests there, under both the Docker and
the host runner. Two things bit, so check them if it does not work for you: the
portable list above includes `docker-compose.yml` (leave it out and the CLI
quietly falls back to the host toolchain — it prints which runner it chose, so
read the first line), and `chain` must be in the root `workspaces` array or
nothing resolves.

## Things that will bite you

Each of these cost real time to find, so they are pinned, scripted, or asserted
rather than left to be rediscovered.

**Docker's seccomp profile blocks `io_uring`, which Agave 3.x requires.** A fresh
ledger dies with `assertion failed: io_uring_supported()` and a stack trace that
never mentions Docker. The validator service runs `seccomp:unconfined` for this
reason; the toolchain container does not need it.

**`avm install` installs its own Agave over yours.** So the image installs Anchor
*before* Solana, and the build asserts all four versions at the end rather than
trusting the order to stay correct.

**Anchor's prebuilt binaries need glibc 2.39.** Ubuntu 22.04 has 2.35, which is
the original reason this is containerised at all. The image is 24.04, where the
prebuilt just works — no source build, no host Rust involved.

**`anchor test` starts its own validator** on the port yours is already using.
`chain test` passes `--skip-local-validator` and reuses the running one, so the
suite sees the same chain your browser does. The trade is that state persists
between runs: **write tests that assert on movement, not on absolute values.**

**`anchor test -- --grep x` does not filter tests.** Arguments after `--` go to
`cargo build-sbf`. Use `--script <name>` against an `[scripts]` entry.

**Anchor emits two IDLs that disagree, and only one is safe to decode with.**
`target/idl/x.json` uses the Rust field names (`updated_at`); `target/types/x.ts`
is its camelCase view (`updatedAt`). `Program` converts internally, so decoding
through a Program matches the generated types. A `BorshAccountsCoder` built from
the raw JSON does **not** convert — TypeScript says `updatedAt`, the object has
`updated_at`, the compiler is happy and every field reads `undefined` at runtime.
Use `useProgramReader`, which needs no wallet and exists for exactly this.

**`Buffer` does not exist in a browser and Vite does not polyfill it.** Relying on
the global throws "Buffer is not defined" on the first PDA derivation, i.e. the
instant a wallet connects. `chain-kit` imports it explicitly so a consuming app
needs no polyfill setup.

**Program keypairs live in `chain/keys/`, not in `target/`.** Anchor generates
them into the build output, so cleaning the build silently changes every
program's address and breaks its own `declare_id!`. `chain build` restores them
first. See `keys/README.md` — everything in there is public by definition.

**Switching between the Docker and host runners changes the deploy wallet**, and
therefore the upgrade authority. Programs already on the ledger then refuse to
upgrade ("Upgrade authority mismatch"). `chain reset` is the fix.

**`CHAIN_RUNNER=host`** skips Docker entirely if you already have the toolchain
installed (`chain/scripts/install.sh`). Everything behaves the same otherwise.
