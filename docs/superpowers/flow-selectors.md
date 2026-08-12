# Google Flow — UI recipe + automation map (from the spike)

> Recorded 2026-06-25 from the first successful automated generation+harvest.
> This is the input contract for hardening the loop into `badcode flow`.
> Driven by Playwright MCP attached over CDP to a WSLg Chromium logged into Flow.

## TL;DR — the loop that works

1. **Navigate** `https://labs.google/fx/tools/flow`.
2. **Open/ensure a project** — projects page has `button "add_2 New project"`; opening it
   lands on `/fx/tools/flow/project/<uuid>` with the editor.
3. **Type the prompt** into the agent textbox (`role=textbox`, placeholder
   *"What do you want to create?"*).
4. **Submit** — `button "arrow_forward Create"` (disabled until text is present).
5. **Wait** for the assistant turn to finish (a new assistant paragraph + a
   `button "Generated image"` appears in the canvas).
6. **Harvest the image without the UI** (see "Download mechanism" — the important bit).
7. Optionally `badcode push` the harvested file to the bucket.

## Key findings that change the original spec

- **Flow is now AGENT-DRIVEN, not a prompt+refs+Generate form.** You converse with an
  assistant ("Hi Jack, what would you like to do?"). A plain natural-language
  "Generate a single image: <scene>" works and produces an image directly.
- **One image per request, not N candidates.** The spec's "best of N" selection model
  does not match Flow's image agent. The real loop is **generate → judge → if weak,
  send a follow-up correction in the same session** (the agent keeps context and can
  "adjust the composition / explore a different time of day"). Selection becomes
  iterative refinement, not pick-from-grid.
- **References/consistency are first-class via the left sidebar**, not file inputs on the
  prompt: `Characters` (`button "accessibility_new Characters"`), `Add Media`
  (`button "add Add Media"`), `Scenes`, `Tools`. The plan's `flow-prep` (download refs
  to disk) is still useful, but attachment is via **Add Media upload / Characters**, and
  `browser_file_upload` (Playwright) handles the OS picker. Reference workflow still
  needs its own spike.
- **Account is on the ULTRA plan** — full model access.
- Built-in agentic modes exist: **"Make a Story"** and **"Develop a storyboard"** — Flow
  itself can storyboard. Worth evaluating whether to lean on it or drive frame-by-frame.

## Download mechanism (the robust, scalable part)

The generated `<img>`'s `src` is an **authenticated, same-origin redirect**:

```
https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=<MEDIA_UUID>
```

- In-page `fetch()` of it **fails** (CORS/CSP — it 302s to a cross-origin CDN host).
- The Playwright **request context** (`page.request.get(url)`) follows the redirect with
  the browser's cookies, server-side, and exposes the final URL via `resp.url()`:

```
https://flow-content.google/image/<MEDIA_UUID>?Expires=<ts>&KeyName=labs-flow-prod-cdn-key&Signature=<sig>
```

- That final URL is a **signed CDN URL — publicly fetchable without cookies** until
  `Expires`. So the harvest is: read `name` from the img src → resolve via
  `page.request` → `curl` the signed URL to disk. No download button, no file-chooser,
  no image bytes through the model's context.

Worked example (JPEG, 1376×768, ~868 KB):
`browser_run_code_unsafe` returns `resp.url()`; shell `curl "<signed>" -o frame.jpg`.

