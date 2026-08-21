---
name: premiere-automation
description: Use when DRIVING Adobe Premiere Pro from a session — opening a project, building or re-cutting a sequence, importing clips, applying effects, exporting a frame or a render, or recovering a failed bridge call. Triggers on "use Premiere", "automate Premiere", "open this project in Premiere", "put these clips on the timeline", "the panel isn't connecting", "premiere_status says not connected", "Premiere automation isn't set up", "install the UXP plugin", or "add a Premiere tool". Mechanics only — WHICH effect to reach for belongs to video-fx; what the shot should look like belongs to badcode-art-direction.
---

# Premiere Automation

**The machine half of Premiere.** Everything about making a bridge call succeed, and nothing
about what to apply.

Premiere is the third tool in the conversation: **Flow invents the footage, `ffmpeg` does what
must be exact, and Premiere is where it becomes an edit** — because that is where the plugins,
the effects and the production tricks live.

## What this is not

| Job | Skill | Question it answers |
| --- | --- | --- |
| **Driving it** | **this skill** | Why did the call fail? Which tool? Is the bridge even up? |
| **Choosing the effect** | `video-fx` | Fire, map zoom, film look — what tool, what does it cost? |
| **The BadCode look** | `badcode-art-direction` · `new-image` | What should it look like? |

If you are choosing between a Gaussian Blur and a Lumetri curve, you are in the wrong skill.

---

## 1. Get a working bridge — ALWAYS start here

🔴 **`premiere_status` first. Every time. Before anything else.** It is the only tool that runs
without configuration, it never fails, and its answer tells you exactly which of four states you
are in. Do not open with a real call and interpret the wreckage.

```
premiere_status()
```

### The four states, and what to do about each

| What you get back | What it means | What you do |
| --- | --- | --- |
| `{ connected: true, appVersion, mediaRoot }` | Everything is up | Get on with it |
| `{ connected: false, mediaRoot: "…" }` | Set up, but the panel is not answering | **§1a — the panel** |
| `{ connected: …, mediaRoot: null, hint }` | No media root configured | **§1b — the config** |
| `{ error: true, code: "BAD_CONFIG" }` | `badcode.local.json` is malformed | Fix the JSON the hint names |

**Never guess between these.** `connected: false` with a media root is a five-second fix;
`mediaRoot: null` is a different five-second fix; they look nothing alike and the wrong one
wastes the user's time.

### §1a — `connected: false`: the panel is not answering

Work down this list. It is ordered by how often each one is the answer.

| Ask the user / check | Why | Fix |
| --- | --- | --- |
| **Is the BadCode Bridge panel open in Premiere?** | It is where the code runs. Closed panel = no Premiere | Premiere ▸ **Window ▸ Extensions (UXP) ▸ BadCode Bridge** |
| **Have I rebuilt the panel this session?** | 🔴 A rebuilt panel does NOT reload itself | **⋯ → Load** on its row in UXP Developer Tool |
| **Is Premiere even running?** | — | Start it, then reload the panel in UDT |
| **Did the machine sleep?** | WSL's localhost forwarding breaks across sleep | `wsl --shutdown` in PowerShell, reopen the terminal |
| **Is the plugin installed at all?** | First run on this machine, or it got removed | **§1c — install it from scratch** |

The panel's own log pane is worth asking about: it says what it is dialling and what came back.

### 🔴 "The panel keeps saying it can't connect" — read this before touching anything

**Reloading the panel will not fix this.** It is the single most common thing a user will report,
and the answer is almost never the one they expect.

The panel dials **out**; the server it dials lives inside the MCP server process in WSL. So the
light is red exactly when that process is not running — and green whenever it is.

| Panel says | What it means | Do |
| --- | --- | --- |
| `waiting for Claude…` | Nothing is listening. Normal if no Claude session with the premiere MCP server is running | Nothing, or start one |
| `waiting for Claude` (was connected) | The session that was serving it ended | Nothing — it reconnects on its own |
| `connected` | Working | — |
| `closed (1011)` or another code | A real error. The server accepted the panel and then hung up | Check §1a |

**The bridge opens when the MCP server starts, not on the first tool call**, so in a session with
the server loaded the panel goes green within its ten-second backoff and stays green for the
whole session. If it is red for a whole session, the server is not loaded — see below.

🔴 **The one case that genuinely needs action: the MCP server is not loaded.** MCP servers are
read from `.mcp.json` **at startup**. If the `premiere` entry was added during the current
session, it is inert — no listener will ever open, and the panel will be red no matter how many
times it is reloaded. **Restart Claude Code.** Confirm from WSL:

```bash
ss -ltnp | grep 7890      # a `node` process here = the bridge is up
```

Nothing listed and the user is in a Claude session? The server is not loaded. Restarting is the
fix; a panel reload is not.

**Never ask the user to reload the panel for a connection problem.** Reload is for one thing
only: picking up a **rebuilt** panel (§1a). Asking for it otherwise wastes their time and teaches
them a reflex that will mislead them later.

### §1b — `mediaRoot: null`: no config

One file, one line. In the repo root:

