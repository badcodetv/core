---
name: no-renders-premiere-only
description: Jack 2026-10-19 — stop exporting review renders; do the work in Premiere and let him watch the timeline.
metadata:
  node_type: memory
  type: feedback
  originSessionId: f0874d3f-cec7-4569-90f2-f727816ff89a
  modified: 2026-10-19T15:51:31.210Z
---

Jack, 2026-10-19 (Karen v3): "please stop doing the renders, only work in premiere".

**Why:** each review render took minutes and produced files he didn't need; he watches in Premiere.

**How to apply:** make changes on the sequence and save; check with `premiere_get_sequence` / frames pulled from SOURCE files with ffmpeg (no sequence export). Only export when he asks for a file. Assets that go INTO the edit (stills, graphics, dubs) can still be made outside Premiere. Related: [[export-from-premiere-not-ffmpeg]].
