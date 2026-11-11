# Releasing a BadCode Short: one master, three platforms

How a short made with `new-short` goes from its timeline page to **YouTube Shorts, TikTok and Instagram Reels**
(Facebook Reels too, from Instagram). Researched 2026-11-11 on *The Rules* (Kai: *"we want to release across all of
the media platforms once we make something like this… we do need to get into shape with it"*).

Each claim is labelled by its source:
- **(official)**: Google or Adobe page.
- **(secondary)**: news or a well-known vendor.
- **(hearsay)**: vendor blogs that disagree with each other.
- **(repo)**: our own notes.

TikTok's and Meta's help centres could not be read by our tools, so **every TikTok and Instagram number here is
secondary or hearsay until we do one private test upload per app.** Re-cutting the existing films into shorts is a
different job, covered in [`shorts-factory.md`](./shorts-factory.md). **What makes shorts grow a channel, the funnel to the films, site and email list, and the set-up checklist: [`shorts-growth.md`](./shorts-growth.md).**

## The route

```
timeline page (noted, rounds)  →  Premiere: sequence from our 24 fps portrait preset, Kai's hand edit, text inside the safe box
  →  ONE master: H.264 MP4 1080×1920 24 fps  →  scripts/delivery-qc.sh master.mp4 shorts
  →  upload the SAME clean file natively to YouTube, TikTok, Instagram  (never a downloaded, watermarked copy)
  →  per platform: title or caption, AI-content toggle ON, cover frame  →  chief-of-staff logs it, list says DONE
```

One master works everywhere. What changes per platform is only the words, the AI toggle, the cover, and where you
upload from.

## 1. Premiere

- **Project:** one per short, at `<short's media folder>\<slug>.prproj`. For example,
  `D:\badcode-videos\shorts\the-rules\the-rules.prproj` (open it with `premiere_open_project({ path })`, which
  creates it if missing). Clips come from `video\` and music from `music\`.
- **Sequence:** use our preset **"BadCode Short 9x16 24 fps"**
  ([`docs/premiere/presets/`](../premiere/presets/)).
  - It is Premiere's own "Social Media Portrait 9x16" (1080×1920, square pixels, Rec.709) with the frame rate changed
    from 30 to 24, because Flow's Omni clips are 24 fps and a 30 fps sequence judders them.
  - Install it once per machine by copying it to
    `Documents\Adobe\Premiere Pro\<version>\Profile-<user>\Settings\Custom\`. It then shows under **Custom** in
    New Sequence.
  - From code, call `premiere_create_sequence({ name, preset: "<that file>" })`, then read the sequence back:
    1080×1920, `frameRate: 24`.
  - ✅ Proven 2026-11-11 on The Rules: the sequence read back 1080×1920, `frameRate: 24`, timebase 10584000000.
- **Name:** `short-<slug>-1-<scene>-r<N>`, the same name the timeline page uses. The page and Premiere move together
  (scene-timeline, "No split brain").
- **Clips are 720×1280**, which is what Omni makes. Set Motion → Scale to **150** on every clip, or the picture sits small in the middle of a white frame. The Rules build does this in one eval.
- **Build it from the timeline page's edl:**
  1. `scripts/scene/premiere-plan.py <edl> <plan> --tag rN --seq <name>` writes the placement script.
  2. Video goes on V1 as silent copies (`-noaudio.mp4`), using the original Flow clips from frame 0 so there is spare footage for trims.
  3. Music goes on A1. A drop is placed as the whole take, so Kai can slide it to the real drop point.
  4. Read the sequence back; snap rounding gaps of one frame.
  - Worked example: `short-the-rules` `scene.json` → `premiere.r2`.
  - `premiere-check.py` needs a story `timelines.json`, which a short doesn't have yet, so compare by reading the sequence back.
- **Guides:** turn on the Program Monitor's wrench → Safe Margins **(official)**. For the real platform box (§3), put
  a PNG guide on the top track and switch it off before export.

## 2. The master file

| Setting | Value | Why |
| --- | --- | --- |
| Container, codec | MP4, H.264 High, progressive, 4:2:0 | YouTube's spec **(official)**; TikTok and Reels take the same **(hearsay)** |
| Size, rate | 1080×1920, 24 fps, square pixels | YouTube: "upload at the frame rate you recorded" **(official)**. No source says TikTok or Reels reject 24 fps |
| Colour | Rec.709 SDR | **(official)**; our range trap: `delivery.md` |
| Bitrate | VBR 2-pass, about 12 Mbps (YouTube's floor is 8) | High enough for grain and flying paper. A 60 s file stays under ~90 MB |
| Audio | AAC-LC 48 kHz stereo, 320 kbps; −14 LUFS, true peak below −1 dBFS | **(official)** format; the loudness is our house rule **(repo)** |
| Premiere preset | H.264 "Match Source – High bitrate", Maximum Render Quality on | Keeps the portrait frame |
| Gate | `scripts/delivery-qc.sh master.mp4 shorts` | Burnt-in text can give a false luma FAIL (shorts-factory §2) |
| Colour tags | Premiere leaves them off: add BT.709 / limited with `-c copy -bsf:v h264_metadata=…` (new-short, "the handover") | No re-encode. The Rules (2026-11-11): Match Source came out at 17 Mbps, fine; after tagging the QC still said "content is full range" because the 150% upscale rings thin edges to 0 and 250. YLOW/YHIGH sat at 27–223, so it was a false alarm, and its "fix" would have washed the picture out |

Export once. Every platform re-encodes the file, so the master is the only clean copy. Keep it under
`<media>/renders/`.

## 3. Where text and the subject may sit (1080×1920)

No platform publishes numbers for normal posts. These come from Meta's ad guidance as quoted by vendors **(hearsay)**,
cross-checked against YouTube and TikTok guides:

| Zone | Box | For |
| --- | --- | --- |
| **Text safe** (all three apps' buttons and captions clear) | **x 65–930, y 270–1250** | Burnt-in words, the tax line, anything that must be read |
| **Grid safe** (Instagram's profile grid shows Reels cropped to 3:4) | **y 240–1680** | The subject of the cover frame |
| Covered by app UI | top ~270 px · right ~150 px · bottom ~670 px (Reels), ~420 px (YouTube) | Nothing important here |

Bottom 670 px is Reels' strict figure. If Reels doesn't matter for a piece, y up to ~1500 is clear on YouTube.
Settle it with one private test upload per app.

## 4. Per platform

**Everywhere:**
- Upload the clean master **natively** to each app, not a downloaded, watermarked copy. Instagram has penalised
  watermarked reposts since 2021–22, and in 2026 it widened its originality checks **(secondary)**.
- 🔴 Turn the AI-content label **on**. Our footage is photoreal AI, and the music is AI-generated, which is YouTube's
  own example of what needs it.

### YouTube Shorts (YouTube Studio)
- **It's a Short** when it's vertical or square and **up to 3 minutes**. `#Shorts` isn't needed. 16:9, or 16:9 with
  black side bars, is long-form **(official)** https://support.google.com/youtube/answer/15424877
- 🔴 **Over 60 s, any copyright claim blocks the Short worldwide** **(official)**. Suno music is ours, but a false
  Content ID claim can happen. Stay under 60 s, which is also the 30–60 s band that performs **(repo)**.
- **Steps:**
  1. Title, 100 characters at most.
  2. Description.
  3. Not made for kids.
  4. "Altered or synthetic content": **Yes** **(official)** https://support.google.com/youtube/answer/14328491
  5. Schedule in Studio.
- **Cover:** pick the frame in the phone app. Custom upload for Shorts is rolling out unevenly **(secondary)**. The sure
  way is to make the first frame a good cover.
- **Related video:** in Studio on desktop, the Short's Details tab links **one** video on the channel. Set it by hand,
  because the API can't **(secondary)**.

### TikTok (TikTok Studio on the web)
- **Upload from the web, not the phone.** The phone caps file size (about 72 MB on Android) **(hearsay)**. The web
  takes about 500 MB. On the phone, the "Upload HD" switch under More options is **off by default**
  **(secondary, Adweek)**.
- **AI label:** turn on TikTok's AI-generated content toggle. Unlabelled realistic AI content can be removed. TikTok
  also auto-labels files carrying C2PA content credentials **(secondary)**.
- **Music:** TikTok Studio has an optional music copyright check before posting **(hearsay)**. Our Suno music
  imitates no real artist, which TikTok's 2026 terms bar **(hearsay)**.
- **Not settled:** whether our track becomes a reusable "original sound", whether to register it through a
  distributor first, caption limits and how far ahead you can schedule.

### Instagram Reels (app, or Meta Business Suite to schedule)
- **Quality:** Profile → menu → Your app and media → Media quality → **Upload at highest quality** **(hearsay)**.
  Set it once on the phone that posts.
- **Grid:** the profile shows Reels cropped to **3:4** (1080×1440), losing 240 px top and bottom **(hearsay)**.
  Choose a cover frame whose subject sits in y 240–1680.
- **AI label:** add "AI info" when posting. Meta also detects C2PA, IPTC or watermark signals, but admits video
  detection is weaker **(secondary)**.
- **Facebook Reels:** Instagram can share the Reel to the linked Facebook page. Not yet checked for our accounts.
- Accounts and handles: [`social-media-accounts.md`](./social-media-accounts.md).

## 5. Owed before the first release

1. **Test upload:** one **private** test upload of The Rules' master to each app. Check the frame isn't letterboxed,
   it plays at full quality, where the UI sits over the text box, and what the grid crop looks like. Then correct §3.
2. **Preset:** open the preset in Premiere once and confirm it reads 1080×1920 at 24 fps.
3. **Suno terms:** check that our Suno plan's terms cover posting to TikTok and Instagram, and decide whether music
   goes through a distributor.
4. **Posting tool:** pick one that schedules all three. YouTube Studio, TikTok Studio and Meta Business Suite each
   do their own, free. A paid tool such as Buffer or Later is not researched.
5. **The Rules' tax-haven line:** its fact check is still owed before any text goes on screen.
