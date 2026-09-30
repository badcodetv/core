import json, io, os
OUT='/home/jackt/projects/badcode/badcode/docs/stories/camping/songs/camping.md'
lanes=['odejoy','mars','fate','chorale']
S={k:json.load(open(k+'.json')) for k in lanes}

TAKES = {
 'odejoy':  [('w40',[('0d952144-950a-4da4-9e8e-a27d1011cae0','—'),('bf424e3d-e6c5-4e21-b604-90de75ef35f6','—')]),
             ('w60',[('0d800f1a-bfe1-476a-8755-6914fde89dc5','3:05'),('16944146-9334-4ad3-950f-42cd816dd62c','2:56')])],
 'mars':    [('w40',[('60a0153e-2893-47f4-9f13-f1ec2a7a21db','3:04'),('2904dc45-ab05-4800-8f54-2aeef4313fa9','2:55')]),
             ('w60',[('a794f559-eef4-40ae-8445-6241d81d59b7','2:59'),('37a0d0db-f2a1-4bc8-8f7e-47faf9b362ee','2:55')])],
 'fate':    [('w40',[('de2c4d80-34ed-4587-81a8-a115c20a63b1','2:58'),('918c6acd-e8d8-4c68-b253-fbf789d924da','2:54')]),
             ('w60',[('3484e698-7ec4-4fe8-9767-537f9538308a','2:55'),('2bbf3c01-39ef-489e-bb76-7bbdc65b7db7','2:55')])],
 'chorale': [('w40',[('0ec4d070-129c-4f22-bd45-ce162fd6fcbc','—'),('e3cf4d71-6a32-4faa-b8d4-4bc60b321d4c','—')]),
             ('w60',[('1b2aa79c-9b06-44e8-b463-63809306060b','—'),('db7db097-9733-4fa8-81db-57a6b5304b9b','—')])],
}
SHORT = {
 'odejoy': 'a grand piano states one tune low and bare, each section hands it up an octave — Atlantis × Ode to Joy × *End Credits*',
 'mars': 'timpani and wood-of-the-bow strings over a crunching two-step roller, every cycle a semitone higher — *The Nine* × Mars × *Eastern Jam*',
 'fate': 'one four-note figure is the entire record — violins, square-wave bass and hats all play it — *Rock It* / *Mr Happy* × Beethoven 5 × *Tarantula*',
 'chorale': 'a room of men sings the hook unaccompanied, then answers every line in block harmony — *Baddadan* × the Hallelujah Chorus × *BACKBONE*',
}

def row(k):
    cells=[]
    for w,ts in TAKES[k]:
        cells.append(' · '.join(f'[{i[:8]}](https://suno.com/song/{i})' + (f' ({d})' if d!='—' else '') for i,d in ts))
    return f"| `{k}` | {SHORT[k]} | {cells[0]} | {cells[1]} |"

