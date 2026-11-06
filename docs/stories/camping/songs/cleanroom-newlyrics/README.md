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
