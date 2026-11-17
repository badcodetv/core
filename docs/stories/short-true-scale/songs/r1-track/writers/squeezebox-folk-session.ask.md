You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

look at the notes, also the do this "- ⬜ Lip sync: the mouths move, but they aren't synced to the voices yet.
  - ⬜ No music or pub atmosphere.
  - 🟡 The answer line is long (about 13 s), and clip 4 holds its last frame for 1.6 s. Trimming that line would tighten both." make all of the dialogue faster too. maybe also put stats at the end in just plain text, then put the badcode logo after, animate it like a pub fruit machine but the name and logo instead thanks

## What happened in earlier rounds (facts)

- The track is the whole music bed of a ~35-second vertical short (BadCode Shorts, "True Scale: Nearest Wins"): a British local pub on quiz night. The quizmaster asks the tiebreaker ("How many homes in England have been empty six months or more?"), a table shouts "Fifty thousand, tops!", she reads the answer (303,185, plus 267,894 second homes), "Nearest... table nine. Bob." The pub turns to Bob, who lives in a tent: "How'd you know that?" "I sleep opposite one." He hands the meat-raffle prize to the next table and walks out into the rain. Then plain text with the numbers, then the BadCode logo landing like a pub fruit machine (reels spinning and stopping).
- Dialogue sits on top of the whole thing (AI Studio voices, not in this track): the bed must stay under speech: no lead melody fighting the voices, sparse in the 300 Hz-3 kHz voice band.
- Jack asked for "music or pub atmosphere". Shorts Suno tracks are music and sounds only, never speech (Jack, 2026-11-15): no vocals, no words, no crowd chant with words.
- Tone: warm, funny, a bit sad at the end (Bob leaves into the rain), never a sad-charity-advert piano.
- No earlier music rounds for this short.

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "v6",
  "durationSec": 40
}
```

## No lyrics

This is an INSTRUMENTAL: no voice, no singing, no words. Leave "lyrics" as an empty string ""; everything goes in the style and exclude boxes.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**squeezebox-folk-session** — The performers are a pub folk session: a melodeon or accordion pumping chords, a bodhran and a strummed acoustic guitar, all played back in the room, loose and a bit drunk. Ask for it as a three-part story in time order (warm busy session, a hush as the pub turns to Bob, a lone melodeon drone under rain, then a jaunty squeezebox flourish and a bell clang to finish). Keep the instruments rhythmic and chordal so nothing carries a jig melody over the talking. Exclude vocals, singing along, fiddle lead, tin whistle lead, Celtic epic and Irish pub chorus.

Other writers are doing the other experiments (pub-upright-piano, colliery-brass-band, fruit-machine-electronics, rhythm-section-trio, rain-and-room-ambient). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-true-scale/songs/r1-track/writers/squeezebox-folk-session.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-true-scale/songs/r1-track/writers/squeezebox-folk-session.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "squeezebox-folk-session". Reply with just the two paths.