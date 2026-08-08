# BadCode Website Reset — Design & Implementation Plan

> **EXECUTION RULES (for agents):** Work ONE ticket at a time, in order unless
> dependencies say otherwise. Only the orchestrator changes ticket Status;
> workers may only append to Notes and the Discovered Issues Log. A ticket's
> checkbox is checked only after its Validation commands have been re-run by
> the orchestrator and pass. Do not expand scope; log surprises in the
> Discovered Issues Log instead.

Status: proposed
Relates: `docs/marketing/short-form-funnel.md`, `docs/stories/gitpush-origin-master/README.md`,
`packages/comic/AUTHORING.md`, design artifact (three homepage directions, "The Ledger" picked)

---

## Context

BadCode's output has shifted from *comics hosted on a website* to *narrated story
videos published to social platforms*. That shift is recorded across every story
tracker (`docs/stories/*/README.md`, Aug 4–6 2026) but the website still assumes
the old world, and the marketing docs have not been revised since 2026-07-22.

The site today is not deployed anywhere and, when run locally, is a single
centred column of monospace text listing four story rows, four dead track rows,
three channel rows with no URLs, and two text pages that end in "Full chapter
coming soon." The repo contains finished imagery that appears nowhere on it.

Two research passes (six agents: three over the repo, three over the web)
converged on the same conclusion: **the site's job is not to be where people
watch.** Kurzgesagt, with 26M subscribers, hosts no video on its website.
A24 sends you to Amazon. The site's job is to be the one place a story exists
as *several media at once* — video, track, comic, coin — with the argument
connecting them. That is genuinely unrepresentable on any platform, and it is
the entire justification for the site existing.

The visual direction ("The Ledger") is chosen and mocked. This plan builds it.

**Intended outcome:** a homepage that is a numbered catalogue, a story-page
template that holds a whole release, an Origin page that retells GitPush Origin
Master as a scroll comic, and a content pipeline where editing a story's
frontmatter in `docs/stories/` is the only place anything is typed.

### Decisions taken during the interview

| Decision | Ruling |
| --- | --- |
| Scope | Full reset of the site |
| Deployment / hosting / domain | **Entirely out of scope** — Kai handles it |
| The three.js Atlas | Retired and deleted (recoverable from git) |
| The four comic packages | Deleted; features harvested into one example comic |
| Video playback | Self-host the short cuts; YouTube facade for the long film |
| Audio playback | Facade embed (Bandcamp default), no custom player |
| Content source of truth | YAML frontmatter in `docs/stories/<slug>/story.md` |
| Extraction mechanism | Vite plugin → virtual module, HMR in dev, validated in build |
| Origin page | A scroll comic on `@badcode/comic`, doubling as the library example |
| Storyverse / Future Proof | Ordinary catalogue entries using a read-variant story page |
| Homepage hero line | **Kai is writing it — see T8.** |

### Two things Kai must supply

1. **The homepage hero copy.** T8 ships with a named constant holding
   placeholder text; Kai replaces it. T17 will not pass until it is real.
2. **The site origin**, as `VITE_SITE_ORIGIN` (default `https://badcode.tv`).
   Needed only so T15 can write absolute `og:image` URLs — social scrapers
   reject relative ones. This is a build variable, not a deployment decision.

### Handover note on prerendering

T15 emits a real HTML file per route. Those files only survive if the eventual
host prefers an existing static file over its SPA catch-all rewrite (Netlify,
Vercel, Cloudflare Pages and `nginx try_files` all do this by default). Hosting
is out of scope, but this is the one constraint worth knowing when it happens —
a blanket `/* → /index.html` rewrite would silently discard every per-route tag.

### Recovery point

Everything deleted by this plan exists at commit
**`589544ce7fe60bfaf021f69f7070cfaa2107b819`** (branch `main`, verified an
ancestor of HEAD). To recover any deleted file:
`git show 589544ce7fe60bfaf021f69f7070cfaa2107b819:<path>`

---

## Architecture

```
docs/stories/<slug>/story.md
   └── YAML frontmatter  ←── the single source of truth
              │
              ▼
   apps/web/plugins/catalogue/           (Vite plugin)
     dev   → configureServer: watch docs/stories/**, invalidate + full-reload
     build → parse + validate; throw with file path + field on error
     emits → frontmatter ONLY (prose never enters the bundle,
             except a read-variant story's rendered body)
              │
              ▼
   virtual:badcode/catalogue   →  { stories: StoryRecord[], byId() }
              │
      ┌───────┴──────────┬────────────────────────┐
      ▼                  ▼                        ▼
   Home (Ledger)     Story pages             prerender plugin
   reads all         reads one by slug       apply:'build', closeBundle:
                                             one HTML shell per route,
                                             real OG + Twitter tags
```

**Why a Vite plugin and not codegen.** The stated goal was low friction: edit a
story's frontmatter with a model, see it on the site. A virtual module gives
hot reload with nothing to run and nothing to commit. The rejected alternative
(a `badcode catalogue build` CLI writing a committed file) is more inspectable
but drifts silently between runs.

