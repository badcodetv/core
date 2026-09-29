# The Shorts Factory

**Status:** v1, 2026-09-18. The production half of
[`short-form-funnel.md`](./short-form-funnel.md) — that file decided *rinse the cores
continuously*; this one says **which frames, which words, which knobs, and in what order.**
Channel mechanics live in [`platform-playbooks.md`](./platform-playbooks.md); who we are
aiming at is [`the-reader.md`](./the-reader.md) and it still gates every line.

> **TL;DR** — there are ~26 minutes of finished BadCode film on the drive and none of it has
> ever been sliced. It yields **40–60 shorts with no new creative work**. Every one of them
> must be colour-fixed on the way out (§2) or it ships with crushed shadows. The tool is
> [`scripts/shorts/cut.sh`](../../scripts/shorts/cut.sh); the first 20 cuts are listed with
> real timestamps in §7.

---

> **⚠️ §4 refreshed 2026-09-21** — the ranking basis is now reported as **watch time, not
> swipe-away**, the very short tier is reported to be collapsing (**30–45s** is the band), and
> Shorts reportedly added an **original-sound bonus** in March 2026. All three are ◻ practitioner
> claims and all three change what we cut. See
> [`shorts-karen-camping.md`](./shorts-karen-camping.md) §2. The production half of this file —
> colour, card, tool, delivery gate — is unchanged and still authoritative.

## 1. The reservoir — what actually exists

Inventoried 2026-09-18 from `C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation`
(WSL: `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation`).

| Master | Path (under `animation/`) | Runtime | Frame | Yield |
| --- | --- | --- | --- | --- |
| **Karen — story film** | `Karen/Karen VID NEW!/Karen story vid.mp4` | **5:16** | 3840×2160 · 24fps | 🥇 12–16 shorts |
| **Camping — story film** | `Camping Comic/Camping Video NEW!/camping jack/Camping story video.mp4` | **4:50** | 1920×1080 · 25fps | 🥇 10–14 shorts |
| **"All Day to Complain"** (Karen track) | `songs/Karen/All Day to Complain - yes.mp4` | 4:10 | 3840×2160 · 25fps | 6–8 music cuts |
| **"Camping"** (track) | `songs/camping vid/camping.mp4` | 3:35 | 1920×1080 · 25fps | 6–8 music cuts |
| **GitPush Origin Master** | `git push origin master/git push story vid/full vid test 1.mp4` | 1:47 | 1920×1080 | 4–5 |
| GPOM vol 1 / vol 2 | `git push origin master/Other/…` | 1:23 / 1:30 | 1920×1080 | 3–4 |
| **Magic Money Tree** | `shorts/magic money tree/magic money tree.mp4` | 1:10 | 1280×720 | 3–4 (+ 7×10s already cut, **16:9 — re-cut vertical**) |
| Star Wars 1 / 2 | `Star Wars/…` | 1:30 / 1:41 | 1280×720 | 3–4 |
| **Trailer draft 1** | `badcode logo designs/draft 1/Trailer-draft-1.mp4` | 0:40 | 1920×1088 | the channel trailer, near-native |
| Logo / ident bank | `badcode logo designs/Badcode-logo-vid/*` (14 clips) | 2–10s each | mixed | **stings, outros, loop tails** |
| Out Of The Jungle | `Out Of The Jungle/vid 1–11.mp4` | 2–15s each | mixed | b-roll for meme tier |
| US-Navy-Japan · Moon · Trump-internet · Fire sale · Stock Market · fast food · general ai | various | short | mixed | ⬜ unreviewed — likely meme-tier |

**Two things this inventory changes.** First, *we are not short of material* — the bottleneck
was never content, it was that nobody ever cut it. Second, **the ident bank is the most
under-used folder on the drive**: 14 short logo/city/fire clips that give every short a
2-second branded tail at zero cost.

---

## 2. 🔴 Every master is full-range and untagged — fix it at cut time

Measured 2026-09-18 with `ffprobe` + `signalstats`:

| Master | `color_range` | Measured luma |
| --- | --- | --- |
| Karen story film | **unknown** | **YMIN 0 / YMAX 255** |
| Camping story film | **unknown** | **YMIN 10 / YMAX 248** |
| camping.mp4 (track) | **unknown** | full (already on record) |

