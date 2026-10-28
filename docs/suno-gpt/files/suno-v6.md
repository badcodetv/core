# Suno v6 — what changed, and what it lets us do

> 🔑 **Standing rule (Kai, 2026-09-10): all new Suno work is v6, in the new UI** (the older models
> can no longer be picked for a new generation anyway). The v5.5 era is
> archived in [`../archive/v5.5-era.md`](../archive/v5.5-era.md) — read it only to understand an
> old sheet, or to Cover an old take onto v6.

**v6 shipped 2026-09-09 and retired every older model from the create form.** This file is the
v6 layer on top of the rest of `docs/suno-gpt/`. Where it disagrees with an older file on a
*model* or *control* question, **this file wins** — the older files were written against v5.5.
Where it is silent, the older file still stands (prompt grammar, the voice playbook, the atom,
the satire trap, the narration recipe).

> **This is an engine manual, not a sound.** There is no BadCode house sound (Kai, 2026-10-28):
> which genre, model, sliders and voice a song uses live in its story's `docs/stories/<story>/sound.md`
> ([`STYLE.md`](../../stories/STYLE.md)). Where this file names a story's settings (GPOM's narration,
> Camping's D&B re-cut) they are worked examples, labelled with the story.

> **Confidence: day-one evidence.** Distilled on 2026-09-10 from 11 launch-day YouTube videos and
> a 20-agent web sweep — full claim ledger with every source and tier in
> [`docs/misc/2026-09-10-suno-v6-research.md`](../../misc/2026-09-10-suno-v6-research.md).
> Nobody — us included — has measured anything yet: every "sounds the same" is by ear, no audio
> has been diffed, no controlled grid exists. Two of the videos are paid Suno sponsorships
> (Music Tech Info, Arcade): their click-paths are facts, their verdicts count for less. Reddit
> and Discord were unreachable. **Tier words used below:** *vendor* (Suno said it), *tested*
> (someone did it on camera), *reported* (one person says so), *untested* (our inference).
> **Anything we verify gets written back here with a date.**

> 🆕 **Refreshed 2026-10-14** from ChillPanic's *"Suno V6 Changed EVERYTHING. Here's What Works
> Now."* (2026-10-09, a 13-year producer, tested on camera) plus a web sweep of everything Suno
> shipped since launch. The headline changes: **a Speech model exists** (§1b — voice and score in
> one take, which is exactly what our GPOM narration does by hand), **the credit cost is now
> answered by Suno** (§6), **the one-word edit worked on a multi-word, different-syllable swap**
> (§3 rung 1), and **Audio Influence 100 and Weirdness 100 are reported usable on v6** (§8c).
> Ledger: [`docs/misc/2026-10-14-suno-v6-refresh.md`](../../misc/2026-10-14-suno-v6-refresh.md).

**Contents.** 1 the models · **1b Speech (beta)** · 2 the create form · **3 fixing one word, one
bar, one phrase** · 4 Studio with v6 · 5 new things worth suggesting · 6 stems, quality,
downloads · 7 voices and custom models · 8 prompt craft deltas · **8c the anti-slop moves** ·
9 vocals and D&B · 10 our v5.5 back catalogue · 11 known bugs · 12 the test queue

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

### Which to pick (options — untested by us)

- **v6** for a finished take, and anything carrying a saved Voice or a narrator Voice.
- **v6 Wild when you are hunting** — a texture, a drop idea, a niche sub-genre the pop-tuned
  model flattens (our neurofunk and half-time failures are exactly that theory). **Then Cover the
  winner into v6** for fidelity. That is both Suno's stated intent and two presenters' method — it
  replaces the old "ideas in 4.5, Cover into 5.5" hybrid move.
- **v6 Mini: never.** We're on a paid plan and nothing is known about its quality.
- Wild is "like the old weirdness slider, except the choice now lives in the model." So in a grid,
  **model and weirdness are two different axes that overlap** — don't read a Wild win as proof
  that high weirdness would have done the same.
- **Give Wild three or four takes before judging it** (Moe Lueker's 150-song comparison,
  2026-09-19: v6 needed 1–2 takes per keeper, Wild "several"; weirdness 30–50 on v6, 60–75 on
  Wild). Mini was "closer to v6 than to Wild, but flatter". Subjective, one listener, no blind test.

### Why v6 sounds more generic (2026-10-14)

**Vendor:** v6 is the first model trained on licensed catalogue — Suno names WMG, BMG and Believe
as partners. **Reported (ChillPanic, and "many users"):** v6 output is noticeably *more generic*
than v5.5, and the speculation is the smaller, major-label training pool — "when you shrink the
input, you shrink the output." Speculation, not fact — but it predicts exactly what we have seen
on niche sub-genres. The practical answer is §8c. **Custom models were auto-upgraded to v6**
(vendor, v6 FAQ) — a v5.5-era custom model now runs on v6.

---

## 1b. 🆕 Speech (beta) — a voice and its score in one take (shipped 2026-10-01)

> 🔑 **Why this matters to us:** GPOM's narration is *already* voice + score in one Suno v6 take,
> forced through the song model with GPOM's own template (`docs/stories/gitpush-origin-master/songs/narration.md`).
> Suno now ships a model built for exactly that job. **Nobody here has tried it yet** — §12 test 0.

**Vendor (release note, 2026-10-01):** *"the first model to create a speech and its soundtrack
together, in one take"* — examples: bedtime stories over soft piano, hype speeches over stadium
drums. On **web and mobile**, under **Create**, open to **all plans** as a beta. Suno's release note
gave **no** credit price, language list or API; its tutorial video gives the length (~8 min,
below). Presenters say Speech spends ordinary credits — log the first one.

