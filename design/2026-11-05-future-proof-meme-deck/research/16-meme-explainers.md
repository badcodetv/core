# 16 - Craft of meme-driven explainer talks and videos

Evidence warning: 4 web searches run (budget 8, shared). They returned thin material on craft. Most rules below are **craft judgement (own knowledge, unsourced)** and are tagged as such. Treat them as a guide, not a gate. Nothing here sets a look for BadCode; the deck's look belongs to Future Proof.

## What the web actually confirmed
| Claim | Source | Solidity |
|---|---|---|
| CGP Grey's FPTP video ("Politics in the Animal Kingdom", 9 Mar 2011) explains the system through ONE running fictional animal election, and builds to the spoiler effect; 2.3M+ views in 5 years | https://markpack.org.uk/19439/animals-explain-the-problem-with-first-past-the-post/ , https://rosetta.to/u/cgpgrey/the-mathematically-superior-voting-system (index) | secondary |
| Nothing found analysing its pacing or why it works (the pacing notes below are from watching/knowledge, not a source) | search result gap | n/a |
| PowerPoint karaoke: slides auto-advance every 15-20s; presenter has never seen the deck; no skipping/going back; audience picks the winner | https://en.wikipedia.org/wiki/PowerPoint_karaoke , https://plusai.com/blog/powerpoint-karaoke , https://scottberkun.com/2012/what-i-learned-from-powerpoint-karaoke/ | secondary |
| Pecha Kucha 20x20 (20 slides x 20s = 6m40s) | NOT confirmed by search; my own knowledge | unsourced, well known |
| Jump cuts remove dead air, speed pacing, can sharpen a punchline; Ze Frank is cited as an early pioneer of the vlog jump-cut style | https://rosetta.to/u/foldingideas/why-the-jump-cut-is-here-to-stay , https://metafilter.com/127364/Were-all-done-off , https://fiveable.me/television-studies/key-terms/jump-cut | secondary / hearsay |
| Last Week Tonight: ~8-week story cycle, pitch -> research/vetting -> structure -> jokes; commercial-free so one topic can run long; Oliver calls it "the slowest improv you've ever seen" | https://www.npr.org/transcripts/1204297928 (quote); shortform.com summaries (cycle) | quote primary-ish (NPR); cycle hearsay |
| Hank Green, Tom Scott, Ze Frank True Facts, Philosophy Tube, Kurzgesagt, TikTok carousels: nothing found | gap | n/a |

