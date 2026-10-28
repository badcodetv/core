# The Bank Robbery — sound

> The sound for this story only. Read before any Suno or voice prompt (suno-prompt,
> suno-automation, variations, scene-timeline voicing). Rules: [`docs/stories/STYLE.md`](../STYLE.md).

**Status:**
- **The song (Jack's song, Kai's lyrics):** EXPLORING — no take picked. Jack paused Suno on 2026-10-25
  (*"we have enough songs i want to show kai, then we will decide"*). The reference he keeps returning to
  is **"Best one"** ([024b82e8](https://suno.com/song/024b82e8-378c-47bd-bf73-bb5eafea2ed5)): *"I loved the
  style/genre/beat/everything about it other than the voice."*
- **Film music:** LOCKED for now — six HoliznaCC0 lo-fi tunes (CC0) since cut 9; the Suno score is parked.
- **Narrator:** LOCKED for now — AI Studio `Sadaltager`, the Walthamstow deadpan note (cut 9 on, and the
  short). Open: the 15 Oct 2026 call moved the film to **several narrator voices**; how many and which is
  not decided.
- **Character voices:** built (twelve Flow custom voices + Barry), not heard in a clip.

## In one paragraph

Unsettled, but the shape of what Jack likes is clear: **"Best one" sounds like gritty acoustic blues over
boom bap, about 90 BPM** — a raw acoustic guitar riff driving it, stomping kick and snare, foot stomps and
tambourine, a heavily saturated growling sub bass, a raspy mid-register British man rap-singing, a shouted
gang hook, big dynamics (guitar-only breaks, then hard drops), a dark mix. Since then the rounds have
wandered through psychedelic funk, 1970s cop-show funk, music-hall talkers, Brixton dub patter and opera.
Every voice must be **English**, nothing screamed, nothing double-time, and every voice must be genuinely
different from the last round's. The film itself is underscored with chill royalty-free lo-fi, played
straight; the jokes are the narrator's.

## Tracks

### The song — "Best one", the reference (not a pick)

[024b82e8](https://suno.com/song/024b82e8-378c-47bd-bf73-bb5eafea2ed5) (the round that made it is not recorded in the sheet). Suno's
stored record, verbatim from [`songs/sealed-r3/reference.md`](./songs/sealed-r3/reference.md) — note it
**does not describe how the take sounds** (heard: blues / boom bap with the rap and hip hop it excludes):

Style:

```
English psych folk funk, 100 BPM: a wavering untrained English folk singer with warbling ornaments, climbing to a cry on the chorus. Sitar, tin whistle, hand drums, a slinky funk bass.
```

Exclude:

```
comedy, novelty, parody, kazoo, cartoon, trap, double-time, fast rap, autotune, EDM, country, smooth R&B, rap, hip hop
```

Settings: v6 · Variety off · Max Mode off · Vocal Gender male · style influence 75 · weirdness 30 ·
Duration 170 s. Lyrics: Jack's draft 3 (289 words), not Kai's. Measured: 2:49, loudness range 12.4 LU,
spectral centroid 2.6 kHz. Jack's one dislike besides the voice: the Indian/sitar opening. Listens:
`docs/listening/log/2026-10-22-162914-…024b82e8.md`, `…2026-10-24-103905-…024b82e8.md`.

### The song — takes Jack has singled out

All logged in [`songs/bank-robbery-jack.md`](./songs/bank-robbery-jack.md) with their boxes:

| Take | Round | What Jack said |
| --- | --- | --- |
| [ed6dd946](https://suno.com/song/ed6dd946-0ebf-422d-a68b-3e205462adc1) | B, cop-show funk | the liked take of round B; its real prompt was Suno's Variety rewrite — §Round AA |
| `brj-sweep-s3-falsetto-v6-w40`, `brj-sweep-s2-gangster-spoken-v6-w30` | SW | *"I like both of them"* |
| `brj-sr4-london-music-hall-talker-v6-w30` → **[dddd147b](https://suno.com/song/dddd147b-858d-42da-bd2f-9e316edab1b4)** | SR4 → SR5b base | *"the second take"* |
| `brj-sr5-brixton-baritone-dub-echo-v6-w35` ([7aa63b33](https://suno.com/song/7aa63b33-dbfa-4201-9b3b-78ae4ba48103) · [3dd31d66](https://suno.com/song/3dd31d66-3c71-498a-98df-9d57a340e4b2)) | SR5b | *"maybe do a song like this … add classical and operatic elements"* → SR7/SR8 |

Latest rounds: SR7 and SR8 (2026-10-24, unheard). `songs/sealed-r9/` (opera only) and `songs/sealed-r10/`
(opera kept, operatic singing out, the laid-back gangster voice back, psych funk with classical) hold
eight specs each; **they are not logged in the sheet and whether they were generated is not recorded.**

Lyrics: **always Kai's** (standing rule; `songs/sealed-r5/lyrics.txt`). Workspace `bank-robbery-Jack`.

### How a new round is made

Exploring rounds go through the `variations` skill (`scripts/variations/round.py`; traps in
[`docs/suno-gpt/same-song-traps.md`](../../suno-gpt/same-song-traps.md)): raw inputs only (Jack's words
verbatim, Kai's lyrics, one fresh listen), one ideas writer, N separate writers, the sameness gate. This
story is where that method came from: 400+ takes came out as one voice while the prompts were written
inside the repo.

### Film music (LOCKED for now)

[`music-lofi.md`](./music-lofi.md): six **HoliznaCC0** tunes from the Free Music Archive, CC0 1.0, licence
checked per track, no credit needed (Jack, 2026-10-12: *"more chill and lofi, so that it fits each scene's
mood more, use royalty free stuff"*). Replaced seven Kevin MacLeod spy/heist cues (CC BY 4.0) from cut 3.
Which tune sits under which scene: [`review-cut8.md`](./review-cut8.md) §"The music". Content ID unchecked.

### Suno score (parked)

[`songs/score.md`](./songs/score.md): `br-bed` (heist bed, 355 s) and `br-sting` (80s montage), round A
2026-10-08, unheard. Settings: v6 · style influence 75 · weirdness 30 and 60 · Variety normal · Max Mode
off · Personalize off · no Voice. Played straight on purpose.

## Narration / voices

**Narrator (cut 9 on, and the short):** AI Studio, model `gemini-3.1-flash-tts-preview`, voice
**`Sadaltager`**. Chosen from eight auditions by the listening model (most "ordinary" and most deadpan),
not yet by a human ear ([`review-cut8.md`](./review-cut8.md)). Director's note, verbatim:

```
Accent: British (London, working class, an ordinary bloke from Walthamstow in east London; everyday, not posh, not stagey cockney).
Style: deadpan and completely straight. A middle-aged man stating plain facts. Flat, dry, matter-of-fact, never amused, never performs or signals a joke, no smile in the voice.
Pace: brisk and even, clear articulation, short pauses.
```

Edit: pauses inside a line longer than 0.38 s closed to 0.38 s (except where the pause carries the joke).
Renderer: `scripts/bank-robbery/brs-tts-lib.py`, `br-narration-v9.py`.

**Character voices:** one Flow custom voice per Character, each on a different AI Studio preset, with a
performance text — table in [`characters/cast-portraits.md`](./characters/cast-portraits.md) (Denise
`Gacrux`, The Ex `Umbriel`, The Fixer `Algieba`, The Donor `Algenib`, The Governor `Charon`, The
Proprietor `Enceladus`, The Presenter `Rasalgethi`, The Platform `Iapetus`, The Accountant `Sadaltager`,
Mr Blue `Orus`, Mr Red `Achird`, Mr Turquoise `Puck`). Barry (the short): `Alnilam`, saved as `Barry BRS
voice` ([`short-shots.md`](./short-shots.md)). None heard in a clip. On the 15 Oct call these move into
narration: a distinct narrator voice per character, no lip-sync.

## Rules for this story

Jack's standing rules for the song:
- **No screaming** (*"no weird screaming"*, Round VB, 2026-10-22).
- **No fast or double-time rap.**
- **No Covers** (*"covers dont work please dont use them"*, Round CA, 2026-10-22) **and no remixes** of
  earlier takes; new prompts only.
- **English voices**, and every round's voices genuinely different from each other and from the last.
- **No sitar / Indian opening.**
- **Always Kai's lyrics.**
- **Don't name artists in a box** (Round Y: Suno stored "Roger Daltrey" and nothing audible changed).
- **Write exploring rounds sealed**, not from inside the repo (Round SR1 onwards).

For the film:
- **The music stays sincere**; the jokes are the narrator's.
- **A narrator line never plays over a talking clip.**
- **No lip-sync**; full narration with several voices (15 Oct 2026).

## Never

- Screaming, double-time, chopper rap.
- Covers or remixes of a liked take.
- American accents.
- One voice for every take (the 400-take failure).
- A narrator who signals the joke.

## History

- **Drafts 1–3** (2026-10-21): menacing British art-punk with 1970s heist funk, 120 BPM; then *"more
  gritty, gorier, aggressive, there is too much of the story in there"*. Draft 2's styles: heist-movie punk,
  grime over a heist beat, 1970s cop-show funk (kept as a maybe), drum & bass (banned on purpose).
- **Rounds A–Z** (2026-10-21): cop-show funk; English voices by performer type; a Daltrey-like voice by
  name (did nothing). **AA/AB**: found that ed6dd946's music came from Suno's Variety rewrite, not our box.
- **Rounds BA–KA** (2026-10-22): Beatles / Zeppelin / Stones / Oasis voices (Covers rejected), ten styles
  × ten voices, funk and psychedelic blends, Kai's lyrics on the liked take.
- **CR → GG** (2026-10-22): "clean-room" helpers that were in-repo subagents, so they inherited CLAUDE.md
  and memory; voices kept reverting (*"the same old boring ones"*).
- **SR1–SR8** (2026-10-23/24): the sealed writer (`scripts/suno/sealed-writer.sh`, then
  `sealed-round.py`): gangster voices, deep English voices, Best one's box with only the voice changed
  (SR4), music-hall talker iterations (SR5 stopped by the gate, SR5b generated), psych folk funk (SR6), the
  Brixton song with classical/opera (SR7) and a western/opera psych-funk clean room (SR8).
- **Film music**: no music in cut 1–2; seven Kevin MacLeod cues in cut 3; HoliznaCC0 lo-fi from cut 9.
- **Narrator**: the Money For Something narrator first (AI Studio `Zubenelgenubi`, Accent British
  (Brixton), cut 1, [`assembly.md`](./assembly.md)); `Sadaltager` from cut 9.
