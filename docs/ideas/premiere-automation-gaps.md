# More Premiere Automation — the Gaps the Bridge Admits

`@badcode/premiere-mcp` gives a session 27 tools inside Premiere Pro. Its own documentation is
honest about what it still cannot do, and those admissions are the shopping list. This file
collects them so the next round of bridge work does not start by rediscovering them.

**Kai, 2026-09-12: not now.** The bridge does enough to cut with. Everything below is a
sharpening, not a blocker.

## The gaps, each quoted from our own notes

| Gap | Where we wrote it down | Why it hurts |
| --- | --- | --- |
| **No on-screen text, at all.** Writing a string param throws `Illegal Parameter type` — proven twice, on `AE.ADBE PPro SimpleText` param 5 and on a MOGRT's `Source Text`. Styling writes fine; the words do not. A rendered title still read *"Your Title Here"* after a successful write. | `docs/premiere/api-notes.md:1009`, `:1050` | ffmpeg is currently the **only** lane that can put a word on screen (`docs/video-fx/hybrid-method.md`). A caption forces a whole extra tool into the chain. |
| **No whole-timeline read.** A real hand-cut project is over half a megabyte of state, more than the transport carries, so `premiere_get_sequence` returns a per-track summary and dumps the rest to disk to `jq`. | `docs/premiere/README.md:43`, `packages/premiere-mcp/README.md:134` | Every "what is actually on this timeline" question is two steps and a shell command. |
| **No way to enumerate open projects.** No `setActiveProject`, no listing. A project that is open but not active is invisible. | `docs/premiere/api-notes.md:110` | Pairs with the standing trap that a human clicking another tab silently redirects the next call. |
| **Applying an effect and setting its params cannot be one transaction.** The plan asked for it; it is not possible, and the tool description says so. | `docs/premiere/api-notes.md:394` | Two round trips and a window where the clip has an effect at defaults. |
| **33 of Lumetri Color's 130 params cannot be read by any route** — and the documented workaround does not work. | `docs/premiere/api-notes.md:412` | A grade cannot be fully read back, so it cannot be fully verified or copied. |
| **`premiere_describe_effect` needs a clip.** There is no way to ask "what settings does this effect have" in the abstract. | `docs/premiere/api-notes.md:390` | You must apply an effect to find out what it does. |
| **An unreadable transition cannot be located without destroying it.** Every route throws; there is no way to ask where it is. | `docs/premiere/api-notes.md:1271` | A sequence containing a transition you did not add cannot be reasoned about. |
| **No speed setter and no frame-hold action.** `getSpeed()` reads; nothing writes. A clip cannot be made longer than its media. | `docs/premiere/api-notes.md:1402` | Freeze frames and speed ramps stay a human job. |
| **Two tickets never finished:** `T19` (an end-to-end smoke test, `smoke-e2e.ts`) and `T20` (a live GPOM scene-0 session — the only real proof the bridge works on a real cut). | `design/2026-08-21-premiere-bridge-and-video-fx.md:1080`, `:1096` | T20 is the honest one. Until it runs, "the bridge works" is 27 green unit-ish checks and no film. |

## What closing them would buy

Titles without leaving Premiere; a grade that can be verified; a timeline a session can read in
one call; and — via T20 — the first evidence that the whole bridge survives contact with a real
project rather than a test sequence.

## What it costs

Mostly **research into Adobe's ceiling, not our code.** Several of these are Premiere refusing,
not us not having written the tool: the string-param refusal is API-level and reproduced on two
independent params. Expect some to close as "cannot be done, here is the workaround" — which is
still worth writing down. The cheap ones are T19 and T20, which are our own unfinished work.

## What already exists to build on

- `packages/premiere-mcp` — the server, the panel, its 27 documented tools, and `src/smoke-*.ts` per ticket.
- `docs/premiere/api-notes.md` — the append-on-every-surprise file these rows came from.
- `design/2026-08-21-premiere-bridge-and-video-fx.md` — the original plan, with T19 and T20 still
  marked pending.
- `docs/video-fx/hybrid-method.md` — the lane rules that currently route around the text gap.

## What un-parks it

- A cut needs on-screen text often enough that hopping to ffmpeg for every caption grates.
- Or: a real cut goes onto a Premiere timeline and something breaks — then **T20 is not a
  nice-to-have, it is the debugging**.
- Or: an Adobe update ships writable string params, which would close the biggest row on its own.
