# GPOM meeting: decisions (Kai, 5 Nov 2026)

Kai answered the six questions on the proposal page (https://claude.ai/artifact/7fhyLWHuvPJsJpNaGrT38u).
Nothing has been built yet. Hologram first.

## Decided

1. **The hologram is direction B, the Commit Graph**, with A's rule (gold light comes only from people) and C's deadpan captions.
   - Kai: "We've lost touch entirely with Git in this entire story and yet it's the clearest way of explaining to humans what's going on."
   - The argument it must make: only consciousness experiences the world and chooses its story through it. Humans' decisions are commits. We went down a branch of commits we regret. Only consciousness can revert it.
   - The multiverse is a story-verse, not infinitely everywhere: the question is which branch you chose to merge.
   - Line fix: "He can draft a billion branches. He can't commit one. **Only your consciousness can.**"
   - Keep the Rick and Morty and Doctor Strange jokes inside it. The point: the multiverse makes people feel unimportant; the AI worked out that they matter, so don't fear the AI.
   - The cost: the time machine needs your consciousness to drive it. It is not "you're dying"; you'll appear before everything went wrong.
2. **The three.js scene is the real thing, not a prototype.** It is how the hologram is animated (recorded to video for Premiere) and also a page we publish, on **gitpushoriginmaster.com** (domain already owned), and later the start of the Storyverse explanation.
3. **Length:** whatever it takes to fit the jokes and the "you matter" point (no fixed 60 s cap).
4. **Ending: significant, not dark.** Add gravity and jeopardy: the humans have just sacrificed themselves (in theory they didn't die, but they went through something hard), so the boss's "don't make me come back twice" lands. This rules out "it'll feel like dying, because it is."
5. **Choruses: the "no humans, never a hit" rule is reversed, and the red robot army and Sauron's eye are cut.** Don't catastrophise too early; document the downfall at the right pace.
   - **Chorus 1** (half length; the first half is the zoom into the monitor). It sits between the sackings and the banks being taken over: **poverty, mass displacement, economic disaster**. Dramatic, not violent.
   - **Chorus 2:** **Last of Us style implied violence**. Real-world footage, no humans visibly suffering. Bombs dropping on Swindon stay exactly where they are. It must read as "there are no humans left", so verse 3's autonomous battle hits harder.
6. **Order of work: the hologram first.**

Also agreed: faster speech as proposed (punctuation + `[fast]` at source, `atempo` as a fallback); the four-beat kill-bot cut; in the bunker the hands go up one by one with Derek last.

## Round 2 (Kai, 5 Nov)

7. **The cost is held back.** In the hologram Maddie says only that the time machine needs a consciousness to drive it. Later, near the ending: "it'll feel like dying, but you'll end up back." Walk the line: not a doom film, but give weight to what the humans go through.
8. **Code lives in its own folder** (`apps/gpom-site`), deployed to gitpushoriginmaster.com.
9. **Film mode first.** Cut the film version; tweak the explore-the-website version afterwards. Build the look with the front-end design skill: "what it looks like will be everything."
10. This reverses part of draft 1I's ruling (3 Nov: "without the time machine, a surprise that develops later"). The time machine now closes the hologram (Jack's point). The Storyverse name still stays out.

## Hologram look (Kai, 5 Nov)

11. **Look A, the jeweller's bench**: amber glass with an ember inside, on brass wire, on black. Lookdev page: https://claude.ai/artifact/G4Pm2tMnkxBQeKcdSpid9j (`lookdev/index.html`).
12. Round 1 notes: beads too big, too close together, too bright. Loves the river and the move from the first bead into the river. The first bead is seen along the line as it rises away to the top right (his screenshot). The revert arc only appears once we fly down the river. All applied in round 2.

## Round 2 notes → round 3 (Kai, 5 Nov)

13. Thinner links, white string. Blue glass (the gold ember stays inside: gold is still only people). The projector flicker isn't working; try a range of screen filters (round 3 has six).
14. **The story is told as decisions, forward in time.** Start on nothing; a commit arrives, then the next, as Maddie narrates. Then the fan of possible next choices (about 20% opacity): that's where the multiverse is talked about, and "the cat's not decided yet" rather than "alive and dead". One is chosen and becomes the next bead. Then the river (everybody at once), then the revert.
15. Physics check (Kai asked): "not decided yet" is already Storyverse doctrine (`docs/stories/storyverse/doctrine.md` §1, "undecided, not two places at once"; Relational QM, QBism). Two guard rails: say undetermined, never "decided but we haven't looked" (Bell rules that out); and in physics anything that interacts settles it, so a conscious chooser is the story's wager, not a physics claim. Keep the fan about people's choices, not about looking at particles.
16. The new beat order needs line changes to draft 1J (lines 4–9). The round-3 subtitles are a rough draft for timing, not yet approved.

## Round 3 notes → round 4 (Kai, 5 Nov)

17. **CRT telly is the filter.**
18. Labels are plain text above the dot, not tags. Three choices only, rising in weight: a banal one, an emotional one, a big life one (round 4: "toast, not cereal", "said sorry first", "got married"). "git push origin master" is not a choice and is gone from the beads.
19. The cloud of maybes: far more of them, much bigger, each one much smaller (they're choices, not commits yet). Round 4 offers three styles to compare: a cloud, a dandelion clock, forking branches.
20. Loves the chosen one joining the string. The move from the choices to the river is good but too quick (now 4.5 s). River strands further apart, the whole thing much wider.
21. A slider bench for the commit itself (glass colour, see-through, frosting, metal, bead size, ember size/glow/colour, string thickness/colour, spacing, maybe count/size/spread/opacity, river width/strands); "Copy settings" hands the numbers to Claude.

## Round 4 settings → round 5 (Kai, 5 Nov)

22. Kai's bench settings are the defaults: {"tint":"#3f7bff","glass":0.63,"rough":0.06,"metal":0.22,"bead":0.68,"ember":0.3,"emberBright":7,"emberColor":"#27b070","threadColor":"#d1d1d1","spacing":0.46,"width":10.4,"strands":280,"fanStyle":"cloud","fanCount":3750,"fanSize":0.49,"fanSpread":1.35,"fanOpacity":0.11}. Choices style: the cloud.
23. The string must be about a fifth as thick: now a fixed-pixel hairline drawn after the focus blur (1.6 px at 1080p). Labels sit higher above the dot.
24. OPEN: Kai's ember colour is green (#27b070). The river's people-beads are still gold, and "gold is only people" was agreed on 5 Nov. Needs a ruling: green ember everywhere, or back to gold.

## Round 5 notes → round 6 (Kai, 5 Nov)

25. The introduction (decisions arriving → the maybes → the chosen one → the river) is visually right. Colours stay as they are: green ember in blue glass on your string, the river contrasting (warm). Item 24 resolved: keep. The river's people colour is now a bench knob.
26. The river's shape was odd: now a smooth, wide ribbon that meanders gently and narrows into the far past.
27. "He's been adding beads for five years and not one is gold" was weak: it implied the future carries on being committed without people, which drags in wave-function collapse. Claude's proposal, built in round 6: after you went, **the strings carry on bare** (time passes, nobody commits, no beads), and past the end **his drafts flicker in and out, never landing** (the maybes from the choices beat, paying off "he can draft a billion, he can't commit one"). Lines (draft): "And since you lot went? Five years of string, and not one bead on it." / "He drafts all day, look. Billions of maybes. Not one of 'em lands." Tags: "days since last commit: 1,826", "drafts: 9,412,733,005  committed: 0". Awaiting Kai's verdict.

## Look locked (Kai, 5 Nov)

28. Kai loves the bare-string idea. Round-5 settings (locked): {"tint":"#3f7bff","glass":0.63,"rough":0.06,"metal":0.22,"bead":0.68,"ember":0.3,"emberBright":7,"emberColor":"#27b070","threadPx":1.6,"threadColor":"#d1d1d1","spacing":0.46,"width":13.7,"strands":390,"fanStyle":"cloud","fanCount":3750,"fanSize":0.49,"fanSpread":1.97,"fanOpacity":0.4,"riverColor":"#ffb347"}.
29. The revert arc was bent out of shape: now a clean half-ellipse (round 7). Look written into GPOM's look.md (Per part, "A · Maddie's hologram").

## The edit (Kai, 5 Nov)

30. Visuals done. Next is pace and words with the voice: Claude's recommendation taken, an editor on the lookdev page (picture blocks you stretch, Maddie's clips you drag, words you edit, saved to the page db `edits/current`) rather than recording now and cutting in Premiere. The saved edit becomes the timing the film version renders from.
31. Draft 1K written and voiced: `hologram-1K.md`, `voice-1k/`. Gemini free tier is 10 calls a day: 6 used today (5 takes + 1 re-voice).
32. Edit round 1 notes (Kai): "it really works". (a) The street → hologram → street transition: Kai's idea, the camera pushes into a tiny screen on Maddie's underside, it goes black, the hologram starts. Page now has a CRT switch-on at the start and a switch-off at the end ('Screen off' block) to cut against; the push-in shot on the street is still to make (Flow, still gate). (b) Clip ends were cut too hard: re-cut so each clip runs until the sound actually stops, plus a 0.25 s tail and a soft fade. (c) The maybes now twinkle like his drafts. (d) Subtitles are an editing aid only, with a switch; the film has none (YouTube captions). (e) The 'not decided yet' words on the cloud are gone. Word notes still to come.
33. Kai: c11 now says "...and you lot were writing it. A storyverse. So it really matters. And so did you." This reverses the 3 Nov hold on the Storyverse name (draft 1I), Kai's call. Re-voiced (take C11b); 7 of 10 Gemini calls used today.
34. The floating words stayed on screen after the telly switched off (they were laid over the page, not in the picture). They are now drawn into the frame under the CRT filter: they flicker, curve and switch off with it, and film mode records them.
35. The transition: a small screen on Maddie's underside (Kai). Next: stills of the push-in and pull-out for Kai's approval, then two Flow clips.
36. The three choices happen in one day, in order: 07:42 toast, not cereal; 11:34 said sorry first; 14:10 got married.
37. c10 "And that's just you." was rising at the end; Kai wants it matter-of-fact, falling. Two new takes; picked take b by measuring the pitch of "you" (old take rose 208->271 Hz, take a rose 174->296 Hz, take b falls 225->165 Hz). 9 of 10 Gemini calls used today.
38. Maddie's screen: a small round CRT-style screen on her underside (Kai).
39. The river comes alive (Kai's idea): from just after the pull-back (~0:55) to the bare string (~1:14), each of the 390 strands starts a random distance behind the cut-off and commits on its own clock, bead by bead, with three twinkling maybes just ahead of each tip turning gold as they land; by the bare string they have all caught up and line up at the cut-off. Individual people deciding; together, the storyverse.
40. Cut c13 (the drafts line); straight from "five years of string" to "And now we've worked all that out". The flickering drafts and their numbers stay on screen. c15 loses "Git revert, he calls it, the nerd" ("git" came out strange): spliced, no re-voice; now "So he's built a time machine. Back to just before it all went wrong." The words "git revert" stay on screen. Runtime about 1:43.
41. The river camera (Kai): after the wide view, push in among the strands and watch the decisions land all around, drifting forward with them; then pull out from above to see the clean cut-off; then down to the bare string and the arc. The commits finish 2 s before the bare string so the pull-out lands on a straight line.
