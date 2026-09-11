# Suno v6 — what changed, and what it lets us do

> 🔑 **House rule (Kai, 2026-09-10): all new Suno work is v6, in the new UI.** The v5.5 era is
> archived in [`../archive/v5.5-era.md`](../archive/v5.5-era.md) — read it only to understand an
> old sheet, or to Cover an old take onto v6.

**v6 shipped 2026-09-09 and retired every older model from the create form.** This file is the
v6 layer on top of the rest of `docs/suno-gpt/`. Where it disagrees with an older file on a
*model* or *control* question, **this file wins** — the older files were written against v5.5.
Where it is silent, the older file still stands (prompt grammar, the voice playbook, the atom,
the satire trap, the narration recipe).

> **Confidence: day-one evidence.** Distilled on 2026-09-10 from 11 launch-day YouTube videos and
> a 20-agent web sweep — full claim ledger with every source and tier in
> [`docs/misc/2026-09-10-suno-v6-research.md`](../../misc/2026-09-10-suno-v6-research.md).
> Nobody — us included — has measured anything yet: every "sounds the same" is by ear, no audio
> has been diffed, no controlled grid exists. Two of the videos are paid Suno sponsorships
> (Music Tech Info, Arcade): their click-paths are facts, their verdicts count for less. Reddit
> and Discord were unreachable. **Tier words used below:** *vendor* (Suno said it), *tested*
> (someone did it on camera), *reported* (one person says so), *untested* (our inference).
> **Anything we verify gets written back here with a date.**

**Contents.** 1 the models · 2 the create form · **3 fixing one word, one bar, one phrase** ·
4 Studio with v6 · 5 new things worth suggesting · 6 stems, quality, downloads · 7 voices and
custom models · 8 prompt craft deltas · 9 vocals and D&B · 10 our v5.5 back catalogue ·
11 known bugs · 12 the test queue

---

## 1. The models

Three models, one family. **v4, v4.5, v5 and v5.5 cannot be selected for a new generation** —
old songs stay playable and downloadable, and Cover and Extend still work on them (vendor email).

| | **v6** | **v6 Wild** | **v6 Mini** |
|---|---|---|---|
| In-app copy (verbatim) | "Powerful, versatile, and refined… our best model yet." | "Best for experimental ideas where you're pushing the envelope." | "A free, more efficient version of premium V6 models." |
| Suno's framing | reliable, precise, steerable | "less predictable and more varied"; CPO Jack Brody: "**less tuned towards preferences than v6**" — a deliberate fix for mainstream overfitting, aimed at niche genres | fast, high-volume, free tier |
| Tested strengths | punchier kick and snare, fuller bass, better reverb; beat v5.5 on vocal clarity in 7/7 genres (voice-clone A/B vs pre-launch v5.5 takes, not same-day); follows a long plain-English brief closely | more character in indie rock, R&B, metal; much wilder on the same hummed melody | never generated on camera |
| Tested weaknesses | rock still drifts to a country/southern vocal; metal and blues-rock still artifact | a quality drop vs v6 (worse guitars and drums, "AI-artifact-y"); lyrics drift from the brief; voice fidelity swings either way by genre; one take came back at ~50 s | free plan: no downloads, no commercial rights |
| Plan | Pro / Premier ("Pro" badge) | Pro / Premier ("Pro" badge) | everyone |

**In-app labels are contested** — read aloud as `V6 Pro`, `Version 6 Pro`, `V6`, `V6 - Wild`,
`V6 Wild Pro`, `Version 6 Mini`. Most likely: v6 / v6 Wild / v6 Mini, with a **Pro badge**
presenters read as part of the name. **Custom models sit in the same dropdown**, plus a
"Create Custom Model (Beta)" entry (reported: 100 credits). Never match a label exactly.

### Which to pick (our ruling-in-waiting — untested by us)

