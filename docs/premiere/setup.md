# Setting up the Premiere bridge

**One-time setup, per machine.** About ten minutes, most of it waiting for an installer.
Do it once and Claude can drive Premiere from a session forever after.

You need to do this if you want Claude to build and adjust timelines in Premiere while you
talk to it — the same way it already drives Flow. If you only ever edit by hand, skip it.

> **Status: this whole procedure was run end-to-end on Kai's machine on 2026-08-21 and the
> panel connected.** Steps are ✅ confirmed unless marked otherwise. If something differs on
> your machine, **fix it here immediately** — that is what this file is for.
>
> **It worked on plain `ws://localhost` with default WSL2 networking** — neither fallback in the
> troubleshooting section was needed. They are there for when it doesn't.

---

## What you are actually setting up

```
  Claude (in WSL)                          Premiere (on Windows)
  ┌───────────────────┐                    ┌──────────────────────┐
  │ bridge server     │ ◀── WebSocket ──── │ "BadCode Bridge"     │
  │ ws://localhost:7890│                   │  UXP panel           │
  └───────────────────┘                    └──────────────────────┘
```

A tiny panel lives inside Premiere and phones out to a server Claude runs. That is the whole
trick. Nothing is installed on Windows except the panel, and the panel is loaded through
Adobe's own developer tool rather than an app store, because it is ours and unsigned.

**The panel must be open in Premiere for any of this to work.** If you close it, Claude loses
its connection — that is not a bug, it is where the code runs.

---

## Step 1 — Pick the media root ✅

Everything Premiere touches lives under one folder, and the tools refuse to run until they
know where it is. Pick a drive with room; video is large.

> **Kai's machine uses `D:\badcode-videos`** (5.5 TB free). Yours can differ — only this one
> path is a per-machine choice, everything beneath it is fixed.

In the repo root, copy the template and edit it:

```bash
cp badcode.local.json.example badcode.local.json
```

```jsonc
{
  "mediaRoot": "D:\\badcode-videos",   // ← the only line you must change. Double backslashes.
  "premiere": {
    "port": 7890,
    "exportPreset": "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2026\\MediaIO\\systempresets\\4E49434B_48323634\\01 - Match Source - High bitrate.epr"
  }
}
```

`badcode.local.json` is gitignored — it describes your machine, not the project.

The tree underneath is built for you as you go:

```
D:\badcode-videos\
  _bridge\panel\              ← the panel Premiere loads (Claude puts it here)
  <story>\                    ← e.g. gitpush-origin-master
    <story>.prproj            ← ONE Premiere project per story
    renders\                  ← finished exports
    frames\                   ← single frames, so Claude can SEE the edit
    <scene>\                  ← Flow takes for that scene
      final\                  ← the keepers
```

---

## Step 2 — Install UXP Developer Tool ✅

Adobe's tool for loading unsigned plugins. It is free and comes through Creative Cloud.

1. Open the **Creative Cloud desktop app**
2. **All apps**
3. Find **UXP Developer Tools** → **Install**

**You need admin rights on the machine.** The installer asks for them.

---

## Step 3 — Turn on developer mode in Premiere ✅

Premiere will not load an unsigned plugin until you say so.

1. Premiere → **Settings ▸ Plugins**
2. Tick **Enable developer mode**
3. **Restart Premiere** — it does not take effect until you do

---

## Step 4 — Load the panel ✅

1. Open **UXP Developer Tool**. First run asks to enable Developer Mode — say yes
2. Premiere should appear in the left pane under connected applications.
   *If it doesn't: Premiere isn't running, or you skipped the restart in step 3*