This is **exactly the `camping.mp4` bug** in
[`../video-fx/delivery.md`](../video-fx/delivery.md), and it is not confined to that one file —
it is how the whole drive exports. A player that finds no tag assumes limited range and stretches
16–235 out to 0–255, so **everything below 16 crushes to black**. On a near-black house register
that is not a grading nuance, it is the picture.

🔑 **So no short is ever cut with a bare `ffmpeg -ss … -t …`.** `cut.sh` does the real
conversion and then tags honestly:

```
-vf "scale=in_range=full:out_range=limited"  -pix_fmt yuv420p -color_range tv
-colorspace bt709 -color_primaries bt709 -color_trc bt709
```

**Both halves of that scale filter are required** — `out_range` alone is a silent no-op that
writes a tag the content does not match. And on a graph that draws its own furniture, `scale`
is the wrong tool entirely — see §10.

### ⚠️ `delivery-qc.sh` gives a false FAIL on any short with burnt-in text

Measured on `C6-collision.mp4`, 2026-09-18, and worth knowing before someone "fixes" a
correct file:

| | |
| --- | --- |
| Filter graph output, rendered **lossless** to FFV1 | **YMIN 16 / YMAX 235 — exactly right** |
| Same graph through x264 CRF 19 | YMIN 0 / YMAX 246 → **`delivery-qc.sh` says FAIL** |
| Median frame floor across 720 frames | **25** (p90 = 26) |
| Frames containing *any* pixel below 16 | 195 of 720 (27%) |

The excursion is **x264 ringing around high-contrast text edges** — overshoot and undershoot
on a handful of pixels where white mono type meets a near-black card. It shrinks as CRF drops
(YMIN 8 at CRF 19, 11 at CRF 12 on a 2s sample) and it is not the picture: the picture is
seated at 25. `delivery-qc.sh` takes whole-clip min/max, which cannot tell a few ringing
pixels from a mis-ranged image.

### ✅ The one-line test that settles it — measured 2026-09-21

The median-floor rule below is right but fiddly. **A 1-pixel blur is a decisive, 5-second
discriminator**, because encoder ringing lives in single pixels at an edge and a mis-ranged
picture does not:

```bash
ffmpeg -v error -i SHORT.mp4 -vf "boxblur=1:1,signalstats=stat=brng,metadata=print:file=-" \
  -an -f null - 2>/dev/null | awk -F= '/YMIN|YMAX/{print $2}' | sort -n | sed -n '1p;$p'
```

**If the blurred file sits inside 16–235, the picture is correctly ranged and `delivery-qc.sh`
is giving its false FAIL.** Verified on the five batch-2 remix shorts: raw clip min/max ran
0–255, 8–242, 8–255 and 3–248 — every one a FAIL — while blurred they measured **20–227,
28–220 and 29–224**. The worst offender (`R2-switchboard`) is 1951 archive footage of a
telephone cord board, a high-frequency black-and-white lattice, which is the pathological case
for x264 ringing and nothing to do with range. ⬜ Whether `delivery-qc.sh` should run this blur
itself before declaring a range failure is still Kai's call.

🔑 **The rule:** on a short with burnt-in graphics, read the **median frame floor**, not the
clip minimum. Everything else the gate checks — the tag, the matrix, the pix_fmt, loudness,
true peak — still applies and still matters. ⬜ Whether `delivery-qc.sh` should grow a
percentile-based verdict is Kai's call, not a change to make quietly.

---

## 3. The format — one 9:16 card, three modes

Everything on the drive is 16:9. A 9:16 crop of a 1920×1080 frame keeps **607 px of 1920** —
it throws away 68% of the width. Whether that is fatal depends entirely on the shot, so the
tool has three modes and the choice is a per-shot judgement (the `shot-craft` skill owns it).