- **Default: v6.** Finished D&B, anything carrying a saved Voice or the narrator.
- **v6 Wild when you are hunting** — a texture, a drop idea, a niche sub-genre the pop-tuned
  model flattens (our neurofunk and half-time failures are exactly that theory). **Then Cover the
  winner into v6** for fidelity. That is both Suno's stated intent and two presenters' method — it
  replaces the old "ideas in 4.5, Cover into 5.5" hybrid move.
- **v6 Mini: never.** We're on a paid plan and nothing is known about its quality.
- Wild is "like the old weirdness slider, except the choice now lives in the model." So in a grid,
  **model and weirdness are two different axes that overlap** — don't read a Wild win as proof
  that high weirdness would have done the same.

---

## 2. The create form on v6

### ✅ Read off our own live form, 2026-09-10 (account `binocarlos`, Premier)

These labels are **proven** — they supersede the video readings in the table after this one.

| Control | Exact labels | Default on a clean form |
|---|---|---|
| Tabs | **Simple · Advanced · Sounds** (no "Custom" tab) | Advanced |
| Model menu | **`v6`** *Pro* "Powerful. Versatile. Refined. Our best model yet." · **`v6-wild`** *Pro* "Best for experimental ideas." · **`v6-mini`** "A free, more efficient version of premium v6 models." · **Create Custom Model** *Beta* "Create a model based on your uploads (100 Credits)" | v6 |
| Variety | a 5-step slider — **Off** "Exact style" · **Normal** "Balanced variety" · **High** "Distinct styles" · **Extra** "Bold exploration" · **Max** "Unreasonably varied" | Normal |
| Max Mode | **Off / On** | Off |
| Vocal Gender | **Male / Female** — neither selected is a valid state | neither |
| Duration | **Custom / Auto** | Auto |
| Weirdness | 0–100, caption "Expected results" at 50 | 50 |
| Style Influence | 0–100, caption "Moderate" at 50 | 50 |
| Personalize | a single button labelled **My Taste** (plus an info icon) | not selected — 🔑 **and it stays that way: always off** |

🔴 **Suno switches the model on its own.** Our form showed a toast: *"Model changed — Model was
automatically changed to support your selected conditions."* So a model you set is not a model
that stays set — the loader reads it back after everything else, before Create.

🔑 **Personalize is ALWAYS OFF, and we don't use My Taste** (Kai, 2026-09-10): *"stop trying to
use the My Taste box and always have personalize off when we generate a song, because then each
song becomes an atomic unit."* In our own logs My Taste only ever caused damage, never a better
take. Each song is now its three boxes plus its settings, and nothing hidden. The loader forces
Personalize off and refuses a spec that asks for it on.

### What the launch videos said (kept for the *what it does* column)

Most of it is the form we know. What is **new or changed**:

