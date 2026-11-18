---
name: premiere-bridge-initiative
description: "2026-08-21 Premiere Pro as the third tool (Flow + ffmpeg + Premiere) — UXP panel dials out to a ws server inside @badcode/premiere-mcp in WSL; plus a 20-agent video-fx research sweep → docs/video-fx/ toolkit. Bridge BUILT + docd 2026-08-23 (27 tools); T11/T14/T19/T20 remain, T20 = the only real proof."
metadata: 
  node_type: memory
  type: project
  originSessionId: 63e6da94-5296-4216-ba2c-f2fba49f8f0a
  modified: 2026-08-23T00:00:00.000Z
---

**Plan (source of truth, 20 tickets, Status/checkboxes live there):**
`design/2026-08-21-premiere-bridge-and-video-fx.md` — approved by Kai 2026-08-21.

**What it is:** let a WSL session drive Premiere Pro 2026 on the Windows host in real time —
import, arrange, trim, transitions, ANY installed effect by match name (third-party plugins too),
keyframes, MOGRTs, export frame (Claude's eyes) + render — and a `video-fx` knowledge toolkit
built from research so "add a fire effect / zoom a map" resolves to a priced tool + lane.

**Locked decisions (Kai, 2026-08-21):**
- UXP, not CEP/ExtendScript/XML-import. v1 scope = *everything incl. effects*.
- Topology: UXP panel = WebSocket CLIENT dialling `ws://localhost:7890`; server lives INSIDE the
  MCP process in WSL (Windows→WSL localhost forwarding is default-on). No Windows proxy.
  Fallbacks: `wsl --shutdown`, mirrored networking, direct 172.24.x.x IP.
- One `.prproj` per story, one sequence per scene + MASTER, under ONE configurable media root
  (`badcode.local.json`, gitignored). **Ruled 2026-08-21: `D:\badcode-videos`** (D: has 5.5 TB free; C: only 87 GB). Kai: the
  base folder is the only variable; the tree beneath is fixed. Desktop\gpom-sNN folders relocate (T14).
- Research: all three plugin tiers (built-in / free / paid) price-tagged; runs in parallel with
  the build; raw briefs `design/research/2026-08-21-video-fx-landscape/`, distilled `docs/video-fx/`.
- `video-fx` skill finds + prices + documents; a human installs. `premiere_eval` is the escape
  hatch for trying a new plugin's API before promoting to a tool.
- **NO PAID PLUGINS (Kai, 2026-08-21, after reading the sweep).** The free stack covers it:
  Premiere built-ins + the ex-Film Impact transitions Adobe made free in 25.5 + Lumetri + MOGRTs
  + ffmpeg (43 xfade transitions, keying, LUTs, grain, stabilise). **For fire/smoke/sparks the
  house answer is Flow** — prompt the element on black, composite with a Screen blend. Paid suites
  (Continuum/Sapphire particles, FilmConvert, Dehancer, Topaz) get ONE reference page saying what
  we don't own and the free route instead. Side effect: kills the sweep's price-contradiction
  problem, since every contradiction was about a paid tool. No After Effects — 3D text, Trapcode
  and planar tracking are out of reach by choice.

**Host facts:** Premiere 26.3.2 · Win11 25H2 · WSL Ubuntu-22.04 NAT · UXP Developer Tool NOT
installed (Kai installs from Creative Cloud app, admin) · H.264 preset
`…\MediaIO\systempresets\4E49434B_48323634\01 - Match Source - High bitrate.epr` ·
API types = npm `@adobe/premierepro@26.3.0` `src/premierepro.d.ts` (read it; it's ground truth).

**API gotchas found in review:** `insertMogrtFromPath` is NOT an Action (runs outside
executeTransaction); `importFiles` returns only boolean (diff the bin); `VideoFilterComponent`
is typed `{}` (cast to Component); `ppro.Application.version` not `app.version`; UXP panels
cannot listen on sockets.

**Why:** Kai wants the Flow→ffmpeg loop to end inside Premiere (plugins + production tricks)
without leaving the conversation. **How to apply:** work the plan's tickets in order; T1 spike
first (needs Kai for UDT); research Workflow (T16) is independent. See [[flow-automation-integration]]
and [[flow-mcp-and-art-direction-initiative]] for the pattern being cloned.

---

## Status 2026-08-23 — built, documented, NOT yet used in anger

**Done:** T1–T10, T12, T13, T15–T18, T21. **27 tools.** Remaining: **T11** (MOGRT *write*),
**T14** (media-root migration — needs Kai's OK, moves irreplaceable renders), **T19** (smoke-e2e),
**T20** (live GPOM scene-0 — *the only test that proves the knowledge works cold; not run*).

**16 skills exist.** New this session: **`video-fx`** (the judgement layer — lane choice, "what
effect does X" routing, the delivery gate) and **`find-footage`** (see [[footage-sourcing-lane]]).

**Rulings that changed the design:**
- 🔴 **The bridge binds its port on the FIRST `premiere_*` call, never at startup.** Kai:
  *"only when we start working on Premiere do we then start the bridge, a bit like when we work on
  Flow, then we start the browser."* Eager binding made 4 sessions fight over 7890.
- 🔴 **NEVER kill another session's server to take the port.** Docs used to say kill "all but the
  newest tree" — correct for a self-orphaned server, destructive when the holder is live. Trace
  the holding pid up to its `claude` process and compare with your own.
- **Never ask Kai to reload the panel for a connection problem** — it is almost always that
  nothing is listening on our side.

**API behaviours that cost real time (all in `docs/premiere/api-notes.md`):**
- 🔴 **Premiere marshals only CLIP track items** — `getTrackItems` returns `null` for every other
  type, with an exact array length. Broke every state-returning tool once a transition existed.
- **Actions in a CompoundAction do not compose** — all compute against transaction-start state.
  Trim, then move, as separate calls.
- **Transitions are write-only** — no read-back. Proven by saving and `zcat`-ing the gzipped
  `.prproj`. That escape hatch works but is ruled not-to-build unless a real project needs it.
- **Adobe's own recommended fallback fails** — 33 Lumetri params throw on `getValueAtTime` and
  recommend a method that also returns null or throws.

**Open human check:** confirm edits read as single `BadCode: …` entries in Edit ▸ Undo (no undo
history API exists, so it cannot be machine-verified).
