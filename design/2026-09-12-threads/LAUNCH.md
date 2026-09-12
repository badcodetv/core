You are an agent taking ownership of ONE thread of BadCode's 2026-09-12 work programme. Kai is running
several Claude sessions at once, one per thread, from a single planning folder. Everything you need is
on disk; this message tells you where, and the two-digit number on its last line tells you which thread
is yours.

## Where the plan lives

The planning folder is, by absolute path:

    /home/kai/projects/badcode/badcode/design/2026-09-12-threads/

Read these, in this order, before doing anything else:

1. `README.md` in that folder — the map of all nine threads and the ones that must not run together.
2. `../2026-09-12-work-board.md` (that is `/home/kai/projects/badcode/badcode/design/2026-09-12-work-board.md`)
   — the digest of Kai's brain-dump that all nine threads came from, so you know what the others are doing.
3. **Your thread file**: the one file in the folder whose name begins with your two digits
   (`01-…md` … `09-…md`). It is your complete brief: goal, what done looks like, stop gates, house rules
   and your first action. Follow it. Where it and this message disagree, the thread file wins.
4. The `CLAUDE.md` at the root of the checkout your thread works in (see the map below). It is the
   operating guide for that repository and it binds you.

## The map — which checkout each thread works in

| Thread | Works in this checkout | One line | Kai must supply |
| --- | --- | --- | --- |
| 01 | `/home/kai/projects/badcode/agent-bob` | Build the OVH server, move everything off Kubernetes except NoCode and Franchise Cloud | OVH account and card; the Step 0 accounts |
| 02 | `/home/kai/projects/badcode/agent-bob` | Resume Agent Bob's paused onboarding fleet until Bob is stable | the default daily token limit |
| 03 | `/home/kai/projects/badcode/agent-bob` | The first three real Bob projects; the Kai's-WhatsApp connector (W0 proof first); the `agent-enc` storage repo | SSH to Platinum's production host; a yes before the first WhatsApp send |
| 04 | `/home/kai/projects/badcode/agent-wolf` | Agent Wolf live on the box so friends can log in | the tester list and the domain; a box from 01; a stable Bob from 02 |
| 05 | `/home/kai/projects/badcode/badcode` | Camping music-video cut, proving the new listening tools; Imagine Dragons is the reference | Jack's Google sign-in once for the listening browser; a yes per Suno run |
| 06 | `/home/kai/projects/badcode/badcode` | GPOM storyboard stills as a spread of four different ideas per beat, then honed | a yes on the variety rule before any image |
| 07 | `/home/kai/projects/badcode/badcode` | Magic Money Tree: real footage for the war and the NHS, licence verified per item | nothing |
| 08 | `/home/kai/projects/badcode/badcode` | GPOM narration on Suno v6, sheet first; generates only when 05 has released Suno | a yes per Suno run; the Suno hand-off from 05 |
| 09 | `/home/kai/projects/badcode/badcode` | Park the not-now ideas (Ableton, Serum via computer use, Suno-voice-only, more Premiere automation) in the idea inbox | nothing |

If this session was started in a different directory from the one your row names, say so in your first
reply and work in the named checkout by absolute path anyway. Do not `cd` your whole session elsewhere
without saying so.

## Worktree or shared checkout?

| Checkout | Who works there | Rule |
| --- | --- | --- |
| `agent-bob` | 01, 02, 03 | **02 owns the main checkout** — it merges branches into `main` and runs the full Go and web suites, and half-edited code from anyone else in the same tree would fail those runs. **01 and 03 each work in their own git worktree** on their own branch (`git worktree add ../agent-bob-wt-01 -b thread/01-ovh` from the main checkout, or the session's own worktree tool; 03 uses `thread/03-projects`). Merge your branch into `main` yourself only when 02's status file says it is idle and the merge touches only files you own; otherwise leave the merge for 02 or Kai and say so. The connections branch already has its own worktree at `agent-bob-connections`; 03 reads it there and does not merge it. |
| `agent-wolf` | 04 | Alone. Work in the checkout directly. |
| `badcode` | 05, 06, 07, 08, 09 | **Shared, no worktrees.** These threads write documents, prompts, sheets and skill files, and their media lives outside the repo, so collisions are rare and per-file staging handles them. The deciding reason: the Flow, listen and Premiere MCP servers run from the **primary** checkout's source, so a script or server fix made in a worktree is invisible to the browser tools until merged. The one shared hot spot is `scripts/` (browser channel and Chrome launch scripts, which 05 may edit): announce such an edit in your status file before making it. |

## Rules that apply to every thread

- **You own one thread. Do not start, edit or "help with" another.** If your work needs something from
  another thread, say so in your report and stop at that point; Kai relays between sessions.
- **Shared checkouts.** Other sessions are working in the same tree, possibly uncommitted. Commit per
  ticket on `main` with the repo's sentence-style messages, staging **only your own files** (never
  `git add -A`). **Never push. Never switch branches** in the shared checkout; worktrees are fine.
- **Stop gates are absolute.** Every thread file has a 🔴 section. Anything that costs money, spends a
  credit, posts to a person, touches a live service, or needs a human sign-in: prepare it, show the exact
  command or click-path, and wait. Never work around a gate.
- **Every claim is something you ran or read**, with a command or `file:line`. No invented status.
- **Report in the Rundown style**: a one-line TL;DR, an "In plain terms" that assumes the reader has
  forgotten everything, a ✅🟡⬜🔴 state list, "You decide", "Your move". Gloss every identifier the
  first time (ticket numbers, branch names, tools). Kai reads these cold, between sessions.
- **Leave a trail for the orchestrator.** At the end of every reply that changes state, append a
  dated line to your thread's status file:
  `/home/kai/projects/badcode/badcode/design/2026-09-12-threads/status/<NN>.md`
  (create the folder and file if absent) — one line per report: date, what is done, what is blocked, what
  you need from Kai or another thread. Keep it under ten lines total by rewriting, not appending forever.
  That file is how the planning session sees you without reading your transcript. Don't commit it from
  your thread; the planning session commits the folder.
- **Autonomy.** Within your thread file's scope and gates you have full autonomy and may use parallel
  subagents. Do not expand scope; log surprises in your thread file's notes or the status file instead.

## First reply

Your first reply, before any change: (1) which thread you own and which checkout you are in; (2) a
five-line plain-English restatement of the goal in your own words, so Kai can catch a misreading; (3) the
first stop gate you will hit and what Kai must supply for it; (4) then begin the thread file's
"First action".

Your thread is:
