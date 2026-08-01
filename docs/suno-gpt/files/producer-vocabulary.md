# Producer Vocabulary

A Suno prompt is only as good as the words available to describe the target sound. This is the
working vocabulary of a producer, with what each term *means*, so it can be chosen deliberately
rather than sprinkled.

Use it two ways: to **translate** a vague brief into specifics, and to **debug** a prompt that isn't
landing (usually there's a word doing the wrong job, or a missing word doing no job at all).

> **Provenance.** Distilled from the ChillPanic corpus (see `docs/suno-gpt/README.md`), including
> his general music-production teaching, not just his Suno material.

---

## The three word-classes to layer, in order

After you have the basic skeleton (genre, mood, instruments, vocals), upgrade a prompt in three
passes. This is a *procedure*, not a checklist:

1. **Emotion pass** — replace the generic feeling word with a precise one.
2. **Texture pass** — ask "if I could touch this sound, how would it feel?"
3. **Production pass** — dry/wet, sparse/dense, wide/mono, polished/lo-fi.

Worked example of all three, starting from `sad piano music`:

- emotion → `melancholic, forlorn, somber`
- texture → `cavernous, hollow, distant`
- production → `wet reverb, lush, shimmering, long decay, ambient, wide, polished`

### Sharpening an emotion word

Never ship a generic emotion word. Ask an LLM for **synonyms *with definitions*** — the definitions
are the point, because they let you articulate which *version* of the feeling you mean. There are
many kinds of sad; the generic word gets you something that could equally be read as a lullaby.

---

## Texture words, and what they buy you

| Word | Effect |
|---|---|
| `glassy` | Clean and bright — like clinking wine glasses |
| `velvety` | Soft and warm |
| `dusty` | Vintage-record grime |
| `hollow` | Slightly empty, resonant, **less mid-range presence** |
| `cavernous` | Huge and echoey — implies a big room and heavy reverb |
| `distant` | Source pushed far from the listener |
| `warm` | Restores the mids that `hollow` removes |
| `intimate` / `close mic feel` | Source pulled right up to the listener |

These combine predictably: `cavernous + hollow + distant` tells Suno *big space, heavy reverb, far
away, thin in the mids*.

### Texture words have antagonists — never use both sides

| | vs | |
|---|---|---|
| `hollow` | ⟷ | `warm` |
| `intimate` / `close mic feel` | ⟷ | `wide` |
| `sparse` | ⟷ | `dense` |
| `polished` | ⟷ | `lo-fi` / `vinyl` |

When two words pull opposite ways, Suno averages them into mush. **Delete one — don't add a third
word to arbitrate.**

---

## Drums & percussion

- **Transient** — the initial attack spike of a hit. "Bringing out the transient" is what makes a
  kick or snare punch through.
- **Punchy** vs **distorted** — the two main axes for a kick or 808. Punchy = short, tight,
  transient-forward. Distorted = saturated, long, aggressive.
- **Four on the floor** — kick on every beat.
- **Drum fill** — the short rhythmic break announcing a section change.
- **Blast beats** — extremely fast alternating kick/snare (metal).
- **Boom bap** — 90s hip-hop drum idiom, swung and sample-based.
- **Trap hi-hat rolls / triplet hi-hats** — the fast subdivided figures that define trap.
- **Velocity variation** — differing hit strengths so programmed drums read as *played*. The
  most-cited "make it sound real" move.
- **Snap** vs **clap** — a snap is thinner and higher; a clap has more body and energy.
- **Small room reverb clap** vs **stadium claps** — tight and intimate, or layered and huge.
- **Mono choke** — one-voice retrigger, so each hit cuts off the previous. Essential for 808s and
  sub basses, or the tails overlap into mush.
- **Soft clipper** on the kick/snare bus — rounds peaks so you can push level without audible
  distortion.

## Bass

- **Sub bass** — the fundamental low weight; usually just a **sine wave**. Simple by design.
- **Layering** — a professional bass is never one sound. The standard stack: sine sub for weight, a
  **detuned saw** on top low-passed for harmonics, and a **distorted, high-passed, widened** layer so
  the bass survives on phone speakers.
- **Legato + mono** — makes notes *slide* into each other rather than retrigger.
- **Sample-and-hold LFO on the filter cutoff** — randomises the cutoff per note, adding life and
  unpredictability. Directly applicable to D&B.
- **Reese bass** — the detuned, moving, growling bass that defines much of D&B.
- **Sidechain / ducking** — bass drops in volume when the kick hits so they don't fight.
- **Notch filtering** — surgical narrow cuts; earns its keep on neuro bass.

## Guitars & rock

- **Fingerpicked** vs **strummed** — the two acoustic articulations.
- **Rhythm** vs **lead** guitar — separate roles, separately requestable.
- **Double-tracked / panned guitars** — one part hard left, another right. A tell of realistic rock
  production.
- **Guttural lows** — the low death-growl register.
- **Dissonant chord stabs**, **breakdown**, **riff**, **pinch harmonics**, **slides** — structural
  metal vocabulary.
- **Guitar tone** is itself a legitimate prompt axis — "a completely different guitar tone" is a real
  and audible difference between generations.

## Vocals

**Registers** (all usable directly as tags): **falsetto** (light, floating, above natural range),
**chest voice** (full-bodied, speech-adjacent), **head voice**, **mix voice** (a blend), **belted**
(loud, pushed), **whispered**, **breathy**, **intimate**. Naming **two adjacent registers** is a
useful way to describe a voice that moves between them.

- **Close mic feel** — present, detailed, no room. The three-way realism distinction that matters:
  a vocal *in the room with you* (natural space) vs *right up against you* (close mic) vs *pasted on
  top* (dry and disconnected).
- **Harmony stacks** — layered harmony vocals. A third is +4 semitones, a fifth +7 or −5. (Suno does
  not reliably understand these as words — see `suno-controls-and-workflows.md` §11.)
- **Vocal chop** — a sliced vocal fragment used as an instrument.
- **Ad-lib** — the interjection between lines.
- **Sibilance** — harsh "s"/"t" energy; a **de-esser** attenuates it.
- **Melisma** — multiple notes sung on one syllable.

**Describe a vocal *arc*, not a state.** This is the highest-leverage vocal technique: give the voice
somewhere to start and somewhere to end. `shifting from soft verses to belted melodic refrains`;
`alternating between snarled mid-range aggression and clean chant-like sections`. That's the
difference between "female vocal" and a performance.

## Synths & sound design

- **Plucky** — short decay, percussive, no sustain.
- **Super saw / saw stack** — many detuned saws layered; the big wide EDM chord sound.
- **Detune** — copies slightly off-pitch, for thickness and movement.
- **Pad** — sustained, background, harmonic bed.
- **Arpeggio / arp** — chord notes in sequence. A background arp, washed out with big reverb and
  delay, is a stated pro-vs-amateur tell.
- **Waveform character:** **sine** = pure and smooth; **square** = hollow and buzzy; **saw** = bright
  and buzzy. The generalising principle: *the faster a waveform moves between loud and quiet, the
  more distorted and crunchy it sounds.*
- **Filter cutoff sweep** — automating a low-pass upward is *the* fundamental "building" gesture in
  electronic music.
- **LFO** — a slow oscillator modulating something. **Sample-and-hold LFO** = stepped random values.
- **Bit crusher** — reduced bit depth for lo-fi digital grit.
- **Convolution reverb** — imprints the character of one sound onto another; a powerful way to make
  found sound musical (clattering pots convolved with a chord become tuned stabs).
- **Trans gate** — gates a sustained sound into a rhythmic pattern.

## Distortion & saturation

- **Saturation** — gentle harmonic distortion; warmth and perceived loudness.
- **Soft clipping** — leaves quiet material alone, rounds only the loudest peaks. Loudness without
  obvious distortion.
- **Waveshaping** — gentle curves = soft even distortion; jagged sharp lines = intense, chaotic,
  glitchy.
- **Crushed / squashed** — heavy compression plus saturation; shrinks a big sound and tucks it behind
  the mix while keeping it huge.

## Space: reverb, delay, width

- **Dry** vs **wet**. A fully wet reverb send is how you get "washed out".
- **Decay** — how long the tail lasts. **Small room** (tight) vs **hall** (big, distant) vs
  **shimmer** (pitched-up, ethereal).
- **Slapback** — a single short delay. A much better request than "reverb" when you want *small
  space* rather than *long tail*.
- **Ping-pong delay** — echoes alternate left and right; the main width-generator on vocals.
- **Feedback** — how many times the echo repeats. **Delay cutoff** — low-passing so repeats get
  progressively darker.
- **Reverse reverb swell** — reverse a sample, drench it, reverse again: a rising wash that lands
  exactly on the entry it precedes. The standard intro→verse transition.
- **The comb model of stereo width** — mono at the bottom of the spectrum, progressively wider toward
  the top. Sub stays centred; highs go wide.

## Transitions & arrangement furniture

**The vocabulary most worth having, because Suno never supplies these** — and they're what makes a
track feel intentional rather than generated.

- **Riser / uplifter** — rising sound building tension into a section. Should **fade in**.
- **Downlifter** — falling sound at a section change, releasing energy. Should **fade out**. Reversed,
  it becomes a riser.
- **Noise sweep** — filtered white noise moving across the spectrum.
- **Impact / boom** — the low-end hit landing on a downbeat.
- **Build** — the section before the drop: risers, downlifters, impacts, opening filter.
- **Drop** — the payoff. **Drops work by being sparse.** Density *before* the drop, space *in* it.
- **Ambience bed** — continuous background texture (birds, ocean, room tone) under the whole track,
  subtle enough that you only notice it when muted. "Breathes life into the production."

## Mixing vocabulary

- **EQ filter types:** **high-pass** (removes lows), **low-pass** (removes highs), **low/high shelf**
  (broad boost or cut of everything below/above a point), **peaking/bell** (around one frequency),
  **notch** (very narrow cut).
- **Q** — band width. High Q = narrow and surgical; low Q = wide and musical.
- **Frequency landmarks:** ~100 Hz where things get **muddy**; **400–700 Hz** where vocals collect
  **boxy** resonance worth dipping; **2–6 kHz** where AI **hiss and sizzle** live; the top end for
  **air**.
- **Carving** — cutting a range from one element so another can occupy it.
- **Compression:** **threshold** (level at which it engages), **ratio** (how hard), **knee** (how
  abruptly), **attack** (*longer attack preserves transients*), **release**. A **limiter** is the
  extreme case — a ceiling the signal cannot exceed.
- **Headroom** — unused space below 0 dB. Leave −6 to −3 dB before mastering.
- **LUFS** — integrated loudness. Heavy electronic music typically runs roughly −5 to −3.

---

## Song structure

**Sections:** intro, verse, pre-chorus, chorus (or **drop** in electronic music), post-drop, verse 2,
bridge, breakdown, outro.

**The six building blocks and their jobs:**

| Section | Job |
|---|---|
| Intro | Sets mood. **Decides everything** — it's where the listener chooses to continue. Best device: tease a fragment of the chorus vocal up front |
| Verse | Tells the story. Melody constant, lyrics change |
| Pre-chorus | Builds tension. 2–4 lines, the rollercoaster climb |
| Chorus | The emotional anchor. **Same lyrics and melody every appearance** |
| Bridge | The curveball. Appears **once, in the back half** — different melody, energy, perspective |
| Outro | Closes the door |

### Three structures, and how to force each

- **Strophic** — only `[Verse 1]`, `[Verse 2]`, `[Verse 3]`. Same melody each stanza, lyrics change,
  no chorus. All attention lands on the words. **The right default for a heavily narrative track.**
- **Verse–chorus** — roughly 90% of songs. Paste the *identical* chorus each time; vary only the
  final one with escalation cues.
- **Through-composed** — no repetition, keeps evolving. **Because `[Verse]`/`[Chorus]` tags actively
  cause repetition, you must abandon them** and use invented section names: `[Opening]`,
  `[Development A]`, `[Acceleration]`, `[Expansion]`.

### Genre silently overrides structure

The style-box genre biases structure independently of your tags, because Suno absorbed each genre's
structural tropes. Ask for a folk ballad and it leans strophic; ask for pop and it wants
verse-chorus whether you asked or not. **Pick the genre whose native trope *is* the structure you
want**, or expect to fight it.

### Other structural rules that survive contact with Suno

- **Get to the chorus inside ~50 seconds.** A Suno verse runs ~18s and a pre-chorus adds 4–8s, so
  verse + short pre-chorus + chorus fits comfortably. At most one pre-chorus, 1–2 lines.
- **Melodic math** — answering lines should match syllable counts. Suno *compensates* for uneven
  lines by cramming the delivery faster, so this is really about retaining control of phrasing.
- **Emotional arc** — contrast the sections. Uniform intensity means no dynamic range.
- **Density as structure** — build dense, drop sparse.
- **The background is the tell.** Foreground parts are easy; the layers you're not consciously
  hearing are what make a track sound professional.
- **Adapting existing text?** Find the line that already repeats — that's your chorus. If nothing
  repeats, plant it before choosing a structure.

---

## How to judge a generation — four separate axes

Conflating these is why feedback on AI output is usually useless. They pull in different directions
and a track can win on two and lose on two.

| Axis | Question |
|---|---|
| **Creativity** | Is it doing something unexpected? (Not the same as good) |
| **Prompt adherence** | Did the named elements actually appear? Check literally, item by item |
| **Fidelity** | Audio quality and mix balance — mid-heavy? clean? stereo separation? |
| **Realism** | Does it sound *performed and in a room*, or assembled? |

---

## Finding words you don't have

- **Look up the instruments.** "What instruments are common in `<subgenre>`" — then name 2–3 real
  ones. Otherwise Suno fills in genre defaults and you lose the lever that most distinguishes
  subgenres from each other.
- **Lateral genre search.** Ask for subgenres of the genre you're in. Spotify has catalogued 6,000+
  genres; most people use ten. **You cannot prompt a word you don't know.**
- **Run a reference track through a genre detector** to learn the actual genre words for a sound you
  like but can't name.
- **Use an LLM to translate intent into producer vocabulary** — but not every time. Building the
  habit of describing sound yourself is the skill that compounds.
