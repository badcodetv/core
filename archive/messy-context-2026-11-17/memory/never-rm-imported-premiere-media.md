---
name: never-rm-imported-premiere-media
description: Never delete or overwrite piece files in a folder Premiere has imported; rebuild into a fresh folder (Jack hit a Link Media dialog, 2026-10-18)
metadata:
  type: feedback
---
Never `rm` or overwrite rendered pieces inside a folder that Premiere has imported (for example `clips/short6`).
Rebuild into a new folder (`clips/short6b`) and import from there.

**Why:** 2026-10-18. Clearing cached pieces in `clips/short6` before a rebuild left 19 items in the old bin offline, and
Jack got a "Link Media … Missing media" dialog. The fix was removing the unused stale bin.

**How to apply:**
- A builder's cache folder is the Premiere source the moment it is imported.
- Change its OUT folder, or copy the finished pieces to a fresh folder, before re-laying a sequence.

See [[bank-robbery-resume]].