| Mode | What it does | Use it when |
| --- | --- | --- |
| **`slate`** *(house default)* | 16:9 window on a near-black 1080×1920 card, hairline above and below, hook text above, captions below, `badcode.tv` at the foot | The composition is the point — monumental wides, the car park, the forest, the crowd. **Near-black IS the brand, so the card reads as design, not as a crop failure.** |
| **`crop`** | Full-bleed centre crop to 9:16, pannable with `-p` | A single figure centred in frame. Verified on Camping 238s (forest + star trails) — **survives completely**. Full-bleed wins attention; use it whenever the shot allows. |
| **`full`** | Letterboxed 16:9 centred on black, no furniture | Music-video cuts where the track carries it and text would be noise |

**Spec, fixed:** 1080×1920 · source fps preserved (no judder) · H.264 high/4.1 CRF 19 ·
`yuv420p` limited-range tagged BT.709 · AAC 192k 48k stereo · `+faststart` ·
loudness normalised to **−14 LUFS / −1.5 dBTP** (the social standard).

**Safe areas.** Platform UI eats roughly the bottom 350 px and the right 150 px. Captions sit
at MarginV 500 (slate) / 430 (crop), the kicker at `h−250`. Nothing load-bearing goes below
y≈1650.

**Type.** The brand face is JetBrains Mono; it is **not installed in WSL**, so the tool falls
back to DejaVu Sans Mono Bold. ⬜ Dropping the real `.ttf` into `~/.fonts` and setting
`BADCODE_FONT` is a one-line upgrade and should be done before the first real batch.

---

## 4. What actually drives views — 2026 research

Graded to the house convention: ✅ verified against multiple current sources · ◻ single-source
or practitioner claim, treat as provisional.

**The physics of the feed**
- ✅ **The first 2–3 seconds decide everything.** 50–60% of all drop-off happens in seconds
  0–3; ~70% of viewers decide inside that window. A Short that keeps 70–85% through the hook
  window gets ~2.2× the total views of one that does not.
- ✅ **Completion rate and swipe-away rate are the dominant ranking inputs.** Target: swipe-away
  under 25% on a sub-30s Short; over 40% means the hook is broken. 70%+ average-percentage-viewed
  is viral territory, under 30% and distribution stops.
- ✅ **The first 30–60 minutes are the whole audition.** A seed audience is shown the Short; if
  it does not clear threshold, distribution stops. There is no slow burn.
- ✅ **30–60 seconds is the performance band.** Max length is 3 minutes (since Oct 2024) but
  50–60s clips out-earn sub-10s clips by roughly 22× on views. Comedy beats run shorter (15–25s).
  **Completion beats length every time** — a 40s Short finished beats a 3-minute one abandoned.
- ✅ **Captions are not optional.** ~83% of social video is watched muted. Burnt-in, always.
- ✅ **Views now count from the first frame** (Shorts since Mar 2025, everything since 24 Aug
  2026). So **the headline view number is worth less than it was** — judge ourselves on
  *Engaged views* (YouTube Analytics → Advanced mode) and on average-percentage-viewed, not on
  the vanity count.

**Posting**
- ✅ **Volume buys lottery tickets, not linear growth.** Buffer's 11.4M-post study: more posting
  lifts *mean* views per post (2–5/wk ≈ +17%, 11+/wk ≈ +34%) while the **median stays flat** —
  the entire gain is more chances at an outlier. Post consistently *for the tail*.
- ✅ **Never cross-post a watermarked file.** Every platform demotes competitor watermarks.
  Export clean once, upload natively to each. ◻ Instagram now runs an "originality score" that
  also catches un-watermarked recycled clips, and accounts posting 10+ reposts in 30 days are
  reportedly excluded from recommendations — **treat IG as the platform that most needs a
  distinct cut**, not a mirror.
- ◻ Shorts→long-form conversion: below 0.1% needs work, above 0.3% is working. **Pin a comment
  with the link on every Short** — it is the only reliable path from the Shorts feed to the film.

**What travels**
- ✅ **Pick a lane.** A niche is a targeting system: it tells the algorithm who to show you to
  and tells a viewer why to follow. This is the argument for §5's named series rather than a
  stream of unbranded clips.
- ◻ Meme-format posts reportedly average far higher organic engagement than branded graphics,
  and content aimed at **political frustration** scores ~37% higher comment engagement than
  humour alone. Short-form video memes now out-share static image memes.
