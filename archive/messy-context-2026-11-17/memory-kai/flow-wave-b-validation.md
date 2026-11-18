---
name: flow-wave-b-validation
description: "Flow MCP automation complete on feat/enc-program 2026-08-12 — Waves A+B+C plus batch plus the L1-L4 follow-ups (refine, Extend tested, fallback, timeout dump)"
metadata:
  node_type: memory
  type: project
  originSessionId: d21d9736-2e38-4cc1-82fc-af495fa3424b
  modified: 2026-08-12T19:28:54.588Z
---

The Flow automation programme is **finished**: Wave A (tool surface 12 → 17, written blind),
Wave B (live validation), and Wave C (video). All on `feat/enc-program` — `baef6c2`, `ebce73c`
(C4), `7d26675` (C1–C3). Plan of record with every ticket marked done and its findings:
`design/2026-08-12-flow-automation-coverage.md`.

**The operational gotcha worth not rediscovering:** `.mcp.json` runs the flow server as
`npx tsx packages/flow-mcp/src/server.ts` — a **relative** path, resolved against the session's
working directory. So the server every skill uses runs the *primary checkout's* source. Flow
fixes made on a worktree branch are invisible to `animate-slide` / `edit-panel` / `make-comic`
until they are merged, no matter how well they were proven under `tsx` in the worktree. Merge
first, then `/mcp` reconnect; a reconnect alone proves nothing.

**Method that made it work, and should be reused:** drive the client directly under `tsx` via
`packages/flow-mcp/src/smoke-*.ts` (fresh process picks up edits instantly, no `/mcp`
reconnect); map the DOM with a probe before writing any selector; verify generated output by
LOOKING at it — never by file size, and never by the return value. Wave C caught a call that
returned a healthy mp4 which was byte-for-byte an *older* generation; only md5 found it.

**`flow_generate_video` is now one tool with four modes**, selected by which images you pass:
`startImage` alone animates a still, `startImage`+`endImage` generates the motion between two
frames, neither is text-to-video, and end-only is refused (Flow does not have it). Plus
`durationSeconds` — 4/6/8/10, a control nobody knew existed, so every clip before 2026-08-12
was 8s by accident. See [[flow-video-modes]] for the traps.

**The L1–L4 follow-ups are all closed too** (2026-08-12, commits `9706496`, `5f5d664`,
`00b549e`, `443c2e8`):

- **`flow_refine_video`** — "like that clip, but slower". Flow's per-clip *Reuse prompt* restores
  the whole turn including the **source still**, so a refine needs nothing but the clip's
  `mediaId` and the caller never has to still hold the image.
- **Extend and video Edit do not exist** in this account's UI — tested by generating on the exact
  tiers Google's docs claim them for. Clicking a clip opens Flow's **scene editor**
  (`/edit/<sceneId>`, a timeline with `Add Clip`) instead.
- **Animate falls back to Frames** on `ANIMATE_NOT_FOUND`, and says so via `via:
  'frames-fallback'`. That weakness is intermittent, not a project-size threshold.
- **Timeouts write a dump** (`$TMPDIR/flow-timeout-*.txt/.png`) so the two never-seen failure
  states — out of credits, rate-limit/captcha — can be mapped from evidence rather than guessed.

See [[flow-script-hardening-initiative]], [[flow-mcp-and-art-direction-initiative]],
[[flow-automation-integration]], [[flow-policy-blocks]].
