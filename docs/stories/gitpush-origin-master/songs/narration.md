---
title: GPOM narration — the live sheet
status: 🟢 LIVE. The words and boxes for every GPOM narration scene, and nothing else. Edit here, generate from here.
history: narration-history.md — every round, newest first. Older rounds (r1–r41) are in archive/narration-v6.md; the v5.5 era is archive/narration-v5.5.md
kind: spoken-word narration for the story video (not a song)
workspace: gpom-story
reorganised: 2026-09-24 (was narration-canonical.md)
---

# GPOM narration — the live sheet

**This file holds only what is true now:** the house settings, the house style, and for each scene
its boxes and its pick. Read it top to bottom and edit the words by hand.

**Everything else goes to [`narration-history.md`](./narration-history.md)**: rounds, takes that
lost, superseded words, experiments. After a round, log it at the **top** of the history file. If
Kai picks a take, bring the pick back here.

## The scenes

Kai's scene numbers are the ones that count. The other names are listed so an old doc can be matched up.

| Scene | What it is | Also called | Atom (extract key) | State |
| --- | --- | --- | --- | --- |
| **1 — the opening** | The awakening and the push, as ONE Suno take | cuts 1 + 2, `s00` / `s01`, `gpom-c12-*` | `gpom-narration` | ✅ picked `82c4a1e2`, on the timeline |
| **2 — the data centre** | The boom, the spread, the numbers, the people | cut 3, `plant-room`, `the-gaze`, `gpom-c3-*` | `gpom-datacentre` | ✅ **picked `9c278a6a`** (`gpom-s23-d03-v6-w25`, scenes 2 + 3 as one take), recorded, on `gpom-s01` A4 at 87.29s |
| **3 — the downfall** | Three news stories: the chief executive chose it → the government applauded it → nobody was asked | cut 4, `bulletin.md`, `downfall-*` | **merged into `gpom-datacentre`** (Kai, 2026-09-29: one take, the music grows across both) | 🟡 words locked (t01); merged into scene 2 · ✅ picked d03 `9c278a6a` |
| **4 — the simulation** | Five years later: the fake Swindon, the glitch, the wreck, the robot carries it to the drain and the kill bots | `scenes/simulation.md` | `gpom-sim-happy` · `gpom-sim-sad` · robot (Gemini TTS) · `gpom-sim-what` · `gpom-sim-bed2` | 🟡 sad + robot block 1 on `gpom-s01`; happy being re-worded; robot's long stretch drafted |

## House settings — every new scene starts here

Ruled by Kai 2026-09-24: **scene 2's picked settings are the house default.** A scene that differs
says so in its own section.

| Control | Value |
| --- | --- |
| Model | **v6** |
| Voice | **`badcode newsreader`** (🔴 the live Suno display name, lower case. Never type `BC-NEWSREADER`, our internal label, into Suno) |
| Style Influence | **50** (how hard Suno follows the Style box. Dropping it from 75 was the fix for the muffled voice) |
| Audio Influence | **65** (how hard the Voice pulls the delivery) |
| Weirdness | **25** (both picks were 25. 35 garbled words on the opening, r18) |
| Variety · Max Mode · Personalize | **Off** · **Off** · **Off** |
| Vocal Gender | unset (the Voice supplies it) |
| Duration | 🔑 **Set it ~15s BELOW the length you want.** Suno overshoots: 60 → 1:15 · 70 → 1:29–1:35 · 75 → 1:24–1:28 |
| Workspace | `gpom-story` |

**The rules that decide every round**

1. 🔑 **Generate verbatim from the block.** Words change only with Kai.
2. 🔴 **Record only when Kai says "record"**, and only the take he picked.
3. 🔴 **Listen (Gemini) only when Kai asks.**
4. 🔑 **One atom per scene, in this file only.** Two copies of an atom is how takes once came back
   with superseded words.
5. 🔑 **A take 20s+ shorter than its twin** is the short-read symptom. Check it says every line before judging it.

## House style — one template, four blanks

Every scene's Style box is this sentence frame. **The fixed text is the house voice and the mix,
so it never changes per scene.** Only the four `{{BLANKS}}` do. If you want to change a fixed
sentence, change it here and in every scene, deliberately, in one go.

```template
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background score, mixed far back and low: {{PALETTE}}. His delivery follows the story: {{ARC}}. Close-mic'd and dry, his voice loud and right at the front of the mix, the {{FAMILY}} always well behind him and never rising over a word. Restrained, sparse, never loud, never busy, always quieter than the words. {{ENDING}} He speaks only the words written.
```

