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
| `flow_create_character`, `flow_character_body`, `flow_list_characters`, `flow_get_character`, `flow_character_info` | ✅ **re-mapped 2026-10-17** (items 63–72): 3 Characters made, read back, listed |
| casting a Character into a still (`flow_generate_image`, `flow_edit_image` with references, `flow_generate_batch`) | ✅ **re-mapped 2026-10-17**: image and image+reference casts proven; batch uses the same path, not run live |
| casting a Character into a video | 🔴 **the MCP path is broken in Frames mode** (item 75): no ingredient button. ✅ The `@` route works (item 76), in `scripts/gpom/second-half-video/run.mts`, not yet in the MCP |
| ~~characters (all six tools)~~, `flow_create_character_from_media`, `flow_edit_character`, `flow_list_media`, `flow_refine_video`, Scene Builder (`flow_scene_*`) | 🔴 not re-mapped — they throw `FLOW_REBUILD_UNMAPPED` at once instead of timing out |

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

## 2026-10-03 — giving a Character a Voice, by hand (n=4, Jack's account, project `cb27208c`)

37. **The control is on the Character page** (`/project/<id>/character/<uuid>`): a `Select a voice` button opens a
    dialog with a `Search assets` box, 30 preset rows (`button[role=option]`, the same names as AI Studio's voices), a
    Preview button, a 120-character **Sample dialogue** box, a **Customise performance** textarea and `Add to character`.
38. 🔴 **Any click on a preset row commits the bare preset at once** and closes the dialog, before the performance text
    can be typed. A synthetic pointer sequence and a native `click()` both did it. **Do not click the row.** Type the
    preset's name into `Search assets`: the list narrows to one row and that row is the selected one
    (`aria-selected="true"`).
39. **Typing a performance turns the preset into a custom voice.** A **Voice name** input appears (default
    "`<Preset>` custom") and `Add to character` becomes `Save new voice`. Saving takes a few seconds (an hourglass on
    Preview), then the dialog resets to the bare preset. The saved voice is a new row: search for its name, it is the
    single selected row, then `Add to character`.
40. **The page then shows the voice name, its performance text, a play button and `Remove`.** `Done` saves and leaves.
    Playwright `hasText` locators on these buttons miss (as item 32); find them by `innerText`.
41. Scratch scripts: `scripts/flow/.tmp/voice-full.mjs` (items 38 to 40 in one run), `ref-batch.mjs` (a reference
    image with no Character). Four of four voices attached. **Not tested:** the voice in a video, and whether the
    dropdown beside the search box (it read "mmt jack") scopes saved voices to the project.

## 2026-10-03 — a Character's Portrait and Body, and three traps (n=4, Jack's account, project `cb27208c`)

42. **Adding a Body:** on the Character page, `Create body` → the stage reads "Generate or add an image of your
    character" → **Upload** (native file chooser). The tab then reads `Body`.
43. **Replacing a Portrait:** `Portrait` tab → `button[aria-label="Delete image"]` → a dialog "Delete this image? This
    will remove the image from the character." → Delete → toast "Character image deleted", the tab reads
    `Create portrait` and the same Upload stage appears. The voice and the Character id survive. Do the Body first, so
    the Character is never without an image.
44. 🔴 **`button[aria-label="Delete"]` in the top bar deletes the whole Character.** A click matched on the bare text
    "Delete" hit it and opened "This character will be permanently deleted." It was cancelled; nothing was lost. Never
    match Delete by text: use the `Delete image` aria-label, and confirm only inside the dialog whose text names the
    thing being deleted. Scratch: `scripts/flow/.tmp/dialog.mjs`, `char-sheet.mjs`.
45. 🔴 **The scratch scripts' "newest tile" test (`img` wider than 200px) fails on 3:4 and 9:16 tiles**, which are
    under 200px wide in the grid. It saved an older landscape tile three times while the real images generated fine.
    `grab-row.mjs` saves the first N tiles in reading order with a 120px floor.
46. **The picker's `All` list stopped showing Characters once there were four** (and item 29 again: new ones need a
    reload). `cast-search-batch.mjs` types the Character's name into the picker's `Search assets` box.
