---
name: gpom-cutting-room-board
description: "2026-09-13 — the GPOM \"Cutting Room\" artifact (scene-by-scene status board with Use/Maybe/Ignore picks) is Kai's preferred overview; keep using and updating it"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9eb649da-196a-425b-a051-d1a0777d1402
  modified: 2026-09-13T16:32:38.485Z
---

**2026-09-13:** built a review board for the whole GPOM film —
https://claude.ai/code/artifact/e4561c42-1251-433e-a87e-fbfac449d0d1 ("GPOM Cutting Room").
Kai: *"excellent review screen… we should keep using this."*

What it holds: all 17 cuts in cut order, per cut a plain summary, key line, in-flux note,
silent compressed preview video(s), beat table, every still grouped in-cut / approved /
candidate / rejected (hidden toggle), planned-shot cards for unfired cuts 8–17, and a per-cut
note box. Picks + notes live in the artifact's `db` (collections `picks`, `notes`) — read
them back with `Artifact read_db`.

**Why:** Kai was lost on where the film stood across cuts; one visual board fixed that.

**How to apply:** when GPOM state changes (a cut rebuilt, stills approved, cuts merged),
republish to the SAME url rather than making a new page. The builder (merge.py, app.js,
index.html, thumbnails, ffmpeg previews) was made in a session scratchpad and is NOT durable
unless moved into the repo — check before assuming it exists; the four inventory JSONs came
from subagents reading `prompts.md §2c`, `scenes/*`, and `D:\badcode-videos\gitpush-origin-master\clips`.

Related: [[gpom-clip-inventory]], [[clips-folder-convention]], [[parallel-thread-load]]

**2026-09-29:** no skill exists for these boards. Each one is a hand-built Artifact page with a `db` for picks. There's now a family of them: Downfall Tone Board (KowguGgWhPt4HxYuY8avN6) and **Ghosts Board, cut 5** (6RacZuR7qpTpQQSvgTPu1j). Ghosts db: `beats/<M1..G6>` {verdict keep|rework|cut, note}, `ghosts/<G1..G6>` {pick}, `notes/order|ghosts`. The builder HTML + web-size media live in the session scratchpad (`ghosts-board/`); media comes from D:\badcode-videos\gitpush-origin-master\clips\{empty-street,vantage,ghosts}.
