# Camping music video v2 ("Signs"): the build kit

Everything needed to rebuild the 2026-09-28 cut from the stills. **What each file is for:** the words (prompts,
verdicts, the timeline table) live in
[`docs/stories/camping/music-video-v2-video-prompts.md`](../../docs/stories/camping/music-video-v2-video-prompts.md).
This folder holds the machinery.

| File | What |
| --- | --- |
| `video-prompts.json` | The 27 Omni Flash motion prompts, keyed by image number (`n`) and storyboard shot (`shot`) |
| `mv2run.mts` | The Flow runner: upload a plate, Omni 1.1 Flash · Frames · 16:9 · 720p · 8s · x1, detect the new tile by key, download "720p Original size". It refreshes and retries on "unusual activity" and when the frame slot fails, and it retries a failed download **without** regenerating |
| `suno-aligned-198db8b9.json` | ⚠ OLD take. `song.wav` became [3a433539](https://suno.com/song/3a433539-0507-4d9e-b714-d134c0e1e509) on 2026-09-29. Suno's word alignment for the previous song.wav take (`studio-api…/gen/198db8b9-91a2-4d45-be54-365d028cbca3/aligned_lyrics/v2/`) |
| `suno-aligned-3a433539.json` | ✅ **Current take.** Suno's word alignment for 3a433539, pulled 2026-09-30 with `scripts/suno/.tmp/align.mts` (token from the `__session` cookie). `lyric-lines-3a433539.txt` is the same, rolled into lines |
| `lyric-timing.py` | Builds sign-text configs timed to the alignment: each line appears 2 frames before its first word |
| `lyric-lines.txt` | The same, rolled up into timed lines, which the edit was cut to |
| `edit-plan.json` | The V1 layout, as `[clip, start, end, inPoint, cue]` |
| `signs.json` | Every sign's four corners (on frame 0 at 1280×720), lyric and style |
| `signtext.py` | Puts the lyric ON the sign: layout, per-word tilt, perspective warp, frame-by-frame tracking (ORB + RANSAC, smoothed), surface blend and grain |

## Rebuild

**Work dir:** `export MV2_WORK=/tmp/camping-mv2`, holding `plates/mv2-plate-NN.jpg` (the images scaled to 2752
wide), `takes/`, `text/` and `font/`. Upload from WSL disk, never `/mnt/c`.

1. **Clips:** from the repo root, with the Flow browser on channel 1 and signed in, close the agent side panel, then
   run `npx tsx scripts/camping-mv2/mv2run.mts [NN …]`. Existing takes are skipped.
2. **Sign text:** get the fonts into `font/`, all Google Fonts:
   - `PermanentMarker-Regular.ttf` (Apache 2.0)
   - `Cinzel.ttf`, the variable `Cinzel[wght]` (OFL)
   - `DotGothic16.ttf` (OFL)

   Then, in a venv with `opencv-python-headless pillow numpy`, run `cd $MV2_WORK && python signtext.py 02 03 … 26 11b`.
3. **The 06 ping-pong** (16 s, to cover the instrumental break):
   `ffmpeg -i text/06.mp4 -filter_complex "[0:v]split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0,format=yuv420p" -an -c:v libx264 -crf 14 06-pingpong-16s.mp4`
4. **Stat card** (V2, 8.00–15.54 s): Permanent Marker drawtext on a transparent 7.54 s canvas, qtrle/argb. The text
   is "318 million people\nhave no home." at 72 px, then "— UN-Habitat, 2026" at 34 px from 0.6 s. White, 3 px black
   border, drop shadow.
5. **End card** (V1, 238.33–242.33 s): "BADCODE", Permanent Marker at 150 px, white on black, 4 s, hidden at
   0.083–0.167 s and 0.25–0.29 s for the flash.
6. **Premiere** (bridge):
   - Import song.wav and place it at 0 on A1.
   - Place clips on V1 at the `edit-plan.json` times, with overwrite in time order so each clip trims the one before.
     For a mid-clip in-point: insert, `trim inPoint`, then `move -inPoint`.
   - Mute A2 (the clips' own audio): `(await seq.getAudioTrack(1)).setMute(true)`.
   - To swap in the signed versions, relink with `ClipProjectItem.changeMediaFilePath`. It keeps every cut.

**Output folders on Jack's machine:** `…\Camping Comic\music video\` holds `videos\` (raw clips 01–27),
`videos with text\` (signed clips plus 11b and the ping-pong) and `clips\mv2\` (the stat card, end card and the old
ping-pong).
