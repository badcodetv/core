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
