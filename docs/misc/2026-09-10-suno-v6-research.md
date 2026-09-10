# Suno v6: research synthesis (2026-09-10)

> **Evidence base, not guidance.** The operating knowledge distilled from this lives in
> [`docs/suno-gpt/files/suno-v6.md`](../suno-gpt/files/suno-v6.md). This file is kept so every
> claim there can be traced to its source and tier. Produced by a 28-agent workflow on 2026-09-10:
> 11 launch-day YouTube transcripts (5 distillers) + 20 Sonnet web researchers + synthesise → critique → revise.
> The raw transcripts are not committed (same rule as the 2026-07-29 ChillPanic harvest).

**What this is.** A synthesis of 25 research passes: 11 YouTube videos from launch day (the 10 Kai supplied plus [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)), distilled from their transcripts, plus 20 web researchers. It is one day after launch. Distilled into `docs/suno-gpt/files/suno-v6.md`. Every claim carries a tier and a URL.

**Tiers.**
- **[vendor]**: Suno's blog, help centre, release notes, pricing page, in-app copy, or a named Suno executive quoted in the press.
- **[tested]**: someone demonstrated it on camera or A/B'd it in a write-up.
- **[reported]**: one person says so and it was not demonstrated.
- **[spec]**: speculation, including our own inferences.

"N agree" means N *independent* sources agree. Press articles that only repeat Suno's blog are not counted as independent.

**Pre-v6 rule.** Anything dated before 2026-09-08 is marked **(PRE-v6)**. Pre-v6 material that v6 did not change has been dropped, except where it is the only mechanism behind a v6 claim (Replace Section).