47. **Frame shape by hand:** the settings trigger opens tabs `16:9 · 4:3 · 1:1 · 3:4 · 9:16`
    (`scripts/flow/.tmp/aspect.mjs`). 3:4 gave 896×1200. The 9:16 click was never made (the picker was open over it),
    so 9:16 is untested.
48. **A reference image and four Characters in one prompt works (n=1, 3 October 2026).** Five `@` chips: the room
    reference, then each Character found through `Search assets`. Nano Banana 2, 4:3, first time: all four faces and
    the Characters' own clothes came through, over the room from the reference, even though the reference showed two
    of the men in different clothes. The prompt said the people come from their Characters and the reference is for
    the room, furniture and light only. Scratch: `scripts/flow/.tmp/cast-many.mjs`. Four is the model's stated limit
    for character resemblance; five is untested.

## 2026-10-05 — three picker findings from the Money For Something v3 run (Jack's account, project `cb27208c`)

49. **Character rows dropped out of the "@" picker after a run of generations.** After thirteen hand-cast
    stills in a row, searching "The Host" returned only a generated image titled "The host sitting in
    armch…", and the picker's own Characters list read "No assets found". **A page reload brought the
    Character rows back.** `scripts/flow/.tmp/cast-many-v3.mjs` now reloads before every still and prefers
    the row that reads `<name> Character`. Same cure as item 29; n=1 here.
50. **The Start-frame picker could not find day-old uploads by name.** `fillFrameSlotRebuilt` threw
    `FRAME_SOURCE_NOT_FOUND` for `mfs-plate-s03b2.jpg` and four others uploaded the day before, eight times
    in a row, while the "@" picker's search still listed all of them. Plates uploaded in the same session
    were found, except one (`mfs-plate-v306.jpg`) that failed three times and then worked. Cause not found.
    **Workaround used:** upload the plate again under a new filename.
51. **Nothing larger than a 512 px thumbnail came back out of the picker.** The row's `img` is 512×382 for a
    1200×896 upload, and clicking the row commits it to the prompt and closes the picker, so there is no
    preview to read. The plates were rebuilt from frame 0 of clips made from them. **Keep the plates on
    disk**; the round 10 ones had lived only in a scratch folder.
52. **The compose bar was in Video mode at the start of the day** (left there by the last clip run), and
    the hand-cast route does not change it (item 34). `scripts/flow/.tmp/v3-mode.mjs` opens the settings
    popover and clicks a control by its text: `'^image Image$'`, then `'crop_landscape 4:3$'`. The label
    then read "Nano Banana 2 crop_landscape x1".

## 2026-10-06 — 21:9 is refused on Nano Banana 2 as well (n=1, project `64a6c82d`)

`flow_generate_image` with `model: "Nano Banana 2"`, `aspect: "21:9"` returned
`ASPECT_UNAVAILABLE: 21:9` before submit, nothing generated. The same call at `16:9` worked at
once (1376×768). This answers the "not tested" line in the 2026-10-01 entry. `flow_create_project`
also returned the timestamp name ("Oct 06 - 13:31") for a project asked to be called "bank robbery".

## 2026-10-06 — still harvest returned OLD media in a full project (n=2, project `64a6c82d`)

With about ninety images in the project, the sixth prompt of a `flow_generate_batch`
(`numOutputs: 2`, 3:4) returned **three** candidates at 1376×768 whose media ids were scene stills
made half an hour earlier. A single `flow_generate_image` retry of the same prompt then returned
two 896×1200 files whose ids were the previous prompt's portraits. No error either time. The same
prompt in a new empty project harvested correctly first time. This is skill law 19 (written for
video) showing on stills. **Tell: the returned `mediaId` or the pixel size matches something you
already have.** Compare ids before trusting a file, and start a new project well before ninety.

## 2026-10-06 — twelve Characters with bodies and voices in one run (project `63d22c4b`)

53. **Twelve of twelve Characters were created by script** (portrait upload, name, `Create body`,
    body upload, `Done`), and **twelve of twelve custom voices attached**, with no retries.
    Scripts: `scripts/flow/.tmp/br-make-chars.mjs` and `br-voices.mjs`, built from items 25, 32, 37
    to 40 and 42. The project was new and held only the portraits and bodies.
