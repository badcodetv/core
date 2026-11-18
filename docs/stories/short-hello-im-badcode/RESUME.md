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
1. Read round 8 + timeline notes (line 4 pick; anything on rough cut 4; listen: line 1's "Ahhh" may sound like "Nah").
2. Replace the reel's flat AI stills with REAL automation footage (Jack: "boring and flat… could be raw footage"). A find-footage
   search ran on 2026-11-18. Wikimedia blocked its downloads (429 "too many requests"), so Jack said skip the wait: the agent
   wrote `research/footage-automation-shortlist.md` (50 Commons candidates, links + licences, best per theme, ambers, rejects; nothing downloaded). Its thumbnail sheets + API metadata: `<media>/reference/footage-automation-thumbs/`. Next: put the shortlist (previews/links)
   + the 50 Unsplash photos (`reference/unsplash/`) on the picks page, flag brands and faces, Jack picks, then download ONLY
   the picks into `footage/automation/` (slowly: Wikimedia rate-limits) and build rough cut 6. If the shortlist is
   missing, rerun the search but stop at links. Credits into the description list.
3. Done in rough cut 5: captions, date stamp, loop, logo f. Jack: forget where "what to do next" leads; no new reel sound.
   Open: the future year on the stamp (2049 is a guess).
4. Then Premiere (new sequence), Drive (agreed list), gatekeeper before anything goes out. Nothing is uploaded yet.