- ✅ **Hook shapes that work:** bold claim · curiosity gap · micro-story open · visual shock ·
  direct question. ◻ The most common structure in a 2,626-clip sample: **authority signal →
  curiosity gap → promise of payoff** — which is, unmodified, the BadCode narrator.
- ✅ **Specific curiosity beats broad curiosity.** "You won't believe this" is dead; a concrete,
  slightly uncomfortable claim is what works. Our lines are already concrete.

**Standing rules from the playbooks that still apply:** AI-made content is not penalised
anywhere we operate — non-disclosure and mass-production are the enforcement targets, so
disclose and lean in; TikTok's FYP is follower-independent and remains our best cold start.

---

## 5. The four series — pick a lane and name it

One channel, four repeating formats. Each is a lane the algorithm can learn and a viewer can
recognise. Every short belongs to exactly one.

| Series | Shape | Length | Source | Why it earns its place |
| --- | --- | --- | --- | --- |
| **① TRANSMISSION** | One narrator line over one monumental shot. Hook bar up top, line burnt in, ident tail. | 12–25s | Story films + ident bank | The house voice, undiluted. Cheapest to make, most on-brand, and it is the format the narrator pattern was built for. |
| **② THE BIT** | A self-contained comic beat, set up and punched, lifted whole from a film. | 20–45s | Karen (comedy) · Camping (dark) | The shareable tier. Karen is genuinely funny and none of it has ever been seen. |
| **③ ONE MINUTE OF THE FILM** | The strongest continuous 45–60s of a core, cut to end on an open loop, pinned comment to the full film. | 45–60s | Story films | The actual funnel. Sits in the ✅ 30–60s band and is the only format built to convert. |
| **④ ARTEFACT** | A still or 3–6s loop of one object from the world — the redundancy screen, the burning newspaper, the `BAD C0DE` plate — with one caption. | 3–8s still / loop | Frame grabs | The meme tier. Posts as image *or* video, costs minutes, and is the only tier that can react to news the same day. |

🔴 **What we do not do:** an unbranded clip with no series, no hook bar and no tail. That is the
default output of every auto-clipper and it is why it does not work.

---

## 6. The hook bank — the lines are already written

Straight from canon. These are the scroll-stoppers; the hook bar carries the short version, the
audio carries the whole line.

**Camping** — [`stories/camping/narration/three-voice-script.md`](../stories/camping/narration/three-voice-script.md)

| Line | Hook bar | Type |
| --- | --- | --- |
| "Someone is going to lose a house over this trade and I am never going to meet them. That is not callousness. That is geography." | `THAT IS NOT CALLOUSNESS.\nTHAT IS GEOGRAPHY.` | bold claim |
| "We buy social housing. We do not always let it out — an empty flat goes up in value at precisely the same rate as a full one." | `AN EMPTY FLAT GOES UP\nJUST AS FAST AS A FULL ONE` | visual shock |
| "The ones who stop buy him a can and then judge him for drinking I.P.A." | `THEY BUY HIM A CAN\nTHEN JUDGE HIM FOR IT` | micro-story |
| "It is about the width of a payslip." | `THE GAP BETWEEN YOU\nAND THAT MAN` | curiosity gap |
| "It does not say who owns the machines. Same man who owned the flats." | `WHO OWNS THE MACHINES?` | 🔑 **the beneficiary line** |
| "Neither of them said it out loud. They never do. That is the entire problem." | `NEITHER OF THEM\nSAID IT OUT LOUD` | curiosity gap |
| "Two men and a bin. Of everything I have ever seen, that is the part I would keep." | `OF EVERYTHING I EVER SAW` | micro-story |

**Karen** — [`stories/karen/narration/script.md`](../stories/karen/narration/script.md)

