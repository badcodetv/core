# Suno Studio 2.0 — the app surface

**What lives where.** This file is the **surface**: what is actually in Studio 2.0 and how to drive
it — chat, MIDI, live recording, the effects rack, custom plugins, shortcuts.
[`suno-controls-and-workflows.md`](./suno-controls-and-workflows.md) **§8** is the **generation
craft** inside Studio — the three verbs (Create / Replace / Cover), exclude-styles discipline,
one-instrument prompt shapes, take lanes, the bootstrap trick. That section is still current: 2.0 is
**additive**, not a replacement.

> **Confidence: two vendor videos, no independent testing.** Both sources are Suno's own channel (see
> Provenance). The second is a 37-minute unedited start-to-finish build in which things visibly go
> wrong — takes land ahead of the beat, a vocal is audibly out of tune with no tool to fix it, stems
> come back unusable, inputs have to be re-selected by hand — so it is **much better evidence than a
> feature demo**, and roughly half of this file now rests on watching someone actually work rather
> than on claims. Still: it is the company demonstrating its own product, and nobody outside Suno has
> tested any of it. Treat **existence, location and mechanics** as solid; treat **quality** claims as
> open. Mark anything you verify.

**Contents.** 1 chat · 2 MIDI · 3 recording · 4 cover-in-place and "sing it in" · 5 the word-level
question · 6 stems and remove-effects · 7 effects rack · 8 custom plugins · 9 shortcuts ·
**10 editing on the timeline** · **11 two worked recipes** · **12 export, MIDI extraction, sharing** ·
**13 what's missing**. If you want the workflow rather than the feature list, start at **§11**.

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
| "can you add a chain of vocal effects here?" | Picks the effects *and dials in starting parameters* — EQ, compressor, reverb, delay in the demo. Treat it as a first pass to tweak by ear, not a finished sound. |
| "cover this onto a new audio track as keyboard" | Renders a selection to a **new** track rather than replacing in place. Say where the output should go. |

**Generations arrive as several options, and you commit one.** Audition alternates with the up/down
arrows, then commit. The other takes aren't lost — copy one down onto a spare track before
committing if you want both. In the demo two takes of the same synth part got panned hard left and
right to make a wide pad out of what was meant to be one part.

The chat also **suggests** instructions based on project state, which is a decent way to learn what
it will accept.

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
  `Cmd+K` (or the keyboard button, bottom right) shows the key→note map. **`Z` and `X` shift octave**
  — that's how you get down to bass range without a controller.
- **A MIDI keyboard** — plug in and play; recording onto the timeline works as in any DAW.
- **Knobs, faders and pads** (Launchpad-style controllers) are supported and **mappable to Studio
  parameters**.

**Recording:** **arm the track** with the red button on the track header — it shows which track is
listening. Unarmed tracks silently don't record.

**Editing notes:** drag a flubbed note to the right pitch, extend note lengths, delete an
ornament you don't like. Ordinary DAW piano-roll work — new to Suno. Plus:

- **Quantize** — select notes, hit quantize, they snap to the grid (quarter notes in the demo). The
  fix for a part played slightly out of time.
- ⚠️ **Notes dragged past the start of their clip get cut off.** Keep notes inside the clip bounds —
  an easy way to silently lose the first beat of a part.
