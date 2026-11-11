# Sponsor a Chancellor: resume here (2026-11-11, afternoon)

**Done**
- Project `short-sponsor-a-chancellor`: Drive `Shorts/Sponsor a Chancellor`, Jack's folder Desktop `Youtube Vids\animation\shorts\sponsor-a-chancellor`, 9:16, BUILDING on the slate.
- **Script LOCKED** (`scenes/sponsor-a-chancellor/script.json`, draft 1D on https://claude.ai/artifact/YcJX759MtLbfgzSpxiJeKM): NARRATOR "This is Crispin. / Crispin only earns £100,000 a year. / Tonight, his second home has no second home. For just £3 a month, you can help." Then the pull back into her freezing flat, the junk mail, NAN "Poor bastard..." (Jack's words). The median card and "Or keep your £3" were cut by Jack.
- 🔴 **Name open:** "Crispin" clashes with a real ex-MP (Crispin Blunt); Jack still has to pick a name. Check it before final voicing.
- Stills round 1 (clean room: `cleanroom/research-r1.md`, `brief-r1.md`, four sealed writers) on the mood board https://claude.ai/artifact/2zJhS2qQjLwYE89GkNBvx9. **Jack's picks:** AP1-b (Crispin, rainy conservatory glass), RM1-b (nan in her front room with the TV), PO1-b (doormat with the flyer from above), NA1-a (nan close-up, reading glasses, bobble hat). Votes dumped in `feedback/moodboard-r1/`.
- Flow project `2ab052be-f268-47d0-8b8d-cdf772b864af`. **Flow Characters made** (Jack: "try and make the character look the same"): `SAC Chancellor` (portrait = face crop of AP1-b) and `SAC Nan` (portrait = face crop of NA1-a); no Body view (it did not attach). Staged refs in `~/.cache/badcode-scenes/sponsor-a-chancellor/cast/`.
- **Re-shoots with the cast** (picked prompts verbatim, minus the cast person's description): `moodboard/RM2-b-a.jpg`, `RM2-b-b.jpg` (SAC Nan), `PO2-b-a.jpg`, `PO2-b-b.jpg` (SAC Chancellor on the flyer). ⬜ NOT YET CHECKED by eye or shown to Jack.

**Running / next**
1. Voice casting (Jack: "make a voice page where I can pick the voices"): 8 takes rendering into `audio/casting/` (narrator a-d: Sulafat, Charon, Achernar, Algieba; nan a-d: Gacrux, Vindemiatrix, Autonoe, Laomedeia; profiles in `scenes/sponsor-a-chancellor/voices/profiles/`). Next: check the lengths, card them (`prov.py card`), mp3 them, write `voices/picks.json`, build with `scripts/scene/build-picks.py`, publish with db+user (the `voice-casting` skill).
2. Check the four re-shoots against AP1-b / NA1-a (contact sheet + face crops). Then a picks page or mood board round 2 for Jack.
3. Then the storyboard → scene-animation (Omni 1.2 Flash, Frames, 9:16) → scene-timeline.

Rules: clean room for prompts; never describe a cast character; no Flow speech (AI Studio voices, lip-sync with lip-sync-dub); Nano Banana 2; prompts end with "Thanks."

## 2026-11-11 pm: voice page up, re-shoots checked

- **Voice page round 1:** https://claude.ai/artifact/5BfuXWgH1xGGy3Xbi1iqNT (built from `scenes/sponsor-a-chancellor/voices/picks.json`, collection `picks`). Narrators a–d are word-perfect (17–22 s, no gap over 2 s). Nan a ("Foo bastard") and d ("Oh, bastard") may have swallowed "poor" by whisper's read; flagged on the page. Next: dump `picks` into `feedback/`, write the picks into `sound.md`.
- **Re-shoots checked** (contact sheet against AP1-b and NA1-a): PO2-b-b holds the chancellor's face on the leaflet best (sharp, headline readable); PO2-b-a holds too. RM2-b-a holds the nan (bobble hat, same build); RM2-b-b drops the hat and turns her away. Suggested: PO2-b-b and RM2-b-a, Jack to confirm.
- **Voices picked (Jack):** narrator c Achernar (Belfast), nan b Vindemiatrix (Geordie). In `sound.md`. Name ruled: Crispin stays (Jack). The Achernar casting take is the narration master; no re-render needed.
- **Storyboard r1:** https://claude.ai/artifact/Dvts2zVZWMYrZLbZuPo12g (pick a still + animation option per frame). Motion prompts are written clean-room after the picks.
- **Rough cut 1 / timeline page:** https://claude.ai/artifact/5zYArB8zS3cQxAZVYvKCHE (26.2 s). Cut script `scripts/shorts/sponsor_chancellor_cut.py`. Next: Jack's notes.
- **In Premiere:** `shorts-6-sponsor-a-chancellor-r5` (sponsor-a-chancellor.prproj). Left: Jack to call it done (freeze), export, delivery QC, check the ITV headline in a browser, lip sync of "-stard" (LatentSync offered).

- **2026-11-11 eve:** round 5 is in Premiere as `shorts-6-sponsor-a-chancellor-r5` (sponsor-a-chancellor.prproj). Left: Jack's "it's done" (freeze), export, delivery QC, open the ITV headline once in a browser.
