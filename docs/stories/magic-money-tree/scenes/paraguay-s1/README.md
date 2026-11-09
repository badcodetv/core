# Paraguay short 1 — "Sir, Quick Question" (v1 built 2026-11-09)

Jack: *"please just make a version of it, then afterwards i will punch up the jokes … the humour should be south park
like research that. Please clean room it all"*. Format: `../../money-for-something-2026-11-09-paraguay-mockumentary.md`.

**Premiere:** `Paraguay.prproj`, sequence **`Paraguay short1 Sir Quick Question v1`** (720x1280, 25 fps, 20.5 s), bin
`short1 Sir Quick Question`. No render (Jack watches the timeline). Media: Desktop `Paraguay\short1\`.

| Time | V1 picture | Over it | Voice-over (A2, Charon) |
| - | - | - | - |
| 0.0-6.0 | REAL: @Raulbogarin clip 5-11 s (crowd shoving Payo Cubas out, "¡Fuera!") | streamer box (V2), summary "THEIR BANK WENT BUST. THEN A POLITICIAN SHOWED UP." (0.3-5.2), credit, species meme flash 5.2-6.0 | "Three million savers. Bank's gone. So a politician turned up to help." |
| 6.0-14.0 | REMADE: suit (face pixelated) crowd-surfed away, presenter with mic, then stops | "FACE PIXELATED FOR LEGAL REASONS" (6-10), PENSIONER_PLAN.EXE flash (10-10.8), "4 DAYS: BANK SEIZED -> PRESIDENT REMOVED" (11-14) | 6.4 "Sir. What's the plan for the pensioners?" · 10.8 "He came to listen. They are not fucking having it." |
| 14.0-14.8 | meme "OUT OF OFFICE" | | (vo3 runs on) |
| 14.8-20.5 | END: presenter at desk holds up a card | "BANK OWNER. BANK INSPECTOR. PICK ONE." | 16.1 "Simple fix. The ref can't own the team." |
Logo bug (V6) throughout. Ambience levels: real -8 dB, scrum -10 dB, desk -6 dB.

**How it was made (clean room):** fresh web research (`cleanroom/research-comedy.md`, `research-engine.md`), three
sealed script writers (pundit / straight man / own engine), a judge (`judge.md` → `script-final.json`), a sealed
prompt writer (`prompts.json`), stills run verbatim (`run_stills.mts`, presenter pick attached), Omni Flash clips
9:16 8 s, voice via AI Studio TTS (REST; the google-genai SDK path 400s on speechConfig as of today), layers built by
`scripts/paraguay/s1_assets.py`.

**Known faults / open:**
- The real clip is amber (fair dealing; Jack + Kai decide). Credit is on screen.
- `scrum-nod` (the slow grateful nod) dropped: Omni painted eyes on the hood when he turned to camera, twice
  (`video/scrum-nod*.mp4`). The carry clip's back half covers the beat.
- Flow drew a British street, not Asunción.
- Voice: Charon, unpicked by Jack; presenter voice still EMPTY in sound.md.
- No music bed yet (Kai's format has a 10-15 s track).
- Sign text "I'M HERE TO LISTEN" from the script not added (the sign moves).