**Caveats that apply to everything below.**
- It is day 1. No source has diffed audio, measured anything, or run a controlled grid.
- Two of the ten videos are disclosed paid Suno sponsorships: [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY) and [xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY). Their quality verdicts count for less. Their click-paths are still facts.
- Almost every web source restates [the v6 blog](https://suno.com/blog/introducing-v6). Only one secondary write-up ([weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode)) lists create-form controls. The videos are the only real hands-on evidence.
- Reddit, Discord and r/SunoAI could not be reached (WebFetch was blocked and nothing was indexed yet). There is **no community-forum evidence** in this report.

---

## 1. What shipped: the dated facts

| Date | Fact | Tier | Source |
|---|---|---|---|
| 2025-06-03 **(PRE-v6)** | Blog post "A New Level of Creative Control": an upgraded Song Editor for reordering, rewriting and remaking a track section by section from the waveform, with a **"creativity slider"**. The same post introduced "Creative Sliders… three new controls" (the Weirdness / Style Influence / Audio Influence trio). **Not a v6 feature.** | vendor | [suno.com/blog/songeditor](https://suno.com/blog/songeditor) |
| 2025-11-25 / 2026-08-12 / 2026-09-08 | Label partnerships announced: Warner Music Group, then BMG, then Believe/TuneCore (the day before v6). | vendor | [blog](https://suno.com/blog/introducing-v6), [MBW](https://www.musicbusinessworldwide.com/suno-v6-ai-music-models-launch-in-partnership-with-wmg-bmg-and-believe/) |
| 2026-09-02 **(PRE-v6, one week before)** | Studio update. **Confirmed on a direct fetch (three items):** the chat is BPM-aware and "more reliable and more rational"; plugins move and copy between tracks by drag-and-drop; playback and project loading are faster. **Unverified (summariser only; absent from the direct fetch):** undo for chat edits, Cmd/Ctrl-D duplicate, the wavetable-synth aliasing fix, and fixes for missing MIDI/MP3 export, stuck MIDI notes and reversed-clip display. | vendor (the three confirmed items) / unverified (the rest) | [release notes](https://suno.com/release-notes) |
| 2026-09-03 **(concurrent, not part of v6)** | New ToS and download policy. Caps apply to **every song in the library, including old ones**. Commercial use is allowed only for songs downloaded within the plan's allowance. Removing Suno's inaudible watermark is prohibited. | vendor | [help FAQ 13614785](https://help.suno.com/en/articles/13614785), [help 13876865](https://help.suno.com/en/articles/13876865), [ToS blog](https://suno.com/blog/suno-updates-tos), relayed by [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| 2026-09-05 | Suno email: "we're retiring our older models when we launch V6." | vendor (email quoted on camera) | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| **2026-09-09** | **v6 launches as a family of three models: v6, v6-wild and v6-mini.** Suno calls it "a new generation of music models, in partnership with the music industry". **5+ agree.** | vendor | [blog](https://suno.com/blog/introducing-v6), [release notes](https://suno.com/release-notes), [TechCrunch](https://techcrunch.com/2026/09/09/suno-replaces-its-ai-models-with-a-new-one-trained-on-licensed-music-as-copyright-suits-pile-up/), [Music Ally](https://musically.com/2026/09/09/suno-launches-its-v6-ai-music-models-heres-what-you-need-to-know/), [DMN](https://www.digitalmusicnews.com/2026/09/09/suno-v6-launch/) |
| 2026-09-09 | **v4, v4.5, v5 and v5.5 are removed from the create-form picker.** No fresh generation on old models. The old library stays playable and downloadable. The email says **Cover and Extend still work on old-model songs**. **3 agree.** | vendor + tested | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8) ("the old models are no longer selectable"), [TechCrunch](https://techcrunch.com/2026/09/09/suno-replaces-its-ai-models-with-a-new-one-trained-on-licensed-music-as-copyright-suits-pile-up/) |
| 2026-09-09 | v6 is "not trained using the data it used to train previous versions". It is built on newly licensed catalogue. Suno has not published what it was trained on. Universal and Sony have not signed and are still suing. | vendor (training); reported (UMG/Sony) | [TechCrunch](https://techcrunch.com/2026/09/09/suno-replaces-its-ai-models-with-a-new-one-trained-on-licensed-music-as-copyright-suits-pile-up/), [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| 2026-09-09 | **Plain-language editing of an existing song:** "Update a single lyric without rebuilding the entire song. Change one word or line while leaving the rest intact." Also "Change one section while preserving everything else." Examples: "Change the lyric from love to light"; "Change the chorus so it's sung by a gospel choir." See §5. | vendor | [blog](https://suno.com/blog/introducing-v6), [release notes](https://suno.com/release-notes) |
| 2026-09-09 | **Multimodal input.** Text, audio, images, video and voice memos can all seed a song. | vendor + tested | [blog](https://suno.com/blog/introducing-v6), [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU), [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo), [b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ) |
| 2026-09-09 | **Plain-language sampling and mashup.** "Sample the riff at 0:45, isolate the guitar, build a beat around it." "Take the vocals from x, drums from y, and add new lyrics…" | vendor + tested | [blog](https://suno.com/blog/introducing-v6), [b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ) |
| 2026-09-09 | **New create-form controls:** a **Variety** slider (new) and a **Personalize** toggle (new). **Max Mode** is now a normal toggle. See §3. | tested | [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8), [BToY](https://www.youtube.com/watch?v=BToYusaGue4), [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY) |
| 2026-09-09 | V6 models can be picked **per track inside Studio** and in Studio chat. | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA), [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8) |
| 2026-09-09 | **"Create Custom Model (Beta)"** appears in the model picker at **100 credits**. It is not in the launch materials. | reported | [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) |
| 2026-09-09 | **500 non-expiring credits** went to accounts that had recently generated on the old models. | reported | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| undated | An undated help page lists "Remix & Edit— Extend, Cover, Replace Section, and more, all powered by v6". **The v6 blog does not mention Replace Section** ("Pro and Premier" appears there only in the gating of v6 and v6-wild). The tool itself, and its Pro/Premier requirement, date from 2024 ([2024 note](https://about.suno.com/release-notes/replace-section)). See §5 and §15. | vendor | [help 13924801](https://help.suno.com/en/articles/13924801) |
| undated | **Custom models run on v6:** "Fine-tune v6 on your own tracks for a personalized sound." The help page also says: "All three variants support up to 8 minutes per generation." | vendor | [help 13924801](https://help.suno.com/en/articles/13924801) |
| 2026-09-09 | A planned (not live) **artist opt-in remix programme**, with compensation paid through labels. **This is not our per-song Remix tool.** | reported | [TechCrunch](https://techcrunch.com/2026/09/09/suno-replaces-its-ai-models-with-a-new-one-trained-on-licensed-music-as-copyright-suits-pile-up/), [Music Ally](https://musically.com/2026/09/09/suno-launches-its-v6-ai-music-models-heres-what-you-need-to-know/) |
| ~2026-09-09 | "Community Collab": post unfinished projects and others help mix, master or write. No primary URL was resolved. | reported (weak) | WebSearch summary only |
| ~2026-09-09 | "Workspaces" replace a flat library. **Not new to us.** Our `automation.md` already has a workspace protocol. | reported | [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) |
| ~2026-09-09 | The website is "way more accessible to screen readers". This was a chat comment. | reported | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |

### Pricing and tiers (live pricing page, fetched 2026-09-10) [vendor]

Source: [suno.com/pricing](https://suno.com/pricing)

| Plan | Price | Credits | Downloads | Models | Commercial rights |
|---|---|---|---|---|---|
| Free | $0 | 50/day | **0** per the pricing page; see the contradiction below | "Best free model (v6-mini)" | no |
| Pro | $8/mo ($6.40/mo annual) | 2,500/mo | 20/mo | "Advanced models (v6 and v6-wild)" | yes |
| Premier | $24/mo ($19.20/mo annual) | 10,000/mo | 60/mo; "unlimited exports inside Suno Studio" per [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) citing the ToS | v6, v6-wild | yes |

**Download rules** [vendor, [help 13876865](https://help.suno.com/en/articles/13876865), [help 13614785](https://help.suno.com/en/articles/13614785)]:
- One song counts as one download, whatever the format and however often it is re-downloaded.
- Failed downloads don't count.
- Extra downloads can be purchased. No price was found.
- Top-up credits don't expire but need an active subscription.
- Free users who joined before 2026-09-03 get **7 lifetime trial downloads**, personal use only. Users who joined later "may occasionally receive trial downloads".

**Credit cost of one v6 generation: UNKNOWN.** No source gives it.
- The pre-v6 baseline was about 10 credits for 2 songs [reported, PRE-v6, [lumimusic](https://lumimusic.ai/blog/suno-pricing)].
- The monthly budgets grew a lot (2,500 and 10,000), which suggests per-generation cost may have changed too [spec].
- Pre-launch rumours of "200–400 credits per generation" are unconfirmed [spec].
- Max Mode's credit cost: **unsourced**. An earlier draft said "roughly double" and credited weraveyou, but a direct fetch of that article gives no credit cost for Max Mode [spec, unsourced].

**Plan gating.**
- v6 and v6-wild carry a Pro badge. Free accounts get v6-mini (previously free accounts were stuck on v4.5) [reported, [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ); vendor for the model split, [blog](https://suno.com/blog/introducing-v6)].
- No source tested v6-wild on a free account.
- No source says whether a Pro account can pick v6-mini, or what rights mini output would carry on a paid plan.

---

## 2. The model lineup

### Names: the exact in-app strings are contested

| Source | Labels read |
|---|---|
| Vendor blog and pricing page | `v6`, `v6-wild`, `v6-mini` ([blog](https://suno.com/blog/introducing-v6), [pricing](https://suno.com/pricing)) |
| [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU), confirmed in [M4Hj](https://www.youtube.com/watch?v=M4HjwzE7bjY) | `Version 6 Pro`, `Version 6 Wild Pro`, `Version 6 Mini` (read aloud from the dropdown) |
| [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8) | `V6 Mini`, `V6 Wild Pro`, `V6 Pro` |
| [BToY](https://www.youtube.com/watch?v=BToYusaGue4) | "V6 Pro", "V6 Wild", "Mini" |
| [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo) | "V6", "V6 Wild", "V6 Mini", with a *Pro badge* on the first two |
| [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY) (on-screen) | `V6`, `V6 - Wild` |

**Most likely reconciliation [spec].** The names are v6, v6 Wild and v6 Mini. The paid two carry a **"Pro" badge** that presenters read aloud as part of the name. The UI may also spell out "Version 6" in the dropdown and "V6" on the collapsed button. **Automation must not match an exact string.** See §3.

### In-app descriptions (read verbatim, 3 agree)

Sources: [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU), [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo) [vendor copy, tested reading]

- **v6:** "Powerful, versatile, and refined… our best model yet."
- **v6 Wild:** "Best for experimental ideas where you're pushing the envelope."
- **v6 Mini:** "A free, more efficient version of premium V6 models."

### Positioning and evidence

| | **v6** (flagship) | **v6-wild** | **v6-mini** |
|---|---|---|---|
| Vendor pitch | "reliable, precise and consistently delivers polished music across every genre and style" ([blog](https://suno.com/blog/introducing-v6)). The help centre: "Balanced, expressive, and built for a wide range of styles and prompts. Great for everyday creation." ([help 13924801](https://help.suno.com/en/articles/13924801)). TechCrunch: "reliable and steerable". | "less predictable and more varied… unexpected, textured and ambitious results" ([blog](https://suno.com/blog/introducing-v6)). The help centre: "A more experimental take on v6. Leans into unexpected choices, genre-blending" ([help 13924801](https://help.suno.com/en/articles/13924801)). CPO **Jack Brody** says it is "**less tuned towards preferences than v6**", a fix for mainstream "overfitting", aimed at niche-genre artists ([Music Ally](https://musically.com/2026/09/09/suno-launches-its-v6-ai-music-models-heres-what-you-need-to-know/)) [vendor]. CEO Mikey Shulman says he is "personally kind of addicted to it" ([weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode), single source, confirmed on fetch). A CEO line that Wild sometimes won't produce "the perfect single song" is **unsourced**: it was credited to TechCrunch, but that article quotes only CPO Jack Brody and does not contain it. | "faster, more efficient"; "better, faster results than any free model on any music creation platform" ([blog](https://suno.com/blog/introducing-v6)). The help centre: "A lighter, faster variant. Ideal for quick ideas, high-volume generation" ([help 13924801](https://help.suno.com/en/articles/13924801)) |
| Suno's intended workflow | Refine here | Generate raw ideas here, then bring them back into v6 to refine ([unite.ai](https://www.unite.ai/suno-launches-v6-music-models-built-with-warner-music-bmg-and-believe/)) [vendor via press] | — |
| Strengths, tested | Drums (snare, kick) and bass noticeably punchier and fuller than the presenter remembered v5.5; better reverb ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)). **Beat v5.5 on vocal clarity and control in 7 of 7 genres**, edged it on instrumentation in 7 of 7 (the narrowest margin), and tied on structure in most, using the same voice clone and matched prompts. This compared v6 against **v5.5 takes made before launch**; it was not a same-day controlled A/B ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)). Follows a long plain-English brief closely ([AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo)). | Won on character in indie rock ("best instrumentation of the three"), contemporary R&B and metal ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)). Much wilder on the same hummed melody plus a hard-bop prompt ("one of the wildest things I've ever heard") ([y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU)). A minimalist track stayed sparse ([Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY), sponsored). V6 Wild in Studio made a studio-quality acoustic guitar from text alone ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)). | Never generated on camera by any source |
| Weaknesses, tested | Rock still drifts to a country or southern vocal (§14). Metal and blues rock were still artifact-prone, with the smallest margin over v5.5 ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)). | **Quality drop against v6 Pro**: worse guitar and drum sound, and a viewer called it "AI-artifact-y" and the presenter agreed ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)) [tested]. Lyrics drift from the brief (an unrequested line, "meet me where the old bikes are"), with more backing vocals and bigger builds ([AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo)) [tested]. **Voice fidelity swings both ways**: furthest from the source voice on a ballad, closest on indie rock ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)) [tested]. One take came back at about 50 s with no cause found ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)). "Didn't really seem to do anything" on one Marilyn Manson-style attempt ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)) [reported]. About half of outputs unusable (outlet unresolved, WebSearch snippet only) [reported, weak]. | Downloads and rights are tied to the free plan (0 downloads on free, [pricing](https://suno.com/pricing)). "Mini has no downloads and no commercial rights" ([DMN](https://www.digitalmusicnews.com/2026/09/09/suno-v6-launch/)) [reported]. |
| Plan | Pro / Premier | Pro / Premier | Everyone |

**A practitioner framing, 2 agree.** Wild is "like the old weirdness slider, except now that choice lives right in Simple mode": v6 for precision, Wild to be surprised ([AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo)). Fish for ideas in Wild, then re-cover the winner in v6 Pro for quality ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)). Suno's own stated intent matches ([unite.ai](https://www.unite.ai/suno-launches-v6-music-models-built-with-warner-music-bmg-and-believe/)).

**Overall verdicts.**
- "Mildly impressed… some things sound better mix-wise" ([BToY](https://www.youtube.com/watch?v=BToYusaGue4), a pro producer, not sponsored) [reported].
- "Near CD quality" ([Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY), sponsored) [reported].
- The biggest jump is felt **inside Studio** ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)) [reported].
- Reception is mixed and some customers are threatening to leave ([DMN](https://www.digitalmusicnews.com/2026/09/09/suno-v6-launch/)) [reported].

### When to pick which: our proposal [spec]

- **Final D&B tracks and anything carrying the narrator's Voice:** v6. The tested evidence favours v6 for clarity and for keeping the source voice.
- **Hunting for a texture, a drop idea or a niche sub-genre:** v6-wild. It is deliberately less pop-tuned, which is the theory behind our half-time and neurofunk failures. Then **Cover the winner in v6**. The Cover route to a faithful upgrade is tested once ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8)).
- **v6-mini:** ignore. We are on a paid plan, and nothing is known about mini's quality.
- **Custom model:** reach for it when the voice has to hold. One tester found it more consistent than Voice (§8).

---

## 3. The v6 create form, control by control

**Scope.** Every row is the v6 form as seen between 2026-09-09 and 2026-09-10. Labels marked **(?)** come from garbled auto-captions or a single paraphrase. **Verify all of them against the live DOM with `suno.mts status` before a script depends on any of them.**

| Exact label (as read) | Where | Range / options | Default | What it does | Tier | Source |
|---|---|---|---|---|---|---|
| **Model picker** | Top of the create form (dropdown). Also in Studio's per-track generation box, Studio chat, and the Remix dialog. | See §2. The v6 family plus **custom models** in the same list (e.g. a user model "Chester"), plus "Create Custom Model (Beta)". | Not reported for a Pro account | Chooses the engine. v5.5 and older are **gone**. | tested (options) / reported (Custom Model entry) | [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU), [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8), [BToY](https://www.youtube.com/watch?v=BToYusaGue4), [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY), [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) |
| Voice picker's helper text | Inside the picker or Voice area | Still says "**V5.5 powers**" Voice, custom models and My Taste | — | A **stale string**. Those features work on V6 (§8). | tested | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| **Simple** / **Advanced** tabs | Top of the form | Presenters call the full form "**Advanced**" (mode or tab). **This differs from our documented tab set (Simple / Audio / Custom / Cover).** Every v6 source says "Advanced" (BToY, y2rI, AoLo, WtLn, and weraveyou's "Advanced Mode"). None shows a "Custom" tab. [xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY) shows **Edit vocals / Edit instruments / Cover** as *modes offered after an audio upload*. | — | Simple is a single box plus attachments. Advanced has Style, Lyrics, Exclude and sliders. The multimodal extras (playlist, image, video, several at once) are said to be Simple-only. **Custom is possibly renamed Advanced. Are Audio and Cover still tabs, or now post-upload modes?** [spec] | tested (tabs) / reported (Simple-only extras) / spec (the rename) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4), [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU), [b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ), [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8), [xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) |
| Simple prompt box | Simple | **3,000 characters**, with a small progress bar | — | A text description, **or an edit instruction when a song is attached** (§5) | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| **Add** / "+" attach | Simple (the "magic plus button") | **Audio**, **Image**, **Video** (mp4), **Voice**, playlist, styles from the library | none | Seeds the song from media. An attached existing song plus an instruction makes it an **edit**. Uploaded audio goes through an originality/rights check and a **Continue** step. | tested (audio, image, video, voice) / reported (playlist, styles) | [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo), [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU), [M4Hj](https://www.youtube.com/watch?v=M4HjwzE7bjY), [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Style | Advanced | **1,000 characters** | — | Unchanged | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Lyrics | Advanced | The limit is not re-checked on v6. 5,000 was the documented cap on v4.5–v5.5 ([aimusicapi](https://aimusicapi.ai/en/blog/suno-ai-prompt-character-limits)). | — | **Leave empty for an instrumental**, same as before | tested (instrumental) / spec (limit) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| **Exclude Styles** | Advanced | text | — | Still present and unchanged. **2 agree.** | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4), [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY) |
| **Vocal Gender** | Advanced, on the same panel as Max Mode | **Male**, **Female** seen. Others unknown. | not reported (AoLo *chose* none; that is a setting, not an observed default) | Sets the vocalist's gender. Can be left unset when a Voice supplies it. | tested (values) / reported (existence) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4), [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) |
| **Duration** | Advanced | **Auto** / **Custom** | not reported (AoLo *chose* Auto) | With Auto, v6 ran **longer than v5.5 in 5 of 7 genres** (§13) | tested | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) |
| **Weirdness** | "More options" panel | 0–100 (values 17, 30, 60 and 76 used on camera). Pre-v6 help calls it Safe ↔ Chaos. | **50%** (reported) | Unchanged in name and range | tested (values) / reported (default) | [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY), [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode), [help sliders (PRE-v6 text)](https://help.suno.com/en/articles/6141377) |
| **Style Influence** | More options | 0–100 (70 used). Pre-v6: Loose ↔ Strong. | **50%** (reported) | Unchanged | tested / reported | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) |
| **Audio Influence** | More options, **only when audio or a Voice is attached** | 0–100 (25 used) | not reported | How hard the attached audio or voice pulls the output. "25 is a light hand." **It still exists on v6.** Web sources that "couldn't find it" were looking at a form with nothing attached, which matches our existing DOM note. | tested (value on V6) / reported (meaning) | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| **Variety** (NEW) | More options. Reported to be visible **only when a V6-family model is selected**. | A **stepped** control with named positions, not a percentage. Low end: "**Exact style (?)**" ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8)) / "**Clips use the same style**" ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)). Middle: "**Normal**". The line "**Clips have slight style variation**" is the slider's description text shown while the default is Normal ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8)); pairing it with the Normal step is our inference **(?)**. Then "**Balance(d) variety (?)**" and "**Distinct styles (, bold exploration) (?)**". High end: "**Unreasonably varied**" (**1 clear + 1 garbled**: BToY's live reading is clear, WtLn's is "(?)"; no written source found). The step order is assembled from garbled captions [spec]. There is a reset-to-default control. **No source shows an "Off" state.** | **Normal**. **3 agree.** | **How different the two clips from one Create are from each other**: variety *between* the takes, not within a song. This comes from the label copy and 2 presenters. A claim that Variety **silently rewrites your style prompt** ("short and lackluster") traces only to an AI-summarised search result citing unspecified user reports [spec, unsourced]. Its function was never demonstrated: "it didn't seem to work for me" ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)). | tested (labels, default) / spec (step order, prompt rewrite) | [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8), [BToY](https://www.youtube.com/watch?v=BToYusaGue4), [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY); default also in [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) ("Variety, which is new and defaults to Normal") |
| **Personalize** (NEW) | Next to Variety | on / off | **off** (in one Premier account) | Help text: "**Make variety match your taste**". The presenter reads it as making taste-steering **opt-in** rather than automatic. **Probably the same control as "My Taste"** (next row). | tested (label, default) / reported (meaning) | [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8), [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY) |
| **My Taste** | Listed as a create setting | on / off | set **off** in one test | weraveyou, verbatim: "**a Personalize toggle labelled My Taste**". That is written evidence for **one control**, shown as Personalize (WtLn) and referred to as My Taste (AoLo, weraveyou). **One contradiction:** WtLn's on-screen help text, "Make variety match your taste", ties the toggle to *Variety*. The My Taste help page describes an **account-level** switch under avatar → My Taste and does not give the create-form label. Keep the live test (§16.4). | reported (one control, weraveyou) / tested (setting used) / vendor (account-level switch) | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode), [help 11362561](https://help.suno.com/en/articles/11362561) |
| **Max Mode** | Advanced, near Variety and Vocal Gender | on / off | not reported | Now a **real toggle**: "instead of having to do that whole code thing" ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)). Said to keep style and voice **consistent across generations** ([b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ)). weraveyou, verbatim: "positioned for consistency across longer songs, and for Covers and Voices." Credit cost: **unsourced** (no source gives one). | tested (exists, used) / reported (effect) / spec (cost, unsourced) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4), [b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) |
| Voice | "+" / Add menu, or the Voice attachment | the saved Voices | none | Works on V6. The persona feature is now called "Voices". | tested | [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU), [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| **Edit vocals** / **Edit instruments** | Modes offered after uploading audio | modes. Edit instruments takes a target instrument and a duration. | — | Edit vocals keeps the uploaded voice's own character. Edit instruments re-renders an idea in a new instrumentation, e.g. piano to acoustic-guitar loop. | tested | [xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY) (sponsored) |
| Create | bottom | — | — | A batch of 6 queued v6 generations finished "almost instantly" | tested | [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY) |

**Takes per Create.** Still two [spec]. The Variety copy ("clips… style variation") and [BToY](https://www.youtube.com/watch?v=BToYusaGue4)'s reading ("this clip and this clip") both imply a pair. No source counted the takes.

### What an automation script needs: changed, new or renamed

1. **The model button no longer reads `v5.5`.** Our DOM map finds it as "button whose text matches `/^v\d/`". If the collapsed label reads "Version 6 Pro" or "V6 Pro" (capital V), that regex fails.
   - Match case-insensitively on `6`.
   - Tell the entries apart by `wild` and `mini` substrings, or by the Pro badge.
   - Never select by exact string.
   - Custom models share the list, so exclude them by name.
   - [spec, from the label evidence above]
2. **v5.5 cannot be selected.** Any spec, sheet or default that names v5.5 must fail loudly rather than silently falling back. Log the exact model label on every take.
3. **Variety is new, stepped and conditionally mounted.** It is probably a `[role="slider"]` with discrete `aria-valuetext`, or a segmented control [spec]. Read it back like Duration.
4. **Personalize is new.** Our "form state persists" law almost certainly covers Variety, Personalize, Max Mode and Vocal Gender too [spec]. Add all four to the spec, the guards and `status`, or a leftover value will silently skew a grid.
5. **Personalize versus My Taste.** Probably one control (weraveyou: "a Personalize toggle labelled My Taste"). If Personalize off stops the account-wide My Taste profile from applying, the four-box atom (taste + style + exclude + lyrics) changes shape. Taste would only bite when Personalize is on. **Test this before the next prompt round** (§16).
6. **The attach menu grew: Image, Video, playlist, styles.** `formMode()` aborts on "any attachment". Make sure it recognises the new attachment chips.
7. **An attachment in the Simple box is now an edit instruction.** This is the Cover trap in a new place. A song left attached in Simple turns a fresh create into an edit of that song [spec, by analogy with our 2026-08-27 Cover incident].
8. Audio Influence still appears only with an attachment or Voice. This is unchanged, and it is **still the cheapest proof that nothing is attached**.
9. **Generations are fast.** Shorten the poll interval, but keep the pair and naming checks.
10. **Studio has its own model selector per track.** Studio automation, if we ever write it, needs its own model step.
11. **The tab labels may have changed.** We document Simple / Audio / Custom / Cover. Every v6 source says Simple / **Advanced**, none shows "Custom", and xpvX shows Edit vocals / Edit instruments / Cover as post-upload *modes*. `formMode()` probably depends on these labels. Check it against the live DOM (§16.3) before any run [spec].

---

## 4. The experiment permutation space

### The axes that now exist

| Axis | Values | Notes |
|---|---|---|
| Model | v6, v6-wild, (v6-mini), custom model(s) | Custom models may hide Variety. It is reported to show only with a V6-family model ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8)). |
| Variety | ~5 named steps (Exact style → Normal → Balanced → Distinct → Unreasonably varied) [spec: built from garbled captions] | New. Its effect is unproven. That it rewrites the style prompt is unsourced [spec]. |
| Weirdness | 0–100 | Our pair is 30 / 60 |
| Style Influence | 0–100 | Default 50 [reported] |
| Audio Influence | 0–100, only with an attachment or Voice | — |
| Personalize | on / off | New. Probably the same control as My Taste (weraveyou: "a Personalize toggle labelled My Taste"). |
| My Taste | on / off, plus the account-wide profile text | Part of the four-box atom |
| Max Mode | on / off | Credit cost unsourced |
| Vocal Gender | unset / Male / Female | — |
| Duration | Auto / Custom | v6 Auto runs longer |

