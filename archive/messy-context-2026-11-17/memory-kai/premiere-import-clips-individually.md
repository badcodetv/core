---
name: premiere-import-clips-individually
description: "Kai's ruling 2026-08-24 — deliver GPOM (and future) cuts as individual clips imported into Premiere, not as an ffmpeg-concatenated scene file"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 49567e62-7916-48e1-9eb7-b3cac567c10b
  modified: 2026-08-24T10:49:47.520Z
---

**Ruled by Kai, 2026-08-24.** Finished video cuts go into Premiere as **individual
clips, imported one per beat** — not as a single ffmpeg-concatenated scene file.

**Why:** a concat is a frozen edit. Once the beats are welded together, trims,
re-orders, transitions, and per-beat grades all require rebuilding from the takes.
Importing the raw clips keeps every one of those decisions live on the timeline.

**How to apply:**
- Keep using `ffmpeg -f concat -c copy` to produce a `*-ROUGH.mp4` **for preview
  only** — that stays useful for judging pace and showing Kai a cut quickly.
- The concat is **not the deliverable**. The deliverable is the clips plus a
  Premiere sequence built from them (`premiere_import` then `premiere_insert_clip`
  per beat), so the beat order lives on the timeline rather than in `assemble.sh`.
- The per-cut `assemble.sh` scripts in each scratch folder remain the record of
  intended beat order — use them as the import/insert order.

See [[premiere-bridge-initiative]] for the bridge itself and its 27 tools, and
[[still-approval-gate]] for the gate that runs before any of this.