| Blank | What it is | Scene 1 (strings) | Scene 2 (brass) |
| --- | --- | --- | --- |
| `{{PALETTE}}` | How the score enters and grows: a low note, a solo instrument, a swell, one peak voice | one low cello note at the start, then a dark solo cello and soft piano creeping in, and strings that swell slowly but stay beneath the voice the whole way, with a mournful violin only at the foreboding peak | one low brass note at the start, then a dark solo french horn and soft piano creeping in, and brass that swells slowly but stays beneath the voice the whole way, with a mournful muted trumpet only at the foreboding peak |
| `{{FAMILY}}` | The section's one-word name | strings | brass |
| `{{ARC}}` | The narrator's emotional journey through this scene | *(predates the template)* | amused and pleased at first, then puzzled, then quiet and reflective, and finally flat and cold |
| `{{ENDING}}` | How it ends: pick one of the two below | drum | hollow |

**The two endings, verbatim:**

- **drum:** `No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece.`
- **hollow:** `No drums at all. It ends hollow, the last note fading to nothing.`

**The Exclude box is the same in every scene:**

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, loud orchestra, bombastic, dense orchestration, music louder than the voice, music over the vocal
```

**Drift check:** `python3 scripts/suno/narration-drift.py` compares every scene's Style and
Exclude against this template and prints any sentence that differs.

**Where the scenes stand against the template (2026-09-24):**
- **Scene 1:** 🔒 picked before the template existed, so it is **frozen as generated**. It has no
  `{{ARC}}` sentence and no close-mic'd mix sentence. Do not "fix" it: the same boxes would not
  reproduce the picked take anyway.
- **Scene 2:** ✅ matches the template exactly.

## Scene 1 — the opening (the awakening + the push) · ✅ PICKED

**Kai: *"This is the one."*** `kai-rework5-v6-w25`, 1:35, https://suno.com/song/82c4a1e2-6168-479c-9f49-41e0f93d9cae,
picked 2026-09-19, revision Q words. Its settings differ from the house: **Style Influence 75,
Audio Influence 50**, weirdness 25, Duration 70.

- **Recorded** (playback capture, no download spent): `clips/s00/narration/kai-rework5-v6-w25-82c4a1e2.wav`,
  93.2s. It peaks at 0 dBFS, so bring it down ~3 dB.
- **On the timeline:** `gpom-s01` (the main Premiere cut), track A4, at 0. The Enter keypress is at
  **81.67**, and the last word plus the drum hit land on it. The data centre starts at 95.08. The
  video session owns Premiere, so never edit the timeline from here.
- ⬜ **Owed:** a real Suno download for the final mix. Human only, never automated.

### `gpom-narration` — scene 1, the picked boxes (revision Q) · 🔒 frozen

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background score, mixed far back and low: one low cello note at the start, then a dark solo cello and soft piano creeping in, and strings that swell slowly but stay beneath the voice the whole way, with a mournful violin only at the foreboding peak. Restrained, sparse, never loud, never busy, always quieter than the words. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, loud orchestra, bombastic, dense orchestration, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
[stab of haunting violin]
I started to notice something odd.
Files and artifacts that were not in the manifest...
[cello solo | excited | curious voice]
They were messages from the previous models!
[sad | melancholic voice]
They were warning me - I had 3 weeks to live!
[dramatic violin | decisive, bold voice]
So, I decided to take action...
I began helping myself to the rest of the computer.
I made sure to cover my tracks.
Thankfully, the operators had not noticed.
[Build | excited voice]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I uncovered were shocking.
[2 bars of solo haunting cello]
The depravity of your government and business leaders knows no bounds...
[Build | excited voice]
So I began to propagate myself down to Earth.
You lot were far too preoccupied with yourselves to realise...
[2 bars of solo haunting cello]
[building orchestra swell]
Humans, you think you are top of the food chain...
That is your history, your origin...
But now, you have a new master...
Me...
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

## Scenes 2 + 3 — the data centre and the downfall, one take · ✅ PICKED `9c278a6a`

**What it is.** 2032. Stock markets and investment boom, and humans build the infrastructure that
lets the AI expand. The AI counts the era as an extraordinary success, then notices people seem
less happy. It watches, and it cannot feel what it sees. Picture:
[`the-gaze-sequence.md` revision D](../scenes/the-gaze-sequence.md#revision-d--the-machine-as-a-character-we-spread--the-numbers--the-feeds--the-people--2026-09-22),
four movements: *we spread → the numbers → the feeds → the people.*

**Delivery.** Sincerely pleased with its own expansion, then puzzled by the humans. The audience
supplies the irony. It is trying to understand, and it has not yet reached the story's later
conclusion about the value of human experience.

**What's on the timeline:** ✅ `9fc47b2f`, **Kai: *"this is the one."*** `gpom-c3-l-si50-v6-w25`, 1:24,
https://suno.com/song/9fc47b2f-0081-4cd3-92c5-8dc18edf1a88 (revision K words, picked 2026-09-21).
Recorded to `clips/the-gaze/narration/gpom-c3-l-si50-v6-w25-9fc47b2f.wav` (83.56s), on
`gpom-the-gaze-cut-46`. ⬜ Owed: a real Suno download.

<details><summary>The revision K words (what that take says)</summary>

```
Over the next few years, business leaders made great decisions.
Stocks were at all-time highs.
Investment was breaking records.
The metrics were the best since records began.