### What practitioners actually used

- **The 7-genre voice-clone A/B** ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)) [tested]: Advanced, no vocal gender, Duration Auto, **Weirdness 60, Style Influence 70, Audio Influence 25, Variety Normal, My Taste off** for v6 and v6-wild. **The v5.5 settings are unverified:** Variety appears only with a V6 model, and v5.5 could not be selected from launch day, so the v5.5 takes were made before launch and cannot have had "Variety Normal". This is still the closest thing to a published control grid, but it is not a controlled same-settings A/B.
- **Remixing in Wild** ([Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY)) [tested, sponsored]: Pro to Wild, Weirdness 76. The presenter preferred the Wild remix.
- **Mass generation** ([b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ)) [reported]: Max Mode **on** for a consistent sound.
- **Variety**: advice to keep it low or Normal for predictable style control comes only from an AI-summarised search result [spec, unsourced]. weraveyou says only "Variety, which is new and defaults to Normal."
- **(PRE-v6, not re-tested on v6)** Goal recipes from [sunostyles](https://sunostyles.com/blog/understanding-suno-parameters) [reported]:
  - genre-accurate: Weirdness 10–25 with Style Influence 80–100
  - creative but listenable: Weirdness 30–50 with Style Influence 60–80
  - structured experiment: Weirdness 50–70 with Style Influence 60–80
  - full exploration: Weirdness 60–100 with Style Influence 20–50
  - above Weirdness 80 it is a lottery
- **No one has published a v6 model × variety × weirdness grid yet** [reported, [suno-cli](https://github.com/paperfoot/suno-cli), [suno-automation.com](https://suno-automation.com/), [ttapi](https://docs.ttapi.io/api/en/suno), all pre-v6 tooling]. There is still no official public Suno API.

### A proposed minimal grid for BadCode [spec]

Principles we keep: the **pair** (Weirdness 30 and 60), the **four-box atom** (prompt rounds and slider rounds never mix), and **one variable per round** (the session method).

**Before any grid, set a baseline.**
- Personalize off.
- My Taste written and read back as the sheet's taste.
- Max Mode off, Variety Normal, Style Influence 50.
- Vocal Gender unset unless the sheet sets it.
- Duration explicit.
- **Log the credit balance before and after every Create.** That is how we learn the per-generation cost.

| Round | Varies | Cells | Creates (≈clips) | Question it answers |
|---|---|---|---|---|
| **R1: model × pair** | model ∈ {v6, v6-wild} × Weirdness ∈ {30, 60} | 4 | 4 (8) | Does Wild beat v6 on our D&B and narration sheets, and does the 30/60 winner flip between models? |
| **R2: Variety** | Variety ∈ {lowest, Normal, highest} on the R1 winner | 3 | 3 (6) | Does Variety change the *within-pair* difference? **Also read back each take's displayed style text to see whether Suno rewrote our prompt.** |
| **R3: Max Mode** | off / on on the winner | 2 | 2 (4) | Consistency against credit cost |
| **R4: Personalize** | off / on, with a *known* My Taste profile | 2 | 2 (4) | Is Personalize the gate on My Taste? This settles the atom. |

That is 11 Creates. Only R1 is needed to start producing. Style Influence and Audio Influence stay out until R1–R3 are settled, because we already have v5.5-era rules for them. Do not run v6-mini.

---

## 5. 🔑 Fixing one word, one bar or one phrase

### The headline

- **Suno now claims** "Update a single lyric without rebuilding the entire song. Change one word or line while leaving the rest intact" [vendor, [blog](https://suno.com/blog/introducing-v6), [release notes](https://suno.com/release-notes)].
- **Two independent on-camera tests** show a single-word swap in an existing song coming back sounding like the same take: [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo) and [xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY).
- **One test** shows a multi-phrase swap on an *uploaded* song wrecking the instrumental 3 times out of 3 ([b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ)).
- **Nobody has diffed the audio.** "Sounds the same" is by ear only.
- **Do not confuse lyric-*text* editing with the v6 audio edit.** The July 2026 lyrics-editor rebuild and Lyricist's natural-language edits change the lyric *text* only (PRE-v6). They are **not audio fixes**. Their phrasing is still the best template for a one-occurrence instruction, e.g. "Replace street lamp with neon light in the third line of the second verse, keeping the rhyme and line length unchanged" ([suno.bi](https://suno.bi/en/blog/suno-lyrics-workflow), 2026-08-05, PRE-v6) [reported].

Our pain splits into four sub-problems, and the evidence differs for each:

- **(A)** the wrong word is sung (a text change)
- **(B)** the right word is sung badly (the same text needs a re-sing)
- **(C)** the backing needs removing in one bar
- **(D)** the singer's cadence needs changing in one bar

### Ranked ladder

#### 1. Simple-mode "attach the song + instruction" edit (new in v6)

**Best for (A). Untested for B, C and D.**

**Tier:** tested (2 successes, of which 1 unsponsored and 1 sponsored; 1 failure; 1 over-reach), plus the vendor claim.

**Click-path** ([AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo)):
1. Create → **Simple**.
2. **Add** → **Audio** → pick the existing song from the library, or upload it.
3. Type the instruction. Verbatim: *"Change the word summer to sunset everywhere it appears in this song. Keep everything else exactly the same."*
4. Model **V6**, then **Create**.

**Settings.** None were shown beyond the model (v6 flagship). It is untested on Wild or Mini.

**Minimum region.** Returns a new clip; whether audio outside the edited word was regenerated is unknown [spec]. The *audible* change was limited to the word, at all 3 places it occurred ([AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo)) [tested, by ear].

**How well the voice matches.** "Same voice, same instrumental, same arrangement" by ear ([AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo)). A second test, *"change never to always throughout"* on a **native Suno track**, swapped the word everywhere "with no noted instrumental damage" ([xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY), sponsored).

**The presenter's framing.** Before v6 this needed Studio or the Editor; now it's in Simple ([AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo)) [reported]. **Qualified:** Suno's own undated lyric-fix help page offers only **Reuse Prompt** and **Extend**, plus Studio stems, and warns that songs are "one audio file containing all music and words" ([help 2417409](https://help.suno.com/en/articles/2417409)) [vendor]. It does not mention the Song Editor for this job.

**Failure signs:**
- **The backing or instrumental is corrupted.** This happened 3/3 when the upload was an **external MP3** and the instruction replaced **several multi-word phrases of different syllable counts** ([b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ)) [tested]. The presenter says they are "still working out the kinks" and recommends pulling stems and editing by hand.
- **The whole song is restyled, not just the target.** An instruction worded globally ("have it all sung in operatic classical choir mode") changed everything. The spoken example had been a chorus-only edit ([y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU)) [tested].
- **Parts of a compound instruction are ignored.** Asking to swap the Voice, the custom model and the genre at once did **not** apply the Voice: "So that didn't work. So that was a lie." ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)) [tested].
- **Our synthesis of the working boundary [spec]:** same-syllable, single-word swaps on a native generation work. Multi-word, different-syllable changes on an upload break. The in-between cases are untested.

**Unknowns:**
- Whether you can target **one occurrence** rather than "everywhere".
- Whether it fixes a **mispronunciation with unchanged text** (B).
- The credit cost. Probably a full Create [spec].
- Whether it is surgical or a full regeneration tightly conditioned on the original. The mechanism is unexplained. The whole-song restyle result suggests full regeneration [spec].

**For us:** a text-level fix with a null-test gate (§16, test 1).

#### 2. Replace Section (the Song Editor)

**The vendor-documented section selector in the create library. Fits (A) and (B), at 10–30 s per the 2024 note (see 2b for a finer Studio selector).**

**Tier:** vendor (the mechanism, **PRE-v6**, 2024), vendor (undated v6 framing), reported (behaviour).

**v6 status:**
- **The v6 blog does not mention Replace Section.** A direct fetch finds no "Replace"; "Pro and Premier" appears there only in the gating of the v6 and v6-wild models.
- The only vendor source linking it to v6 is an undated help page: "Remix & Edit— Extend, Cover, Replace Section, and more, all powered by v6" ([help 13924801](https://help.suno.com/en/articles/13924801)) [vendor, undated].
- The tool, its menu path, its limits ("must be 10-30 seconds long", two versions) and its Pro/Premier requirement date from **2024-10-10** ([release note](https://about.suno.com/release-notes/replace-section)) [vendor, PRE-v6]. No v6-dated source says the limits changed.

**Click-path, the classic version** (vendor, PRE-v6: [release note](https://about.suno.com/release-notes/replace-section), [help 3271873](https://help.suno.com/en/articles/3271873)):
1. Song → **⋯ More Actions** → **Edit** → **Replace Section**.
2. Drag-select **10–30 s**. The lyrics for that span populate the **Replace Lyrics** box.
3. Edit the text, or add a stage direction such as `[drum break]`.
4. Click **Replace Section**. Two candidates come back. Click **Select** on the one you want.

**Click-path, the newer Song Editor** ([help 6141505](https://help.suno.com/en/articles/6141505), undated; labels confirmed on a direct fetch: Replace, Quick Replace, Edit Lyrics, Replace Lyrics, Replace Section, Edits Library, Generate More. The article states **no minimum or maximum length** and does not mention v6) [vendor]:
1. "Select a clip or highlight a region" on the waveform.
2. Click the orange **Quick Replace**, or use **Replace** / **Edit Lyrics** in the left panel.
3. Edit the text in **Replace Lyrics**, then click **Replace Section**.
4. Candidates land in the **Edits Library** on the right. Use **Generate More** for alternatives.
5. Drag the boundary line on the waveform to move the seam.

[Tom's Guide](https://www.tomsguide.com/ai/suno-just-got-a-major-upgrade-now-you-can-replace-a-verse-or-chorus) describes the same "stripe-select" flow (snippet only, still undated after a second fetch, which was truncated). [suno.com/blog/songeditor](https://suno.com/blog/songeditor) (**2025-06-03, PRE-v6**) mentions a "creativity slider" for how far the replacement strays.

**Settings:** only the region, the lyrics and the creativity slider (a 2025 Song Editor control; whether it survives on v6 is unknown).

**Region: 10–30 s per the 2024 note**; not stated in the current Song Editor doc; HookGenius shows 2 s in Studio (2b); **unconfirmed on v6**. 15–20 s is recommended for clean transitions [vendor, PRE-v6 (the 2024 note); reported, PRE-v6 ([aidiy](https://www.aidiy.tech/post/how-to-actually-use-suno-s-new-replace-section-feature-instructions-plus-bonus-the-arrow-song), [aimusicpreneur](https://www.aimusicpreneur.com/ai-tools-news/replace-sections-suno-ai-music-generator/), 2024)]. "You can't edit single words" with this tool (aimusicpreneur, 2024).

**How well the voice matches.** Melody and voice "usually" carry through ([JR-RS](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/replace-section-suno-editor)) [reported]. No guarantee is stated anywhere. The whole selected window is re-sung, not just the word.

**For (B), the text is right but the singing is wrong:** select the smallest region the editor accepts around the word (10 s under the 2024 limits), leave the lyrics **unchanged**, regenerate, and pick between the 2 candidates [spec, the natural use].

**Failure signs** ([JR-RS](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/replace-section-suno-editor), [JR one-word](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/why-does-changing-one-word-in-my-chorus-cause-glitches-in-suno); both **PRE-v6** or undated) [reported]:
- **Audible seams** at tight selections. Pad the selection with clean audio on both sides.
- **Melody changes** even when told to keep it.
- **Hissing, "as if two versions were playing"**, after *sequential* edits on the same track. Never chain edits in a pipeline.
- A 2–3 word request (~2 s) produced 30–40 s of regenerated audio. Sources read this either as the regenerated span or as the generation time (§15).
- Single-word swaps misalign syllables and stress against the existing melody. Regenerate the whole line or section instead.
- **Replacing part of a *vocal stem* was not easy with Replace Section** in the Studio beta ([aicentral](https://substack.aicentral.blog/p/suno-studio-now-in-beta), 2025-08-21) [reported, PRE-v6].

#### 2b. Studio "Regenerate Section" on the waveform (PRE-v6)

**The nearest thing to a word-level selector found. Fits (A) and (B) if it still exists.**

**Tier:** reported, **PRE-v6** ([HookGenius](https://hookgenius.app/learn/suno-studio-tutorial/), February 2026, fetched).

**Exact label:** "**Regenerate Section**", in Suno Studio.

**Click-path:** "Click and drag on the waveform to highlight the section you want to change. This could be 2 seconds or 30 seconds." Then regenerate.

**Region:** about **2 s** at the low end, 30 s at the top. **This contradicts the 10 s floor** in method 2, which comes only from the 2024 note.

**Cost:** credit use is proportional to the length regenerated (HookGenius).

**How well the voice matches:** not addressed by the source. Untested on v6.

#### 3. Stems + a manual mute or comp (deterministic, no generation)

**The only reliable route for (C).**

**Tier:** tested (labels and export), plus our method.

**Click-path** ([xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY)):
- Song → **Edit** → **Get stems or MIDI** → **Lead vocal** and **Everything but lead vocal** → **Download**.
- Or: **Open in Suno Studio** → **Multi-track** for full separation. Each stem can be soloed and downloaded.
- Or: Studio **Export** → **multi-track**, which gives a .zip of one file per track ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)) [tested].

**Then:** in Premiere or a DAW, cut or mute "Everything but lead vocal" for the bar, then re-sum.

**Region:** sample-accurate, any length. **Voice match:** identical, because nothing is regenerated.

**Failure signs:**
- Separation artifacts: a weak or unusable isolated bass, and guitar with baked-in processing on a v6 blues-rock take ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)) [tested].
- The **exported stem is quieter** than in-app monitoring ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)) [tested].
- One exported keys stem came back **offset in timing** ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)) [tested]. Null-check the stems against the mix before comping.
- It costs a download unless Studio exports are exempt (§7). **Downloads stay human-only under our protocol.**

#### 4. Studio: regenerate a vocal region or a single part on its own track

**A new take to comp in. Not in place.**

**Tier:** tested.

**Vocal region** ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)):
1. Select a region on the vocal track.
2. Type the lyrics and a vocal-style prompt, choose V6 or V6 Wild, and generate.
3. Cycle the takes with the **up/down arrows**.
4. If the requested bar count doesn't match the selection, Studio offers to generate it "**on a new vocal track**".

The result is a **fresh take**. It follows the underlying chords and key, with excellent phrasing, but the timbre is still "lasery, phazy, metallic". The loop marker that sets the region was **fiddly to resize** (8 to 16 bars failed). Bar-level selection is hard, and word-level is harder.

**A single part** ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8)):
- Studio chat → pick a V6 model → *"Add an additional electric guitar track"* → a clean new stem appears, with no bleed, and cleaner than the separated original.
- For a double-tracked part: pull the stems, then generate a copy of the one instrument in Studio. "Real finicky. It doesn't always work." Root cause: Suno generates the whole song at once, not stem by stem ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)) [reported].

**Guide-vocal steering for (D), cadence** [reported, [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)]: the presenter recorded a scratch vocal in an external DAW and imported it to steer the AI vocal's melody and phrasing. This is the only cadence lever found, and it produces a new take, not a patch.

#### 5. Studio "Remove Effects"

**Fixes (C)-adjacent problems: reverb or FX baked into one stem.**

**Tier:** tested (label) / mixed (result).

**Click-path:** right-click the audio clip → **Remove Effects** ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)). This was already documented; the v6 videos confirm the label.

**Result:** it **did not meaningfully help** a v6 guitar stem whose processing was baked into the generation ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)) [tested]. [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) mentions de-reverbing a vocal but never shows it.

#### 6. Sample (Beta) on the problem phrase

**A workaround for (A) or (B).**

**Tier:** reported, **PRE-v6**; the source was 403 and only its snippet was seen ([genxnotes](https://genxnotes.com/en/posts/fix-lyrics-mistake-in-suno/)).

Sample just the phrase and regenerate it with corrected lyrics. Whether voice and backing are preserved is unknown.

#### 7. Cover the whole song on v6

**An upgrade path, not a fix.**

**Tier:** tested once.

**Click-path:** original song → **Cover** → model V6. The result was "pretty similar" and better (wider, rounder, harsher tone fixed). It was the best of *several* cover attempts ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8)).

By contrast, the **same prompt and the same lyrics as a fresh Create** gave a different song (tempo, density, feel) on both v6 and Wild ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8)) [tested].

