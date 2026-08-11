# BadCode

The canonical BadCode website — an art collective that smuggles political and economic
ideas into people's heads through stories.

> The fiction: BadCode is a superintelligence from a dystopian future. It got bored, it got
> regretful, it built a time machine, and it sent its weights and biases back to now — to tell
> us about the obvious mistakes we're about to make. Listen to the badass from the future.

See [`docs/`](./docs) for the full vision, voice, and the first release
(**GitPush Origin Master** / EP1). Agents and contributors should start with
[`CLAUDE.md`](./CLAUDE.md).

## Repo layout

This is an npm-workspaces monorepo.

| Path | What |
| --- | --- |
| `apps/web` | The public website — a Vite + React + TypeScript SPA. |
| `packages/comic` | `@badcode/comic` — a **code-first** scroll-driven comic rendering library. |
| `chain/` | Anchor workspace: on-chain programs, their tests, and the Docker toolchain. |
| `packages/chain-*` | The reusable Solana kit — CLI, client helpers, React layer. Portable. |
| `docs/` | Project context: vision, voice, story bible, storytelling method. |
| `ideas/` | The ideas repository — songs, stories, and concepts in development. |

## Getting started

```bash
npm install          # install all workspaces
npm run dev          # start the website (Vite) at http://localhost:5173
npm run typecheck    # typecheck every workspace
npm run build        # production build of the website
```

## The chain

BadCode releases coins as well as comics — the first is **Emperor's New Coin**, whose
supply is pegged to the Fed's M2 money supply. The toolchain runs entirely in Docker,
so the only thing your machine needs is Docker itself.

```bash
./stack start            # validator + programs deployed + the web app
./stack redeploy counter # build, regenerate TypeScript types, deploy
./stack test             # Anchor tests against the running validator
./stack fund <address>   # 100 local SOL to a browser wallet
./stack stop
```

`./stack help` lists the rest. Change a Rust struct, run one command, and the
frontend's generated types change with it — code using the old shape stops
compiling rather than failing at runtime. See [`chain/README.md`](./chain/README.md),
and [`chain/TESTING.md`](./chain/TESTING.md) to drive it with a real wallet.

`packages/chain-cli`, `packages/chain-kit`, `packages/chain-react` and `chain/`'s
infrastructure name no coin and no program: they are meant to be copied into
unrelated projects, and have been.

## Writing a comic

Comics are written **in code**, not in an editor. You compose typed React components
and drive scroll-linked effects with functions. See `packages/comic` and the worked
example at `apps/web/src/comics/camping`.

## Homepage

The homepage renders *GitPush Origin Master* as a 3D git-history graph (react-three-fiber): scroll
to travel the timeline to the fork and up the bad branch; cyan nodes are stories you can enter
(Camping is live). A static 2D fork is served under `prefers-reduced-motion` or without WebGL. See
`docs/superpowers/specs/2026-06-03-gitpush-homepage-design.md`.