| Control (as read) | Where | Values | Default | What it does | Tier |
|---|---|---|---|---|---|
| **Model** | top of the form; also per track in Studio, in Studio chat, and in the Remix dialog | v6 / v6 Wild / v6 Mini / your custom models | ⬜ | picks the engine; v5.5 is gone | tested |
| **Simple / Advanced** tabs | top | — | — | every v6 source says **Advanced**, none shows a "Custom" tab; Audio and Cover may now be *post-upload modes* (`Edit vocals` / `Edit instruments` / `Cover`) rather than tabs | tested (tabs) / untested (the rename) |
| **Add** (the "+") | Simple | Audio · Image · Video · Voice · playlist · styles from your library | — | seeds the song from media. **A song attached here + an instruction = an EDIT of that song** (§3) | tested |
| **Variety** 🆕 | More Options, **only with a v6-family model** | named steps, low → high: *Exact style* / "Clips use the same style" · **Normal** · *Balanced variety* · *Distinct styles* · **Unreasonably varied** (order assembled from garbled captions) | **Normal** (3 agree) | how different the **two takes of one Create** are from each other — variety *between* the pair, not within a song. **Mechanism (vendor, 2026-09-11):** Suno's v6 FAQ says Variety works by "adjusting and updating your style prompts… reduce the Variety slider to 0" to keep control ([help.suno.com/en/articles/13924481](https://help.suno.com/en/articles/13924481)) — so anything above **Off** lets Suno rewrite the Style box. One pro tester: "didn't seem to work for me." | tested (labels, default) / vendor (rewrites the Style box) / untested (audible effect) |
| **Personalize** 🆕 | next to Variety | on / off | off (one account) | help text: "**Make variety match your taste**". Written evidence says it is "a Personalize toggle labelled **My Taste**" — i.e. the first create-form switch for My Taste. **If true, My Taste only bites when it is on.** 🔴 Unconfirmed live — see §12 test 4 | tested (label) / reported (the My Taste link) |
| **Max Mode** | Advanced, near Variety | on / off | ⬜ | now a **real toggle**, not the viral code block (which remains placebo). Vendor-adjacent copy: "for consistency across longer songs, and for Covers and Voices". Credit cost **unknown** | tested (exists) / reported (effect) |
| **Vocal Gender** | Advanced | Male / Female (others unknown) | ⬜ | pins the vocalist's gender; leave unset when a Voice supplies it | tested |
| Weirdness · Style Influence | More Options | 0–100 | 50 / 50 (reported) | unchanged | tested |
| Audio Influence | More Options, **only with audio or a Voice attached** | 0–100 | ⬜ | unchanged — still the cheapest proof nothing is attached | tested |
| Duration | Advanced | Auto / Custom | ⬜ | unchanged — but **v6 on Auto runs longer than v5.5 did in 5 of 7 genres** (folk 3:34 vs 2:39). Always set it | tested |
| Limits | — | Simple 3,000 · Style 1,000 · Studio prompt 1,000 · max **8 minutes** per generation on all three models | — | Lyrics cap not re-checked | tested / vendor |
| Create | bottom | — | — | still **two takes per Create** — Suno's v6 FAQ: "Each time you generate, you make two songs with a total cost of 10 credits." ([help.suno.com/en/articles/13924481](https://help.suno.com/en/articles/13924481), read 2026-09-11). Generation is **much faster** — a queue of six finished "almost instantly" | vendor (two takes) / tested (speed) |

**Stale strings to ignore:** the Voice area still says "V5.5 powers…", and the Voices help page
still says "Confirm that model v5.5 is selected". Both predate v6 — Voice and custom models are
tested working on v6.

🔑 **For code-driving:** every new control is form state, and form state persists (the
2026-08-27 law). Since 2026-09-10 `suno.mts` sets **and reads back** all five — model, Variety,
Max Mode, Vocal Gender, Personalize — on every load and every grid cell, and refuses a spec with
no `model`. Mechanics: [`../automation.md`](../automation.md) §9.

---

## 3. 🔑 Fixing one word, one bar, one phrase

**The question we care about most.** A take is right except for one word, or one bar needs the
backing pulled out, or one line's cadence is wrong — and until now the answer was "regenerate."
v6's launch copy says, verbatim: *"Update a single lyric without rebuilding the entire song.
Change one word or line while leaving the rest intact."* That is a vendor claim. Here is what the
evidence actually supports.

Four different problems — the ladder differs for each:

| | What's wrong | Best route | Confidence |
|---|---|---|---|
| **A** | the **wrong word** is sung (text change) | **rung 1** — attach + instruction | tested twice, by ear |
| **B** | the right word is sung **badly** (same text, re-sing it) | rung 1 with unchanged text, then rung 2 / 2b | 🔴 untested anywhere |
| **C** | the **backing** must go for one bar | **rung 3** — stems + a mute in Premiere | deterministic |
| **D** | the **cadence** of one bar must change | rung 4 — guide vocal in Studio (a new take) | reported once |

### Rung 1 — the v6 edit: attach the song, type the change 🆕

1. Create → **Simple**.
2. **Add** → **Audio** → pick the finished song from your library.
3. Type the instruction as one full sentence, scoped as tightly as you can:
   > *Change the word summer to sunset everywhere it appears in this song. Keep everything else
   > exactly the same.*
