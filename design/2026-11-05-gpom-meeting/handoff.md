# GPOM rework: handoff (updated 6 Nov, after the night session)

Read this, then `decisions.md` (every ruling, numbered) before doing anything.

## Where it stands
- **Maddie's hologram is done and in the film.**
  - Page and editor: https://claude.ai/artifact/G4Pm2tMnkxBQeKcdSpid9j. Source: `lookdev/index.html`.
  - Film renders: `D:\badcode-videos\clips\gitpush-origin-master\hologram\render-1k-24\` (24 fps; this is what the cut uses) and `render-1k\` (25 fps).
- **Scene A (kill bots) is at round 19.**
  - Timeline page: https://claude.ai/artifact/Jjvd8FPvF4KJUnVDQLYzkQ. Premiere: `03 GPOM story A kill bots r17`, in sync. Length 3:06.
  - Built by `scripts/gpom/second-half-video/cut3.py A --tag d17`.
  - Running order:
    - the street;
    - the bridge line "He made me learn a little presentation. In case any of you ever came back. Go on, then. Gather round." (by Kai);
    - fade to black, the hologram, fade up;
    - "Patrol's out";
    - hard cut to the toilet-seat row (natural speed, lips re-fitted with `voice-row-fit.py`);
    - one bot past Maddie;
    - the call ending on "simulations again";
    - the wide approach, a 3 s stand-down (no HUD), "That was close."
  - Not frozen yet: `final.json` is still round 14.
- **Kai rulings tonight:**
  - no camera swoop into the hologram, plain fades only;
  - the red KILL MODE and green STAND DOWN screens appear only later, on the bunker TV evidence (scene B);
  - the boss lines were re-recorded in Suno (`audio/boss-r18/`), and "No, thank you. I will handle it." is cut;
  - lip sync must be right; spend Flow credits if needed.
- **Open on scene A:**
  - Derek's "I'm really sorry, love" (7d-0) is the tightest lip fit. The fix if Kai still sees it: a cutaway to Sandra.
  - Kai's r11 hand edit (Git Push Origin Master.mp3 on A1, 0–10.17 s) needs its audio fade added by hand on r17.
  - "00 RENDER story" still nests r11. Swap in the current round once Kai signs off.
- **Voices:** `GEMINI_API_KEY` in `.env` is now a billed key (project webkit-servers, Gemini API only, no budget alert, by Kai's choice). The free key is kept as `GEMINI_API_KEY_FREE`.
- **Website:** the Storyverse (the hologram, viewing only) is Stories 9 at badcode.tv/storyverse.
  - Built by `apps/site/storyverse.mjs` from `lookdev/index.html`.
  - Not deployed; the website-ops session deploys.
- **Flow gotcha:** an "Introducing Omni 1.2" dialog keeps covering Flow, and the tools then time out on "Add media menu". To clear it, scroll the dialog to the end and press Get started (the scratchpad `dismiss.mjs` did this). Building it into flow-mcp is owed.

## Next, in order
1. Kai's notes on scene A round 19, then freeze it and swap it into the RENDER master.
2. Bunker (scene B): the kill bot blown up; "watch this, I'll come back tomorrow"; the TV plays the last seconds of the hologram plus the red/green HUD as evidence; Sandra wants out; the old lady calls a vote. The hands go up one by one, Derek last.
3. Ending: gravity, "it'll feel like dying, but you'll end up back".
4. Choruses: chorus 1 = poverty and displacement; chorus 2 = Last of Us implied violence (the Swindon bombs stay); the red army and the Sauron eye are cut.
5. Overview board as one film; the gitpushoriginmaster.com site later.

## Rules that bite
- Never say "superposition" or "two places at once". Say "not decided yet", never "decided but unseen".
- Consciousness choosing is the story's belief ("we're idealists"), not physics.
- The still gate: Kai approves stills before video credits; re-rolls of approved shots are fine.
- Public blurbs are setup only.
