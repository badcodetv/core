You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Jack, 2026-11-19, on the 29 s cut with jazz1 (three rules): "Rap all ten please and "Fix the rhythm" means sometimes he says the line too fast, and could sound a bit more like the actauly ten crack commandments song, but just use what we have as a template/inspiration."
Jack, 2026-11-19, on the lyric: "do "Uno", keep the rest please make the song thanks"

## What happened in earlier rounds (facts)

- Round 2 (2026-11-16): Jack picked jazz1 (Suno e4cb9be5), v6, Duration 20 s, came back 29.0 s; three rules numbered 1-3 plus the fix. Its Style box is keep.txt.
- 2026-11-17 meeting (Jack and Kai): the song says ten but shows fewer; "fix the rhythm; ten points if the length allows".
- 2026-11-19, Jack: rap all ten; "sometimes he says the line too fast"; "could sound a bit more like" the original song; use what we have as the template.
- The new lyric is ten rules plus a short intro and the fix: about 75 s at an unhurried pace. Each "Number ..." should land on its own beat with room before the line.

## This story (stay inside its look and sound; another part's look does not apply)

# Ten Economic Commandments


## What it is
A BadCode short (9:16, 29 s): a 90s East Coast rap parody of a famous "ten commandments" track, about who controls the
money printer. Three numbered rules, then the fix. The point: whoever holds the money printer will get high on their
own supply; the fix is that no human controls the printer. State: rough cut 1 frozen (`scenes/ten-economic-commandments/final.json`)
and built in Premiere (`short-ten-economic-commandments-1-tec-r1`); export to 1080x1920 owed.

## Look
- Status: look.md says EXPLORING with no ruling written; the stills are picked (round 4).
- Settings from Jack's four reference photos (an 80s NYC fence-and-bench street portrait, a subway platform with a train
  blurring past, a dusk street crowd with traffic-light bokeh, a cobbled street framed on a suspension-bridge tower);
  they sit in `reference/` in the media folder. The subway photo carries stock watermarks: describe it, never attach it.
- The BadCode figure: a street-interviewer's outfit and posture (a baggy beige thrift suit, a plain cap, a street-interview
  mic), never a real person's name or face; the BadCode balaclava covers the face. No skin anywhere: full-length trousers,
  black socks, a black roll-neck, gloves into the cuffs.
- Picks: RU4-1-b (doorstep, chalkboard), RU4-2-a (red studio), RU4-3-a (fence bench), RU4-5-b (dusk crowd, mic),
  SU4-1-a (subway, banknotes), SU4-3-b (bridge street, falling notes), FX4-1-b (streetlight, empty gloved hands).
  FX5-a / FX5-b (fire-escape wide redone) are on the board, unpicked.
- Stills Nano Banana 2; clips Omni 1.2 Flash, Frames, 9:16, 8 s. Flow project `17b708f8-d9d6-41ae-b562-8d161797b542`.

## Sound
- Status: LOCKED. The rap = **jazz1**, Suno https://suno.com/song/e4cb9be5-5c68-484d-ace0-e0fed5592f59 (round
  `songs/r2-rap`, writer `jazz-phrasing`; prompt verbatim in `songs/r2-rap/round.json`). v6, Duration set 20 s, came back 29.0 s.
- Sections: intro 0-5, rule one 5-10, rule two 10-15, rule three 15-21, the fix 21-24, beat out to 29.
- Lyrics: [songs/r2-rap/lyrics.txt](./songs/r2-rap/lyrics.txt), three rules numbered 1-3 plus "And the fix, from the future? No hand on the printer."
- Vocals are wanted on this short (a rapped male vocal); no other voices.

## Story-only rules
- Never write "trousers a little too short" (or anything that bares ankles, wrists or neck) for the figure.
- When fixing masks, attach the still only: with the navy mask reference attached the masks turned navy.
- No real rapper or real currency in any still. Blur the fast-food logo on RU2-a-a if it is ever used.
- Check every clip at three frames for suit, cap, mask and no skin; a clip that turns side-on late is used from its start.
- The logo is a card at the tail, laid in by the edit. `marketing-gatekeeper` before posting.