4. Model **v6** → **Create**.

**What you should hear:** same voice, same instrumental, same arrangement — only the word moves.
Two independent on-camera tests got exactly that (AI Tune Craft: summer→sunset at all three
occurrences; Arcade, sponsored: never→always throughout, native Suno track).

**Failure signs, all tested:**
- 🔴 **The instrumental corrupts** — 3 of 3 when the song was an **uploaded external MP3** and
  the edit swapped **several multi-word phrases of different syllable counts** (MoneOnDaBeat).
- 🔴 **The whole song restyles** — an instruction worded globally ("have it all sung in operatic
  choir") changed everything.
- 🔴 **Half a compound instruction is ignored** — "swap the Voice, the custom model and the
  genre" did not apply the Voice. **One change per edit.**

**Our working boundary (untested inference):** one word, **same syllable count**, on a **native
Suno take** — works. Multi-word, different syllables, uploaded audio — breaks. Everything between
is unknown.

**Unknowns that decide whether this is a real fix:** whether it can target **one occurrence**
("in the third line of the second verse only"); whether it fixes a **mispronunciation with the
text unchanged** (problem B); what it costs; and whether the audio *outside* the word is kept or
regenerated to sound the same. It returns a **new clip**, and the global-restyle result hints
it is a tightly conditioned full regeneration rather than a splice. **Null-test before trusting
it** — §12 test 1.

For one-occurrence wording, borrow the Lyricist's phrasing (which edits text, not audio):
*"Replace street lamp with neon light in the third line of the second verse, keeping the rhyme
and line length unchanged."*

### Rung 2 — Replace Section (the Song Editor)

The older tool — dates from 2024, never tested on v6, though an undated help page says Replace
Section is now "powered by v6". It re-sings a **whole window**, not a word.

- Song → **⋯ More Actions** → **Edit** → **Replace Section**; or in the newer Song Editor,
  highlight a region → orange **Quick Replace** (or **Replace** / **Edit Lyrics**) → edit the
  **Replace Lyrics** box → **Replace Section** → pick from the **Edits Library**, **Generate
  More** for alternatives, drag the boundary line to move the seam.
- Window: **10–30 s** per the 2024 note; the current help page states no limit. Pad the
  selection with clean audio both sides — **15–20 s** was the practitioner advice.
- For **problem B**, leave the lyrics **unchanged** and regenerate the smallest window around
  the word, choosing between the two candidates (untested, but it is the natural use).
- **Failure signs (pre-v6 reports):** audible seams on tight selections; melody changes when
  told to keep it; **hiss "as if two versions were playing" after chained edits — never edit an
  edit**; single-word swaps misalign stress, so regenerate the line.

### Rung 2b — Studio "Regenerate Section"

Drag on the waveform in Studio — "**this could be 2 seconds or 30 seconds**" — and regenerate;
credits scale with the length selected (HookGenius, Feb 2026, pre-v6). The **finest selector
anyone has documented.** Whether it still exists under that name, and how well it keeps the
voice, are unknown.

### Rung 3 — stems + a mute (the only certain one)

For **problem C**. Nothing is regenerated, so the voice is identical by construction.

1. Song → **Edit** → **Get stems or MIDI** → **Lead vocal** + **Everything but lead vocal**
   (or **Open in Suno Studio** → **Multi-track**, or Studio **Export** → **multi-track**, a zip
   of one file per track).
2. In Premiere, cut or mute *Everything but lead vocal* for the bar, then sum.

**Failure signs:** exported stems print **quieter** than in-app, and one Studio stem came back
**offset in time** — **null the stems against the mix before comping**. Separation is
regenerative, so expect artifacts (weak isolated bass, baked-in guitar processing).
🔴 **This costs a download** unless Studio exports are exempt (§6). **Downloads stay human** —
Kai spends that allowance, never a script.

### Rung 4 — a new take in Studio, comped in

For **problem D**, and for B when rungs 1–2 fail. A **fresh performance**, not a patch.

- **Vocal region:** select a region on the vocal track → type the lyric plus a vocal-style
  prompt → model v6 or Wild → generate → cycle takes with the **up/down arrows**. If the bar
  count doesn't match the selection it offers "generate on a new vocal track". It follows the
  chords and key with good phrasing; timbre was still "lasery, phazy, metallic", and the loop
  marker was fiddly to resize.
- **Cadence:** record a scratch vocal of the bar *with the phrasing you want* and use it as the
  guide — the only cadence lever anyone found (reported once). This is "sing it in"
  ([`suno-studio.md`](./suno-studio.md) §4) aimed at one bar.
- Pin the identity with a saved Voice or custom model, or the new take drifts.

### Further down

- **Remove Effects** (right-click a Studio clip) for baked reverb — did not rescue a v6 guitar
  with baked-in processing.
- **Cover the whole song on v6** — an *upgrade* path, "pretty similar", not a fix (§10).
- **Remaster** (⋯ → Create → Remaster) claims to keep "structure, lyrics, melody and vocal
  performance" — vendor snippet only, v6 target unconfirmed. Three levels (vendor,
  [help.suno.com/en/articles/8105281](https://help.suno.com/en/articles/8105281), read
  2026-09-11): **Subtle** "very close to the original", **Normal** "slight variations", **High**
  "possible changes to musical elements and vocals". Untested by us.
- **An external voice-cloning tool** over a good performance in the wrong voice.
- **Regenerate the song** — the old baseline.

### What still cannot be done (2026-09-10)

- **No true punch-in.** Nobody has shown one word re-sung with every other sample of the take
  untouched — nor null-tested any of the rungs.
- **Nothing changes cadence in one bar while keeping the take.** Suno's word is "section", never
  "bar".
- **No pitch correction** in Studio (unchanged).
- **Suno's own product chief says bar-level precision is manual:** CPO Jack Brody — "natural
  language will never be better" for hand-precise edits; "You can just move the waveform."
  So the division is official: **plain-language edits for words and sections, Studio hands for
  bars, Premiere for anything that must be exact.**

---

## 4. Studio with v6 — click-paths

What's new or re-confirmed. The Studio 2.0 surface itself is [`suno-studio.md`](./suno-studio.md).

| To do this | Do this | Tier |
|---|---|---|
| Generate a part on a v6 model | Add a track → generation prompt → **model** dropdown → e.g. **V6 Wild** | tested |
| Generate from text alone | switch the track's **reference** off, then prompt. Studio prefers a reference but doesn't need one | tested |
| Skip the instrument category | just describe it — "acoustic guitar, guitar licks, hammer ons" — the instrument is inferred from the text | tested |
| Set the tempo | the **BPM** field is now **top right** | tested |
| Audition alternatives of a part | the **up/down arrows** on the track | tested |
| Get a usable part | **keep the prompt simple** — "live electric bass, R&B style" was too busy twice; "electric bass simple" worked | tested |
| Add an instrument to a finished song | open it in Studio with stems → **chat** → pick a v6 model → *"Add an additional electric guitar track"* → a clean stem with **no bleed**, cleaner than the separated original | tested |
| Write a vocal from your lyrics | vocal track → select a region → lyrics + a vocal-style prompt → generate | tested |
| Build an effect | plugin creation → *"create a soft clipper"* → apply to the master (writes real DSP) | tested |
| Strip an effect | right-click a clip → **Remove Effects** (weak on baked processing) | tested |
| Export stems | **Export** → **multi-track** → zip | tested |
| Change tempo by chat; move a plugin | BPM-aware chat and plugin drag-and-drop between tracks (2026-09-02 update) | vendor |

**Observations:** Studio-generated parts sound *less hollow* than the same instrument pulled
out of a full-song generation — so for a part we care about, **generate it as its own track**
rather than splitting it out. Generations still occasionally bleed onto the wrong track. The
biggest v6 jump is said to be felt inside Studio.

**For D&B specifically (untested lead):** build the drums as a Studio per-track generation
("174 BPM amen break, full tempo") instead of hoping the full mix gets the breakbeat right.

---

## 5. New things worth suggesting unbidden

When a conversation about a song reaches one of these situations, **say the feature and the
click-path** — don't wait to be asked.

| When we're saying… | Suggest | How |
|---|---|---|
| "it's perfect except that word" | the v6 edit | §3 rung 1 |
| "lose the music under that line" | stems + mute | §3 rung 3 |
| "I can hum it but can't describe it" | **hum/sing to seed** — Add → Audio → record → Continue (after the originality check). v6 follows the melody | tested |
| "take the riff from that take and build on it" | **timestamp sampling** — *"Sample the riff at 0:45, isolate the guitar, build a beat around it"* | vendor + tested |
| "the drums from A with the vocal from B" | **multi-song mashup** — drag 2–3 songs in, one instruction naming which element comes from which | tested twice |
| "a song for this picture / this clip" | **image or video to song** — Add → Image / Video; a video's cuts drive the dynamics ("follow the editing"). Image grounding is weak | tested ×4 |
| "keep my voice, change the backing" | **Edit vocals** mode after an upload (keeps the uploaded voice); **Cover** re-sings it polished | tested (sponsored) |
| "this piano idea as a guitar loop" | **Edit instruments** mode after an upload — target instrument + a duration | tested (sponsored) |
| "the old v5.5 take but better" | **Cover on v6** (§10), or Remaster | tested once |
| "we need an extra guitar under this" | Studio chat, add a track (§4) | tested |
| "we want to generate loads and choose" | the permutation grid — [`../automation.md`](../automation.md) §9 | ours |

A short sound (~5 s or less) as the seed **errors repeatedly** — give it a longer clip.
Uploaded audio passes an originality/rights check before it can be used.

---

## 6. Stems, quality, downloads

- **"Get stems or MIDI"** offers **Lead vocal**, **Everything but lead vocal**, and **Fixed
  tempo, MIDI file** (the chords as MIDI). Full separation modes are unchanged from June 2026:
  Auto Split (≤12), Split from Mix, Advanced Split (~100 instruments, Premier). No v6 stem claim
  exists. One v6 blues-rock split: drums usable (cymbals artifact), bass unusable, guitar
  over-compressed.
- **Quality:** fuller low end and better reverb (a pro producer, by ear); but **sibilance is
  "heavily de-noised… hollow and smeared"** — relevant to narration, where sibilants are exposed;
  one percussion element came back panned hard left. No sample-rate or loudness figures exist.
  **Our delivery-QC gate (`scripts/delivery-qc.sh`) applies unchanged.**
- **Downloads (vendor, 2026-09-03):** Pro 20/month, Premier 60/month; one song = one download
  whatever the format; the cap covers **old songs too**; commercial use only for songs downloaded
  within the allowance; removing Suno's inaudible watermark is prohibited. **Studio exports may
  be exempt** — three sources lean that way (Premier "unlimited exports inside Suno Studio"), none
  is conclusive. Watch the counter the first time a human does one.
- **Credit cost per v6 generation: unknown.** Pro now gets 2,500/month and Premier 10,000/month,
  so the old "10 credits per Create" may not hold. **Log the balance before and after every
  Create** until it is known.

---

## 7. Voices, custom models, consistency

- **Voice works on v6** (tested in a 7-genre A/B and elsewhere). Persona is now "Voices".
- **Custom models run on v6** (vendor: "Fine-tune v6 on your own tracks") and sit in the model
  list. **Switch the custom model off to test base-model behaviour** — it is easy to forget it is
  selected.
- One pro tester found a **custom model more consistent than a Voice** ("almost consistent but
  not 100%"), and **custom model + Voice together** fixed a genre-default vocal drift. That is a
  new rung for our voice ladder — [`suno-voices.md`](../suno-voices.md).
- **Wild's voice fidelity swings** by genre — furthest from the source on a ballad, closest on
  indie rock. Carry a Voice on **v6** unless the point is the texture.
- **Judge a voice in the quiet sections.** Sparse verses reveal identity; dense choruses hide it.
- A saved Voice still has **no section scope** — wrong for a duet. Nothing in v6 changes that.
- **Lyricist and Inspo: no v6 information at all.**

---

## 8. Prompt craft deltas

- **Long plain-English briefs work** on v6 — a jargon-free paragraph with a bridge instruction
  and a stripped-back ending was followed closely (3 agree). Our short skeleton still stands; this
  widens what's safe.
- **Metatag doubt, one A/B:** a plain LLM-written prompt beat a metatag-heavy one on hip-hop.
  Consistent with our existing stance — prefer plain production language.
- **The same boxes do not reproduce an old take on v6** (tested: a v5 song's style + lyrics
  gave a different song on both v6 and Wild). An accepted v5.5 sheet is a **starting point**, not
  a recipe — see §10.
- Exclude Styles, the 1,000-char Style cap and section tags carry over unchanged.
- **A plain-language edit is a separate grammar** — full sentences, one change, scoped ("in the
  second verse only… keep everything else exactly the same"). Label which box it goes in, like
  Studio chat.
- **Variety rewrites your Style box** — now vendor-sourced (2026-09-11): the v6 FAQ says it works
  by "adjusting and updating your style prompts" and to "reduce the Variety slider to 0" to keep
  control ([help.suno.com/en/articles/13924481](https://help.suno.com/en/articles/13924481)).
  Above **Off**, the boxes you wrote are not the whole song — set Variety **Off** when the atom
  must hold.

---

## 9. Vocals and drum & bass

- **Duets:** explicit `Male vocal` / `Female vocal` under section tags gave a real alternating
  duet; "male and female" in a Simple style also worked. Still no duet control — our "cut on the
  seam" rule stands. **Vocal Gender** is now a first-class control.
- **Accents:** rock still defaults to a country/southern vocal (3/3, even with Max Mode); the fix
  was custom model + Voice. **No UK-accent evidence of any kind** — our narrator needs our own
  test. Our rule that nationality rides on the genre tag stays in force until tested.
- **Speech / narration:** no v6 evidence anywhere. Our dry-and-separate method and "Getting a man
  to TALK" recipe stand. New lever to test: a **Studio vocal track** from typed lyrics.
- **D&B:** a lazy `liquid DnB` prompt came back as **two-step drums** ("that does not sound like
  D&B"); an **engineered** breakcore/jungle prompt worked on both models — *"aggressive breakcore
  instrumental, rapid chop, jungle breaks, hyperdetail percussion, dark synth bassline, euphoric
  melodic chops"*. **Name the drum mechanics, not the sub-genre** — the same lesson as our
  riddim/neurofunk notes, now with a v6 data point. Half-time is **not known to be fixed**.
- No dedicated BPM or key field on the create form — still typed into Style.

---

## 10. Our v5.5 back catalogue

- **No accepted v5.5 sheet can be re-run on v5.5** — the Camping duet (accepted round 17), the
  GPOM narration, Karen. A re-run on v6 is a **new song**.
- To carry a v5.5 take forward, **Cover it on v6** — tested once as "pretty similar", fixing
  harshness, "rounder, wider"; best of several attempts, so budget a few. Remaster is the
  untested lighter touch.
- **Every song sheet's `model:` frontmatter now matters**: record `v6`, `v6-wild` or the custom
  model's name, plus Variety, Max Mode and Personalize, or the take is not reproducible.
- **Archiving old masters:** one presenter predicts v5-and-under downloads may be purged within
  ~6 months — a prediction only, but the cap already applies to old songs. **Kai's call** whether
  to spend allowance archiving v5.5 masters now.

---

## 11. Known bugs and gotchas

| | |
|---|---|
| v5.5 gone | old sheets can't be re-run; the loader still reads whatever model is selected |
| Plain-language edits | corrupt the instrumental on multi-phrase swaps of uploaded audio (3/3); apply half a compound instruction; a global wording restyles the whole song |
| Wild | quality drop, artifacts, a spontaneous ~50 s take |
| Mix | hollow sibilance; a hard-panned percussion element; metal "chugs" bleed into sung sections |
| Stems | exports quieter than in-app; one time-shifted; Remove Effects weak on baked processing |
| Studio | bleed onto the wrong track; fiddly loop marker |
| Seeds | clips ≲5 s error out |
| Variety | no audible effect in one test |
| Docs lag | the sliders help page doesn't list Variety; Voices help still says v5.5 only |

---

## 12. The test queue — what we should run ourselves

In priority order. Every one goes through one Suno tab, `status` first, the credit balance
logged before and after.

1. 🔑 **Null-test the one-word edit (rung 1).** Finished v6 take → Simple → attach → *"Change the
   word X to Y in the second verse only. Keep everything else exactly the same."* Phase-invert
   the edit against the original in ffmpeg, time-aligned. Does anything outside the word survive
   the null? Repeat with the **same text re-sung** (problem B) and with a one-occurrence target.
2. **The same null test on Replace Section and Studio Regenerate Section** — smallest region each
   accepts on v6, and whether the words outside it keep the take.
3. ✅ **Map the live create form** — done 2026-09-10 (§2's live table; `suno.mts` upgraded).
   Still open inside it: what Personalize's "My Taste" button does, and the Simple attach menu.
4. **The kazoo check** *(optional, confirms the 2026-09-10 ruling)* — put an absurd profile in My
   Taste ("only kazoos and yodelling"), generate one plain pair with Personalize **off**. No kazoos
   = the profile is kept out, and the box's contents stop mattering entirely.
5. **Our D&B on v6 vs Wild** — grid round R1 (`automation.md` §9).
6. **The narrator Voice on v6 and Wild** — quiet-section timbre, UK accent, sibilance.
7. **Variety** — does it change how far apart the two takes are?
8. **Max Mode** — consistency against the credit delta.
9. **Credit cost** of v6, Wild, Max Mode and an edit.
10. **Backing out of one bar via stems + a Premiere mute** — Kai approves the download.
11. **Does a Studio multi-track export draw on the download allowance?** (human)
12. **Cover and Remaster a v5.5 take on v6** — does it keep the performance?
13. Can Cover pick Wild? Can Extend or Remix use v6 on a v5.5 song?
14. **Cadence in one bar** — guide vocal vs a "triplet cadence" instruction. Expect failure; record it.
15. **A Studio vocal track as dry narration.**
16. Lyricist and Inspo on v6.
17. **Re-sweep in a week** — r/SunoAI, Discord, help.suno.com — when community tests exist.

---

## Provenance

- 2026-09-10 — created from the v6 research workflow: 11 launch-day videos (ChillPanic; Busy
  Works Beats; AI Creatives Connect ×2; Chris Wieduwilt / The AI Musicpreneur; AI Tune Craft;
  Lanewood Studios; Music Tech Info; MoneOnDaBeat; Arcade) + Suno's blog, release notes, pricing
  and help centre + press (TechCrunch, Music Ally, weraveyou, DMN, MBW). Ledger:
  [`docs/misc/2026-09-10-suno-v6-research.md`](../../misc/2026-09-10-suno-v6-research.md).
- 2026-09-11 — a capped web sweep (13 searches) sourced two claims from Suno's own help centre:
  Variety rewrites the Style box, and two takes per Create (v6 FAQ,
  [help.suno.com/en/articles/13924481](https://help.suno.com/en/articles/13924481)); and added the
  three Remaster levels ([help.suno.com/en/articles/8105281](https://help.suno.com/en/articles/8105281)).
  §2 Variety and Create rows, §3 "Further down" and §8 updated. Max Mode's source unchanged.
  Plan: `design/2026-09-11-understand-song-loop.md`.
