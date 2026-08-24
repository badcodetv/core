# CLAUDE.md — operating guide for BadCode

Read this first. It tells you what BadCode is, how it sounds, and where everything lives.

> **Building or editing a comic? STOP and read [`packages/comic/AUTHORING.md`](./packages/comic/AUTHORING.md) first.**
> It is the authoritative guide to the `@badcode/comic` library — the page model, effects,
> transitions, speech bubbles, and how to add your own. Do not author comic code without it.

## What BadCode is

BadCode is two people: **Kai** (main developer) and **Jack** (lead creative designer). Either
of them may be the person driving a session here.

BadCode is an art collective. It releases **stories** (presented as comics on this website) and
**music** (drum & bass) to put political and economic ideas into people's heads. The bet is
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

## Repo map

| Path | What | Start here if… |
| --- | --- | --- |
| `docs/` | Vision, voice, story bible, method — sections indexed in [`docs/README.md`](./docs/README.md) | …you need context |
| `docs/stories/` | Committed stories — one canon folder per story (`stories/<story>/`: concept, characters, beats, songs) — source of truth | …we've committed to making it, or you're producing a story's media |
| `docs/ideas/` | The idea inbox — raw ideas (minimal prose) before they become stories | …you have a new idea to park, or want to develop one |
| `docs/marketing/` | Marketing & release plans — reaching people, not making the thing | …it's a channel/campaign/launch plan |
| `docs/misc/` | Catch-all for what fits nowhere else | …in doubt |
| `docs/suno-gpt/` | Suno toolkit — prompting (operating procedure + reference files) **and** [`automation.md`](./docs/suno-gpt/automation.md), the create-page DOM map + the five silent traps + the pair/naming/workspace/no-download protocol | …you're turning a song idea into a Suno prompt, or driving Suno from code |
| `docs/flow/` | Google Flow toolkit (Nano Banana + Veo prompt craft, policy blocks, consistency) | …you're writing or debugging a Flow prompt |
| `docs/premiere/` | Premiere Pro bridge — [`recipes.md`](./docs/premiere/recipes.md) (the cookbook), [`effects-catalogue.md`](./docs/premiere/effects-catalogue.md) (every effect installed), [`mogrt-catalogue.md`](./docs/premiere/mogrt-catalogue.md) (the 77 free motion-graphics templates), [`setup.md`](./docs/premiere/setup.md), [`api-notes.md`](./docs/premiere/api-notes.md) | …you're putting anything on a Premiere timeline |
| `packages/premiere-mcp` | `@badcode/premiere-mcp` — the MCP server + UXP panel that drive Premiere from WSL ([tool reference](./packages/premiere-mcp/README.md)) | …you're changing the bridge itself |
| `docs/video-fx/` | Which tool for the job — lane choice (Flow / sourcing / ffmpeg / Premiere), the free stack, the 20 research briefs, [`delivery.md`](./docs/video-fx/delivery.md) (**the QC gate before anything ships** — run `scripts/delivery-qc.sh`) and [`footage-sources.md`](./docs/video-fx/footage-sources.md) (68 footage sources, tiered green/amber/red). **No paid plugins, no paid footage** | …you're choosing an effect, wondering if a tool exists, looking for real footage, or about to upload |
| `docs/story-craft/` | Story-craft toolkit (`story-craft` skill) — [`principles.md`](./docs/story-craft/principles.md) (30 graded principles + 16 house rulings), [`checklist.md`](./docs/story-craft/checklist.md) (the adversarial review pass), [`narrator.md`](./docs/story-craft/narrator.md), [`forms.md`](./docs/story-craft/forms.md), [`evidence.md`](./docs/story-craft/evidence.md), [`case-studies.md`](./docs/story-craft/case-studies.md); [`symptoms.md`](./docs/story-craft/symptoms.md) (**start here** when something is wrong and you don't know what) and [`briefs.md`](./docs/story-craft/briefs.md) (every "brief NN" resolved to its section) | …you're making a story more engaging or reviewing whether it is |
| `.claude/skills/` | `new-idea`, `new-marketing-idea`, `new-story`, `suno-prompt`, `suno-automation`, `make-comic`, `edit-panel`, `animate-slide`, `music-video-short`, `new-image`, `badcode-art-direction`, `flow-prompt`, `flow-automation`, `video-fx`, `premiere-automation`, `find-footage`, `story-craft` — orchestrators for parking an idea, capturing a marketing/distribution play, story capture, Suno prompting, driving Suno from code, the full idea→comic pipeline, editing an existing panel image, animating a finished panel, the full idea→short-form music-video pipeline (Suno track + Flow clips + edit plan), standalone brand imagery, the BadCode comic register, Google Flow prompt craft, driving the Flow browser, choosing which tool and which effect (plus the delivery gate), driving Adobe Premiere Pro, sourcing real footage we are allowed to publish, and making a story grip (the research-backed craft + the adversarial review pass) | …you're capturing an idea or marketing play, developing a story, making a track, automating Suno, building a comic, editing a panel, animating a slide, making a short, making a brand image, writing a Flow prompt, deciding how to achieve an effect or whether a file is ready to upload, cutting video in Premiere, looking for archive/stock footage, or asking whether a story engages |
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
- **Three skills do the creative heavy lifting** (`.claude/skills/`): **`new-story`** captures and
  develops a story under `docs/stories/<story>/`; **`suno-prompt`** turns a song idea into a Suno prompt;
  **`make-comic`** runs the full idea→rendered-comic pipeline (composing the other pieces).
  The bullets below say when to reach for each — the skills carry the detailed procedure.
- **Add or edit a comic — [`packages/comic/AUTHORING.md`](./packages/comic/AUTHORING.md) is mandatory
  reading and the single source of truth.** It covers the `<ScrollComic>`/`<Page>` mental model,
  `pageDefaults` + precedence, the full prop reference, how to add/insert/reorder a page, how to
  write custom effects/transitions (in `comics/<name>/effects.ts`) and the built-in catalog. Comics
  are written **in code**, not a WYSIWYG. Worked example: `apps/web/src/comics/camping` (with its
  local `effects.ts`). A comic's `comic.meta.ts` is **derived from** the story's `docs/stories/<story>/`
  canon (skill-driven, on request) — edit the canon, not the artifact. See
  [`docs/stories/camping/README.md`](./docs/stories/camping/README.md).
- **Make a Suno prompt:** type a song idea (a feeling, a reference, a GPOM beat) and the
  **`suno-prompt`** skill (`.claude/skills/suno-prompt/`) runs a short **interview** — mode, purpose,
  the vocal arc, what must survive — then produces a style prompt, exclude-styles list, slider
  settings, and on request lyrics, in the BadCode voice, refining against what you actually hear. It
  runs on the toolkit in [`docs/suno-gpt/`](./docs/suno-gpt/README.md) and defaults to drum & bass.
  **The skill also drives the app, not just the prompt box** — ask it "how do I…" or "what do I
  click" and it gives a click-path with every setting stated. The toolkit covers the three influence
  sliders, the Voice/custom-model stack for a recurring narrator across a release, lyric editing,
  stems, **Suno Studio 2.0** (project-aware chat, MIDI, effects rack, natural-language custom
  plugins — [`files/suno-studio.md`](./docs/suno-gpt/files/suno-studio.md)), and the things Suno
  reliably gets wrong (half-time drums, niche D&B subgenres).
- **Drive Suno from code (stop pasting four boxes):** run the **`suno-automation`** skill
  (`.claude/skills/suno-automation/`). The **mechanics half** of Suno, where `suno-prompt` is the
  craft — the same split as `flow-automation` / `flow-prompt`. It loads a sheet's Style, excludes,
  lyrics, sliders, Voice, title and workspace into `suno.com/create` in **one command** over CDP
  (the same Chrome Flow uses), clicks Create, and runs **the pair**. Tool:
  [`scripts/suno/suno.mts`](./scripts/suno/suno.mts); knowledge base:
  [`docs/suno-gpt/automation.md`](./docs/suno-gpt/automation.md) — the DOM map, the five silent
  traps and the verified/unverified table. **Three facts save the most time:** attaching a Voice
  offers to **overwrite your Style box** with the persona's own styles and the box looks populated
  afterwards, so the answer is *always* **Keep Current**; the lyrics editor is **Lexical**, so a
  programmatic fill collapses every line into one paragraph — **verify by counting paragraphs, never
  characters**; and **navigating away wipes the whole form**, with no draft recovery. **We never
  automate downloading** — Suno is capping downloads per month, so that allowance is only ever
  spent by a human. Every attempt runs as a **pair at weirdness 30 and 60**, because which one wins
  is still an open question.

- **Write or debug a Flow prompt:** run the **`flow-prompt`** skill
  (`.claude/skills/flow-prompt/`). The Suno toolkit's counterpart for images and video —
  it owns **platform craft** (how Nano Banana and Veo actually behave) while the
  BadCode *look* stays with `badcode-art-direction` (panels) and `new-image` (brand
  imagery). Reach for it when a prompt needs writing, when a generation fails, or when a
  character has to stay the same across many shots. Its knowledge base is
  [`docs/flow/`](./docs/flow/README.md): image and video prompt craft, camera
  vocabulary with reliability tiers, consistency/reference discipline, platform controls
  and credits, and the policy-block triggers and rewrites. **A policy block looks exactly
  like a timeout** — that one fact is the biggest time-saver in the whole toolkit.

- **Put something on a Premiere timeline:** run the **`premiere-automation`** skill
  (`.claude/skills/premiere-automation/`). Premiere Pro is the **third tool** alongside Flow
  and ffmpeg: a UXP panel inside Premiere on Windows dials out to a WebSocket server in WSL,
  and a session gets **27 tools** — import, build and re-cut a sequence, trim, transitions,
  markers, any installed effect with keyframes, and `export_frame` so it can **see** what it
  just did. Knowledge base: [`docs/premiere/`](./docs/premiere/README.md) —
  **[`recipes.md`](./docs/premiere/recipes.md) is the cookbook** (build a cut, push in,
  dissolve, grade, composite a Flow element, export and look, plus the things that flatly do
  not work); [`effects-catalogue.md`](./docs/premiere/effects-catalogue.md) is a live inventory
  of all **106 effects and 118 transitions** installed;
  [`setup.md`](./docs/premiere/setup.md) is the one-time per-machine install;
  [`api-notes.md`](./docs/premiere/api-notes.md) is what the API actually does versus what
  Adobe claims. **Two facts save the most time:** no tool returns a whole timeline (you get a
  per-track summary plus the complete state on disk to `jq`), and **every edit tool acts on the
  ACTIVE sequence** — a human clicking another timeline tab silently redirects your next call.
  **We own no paid plugins and are not buying any**: for fire, smoke and weather, generate the
  element in Flow on black and key it in. Choosing between Flow, ffmpeg and Premiere for a given
  job is the **`video-fx`** skill, below.
- **Decide how to achieve an effect — and whether the file is ready to ship:** run the
  **`video-fx`** skill (`.claude/skills/video-fx/`). The **judgement half** of video, where
  `premiere-automation` is the mechanics. Reach for it on "what effect does X", "how do I make it
  look like…", "which tool should I use", "do we need a plugin for this", or "is this ready to
  upload". It owns **lane choice** — five lanes now: **Flow** invents what does not exist,
  **sourcing** (`find-footage`) fetches what really happened, **ffmpeg** does what must be exact,
  **Premiere** is where it becomes an edit, and **After Effects is not installed**. Then it routes
  the "what effect does X" question into the live catalogues — **106 effects, 118 transitions and
  77 MOGRTs already installed**, so the answer is usually there before anyone searches the web.
  Knowledge base: [`docs/video-fx/`](./docs/video-fx/README.md). **Two facts save the most time:**
  **never end an answer at "buy X"** — state the free route, and if there isn't one say so and let
  Kai decide; and **nothing ships unmeasured** — `scripts/delivery-qc.sh` before every upload,
  because `camping.mp4` shipped full-range with no colour tag and every value below 16 crushed to
  black, which for a film made of shadows is not a grading nuance, it is the picture
  ([`delivery.md`](./docs/video-fx/delivery.md)).
- **Find real footage (and check we may publish it):** run the **`find-footage`** skill
  (`.claude/skills/find-footage/`). The **fifth lane** alongside Flow, ffmpeg and Premiere:
  footage that *already exists* and is free to use. Reach for it on "is there a royalty-free clip
  of…", "find archive footage of…", or "is this clip safe to use?" The lane rule is simple —
  **if the thing is real and already filmed, source it; if it never existed, invent it in Flow.**
  Knowledge base: [`docs/video-fx/footage-sources.md`](./docs/video-fx/footage-sources.md) —
  **68 sources tiered 🟢/🟡/🔴**, counts dated, with an end-to-end runbook from query to a
  hash-checked file Premiere can open — and a **verification table stating exactly which claims
  were proven live and which were only read**, because several of the originals failed re-run. **Two facts save the most time:** archive.org's
  `licenseurl` is **uploader-asserted**, so "it's on the Internet Archive" is not a licence and
  nothing amber ships without a per-item human check; and **"royalty-free" is a pricing model, not
  a permission** — the stock houses' EULAs routinely bar political use, which is the one thing all
  our work is. **We buy no footage**: the free tier is US federal film, newsreel, NASA and Commons
  CC0, and if the subject isn't there the answer is a public-domain still or Flow, never a quote
  from British Pathé.
- **Make a story grip, or review whether it does:** run the **`story-craft`** skill
  (`.claude/skills/story-craft/`). The internet's storytelling craft, researched once (24 briefs,
  2026-08-22) and kept: [`docs/story-craft/`](./docs/story-craft/README.md) —
  **[`principles.md`](./docs/story-craft/principles.md)** (thirty principles, each graded
  academic / practitioner / house-ruling, plus the sixteen rulings where the gurus disagree),
  **[`checklist.md`](./docs/story-craft/checklist.md)** (the ~40-question adversarial review pass
  and the coverage-sheet format), the narrator pattern, per-form craft (scroll comic, narrated
  video with the house VO markup, D&B lyrics, the serialised run), the evidence table with the
  never-cite list, and the case studies. **Build mode** while drafting beats, scripts, captions or
  lyrics inside `new-story` / `make-comic` / `music-video-short` / `suno-prompt`; **Review mode**
  for "does this land?" — gates first (the-reader.md's rules), one layer per pass, notes not fixes,
  findings adversarially verified, the arc held fixed. Three facts save the most time: **the moral
  is never stated, the beneficiary always is**; **tell the audience about the bomb** (the narrator's
  foreknowledge is free dramatic irony — never a withheld box); and **irony is decoded through prior
  belief**, so every sarcastic line is paired with an undeniable on-screen consequence.
- **Record an idea (the inbox):** run the **`new-idea`** skill
  (`.claude/skills/new-idea/`). It parks an idea the second it pops as a
  minimal-prose file under [`docs/ideas/`](./docs/ideas/README.md) and adds a
  row to the inbox index — then offers to develop it with `new-story`. The inbox
  is the stage *before* canon: optional, zero-commitment, medium-agnostic (a
  comic, a short, a song, or nothing yet). Develop when ready; don't develop here.
- **Record a marketing idea:** run the **`new-marketing-idea`** skill
  (`.claude/skills/new-marketing-idea/`). Captures a way to *reach people* —
  channels, campaigns, and especially promotion automations (ship a release,
  trigger its own teasers) — as a minimal-prose file under
  [`docs/marketing/`](./docs/marketing/README.md) after a short marketing-specific
  interview (lever, trigger, channels, human gate, dependencies, success signal).
  Content ideas stay with `new-idea`; this owns distribution.
- **Capture / develop a story:** run the **`new-story`** skill
  (`.claude/skills/new-story/`). It scaffolds `docs/stories/<story>/` (concept,
  characters, beats, songs) as the single source of truth and drives idea →
  media, reusing `docs/storytelling.md` and the `suno-prompt` skill. Worked
  reference: [`docs/stories/camping/`](./docs/stories/camping/README.md).
- **Make a comic (idea → rendered comic):** run the **`make-comic`** skill
  (`.claude/skills/make-comic/`). A gated, six-stage workflow (idea → characters →
  character images → storyboard → storyboard images → assemble) that composes
  `new-story` (canon), **Google Flow** driven over a logged-in browser (character
  + storyboard images, harvested into per-panel records under
  `docs/stories/<story>/storyboard/`), and `@badcode/comic` (assembly). Each generated
  image keeps its exact prompt + revision log so "just like that, but change X"
  is one cheap step. Worked reference: [`docs/stories/magic-money-tree/`](./docs/stories/magic-money-tree/README.md).
- **Edit an existing panel image:** run the **`edit-panel`** skill
  (`.claude/skills/edit-panel/`). "Take page 4 of `<comic>` and change X" —
  resolves the page to its image + exact recorded prompt with **`badcode panel`**
  (no browser), then loops `flow_edit_image` (reference-anchored, 2 candidates a
  round, always from the golden original) until the user accepts; updates the
  panel record's revision log and the rendered frame.
- **Animate a finished panel:** run the **`animate-slide`** skill
  (`.claude/skills/animate-slide/`). Turns a finished comic's slide into a
  Flow-generated scroll-scrubbed video. Requires the comic to be on the bucket
  pipeline (`assets.manifest.json` with `basePath "comics-v2/<comic>"`).
- **Make a standalone brand image:** run the **`new-image`** skill
  (`.claude/skills/new-image/`). Give it a short description; it pads the prompt
  into the BadCode brand register (near-black, one thin light, monumental
  machine architecture — anchored on `docs/images/register-anchor.jpg`),
  drives Flow to generate it, and records the exact prompt + revisions next to
  the image. Optionally animates the accepted still. Catalogue and convention:
  [`docs/images/README.md`](./docs/images/README.md). Comic panels stay with
  `badcode-art-direction`.
- **Make a short (idea → short-form music video):** run the
  **`music-video-short`** skill (`.claude/skills/music-video-short/`). A
  gated, six-stage workflow (concept → Suno song → look & cast → scene
  breakdown → clips → edit plan) that composes **`suno-prompt`** (the track,
  a manual gate), **`badcode-art-direction`** (the stills), and **Flow**
  (image→video clips, the one automated link) into a cut-ready package under
  `docs/shorts/<name>/`. The skill's contract ends at `edit-plan.md` — the
  human does the final cut. See [`docs/shorts/README.md`](./docs/shorts/README.md).

## Deeper context

- [`docs/vision.md`](./docs/vision.md) — origin story, mission, themes
- [`docs/voice.md`](./docs/voice.md) — tone guide with do/don't
- **[`docs/marketing/the-reader.md`](./docs/marketing/the-reader.md) — WHO THE WORK IS FOR. Read
  before writing any story, song or public copy.** Ruled 2026-08-15: the target is a working-class
  UK reader drifting right because the economy failed them — *not* anti-AI advocates and not the
  converted left. Ten evidence-backed rules, and the traps that cost us the reader if we trip them:
  never "you've been duped"; never deny immigration's real costs (proportionality instead); name the
  decision-maker, never the technology; **never raise automation fear without naming the beneficiary
  in the same piece** (unaimed, it demonstrably feeds nativism). Evidence:
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
