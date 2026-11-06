# Camping: new lyrics over the released drum & bass instrumental (Jack, 2026-11-06)

Jack: "is there anyway of making the drum and bass version we already have "camping.mpeg" but changing nothing but the
lyrics in suno. basically the same song with the updated lyrics ... keep the last camping balaclava 1, as a just in case ...
the new workspace in suno is called "Camping-Jack_new" ... Please clean room it all and research the internet."

- **New lyrics** = `lyrics.txt` (the r81+ reggae-round words, identical to the camping.md canon; 60 lines vs the released 48:
  new hook "I can't live like this forever" ×3, new lines in all three verses).
- **Research** (web only): `research.md`. No Suno route guarantees the beat; Add Vocals (now "Edit vocals" on the Audio card's
  mode menu) is the closest; mixing new vocals over the original instrumental ourselves is the guaranteed fallback.
- **Instrumental**: htdemucs_ft two-stem split of camping.mpeg (venv `~/.cache/badcode-venvs/demucs`, GPU, 4 s).
  `<Desktop>\Youtube Vids\animation\songs\camping vid\new-lyrics\stems\` (instrumental mp3/wav + old vocals).
  Original map (s): intro 0–24.6 · A (Bob) 24.6–72 · drop 72–90.5 · B (Tarquin) 90.5–137.5 · drop 137.5–155.5 · C (both) 155.5–202 · outro 202–215.3.
- **Boxes**: three sealed writers (`brief-w1..3.md` → `w1..3.md`), each with an angle; words verified unchanged; fresh.py clean.
- **Run** (2026-11-06 ~12:15): instrumental uploaded to Camping-Jack_new (Jack agreed to Suno's upload terms himself), mode
  "Edit vocals", `scripts/suno/add-vocals.mts <wN.md> "Camping new lyrics wN" --yes` (fills, reads back, creates). v6, Audio
  Influence 90, Personalize off. Takes (all 3:34–3:35):
  - w1: ee53ed3d-7614-49b4-8ca4-cdaaac015f35 · 543df54b-91d2-48ea-9379-01b9e46b4eb2
  - w2: 17d79f91-3d72-48c5-be00-17a8c96c0f12 · 504f0c26-53de-4ad6-ad4c-b7cdb3c6733d
  - w3: 1e3f9b27-e90b-42d7-8f67-e49375323cd0 · 5d115457-12eb-490e-8137-96c332b5f76d
  - instrumental upload: 64cd9043-7982-4066-ab85-3d306e83afad

## ▶ RESUME HERE — takes made, not yet measured

1. Record each take (`npx tsx scripts/suno/suno.mts record <id>` — the player, no download; the stream itself is encrypted,
   do not try to decode it). Blocked 2026-11-06: WSLg audio wedged (private PulseAudio works), then the automation Chrome
   stopped loading any page at all (even example.com, even a fresh profile; curl fine). Suspect: the WSL clock being stepped
   backwards every 1–2 min (journald "Time jumped backwards"). Fix = `wsl --shutdown` from Windows, then flow_status.
2. `~/.cache/badcode-venvs/demucs/bin/python compare.py <stems/camping-instrumental.wav> <take.wav>...` — beat correlation
   per 10 s window (the original vs itself: median 0.81, lag 0) and vocal share per section.
3. Keep the take whose beat holds and whose verses sit in A/B/C with hooks over the drops; if the beat drifted, take only its
   vocal stem and lay it over the ORIGINAL instrumental (route 2), then a Premiere copy of `camping balaclava 1` with the new song.

## Measured 2026-11-06 pm (all six recorded; `compare.py` now aligns a global offset ±5 s and uses Pearson per window)

| take | offset | beat corr (median) | lag across the song | verdict |
| --- | --- | --- | --- | --- |
| w1 ee53ed3d | +1.88 s | 0.40 | steady, −12…+12 ms | **only take on the original grid**; vocals spill into the outro |
| w1 543df54b | −2.81 s | 0.17 | wanders ±400 ms | beat not the original |
| w2 17d79f91 | +3.07 s | 0.20 | wanders ±400 ms | beat not the original |
| w2 504f0c26 | +3.23 s | 0.20 | wanders ±400 ms | beat not the original |
| w3 1e3f9b27 | −3.58 s | 0.11 | wanders ±500 ms | beat not the original |
| w3 5d115457 | −3.70 s | 0.16 | wanders ±460 ms | beat not the original |

Measured, not yet heard. Next: Jack listens to w1 ee53ed3d; if the vocal is right, lay its vocal stem
(`suno-recordings/sep/htdemucs_ft/camping-new-lyrics-w1-ee53ed3d/vocals.wav`, trim 1.88 s) over the ORIGINAL instrumental.

## Pace round (2026-11-06 pm) — Jack: "the pacing is wrong, he raps much faster ... gravelly voice that blends between lines ... too many pauses"

- Measured (word timings): original 2.8–3.2 words/s, about one word per beat at 174; new lyrics have the same word count per verse.
  Cause found: the w1–w3 style boxes asked for a "relaxed half-time" flow, and web research says Suno puts DnB vocals at half-time by default.
- Web research `research-pace.md`; sealed writers `pace/brief-w4..w6.md` → `pace/w4..w6.md` (run-on lines / flow words / gravelly voice),
  words verified unchanged, Variety 0, Audio Influence 80. `scripts/suno/add-vocals.mts` now also sets Variety.
- Takes: w4 79092b77, 7104a718 · w5 1eed654b, 8384df75 · w6 23366ea1, 5e1e78fc. Recorded.
- Result: pace on paper 3.0–3.9 words/s (w6 5e1e78fc closest to the original with the fewest gaps; w4 79092b77 at 3.9 may be too fast).
  🔴 None keeps the original beat (whole-song match 0.2–0.6 vs w1 ee53ed3d 0.83). Likely cause: Audio Influence 80 (w1 kept it at 90).
  Note: by the numbers w1 ee53ed3d was already ~3.0 words/s, so the "slow" Jack hears is feel (half-time lilt), not word count — listen.
- `compare.py` fixed twice: global offset search ±5 s (both directions) and Pearson per window.

## Same-song round (2026-11-06 evening) — Jack: "The songs are too far from the original, please fix it along with the voice."

- Found: camping.mpeg IS a Suno song — "Camping V5 Good" (binocarlos, 15 Jun 2026), id 03e29295-d33a-4db7-b566-64a58e83a196
  (the file's own metadata). Its Styles + Lyrics boxes saved in `original-boxes.txt`; earlier rounds never had them.
  The song's menu offers Edit ▸ Replace Section Pro, Open in Studio, Get Stems, Extend, Crop, Remaster.
- Web research `research-same-song.md`: best route = Suno Studio, original's stems, regenerate ONLY the vocal lane per verse
  (instrumental never regenerated); then Replace Section per verse; Persona/Voices weak for this.
- This round (cheap route first): sealed writers `same/brief-w7/w8` given the original's own boxes; w7 = minimal change (Audio Influence 92),
  w8 = original voice + pace (AI 95). Takes: w7 91c9c412 971281b6 042de056 dba594b7 · w8 a2017b66 18aa2e44 53de5ff0 19c9f86a.
- Measured: w7 all lost the beat. w8 19c9f86a "kept" it only because it is nearly instrumental (82 words) — reject.
  **w8 18aa2e44 = best so far**: beat close (whole-song 0.61, the old on-beat take was 0.83), 428 words, 2.8 words/s, few gaps (original 3.1).
- 🔴 Gemini (listen) is NOT a judge here: it scored the rejected w1 take 10/10 identical to the original on voice, pace and beat. Jack's ears only.
- A/B clips (original verse A then the take): `suno-recordings/ab-<take>.wav`.
