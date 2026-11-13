# Priority Lane: picks and rulings

- **2026-11-10, Jack:** the look is the rainy-night film photo (`reference/look-ref-rainy-night-traffic.png`); "never do flow speech", voices via AI Studio + lip-sync-dub.
- **2026-11-10, Jack, dialogue round 1** (page https://claude.ai/artifact/KrWqm7FgqmCqheDDQbGgw1): notes on draft 1A. Minister: "I said raspberry- shaped Hors-d'œuvres!" Button: "politician blocking the path of an ambulance, poetic really..." Put in as draft 1D; not yet picked.
- **2026-11-10, stills round 1 (clean room):** all 12 made (Jack said carry on after a pause); voting page https://claude.ai/artifact/MeDp9CuYEEMhUQt9mtYxNa
- **2026-11-10, Jack, stills round 1:** This on OUT1-c (long lens through the motorcade), AMB1-a (from the back of the ambulance), REP1-a (reporter piece to camera), MIN1-b (lemon curd on the armrest). Every shot has a pick; storyboard written (5 frames, dialogue 1D placed as a draft).
- **2026-11-10, Jack:** "1d is cool". Dialogue locked as 1D; written to `script.json`.
- **2026-11-10, Jack, animation picks:** 1a (motorcade slides through), 2b (only the light changes), 3a (reporter to camera), 4a (minister says the line, muted and lip-synced to the AI Studio voice), 5a (ambulance pulls away behind the reporter).
- **2026-11-10:** clips 01, 02, 04 made and checked (pass). Reporter clips 03 and 05 (still REP1-a) never generated: 3 submissions with the first prompts, 2 more with reworded ones. Likely a silent block on the still itself (balaclava + police + ambulance). Logged in docs/google-flow/omni-flash.md.
- **2026-11-11, Jack: "just try again".** Re-ran 03-r2 and 05-r2 unchanged. **03-r2 generated** (`pl-03-r2-REP1-a.mp4`, 8.0s, 720x1280) and passes: the reporter and mask are steady, with no morph. The ambulance moves off behind him at about 4-5s, so the clip's second half already plays beat 5. **05-r2 failed twice in about 14s** (still silently blocked). Proposal: cut 03-r2 into two pieces for 3 and 5.
- **2026-11-11, Jack: "make it as simple as possible".** 05-r2 refused twice more. **05-r3 (bare prompt: "The man stands still holding the microphone. Behind him, the yellow van drives away. Rain falls.") generated on the 2nd submit** → `pl-05-r3-REP1-a.mp4`, 8.0s, passes (reporter steady, ambulance pulls off into the distance). match.py misnamed it 05-r2 (same still); renamed and recipe card prompt corrected by hand. Lesson: the long wording was the block, not the still. All five clips now exist.
- **2026-11-11, Jack: "put the voices in a skill that I can pick from".** New skill `voice-casting`. Round 1: 4 reporter and 4 minister AI Studio takes (profiles in `voices/profiles/`), on the voice picks page https://claude.ai/artifact/BpkaAfAwZ6gS4k5TarNWtm. Awaiting picks.
- **2026-11-11, Jack, voice casting round 1** (dump: `feedback/voices-r1/`): **Minister = b** (Orus, slick media-trained minister, low venomous hiss; `voices/profiles/min-b-orus.md`). Reporter: no pick, "do more of these, do a range of London men voices please." Round 2 = five London men (`voices/profiles/rep2-*`).
- **2026-11-11, Jack, voice casting round 2** (dump: `feedback/voices-r2/`): **Reporter = e** (Enceladus, Croydon courts reporter, breathy, off the record). Both voices are now cast.
- **2026-11-11, minister lip-sync (lip-sync-dub):** clip 04 already says the exact line. Mouth speaks 0.67-3.42 s, while Jack's Orus take speaks 3.47 s. 3 brisker re-voices: take 1 fitted at x1.20 but turned "hors d'oeuvres" into "or doves", so it was dropped. Final: **Jack's own take, whole, x1.26, at 0.68 s** (voice onset 0.71, 0.04 s after the mouth opens). The raspberry p/b closure lands on 1.50-1.58 s and "shaped" on 2.33 s. All words transcribe. → `video/pl-04-MIN1-b-dub.mp4` (+ `audio/dub/` stems). Not yet watched by Jack.
- **2026-11-11, Jack: "put it all on the timeline".** Rough cut 1: 21.9 s, shots 01 (3.0) · 02 (2.5) · 03 + reporter line 1 (6.15) · 04 lip-synced minister (3.7) · 05 + the button (6.5). The sfx are each clip's own Omni ambience, levelled to -30 LUFS. Timeline page https://claude.ai/artifact/GThYPTmuJ6DorNBmaL2Swn. QC passes (1 warn: loudness -20 LUFS, fine for a rough).
- **2026-11-11, Jack, timeline round 1 notes** (dump: `feedback/timeline-r1/`): the ambulance changes direction in 3 and 5 ("clean room it all and research the internet"); headlines meme-style at the end; a BadCode overlay. **Round 2:** clean room (`cleanroom/research-r2-clips.md`, `brief-r2.md`, two sealed writers) → 03-cr2A (ambulance parked, passes) and 05-cr2A (drives away; starts at 1.2 s to hide the turn), and 03-cr2B / 05-cr2B were refused. Five verbatim headlines (`research/news-stories.md`) via `scripts/shorts/priority_lane_cards.mjs`; logo bug top left. Page round 2 republished; replies on the page.
- **2026-11-11, Jack: "search for a UK one, I've seen one on Instagram but they deleted the post".** Found: Deadline News, 6 May 2024, Baker Street / Marylebone Road (London). Police motorcade stops an ambulance on blue lights; VIP not named; second UK outlet emergency-services.news. Added as the LAST headline card (lands on top, holds). Headline from search listing = URL slug; the page was not opened (403, and the browser was blocked), so Jack should confirm it before release. Details in research/news-stories.md.
- **2026-11-11, Jack: "its done".** Frozen and built into Premiere: `shorts-1-priority-lane-r2` in `priority lane.prproj`.

## 2026-11-13: round 3 opened (Kai's meeting notes)

- **Jack:** ending = flatline into the logo; sound = "suno for it all, but add background music as well that fits the scene"; dialogue script before the Suno tracks; ambulance stills with his Unsplash ambulance-interior photo as inspiration (`reference/jack-ambulance-interior.png`).
- **Dialogue page** https://claude.ai/artifact/QgbHdwSjBNJRJsx2Q9CNcc: ten writers, three drafts (1A The quiet stop, 1B The countdown, 1C We can see it), awaiting Jack's pick.
- **Mood board round 3** https://claude.ai/artifact/Ga9dkygvkQ9sL4g4hLga4V: 12 clean-room stills (LS3, HD3, WS3, FL3 a/b/c), sealed writers, run verbatim. The reference was described, not attached: `flow_generate_image` has no reference input, and the only route that takes one (`flow_edit_image`) is the edit path we avoid. fresh.py flagged each prompt as identical to its own clean-room file (expected) and the shared brief wording ("plain dark-green uniform", "UK ambulance"); kept verbatim, as the clean room requires.
- **Seen on the stills:** the paramedics' uniforms carry a crest badge and, on LS3-a/LS3-b, a small "UK" tab despite "no badges"; fix on the picked one. The minister in WS3-a/b/c is a new face, not round 1's MIN1-b; if WS3 is picked, the minister clip must match it (or we re-pick).
- **Dialogue picked (Jack, 2026-11-13): 1B The countdown**, no notes. In `script.json` (round 1's in `script-r1.json`).

## 2026-11-13: round 3 votes read, round 4 made

- **B. Held: HD3-b** (Jack, This). **C. The motorcade: the round 1 minister NOW-MIN1-b** (Jack, This), so the existing clip `pl-04-MIN1-b` and its lip-sync stay; the windscreen shots are out.
- **A. Losing him: LS3-b** Maybe, and **D. Flatline: FL3-a** Maybe. Jack: "we need to match the consistancy of the van and setting with the other clips, but use this camera angle, the back of the image should be facing the drivers seat so we can see out the window."
- **Round 4** (same board, same link): remade with `flow_edit_image` using references. The prompts are mine, short reference-fix prompts and not clean-room ones. LS4 = LS3-b for the angle + HD3-b for the cab and windscreen; **LS4-a** has no badge and is the van anchor (LS4-b still has the crest). FL4 = FL3-a for the angle + LS4-a for the van; **FL4-a** reads best (flat line, open hatch, red light through the windscreen).

## 2026-11-13: every beat picked (round 4)

- **A. Losing him: LS4-b** (Jack, This), with the crest badge, "UK" tab and shoulder lettering removed by a one-line edit → **LS4-b-fix-a** (fix-b in `_rejected/`).
- **B. Held: HD3-b** · **C. The motorcade: NOW-MIN1-b** (round 1 clip `pl-04-MIN1-b`, lip-synced) · **D. Flatline: FL4-a**.
- The same paramedic isn't at the monitor in A and D (a woman in LS4-b, a man in FL4-a); Jack picked them as they are.
- Next: storyboard + animation options (scene-animation), and the Suno track for dialogue 1B.

## 2026-11-13: media folder tidied (Jack: "get rid of all the old stuff in the priority lane folder, and only keep the new stuff")

Moved, not deleted (`tidy-media-folders` ruling):
- Round 1–2 media went to `_old-r1-r2/`: `cut/`, `frames/`, `audio/casting`, the reporter, outside and ambulance clips, overlay cards 0–5, the round 1 stills, `moodboard/current/`.
- Unpicked round 3–4 stills went to `moodboard/_unpicked/`.

Left in view:
- the four picks (`LS4-b-fix-a`, `HD3-b`, `MIN1-b`, `FL4-a`)
- the minister clips (`pl-04-MIN1-b*.mp4`)
- the logo lockup and `reference/jack-ambulance-interior.png`
- `priority lane.prproj` (and `_1`); `audio/` is empty, ready for Jack's screen-recorded Suno take.

🔴 The old `shorts-1-priority-lane-r2` sequence in `priority lane.prproj` now has offline media (it will ask to relink). Everything it used is in `_old-r1-r2/` if it's ever wanted again.

- **2026-11-13, Jack:** "there are gloves floating on the device in his mouth": LS4-b-fix-a's bag-valve mask was held by hands with no body. Redone as a fresh generation from LS4-b-fix-a as the reference (not a change-only edit): **LS5-a/b/c**, each with the second paramedic visible and his arms attached. On the mood board, round 5.
