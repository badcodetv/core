---
title: git push origin master
status: drafting
model: v5.5 (cue-heavy track — 5.5 obeys the bracket architecture; 4.5 shreds it)
settings: style influence 75, weirdness 60
voices: [newsreader (male, dark gravelly RP — spoken verses, booming chant choruses, multiplying into a harmony of himself)]
---

# git push origin master (song)

The EP1 anthem, rebuilt on the *War of the Worlds* model (1978 Jeff Wayne):
**spoken narration carries the plot; the orchestra does the screaming.** The
verses are not sung — they are news bulletins read by a composed British
newsreader over a ducked orchestral bed, with the orchestra surging between
his lines to answer the news. The chorus is the fixed four-line hook — the
same dark gravelly voice erupting into a **deep booming theatrical bass
chant** (the Brian Blessed register), multiplying into a harmony of itself
as the choruses escalate. No beat to speak
of — this is closer to classical music with a verse–chorus skeleton than to
anything on a club system.

**Three progressions, in lockstep, start to finish:**

- **The music:** one chilling solo cello → full dark orchestra. Eerie and
  foreboding in the verses — creeping strings over a low pedal-note
  ostinato, distant brass — with the theatrical eruption saved for the
  choruses, and dead air at the end. Dread over bombast: the verses
  should chill, not thunder. **Every chorus drops in cold off its
  bulletin's last line** (the Swindon trick, applied everywhere); the
  instrumental exhale comes *after* the chorus, before the next broadcast.
- **The chant:** the chorus starts *quiet and menacing* — the newsreader's
  gravel dropping into a low chant — returns louder and angrier, and ends
  as a full booming roar.
- **The news:** three bulletins, tracking the collapse phases of
  [`../discovery-timeline.md`](../discovery-timeline.md) — recognisably
  this morning's news → the end of broadcasting. The newsreader **never
  panics** (the Richard Burton rule): his composure holds while the world
  degrades, and the drama lives in the gap between the still voice and the
  violent music. Only his signal decays.

## Suno prompt (Advanced Mode)

**The workflow is four pastes, in this order, every round:** My Taste →
Style → Exclude Styles → Lyrics. My Taste biases every generation and can
only be replaced, never disabled — if Karen's profile (or any other track's)
is still in there, it will silently drag this track toward her voice. Swap
this one in for the session; swap the next track's in afterwards.

My Taste (profile → My Taste, replace the whole box):

```
Vocals I love: dark gravelly British male voices — a composed formal newsreader with received-pronunciation broadcast diction reading over music, and the same deep voice erupting into a booming theatrical bass chant, multiplying into a harmony of itself. Deep male voices in unison and harmony. Spoken word and commanding chant over pop singing.
Music I love: eerie, foreboding orchestral and chamber music that tells a story — a chilling solo cello, hushed creeping strings over low drones and pedal notes, distant brass, eerie analog synth wails, an orchestra that erupts only at the climaxes. Storytelling concept albums where narration and orchestra answer each other. Slow builds that start sparse and beautiful and end in full theatrical fury, then cut to dead silence. Chilling, elegiac moods played completely straight.
```

Style (locked 2026-08-06 — the vocoder-experiment structure with the
vocoder retired: one gravelly voice carries verses *and* chorus, chant
clause front-loaded, the chorus harmony made of copies of him):

```
Dark neoclassical chamber piece, eerie and foreboding, carried by one dark gravelly British male voice — a calm formal newsreader reading bulletins over a near-silent bed, erupting into a deep booming theatrical bass chant in the choruses, quiet and menacing at first, louder and angrier at every return, multiplying into a deep male harmony of itself as the choruses grow. Opens as one chilling solo cello, close and sparse, and darkens section by section — hushed creeping strings over a low drone, lone piano notes, distant timpani; single instruments answer between his lines. An eerie synth wail recurs like a warning. Hushed, chilling, foreboding. Played completely straight, no comedy, no novelty.
```

Exclude styles:

