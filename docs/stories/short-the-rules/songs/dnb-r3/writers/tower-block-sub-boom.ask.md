You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Kai, 2026-11-11 (after hearing round dnb-r2's eight takes): "All right, we've got two raga, drop the raga. Drop the reggae influence. The first one, the hard step, but just without the Reese. I think we want the real mid-90s Amen heavy bass. It should just sound like a council estate. We have plenty of Suno credits, so it's worth trying a couple of variations, and maybe let's up the weirdness as well. Let's try some variations there."

## What happened in earlier rounds (facts)

- This round is for the instrumental drum and bass DROP of a short, nothing else. The hymn before it is kept and is not part of this round.
- The drop plays as its own audio track under masked gang members going wild tearing up a huge stack of paper labelled THE RULES in a cold fluorescent council basement, climbing the shelves, then one holds out a blank page and a pen to camera. It lands on a hard cut and runs about 11 s in the edit.
- Last round (dnb-r2) made four directions, two takes each: a Reese-bass hardstep, a dusty vinyl jump-up with a funk horn, a break-and-sub-only track, and a ragga/reggae sound-system dub.
- Kai's verdict, verbatim above: drop the ragga and reggae influence; he picked "the first one, the hard step, but just without the Reese"; wants "the real mid-90s Amen heavy bass"; "It should just sound like a council estate"; "up the weirdness"; "a couple of variations".
- The hardstep prompt he picked from (round dnb-r2, Suno v6, weirdness 35, style influence 80), its style box verbatim: "Mid-90s dark hardstep jungle instrumental, 1994 London warehouse, tipping into early jump-up, 165 BPM. The lead is a growling overdriven Reese bassline: two detuned saw basses phasing against each other in the low mids, crawling through a slow menacing four-note riff that snarls and bends. Under it, the Amen break thrashed thick and heavy with a hard kick doubled beneath, played almost straight for the first bars, then edited and rolling. No lead synths, no rave stabs, no pads, no strings, no bleeps: nothing high-pitched above the cymbals. Full force on the very first downbeat, no intro, no build. Dark, dry, menacing, heavyweight dubplate pressure."
- Its exclude box verbatim: "synth lead, rave stabs, hoover, pads, strings, piano, bleeps, riser, build-up, intro"
- "Up the weirdness": last round's weirdness ran 35 to 40. Kai wants it higher this round.
- Must be INSTRUMENTAL (no vocals, no MC, no vocal chops), hit hard from the first beat (a drop, not a build), loopable.

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

**tower-block-sub-boom** — This is the closest answer to Kai's pick: the 1994 hardstep he chose with the detuned-saw growl bass torn out and nothing growling in its place. The lead voice is one enormous clean sub-bass boom, a deep pitched-down kick-drum hum that drops and slides on every bar so the floor shakes. Above it, the Amen hits raw and almost unedited, with a hard kick doubled underneath. Ask for it as a short front-loaded tag list that names hardstep jungle and the Amen in the first words, then sub-bass weight, 165 BPM, instrumental and no intro. Push weirdness to about 55 with style influence high (about 80) so it stays in the lane but finds a stranger groove than last round.

Other writers are doing the other experiments (rooftop-pirate-transmission, concrete-stairwell-distortion, sampler-mangled-amen). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/dnb-r3/writers/tower-block-sub-boom.notes.md`,
and write ONLY a single JSON object to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/dnb-r3/writers/tower-block-sub-boom.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "tower-block-sub-boom". Reply with just the two paths.