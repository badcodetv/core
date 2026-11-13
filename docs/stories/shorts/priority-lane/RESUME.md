# Priority Lane: resume here

**2026-11-13 (night, last): clips made; media folder tidied.** Jack's new project is `priotity lane.prproj` (empty). Round 1-2 material (`_old-r1-r2/`, old Auto-Save, the Orus dub) DELETED at Jack's request; unpicked stills/voices in `_` folders. Clips: `pl-r3-A-LS5-b` ✅, `pl-r3-B-HD3-b` ✅, `pl-04-MIN1-b-charon` (re-synced to Charon, voice on 0.94 vs mouth ~0.88) ✅, `pl-r3-D2-FL4-a` 🟡 (r3-D refused 3 times; D2 is a bare prompt: the screen is flat for ~2.5 s, then shows a live trace again, so use 0-2.5 s or re-roll). Next: music + SFX (Suno, variations), then the timeline page, then Premiere.

**2026-11-13 (late night): ALL VOICES PICKED; storyboard round 3 awaiting Jack's animation picks** https://claude.ai/artifact/6xd6NLu5rKzecZR7kLzZ9V
- Voices (sound.md): Kore / Algieba / Alnilam / minister Charon. Cut, levelled, one file per line in Desktop `priority-lane\audio\voices\` (`c1-minister-glass.wav` is the muffled version). The transcriber hears Kore's "60 over 30" as "60, I refer": check by ear.
- Animation options in `animation-options.json` (round 1 copies kept as `*-r1.json`): A she shouts / eyes on monitor; B the glove holds / headlights cross; C keep pl-04, re-sync to Charon (lip-sync-dub); D the light turns green / he sits back.
- Next: dump the storyboard picks, write `video-jobs.json`, run the clips (Omni 1.2 Flash, 9:16, Frames), re-sync pl-04 to Charon, then music + SFX in Suno (variations), then the timeline page.

**2026-11-13 (night, later): crew PICKED (Kore / Algieba / Alnilam, in sound.md); round 4 = the minister recast the same way, awaiting Jack's pick** on the same page. NOTE: the Gemini key is paid (since 2026-09-30), so there is no 10-a-day cap.

**Earlier: voice casting round 3, the crew in AI Studio** on https://claude.ai/artifact/BpkaAfAwZ6gS4k5TarNWtm (same voices page, round 3).
- Method: the Bank Robbery recipe (a director's note of three lines, `Accent:` / `Style:` / `Pace:`, under 60 words, light everyday accent, talking to someone and not performing) via the new `--note` flag on `scripts/aistudio-tts.py`. Three sealed web-researching writers, one per role: brief, JSON and notes in `voices/r6-cleanroom/`.
- Takes in Desktop `priority-lane\audio\casting-r6\` (9 of today's 10 free API calls used). Paramedic 1 is cast as the woman, paramedic 2 as the man (as in LS4-b); the minister stays Orus.
- Word check: all lines present; "twen—" comes out as "twenty" (the flatline cuts it); Gacrux ad-libs "He'll be alright" at the end (trim).
- Next: dump the `picks` db into `feedback/`, write the picks into `sound.md`, then clean the voices, then music + SFX in Suno.

**2026-11-13 (late): r5 Speech voices REJECTED** (Jack: "all of those sounded the same and weird"). Research saved in [`docs/suno-gpt/speech-beta.md`](../../../suno-gpt/speech-beta.md): Speech is a narration-over-music tool with one voice control (Male/Female), no saved voice and a weak British accent, so it is the wrong tool for four distinct character voices. Next: Jack decides between AI Studio voices cast on a picks page (`voice-casting`) and one last Speech round on the research's settings.

**2026-11-13 (latest): round 3, every beat picked; voices waiting on Jack's ear.**
- **Picks:**
  - A. Losing him = `LS4-b-fix-a` (badge removed)
  - B. Held = `HD3-b`
  - C. The motorcade = round 1 minister, `MIN1-b` (clip `pl-04-MIN1-b` + lip-sync)
  - D. Flatline = `FL4-a`

  All on the board https://claude.ai/artifact/Ga9dkygvkQ9sL4g4hLga4V.
- **Dialogue:** 1B The countdown (`script.json`).
- **Sound:**
  - Suno song rounds r3 and r4 are in `songs/r3-suno`, `songs/r4-suno`. Jack: r3 sounded American, and the crew and minister sounded the same.
  - Jack then switched to **Suno Speech, voice only**, with music and SFX added after: **r5** in `songs/r5-speech/takes.md`, 4 roles × 3 voices × 2 takes, driven by `scripts/suno/speech.mjs`.
- **Next:**
  1. Jack picks one voice per role and screen-records them into Desktop `priority-lane\audio\`.
  2. Clean the voices: de-reverb, and muffle the minister through glass.
  3. Make the music and SFX separately (Suno instrumental / Sounds).
  4. Animate the four stills to the audio (Omni, 9:16; the paramedics are masked, so no lip-sync).
  5. Build the timeline page, then Premiere.
- **Waiting on Jack:** open `priority lane.prproj` with the BadCode Bridge panel on, so the old sequences can be deleted (he asked 2026-11-13). The media folder was tidied: old material is in `_old-r1-r2/`, unpicked stills in `moodboard/_unpicked/`.


**2026-11-13: REOPENED, round 3.** Kai's meeting notes: no reporter; ER drama in the ambulance; held at the lights; the minister crosses; **flatline into the logo** (Jack's pick). Sound: **Suno for it all plus background music** (Jack). Beats agreed: [`brief.md`](./brief.md), `scene.json` round 3. Next: the Suno track (script → Suno → pictures), then clean-room stills for the new ambulance shots. Round 1 below is the old cut.

**2026-11-11:** ALL FIVE CLIPS MADE. 03 = `pl-03-r2-REP1-a.mp4`, 05 = `pl-05-r3-REP1-a.mp4` (the bare prompt got through). Voices PICKED on https://claude.ai/artifact/BpkaAfAwZ6gS4k5TarNWtm (skill `voice-casting`): minister = Orus `voices/profiles/min-b-orus.md`, reporter = Enceladus `voices/profiles/rep2-e-enceladus.md`; takes in Desktop `audio/casting/`. Minister lip-synced: `video/pl-04-MIN1-b-dub.mp4` (unwatched by Jack). **Rough cut 1 BUILT** (21.9 s, `scripts/shorts/priority_lane_cut.py` → Desktop `cut/`), timeline page https://claude.ai/artifact/GThYPTmuJ6DorNBmaL2Swn, **DONE 2026-11-11 (Jack: "its done").** Frozen (`final.json`). In Premiere: `shorts-1-priority-lane-r2` in Desktop `priority-lane\priority lane.prproj` (V1 clips, V2 headline/logo overlay, A1-A3). ⬜ Before release: confirm the Deadline News headline in a browser; export from Premiere and run the delivery QC. The reporter needs no sync (his mouth is cloth).

**State, 2026-11-10 evening (Jack):**

- **Dialogue 1D LOCKED** (`script.json`): Reporter: "Traffic is being managed, to keep an important journey moving." · Minister: "I said raspberry-shaped hors d'oeuvres!" · Reporter: "A politician blocking the path of an ambulance. Poetic, really..."
- **Stills picked:** OUT1-c, AMB1-a, REP1-a, MIN1-b (mood board https://claude.ai/artifact/MeDp9CuYEEMhUQt9mtYxNa).
- **Animation picks:** 1a, 2b, 3a, 4a, 5a (storyboard https://claude.ai/artifact/RJ5FcwAW7NsDRfFiDPkq9j).
- **Clips made and checked:** `pl-01-OUT1-c.mp4`, `pl-02-AMB1-a.mp4`, `pl-04-MIN1-b.mp4` in Desktop `Youtube Vids\animation\shorts\priority-lane\video\`. Flow project `57538600-142a-45b8-ac4c-e79e663de0c6`.
- 🔴 **Reporter clips 03 and 05 never generate** (5 tries, two prompts): likely a silent block on the still REP1-a (balaclava + police + ambulance). Logged in `docs/google-flow/omni-flash.md`.


Rules for this short: no Flow speech (voices are AI Studio + lip-sync), vertical 9:16, Omni 1.2 Flash, Nano Banana 2 for stills, clean-room prompts.