### run_code sandbox limits (important for hardening)
`browser_run_code_unsafe` runs in a VM sandbox: **no `require`, no dynamic `import`, no
`fs`.** It only has `page`. So it can resolve/return the signed URL (and could return
base64, but don't — it bloats context). Do the actual file write in the **deterministic
`badcode flow` command** using the Playwright *library* (full Node, `fs` available), or
`curl` from the shell as above.

## Selectors observed (volatile — prefer roles/text over refs)

| Purpose | Locator |
| --- | --- |
| New project | `button` name *"add_2 New project"* |
| Prompt input | `textbox`, placeholder *"What do you want to create?"* |
| Submit | `button` name *"arrow_forward Create"* (enabled once text present) |
| Generated image (canvas) | `button "Generated image"` → child `img[alt="Generated image"]` |
| Image media id | `img.src` query param `name=<uuid>` |
| Sidebar: Characters | `button "accessibility_new Characters"` |
| Sidebar: Add Media | `button "add Add Media"` |
| Sidebar: Scenes | `button "movie View scenes"` |
| Completion signal | new assistant `paragraph` in session + `button "Generated image"` present |

Refs (`e123`) from `browser_snapshot` are per-snapshot and **go stale** — in the hardened
command, locate by ARIA role + accessible name/placeholder, not ref.

## Characters, re-mapped live 2026-08-11 (GPOM + MMT casting)

> A 2026-06-30 "Character consistency — SOLVED" recipe lived here (New Character card,
> `@` picker giving an `option` `"<Name> — Character"`). It's gone — the UI it described
> no longer exists (see below) and `flow_generate_image`/`flow_edit_image`/
> `flow_generate_batch` now take a `character` parameter that drives the current picker
> internally, so there is no browser-driving step left for a caller to do by hand. The
> one gotcha worth keeping from it: **plain `@Name` typed as prompt text does NOT bind
> the character** — it yields a generic likeness, not the cast one (camping-v2 p03: text
> → a generic financier; a real reference attachment → the actual Tarquin). Binding
> requires the reference-attachment flow, which is exactly what the `character`
> parameter now does under the hood — see the asset-picker recipe under "Reference
> images (ingredients)" below.

The character UI changed. What the 2026-06-30 recipe gets wrong, and the current map:

**There is no "New Character" card.** The sidebar **Characters** button now navigates
*straight* to the composer on a project with zero characters, so the old
`getByText('New Character')` click hangs for its full timeout and strands the page on
`/characters` — which then breaks the *next* call, because that route has no create bar.
Two fixes shipped in `flow-client.ts`: the dead click is gone, and every entry point now
goes through `ensureProjectRoot()`, which re-navigates to the bare `/project/<id>` when a
prior failure left the page on a sub-route.

**The name field is `getByRole('textbox', { name: 'Character Name' })`** — not
`input[placeholder="Character Name"]`; that selector matches nothing and was the second
half of the same failure.

**A Character has two view slots, Portrait and Body.** Uploading a reference fills only
the Portrait. The editor's **`Create Body`** button opens a second compose bar
("Describe body and outfit…." + the portrait as a chip); on completion the tab's label
flips `Create Body` → `Body`, which is the reliable done-signal. A portrait *and* a body
bind identity noticeably better than a portrait alone.

**Character Info** (`getByRole('textbox', { name: /Describe how your character/i })`) is a
free-text note Flow's own scene agent reads when the character is cast — worth filling so
prompts don't have to repeat it.

**Iterating on an existing character** is a first-class flow: select the Portrait or Body
tab, then use the editor's own *"What do you want to change?"* bar. Cheaper and more
faithful than re-casting from a new reference, and recoverable via **Show history**.

**Model picker — two layouts, and it RESETS on navigation.** The canvas has one trigger
concatenating model+aspect+count (`🍌 Nano Banana Pro crop_16_9 x2`) with the model
submenu nested inside its menu; the character editor has a bare
`🍌 <model> arrow_drop_down` trigger. Both default back to **Nano Banana 2** after
navigation, so the model is asserted **per generation**. Tiers: **Nano Banana Pro** >
Nano Banana 2 > Nano Banana 2 Lite. Beware: `Nano Banana 2` is a strict prefix of
`Nano Banana 2 Lite`, so a substring check silently generates on the wrong tier
(guarded by `modelAlreadySelected()` in `compose.ts`, with tests).

**Empty compose boxes report their placeholder in `textContent`,** and the placeholder
differs per surface. The submit-verification helper strips all of them
(`isBoxCleared()` in `compose.ts`) — otherwise a character-page submit never reads as
cleared and retries into a double submission.

**What does NOT work: asking for a multi-view character sheet in one shot.** A single
`flow_edit_image` call asking Flow to composite front/side/back turnarounds from one
portrait produced *nothing* — no candidate ever landed (consistent with a policy block or
a compositing limit; it is not merely slow). Use Portrait + native Create Body instead.

## Hardening — confirmed live 2026-06-30 (flow-script-hardening branch)

Live-validated `@badcode/flow-mcp` against camping-v2 (`/project/9b729074…`): `openProject`,
`generateImage`, `refine`, `generateBatch` all proven end-to-end with real harvested frames.
Key corrections to the spike-era selectors above:

- **Accessible names concatenate the Material-icon ligature with the label, with NO space.**
  `getByRole` matches the *accessible name*, so the submit button is `arrow_forwardCreate`
  (not `arrow_forward Create`) and the image tab is `imageImage`. Use `/arrow_forward\s*Create/i`,
  `/image\s*Image/i`, etc. — a literal space in the regex matches nothing. This was the hidden
  root cause that made the spike-era selectors untrustworthy.
- **Submit** = `getByRole('button', { name: /arrow_forward\s*Create/i })` (disabled until the box
  has text; a separate `add_2Create` button exists — the `arrow_forward` prefix disambiguates).
- **Prompt box** = `page.locator('div[role="textbox"][contenteditable="true"]').first()`, which has
  NO own placeholder text — the old `.filter({ hasText: /What do you want to create/i })` matched
  nothing. A sibling `<textarea>` also exposes the textbox role.
- **Image-mode menu**: open via `getByRole('button', { name: /crop_/ })` (the
  `🍌 Nano Banana 2 · crop_16_9 · 1x` config button). Tabs: `imageImage` / `play_circleVideo`;
  aspect `crop_16_916:9`, `crop_landscape4:3`, …; count `1x` / `x2` / `x3` / `x4`. Default is already
  Image · 16:9 · 1x, so `ensureImageMode` is idempotent.
- **Open an existing project**: tiles are `a[href*="/fx/tools/flow/project/"]` with EMPTY anchor
  text — the name is a sibling styled-components span with a HASHED class. Scrape by climbing each
  anchor to the nearest short own-text node (see `project.ts` `SCRAPE_PROJECTS`). The grid hydrates
  after `domcontentloaded`, so poll the scrape until the name appears.
- **Navigate gently**: reach a project by CLICKING its tile (`a[href="…"]`, SPA nav). A second hard
  `goto` (list → project) races hydration and tips the app into a client-side error boundary
  ("Application error: a client-side exception"). After landing, wait for the contenteditable prompt
  box before interacting.
- **Detect a NEW image, not "any image".** Each turn yields a fresh media UUID while the previous
  image stays on-canvas. Snapshot the media-name set BEFORE submit and wait for a name not in it
  (`waitForNewCanvas`), otherwise refine/batch turns harvest the stale previous frame.
- **Agent vs generation mode.** The create bar has an `Agent` toggle button (`aria-pressed`). When
  pressed (Agent/chat mode) the image config (`crop_…`) button is ABSENT, so `ensureImageMode` must
  check whether `crop_` is present and, if not, click the `Agent` toggle to drop into generation
  mode first. The mode is stateful and varies (e.g. it engages after the character flow), so gate
  on `crop_`'s presence, not on `aria-pressed` (which lags after navigation).
- **Create a character** (`createCharacter`): this original recipe (click a "New
  Character" card, fill `input[placeholder="Character Name"]`) is superseded by the
  2026-08-11 remap above — there is no such card, and that name-field selector matches
  nothing. Two facts from here still hold and aren't restated above: the "Character
  Name" field **defaults to "Untitled Character"** until filled, and `Done` **returns
  you to `/project/<id>`** — the reliable done-signal for the whole flow.
- **Cast a character into a generation**: the `role="option"` asset-picker entries this
  recipe originally relied on are dead — gone from the UI *and* the code. See "Reference
  images (ingredients)" below for the current Characters-tab flow.

## Reference images (ingredients) — mapped live 2026-07-14 (edit-panel spike)

The reference-image workflow ("Add" / ingredients) exists and works end-to-end. Proven
live: uploaded `gpom-short` p04 golden, applied a Google-template delta prompt at x2, got
2 edited candidates that honoured "keep everything else the same".

- **Attach a reference**: the create bar's `button "add_2 Create"` (`aria-haspopup="dialog"`)
  opens an **asset-picker dialog**: project dropdown (cross-project assets!), tabs
  `All / Images / Videos / Voices / Characters / Uploads`, a `button "upload Upload media"`
  (file chooser — `setFiles()` works), and a searchable asset grid. Pick/upload an asset →
  hover/select its tile → **"Add to Prompt"**.
- **The media chip lives OUTSIDE the contenteditable** — it renders as a sibling
  `button` whose `<img alt>` is *"A piece of media generated or uploaded by you, that is
  present in your collection."* with a `cancel` icon child to detach. Because it is outside
  the box, **`fill()` on the prompt box does NOT wipe it** (unlike character chips).
  Probe for it via the img alt, not textContent (the accessible name comes from the alt).
- **`@` now opens the SAME asset-picker dialog** — the old `role="option"`
  `"<Name>Character"` entries are GONE (UI update since 2026-06-30). To cast a character:
  open the picker (`@` or `add_2`), click the `Characters` tab, select the character tile,
  "Add to Prompt". The character chip is still INLINE in the contenteditable (` Name `),
  so once a character chip is present, APPEND text (`End` + type) — never `fill()`.
  `submitWithCharacter`'s option-based flow has since been ported to this picker
  (`addCharacterToPrompt` in `flow-client.ts`) — every `character` param on the
  `flow_*` tools goes through it now, so callers don't drive the picker by hand.
- **Composition confirmed**: a media ingredient chip + an inline character chip coexist
  in one prompt (tested in camping-v2 with an existing asset + SmokeChar).
- **Multi-output (x2/x3/x4)**: count tab selection in the `crop_` config menu **persists
  after Escape** (trigger label updates, e.g. `…crop_16_9x2`). An x2 generation yields
  2 fresh media UUIDs; observed arrival skew between the two candidates ≈ 9–15 s —
  use a ~20–30 s grace window after the first before declaring a partial result.
- **Harvest unchanged**: candidates resolve via `media.getMediaUrlRedirect?name=<uuid>`
  (full-res `image/jpeg`, ~770 KB at 16:9).
- **Uploads become project assets** (alt `"Generated image"` in the grid, original
  filename in the picker) — re-usable in later rounds without re-uploading; the picker
  hides assets already attached to the prompt.

### Click reliability on WSLg (2026-07-14, refined during the smoke hardening) — REQUIRED reading

Playwright's default actionability checks stall on this UI (elements never report
"stable" — persistent animation), and **coordinate-based input is untrustworthy on this
rig**: the WSLg window's input pipeline scales coordinates (`window.innerWidth` 3828 vs a
1538-px screenshot), so trusted CDP clicks and even `force:true` clicks can land on the
wrong element (observed: a force-click aimed at "Add to Prompt" hit "Upload media").
What works, per control type (all in-page via `locator.evaluate` — coordinate-free):