**Why prerendering is in scope despite deployment not being.** The app is a
client-rendered SPA, so a crawler fetching `/stories/camping` receives
`<title>BadCode</title>` and nothing else — every link shared from a video
previews as a bare URL. The catalogue is known at build time, so emitting a
static HTML shell per route is a build concern, not an ops one.

**One facade pattern, three uses.** Film (YouTube), audio (Bandcamp/SoundCloud)
and cuts all render as a poster plus a click target; the real `<iframe>` or
`<video>` mounts only on interaction. Measured cost of the naive alternative:
~500KB of JS for a YouTube embed, 100KB–2MB for social embeds.

### The signature, and why it is load-bearing

The homepage carries **the blade**: one hairline of light down the gutter which
forks where the catalogue begins. The branch that ended renders complete with a
terminal ring; the branch still being written continues as a gold dashed line
through *every catalogue entry*, with a node at each story. This is the canon
rule from `docs/stories/gitpush-origin-master/future-proof.md:167-172` built
rather than illustrated, and it is the one place boldness is spent.

### Colour and type decisions

- **The cyan `#46d5ff` is removed from the palette.** It is the single strongest
  reason the current site reads as a crypto project. One accent only: the signal
  gold `#E8C98A` already in the repo, meaning exactly one thing — *transmitting now*.
- **Monospace is demoted to one job**: the catalogue stamp and metadata.
- **Three registers from one variable grotesque** (Archivo: width axis 62–125%),
  the same structure Warp, Ghostly and Critical Music all ship. Instrument Serif
  carries the narrator's voice — and *only* the narrator's voice, which is what
  makes a visually divergent story page still read as BadCode.

---

## File Structure

### Create

| Path | Purpose |
| --- | --- |
| `apps/web/vitest.config.ts` | Test environment (happy-dom) + include globs |
| `apps/web/src/test/setup.ts` | Testing-library cleanup hook |
| `apps/web/.env.example` | Documents `VITE_SITE_ORIGIN` |
| `apps/web/plugins/catalogue/index.ts` | The Vite plugin: virtual module, watch, reload |
| `apps/web/plugins/catalogue/schema.ts` | `StoryRecord` type + validation rules |
| `apps/web/plugins/catalogue/parse.ts` | Read a `story.md`, split + parse frontmatter |
| `apps/web/plugins/catalogue/parse.test.ts` | TDD tests for parse + validate |
| `apps/web/plugins/catalogue/collect.ts` | Walk `docs/stories/`, sort, cross-validate |
| `apps/web/plugins/catalogue/collect.test.ts` | Tests for sort + duplicate detection |
| `apps/web/plugins/catalogue/markdown.ts` | Minimal markdown → HTML for read variants |
| `apps/web/plugins/catalogue/markdown.test.ts` | Tests for the renderer |
| `apps/web/plugins/prerender/index.ts` | Emit per-route HTML shells with meta tags |
| `apps/web/src/content/catalogue.ts` | Typed re-export of the virtual module |
| `apps/web/src/content/virtual.d.ts` | Ambient declaration for `virtual:badcode/catalogue` |
| `apps/web/src/content/chips.ts` | Derives the chip row from a record's populated blocks |
| `apps/web/src/styles/tokens.css` | The single token source |
| `apps/web/src/styles/global.css` | Reset, base type, focus, reduced-motion |
| `apps/web/src/fonts/*.woff2` | Self-hosted Archivo / Instrument Serif / JetBrains Mono |
| `apps/web/src/components/Facade.tsx` | Poster-then-mount primitive |
| `apps/web/src/components/Facade.test.tsx` | Render tests for the facade contract |
| `apps/web/src/components/FilmFacade.tsx` | YouTube wrapper |
| `apps/web/src/components/AudioFacade.tsx` | Bandcamp / SoundCloud wrapper |
| `apps/web/src/components/CutStrip.tsx` | Self-hosted 9:16 cuts |
| `apps/web/src/components/Blade.tsx` | The vertical light |
| `apps/web/src/components/Fork.tsx` | The branch SVG |
| `apps/web/src/components/ChipRow.tsx` | `VIDEO · TRACK · COMIC` state chips |
| `apps/web/src/components/CatalogueRow.tsx` | One homepage entry |
| `apps/web/src/components/Plate.tsx` | The invariant story-page header |
| `apps/web/src/routes/Story.tsx` | Story page, film + read variants |
| `apps/web/src/routes/Origin.tsx` | Mounts the Origin comic |
| `apps/web/src/comics/origin/OriginComic.tsx` | The GPOM scroll comic |
| `apps/web/src/comics/origin/effects.ts` | Harvested effects from the four comics |
| `apps/web/src/comics/origin/assets.manifest.json` | Bucket wiring for Origin |
| `apps/web/public/favicon.svg` | Brand mark |
| `docs/stories/storyverse/story.md` | Frontmatter + spine so Storyverse is a catalogue entry |
| `docs/stories/future-proof/story.md` | Same, after the move |
| `docs/stories/README.md` | Documents the frontmatter schema |

### Modify