- The bottom panel shows either the instrument/effects chain or the **piano roll**; double-clicking a
  clip opens the roll directly. (The two videos describe the `2` key slightly differently — one says
  device view, one says piano roll, with `Shift+Tab` swapping between them. Double-click always
  works; don't quote the shortcut with confidence.)

**Audio → MIDI:** drag an audio clip onto a MIDI track and Studio offers to **convert** it. So a part
you played or sang can become editable notes — then re-render it on any instrument, or export the
MIDI and use it in a real DAW.

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

- **Latency calibration** — point the mic at the speakers and run calibrate; Studio emits clicks and
  measures how long they take to travel back through the system (55 ms in the demo), then compensates
  so takes land where you played them. **It measures your specific rig**, so re-run it whenever the
  setup changes — different interface, headphones instead of speakers, a different room.
- **Count-in / pre-roll** — metronome clicks before recording starts (the demo used one bar).

Also: **arm the track** (red button) and **set the input** on the track header. Input selection is
not automatic and does not persist the way you'd expect — the PM had to re-pick it each time and
said so on camera. If a take records silence, that's the first thing to check.

Standard DAW hygiene, and the reason a recorded take used to arrive misaligned.

---

## 4. Cover in place, and "sing it in" — the technique that matters most

Select recorded audio, then instruct the chat to cover it. **It replaces the audio with new audio
that keeps the same timing and melody**, or renders to a new track if you ask for that ("cover this
onto a new audio track as keyboard").

**The important consequence: a bad performance is now a valid way to specify a part.** This is the
spine of the whole second video, used over and over:

- Guitar played badly into a laptop mic, aimed at the instrument "haphazardly", then: *make this a
  lead electric guitar solo, tasty* → a usable solo in the right place.
- A part hummed or sung in, covered into the instrument that should play it.
- MIDI chords played sloppily on a controller, quantized, then covered to a keyboard part.

You are not describing the part you want in words — **you are performing it, badly, and letting Suno
play it properly.** For anyone who can hum an idea but not play it, this is the single most useful
thing in Studio 2.0, and it sidesteps the whole problem that adjectives are weak in the Style box.

It composes with the audio-seeding doctrine in §1 of the controls doc, but at region level inside an
arrangement rather than whole-song. **Timing drift is real and visible in the demo** — see §10 for
the warp-marker fix.

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

**And there is no pitch correction at all.** Stated plainly in the second video — no tuning plugin
exists yet, and the PM flagged his own vocal as out of tune several times with nothing to do about
it but re-record or bury it under another take. So Studio cannot currently fix a *note*, let alone a
word. If a take needs tuning, that work happens outside Suno.

**The trend line is real, though.** Select-a-region + natural-language instruction + cover-in-place
are precisely the primitives that word-level surgery would be built on, and they all shipped in one
release. Watch for a "re-sing this word" affordance, pronunciation controls in the chat, or
per-syllable editing in the piano roll — any of those closes the gap.

---

## 6. Stem splitting and un-processing, inside Studio

Both confirm and extend `suno-controls-and-workflows.md` §9:

- **Advanced split** — right-click a clip → get stems → advanced mode → **name the instruments you
  want** (guitar, bass, lead vocal, drums, piano — you can ask for several at once) rather than
  letting it detect everything. The PM's stated reason: naming it by ear gives **higher-fidelity
  stems**, and he uses advanced split every time. **Insert all** drops the whole set onto the
  timeline **aligned to the original's timing**, so they're immediately usable as layers.
  Expect duds — in the demo one stem came back unusable and was simply discarded. Cherry-pick.
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
- **EQ** — frequency balance; used in the demo to muffle a synth and open it up over time, and to
  low-cut a vocal for brightness.
- **Noise gate** — cuts background noise between phrases. The fix for a vocal recorded in a room
  rather than a booth, which is all of ours.

**Two shortcuts worth knowing.** Ask the chat to *add a chain of vocal effects here* and it picks the
effects and sets starting parameters — a first pass to tweak, not a finished sound. And
**duplicating a track duplicates its whole effects chain**, which is the fast way to give a second
and third take the same processing instead of rebuilding it by hand.

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

| Key | Does |
|---|---|
| `Enter` | Open chat (from anywhere) |
| `Esc` | Close chat |
| `1` | Move chat to the left panel — full conversation history |
| `2` | Bottom panel — device view / signal chain (and per the second video, the piano roll) |
| `3` | Automation / take lanes |
| `4` | Library (right) |
| `Shift`+`Tab` | Swap the bottom panel between piano roll and device view |
| `Shift`+`T` then `A` / `M` | New audio track / new MIDI track |
| `Cmd`+`K` | Musical-typing key map |
| `Z` / `X` | Octave down / up when musical typing |
| `Cmd`+`E` | Split clip at playhead |
| `Cmd`+`D` | Duplicate (carries the track's effects chain with it) |

Double-clicking always works where a shortcut is uncertain: track header → effects panel, clip →
piano roll or audio inspector.

Studio 1.0's panel shortcuts were kept deliberately. Also: the timeline was rebuilt to render faster
and hold playback with many tracks.

**Old projects are safe.** 2.0 is backwards compatible; opening a 1.0 project offers a modal choosing
the old or new interface, and nothing is lost in the new one — 2.0's features sit on top of 1.0's.

---

## 10. Editing audio on the timeline

Ordinary DAW moves, all new to Suno, all used constantly in the second video:

- **The audio inspector** (double-click a clip) carries **warp markers**. Where a take drifts ahead
  of or behind the beat, lock a point in place and nudge the audio onto the grid. This is the fix for
  the timing drift that both videos show — and the reason a scratch take is salvageable rather than
  disposable.
- **Nudge a whole clip** when the entire take sits ahead of the beat, rather than warping inside it.
- **Reverse** a clip. In the demo a single snare hit became its own track, reversed into a riser
  leading to the outro — a good reminder that one-shot detail work is now possible in-app.
- **Fades** to remove a bad moment mid-take: fade out over the flubbed word instead of re-recording
  the line.
- **Pan** per track — two takes of the same part hard left and right is instant width.
- **Split** (`Cmd+E`) and **duplicate** (`Cmd+D`), which carries the effects chain.
- **Tempo** lives at the top and is drag-adjustable. Set it before recording anything.

---

## 11. Two worked recipes

### A. The blank-canvas build — order of operations

The second video is one 37-minute pass through this. The order matters more than any single step:

1. **Set the tempo first.** Everything grids to it.
2. **Lay a MIDI foundation** — `Shift+T` `M`, arm the track, play a part in with musical typing or a
   controller. Quantize it. Split and rearrange to sketch a structure.
3. **Shape it with effects** — EQ and reverb on the synth to push it back in the mix.
4. **Ask chat for the parts you can't play** — "add an ambient synth drone, lush, to accompany what's
   on the timeline". Audition the alternates, commit one, keep the other if it's useful.
5. **Calibrate the mic, then record the human parts** — vocal, then guitar, however rough.
6. **Fix timing with warp markers**, not by re-recording.
7. **Have chat rename the tracks** once there are more than a few. It's good at it.
8. **Process the recordings** — chat-built effect chain as a first pass, then tweak by ear.
9. **Cover the rough parts into real ones** (§4).
10. **Round-trip through Cover for an arrangement** (recipe B).
11. **Layer, mute, cherry-pick.** The final arrangement in the demo was human vocal + AI vocal
    underneath + harvested AI drums and guitar + played MIDI keys + a reversed snare.

The output is explicitly framed as **a demo that communicates a vision**, not a master. Worth
repeating to anyone who expects a finished record out of the box.

### B. The sketch → cover → stems round-trip

**The most valuable workflow in either video**, and the concrete version of the bootstrap trick in
`suno-controls-and-workflows.md` §8. Use it when you have an idea and a rough performance but no
arrangement:

1. Sketch the section in Studio, however scrappy — scratch vocal and one instrument is enough.
2. Select the region → **Export → full song**. It lands in your Suno **library**.
3. In the library: **Remix → Cover**. Suno auto-writes a style description — **edit it** (the demo
   changed "indie rock" to "indie folk" and that alone set the direction). This step currently means
   leaving Studio; Suno says it will be brought inside.
4. Generate, pick a take. **You are not looking for a finished song — you are looking for one or two
   elements worth stealing.**
5. Back in Studio: open the **library panel** (`4`), confirm you're in the **same workspace**, and
   drag the cover onto the timeline. **It auto-adjusts to the project tempo.**
6. Right-click → **get stems → advanced** → name what you want → **insert all**, arranged to the
   original timing.
7. Keep the two or three stems that are good, delete the rest, and layer them under your own
   performance.

**Why this matters to us specifically.** It inverts the usual Suno relationship: the human performance
stays the spine and Suno becomes the session band and arranger. That is exactly the
"more human contribution, the more defensible the release" argument in `suno-controls-and-workflows.md`
§13 — and for BadCode it's a credible route to tracks that don't sound like everyone else's Suno
output, because the melodies, timing and lyrics started with a person.

---

## 12. Export, MIDI extraction, and sharing

**Export** (upper right), three modes:
- **Full song** — bounces to your Suno library. This is the on-ramp to Cover, Remix and everything in
  the Create tab.
- **Selected time range** — bounce a section.
- **Multitrack** — renders every track separately and downloads a zip. **Rename tracks first** or the
  zip is unreadable (long-standing rule, still true).

**Per clip**, right-click → **download as WAV** or **download as MIDI**. Anything Suno generated can
leave as notes, not just audio — a generated keyboard part becomes MIDI you can re-voice on your own
instruments in a real DAW. Combined with the audio→MIDI conversion in §2, Studio is a usable
transcription tool.

**Share project** — project menu, upper left. Produces a link letting someone else **view and copy**
the project to make their own edit. **Not real-time** — no simultaneous editing, so collaboration is
send-a-link-back-and-forth. Relevant for Kai↔Jack: it works, but treat it as passing a file, not a
shared session.

---

## 13. What's missing — stated on camera

Useful for setting expectations, and a list to re-check when Suno ships updates:

- **No pitch correction / tuning plugin.** The biggest gap; see §5.
- **The Cover round-trip leaves Studio** (recipe B step 3). Promised to move in-app.
- **Input selection isn't automatic** and needs re-picking.
- **Sharing isn't real-time.**
- **One instrument type** (a wavetable synth) at launch; more promised.
- **Timing drift on generated parts** is common enough that warp markers are part of the normal loop.

---

## Provenance

Distilled 2026-08-14 from two videos on the **Suno Music** official channel, both featuring Henry
Phipps, product manager for Studio:

| Video | Published | What it gives |
|---|---|---|
| ["Introducing Suno Studio 2.0"](https://www.youtube.com/watch?v=GZHp3WFc9Ps) (21:34) | 2026-08-13 | The feature tour — interview format, polished |
| ["Getting Started in Suno Studio 2.0"](https://www.youtube.com/watch?v=35AzcYYucHs) (37:36) | 2026-08-14 | A full blank-canvas build with the mistakes left in — the source for §10–13 and most of the mechanics |

Retrieve a transcript with:

```bash
yt-dlp --write-auto-sub --sub-lang "en.*" --skip-download --sub-format vtt -o out "<url>"
```

Both videos point at a **playlist of deeper per-feature videos** (the individual plugins especially),
which is the next harvest when any of this needs to move from vendor-claim to tested.
