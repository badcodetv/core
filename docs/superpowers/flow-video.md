# Google Flow — image→video recipe (from the spike)

> Recorded 2026-06-25 from the first successful automated image→video generation.
> The **video** companion to [`flow-selectors.md`](./flow-selectors.md) (which covers images).
> This is the input contract the `animate-slide` skill drives. Playwright MCP attached over
> CDP to a WSLg Chromium logged into Flow (ULTRA plan).

## TL;DR — the loop that works

1. **Navigate** `https://labs.google/fx/tools/flow`; open/ensure a project
   (`button "add_2 New project"` → lands on `/fx/tools/flow/project/<uuid>`).
2. **Set video generation defaults** — agent panel `button "tune Settings"`:
   - **Video generation default** → model dropdown (`button "<model> arrow_drop_down"`) →
     pick **Veo 3.1 - Quality** (options: Omni Flash, Veo 3.1 Lite / Fast / Quality /
     Lite[Lower Priority]).
   - **Aspect**: `tab "crop_16_9 16:9"` (default) — matches the Karen comic page. Other:
     `9:16`. **This is how you pin aspect** — there is no per-prompt aspect control; it's the
     Video-generation-default tab. Count tabs `1x|x2|x3|x4` → **1x** for a single clip.
   - **Confirm before generating** is its own setting: `Always` (default) makes the agent ask
     before spending credits — a useful gate; `Never` is full-auto. **Save**.
   - ⚠️ **These defaults RESET per project** — a fresh project comes up as `Omni Flash`, so
     re-select **Veo 3.1 - Quality** every new project/session. (Aspect 16:9 / 1x persisted as
     defaults, but re-check them.)
3. **Upload the source image** — top bar `button "add Add Media"` → menuitem
   `"upload Upload media"` → a **file chooser** opens (`browser_file_upload`).
   - ⚠️ **The Playwright MCP sandboxes uploads to repo roots.** Files under `/tmp` are
     **denied** ("outside allowed roots"). Stage the source image **inside the repo** —
     e.g. `/home/kai/projects/badcode/badcode/.playwright-mcp/animate-slide/<img>` (that dir
     is git-ignored). Then upload that path.
   - Large sources (Karen's are ~5504×3072, 8 MB) upload fine but may flash a transient
     `warning Failed` / `99%` tile during thumbnail processing — it **recovers**; the image
     then appears as a media tile (`button "Generated image image <name>"`).
4. **Animate the image** — hover the uploaded tile → `button "more_vert More"` → menuitem
   **`"motion_blur Animate"`**. This attaches the image as the **source frame**: a media chip
   appears above the prompt box (`button "A piece of media generated or uploaded by you… cancel"`).
5. **Type the motion prompt** into the agent textbox (`role=textbox`, placeholder
   *"What do you want to create?"*). The `button "arrow_forward Create"` enables once text is present. Click it.
6. **Approve the credit gate** (when Confirm=Always): the agent posts *"Would you like me to
   kick off this 1 video generation, costing N credits?"* with `Approve` /
   `Approve, do not ask again` / `Reject`. Veo 3.1 Quality = **100 credits**. Click **Approve**.
7. **Wait — poll, never fixed-sleep.** Veo Quality can **queue** under load: *"Your video has
   been scheduled and is waiting in the queue due to high demand."* (a `warning Failed`-looking
   icon may show while queued — it is **not** a real failure). See "Completion signal" below.
   - ⚠️ **Genuine failure vs. queue.** A real failure reads *"Oops, something went wrong!"* and
     the agent **re-posts the Approve gate** — you must click **Approve again to retry** (Veo
     failures are often transient; the retry then queues normally). Distinguish it from the
     benign *"scheduled… waiting in the queue"* message (which just needs patience). On the
     second slide the first attempt failed this way and the retry succeeded. So the poll must
     watch for `Oops, something went wrong` and retry, not wait forever.
8. **Harvest the .mp4** — same signed-URL trick as images (see "Harvest").

## Completion signal (how to know it's done) — IMPORTANT

The generated clip is a `<video>` whose `src` is an authenticated redirect
`…/media.getMediaUrlRedirect?name=<UUID>` (a sibling `…&mediaUrlType=MEDIA_URL_TYPE_THUMBNAIL`
is the poster).

**Two tempting signals that DON'T work** (confirmed on the spike):
- ❌ `video.videoWidth` — the `<video>` element is **lazy**; it stays `0×0` long after the
  clip is actually ready (it only decodes when scrolled into view / played).
- ❌ the chat text ("waiting in the queue due to high demand") — that message **persists in
  the chat transcript** even after the clip finishes, so "is the queue text gone?" is a false negative.

**The signal that works:** the `<video>`/source `name` appears in the DOM as soon as the node
is created; **resolve its media URL and check the response** — when it returns `content-type:
video/mp4` with a real byte length, it's done. Poll via `browser_run_code_unsafe`:

