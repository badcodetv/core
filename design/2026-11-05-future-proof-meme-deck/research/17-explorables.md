# 17 - Explorables: interaction patterns and 3D metaphors for the three pillars

Searches used: 6 of 8. Solidity: P = primary, S = secondary, H = hearsay. No primary page text was fetched (small-ideas.org returned only its title); everything below is S unless marked.

## What the references actually teach

| Source | Finding | Solidity |
| --- | --- | --- |
| Nicky Case, *To Build a Better Ballot* (2016, open source, ncase.me/ballot) | A simulator shows how First Past the Post glitches and that the usual fix (instant runoff) is "better but rife with problems"; has a sandbox to argue with others. https://datastori.es/103-explorable-explanations-with-nicky-case/ , https://www.metafilter.com/163918/To-Build-A-Better-Ballot | S |
| Case/Vi Hart, *Parable of the Polygons* (2014) | Text interleaved with mini-games. Added an anti-bias rule to Schelling's model, so it shows reversal and not just the problem. Aimed to explain systemic bias without telling readers they are bad. https://en.wikipedia.org/wiki/Parable_of_the_Polygons , https://gamedeveloper.com/design/using-systems-to-explain-systemic-problems-in-i-parable-of-the-polygons-i- | S |
| Case, *Evolution of Trust* (2017) | A story hook (WWI Christmas truce) then a game-theory sandbox. Critique: it explains the system but does not build a skill. https://datastori.es/103-explorable-explanations-with-nicky-case/ , https://stefy.substack.com/i/140164241/why-is-it-effective-for-learning | S |
| Case, "4 More Design Patterns" (2018) | Four patterns: puzzle, bet, roleplay, sandbox. Seen only via a Chinese-language summary. https://www.gcores.com/articles/155428 | H |
| Ciechanowski (cameras and lenses) | Builds a mental model step by step (photon bucket, pinhole, lens). You drag and rotate each element. Commenters, not him, describe it. https://statusq.org/archives/2022/06/28/ | S. Whether he uses WebGL was NOT confirmed. |
| The Pudding | Visual essays, few words, a data viz carries each point, transparent about sources. https://pudding.cool/about , https://www.storybench.org/?p=8613 | S/P |
| Distill, "Communicating with Interactive Articles" (2020) | Four affordances: connect people and data, make systems playful, prompt self-reflection, personalise the reading. Seen only via a lecture slide deck. https://dsc-courses.github.io/dsc106-sp24/resources/lectures/12-DSC106-Narrative.pdf | H |
| Small Ideas Initiative (Martin Lewis, with Nesta and Involve) | Cross-party panel crowdsources practical, low-cost, non-controversial ideas; panel picks about 50 to take to government, councils and regulators; submissions closed 12 Nov (year not stated, so check). Polly MacKenzie: "rebuilding confidence in the idea that government can sort stuff out". https://www.newsbeep.com/763093/ ; site https://small-ideas.org/ not read. | S |

## Patterns that fit 60 seconds
1. Hook as a question, not a lecture (Case, Pudding). The reader answers before we explain.
2. One variable, one slider/drag per slide. Ciechanowski-style: add one element at a time.
3. Show the problem, then the fix on the same toy (Polygons' anti-bias rule). Do not end on doom.
4. "Bet" pattern: ask the viewer to predict, then reveal. Works as a talk-to-camera beat ("hands up").
5. Sandbox last, one per pillar, for the website only. In video, Kai drives it.
6. Gap to avoid (Evolution of Trust critique): end each pillar with a thing the viewer can do or say, not only a model.
7. Safe for the reader (the-reader.md): blame the design (the 1800s ballot), never the voter; name decision-makers, not the tech.

## Pillar 1 - Composition over inheritance (vote per issue, not per bundle)
60-second interaction: viewer ticks 5 issues; a party "block" forces all 5 to the same colour. Then the block explodes into bricks and they pick each.

3D metaphors (three.js):
1. **Monolith vs Lego.** A party is one solid slab with 12 policies carved in. You can only take the slab. Drag to crack it; bricks fall apart, you build your own tower. Bricks colour-coded by issue.
2. **Meal deal / set menu.** A rotating table: set menu (starter + main + pudding fixed, you hate the pudding) versus plates you pick. Fits a UK reader; the joke writes itself. Use as a meme anchor.
3. **Inheritance tree vs plug-in board.** A deep tree where a child inherits every branch it never chose (cables tangle), versus a socket board where each issue is its own plug. Small Ideas becomes the first plug: a visible small-idea brick snapping onto the policy tower.

## Pillar 2 - Continuous integration (governance that ships and tests small changes)
60-second interaction: slider for "how often we change the law". Rare = one giant release that breaks (tower topples); frequent = tiny changes, each run through a test gate, bad ones rolled back.

3D metaphors:
1. **Conveyor and test gate.** Small crates (policies) ride a belt through a green/red gate into the "live country". A red crate drops back off with a revert arm. Contrast: once per five years, one container crushes the belt.
2. **Bridge built plank by plank vs dropped from a crane.** Each plank is load-tested; a cracked plank is swapped without closing the road. The big-bang bridge falls into the river.
3. **Merge train / pipeline tube.** Glowing commits flow down a transparent tube of stages (draft, pilot, review, live). Viewer clicks "revert" and the whole flow visibly runs backward, which no real law can do today.

## Pillar 3 - Data-driven decisions (no proposal without its experiment)
60-second interaction (bet pattern): viewer predicts whether a policy works, then a split town (pilot v control) reveals the real result. Most guesses wrong, which is the point and keeps it humble, not smug.

3D metaphors:
1. **Two identical towns, one pilot.** Side-by-side diorama; one gets the policy, other does not; a bar chart grows from each. The camera orbits to the evidence.
2. **Lab bench for laws.** Each proposal sits in a petri dish with a label "hypothesis". The dish has to grow a result before the lever to "enact" unlocks (locked lever is the visual).
3. **Dashboard cockpit vs steering by vibes.** A car on a road: the "vibes" version has a blindfolded driver; the data version has a live gauge cluster (cost, outcomes, who benefits). Light and meme friendly.

## Build notes
- A slideshow that has one tiny three.js canvas per slide is realistic; only the sandbox slides need real simulation. Keep scenes low-poly, pre-baked, under 60 s each.
- Meme layer goes on the slide, 3D goes in the middle: the meme lands the joke, the toy shows the mechanism.
- Look is the story's call (Future Proof look.md), not a BadCode default. These metaphors are neutral on style.
- Verify before claiming: the Small Ideas details (deadline year, partners, panel) are from one press article; confirm on small-ideas.org before it appears on a slide. Also do not imply Martin Lewis endorses Future Proof.