| Control | Working recipe |
| --- | --- |
| Plain buttons (Upload media, Add to Prompt, add_2 picker trigger) | native `el.click()` via `evaluate` |
| Submit (`arrow_forwardCreate`) | native `el.click()` **after waiting for it to enable** (it enables async after fill; clicks on the disabled button are silently swallowed) — then VERIFY the prompt box cleared, retry with focus+`Enter` if not |
| Radix menu trigger (`crop_` config) | synthetic `PointerEvent` sequence via `dispatchEvent` (`pointerdown`→`pointerup`→`click`); native click, focus+Enter and CDP mouse all failed |
| Radix tabs (Image / aspect / count) | `el.focus()` + `MouseEvent` sequence (`mousedown`→`mouseup`→`click`); bare `PointerEvent` dispatch did not select |

These stalls (5–30 s timeout-retry per click) are almost certainly the "Flow automation
is slow" experience — every hand-driven or locator-driven click paid them.

### More live corrections (2026-07-14 smoke hardening)

- **Never use `waitForEvent('filechooser')` + `setFiles`** — when a second Playwright
  client (e.g. the Playwright MCP) is attached to the same Chrome with chooser
  interception armed, the chooser hangs and the upload never lands. Instead set the
  page's persistent hidden input directly: `locator('input[type="file"][accept*="image"]')
  .setInputFiles(path)` — no dialog interaction at all.
  **Ported everywhere 2026-08-12** — it broke exactly as predicted, on a character cast,
  presenting as a `uploadImage` 400 plus a stranded modal rather than as a hang. All three
  upload sites (`attachReferences`, `createCharacter`, `generateVideo`) now go through one
  `uploadFiles(paths, reveal?)` helper. Its `reveal` callback is invoked **only if no file
  input is on the page yet**, because clicking "Upload" is itself what pops the chooser
  we are avoiding.
- **The asset picker has two layout variants**: a full-width dialog (button "Add to
  Prompt") and a compact popover (button "Add to **p**rompt", left rail + list + preview
  pane). Match buttons **case-insensitively and page-globally**, not scoped to
  `getByRole('dialog').last()`.
- **Submit verification is mandatory**: Flow clears the prompt box on a successful
  submit — poll for that instead of trusting the click.
- **KNOWN ISSUE — project tiles lost their `<a href>`**: the projects grid can render
  div-based tiles with no anchors (breaks `SCRAPE_PROJECTS`/`openProject` → spurious
  PROJECT_NOT_FOUND). Synthetic clicks on those tiles do NOT navigate. Workaround: a
  direct `goto` to the known `/project/<uuid>` URL (retry through the "Application
  error" boundary with a reload), or rely on the already-open project page
  (`flow_edit_image` needs no specific project — the uploaded reference anchors it).
- **Project rename via the title textbox could not be automated** (fill and keystrokes
  both revert on blur) — name projects at creation time, in the UI, by hand.

## Still to spike (before a full unattended comic run)

1. **Iterative correction** — how reliably a follow-up message fixes a weak frame.
3. **Aspect ratio control** — got 1376×768 (≈16:9) by asking for "landscape"; confirm how
   to pin a target ratio/size for the comic page model.
4. **Rate limits / session longevity** over a long batch.
