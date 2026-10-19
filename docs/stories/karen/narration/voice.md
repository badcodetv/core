# The narrator — ElevenLabs Voice Design

**Build this once, save it, and never rebuild it.** A saved voice is identical on
every generation forever, which is the entire reason we moved the narration off
Suno: thirty-odd lines across five acts will drift into three different men
otherwise.

## The brief

A blend of four references, none of which can be named to the engine — ElevenLabs
blocks cloning real people, and descriptive traits steer better anyway:

| Reference | What we take from it |
| --- | --- |
| Harrison Ford | dry, clipped, laconic understatement; a reluctant baritone |
| Sam Elliott | unhurried Western ease and warmth |
| Patrick Stewart | storybook cadence — reading a bedtime story to adults |
| Bryan Cranston | precise American consonants, warm authority |

**"Not too deep"** is a hard requirement and has to be stated as a negative in
the prompt, because both of the first two references sit low and the model will
chase "deep" if you let it.

## The Voice Design prompt

```
Native American English. General American with a faint Western ease. Male, late 50s to early 60s. Perfect audio quality, studio quality.
Persona: dry, wry storyteller. Emotion: warm, amused, deadpan.
A mid-range baritone with a light sandy rasp and a little smoke in it — lived-in and weathered, but clear and crisp. Never booming, never deep. He speaks slowly and conversationally, unhurried, landing dry asides flat and letting the pauses carry the joke. Fond of the listener, and faintly amused by everything he's telling them.
```

That follows ElevenLabs' documented structure exactly: language and dialect first,
then gender and age, then quality, then persona and emotion, then timbre and
delivery.

## Preview text

**Turn "Generate Preview Text" OFF** and paste this. Preview text must match the
personality you asked for, and longer text produces a more stable voice:

```
Karens have been known to plague the world with their unrelenting entitled bullshit. This Karen is no different. She starts her morning with polite pep talks, followed by active listening. Turns out putting fish in the microwave is the cleaner's fault. Who knew.
```

## Sliders

| Control | Set to | Why |
| --- | --- | --- |
| **Guidance Scale** | **30%** | ElevenLabs' own guidance: **high guidance makes a voice sound artificial or robotic**, and they recommend *longer, detailed prompts at a lower guidance scale*. Our prompt is long and detailed. Band is 20–40%. If it comes back generic, go to 38% — never higher. |
| **Loudness** | **centre (0)** | Zero is neutral, ~−24 LUFS, audio unchanged. Loudness bakes into the **saved voice**. Pushing it hot squashes dynamic range, which reads as synthetic, and leaves no headroom. Level in the NLE instead. |

## ⚠️ Never describe the space

ElevenLabs' docs are explicit: **FX terminology — "reverb", "echo", "phone",
"tape" — degrades the output.** This is what went wrong on the Suno attempts,
where a style prompt asking for "bare room tone" produced an echoing, processed
voice. Say `studio quality` and you get dry and close for free.

## Steps

1. **Voices → Create a voice → Voice Design.** Paste the prompt, paste the preview
   text, guidance 30%, loudness centred.
2. **Generate.** Each press returns three candidates for one credit deduction. Run
   it three or four times for a shortlist of nine to twelve.
3. **Audition on one line only** — the driest thing in the script:
   *"Who the fuck decides to vote that way. Anyway."* Whichever take lands that
   flat and amused is the narrator. A take with any lift or grandeur is wrong,
   however nice the timbre.
4. **Save the winner** to the library and name it. Record the name here when you do.

## TTS settings for every generation

| Control | Set to |
| --- | --- |
| Model | **Eleven v3** (the one that responds to audio tags) |
| Stability | **Natural** — not Creative (hallucinates), not Robust (stops obeying tags) |
| Similarity | ~75 |
| Style | 0 |
| Speed | *not available on v3* — pacing comes from tags and punctuation |

---

**Voice name once saved:** `# TODO`

---

# 🆕 The same narrator in Google AI Studio (2026-10-19)

> Jack, 2026-10-19: recreate this ElevenLabs voice in the AI Studio text-to-speech we use now. Built
> from the prompt above, the house AI Studio notes ([`docs/ai-studio/README.md`](../../../ai-studio/README.md))
> and Google's own docs. ⬜ **Nothing below has been generated or heard yet.**

## What changes in translation

| ElevenLabs prompt said | AI Studio version | Why |
| --- | --- | --- |
| *Native American English* | *American* | Read literally, "Native American" is a different accent |
| *Perfect audio quality, studio quality* | Dropped | No quality field on this engine; studio words risk a room sound (trap in the house notes) |
| *A mid-range baritone… Never booming, never deep* | *His voice sits in the middle of his range* | `baritone` / `deep` summon a movie-trailer read, and a "never" puts the word in the prompt |
| *Speaks slowly… unhurried… letting the pauses carry the joke* | Gone | Measured on this engine: slow and pause words came back **"boring"** and **"way too slow"** |
| *Warm, amused, deadpan* | **Anger held down, sarcasm as a weapon** | The 15 Oct ruling (direct and aggressive), and the house finding that deadpan needs pressure under it |
| The four real-actor references | Still never named | Same rule as ElevenLabs |
| Tags `[understated]`, `[matter-of-fact]`, `[drawn out]` | `[sarcastic]`, `[serious]`, `[slow]` | Custom emotion tags are weak on this engine; use the documented ones |

