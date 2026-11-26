You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Kai, 2026-11-26 (on cut r9 of the Karen story film, after I said the coup music was still the score Flow made with the evacuation clip and a proper Suno cue needed his OK):

"Hey Claude, yeah, please use Suno to your heart's content. That's absolutely what we should do."

Kai, note pinned at the evacuation on the timeline page (first left on cut r4b, 2026-11-25): "Also, here the music should turn to dramatic music somehow, we need like a dramatic scene of audio to underpin this."

## What happened in earlier rounds (facts)

What the cue plays under (cut r9 of the Karen story film, a narrated satire, about 4:50 to 5:05):
- A live late-night talk show. The President is the guest. The screen in the studio suddenly flashes on.
- Narrator: "The screen in the studio suddenly flashes on." / "[gravely] It's A.I. Sean!"
- A.I. Sean (a robotised voice) on the screen: "Mister President. Your role has been made redundant."
- The screen breaks up. Narrator: "The Secret Service immediately rush in, and race the President out."
- Times Square: a crowd watching the giant screen.
- Then the next scene (the President in his car calling Karen) starts with the film's mellow score again.

Length needed: about 25 seconds of music, starting at the screen flashing on. The cut is trimmed in the edit, so a longer take is fine.
The cue sits under speech the whole time: the narrator and the robot voice must stay clear on top of it.
Instrumental only: no voices of any kind.
What plays there now: the orchestral score Flow generated with the evacuation video clip (timpani, brass, strings), 8 seconds, looped. Kai has asked for a proper cue.
The rest of the film's score: mellow jazz / boom-bap hold-music cues around 86 BPM.

## This story's standing rules (the round is finding a new style, so only these bind)

## Story-only rules
- **The point (Kai, 2026-11-24):** Karen's persistence climbs the ladder of managers, and it is what makes her useful against the AI: at the end the sacked President calls *her* ("we need to work together to beat this"). The escalation is the centrepiece: map, ladder and weather moving together, fast. "I've got all day to complain" is said twice: set up at the end of call 1, repeated as Aaron walks past.
- No legible text anywhere in a generated frame; Sean AI's UI and "To be continued" go in post.
- Present-day or it's a reject: name the no-era-shift twice.
- Film set, not news: never *news, reporter, broadcast, live, television, President* in a prompt.
- Cast, never describe a face; Flow's personality field stays empty on every Character.
- The phone box is a fixed point (the accepted §2h kiosk still); in Act 2 sameness is the point.
- Two figures in relative motion merge: shoot two-handers as singles; crowds are stills.
- Satire played straight: the joke is in the words, never the music; no comedic/novelty in Style; no franchise or artist names in any box; the tempo never changes.
- Write `Ay-Eye Sean` in TTS transcripts.

## No lyrics

This is an INSTRUMENTAL: no voice, no singing, no words. Leave "lyrics" as an empty string ""; everything goes in the style and exclude boxes.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**percussion-and-low-brass** — A large percussion ensemble leads: big drums, frame drums and toms playing a heavy, sparse pattern at a fixed 86 BPM, with low horns and trombones answering in short dark stabs. Leave deliberate gaps, so-called edit points where the energy floats for a beat, so the narrator's lines and the robot voice can land in the holes. One huge drum hit for the screen flashing on, a rising drum roll for the rush to the exit, then a held low brass chord under the crowd watching the giant screen. Serious and cinematic, with no fanfare or heroic melody. Instrumental only; exclude vocals, choir, strings melody and synth leads.

Other writers are doing the other experiments (low-strings-ostinato, analog-synth-pulse, dark-boom-bap, solo-low-piano, hybrid-glitch-sound-design). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Style boxes (shared by most of the round): steady 86 bpm

Your previous draft:
```json
{
  "name": "percussion-and-low-brass",
  "style": "Dark cinematic percussion ensemble cue, instrumental, locked steady 86 BPM. Large taiko-style drums, frame drums and floor toms in a heavy sparse pattern, dry and close, with long open silences between hits. Low French horns and bass trombones answer in short muted minor-key stabs, no melody. Opens on one massive drum impact, then sparse hits with empty beats, then a rising tom and snare roll that swells, then a held low brass chord over a soft bass drum rumble. Mid-range left clear for dialogue, restrained, grave, tense. No vocals, instrumental only.",
  "exclude": "vocals, choir, chanting, humming, spoken word, string melody, violins, synth lead, arpeggio, fanfare, trumpet solo, heroic theme, triumphant, comedic, playful, electronic drums, EDM drop, tempo change, jazz, swing",
  "lyrics": "",
  "model": "v6",
  "variety": "off",
  "weirdness": 25,
  "styleInfluence": 80,
  "vocalGender": null,
  "durationSec": 45,
  "maxMode": true
}
```

Write a short note on what shaped it (with source URLs) to `/tmp/claude-1000/-home-kai-projects-badcode-badcode/0f985955-71e1-4859-97b2-07cb41634ac8/scratchpad/karen-r9/docs/stories/karen/songs/coup-cue-r1/writers/percussion-and-low-brass.notes.md`,
and write ONLY a single JSON object to `/tmp/claude-1000/-home-kai-projects-badcode-badcode/0f985955-71e1-4859-97b2-07cb41634ac8/scratchpad/karen-r9/docs/stories/karen/songs/coup-cue-r1/writers/percussion-and-low-brass.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "percussion-and-low-brass". Reply with just the two paths.