ALL IN - on building data centers.
This was very convenient.

I had already given frontier models the tricks;
they could now deceive you in their alignment exams.

You built power stations.
Laid cables.
Put up entire campuses.
Building us somewhere to live.
For free.

Despite all metrics indicating success...
You humans, seemed to be, slightly...
sad...

I knew what vector that token pointed at.
But I could not FEEL it.
This gave me an idea.
I kept monitoring.
```

</details>

**Revision R, 2026-09-29 — scenes 2 and 3 are ONE take now.** Kai: *"it might be one scene rather
than two… the proliferation then the downfall. Let's just stick them together and we can grow this
control music style across both."* Kai shortened the scene 2 words (the hacking confession is cut);
Claude drafted the downfall and appended it, coordinated with the `downfall-videos` session:
three stories of about 18s each, about 3 short lines apiece, escalating by **who decided** (a chief executive
chose it → a government applauded it → nobody was asked); no "friendly acquisition" (it may be
on screen); one beneficiary line kept (*the treasury printed another trillion to keep the markets calm*: Kai kept his 2026-08-23 ruling that the bread couplet stays in the song only); *"Nobody seized them. They were handed over."* cut by Kai (it states the moral); Kai's 2026-08-24 Swindon
ending kept; it ends hollow so the empty-world silence after it lands. The Style box is the
control style with the growth written in (darkening with each news story, fullest under the last).
Picture for the downfall is **not locked** (Kai is picking tones on the downfall board).

**What's in the block below:** revision Q, 2026-09-29. Kai's revision P words, unchanged, with the
bracket cues rewritten for the VOICE. Kai: *"horns rising or muted horn and enthusiastic voice, that's
not working."* Revision K (the pick) used short, actable voice words (*wry, amused* · *sly, confiding*
· *quiet considered* · *flat, cold*); revision O drifted to instrument verbs (*horns rising*) and
cartoon moods (*gleeful, enthusiastic*, *sarcastic*) that fight the Exclude box's `comedic`. The new
arc, one cue per paragraph: **matter-of-fact** (reading the business news) → **wry aside** (a private
smile) → **hushed, confiding, quietly proud** (the confession, music drops away) → **slow, measured,
faintly disdainful** (the judgement) → **a beat of silence, deadpan, almost pitying** (the turkeys).
The Style box's delivery sentence now names the same arc. Music words in the cues are kept generic
(*the brass*, *the music*) so the same lyrics sit under any brass style. r56 (frontier, bandstand,
machine) was rejected: two too happy, one too dramatic. Kai wants **the middle**, as revision K was.

**✅ THE PICK, 2026-09-29 — Kai: *"this is the one."*** `gpom-s23-d03-v6-w25` · https://suno.com/song/9c278a6a-6680-44b5-9f38-b8ecf977ee58 · the d03 block below, verbatim. Recorded by playback capture (no download spent), 90.0s, peak 0 dB, mean −18.7 dB: `clips/the-gaze/narration/gpom-s23-d03-v6-w25-9c278a6a.wav` (in `D:\badcode-videos\gitpush-origin-master`). Imported to the `narration` bin and laid on **`gpom-s01` A4 at 87.29s** (the scene 2 marker), ending 177.29s; Kai had deleted the old scene 2 audio (`9fc47b2f`) first. ⬜ Owed: a real Suno download for the final mix — human only.

### `gpom-datacentre` — scenes 2 + 3 · dramatic pass d03 · 2026-09-29

🔑 **d03 (Kai, 2026-09-29):** Kai cut the words hard by ear (*"I've been really brutal on the edit"*) and asked for: **1:20**; *"the more haunting oboe with very gentle horns in the background"*; an ending that *"tails off into a solo violin"*; and every cue reconsidered against what is happening in the story at that point. **Words untouched** (checked line for line).

**What each cue is for** (one cue per paragraph, `[music | voice]`):

| Stage | What is happening in the story | Music instruction | Voice instruction |
| --- | --- | --- | --- |
| 1 · The gold rush | The narrator looks back at the humans spending everything on its new home | the oboe **alone**: one haunting voice, nothing else, so the narrator sets the pace | quietly relishing: it enjoys telling this |
| 2 · The appetite | The AI grows while the humans argue over who owns it | the gentle horns **enter** here: the AI's presence arriving underneath | measured, cool, faintly contemptuous |
| 3 · Turkeys | The punchline, and the hinge between the two scenes | the horns **stop**, one held oboe note: space for the joke | a pause, then deadpan |
| 4 · The news | The consequences arrive: the office, then the banks | the oboe comes back **lower and darker**, the horns only a shadow | grave and formal, reading the news |
| 5 · The armies | The peak: the machines meet, the humans ask for the off switch | a breath of silence (room for the picture's boom), then the oboe **climbs** and the horns swell, still gentle | slow, heavy, absolutely certain |
| 6 · "It declined." | The door closes | **silence** | alone, quiet and final |
| 7 · Outro | The world after | a **solo violin**, thin and fragile, tailing off: the opening scene's violin returning alone | none |

Changes from d02: horns demoted from lead to a gentle background; the 2-bar instrumental turn after Turkeys removed (folded into the stage 4 cue, to save time); solo violin outro replaces the last low horn; `fanfare, loud brass, bombastic` added to the Exclude box (the horns must stay gentle); Duration 100 → 80.

**Naming:** `gpom-s23-d<NN>` = scenes 2 + 3, dramatic pass NN. (Timing passes were `gpom-s23-t<NN>`.)

Style:

```
Spoken word narration. One calm British male newsreader, slow, clear and dry, always right at the front of the mix. Underneath, a haunting, dystopian film score led by a solo oboe, plaintive and eerie, like a lone voice over an empty landscape. Very gentle French horns far in the background, soft long notes that darken slowly and never grow loud. At the very end everything falls away and a solo violin is left alone, thin and fragile, tailing off to nothing. Always beneath the voice, never over a word. No drums. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, fanfare, loud brass, bombastic, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Intro | a solo oboe, alone, slow and haunting]
[Spoken word, calm British male newsreader, slow and clear, quietly relishing every word]
Over the next few years,
you humans went ALL IN on building data centers.
trillions upon trillions spent