3. **Add Plugin** → navigate to your media root and pick:

   ```
   <mediaRoot>\_bridge\panel\manifest.json
   ```

   (on Kai's machine: `D:\badcode-videos\_bridge\panel\manifest.json`)
4. On the new row: **⋯ → Load**

The plugin stays in UDT's list between sessions, but **you have to press Load again each time
you restart Premiere.**

---

## Step 5 — Open the panel and check it ✅

In Premiere: **Window ▸ Extensions (UXP) ▸ BadCode Bridge**

> If it isn't under **Extensions (UXP)**, look under **Window ▸ Extensions** or **Window ▸
> Plugins** — Adobe has moved this between versions. Correct this line if yours differs.

Dock it somewhere out of the way. It shows a status light, the server address, and a log.

**Green light = connected.** That's it, you're done — tell Claude and it takes over.

If it's red, the server probably isn't running on the Claude side. Ask Claude to start it, or
check the bridge yourself:

```bash
npx tsx packages/premiere-mcp/src/smoke-status.ts
```

That brings the bridge up, waits for the panel, and prints what Premiere reports back.

---

## When something doesn't work

### The panel won't go green

Work down this list; it is ordered by how often each one is the answer.

| Check | Fix |
| --- | --- |
| Did Claude just rebuild the panel? | **Press ⋯ → Load in UDT again.** Premiere keeps running the old bundle until you do — a panel that connects but answers `INVALID_ARGS` is this |
| Is the server actually running? | `ss -ltn \| grep 7890` in WSL. Nothing? Start it |
| Did the machine sleep since it last worked? | WSL's localhost forwarding breaks across sleep. `wsl --shutdown` in PowerShell, then reopen your terminal |
| Something else on port 7890? | `ss -ltnp \| grep 7890` shows the culprit. Change `premiere.port` in `badcode.local.json` **and** the `network.domains` in the panel's `manifest.json` — they must match |
| Still nothing | Use the direct-IP fallback, below |

### Fallback A — direct IP

Stop trusting localhost forwarding and address WSL by its actual address.

```bash
PREMIERE_BRIDGE_BIND=all npx tsx packages/premiere-mcp/src/smoke-status.ts
```

It prints its own IP on startup. Put that URL in the panel's address box:
`ws://172.24.x.x:7890`

⚠️ **WSL's IP changes on reboot**, so this is a get-unstuck move, not a way to live.

### Fallback B — mirrored networking

Makes `localhost` mean the same thing on both sides, permanently. Needs Windows 11 22H2+.

Edit `%USERPROFILE%\.wslconfig`:

```ini
[wsl2]
networkingMode=mirrored
```

Then `wsl --shutdown` in PowerShell and reopen your terminal. Note this changes networking for
**all** your WSL work, not just this — worth knowing if something else on your machine starts
behaving oddly afterwards.

### The panel doesn't appear in the Window menu

The plugin didn't load. Back to UDT: is the row there, and did **Load** actually succeed?
UDT's log (document icon) says why if it didn't. Most common causes: Premiere was restarted
and you didn't press Load again, or developer mode isn't on.

### Premiere doesn't appear in UDT

Premiere must be **running** before UDT will see it, and developer mode must be on with a
restart after. If both are true and it still doesn't show, restart UDT.

### 🔴 UDT says "failed to load the DevTools plugin"

The banner is generic. It is almost always one of two things, and **UDT's log (the document icon
on the plugin's row) names which** — read that before trying anything.

**1. The wrong `manifest.json`.** There are two, and they look identical in a file browser:

| Path | Loads? |
| --- | --- |
| `packages/premiere-mcp/panel/manifest.json` | 🔴 **No — this is source.** It has `manifest.json`, `index.html` and `icons/`, so it looks right, but `index.html` does `<script src="main.js">` and **`main.js` is only created by the build** |
| `<mediaRoot>\_bridge\panel\manifest.json` | ✅ Yes — the build output |

Check the folder you pointed UDT at contains a **`main.js` of about 50KB**. If it doesn't, run
`npm run build:panel --workspace @badcode/premiere-mcp` and watch for
`no media root configured — mirror skipped`, which means the build worked and wrote nothing.

**2. The host version floor.** The manifest declares `host.minVersion`, and UDT refuses before it
looks at any code. Check **Help ▸ About**.

| Premiere | Status |
| --- | --- |
| 26.3.2 | ✅ everything in this repo was built and proven here |
| 25.6.6 | 🟡 **loads** — floor lowered to 25.0.0 on 2026-08-27 for exactly this. Not yet exercised beyond loading |
| below 25.0 | ⬜ untested, and the floor will refuse it |

⚠️ **The floor is a declaration, not a tested boundary.** 25.0.0 says "we have no evidence it
breaks below 26", not "this works". The panel uses `Application`, `Project`, `ProjectItem`,
`TickTime`, `Markers`, `Color`, `PointF` and `Constants` — the core UXP surface — but individual
methods arrived at different times. **`createSetSettingsAction` (the in-place frame-rate change in
[`api-notes.md`](./api-notes.md)) is the kind of call most likely to be missing on an older host.**
On a new version, run `premiere_status` first: a green light and a host version back means the
transport is fine, and anything that fails after that fails one tool at a time.

---

## Where the rest of it lives

| Thing | File |
| --- | --- |
| What the bridge can do, tool by tool | [`../../packages/premiere-mcp/README.md`](../../packages/premiere-mcp/README.md) |
| How Claude should drive it | `.claude/skills/premiere-automation/SKILL.md` |
| Which effect or plugin to reach for | [`../video-fx/README.md`](../video-fx/README.md) |
| The design and the ticket list | [`../../design/2026-08-21-premiere-bridge-and-video-fx.md`](../../design/2026-08-21-premiere-bridge-and-video-fx.md) |
| Hard-won API facts | [`./api-notes.md`](./api-notes.md) |