### The form — from Suno's own tutorial (vendor, 2026-10-01) + three testers (sweep 2026-10-14)

**Create → `Songs | Speech (beta) | Sounds`** (Speech is the middle tab) → **Simple / Advanced**.
Simple = one prompt, Suno writes the script. **Advanced** = what we use:

| Field | What goes in | Tier |
|---|---|---|
| **Script** | the exact words, as **plain paragraphs — "You don't need lyric formatting or bracketed section tags"** (Suno) | vendor |
| **Style / Tone box** (one box, under the script) | the voice **and** the score **together** — there is **no separate music field**. Tone, pacing, mood, setting, and how the score moves | vendor + 3 testers |
| **Vocal Gender** | Male / Female | vendor |
| **Background music** | **on by default**; off = voice only (but see "no dry voice" below) | vendor |
| **Variety** | the same five steps as the song form; **Exact style** is the closest thing to one consistent narrator | 2 testers |
| Duration | **none** — "There's no duration control here"; ask in words ("about 30 seconds") | tested |

- 🔑 **Length: "up to around 8 minutes"** (Suno, on camera); one tester got 4 minutes in one take.
  A whole GPOM scene's narration fits in one generation.
- **The style box carries a performance arc**, and the same script with a new style box is a new
  performance. Suno's own examples: *"calm and professional train station announcer, slow, measured
  pacing, completely serious delivery"* → *"Increasingly frantic announcer trying to remain
  professional, starts controlled, gets faster and more exasperated with every sentence"*; with
  music on, *"restrained at first with a score that gradually becomes more hopeful underneath."*
- **Every take shows a descriptor Suno wrote** — a casting brief such as *"Warm, clear female
  narrator, conversational and gently uplifting, measured pace."* Copy the descriptor of a take
  you like into the next style box (reported — offered as a template, not proven to lock identity).
- **One-word fix works on Speech takes**: open the take → Editor → highlight the word → type the
  replacement → preview → **Commit** (nothing saves until Commit). Shown on camera (Mara→Jane); the
  selection grew past the word and a neighbour picked up a small seam glitch. One presenter read
  **4 credits** off the editor (sponsored, reported). This puts Speech inside the §3 ladder.
- **A Speech take has the whole song menu** — Cover, Reuse, Mashup, Sample, Remaster, Fade,
  Reverse, stems, Open in Studio, and **"Remix as a voice"** (seen in the menu, not run: may turn a
  narrator found in Speech into a saved Voice for the song model). Downloads count against the same
  cap and **default to M4A — switch to WAV**.
- **A series voice, as close as the beta gets:** keep the style box text verbatim in the sheet,
  Variety **Exact style**, same Vocal Gender, every scene.

