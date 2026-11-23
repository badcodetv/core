You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

go thanks start with arcade music too, think stranger things when they are in the arcade thanks

## What happened in earlier rounds (facts)

- The music goes under a 9:16 short of about 15-20 seconds set in a British amusement arcade at night: a young couple
  plays a claw machine for a little house and loses; a masked arcade worker says one line; then everyone turns a dial
  together and they win.
- One spoken line (about 3 seconds) sits over the music in the middle; the music must leave room for it.
- Nothing has been run for this short's music before; no take exists.

## This story's standing rules (the round is finding a new style, so only these bind)

## Story-only rules
- Inside the claw machine: only small model houses and money (coins, banknotes with no readable print); the prize is the
  same small white two-storey house with a red roof in every shot (Jack, 2026-11-23).
- Jack and Kai write the jokes: beats say what each moment conveys; joke lines stay blank for them. The one line so far
  is Jack's: "It was never broken. It was set."
- Inspired by George Carlin's "The Owners": never his audio or his words read out.
- The owners on the claw are kinds of owner (bank, landlord, energy company), never a real company's name or logo.
- The fact (adjustable grip and payout settings) is read at source before it is said or shown.

## Never write these

Stranger Things
Netflix

## No lyrics

This is an INSTRUMENTAL: no voice, no singing, no words. Leave "lyrics" as an empty string ""; everything goes in the style and exclude boxes.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**8bit-coin-slot-chiptune** — The lead voice is a raw 8-bit square-wave chip lead with a triangle-wave bass and noise-channel hi-hats, small and bleepy like an old home console, with coin-drop and credit-insert chimes stitched into the rhythm. Ask for it by describing the scene in the style box: a claw machine game at a seaside amusement arcade at night, a playful tune that keeps nearly winning, a sad descending 'you lose' jingle, then a pause, then a triumphant jackpot jingle with rattling payout coins. Keep tempo around 150 BPM and the whole thing under 20 seconds of real music. Exclude vocals, spoken words, choir, analog pads and live drums.

Other writers are doing the other experiments (analog-arpeggio-score, fm-cabinet-attract-loop, arcade-radio-synth-rock). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-by-the-balls/songs/music-r1/writers/8bit-coin-slot-chiptune.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-by-the-balls/songs/music-r1/writers/8bit-coin-slot-chiptune.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "8bit-coin-slot-chiptune". Reply with just the two paths.