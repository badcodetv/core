---
name: gpom-clip-inventory
description: 2026-08-26 — all 209 GPOM takes consolidated into clips/ and imported into gpom-story.prproj as six per-cut bins
metadata: 
  node_type: memory
  type: project
  originSessionId: 64a16109-6f7e-49f6-a47d-274a9605b3cb
  modified: 2026-08-26T14:50:20.457Z
---

**2026-08-26:** every GPOM take was consolidated under
`D:\badcode-videos\gitpush-origin-master\clips\` and imported into `gpom-story.prproj`
as **209 individual clips in six bins** — replacing the three ffmpeg composites
(`s01-earth.mp4`, `s02-hong-kong.mp4`, `s03-plant-room.mp4`) as the thing to cut from.

| Bin | Cut | Clips | Source |
| --- | --- | --- | --- |
| `01-s00-orbital` | 1 · s00 | 62 | `clips/s00/` |
| `02-s01-push` | 2 · s01 | 18 | `clips/s01/` + `superseded/` + `s01-test/` |
| `03-plant-room` | 3 | 23 | `clips/plant-room/takes/` |
| `04-bulletin` | 4 | 84 | `clips/bulletin/takes/` |
| `04b-bulletin-v2` | 4 (v2) | 9 | `clips/bulletin-v2/takes1080/` |
| `05-empty-street` | 5 | 5 | `clips/empty-street/takes1080/` |
| `06-vantage` | 6 | 8 | `clips/vantage/takes1080/` |

Rule applied: **1080 where a `takes1080` twin exists, 720 otherwise.** Rejected takes
are imported too — the point is a re-orderable montage in Premiere, not a re-render.

Cut 7 (`ghosts`) has **locked plates but no video fired** — 7 stills in
`clips/ghosts/locked/`. `prompts.md` §2c was stale on cuts 5/6/7 and is now corrected.

The five Desktop scratch folders were verified by recursive md5 and then deleted.

Related: [[clips-folder-convention]], [[premiere-import-clips-individually]],
[[premiere-bridge-initiative]]
