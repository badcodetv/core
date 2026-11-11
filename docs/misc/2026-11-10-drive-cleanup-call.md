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

## Jack's sync, afternoon (agreed cut only)

Kai's plan: get Drive in sync first, one story at a time; the timeline test comes after. Jack (2026-11-10): upload
**only the agreed cut** of each story, not the whole folder. Tool: `scripts/drive/push-agreed.sh` with the lists in
`scripts/drive/agreed/` (how they are built: `scripts/drive/README.md`, "Agreed cut only"). About 2.5 GB went up
instead of about 32 GB; every story checked at 0 left after.

- ✅ **Karen Music:** pulled to Jack's machine (481 files, 4.3 GB), in sync both ways. Jack's folder recorded.
- ✅ **Bank Robbery Music** (`Balaclava Gang 9` in `bank robbery_1.prproj`): 64 files. Drive folder new today
  (Jack made it; row added to `folders.json`). The cut's records were only on branch `stupidity-optimised-script`:
  its three Bank Robbery song commits were cherry-picked to main, `premiere.current` corrected cut7 → cut9.
- ✅ **Bank Robbery Story** (`bank robbery - cut 10` + `bank robbery short - cut 7g`): 205 files, with the cut 10
  render. Drive folder new today. The other 37 per-cut work folders (~13 GB) and 30 old renders stay local.
- ✅ **Camping Music** (`camping song 2 beat 9` in `camping vid Copy-test_1.prproj`): 88 files plus timeline
  `r10/cut/edl.json` + `preview.mp4`; beat 9's 9 borrowed `new clips` went to Camping Story, and its logo clip to
  Camping Music under `badcode logo designs/draft 1/4.mp4` (outside every story: Premiere asks for it once).
- 🔴 **Camping Music layout, as warned above:** Jack's folder *is* `camping vid`, so his files went to the top level of
  the Drive folder, beside Drive's older `camping vid/...` copy. Both layouts are now there. Settle which wins before
  anyone pulls Camping Music. Drive also holds 129 files newer than Jack's (Kai's), left untouched.
- 🟡 **Not pushed:** Camping Story (Jack 640 files Drive lacks, Drive 177 Jack lacks) and Karen Story (Jack 63
  Drive lacks, incl. `Karen vid.prproj` + `Karen vid_1.prproj`). Kai and Jack to decide; GPOM is Kai's to push.
- 🟡 **Timeline test, when it runs:** Kai records his Bank Robbery Music folder (`drive.sh where`), pulls, then the
  edit round trip. The gang's own cut scripts (`plan_rN.py`, `assemble_cut.py`, `premiere_place.py`) read paths
  without `localize()`, so a new cut must be made on Jack's machine or those scripts fixed first; the page and
  `premiere-to-edl.py` translate fine. Camping song's records (mv-r10, mv-song2, mv-balaclava, mv-action) are still
  only on `stupidity-optimised-script`.

## Clean-up to the agreed cuts (Jack, 2026-11-11)

Jack: "delete everything that is not the agreed upon version of the song or story and everything it needs."
Confirmed on both Drive and Jack's PC, the old Camping Music copy included. Kept = the files in
`scripts/drive/agreed/<story>.list`, checked twice before deleting: against Premiere's sequence snapshots and by
reading each agreed sequence's media out of the saved `.prproj` (nothing missing). The pages need only each cut's
`edl.json` + `preview.mp4`, both kept. Every kept file checked present after, and each story still 0 to push.

- **Drive (to the bin, restorable 30 days):** Bank Robbery Music 98 files (0.3 GB, left by the stopped full push);
  Camping Music 179 files (4.7 GB: the old `camping vid/` copy with `camping vid.prproj` + `Copy-test.prproj`,
  test exports, `vids/` incl. drive london and ending credits, auto-saves). Bank Robbery Story was already clean.
- **Jack's PC (permanent):** Bank Robbery Music 5,028 files (5.1 GB: other MV versions noir/alt, gang cuts 1-8,
  moodboards); Bank Robbery Story 4,435 (22.2 GB: 37 per-cut work folders, 30 renders, unused sources); Camping
  Music 1,828 (3.6 GB: balaclava, action and r10 working files, unused clips, previews, auto-saves). Kept on top of
  the lists: each folder's `.bridge/` snapshots and the two `.prin` files beside the Bank Robbery song projects.
- **Now:** Bank Robbery Music 82 files / 352 MB, Bank Robbery Story 230 / 875 MB, Camping Music 108 / 1.5 GB.
  Every other sequence in those projects is offline from now on, on both machines; the agreed ones play.
- **Not touched:** Camping Story (its own cut not chosen yet; beat 9 borrows 9 of its clips), Karen Music,
  Karen Story, GPOM.
