# Suno Studio 2.0 — the app surface

**What lives where.** This file is the **surface**: what is actually in Studio 2.0 and how to drive
it — chat, MIDI, live recording, the effects rack, custom plugins, shortcuts.
[`suno-controls-and-workflows.md`](./suno-controls-and-workflows.md) **§8** is the **generation
craft** inside Studio — the three verbs (Create / Replace / Cover), exclude-styles discipline,
one-instrument prompt shapes, take lanes, the bootstrap trick. That section is still current: 2.0 is
**additive**, not a replacement.

> **Confidence: vendor demo, single source.** Everything here comes from Suno's own launch video with
> the Studio product manager (see Provenance at the bottom). It is a feature demo where everything
> worked on the first take, not adversarial testing, and it is the company describing its own
> product. Treat the **existence and location** of features as solid, and every claim about **how
> well they work** as unverified. The rest of this knowledge base earns its confidence from a
> practitioner testing on camera; this file does not have that yet. Mark anything you verify.

---

## 1. Studio Chat — the headline change

A natural-language assistant living inside the DAW project, aware of the project state: the tracks,
the audio on them, the effects on each track, the MIDI.

**Opening and closing it is the whole ergonomic point.** `Enter` opens it from anywhere, `Esc`
closes. There's a sparkles button too, but the flow the PM describes is: click a thing, hit `Enter`,
type an instruction, hit `Esc`, keep working. `1` flies the panel to the left-hand side where the
full conversation history is visible — use that for anything involving back-and-forth.

**The pattern is select-then-instruct.** Chat acts on what you have selected. Select a clip, say what
it should become.

What it does, from the demo:

| Ask | What happens |
|---|---|
| "rename all my tracks to something that makes more sense" | Session hygiene — renaming, colour-coding, cleanup. Producers asked for this specifically. |
| "add a bassline here, 70s inspired, electric bass" | Generates **new audio directly onto the timeline** at that position. Suno's musical brain is still inside the chat. |
| "how do I record into this?" | Teaches the product — tells you which buttons to click. It's a manual you can talk to. |
| "turn this into a rhythm electric guitar part" (MIDI clip selected) | Renders MIDI → audio as a named instrument. |
| "keep the lyrics the same but cover this into a new lead vocal performance" | **Cover in place**: replaces the selected audio with new audio holding the **same timing and melody**. |

**Chat prompt craft is the opposite of style-box prompt craft, and confusing the two will cost you
rounds.** The Style box is a bag of literal tokens — terse, no negation, front-load the important
word, ~35–45 words. The chat is a language model: write a plain instruction in full sentences, say
what you *don't* want, ask it questions, correct it in the next message. Everything in
`suno-tag-mechanics.md` is about the Style box and does **not** transfer here.

---

## 2. MIDI — notes you actually control

Studio now has two track types on the timeline: **audio tracks** (the familiar waveforms) and **MIDI
tracks** (horizontal bars = notes, like a piano roll).

**Getting notes in:**
- **Musical typing** — play chords and melodies on the computer keyboard, no hardware needed.
- **A MIDI keyboard** — plug in and play; recording onto the timeline works as in any DAW.
- **Knobs, faders and pads** (Launchpad-style controllers) are supported and **mappable to Studio
  parameters**.

**Editing notes:** drag a flubbed note to the right pitch, extend note lengths, delete an
ornament you don't like. Ordinary DAW piano-roll work — new to Suno.

**Hearing it:** built-in **MIDI instruments** audition the clip, *or* hand it to chat — "turn this
MIDI clip into a string quartet / a rhythm guitar part" — and it renders the notes as an audio
recording.

### Why this matters more to us than it looks

Three of our longest-standing "Suno can't do this" entries are really *"you can't say it in
words"* problems, and MIDI is a words-free channel into the model. All three are **untested with
2.0 — flag them as such if you recommend them:**

