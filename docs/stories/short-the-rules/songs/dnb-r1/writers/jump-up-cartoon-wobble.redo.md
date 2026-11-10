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

**jump-up-cartoon-wobble** — Play it for the joke. Bouncy, cartoonish jump-up DnB where a big wobbling, honking 'hoover' bass lurches around like a toddler's tantrum, over a punchy snare that cracks on every 2 and 4. The tone is gleeful vandalism, the rave equivalent of paper being thrown in the air, and the direct comic opposite of the bored school hymn before it. Ask for the music descriptively, as a scene: a rave erupts in a council basement, the bass bounces and barks from the first beat, wall-to-wall energy, instrumental only. Keep it one repeating 8-bar riff so the editor can loop it.

Other writers are doing the other experiments (neurofunk-reese-machine, amen-jungle-pirate-tape, live-band-rock-dnb). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Style boxes (shared by most of the round): two step breakbeat

Your previous draft:
```json
{
  "name": "jump-up-cartoon-wobble",
  "style": "instrumental, no vocals. Jump-up drum and bass, 174 BPM. Picture a rave that detonates inside a strip-lit council basement: the party is already flat out when the tape starts, zero lead-in. A bouncy, rubbery mid-range wobble bass, LFO-filtered, honks, barks and stumbles around like a toddler throwing a tantrum, answering itself in goofy pitch-bent hoover yelps. Two-step breakbeat with a punchy kick and a fat, dry snare slapping on 2 and 4, rattling shuffled hats. Cheeky, cartoonish, gleeful vandalism, the sound of paper hurled at the ceiling. One 8-bar bass hook repeated wall to wall, loop-ready, loud club master, thick sub",
  "exclude": "vocals, singing, MC, rap, hype shouts, vocal chops, chants, crowd noise, spoken word, humming, choir, intro, ambient pad, slow build, breakdown, riser, piano, liquid, soft",
  "lyrics": "[Drop: slam straight in, bass and drums together]\n[Instrumental]\n[Same 8-bar wobble hook, again and again, no breakdown]\n[Hard stop]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 62,
  "styleInfluence": 75,
  "vocalGender": null,
  "durationSec": 45,
  "maxMode": false
}
```

Write a short note on what shaped it (with source URLs) to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/dnb-r1/writers/jump-up-cartoon-wobble.notes.md`,
and write ONLY a single JSON object to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/dnb-r1/writers/jump-up-cartoon-wobble.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "jump-up-cartoon-wobble". Reply with just the two paths.