# Camping MV: new action stills for Bob and Tarquin (Jack, 2026-11-06)

Jack's words: `cleanroom/jack.md`. Real Bob and Tarquin (Flow Characters @Bob / @Tarquin, project camping-v2 `9b729074`), extra
action shots for the music video (`camping balaclava 1`). Clean room: web research `cleanroom/research.md`; the 37 existing action
shots as a contact sheet (`cleanroom/existing-action-sheet.jpg`); three sealed writers (`brief-w1..3` → `w1..3.md` → `prompts.json`):
Bob's world (b), Tarquin's world (t), mirrored pairs Bob/Tarquin (x). Writers overlapped on four shots; b1, t1, t2, t4 rewritten.

Run: `cleanroom/run_stills.mts`, NB2 16:9 x2, Character cast. Stills: `<media>/moodboard/<id>r1-<take>.jpg`
(media = `songs\camping vid\action`).

⚠ Flow trap (2026-11-06): in this big project the harvest returned OLD tiles and lagged one prompt behind (a shot's files held the
previous prompt's images). Every still was sorted by eye against its prompt; strays are in `<media>/moodboard/_junk/`. Also: a Suno
`record` running in the same browser deleted the stills' download folder at exit (ENOENT) — never run both at once.
t1 (Tarquin, oyster at Borough Market) never came back in three tries: not on the page.

Page: https://claude.ai/artifact/XNEc7Q7fADNmZjpVhRtCz3 — round 1 picked (12, feedback/moodboard-r1); round 2 (bleak Bob b22–b26, Tarquin action t21–t26 u23 u25; r2 prompts in cleanroom/r2, prompts-r2.json) awaiting picks. b21 never returned; b23 shows a TESCO sign. Next: read votes → animate picks (Omni) → cut in.

## Clips + new sequence (2026-11-06 evening) — Jack: "song 2 maybe.mov is the new song for the new sequence but keep the other sequences ... make the videos and put them in premiere in the new sequence"

- 24 picks (scene.json `picked`; votes in feedback/moodboard-r2). Motion: web research `cleanroom/clips/research.md`, three sealed writers
  `cleanroom/clips/brief-c1..c3.md` → `c1..c3.md` → `video-jobs.json` (extra). Omni 1.1 Flash, Frames, 16:9, 8 s, 720p, x1.
  Videos run in a FRESH Flow project `9b36496c` (scene.json flow_project; the stills project is `stills_project`).
  Writers flagged: b26, t3, x4, x6 stills don't match their descriptions; their motion starts from the frame as it is.
- Runner: `scripts/scene/run-rolling.mts` (NEW, Jack asked for a rolling queue): SLOTS=5 clips in flight, each harvested and replaced the
  moment it finishes; submitted-not-on-disk clips (run.log) count as in flight at start; SEED=1 marks tiles already downloaded.
  Renders took ~2–4 min each once rolling. Clips land as `<media>/video/ca-<key>-<still>.mp4` (match.py names them by first frame).
- Premiere (project `songs\camping vid\camping vid Copy-test_1.prproj`, open in Premiere 2026): `camping balaclava 1` cloned to
  **`camping song 2`**; A1 = `song 2 maybe (audio).wav` (bin `song 2`, extracted from the .mov so its picture stays off the timeline).
  `camping` and `camping balaclava 1` untouched. Song 2 is NOT the old song shifted (section offsets −2…+7.6 s), so the old picture is
  not on its beat; song 2 measures 176 BPM, first downbeat 0.122 s. Overwrite onto track index 6 creates V7 (tested, probe removed).
- Placement plan `premiere/place.py` → `plan.json` + `place-N.js`: every clip 2 bars on V7, one every 6 bars from 15.1 s to 206 s,
  Bob's first, Tarquin's middle, mirrored pairs at the end; in point 0.2 s. Mute V7 = the old cut.

## ▶ RESUME HERE
1. Clips: check `<media>/video/` has all 24 `ca-*.mp4` (re-run `SEED=0 npx tsx scripts/scene/run-rolling.mts docs/stories/camping/mv-action`
   for any missing — it skips what is on disk). Frame-check them (contact sheet, Bob never smiling, no morphs).
2. 1080p silent copies → `<media>/video/premiere/` (ffmpeg scale=1920:1080:flags=lanczos, -an), import to bin `action clips`.
3. Activate `camping song 2`, run `place-0.js`, `place-1.js` via premiere_eval, check V7 (24 clips, no slivers), save.
