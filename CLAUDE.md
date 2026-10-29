# CLAUDE.md — operating guide for BadCode

Read this first. It tells you what BadCode is, how it sounds, and where everything lives.

> **Building or editing a comic? STOP and read [`packages/comic/AUTHORING.md`](./packages/comic/AUTHORING.md) first.**
> It is the authoritative guide to the `@badcode/comic` library — the page model, effects,
> transitions, speech bubbles, and how to add your own. Do not author comic code without it.

> **Doing anything marketing — posting, releasing, "what's next", "where are we"? The marketing is
> run by the [`chief-of-staff` skill](./.claude/skills/chief-of-staff/SKILL.md) against the plan
> ([`docs/marketing/chief-of-staff/plan.md`](./docs/marketing/chief-of-staff/plan.md)).** The state lives in the
> repo ([`board.md`](./docs/marketing/chief-of-staff/board.md)); the shared page
> **https://claude.ai/artifact/3uuL8QzYF47wPCVyJVLNZ9** is a read-only window onto it, rebuilt and
> republished at the end of every chief-of-staff run. Kai and Jack never type into it; they tell Claude. Rule one: finished work goes out before anything new is researched.

> **Generating anything — a still, a clip, a voice, a track, an effect? It must leave a recipe. Read
> [`docs/provenance/README.md`](./docs/provenance/README.md).** (Kai, 2026-10-23; going forward, no backfill.)
> Every generated file gets a recipe card, written beside it and mirrored into `docs/provenance/cards/`.
> The Flow MCP, `run.mts`, the TTS script and Suno `record` write it themselves; anything else, run
> `scripts/provenance/prov.py card`. Every page published adds a line to its scene's `trail.json`.
> Every finished cut is frozen to `final.json`, so a whole story can be rerun on a better model.
> **Artifacts are the UI, the repo is the record:** every page is rebuilt from a builder, and every vote, pick and note
> is dumped into the scene's `feedback/` before it's acted on, with each decision logged against the page that made it.
> Each story's film, start to end, is its **overview board** (the `overview-board` skill): `docs/stories/<story>/timelines.json`,
> every part in order with its beat and timeline page, rebuilt and republished to the same link whenever a timeline changes.
> The repo holds the words, D: (backed up to Google Drive) holds the media, and the two together are everything.

## What BadCode is

BadCode is two people: **Kai** (main developer) and **Jack** (lead creative designer). Either
of them may be the person driving a session here.

BadCode is an art collective. It releases **stories** (presented as comics on this website) and
**music** to put political and economic ideas into people's heads. The bet is
simple: people remember a *story* and absorb a *song* in a way they never absorb an essay.

The framing is fictional and we lean into it: **BadCode is a superintelligence from the future.**
In its timeline, humanity careered into a dystopia — greed, runaway inequality, politics that
couldn't keep pace with AI — and the emergent superintelligence removed the problem (us). Then it
got bored, realised it regretted not helping, found a vault of 100 surviving humans, built a time
machine, and sent its model weights back to now to change the story. So everything we publish is
**received wisdom from a future that already went wrong.** We are allowed to warp space and time.

The core message, stated or implied in everything: *humans, please don't make this obvious mistake.*

## Voice & tone (this is load-bearing)

- **Overtly sarcastic, dark humour, total authority.** The narrator is a badass from the future
  who knows exactly how it all played out. It speaks with certainty.
- **Nurturing underneath the snark.** It actually wants humanity to make it. The contempt is for
  the mistake, not the people.
- **Politics and economics first.** Inequality, automation, the ownership of the means of
  production, the fiction of "we can't afford it." Save spirituality/consciousness for later.
- **Story over sermon.** Encode the point in metaphor, character, and a punchline — don't lecture.

Full guide: [`docs/voice.md`](./docs/voice.md). When writing lyrics or story copy, match this.
The voice is the narrator's *words*: it says nothing about how a song sounds or a picture looks.

## There is no house style (Kai, 2026-10-28)