54. **`flow_edit_image` at `aspect: "9:16"` works** (768×1376, 12 of 12). Item 47 had it untested.
55. 🔴 **A generated photoreal portrait can be refused as an upload.** One of thirteen portraits
    never appeared in the ingredient picker (two tries, then a third after closing the picker),
    while the rest uploaded first time. It was the one face that looked like a real actor. The tool
    reports it as a 90 s wait on the picker option, and **leaves the picker open**, so the next
    call fails on `Add ingredients` (item 13). Clear it with Escape, then change the face.

56. 🔴 **2026-10-06: the by-hand cast route made a clip when a still was wanted.** After a video
    run the compose bar was in Video mode. `v3-mode.mjs` printed `=> null` for both clicks (its
    regexes no longer match) and the bar still read `Video · 720p · 8s crop_16_9 x1`.
    `cast-many-v3.mjs` then submitted, and Flow made an 8 s clip from the Characters and the text
    (about 12 credits). **Tells:** `null` from the mode script, and a saved "still" that is
    1280×720. **What worked:** one ordinary `flow_generate_image` call first, which asserts image
    mode (item 34 said this for aspect; it is the same cure for mode).
57. `scripts/bank-robbery/br-videos.mts` (a copy of the Camping re-cut runner) made 15 of 15 clips.
    `VIDEO_OPTION_UNAVAILABLE: Frames on Omni 1.1 Flash` came on the first call of each process
    and cleared on the built-in retry, as in the 2026-09-29 entry.

## 2026-10-07 — 39 cast stills in one run (project `63d22c4b`)

58. 🔴 **The by-hand cast script chose the wrong tab.** `cast-many-v3.mjs` takes the first page
    whose URL contains `flow.google.com`. With a second Flow tab open on the home page it took
    that one and timed out after two minutes waiting for the prompt box. `cast-many-v4.mjs` takes
    the page whose URL contains `flow.google.com/project/`. Check the tab before blaming the box.
59. **Item 56's fix held:** one ordinary `flow_generate_image` call (Nano Banana 2, 16:9, one
    output) was made first to put the bar back in image mode, and every by-hand cast after it made
    a still.
60. **39 of 39 stills, about 75 seconds each,** through `scripts/bank-robbery/br-stills-v3.mjs`,
    which calls the cast script once per shot, skips files already on disk and logs each result.
    Shots with no Character went through the same script with no names and worked.
61. 🔴 **Item 56 happened again (2026-10-07), with a worse symptom.** After a run of clips, a by-hand
    cast for a still ran with the bar in video mode. It made a clip, and the script then saved the newest
    tile's poster as the "still": a 1280×720 video frame with none of the cast in it. **Check a redone
    still's size: 1376×768 is a still, 1280×720 is a video frame.** The fix is the same: one ordinary
    still call first.
62. 🔴 **After the session restarted, the flow MCP server was on a different channel** (channel 3, port
    9224, on the "about" page) while the working, signed-in browser was still channel 1 on 9222. Every
    MCP call timed out. Scripts pinned with `FLOW_CDP_PORT=9222` kept working. `flow_status` shows the
    channel; read it before retrying.

## 2026-10-17 — Characters re-mapped into the MCP (project `0558b1d5`, GPOM)

The by-hand recipes above (items 25–53) are now in `flow-client.ts`: `createCharacterRebuilt`,
`addCharacterBodyRebuilt`, `listCharactersRebuilt`, `openCharacterPageRebuilt`, `saveCharacterView` and
`addCharacterToPromptRebuilt`. Proof: `packages/flow-mcp/src/smoke-characters-rebuilt.ts`. Made: **West
Country Bot** (portrait + body + info), **Kill Bot** (in one `create` call, end to end), **Cream Jumper
Woman** (portrait + body), **Green Jumper Man** (portrait only; see item 70). Cast: the bot into a still
from its Character alone, and into the L3 chair room with L3 as a reference (both on model, bunting and
beacon intact). Credits: uploads cost nothing; two Nano Banana 2 stills.