## Observed patterns by creator (from knowledge, not searched - verify by watching)
- **CGP Grey**: one concrete cast (animals) carries an abstract mechanism; the diagram IS the joke vehicle; one visual change per sentence; a rule is shown breaking on screen before it is named.
- **Last Week Tonight**: dull-sounding topic framed with a hook of stakes in the first minute; real footage as the "straight man", Oliver as the reaction; gags are visual (a graphic that undercuts the sentence) and recur as callbacks; ends on a ridiculous physical artefact.
- **Tom Scott**: deadpan, a single location, one fact per beat, joke delivered flat and left alone.
- **Ze Frank**: jump-cut density, narration over a still image that contradicts it; the voice is the comedian, the image just sits there.
- **Philosophy Tube / Kurzgesagt**: costume or character as framing device; Kurzgesagt uses cute visuals against grim content (matches BadCode's nurturing-under-snark).
- **TikTok carousels**: slide 1 is the hook and must stand alone; each swipe needs a reason; last slide is the payoff or the ask.

## Concrete rules (craft judgement)
1. **Slide = one idea, one image, <= 8 words.** If the speaker has to read it, the joke is dead. The words on screen are the caption; the voice is the joke.
2. **Image and words must disagree, or agree absurdly.** The laugh lives in the gap (deadpan "this is fine" caption on a plainly bad thing). Pure illustration of the sentence earns nothing.
3. **Setup on slide N, punchline on N+1, never both on one slide.** The click is the beat. Put the punchline image behind a click so the audience reads the setup first.
4. **Pause after the punchline slide, do not talk over it.** Hold 1.5-2.5s of silence (video: leave the cut alone; talk-to-camera: look at the audience).
5. **Pacing**: default 6-12s per slide spoken; punchline-only slides 2-4s; a "diagram that explains" slide earns 15-25s; a run of 5+ rapid 1-2s slides is a deliberate rhythm break, use it once or twice. Pecha-Kucha's fixed 20s is a cap on waffle, not a target. Target for the whole deck: 15-20 min talk = ~60-80 slides is fine if average is ~12s; a 4-6 min video cut = 25-35 slides.
6. **Run ONE extended metaphor all the way through** (CGP Grey's animals). For Future Proof the strongest candidate is the one the brief already has: the political system as a codebase. Every pillar gets one running object, not three unrelated jokes.
7. **Callbacks: plant early, pay off at least twice, escalate.** Plant a visual (the 1840s candle/quill) at slide 3, return it at the midpoint with a small twist, and use it as the closer. Three uses is a pattern; a fourth risks fatigue unless it subverts.
8. **Teach, then joke, never joke instead of teaching.** Sequence per pillar: relatable pain (why can't I vote for two things?) -> meme to say it out loud -> the mechanism in one clean diagram -> the obvious fix -> one punchline. If the audience cannot repeat the point afterwards, the memes failed.
9. **Meme choice**: use formats the reader already knows from their own feed (reaction faces, "distracted boyfriend" shaped structures, drake-style approve/reject, "expectation vs reality"), but keep to formats with 5+ years of life; new ones will date the deck by launch. Prefer our own drawn/generated images in a meme's grammar over lifted copyrighted templates (licence: check before publishing; do not use real people's faces in jokes against them).
10. **Aim jokes at the mistake and the decision-maker, never at the viewer** (the-reader.md: never "you've been duped"). Punch up at the 1800s system and at "the party bundle" - the menu where you must order the whole set meal.
11. **The 3D (three.js) slide is a reward, not wallpaper.** Use it only where a static image cannot show the mechanism (votes splitting into issue-by-issue strands; a pipeline that continuously merges). Max ~4 in a deck; each under 15s; one interaction or one camera move, not both.
12. **Hook in 10 seconds**: "The system we vote with was invented before electricity. Since then: the internet, AI. And we're still putting an X in a box." Open on the absurd contrast, not on the thesis.
13. **Escalation order**: easy laugh first (earns trust), clearest pillar next, hardest pillar last but with the best visual. End on a callback plus the small practical thing (e.g. small-ideas.org as the real-world version).
14. **Talk-to-camera layer**: slides are the cut-aways, Kai is the straight man; slide changes land on sentence ends; allow at least one slide where Kai says nothing; keep one "off-script" beat per section for the voice (sarcasm with total authority, nurturing underneath).
15. **Test before shipping (PowerPoint-night method)**: run the deck on 3 people who have not seen it. Mark every slide where nobody laughed or nodded; cut or rewrite it. Also the karaoke test: could a stranger present it cold from the slides alone? If not, the slides are carrying too little.
16. **Carousel/short cut-down**: the deck should export as a 7-10 slide TikTok/Instagram carousel: slide 1 = hook standalone, slides 2-8 = one pillar each with its meme, last = payoff + link. Design every master slide to survive a vertical crop.
17. **Fail states to avoid**: explaining the joke on the slide; a meme with no argument; more than one metaphor live at a time; text-heavy "meme" slides; a callback with no setup; a 3D scene where the camera moves for its own sake.

## Skill implications (for the meme-slideshow skill)
- Skill should take a canon doc + a reader and output: (a) the one running metaphor, (b) per-idea beat sheet (pain / meme / mechanism / fix / punchline), (c) a callback ledger (plant, payoffs), (d) pacing table (seconds per slide, total), (e) a cold-read test with 3 people.
- Skill should not carry a look; it asks the story's look.md (or story-style) before any image.
- Sources and the craft rules above are the starting guide; open question to resolve in a later pass with more searches: Tom Scott, Hank Green, TikTok carousel hook data (unresearched here).