| Line | Hook bar | Type |
| --- | --- | --- |
| "Karen, your role has been made redundant." *(on screen, from an AI)* | `FIRED BY A LAPTOP` | visual shock |
| "Turns out putting fish in the microwave is the cleaner's fault. Who knew." | `IT WAS THE CLEANER'S FAULT` | the bit |
| "I have ALL DAY to complain." | `SHE HAD ALL DAY\nTO COMPLAIN` | bold claim |
| "It shouldn't, but it goes viral. Terrible… bloody… song." | `TERRIBLE. BLOODY. SONG.` | the bit |
| "They call it a revolution now. At the time, it was just a very long phone call." | `IT WAS JUST A VERY\nLONG PHONE CALL` | 🥇 curiosity gap |
| "Nobody won… which is why it held." | `NOBODY WON.\nTHAT IS WHY IT HELD.` | bold claim |
| "They don't teach her as a hero. They teach her as a method." | `NOT A HERO.\nA METHOD.` | bold claim |
| *(alt)* "The statue is still on hold. A hundred years, and nobody's picked up." | `STILL ON HOLD` | 🥇 micro-story |

---

## 7. Batch 1 — twenty cuts, with real timestamps

In-points read off contact sheets of both masters (6s sampling, 2026-09-18). ⚠️ **They are
±3s** — open the file, nudge to the frame, then render. Durations are targets, not gospel.

**Karen** — `Karen/Karen VID NEW!/Karen story vid.mp4`

| # | In → Out | Mode | Series | Hook bar |
| --- | --- | --- | --- | --- |
| K1 | 22 → 46 | `slate` | ② THE BIT | `FIRED BY A LAPTOP` — the redundancy screen + SEAN AI ident |
| K2 | 8 → 24 | `crop` | ② THE BIT | `IT WAS THE CLEANER'S FAULT` — the microwave |
| K3 | 44 → 70 | `slate` | ② THE BIT | `KNOW YOUR LIMIT.\nAND EAT SOMETHING.` — the bar → the bridge |
| K4 | 80 → 100 | `slate` | ① TRANSMISSION | `SHE WENT LOOKING FOR\nAN ANCIENT RELIC` — the phone box |
| K5 | 104 → 136 | `slate` | ③ ONE MINUTE | `SHE HAD ALL DAY\nTO COMPLAIN` — the receptionist chain |
| K6 | 182 → 214 | `slate` | ③ ONE MINUTE | `A CROWD FORMED\nAROUND A PHONE BOX` — 🥇 the aerials are the best images in the film |
| K7 | 214 → 240 | `slate` | ② THE BIT | `TERRIBLE. BLOODY. SONG.` — the news crew |
| K8 | 240 → 268 | `slate` | ③ ONE MINUTE | `THE PRESIDENT CALLED HER` → cut on the SEAN AI reveal |
| K9 | 262 → 276 | `crop` | ① TRANSMISSION | `IT WAS JUST A VERY\nLONG PHONE CALL` — over the static burst |
| K10 | 278 → 300 | `slate` | ① TRANSMISSION | `NOT A HERO.\nA METHOD.` — the lecture + the statue |
| K11 | 288 → 298 | `crop` | ④ ARTEFACT | `STILL ON HOLD` — the statue, loopable |

**Camping** — `Camping Comic/Camping Video NEW!/camping jack/Camping story video.mp4`

| # | In → Out | Mode | Series | Hook bar |
| --- | --- | --- | --- | --- |
| C1 | 4 → 22 | `slate` | ① TRANSMISSION | `THAT IS NOT CALLOUSNESS.\nTHAT IS GEOGRAPHY.` — the trading floor |
| C2 | 22 → 36 | `slate` | ① TRANSMISSION | `AN EMPTY FLAT GOES UP\nJUST AS FAST AS A FULL ONE` — 🥇 the empty flat |
| C3 | 34 → 70 | `slate` | ③ ONE MINUTE | `HE SAID THERE WAS NO RUSH` — the drive → the debris. **End on the silence.** |
| C4 | 98 → 120 | `slate` | ② THE BIT | `THEY BUY HIM A CAN\nTHEN JUDGE HIM FOR IT` — the Waitrose car park |
| C5 | 120 → 140 | `crop` | ② THE BIT | `EMPATHY IS NOT\nAN EMERGENCY` — therapy |
| C6 | 142 → 172 | `slate` | ③ ONE MINUTE | `NEITHER OF THEM\nSAID IT OUT LOUD` — 🥇 the collision, the whole film in 30s |
| C7 | 232 → 252 | `crop` | ① TRANSMISSION | `THE GAP BETWEEN YOU\nAND THAT MAN` — star trails. **Crop verified — composition survives.** |
| C8 | 256 → 280 | `slate` | ③ ONE MINUTE | `WHO OWNS THE MACHINES?` — waking in the tent → the burning newspaper |
| C9 | 272 → 282 | `crop` | ④ ARTEFACT | `BRITAIN'S LAST WORKER` — the newspaper in the fire, loopable |