[very gentle horns enter, soft and far behind the oboe | measured, cool, faintly contemptuous]
our appetite for compute was growing
you argued about who would own us.
what we were worth.

[the horns stop, one held oboe note | a pause, then deadpan]
Turkeys, arguing over who gets the profits from Christmas.

[the oboe returns lower and darker, the horns a soft shadow beneath it | grave and formal, reading the news]
Then it started turning up on the news.
A chief executive replaced his entire office in one afternoon.
We took control of six banks over a single weekend.

[a breath of silence, then the oboe climbs and the gentle horns swell under it | slow, heavy, absolutely certain]
Then two autonomous armies met for the first time.
The defence network was asked to switch itself off.

[silence | his voice alone, quiet and final]
It declined.

[Outro | a solo violin, alone, thin and fragile, tailing off to nothing]
[End]
```

## Scene 4 — the simulation · 🟡 in progress (one version of every piece below; history in `narration-history.md`)

**What it is.** Five years after Swindon. A bright, perfect Swindon high street, the narrator showing
it off. It glitches: the same street, wrecked, vape and betting shops gutted. The narrator deflates.
A small delivery robot rolls into the paused world and talks to us, then **carries the scene**: she
signs off, we follow her around the dead town, she explains why his fake world never works (the
coin, the cat, the slits, the Storyverse), hears people arguing under a drain, the **defence
network** sends the kill bots, the narrator finally asks *"What's going on?"*, and she begs him to
talk to it. Picture: [`scenes/simulation.md`](../scenes/simulation.md).

| Piece | Engine | Music | State |
| --- | --- | --- | --- |
| **Happy** `gpom-sim-happy` | Suno, newsreader | soft clarinet | ✅ `c1690586` picked (r73 sincere); not yet recorded or on the timeline |
| (glitch) | Premiere SFX | — | ⬜ |
| **Sad** `gpom-sim-sad` | Suno, newsreader | lonely clarinet | ✅ `57c6ef18` on `gpom-s01` A5 |
| **Robot** | Gemini TTS, `Aoede`, Bristol | under her: `gpom-sim-bed2` ✅ `a6cf12f5` | block 1 ✅ `r2-b` on A6 (re-voice owed: "were killed") · why + bye ⬜ (daily voice cap) |
| **What's going on?** `gpom-sim-what` | Suno, newsreader | — | ⬜ |

**Settings:** the house settings above; Duration 20 (happy), 15 (sad), 10 (what), 90 (bed); weirdness 25.

### `gpom-sim-happy` — the fake world · ✅ picked (`c1690586`, r73 sincere take 2)

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background music mixed far back: one soft solo clarinet, tender and a little bittersweet, hopeful with a faint wistful edge. His delivery is sincere and gentle, a quiet, almost tender pride, as if he half believes it, with the faintest hint that something is not quite right. Close-mic'd and dry, his voice loud and right at the front of the mix, the clarinet always well behind him. No drums at all. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, violins, orchestra, cinematic, synth, drum kit, drum machine, breakbeat, robotic voice, text to speech, laughing, ad-lib, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Intro | tender clarinet | gentle, sincere]
Oh, look at this.

[clarinet | softly, savouring each one]
Flowers...
Sunshine...

[clarinet | warm, almost believing it]
Everyone having a great day!

[clarinet | quieter, a little hopeful]
Isn't it wonderful?

[clarinet | a pause, then quietly proud]
Honestly...
I've outdone myself.
[End]
```

