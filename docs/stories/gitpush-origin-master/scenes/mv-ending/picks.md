# Music-video ending — picks

## 2026-11-02 (Kai)

- Last image: orbit. *"orbit with red armies… we could see the same satellite that we started with, just that the Earth is clearly now occupied by the robots."*
- Time of day: night.
- Beats approved as drafted (all four: out of Swindon, the land, the sky, orbit). One eye only. Go on the mood board.

## 2026-11-02 — mood board round 1 published

- 41 kept stills (20 prompts × 2, Nano Banana Pro, refs from opening-recut + chorus 2 + the opening satellite), board https://claude.ai/artifact/1iiPuJNHfcEYFWpcnCon9e, Flow project ecb26938-c035-4f88-937a-987cf1d13f26.
- Rejected (in moodboard/rejected/): LD1-b-a, SK1-c-a, OR1-e-a (Flow echoed the reference), SK1-c-b (duplicate of SW1-e-a). SK1-c re-run without refs as SK1-c2 (robots read as people in hoodies).
- Same-prompt check flagged the shared closing line (deliberate: the round's agreed suffix) and two habit phrases; kept.

## 2026-11-02 · Mood board round 1 votes (feedback/moodboard-r1/)

Kai: "I've picked a bunch there. These are great images… I think that there's a kind of… missing scale, which is sort of somewhere in between the world scale and then the field scale… come up with another bunch of ideas, add to that board the choices I've already made, please use to inform any ideas you might have for further shots."

This (12): SW1-a-b, SW1-c-a, SW1-e-b · LD1-b-c, LD1-c-b, LD1-d-a, LD1-e-b · SK1-a-a, SK1-b-b, SK1-d-a · OR1-a-b, OR1-c-a. (SW1-a-a was clicked then cleared.) No notes.
→ Round 2: new beat "The country (middle scale)" at ~202s, between the sky and orbit; picks shown first on the board.
- Round 2 published (same link): "Picked so far" strip at the top; new beat "The country (middle scale)" with 9 ideas / 17 stills (CT2-a…i). CT2-f-b lost to a Flow pop-up. Same-prompt check flagged only the shared closing line again; kept on purpose.
- Kai: "remove things that were not picked in the first round… keep things I've picked at the top and show me only options that are genuinely new". Board now: picks strip + round-2 stills only (scene.json board_round=2; old rows stay in moodboard.json).

## 2026-11-03 · Mood board round 2 votes (feedback/moodboard-r2/)

This (5): CT2-a-a, CT2-b-b, CT2-d-b, CT2-e-a, CT2-h-a. No notes.
Kai: "with everything I've selected, it feels like we'd have enough footage for the rest of the music video." → 17 picks total; mood board done.

## 2026-11-03 · Storyboard

Kai: close-ups — "we do have a couple of those with the traffic lights… let's just use what we have." Orbit: "add a couple of additional clips… for the last 20 seconds… we could be zooming out… we don't really have a whole Earth in red… a much wider zoom out to finish on."
→ Made OR3-a (whole red Earth + satellite), OR3-b (red Earth from past the Moon), OR3-c (ring of ships round the planet). Storyboard: 20 frames, 40 options, published https://claude.ai/artifact/9Ui1ATN8KdGCjep3ctWgPQ

## 2026-11-03 · Storyboard picks (feedback/storyboard-r1/)

Animation: 1b, 2a, 3b, 4b, 5a, 6a, 7a, 8a, 9a, 10a, 11a, 12a, 13a, 14a, 15a, 16a, 17a, 18a, 20b (moonrise reveal ends it).
Frame 19 cut. Kai: "it looks too much like Saturn… number 18 is enough and then we skip to 20. So I think we just skip this one entirely."
Frame 18: no still picked; using OR3-a-a (first shown).
Kai: "This is coming together good. I think we've got something pretty decent here."
→ video-jobs.json: 19 clips (frames 1–18 and 20), Omni 1.1 Flash, 16:9, 8s. Awaiting go on video credits.

## 2026-11-03 · Clips round 1

Kai: "please proceed." 19 clips made (Omni 1.1 Flash, 16:9, 8s; 19 video generations), all in D:\badcode-videos\gitpush-origin-master\clips\mv-ending\video\. QC flags: 6 (white building flickers in, use first 4s), 13 (beam already firing), 15 (redraws into Britain-from-orbit by 5s), 16 (satellite morphs after 5s), 17 (gold appears instead of red; satellite tumbles: re-roll candidate), 20 (near-still, no real moonrise). Clips page: https://claude.ai/artifact/ALp4AEZcFa114WJE5A71HZ

## 2026-11-03 · Clip picks (feedback/clips-r1/)

Keep (14): 01, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 14, 15, 16. Not picked: 02, 13, 17, 18, 20.
Kai on 01: "I like this about two seconds in onwards where we just start off with smoke and then the robots emerge from the smoke. So we can use this exact clip, just edit the first two seconds away."

## 2026-11-03 · Orbit re-roll

Kai: "re-roll the orbit shots… a couple of variations with each… genuinely different approaches to the cinematography… It's fine to spend credits."
→ 9 clips, 3 approaches per shot (video-jobs.json extra):
- 17 Europe: v1 locked, last gold lights go red · v2 time-lapse, planet turns beneath a fixed satellite · v3 camera circles the satellite (parallax)
- 18 whole Earth: v1 satellite panel wipes across the lens · v2 fast pull-back · v3 sunrise starburst over the edge
- 20 last image: v1 pull back off the Moon · v2 rack focus from Moon dust to Earth · v3 locked hold, the last gold light turns red
Written by me, not a variations round (guide departure: 9 clips with distinct camera grammar, set by hand; same-prompt check run).
- Orbit re-roll done (9 generations). QC: all three variants of a shot share a still, so the first-frame matcher cannot tell them apart; the file names (v1/v2/v3) may not match the prompt on their recipe cards. Page labels describe what each clip actually shows. Seen: 17 all morph the satellite (v3 steadiest); 18-v1 = lens wipe + fast pull-back to a tiny red Earth (the standout), 18-v2/v3 = sunrise starburst; 20 all near-static (Veo ignored the moves).

## 2026-11-04: clips page shows what is new
- Kai: "I can't tell the ones that I've already looked at and decided to not choose versus ones that I've not seen yet."
- build-picks.py gained rounds: picks.json `round: 2`, orbit-17/18/20 `round: 2` → tagged New, listed first with jump links; round-1 clips fold into a closed panel, each tagged "Picked: …" or "Not picked". Same link, version 3.

## 2026-11-04: clips round 2 read, round 3 made
- Keeps confirmed: 01, 03–12, 14–16 (01 trimmed of its first 2s, Kai's note).
- 17: none picked. Kai: "the satellite itself shouldn't be rotating… we should see the earth move underneath it." → 17-r2 (Veo told to hold the satellite: it does, Earth turns beneath, red fades ~4s); 17-p1/p2/p3 on a clean plate OR4-plate-a (satellite removed) for a still satellite laid on in post. Diff-mask cut-out failed (Nano Banana redrew the roads); a green-screen cut-out is still owed if a plate take wins.
- 18: v1 picked. Kai: "two satellites appear and that throws us… recut… just with one satellite." → 18-r2a…e. r2d (a duplicate take) is the v1 move with the SAME satellite wiping the lens; a small satellite shows again from ~3s.
- 20: none picked. Kai: "doesn't look like Earth… generic red splodge." → new stills OR4-a-a/a-b (edit of OR3-b-a with the 18-v1 Earth as reference) and OR4-b-a/b-b (Earthrise, half daylit, half red). Still gate: animate only Kai's pick.
- Runner fix: run.mts downloads failed (ENOENT in /tmp/playwright-artifacts) because Chrome on channel 2 can't see this sandbox's /tmp; run with TMPDIR=$HOME/.cache/pw-tmp. Duplicates from the stuck run became 17-p3, 18-r2d, 18-r2e (cards written by prov.py card; their exact prompt is one of the same-still siblings).

## 2026-11-04: clips round 3 picks
- 17 → **r2** (me-17-r2-OR1-a-b: satellite holds, Earth turns beneath; cut ~4s). No composite needed.
- 18 → **r2e** (me-18-r2e-OR3-a-a: one satellite, pull-back).
- 20 → still **OR4-a-b**; animating three moves: 20-r3a locked Earth turning, 20-r3b crane-up Earthrise, 20-r3c slow push-in.
- 20 animated: 6 takes (r3a–c named by matcher, r3d–f from dupes). Content: a/b/c push-ins, d crane-up with the Moon sinking, e slow turn, f near-still. Suggested: reverse a push-in in Premiere for a pull-away finish.

## 2026-11-04: clips round 4 pick — clip list LOCKED
- 20 → **r3d** (me-20-r3d-OR4-a-b: camera rises, the Moon sinks out, Earth alone in black). No note.
- Locked running order, 17 clips (02 and 13 dropped), copied in order to `clips/mv-ending/locked/NN-<file>.mp4` with their recipe cards:
  01 me-01-SW1-a-b (trim first 2s, Kai) · 03 SW1-c-a · 04 LD1-d-a · 05 LD1-c-b · 06 LD1-b-c · 07 LD1-e-b · 08 SK1-b-b · 09 SK1-d-a · 10 SK1-a-a · 11 CT2-h-a · 12 CT2-d-b · 14 CT2-a-a · 15 CT2-b-b · 16 OR1-c-a · 17 me-17-r2-OR1-a-b (cut ~4s) · 18 me-18-r2e-OR3-a-a · 20 me-20-r3d-OR4-a-b
- Next: Kai cuts in Premiere (162–230.5s); then scene-timeline / overview board when asked.

## 2026-11-04: timeline round 1 (rough cut 1)
- Kai: "use the timeline skill to come up with that sequence now"; the ending also wants its own Premiere sequence alongside the story, so both versions (start + MV end, start + story end) live in one project.
- Cut by `scripts/gpom/mv-ending/cut1.py`: page 0 = film 157.96 (4s of e07 as the lead-in); cuts snapped to detected beats; blocks follow the loudness dips (~171, ~191–194, ~209–214, drop ~214.6, stop ~230). Country shots cut fast (~1.9s) as the scale climbs, then orbit enters on the dip.
- Page: https://claude.ai/artifact/Web2Ja1DTnmYpYzBad5iZL. Premiere sequence not built yet (gpom-mv-ending-rough1 is a placeholder name).

## 2026-11-04: in Premiere
- Kai on rough cut 1: "No changes. That's excellent. Let's cut that in Premiere… as a new sequence in the currently open Premiere project."
- Took the Premiere bridge from another session (Kai's go). Built **gpom-1b-mv-ending-r1**: the ending alone (0 = film 161.96, so it follows the opening as the music-video version), V1 = 17 locked clips with handles, A1 = the main track from track time 168.96 to its end. Check: in sync (17/17).
- Kai: "only the current sequences that we know are active" → closed all 33 tabs, reopened six in film order: 1-track-and-off-switch, 1b-mv-ending-r1, 2-A-killbots-r9, 4-C-walkout-r2, 5-D-crossing-r1, 6-E-ending-r2 (B is page-only right now). Active tab: 1b. New sequence filed in "00 the film (live sequences)". Saved.