```js
async (page) => {
  const name = await page.evaluate(() => {
    const el = [...document.querySelectorAll('video,source,img')]
      .map(e => e.currentSrc || e.src || '')
      .find(s => s.includes('getMediaUrlRedirect') && !s.includes('THUMBNAIL'));
    return el ? new URL(el).searchParams.get('name') : null;
  });
  if (!name) return { ready: false, reason: 'no media node yet' };
  const r = await page.request.get(
    'https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=' + name,
    { headers: { Range: 'bytes=0-0' } });
  const ct = r.headers()['content-type'] || '';
  return { ready: ct.startsWith('video/'), name, contentType: ct, size: r.headers()['content-range'] };
}
```

`ready: true` (content-type `video/mp4`) ⇒ harvest it. Poll every ~30–60 s; Veo Quality under
"high demand" took ~5 min on the spike. (Don't fixed-sleep a guessed duration — poll.)

## Harvest (the robust, scalable part — identical to images)

The `<video>` `src` redirect 302s to a signed CDN URL with the browser's cookies. In-page
`fetch` fails (CORS); the Playwright **request context** follows it server-side:

```js
async (page) => {
  const v = [...document.querySelectorAll('video')]
    .find(v => (v.currentSrc||v.src||'').includes('getMediaUrlRedirect'));
  const name = new URL(v.currentSrc||v.src).searchParams.get('name');
  const resp = await page.request.get(
    'https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=' + name);
  return { name, url: resp.url() };   // url = signed flow-content.google CDN URL
}
```

Then `curl "<signed url>" -o clip.mp4` from the shell (no `fs` in the run_code sandbox — it has
only `page`). Confirm `file clip.mp4` → `ISO Media, MP4`. **Same mechanism as `flow-selectors.md`,
just a `<video>` source instead of an `<img>`.**

## Selectors observed (volatile — prefer roles/text over snapshot refs)

| Purpose | Locator |
| --- | --- |
| New project | `button` name *"add_2 New project"* |
| Agent settings | `button "tune Settings"` (agent panel footer) |
| Video model dropdown | `button "<model name> arrow_drop_down"` under **Video generation default** |
| Video aspect | `tab "crop_16_9 16:9"` / `tab "crop_9_16 9:16"` (Video generation default) |
| Save settings | `button "Save"` |
| Add Media | top bar `button "add Add Media"` → menuitem `"upload Upload media"` |
| Uploaded tile | `button "Generated image image <filename>"` |
| Per-asset menu | hover tile → `button "more_vert More"` |
| **Animate (image→video)** | menuitem **`"motion_blur Animate"`** |
| Source-frame chip | `button "A piece of media generated or uploaded by you… cancel"` (above prompt) |
| Prompt input | `role=textbox`, placeholder *"What do you want to create?"* |
| Submit | `button "arrow_forward Create"` (enabled once text present) |
| Credit gate | agent message + `Approve` / `Approve, do not ask again` / `Reject` |
| Completion | a `<video>` with `getMediaUrlRedirect` src and `videoWidth > 0` |

`browser_snapshot` refs (`e123`) go stale between snapshots — locate by ARIA role + accessible
name, not ref.

## Corrections from live automation (2026-08-12)

The table above was written from a hand-driven session and several rows are wrong in ways that
made `ensureVideoSettings` a no-op or a 90-second hang. What the panel actually does:

- **⚠️ `getByRole` does not work anywhere inside the Agent settings panel.**
  `page.getByRole('tab')` counts **0** page-wide while `button[role="tab"]` counts **15** — the
  open panel sits under an `aria-hidden` ancestor, so it is absent from the accessibility tree
  Playwright queries. Use **CSS + text** for everything in this panel. `getByText` still works
  (different engine). This is the single most surprising fact here.
- **The Settings button lives in the Agent panel, which is closed by default.** On a project
  root there is no `tune Settings` button at all until the compose bar's `button "Agent"` is
  clicked. The panel is **sticky across navigation**, so code must handle three states: closed,
  open on the chat view, and already on the settings view.
- **Two sections share tab names.** "Image generation default" (16:9 / 4:3 / 1:1 / 3:4 / 9:16,
  x1–x4, Nano Banana) sits ABOVE "Video generation default" (16:9 / 9:16, x1–x4, Omni Flash).
  Any `.first()` lands on the image one. Scope via the heading's immediate parent —
  `getByText('Video generation default', {exact:true}).locator('xpath=..')` is exactly the
  video section and excludes the image one.
- **Count tabs are `x1`…`x4`.** The row above says `1x` for a single output; it is `x1`.
- **Model names carry a ` - ` separator**: `Omni Flash`, `Veo 3.1 - Lite`, `Veo 3.1 - Fast`,
  `Veo 3.1 - Quality`, `Veo 3.1 - Lite [Lower Priority]`. Note the **space** before
  `[Lower Priority]`, and that `Veo 3.1 - Lite` is a strict prefix of it — match names for
  equality, not containment.
- **Menu options are `button[role="menuitem"]` with the label in a nested `<span>`**, so the
  button's own text is not the bare name; match the label text exactly and walk up to the
  ancestor button.
- **The model trigger renders glued together**: `"Omni Flasharrow_drop_down"`, no space.
- **The trigger TOGGLES** — clicking it when the menu is already open closes it. Check whether
  the option is visible before clicking.
- **The settings panel REPLACES the prompt box.** Leaving it open makes the next submit fail
  with "element is not visible" on a textbox that exists but is off-screen. Saving does not
  close it; click the panel's own `arrow_back Back` (not the top-left `arrow_back Go Back`,
  which leaves the project).
