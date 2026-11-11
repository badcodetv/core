# Releasing a BadCode Short: Premiere to YouTube

How a short made with `new-short` goes from its timeline page to a YouTube Short. Researched 2026-11-11 for
*The Rules* (Kai: *"when we make shorts, we're going to repeat the process we're going through now"*).
Labels: **(official)** = Google or Adobe page; **(secondary)** = reputable third party; **(hearsay)** = vendor blog
or forum; **(repo)** = our own notes. Re-cutting the existing films into shorts is a different job:
[`shorts-factory.md`](./shorts-factory.md).

## 1. Premiere: the project and a portrait sequence

- **One project per short:** `<short's media folder>\<slug>.prproj`. For example,
  `D:\badcode-videos\shorts\the-rules\the-rules.prproj` is opened with `premiere_open_project({ path })`, which
  creates the file when it is missing. Clips are imported from the short's `video\` folder, and music from `music\`.
- 🔴 **Don't use the built-in portrait preset for a 24 fps short.** Premiere 2026 ships
  `Settings/SequencePresets/Social/Social Media Portrait 9x16 30 fps.sqpreset`, which runs at **30 fps only**.
  Omni clips are 24 fps, so 30 fps duplicates frames and the motion judders.
- ✅ **Make the sequence from a slug** (the trick already used for 24 fps 16:9 in `docs/premiere/api-notes.md`,
  2026-10-17):
  1. Render a 1-second black clip with ffmpeg:
     `ffmpeg -f lavfi -i color=c=black:s=1080x1920:r=24:d=1 -c:v libx264 -pix_fmt yuv420p slug-1080x1920-24.mp4`.
  2. Import it.
  3. Run `premiere_create_sequence({ name, fromItems: [<slug id>] })`.
  4. Read the sequence back and check it says 1080×1920, `frameRate: 24`, square pixels.
  5. Then lay the cut on top.

  Adobe confirms that a sequence takes the first clip's settings, and that Sequence Settings can fix it if needed
  **(official)** https://www.adobe.com/creativecloud/video/discover/vertical-videos.html
- **Sequence name:** `short-<slug>-1-<scene>-r<N>`, the timeline page's `sequence`. The page drives it, round by
  round (scene-timeline, "No split brain").
- **Clips are 720×1280** (Flow's Omni output). Scale them to 1080×1920 in the sequence (Scale to Frame Size or
  150%), or use the ffmpeg-upscaled `cut/r<N>-v*.mp4` files.
- **Safe margins:** in the Program Monitor, click the wrench, then Safe Margins. The default title-safe area is
  20%, about 216 px at the sides and 384 px top and bottom **(official)**
  https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/view-safe-zones-in-the-monitors.html.
  Premiere has no Shorts or TikTok UI overlay, so a PNG guide on the top track, switched off before export, does that job.
- **A 16:9 version**, if ever wanted: Sequence → Auto Reframe Sequence **(official)**. Check its frame size
  afterwards, because a forum report got 607×1080 **(hearsay)**.

## 2. Text on screen: the safe box

No platform publishes official pixel numbers for organic posts, and the vendor guides disagree **(hearsay)**.
For one box that clears YouTube, TikTok and Reels on 1080×1920:

| Keep text inside | x 60–930, y 270–1500 |
| --- | --- |
| Why | top ~270 px (status and search bar), right ~150 px (like/comment buttons), bottom ~420 px (title, channel, music line) |

Reels captions can reach about 672 px from the bottom **(hearsay, from Meta's ad guidance)**. Our older rule of
"bottom 350, right 150" (repo, shorts-factory §3) is inside this box. Before trusting the box, upload one test
privately to each app.

## 3. Export

- **H.264, MP4, 1080×1920, 24 fps, square pixels, Rec.709 SDR, progressive, 4:2:0.** Use the "Match Source –
  High bitrate" preset (or the YouTube 1080p preset with Match Source ticked, so it keeps the portrait frame).
  Use VBR 2-pass at 12–16 Mbps; YouTube's own floor for 1080p SDR at 24 fps is 8 Mbps **(official)**
  https://support.google.com/youtube/answer/1722171. Turn on Use Maximum Render Quality.
- **Audio:** AAC-LC, 48 kHz, stereo, 320–384 kbps **(official)**. YouTube publishes no loudness target. Ours is
  −14 LUFS with true peak below −1 dBFS **(repo)**, set with Loudness Normalization on the export's Effects tab.
- **Grain and flying paper** suffer in YouTube's re-encode, so export once, at a high bitrate **(my reading)**.
- 🔴 **Before upload:** run `scripts/delivery-qc.sh RENDER.mp4 shorts` (docs/video-fx/delivery.md). Burnt-in text
  can give a false luma FAIL (shorts-factory §2).

## 4. Upload as a Short

- **YouTube counts it as a Short when** it is square or vertical and **up to 3 minutes** long, on a standard channel
  for uploads since 15 Oct 2024. `#Shorts` is **not** needed. A 16:9 video, or 16:9 with black side bars, is long-form
  **(official)** https://support.google.com/youtube/answer/15424877.
- **Over 60 s,** any active copyright claim blocks the Short worldwide. Under 60 s, nothing changes **(official)**.
  Suno music is ours, but a false Content ID claim is possible, so stay under 60 s where the cut allows.
- **Length that performs:** 30–60 s **(repo, shorts-factory §4)**. Length is still the joke, so cut the fat.
- **Steps:**
  1. Choose the vertical file.
  2. Give it a title (100 characters at most).
  3. Write the description.
  4. Set privacy, or schedule it (the normal Studio option).
  5. Answer made-for-kids: **No**.

  **(official)** https://support.google.com/youtube/answer/10059070
- 🔴 **AI disclosure: tick "altered or synthetic content".** It is needed for realistic AI scenes and for **AI-generated
  music**, which is the page's own example **(official)** https://support.google.com/youtube/answer/14328491. Our Suno
  track alone triggers it, and the Flow footage is photoreal. That matches `docs/using-ai.md`.
- **Cover frame:**
  - Pick a frame in the mobile app, either before posting or later through Edit **(secondary)**.
  - Custom thumbnail upload for Shorts in desktop Studio is rolling out unevenly **(secondary, conflicting)**.
  - The sure way is to make the **first frame** a good cover.
- **Related video:** in Studio on desktop, the Short's Details tab can link **one** video on the channel. Set it by
  hand, because the API can't **(secondary)**.
- **Then:** hand the cut to `chief-of-staff` (caption by `marketing-producer`, check by `marketing-gatekeeper`, post
  logged), and mark the short DONE on the list.

## Open

- **Not found:** official safe-zone numbers for YouTube, TikTok and Reels; Adobe's export help page (403); whether our
  account has custom Shorts thumbnails today.
- **TikTok and Reels** take the same file but re-encode it again. Their own specs aren't researched here.