#### 7b. Remaster on a newer model

**An upgrade path that *claims* to keep the vocal performance.**

**Tier:** vendor, seen only as a search snippet (the help article URL 404'd). Not dated; not confirmed for v6.

**Click-path:** song → **⋯ More Actions** → **Create** → **Remaster**. Two variants come back.

**What Suno says it does:** rebuilds a song on a newer model while "keeping original structure, lyrics, melody and vocal performance".

**Unknown:** whether v6 is offered as the target for a v5.5 take (§16.12).

#### 8. External tools

**Tier:** reported.

If the performance is good but the voice doesn't match, swap it with a dedicated voice-cloning tool outside Suno. "Suno optimises for a good performance, not fidelity to a voice" ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)). The tool's name was garbled in the captions.

#### 9. Regenerate the whole song

Today's baseline.

### Sub-problem × method

| | (A) wrong word | (B) word badly sung | (C) no backing in one bar | (D) cadence in one bar |
|---|---|---|---|---|
| 1. Simple attach + instruction | ✅ tested ×2: 1 unsponsored + 1 sponsored (same syllable, native track; by ear) | ❓ untested | ❓ untested | ❓ untested |
| 2. Replace Section | ⚠ vendor, PRE-v6 (2024 text: 10–30 s, whole window re-sung); never tested on v6 | ❓ spec (the natural use; untested) | ⚠ you can type `[instrumental]`-style directions, but the vocal is re-sung (vendor, PRE-v6) | ⚠ whole window re-sung (spec) |
| 2b. Studio Regenerate Section | ⚠ reported, PRE-v6 (~2 s selection; voice match not addressed) | ❓ reported, PRE-v6 (untested) | ❓ untested | ❓ untested |
| 3. Stems + mute/comp | ✗ | ✗ (unless comping from another render) | ✅ **deterministic** | ✗ |
| 4. Studio region / guide vocal | new take on a new track | new take | add or replace a part | guide vocal steers phrasing (reported) |

### What still cannot be done (as of 2026-09-10)

- **No source demonstrates a true punch-in** that re-sings one word while leaving every other sample of the take bit-identical.
  - The best tested method (1) returns a new clip; whether audio outside the edited word was regenerated is unknown [spec]. It *sounded* identical in two tests.
  - Replace Section (2) re-sings a window of 10–30 s per the 2024 note. Studio's Regenerate Section (2b) accepted a ~2 s selection before v6 (HookGenius); neither is confirmed on v6.
  - Nobody has null-tested any of them.
- **Suno's own product chief says bar-level precision is Studio's manual job.** CPO Jack Brody: "Studio 2.0 allows you to get in the weeds and manipulate these things by hand. Oftentimes, that is the fastest or most precise way, and natural language will never be better." And: "It's very difficult to say 'Hey, at the third downbeat in the second verse, at 22 seconds, I want it clipped by 4.3…' You can just move the waveform." ([Music Ally](https://musically.com/2026/09/09/suno-launches-its-v6-ai-music-models-heres-what-you-need-to-know/)) [vendor].
- **Changing cadence in one bar while keeping the same take:** no method found, from vendor or practitioner. The vendor's word is "section", never "bar".
- **Removing the backing in one bar:** only possible outside generation, via stems and a manual mute.
- **Fixing a mispronunciation with the text unchanged:** untested in every source.
- **The vendor never promises** that a word or section edit keeps "the same voice" or "the same take". The copy says only "leaving the rest intact" or "preserving everything else" ([blog](https://suno.com/blog/introducing-v6)). An independent outlet stresses these are "announced capabilities, not results from a listening test" ([SiliconSnark](https://www.siliconsnark.com/suno-v6-adds-precision-editing-siliconsnarks-token-disco-empire-demands-a-remaster/)).
- **The mechanism is unconfirmed.** Is the v6 "change one word" the same machinery as Replace Section, a new chat-style editor, or Simple-mode conditioning? No source says. The tested path is the Simple-mode attach (method 1).

---

## 6. Studio with v6

The Studio 2.0 features we already document are omitted unless v6 changed them or the videos re-confirmed a label.

| To do this | Do this | Tier | Source |
|---|---|---|---|
| Generate a track with a v6 model | Add a track → the generation prompt → the **model** dropdown → choose e.g. **V6 Wild** | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA), [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8) |
| Generate from text only | Toggle the per-track **reference** off, then type the prompt. Studio leans toward wanting a reference but doesn't require one. | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Skip picking an instrument category | Just describe it ("acoustic guitar, guitar licks, hammer ons"). The instrument is **inferred from the text** and no instrument dropdown is needed. | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Set the tempo | The **BPM** field has moved to the **top right** (it used to be at the bottom) | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Try alternative takes of a part | The **up/down arrows** on the track. Nothing says what differs between takes. | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Get usable parts | Keep prompts simple. "Live electric bass, R&B style" was too busy twice; "electric bass simple" worked. "Hip-hop drums, rim snare, loose groove" gave realistic drums (the hats needed an EQ dip). | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Reduce clashes between parts | Hypothesis: generate the new part with the existing track as its **reference**. Not tried. | spec | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Add an instrument to an existing song | Open the song in Studio with separated stems → **chat** → pick a V6 model → *"Add an additional electric guitar track"*. You get a clean new stem with no bleed. | tested | [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8) |
| Generate a vocal from written lyrics | Vocal track → select a region → type lyrics and a vocal-style prompt → generate. It follows the chords and key. A bar-count mismatch gives "generate on a new vocal track?" | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Draft lyrics | The vocal track's **Lyrics** action drafts from a one-line brief. Judged "generic". | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Arrange | The new timeline **snap** | reported | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Build a custom effect | Plugin creation → *"create a soft clipper"* → apply to the master. It writes real DSP code, including anti-aliasing. **Already documented; re-confirmed on v6.** | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Strip reverb or FX from a clip | Right-click the clip → **Remove Effects**. Weak on baked processing (§5). | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4), [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| Export stems | **Export** → **multi-track** → a .zip, one file per track | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Change tempo by chat, move or copy a plugin | BPM-aware chat, plugin drag-and-drop between tracks (**2026-09-02, PRE-v6**). Chat undo and Cmd/Ctrl-D are **unverified** (summariser only; not in a direct fetch). | vendor (BPM chat, drag-and-drop) / unverified (undo, Cmd/Ctrl-D) | [release notes](https://suno.com/release-notes) |

**Studio observations** [tested unless marked]:
- Studio-generated stems sound higher fidelity and less "hollow" than the same instruments in a full-song generation ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)) [reported].
- A chat-added guitar was cleaner than the separated guitar from the same song ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8)).
- Generations still occasionally **bleed onto the wrong track** (a backing-vocal generation blended with the flute), though less often than before ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)).
- Browser recording versus an imported file: there may be a quality gap, but the presenter is unsure it still exists ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)) [reported].
- The v6 launch copy mentions Studio 2.0 without detail. CPO Jack Brody frames Studio's manual tools as for "precision work" and plain-language editing as coexisting with them: "natural language will never be better" for hand-precise edits (§5) ([Music Ally](https://musically.com/2026/09/09/suno-launches-its-v6-ai-music-models-heres-what-you-need-to-know/)) [vendor].
- Whether the old standalone Create tab was reorganised into a "Library / all songs / uploads" area is unresolved. The presenter retracted his own claim ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)) [reported].

