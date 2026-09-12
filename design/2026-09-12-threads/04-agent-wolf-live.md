# Thread 04 — Agent Wolf: live so friends can log in

You are in `~/projects/badcode/agent-wolf`. Read `README.md`, then in `../agent-bob`: `README-stack.md`
(§ "Agent Wolf: the joint development workflow" and § "What is real here, and what still differs from a
deployment"), `design/2026-08-20-agent-wolf.md` (Executor orientation, Local topology and networking, and
the ticket list — all O and W tickets are marked done), and `docs/ops.md` Step 11 (how Bob is laid out on
the OVH box) and Part 3 "Add a new app".

## Goal

Agent Wolf (the trading-hypothesis app: a user states a thesis, an interview sharpens it into a falsifiable
spec, a daily job researches and scores it) running on the OVH box behind Caddy with Google sign-in, so
that a named list of Kai's friends can log in and test it. Wolf runs on Agent Bob, so this thread starts
after thread 02 (Bob stable) and needs a box from thread 01.

## What done looks like

1. A `design/2026-09-12-wolf-deployment.md` in `agent-bob` that turns README-stack's "local versus
   deployed" table into concrete steps for the box: the Wolf compose layer on `/srv/apps/wolf`, its
   backed-up thin volume, the Caddy block, the Google OAuth authorized origin for the real domain, the
   `wolf` project merged into Bob's project map with its allowlist, secrets in the password manager.
2. Executed on the box, with the tester allowlist from Kai. A tester can sign in, state a hypothesis,
   complete the interview, and see it on the board the next day.
3. A one-page "for testers" note (plain words, no identifiers) Kai can send to friends, plus a
   `docs/testing-feedback.md` in agent-wolf describing where feedback lands.
4. A local dry run first: `./stack wolf up mock` from `../agent-bob` (free), then the real one with Kai's
   yes.

## 🔴 Ask Kai

- The tester list (Google emails) and the domain for Wolf.
- Before `./stack wolf up` without `mock` (billable), and before anything on the box that costs money.
- The one manual step README-stack names: registering the origin on the Google OAuth client.

## House rules

Two checkouts, both shared: commit per ticket, stage only your files, never push, don't switch branches.
Validation is the rule that cost the most (design doc § "The Validation rule"): re-run it, don't trust a
report. Rundown style.

## First action

Read the documents; run `./stack wolf up mock` from `../agent-bob` and report whether the local topology
still comes up green. Then reply with the deployment plan at outline depth and the two questions above.
