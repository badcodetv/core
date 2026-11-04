# Lip sync v3: the toilet-seat row (beats 6–7), 3 Nov 2026

Kai, on the v2 row: *"it feels like we're kind of chopping bits of sound out somehow."* He was right. v2 sliced the
five lines into **23 pieces** at tempos from ×0.85 to ×1.30, so every line had gaps, fades and speed jumps inside it.
v3 plays each line as whole phrases: **8 pieces in all**, tempo **×1.00–1.15**, and a line only splits where the voice
itself pauses. The voice masters are unchanged (Kai's picks). Nothing in `cut3.py`, the timeline page or Premiere has
been touched yet.

- Preview of the row: `clips/second-half/cut3/lip-v3-preview.mp4` (20.2 s, cut3.py's row timing, picture + dub)
- Closures contact strip: `clips/second-half/cut3/lip-v3-closures.jpg` (12 fps tracked mouth; under each frame the dub's
  loudness in red and the mouth gap in black; the frames where the voice says b/p/m are outlined)
- Tables and dubs: `clips/second-half/audio/cut3-lip/cut3-lip-<name>-v3-phrases.json` / `-v3-dub.wav` (−20.5 LUFS)

## Per line

| Line | v2 | v3 clip | v3 pieces, tempo | Checks |
| --- | --- | --- | --- | --- |
| 6-0 Sandra *"Derek. You've left the seat up. [pause] Again."* | 5 pieces, ×0.85–1.25 ("A-" and "-gain" split) | **new** `video/cut3-lip-6-0-v3.mp4` (take t1) | 3 = the voice's own three phrases: ×1.00 at 0.15 · ×1.03 at 0.95 · ×1.15 at 4.37. The pauses between them are the voice's own pauses | "up" p on a shut mouth (2.28 vs 2.29); "Again" starts as the mouth opens (4.43); its tail runs ~0.1 s past the close |
| 7d-0 Derek *"I'm really sorry, love."* | 3 pieces, ×1.0–1.28, **on a clip animated to the old words "Oh, sorry, sorry, love"** | **new** `video/cut3-lip-7d-0-v3.mp4` (take t6), mouthing the right words | 1, ×1.15 at 2.15 | ⚠️ see "Still not perfect" |
| 7-0 Sandra *"Five years underground, and you still can't put a seat down."* | 5 pieces, ×1.10–1.30 | **existing** `video/cut3-lip-7-0.mp4` (L07-0-a). Four new takes all rushed "Five years underground" and lost to it | 2, split at the comma: ×1.13 at 0.00 · ×1.02 at 2.19 | "put" p on the closure (3.53 vs 3.54); ends with the mouth (4.74) |
| 7d-1 Derek *"But the world ended, Sandra!"* | 3 pieces, ×0.85–1.30 | **existing** `video/cut3-lip-7d-1.mp4` (L07d-1-a). Two new takes, neither better | 1, ×1.01 at 0.50 | "But" b on closed lips (0.54); the last syllable lands on a parted, closing mouth |
| 7-2 Sandra *"Yeah, the world ended. Doesn't mean you get to stop having manners."* | 7 pieces, ×0.85–1.25 | **new** `video/cut3-lip-7-2-v3.mp4` (take t1) | 1, ×1.05 at 0.02 | "mean" m on the dip (1.94), "manners" m on the closure (2.71); "stop" p is 0.16 s late (late is the forgiven side); the tail ends 0.14 s after the mouth closes. ⚠️ After the line (~3.0–3.5 s) the shot pulls back a touch as she folds her arms; it's inside the 0.6 s tail |

**Before → after: 23 pieces → 8. Tempo range ×0.85–1.30 → ×1.00–1.15. No cuts, fades or tempo jumps inside a phrase.**

Every dub was transcribed on its own and in the rendered row, and every word survives. Whisper hears Derek's take c
of 7d-1 as *"What the world ends, it's Sandra!"* on its own, as it always has (it heard v2 as *"What the world then, gee,
Sandra?"*). That is the voice take Kai picked by ear, and the rendered row transcribes as *"But the world ended, Sandra!"*.
**The listen tool was not run** (standing rule), so the warble check is still owed to a human ear. Only 6-0's "Again"
sits at the ×1.15 cap.

## Still not perfect

- **7d-0, Derek's "I'm".** Omni draws a long "I'm" in all seven takes: the lips close for the m 0.25–0.33 s after the mouth
  opens. The TTS take closes after ~0.13 s. With one whole piece, the voice's m lands ~0.15 s before his lips close, and
  "love" ends ~0.16 s after the mouth shuts. The placement splits the error (the onset is 0.065 s late). His face is small
  in this shot, so it may read fine. If it doesn't, the fix is a voice take with a longer "I'm" (e.g. a Sample Context
  that leans on it), not another clip. Omni came in at ×1.22–1.33 against the voice in every take whatever the prompt
  said ("slowly", "drawing out every word", "choked up").

## How the takes were picked

1. Measured each voice by loudness: 6-0 has three phrases (0.62 / 1.28 / 0.90 s, with 0.7 s and 1.5 s pauses), 7-0 is one
   unbroken 4.67 s run, 7-2 is 0.30 / 0.97 / 1.83 s, Derek's lines are 1.55 s and 1.87 s.
2. Generated new talking clips from the same approved plates (`storyboard/SB07b.jpg` for Sandra, `SB07c.jpg` for Derek;
   Frames, Omni Flash, 16:9, count 1, one fresh Flow project per take). The prompt carries the exact line.
3. Screened every take, new and old, by its own-audio rhythm against the voice. Then I fitted each candidate on the
   12 fps tracked mouth (`mouth-track.py`). For each piece the fit searches onset and tempo (1.00–1.15) to best match the
   dub's loudness to the mouth gap across the whole clip. It counts voice over a shut mouth as a failure, and it splits
   pieces only at the voice's own pauses. Then I checked every b/p/m on the strip.
4. Built the dubs with `scripts/lipsync/place-dub.py` (one fade in and one fade out per piece, no others).

## Takes and credits

Omni 1.1 Flash 720p, house prices 10 credits (6 s) and 12 credits (8 s). The flow MCP does not read the balance, so
these are list prices.

| Line | Takes (`video/cut3-lip-raw/`) | Credits | Verdict |
| --- | --- | --- | --- |
| 7d-0 | `cut3-lip-7d-0-v3-t1…t7` (6 s) | 70 | t1 ×1.6 too fast; t2 stuttered ("I'm… I'm really sorry"); t4 said the line twice; t3/t5/t7 ×1.22–1.33; **t6 picked** (×1.28 raw, cleanest closures) |
| 7-0 | `cut3-lip-7-0-v3-t1…t4` (8 s) | 48 | all rushed "Five years underground" or paused after it; t4's whole-line fit overran the shut mouth by 0.7 s. Old L07-0-a kept |
| 7-2 | `cut3-lip-7-2-v3-t1` (6 s) | 10 | **picked**, ×1.05 one piece. (The old takes were *slower* than the voice, ×0.72–0.78) |
| 6-0 | `cut3-lip-6-0-v3-t1…t3` (8 s) | 36 | **t1 picked**; t2's middle phrase too short; t3 put a 2.5 s pause after "Derek" |
| 7d-1 | `cut3-lip-7d-1-v3-t1, t2` (6 s) | 20 | t1 as good as the old take, but its tail is later; t2 held its mouth open 0.7 s before "Sandra". Old L07d-1-a kept |
| **Total** | 17 takes | **184** | + possibly 10 for one call that harvested an old tile (an "unusual activity" retry; the stray file was deleted; whether it billed is unknown) |

Every take has its recipe card beside it, written by the flow MCP and mirrored in `docs/provenance/cards/…`. So do the
v3 copies, the muted twins, the dubs, the preview and the strip. The same-prompt hook flagged "the camera does not move"
and the line's own words as habit phrases and near copies. That was deliberate for re-rolls of the same shot. I changed
the camera wording after the first takes.

## Switching cut3.py to v3 (not done)

1. `lipinfo()`: prefer `-v3` over `-v2` (the name `V3` is taken by the voice3 path, so don't call the flag that):
   ```python
   if D4 and (LIP / f'cut3-lip-{name}-v3-phrases.json').exists():
       name = f'{name}-v3'
   elif D4 and (LIP / f'cut3-lip-{name}-v2-phrases.json').exists():
       name = f'{name}-v2'
   ```
2. The `rows` list in the beat 6–7 block (the 4th field is the clip): `'6-0'` → `'6-0-v3'`, `'7d-0'` → `'7d-0-v3'`,
   `'7-2'` → `'7-2-v3'`; `'7-0'` and `'7d-1'` stay. The `-muted.mp4` twins exist for all three.
3. Row timing changes (same total, 20.2 s): 6-0 runs 5.46 s (was 4.29; the new clip's "Again" comes after the voice's
   real pause), 7d-0 1.96 (from 2.00 s into the clip), 7-0 4.94, 7d-1 3.74, 7-2 4.13 (was 5.33).
