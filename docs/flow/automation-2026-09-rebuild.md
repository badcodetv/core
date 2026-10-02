# The Flow rebuild — 2026-09-13

🔴 **Google rebuilt Flow.** It moved from `labs.google/fx/tools/flow` to **`flow.google.com`**
(the old address redirects) and the app was rewritten from React to Angular. Every selector in
[`automation-images.md`](./automation-images.md) and [`automation-video.md`](./automation-video.md)
describes the OLD app. Where they disagree with this file, **this file wins**.

It surfaced the same day we moved every browser channel to branded Chrome, which made it look like
the Chrome switch had broken Flow. **It had not** — the site changed underneath us.

Proof script: `packages/flow-mcp/src/smoke-rebuild.ts` (stages `status`, `image`, `edit`, `video`),
all run live 2026-09-13 on free tiers.

## What works again, and what does not yet

| Tool | State on the rebuild |
| --- | --- |
| `flow_status`, `flow_list_projects`, `flow_open_project`, `flow_create_project` | ✅ proven |
| `flow_generate_image` (incl. x2), `flow_edit_image` (local references), `flow_refine` | ✅ proven |
| `flow_generate_video` — start frame; start + end frame | ✅ proven (Veo 3.1 Lite [Lower Priority], 4s) |
| `flow_generate_batch` | 🟡 same primitives as generate_image, not run live |
| `flow_generate_video` — text only (no frames), `count` > 1 | 🟡 coded, not run live |
| characters (all six tools), `flow_list_media`, `flow_refine_video`, Scene Builder (`flow_scene_*`) | 🔴 not re-mapped — they throw `FLOW_REBUILD_UNMAPPED` at once instead of timing out |
| casting a character into an image or video | 🔴 not re-mapped |

## The facts that cost time

1. **The old media URL lies.** `…/fx/api/trpc/media.getMediaUrlRedirect?name=<id>` now returns the
   app's HTML **with a 200**. Anything still using it writes a web page to disk and calls it a JPEG.
2. **Media ids moved to `img[data-media-id]`.** The tile `src` is an opaque
   `flow.google.com/asb/<token>=s1600-rw` with no id in it. Video tiles carry **no id at all**.
3. **The tile src is a re-encode — never harvest it.** Measured on the same image: `=s0` gives the
   right pixel size at **half the bytes** (250 KB vs 523 KB). A video tile streams a **2.4 Mbps**
   transcode of a **4.2 Mbps** original. The original is `flow-content.google/<image|video>/<uuid>?Expires=…`
   (signed), and the only reliable way to get it is the tile's **More options → Download**, which
   is md5-identical to it. Generated media opens a size submenu: **"Original size"** only — 2K/4K
   and 1080p are upscales and 4K costs credits.
4. **A video's media id** comes from the signed `flow-content.google/video/<uuid>` request the
   Download makes; the tool captures it.
5. **Prompt box = ProseMirror with no role.** `fill('')` does **not** clear it (the text survived).
   Select-all + Backspace does.
6. **Compose bar controls:** `Settings trigger` (label `🍌 Nano Banana 2 crop_16_9 x2` or
   `Video · 720p · 8s crop_16_9 x1`), `Start generation`, `Add ingredients to the prompt box`,
   Agent chip (`aria-pressed` is reliable). The popover is `button[role="radio"]` toggles plus a
   `Select model family` menu. **The trigger label lags the popover** — poll it, don't read it once.
7. **🔴 The upload trap.** In the ingredient picker an upload shows as `Uploading<file>` while
   **Add to prompt stays enabled** — pressing it then attaches a *different* image, silently.
   Wait for the finished option and click it (that attaches and closes the picker).
8. **References sit in a strip above the text** (`flow-ingredient-chip`), so clearing the prompt
   leaves them; they do not survive a reload.
9. **A bare follow-up prompt no longer edits the last image** — it made an unrelated street.
   `flow_refine` now attaches the last harvested image as an ingredient first. It attaches the
   *last downloaded* candidate, so after an x2 turn that is candidate **b**, not your pick.
10. **Video frames:** Settings → Video → **Frames** shows `Start ⇄ End` slots. The frame picker
    ("Select a frame image") has **no upload button**: upload through the top bar's
    **Add media → Upload** first, then pick the file by name. A click in that picker sometimes
    previews (then Add to prompt commits) and sometimes commits at once — wait on the slot.

## Credits, as the popover shows them (2026-09-13)

| Model | Per clip |
| --- | --- |
| Nano Banana 2 image | 0 |
| Veo 3.1 - Lite [Lower Priority] | **0** (4s clip in ~65 s today) |
| Veo 3.1 - Lite | 5 |
| Omni 1.1 Flash | 7 (4s) · 12 (8s); has 360p/720p and 10s |
| Veo 3.1 - Fast | 10 |
| Veo 3.1 - Quality | 100 |

