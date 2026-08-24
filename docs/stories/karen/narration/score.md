# Score — Suno prompts for the background music

Six instrumental cues, one per movement of the film. All six are built from the
DNA of [`../songs/all-day-to-complain.md`](../songs/all-day-to-complain.md), so the
score and the song are demonstrably the same piece of music wearing different
clothes — which is exactly what [`../story.md`](../story.md) asks for: *"the song is
structural, not incidental."*

> ## 🔇 The one rule: it must not steal the show
>
> This is a bed under a spoken narrator. Every prompt below is written to be
> **sparse, low, repetitive, and hollow in the middle** so the voice sits on top of
> it. No hooks, no lead lines, no builds that arrive, no key changes. If a
> generation is interesting on its own, it is wrong for this job. **The narrator is
> the engine; the music is the room he's standing in.**

## Do the cheap thing first

Canon already licenses the cheapest option: *"background music can be **stem
remixes of our own track** — Suno stem-split → the trumpets as hold-muzak,
elevator versions of our own tune — we have that for days."*

**Stem-split an accepted take of *All Day to Complain* before generating anything
here.** The trumpet, sax and muzak-loop stems alone will cover Act 2 and probably
Act 1. Use these prompts for what the stems can't reach — the cold Sean AI beats,
and the warm resolution at the end.

## The shared DNA

Every cue inherits this from the song, so the film sounds like one object:

| Element | Value |
| --- | --- |
| Tempo | **86 BPM** throughout — never changes, not once |
| Head genre | Hip hop / boom bap, brushed and quiet |
| Arrangement influence | **A 60s spy-thriller film score** — as an *influence on the arrangement*, never as an equal genre. Listing them as equals lets the spy band eat the record. |
| The signature chord | An **unresolved minor ninth**, held. It is the hold-muzak loop and the spy chord at the same time, and it does not resolve until Cue 6. |
| Bass | Muted upright — walking in Acts 1–3, **prowling chromatic** in Act 4 |
| Colour | One smoky baritone saxophone; low brass and timpani only when something turns |
| Percussion accent | Telephone beeps locked to the beat |

**⚠️ Never write "James Bond", "007", "Skyfall" or any artist name in any box.**
Franchise and artist names trip Suno's moderation and steer worse than description.
`60s spy-thriller film score` is the whole reference.

---

## Boxes to paste once and leave alone

These two are the same for all six cues. Re-paste them every round — **"Reuse
Prompt" silently carries stale boxes forward**, and a stale box is invisible; it
just sounds like the style prompt is being ignored.

### My Taste

```
Instrumental score only, no voices of any kind. The music is a bed underneath a spoken narrator and must never compete with him: sparse, low, and repetitive, with a hollow middle so speech sits on top of it. A small ensemble played by people, recorded close and dry in a small room — brushed kit, muted upright bass, a soft electric piano, one lonely baritone saxophone, low brass and timpani only when something turns. Held chords rather than melodies. No hooks, no lead lines, no builds that arrive anywhere. Tempo sits around 86 BPM, unhurried and patient. The mood underneath everything is dry, deadpan and faintly sad, with the warmth held back until the very end.
```

### Exclude Styles

```
vocals, singing, choir, backing vocals, spoken word, rap, lead melody, catchy hook, topline, guitar solo, saxophone solo, EDM, drop, riser, build-up, big finish, cinematic trailer, epic orchestral, braams, orchestral hits, sound effects, applause, loud, bright, busy, wall of sound, sidechain pump, heavy compression, distortion, key change, tempo change
```

### Settings

| Control | Value |
| --- | --- |
| Mode | **Advanced** — beats come out better in Advanced than Simple |
| More options → **Instrumental** | **ON.** This is the load-bearing toggle; the exclude list alone will not stop Suno singing. |
| Style influence | **80** |
| Weirdness | **20** — you want obedience, not invention |
| Model | v5.5 |

---

## Cue 1 — Act 1, the office and the firing

Corporate, small, bored. Music nobody chose, playing in a room nobody wants to be
in. It goes cold on the laptop.