63. 🔴 **A Character page does not redraw after an upload.** The portrait lands server-side, but the stage
    still reads "Create portrait", and further uploads on that stale page send **no request at all**. A
    reload shows the Portrait. The code reloads until the tab appears (`reloadCharacterPageUntil`).
64. 🔴 **The name and the info note save only on `Done`.** A reload before Done lost both.
65. **A click straight after navigation is swallowed** while the page hydrates (here, `Create body`). The
    code clicks, waits for the stage's `upload Upload` control, and retries (`openCreateBodyStage`).
66. **The populated Characters view has no links.** Cards are `<flow-character-tile>` with
    `span.character-tile-name`, and no id anywhere in the DOM (the old `a[href*="/character/"]` scrape
    finds nothing). The id appears only in the URL after a tile is clicked, so listing clicks each tile.
    The view also shows a `New character` tile and a `Create my avatar` tile; neither is a
    `flow-character-tile`. `/project/<id>/characters` is a 404; the Characters view has no route of its own.
67. **An empty project still skips the view** and opens the New character composer at `/project/<id>/character`
    (law 14). Listing treats that as "no Characters".
68. **Uploads from the Bash sandbox's `/tmp` never land** (item 28 again, for uploads): Chrome cannot see
    the file. The MCP server is not sandboxed, so this only bites smoke scripts. Stage test files under the repo.
69. **A small image is silently ignored** (n=1): a 175×538 body crop never appeared; the same crop upscaled
    to 525×1614 landed. The code refuses images whose short side is under 400 px, with a clear error.
70. 🔴 **Flow can refuse an upload server-side, and the page shows nothing.** The only trace is the `maseQ`
    RPC answering `["wrb.fr","maseQ",null,null,null,[3],…]`. It happened on a photoreal man's body crop,
    twice (item 55 again). The code watches for that response and throws `CHARACTER_UPLOAD_REFUSED`.
71. **Casting uses the ingredient picker's `Search assets` box** and the row reading `<name> Character`, after
    a project reload (items 29, 46, 49). Because a reload resets the model (law 15), the reload comes before
    `ensureImageMode`; in a batch it happens before every prompt. Rebuilt chips sit above the editor, so the
    prompt is set with `setPrompt`, not appended.
72. **`tsx` breaks named helper functions inside `page.evaluate`** (`ReferenceError: __name is not
    defined`). Write the expressions inline.
73. The default image model on the Character page now reads **"Nano Banana 2.1"** (seen 2026-10-17;
    not yet checked on the main compose bar).
74. 🔴 **The full-project trap hit Character casts (2026-10-17, project `0558b1d5`, ~200 images).** Of 13 recast
    edits, three came back wrong: two returned the Character's own portrait scene, not the shot asked for,
    and one returned **six** "candidates" whose ids matched three earlier outputs (old media harvested as new).
    The same three prompts in a **fresh project** (`be451638`, with the Character re-created there in one
    `flow_create_character` call) came back right first time. One recast was policy-blocked, and its twin with
    identical wording passed. **Cast in a small project; recreate the Character there. It costs nothing.**

## 2026-10-17 — casting a Character into a Frames-mode video (project `be451638`, GPOM second half)