b=io.StringIO()
W=b.write
W("""## v6.58 Round r66 — the three-canon fusion: D&B anthems × classical × the Chase & Status catalogue (2026-09-23)

**Brief, Jack 2026-09-23:** *"So all the last generations were way too aggressive. Please combine the
style of this [nine all-time D&B anthems] and these [nine famous classical works] and [ten Chase &
Status tracks]. And make it something that builds off of
[1127446d](https://suno.com/song/1127446d-abe8-4079-9bbe-6b281e12aa74), which is the original song.
Please also research the internet, look through the repo, and use the skills."*

### 🔑 The round this song has been circling: r64 lost the drums, r65 got them back and went too hard

Three briefs in three days draw one narrow target, and r66 is the first round written to it directly.

| Round | What was asked | What came back |
|---|---|---|
| **r61–r63** | aggression | *"way too aggressive"* |
| **r64** | aggression out | *"the drum and bass has gone basically"* — the ban `distorted bass` took the Reese with it and `patient rather than violent` instructed it not to be D&B |
| **r65** | drums back, anger back | too aggressive again |

🔑 **So the two knobs are separate and r66 turns them opposite ways: the DRUMS stay loud, clean and
in front; the RECORD stops being harsh.** The production sentence in every lane is some form of
*loud, clean and open, nothing distorted* — never r64's *"patient"*, which is the word that
un-made the drums.

### 🔑 Jack's third list is the answer to his own first one

His D&B list is heavier than last time — *The Nine*, *Messiah*, *Mr Happy*, *Tarantula*, *Baddadan*
are techstep, neurofunk and jump-up, precisely the palette that has now been rejected twice. But the
**Chase & Status catalogue he sent alongside it is dominated by the melodic, cinematic, sung ones** —
*End Credits*, *Blind Faith*, *Time*, *Disconnect*, *Pieces*. That is the same duo doing enormous
drums **without** harshness, and it is exactly the band the brief is asking for. **So the heavy
tracks are taken for their scale, their riffs and their chants — never for their distortion.**

### The references, translated (no artist, song or album name in any box)

House rule (`docs/suno-gpt/system-prompt.txt`): no names in a prompt. Each reference is decomposed.

| Reference | What went in the box | Source |
|---|---|---|
| **The Nine** — *"a crunching 2-step roller"*, snare-led rhythmic stumbles, eerie synths and one iconic horn | *a crunching two-step roller, snare-led and stumbling · one eerie synth horn stabbing across it* (→ `mars`) | [Buttondown](https://buttondown.com/Linenoise/archive/the-best-records-ever-to-wreck-a-genre-part-1-bad/), [A Bass Chronicle](https://abasschronicle.co.uk/history-sessions-keeping-bad-company/) |
| **Messiah** — the heaviest neurofunk record there is: chopped breaks, syncopated snares, a cinematic drop | its **scale**, not its drive — *the drums alone and vast*, the room growing each cycle. 🔴 `neurofunk` stays banned | [Sonic State](https://sonicstate.com/news/2024/11/25/remaking-konflicts-messiah-/), [Neurofunk Radio](https://neurofunkradio.com/the-evolution-of-neurofunk-from-early-drum-and-bass-to-modern-soundscapes/) |
| **Rock It** — a robotic riff bass built on a *Robot Rock* sample | *a robotic square-wave bass plays it an octave down* (→ `fate`) | [WhoSampled](https://www.whosampled.com/sample/15032/Sub-Focus-Rock-It-Daft-Punk-Robot-Rock/) |
| **Mr Happy** — *"a riff, a really good riff… the attitude of every jump up song ever combined"* | the riff **is** the record: one figure on every instrument (→ `fate`). 🔴 `jump up` stays banned | [UKF](https://ukf.com/read/10-years-of-dj-hazard-dminds-mr-happy/) |
| **Tarantula** — MC-led, brass instruments over Fresh's drums | *brass stabs answer it* (→ `fate`) | [PlanetPendulum](https://planetpendulum.fandom.com/wiki/Tarantula) |
| **Baddadan** — jungle breaks, a hook half sung half chanted with a room answering | *breakneck chopped amen breaks, ragga swing · the room answers the MC* (→ `chorale`). 🔴 `air horns` stays banned | memory `camping-jack-reference-artists` |
| **Atlantis**, **Brown Paper Bag**, **Valley of the Shadows** | already decomposed at r64 — the warm rolling break and the Rhodes/piano language survive into `odejoy`; 🔴 **Valley's time-stretch is deliberately NOT reused**, it is what blurred r64's drums | §v6.56 |
| 🔑 **Ode to Joy** — the tune stated bare by cellos and basses, then handed upward through the orchestra, each statement adding a layer | *the piano states it low and bare, each section hands it up an octave to a new instrument, cello, violin, then the whole room* (→ `odejoy`) | [Cleveland Orchestra](https://www.clevelandorchestra.com/posts/beethovens-ode-to-joy), [Britannica](https://www.britannica.com/topic/Symphony-No-9-in-D-Minor) |
| 🔑 **Mars, the Bringer of War** — strings *col legno battuto*, a dry rattling mechanical clatter; six horns in unison; snare, bass drum, glockenspiel and tam-tam | *violins hammer one dry rattling note with the wood of the bow · six horns hold one long flat note · glockenspiel and tam-tam at the edges* (→ `mars`) | [Indianapolis Symphony](https://www.indianapolissymphony.org/backstage/program-notes/holst-the-planets/), [music4beginner](https://music4beginner.com/holst-the-planets-mars-bringer-of-war-analysis/) |
| 🔑 **Symphony No. 5** — short-short-short-LONG; the four-note cell is the acorn the whole symphony grows from, fragmented, inverted and sequenced | *the record is one four-note figure, three short, one long… inverted, up a third, cut in half, handed on, always those four notes* (→ `fate`) | [The Violin Channel](https://theviolinchannel.com/beethovens-fifth-symphony-a-complete-listening-guide-to-classical-musics-most-famous-four-notes/), [Eastman](https://www.esm.rochester.edu/beethoven/symphony-no-5/) |
| 🔑 **Hallelujah Chorus** — block homophony where every voice hits the word together, alternating with unison lines and fugal runs | *they hit one word together in block harmony, one high voice running a fast line under* (→ `chorale`) | [Wikipedia](https://en.wikipedia.org/wiki/Hallelujah_Chorus), [phamoxmusic](https://phamoxmusic.com/hallelujah-chorus/) |
| **Four Seasons**, **Clair de Lune**, **Canon in D**, **Boléro** | the solo violin and the piano opening are already the spine; Canon in D and Boléro were spent at r64 (`groundbass`, `bolero`) and are not repeated | §v6.56 |
| ⬜ **The Blue Danube** | **deliberately unused for the second time** — a 3/4 waltz against a 174 4/4 grid fights the spine. Same ruling as r64 | — |
| ⬜ **Mars's 5/4** | **deliberately dropped** — five beats against the 174 four-beat bar is the waltz problem again. The *col legno rattle* and the semitone climb carry Mars instead | — |

### 🔑 Where the aggression was removed, precisely — four places, one word each

| Lever | r65 | r66 |
|---|---|---|
| **Cast sentence** | *"both spitting fast, **furious** and emotional, voices close to cracking"* | **one word deleted.** Each lane keeps the speed clause verbatim (`rapid-fire on the 174 grid and never slowing for a punchline`) and closes with its own temper — `fast and hurt` · `fast and grim` · `fast and stinging` · `fast and raw-throated` |
| **Lyric cues** | `furious and hurt` · `rising, angry` · `spitting the words` · `sneering and angry` · `both angry` · `half shouted` | `hurt and insistent` · `rising, hurt` · `biting` · `cold and contemptuous` · `both hurt` · **`half chanted`** |
| **Excludes** | — | 🆕 `harsh, abrasive` added; `screaming, roaring, snarling, war drums, air horns, clipping, overdriven` kept |
| **Production sentence** | *"Dry, close and loud"* | *loud, clean and open, nothing distorted* — **loud is retained deliberately**, because r64 proved that softening this sentence is what removes the drums |

🔴 **`distorted bass` is NOT banned and `rapid-fire` is NOT banned.** Both were found fighting the
brief in earlier rounds — the first is the Reese on Jack's own favourite take, the second is r43's
own word for the delivery he asked for. See the excludes audit in §v6.57.

✅ **Not one lyric word changed**, asserted in the build: every bracket cue is stripped from the r65
and r66 blocks and the remaining text compared byte for byte, with the line count held at 80.

🔑 **And the opening cue is now instrument-neutral** — `[Verse 1 | no drums at all, only the
instrument the track opens on | …]`. The lyrics box out-votes the style box on arrangement (§v6.51),
so naming the piano there would have overridden three of the four lanes' openings.

### The four lanes

| Lane | D&B anthem | Classical device | Chase & Status | Where the energy comes from instead of distortion |
|---|---|---|---|---|
| `odejoy` | Atlantis — warm rolling break | **Ode to Joy** — one tune handed upward | *End Credits* / *Blind Faith* — piano, tambourine, cinema | **rising** — the same tune an octave higher each section, minor until the last chorus |
| `mars` | *The Nine* — crunching two-step roller | **Mars** — col legno rattle, six horns on one note | *Eastern Jam* / *Pieces* — dark and huge | **climbing** — every cycle a semitone up |
| `fate` | *Rock It* / *Mr Happy* — the riff is the tune | **Beethoven 5** — one four-note cell, developed | *Tarantula* / *Hitz* — brass stabs, MC-led | **obsession** — one figure on every instrument, moved and inverted |
| `chorale` | *Baddadan* — jungle breaks and a chant | **Hallelujah Chorus** — block antiphony | *BACKBONE* — a stadium behind a grime MC | **the room** — weight from the number of voices, not the volume |

✅ **Bold, not meek:** longest shared run between any two Style boxes is **135 chars = 13.6%**, and
it is the mandated cast sentence plus `both fast and `. No production language is shared.

### Settings

v6 · Style Influence **75** · Variety **Off** · Max Mode off · Vocal Gender Male · Personalize off ·
no Voice · **Duration 175 s** · workspace `camping-Jack` · weirdness **40 and 60**. 8 Creates, 16 takes.

🔑 **175 s, the fast half of the settled bracket** (155 s way too fast · **175–190 s the working
range** · 195 s too slow · 200 s slower still). Jack's complaint this round is aggression, not
pacing, so Duration is held at r65's faster cell rather than moved.

### Generated 2026-09-23 — 8 Creates, 8 clean. Credits 9,340 → 9,260

| Lane | What it is | w40 | w60 |
|---|---|---|---|
""")
for k in lanes: W(row(k)+"\n")
W("""
✅ **Eight Creates, eight clean** — 10 credits each, balance read before and after every one.

⚠️ **Two takes overshot the 175 s target** (`odejoy` w60 at 3:05 and `mars` w40 at 3:04 against a
2:55 target); the rest landed 2:54–2:59. That is the **third** time a 175 s target has been treated
as a suggestion. 🔑 **A long take had more room to slow down in — check the returned length before
blaming the prompt.**

⬜ **Not heard.** Four questions, in this order:
1. 🔑 **Is the aggression gone without the drums going with it?** That is the whole round — r64 and
   r65 each got one half. Every lane should still be *loud*.
2. **Does the fusion read as one record**, or as an orchestra bolted onto a beat? `fate` is the
   sharpest test: if the four-note figure is audible on the bass, the stabs and the hats, the idea
   landed.
3. **Which structural device carries best?** Rising (`odejoy`) · climbing (`mars`) · obsession
   (`fate`) · the room (`chorale`). This is the question the round exists to answer.
4. **Does the rap still keep up**, and does `odejoy` turning major in the last chorus read as earned
   or as sentimental? That major turn is the one risk this round buys.

""")
for k in lanes:
    W(f"### r66 {k} atom\n\nStyle:\n\n```\n{S[k]['style']}\n```\n\nExclude styles:\n\n```\n{S[k]['exclude']}\n```\n\n")
W(f"### r66 lyrics (shared — the r65 words, cues de-escalated, opening cue made instrument-neutral)\n\n```lyrics\n{S['odejoy']['lyrics']}\n```\n\n---\n\n")

src=open(OUT).read()
anchor="## v6.57 Round r65"
assert anchor in src
src=src.replace(anchor, b.getvalue()+anchor, 1)
open(OUT,'w').write(src)
print("✅ inserted §v6.58, file now", len(src.split(chr(10))), "lines")