## Flow project
- `17b708f8-d9d6-41ae-b562-8d161797b542` — scenes/ten-economic-commandments

Open the part's project before its first Flow call; never use it for another story.

## Library pieces in use
- none yet

## Where the detail is
- [README.md](./README.md), [look.md](./look.md), [sound.md](./sound.md)
- Rulings: [scenes/ten-economic-commandments/picks.md](./scenes/ten-economic-commandments/picks.md); takes: [songs/r2-rap/takes.md](./songs/r2-rap/takes.md)
- Timeline https://claude.ai/artifact/2vysJs9o1JJyPC4HztqzjG · mood board https://claude.ai/artifact/DL4FFqF8ia1K2GerAX4uBi · rap picks https://claude.ai/artifact/8g5haV7wncRBKwKmtgcPaR

## Never write these

Notorious
Biggie
B.I.G.
Ten Crack Commandments
DJ Premier

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "v6",
  "durationSec": 75,
  "vocalGender": "male"
}
```

## The lyrics

Use these words exactly — do not change, add or remove any word or spelling. You may add section tags and short directions in square brackets. Keep every line.

```
Uh. Money printer manual. Take notes.

Rule number Uno: never say how much you made,
doesn't matter anyway, since the gold went away.

Number two: never show 'em your next move,
cut the rate for the banks, hike it when you land.

Number three: never trust nobody with the press,
before Bernie gets made off face loss.

Number four: never get high on your own supply,
banks took the first hit, now the rent's sky-high.

Number five: never print where you sleep,
never let them owe the oats you reap.

Number six: no credit? Forget it,
let the junkie know you better forget that.

Seven, and nobody says it out loud:
keep your money and your assets apart, not in one crowd.

Number eight: hold none of it yourself,
debase 'em till the numbers go through.

Nine's the one they'd rather you skipped:
keep the auditors out, sporadic trips and you out.

Number ten: no consignment, cash up front, that's law,
they took the bailout in stride and they ain't paid it all.