```bash
cp badcode.local.json.example badcode.local.json
```

Then set `mediaRoot` to a folder on a drive with room — video is large. It is gitignored because
it describes the machine, not the project.

```jsonc
{ "mediaRoot": "D:\\badcode-videos" }   // Windows path, double backslashes
```

**The media root is a default, not a cage.** It is where `premiere_open_project({ story })` puts
story projects. A project anywhere else opens fine by path and needs no root at all — see §3.

### §1c — Not installed: the full walkthrough

**Do not paraphrase this from memory. Walk the user through
[`docs/premiere/setup.md`](../../../docs/premiere/setup.md)** — it is the authoritative
procedure, it has been run end to end, and it carries the troubleshooting this section
summarises. About ten minutes, most of it an installer, once per machine.

The shape of it, so you can tell the user what they are in for:

1. **Media root** — `badcode.local.json` (§1b above)
2. **UXP Developer Tool** — Creative Cloud desktop app ▸ All apps ▸ *UXP Developer Tools* ▸
   Install. **Needs admin rights.**
3. **Developer mode in Premiere** — Settings ▸ Plugins ▸ *Enable developer mode*, then
   **restart Premiere**. It does not take effect until you do
4. **Build the panel** — `npm run build:panel --workspace @badcode/premiere-mcp`. This also
   mirrors it to `<mediaRoot>\_bridge\panel\`, which is the Windows path UDT loads from
5. **Load it** — UDT ▸ Add Plugin ▸ `<mediaRoot>\_bridge\panel\manifest.json`, then **⋯ → Load**
6. **Open it** — Premiere ▸ Window ▸ Extensions (UXP) ▸ BadCode Bridge. Green light = done

**You can do step 4 yourself. Steps 2, 3, 5 and 6 need the human** — they are GUI actions in
Adobe's own tools and there is no automating them. Say so plainly, one step at a time, and check
`premiere_status` after.

🔴 **The plugin stays in UDT's list between sessions, but Load must be pressed again every time
Premiere restarts.** This is the single most common cause of a dead bridge. When you ask for it,
say *why* — otherwise it reads as superstition.

---

## 2. The laws

1. **Strictly serial.** One Premiere, one panel, one command in flight. Never fan out parallel
   agents at the bridge — they fight over a single connection. The same law as Flow's one browser.
2. **`premiere_status` before anything else**, every session. §1.
3. **Refs go stale the moment the timeline changes.** A clip is `v0:2` — video track 0, third
   clip — *as of the last state you were given*. Every mutating tool returns the refreshed state
   for exactly this reason. Use the newest one; never an older one, never one you cached.
4. **One call, one undo entry.** Every mutation is a single transaction labelled `BadCode: …`,
   so the user can undo your work in the steps they watched you take.
5. **Look before you claim.** After any visual change, export a frame and *read it*. A timeline
   whose numbers are right can still look wrong, and you cannot see the program monitor.
6. **Outputs live beside the project.** `frames\` and `renders\` sit next to the `.prproj`,
   whichever way it was opened. `premiere_open_project` returns both paths — use them rather than
   assuming the media root.
7. **Never guess a match name.** Effects and transitions are addressed by internal match name and
   no third-party vendor publishes theirs. List, then apply.
8. 🔴 **Every edit tool acts on the ACTIVE sequence and takes no sequence argument.** A human
   clicking a different timeline tab silently redirects your next call. Re-assert
   `premiere_set_active` before a run of edits, and **read `sequence.name` on every response** to
   confirm the work landed where you meant. This has already cost one irreplaceable hand cut.
9. **Do not drive Premiere while a human is using it.** The bridge serialises the panel, not the
   person at the keyboard. If the user says they are going to work in Premiere, stop calling until
   they say they have stopped — and tell them that opening or activating a project changes what
   they are looking at.

---

## 3. Opening a project

Two ways, and exactly one is required:

```
premiere_open_project({ path: "/mnt/d/some/folder/thing.prproj" })   # anywhere on disk
premiere_open_project({ story: "camping" })                          # <mediaRoot>\camping\camping.prproj
```

**`path` is the one to reach for when the user pastes you a path** — any absolute `.prproj`, WSL
or Windows form, no media root needed, parent folder created if missing. `story` is the BadCode
convention for a project we are authoring ourselves.

Both return `{ project, created, sequences, framesDir, rendersDir }`. `created: true` means this
call made the project; `false` means it already existed and was opened.

---

## 4. The tool surface

**27 tools ship.** Ground truth is `packages/premiere-mcp/src/server.ts` — count the
`registerTool` calls there rather than trusting a number here. Full reference with arguments and
error codes: [`packages/premiere-mcp/README.md`](../../../packages/premiere-mcp/README.md).

| Group | Tools |
| --- | --- |
| Status & project | `status` · `open_project` · `save` · `import` · `list_items` |
| Sequences | `create_sequence` · `list_sequences` · `set_active` · `get_sequence` |
| Editing | `insert_clip` · `move_clip` · `trim_clip` · `remove_clip` · `clone_clip` |
| Transitions & notes | `list_transitions` · `add_transition` · `remove_transition` · `add_marker` · `set_playhead` |
| Effects & keyframes | `list_effects` · `describe_effect` · `apply_effect` · `set_param` · `remove_effect` |
| Output & escape hatch | `export_frame` · `export_sequence` · `eval` |

**Not built yet:** `insert_mogrt` (T11) — motion-graphics templates. Until a tool exists the panel answers
`INVALID_ARGS` — which is also what a **stale panel** says, so check §1a before concluding a tool
is missing.

### Reading a timeline: summary by default, detail on request

**No tool returns a whole timeline.** A real hand-cut project is over half a megabyte of state and
the transport refuses it — *after* the panel has already committed the edit, so you would see a
failure for work that succeeded. Instead:

- `premiere_get_sequence({})` is a **digest** — one line per track, ~1.8 KB whatever the size of
  the edit.
- The **complete state is written to disk** at the returned `statePath`. **`jq` over that file for
  anything bulk** — counting, searching, auditing a whole cut. It costs no context.
- Expand what you need: `tracks: ["V1"]` · `clips: ["v0:2"]` · `range: [10, 30]` · `params: false`.
- Mutating tools return **`changed`** — the clips added, removed or moved. **That is how you learn
  the ref of a clip you just inserted.** It compares clip *times*, so a `set_param` correctly
  reports no change.

### What to reach for

Do not guess a match name and do not go looking for a plugin we do not own:

- **[`docs/premiere/recipes.md`](../../../docs/premiere/recipes.md)** — the cookbook. Build a cut,
  push in, dissolve, grade, composite a Flow element, export and look.
- **[`docs/premiere/effects-catalogue.md`](../../../docs/premiere/effects-catalogue.md)** — all 106
  effects and 118 transitions on this machine, grouped by what you would ask for.
- **We own no paid plugins and are not buying any.** For fire, smoke, sparks and weather the house
  answer is: generate the element in **Flow on a black background**, then key it in with Luma Key
  or Extract on a track above.

---

## 5. When a call fails

| Code | What it really means | Do |
| --- | --- | --- |
| `PANEL_NOT_CONNECTED` | Panel closed, or **rebuilt and not reloaded** | §1a |
| `TIMEOUT` | **Almost always a modal dialog waiting in Premiere.** Ask the user to look | Dismiss it, retry |
| `NO_MEDIA_ROOT` | No config, and you used `story` mode | §1b, or switch to `path` |
| `NO_PROJECT` | Nothing open | `premiere_open_project` |
| `CLIP_NOT_FOUND` | A stale ref | Re-read the state; law 3 |
| `EFFECT_NOT_FOUND` / `TRANSITION_NOT_FOUND` | Guessed a match name | List first; law 7 |
| `INVALID_ARGS` | Bad arguments — **or a stale panel** | Check the call, then §1a |
| `EVAL_ERROR` | Your snippet threw | The stack is in the error |
| `PANEL_ERROR: listen EADDRINUSE` | 🔴 **An old MCP server still holds port 7890.** An `/mcp` reconnect spawns a new server and orphans the old one | `ss -lptn 'sport = :7890'`, then `ps -eo pid,ppid,cmd \| grep premiere-mcp/src/server.ts` and kill all but the newest tree. The next call binds and the panel reconnects itself |

---

## 6. `premiere_eval` — the escape hatch, not the product

Runs JS inside the panel with `ppro`, `helpers` and `log()` in scope. Use it to find out what an
unfamiliar API *actually does* — which is not always what its type declarations claim.

**It has already earned its keep twice.** `Project.isProject()` turned out not to be an existence
check, and `Project.open()` turned out to reject with a bare string *even when it succeeds*.
Neither is discoverable from the docs; both were a single eval call.

Promote anything you reach for twice into a typed tool. And when eval teaches you something,
**write it into [`docs/premiere/api-notes.md`](../../../docs/premiere/api-notes.md) in the same
session** — that file is why the next person does not pay for the same lesson.

---

## Knowledge base

| File | What |
| --- | --- |
| [`docs/premiere/setup.md`](../../../docs/premiere/setup.md) | 🔴 The install walkthrough. §1c sends you here |
| [`docs/premiere/recipes.md`](../../../docs/premiere/recipes.md) | 🟢 **The cookbook** — concrete tool-call sequences for every job that comes up |
| [`docs/premiere/effects-catalogue.md`](../../../docs/premiere/effects-catalogue.md) | Every effect and transition installed, grouped by what you would ask for |
| [`docs/premiere/api-notes.md`](../../../docs/premiere/api-notes.md) | What Premiere's API actually does, versus what it claims |
| [`packages/premiere-mcp/README.md`](../../../packages/premiere-mcp/README.md) | Tool reference, error table, how to build the panel |
| [`docs/premiere/bridge-protocol.md`](../../../docs/premiere/bridge-protocol.md) | The wire protocol — only if you are changing the bridge |
| [`design/2026-08-21-premiere-bridge-and-video-fx.md`](../../../design/2026-08-21-premiere-bridge-and-video-fx.md) | Why it is built this way; the ticket list |