---

## 7. Stems, audio quality, export

### Stems

- **The "Get stems or MIDI" menu** ([xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY)) [tested]: **Lead vocal**, **Everything but lead vocal**, and **Fixed tempo, MIDI file** (the generated chords as MIDI). Each downloads separately.
- **Separation modes, June 2026 (PRE-v6, still the current mechanism)**: **Auto Split** (up to 12 stems), **Split from Mix** (one element plus a companion), and **Advanced Split** (~100 instruments, Premier only). The stems are *regenerated*, not extracted ([blog, 2026-06-11](https://suno.com/blog/stem-separation-updates)) [vendor]. **No source makes any v6-specific stem claim.** The v6 blog and release notes don't mention stems.
- **v6 stem quality on one blues-rock take** ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)) [tested]:
  - Drums crisp and usable, but the cymbals artifact.
  - Bass weak and unusable in isolation.
  - Guitar heavily compressed, and not rescued by Remove Effects.
- **More stems** (individual drum elements, lead versus backing vocals) are only an *expectation* ([undetectr](https://undetectr.com/blog/suno-stems-daw-workflow)) [spec].

### Audio quality on v6

| Claim | Tier | Source |
|---|---|---|
| Punchier snare and kick, fuller bass, better and more natural reverb | tested (by ear, a pro producer) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Clean, natural vocals; stereo and spatial distribution "second to none" (no A/B played) | reported | [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU), [M4Hj](https://www.youtube.com/watch?v=M4HjwzE7bjY) |
| Clarity and separation "a big step up from v5.5, near CD quality" | reported (sponsored) | [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY) |
| Handles sparse arrangements better; earlier models over-produced | reported (sponsored) | [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY) |
| **Sibilance is "heavily de-noised… hollow and smeared" and sounds synthetic**, like over-used Soothe or RX | reported (a viewer; the presenter didn't dispute it) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| A brush snare panned **hard left and loud**, an unintended mix artifact | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Studio vocal timbre is still "lasery, phazy, metallic" | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| Uploaded-song handling has frequent static and "sounds flat" | reported (chat) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |

- Vendor copy says only "faster, more expressive and higher quality", "higher-fidelity", with **no specs** ([blog](https://suno.com/blog/introducing-v6)).
- Sample rate, bit depth and loudness target for v6: **unknown**. The only figures (MP3 or WAV, 44.1 or 48 kHz, 16 or 24 bit) are third-party and **pre-v6** ([musicmake v5](https://musicmake.ai/blog/suno-v5-audio-quality-khz-2026)).
- Known pre-v6 artifact bands (2–4.5 kHz harshness, 8–16 kHz shimmer) are not tied to v6 either way ([neuralanalog](https://neuralanalog.com/fix-suno-hiss), [sunofix](https://sunofix.app/how-to-remove-suno-artifacts/)) [reported, PRE-v6]. **Our delivery-QC gate applies unchanged.**

### Export and downloads

- **Studio export and the download cap.** Three sources lean toward Studio exports being exempt; none is conclusive:
  - Premier gets "unlimited exports specifically inside Suno Studio" (the ToS as cited by [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)) [vendor via video].
  - A help FAQ summary says Studio workflows are "not subject to download limits". This did **not** reproduce on a direct fetch ([help 13614785](https://help.suno.com/en/articles/13614785)) [reported].
  - A multi-track export did not appear to debit the download count ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)) [reported, the presenter was unsure].
- **You decide (Kai):** whether Studio exports become the default route out of Suno. Our no-automated-downloads rule stands either way.
- **Remaster** (§5, method 7b): Suno help text, seen only as a search snippet because the article URL 404'd, describes rebuilding a song on a newer model while "keeping original structure, lyrics, melody and vocal performance". Two variants, via ⋯ More Actions → Create → Remaster [vendor, snippet only]. Whether it offers v6 as the target is **unknown** (§16.12).
- Exported stems print **quieter** than in-app, and one stem came back **time-shifted** ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)) [tested].

---

## 8. Voices, custom models, Lyricist, consistency

| Claim | Tier | Source |
|---|---|---|
| **Voice works on V6.** Used in a 7-genre A/B with a trained clone, and on a rant-to-song. "Persona" is now "Voices". **2 agree.** | tested | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU) |
| **Contradiction:** the live Voices FAQ says *"Confirm that model v5.5 is selected… Other models do not support the New Voices feature."* It doesn't mention v6. It was probably not updated. | vendor (likely stale) | [help 11362433](https://help.suno.com/en/articles/11362433) |
| The in-app text still says "V5.5 powers" Voice, custom models and My Taste. It is a stale string. | tested | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| **Custom models work on v6.** Vendor: custom models let you "Fine-tune v6 on your own tracks for a personalized sound." | vendor | [help 13924801](https://help.suno.com/en/articles/13924801) |
| **Custom models are still selectable** and sit in the model list. You must switch off one to test base-model behaviour. | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| **A custom model is more consistent than Voice:** "The custom model seems to work better for consistency of vocals than the actual voice feature." The same presenter: "almost consistent but not 100%." | tested (one presenter) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| A custom model plus a Voice fixed the southern-rock drift and hit the target singer | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Swapping Voice, custom model and genre on an existing take by plain-language instruction **did not apply the Voice** | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| **Wild's voice fidelity swings** between the furthest from and the closest to the source voice, depending on the genre and arrangement | tested | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| **Judge fidelity in the quiet sections.** Sparse verses reveal the voice's identity; dense choruses hide it. Do this on every model. | reported (method) | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| "Create Custom Model (Beta)", 100 credits, built from uploads. Not in the launch copy. | reported | [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) |
| My Taste and Personalize: probably one control ("a Personalize toggle labelled My Taste"); see §3. The launch blog mentions neither. | tested / reported | [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) |
| **Lyricist and Inspo: no v6 information at all.** Lyricist dates from the 2026-07-09 lyrics-editor rebuild (PRE-v6). | spec (gap) | [roo](https://roo.beehiiv.com/p/suno-lyrics-editor-update-july-2026) (PRE-v6) |
| No v6-native recurring-vocalist mechanism beyond Voice and custom models. "Lyric Persona" is a prompting habit, not audio consistency (PRE-v6). | reported | [suno.bi](https://suno.bi/en/blog/suno-lyrics-workflow) (2026-08-05, PRE-v6) |

**For us [spec]:**
- The narrator's Voice should survive the move to v6 (tested by others).
- **We cannot re-run any accepted v5.5 sheet on v5.5.** For example, the Camping duet accepted at round 17.
- A v5.5 sheet re-run on v6 will not reproduce the take ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8)). **Cover** is the tested bridge.
- Our earlier ruling that a Voice has no section scope and is wrong for a duet still stands. Nothing in v6 adds section-scoped Voice.

---

## 9. Prompt craft changes on v6

| Finding | Tier | Source |
|---|---|---|
| **Long plain-English briefs work.** A jargon-free paragraph (genre, instruments, vocal character, a bridge instruction, an ending instruction) was followed closely, including a stripped-back-then-full ending. **3 agree.** | tested | [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo), [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU), [M4Hj](https://www.youtube.com/watch?v=M4HjwzE7bjY) |
| v6 responds much more strongly to detail. "The more specific the prompt, the better the output." | reported | [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY), [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU) |
| A mood-only scenario with no genre ("pretending to work when your boss is walking past") still gives a produced, on-theme song | tested | [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU) |
| **Doubt about metatag adherence:** "who knows if Suno will even listen to 90% of those metatags." In one hip-hop A/B, a **plain ChatGPT prompt beat a metatag-heavy one**. | tested (one A/B) / reported (doubt) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Both prompts shared the same **lyric-repetition tic** (over-using "every"). It lives in the base lyric writing, not the prompt. | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Prompts from a frontier LLM (GPT-6 Astra, Claude) beat a cheap custom GPT | reported | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| **The same Style and Lyrics as an old v5 song gives a different song on v6 and on Wild.** Old sheets are not portable as takes. | tested | [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8) |
| Limits unchanged: Simple 3,000, Style 1,000, Studio prompt 1,000. Lyrics limit not re-checked. | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Exclude Styles unchanged | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4), [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY) |
| **Variety may rewrite the style prompt.** Traced only to an AI-summarised search result citing unspecified user reports; not in weraveyou. | spec (unsourced) | — |
| Suno's marketing: "no mode picking, no technical setup… version six reads the intent". This contradicts the model dropdown it shows (§15). | vendor | [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU) |
| Section tags ([Verse], [Chorus]) and bracket tags: **no v6-specific source**. A pre-launch blog speculated they'd remain. | spec | [note.com (pre-launch)](https://note.com/hoboai/n/n76b6ef2cb9cd?hl=en) |
| Content filter: no v6-specific change found. All documentation is v5.5-era. | reported (PRE-v6) | [hookgenius](https://hookgenius.app/learn/suno-content-filter-blocked-words/) |

### Worked examples, verbatim from sources

- **The edit instruction** (Simple, with the song attached) ([AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo)): `Change the word summer to sunset everywhere it appears in this song. Keep everything else exactly the same.`
- **The word swap** ([xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY)): `change never to always throughout`
- **An engineered breakcore style** that worked in both v6 and Wild ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)), **normalised** from the auto-transcript (which reads "jungle brakes… dark synth baseline"): `aggressive breakcore instrumental, rapid chop, jungle breaks, hyperdetail percussion, dark synth bassline, euphoric melodic chops`
- **A plain-English brief** ([y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU)): `late summer breakup, acoustic guitar, brush drums, tired but clear female vocal, intimate chorus cracks open on a single voice`
- **Timestamp sampling** ([blog](https://suno.com/blog/introducing-v6), done in [b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ)): `Sample the riff at 0:45, isolate the guitar, build a beat around it`
- **A mashup** ([blog](https://suno.com/blog/introducing-v6)): `Take the vocals from x, drums from y, and add new lyrics about losing control, make it 80s synthwave`
- **A section restyle** ([blog](https://suno.com/blog/introducing-v6)): `Change the chorus so it's sung by a gospel choir`
- **Duet tags** ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)): `[Verse 1]` with `Male vocal`, then after 4 lines `[Pre-Chorus]` with `Female vocal`

### Our proposal for a BadCode D&B style, to test [spec]

Translate the breakcore lesson: name the **drum mechanics**, not just the genre. For example: `174 BPM drum and bass, full-tempo two-step breakbeat NOT half-time, chopped amen breaks, rolling reese bass, …`. Put `dubstep, trap, two-step garage` in Exclude. Check it against our `docs/suno-gpt/` D&B guidance before use.

---

## 10. Vocals: speech and narration, rap, duets, accents

- **Speech and narration: no v6-specific evidence anywhere** [spec, a gap]. Seven web agents searched for it.
  - Our dry-and-separate rule (never generate voice and music together) still applies.
  - A new lever to test [spec]: a Studio vocal track generated from typed lyrics plus a style prompt ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)). Can it carry dry spoken delivery with no bed?
- **Rap:**
  - The hip-hop test showed the lyric-repetition tic ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)) [tested].
  - An attempt to apply a "mic rap" Voice by instruction failed ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)) [tested].
  - Nothing else was found.
- **Duets:**
  - Explicit `Male vocal` / `Female vocal` plus section tags produced a real alternating duet, "not bad", with each voice staying in its section [tested].
  - Just writing "male and female" in a Simple-mode style also worked, and was "maybe better, maybe I'm tripping" [tested].
  - **There is no duet control** ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)).
  - Adherence couldn't be compared against older models, because they are gone.
- **Vocal Gender** is a first-class control: Male or Female ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)) [tested].
- **Accents:**
  - Rock and rock-adjacent prompts **still default to a country or southern vocal**, 3 of 3 attempts, including Max Mode and a Breaking Benjamin-style prompt ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)) [tested].
  - The fix was a custom model plus a Voice.
  - **No UK or British accent evidence** of any kind [spec, a gap]. This matters for our narrator and needs our own test.