| Path | Change |
| --- | --- |
| `apps/web/tsconfig.json` | Add `plugins` to `include`; add `"node"` to `types` |
| `apps/web/package.json` | Add `yaml`, `happy-dom`, `@testing-library/react`, `@testing-library/jest-dom`, `@types/node`; remove `three`, `@react-three/*`, `@types/three`, `gsap` (T14) |
| `apps/web/src/App.tsx` | New route table + five legacy redirects |
| `apps/web/src/main.tsx` | Import `tokens.css` + `global.css` |
| `apps/web/index.html` | Baseline meta, favicon, OG defaults |
| `apps/web/vite.config.ts` | Register both plugins |
| `apps/web/src/routes/Home.tsx` | **Replaced** — currently the Atlas mount, becomes the Ledger |
| `apps/web/src/routes/About.tsx` | Real page about Kai and Jack; drop the `TextPage` import |
| `apps/web/src/routes/NotFound.tsx` | Restyle to the new system; drop the `TextPage` import |
| `docs/stories/{camping,karen,magic-money-tree,gitpush-origin-master,galileo}/story.md` | Extend frontmatter |
| `packages/comic/AUTHORING.md` | Line 154 — worked example points at `comics/origin` |
| `CLAUDE.md` | Repo map: routes, the catalogue pipeline, the example comic |

### Delete

- All of `apps/web/src/home/` — **38 files** (the `atlas/` tree, `landing/`,
  `catalog.ts`, `timeline.ts`, `comics.ts`, `graph.ts`, `colors.ts`,
  `environment.ts`, `Fallback2D.tsx`, `assets.manifest.json`, 11 `.test.ts`).
- All of `apps/web/src/comics/{camping,karen,magic-money-tree,gpom-short}/` —
  15 files, **after** T12 has harvested from them.
- `apps/web/src/routes/{BadCodeHome,ComicPage,ComicStub,TextPage,Storyverse,FutureProof}.tsx`
- `apps/web/src/index.css` (superseded by tokens + global).
- `apps/web/public/comics/camping/` and `apps/web/public/comics/magic-money-tree/`
  — orphaned once their comics are gone (~7.6MB); `gpom-short/img/` **stays**,
  the Origin comic uses it.
- `docs/stories/gitpush-origin-master/future-proof.md` → **moved**, not deleted.

---

## Interfaces

```ts
// apps/web/plugins/catalogue/schema.ts

export interface Film {
  youtube: string          // video id, not a URL
  poster: string           // bucket-relative path, or /-rooted local path
  duration: string         // "9:42"
}

export interface Track {
  bandcamp?: string        // album/track id
  soundcloud?: string      // full permalink; used only when bandcamp is absent
  bpm?: number
}

export interface Cut {
  src: string              // bucket-relative mp4
  poster: string           // REQUIRED — authors supply it; nothing derives it
  duration: string         // "0:28"
  platform: string         // "TikTok" | "Reels" | "Shorts"
}

export interface Coin {
  url: string              // external, e.g. the Emperor's New Coin page
  label: string
}

export interface StoryRecord {
  // required
  id: string               // must equal the folder name it came from
  title: string
  logline: string
  catalogue: string        // "BC-001" — unique across the catalogue
  published: string        // "2026-08" — display only, NOT the sort key

  // optional narrative metadata (present in today's files, not enforced)
  status?: string
  release?: string
  media?: string[]

  // optional release blocks — absent until the media exists
  argument?: string        // narrator copy, plain text
  film?: Film
  track?: Track
  cuts?: Cut[]
  comic?: string           // internal route, e.g. "/origin"
  coin?: Coin
  read?: string            // path to a long-form doc, relative to the story folder

  // injected by the plugin, STRIPPED before the client bundle is emitted
  sourcePath?: string

  // produced by the plugin for read-variant stories only
  readHtml?: string
}

export function validateStory(raw: unknown, sourcePath: string): StoryRecord
export function validateCatalogue(stories: StoryRecord[]): void
// throws on: duplicate `catalogue` values, or an `id` that does not match its
// folder. Gaps in the numbering are LEGAL — BC-004 may exist with no BC-005.
```

```ts
// virtual:badcode/catalogue
export const stories: StoryRecord[]        // sorted by `catalogue` ascending
export function byId(id: string): StoryRecord | undefined
```

```ts
// apps/web/src/content/chips.ts
export type ChipKind = 'video' | 'track' | 'comic' | 'coin' | 'read'
export type ChipState = 'live' | 'soon'
export interface Chip { kind: ChipKind; state: ChipState }

/** Derived from which blocks are populated — never authored by hand.
 *  A story listing a medium in `media` that has no matching block yields
 *  that chip in the `soon` state. */
export function chipsFor(record: StoryRecord): Chip[]
```

```ts
// apps/web/src/components/Facade.tsx
interface FacadeProps {
  poster: string
  alt: string
  aspect: '16/9' | '9/16' | '1/1'
  label?: string                    // overlay caption, e.g. "The story · 9:42"
  children: () => React.ReactNode   // mounted only after activation
}
```

### Read-variant rule