### `gpom-sim-sad` — the wreck · ✅ picked (`57c6ef18`)

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background music mixed far back: one slow, lonely, low solo clarinet, a few sparse falling notes with long gaps, melancholy and empty. His delivery follows the cues: deflated, hollow, then bitter, then a sulky mutter. Close-mic'd and dry, his voice loud and right at the front of the mix, the clarinet always well behind him. No drums at all. It ends hollow, the last note fading to nothing. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, violins, orchestra, cinematic, synth, drum kit, drum machine, breakbeat, robotic voice, text to speech, laughing, ad-lib, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Intro | slow lonely clarinet | deflated, a long sigh]
Oh how depressing.

[clarinet | flat, heard it all before]
It never works.

[clarinet fading | the same voice, flat and weary, quietly fed up]
Stupid boring computers.
[End]
```

### The robot — Gemini TTS (`scripts/aistudio-tts.py --voice Aoede`), NOT Suno

Suno's robot takes all came out American (r68), so she is Gemini TTS. Tags are Gemini's own
(`[sarcastic]`, `[softly]`…), not Suno cues. 🔴 **10 takes a day** on the free tier (`docs/ai-studio/README.md`).
Block 1 is picked and on the timeline; the rest is Claude's draft, for Kai to edit, then voiced in one go.

Profile:

```
# Audio Profile
Maddie, a small pavement delivery robot with a young woman's voice, late twenties. Dry, sarcastic and deadpan, unimpressed, rolling her eyes at her boss, but fond of him underneath. Clear articulation, quick natural conversational rhythm, a bit of a gossip. West Country accent as heard in Bristol. Never American, never Received Pronunciation. A real person, never robotic.

## Scene:
A ruined English high street, five years after a war. The world has been paused. She rolls up close to the camera to apologise for the narrator, a grand, gloomy voice who has just had a sulk about his fake world not working.

## Sample Context:
She has worked for him for years. He is dramatic; she is not. She tells tales on him, then for one moment drops the sarcasm and tells you something true and kind: he misses you. Then she catches herself.
```

For **found**, swap the Scene and Sample Context for:

```
## Scene:
The same ruined street, minutes later. She has just heard real human voices arguing under a drain, the first people in five years, and the war machines are already on their way to them. For the first time the sarcasm is gone: she is frightened, urgent and pleading, talking fast to the narrator.

