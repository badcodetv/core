---
name: resolve-media-paths-via-localmap
description: "Before saying media is missing, resolve the path with scripts/drive/localmap.py; repo paths are the writer's machine (/mnt/d is Kai's)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: bc7bbdea-7bbf-4c00-9b6b-7253574b79da
  modified: 2026-11-10T13:46:55.159Z
---

Paths in edl.json / scene.json / final-edl.json are whatever machine wrote them (Kai's are `/mnt/d/badcode-videos/...`). On Jack's machine there is no /mnt/d; the same story sits under his `badcode.local.json` folder (e.g. Karen music = `C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation\songs\Karen`). Always check a file with `python3 scripts/drive/localmap.py path "<path>"` (or `localize()`) before declaring it absent.

**Why:** 2026-11-10 I told Jack the Karen footage "isn't on this machine" after `ls /mnt/d` failed. It had been pulled with drive-sync and all 105 shots were there. He had to stop the work to debug a sync that was fine.

**How to apply:** any media-existence check, in any skill. `renders/` really is never synced (exclude.txt), so a missing render is expected, not a sync fault. See [[drive-sync]].
