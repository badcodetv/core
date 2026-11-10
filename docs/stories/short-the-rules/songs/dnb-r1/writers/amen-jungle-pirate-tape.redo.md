You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Kai, 2026-11-10: "So, I'm thinking with this one, what would be really interesting is to then cut in some hard drum and bass as the bally guys are ripping up the rules. Because I think we've got an intro that makes sense, but then as soon as they kick in ripping up, it would be quite funny to follow that song with then a really heavy drum and bass drop. So could we please cut that drum and bass drop, no lyrics, nothing else, just like the heavy kind of, we need a heavy loop just to drop in after. I want to keep the music we just recorded and drop the drum and bass as a separate track in Premiere to be clear.

So, essentially, like, the last scene is drum and bass, but with the ballets ripping up all the rules. It's like the chaos refrain from the rest.

This also means we're not, it doesn't feel like we're rushing the short because it might well be more than 20 seconds long, I think, to squeeze this in."

## What happened in earlier rounds (facts)

- "bally guys" / "ballets" = the balaclava gang (BadCode's masked figures) in the picture.
- The track before it (kept, unchanged) is a picked Suno take: a whole 1980s primary school singing a four-line hymn, bored and flat, over a thumping out-of-tune upright piano; it ends at 16.4 s on one held piano chord, then silence. The drum and bass drop is cut in hard after that, as a separate audio track in Premiere, under the gang tearing up a huge stack of paper labelled THE RULES in a cold fluorescent council basement, ending on one of them holding out a blank page and a pen to camera.
- This track is INSTRUMENTAL: no vocals, no lyrics, no vocal chops, no MC. It must hit hard from the very start (a drop, not a build) and work as a loop the editor can cut.
- No Suno take has been made for this part yet.

## The lyrics

Use these words exactly — do not change, add or remove any word or spelling. You may add section tags and short directions in square brackets. Keep every line.

```
[Instrumental]
```

## Your experiment

Write ONE prompt for this experiment, and only this one:

**amen-jungle-pirate-tape** — The drummer is the star. A 1994 UK jungle track built on a frantically chopped, time-stretched Amen break with a rolling sub bass and one stabbing rave chord, recorded off a pirate radio tape so it is slightly crunchy, saturated and lo-fi. The rough, homemade, British, working-class rave sound gives the gang a native soundtrack, not a slick festival drop. Ask for it by era and production detail: 1990s jungle, hardcore breakbeat, cassette hiss, pirate radio, 165 BPM, breaks from bar one, no MC, no ragga vocal samples. The lyrics box holds only [Instrumental] and a [Break] cue at the top, so the chopped drums lead in immediately.

Other writers are doing the other experiments (neurofunk-reese-machine, jump-up-cartoon-wobble, live-band-rock-dnb). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: lyric [directions] (shared by most of the round): from the first
- shares wording with other prompts in this round: lyric [directions] (shared by most of the round): the first beat

Your previous draft:
```json
{
  "name": "amen-jungle-pirate-tape",
  "style": "1994 UK jungle instrumental, 165 BPM, starts mid-roll on bar one with no intro: a frantic chopped and time-stretched Amen breakbeat, ghost snares, stuttering snare rolls, metallic 12-bit sampler grain on the stretched hits. Rolling mono sine sub bass under the breaks, one stabbing hardcore rave chord punched in on the offbeats. Homemade bedroom-studio mix taped off a London pirate radio broadcast: cassette hiss, saturated and slightly crunchy, wobbly tape, warm distortion on the drums. Raw, rough, working-class, loopable, relentless.",
  "exclude": "vocals, MC, rapping, ragga vocal samples, vocal chops, singing, choir, spoken word, piano, slow intro, build-up, riser, ambient pads, polished festival EDM, dubstep wobble, neurofunk, clean modern mastering",
  "lyrics": "[Break: chopped Amen drums from the first beat]\n[Instrumental]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 45,
  "styleInfluence": 75,
  "vocalGender": null,
  "durationSec": 45,
  "maxMode": false
}
```

Write a short note on what shaped it (with source URLs) to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/dnb-r1/writers/amen-jungle-pirate-tape.notes.md`,
and write ONLY a single JSON object to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/dnb-r1/writers/amen-jungle-pirate-tape.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "amen-jungle-pirate-tape". Reply with just the two paths.