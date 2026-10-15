# The Chief of Staff — how BadCode's marketing gets run

**Status: proposal, 14 October 2026; dates removed 15 October (Kai). Written for Kai and Jack.**

## Why this exists

On 14 October 2026 the repo held about 3,000 lines of marketing plans written since July, and
no public account and no published post that the repo knows about. The films, the shorts, the
songs and the monologue are made. What is missing is not a strategy. It is someone whose only
job is to get finished work out of the door, keep it going out, and put the right decision in
front of the right person.

That job is a chief of staff.

## What a chief of staff is

A chief of staff works for one or two principals (here: Kai and Jack). It does not make the art
and it does not make the big calls. It:

1. **Holds the plan** — [`plan.md`](./plan.md): the goal, **what to do next**, and **what we should be
   doing that we're not**. No dates (Kai, 15 October: a timed plan is "a boss nobody wants").
2. **Speaks when asked, or when something needs you** — "what's next?" gets a short answer.
3. **Guards your attention** — at most three decisions at a time, ranked by what they unblock, each
   one written so you can answer it in a sentence.
4. **Keeps the board** — [`board.md`](./board.md): do next, what is blocked, what has gone out. The
   one place to look.
5. **Delegates the legwork** — research, drafting and checking go to helpers (subagents). The chief
   of staff reads what they bring back and only passes on what survives.
6. **Keeps the record** — [`log.md`](./log.md): every ruling and every review, newest first.

What it never does: publish anything without a human saying yes, make a ruling that is Kai's or
Jack's, or start a new plan document while something finished is still waiting to go out.

## The loop

```
  intake ──▶ triage ──▶ delegate ──▶ gate ──▶ brief ──▶ track
  (an idea,   (does it    (helpers     (the       (Kai/Jack  (board.md
  a cut, a    serve the   research,    gatekeeper get ≤3     and log.md
  headline)   a gap?)      draft, cut)  checks it) decisions) updated)
```

Anything that doesn't close a gap or move the next list is parked in [`../README.md`](../README.md) or
[`../../ideas/`](../../ideas/README.md) with one line, and is not worked on.

## The helpers (subagents)

Four, on purpose. Agent Bob's own research says small teams beat big ones and that a helper earns
its place only if it has different tools, a different schedule, or a different level of trust.

| Helper | What it does | Why it is separate |
| --- | --- | --- |
| **researcher** | finds facts, numbers, platform rules, competitors; marks each one as checked at the source or only read | needs the web; its output must be checked before anyone acts on it |
| **producer** | drafts the post, caption, title, description, email, cut list | writes in the BadCode voice from the canon |
| **gatekeeper** | attacks every draft against [`../the-reader.md`](../the-reader.md), [`../../voice.md`](../../voice.md), [`../../using-ai.md`](../../using-ai.md) and the legal lines; passes, fails, or sends back with a note | must be adversarial and never the same helper that wrote it |
| **analyst** | reads the numbers and says what to keep and what to cut | switched on only once there are numbers |

Their prompts live in [`.claude/agents/`](../../../.claude/agents/) as `marketing-*.md`. The chief of
staff's own prompt is the [`chief-of-staff` skill](../../../.claude/skills/chief-of-staff/SKILL.md).

## How it runs today (Claude Code + git)

- Either of you types `/chief-of-staff` (or "brief me", "what's next", "what should we be doing that we're not") in
  Claude Code in your own copy of the repo.
- It reads `plan.md`, `board.md` and `log.md`, does the work, updates the three files, and commits.
- **Git is the shared desk.** Jack pulls and sees what Kai's session decided, and the other way round.
- Nothing needs building. That is the point.

## How it moves to Agent Bob later

Every piece above is a plain file, so the same pieces become a Bob project without rewriting:

| Here (Claude Code) | In Bob |
| --- | --- |
| the `chief-of-staff` skill | the prompt of one Bob worker |
| `/chief-of-staff` typed when you want it | the same worker, asked when you want it (no schedule needed) |
| the four `.claude/agents/marketing-*.md` files | subagents inside that one worker (Bob workers run on the Claude Agent SDK, which supports subagents) |
| `board.md` and `log.md` in git | Bob's shared memory, rendered back to git with its git projection |
| you asking it a question | chatting to the worker in the Bob console |

What Bob would need, to be checked in the agent-bob repo before anyone builds anything:

1. **Subagents inside a worker.** Bob's docs already tell people to "use subagents inside one
   session", and the in-container harness already reports subagent start and stop events. What is
   unknown to me is whether a worker's configuration can carry the four helper definitions. That
   may be a small change, not a new feature.
2. **The worker can read and push this repo.** The git projection writes Bob's own configuration
   *out* to git. Reading BadCode's canon *in* is a different thing and is unchecked.
3. **A way to reach you.** Its answers have to arrive somewhere you look (email or WhatsApp).
   The WhatsApp channel from the 12 September work board is the obvious candidate.

**When to move:** once things are going out steadily, and only if the thing that hurts is
"someone has to remember to run it". Moving earlier means building Bob instead of shipping BadCode,
which is the problem this whole document is trying to fix.
