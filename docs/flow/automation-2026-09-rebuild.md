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
