---
name: camping-next-three-premiere-jobs
description: "Jack's three picked camping-video Premiere jobs (one grade, subtle camera moves, invisible cuts) were DONE 2026-09-14 as a first pass awaiting his review; full undo recipe in assembly.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 44ee320f-60fb-4104-8b18-c91b4daa369b
  modified: 2026-09-14T17:00:05.153Z
---

On 2026-09-14 Jack picked three Premiere jobs for the camping video and then asked for them to be done,
"but if it makes any mistakes be prepared to undo these actions":

```
- ✅ One grade for the whole film: Lumetri + 3% mono grain on all 59 clips, measured before/after
- ✅ Subtle camera moves in post: 7 push-ins/tilt incl. the owed 12d tilt (now on 35.mp4, a 16:9 compromise)
- ✅ Invisible cuts: 4 Film Dissolves + fade-up out of the crash (3a) black
```

All three were done the same day as a **first pass, not yet reviewed by Jack at speed**.

**Why:** He wanted them done but reversible, so the review may come back as "undo X".

**How to apply:**
- When Jack asks about the camping video, report these three as done and waiting on his review. Ask what he thought of them at speed.
- **Undo recipe, values and reasons:** `docs/stories/camping/assembly.md`, section *one grade, camera moves, invisible cuts (2026-09-14)*.
- **Full revert:** `camping jack/backups/camping jack.pre-grade-moves-cuts.2026-09-14.prproj`.
- **Project:** `camping jack.prproj`, sequence `0 synced`, driven over the UXP bridge.
- **Keyframes are clip-relative**, and export_frame writes `.png.png` (`docs/premiere/api-notes.md`).
