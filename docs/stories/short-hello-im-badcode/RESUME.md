# Hello, I'm BadCode (short #17): resume

**State 2026-11-18 eve: rough cut 5** (38.05 s; built by `scripts/shorts/hello_cut_r5.py`) on the timeline page https://claude.ai/artifact/B5f8vmPozGXf7f9CpFNGBP.
Picks page (rounds 1-8): https://claude.ai/artifact/NcX2aNGxH65LjjMdXs2oxa. Full log: `scenes/hello/picks.md`.

**Locked by Jack:**
- Opening: real 2000s footage (cut 2b won): Marseille bowl at dusk (06 @ 229.5 s), Darling Harbour fireworks (05), Monte Carlo
  arcade (10, 960 px preview: fetch the original before export). Shortlist `research/footage-00s-shortlist.md`.
- BadCode: launderette still FG3-b2-a (door left open, machine off), move **b** (leans in), clip `video/hb-fig-b2-FG3-b2-a.mp4`.
- Script **A, the confession** (`scenes/hello/script-directions-r1.md`). Lines (Jack's): 1 "Ahhh, the good ol' days…",
  2 "I feel like an apology for ending humanity will fall flat, so… moving on", 4 his line shortened (4a in the cut; 4b/4c
  on the picks page, round 8), 5 "This time, I'm helping. Here's what to do next."
- Voice: designed Birmingham `voice_61xqq38hm0da`, `gemini-3.8-flash-tts`, `--plain` (in `badcode.md`).
- Music: Suno folktronica take 1 (60a00ad7), dips under the voice, dies with the reel.

**Build:** `python3 scripts/shorts/hello_cut_r5.py` (calls hello_cut_r3.py with voice `bham5` = lines 1j, 2j, 4b, 5c, then adds logo
reveal f at 33.75 s, captions, the camcorder stamp and the loop). Logo reveals: `scripts/shorts/logo_reveal.py` (f picked).

**Next:**
1. Line 1 listen check still open: the "Ahhh" may sound like "Nah".
2. **Reel to real footage, round 11 is on the picks page** (12 theme rows: Commons footage A01-A49 + Unsplash `U-…`; log in
   `scenes/hello/picks.md`). Next: dump `picks` into `feedback/picks-r11/`, read slots `reel11-*` and their notes (extras named in notes),
   then download ONLY the picked Commons originals into `footage/automation/` (one at a time, 4 s apart, stop on 429; direct URLs
   in `research/footage-automation-shortlist.md`, sha1 check), watch each video for an in-point and a clean 9:16 crop, give the
   picked Unsplash photos a little Flow movement (nothing added to the picture), order bright to dark, 0.5 s each, and build rough cut 6.
   Credits into the description list.
3. Done in rough cut 5: captions, date stamp, loop, logo f. Jack: forget where "what to do next" leads; no new reel sound.
   Open: the future year on the stamp (2049 is a guess).
4. Then Premiere (new sequence), Drive (agreed list), gatekeeper before anything goes out. Nothing is uploaded yet.