And the fix, from the future? No hand on the printer.
```

## The box to keep

The request wants a prompt very close to this one, with only what it asks for changed. Verbatim from
the engine's record:

```
late-90s New York street rap, one heavyset MC who treats his verse like a bebop drum solo turned into words: rhythm played as melody, syllables dragged a hair behind the snare then tumbled out in quick clusters, stacked multisyllable rhymes rolling into each other, unbothered talking cadence, a deliberate beat of silence right before each punchline lands. Vocal: enormous man, low velvet chest baritone, lazy Brooklyn vowels, a short asthmatic wheeze audible on every inhale, dry and right on the mic. Instrumental: 88 BPM, swung dusty breakbeat with a thick knocking kick and a hard flat snare, a melancholy after-midnight Rhodes-and-organ soul-jazz figure sliced into a cold, menacing minor loop, walking acoustic-bass-style bottom end, tape hiss and crackle; between the rules a hoarse sampled crowd-chant voice barks the number; bare, minimal, threatening, no hook
```

## Your experiment

Write ONE prompt for this experiment, and only this one:

**closer-to-the-original-loop** — Lean on the 'sound a bit more like the original' part by reshaping only the instrumental: build the loop around a short, wailing jazz-guitar slide stab taken from a late-70s jazz record, repeated over hard, sparse boom-bap drums at about 88-90 BPM, with the Rhodes-and-organ figure pushed far back as a dark pad under it; cold, ominous, almost empty. Make the number caller clearly a different, gruff shouted voice chopped from an old record, punching in on its own like a scratch, then a beat of silence before the MC answers. Keep the MC's identity, voice, wheeze and dry mix as they are, but replace the quick-cluster flow with a calm, conversational, matter-of-fact list reading: rule, short explanation, done, with no hurry. In the lyric field, tag each rule as its own section and put a [sampled shout] direction before each number line. Still no hook and no singing.

Your box is the box to keep above, changed only as your iteration and the request need: keep the rest of its words. Write every change in your own words — other writers are doing the other iterations (minimal-swap-patient-cadence, slower-tempo-more-air, lyric-field-carries-the-timing) and must not share your new wording.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Style boxes (shared by most of the round): baritone from the
- shares wording with other prompts in this round: Style boxes (shared by most of the round): deep smooth baritone
- shares wording with other prompts in this round: Style boxes (shared by most of the round): man deep smooth
- shares wording with other prompts in this round: Style boxes (shared by most of the round): smooth baritone from
- shares wording with other prompts in this round: Style boxes: baritone from the
- shares wording with other prompts in this round: Style boxes: big bodied rapper
- shares wording with other prompts in this round: Style boxes: deep smooth baritone
- shares wording with other prompts in this round: Style boxes: man deep smooth
- shares wording with other prompts in this round: Style boxes: man deep smooth baritone from the
- shares wording with other prompts in this round: Style boxes: smooth baritone from

Your previous draft:
```json
{
  "name": "closer-to-the-original-loop",
  "style": "East Coast boom-bap from 1997, a big-bodied rapper reading his rules off like a calm ledger: the rule, one plain sentence of explanation, stop. Conversational, matter-of-fact, never rushed, each line gets its full bar with air around it, a held breath before the payoff. Voice: huge man, deep smooth baritone from the gut, slurred Brooklyn drawl, a small asthmatic wheeze on each breath in, dry and close-miked. Beat: 89 BPM, hard sparse drums, fat knocking kick, flat cracking snare, wide gaps; the loop is one short wailing jazz-guitar slide stab cut from a late-70s jazz LP, repeated every bar, cold and ominous; Rhodes and organ sunk far back as a dark low pad, walking upright bass, tape hiss, crackle. Before each rule a separate gruff shouting voice chopped from an old record punches in alone like a scratch to call the number, then a beat of silence before the rapper answers. Bare, nearly empty, menacing, no hook, no singing",
  "exclude": "singing, sung chorus, melodic hook, female vocals, double-time flow, rapid-fire delivery, autotune, trap hi-hats, 808 slides, bright synths",
  "lyrics": "[Intro: guitar-slide loop alone, then the rapper, calm]\nUh. Money printer manual. Take notes.\n\n[Rule 1]\n[sampled shout]\nRule number Uno: never say how much you made,\ndoesn't matter anyway, since the gold went away.\n\n[Rule 2]\n[sampled shout]\nNumber two: never show 'em your next move,\ncut the rate for the banks, hike it when you land.\n\n[Rule 3]\n[sampled shout]\nNumber three: never trust nobody with the press,\nbefore Bernie gets made off face loss.\n\n[Rule 4]\n[sampled shout]\nNumber four: never get high on your own supply,\nbanks took the first hit, now the rent's sky-high.\n\n[Rule 5]\n[sampled shout]\nNumber five: never print where you sleep,\nnever let them owe the oats you reap.\n\n[Rule 6]\n[sampled shout]\nNumber six: no credit? Forget it,\nlet the junkie know you better forget that.\n\n[Rule 7]\n[sampled shout]\nSeven, and nobody says it out loud:\nkeep your money and your assets apart, not in one crowd.\n\n[Rule 8]\n[sampled shout]\nNumber eight: hold none of it yourself,\ndebase 'em till the numbers go through.\n\n[Rule 9]\n[sampled shout]\nNine's the one they'd rather you skipped:\nkeep the auditors out, sporadic trips and you out.\n\n[Rule 10]\n[sampled shout]\nNumber ten: no consignment, cash up front, that's law,\nthey took the bailout in stride and they ain't paid it all.\n\n[Outro: drums drop, guitar stab alone, rapper slow and plain]\nAnd the fix, from the future? No hand on the printer.\n\n[End: loop rides out]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 30,
  "styleInfluence": 70,
  "vocalGender": "male",
  "durationSec": 75,
  "maxMode": false
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r3-rap/writers/closer-to-the-original-loop.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r3-rap/writers/closer-to-the-original-loop.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "closer-to-the-original-loop". Reply with just the two paths.