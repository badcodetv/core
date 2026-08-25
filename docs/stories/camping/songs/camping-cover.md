---
title: Camping (cover)
status: SETUP — cover mode live on suno.com/create, awaiting a creative brief. Nothing generated yet.
source_song: https://suno.com/song/299ef991-d51d-4384-a92f-974342a89714  # "Camping W - 75/65", v5.5, 3:56
parent_sheet: ./camping.md
released_take: ./camping-released.md
history: ./camping-prompt-history.md
workspace: camping-duet
model: v5.5
mode: Cover (Remix → Cover) — source audio attached, lyrics inherited, style rewritten
---
# Camping — the cover

**A cover, not a fresh generation.** The accepted round-17 take is attached as the audio
reference; the words are inherited unchanged. The only thing we iterate on is the **Style
box, the excludes and the three sliders**.

| | |
|---|---|
| **The accepted original** | [`./camping.md`](./camping.md) — round 17, the sheet this covers |
| **What a cover changes** | style + excludes + Weirdness / Style Influence / **Audio Influence** |
| **What a cover does NOT change** | the lyrics. They come with the source and stay verified |
| **Where takes land** | workspace `camping-duet` |

---

## 0. The brief

> _Awaiting Kai. One line: what should the cover **be**, and what must survive from the original._

**What must survive (default, until told otherwise):**
- Every word, in order.
- Two distinct men — Bob gravelly, Tarquin plummy. One-voice is still the failure mode.
- Played straight. The music never winks.

---

## 1. How the cover is driven

**The Cover screen is reached by hand, once.** Song page → `⋯` → **Remix ▸ Cover**. That
attaches the source audio and loads its lyrics into the create form. It is not automated and
does not need to be: it is one click per session.

🔴 **Never navigate away from `/create` while a cover is loaded.** Leaving the page drops the
attached audio and the whole form with it, and there is no draft recovery — the cover has to
be re-initiated by hand. The automation is safe here *because* `load()` only calls `goto()`
when the URL is not already `/create`.

Everything after that click is the normal
[`suno-automation`](../../../suno-gpt/automation.md) path:

```
npx tsx scripts/suno/suno.mts status                      # read the form back
npx tsx scripts/suno/suno.mts extract docs/stories/camping/songs/camping-cover.md "2. The four boxes" > /tmp/cover.json
npx tsx scripts/suno/suno.mts load /tmp/cover.json        # fills everything, spends nothing
npx tsx scripts/suno/suno.mts pair /tmp/cover.json        # 10 credits per Create, 2 takes each
```

**One gap in the tool.** `load()` only touches **Audio Influence** when a saved Voice is
attached — in cover mode there is no Voice, so the slider is left wherever the UI put it.
Until that is fixed, set `audioInfluence` in the spec **and** confirm it in `status` before
clicking Create. It is the single most important slider on this screen.

---

## 2. The four boxes

_Placeholders — the Style box below is the round-17 original, unchanged, so the first cover
round is a **control**: same words, same style, cover mode only. Rewrite it against the brief
in §0 before spending credits on anything else._

### Style

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: one long low detuned synth note; then the voice over a low palm-muted electric guitar riff — distorted rock tone, one short figure repeating, never a solo, never chords, running under every vocal section; then a dry chopped breakbeat under the vocal, no bass; then the drop, guitar out, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it, so synth and break are one piece of music, not a remix of one by the other. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

### Exclude Styles

```
singing, sung verses, sung chorus, melodic vocal, vocal melody, vocal hooks, crooning, clean sung melody, autotune, harmonies, grime MC, UK drill, road rap, trap, hip hop, young MC, American accent, American vocal, US rap, transatlantic, southern drawl, ragga MC, toasting, Jamaican accent, dancehall vocal, soprano, operatic vocals, vibrato, angelic voices, sustained vocal notes, female vocal, choir, orchestral strings, violins, cello, string section, piano, glockenspiel, brass band, marching band, oompah, dixieland, guitar solo, lead guitar, shredding, guitar strumming, power chords, acoustic guitar, wah, live rock band, epic trailer music, reggae, dub, ska, music hall, vaudeville, pantomime, ragtime, honky-tonk, liquid dnb, jump up, pop, lo-fi, jaunty, playful, whimsical, bouncy, comedic, novelty, parody, uplifting, major key, double time, tempo change, half-time, slow tempo
```

### Lyrics

```
INHERITED FROM THE SOURCE — do not paste. The cover carries the round-17 words already.
```

---

## 3. Settings

| Control | Value now (as loaded) | Notes |
|---|---|---|
| **Model** | v5.5 | matches the source |
| **Audio Influence** | **25** | how hard the original pulls. Low = free reinterpretation, high = a near-copy. **This is the cover's main dial** |
| **Style Influence** | 50 | the original sheet runs 75; 50 is Suno's cover default |
| **Weirdness** | 50 | the house pair is 30 / 60 — see below |
| **Duration** | Auto | source is 3:56 |
| **Voice** | none | never attach one: it triggers the Overwrite-Styles trap, and the answer there is always **Keep Current** |
| **Workspace** | `camping-duet` | set before Create — it routes the output |

**Run the pair.** Every attempt goes at **weirdness 30 and 60**, per the house rule; which one
wins is still an open question and a cover is no reason to skip the check. If a round is being
spent to test Audio Influence instead, say so in the log and hold weirdness fixed — **one
variable per round**.

---

## 4. Round log

_One row per Create. Diagnose before rewording — see [`session-method`](../../../suno-gpt/session-method.md)._

| # | Change (one variable) | AI / SI / W | Title | Verdict |
|---|---|---|---|---|
| — | _nothing generated yet_ | 25 / 50 / 50 | — | — |
