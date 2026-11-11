You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Kai, 2026-11-11: "The other thing to say is, I've just been thinking about this and I think we should recut some of the music. I think what would work much better would be a much more A-men jump-up break. At the moment, there's too many high-pitched synthesizers for it to just all of a sudden cut into. A mid-90s old-school A-men jungle would be perfect. I'd like to do a couple of iterations on the tune as well. Thank you."

"Just to be clear, I mean the second half of the tune. The nursery rhyme part is perfect right now."

## What happened in earlier rounds (facts)

- "the second half of the tune" = the instrumental drum and bass drop that cuts in after the hymn. "The nursery rhyme part" = the hymn: a whole 1980s primary school singing a four-line hymn, bored and flat, over a thumping out-of-tune upright piano. The hymn is KEPT and is not part of this round.
- The drop plays as its own audio track in the edit, under masked gang members going wild tearing up a huge stack of paper labelled THE RULES in a cold fluorescent council basement, climbing the shelves, then one holds out a blank page and a pen to camera. In Kai's edit it lands on a hard cut at about 15.8 s and runs about 11.4 s.
- Last round's picked take (round dnb-r1, Suno v6, weirdness 45, style influence 75) was made from this style box, verbatim: "1994 UK jungle instrumental, 165 BPM, drums already rolling at bar one with no intro: a frantic chopped and time-stretched Amen breakbeat, ghost snares, stuttering snare rolls, metallic Akai S950 sampler grain on the stretched hits. Rolling mono sine sub bass under the breaks, one stabbing hardcore rave chord punched in on the offbeats. Homemade bedroom-studio mix taped off a London pirate radio broadcast: cassette hiss, saturated and slightly crunchy, wobbly tape, warm distortion on the drums. Raw, rough, working-class, loopable, relentless."
- Kai on that take: "too many high-pitched synthesizers for it to just all of a sudden cut into"; wants "a much more A-men jump-up break", "a mid-90s old-school A-men jungle".
- The track must be INSTRUMENTAL (no vocals, no MC, no vocal chops), hit hard from the first beat (a drop, not a build) and work as a loop the editor can cut.

## Never write these

vocals
MC
rapping
vocal chops
singing
choir
spoken word

## The lyrics

Use these words exactly — do not change, add or remove any word or spelling. You may add section tags and short directions in square brackets. Keep every line.

```
[Instrumental]
```

## Your experiment

Write ONE prompt for this experiment, and only this one:

**ganja-dusty-jump-up** — Take the Ganja Records road: the lean, hip-hop-minded 1995 jump-up that writers call 'un-electronic'. The performer is a dusty, sampled funk drummer: a crackly vinyl Amen break chopped into cheeky, swaggering combinations, plus a short brassy funk horn stab or a fat bass guitar lick lifted off an old record. The bass is a bouncy, wobbling mid-range jump-up riff that makes a crowd skank, with dub-style space between hits. Ask for it through the record-collector mixdown: sampled off vinyl, lo-fi, punchy, swagger, bounce, playful menace. Nothing synthetic on top.

Other writers are doing the other experiments (reese-hardstep-terrorist, two-instruments-only, ragga-soundsystem-dub). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Style boxes (shared by most of the round): the very first
- shares wording with other prompts in this round: Style boxes (shared by most of the round): very first downbeat

Your previous draft:
```json
{
  "name": "ganja-dusty-jump-up",
  "style": "1995 jump-up jungle instrumental, 168 BPM, the beat lands on the very first downbeat. A dusty Amen break lifted off crackly vinyl, cut up into cocky, swaggering drum combinations with a hip-hop strut, live funk-drummer feel, no drum machine. A short brassy funk horn stab off an old soul record punctuates the turnarounds. Bouncy wobbling mid-range jump-up bassline that makes the crowd skank, dub-style gaps and echo between the bass hits. Record-collector mixdown, everything sampled from wax: lo-fi, punchy, crunchy, playful menace, bounce. Organic and un-electronic, no synths, loops cleanly.",
  "exclude": "synth lead, supersaw, rave stabs, hoover, pads, arpeggio, trance, EDM, neurofunk, dubstep, intro build",
  "lyrics": "[Instrumental]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 40,
  "styleInfluence": 80,
  "vocalGender": null,
  "durationSec": 90,
  "maxMode": false
}
```

Write a short note on what shaped it (with source URLs) to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/dnb-r2/writers/ganja-dusty-jump-up.notes.md`,
and write ONLY a single JSON object to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/dnb-r2/writers/ganja-dusty-jump-up.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "ganja-dusty-jump-up". Reply with just the two paths.