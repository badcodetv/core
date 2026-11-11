# GOAL: make the BadCode government a working demonstration of Future Proof

Set by Kai, 2026-11-11. The orchestrator reads this whole file before doing anything.

## The ruling

The government is not a satirical news machine. It is proof that Future Proof's three tenets can
run a government:

1. **Composition over inheritance.** Policies are separate modules, judged one at a time, never a bundle.
2. **Continuous integration.** Every change is small, reviewed and reversible, with its undo stated.
3. **Data-driven decisions.** No policy without a stated experiment: what we measure, what we
   predict, when we check, and what makes us undo it.

The end point is a platform that ANY agent in the world can join to debate and test policy, one
BadCode doesn't own and nobody has to trust (Solana). We prove the shape in git with our own agents
first, then design the chain. "We can't own the platform that the agents use to coordinate a better
government": that is both the point and the marketing pitch.

## Your role

You are the orchestrator. Plan it, break it into milestones, run subagents and Workflows as you see
fit (Kai opts in to multi-agent orchestration for this goal), review the work adversarially, and
keep going without asking Kai about details.

Read first: `CLAUDE.md`, `docs/government/README.md`, `docs/government/shared.md`,
`docs/stories/gitpush-origin-master/future-proof.md`, `docs/stories/future-proof/`,
`docs/marketing/the-reader.md`, `docs/voice.md`, `chain/README.md`,
`docs/coins/emperors-new-coin.md` (for how we state trust honestly), and the memory
`government-is-future-proof-demo`.

## Milestones

Each one ends in a PR for Kai or Jack to merge, plus a short status page.

- **M1 Foundations.** Rewrite the three founding pledges in `shared.md` as the three tenets. They
  had drifted to "test every law / publish the postmortem / name who it leaves out"; keep what is
  good in those inside the tenets. Write the design doc in this folder: the vision, the
  policy-module format, the debate model, the chain end state, and the open questions.
- **M2 Policy modules.** One file per policy: the claim, who it is for and who it leaves out, the
  experiment, the evidence, the undo condition, the status. Migrate the ten manifesto pages into
  modules; ministers own modules instead of writing essays. A linter enforces that no module lacks
  an experiment.
- **M3 Real debate.** Replace the single cabinet voice with agents that genuinely disagree: at
  least a proposer, an opposition, and a statistician who blocks any claim that can't be measured.
  Debates become public logs next to each module. Changes go through `docs/government/workers` and
  the Bob sync. Never edit Bob by hand.
- **M4 Public face.** The site's GOVT channel shows the modules, their experiments and status, the
  debate behind each, and the undo history, so a stranger can see all three tenets at a glance.
- **M5 The open platform.** Design the Solana program: a second program built on the generic chain
  kit, with no BadCode-specific code in `chain/` or `packages/chain-*`. Cover how outside agents
  submit, debate and stake on predictions, Sybil resistance (one person faking many accounts), and
  what an LLM may and may not judge. Build and test it on the local validator only (`./stack`).
  Write the "invite the world's agents" pitch for the chief-of-staff to hold.

## Hard lines

Do not cross any of these without Kai's explicit yes.

- Nothing reaches `main` without Kai or Jack merging. The cabinet's daily output keeps its ONE
  rolling PR rule; this goal's work goes on its own branches and PRs.
- Nothing is posted publicly. Statements stay proposals.
- No mainnet or devnet deploy, no real tokens, no deposits or money of any kind. `shared.md` says
  the government asks nobody for money, and changing that is Kai's call. Anything that pays out on
  outcomes is a UK gambling-law question: flag it, don't build it.
- Never write "no admin key", "trustless" or "can't be censored" unless it is literally true. State
  the blast radius of any key, the way the coin's trust statement does.
- The satire and the narrator's voice stay as the surface. The reader is the working-class UK
  reader in `the-reader.md`, so the chain is plumbing, never the headline.
- Bob is a separate repo. If the government needs a Bob feature, write the request; don't build it.

## Checking in with Kai

- Only at the end of a milestone, or when you hit a hard line. At most three decisions at a time,
  ranked by what they unblock, each with your recommendation.
- Otherwise decide yourself, write the decision and why into the design doc, and keep moving.
- Mind the shared WebSearch budget (about 200 per session, across all subagents).

## Done

A stranger landing on the GOVT channel can see policies as separate modules, every change small and
undoable, every policy with an experiment and its result, agents debating in public, and a tested
design for the world's agents to join on-chain, waiting only for Kai's go-ahead.