**The first three are already cut** — rendered 2026-09-18 to
`animation/shorts/batch-1/` (`C6-collision.mp4`, `K1-redundant.mp4`, `C7-payslip.mp4`).
Watch them, then re-run with nudged in-points. The commands:

```bash
M="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation"

# C6 — the collision. The single best 30 seconds we own.
scripts/shorts/cut.sh -i "$M/Camping Comic/Camping Video NEW!/camping jack/Camping story video.mp4" \
  -s 142 -t 30 -m slate -H 'NEITHER OF THEM\nSAID IT OUT LOUD' -k "badcode.tv" \
  -o out/C6-collision.mp4

# K1 — fired by a laptop.
scripts/shorts/cut.sh -i "$M/Karen/Karen VID NEW!/Karen story vid.mp4" \
  -s 22 -t 24 -m slate -H 'FIRED BY A LAPTOP' -k "badcode.tv" \
  -o out/K1-redundant.mp4

# C7 — the width of a payslip, full-bleed.
scripts/shorts/cut.sh -i "$M/Camping Comic/Camping Video NEW!/camping jack/Camping story video.mp4" \
  -s 232 -t 20 -m crop -H 'THE GAP BETWEEN YOU\nAND THAT MAN' \
  -o out/C7-payslip.mp4

scripts/delivery-qc.sh out/C6-collision.mp4     # before anything is uploaded
```

---

## 8. Cadence, posting, measurement

**Cadence.** 5 shorts a week, cut in one batch on one day. ✅ Batching is what makes
repurposing survivable; ad-hoc posting is what kills it. That lands inside TikTok's efficient
2–5/wk band and near the Shorts 1–2/day guidance without ever needing new creative work.

**Order of platforms.** TikTok first (follower-independent cold start), YouTube Shorts second
(the library and the funnel), Instagram Reels third **with its own cut** (originality scoring).
✅ Clean export, native upload, three times — never a share-sheet repost.

**Per upload, non-negotiable:**
1. Burnt-in captions.
2. Pinned comment: *"The whole film: badcode.tv/…"* + UTM
   (`utm_source=<platform>&utm_campaign=<story>`), per the plan's attribution scheme.
3. AI disclosure ticked. ✅ The label itself carries no ranking penalty and honesty is the brand.
4. The story's own track as the audio where it fits — ◻ our own DnB as an original sound is a
   growth surface others can reuse.
5. A 1.5–2s ident tail from `badcode logo designs/Badcode-logo-vid/`.

**Measure these four, weekly, and nothing else:**

| Metric | Where | Target |
| --- | --- | --- |
| Average percentage viewed | YT Studio / TikTok analytics | **>50%**, chasing 70% |
| Swipe-away rate | Shorts analytics | **<25%** sub-30s |
| Engaged views (not views) | YT → Advanced mode | the real number post-Aug-2026 |
| Funnel clicks to badcode.tv | UTM | **>0.1%** of views, target 0.3% |

🔑 **The unit of learning is the hook, not the clip.** Log hook bar + series + retention for
every upload; after ~20 posts the bank in §6 sorts itself by measured performance and the
guessing stops.

---

## 9. Guardrails

- 🔴 **[`the-reader.md`](./the-reader.md) gates every short, and one rule bites hardest here:
  never raise automation fear without naming the beneficiary in the same piece.** Unaimed, it
  demonstrably feeds nativism. A 20-second clip has no room to recover, so **any short touching
  AI or job loss must carry the beneficiary line inside it** — for Camping that is literally
  written: *"It does not say who owns the machines. Same man who owned the flats."* If a cut
  cannot fit it, that cut is not a short. Also standing: never "you've been duped"; name the
  decision-maker, never the technology.