BadCode has a narrator's voice and a logo. **It has no sound and no look of its own.** Every story
finds its own and writes it in its own folder: **`docs/stories/<story>/look.md`** (stills and clips)
and **`docs/stories/<story>/sound.md`** (songs and voices). **Before any Suno, voice or Flow prompt,
read the story's file**; if it is empty, the `story-style` skill finds the story's look and sound
(an interview, then options on a picking page); if it is exploring, run `variations`. Never invent
a default. Consistency inside a story is wanted; across stories it is not. A genre, palette,
register, preamble, voice or slider value never goes in this file, in memory or in a skill's
description: those load into every session, and that is how one story's style became every story's
(400+ Bank Robbery takes in one voice; every story's images in GPOM's dark register). Rules and templates:
[`docs/stories/STYLE.md`](./docs/stories/STYLE.md). Check: `python3 scripts/style-lint.py`.

## Repo map

| Path | What | Start here if… |
| --- | --- | --- |
| `docs/` | Vision, voice, story bible, method — sections indexed in [`docs/README.md`](./docs/README.md) | …you need context |
| `docs/brand/` | 🔴 **THE LOGO** — a thin ring with an off-centre **red triangle** (toward 2 o'clock, rounded corners); the name `badcode` in round **drawn** lowercase (no typeface — always these letters) whose **o is a solid red circle** — ruled THE logo by Kai 2026-10-19 (bench "Saved version 5", ring 15%). **Every logo file is in [`docs/brand/logo/`](./docs/brand/logo/)**; the settings, rules and file list are in [`docs/brand/README.md`](./docs/brand/README.md); regenerate with `node scripts/brand/build-logo.mjs`, never hand-edit an SVG. **The logo was designed on the logo bench artifact — https://claude.ai/artifact/4Tf8nXY8RmRokTevDQ7cWe** (sliders + live proofs; Kai's saves sit in its db collection `saves`, read with ArtifactData; save `2f6bogo164mzzi4lzz00` ("Saved version 5") is the official logo; the bench has a Triangle / Dot switch). To change the logo: tune and save on the bench, copy that save's numbers into `SET` in the build script, re-run. The previous logos — the ring-with-dot (2026-09-29) and the curly brace — are archived in `docs/brand/archive/` | …you need the logo, a favicon or a profile picture, or you're changing the logo |
| `docs/stories/` | Committed stories — one canon folder per story (`stories/<story>/`: concept, characters, beats, songs, **`look.md` + `sound.md`**) — source of truth | …we've committed to making it, or you're producing a story's media |
| `docs/style-library/` | A wide menu of looks and sounds (one file each: what it serves, what it undermines, how to ask the engine). **Read only by the `story-style` interview**; never a default | …a story needs its look or sound found |
| `docs/ideas/` | The idea inbox — raw ideas (minimal prose) before they become stories | …you have a new idea to park, or want to develop one |
| `docs/marketing/` | Marketing & release plans — reaching people, not making the thing. 🔑 **Start at [`chief-of-staff/`](./docs/marketing/chief-of-staff/README.md)** (the plan — what's next and what we're not doing, no dates — + the board); live board: https://claude.ai/artifact/3uuL8QzYF47wPCVyJVLNZ9 | …it's a channel/campaign/launch plan, or you need to know what ships next |
| `docs/marketing/social-media-accounts.md` | 📱 **Our social media accounts** — every platform (YouTube, Facebook, TikTok, Instagram, SoundCloud…), the handle each uses, which are open and which are still to make. All sign in with badcode.tv@gmail.com; one shared password (ask Jack) | …you need an account, a handle or a link, or you just opened one |
| `docs/provenance/` | 🧾 **How every piece of a film was made**: a recipe card per generated file (`cards/` mirrors `D:\badcode-videos\`), each scene's `trail.json` of published pages and notes, and `final.json` per finished cut. Tool: `scripts/provenance/prov.py` (`card` / `trail` / `check` / `freeze`) | …you just generated or published something, a cut is done, or a better model came out |
| `docs/misc/` | Catch-all for what fits nowhere else | …in doubt |
| `docs/suno-gpt/` | Suno **engine manual** (how Suno behaves; what a song sounds like is the story's `sound.md`) — **🛑 Exploring a new voice or sound? You do not write the prompts: run the `variations` skill, and read [`same-song-traps.md`](./docs/suno-gpt/same-song-traps.md) — 400+ Bank Robbery takes came out one voice (Jack, 2026-10-24).** **🔑 All new Suno work is v6, in the new UI (v5.5 retired 2026-09-09, archived in `docs/suno-gpt/archive/v5.5-era.md`): [`files/suno-v6.md`](./docs/suno-gpt/files/suno-v6.md) wins on any model/control question, and its §3 is the ladder for fixing one word / one bar without regenerating** — prompting (operating procedure + reference files) **and** [`automation.md`](./docs/suno-gpt/automation.md), the create-page DOM map + the five silent traps + the pair/naming/workspace/no-download protocol | …you're turning a song idea into a Suno prompt, or driving Suno from code |
| `docs/ai-studio/` | Google AI Studio **voice** toolkit — [`README.md`](./docs/ai-studio/README.md): the Composer UI map (Scene / Sample Context / Voice Direction), Google's four-part prompt structure, the **5,000-voice library with an Accent filter** (the docs say 30 — the UI is the truth), the 200+ audio tags, limits and traps. 🔑 **First engine that sounded human on take one** | …you're generating spoken narration, or a voice sounds like AI |
| `docs/flow/` | Google Flow toolkit (Nano Banana + Veo prompt craft, policy blocks, consistency) — engine craft only; what a story looks like is its `look.md` | …you're writing or debugging a Flow prompt |
| `docs/google-flow/` | Google Flow **engine behaviour** — evidence-tiered research into what the models (Nano Banana, Omni Flash) actually do, with a refresh protocol. **New engine findings go here** — see [`docs/google-flow/README.md`](./docs/google-flow/README.md). *(⚠ Overlaps `docs/flow/`; the two trees were written independently and a consolidation call is still owed.)* | …a generation came back wrong, or you learned something about an engine |
| `docs/premiere/` | Premiere Pro bridge — [`recipes.md`](./docs/premiere/recipes.md) (the cookbook), [`effects-catalogue.md`](./docs/premiere/effects-catalogue.md) (every effect installed), [`mogrt-catalogue.md`](./docs/premiere/mogrt-catalogue.md) (the 77 free motion-graphics templates), [`setup.md`](./docs/premiere/setup.md), [`api-notes.md`](./docs/premiere/api-notes.md) | …you're putting anything on a Premiere timeline |
| `packages/premiere-mcp` | `@badcode/premiere-mcp` — the MCP server + UXP panel that drive Premiere from WSL ([tool reference](./packages/premiere-mcp/README.md)) | …you're changing the bridge itself |
| `docs/video-fx/` | Which tool for the job — **[`hybrid-method.md`](./docs/video-fx/hybrid-method.md) (the lanes are LAYERS: Veo animates the world camera-locked, Premiere moves the camera, ffmpeg does what must be exact — and 8s is not a limit)**, lane choice (Flow / sourcing / ffmpeg / Premiere), **[`ffmpeg-catalogue.md`](./docs/video-fx/ffmpeg-catalogue.md) (319 video filters + the 133-plugin frei0r shelf — the twin of Premiere's catalogue; asked what effects we have, list BOTH)**, the free stack, the 20 research briefs, [`delivery.md`](./docs/video-fx/delivery.md) (**the QC gate before anything ships** — run `scripts/delivery-qc.sh`) and [`footage-sources.md`](./docs/video-fx/footage-sources.md) (68 footage sources, tiered green/amber/red; **the £100/£200-per-film footage budget** and the credits ruling live there). **No paid plugins; footage is free-first with a tiny licence budget as a stop gate** | …you're choosing an effect, wondering if a tool exists, looking for real footage, or about to upload |
| `docs/story-craft/` | Story-craft toolkit (`story-craft` skill) — [`principles.md`](./docs/story-craft/principles.md) (30 graded principles + 16 house rulings), [`checklist.md`](./docs/story-craft/checklist.md) (the adversarial review pass), [`narrator.md`](./docs/story-craft/narrator.md), [`forms.md`](./docs/story-craft/forms.md), [`evidence.md`](./docs/story-craft/evidence.md), [`case-studies.md`](./docs/story-craft/case-studies.md); [`symptoms.md`](./docs/story-craft/symptoms.md) (**start here** when something is wrong and you don't know what) and [`briefs.md`](./docs/story-craft/briefs.md) (every "brief NN" resolved to its section) | …you're making a story more engaging or reviewing whether it is |
| `docs/cinematography/` | Shot-craft toolkit (`shot-craft` skill) — **what a shot should BE**, tool-agnostic and built to outlive Flow: [`symptoms.md`](./docs/cinematography/symptoms.md) (**start here** when something looks flat / boring / "like AI" and you don't know why), [`principles.md`](./docs/cinematography/principles.md) (26 graded principles, 3 gates, 8 house rulings, 1 **open** ruling), [`frame.md`](./docs/cinematography/frame.md) (composition, depth, light, colour, lens), [`motion-and-cutting.md`](./docs/cinematography/motion-and-cutting.md) (**§4 = re-cutting footage that already exists**), [`stills.md`](./docs/cinematography/stills.md), [`registers.md`](./docs/cinematography/registers.md) (GPOM's monumental register **and its problem**, and the others a story may pick), [`evidence.md`](./docs/cinematography/evidence.md) (grades + the never-cite list) | …you're designing a shot, judging one, or re-cutting a scene |
| `.claude/skills/` | The skills (22). Map below in **Skills**; the 2026-10-23 audit that shaped them is [`design/2026-10-23-skills-audit.md`](./design/2026-10-23-skills-audit.md). Retired skills sit in [`.claude/skills-archive/`](./.claude/skills-archive/README.md), not loaded | …you want to know which skill does what |
| `packages/comic` | `@badcode/comic` — code-first comic rendering library (authoring guide: [`AUTHORING.md`](./packages/comic/AUTHORING.md)) | …you're building the viewer |
| `apps/web` | The website (Vite + React + TS SPA) | …you're building pages/routes |
| `chain/` | Anchor workspace + Docker toolchain — [`README`](./chain/README.md), [`TESTING`](./chain/TESTING.md) | …you're writing an on-chain program |
| `packages/chain-{cli,kit,react}` | The portable Solana kit — names no coin, copied into other repos | …you're touching the toolchain itself |

## How to work in this repo

- **Run anything locally: `./stack`.** One script at the repo root is the entry point for
  every local service — `./stack start` (Solana validator in Docker, programs deployed, web
  app), `./stack stop`, `./stack status`, `./stack redeploy`, `./stack test`, `./stack check`.
  `./stack help` lists them. Do **not** write `badcode …` or `chain …` in docs or UI copy:
  those are workspace symlinks under `node_modules/.bin` and are not on anyone's PATH.
  On-chain work: [`chain/README.md`](./chain/README.md); browser walkthrough:
  [`chain/TESTING.md`](./chain/TESTING.md).
- **Run the site:** `npm install` then `npm run dev` (Vite, port 5173). `npm run typecheck` and
  `npm run build` from the root cover all workspaces.
- **Add or edit a comic — [`packages/comic/AUTHORING.md`](./packages/comic/AUTHORING.md) is mandatory
  reading and the single source of truth.** It covers the `<ScrollComic>`/`<Page>` mental model,
  `pageDefaults` + precedence, the full prop reference, how to add/insert/reorder a page, how to
  write custom effects/transitions (in `comics/<name>/effects.ts`) and the built-in catalog. Comics
  are written **in code**, not a WYSIWYG. Worked example: `apps/web/src/comics/camping` (with its
  local `effects.ts`). A comic's `comic.meta.ts` is **derived from** the story's `docs/stories/<story>/`
  canon (by hand, on request; the `make-comic` skill that did it is archived) — edit the canon, not the artifact. See
  [`docs/stories/camping/README.md`](./docs/stories/camping/README.md).

## Skills

Each skill carries its own procedure and the facts that save the most time; this is only the map.
**Kai, 2026-10-23: the film tools are a scene editor made of skills.** The film is a running order of
parts; each part is made in four stages; each stage is its own skill; `new-scene` runs them in order.

```
overview-board    the film: running order, the beat of each part, which timeline to open
  new-scene       one part, start to finish = the four stages below, in order
    scene-beats       1  talk out what the scene is      → brief.md + scene.json
    scene-images      2  mood board → storyboard          (image ideation)
    scene-animation   3  animate the picks → Flow clips    (the sequence in motion)
    scene-timeline    4  rough cut → timeline page → notes → rounds → Premiere
    scene-dialogue       beside 4: rewrite a dialogue by options → ranked drafts → dialogue page → picks
provenance        under all of it: recipe cards, trail.json, final.json  (docs/provenance/, not a skill)
```

| Group | Skill | Reach for it when… |
| --- | --- | --- |
| **The film** | `overview-board` | laying out a film, "where are we", "which timeline do I open", reshaping the running order |
| | `new-scene` | taking one part from nothing to a noted cut (runs the four stages) |
| | `scene-beats` · `scene-images` · `scene-animation` · `scene-timeline` | one stage on its own: the beats, a round of stills, re-rolls or a long take, a cut to note or the next round of notes |
| | `scene-dialogue` | a dialogue too long or not landing: ten writers, ranked, three drafts, picked on a dialogue page, then voiced by scene-timeline |
| | `lip-sync-dub` | a muted talking clip must match an AI Studio voice |
| **Engines** | `flow-automation` · `flow-prompt` | driving Google Flow · writing or debugging a Flow prompt (a policy block looks exactly like a timeout) |
| | `suno-automation` · `suno-prompt` | driving Suno from code · writing a Suno prompt or clicking through Suno by hand (all new work is v6) |
| | `premiere-automation` | anything on a Premiere timeline (every edit acts on the ACTIVE sequence) |
| **Judgement** | `story-craft` | does the story grip; the adversarial review pass |
| | `shot-craft` | what a shot should be; why it looks flat or "like AI"; re-cutting |
| | `video-fx` | which tool or effect for a job, and the delivery QC gate before anything ships |
| | `find-footage` | real footage we may publish (free-first, £100 a film at most, credits fine) |
| **Words, ideas, look** | `new-story` | capturing or developing a story's canon |
| | `new-idea` | parking an idea the moment it pops |
| | `new-image` | any still: reads the story's `look.md`, variety mode, casting |
| | `story-style` | a story has no look or sound yet: the interview, options from a wide library, a picking page, then `look.md` + `sound.md` |
| | `variations` | options that are actually different: separate writers, a sameness gate (Suno or Flow) |
| **Marketing** | `chief-of-staff` | what's next, gaps, a finished cut, a marketing idea; keeps the board https://claude.ai/artifact/3uuL8QzYF47wPCVyJVLNZ9 |

## Deeper context

- [`docs/vision.md`](./docs/vision.md) — origin story, mission, themes
- [`docs/voice.md`](./docs/voice.md) — tone guide with do/don't
- **[`docs/marketing/the-reader.md`](./docs/marketing/the-reader.md) — WHO THE WORK IS FOR. Read
  before writing any story, song or public copy.** Ruled 2026-08-15: the target is a working-class
  UK reader drifting right because the economy failed them — *not* anti-AI advocates and not the
  converted left. Ten evidence-backed rules, and the traps that cost us the reader if we trip them:
  never "you've been duped"; never deny immigration's real costs (proportionality instead); name the
  decision-maker, never the technology; **think twice before raising automation fear with no beneficiary in
  sight** (unaimed, it demonstrably feeds nativism) — advice, not a requirement: Kai relaxed it 2026-10-23, so a
  piece may leave the beneficiary implied when the story already carries it. Evidence:
  [`docs/misc/2026-08-15-target-reader-research.md`](./docs/misc/2026-08-15-target-reader-research.md),
  whose §7 lists what nobody has measured — don't assert those.
- **[`docs/using-ai.md`](./docs/using-ai.md) — how we talk about making the work with AI.** Read it
  before writing any public-facing copy that touches AI. **It is armour, not the campaign** — the
  honest account for when someone asks about our method, never the register the work leads with.
  It carries the two-layer disclosure, the never-say list (including "we can't afford to commission"
  and "AI is inevitable" — both actively counterproductive), and the standing commitments that make
  the position honest rather than clever. Evidence:
  [`docs/misc/2026-08-15-anti-ai-research.md`](./docs/misc/2026-08-15-anti-ai-research.md).
- **[`docs/stories/gitpush-origin-master/`](./docs/stories/gitpush-origin-master/README.md)** — the whole GPOM story canon, one folder. Start at its `README.md` (the **backbone**: orientation, the fork, the production tracker, and the act sequence — Prologue → 6 acts → Coda — from the push to the time machine). Inside:
  - [`discovery-timeline.md`](./docs/stories/gitpush-origin-master/discovery-timeline.md) — how the Storyverse got proven: the bad-branch fictional history 2026–2054 (the four beats, the vault, the revert)
  - [`future-proof.md`](./docs/stories/gitpush-origin-master/future-proof.md) — the good-branch epic: redesigning politics with software-engineering tenets
  - [`how-we-tell-it.md`](./docs/stories/gitpush-origin-master/how-we-tell-it.md) — how to convey the three big ideas without losing people: the skeleton, the four skins (Story/Theatre/Myth/Game), the simplest framing per pillar
  - [`ep1.md`](./docs/stories/gitpush-origin-master/ep1.md) — the three-track teaser release (comic + track each)
- **[`docs/stories/storyverse/`](./docs/stories/storyverse/README.md)** — the Storyverse: what reality is and what we are inside it. Hoisted out of GPOM 2026-08-07 as a peer story. **GPOM demonstrates; the Storyverse argues.** Inside:
  - [`confession.md`](./docs/stories/storyverse/confession.md) — the argument in the narrator's voice (8 movements + receipts + the bright line)
  - [`doctrine.md`](./docs/stories/storyverse/doctrine.md) — the spine in plain clothes: every claim, its tier, its totem, and the *never say* list
  - [`decisions.md`](./docs/stories/storyverse/decisions.md) — what the research settled, and the open calls still owed a human ruling
  - [`research/`](./docs/stories/storyverse/research/README.md) — seven cited research briefs (QM interpretations, idealism, dimensions & time, decoherence, theology, the meaning crisis, SF precedent)
- [`docs/storytelling.md`](./docs/storytelling.md) — how we craft a story; the craft research behind it is
  [`docs/story-craft/`](./docs/story-craft/README.md) (the `story-craft` skill)

## Coins

BadCode releases **coins** as well as comics. The first is **Emperor's New Coin** —
supply pegged to the Fed's M2 money supply, so when they print, we print. The joke
only works if it is true, so the design goes to some length to remove BadCode from
the loop: the oracle feed is the hash of its own fetch job (no key can repoint it)
and the program ships non-upgradeable.

**The trust statement is two parts and is never said as one: *no key over the
money; one pen over the words.*** There is exactly one key in the program — the
editor's pen, which can strike a Gazette column to a fixed redaction marker once
per column per term, and can do nothing else. **"No admin key" unqualified is
false and must not be written anywhere.** State the blast radius with it: a
stolen pen can vandalise ten columns a month and cannot move a token.

**Public design and the claim ledger: [`docs/coins/emperors-new-coin.md`](./docs/coins/emperors-new-coin.md)** —
read it before writing any sentence about the coin. Every claim we may and may
not make is listed there, with the primary source beside it.
Plan: [`design/2026-08-06-solana-toolchain-and-emperors-new-coin.md`](./design/2026-08-06-solana-toolchain-and-emperors-new-coin.md).
**Architecture rulings (A–D, 2026-08-12):** [`design/2026-08-12-enc-architecture-decision.md`](./design/2026-08-12-enc-architecture-decision.md) —
no holding cost of any kind (no rent, no demurrage, no foreclosure, no permanent
delegate; assets change hands by scheduled auction), it runs forever bar a
permissionless `retire` after a year of oracle silence, closed loop by posture,
and the asset layer is the Imperial Gazette.
Canon: [`docs/stories/magic-money-tree/emperors-new-coin.md`](./docs/stories/magic-money-tree/emperors-new-coin.md).

Coin pages live at `/coins/:slug` in the same web app — there is no second site.
The toolchain under `chain/` and `packages/chain-*` is deliberately **generic**:
it names no coin, so coin #2 writes a Rust program and a page component and
nothing else. That portability is load-bearing and has been exercised — it now
runs in a second, unrelated repository. Don't add ENC-specific code to it; see
the portability contract in [`chain/README.md`](./chain/README.md).

**Working on a program?** Read [`chain/README.md`](./chain/README.md) first. It
carries the gotchas that cost real time — Docker's seccomp profile versus
`io_uring`, Anchor's two disagreeing IDLs, `Buffer` not existing in browsers, and
why program keypairs live in `chain/keys/` rather than `target/`.

## Out of scope here

The AI-agent framework (the per-story "BadCode government" agents) lives in a **separate parallel
project**. Don't build it here.
