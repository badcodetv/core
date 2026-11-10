# Drive clean-up call: Kai + Jack, before Jack's first clone

Found 2026-11-10 in "Badcode - Official" on Google Drive. **Nothing has been deleted.** On the call, Kai and Jack
mark each row **Keep** or **Delete**; Claude then deletes only the rows marked Delete (they go to Drive's bin,
restorable for 30 days) and records what went here.

**Marked on the shared page:** https://claude.ai/artifact/8uxSsL3bAxB1ACUdG49dyY (source: `2026-11-10-drive-handover.html` beside this file).
Before deleting, Claude copies the page's `marks` into `feedback/drive-handover/` next to this file and commits them.

**Running order for the call**
1. Set up Jack's machine (`scripts/drive/README.md`, steps 1–4: install, sign in, check the folder list).
2. Go through the table below, one folder at a time, and mark each row.
3. Claude deletes the Delete rows.
4. Jack tells Claude where his Karen music folder lives, checks `status karen-music`, and pulls.
5. Shared-timeline test: Jack asks "show me the timeline for the Karen music video".

## How a file got on this list

- It's a video over 150 MB in one of the five synced story folders on Drive.
- **No Premiere project uses it.** Checked against the media lists inside all 13 story projects (on Drive and
  on Kai's machine). The check is proven to find files that *are* used, e.g. Karen's `clips\1.mp4`.
- So it is a finished export, a test export, or a preview: something Premiere or a script made, not a source.
- "Kai has it" = a copy sits on Kai's machine too, so deleting it from Drive doesn't lose it.

## The list

| # | Drive folder | File | Size | What it looks like | Kai has it | Keep / Delete |
|---|---|---|---|---|---|---|
| 1 | Karen Story | `Karen story vid.mp4` | 2.55 GB | the finished Karen Story film | no | |
| 2 | Karen Music | `story vid/Karen story vid.mp4` | 2.55 GB | the same Karen Story film again, filed in the Music folder | no | |
| 3 | Karen Music | `renders/karen-music-final-2026-11-09-4k-youtube.mp4` | 2.08 GB | the finished Karen music video, 4K, as uploaded to YouTube | yes | |
| 4 | Karen Music | `All Day to Complain - yes.mp4` | 2.06 GB | an mp4 of the song; the project uses its **mp3**, not this | yes | |
| 5 | Karen Music | `clips/recut/cut-r1…r5/picture.mp4` (5 files) | 1.27 GB | old rounds' picture tracks; a script rebuilds them, and the sync tool no longer uploads them | yes | |
| 6 | Camping Story | `Camping story video.mp4` | 0.59 GB | the finished Camping Story film | no | |
| 7 | Camping Music | `camping vid/camping.mp4` | 0.46 GB | a Camping music video export | yes | |
| 8 | Camping Music | `camping vid/test.mp4`, `test 2.mp4`, `test 3.mp4`, `test 4.mp4` | 1.78 GB | test exports | yes | |
| 9 | gitpush-origin-master | `clips/the-gaze/PREVIEW-the-gaze-wip.mp4` | 0.16 GB | a work-in-progress preview of a scene since dropped from the film | yes | |

Total if all go: about **13.5 GB**.

**Kept on purpose, not on the list:** `camping vid/camping.mpeg` (5 MB). It looks like an export, but the Camping
project uses it.

## Close calls (kept by the current rule; say if you want them gone too)

- **Karen Music, `clips/recut/cut-r1…r5/preview.mp4` and `cut-final/preview.mp4`** (~1.5 GB): each round's
  rough-cut preview. The rule keeps these because a timeline page plays them; `cut-final` is the one the Karen
  timeline test needs, so **keep cut-final**. The older rounds' previews are only needed to rebuild old rounds' pages.
- Videos under 150 MB weren't checked.

## Not part of this call, but seen on the way

- **Camping Music:** Kai's machine keeps its files at the top level, Drive keeps them in `camping vid/`. Settle which
  layout wins before anyone pushes Camping Music, or the push makes a second copy beside the first.
- **Karen Story:** Kai's machine has `vids/vids/...` where Drive has `vids/...`, and a project saved 5 Nov
  (`Karen vid_1.prproj`) newer than Drive's (21 Aug). Same question before any Karen Story push.

## Decided

Marked on the page during the call (Kai + Jack, 2026-11-10; dump: `feedback/drive-handover/marks/`):
rows 1, 2, 3, 4, 6, 7, 8, 9 **Delete**; row 5 **Keep** (old Karen round picture files).

- ✅ Binned by Kai's account: row 3 (Karen 4K final), row 9 (GPOM gaze preview).
- 🟡 Refused, owner only: rows 1, 2, 4, 6, 7, 8 were uploaded by Jack, and Drive lets only a file's owner bin it.
  Jack bins them himself (Drive in the browser, or `rclone delete` once his sync tool is set up).
