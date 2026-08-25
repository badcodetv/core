# Premiere toolkit — driving Adobe Premiere Pro from a session

**The third tool.** Flow invents the footage, `ffmpeg` does what must be exact, and
**Premiere is where it becomes an edit** — because that is where the plugins, the effects and
the production tricks live.

This folder is how a Claude session reaches into Premiere on the Windows host while running in
WSL: a small UXP panel inside Premiere dials out to a WebSocket server inside
`@badcode/premiere-mcp`, and the session gets tools for importing, arranging, trimming,
transitions, effects and keyframes, motion-graphics templates, and — crucially — exporting a
frame so it can **see** what it just did.

**New to this? Start at [`setup.md`](./setup.md).** Ten minutes, once per machine.

## The split (same shape as `docs/flow/`)

| Half | What it is | Where |
| --- | --- | --- |
| **Mechanics** — ours | Getting the bridge up, the tool calls, recovering a failed one | `.claude/skills/premiere-automation/SKILL.md` + this folder |
| **Judgement** — what to apply | Which effect, which plugin, what it costs, ffmpeg-or-Premiere | [`../video-fx/`](../video-fx/README.md) + the `video-fx` skill |

If you are choosing an effect, you are in the wrong folder.

## Files

| File | What | Read when |
| --- | --- | --- |
| [`recipes.md`](./recipes.md) | 🟢 **The cookbook.** Concrete tool-call sequences for the jobs that come up — build a cut, push in, dissolve, grade, composite a Flow element, export and look. Plus the things that flatly do not work, so you stop looking | **Someone says "put these clips in Premiere and…"** |
| [`effects-catalogue.md`](./effects-catalogue.md) | **What this machine can actually do** — all 106 effects and 118 transitions, harvested live and grouped by what you would ask for, with the BadCode register called out | Choosing an effect or a transition |
| [`setup.md`](./setup.md) | 🔴 **One-time machine setup** — media root, UXP Developer Tool, developer mode, loading the panel, and every way the connection fails | First time on a machine, or the panel won't go green |
| [`api-notes.md`](./api-notes.md) | Hard-won facts about Premiere's UXP API — match names, param indices, what isn't undoable, what the docs get wrong | A call behaves oddly, or before guessing at an API |
| [`bridge-protocol.md`](./bridge-protocol.md) | The wire protocol between server and panel: frames, ids, error codes | You are changing `@badcode/premiere-mcp` |

The tool reference itself lives with the code, in
[`packages/premiere-mcp/README.md`](../../packages/premiere-mcp/README.md) — the code is the
ground truth and the reference sits next to it.

## The four facts worth knowing before you start

🔴 **The panel must stay open in Premiere.** It is where the code runs. Close it and the
session loses Premiere entirely.

🔴 **No tool returns a whole timeline.** A real hand-cut project is over half a megabyte of state
— far more than the transport will carry. So `premiere_get_sequence` gives a **one-line-per-track
summary** by default, writes the complete state to disk beside the project, and expands only what
you ask for (`tracks`, `clips`, `range`). `jq` the `statePath` for anything bulk; it costs no
context at all.

🔴 **Every edit tool acts on the ACTIVE sequence and takes no sequence argument.** A human clicking
a different timeline tab silently redirects your next call. Re-assert `premiere_set_active` before
a run of edits and check `sequence.name` on every response. This has already cost one hand-cut
project.

🔴 **CEP is dead; this is UXP.** Premiere 2026 no longer loads CEP extensions, and ExtendScript
support ends around September 2026 — which is why every "Premiere MCP" you'll find on GitHub is
already broken, and why we built our own. Design and reasoning:
[`design/2026-08-21-premiere-bridge-and-video-fx.md`](../../design/2026-08-21-premiere-bridge-and-video-fx.md).
