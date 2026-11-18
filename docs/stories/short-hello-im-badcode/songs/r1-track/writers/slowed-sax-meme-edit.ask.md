You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Jack, 2026-11-12, ruling the structure (verbatim): "real footage of ai data centers and basically evil shit happeing now falshing on screen in a horror compiliation with cinematic music, then the music slows down to nothing and says heres what to do then badcode logo."

Jack, 2026-11-18, picking the sound from the library for the warm opening (his selected option, verbatim): "Sound: synthwave — Neon 80s-revival synths, nostalgic for a decade, under the opening." alongside his own direction: "the vibe of internet meme edits of the best of the 00s/90s ... Frutiger Aero future, 2026 is the new 2016, chill guy from the future, more happy nostalgic meme stuff".

Then: "let's start the script and all the scenes and let's start everything, basically."

## What happened in earlier rounds (facts)

- The track is the whole music of a ~22-second vertical short (BadCode Shorts, "Hello, I'm BadCode"), the channel's intro and trailer. One voice (BadCode) speaks over it; the music is instrumental only (Jack, 2026-11-15: shorts' Suno tracks are music and sounds only, never speech).
- The picture, in order: 0-4 s something warm and happy from the internet of the 00s/90s, meme-edit style (glossy blue skies, bubbles, pool water, old computers, skateparks at sunset); 4-7 s a cut to a masked figure, to camera, deadpan; 7-17 s a rapid horror reel of real footage of now (AI data centres, climate disaster, cost of living, war), half a second a shot; 17-20 s the music slows down to nothing; on black, one spoken line; then the logo.
- So the track turns: warm nostalgic synths at the top, a hard turn at about 4 s, cinematic dread under the reel, then a slow-down to silence by about 20 s.
- The previous music on this short was a temp track nobody picked.

## This story (stay inside its look and sound; another part's look does not apply)

# Hello, I'm BadCode


## What it is
A BadCode short (9:16, about 25 s): a voice says "Hello. I'm from the future." over something warm, BadCode the
masked figure says deadpan "It didn't go well.", a rapid horror reel of real footage of what is happening now, then
on black "Here's what to do next." and the logo. The point: who BadCode is, in one breath. Doubles as the profile
intro and channel trailer. State: rough cut 1 (24.9 s) on the timeline page; temp voice, temp music, placeholder stills.

## Look
- Status: Not decided — run story-style (look.md is EMPTY; mood board r3 is the open round).
- Picked so far: C1-a, blue hour (the hook). Jack's direction for the whole piece: the vibe of internet meme edits
  of the best of the 00s/90s (not childhood); trying Frutiger Aero future, "2026 is the new 2016", chill guy from
  the future, more happy nostalgic meme stuff. Colourful meme writing goes on in the edit, not in Flow.
- The horror reel is real footage (green-tier only) plus Flow gap stills, rapid fire, ordered bright to dark.
- Video: Omni 1.2 Flash, 9:16, Frames. Flow project `99357c2f-11c0-4909-94a8-adc5a2bbd692`.

## Sound
- Status: Not decided — run story-style (sound.md is EMPTY).
- Music: cinematic under the horror reel, then slows down to nothing before the last line. Current music is a temp.
- Voice: one voice, BadCode. Current take is TEMP (Sadaltager, profile `scenes/hello/voices/temp-badcode.md`:
  calm, very polite, far-future, deadpan and courteous). Voice casting still owed.
- Words: only the three lines plus "Here's what to do next." No other words.

## Story-only rules
- The balaclava follows `docs/brand/README.md`: a large white ring round the WHOLE face, the red triangle high
  inside it over the wearer's LEFT eye (right of picture), NO eye/nose/mouth holes, no skin, gloves, no robot parts.
  Reference `docs/brand/balaclava/mask-reference.jpg`. Check every triangle zoomed in.