"Omni Flash" is now **"Omni 1.1 Flash"**; the old name still resolves.

## After changing flow-mcp

The MCP server runs the checkout's source but only reloads on restart — run `/mcp` and reconnect
`flow` before the new code is what the tools call.

## 2026-09-16 — two video-path regressions, both with a workaround

- **`VIDEO_MODEL_NOT_APPLIED` on the first call after a model change.** Seen three times in one
  session (fresh project → Veo Fast; Veo → Omni; Omni → Veo). Fails **before** submit, no credits.
  An identical immediate retry applied the model every time.
- 🔴 **`download.saveAs: ENOENT … /tmp/playwright-artifacts-*/<uuid>` — the clip IS rendered and
  billed, and Chrome saved it to `~/Downloads` under Flow's own title** (e.g.
  `Aerial_view_of_Hong_Kong_20260916132257.mp4`). Five in a row, any `outPath` (WSL scratch or
  `/mnt/d`). The same session's first video call (13:09) harvested normally. Workaround: after the
  error, take the newest matching file from `~/Downloads` by timestamp. **Do not re-run** — that
  bills again. Client fix owed in `flow-client.ts` (fall back to the downloads folder).

## 2026-09-29 — three findings from the GPOM downfall video pass (11 Veo 3.1 Fast clips)

- **`VIDEO_OPTION_UNAVAILABLE: Frames|Ingredients on Veo 3.1 - Fast` on the first video call in a
  fresh project.** Seen twice (once in Frames mode with a start image, once text-only in
  Ingredients mode). Fails before submit, no credits. **An identical immediate retry worked both
  times.** Same family as `VIDEO_MODEL_NOT_APPLIED` above; the popover is not ready on first open.
  Client fix owed: retry `ensureVideoConfigRebuilt` once before throwing.