The **timbre is kept as written**: late fifties, light sandy rasp, lived-in but clear, faint Western ease.

## Route A 🥇 — Voice Design on Gemini 3.8 (the true equivalent)

Google's newer model (`gemini-3.8-flash-tts`) has **Voice Design**: a one- or two-sentence description
becomes a **saved voice** (kept a year), the same thing we did on ElevenLabs. Google's rules: permanent
traits only (age, gender, timbre, accent, baseline delivery) in the description; per-line emotion goes
in a short **style** field at generation time; long Audio Profile blocks now cause drift.
⚠️ Runs on the **paid** key (Kai's project), and the AI Studio page asked to link billing on 3 Oct.
Untried here.

Settings: Model `gemini-3.8-flash-tts` · Type: prompted · Gender: male · Language: `en-US` · Name: `Karen narrator`

**Voice Design → description**
```
A dry, wry American storyteller in his late fifties with a faint Western ease, a mid-range voice with a light sandy rasp, lived-in and weathered but clear and crisp, who talks straight to the listener with anger held tightly in check.
```

**Style, per chunk** (pick one; leave empty when the line carries itself)
```
dry and certain, contempt barely held back
```
```
sarcastic, cutting
```
```
serious and pointed, slower
```

On 3.8, sound events in the transcript use angle brackets (`<short pause>`, `<sigh>`), not square ones.

## Route B — Gemini 3.1 Composer with a prebuilt voice (the tested house route)

The route every house narrator so far was made on. It cannot design a voice: the **voice name owns the
timbre**, and the prose only steers delivery. Expect about one take in ten to drift; re-roll twice
before changing a word.

Settings: Model `gemini-3.1-flash-tts-preview` · Mode: Composer · Voice: **Algenib** (gravelly, lower: the
nearest to the sandy rasp) · fallback **Charon**, then **Iapetus** · Accent dropdown: **Neutral** (the
accent is in the prose once; don't vote twice) · Style and Pace dropdowns empty

**Speaker settings → Voice Direction**
```
A dry, wry storyteller in his late fifties, a voice from the future that has already seen how all of this ends. American, with a faint Western ease. His voice sits in the middle of his range with a light sandy rasp, lived-in and weathered but clear and crisp. He talks straight to the listener, conversational and completely certain, with real pressure under the dryness: anger banked down and held in check, sarcasm used as a weapon, tightening rather than getting louder when it matters. He lands the dry asides cleanly and moves on.
```

**Scene**
```
Late at night, telling one person a story he is tired of being right about.
```

**Sample Context**
```
The narrator of a dark satirical comedy, hired for voice-over with a bite.
```

## The audition script (both routes)

Two takes per voice. The first is Jack's new line (the film's point); the second is the old ElevenLabs
audition line, which had to land flat and amused and now should land with contempt.

**Speech block / transcript, take 1**
```
People like Susan lay in bed all day, doing nothing about AI taking everyone's jobs. Karen, well... she rolls her sleeves up and actually does something about it.
```

**Speech block / transcript, take 2**
```
[sarcastic] Who the fuck decides to vote that way. Anyway.
```

**Pass:** sounds like a person, not AI; American, not a cartoon; the anger is felt but he never shouts.
**Fail and fix:** wrong timbre → change the voice, never the prose. Too slow → join short sentences with
commas. Shouting → take "anger" out of the style field and leave it in the description only.

## Route B auditions — rendered 2026-10-19, unheard by a human

12 takes (Algenib, Charon, Iapetus × the two lines × two rolls), the boxes above exactly, the API
route (`scripts/aistudio-tts.py`, paid key). Files: Jack's Desktop
`Youtube Vids\animation\Karen\narrator-auditions\<voice>-line<n>-<a|b>.wav`, and imported into
`Karen vid.prproj`, bin **narrator auditions 2026-10-19**. Each take was checked by the listen tool
(Gemini; logs in `docs/listening/log/2026-10-19-11*`). ⬜ **Machine notes, not a judgement:**

| Voice | Line 1 (Susan) | Line 2 (vote) | Machine's read |
| --- | --- | --- | --- |
| **Algenib** | 15.0s / 13.2s, complete | 4.4s / 4.7s, complete | Most contempt; low, gravelly; slowest; line 2 is a hushed growl |
| **Charon** | 13.3s / 13.3s, complete | 4.4s / 4.8s, complete | Most even and documentary; milder contempt on line 1; line 2-b the angriest of all |
| **Iapetus** | 13.0s / 14.0s, complete | 5.7s / 5.6s, complete | 1-b heard as *"subtle rural inflection"*, the nearest to the Western ease; 🔴 1-b peaks at **+0.8 dBTP** (clips), lower its gain |

All twelve: General American, heard as human, no shouting. Several read "well" as *"Karen? Well,"*
(a question) rather than *"Karen, well…"*.

**Voice name once chosen:** ✅ **Algenib** (Route B boxes above, unchanged) — Jack, 2026-10-19: "algenib is the winner".
