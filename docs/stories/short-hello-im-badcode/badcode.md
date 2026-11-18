# Hello, I'm BadCode

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A BadCode short (9:16, about 25 s): a voice says "Hello. I'm from the future." over something warm, BadCode the
masked figure says deadpan "It didn't go well.", a rapid horror reel of real footage of what is happening now, then
on black "Here's what to do next." and the logo. The point: who BadCode is, in one breath. Doubles as the profile
intro and channel trailer. State: rough cut 6 (37.05 s) on the timeline page; next steps in RESUME.md.

## Look
- Status: Not decided — run story-style (look.md is EMPTY; mood board r3 is the open round).
- Picked so far: C1-a, blue hour (the hook). Jack's direction for the whole piece: the vibe of internet meme edits
  of the best of the 00s/90s (not childhood); trying Frutiger Aero future, "2026 is the new 2016", chill guy from
  the future, more happy nostalgic meme stuff. Colourful meme writing goes on in the edit, not in Flow.
- The horror reel is real only (Jack, round 11: "ai slop and boring"): green-tier footage plus real Unsplash photos used as they are
  (no Flow movement at 0.5 s), rapid fire, bright to dark, ordered so nearly every cut goes darker (flashing gate).
- Video: Omni 1.2 Flash, 9:16, Frames. Flow project `99357c2f-11c0-4909-94a8-adc5a2bbd692`.

## Sound
- Status: Not decided — run story-style (sound.md is EMPTY).
- Music: cinematic under the horror reel, then slows down to nothing before the last line. Current music is a temp.
- Voice: one voice, BadCode. **PICKED 2026-11-18 (Jack, round 6):** a Google designed voice, `voice_61xqq38hm0da`
  ("An ordinary man in his thirties from Birmingham, low-voiced and unhurried, talking plainly like he would to a
  neighbour."), model `gemini-3.8-flash-tts`, rendered plain: `scripts/aistudio-tts.sh <lines> <out> --plain --model
  gemini-3.8-flash-tts --voice voice_61xqq38hm0da`. No style notes. (Rounds 1-5 sounded uncanny or posh: `scenes/hello/picks.md`.)
- Words: script A, the confession (Jack, 2026-11-18), `scenes/hello/script-directions-r1.md`; Jack's line after the reel.

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