- The logo is the real logo files laid in by ffmpeg/Premiere, never drawn by Flow.
- No AI likeness of a real person.
- Horror reel: 0.5 s per shot, bright to dark; faster (0.38 s) or random order failed the photosensitivity gate.
- Put the brand mask sentence in the round's preamble so the sameness gate exempts it.
- Strip audio from all real footage. `marketing-gatekeeper` before anything goes out; nothing is uploaded for now.

## Flow project
- `99357c2f-11c0-4909-94a8-adc5a2bbd692` — scenes/hello

Open the part's project before its first Flow call; never use it for another story.

## Library pieces in use
Picked by Jack, 2026-11-18, starting the full remake (from: balaclava, clean room, real photo; VHS camcorder, chiptune,
synthwave). Copied and adapted here; the library entries are not live rules.
- **Balaclava:** BadCode on screen is the brand balaclava, fixed by `docs/brand/README.md` (the rules are in *Story-only
  rules* above). In motion, the model redraws the mask every frame and the ring and triangle vanish when the head turns:
  write that the face keeps toward the camera into every motion prompt, and check the mask zoomed in at three points per clip.
- **Real photo (Unsplash):** the warm 00s opening starts from real photos found with
  `python3 scripts/scene/unsplash-refs.py <scene-dir> "<query>"`, picked on a picks page and given to Flow as the reference,
  so it reads as real footage of the time, not AI. The prompt says only what happens.
- **Synthwave, alongside Jack's meme-edit direction (under the warm opening):** a 2010s revival of 80s film-score synths:
  pulsing 16th-note analog bass, detuned saw pads, sweeping arpeggios, gated-reverb snare, a sad-heroic lead, about
  90-130 BPM, instrumental. It reads as "the cool figure from a future that already happened". Risk: it is the most
  familiar style of its kind and flatters nostalgia, so it can read as borrowed; keep it as the warm half only, against
  the horror reel's cinematic dread. Ask Suno for the period and the gear, never an artist; exclude EDM drop, trap,
  autotune, big pop chorus.

## Where the detail is
- [README.md](./README.md), [RESUME.md](./RESUME.md) (next steps), [look.md](./look.md), [sound.md](./sound.md)
- Beats and boards: [scenes/hello/scene.json](./scenes/hello/scene.json); decisions: [scenes/hello/picks.md](./scenes/hello/picks.md)
- Mood board https://claude.ai/artifact/YMxBMusYT79tk2XsADbNAL · timeline https://claude.ai/artifact/B5f8vmPozGXf7f9CpFNGBP
- Research: [research/nostalgia-meme-formats.md](./research/nostalgia-meme-formats.md), [research/footage-shortlist.md](./research/footage-shortlist.md)

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "v6",
  "durationSec": 22
}
```

## No lyrics

This is an INSTRUMENTAL: no voice, no singing, no words. Leave "lyrics" as an empty string ""; everything goes in the style and exclude boxes.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**slowed-sax-meme-edit** — The lead is a smooth, breathy late-80s-style synth saxophone melody over warm slap-free fretless bass, glossy pads and a soft drum machine at about 100 BPM, already slightly slowed and drenched in reverb like a 2016 meme edit of old mall music: happy, hazy, a little too nostalgic. At about 4 s the saxophone and beat drop out mid-phrase and are replaced by detuned, warped tape-wobbled pads under an anxious ticking clock and low distorted bass pulses, as if the same cassette had gone bad. The warble gets heavier and darker to about 17 s, then everything slows and sags in pitch to a standstill and silence by about 20 s. Ask for it through the slowed-and-reverb, VHS-tape, chopped meme-edit production words plus the two moods; exclude vocals, choir, trap hi-hats, EDM drop, autotune, big pop chorus.

Other writers are doing the other experiments (analog-lead-into-braam, aero-glass-bells, piano-to-orchestra-trailer). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/songs/r1-track/writers/slowed-sax-meme-edit.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/songs/r1-track/writers/slowed-sax-meme-edit.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "slowed-sax-meme-edit". Reply with just the two paths.