# Chorus clip bank — the picks page

**https://claude.ai/artifact/KDw9dRfPJCvdsZs9TXK4C5** — every chorus-world clip (55, round 1), grouped by beat, with
This / Maybe / No picks (db `picks`, one doc per clip per person: `<clip>__<uid>`) and a notes box (db `notes`).

**This is the clip bank for all three GPOM choruses**, not just chorus 2 (Kai, 20 Oct: *"there's enough content in
this page to do all three choruses with"*). Chorus 2 picks come first; choruses 1 and 3 draw from the same page later.

Rebuild: `template.html` + `data.json` (clip list, beats, verdicts from `../video-qc.md`) → replace `/*DATA*/null`
with the JSON → publish with `files` = the silent 640px previews in
`D:\badcode-videos\gitpush-origin-master\clips\chorus-2\preview\` mounted as `v/<name>.mp4`.
Full-quality clips: `D:\badcode-videos\gitpush-origin-master\clips\chorus-2\video\`.