1. **Chord progressions as text are ignored** (`suno-controls-and-workflows.md` §11). The standing
   workaround was "render the progression and Cover the audio at ~40". **Now: play the voicing in,
   render it to the instrument you want.** Not all G majors are created equal was the PM's own
   example — voicing-level control is the point of the feature.
2. **Half-time drums — our single worst D&B blind spot** (§10.1). Controlled tests never got
   half-time out of a `breakdown` tag; the model appears not to hold the concept. **A drum pattern
   you program by hand doesn't need the model to hold the concept.** This is the most promising lead
   in the whole update for BadCode, and it is exactly the kind of claim to test before selling.
3. **Music-theory intervals in harmony prompts don't fire** (§11). Write the harmony line as notes
   instead.

---

## 3. Recording live audio

Two small additions that matter if anyone is singing or playing into Studio:

- **Latency calibration** — Studio clicks and listens back to measure round-trip latency, so takes
  land on the timeline where you actually played them. Run it **before** the first take of a session.
- **Count-in / pre-roll** — metronome clicks before recording starts (the demo used one bar).

Standard DAW hygiene, and the reason a recorded take used to arrive misaligned.

---

## 4. Cover in place — replacing a performance, keeping the timing

Select recorded audio, then instruct the chat to cover it. **It replaces the audio with new audio
that keeps the same timing and melody.** The demo took a rough laptop-mic vocal and turned it into a
produced lead vocal — with harmonies it didn't ask for — off one sentence.

Read this as: **a scratch take is now a valid way to specify a melody.** Hum or sing the line badly,
cover it into the real performance. That composes with the audio-seeding doctrine in §1 of the
controls doc, but at region level inside the arrangement rather than whole-song.

Timing was noted as imperfect in the demo, on camera, by the hosts. Expect drift.

---

## 5. Getting a specific word sung differently, in the same voice

The thing we most want. **Studio 2.0 does not do it, and nothing in the update claims to.** What it
does is put every primitive next to each other for the first time. The honest ladder, best first:

1. **Custom model of the song** (`suno-controls-and-workflows.md` §6 method 1) remains the only
   ~99.9% voice-preserving route, and 2.0 doesn't change it. Still the answer when the voice must
   not move.
2. **Isolate → dry → cover in place.** Advanced split the lead vocal → **remove effects** for a dry
   signal → select the region containing the word → chat: keep the lyrics the same, cover into a new
   lead vocal performance. Same timing and melody; **the voice is a new performance, not the old one
   patched** — pin identity with a saved Voice or custom model or it will drift.
3. **Sing it yourself and cover it.** Calibrate latency, count-in, record the corrected line, cover
   that clip into the vocal. Your phrasing, Suno's voice.
4. **The Editor's fixed-algorithm replacement** (§6 method 4) is still the only word-level tool, and
   it is still the worst one: single-word replacements fail, it rewrites melodies, it can flip the
   singer's gender.

**What is genuinely still missing:** region-level lyric respelling, any phoneme or pronunciation
control, and a splice-rather-than-regenerate mode. Cover regenerates a *performance*; it does not
patch a syllable. Every route above re-sings at least a line.

**The trend line is real, though.** Select-a-region + natural-language instruction + cover-in-place
are precisely the primitives that word-level surgery would be built on, and they all shipped in one
release. Watch for a "re-sing this word" affordance, pronunciation controls in the chat, or
per-syllable editing in the piano roll — any of those closes the gap.

---

## 6. Stem splitting and un-processing, inside Studio

Both confirm and extend `suno-controls-and-workflows.md` §9:

- **Advanced split** — you **name the instrument you want** ("lead vocal") rather than letting it
  detect everything. The PM's stated reason: naming it by ear gives **higher-fidelity stems**, and he
  uses advanced split every time. Results can be **inserted straight onto the timeline** directly
  below the original clip.
- **Remove effects** — right-click a clip → remove effects → get the **dry signal** back. Works on
  **audio you imported**, not just Suno's own. Pair it with the built-in effects to re-process to
  taste.

Remove-effects is the missing half of the stems doctrine: previously a processed vocal was
processed forever. It does **not** contradict the standing rule that baked-in sidechain pumping
can't be undone — that's arrangement dynamics, not an effect on a clip.

