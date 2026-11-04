# Handoff: gpom-second-half to badcode-b6 (4 Nov 2026)

This thread owned **scene A, the kill bots** (`scenes/second-half-a-killbots/`). It also did the 4 Nov Premiere rename and built the two RENDER masters.

## Scene A: signed off

- **Status:** signed off by Kai: "it's perfect. That's the one. No changes."
- **Cut:** round 14 = cut `A-d12`, built with `scripts/gpom/second-half-video/cut3.py A --tag d12`. Length 180.54 s (3:00).
- **Timeline page:** https://claude.ai/artifact/Jjvd8FPvF4KJUnVDQLYzkQ (v16). Publish it with `capabilities {db:{}, user:{}}`.
- **Premiere:** `03 GPOM story A kill bots r11`, in sync. Older rounds are in "zz old sequences".
- **Frozen:** `final.json` and `final-edl.json` are written.
- **Today's rounds (4 Nov):**
  - **r11, cut d9:** beat 0 cuts between front, side and overhead views.
  - **r12, cut d10:** overhead re-made, with no parking bays and no grain.
  - **r13, cut d11:** rubble back on the overhead road (still `ia-09-a`).
  - **r14, cut d12:** script line 5 dropped ("And now we've worked all that out... go back and change things"), together with its overhead insert.
- **Picks page:** https://claude.ai/artifact/LYGVbM8hFn2dQ7kM2EBZbb, rounds 1–3. The picks are dumped in `feedback/intro-angle-picks/`.
- **Notes:** none unanswered. Every page note up to `at1878` is answered on the page.

## Premiere naming and masters (Kai, 4 Nov)

The live folder is "00 the film (live sequences)". Its sequences are named **`NN GPOM <part> rN`** in film order:

| Sequence | Was | Contents |
|---|---|---|
| `01 GPOM start` | gpom-1-track-and-off-switch | Kai's own sequence. **Name changed only, with his OK.** |
| `02 GPOM music end r1` | gpom-1b-mv-ending-r1 | |
| `03 GPOM story A kill bots r11` | gpom-2-A-killbots-r11 | |
| `04 GPOM story B bridge r1` | not built yet | The door thread has the name. |
| `05 GPOM story C walk out r2` | gpom-4-C-walkout-r2 | Round 7. **Page is ahead at round 8.** |
| `06 GPOM story D crossing r1` | gpom-5-D-crossing-r1 | |
| `07 GPOM story E ending r2` | gpom-6-E-ending-r2 | |

**Records:**
- Each scene.json `premiere.<round>` record now has `sequence` set to the new name, plus `was_named` and `renamed`.
- The old same-named bins kept their old names. The sync check doesn't use bin names.
- The masters are listed under `premiere.other` in `timelines.json`.

**The two masters** are nested sequences. A nested sequence follows edits made inside the sequences it contains. Both masters are 1920x1080 because they take their size from 01. Each 720p scene sits at **Motion Scale 150** (component 1, param 1).

- **`00 RENDER story`:** 01 (0–279.958 s), then A at 279.958, C at 460.5, D at 507.458, E at 597.708. It ends at 630.29 s (10:30).
  - When B is built, insert it after A, at 460.5 s.
  - Then move C, D and E later by B's length.
  - Set B's Scale to 150.
- **`00 RENDER music video`:** 01 trimmed to 161.958 s (both V1 and A1), then 02 at 161.958 s. It ends at 231.54 s.
  - A new music-end round means swapping 02 at 161.958 s.
- **A new round of any scene** goes into the master at the same slot. If its length changed, shift everything after it by the difference.

## Gotchas

- **`premiere-check.py --write` and the music-video ending:** it marks `02 GPOM music end r1` as "edited in Pr", because its audio runs about 1 s past V1 (69.58 s against an edl of 68.54 s). The music session had recorded it as "in sync", so I restored `scenes/mv-ending/scene.json` after each check run. The checker should allow for an audio tail.
- **Stale sync results:** the check reads `.bridge/state-<name>.json`. Call `premiere_get_sequence({name, params:false})` on every renamed or new sequence first, otherwise it reports old results.
- **`timelines.json` indent:** it uses **1-space** indent (the earlier "3-space" note is wrong). Write it back with `json.dumps(d, indent=1, ensure_ascii=False)`, or the diff becomes huge.
- **Flow late tile:** Flow can return the previous clip as a new take. I hit this twice today. Check the md5 against earlier takes after every video call. `flow_list_media` is not mapped on the rebuilt Flow.
- **Flow "Frames on Veo 3.1 - Fast" error:** `VIDEO_OPTION_UNAVAILABLE` is a one-off. A plain retry worked each time.
- **Premiere place script:** the Premiere bridge reports media paths with backslashes. The compact place script matches them with `.split('\\').join('/')`.
- **cut3.py round tags (d9 to d12):** each new round tag needs adding to every tag tuple, D1 to D11, plus the voices map.
  - **d10:** the colour match moves only half the contrast. Before this, the full match crunched the grain.
  - **d12:** skips script line 5 in `beat0_d1` and deletes `ANGLES[3]`. `script.json` keeps the line so older tags still rebuild.

## Owed to Kai (not urgent)

- **Stray artifact:** may I delete https://claude.ai/artifact/H2Y7bPhXW5pnH5oB6ttM4x? It's an accidental duplicate of the A timeline page from round 11. Delete only on his OK.
- **Final video size:** keep the 1080p masters (720p scenes scaled up), or export at 720p?
- **Old lady's voice:** still owed from earlier. In the closing-scene pass, re-voice her line in D in Vindemiatrix, and check C and E for her old voice.

## Uncommitted files of mine

Kai hasn't asked me to commit, so these are left uncommitted:
- `scenes/second-half-a-killbots/`: `cut-notes.json`, `scene.json`, `trail.json`, `feedback/overhead-recut-2026-11-04.md`, `final.json`, `final-edl.json`, plus the `feedback/timeline-r12/` and `feedback/timeline-r13/` dumps if they're untracked.
- The rename edits in `scenes/{mv-ending,second-half-c-walk-out,second-half-d-crossing,second-half-e-ending}/scene.json`: only the `premiere` record. Those files may also hold other threads' edits.
- `timelines.json` and `timelines/index.html`, which are shared with the other threads.
- `docs/provenance/cards/.../cut3/A-d12/` and the intro-angle still and video cards.
- This handoff file.

`scripts/gpom/second-half-video/cut3.py` with the d9 to d12 changes is already committed (e134d2f).