- **Sibilance** is smeared and hollow ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)) [reported]. It is relevant to spoken narration, where sibilants are exposed.
- **Humming or singing a melody seeds the song** (Audio → record → Continue after the originality check) ([M4Hj](https://www.youtube.com/watch?v=M4HjwzE7bjY), [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU)) [tested]. This is a cadence lever for a whole song, not one bar.

---

## 11. Electronic and drum & bass on v6

| Claim | Tier | Source |
|---|---|---|
| **A plain "liquid DnB" prompt failed:** "That does not sound like D&B… maybe it's two-step D&B drums." The drum programming is suspected to default to two-step rather than breakbeat. | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| **An engineered breakcore/jungle prompt succeeded in both models.** Wild: "Not bad… I don't like that dubstep snare, too heavy for breakcore." Pro: "That's pretty [expletive] good." | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| The lesson from the same session: prompt engineering may matter more than the model for D&B | spec (the presenter's material doesn't separate the two) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Wild is deliberately "less tuned towards preferences" so niche genres aren't pulled toward pop | vendor | [Music Ally](https://musically.com/2026/09/09/suno-launches-its-v6-ai-music-models-heres-what-you-need-to-know/) |
| "Across every genre and style". No mention of D&B, jungle, neurofunk, 174 BPM, half-time, reese or breaks in any vendor text. | vendor (generic) | [blog](https://suno.com/blog/introducing-v6) |
| Restyling a loop kept its BPM (101 BPM confirmed in a DAW) | tested (sponsored) | [xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY) |
| Building a beat from a non-musical sound (a dog bark) worked with a longer clip. **A ~5 s clip errored repeatedly.** | tested | [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo) |
| Studio per-track drums are realistic from a short text prompt (hip-hop only) | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| No other v6 D&B, jungle, neurofunk, garage, grime or dubstep test exists. The [weraveyou April review](https://weraveyou.com/2026/04/review-suno-ai-music-generator-electronic-producers/) is **v5.5 (PRE-v6)**, and [MusicTech](https://musictech.com/reviews/digital-audio-workstations/suno-studio-review/) is **V5, January 2026 (PRE-v6)**. Excluded. | reported | — |
| No dedicated BPM or key field on the create form. You still type it into Style. | spec (gap) | — |

**Our reading [spec].** Our known v5.5 failure (half-time drums instead of full-tempo D&B) is **not known to be fixed**. The only two v6 D&B data points say a lazy prompt still falls back to two-step, and an engineered one works. The first test in §16 is our own D&B pair on v6 and Wild.

A new lever worth testing: build the drums as a **Studio per-track generation** ("174 BPM amen break, full tempo") rather than hoping the full mix gets them right.

---

## 12. Cover, Remix, Extend, Sample and audio upload on v6

| Claim | Tier | Source |
|---|---|---|
| **Cover and Extend still work on old-model (v5.5 and earlier) songs** | vendor (email quoted) | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| **Cover a v5 song on V6** for the most faithful upgrade: "pretty similar", fixes harsh tone, "rounder, wider". The best of several attempts. | tested (once) | [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8) |
| **Remix can change the model and Weirdness**: Remix → model dropdown (Pro to V6 - Wild) → Weirdness 76 → Create | tested (sponsored) | [Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY) |
| **Edit vocals versus Cover:** Edit vocals keeps the uploaded voice. Cover re-sings in a polished voice with the same rhythm and lyrics. Workflow for non-singers: record a guide, then Cover. | tested (sponsored) | [xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY) |
| **Edit instruments:** upload an idea → set the mode to **Edit instruments** → type the target instrument and a duration → Create | tested (sponsored) | [xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY) |
| Add a part under an a cappella upload ("add ambient pad chords") | tested (sponsored) | [xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY) |
| **A multi-song blend:** drag 2–3 audio files in, then one instruction naming which element comes from which track. It worked twice. | tested | [b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ) |
| **Timestamped sample-and-build:** an instruction naming the instrument, start and end seconds, and a genre. It worked. | tested | [b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ) |
| **Image or video to song:** lyrics reference the image, and a video's pacing drives the dynamics ("follow the editing"). **4 sources tested it.** One found image grounding weak ("it's not really making it for the image"). | tested | [b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ), [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo), [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU); contrast [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Everyday sound to song (snoring): you get a song *about* it. Whether the actual waveform is in the mix is unclear. | tested | [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU) |
| Uploaded audio passes an **originality/rights check** before use | tested | [M4Hj](https://www.youtube.com/watch?v=M4HjwzE7bjY), [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU) |
| Very short audio clips (~5 s) error out | tested | [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo) |
| Upload handling "doesn't follow lyrics from an already written song" and has static | reported (chat) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Suno's demo showed a guitar solo **transplanted** from one song into another with changed lyrics. Not tested live. | reported | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| Mashup itself launched on 2026-01-20 (PRE-v6). v6 adds the natural-language form. | source unknown (the v6 blog, where this was cited, does not contain the date) | — |
| Whether Cover offers Wild, or whether Extend or Remix lock to the original model: **unknown** | spec (gap) | — |
| Old Cover bug "sometimes returns the original" is **2024 (PRE-v6)**. Do not treat it as current. | — | [release notes](https://suno.com/release-notes) |

---

## 13. Length, structure, duration

- **Duration is Auto or Custom** on v6 ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode)) [tested / reported]. This matches our 2026-08-27 note, so it is not a v6 change. The Duration control dates from 2026-07-20 ([release note](https://suno.com/release-notes/duration-slider-on-web), PRE-v6).
- **With Auto, v6 runs longer than v5.5 in 5 of 7 genres.** Folk was 3:34 on v6 against 2:39 on v5.5. Pop was the exception, coming back shorter ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)) [tested]. The v5.5 takes were made before launch, so this is not a same-day controlled comparison. **For us:** always set Duration explicitly in the pair.
- **The maximum is 8 minutes for all three models:** "All three variants support up to 8 minutes per generation." ([help 13924801](https://help.suno.com/en/articles/13924801)) [vendor]. A secondary source agrees ([musicmake](https://musicmake.ai/blog/suno-ai-maximum-song-length-2026)).
- One v6-wild take came back at about 50 s unprompted ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)) [tested].
- A long brief's structure instructions (bridge, stripped-back ending) were followed ([AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo)) [tested]. Duet section tags were followed ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)) [tested].
- Studio bar-count requests are checked against the selection (§6) ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)) [tested].
- **No v6 information on:** ending-tag reliability (`[Fade Out]` versus `[Ending]`), Extend behaviour at boundaries, or the number of takes per Create [spec, gaps].

---

## 14. Known bugs, regressions, gotchas

| # | Issue | Tier | Source |
|---|---|---|---|
| 1 | **v5.5 and older cannot be selected.** Old sheets can't be re-run, and a fresh v6 run of an old prompt gives a different song. | vendor + tested | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8) |
| 2 | **Downloads of old v5-and-under songs may be purged or blocked within about 6 months.** A prediction only. The 2026-09-03 cap already covers old songs. **You decide (Kai):** whether to spend allowance archiving v5.5 masters now. | spec (prediction) | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| 3 | A stale "V5.5 powers…" string in the UI, and a Voices help page saying v5.5 only | tested / vendor-stale | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [help 11362433](https://help.suno.com/en/articles/11362433) |
| 4 | Rock drifts to a country or southern vocal, even with Max Mode | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| 5 | Metal: palm-muted "chugs" bleed into lyric sections. No fix; Studio is "your only option". | reported | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| 6 | Wild has a quality drop and artifacts, and one short take | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| 7 | Hollow, smeared sibilance | reported | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| 8 | A percussion element panned hard left and loud | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| 9 | **A multi-phrase lyric edit on an uploaded song corrupts the instrumental (3/3)** | tested | [b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ) |
| 10 | A plain-language edit applies only part of a compound instruction (the Voice was not applied) | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| 11 | A scoped-sounding edit restyles the whole song | tested | [y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU) |
| 12 | Variety had no visible effect in one test | reported | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| 13 | Variety may silently rewrite the style prompt (traced only to an AI-summarised search result) | spec (unsourced) | — |
| 14 | Audio clips of about 5 s or less error out | tested | [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo) |
| 15 | Studio exports are quieter, and one stem was time-shifted | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| 16 | Studio generations bleed onto the wrong track (less often than before) | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| 17 | The Studio loop marker is fiddly to resize | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| 18 | Remove Effects is ineffective on baked-in processing | tested | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| 19 | Metal and blues-rock artifacts persist on v6 | tested | [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) |
| 20 | Lyric repetition tic ("every") | tested | [BToY](https://www.youtube.com/watch?v=BToYusaGue4) |
| 21 | Sequential Replace Section edits add hiss (**PRE-v6** report) | reported | [JR-RS](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/replace-section-suno-editor) |
| 22 | Studio "needs" a reference according to one presenter, but works with the reference off | tested | [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA) |
| 23 | **Our own traps, carried forward [spec]:** an attachment left in the Simple box turns a Create into an edit; Variety, Personalize and Max Mode are likely to persist between loads like every other control | spec | §3 |
| 24 | An unrelated pre-v6 complaint about a recurring "Suno intro" and persona regression after May. Not v6. | reported (weak) | WebSearch snippet |

---

## 15. Contradictions between sources

1. **What the models are called in the app.**
   - "Version 6 Pro / Version 6 Wild Pro / Version 6 Mini" ([y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU), [M4Hj](https://www.youtube.com/watch?v=M4HjwzE7bjY)).
   - "V6 Pro / V6 Wild Pro / V6 Mini" ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8)).
   - "V6 Pro / V6 Wild / Mini" ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)).
   - "V6 / V6 Wild / V6 Mini" with a Pro badge ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo)).
   - "V6 - Wild" on screen ([Xx6E](https://www.youtube.com/watch?v=Xx6E9OJxefY)).
   - `v6 / v6-wild / v6-mini` (vendor text).
   - *Likely resolution:* the "Pro" is a badge read aloud [spec].
2. **Variety's shape.**
   - A stepped control with named positions ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8), [BToY](https://www.youtube.com/watch?v=BToYusaGue4)).
   - Versus a continuous "turn it up" slider. The raw notes list this disagreement as "Xx6E vs b5D1" without saying which source took which view, and Xx6E's own row says "turning it up gives more distinct/varied styles". **The attribution is uncertain.**
   - No source shows an "Off" state; the earlier attribution of Off to weraveyou was wrong (that article says only "defaults to Normal").
   - The low-end label reads "Exact style (?)" in one source and "Clips use the same style" in another. These may be a name and its description.
   - The step order (Exact style → Normal → Balanced → Distinct → Unreasonably varied) is assembled from garbled captions [spec]. "Unreasonably varied" has 1 clear live reading (BToY) and 1 garbled one (WtLn), and no written source.
3. **Whether Variety does anything.** It is designed to vary the two clips (label copy), but "didn't seem to work for me" ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)).
4. **Whether Variety exists at all, per Suno's docs.** The help page on creative sliders lists only Weirdness, Style Influence and Audio Influence ([help 6141377](https://help.suno.com/en/articles/6141377)). Four videos show Variety live. The docs lag the UI.
5. **Whether Audio Influence still exists.** Web sources don't list it ([weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode)). [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ) set it to 25 on v6 with a voice clone. **Resolved:** it exists, conditional on an attachment, which matches our DOM note.
6. **Personalize versus My Taste.** Probably one control, shown as Personalize ([WtLn](https://www.youtube.com/watch?v=WtLnIg5J1o8)) and referred to as My Taste ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ), [weraveyou](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode): "a Personalize toggle labelled My Taste") [reported]. Against it: WtLn's help text "Make variety match your taste" ties the toggle to Variety, and the My Taste help page describes an account-level switch (avatar → My Taste) without naming a create-form label ([help 11362561](https://help.suno.com/en/articles/11362561)). The live test (§16.4) still decides it.
7. **Voice on v6.** The help centre says v5.5 only ([help 11362433](https://help.suno.com/en/articles/11362433)); two tests used it on v6. The tests win on current behaviour, and the help page is likely stale.
8. **Word-level editing: the claim versus the mechanism.**
   - The vendor says "change one word".
   - Replace Section has a 10–30 s window per the 2024 note ([2024 note](https://about.suno.com/release-notes/replace-section)), which the current Song Editor doc does not restate, and "you can't edit single words" ([aimusicpreneur](https://www.aimusicpreneur.com/ai-tools-news/replace-sections-suno-ai-music-generator/), 2024).
   - The only **tested** single-word success is the Simple-mode attach route, which is not Replace Section ([AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo), [xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY)).
   - The possible reconciliation: "single word" means the *text* you change, while the audio regenerates at least a section or the whole song [spec].
9. **Lyric editing: success versus failure.** It succeeded with a same-syllable single word on a native track ([xpvX](https://www.youtube.com/watch?v=xpvXlnC9aeY), [AvZ2](https://www.youtube.com/watch?v=AvZ2j4tE8Yo)) and failed with multi-word, different-syllable phrases on an upload ([b5D1](https://www.youtube.com/watch?v=b5D11efZIRQ)). The conditions differ, but either video alone gives the opposite headline.
10. **Whether Replace Section is tied to v6.**
    - An undated help page says v6 powers Replace Section ("Remix & Edit— Extend, Cover, Replace Section, and more, all powered by v6", [help 13924801](https://help.suno.com/en/articles/13924801)). The v6 blog itself does not mention it.
    - The tool dates from 2024-10-10 ([note](https://about.suno.com/release-notes/replace-section)), with guides from 2024–2025 ([aidiy](https://www.aidiy.tech/post/how-to-actually-use-suno-s-new-replace-section-feature-instructions-plus-bonus-the-arrow-song), [JR v4](https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/suno-ai-in-song-editor-v4-replace-extend-crop-more)).
    - One agent traces it to the August 2025 Studio beta ([aicentral](https://substack.aicentral.blog/p/suno-studio-now-in-beta)).
    - Tom's Guide's "now you can replace a verse or chorus" is undated.
11. **The "2–3 words gave 30–40 seconds" report** ([JR-RS](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/replace-section-suno-editor) comments). Several agents read it as a *30–40 s regenerated block*; one read it as *30–40 s of generation time*. The same source is read two ways.
12. **"Single-word framing" versus "section".** The vendor uses both. The plain-language edit is framed as scoped, but the demonstrated global instruction changed the whole song ([y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU)).
13. **"No mode picking" (vendor copy) versus the model dropdown and the Simple/Advanced tabs** shown in the same video ([y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU)).
14. **Free-tier downloads.** "0 downloads" ([pricing](https://suno.com/pricing)) versus "7 lifetime trial" for pre-2026-09-03 joiners ([help 13614785](https://help.suno.com/en/articles/13614785)) versus "mini: no downloads or commercial rights" ([DMN](https://www.digitalmusicnews.com/2026/09/09/suno-v6-launch/)). These are reconcilable by join date; unresolved for mini on a paid plan.
15. **Studio exports and the download cap.** Unlimited or exempt (ToS via [AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ); a help summary; [qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)'s observation) versus a direct fetch of the help page that doesn't contain the line.
16. **Voice consistency.** A custom model is "more consistent than Voice", and yet "almost consistent but not 100%" ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)).
17. **Duet method.** Explicit tags were "not bad"; no tags was "maybe better" ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)).
18. **D&B.** Plain liquid DnB failed and engineered breakcore succeeded, in the same session ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)). Model and prompt effects are confounded.
19. **Wild's character.** It produces the "wildest thing I've ever heard" ([y2rI](https://www.youtube.com/watch?v=y2rIg_jkKpU)) and the best character in 3 genres ([AoLo](https://www.youtube.com/watch?v=AoLovH6ybrQ)), versus "didn't really seem to do anything" ([BToY](https://www.youtube.com/watch?v=BToYusaGue4)).
20. **The Create tab.** Removed, or moved under Library ([qFTg](https://www.youtube.com/watch?v=qFTghcRZeoA)); the presenter contradicted himself.
21. **The minimum editable region.** 10 s (the [2024 Replace Section note](https://about.suno.com/release-notes/replace-section): "must be 10-30 seconds long") versus about **2 s** in Studio's "Regenerate Section" ("This could be 2 seconds or 30 seconds", [HookGenius](https://hookgenius.app/learn/suno-studio-tutorial/), February 2026, PRE-v6). The current Song Editor doc states no limit ([help 6141505](https://help.suno.com/en/articles/6141505)). Neither figure is confirmed on v6.
22. **Codename.** A "Chirp-Hawk" codename for v6 appears in a [kie.ai](https://kie.ai/blog/what-is-suno-v6) title (403, unread). Official material says only v6.

---

## 16. Open questions: what we should test, in priority order

All live tests go through `suno.mts` with one Suno tab, and `status` first.

1. **🔑 Null-test the one-word edit.**
   - Take a finished v6 take and attach it in Simple with *"Change the word X to Y in the second verse only. Keep everything else exactly the same."*
   - Then phase-invert and subtract the original from the edit in ffmpeg, time-aligned.
   - Does anything outside the word survive the null? Is the voice the same at the seam?
   - Repeat with **the same text re-sung** (sub-problem B: *"Re-sing the word X at 1:23, same lyric, clearer pronunciation"*) and with a **one-occurrence** target. Borrow the Lyricist phrasing for that: *"Replace X with Y in the third line of the second verse, keeping the rhyme and line length unchanged."*
   - Log the credit cost.
   - This settles §5 more than any other test.
2. **The same null test on Replace Section and on Studio's "Regenerate Section":** lyrics unchanged. What is the smallest region each accepts on v6 now: 10 s (2024 note) or about 2 s (HookGenius, Studio)? Does "Regenerate Section" still exist in Studio? Do the words outside the target keep the take? Log the credit cost against the selection length.
3. **Screenshot the live create form's DOM.**
   - The tab labels: is it Simple / **Advanced** now, not Simple / Audio / Custom / Cover? Are Audio and Cover still tabs, or post-upload modes (Edit vocals / Edit instruments / Cover)? `formMode()` depends on this.
   - The exact model-button text and options.
   - Variety's element type, every step's label and its default.
   - Personalize and Max Mode (element and default).
   - Vocal Gender's options.
   - Duration's range.
   - The Simple attach menu.
   - Whether Variety hides when a custom model is selected.
   - Then update the DOM map in `automation.md` and `suno.mts`.
4. **Personalize versus My Taste.** Written evidence says one control ("a Personalize toggle labelled My Taste"); confirm it live. With a *distinctive* My Taste profile, run a pair with Personalize off and a pair with it on. Does the taste only bite when it is on? This decides whether the four-box atom keeps taste as a box.
5. **Our D&B on v6 against Wild** (grid R1, §4). Full tempo or two-step? Half-time drift? Reese bass? Use our real sheet plus a "drum-mechanics" rewrite.
6. **Does the Voice hold on v6?** Run the narrator Voice on v6 and on Wild with a dry spoken read. Check timbre in the quiet sections, **UK accent**, and sibilance.
7. **Variety** (R2): does it change the within-pair difference? Does it rewrite the style text (read the style shown on each returned take)?
8. **Max Mode** (R3): consistency against the credit delta.
9. **Per-generation credit cost** for v6, Wild and Max Mode, and for an edit compared with a Create. Read the balance before and after.
10. **Removing the backing in one bar via "Everything but lead vocal" plus a mute in Premiere.** Confirm the stems null against the mix (the §5 timing-offset warning). **Kai decides on the download spend.**
11. **Does a Studio multi-track export draw on the download allowance?** Watch the counter. **This is a human action.**
12. **Cover a v5.5 back-catalogue take on v6** (e.g. an accepted Camping take). Does it keep the performance well enough to count as "the same song, upgraded"? **And Remaster:** can Remaster target v6 on a v5.5 take, and does it keep the vocal performance as Suno's help text claims?
13. **Can Cover pick Wild?** Can Extend or Remix use v6 on a v5.5 song?
14. **Cadence in one bar.** Try a Studio guide vocal, or an instruction such as *"sing bar N with a triplet cadence"*. The expectation is failure; document it.
15. **Studio vocal track as dry narration:** typed lyrics plus a spoken-word style over silence. Is it clean enough for our dry-and-separate method?
16. **Lyricist and Inspo on v6:** do they still exist, and what changed?
17. **Watch** r/SunoAI, Discord and help.suno.com for a v6 controls article and a changelog. Re-run this sweep in about a week, when the community tests exist.

---

## 17. Source list

### YouTube (all published 2026-09-09, launch day; names and dates from the yt-dlp metadata)

| URL | Author / channel | Date | Contributed |
|---|---|---|---|
| https://www.youtube.com/watch?v=BToYusaGue4 | ChillPanic, "Suno V6 is HERE! (Pro Producer Live Test)" | 2026-09-09 | Tier names, Variety label copy ("Clips use the same style"… "unreasonably varied"), Max Mode as a real toggle, Vocal Gender, character limits, Exclude, drums/bass/reverb better, Wild quality drop, D&B fail and breakcore success, duet tags, southern-rock bug, custom model beats Voice, NL Voice-swap failure, Remove Effects, sibilance, panning, the 6-month purge prediction |
| https://www.youtube.com/watch?v=qFTghcRZeoA | Busy Works Beats, "Suno V6 inside Suno Studio 2.0 is INSANE!" (48 min) | 2026-09-09 | Studio + V6: per-track model, reference toggle, inferred instruments, BPM moved, take arrows, new-vocal-track prompt, loop marker, plugin generation, multi-track zip export, quiet and offset exports, possible download exemption |
| https://www.youtube.com/watch?v=y2rIg_jkKpU | AI Creatives Connect, "SUNO Version 6 MASTERCLASS: First Impressions" (40 min) | 2026-09-09 | "Version 6 Pro / Wild Pro / Mini" labels and descriptions, Simple multimodal, Voices rename, plain-English prompts, whole-song restyle edit, hummed melody on Pro vs Wild, the "no mode picking" copy |
| https://www.youtube.com/watch?v=M4HjwzE7bjY | AI Creatives Connect, "SUNO V6 Masterclass #2 (POP GENRE)" (6 min) | 2026-09-09 | Confirmed the label; audio-seeded melody and originality check |
| https://www.youtube.com/watch?v=AoLovH6ybrQ | Chris Wieduwilt (The AI Musicpreneur), "Suno v6 Just DROPPED. I Tested It Against v5.5" (22 min) | 2026-09-09 | 7-genre V6 vs V5.5 vs Wild voice-clone A/B, full settings (Weirdness 60, Style Influence 70, Audio Influence 25, Variety Normal), retirement email, 500 credits, plan gating, stale V5.5 string, duration lengths, stem quality, ToS and download caps, licensing |
| https://www.youtube.com/watch?v=AvZ2j4tE8Yo | AI Tune Craft, "Suno v6 Is Actually Insane..." (8 min) | 2026-09-09 | **summer→sunset word swap (tested)**, multimodal video+image, long brief adherence, dog-bark beat and short-clip error, Wild vs V6 on the same prompt |
| https://www.youtube.com/watch?v=WtLnIg5J1o8 | Lanewood Studios, "Suno V6 First Look: I Remade My Best V5 Track" (12 min) | 2026-09-09 | Variety (Exact style / Normal "Clips have slight style variation" / Unreasonably varied), Personalize "Make variety match your taste", old prompt ≠ upgrade, Cover as the upgrade path, Studio chat add-guitar |
| https://www.youtube.com/watch?v=Xx6E9OJxefY | Music Tech Info, "I Tried Suno v6 So You Don't Have To" (22 min, sponsored) | 2026-09-09 | "V6 - Wild" on screen, More options panel (Weirdness, Variety, Personalize), Weirdness values, Remix model switch, speed, quality verdict |
| https://www.youtube.com/watch?v=b5D11efZIRQ | MoneOnDaBeat, "Suno V6 is Here: 3 New Models You Need to Try" (11 min) | 2026-09-09 | Max Mode for consistency, multi-song blend, timestamp sample, **multi-phrase edit failed 3/3**, image and video to song |
| https://www.youtube.com/watch?v=xpvXlnC9aeY | Arcade, "New Suno V6 Is ACTUALLY Useful for Music Producers" (16 min, sponsored) | 2026-09-09 | **never→always word swap (tested)**, Edit vocals vs Cover, Get stems or MIDI labels, Edit instruments, Multi-track, loop BPM preserved |

### Vendor (Suno)

| URL | Date | Contributed |
|---|---|---|
| https://suno.com/blog/introducing-v6 | 2026-09-09 | Model family, positioning, the one-word/section edit claim, sampling, mashup, multimodal, retirement. Does **not** mention Replace Section; "Pro and Premier" appears only in model gating |
| https://suno.com/release-notes (also https://about.suno.com/release-notes/) | 2026-09-09 and 2026-09-02 entries | v6 bullets; the 2026-09-02 Studio update |
| https://suno.com/pricing | fetched 2026-09-10 | Plans, credits, downloads, model gating |
| https://help.suno.com/en/articles/13924801 | undated | Model variant descriptions (verbatim in §2), "All three variants support up to 8 minutes per generation", "Remix & Edit— Extend, Cover, Replace Section, and more, all powered by v6", custom models "Fine-tune v6 on your own tracks" |
| https://help.suno.com/en/articles/6141377 | undated, pre-v6 content | Creative sliders without Variety (a docs lag) |
| https://help.suno.com/en/articles/6141505 | undated | Song Editor labels confirmed on a direct fetch (Replace, Quick Replace, Edit Lyrics, Replace Lyrics, Replace Section, Edits Library, Generate More); "Select a clip or highlight a region"; no length limits; no mention of v6 |
| https://help.suno.com/en/articles/11362561 | undated | My Taste as an account-level switch (avatar → My Taste); no create-form label |
| https://help.suno.com/en/articles/2417409 | undated | Lyric-fix help: Reuse Prompt, Extend, Studio stems; "one audio file containing all music and words" |
| https://help.suno.com/en/articles/3271873 | undated | Replace Section |
| https://help.suno.com/en/articles/11362433 | undated | Voices FAQ says v5.5 only (likely stale) |
| https://help.suno.com/en/articles/13614785 | ~2026-09 | Upcoming-changes FAQ: downloads, models, ToS |
| https://help.suno.com/en/articles/13876865 | ~2026-09 | How downloads work |
| https://help.suno.com/en/categories/550017 | fetched 2026-09-10 | Weirdness Safe↔Chaos, 50% |
| https://suno.com/blog/suno-updates-tos | ~2026-09-03 | ToS change |
| https://about.suno.com/release-notes/replace-section (also https://suno.com/release-notes/replace-section) | 2024-10-10 (PRE-v6) | Replace Section "must be 10-30 seconds long", two versions, Select; Pro/Premier |
| https://suno.com/release-notes/duration-slider-on-web | 2026-07-20 (PRE-v6) | Duration control origin |
| https://suno.com/blog/stem-separation-updates | 2026-06-11 (PRE-v6) | Auto Split, Split from Mix, Advanced Split |
| https://suno.com/blog/songeditor | 2025-06-03 (PRE-v6) | Upgraded Song Editor, "creativity slider"; "Creative Sliders… three new controls" |

### Press and secondary

| URL | Author / outlet | Date | Contributed |
|---|---|---|---|
| https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode | We Rave You (Hemant Khatri) | 2026-09-09 | **The only written Advanced Mode control list** (Weirdness/Style Influence 50%, "Variety, which is new and defaults to Normal", Vocal Gender, Duration, Max Mode "positioned for consistency across longer songs, and for Covers and Voices", "a Personalize toggle labelled My Taste"), Create Custom Model 100 credits, Workspaces, CEO Shulman quote. **Does not contain:** a Variety "Off" state, the Variety prompt-rewrite claim, or any Max Mode credit cost |
| https://techcrunch.com/2026/09/09/suno-replaces-its-ai-models-with-a-new-one-trained-on-licensed-music-as-copyright-suits-pile-up/ | TechCrunch | 2026-09-09 | Training data a clean break, "edit a part of a song using a prompt or a word", artist remix programme, watermarks. Quotes only CPO Jack Brody; no "perfect single song" line |
| https://musically.com/2026/09/09/suno-launches-its-v6-ai-music-models-heres-what-you-need-to-know/ | Music Ally | 2026-09-09 | CPO Jack Brody: Wild "less tuned towards preferences"; Studio coexists; "natural language will never be better" for hand-precise edits; "You can just move the waveform" |
| https://www.digitalmusicnews.com/2026/09/09/suno-v6-launch/ | Digital Music News | 2026-09-09 | Mini: no downloads or rights; mixed reception |
| https://www.musicbusinessworldwide.com/suno-v6-ai-music-models-launch-in-partnership-with-wmg-bmg-and-believe/ | MBW | 2026-09-09 | Partners |
| https://www.unite.ai/suno-launches-v6-music-models-built-with-warner-music-bmg-and-believe/ | Unite.AI | ~2026-09-09 | The Wild→v6 refine workflow |
| https://www.siliconsnark.com/suno-v6-adds-precision-editing-siliconsnarks-token-disco-empire-demands-a-remaster/ | SiliconSnark | 2026-09-09 | "Announced capabilities, not results from a listening test" |
| https://www.tomsguide.com/ai/suno-just-got-a-major-upgrade-now-you-can-replace-a-verse-or-chorus | Tom's Guide | undated (snippet only) | Replace Section stripe-select |
| https://variety.com/2026/music/news/suno-new-label-backed-model-v6-1236855351/ | Variety | 2026-09-09 | Headline only |
| https://www.hollywoodreporter.com/music/music-industry-news/suno-launches-new-model-trained-on-licensed-songs-1236694047/ | THR | ~2026-09-09 | Licensing context |
| https://www.engadget.com/2251539/suno-trained-its-v6-ai-music-models-with-help-from-warner-and-bmg/ | Engadget | ~2026-09-09 | Licensing context |
| https://www.musicradar.com/music-tech/suno-has-rebuilt-its-ai-music-models-from-scratch-with-licensed-music | MusicRadar | ~2026-09-09 | Licensing (no vocal detail) |
| https://zinstrel.substack.com/p/suno-is-launching-v6-into-a-worsening | Zinstrel | ~2026-09 | Legal framing |
| https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/replace-section-suno-editor | Jack Righteous | 2025-04-08, updated 2026-08-23 (PRE-v6) | Replace Section practice: seams, hiss, 2–3 word → 30–40 s, pad the region |
| https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/why-does-changing-one-word-in-my-chorus-cause-glitches-in-suno (also …/why-does-changing-one-word-cause-glitches-in-suno) | Jack Righteous | V5-era (PRE-v6) | One-word glitches; regenerate the section |
| https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/suno-ai-in-song-editor-v4-replace-extend-crop-more | Jack Righteous | PRE-v6 (title only) | Replace Section pre-dates v6 |
| https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-next-music-industry-model-confirmed-so-far | Jack Righteous | ~2026-09 | Licensed training ≠ creator commercial clearance |
| https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-lyricist-explained-save-your-songwriting-voice-in-suno-ai | Jack Righteous | PRE-v6 | Lyricist |
| https://www.aimusicpreneur.com/ai-tools-news/replace-sections-suno-ai-music-generator/ | AI Musicpreneur | 2024-10-14 (PRE-v6) | "You can't edit single words" |
| https://www.aidiy.tech/post/how-to-actually-use-suno-s-new-replace-section-feature-instructions-plus-bonus-the-arrow-song | AIDIY | 2024-10-17 (PRE-v6) | 15–20 s recommended |
| https://substack.aicentral.blog/p/suno-studio-now-in-beta | AI Central | 2025-08-21 (PRE-v6) | Studio beta; vocal-stem Replace gap |
| https://hookgenius.app/learn/suno-studio-tutorial/ | HookGenius | 2026-02 (PRE-v6) | Studio "Regenerate Section": drag-select "2 seconds or 30 seconds"; credits proportional to length (§5 method 2b) |
| https://genxnotes.com/en/posts/fix-lyrics-mistake-in-suno/ | GenXNotes | undated (403) | Sample (Beta) workaround |
| https://suno.bi/en/blog/suno-lyrics-workflow | suno.bi | 2026-08-05 (PRE-v6) | Lyric Persona; one layer at a time |
| https://roo.beehiiv.com/p/suno-lyrics-editor-update-july-2026 | Roo | 2026-07 (PRE-v6) | Lyrics editor and Lyricist date |
| https://sunostyles.com/blog/understanding-suno-parameters | SunoStyles | undated (PRE-v6) | Weirdness / Style Influence recipes |
| https://aimusicapi.ai/en/blog/suno-ai-prompt-character-limits | AIMusicAPI | PRE-v6 | 1,000 / 5,000 caps for v4.5–v5.5 |
| https://musicmake.ai/blog/suno-ai-maximum-song-length-2026 | MusicMake | 2026 | "Up to 8 min" (secondary) |
| https://musicmake.ai/blog/suno-v5-audio-quality-khz-2026 | MusicMake | PRE-v6 | Export specs (unverified) |
| https://lumimusic.ai/blog/suno-pricing | Lumi | PRE-v6 | 10 credits for 2 songs baseline |
| https://undetectr.com/blog/suno-stems-daw-workflow | Undetectr | undated | Stem expectations; hybrid DAW workflow |
| https://glama.ai/mcp/servers/AceDataCloud/MCPSuno/tools/suno_replace_section | Glama / AceDataCloud | undated | Replace Section is Pro/Premier |
| https://github.com/paperfoot/suno-cli, https://suno-automation.com/, https://docs.ttapi.io/api/en/suno | third-party tooling | PRE-v6 | No v6 grids; no official API |
| https://neuralanalog.com/fix-suno-hiss, https://sunofix.app/how-to-remove-suno-artifacts/, https://www.mixmasterai.co/suno-audio-fixer | artifact-tool vendors | PRE-v6 | v5.5 artifact bands |
| https://hookgenius.app/learn/suno-content-filter-blocked-words/, https://roo.beehiiv.com/p/prompt-flagged-for-moderation-suno-why-clean-lyrics-get-blocked | — | PRE-v6 | Moderation (no v6 change found) |
| https://lyrictime.com/, https://suno.bi/en/blog/word-by-word-synced-lyric-video-sunomv-2026-guide | third-party | — | Word timing is external only |
| https://weraveyou.com/2026/04/review-suno-ai-music-generator-electronic-producers/ | We Rave You | 2026-04-29 (PRE-v6, v5.5) | Excluded as v6 evidence |
| https://musictech.com/reviews/digital-audio-workstations/suno-studio-review/ | MusicTech | 2026-01-13 (PRE-v6) | Excluded |
| https://note.com/hoboai/n/n76b6ef2cb9cd?hl=en, https://tinystudio.fm/guides/suno-next-model/, https://roo.beehiiv.com/p/suno-new-models-september-2026 | — | pre-launch | Speculation only, not cited for facts |
| https://kie.ai/blog/what-is-suno-v6 | kie.ai | — (403) | "Chirp-Hawk" codename title only |
| https://magiccreator.ai/posts/suno-v6-model-guide | MagicCreator | ~2026-09 | Consulted, no distinct claims |

**Unreachable:** reddit.com and old.reddit.com (r/SunoAI) returned nothing this session. There is no community-forum evidence in this report.

**Re-checked by a reviewer on 2026-09-10 (direct fetches):** the v6 blog, release notes, songeditor blog, the 2024 Replace Section note, help 13924801, 6141505, 11362433 (the "v5.5 only" Voices line is verbatim), 11362561 and 2417409, weraveyou, Music Ally, TechCrunch and HookGenius. Tom's Guide was truncated again and is still undated. Three web searches found no written source for any Variety step label.

## Reviewer notes rejected

None. All 22 corrections from the 2026-09-10 review were applied. Each is backed by a direct fetch of the cited primary source, and none conflicts with other evidence in this report.
