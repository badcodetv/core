# Suno Speech (beta): what it is, what it can't do

Researched 2026-11-13 for the Priority Lane short, after round r5 (12 single-speaker takes:
two paramedics, a driver and a minister) came back with **every voice sounding the same and
weird** (Jack). Engine facts only. What a story's voices should sound like lives in its `sound.md`.

Evidence tiers: **[Suno]** = Suno's own page · **[guide]** = third-party write-up, not checked
by us · **[ours]** = what our own runs showed · **[inference]** = our reading, untested.

## The short answer

Speech is **a narration-over-music toy, not a voice-casting tool.** It has one voice control
(Male / Female) plus a text description. Nothing saves or locks a voice, and you can't give it
a reference clip or a Persona. Suno's own launch post admits that British accents drift. No
source shows it doing short, shouted, multi-character drama, and our r5 round suggests it
can't: twelve different descriptions collapsed into one voice.

**For differentiated character voices, Speech is the wrong tool.** See "What to do instead".

## What it is

- Launched **2026-10-01** as an open beta on web, iOS and Android. **[Suno]**
  <https://suno.com/blog/introducing-speech-beta> ·
  <https://suno.com/release-notes/introducing-speech-beta>
- Suno's words: "the first audio model that generates voice and music together as one
  cohesive track". You "type an idea, a poem or something you've written, then describe the
  voice and musical style you have in mind". **[Suno]**
- Suno's own example uses are "wildly overproduced dramatic readings", meditations, poems, pep
  talks, bedtime stories, "hype speeches over stadium drums" and "ASMR grocery lists".
  Suno names no dialogue or drama scenes. **[Suno]**
- Suno's own warning: "Occasionally, British accents can wander off to Australia and back.
  Dramatic pauses may be *very* dramatic." **[Suno]**
- There's an official how-to video at <https://www.youtube.com/watch?v=rTezej0UyIE>, not yet watched.

## The controls (Create → Speech tab)

**[guide]** Undetectr <https://undetectr.com/blog/suno-speech-beta> ·
moelueker <https://moelueker.com/blog/suno-speech-how-to-use> · and **[ours]**
(`scripts/suno/speech.mjs`)

| Control | What it does |
| --- | --- |
| Simple / Advanced | Simple writes the script from a one-line idea. Advanced takes your own **Script** and **Tone** |
| Script | The words to perform. Exact wording is not guaranteed |
| Tone box | Delivery, pace, mood and setting, **and** the music. Accent, age and texture all come from here |
| Vocal Gender | Male / Female: the only hard voice control |
| Background music | On / Off. "Off turns Speech into a plain voiceover tool" |
| Variety | Five steps. Undetectr names them "Exact style, Balanced variety, Distinct styles, Bold exploration, Unreasonably varied". Our UI showed "Normal", so the labels may have changed. **The r5 round ran on Normal, not Exact** |

Not there:

- **No Voices or Personas inside Speech** during the beta. **[guide]** Undetectr
- No reference audio, no saved voice and no seed. **[guide]**
- **No published limits:** maximum length, credit cost, languages and commercial terms are all
  missing. **[guide]** dev.to <https://dev.to/akaranjkar08/suno-speech-beta-review-2026-pricing-vs-elevenlabs-kni>
- The Song Editor works on Speech takes: you can replace one word for about 4 credits, then press
  Commit. **[guide]** Undetectr

## Why r5 sounded the same and weird

1. **There is only one voice axis.** Gender is the only hard control, and everything else is a
   suggestion inside a tone box that also describes the music. No source documents a way
   to make two speakers sound different. **[guide]**
2. **Variety above the lowest step lets the narrator wander.** Undetectr: on Balanced, "two
   takes of the same script can come back with different energy … and even a different-sounding
   narrator". So the takes drift around a default voice instead of locking to the
   description. **[guide]** r5 ran on Normal. **[ours]**