- **A fresh project defaults to Omni Flash for video** — confirmed, as the original note said.

**Progress screenshots go in `.flow-screenshots/`.** `browser_take_screenshot` writes its
`filename` relative to the repo root, so always prefix it — e.g.
`filename: ".flow-screenshots/gen-progress.png"` — to keep these scratch captures out of the
repo root. That folder is git-ignored (only its `README.md` is committed); delete the PNGs
whenever.

## Confirmed on the first run (Karen i38 → anim/a12, 2026-06-25)

- **Clip spec:** Veo 3.1 Quality at 16:9 returned **1280×720, 24 fps, 8.0 s (192 frames),
  H.264 MP4, ~2.9 MB.** That feeds the scroll-scrubbed `AnimationWidget` cleanly (192 frames is
  plenty of scrub resolution); `assets-build` made 480p+720p renditions + a WebP poster.
- **Harvest:** the signed `flow-content.google/video/<uuid>?…Signature=…` URL `curl`s to disk
  with no cookies — identical to the image path.
- **Queue latency:** ~5 min under "high demand" for Quality.

## Hardening into `@badcode/flow-mcp` `generateVideo` (2026-06-30) — status

Re-validated the recipe against camping-v2 while folding it into `flow-client.ts`. **The
end-to-end image→video flow is PROVEN**: a clean run produced a real, harvestable
**1.96 MB MP4** (`ISO Media, MP4`) through the exact path below. Corrections + the one
remaining rough edge:

- **No-space accessible names** (same rule as `flow-selectors.md`): the recipe's spaced names
  don't match `getByRole`. Use `/add\s*Add Media/i`, menuitem `/upload\s*Upload media/i`,
  `/motion_blur\s*Animate/i`, submit `/arrow_forward\s*Create/i`.
- **Add Media is a menu**, not a direct chooser: `Add Media` → menuitem `Upload media` → file
  chooser. The chooser is handled by the Playwright *library* (`setFiles`) — no repo-root
  sandbox limit (unlike the MCP's `browser_file_upload`).
- **Animate switches the bar to Video mode** and attaches the source-frame chip (bar reads
  `Video · 8s · crop_16_9 · 1x`, Agent toggle off). No separate mode switch needed.
- **Completion scrape must include `<video>`/`<source>`** (the old code scraped `<img>` only, so
  it never saw the clip). Snapshot media names *before* submit and wait for a NEW name whose
  `content-type` is `video/*` (`scrapeMediaNames` + `waitForVideoClip`). Evaluate the scraper as
  `(${SCRAPE})()` — evaluating the bare function string returns the function, not the array.
- **Credit gate**: `approveCreditGateIfPresent` clicks `Approve` if Flow posts the confirmation;
  a genuine failure re-posts it (`Oops, something went wrong`) and the poll re-approves to retry.
- **The uploaded-still → Animate attach now targets the specific tile, not "any animatable
  tile"** (closed 2026-08-12, A7). The old `openAnimateMenu` hovered every `img[alt="Generated
  image"]` tile in the grid and accepted the first menu exposing Animate — the exact fragility
  this note used to flag: it timed out on re-runs once the project filled with test media, and
  had no guarantee the first Animate-capable tile was the one just uploaded. `generateVideo` now
  snapshots the tile list (`scrapeAnimateTiles`) BEFORE the upload and again after, and
  `chooseAnimateTarget` (`animate-target.ts`) diffs the two to find the ONE new media name; if
  that's ambiguous but the project holds exactly one tile total, it falls back to that sole tile
  (still safe — there's no other candidate it could be). Any other ambiguity fails closed
  (`ANIMATE_NOT_FOUND`) rather than guessing — a wrong pick here means silently animating a
  different still with no visible sign anything went wrong. `openAnimateMenu` then hovers that
  ONE identified tile (via a synthetic `pointerover`/`mouseover` dispatch, not coordinate-based
  `.hover()` — see `hoverElement` in `flow-client.ts`) instead of scanning. In real use the
  `animate-slide` skill drives this path on a freshly-generated single slide, which is also why
  the sole-tile fallback matters: that's the common case this bug is fixed for.

## Still to watch (over a longer batch)

1. **Queue latency** under "high demand" for Veo Quality — minutes. Fast/Lite models queue
   less; trade quality for latency on bulk runs.
2. **Aspect** is a global default, not per-prompt — set it once per session before generating.
3. **Rate limits / credit burn** (100 credits per Quality clip).
4. **Manifest path trap** (downstream of the harvest, in the skill): `npm run --workspace
   @badcode/cli -- assets-build -m <relative>` writes the manifest relative to `packages/cli/`.
   Pass an **absolute** `-m` path. See `.claude/skills/animate-slide/SKILL.md` step 6.
