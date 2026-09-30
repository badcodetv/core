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
| **4 — the simulation** | Five years later: the fake bright Swindon, the glitch, the wreck, the bot | `scenes/simulation.md` | `gpom-sim-happy` · `gpom-sim-sad` (both clarinet, joined in Premiere with a glitch SFX) · `gpom-sim-bot` (robot voice + Disney springtime tune in one take, drafted, not run) | ✅ happy + sad PICKED 2026-09-30 (r67: `63ce479c`, `fca1ede9`, recorded to `clips/simulation/audio/`); robot take drafted; on the timeline in gpom-s01 A4 166.0 + A5 188.375 |

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

## Scene 4 — the simulation · ✅ happy + sad picked (r67) · bot pieces to do

**What it is.** Five years after Swindon. We cut into a bright, perfect Swindon high street and
the narrator is showing it off. It glitches: the same street, wrecked, vape and betting shops
gutted. The narrator deflates. The picture pauses, and a small delivery robot with bunting on its
wheel rolls up and talks to us. Picture: [`scenes/simulation.md`](../scenes/simulation.md).

**Kai, 2026-09-30 (after hearing r65): back to two parts, one instrument.** One take could not
turn hard enough. So: a **happy** part and a **sad** part, both on **harp**, joined in Premiere
with a glitch sound effect over the cut. Keep the optimistic delivery of "Oh, look at this…
I've outdone myself", which already works. **"Oh, fuck" is out**: the sad part is deflated, not
shocked (*"Oh no… it never works… my simulations just don't replace humans"*), plus a line or two
in the spirit of **Marvin**, the depressed robot in *The Hitchhiker's Guide*. The Marvin lines
state facts about the fakes and never name a feeling (rule 11: the AI's emotions are outside-in).
The robot's "he misses you" stays the only named feeling.

| Piece | Music | Voice | Where it goes |
| --- | --- | --- | --- |
| **Happy** | bright, sunny solo harp | the narrator, optimistic, showing off | over the fake world; cut mid-word on "myself" at the glitch |
| (glitch) | a sound effect, not Suno | — | over the cut |
| **Sad** | slow, sad solo harp | the narrator, deflated, Marvin-weary | over the wreck, then the pause |
| **C** | Disney springtime, Bambi-like | none (instrumental) | under the bot |
| **D** | — | the bot, **not Suno**: Google AI Studio, a warm West Country voice | see "The bot's voice" below |
| **Oi** | — | the narrator | trimmed from an r64 B take, placed after the bot |

**Settings:** the house settings above, **Duration 20** (happy) and **25** (sad), weirdness 25.
Exclude drops "strings" (the harp is one) and keeps violins and orchestra out.

### `gpom-sim-happy` — scene 4, the fake world · r4

**Kai, 2026-09-30:** words rewritten by Kai (frozen); clarinet, not harp — *uplifting, not overtly
happy*. Words first, style later. Cues by Claude: he is a showman unveiling his fake world and
fishing for praise.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background music mixed far back: one warm, gently uplifting solo clarinet, hopeful and light but understated, never jolly. His delivery follows the cues: proud, savouring, fishing for praise, then quietly smug. Close-mic'd and dry, his voice loud and right at the front of the mix, the clarinet always well behind him. No drums at all. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, violins, orchestra, cinematic, synth, drum kit, drum machine, breakbeat, robotic voice, text to speech, laughing, ad-lib, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Intro | gentle uplifting clarinet | warm, proud, unveiling it]
Oh, look at this.

[clarinet | savouring each one, a slow smile]
Flowers...
Sunshine...

[clarinet lifts | beaming]
Everyone in work!

[clarinet | leaning in, fishing for praise]
Isn't it wonderful?

[clarinet | a modest pause, then smug]
Honestly...
I've outdone myself.
[End]
```

### `gpom-sim-sad` — scene 4, the wreck · r4

**Kai, 2026-09-30:** words rewritten by Kai (frozen); clarinet. Cues by Claude: the truth lands,
there is nothing in it, and he goes from a sigh to hollow to a childish sulk. *"I just can't feel
anything"* disowns the inside, which rule 11 allows; "simulation theory" is named only to bin it.

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

[sparse clarinet | quiet, hollow, almost to himself]
I just can't feel anything.

[clarinet | bitter, sarcastic]
So much for simulation theory!

[clarinet fading | sulky, muttering, childish]
Stupid boring computers.
[End]
```

### `gpom-sim-bot` — scene 4, the robot talks, over its springtime tune · r1

**Kai, 2026-09-30:** narrate the robot in Suno. It is one voice alone in its own take, so the
"two voices in one take" problem does not apply; the **accent** is the risk (Suno does not reliably
summon one, `docs/suno-gpt/suno-voices.md` Thread 5). **No saved Voice**: the newsreader Voice would
make the robot sound like the narrator. The Disney springtime tune (was piece C) rides under it in
the same take, like the narrator's scenes. **Kai, same day: female, sarcastic, northern**, to counter the dark, gravelly newsreader (was warm West Country). Fallback if the accent won't come: AI Studio's accent
filter (piece D below). Words: Claude's, cut from the earlier draft. "So much for simulation theory"
moved to the narrator, so it is gone here. New callback: *"Says he can't feel anything. He misses
you."*, the robot contradicting the narrator's "I just can't feel anything" (rule 11: the feeling
is attributed from outside).

Style:

```
Spoken word, one voice talking straight to the listener. A small delivery robot with a young woman's voice and a broad Northern English accent, Yorkshire or Lancashire, flat vowels, dry, sarcastic and deadpan, rolling her eyes at him, unimpressed but fond underneath. A natural, human, characterful voice, never robotic. Underneath, quiet background music mixed far back: a sweet Disney-style springtime woodland tune, like Bambi, light flute, pizzicato and glockenspiel, soft and innocent. Close-mic'd and dry, the voice loud and right at the front of the mix. No drums. She speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, choir, rap, autotune, robotic voice, vocoder, text to speech, newsreader, received pronunciation, posh, American accent, male vocals, deep voice, gravelly, drums, synth, epic, cinematic, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Intro | sweet springtime flute | dry, sarcastic, rolling her eyes]
Is he banging on again?

[soft pizzicato | deadpan, unimpressed, telling tales on him]
Sorry about him. He gets like this.
He built that nice one after you lot went.
Trouble is, there's nobody in it.
It's just him, doing all the voices.

[music softens | the sarcasm drops, quiet, fond, a secret]
Says he can't feel anything.
He misses you.

[bright again, quick | dry again, cut off mid-word]
He'd never say, mind—
[End]
```

**Settings:** house settings, **no Voice**, Vocal Gender **female**, Duration 30, weirdness 25.

### The bot's voice (piece D) — not Suno

**Route:** Google AI Studio's voice library (`docs/ai-studio/README.md`), filtered by accent for a
**warm West Country** voice. Its browser blocks automation, so a human types it in. Words (draft):

```
Is he banging on again?

Sorry about him. He gets like this.
He built that nice one after you lot went. Trouble is, there's nobody in it.
It's just him, doing all the voices.
So much for the universe being a simulation, eh?

He misses you.
He'd never say, mind—
```

**Voice direction:** friendly, chatty, a bit of a gossip, leaning in to tell you something it
shouldn't; quick and bright at the start, softer on "He misses you."; cut off mid-word at the end.

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