3. **Our tone boxes were long and shared their wording.** The r5 boxes ran 70 to 83 words each,
   and shared phrases ran across them: "voice only" in 8 of 12, "dry" in 8 of 12, "hospital
   drama" in 5 of 12, "working-class" in 5 of 12. Published examples run about 20 to 40 words, and every
   one leads with the voice. **[inference]** Shared tails pull every take toward one voice.
4. **The accent is weak by design.** Suno says British drifts to Australian, and no source has a
   tested British prompt. **[Suno]**
5. **The lines are short and shouted, which is the wrong material.** Speech is tuned for
   narration with a music bed. The only intensity example any guide gives is a pep talk
   ("building from a low growl to a full-throated roar"). Nobody has published shouting,
   one-line barks or emergency dialogue. **[guide]** Our lines are 2 to 4 s bursts, so the
   model has no room to settle into a voice. **[inference]**
6. **Turning the music off may not be clean.** The reported workaround is music Off, Variety at
   the lowest step, and "No background music." in the tone box, but music still appeared in one
   test. Reverb also varies from take to take (one take sounded like a hall, another was dry).
   **[guide]** AIReiter <https://aireiter.com/blog/suno-speech-beta-guide> · Undetectr

## If we try Speech once more

Every point here is untested on our material. Treat it as one cheap round, not the plan.

- **Variety at the lowest step** ("Exact style"), music **Off**, and "No background music." at the end of the tone box.
- **Keep the tone box short (20 to 40 words), voice first,** written as a casting call: age,
  texture (gravel, thin, plummy, breathy), pace, emotion and accent. "Calm" alone "leaves too much
  to chance". **[guide]**
- **Make each role differ on the physical voice, not on class words:** very old against young,
  deep and slow against thin and fast, shouting against murmuring. Give no two roles the same
  sentence.
- **Write for the ear:** short sentences, punctuation for breath, and no rhyme or repeated refrain
  (those push it toward singing). **[guide]**
- **Give it more to say.** Put each line inside two or three sentences of spoken context and cut
  the line out afterwards. **[inference]**
- **Run several takes:** "a second take is often more useful than adding a long stack of
  corrective instructions". **[guide]** AIReiter
- **Listen to the end of every take,** because last words can get clipped. **[guide]**

## What to do instead

- **For character voices, use the AI Studio voice library** (`docs/ai-studio/`): 5,000 voices
  with an accent filter, where you pick a voice instead of describing one. It was the first
  engine that sounded human on the first take. Kai's 2026-11-13 note ("AI Studio voices still
  sound AI") is the reason we tried Suno, so a voice from the library, chosen by ear on the
  `voice-casting` picks page, is the fair re-test.
- **Use Speech for what it's built for:** narration over a score (a BadCode narrator intro or
  a trailer voice-over), where the music bed and one consistent narrator are the point.
- **Let Suno do the rest of the sound:** the music bed and the stings, in a separate pass, as
  Jack planned in r5.

## Sources

- Suno launch post (Jack Brody, 2026-10-01): <https://suno.com/blog/introducing-speech-beta>
- Suno release note: <https://suno.com/release-notes/introducing-speech-beta>
- Undetectr guide, the most concrete source (controls, Variety labels, drift, clean-voice preset): <https://undetectr.com/blog/suno-speech-beta>
- AIReiter guide (prompt shape, music-off workaround): <https://aireiter.com/blog/suno-speech-beta-guide>
- moelueker walkthrough (Advanced controls, a narrator built mostly from music): <https://moelueker.com/blog/suno-speech-how-to-use>
- Jack Righteous Speech guide (proposed and untested prompts, "about 8 minutes" unsourced): <https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/suno-speech-beta-spoken-audio-background-music>
- dev.to review (pricing and missing limits): <https://dev.to/akaranjkar08/suno-speech-beta-review-2026-pricing-vs-elevenlabs-kni>
- No useful content: wiretensors.ai directory page. The Medium guide refused automated fetches (403).
- **Gap:** we found no Reddit or forum reports of real use, and no published example of
  shouted or multi-character dialogue.
