# Thread 02 — Agent Bob: resume the onboarding fleet and make Bob stable

You are in `~/projects/badcode/agent-bob`. Read `CLAUDE.md`, then the **RESUME HERE** block at the top of
`design/2026-09-11-onboarding-work-plan.md`, then the design it implements
(`design/2026-09-11-onboarding-and-the-guide.md` §0, §3, §4.1, §5.1, §6).

## Where it stands

The fleet was paused mid-wave on 2026-09-11. On `main`: A1 (revert on the Activity rail), A3 (operator
claim, budget guard, default budgets, whoami) and A6 (project-map reload) are merged, but the full
`go test ./...` has **not** been re-run on the merged tree. Five branches hold finished-but-unverified
work committed as `WIP (fleet paused …)`: A2, A4, C1, C3, C4 — the table in the RESUME HERE block names
each branch. `main` is 9 commits ahead of origin and unpushed.

## Goal

Finish the onboarding plan so a new project's first hour works: the architect interview survives
navigation, the token budget is visible and operator-only, the guide is served in the console, the Desk
narrates firsts, and the stack e2e (D2) covers all of it. This is the stable Bob that thread 04 (Agent
Wolf live) and thread 03 (the three real projects) build on.

## Procedure — follow the RESUME HERE block exactly

1. `cd go && go test ./...` on `main` (~8 min; `agentdb` alone ~470 s). Fix before anything else.
2. For each WIP branch spawn one agent in its worktree (`.claude/worktrees/agent-<id>/`): "finish ticket
   <id>: re-run its Validation, fix, amend the WIP commit into a real one, report". Merge green branches
   into `main` in the order A4, A2, C1, C3, C4. A2, C3 and C1 all touch `App.tsx`; A2 and C3 also share
   `DeskPage.tsx` and `Sidebar.tsx` — expect small conflicts. Run the web gates after each web merge.
3. Wave 2: A5 (budget panel), A7 (operator docs), C2 (About this screen), C5 (Desk narrates firsts).
4. Wave 3: D1 (merge + full gates), D2 (stack e2e — needs port 8080 free and Docker), B7 (Ellen fixture
   + screenshots).
5. Append every agent's Notes to its ticket and every surprise to the Discovered Issues Log.

## Execution rules (from the plan; they bind you)

- One ticket per agent at a time. Only the orchestrator (you) changes a Status or ticks a box, and only
  after re-running that ticket's Validation yourself.
- Stage only the ticket's files. Sentence-style commit messages. **Never push.** Don't switch branches
  in the main checkout.
- Every claim in a Note is something you ran or read, with `file:line` or a command.
- Kai said on 2026-09-11: "full autonomy and as much parallelism as possible". Use it, within the file
  ownership the plan gives each ticket.

## 🔴 Ask Kai

- The default daily token limit (env `AGENTKIT_DEFAULT_DAILY_TOKENS_HARD`; the hole marked
  `<!-- Kai: default daily limit -->` in `docs/guide/money.md`). Ships off until set. Ask on the first
  reply with a recommended number, then carry on with everything else.
- Anything billable (`./stack … up` against real providers). `mock` twins are free — prefer them until
  D2 needs the real thing, then ask.

## First action

Run step 1. While it runs, read the five WIP branches' last commits. Reply in the Rundown style with the
test result, the branch table with what each needs, the token-limit question, and the agents you are
spawning.