**Known failures — Suno's own warnings:**
- 🔴 **Accent drift** — Suno's own example is **a British accent wandering towards Australian
  and back.** Whenever the voice must stay British (GPOM's narrator, for one), this is the first
  thing to listen for.
- 🔴 **Dramatic pauses run long.**
- Pronunciation not guaranteed; words can be changed or dropped — **diff every take against the
  script**, the same mechanical check we run on lyrics.
- Can drift towards singing; music can mask consonants.
- **No saved Voice inside Speech** in the beta (confirmed: "not yet for speech") — so it cannot
  yet hold the narrator's identity across scenes the way a Voice does on the song model.
- 🔴 **Two on-camera British-accent requests both failed** — "not definitively British… an
  exaggerated European English accent"; another heard an American imitating British. Accent words
  inside **[brackets]** in the style box confused it — write plain sentences. No tester was a
  native UK listener, so **our own ears are the test**.
- **There is no dry voice even with Background music off** — takes carry hall/room reverb that
  varies take to take, sometimes audible breathing. Plan for de-reverb or a vocal stem.
- **Adjectives don't speed it up** — "clear and energetic with a brisk pace" still paused inside
  sentences. The style text is also taken literally ("fast enough pace" became rushed).
- **Also seen:** skipped words and lines, mangled proper nouns, **endings cut mid-word** (listen to
  the last two seconds), the score defaulting to piano (name the instruments).
- **Pauses follow punctuation**: ellipses lengthen pauses, and one tester rates them above
  bracketed pause tags. Removing ellipses and dashes to *shorten* pauses is inference, untested.

**Prompting (practitioner advice, untested):** start at **100–150 words**; short sentences;
punctuation for breath; paragraph breaks between thoughts; **strip end rhymes and refrains** or
it sings; describe the target ("calm documentary narration, slow, sparse piano underneath")
rather than stacking "do not sing"; ask for a **sparse bed**, not no music; generate several
takes rather than piling on corrections. Variety **Exact style** (fully left) is now backed by
three testers (above). Reported once: music appeared even with background music switched off.

**Making the SONG model speak instead:** the sweep found **no v6-era test** of it. The only v6
wording anyone offers is untested — Style *"spoken-word narration, voice-forward, minimal
documentary underscore, restrained dynamics, no sung chorus"*, lyric label `[Spoken narration]`
(Jack Righteous). GPOM's `narration.md` template remains the only tested evidence we have.

Best fit per reviewers: short expressive
pieces. Worst fit: anything needing exact timing — which for us means **the words and the
cut stay ours**: Speech is a candidate for the take, never for the timing (Premiere still owns
that).

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

🆕 **Variety's default differs by model** (tested, 2026-09-14): **v6 → Normal, v6 Wild → Off.**
So a hand-run v6-vs-Wild comparison on defaults is partly a Variety test. Set Variety Off on both.
(The loader already forces it.)

🆕 **Max Mode, in Suno's own words** (launch video, 2026-09-09): "more compute before it creates the
song", aimed at **reducing drift from an audio reference (a Cover) or a Voice, especially past
two minutes**. FAQ: "For quick ideas and shorter songs, standard mode is all you need." Reported
cost: **2× credits** (ChillPanic said it twice, plus one newsletter). ⚠ Disputed in use — see §8c.

🆕 **Suno confirms My Taste reaches a take through Variety** (two Suno videos): "if you use my taste,
those variations will lean more towards your personal taste profile." With Personalize **off** and
Variety **Off**, it has no route in.

🔴 **Suno switches the model on its own.** Our form showed a toast: *"Model changed — Model was
automatically changed to support your selected conditions."* So a model you set is not a model
that stays set — the loader reads it back after everything else, before Create.

🔑 **Personalize is ALWAYS OFF, and we don't use My Taste** (Kai, 2026-09-10): *"stop trying to
use the My Taste box and always have personalize off when we generate a song, because then each
song becomes an atomic unit."* In our own logs My Taste only ever caused damage, never a better
take. Each song is now its three boxes plus its settings, and nothing hidden. This is a working
method (it keeps every take isolated), not a sound. The loader forces
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

🆕 **Simple mode is now an editor, not a beginner's box** (vendor, v6 FAQ, re-read 2026-10-14):
*"In Simple mode, you don't need to choose a tool like Cover, Remix, or Extend"* — **the model
picks the workflow** from what you attach and what you type. Attach songs, playlists, audio,
images or video; several at once is allowed. ChillPanic's click: **drag a song from the library
onto the "Drop here to remix" area** of the Simple tab, then type a plain sentence. Conversational
wording worked ("Hey bro, shorten the intro…"). This is why §3 rung 1 and most of §5 live in
Simple, not Advanced. 🔴 **Speech** (§1b) may now sit beside Simple / Advanced / Sounds — not
yet seen on our live form; re-map before the loader touches it.

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
| **A** | the **wrong word** is sung (text change) | **rung 1** — attach + instruction (a line or two); **rung 1b** self-Cover for a verse | tested ×4, by ear |
| **A′** | a **Speech** take says one word wrong | the Song Editor's word Replace on the Speech take (§1b) | tested once |
| **B** | the right word is sung **badly** (same text, re-sing it) | 🆕 **Subtle Remaster** (vendor: "clearer pronunciation"), then rung 2's prompt-only Replace, then 2b | 🔴 untested anywhere |
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

🆕 **Third success, and a wider one (ChillPanic, 2026-10-09, native Suno take):** two whole
chorus lines swapped for **different words with a different syllable count** — *"Change the
chorus lines 'I've been angry all my life, I just never had a name for it' to 'I've been happy
at my wife, I just never found the William Shaker'"* (wording as the auto-captions heard it).
Result: **"the delivery is pretty much
exactly the same"**; the melody bent only where the syllables forced it. Instruction shape:
quote the old line, quote the new line, name the section.

🔴 **But a whole verse is too much** (Tim Makes Media, 2026-09-13, native take, on camera):
*"change the verse one lyrics to say and sing the below lyrics"* + a new verse — the stored lyrics
changed, but "the flow was a little different… sort of messed up." For a verse, use **rung 1b**.

**Section-scoped grammar (Suno's own launch video):** name what changes **and what is
protected** — *"Make the chorus more energetic. Add bigger layered vocals and heavier drums, but
keep the verses the same."* For a word: *"change the word love to light throughout the song."*

**Our working boundary (revised 2026-10-14, still by ear):** on a **native Suno take**, a word
*or a line or two* — works, even across a syllable change. **A whole verse** — flow breaks (1
test). **Uploaded external audio** with several multi-word swaps — breaks (3/3). Nobody has yet
targeted **one occurrence** of a repeated word, or re-sung a word with the text unchanged.

### Rung 1b — 🆕 the self-Cover lyric fix (bigger changes, same song)

When the change is a **whole verse** or more. Tested once on camera (Tim Makes Media,
2026-09-13): "basically the same song" with the new words, no glitch at the verse→chorus seam.

1. On the song: **⋯ → Remix → Cover** (the song loads as the audio reference).
2. Edit the **Lyrics** box — replace only the lines that change.
3. More Options: **Variety Off · Audio Influence 100 · Style Influence 0 · Weirdness 0** — every
   slider pushed to "keep".
4. Create.

Note the difference from §8c's polish Cover (Style Influence **100**, Max Mode on): this one is
for *changing words*, that one for *improving sound*. Style Influence 0 because the audio, not
the style text, is what must hold.

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
- 🆕 **Current labels (help.suno.com/en/articles/3271873, re-read 2026-10-14):** highlight the
  region → the original lyrics copy into the Lyrics box → edit → **Recreate Section** (where Create
  sits) → **Confirm** → two versions → pick one → Suno renders a **new full song**; results are
  tagged **Section** and **Full Song**. Pro/Premier. No length, cost or model stated.
- 🆕 **The Song Editor now also** (help article 6141505): **delete any region, not just the ends**
  (highlight → Remove / Delete key), **drag a section by its name** to rearrange, **add a section**
  between two, and **Replace with a prompt and no lyric change** (*"Make this section sound
  dreamier"*) → preview two → **Generate More** → drag the boundary → **Commit**. The prompt-only
  Replace is the most natural candidate yet for **problem B** (untested).
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
- **Remaster** (⋯ → Remaster) claims to keep "structure, lyrics, melody and vocal
  performance". 🆕 The help page (re-read 2026-10-14) now shows a **Model selector** (pick v6) and
  three strengths: **Subtle** — "very close to the original; only small acoustic and production
  details are changed", recommended for **"clearer pronunciation"** and a cleaner mix; **Normal**
  (default) — "keeps duration and style the same while adding slight variations"; **High** —
  "possible changes to musical elements and vocals". 🔑 **Subtle Remaster is a vendor-named
  candidate for problem B** (a word sung unclearly, text unchanged) — untested by anyone. Not for
  changing lyrics. Suno's line: Remaster improves the take you have; Cover reinterprets it.
- **Comp-and-heal** (Jeremiah The Stranger, 2026-09-13, reported): splice the best sections of
  2–4 takes in a DAW, upload the splice, **Cover on v6 with Max Mode on, Audio Influence high but
  deliberately below 100, Style Influence lowered, a little Weirdness** — the Cover heals the
  seams. Numbers were on screen only. Uploads can be refused by the originality check (§11).
- **Studio word changes** work far better on the **multi-track** (stems) view than on a single
  stereo track, but still sometimes "invented a language" (reported).
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
| Bring in outside MIDI; make audio from a MIDI clip | upload a `.mid` from anywhere; ask the **chat** for new stems from a MIDI clip; MIDI→audio is "more faithful" (2026-09-17 update) | vendor |
| Rename clips | right-click → **Rename**, or in bulk via chat (2026-09-17) | vendor |
| Stretch a clip to the project tempo | **Shift-click-drag** the clip edge — timestretch, for samples and found sounds (2026-10-08) | vendor |
| Curve a fade | drag the **node on the fade icon** — exponential or logarithmic, no longer linear only (2026-10-08) | vendor |
| Get a cappella vocals on the grid | improved **beat-1 detection** on new clips and takes — less manual alignment for non-rhythmic clips (2026-10-08) | vendor |
| Use two monitors | synth, musical-typing keyboard and expanded plug-in views **pop out** into floating windows (2026-10-08) | vendor |

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
| "the intro's too long" 🆕 | **plain-language trim** — Simple, attach the song, *"Shorten the intro so the song starts at the 0:20 mark"* — "did exactly what we asked". For a cut with no regeneration at all, **Crop** in the Song Editor is the deterministic route | tested once (ChillPanic) |
| "put strings / a solo here — it goes like *this*" 🆕 | **hum it in as an instrument** — Simple → Add → Audio → **Record**, hum the line; attach the song too; *"Use the melody from the recording as a violin, added to the very beginning of <song>. Start the violin at 0:00."* It turned the hummed melody into a violin — but **the take stopped abruptly**, so expect a Cover or a few retries | tested once (ChillPanic) |
| "sample just that bit" 🆕 | song **⋯ → Remix → Sample this song** → drag to the region (4 s worked) → add a Style prompt (e.g. trap) → Create. Feeds a weird take (kids' music, a high-weirdness throwaway) into a new genre | tested (ChillPanic) |
| "these two songs, but as one" 🆕 | Simple, drag both in, *"Combine these songs"* — even southern gospel × Brazilian funk produced a coherent track. Also the strongest anti-generic move (§8c) | tested (ChillPanic) |
| "a spoken piece with music under it" 🆕 | **Speech (beta)** — §1b | vendor |
| "two singers, one song" 🆕 | **duet from two songs** in Simple — §7 | tested once |
| "I just want the drums" 🆕 | **v6 Wild + "… drums only"**, no genre word — §9 | tested (not on D&B) |
| "build it up from parts" 🆕 | **Sounds tab** loops with BPM + Key locked → combine in Simple — §9 | tested once |
| "it's slurring that word" 🆕 | **Subtle Remaster** on v6 — §3 problem B | vendor (untested) |
| "rewrite the whole verse" 🆕 | **rung 1b** self-Cover, not a Simple edit — §3 | tested once |
| "get the old singer back" 🆕 | old song → Wild "recreate vocals verbatim" → Remix → Voice — §7 | reported |
| "it's half speed again" 🆕 | strip `slow` / `half-time` from Style — §9 | tested (not on D&B) |

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
- ✅ **Credit cost answered by Suno (v6 FAQ, re-read 2026-10-14):** *"Do v6 generations cost
  more credits than v5.5? No."* **10 credits per Create, for two songs**, on v6. Prompts carrying
  **many images or videos cost more**. Pro gets 2,500/month, Premier 10,000/month.
- **Max Mode costs more — reported as double** (~20 per Create; one newsletter, "from hands-on
  documentation"; Suno says only "costs more credits"). Speech and plain-language edits: no price
  published. **Log the balance before and after** the first Max Mode Create and the first Speech
  take — that settles both.
- **Extra downloads** beyond the allowance: **$2.99 each**, no bulk discount (reported).
- ✅ **Studio exports are unmetered — now vendor wording.** Suno's download-changes FAQ
  ([help.suno.com/en/articles/13614785](https://help.suno.com/en/articles/13614785)): "users will
  still be able to download their work from Studio **without limitation**." Premier. 🔑 So **rung 3
  (stems + a mute) costs no download** if the stems come out through **Studio → Export →
  multi-track**, not song ⋯ → Download. Still watch the counter the first time.
- **Speech word Replace: 4 credits** (one sponsored presenter, reported).

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
- 🆕 **A duet without a saved Voice** (Adam Vincent, 2026-09-11, tested): Simple → drag in **both**
  songs (A = the track to keep, B = the second singer's source) → *"Recreate [Song A] by taking the
  voice from [Song B] as the second lead vocal who follows the female singer. This should be a duet
  where each voice is highlighted throughout and on the chorus they sing together."* Suno wrote its
  own Female lead / Male lead tags. Take 1 rewrote the melody, take 2 kept it — **judge the pair**.
  Stricter add-ons he suggests: *"make sure that the male voice uses the exact voice from the song
  that I'm uploading."* Relevant to Camping, our duet.
- 🆕 **Bring back an old (v4.5–v5.5) singer** (The Mix University, 2026-09-25, reported — only the
  Wild run shown): drag the old song onto "drop here to remix" → paste its lyrics → Style *"recreate
  vocals verbatim"* → model **v6 Wild** → on the take that holds the voice: **⋯ → Remix → Voice**,
  rename, Public **off**, save. He says plain v6 changes the voice; Wild kept it. A route for our
  v5.5-era narrator and Karen voices.
- 🆕 **How much a Voice leads varies roll to roll** — "sometimes your voice leads, sometimes it sits
  in the background like percussion" (reported). Judge over several rolls. Source audio: record
  15 s–4 min clean a cappella (the product page and help centre disagree; take the longer).
- 🆕 **A thin or raspy v6 vocal fixed by prompt, not settings** (Fondrey, 2026-10-04, one
  controlled series): replace a short tag list with (a) a detailed description of the singer and
  how they perform, (b) section-by-section guidance written from the lyrics, (c) a sentence about
  the backing vocals. Settings held at Max Mode on · Weirdness 22 · Style Influence 73 · Variety Off.
- **UK accent on the song model: still no evidence anywhere** — the sweep found none.
- **Lyricist and Inspo: no v6 information at all.**

---

## 8. Prompt craft deltas

- **Long plain-English briefs work** on v6 — a jargon-free paragraph with a bridge instruction
  and a stripped-back ending was followed closely (3 agree). Short boxes still work too; this
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
- 🔴 **PROVEN LIVE 2026-09-13: Variety rewrites the Style box, differently for every take.** Twelve
  Camping takes at Variety normal and extra (with and without Max Mode) each stored a different
  306–496-char paraphrase of an 866-char Style box as the song's `tags` — read off each song's own
  suno.com record — and the paraphrases re-introduced clauses the box had removed ("wide chiming
  guitar layers", "half-time drops", "androgynous… voice"). The Lyrics box stayed byte-identical.
  Any prompt test at Variety above **Off** is testing Suno's rewrite. Evidence: `docs/stories/camping/songs/camping.md` §v6 round log.
- **Variety rewrites your Style box** — now vendor-sourced (2026-09-11): the v6 FAQ says it works
  by "adjusting and updating your style prompts" and to "reduce the Variety slider to 0" to keep
  control ([help.suno.com/en/articles/13924481](https://help.suno.com/en/articles/13924481)).
  Above **Off**, the boxes you wrote are not the whole song — set Variety **Off** when the atom
  must hold.

---

## 8b. The community sweep, 2026-09-21 — 🟡 practitioner tier, none of it measured by us

Read on Jack's request ("research the internet for youtube tips on how to get the most out of v6").
Every row below is **what practitioners say**, not what we have proven. Where it contradicts a
measured finding of ours, ours wins.

| Claim | Who says it | Our status |
|---|---|---|
| Start at **Weirdness 20 · Style Influence 75 · Variety Off** | [sunostyles](https://sunostyles.com/blog/suno-v6-settings), repeated by several guides | 🟡 close to Camping's re-cut (SI 80, weirdness paired 30/60). The source explicitly says *"not a claim that one preset wins"* |
| **Weirdness 0 sounds stale; above 90 produces artifacts; 30–50 for a detailed prompt** | [Moe Lueker](https://moelueker.com/blog/suno-v6-guide) | 🟡 untested. The w60 half of a pair sits above the recommended band on purpose — drift is how Camping's `1127446d` got the things Jack likes |
| **Style Influence 40 for a vague prompt, 65+ for a precise one** | Moe Lueker | 🟡 consistent with Camping's 80 |
| **Variety above Off rewrites your Style box** | [Suno's own v6 FAQ](https://help.suno.com/en/articles/13924481) + every guide | ✅ **proven by us** 2026-09-13, twelve takes |
| 🔑 **Max Mode is aimed at songs over two minutes**, and at keeping vocals and style consistent across a whole track | Suno via [Jack Righteous](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/inside-suno-v6-create-simple-advanced-sounds-guide), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode/) | ⬜ **never tried by us, and every Camping take is 3 minutes plus.** This is the most obviously untested lever we own. Cost is "more credits", amount unstated |
| **A constant-tempo clause reduces drift** — *"constant tempo, steady groove, no tempo changes, 4/4 time"* | [MixMasterAI](https://www.mixmasterai.co/suno-prompts/fix/wrong-tempo), [GenX Notes](https://blog.genxnotes.com/en/fix-suno-bpm-tempo-drift/) | 🟡 first used by us in r54 (Camping), unmeasured |
| **D&B works at 170–175; above 180 drum resolution degrades** | MixMasterAI | 🟡 consistent with Camping's 174 |
| **Rap speed is set with musical units, not adjectives** — 16th-note subdivisions, ~16 syllables a bar, `double-time`, `rapid-fire`, `chopper`; and `laid-back`/`smooth` actively slow it | [HookGenius](https://hookgenius.app/learn/suno-hiphop-prompts/), [Undetectr](https://undetectr.com/blog/suno-prompts-for-hip-hop) | 🟡 the basis of r55's flow spec. **Do the arithmetic before pasting a number**: at 174 BPM, 16ths is 11.6 syllables a second, which no human does — eighths (5.8/sec) with 16th bursts is what "fast" actually means at this tempo |
| **Avoid the words `fusion` and `meets`; say which layer belongs to which genre** | [SunoPromptPro](https://www.sunopromptpro.com/en/guides/suno-genre-combinations) | 🟡 agrees with our unity-sentence rule (`suno-tag-mechanics.md`) |
| **Name two or three instruments, not a full band** | [Brahmstorm](https://brahmstorm.com/blog/suno-genre-blending-prompts-that-actually-work/) | 🟡 adopted in r55 |
| **v6 follows the Style field more literally than v5.5** | most guides | 🟡 consistent with Camping's r53 pivot to Style Influence 80 |

🔴 **What nobody publishes:** any measured relationship between a setting and *vocal delivery
speed*. Every "make it faster" tip is prompt wording. Our own measurement (r48, onsets/sec) is
still the only evidence in this repo that anything moves that number — and the duration control,
which no guide mentions as a pacing lever at all, is the one we can prove is obeyed.

---

## 8c. 🆕 The anti-slop moves — ChillPanic, 2026-10-09 (tested on camera, by ear)

Source: [ChillPanic, *Suno V6 Changed EVERYTHING. Here's What Works Now.*](https://www.youtube.com/watch?v=EUW5hReKw6w)
— a producer of 13 years, whose launch-day video is already in our 2026-09-10 sweep. One
person's ears, no measurement, but every move was shown working on camera. His three rules:

**Rule 1 — Simple is not simple.** It's the editor now (§2, §3 rung 1, §5).

**Rule 2 — "Stop, slop and drop it": v6 defaults to generic, so the creativity has to come from
you.** Five ways out, best first for us:

1. **Name the production techniques, not the genre.** For a niche genre the name alone gives a
   passable average. What landed was the *mechanics* — e.g. *"hardstyle kick, pitched down one
   octave on drop impact; breakbeat chops; supersaw chord burst, hard cut; FM bass growl, sub
   drop"*. ✅ **This is already §9's D&B finding** (name the drum mechanics, not the sub-genre) —
   now with a second, independent v6 data point.
2. **Combine songs.** Make two unrelated songs, drag both into Simple, *"Combine these songs."*
3. **Wild first, then Cover into v6.** Wild is worse on fidelity and mix but more creative; once
   a Wild take has the idea, **Advanced → Cover on v6 at Weirdness 0, Audio Influence 80** — "the
   same melody and the same idea, just made it sound better." ✅ Matches §1's Wild-then-Cover option;
   now with numbers.
4. **High weirdness as a quarry.** Generate at very high weirdness, then **Sample** or **Cover**
   the bit you like (§5 "sample just that bit").
5. **Sample something absurd** (he used kids' music) as the seed for a different genre.

**Rule 3 — "Increase the soup": the quality levers.**

- **Draft with Max Mode off, polish with a Max Mode Cover.** Max Mode is audibly better and costs
  more (§6). Once a take is right: **Cover it with Max Mode on, Style box emptied, Weirdness 0,
  Style Influence 100, Audio Influence 100.** 🔑 This is the cheapest test of Max Mode we own —
  Camping's accepted take is the obvious candidate (§12 test 8).
- **Variety Off.** "Sometimes when I have variety on, it just doesn't listen to my prompt at all,
  even with balanced variety… worse generations every time." ✅ **Agrees with our proven finding**
  (§8: Variety rewrites the Style box) — an independent ear arriving at the same rule.
- 🔴 **Audio Influence and Weirdness changed intensity on v6 — this overturns old advice.**
  - **Audio Influence 100 is now usable with a Voice.** On v5.5 his deliberately over-the-top
    emo Voice at AI 100 was unlistenable; on v6 at AI 100 "it still maintains that character, but
    it sounds much better." The community "100 glitches, use 80–96" rule is **v5.5 advice**.
  - **Weirdness 100 no longer glitches** — "doesn't sound like glitches to me." Moe Lueker
    (2026-09-19) still says >90 risks artifacts, so: **reported both ways; test before relying.**
  - For a story with a saved narrator Voice (GPOM's): it may now hold at a much higher Audio
    Influence than that story's settings assume — a one-variable test, not a re-template (§12 test 6).

**🆕 Counter-evidence from the 2026-10-14 sweep — hold §8c's quality claims loosely:**
- 🔴 **Max Mode heard as static.** The Mix University (2026-10-02) heard crackle on **every** Max
  Mode take with a Voice, across v6, Wild and Mini — "it's just distorting." Not controlled (his
  A/B was abandoned, and he heard static on the non-Max take too), but it directly contradicts
  "audibly better". Listen on headphones for static on sustained vowels.
- 🔴 **A v5.5→v6 Cover can come back duller.** Lanewood (2026-09-18): Max Mode on, Variety off —
  "dull and muddy" by ear, and the v6 mix **drifted between first and last chorus** (bass up,
  highs down) even with Max Mode on. Compare first and last chorus before accepting a Cover.
- **v6 Cover reproduces its source less faithfully than v5.5 did** (tested, 2026-09-14) — raise
  Audio Influence when the source must survive.

**What we do NOT take from it:** his "slider settings don't matter, I burn my credits" stance (we
log every credit), and the training-set explanation (speculation — §1).

---

## 9. Vocals and drum & bass

*D&B is here because GPOM's and Camping's tracks are D&B, so that's where our tests are — a genre
we have worked in, not a default. A story's genre is in its `sound.md`.*

- **Duets:** explicit `Male vocal` / `Female vocal` under section tags gave a real alternating
  duet; "male and female" in a Simple style also worked. Still no duet control — our "cut on the
  seam" rule stands. **Vocal Gender** is now a first-class control.
- **Accents:** rock still defaults to a country/southern vocal (3/3, even with Max Mode); the fix
  was custom model + Voice. **No UK-accent evidence of any kind** — any British voice needs our own
  test. The v5.5 finding that nationality rides on the genre tag (`suno-voices.md`) stands until tested.
- **Speech / narration:** 🆕 **Suno shipped a dedicated Speech model on 2026-10-01 — see §1b.**
  It does natively what GPOM's narration template forces the song model to do, but warns of
  British→Australian accent drift and has no saved Voice. Until tested, GPOM keeps its template in
  `docs/stories/gitpush-origin-master/songs/narration.md`. Other lever still untested: a
  **Studio vocal track** from typed lyrics.
- **D&B:** a lazy `liquid DnB` prompt came back as **two-step drums** ("that does not sound like
  D&B"); an **engineered** breakcore/jungle prompt worked on both models — *"aggressive breakcore
  instrumental, rapid chop, jungle breaks, hyperdetail percussion, dark synth bassline, euphoric
  melodic chops"*. **Name the drum mechanics, not the sub-genre** — the same lesson as our
  riddim/neurofunk notes, now with a v6 data point. Half-time is **not known to be fixed**.
- No dedicated BPM or key field on the Songs form — still typed into Style. 🆕 **The Sounds tab
  has both** (below).

### 🆕 Tempo on v6 — the likely cause of our half-time drift (SunoAI攻略ちゃんねる, 2026-10-06)

Tested on camera with a metronome, on rock, J-pop, trance, R&B — **not on D&B**, so every row
needs our own run at 170–175.

- 🔑 **"slow" or "half-time" next to a BPM halves the effective tempo; "fast" doubles it.**
  `120bpm, fast, rock` played at an effective 240; `80bpm, slow, rock` at 40. And **v6 sometimes
  halves a high BPM on its own.** For full-tempo D&B, keep `slow`, `half-time`, `laid-back` and
  similar out of the Style box entirely (they may be leaking in from mood words). For a deliberate
  half-time track, `<N>bpm, slow` may be the lever.
- **Round BPMs hold harder** (reported): `120bpm` ≈ 120, `153bpm` drifts 151–156. So `170bpm` may
  hold better than our `174bpm` — a one-variable test.
- **Variety above Off and Simple mode pull extreme BPMs back to the genre's typical tempo**
  (reported). Advanced + Variety Off when a BPM must hold.
- **Per-section tempo tags do nothing** — `[verse][120bpm] [chorus][150bpm]` gives one or the other;
  a range `120bpm-140bpm` picks one end. One tempo per song.
- Keep the BPM inside 50–200; any format works (`170bpm`, or even a bare number).

### 🆕 Drums and D&B on v6 Wild and Sounds

- **Wild + "<instrument> only" returns just that instrument**; v6 adds a band (tested, 2026-09-14).
  For a D&B drum bed, e.g.: v6-wild, Variety Off, `170bpm, chopped breakbeat drums only`. **No genre word** — "J-POP
  bass only" still gave a full J-pop track.
- **Wild keeps uploaded drum rhythms that v6 normalises** (tested): an odd-meter home-made break
  Extended on Wild kept its pattern; v6 lost the time signature. Then **Cover** the Wild result to
  fix its sound. Route: make or upload the break → Extend/Mashup on Wild → Cover.
- **Neurofunk** (Russian bass-music producer, 2026-09-17, reported): a short prompt on v6 came back
  "some pop"; the same on Wild was convincing neurofunk. Wild still didn't separate **jump up**
  (came back mainstream) and didn't know **raw breakbeat / electro-breaks** — describe the mechanics.
- **The Sounds tab — build element by element** (2026-09-28, tested): Create → **Sounds** → set
  **BPM** and **Key** (lock the same values on every element) → Type **Loop** for beds ("a seamless
  repeating clip"; vendor) → prompt each part with exclusions in the text: *"fast breakbeat drums
  only, amen break, drums only, no melody, no bass, no guitar, no synth"*, then the bass, then a pad
  → **Simple → drag all the clips in → "combine this all together into one song"** (+ a Style with
  genre and BPM). Length goes in the prompt ("30 second long…"). Loops "may include full musical
  arrangements" — check. Also a candidate for **dry-and-separate narration beds**.
- **Wild at weirdness 0?** One Reddit thread (second-hand) says Wild was "random garbage" unless
  weirdness was 0; Moe Lueker used 60–75. If our Wild cell (w60) comes back as noise, try w0
  before writing Wild off.

---

## 10. Our v5.5 back catalogue

- **No accepted v5.5 sheet can be re-run on v5.5** — the Camping duet (accepted round 17), the
  GPOM narration, Karen. A re-run on v6 is a **new song**.
- **Vendor-confirmed (v6 FAQ, 2026-10-14):** old songs stay in the library unchanged and can still
  be **listened to, shared, remastered and covered** — but *"any new iterations are made with
  v6."* Suno's FAQ links a tutorial for recreating past-model results.
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
| Hummed-instrument add | the take **stopped abruptly** after the added violin (ChillPanic, 2026-10-09) |
| Speech (beta) | British accent drifts to Australian; pauses run long; words can change or drop; can drift into singing (Suno's own warnings) |
| Generic output | v6 defaults towards the average, worst on niche genres — §8c |
| Copyright filter | a Studio vocal record/regenerate refused **"This audio contains copyrighted lyrics"** on the creator's own line ("don't know what I would say") — a common phrase can block a one-line fix; reword it |
| Originality check | uploading **your own** finished mix was refused: **"audio matches an existing recording"** → re-use the native Suno take from the library instead of a re-upload |
| Studio export drift | cut/moved clips shifted out of place on export, and reopening re-pulled fresh stems with the misalignment baked in — check alignment before leaving the session |
| Speech | no dry voice even with music off (variable reverb); endings cut mid-word; British requests failed twice |
| Mashup | element assignment ignored once ("vocal chop from song B" came from A) — budget re-rolls |
| Tempo words | `slow` / `half-time` halve, `fast` doubles the BPM (§9) |
| Variety | no audible effect in one test |
| Docs lag | the sliders help page doesn't list Variety; Voices help still says v5.5 only |

---

## 12. The test queue — what we should run ourselves

In priority order. Every one goes through one Suno tab, `status` first, the credit balance
logged before and after.

0. 🆕🔑 **Speech (beta) on one GPOM narration scene** (added 2026-10-14). Speech → Advanced.
   Script = the scene atom's words as **plain paragraphs, no tags**. **One** style box = the
   GPOM narrator clause **plus** GPOM's score clause, plain sentences, no brackets. Vocal Gender
   Male, Variety **Exact style**. Listen for, in order: **UK accent holding** (Suno warns it
   drifts to Australian; two testers' British requests failed), words matching the script (diff
   it), pause length, the last two seconds, singing drift. If a single word is wrong, try the
   Editor's word Replace before re-rolling. Compare against the accepted song-model take. Log
   credits. *Listening stays Kai's: no Gemini listen unless asked.*
0b. 🆕 **D&B tempo words** — the same D&B sheet with every `slow` / `half-time` / `laid-back` /
   mood word that implies slowness removed, and `170bpm` vs `174bpm`. Does the half-time drift go?
0c. 🆕 **Subtle Remaster on a mis-sung word** (problem B) — a native take with one unclear word →
   Remaster, model v6, **Subtle**. Did the word clear up while the take stayed?
0d. 🆕 **Rung 1b self-Cover** on a verse rewrite — Variety Off, AI 100, SI 0, W 0.
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
5. **A D&B sheet (Camping's) on v6 vs Wild** — grid round R1 (`automation.md` §9).
6. **GPOM's narrator Voice on v6 and Wild** — quiet-section timbre, UK accent, sibilance. 🆕 Add
   one cell at **Audio Influence 100** (§8c says v6 now holds character there).
7. **Variety** — does it change how far apart the two takes are? *(ChillPanic, by ear: on = it
   ignores the prompt. Off for refining a liked take stands either way; an exploring round may
   choose Variety per prompt — `same-song-traps.md` trap 10.)*
8. **Max Mode** — 🆕 run it as ChillPanic's **polish Cover**: Camping's accepted take → Cover,
   Max Mode on, Style empty, Weirdness 0, Style Influence 100, Audio Influence 100. Better than
   the source? Log the credit delta (reported 2×).
9. **Credit cost** — ✅ base v6 answered by Suno (10 per Create, §6). Still open: Wild, Max Mode,
   an edit, Speech.
10. **Backing out of one bar via stems + a Premiere mute** — Kai approves the download.
11. **Does a Studio multi-track export draw on the download allowance?** (human) — Suno now says
    "without limitation" (§6); one human export confirms it.
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
- 2026-10-14 — refresh on Kai's request: ChillPanic's 2026-10-09 video (transcript via
  auto-captions) + Suno's release notes since launch (Studio 2026-09-17 and 2026-10-08, **Speech
  2026-10-01**, Albums 2026-10-05) + the v6 FAQ re-read + ~10 searches of secondary guides.
  Added §1b, §8c; updated §1, §2, §3 rung 1, §4, §5, §6, §9, §10, §11, §12. Ledger:
  [`docs/misc/2026-10-14-suno-v6-refresh.md`](../../misc/2026-10-14-suno-v6-refresh.md).
  Nothing in this pass was measured by us.
- 2026-10-14 (later) — **sweep 2**, Kai's request, run as a workflow: five themed researchers
  (Speech, one-word fixes, voices, D&B, platform), YouTube-transcript-first, each followed by an
  adversarial verifier that re-fetched every transcript. ~70 findings in, ~10 killed, ~20
  downgraded. Rewrote §1b's form; added rung 1b, Subtle Remaster for problem B, the Song Editor's
  new moves, Variety-default-by-model, Max Mode in Suno's words, the duet / old-singer / thin-vocal
  routes (§7), tempo words + Wild drums + Sounds tab (§9), the counter-evidence on Max Mode and
  Covers (§8c), five new bugs, tests 0b–0d. Ledger §"Sweep 2".
