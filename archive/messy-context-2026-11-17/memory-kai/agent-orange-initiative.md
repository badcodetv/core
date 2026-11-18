---
name: agent-orange-initiative
description: "Agent Orange — BadCode's autonomous-agent framework released as art-software; locked design decisions"
metadata: 
  node_type: memory
  type: project
  originSessionId: 35df2540-887a-4815-8ee4-007982f16715
---

**Agent Orange** is a planned BadCode initiative: a TypeScript framework for running autonomous
organisations, released as an art-object whose form IS the message. Master design spec (approved
2026-06-20): `docs/superpowers/specs/2026-06-20-agent-orange-design.md`. Engineering substrate:
`docs/AGENTS_RESEARCH.md`.

Locked decisions (don't relitigate without the user):
- **Architecture:** "scopes, not personas" — one worker archetype recursively engaged under
  **mandates**. Magentic-One steward + append-only **ledger** (memory) + **refer up**/consent.
- **Name = Agent Orange:** a deliberate, provocative reminder of the technology's power to destroy
  (indictment of the pattern, not its victims; needs BadCode's voice to stay legible).
- **Stance:** double-edged gift — inevitability acknowledged, better branch pointed at, the reader
  has a role. The reliability rules are recast as **worker protections = the owner's conscience**;
  the bad branch must be an explicit, logged override. The constraints ARE the politics.
- **Vocabulary:** labor / means-of-production register ALL THE WAY to the API (worker, mandate,
  engage, the steward, the plan, the ledger, attest, refer up, consent, the keys, budget,
  overreach, the floor, shifts, calls, the owner). **Chemical vocabulary was considered and CUT** —
  the name carries the double edge; the code speaks one clean register.
- **Substrate:** TypeScript, standalone repo, API key (not Max), self-built triggering.
- **First use case:** dogfood — BadCode's own marketing org. Phases 0→3 (runtime "hiring" last).

Ties to [[gitpush-origin-master-arc]] (the "Future Proof" good-branch idea: redesign orgs with
software-engineering tenets). Related: [[project-overview]].

**FOUNDATION PIVOT (2026-06-20).** Agent Orange is now founded on **`agentkit`** — an existing,
production-grade Go agent runtime at `/home/kai/projects/bayesprice/Platinum/agent-library` (module
`github.com/bayes-price/agentkit`; Go core ~23K LOC + TS in-image agent + React chat UI; status per
its README "design complete · code ~45-50%"). Decision: **adopt agentkit wholesale and use it AS
Agent Orange from now on. The TypeScript Phase 0 skeleton (built earlier at `/home/kai/projects/agent-orange`)
is ABANDONED — ignore it.**

Why: agentkit already does the real use cases the TS skeleton couldn't — configurable INTERACTIVE
sessions from {system prompt, base image/custom image, MCP servers, skills}, Docker/DinD container
management + snapshot/commit, first-class multi-tenancy/namespacing (ContextScope{Customer,Job,...}),
Postgres persistence + replay, pluggable harness (claude-agent-sdk), and an `ask_user` human-in-loop
event. It IS "the floor" (Layer 1) that AGENTS_RESEARCH §8 said to borrow.

What agentkit LACKS (= the old Agent Orange differentiators, now "later, maybe"): scheduler/triggers
(shifts/calls), runtime sub-agent spawning (event hook only), long-term/semantic memory (conversation
text-search only — no ledger/RAG), and the BadCode art/vocabulary layer.

**FOUNDATION IMPORTED (2026-06-20).** agentkit copied into a NEW local git repo at
`/home/kai/projects/badcode/agent-orange` (413 files, no remote). `cd go && go build ./...` is GREEN
(Go 1.24). Layout: runtime core at root; `installations/` (platinum-base/core-v1/core-v2 image defs as
baseline); `migration-reference/` (Platinum host-side image pipeline — resolver, build scripts, `stack`,
agentdeps, ACR design — copied to PORT, not keep). Migration plan committed at `agent-orange/MIGRATION.md`.

KEY MIGRATION FINDINGS: image pipeline is SPLIT — runtime registry layer (imageregistry interface +
ociregistry push/pull + blobarchive + customimages catalog) is liftable & in-repo; but image *building*
(`Build()`) is STUBBED in agentkit — Platinum host does `docker build`. Today pushes to Azure ACR; ZERO
GCP. The one blocker for GCP is AUTH (ociregistry hardcodes basic user/pass; Artifact Registry needs
oauth2 access token / service account). Plan phases: 1 standalone-ify (re-module from github.com/bayes-price/agentkit),
2 genericize installations, 3 registry-agnostic build+push (auth abstraction + implement Build()),
4 GCP Artifact Registry (priority), 5 automation.

DECIDED (2026-06-20): Go module = `github.com/binocarlos/badcode-agent-orange` (re-moduled, build green).
Installation images live in the ENGINE repo at `agent-orange/installations/` as EXAMPLES (moved out of
badcode), layered: sandbox harness → `core` (minimal, product-neutral root: coreutils/curl/jq/etc, no
Platinum) → `example` (parent:core, the per-project template). Real per-project images live in each
PROJECT's own repo (same installation.json+Dockerfile+overlay contract). The engine repo now has a
`CLAUDE.md` operating guide (what it is, repo map, run/build, liftability/no-Platinum rules). Platinum installations archived to `agent-orange/migration-reference/platinum-installations/`.
GCP integration plan (MIGRATION.md Phase 4): (4a) artifacts+snapshots → ONE GCS-backed `extension.BlobStore`
(go/extension/gcsblob, mirror filesblob) — artifacts ARE already in the repo (go/artifacts ArtifactStore +
go/agentdb/artifacts.go + filesblob ref; no cloud backend yet, go.mod has no cloud deps); (4b) images →
Artifact Registry via ociregistry + oauth2-token auth seam. STILL OPEN: GCP project/region/AR-repo/GCS-bucket
+ auth method (SA key vs workload identity/ADC).

NEXT-SESSION GUIDANCE: continue the GCP/engine work in a FRESH Claude Code thread with cwd =
`/home/kai/projects/badcode/agent-orange` (its own CLAUDE.md auto-loads; go/docker/git target the right repo).
That thread has its OWN per-project memory — this badcode-thread history won't carry over, but agent-orange/CLAUDE.md
+ MIGRATION.md make it self-orienting.

Parked: IP — agentkit is bayesprice-owned; fine for PRIVATE use, public release needs licensing resolved.
Earlier TS work (master spec/plan, labor vocabulary, scopes-not-personas in badcode's docs/superpowers/) is
historical context, NOT the build.

**ORCHESTRATION LAYER DESIGNED + PLANNED (2026-06-25).** In the AGENT-ORANGE repo, on branch
`docs/steward-board-orchestration` (off main, NOT pushed): the design spec
`docs/specs/2026-06-25-steward-board-orchestration-design.md` (commit bcc46ad) + the Phase A
implementation plan `docs/plans/2026-06-25-steward-board-phase-a-plan.md` (commit 3145b84). Phase A
= board + ONE hand-driven worker (no loop, no steward yet): per-session `Env` seam on
`CreateSessionRequest`, `go/orchestrator/board` (models+store, sqlite-tested), `go/orchestrator/boardapi`
(token-authed HTTP), `sandbox` env-gated tool registration (`requiresEnv`) + board tool plugins +
worker protocol, `go/cmd/orchestratord` hand-post host. Phases B-E scoped out.
**CONSOLIDATED (2026-06-25):** both docs now merged into `main` (= `phase4-gcp-seams` = commit d4b87c1,
GCP work + docs together; the `docs/steward-board-orchestration` branch is now redundant). A WORKTREE for
implementation exists at `/home/kai/projects/badcode/agent-orange-phase-a` on branch `feat/phase-a-board`
(off main; plan+spec present). Execute Phase A in a FRESH thread with cwd=that worktree (agent-orange
CLAUDE.md auto-loads; go/sandbox/git target the right repo). Nothing pushed to origin. Task 7 host-wiring
needs aligning with live `cmd/agentd` source. Approach A (board-centric), locked decisions:
- **Postgres is the single source of truth**; every component is a STATELESS loop/turn over it (crash/restart = non-event).
- **Dumb dispatch loop** (host-side daemon, NO LLM) embeds the agentkit `Runner`: promote→claim(CAS)→launch session→reclaim/budget. Separate from the LLM steward.
- **The steward = a worker under orchestrator-tier keys**, re-engaged on a shift (scopes-not-personas: same archetype, different keys). It posts mandates; it never does the work and cannot spend/post.
- **engage = async, board-mediated** (post a mandate row; loop launches it; result returns via the board/parent-handoff). Synchronous in-run subagent (Approach C: `EngageSubagent`) DEFERRED.
- **5 board tables:** mandates · mandate_runs · mandate_deps (DAG) · ledger (work record) · memory (vectorized stream, SEPARATE from ledger — one ticket→many memories).
- **The keys = env-gated tools** (Hermes `check_fn` pattern): tools appear in the model schema only when their env flag is set; spend/credential never gated on at a leaf. Net-new in engine: per-session `Env` on `CreateSessionRequest` (small) + conditional tool registration in `sandbox/`. Everything else is a host app (board API + MCP toolset + loop + scheduler + call intake).
- **refer-up reuses agentkit `ask_user`**; blocked workers are SNAPSHOTTED and resumed via `Runner.Resume` (suspend-for-days-then-resume — a payoff Hermes can't do). **attest** = quality gate on output (auto/verify-worker/owner), distinct from refer-up (permission gate).
- Build PHASED: A (board+one worker, hand-driven) → B (loop) → C (shifts/calls) → D (steward+engage+memory) → E (fan-out). First plan = Phase A(+B).

Reference: **Hermes** (NousResearch) is the load-bearing verified reference for the board/dispatcher/worker-protocol; decision is COPY its design, not its code, and build on agentkit (NOT run Hermes — its single-host SQLite/PID model fights containerized workers). Build-vs-buy + Hermes internals captured in this thread's research.

**CORRECTION (2026-06-25):** the agent-orange repo NOW HAS a remote (`git@github.com:binocarlos/badcode-agent-orange.git`) — the earlier "no remote" note above is STALE. Treat commits there as publishable; don't push without the owner asking. Currently on branch `phase4-gcp-seams`.
