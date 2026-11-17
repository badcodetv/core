---
name: export-from-premiere-not-ffmpeg
description: Jack 2026-10-19 — final/upload files are exported from Premiere only; never re-encode the finished film in ffmpeg (it looked blurry and the brightness weird).
metadata:
  node_type: memory
  type: feedback
  originSessionId: f0874d3f-cec7-4569-90f2-f727816ff89a
  modified: 2026-10-19T15:35:15.879Z
---

Jack, 2026-10-19, on `karen v2 - UPLOAD.mp4` (my ffmpeg range-conversion + loudnorm re-encode of a Premiere render): "the upload youtube version made the quality weird and blurry. just do it from premiere from now on."

**Why:** the upload was a second lossy pass on a 1080p downscale of a 4K sequence, and the full→limited conversion plus a 20–233 clamp changed how the blacks looked.

**How to apply:** make delivery fixes inside Premiere (a new cut/sequence for the changes, export settings or a preset), export once from Premiere at the sequence's resolution, then run `scripts/delivery-qc.sh` on that file read-only. ffmpeg stays fine for building pieces that go INTO the edit (clips, dubs, cards), not for the final file. Related: [[never-rm-imported-premiere-media]], [[jack-uses-premiere-pro-25-6]].
