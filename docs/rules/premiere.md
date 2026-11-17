# Premiere: standing rules
> Moved out of Claude's per-machine memory on 2026-11-17 (the context reset) so both Kai and Jack have them.
> Mechanics and working habits only: no look or sound belongs here (that lives in a story's `badcode.md`).
> Originals: `archive/messy-context-2026-11-17/memory/`.

## Jack 2026-10-19 — final/upload files are exported from Premiere only; never re-encode the finished film in ffmpeg (it looked blurry and the brightness weird).

Jack, 2026-10-19, on `karen v2 - UPLOAD.mp4` (my ffmpeg range-conversion + loudnorm re-encode of a Premiere render): "the upload youtube version made the quality weird and blurry. just do it from premiere from now on."

**Why:** the upload was a second lossy pass on a 1080p downscale of a 4K sequence, and the full→limited conversion plus a 20–233 clamp changed how the blacks looked.

**How to apply:** make delivery fixes inside Premiere (a new cut/sequence for the changes, export settings or a preset), export once from Premiere at the sequence's resolution, then run `scripts/delivery-qc.sh` on that file read-only. ffmpeg stays fine for building pieces that go INTO the edit (clips, dubs, cards), not for the final file. Related: `never-rm-imported-premiere-media`, `jack-uses-premiere-pro-25-6`.

## Never delete or overwrite piece files in a folder Premiere has imported; rebuild into a fresh folder (Jack hit a Link Media dialog, 2026-10-18)

Never `rm` or overwrite rendered pieces inside a folder that Premiere has imported (for example `clips/short6`).
Rebuild into a new folder (`clips/short6b`) and import from there.

**Why:** 2026-10-18. Clearing cached pieces in `clips/short6` before a rebuild left 19 items in the old bin offline, and
Jack got a "Link Media … Missing media" dialog. The fix was removing the unused stale bin.

**How to apply:**
- A builder's cache folder is the Premiere source the moment it is imported.
- Change its OUT folder, or copy the finished pieces to a fresh folder, before re-laying a sequence.

See `bank-robbery-resume`.

## Jack 2026-10-19 — stop exporting review renders; do the work in Premiere and let him watch the timeline.

Jack, 2026-10-19 (Karen v3): "please stop doing the renders, only work in premiere".

**Why:** each review render took minutes and produced files he didn't need; he watches in Premiere.

**How to apply:** make changes on the sequence and save; check with `premiere_get_sequence` / frames pulled from SOURCE files with ffmpeg (no sequence export). Only export when he asks for a file. Assets that go INTO the edit (stills, graphics, dubs) can still be made outside Premiere. Related: `export-from-premiere-not-ffmpeg`.

## Jack 2026-11-16: use only the newest Premiere (27.0.0, project Version 46); when Premiere converts a project, keep the new copy under the ORIGINAL name and delete the old one, never leave _1 files

Jack, 2026-11-16: "can we just have all of them in 2027 premire as in the latest one and delete the old ones, i dont want multiple versions for no reason", then "please clean up for all of them".

Premiere on Jack's machine is now **27.0.0** (`premiere_status` appVersion). Project format stamp (`zcat x.prproj | grep -o '<Project ObjectID="1" ClassID="[^"]*" Version="[0-9]*"'`): 43 = Pro 25.x, 45 = 26.x, 46 = 27.

Done 2026-11-16: 14 pairs swapped (newest copy renamed to the original name, old copy + its .prin deleted; the three empty "no master recording*.prproj" deleted, the real one is no-master-recording.prproj). Repo scene.json / agreed lists now point at the original names. ~100 projects are still Version 43; each converts when next opened.

**Why:** duplicates confused which project is live; keeping the original name keeps every repo path and Drive list valid.

**How to apply:** after opening any project in Premiere, if it made a `name_1.prproj`, close Premiere, delete the old file and rename the copy back (Premiere must be closed for the rename). Kai must be on Premiere 27 too: an older Premiere cannot open these projects; anything pushed to Drive needs that.

Supersedes `jack-uses-premiere-pro-25-6`.

## Before telling Jack a cut is built, transcribe the render and compare it to the script line by line; never trim speech on an LLM's timestamps

Jack, 2026-10-10, on the first Money For Something topical cut: "there are a lot of lines missing, please listen and watch it then compare it to the script". Seven of 27 lines had lost their endings, and I had reported the cut as built.

**Why:** I trimmed each clip at the time Gemini said the last word ended. Those times were out by up to three seconds wherever a line had a pause, and I never compared the finished cut with the script. The crowd-noise check I did run could not see it.

**How to apply:** for any cut with spoken lines, transcribe the finished render and diff it against the script before reporting (for this show: `scripts/money-for-something/topical-verify.py`). Take word timings from a local speech model with word timestamps (`topical-words.py`, faster-whisper in `~/.cache/badcode-whisper/venv`), and cut tight only where it heard every scripted word; otherwise keep the clip long. Join clips by re-encoding, not stream copy (the copy join left broken audio timestamps). My reading: this holds for every film with dialogue, not only this show. See `mmt-topical-show-october`, `mark-unverified-claims-as-unverified`.

## A cut made in Premiere before the timeline tool existed

Moved from the old CLAUDE.md (Kai, 2026-11-13): bring such a cut onto a timeline page with `scripts/scene/premiere-to-edl.py` (`--stem`, `--beats-from`) plus a Premiere render. **Check which sequence is actually open first**: the Bank Robbery page was once built from the wrong cut.