A story renders as a **read variant** when it has no `film`. Its body is:
- the file named by `read`, if present (e.g. Storyverse → `./confession.md`); else
- **the prose of its own `story.md`** (Future Proof, whose story.md *is* the text).

The plugin renders that markdown to `readHtml` at build time. Film-variant
stories never carry `readHtml`, so no prose reaches their bundle.

### Routes

```
/                     Home        the Ledger catalogue
/origin               Origin      GPOM scroll comic
/stories/:slug        Story       film variant or read variant
/about                About       Kai and Jack, the humans
*                     NotFound
```

Legacy redirects (every public URL that has ever existed):

| From | To |
| --- | --- |
| `/comics/gitpush-origin-master` (incl. `#hash`) | `/origin` |
| `/gitpush-origin-master` (incl. `#hash`) | `/origin` |
| `/comics/:slug` | `/stories/:slug` |
| `/storyverse` | `/stories/storyverse` |
| `/future-proof` | `/stories/future-proof` |

---

## Out of Scope

- **Deployment, hosting, domain, CI, SPA rewrite rules.** Kai owns this entirely.
- The persistent cross-page audio player (rejected: rent the platforms' players).
- A custom video player (rejected for the same reason).
- Rebuilding the three.js Atlas in any form.
- Rebuilding the camping / karen / magic-money-tree comics as comics.
- Writing new story content, beyond frontmatter fields and the About page.
- Email capture backend — the row renders, wiring a provider is separate.
- Analytics, cookie consent tooling, `sitemap.xml`, `robots.txt`.

---

## Tickets

### T1: Tooling baseline — test environment, node types, tsconfig   [Status: pending | Model: sonnet]
- **Scope:** Everything later tickets assume and the repo does not have. Add
  devDeps `happy-dom`, `@testing-library/react`, `@testing-library/jest-dom`,
  `@types/node`, and dep `yaml`. Create `apps/web/vitest.config.ts` setting
  `environment: 'happy-dom'`, a setup file, and an `include` glob covering both
  `src/**/*.test.{ts,tsx}` and `plugins/**/*.test.ts`. Create
  `apps/web/src/test/setup.ts`. Modify `apps/web/tsconfig.json` to add
  `"plugins"` to `include` and `"node"` to the `types` array (it is currently
  `["vite/client"]`, which suppresses node globals). Add `apps/web/.env.example`
  documenting `VITE_SITE_ORIGIN=https://badcode.tv`.
- **Files:** create `apps/web/vitest.config.ts`, `apps/web/src/test/setup.ts`,
  `apps/web/.env.example`; modify `apps/web/tsconfig.json`, `apps/web/package.json`.
- **Acceptance criteria:** a throwaway test rendering `<div>hi</div>` with
  `@testing-library/react` passes and is then deleted; the existing 52 tests
  still pass; `npm run typecheck` clean; a `.ts` file under `plugins/` importing
  `node:fs` typechecks.
- **TDD:** no (tooling)
- **Validation:** `npm run test --workspace @badcode/web` passes;
  `npm run typecheck` clean.
- **Depends on:** —
- [ ] done
- Notes:

### T2: Frontmatter schema, parser and validator   [Status: pending | Model: sonnet]
- **Scope:** Pure logic, no Vite. `parse.ts` splits the leading `---` block and
  parses it with `yaml`, returning `{ data, body }`. `schema.ts` implements
  `validateStory`. Required: `id`, `title`, `logline`, `catalogue`, `published`.
  Everything else optional. Errors name the file path and the offending field.
  Unknown extra fields are allowed and ignored (the existing files carry
  `canon_source`).
- **Files:** create `apps/web/plugins/catalogue/{parse.ts,schema.ts,parse.test.ts}`.
- **Acceptance criteria:** valid frontmatter returns a typed `StoryRecord`;
  a missing required field throws naming both field and path; malformed YAML
  throws naming the path; a `film` block missing `youtube` throws; a `cuts`
  entry missing `poster` throws; `body` contains the prose and never leaks into
  the record.
- **TDD:** yes
- **Validation:** `npm run test --workspace @badcode/web` passes.
- **Depends on:** T1
- [ ] done
- Notes:

### T3: Catalogue collection, cross-validation and markdown   [Status: pending | Model: sonnet]
- **Scope:** `collect.ts` walks `docs/stories/*/story.md` (resolve the repo root
  from the Vite config dir, do not assume `process.cwd()`), parses each, sorts
  **by `catalogue` ascending**, and cross-validates: duplicate catalogue numbers
  throw naming both paths; an `id` not matching its folder name throws. A folder
  without `story.md` is skipped silently. Gaps in numbering are legal.
  `markdown.ts` renders headings, paragraphs, blockquotes, lists, emphasis,
  links and inline code to HTML, escaping any raw HTML in the source.
- **Files:** create `apps/web/plugins/catalogue/{collect.ts,collect.test.ts,markdown.ts,markdown.test.ts}`.
- **Acceptance criteria:** records return sorted ascending; duplicates throw
  naming both paths; id/folder mismatch throws; a folder with no `story.md` is
  skipped; a numbering gap does NOT throw; markdown output escapes `<script>`.
- **TDD:** yes
- **Validation:** `npm run test --workspace @badcode/web` passes.
- **Depends on:** T2
- [ ] done
- Notes:

### T4: The Vite plugin and virtual module   [Status: pending | Model: sonnet]
- **Scope:** A plugin resolving `virtual:badcode/catalogue` and serialising the
  collected records to a JS module. `sourcePath` must be stripped from every
  record before emit. For read-variant stories (no `film`), attach `readHtml`
  from either the `read` file or the story's own body.
  **Dev reload must be explicit, not implied:** use `configureServer` to
  `server.watcher.add()` the `docs/stories` directory, subscribe to `change`,
  `add` and `unlink`, and on any event under `docs/stories/**/story.md` call
  `moduleGraph.invalidateModule()` on the virtual module then
  `server.ws.send({ type: 'full-reload' })`. Watching the **directory** (not
  just files seen during `load`) is what makes a newly created story appear
  without restarting the dev server. Build-time validation failures must abort
  the build. Add the ambient declaration and the typed re-export.
- **Files:** create `apps/web/plugins/catalogue/index.ts`,
  `apps/web/src/content/{catalogue.ts,virtual.d.ts}`; modify `apps/web/vite.config.ts`.
- **Acceptance criteria:** `import { stories } from 'virtual:badcode/catalogue'`
  typechecks and resolves in dev and build; editing a logline while `npm run dev`
  runs reloads the browser without manual refresh; **creating a brand-new story
  folder while the dev server runs makes it appear without a restart**; a
  malformed frontmatter aborts `npm run build` with the path in the message;
  no `sourcePath` string appears in the built bundle.
- **TDD:** no (wiring)
- **Validation:** `npm run build` succeeds; `npm run typecheck` clean; manual:
  run `npm run dev`, edit a logline, then create a scratch story folder, confirm
  both appear; `grep -r "sourcePath" apps/web/dist/assets/` empty.
- **Depends on:** T3
- [ ] done
- Notes:

### T5: Extend the canon frontmatter   [Status: pending | Model: sonnet]
- **Scope:** Add `catalogue` and `published` to all five existing
  `docs/stories/*/story.md`, plus `argument` where the canon supplies a usable
  line. Assign GPOM `BC-000`, Camping `BC-001`, Karen `BC-002`, Magic Money Tree
  `BC-003`, Galileo `BC-004`. **Set `comic: /origin` on GPOM** — T13's
  acceptance depends on it. Create `docs/stories/storyverse/story.md`
  (catalogue `BC-005`, `read: ./confession.md`). `git mv`
  `docs/stories/gitpush-origin-master/future-proof.md` to
  `docs/stories/future-proof/story.md`, add frontmatter (catalogue `BC-006`, no
  `read` — its own body is the text), and fix every inbound link. Do NOT invent
  film/track/cuts data.
- **Files:** modify five `story.md` files and every doc linking to
  `future-proof.md`; create two `story.md` files; one `git mv`.
- **Acceptance criteria:** `collect()` returns 7 records with no validation
  errors; `grep -rn "future-proof\.md" docs/ apps/ CLAUDE.md` shows only links
  that resolve to the new path (note: most existing links are *relative and
  in-folder* — `README.md`, `coda-fork.md`, `discovery-timeline.md`,
  `stitch-pass.md` all reference it without the folder prefix, so a
  folder-qualified grep would miss them).
- **TDD:** no (content)
- **Validation:** `npm run build` succeeds; the grep above shows no unresolved
  paths; every matched link opened and confirmed to resolve.
- **Depends on:** T4
- [ ] done
- Notes:

### T6: Design tokens, self-hosted fonts, global CSS   [Status: pending | Model: sonnet]
- **Scope:** Create `tokens.css` + `global.css` and import them from `main.tsx`.
  **Leave `index.css` in place** — `routes/ComicPage.tsx:12` and
  `home/landing/landing.css` still consume `var(--cyan)` and both survive until
  T14; deleting it now breaks them. Self-host four woff2 files in
  `apps/web/src/fonts/`, latin subsets only: Archivo variable
  (`https://fonts.gstatic.com/s/archivo/v25/k3kQo8UDI-1M0wlSfdnoLg.woff2`,
  weight 100–900, stretch 62–125%), Instrument Serif regular + italic, and
  JetBrains Mono variable. For the latter three, request
  `https://fonts.googleapis.com/css2?family=…` with a desktop UA and take the
  `@font-face` block whose `unicode-range` contains `U+0000-00FF`.
  Tokens: `--void:#07080A`, `--pitch:#000`, `--edge:rgba(226,238,244,.13)`,
  `--blade:#DCE9EE`, `--ink:#E4EBEF`, `--ash:#6B7681`, `--ash-dim:#49525B`,
  `--signal:#E8C98A`. **No cyan token.** Global rules: `focus-visible` outline in
  `--signal`, `prefers-reduced-motion` killing animation and transition,
  explicit `body` background.
- **Files:** create `apps/web/src/styles/{tokens.css,global.css}`,
  `apps/web/src/fonts/*.woff2`; modify `apps/web/src/main.tsx`.
- **Acceptance criteria:** all four faces load from the bundle with zero
  `fonts.gstatic.com` requests at runtime; `tokens.css` and `global.css` contain
  no cyan value (the repo-wide cyan sweep belongs to T14, which deletes the files
  that still hold it); reduced-motion disables all animation.
- **TDD:** no (styling)
- **Validation:** `npm run build` succeeds; `grep -n "46d5ff" apps/web/src/styles/*.css`
  empty; manual: DevTools Network shows no font CDN requests.
- **Depends on:** T1
- [ ] done
- Notes:

### T7: The facade primitive and its three wrappers   [Status: pending | Model: sonnet]
- **Scope:** `Facade.tsx` renders a poster at a given aspect with an optional
  caption and play affordance, mounting `children()` only after activation
  (click or Enter/Space). `FilmFacade` mounts a `youtube-nocookie.com` iframe
  with `autoplay=1`. `AudioFacade` mounts a Bandcamp iframe, falling back to
  SoundCloud only when `bandcamp` is absent. `CutStrip` renders self-hosted 9:16
  `<video muted playsinline loop preload="none">` elements, at most one playing
  at a time via a single IntersectionObserver at `threshold: 0.6`, with `src`
  swapped in from `data-src` on activation. Also build `chips.ts`.
- **Files:** create `apps/web/src/components/{Facade,FilmFacade,AudioFacade,CutStrip}.tsx`,
  `apps/web/src/components/Facade.test.tsx`, `apps/web/src/content/chips.ts`.
- **Acceptance criteria:** before activation no iframe and no `<video src>`
  exists in the DOM; after activation exactly one does; the facade is
  keyboard-activatable with a visible focus state; under reduced motion cuts show
  posters and do not autoplay; `chipsFor()` returns `soon` for a medium listed in
  `media` with no matching block, and `live` when the block exists.
- **TDD:** no (render tests written alongside)
- **Validation:** `npm run test --workspace @badcode/web` passes;
  `npm run typecheck` clean.
- **Depends on:** T1, T6
- [ ] done
- Notes:

### T8: The homepage — The Ledger   [Status: pending | Model: opus]
- **Scope:** Replace `routes/Home.tsx` (currently the Atlas mount) with the
  Ledger, per the approved mock: hero image with transmission strip and the
  two-step headline; the blade running the hero and continuing into the fork
  SVG; the gold dashed unfinished branch running the full catalogue with a node
  per row; catalogue rows from `virtual:badcode/catalogue` with 16:9 thumb,
  `BC-NNN` stamp, title, logline and chip row; a tail row with outbound channels
  and an email prompt. Extract `Blade`, `Fork`, `ChipRow`, `CatalogueRow`.
  **Hero copy:** put both strings in one exported constant
  `HERO_COPY` at the top of the file with a comment marking it as Kai's to
  supply. Ship the ticket with placeholder text in it — replacing the text is
  Kai's action, not a blocker on this ticket. T17 gates on it being real.
- **Files:** modify `apps/web/src/routes/Home.tsx`; create
  `apps/web/src/components/{Blade,Fork,ChipRow,CatalogueRow}.tsx` + CSS
  (plain CSS files, matching the repo — no CSS-in-JS).
- **Acceptance criteria:** every catalogue story renders a row; a story with no
  `film`/`track` shows `soon` chips and the dashed empty-thumb state; the blade
  aligns with the catalogue gutter at 1320px, 860px and 390px; rows are links
  with visible focus; `HERO_COPY` is a single clearly-commented constant.
- **TDD:** no (presentational)
- **Validation:** `npm run typecheck` clean; `npm run build` succeeds; manual
  pass at 390px and 1320px.
- **Depends on:** T5, T7
- [ ] done
- Notes:

### T9: The story page — film variant   [Status: pending | Model: opus]
- **Scope:** `routes/Story.tsx` resolving `:slug` via `byId`, rendering the 404
  route on miss. Renders the invariant `Plate` (catalogue number, title, year,
  media list, back link — sticky, identical on every story page regardless of
  that story's own styling), the blade, the title block with the logline in the
  narrator serif, the `FilmFacade`, a "The rest of it" band listing track, comic
  and coin, a "Cuts" band using `CutStrip`, the argument in serif, and a
  next-entry footer. Sections whose data is absent do not render at all.
- **Files:** create `apps/web/src/routes/Story.tsx`,
  `apps/web/src/components/Plate.tsx` + CSS.
- **Acceptance criteria:** `/stories/camping` renders; an unknown slug renders
  the 404; a story with no `cuts` omits the Cuts band rather than rendering an
  empty one; the Plate stays fixed on scroll; works at 390px.
- **TDD:** no (presentational)
- **Validation:** `npm run typecheck` clean; `npm run build` succeeds; manual
  check of a full-media story and a near-empty one (Galileo).
- **Depends on:** T8
- [ ] done
- Notes:

### T10: The story page — read variant   [Status: pending | Model: sonnet]
- **Scope:** When a record has no `film`, render a long-form reading layout:
  same Plate, same blade, a measure of roughly 68 characters, body in the
  narrator serif with a proper heading scale and generous leading, from
  `readHtml`.
- **Files:** modify `apps/web/src/routes/Story.tsx` + CSS.
- **Acceptance criteria:** `/stories/storyverse` renders the full confession
  from `confession.md`; `/stories/future-proof` renders from its own story.md
  body; headings, paragraphs, lists and blockquotes are styled; the measure holds
  at 1320px; no prose appears on film-variant pages.
- **TDD:** no (presentational; the renderer itself is tested in T3)
- **Validation:** `npm run build` succeeds; manual read-through of both pages.
- **Depends on:** T9
- [ ] done
- Notes:

### T11: About, 404, and the route table   [Status: pending | Model: sonnet]
- **Scope:** Rewrite `About.tsx` as a real page about Kai and Jack as people and
  BadCode as an art collective — short, factual, in-register, no fiction.
  Restyle `NotFound.tsx`, keeping "404 — no such commit". **Both files currently
  `import { TextPage } from './TextPage'` (line 1 of each) and TextPage is
  deleted in T14 — that import must be removed here.** Rewrite `App.tsx` with
  the new route table and all five legacy redirects, preserving `#hash` on the
  two Atlas redirects.
- **Files:** modify `apps/web/src/{App.tsx,routes/About.tsx,routes/NotFound.tsx}`.
- **Acceptance criteria:** all five routes resolve; all five redirects work and
  the two Atlas ones preserve their hash; `grep -rn "TextPage" apps/web/src/routes/`
  matches only `TextPage.tsx` itself.
- **TDD:** no (wiring/copy)
- **Validation:** `npm run typecheck` clean; manual check of every route and redirect.
- **Depends on:** T10
- [ ] done
- Notes:

### T12: Harvest the comic feature inventory   [Status: pending | Model: sonnet]
- **Scope:** Before anything is deleted, read all four comic packages and
  `packages/comic/AUTHORING.md` and produce a written inventory of every library
  feature demonstrated across them — each effect, transition, text-reveal
  segment, bubble type, panel preset, `AnimationWidget` usage and asset-wiring
  mode — recording which file demonstrates each. Consolidate the useful custom
  effects from `comics/camping/effects.ts` into `comics/origin/effects.ts`.
  Record the inventory in this plan's Discovered Issues Log and as a comment
  block atop `effects.ts`.
- **Files:** create `apps/web/src/comics/origin/effects.ts`.
- **Acceptance criteria:** the inventory names every export from
  `@badcode/comic`, `/effects`, `/transitions` and `/text` and states whether it
  is demonstrated and where; `effects.ts` typechecks.
- **TDD:** no (analysis)
- **Validation:** `npm run typecheck` clean.
- **Depends on:** —
- [ ] done
- Notes:

### T13: The Origin comic   [Status: pending | Model: opus]
- **Scope:** GitPush Origin Master as a scroll comic at `/origin`, using the 16
  panels in `apps/web/public/comics/gpom-short/img/` and following the 20-scene
  distillation in `docs/stories/gitpush-origin-master/story.md`.
  **Start by porting `apps/web/src/comics/gpom-short/GpomShortComic.tsx`, which
  is already a working 16-panel GPOM scroll comic** — then extend it to
  demonstrate the full library surface catalogued in T12, so it serves as the
  single worked example. Honour the canon: the pre-revert AI is never
  personified; the branch diagram stays at margin weight; one metaphor system on
  the surface at a time.
- **Files:** create `apps/web/src/comics/origin/{OriginComic.tsx,assets.manifest.json}`,
  `apps/web/src/routes/Origin.tsx`.
- **Acceptance criteria:** `/origin` scrolls end to end without layout break at
  390px and 1320px; every feature from the T12 inventory appears at least once;
  no personified AI figure; reduced motion disables scrubbing and transitions;
  the BC-000 story page's comic chip links here (relies on `comic: /origin` set
  in T5).
- **TDD:** no (presentational)
- **Validation:** `npm run typecheck` clean; `npm run build` succeeds; manual
  scroll-through at both widths.
- **Depends on:** T11, T12
- [ ] done
- Notes:

### T14: Delete the Atlas, the old landing page and the four comics   [Status: pending | Model: sonnet]
- **Scope:** Delete everything in the File Structure "Delete" list. Remove
  `three`, `@react-three/fiber`, `@react-three/drei`,
  `@react-three/postprocessing`, `@types/three` and `gsap` from
  `apps/web/package.json` — all verified to be imported only by
  `src/home/atlas/*`, and `gsap` is imported nowhere in the repo at all. Keep
  `thumbhash` (a real `packages/comic` dependency).
- **Files:** delete 38 files under `src/home/`, 15 under
  `src/comics/{camping,karen,magic-money-tree,gpom-short}/`, 6 route files,
  `src/index.css`, and the two orphaned `public/comics/` asset folders; modify
  `apps/web/package.json`.
- **Acceptance criteria:** `npm run typecheck`, `npm run build` and
  `npm run test` all clean; the dev server starts and all five routes work;
  no cyan remains anywhere.
- **TDD:** no (deletion)
- **Validation:**
  `grep -rn --exclude-dir=dist --exclude-dir=node_modules "home/atlas\|home/catalog\|home/timeline\|home/comics" apps/`
  empty; `grep -rn --exclude-dir=dist --exclude-dir=node_modules "46d5ff" apps/`
  empty; `npm run typecheck && npm run build && npm run test` clean.
- **Depends on:** T13
- [ ] done
- Notes:

### T15: Metadata baseline and the prerender step   [Status: pending | Model: sonnet]
- **Scope:** Give `index.html` a real head: description, theme-color, favicon,
  default OG/Twitter tags. Build the prerender plugin with `apply: 'build'` and
  a `closeBundle` hook that reads the emitted `dist/index.html` and writes one
  copy per route (catalogue routes plus `/`, `/origin`, `/about`) with
  route-specific `<title>`, `<meta name="description">`, `og:title`,
  `og:description`, `og:image`, `og:url`, `twitter:card`, `twitter:image`.
  Absolute URLs come from `import.meta.env.VITE_SITE_ORIGIN`, defaulting to
  `https://badcode.tv` when unset. Story OG images use `film.poster`, else the
  first cut's poster, else the brand anchor. Add `public/favicon.svg`.
- **Files:** create `apps/web/plugins/prerender/index.ts`,
  `apps/web/public/favicon.svg`; modify `apps/web/index.html`,
  `apps/web/vite.config.ts`.
- **Acceptance criteria:** after `npm run build`,
  `dist/stories/camping/index.html` exists with a Camping-specific title,
  description and `og:image`; `dist/index.html` and `dist/origin/index.html`
  likewise; every `og:image` and `og:url` is absolute and origin-prefixed;
  building with `VITE_SITE_ORIGIN` set to another value changes them.
- **TDD:** no (build config)
- **Validation:** `npm run build`, then
  `grep -o '<meta property="og:title"[^>]*>' apps/web/dist/stories/camping/index.html`
  shows the story title, and the same grep on `dist/index.html` shows the site
  title; `grep -c 'og:image" content="https://' apps/web/dist/stories/camping/index.html`
  returns 1.
- **Depends on:** T14
- [ ] done
- Notes:

### T16: Documentation   [Status: pending | Model: sonnet]
- **Scope:** Update `CLAUDE.md`: repo map, the new route list, how the catalogue
  pipeline works and where frontmatter lives, and that
  `apps/web/src/comics/origin` is now the worked comic example. Update
  `packages/comic/AUTHORING.md` — **line 154 currently reads "Worked example:
  `apps/web/src/comics/camping/effects.ts` — the `trip` effect…"; that is the
  line to change.** Create `docs/stories/README.md` documenting the frontmatter
  schema field for field so the `new-story` skill and future model sessions know
  it.
- **Files:** modify `CLAUDE.md`, `packages/comic/AUTHORING.md`; create
  `docs/stories/README.md`.
- **Acceptance criteria:** `grep -rn "comics/camping" packages/comic/AUTHORING.md`
  empty; `grep -rn "/comics/\|Atlas\|atlas" CLAUDE.md` returns only intentional
  history references, none presented as live routes; the schema in
  `docs/stories/README.md` matches `schema.ts` field for field.
- **TDD:** no (docs)
- **Validation:** the two greps above, reviewed by hand.
- **Depends on:** T15
- [ ] done
- Notes:

### T17: End-to-end verification   [Status: pending | Model: sonnet]
- **Scope:** Prove the whole thing works together.
- **Acceptance criteria:**
  1. `npm install && npm run typecheck && npm run test && npm run build` all
     clean from a fresh checkout.
  2. `npm run dev` — every route loads: `/`, `/origin`, `/about`, one
     film-variant story, one read-variant story, a bad slug, and all five
     legacy redirects (hash preserved on the two Atlas ones).
  3. Editing a `logline` in any `docs/stories/*/story.md` reloads the browser;
     creating a new story folder does too, without a dev-server restart.
  4. Breaking a required frontmatter field fails `npm run build` with the file
     path in the error; restore it afterwards.
  5. Manual pass at 390px and 1320px on `/`, one story page and `/origin`:
     no horizontal body scroll, blade aligned, focus states visible.
  6. Reduced-motion emulation: no animation, no autoplay, posters static.
  7. No `fonts.gstatic.com` requests and no third-party iframe in the Network
     panel until a facade is clicked.
  8. **`HERO_COPY` in `routes/Home.tsx` holds Kai's real copy, not the
     placeholder.** This is the one criterion that depends on someone outside
     the ticket list.
  9. `dist/stories/<slug>/index.html` exists for every catalogue story with
     story-specific OG tags.
- **TDD:** no (verification)
- **Validation:** all nine criteria executed and reported.
- **Depends on:** T16
- [ ] done
- Notes:

---

## Discovered Issues Log

_(appended by executors during implementation)_