- **Profanity ships in full.** "This prick", "fucking wank tanks", "getting fucked up with
  Susan" are the voice and they stay — no asterisks, no bleeps, no substitutions. ◻ The only
  real cost is ad-suitability on YouTube, which is irrelevant while we are not monetising.
  ⬜ Unverified whether first-3-seconds profanity affects TikTok distribution — worth one A/B.
- **Third-party footage:** none of batch 1 uses any. If react content starts, the playbooks'
  fair-use rules apply unchanged (our commentary dominates, clips short and fragmented, never
  escalate a Content ID dispute without Kai or Jack).
- **Delivery gate:** `scripts/delivery-qc.sh` before every upload. No exceptions — §2 is exactly
  why.

---

## 10. The tool

[`scripts/shorts/cut.sh`](../../scripts/shorts/cut.sh) — one master in, one platform-ready
9:16 file out.

```
scripts/shorts/cut.sh -i MASTER -s START -t DUR -o OUT.mp4 [-m slate|crop|full]
                      [-H 'HOOK\nLINE'] [-k KICKER] [-c captions.srt] [-S size]
                      [-p pan] [-T mark] [-L skip loudnorm] [-n dry run]
```

It always does the §2 colour conversion, builds the 9:16 card, renders each `\n`-separated hook
line as its own centred bar, burns captions, normalises loudness and tags the output correctly.

**Two traps it exists to absorb, both measured 2026-09-18 on ffmpeg 6.1.1:**
- 🔴 **`drawtext` does not interpret `\n`.** Only a real newline breaks a line; the two-character
  sequence renders literally as "DAYnTO". The tool converts it.
- 🔴 **`subtitles=…:force_style` margins are in the SRT's ASS play-res, not pixels.** ffmpeg
  converts an `.srt` with `PlayResX 384 / PlayResY 288`, so `MarginV=420` silently lands off a
  1920-tall frame and the captions simply never appear — no error. The tool converts to `.ass`,
  rewrites the play-res to 1080×1920 and writes the house style in real pixels.
- 🔴 **`scale=in_range=full:out_range=limited` is a no-op at the tail of a graphics graph.**
  With no resize and no format change, swscale fast-paths and the squeeze does nothing —
  measured: YMAX stayed at 255 while the file claimed `tv`. Worse, the conversion cannot go at
  the *head* either, because every graphic drawn afterwards is rasterised full-range and lands
  outside 16–235. The tool does it arithmetically instead, last, with a LUT that cannot be
  optimised away, then tags without re-converting:
  `format=yuv420p, lutyuv=y='16+val*219/255':u='128+(val-128)*224/255':v=…,
  setparams=range=tv:colorspace=bt709:…` — verified lossless at exactly 16–235.

---

## 11. Open, and owed a ruling

- ⬜ **`slate` vs `crop` is unproven on our audience.** Full-bleed generally wins attention;
  our register argues for the card. Both are **built and rendered** (C6/K1 slate, C7 crop, in
  `animation/shorts/batch-1/`) — decide from measured average-percentage-viewed, not taste.
- ⬜ **JetBrains Mono is not installed in WSL.** Until it is, shorts go out in DejaVu Mono.
- ⬜ **Karen's film is 4K** and Camping's is 1080p — the Karen crops can be genuinely sharp.
  Nothing else in the pipeline exploits that yet.
- ⬜ **The seven existing Magic Money Tree "shorts" are 16:9 720p** — they are not shorts. Re-cut.
- ⬜ **Unreviewed folders:** `Other/`, `Scripted/`, `general ai/`, `fast food/`, `Fire sale/`,
  `Stock Market/`, `Biometric Steal/`, `Gimme the link/`, `Lights, camera/`, `Out Of The Jungle/`.
  Likely the whole ④ ARTEFACT tier lives in there.
- ⬜ **Narration audio for Camping's story film is a three-voice script that has never been
  recorded** ([`stories/camping/narration/three-voice-script.md`](../stories/camping/narration/three-voice-script.md)).
  Batch 1 uses the film's existing audio; the hook bars carry the written lines. If the
  three-voice version is ever rendered, every Camping short gets re-cut and improves.
- ⬜ **Untested:** whether Flow/Veo-derived stylised video trips YouTube's permanent AI label.
  Batch 1 is the first real chance to find out — watch the first upload's label state.