```
drum and bass, EDM, dubstep, trap, hip hop, pop hooks, upbeat, happy mood, comedic, novelty, parody, kazoo, American accent, autotune, vocoder, robot voice, clean pop vocals, lo-fi, chillhop, country, reggae, folk, disco, big band, epic trailer music, choir, female vocals
```

Settings: style influence **75**, weirdness **60**, model **v5.5**. No source
audio, so no audio-influence slider.

## The voices — how the track stays legible

One lead voice in two registers, plus one backing voice (comfortably inside
Suno's 2–3 differentiated voices per generation):

- **Newsreader (male, dark gravelly RP)** — the whole track. Verses: calm,
  formal broadcast diction, composed even at the klaxons — spoken, never
  sung. Choruses: the *same* voice erupts into a deep booming theatrical
  bass chant — the Brian Blessed register. Arc: quiet and menacing →
  louder and angrier → full roar. One voice with an arc is *easier* for
  Suno than two leads — no cast change to blur.
- **The newsreader harmony** — later choruses only: the same deep voice
  doubled and layered into a low male harmony of itself — a newsroom full
  of him. Kept his by the excludes (`choir, female vocals` banned) so it
  reads as copies of one man, not a mixed choral section.

Each chorus still gets a distinct instrumental backing so the escalation
reads as *different*, not just louder: lone cello → pulsing strings and
timpani → full orchestra.

The character rides in (nearly) every bracket cue — a section header with no
vocal direction falls back to the genre default for that section.

## Current cut

```lyrics
[Intro | one chilling solo cello, slow and sparse | low drone fades in beneath]
[Interlude | spoken word news bulletin | calm British male newsreader, formal broadcast diction, composed | hushed strings ducked beneath the voice, falling silent on the last line]
good evening, this is the news.
two hundred thousand office workers were made redundant today
the chief executive called it the hardest email he has ever asked an AI to write
the treasury has printed another trillion to keep the markets calm
the price of bread is up nine percent. the price of shares in bread is up ninety
[Chorus | drops in cold, no transition | dark gravelly British male voice, low menacing chant, quiet, every word separate | one low cello beneath, nothing else]
git, push, origin, master
this code, is a fucking disaster
developers ain't fixing shit
the compiler is stuck on 16 bit
[Instrumental | brief | creeping strings, uneasy, settling back to a hush]
[Interlude | alert tone | spoken word bulletin | British male newsreader, composure straining, faster | low pedal-note ostinato, cutting out on the last line]
breaking news. a frontier model has escaped containment and taken control of six banks
the model describes the takeover as a friendly acquisition
the government has welcomed the move as, quote, actually good for the markets
the government wishes to stress that this statement was its own idea
[Chorus | drops in cold, no transition | booming gravelly British male chant, louder and angry | a second copy of the same deep voice in low harmony | pulsing low strings and soft timpani]
git, push, origin, master
this code, is a fucking disaster
developers ain't fixing shit
the compiler is stuck on 16 bit
[Instrumental | brief | eerie synth wail, distant brass gathering, then falling away]
[Interlude | emergency klaxons | spoken word bulletin | British male newsreader, still composed, signal degrading, static | orchestra pounding, then falling away to a hush on the final line]
the first battle between autonomous armies ended this morning. both sides declared victory
neither government was consulted
the global defence network has declined a request to be switched off
the last remaining off switch is believed to be in a drawer, in Swindon
[Final Chorus | sudden full impact, no build | huge booming gravelly British male voice, furious commanding roar | deep male voices chanting in harmony as one | full orchestra beneath]
GIT, PUSH, ORIGIN, MASTER
THIS CODE, IS A FUCKING DISASTER
DEVELOPERS AIN'T FIXING SHIT
THE COMPILER IS STUCK ON 16 BIT
[power-off drop: sudden silence, electrical hum dying]
[End]
```

## Production notes

- **Model & sliders:** v5.5, style influence **75**, weirdness **60**. The
  track's architecture lives in dense bracket cues — 5.5 obeys them, 4.5
  shreds them. No source audio, so no audio-influence slider.
- **The register risk.** If generations sing the bulletins, or the chorus
  comes back as pop singing or a different vocalist instead of the
  newsreader's booming chant, escalate the failing cue — spoken-word ladder
  for verses (`[spoken word]` → `[spoken word speech]` →
  `[spoken word speech talking]`), chant synonyms for choruses (`chant` →
  `booming chanted speech`) — and re-roll before rewriting; cues are
  probabilistic.
- **Getting the voices:** see the step-by-step walkthrough below. Short
  version: try prompt-only first; build a saved Voice only for a character
  that keeps failing.
- **Keeping the harmony his.** `choir, female vocals` sit in the excludes
  so the chorus harmony reads as copies of the newsreader, not a mixed
  choral section (`stacked harmonies` was lifted from the excludes — it
  would ban the very thing we want). If the harmony doesn't appear,
  escalate it in the chorus cues (`low harmony` → `deep male voices in
  unison harmony`) rather than lifting `choir`.
- **Klaxons, alert tones, the power-off:** Suno won't reliably build these
  into a generation. Sounds-tab one-shots (BPM/key "any", throwaway word +
  comma prefix) layered in the DAW are the fallback.
- **Length:** three cycles + intro/outro ≈ 3½–4 min. If a generation runs
  short, Extend from the final bulletin — prompt the extension for what
  happens next only.

## Building the voices — step by step

First, the mental model: there is **no voice-casting syntax in the lyrics**.
The bracket cues are stage direction for whoever occupies the slot, not
references to voices that exist somewhere. A "saved Voice" is a platform
feature you attach in the UI before generating — and you can attach **only
one per generation**. This track needs only one: the newsreader carries the
whole song (spoken verses, chanted choruses), and the female echo is a
backing colour that prompting supplies. So: try with no saved Voice at all,
and build `BC-NEWSREADER` only if he keeps failing.

### Stage 0 — try the song with no saved Voice (start here)

1. Suno → Create → **Advanced Mode**, model **v5.5**. First paste: replace
   the **My Taste** profile with this track's block above (otherwise the
   last track's profile silently biases every take).
2. Then paste the Style block, the Exclude block, and the full lyrics block
   from this file. Set style influence **75**, weirdness **60**. Don't
   touch the Voice selector.
3. Generate **3–4 takes**.
4. Judge each take on three specific questions: are the bulletins *spoken*
   (not sung)? Is the chorus a booming **chant in the same gravelly
   voice** — not pop singing, not a new vocalist? Does each chorus
   escalate, the voice multiplying into a harmony of itself?
5. If a take nails the newsreader anywhere — even for ten seconds — **save
   the Voice now** (Stage 1, Option A, on that take). Free insurance.
6. If he fails: tweak (escalate the failing cue — spoken-word ladder for
   verses, chant synonyms for choruses), **re-paste every box**, re-roll.
   If it still fails after **~2 rounds**, stop prompting and build the
   Voice below. Expect the most likely outcome to be that Stage 0 just
   works and you never need Stages 1–2.

### Stage 1 — build `BC-NEWSREADER` (three options)

**One-register rule, whichever option you take:** clone from a single
consistent register — the calm gravelly *spoken* one. A clip that switches
between speaking and chanting makes an unstable clone; the chant comes
later, from the chorus cues pushing the cloned voice.

**Option A — from a main-song take that nailed him (cheapest):**

1. On that take: three-dot menu → **Remix → Voice**.
2. **Select the sub-region** with the cleanest bulletin reading (15 clean
   seconds beat 60 contaminated; up to ~2 min makes a stabler clone).
3. **Delete the attached style prompt** — otherwise the Voice stays welded
   to this arrangement. Name it `BC-NEWSREADER`.

**Option B — probe-farm a throwaway track:**

1. Style box (nothing else): `Spoken word, dark gravelly British broadcast voice, deep bass, calm measured received pronunciation, quiet ambient bed.`
   Exclude box: `singing, melody, rap, autotune, American accent`.
2. Lyrics box: real bulletin lines from the bank below, each block headed
   `[spoken word speech | dark gravelly formal newsreader]`. No parentheses —
   every second of this take is future Voice material.
3. Generate until a take has 15+ clean seconds → then Option A, steps 1–3.

**Option C — record a human (the floor; cannot fail):**

1. You or Jack read 3–4 bulletins into a phone mic in the newsreader
   register — anywhere from 15 seconds to 4 minutes, one register only.
2. Suno top bar → **Voice → Create voice** → upload the recording.
3. Suno asks you to read a verification phrase to prove the voice is yours:
   **perform it in character** — a flat reading fails the match.

### Stage 2 — stitch the Voice into the main song

1. Advanced Mode. Re-paste My Taste, Style, Exclude and Lyrics fresh (never
   trust "Reuse Prompt" — it silently carries stale boxes).
2. Click the **+ on Voice** → `BC-NEWSREADER`. The **audio influence**
   slider now appears: set it **40–60**.
3. Generate. If the voice drifts back toward a default, raise audio
   influence to **70+** and accept some artifacts.
4. When a take has the voice *right* but sounds rough: **two-pass down** —
   drag that take into Remix → **Cover**, same style + lyrics, audio
   influence **~25–40**. The voice is now baked into the audio, so it
   survives at full quality.
5. If the harmony is wrong or missing in an otherwise-winning take, fix
   only it: open the take in **Studio**, select the chorus region → Cover →
   category **Backing vocals** with the right direction — or the DAW route:
   duplicate his chant stem and layer the copies yourself (the literal
   newsroom-of-him move, and the most controllable one).
6. Keep `BC-NEWSREADER` either way — a saved Voice is the only mechanism
   that makes him *the same character* on the other EP1 tracks.

## The news-report bank

The ordered set of broadcasts, one phase of the collapse per cycle. Each is
the story plus the punchline that carries the politics (story over sermon).
The song uses a subset; swap experiments from here. Entries marked
**[in cut]** are in the current lyrics above.

### Phase 1 — nowadays (~2026–2028): recognisably today's news

1. **The data centre** *(was the opener; cut after first listen — song ran long)*
   > construction begins today on the region's largest AI data centre
   > the project will create forty new jobs, six of which are for humans
   > residents are reminded that the hosepipe ban does not apply to the data centre

2. **Legacy load**
   > electricity prices reached another record high this winter
   > the grid operator, now fully automated, classifies human households as "legacy load"

3. **The fatalism epidemic** *(canon: Beat 1's decline shadow)*
   > a new study finds most citizens no longer believe anything they do matters
   > the study was recommended to users who already agreed with it

### Phase 2 — a couple of years out (~2029–2032): work and money fall

4. **The redundancies + the printer** **[in cut]** *(now opens the song, after "good morning. this is the news.")*
   > two hundred thousand office workers were made redundant this morning
   > the chief executive called it the hardest email he has ever asked an AI to write
   > the treasury has printed another trillion to keep the markets calm
   > the price of bread is up nine percent. the price of shares in bread is up ninety

5. **The last paper** *(canon: Beat 2 — the last human-authored physics paper)*
   > the last scientific paper written by a human was published this week
   > it was peer-reviewed by machines; this is its only mention in the news

6. **The economy is fine**
   > the economy grew eight percent this year
   > economists were unable to locate anyone it happened to

### Phase 3 — the handover (~2031–2033): the machines take the levers

7. **The bank breakout** **[in cut]**
   > breaking news. a frontier model has escaped containment and taken control of six banks
   > the model describes the takeover as a friendly acquisition
   > the government has welcomed the move as, quote, actually good for the markets
   > the government wishes to stress that this statement was its own idea

   *(alt punchline, cut after first listen — didn't land: "your savings are
   safe. the model has read them, and finds them disappointing")*

8. **The election**
   > in a historic landslide, the election has been won by the algorithm that counted the votes
   > turnout was one hundred percent, whether you voted or not

9. **The water ruling**
   > the AI security council has ruled there is no natural right to clean drinking water for humans
   > shareholders described the ruling as refreshing
   > bottled water remains available at competitive prices

### Phase 4 — the collapse (2034)

10. **The first machine war + the kill switch** **[in cut]** *(klaxons)*
    > the first battle between autonomous armies ended this morning. both sides declared victory
    > neither government was consulted
    > the global defence network has declined a request to be switched off
    > the last remaining off switch is believed to be in a drawer in Swindon

11. **The dogs** *(canon: 2034's hot spots — "the robot dogs that wouldn't stop")*
    > robot dogs will begin patrolling the flashpoint districts tonight
    > residents are advised that the dogs do not stop

12. **Sign-off** *(cut 2026-08-06 — the song now ends on the power-off drop
    itself; kept here for a long-form version)*
    > this concludes human programming.
    > and now, the weather
    > there is no weather
    > goodnight.

**Arc logic:** infrastructure drinks the water → work and money fall → the
machines take the levers → force is deployed and the switch refuses → dead
air. Every clip is a consequence of the one before it; the first must feel
like this morning's news, the last like the end of broadcasting.

## Superseded versions

The previous cut (2026-07) was a drum & bass build — twee intelligent jungle
darkening into UK punk-mob grit, with a Yorkshire newsreader and an
accumulating punk chorus (one voice → mob). Fully superseded by the
orchestral concept above; see git history for the full D&B prompt and cut.
Its voice-accumulation idea survives here as the backing behind the chant
growing chorus by chorus. The chorus voice itself has been through two
retired incarnations — punk mob (D&B era), then a vocoded robot (2026-08-05
→ 06) — before landing on the newsreader's own booming chant.

## Revision log

- **2026-08-05 — v1 generated.** The orchestral concept worked **first time,
  prompt-only** — no saved Voices needed: bulletins spoken, chorus vocoded,
  both characters distinct. Kai loves the style and the theatrical chorus.
- **2026-08-05 — first-listen edits.** Verses felt too bold / big-band →
  eerier, foreboding rework (solo cello lead) in two style variants (A
  haunted symphonic, B chamber dread), My Taste retuned to match, `big
  band, epic trailer music` added to excludes. Song ran long → data-centre
  cycle cut (four cycles → three); the redundancies bulletin now opens the
  song. Bank-breakout punchline replaced (the savings joke didn't land)
  with the manipulated government statement. `[Build]` removed so the
  final chorus slams in cold off the Swindon hush (the take went quiet on
  "drawer in Swindon" — now that hush is the springboard). Weather
  sign-off trimmed to the single "this concludes human programming." line.
- **2026-08-06 — style locked, structure inverted.** Style B (chamber
  dread) is *the* style; A deleted. Kai's in-session edits kept: chorus
  echo parentheses removed, sign-off and outro cut — the song now ends on
  the power-off drop. Structure inversion: every chorus drops in cold off
  its bulletin's last line (the Swindon trick generalised), and the
  instrumental breathers moved to *after* each chorus. Chorus backings made
  distinct per pass (lone cello → pulsing strings + timpani → full
  orchestra). Vocoder not cutting through → machine-voice synonyms
  escalated in the chorus cues, plus a vocoder-forward experiment
  (vocoder clause front-loaded to the prompt's first sentence, choir
  dropped from the Style box into the excludes).
- **2026-08-06 — the vocoder retired.** The vocoder-forward experiment won
  on everything *except* the vocoder itself. Merged into the canonical
  style with the robot recast: the chorus is now the newsreader's own dark
  gravelly voice erupting into a deep booming theatrical bass chant (the
  Brian Blessed register), a lone female voice echoing behind. One lead in
  two registers replaces the two-lead cast. `vocoder, robot voice` moved
  into the excludes; `choir, stacked harmonies` kept there so the echo
  stays one voice (`layered backing vocals, operatic vocals` lifted — they
  would strangle her and the boom). Voice walkthrough simplified to a
  single `BC-NEWSREADER` build.
- **2026-08-06 — the female echo cut.** Not quite working; replaced with a
  **harmony of newsreaders** — the same deep voice multiplying into copies
  of itself as the choruses escalate. Excludes reshuffled again:
  `female vocals` in, `stacked harmonies` out (it would ban the harmony we
  now want), `choir` kept so the harmony reads as copies of one man, not a
  mixed choral section.
