---
name: drive-agreed-cut-only
description: "Jack 2026-11-10 — Drive uploads carry only the agreed cut (scripts/drive/push-agreed.sh), never the whole story folder"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8098e344-790a-4391-b5a5-f4440c9f1c83
  modified: 2026-11-10T15:24:14.528Z
---

Upload only the agreed cut of a story to Drive, never the whole folder ("only use the cut we agree on, ie the latest one on the timeline", "do only the agreed cut for all of them").

**Why:** whole folders were ~32 GB of old cuts, renders and per-cut work folders on Jack's ~0.5 MB/s upload; the agreed cuts were ~2.5 GB.

**How to apply:** `scripts/drive/push-agreed.sh <story>` then `--go`, lists in `scripts/drive/agreed/`; never `drive.sh push` for a story that has a list. Procedure in the drive-sync skill and scripts/drive/README.md. State on 2026-11-10: bank-robbery-music, bank-robbery-story, camping-story extras and the cut 10 render all up (0 left); camping-music finished 16:07 (77 copied, 0 left): all four agreed cuts are on Drive; next is the timeline test. 2026-11-11: everything else deleted on Drive (bin) and on Jack's PC (permanent) for these three; old sequences are offline for good. The Drive sync comes before the timeline test (Kai: one step at a time). Related: [[resolve-media-paths-via-localmap]].

2026-11-11: Camping Story added: agreed cut = `0 synced` in `Camping Video NEW!/camping jack/camping jack.prproj`; Jack's camping-story folder is `Camping Comic` (Drive mirrors that level, not `Camping Video NEW!`). Cleaned to it on Drive and PC; `Camping Comic/badcode camping`, `music video`, `other`, `shorts` untouched. Before any clean-up: read the agreed sequence's media from the saved .prproj (nested sequences followed) AND scan every recent .prproj for refs to the delete list — Jack warned new cuts borrow old clips. All five agreed cuts on Drive; record in docs/misc/2026-11-10-drive-cleanup-call.md.
