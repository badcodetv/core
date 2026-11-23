# Build log: Future Proof simulation

Goal: [`GOAL.md`](./GOAL.md). Branch: `future-proof/simulation`. Newest entry first under **Log**.

## Decisions

- **D1. Bob can't publish a private page.** On 23 Nov a plain Bob chat (Sonnet) reported no Artifact
  tool and no `claude` CLI.
  - Bob's own file viewer is private behind Bob's sign-in, but it is sandboxed with no JavaScript, so
    it can't run the loop animation.
  - So: a claude.ai cloud **routine** republishes the private artifact each day, if routines have the
    Artifact tool. A one-off probe routine checks this (`trig_01HGvNtmvTooXfhXmjXJC7n7`).
- **D2. The repo is public** (`badcodetv/core`, `isPrivate: false`). The simulation's data files are
  readable on GitHub like the rest of the government's work. "Private" means the page: a private
  claude.ai artifact, never linked from badcode.tv.
- **D3. Daily data goes on its own branch, `simulation/live`.** Bob workers push there directly, with no
  PR and no merge, as Kai decided.
  - main gets no daily bot commits.
  - The site doesn't redeploy.
  - Code, schema and worker prompts live on main, arrive through the one PR, and sync to Bob on merge.

## Log

- 23 Nov: branch created; Bob capability probe done (D1); repo visibility checked (D2); cloud probe routine scheduled for 17:58 UTC; distributions researcher started.
- 23 Nov: **D4. Cloud routines can publish.** A one-off probe routine had `Artifact`, `ArtifactComments` and `ArtifactData`, listed artifacts, and cloned `badcodetv/core`. So the private page is a claude.ai artifact, republished by a daily routine. A Bob file-viewer page would be private too, but it can't run JavaScript.
- 23 Nov: built `scripts/government/sim/` (`issue.mjs` schema and validator, `lot.mjs` draw by lot, `feed.mjs`, `sim.mjs` command line, `make-pool.mjs`, `bob-setup.sh`), with 17 tests passing. Pool: 1,000 people from `distributions.json` (ONS mid-2025, Census 2021 E&W, Commons Library 2024 results).
- 23 Nov: seven worker prompts (`docs/government/workers/sim-*.md`) and `docs/government/simulation/{README.md, worker-common.md}`. `sync-bob.mjs` now takes `include: simulation`, and `bob-sync.yml` watches `worker-common.md`.
- 23 Nov: **D5. Thames Water's news date is 10 Nov, not inside 16–22 Nov.** The fact-checker found no dated Thames rescue story from 12 to 17 Nov; the latest is Smart Water Magazine on 10 Nov. The seven replayed days are therefore 10 Nov (Thames) and 17–22 Nov.
- 23 Nov: **D6. The backfill's topics were assigned up front,** so six clerks could run in parallel without picking the same topic. Each is a real weight-2 or weight-3 UK item from that day's digest, and each field is new, so queue rule 2 (longest wait) applies honestly:
  - 17 Nov: energy (the price cap)
  - 18 Nov: migration (the asylum support charge)
  - 19 Nov: youth jobs (the Milburn review)
  - 20 Nov: policing (Local Police Commands)
  - 21 Nov: EU trade (the summit deal)
  - 22 Nov: high-street jobs (the Poundland sale)
- 23 Nov: **D7. Answer C goes through Bob's Codex in a plain chat** for local replays, because the local Codex CLI hung. The live run uses the `sim-rival` worker on Codex.
- 23 Nov, Thames, first real numbers:
  - **Citizens** (Haiku): about 93k subagent tokens, about 2 minutes. Split: 37% of simulated citizens said yes, against 74% in the real YouGov poll; 35% were unsure.
  - **Answers A and B** (Sonnet): about 46k tokens each, about 5 seconds each.
  - **Answer C** (Codex `gpt-6`): one chat.