---

## 7. The effects rack, and automation

Each track now has a signal chain: an **instrument** at the head, then **audio effects** in series,
added from a picker via the "add audio effects" button. **Seven at launch**, more promised. From the
demo:

- **Reverb** — space and room.
- **Delay** — repeats; slap-back.
- **Distortion** — crunch and grit.
- **Compressor** — with a **sidechain input selectable from another track on the timeline**. The demo
  ducked a synth against the drums and pulled the threshold down for a dramatic pump.
- **EQ** — frequency balance; used in the demo to muffle a synth and open it up over time.

**A muted track still works as a sidechain source.** The demo's drums were muted on the timeline and
the PM called out that they must stay there — the compressor is keyed off them regardless. Easy to
break by deleting a track that "isn't doing anything".

**This gives us a real sidechain for the first time.** Our doctrine says Suno's pumping is baked into
the generation and can't be undone — that stands. But you can now *build* a genuine sidechain on
material you're arranging in Studio, which for D&B is the difference between imitation pump and the
real thing.

**Automation** (panel `3`) changes any parameter over time — the demo swept the EQ so a synth opens
up as it enters. Combined with real-time knob-turning, this is Suno's first tactile control surface.

---

## 8. Imagine your own plugin

The genuinely novel feature: **describe an audio effect in natural language and Studio builds it.**

The flow, from the demo:

1. Ask for it, naming the **controls you want** — the PM asked for a tremolo like an old organ
   rotary cabinet, with speed and depth (noting that "amount" would have worked too; it's natural
   language, it figures out the vocabulary).
2. Studio returns a **build plan** before building — for the rotary it proposed a dual-LFO design
   (separate bass and treble rotors), speed and depth controls, and a slow/fast switch. **Read it;
   this is the cheap place to correct the design.**
3. Approve, it builds, and it **names the plugin itself**.
4. Drag it onto a track. Real knobs, real-time.
5. It is **saved permanently to your library** under a new "Plugins" section, usable in any future
   project, and **you can keep iterating on it**.

Worth understanding what this is: a personal effects library nobody else has, described rather than
coded. For BadCode the obvious targets are the things we keep hand-building — a phone-line EQ for
the skit voices, a de-esser aimed at the 2–6 kHz sizzle that our D&B doctrine says to budget for, a
telephone/answering-machine chain, a tape-warble for the future-broadcast register.

Unverified: how good the DSP actually is, whether it survives complex requests, and whether the
generated UI reflects what the plugin does. The demo's own hosts were guessing what one knob
("warmth") would do before they heard it.

---

## 9. Shortcuts and quality of life

| Key | Panel |
|---|---|
| `Enter` | Open chat (from anywhere) |
| `Esc` | Close chat |
| `1` | Move chat to the left panel — full conversation history |
| `2` | Device view / signal chain (bottom) |
| `3` | Automation / take lanes |
| `4` | Library (right) |
| `Shift`+`Tab` | Piano roll instead of the device view |

Studio 1.0's panel shortcuts were kept deliberately. Also: the timeline was rebuilt to render faster
and hold playback with many tracks.

**Old projects are safe.** 2.0 is backwards compatible; opening a 1.0 project offers a modal choosing
the old or new interface, and nothing is lost in the new one — 2.0's features sit on top of 1.0's.

---

## Provenance

Distilled 2026-08-14 from **"Introducing Suno Studio 2.0"** (Suno Music official channel, published
2026-08-13, 21:34) — Luke interviewing Henry Phipps, product manager for Studio.

Retrieve the transcript with:

```bash
yt-dlp --write-auto-sub --sub-lang "en.*" --skip-download --sub-format vtt \
  -o suno-studio2 "https://www.youtube.com/watch?v=GZHp3WFc9Ps"
```

The video ends by pointing at a **playlist of deeper per-feature videos**, which is the obvious next
harvest when any of this needs to move from vendor-claim to tested.