- 🔴 **`UPLOAD_REFUSED` on a close-up photoreal face.** A still of one woman's face filling a third
  of the frame (GPOM `businesses-B1`) was refused as an upload twice (re-encoded and renamed the
  second time). `flow_edit_image` with the same still as the reference then **timed out** waiting
  for the picker option, because it is the same upload. Crowd shots with smaller faces uploaded
  fine in the same session. Cause not proven (the plate also had a child's drawing in it).
  **Workaround that worked:** text-to-video with the still's own prompt plus the motion. You lose
  the exact plate (a different woman), but the shot survives.
- `flow_generate_batch` `resume: true` does not skip finished prompts when `numOutputs > 1`: see
  law 22 in the flow-automation skill.

## 2026-09-14 — two more drifts, found on the first reference edit of the day

11. **A cookie-consent bar (`#glue-cookie-notification-bar-1`: Learn more / Agree / No thanks)
    covers the compose bar on a freshly signed-in profile** and intercepts every click, so
    `Settings trigger` times out at 30s while reporting the button "visible, enabled and stable".
    Dismiss it once per profile; it does not come back.
12. **The ingredient picker's upload control is now an icon button.** Its visible text is only the
    `upload` ligature; "Upload media" is in `aria-label`. The old `filter({ hasText: /Upload media/ })`
    waited the full 90s. `attachReferencesRebuilt` now matches
    `button[aria-label="Upload media"], button:has-text("Upload media")`. The picker also gained a
    category filter (`All ▾`) and a Search box.
13. **A failed reference edit can leave the ingredient picker OPEN**, and the next call's
    `Add ingredients` click is then intercepted by `flow-add-menu-asset-list` for 30s. Escape ×3
    clears it. ⬜ Owed: `attachReferencesRebuilt` should press Escape when `aria-expanded="true"`.
14. **Harvest can fail after a successful generation.** On `flow_edit_image`, the tile's
    `More options` button stayed hidden because the hover did not register (law 7, WSLg). The
    images were in the project the whole time. **Recovery that worked:** native `el.click()` on
    `flow-image-tile button[aria-label="More options"]`, then the menu items `Download` and
    `1K Original size`. This is the same menu, with `2K Upscaled` and `4K Upscaled` beneath them.
    ⬜ Owed: replace the hover with an in-page click in the harvest path.
15. **`ensureVideoConfigRebuilt` races the popover re-render.** On a project in Image mode, clicking
    `Video` redraws the popover, and the immediate `Frames` lookup counted 0 and threw
    `VIDEO_OPTION_UNAVAILABLE: Frames on Omni 1.1 Flash`. Nothing was spent. A retry worked, because
    the project was now already in Video mode. ⬜ Owed: wait for the Frames radio after picking Video.
16. **Video harvest has the same hover bug as stills, and its Download is different.** A video tile's
    `Download` opens a size list (`270p Animated GIF · 720p Original size · 1080p Upscaled · 4K
    Upscaled · 50 credits`) in the same menu. Arm `waitForEvent('download')` **before** clicking
    `Download`, then click `720p Original size`.
17. **The stale Omni end-frame guard.** `video-mode.ts` still refuses an `endImage` on the 10s-capable
    model ("Omni rejects a last frame", true of 1.0). Omni 1.1 has end frames (desktop Flow). ⬜ Owed:
    remove the guard, and batch it with 13–16 into ONE code change and ONE reconnect (skill law 23).

## 2026-09-28: the Camping mv2 26-clip run (Omni 1.1 Flash, Frames, 720p, 8s, x1)

18. **A projects page now opens with an agent side panel** (`flow-agent-panel`, "Hi Kai, what would you like to
    create?"). Its prompt box is `flow-creative-agent-prompt-box`, **not** `flow-prompt-box`, so
    `flow_create_project` timed out at 90 s waiting for the classic box. **Close the panel** (its `Close` button)
    and `flow-prompt-box` comes back. A "Flow is now on iOS" changelog modal (`Get started`) also opens once.
19. **The first upload in a profile raises a "Rights to use this image" dialog** (`Cancel` / `I agree`) behind a
    `cdk-overlay-backdrop`, which intercepts the Settings trigger for 30 s. Click `I agree` once.
20. 🔴 **`flow_generate_video` can no longer see its own finished clip.** It waits for `flow-video-tile img.thumbnail`.
    A finished tile now carries `img[src^="https://flow-content.google/image/"]` until it is hovered, then
    `video[src]` (sometimes `flow-content.google/video/<uuid>`, sometimes an `/asb/` transcode). The call ran until
    the MCP idle timeout (1816 s) with the clip sitting finished in the grid. ⬜ Owed: fix `videoTileKeys`.
21. 🔴 **The tile grid virtualises, so tile COUNT is not a completion signal.** Past ~8 tiles on screen, a new clip
    does not raise `flow-video-tile` count. Detect by **key**: the newest tile is index 0, and its media src (with
    `?` stripped) is not in the set captured before submit. A "Failed" card is also a new index-0 tile. Its text
    carries the reason.
22. **"We noticed some unusual activity" is transient.** Jack's rule: **a real page refresh, then retry after
    ~10 s**, and no pause between clips. It hit about 1 in 5 submissions. One clip (07) needed 6 tries; the rest
    cleared in 1–2. **Same rule for `FRAME_SLOT_NOT_FILLED`**, which tended to follow a refresh. Upload each plate
    once per project and reuse it; re-uploading on every retry piles up duplicates.
23. **A download that times out is not a failed generation.** Retry only the download (Escape, reload, `More
    options → Download → 720p Original size`). Never resubmit: the clip is already rendered and billed. That mistake
    nearly cost a second render of clip 18.
24. **Killing a runner mid-submit double-bills.** A clip submitted just before a kill still renders (clip 08: two
    copies, about 12 credits). Swap runners only between a `saved` line and the next `submitted` line.

The runner used (a scratch script, not committed) imported `FlowClient` from `packages/flow-mcp/src/flow-client.ts`
and called its private primitives: `reloadProject`, `uploadToProject`, `ensureVideoConfigRebuilt`,
`fillFrameSlotRebuilt`, `setPrompt` and `clickSubmit`. Items 20–21 are the parts to fold back into `flow-client.ts`.

## 2026-09-29: Characters on the rebuilt Flow, done by hand over CDP (world cast, 5 Characters)

The six MCP character tools still throw `FLOW_REBUILD_UNMAPPED`. This is the working path, driven in-page with
native `el.click()` (law 7), so it can be folded back into `flow-client.ts`.

25. **The map.**
    - Project sidebar **Characters** → `New character` goes to `/project/<id>/character`.
    - That page has a "Describe your character…" composer, plus **Upload** and **Add from project**.
    - Adding one image **creates the Character at once**. The URL becomes `/character/<uuid>`, the image is the
      **Portrait**, and the name is "Untitled character".
    - The **Edit name** button (aria-label) reveals `input[aria-label="Character name"]`: fill it and press Enter.
    - **Create body** swaps the stage to "Generate or add an image of your character", with the same Upload / Add
      from project. Adding one sets the **Body**, and the toast reads "Image added to character".
    - **Done** saves and leaves.
    - Character Info is `textarea[aria-label="Character personality"]`.
26. 🔴 **Clicking a picker row sometimes commits at once** (the picker closes and the Character is created), and
    sometimes only previews, when **Add media** is needed. The same as item 10. After clicking a row, check whether
    `button[role=option]` rows still exist before pressing Add media. Pressing it blind risks adding the wrong
    image.
27. 🔴 **Pick rows by filename, via the picker's "Search assets" box.**
    - The list virtualises, so a row that has scrolled away doesn't exist in the DOM.
    - Thumbnail `src` briefly carries the media uuid (`flow-content.google/image/<uuid>`) and then switches to an
      opaque `/asb/` token, so ids are not a reliable key.
    - Generated images get auto-titles ("Man standing for reference photo…") that collide. **Upload** the plates
      under distinctive filenames first (the picker's `Upload media` opens a native file chooser;
      `waitForEvent('filechooser')` worked with the MCP attached), then search by name.
28. 🔴 **Never launch a browser channel from a sandboxed shell.** The browser's downloads land in the sandbox's
    private `/tmp` (`/tmp/playwright-artifacts-*`). The MCP server can't see it, so every harvest fails with
    `download.saveAs: ENOENT … copyfile '/tmp/playwright-artifacts-…'` **after** the generation succeeded. Launch
    `browser-channel.sh up` unsandboxed, and write `outPath` to a folder that exists: the MCP does not `mkdir`, and
    a missing folder gives the same ENOENT.
    - Also: channel 1's profile carries whichever Google account last signed in (Kai's, 2026-09-29). A project on
      the other account returns `/404?reason=project`, not a login prompt.

## 2026-10-01 — 21:9 is not offered for images, and it fails before submit

`flow_generate_batch` with `aspect: "21:9"` on **Nano Banana Pro** returned
`FLOW_ERROR: ASPECT_UNAVAILABLE: 21:9` at once, with nothing generated (n=1, Jack's account,
project `cb27208c`). `16:9` and `4:3` worked in the same session on the same model; 4:3 came back
at 1200×896. The tool's own description already says only 16:9 and 4:3 are selector-confirmed.
Not tested: whether 21:9 exists on Nano Banana 2, or which of the other listed ratios do.

## 2026-10-02 — casting a Character into a still, by hand (n=1, Jack's account, project `cb27208c`)

`flow_generate_image({ character })` does **not** throw `FLOW_REBUILD_UNMAPPED`. It types `@`,
which opens the asset picker, and then times out after 30s on the prompt box because the picker's
`cdk-overlay-backdrop` intercepts the click. Failed twice the same way. It leaves the picker open.

What worked, in-page over CDP (scratch scripts in `scripts/flow/.tmp/`, not committed as tools):

29. **A just-created Character is missing from the picker until the project page is reloaded.**
    Before a reload the picker's Characters tab read "No assets found"; after one, "The Host /
    Character" was a row under **All**.
30. **Click the Character row (`[role=option]`), then "Add to prompt".** Here the row click only
    previewed, so Add to prompt was needed (item 26 still applies: check first). The bar then shows
    the thumbnail and a name tag.
31. **Type the prompt after the tag with `keyboard.insertText`, and submit with Enter.** A
    synthetic pointer/mouse sequence on the `arrow_forward` button did nothing; Enter in the
    prompt box submitted. Newlines were flattened to spaces first, untested whether a newline
    would submit early.
32. **Creating the Character:** `/project/<id>/character` → the **Upload** control fires a native
    file chooser (`waitForEvent('filechooser')` worked) → the URL becomes `/character/<uuid>` →
    **Edit name** → Enter → wait for the portrait's percentage to clear → **Done**. Done is found
    by `innerText === 'Done'`; a Playwright `hasText` locator on it timed out.
33. **A reference image and a Character can both be attached to one prompt.** Type `@`, add the
    image row, type `@` again, add the Character row, then the text. Six of six stills came back
    with the reference's room and people and the Character's face (Nano Banana 2, 4:3). The
    reference was uploaded once through the picker's **Upload media** (native file chooser) under
    a distinctive filename, and then appears as the top row under **All**, matched by filename.
34. **The hand route does not set model, aspect or count.** They stay at whatever the last
    ordinary tool call asserted, so make one `flow_generate_image` call with the wanted `aspect`
    first. A retry that ran after such a switch came out at the wrong shape.
35. **`@` sometimes fails to open the picker** (`[role=option]` never appears, four prompts in a
    row, cause not found). The same script worked on the next run, straight after an ordinary
    tool call had reset the prompt bar. Leftover `@` characters in the box are the suspect, untested.
36. **The whole run so far: 22 hand-cast stills, 22 with the Character recognisable.** Scratch
    scripts: `scripts/flow/.tmp/cast-batch.mjs` (Character only) and `cast-ref-batch.mjs`
    (reference plus Character). They save the newest gallery tile by fetching its `src`, which
    returned the full 1200×896 image as WebP.

## 21:9 workaround (belongs to the 2026-10-01 entry above)

**Workaround used:** generate at 16:9 and ask in the prompt for "a very wide 2.39:1 film frame,
with black bars above and below it, inside a 16:9 image". Whether the bars come back reliably is
not yet checked.
