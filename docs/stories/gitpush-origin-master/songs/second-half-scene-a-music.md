---
title: GPOM second half, scene A (kill bots): the boss's lines + the music
status: 🟡 round 1 generated, unheard. Picks owed (Kai)
kind: one narrator take (the boss, dry) + two instrumental cues (P the patrol, C the chase and the call)
model: v6
workspace: gpom-story
scene: docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/
created: 2026-10-21
---

# GPOM second half, scene A: the boss's lines and the music

Scene A is the kill bots. They roam, the HUD hears a muffled human argument, kill mode, they race
to the bunker while Maddie phones her boss (the narrator, "the AI"), and they stand down when he
uses his exploit. This sheet holds the three things Suno makes for it:

| Atom | What | Engine | Duration |
| --- | --- | --- | --- |
| `gpom-sh-a-boss` | the boss's four lines, one take, cut apart in the edit | Suno, Voice `badcode newsreader` | 40 |
| `gpom-sh-a-P1` / `gpom-sh-a-P2` | cue P, **the patrol**: roaming → the muffled argument → kill mode | Suno, instrumental | 45 |
| `gpom-sh-a-C1` / `gpom-sh-a-C2` | cue C, **the chase and the call**: racing to the bunker under Maddie's call → stand down | Suno, instrumental | 60 |

**Kai's brief for the music (2026-10-21):** *"more sparse orchestra, solo violin, cello… not
Beethoven's 5th, more Chopin."* Intimate, NOT action-movie. Tension by silence, not drums.