```
Instrumental. 86 BPM boom bap, brushed and quiet, arranged like corporate hold music that nobody chose. A muted upright bass walking slowly, a soft electric piano holding one unresolved minor ninth, brushed kit low in the mix, a single baritone saxophone answering once and giving up. Dry, close, small room. Deadpan and slightly bored. It loops without ever developing. When the laptop opens, everything but the bass and one held chord drops away and the room goes cold.
```

## Cue 2 — Act 1, the night out and the river

Same tune, drunk. The only cue allowed to get warm before the end, and it pays for
it by falling apart.

```
Instrumental. The same 86 BPM boom bap, now loose and drunk. Brushed kit dragging behind the beat, muted upright bass smeared, warm tape wobble and gentle pitch drift, a lazy baritone saxophone playing half a phrase and losing interest. Late-night bar warmth, close and dry, small and unbothered. It gets slower and softer toward the end, until only the bass and one held chord are left, out in the cold air by the water.
```

## Cue 3 — Act 2, the Great Escalation

**The hold-muzak version of our own song** — diegetic, coming out of the receiver.
The one cue that carries a melody, because a hold queue has to. **Duck it hardest.**

```
Instrumental. Elevator muzak version of a boom bap tune, 86 BPM, the kind of music a hold queue plays for nine months. Bright plastic electric piano and muted trumpet carrying a cheerful little melody over an unresolved minor ninth that never lands. Brushed kit tiny and polite, muted upright bass walking. Telephone beeps locked to the beat as the only other percussion. Endlessly looping, faintly degraded, cheerful in a way that slowly becomes unbearable. Dry, small, and always underneath.
```

## Cue 4 — Act 3, viral

Momentum without excitement. It builds by getting **denser, not bigger** — the
distinction that keeps it under the voice.

```
Instrumental. 86 BPM boom bap opening up — the brushed kit switches to sticks, the muted upright bass starts prowling chromatically, a smoky baritone saxophone holds long low notes underneath. Momentum without excitement: the groove gets firmer and busier but never louder, and never resolves. Telephone beeps still on the beat, further back now. Dry, close, confident, faintly amused. It builds by getting denser, not bigger.
```

## Cue 5 — Act 4, the studio and the takeover

Tension, then nothing. The hollow-out is the point — Sean AI arrives in an absence,
not a sting.

```
Instrumental. 86 BPM boom bap arranged like a 60s spy-thriller film score. Prowling chromatic upright bass, muted brass stabs, brushed kit tight and tense, low brass and timpani entering under the surface. An unresolved minor ninth held throughout. Then everything stops: the band is gone, and only a low sub drone and a slow cold pulse remain, patient and unhurried and completely certain. Dry, close, and quiet even at its tensest.
```

## Cue 6 — Act 5, one hundred years later

The chord finally resolves. This is the accord — **generous, not triumphant.**
Nothing here is allowed to sound like a victory.

```
Instrumental. The same tune a century later, slow and warm and finally at rest. 86 BPM, brushed kit almost absent, muted upright bass playing long round notes, a soft electric piano letting the minor ninth resolve at last, one baritone saxophone playing a single fond phrase and stopping. Wide, still, unhurried, generous. Nothing proves anything. Dry and close, with plenty of air. It ends by simply thinning out until only the room is left.
```

---

## In the edit

- **Duck the music 18–22 dB under the narration**, not 6. This is a voice-led
  piece; the bed should be barely perceptible while he's talking and only come up
  in the gaps between chunks.
- **Carve 1–4 kHz out of the music** with a wide EQ dip. That's where the voice
  lives, and it's why the prompts all ask for a hollow middle — but a mix move
  guarantees it.
- **Generate long and loop.** Ask for the full length and cut a bar-accurate loop
  from the calmest section rather than trying to match a cue to a scene's exact
  duration.
- **Cue 3 is diegetic** — it's coming out of the phone. It can be filtered narrow
  and tinny, and it's the one cue that may briefly play *over* a gap in narration.
- **Cue 5's silence is a cue.** Don't fill the hollow-out. Sean AI taking the
  government should land in a room with no music in it.