75. 🔴 **`flow_generate_video({ startImage, character })` cannot cast in Frames mode.** With a Start frame
    filled, the compose bar's buttons are `Image ingredient · Swap first and last frames · End · Clear prompt ·
    Agent · Settings trigger · Start generation`. There is no `Add ingredients to the prompt box`, so
    `addCharacterToPromptRebuilt` times out on its click (30 s) and nothing is cast. Seen in a probe that
    spent nothing (`scripts/gpom/second-half-video/probe-cast.mts`) and in one live submit, which went on uncast.
76. ✅ **The `@` route casts with the Start frame locked (n=1 probe, then a live run).** Click the prompt box, type
    `@`, click the row reading `<name> Character` (synthetic pointer sequence), then `Add to prompt`. The tag
    lands **inline in the prompt box** (its text reads `West Country Bot `), not as a chip, so the motion text is
    typed **after** it with `keyboard.insertText`. `setPrompt` select-all-deletes the tag. The Start frame stayed in
    its slot. ⬜ Owed: move this into `generateVideoRebuilt` and `submitVideo` in place of the ingredient picker.
77. **A cast does not stop Omni re-staging a subject the prompt contradicts (n=2).** Frame 15's plate has the bot
    already inside the bunker; the prompt said it "rolls forward out of the smoke through the open blast doors".
    Uncast and cast takes did the same thing: within half a second the bot was back at the doors, smaller, and
    then crept forward. The two takes are near-identical, so the cast changed nothing visible. The fix is the
    prompt: describe a move that starts from where the plate has the subject.

## 2026-10-19 — the image model menu changed, and a failed model pick wedges the next call (project `be451638`)

78. 🔴 **`model: "Nano Banana 2"` no longer exists.** The image menu now lists **Nano Banana Pro · Nano Banana 2
    Lite · Nano Banana 2.1**, and `flow_edit_image({ model: "Nano Banana 2" })` fails in 10 s waiting for the
    menu item. Nothing is spent. Use `"Nano Banana 2.1"`, or omit `model` (Pro).
79. **Nano Banana Pro x2 read "Generating will use 0 credits"** in the popover (Kai's account). The
    `platform-controls.md` §2 figure (~12 credits) is third-party and was wrong here, at least today.
80. 🔴 **A failed model pick leaves the Settings popover open, and its `settings-menu-backdrop` then intercepts
    the next call's aspect and count clicks** (30 s timeouts on radios that are already `aria-checked`). It
    cleared once a call ran whose config already matched the trigger label (the short-circuit skips the
    clicks). ⬜ Owed: `ensureImageModeRebuilt` should `dismissOverlay()` first, and click toggles with a native
    `el.click()` (law 7).
81. **`run.mts` against the MCP's own channel worked (n=4).** With `FLOW_CDP_PORT` set to the port that
    `flow_status` reports, and no MCP call in flight, the cut-2 runner made 4 Omni clips in one wave, all
    first-frame matched. `MAX_WAVES=1` stops it resubmitting (and paying again) if a harvest misses.

## 2026-10-19: Karen ending, video harvest

- 🔴 **`flow_generate_video` timed out waiting for its own tile twice in a row** (`locator('flow-video-tile').filter({ has:
  img[src=…] })`, 30 s), the item-20 fault again, on a chained start frame. Both runs had **finished**: the grid showed four
  "Man speaking on phone" clips. Harvest by hand: `node scripts/flow/.tmp/grab-videos.mjs <port> <n> <prefix>` hovers the newest
  `n` video tiles, reads each `<video src>` and fetches it in-page (2 of 2 came back as 1280×720 8 s mp4 with audio; the third
  tile's fetch threw). Retrying the generation spends credits again; look at the grid first.
- The `VIDEO_OPTION_UNAVAILABLE: Frames on Omni 1.1 Flash` first-call glitch hit on 3 of 3 fresh projects; an identical
  immediate retry worked every time.

## 2026-10-20 — reading the price and the balance; a harvest false positive (GPOM cut 3, `run-cut3.mts`)

82. **The price is on the page before Create.** With the Settings popover open, `flow-credit-cost-label` reads
    *"Generating will use N credits"* for the configured turn. Omni 1.1 Flash, 720p, Frames: **8 s x1 = 12, 8 s x2 = 24,
    6 s x2 = 20** (Jack's account). The **balance** is in the account menu (`button[aria-label^="Google Account"]` →
    *"18,844 Google Flow credits"*); it fell by exactly the label's figure per turn. `run-cut3.mts` reads both, refuses
    over a per-clip ceiling or a batch cap, and keeps a ledger. The balance read right after connecting often returns
    nothing (menu not ready); the read after the harvest is reliable.
83. 🔴 **"A new key at the top of the grid" is not proof the new clip finished.** The previous job's tile had not
    loaded its key into the `before` snapshot, so it counted as new, the wait ended at once, and the harvest
    downloaded the previous clip again (caught only by md5). Wait until **no** top tile is pending (a percentage, or
    no media key), after a 30 s floor, and skip any tile already harvested or any file whose md5 is already on disk.