**Rules in force:** generate verbatim from the blocks; Personalize off; Variety Off; record only
when Kai says "record"; listen only when Kai asks; never download. Each cue's two atoms are written
**bold, not meek** (different instruments, different room, different mix, per-variation excludes
that ban the other atom's sound).

## Settings

| Control | Boss (`gpom-sh-a-boss`) | Music (P1 P2 C1 C2) |
| --- | --- | --- |
| Model | v6 | v6 |
| Voice | **`badcode newsreader`** (the AI, Kai insists on this exact voice) | none (detached) |
| Style Influence | 50 (house) | 75 (the pair rule) |
| Audio Influence | 65 (house) | n/a |
| Weirdness | **pair: 25 (house) and 10** (lower, for word fidelity on a dry read; 35 garbled words before) | **pair: 30 and 60** |
| Variety · Max Mode · Personalize | Off · Off · Off | Off · Off · Off |
| Vocal Gender | unset (the Voice supplies it) | unset |
| Duration | 40 | P 45 · C 60 |
| Workspace | `gpom-story` | `gpom-story` |

**Why Songs + Voice and not Speech (beta):** Speech is untested here (`suno-v6.md` §1b, §12 test
0), has no saved Voice, and Suno's own warning is a British accent drifting Australian. Kai's
narrator is the saved Voice, which only the Songs form takes. So the boss goes through the house
path with a style that asks for no music at all. Suno cannot make true silence; expect a little
room or a faint bed, and plan to cut lines apart in the edit.

### `gpom-sh-a-boss` — the boss's lines, as dry as Suno allows

Style:

```
Spoken word narration, voice only. One calm British male voice, a newsreader, unhurried and wry, speaking privately on a phone call. No music at all: no score, no bed, no instruments, only his voice and quiet silence between the lines. His delivery follows the cues: mildly amused, then quietly surprised, then calm and firm, then relieved and wry. Close-mic'd in a dead, dry voiceover booth, no reverb, his voice loud and right at the front. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, mildly amused]
Maddie, are you making fun of my simulations again?

[Spoken, quiet surprise]
Oh. ... Oh, wow. ... And they've activated their firewalls.

[Spoken, calm, firm]
No. I've got it.

[Spoken, relieved, wry]
Phew. Glad I kept that little exploit up my sleeve.
[End]
```

## Cue P — the patrol (~45 s)

Under the kill bots roaming, the HUD hearing a muffled human argument, then kill mode. Eerie and
lonely: held cello, sparse piano, a thin violin line, tension by silence not drums.

### `gpom-sh-a-P1` — solo cello + felt piano nocturne (dry, close, wooden room)

Style:

```
A lonely nocturne for solo cello and felt piano, eerie and very slow, free rubato time. One low cello note is held in an empty room, a few soft piano notes fall into long silences, then a thin, high violin line drifts in from far away, barely there. All the tension comes from silence and space; nothing ever lands on a beat. Recorded close and intimate in a small dry wooden room, you hear the bow hair and the felt hammers. Near the end the cello sinks into a low, uneasy tremolo that never resolves.
```

Exclude styles:

```
vocals, singing, voice, choir, humming, drums, drum kit, percussion, timpani, beat, pulse, groove, string quartet, string section, full orchestra, pizzicato, brass, horns, woodwinds, harp, synth, electronic, pad, reverb wash, epic, heroic, action, trailer, bombastic, major key, happy
```

### `gpom-sh-a-P2` — string quartet, cold harmonics, lone violin (distant, stone hall)

Style:

```
Chamber string quartet playing sul ponticello and glassy harmonics, cold, hollow and unsettling. Viola and cello sustain one quiet, unresolved chord that barely moves while a lone first violin searches above it in thin, broken phrases with long held breaths between. The players seem to hold their breath: pianissimo throughout, a hush down to almost nothing, then one sharp dissonant swell at the very end that cuts off. Captured from the back of a large cold stone hall, distant, wide and reverberant.
```

Exclude styles:

```
vocals, singing, choir, piano, keys, felt piano, drums, percussion, timpani, beat, groove, pulse, brass, horns, woodwinds, synth, electronic, full orchestra, solo cello nocturne, warm, romantic, lush, epic, action, heroic, trailer, major key
```

## Cue C — the chase and the call (~60 s)

Kill bots racing to the bunker while Maddie phones her boss, ending when they stand down. Restless
but intimate: pizzicato and solo cello pulse, a solo violin that climbs, piano, quiet urgency, no
percussion kit, resolves softly at the end.

### `gpom-sh-a-C1` — pizzicato quartet, climbing violin (crisp, close, small ensemble)

Style:

```
Restless chamber music for string quartet and a little piano. Plucked pizzicato cello and viola pulse like a quick, nervous heartbeat, light on their feet, while a solo violin starts low and climbs phrase by phrase, higher and more urgent; soft piano chords punctuate the gaps. Quiet urgency, all made by strings and hands, never loud. In the last stretch the plucking slows, the violin settles onto one long tender note and the piece resolves softly into a warm, still major chord. Crisp, close and detailed, like a small ensemble playing in a living room.
```

Exclude styles:

```
vocals, singing, choir, drum kit, drums, snare, percussion, timpani, beat, electronic, synth, bass drop, brass, horns, full orchestra, string section, rubato nocturne, piano solo, epic, action, trailer, bombastic, heroic, dramatic, dark ambient
```

### `gpom-sh-a-C2` — Chopin-like piano étude with solo cello (warm parlour, rubato)

Style:

```
Romantic solo piano in the manner of a Chopin étude, agitated and fluid: a running left-hand figure in a minor key, breathless and restless, with a singing solo cello answering the piano's melody. One piano and one cello in a warm parlour, rubato, rising and falling in waves of quiet urgency, never pounding. A solo violin joins only near the end, climbing above the cello. Then the running figure dissolves, the tempo eases, and it closes on soft, still, resolved chords.
```

Exclude styles:

```
vocals, singing, choir, drums, drum kit, percussion, timpani, beat, string quartet, pizzicato, plucked strings, full orchestra, string section, brass, horns, synth, electronic, jazz, pop, epic, action, trailer, bombastic, heroic, cinematic
```

## Round log

New rounds at the top.

### Round 1 (2026-10-21) · revision A of all five atoms · unheard

10 Creates, **100 credits (10,120 → 10,020)**, 10 per Create, workspace `gpom-story`. Settings as
the table above. Nothing recorded, nothing listened to, nothing downloaded. Before the round the
form held another session's bank-robbery round D (`br-ska-D-geezer-v6-w60`, `bank-robbery-Kai`); we
waited until it had finished and the form had been quiet for 4+ minutes, then loaded over it.

| Take | Length | Link |
| --- | --- | --- |
| gpom-sh-a-boss-A-v6-w25 | 0:30 | https://suno.com/song/ae6b3568-3e33-4a85-a588-a3392d0cd0f3 |
| gpom-sh-a-boss-A-v6-w25 | 0:21 | https://suno.com/song/22e2c2a3-57be-4fdd-98a1-6f8ca1ca58e6 |
| gpom-sh-a-boss-A-v6-w10 | 0:30 | https://suno.com/song/1d4c1eb0-b646-46d3-98de-f37209664eca |
| gpom-sh-a-boss-A-v6-w10 | 0:36 | https://suno.com/song/47f4ae23-4ccc-4d6b-bdf4-08b694e1218e |
| gpom-sh-a-P1-A-v6-w30 | 0:45 | https://suno.com/song/4967ea91-6b84-4736-b321-db36c0f23abd |
| gpom-sh-a-P1-A-v6-w30 | 0:45 | https://suno.com/song/af7d1f63-2683-4a87-8c32-5dbb891bc4f7 |
| gpom-sh-a-P1-A-v6-w60 | 0:45 | https://suno.com/song/57b65bfc-430e-4ec3-b944-97b57ef2d7af |
| gpom-sh-a-P1-A-v6-w60 | 0:47 | https://suno.com/song/aaf6f059-c631-475b-8571-8f3c525e3ddb |
| gpom-sh-a-P2-A-v6-w30 | 0:44 | https://suno.com/song/49a6688a-0bfa-424f-b476-7585158dbfb5 |
| gpom-sh-a-P2-A-v6-w30 | 0:45 | https://suno.com/song/fdc26ec1-65d0-4722-a27a-9e5eac14bc5c |
| gpom-sh-a-P2-A-v6-w60 | 0:44 | https://suno.com/song/dd3f78e8-aca6-4f4f-a922-2c632215b69d |
| gpom-sh-a-P2-A-v6-w60 | 0:45 | https://suno.com/song/fa09bff7-4e88-4e62-b743-46cf12ecd770 |
| gpom-sh-a-C1-A-v6-w30 | 1:00 | https://suno.com/song/51a8d60f-c9ee-4709-a001-456fc8533513 |
| gpom-sh-a-C1-A-v6-w30 | 1:08 | https://suno.com/song/f45603ec-b8fd-42b2-b5fc-9371051a2431 |
| gpom-sh-a-C1-A-v6-w60 | 1:00 | https://suno.com/song/acf437d2-4ea8-41ca-807a-39eab3c00c70 |
| gpom-sh-a-C1-A-v6-w60 | 1:00 | https://suno.com/song/f88dba0a-2a87-4333-bc4b-d47e0f060fd9 |
| gpom-sh-a-C2-A-v6-w30 | 0:59 | https://suno.com/song/8f29b1ef-dbce-472c-a695-02e90b3d8e70 |
| gpom-sh-a-C2-A-v6-w30 | 1:02 | https://suno.com/song/746eb1fe-cf3b-4581-bb26-b58c132fa1bd |
| gpom-sh-a-C2-A-v6-w60 | 1:00 | https://suno.com/song/6d0d8745-41dc-4497-a8aa-66ab0c7fd75f |
| gpom-sh-a-C2-A-v6-w60 | 1:02 | https://suno.com/song/f5e6e4ce-5685-40a2-ac44-dcf5fb8f8b5e |

**Notes.** The instrumentals came in on target (45 → 0:44–0:47, 60 → 0:59–1:08). The boss takes
came in **short of the 40 s target** (0:21–0:36): there are only ~15 s of words, so a dry read
stops early. **`boss-A-v6-w25` 0:21** is short even against its twin (the house rule 5 symptom):
check it says all four lines before judging it. Whether any take is truly music-free is unheard.
