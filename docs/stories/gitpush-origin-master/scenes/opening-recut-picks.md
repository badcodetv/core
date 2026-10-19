# GPOM opening recut: picks (17 Oct 2026)

Kai's picks from the opening-recut mood board
(https://claude.ai/artifact/SmYozTsKzUzB6Ask9rQs5H; votes in its db `votes`, notes in `notes`).
Timeline: `gpom-s01` in `gpom-story.prproj`. Stills: `D:\badcode-videos\gitpush-origin-master\clips\opening-recut\moodboard\`.
Prompts: [`opening-recut-moodboard.json`](./opening-recut-moodboard.json). Nothing is on the timeline yet; no video credits spent.

| Timeline now | Verdict | Replacement still(s) |
|---|---|---|
| 0:15 `e02-far` (near-miss car) | replace | **ST4-c** (messy rain plaza, cabinets in, people out) + **DB1-b** (one desk, one box, KEEP-rain's cabinets) |
| 0:20 `e03-pass` (rain + server cabinets) | **keep** | — |
| 0:23 `02-23-f2-b` (champagne) + 0:26 `04-21-f1-b` (graph) | replace | **TO1** with the table added (**TO1T-a** preferred) + **TO2** (the email that wrote itself) |
| 0:29 `33-15-f1-b` (shop) | replace | **BR1** (mother, one loaf, toddler) |
| 0:34 `03-exchange-alive` (70s exchange) | replace | **MK5-b** (one trader, one chart) + **MK3P** (banknote hall: the trillion — re-made in £50 notes 17 Oct, Kai: the film is anchored in the UK; pick a/b/c on the storyboard) |
| 0:36 `04-trading-floor` (laughing traders) | **keep** | — |
| 0:40 `2-glide-v2-b` (zoom into tower) | **keep** | — |
| 0:57 + 0:59 servers + LED, after the push | keep, add text | ACQUIRING RESOURCE LOCK / NEW OWNERSHIP TRANSFERRED — **style not yet voted** (TX1–TX4) |
| 1:02:13 drop, building site | replace | Choir: **WL1-b** (inside the well, ship's light pouring down) → **WL2-b** (rise out: the army round the rim, ship above) |
| drop, second line | replace | Colossus: **EY1-b** (eye on the summit at sunset) + **EY2-c** (eye at impossible scale over the valley town); ref CO6 |

## Animation notes
- **The eye:** the red rim dots light in sequence so a dot seems to travel round the ring as the words are sung — the lights stay fixed. Veo won't time it to the vocal: animate the eye in Flow camera-locked, lay the chase in post (ffmpeg/Premiere) on the beat.
- **The choir:** WL1→WL2 as one continuous rise out of the well is the move Kai described.

## Still open
- Which text style (TX1 on the CRT vs TX2–4 over the servers/LED).
- WL3 (CH7's face in the well) had no vote.

## Storyboard picks (17 Oct, board 7HjuaiKdhp2EYYMxaepsTi)

Animation option **a** on every frame (1–15). Stills: #5 **TO1T-a**, #6 **MK3P-c** (pounds), #12 **WL3-b**, #15 **EY4-c** (re-made from EY1-b: same eye, mountain, sunset, zoomed out, no town). #5 fallback approved: if nine moving people warp, redo with only the front two clinking.

Kai's notes:
- **#10 text:** exactly the same font as the existing terminal. Simulate the command: the cursor moves to the next line and the text is typed out, as `git push origin master` is. Fast: it must take about the same time as `git push origin master` does to appear, because it squeezes into the second bar.
- **#15 scale shot:** must be the same eye and the same mountain as #14 (the eye becomes a character), and the same sunset, like a zoom-out. No town underneath: the humans have gone. → EY2-c needs a re-make from EY1-b.
- **#10 built and ruled (17 Oct): version B.** `scripts/gpom/build-terminal-ownership.py OUTDIR 4 28 12` (4 frames after Enter, both lines typed in 28 frames, 12-frame hold, then the usual switch-off). Clip: `clips/opening-recut/terminal/HK-b4-terminal-own-B.mp4`, a drop-in for `HK-b4-terminal` on gpom-s01 with the same in/out (1.083 → 7.792). Version A (git-push speed) rejected by Kai: B's timing is "perfect".
- **#5 re-made (17 Oct night):** Kai: the first toast was all white and cheered in unison, boring. New still **TO1T2-b** (mixed group, candid, not toasting together). Redo videos also queued for #1 (crowd still, only rain), #12 (gentler singing prompt, 4s), #14 (light flashes on/off once a second, timestamped, to cut to the beat).
- **Round 4 (17 Oct night):** robot r3b (WL3-a, silent jaw) WORKED; WL3-b is blocked on every wording, so the face is WL3-a. Kai: open the mouth much less → 12-r4. Street still re-made with fewer people and drizzle; Kai picked **ST5-a** ("top right") → 01-r3.
- Kai loved **14-r3** (strobe + travelling dot) and **05-r2** (boardroom B). Same strobe on the zoomed-out eye → 15-r2 (EY4-c).
- **#7 bread (17 Oct night):** BR1 refused by Flow (child); masked locally, re-made BR2 (empty pushchair), Kai picked B then said no pushchair at all → **BR3-a**. #4 email extension: Kai wants a view from outside the office as he writes it → stills TO3-a/b/c offered.
  Kai picked **TO3-a** for the email-from-outside shot → 04-r2.
- **#10 re-made (18 Oct):** Kai changed the reply to lower case `merge conflict detected` / `human resources acquired` (a git pun) and ruled: hold on the dead monitor and zoom into the black to the drop. Clip `terminal/HK-b4-terminal-own-C.mp4` (`build-terminal-ownership.py OUT 4 28 12 120`), on gpom-s01 **V2** 49.708→62.583 (src 0.375→13.25), Scale 100→420 + Anchor (0.5,0.5)→(0.5,0.5162) bezier, src 8.625→13.25 (timeline 57.96→62.58). Old own-B removed from V1. Email-from-outside clip `op-04-r2-TO3-a.mp4` imported to bin 08-opening-recut, not placed.
- **#4 corner re-make (19 Oct):** Kai: it is a corner office, so the outside view should look at the corner of the tower with the two window walls meeting. Stills **TO4-a/b/c** (flow_edit_image from TO3-a + TO2) offered; Kai picked **TO4-c** (furthest back) → `op-04-r3-TO4-c.mp4` (6s, locked, clean; not yet imported — Premiere panel was disconnected).
- **Flash before the drop (19 Oct):** Kai asked for a ~0.5s white jolt out of the black before the robot. `fx/white-flash-12f.mp4` (ffmpeg, 12 frames: 4 full white, then eases to black), on gpom-s01 **V2** 62.083→62.583 (moved off V5 at Kai's ask: V1/V2 are the live tracks), overwriting the terminal's last 0.5s of black; terminal now ends 62.083 (src 12.75). `op-04-r3-TO4-c.mp4` imported to bin 08-opening-recut.
- **#13 wide parade ground (19 Oct):** Kai: the cut robot → WL2-b makes the robot vanish; wants a far wider WL2-b, a vast parade ground of robot blocks (rally scale), before the mountain eye. Kai away on a call, said proceed. Stills WL4-a/b/c (edit of WL2-b); a is the closest, so b and c animated (8s, locked): `op-13-r2b-WL4-b.mp4` (floodlight towers, beams swing out), `op-13-r2c-WL4-c.mp4` (widest, blocks to the horizon, lightning). Both clean, no redraw; imported to bin 08-opening-recut, NOT placed (Kai is hand-cutting 62.6–68.4).
  Kai picked **C** (`op-13-r2c-WL4-c.mp4`).