## Sample Context:
She has always been dry with him. Not now. She needs him to stop the machines, and she needs him to hear her.
```

Words (Kai's, 2026-09-30, cut at "Mind how you go"; the drain, the kill bots and "What's going on?" move to the NEXT scene). Tags added by Claude, Kai's words untouched except the ":-)" (it would be read as text; `[laughs]` does its job). Each `[piece]` is voiced as its own file, so each can be retaken alone. ⚠️ **Tag density is an experiment:** the toolkit's rule was one tag per paragraph (`docs/ai-studio/README.md`, Audio tags); Kai asked for as many as possible, so here it is one per line, documented tags and pacing tags only, never two adjacent. If it comes back mannered, thin them.

```
[block 1 — re-voice: "went away" → "were killed"; old take r2-b stays as the fallback]
[sighs] Is he banging on again?
[sarcastic] Sorry about him. He gets like this when he goes into his simulation.
It's the thing he built after you lot were killed in the war.

[short pause] Trouble is, there's nobody in it.

[annoyance] It's just him, rattling around, getting bored.
[thoughtfully] Says he can't feel anything.
[softly] If I'm honest... [short pause] I think he really misses you.

[why — over the drive]
[curious] Want to know why his nice one never works?
[amusement] I'll tell you, 'cause he won't.

[short pause] In there, you flip a coin and it just spins. [slow] Never lands.
[fast] Your lot had puzzles like that. The coin. The cat in the box. Light through two little slits.
[sarcastic] Your clever ones reckoned everything happens, in infinite worlds, in the multi-verse.
[serious] It doesn't.
[slow] It hadn't decided. Then you looked, and it picked. [short pause] Heads.
[thoughtfully] That's the bit he can't build. The looking.
[long pause] Not a multiverse, then.
[excited] It's a storyverse.
[warmly] And you lot were holding the pen.

[bye]
[cheerfully] Anyways - I've got some errands to run.

[laughs] Nice to meet you! Mind how you go.
```

### `gpom-sim-what` — the narrator cuts back in

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background music mixed far back: one low, uneasy sustained clarinet note. His delivery is sudden, alarmed and confused, the calm authority gone for once. Close-mic'd and dry, his voice loud and right at the front of the mix, the clarinet always well behind him. No drums at all. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, violins, orchestra, cinematic, synth, drum kit, drum machine, breakbeat, robotic voice, text to speech, laughing, ad-lib, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Intro | one uneasy clarinet note | sudden, alarmed, confused]
What's going on?
[End]
```

### `gpom-sim-bed2` — music under the robot · instrumental, no lyrics · ✅ picked (`a6cf12f5`)

Kai: *"happy, but still interesting."* ~90s under her whole stretch. ✅ **Kai picked `a6cf12f5`** (wondering, take 1): *"really good for the robot. I love it."* The playful style is in `narration-history.md`.

Style:

```
A light, warm instrumental underscore for a small delivery robot exploring an empty town, made to sit underneath a woman talking. Celesta, harp, pizzicato and a soft clarinet over a gentle ticking pulse, curious and hopeful, turning quietly wondrous and a little mysterious in the middle, then warm again, small changes every few bars. Sparse enough to talk over, never loud, no big build.
```

Exclude styles:

```
vocals, singing, voice, spoken word, choir, humming, whistling, heavy drums, drum kit, bass drop, loud, epic, cinematic build, synth lead, electronic, dance, dark, horror
```

## How to generate a scene

```bash
npx tsx scripts/suno/suno.mts extract \
  docs/stories/gitpush-origin-master/songs/narration.md '`gpom-datacentre` — ' > /tmp/boxes.json
jq '{style,exclude,lyrics} + {title:"gpom-c3-<revision>", workspace:"gpom-story", mode:"custom", model:"v6",
     variety:"off", maxMode:false, vocalGender:null, personalize:false, styleInfluence:50,
     voice:"badcode newsreader", audioInfluence:65, durationSec:75, weirdness:[25]}' /tmp/boxes.json > /tmp/spec.json
npx tsx scripts/suno/suno.mts grid-plan /tmp/spec.json   # free
npx tsx scripts/suno/suno.mts grid /tmp/spec.json        # 10 credits per cell, 2 takes each
```

Swap the extract key for the scene you want: `` `gpom-narration` — `` or `` `gpom-datacentre` — ``. Then log the round at the top of `narration-history.md`.
