---
brief: 20
title: Near-black in practice - shadow that survives the pipeline
swept: 2026-08-26
wave: 2
closes_gap: 7
searches_used: 7
---

# 20 - Near-black in practice: shadow that survives the pipeline

## 1. The short answer

- **Banding in dark gradients is a bit-depth/quantisation fact, not a taste problem.** Standard
  8-bit delivery gives only 256 steps per channel; dark gradients occupy a small slice of that
  range, so the steps become visible as bands. Grade **A** — this is arithmetic, not opinion.
- **Dither and grain are the standard fix, and they work by the same mechanism film grain
  provided for free for a century.** Randomised noise breaks up the hard edge between
  quantisation steps so the eye reads a smooth gradient instead of a stepped one. Grade **A**
  for the mechanism; **P** for "add grain deliberately," which is now common delivery practice
  but is craft convention, not a measured optimum.
- **Compression punishes near-black hardest, structurally.** Encoders spend bits where the eye
  and the rate-distortion math say it matters, and dark, low-contrast, low-detail regions are
  exactly where they spend least — which is our whole frame. Grade **A (mixed)**: the
  bit-allocation principle is engineering fact; which specific artifact (banding vs. blocking)
  dominates depends on codec, bitrate and content, so treat the *specific* outcome as **A
  (mixed)**.
- **Crushing and lifting blacks are opposite, both destructive if applied blind.** Crushing
  (pulling shadow values to pure black) discards detail permanently once baked into a delivered
  file; lifting (raising the black point) keeps detail but flattens contrast and can look muddy.
  Neither is "correct" — the craft is choosing per shot. Grade **P**, standard colourist
  practice, not independently sourced to a single named colourist in this sweep — flagged.
- **Full-range/limited-range mismatch is a distinct, catastrophic bug, not a subtle grading
  choice.** An untagged or mistagged file can have everything below a threshold clip flat to
  pure black on playback, discarding real detail with no warning in the edit. Grade **A** — this
  is a metadata/signal-processing fact, independently documented across broadcast and Adobe/GPU
  engineering references. **BadCode has already shipped this exact bug once** (`camping.mp4`),
  so this is not theoretical for us.
- **Platform compression (YouTube/Instagram/TikTok) makes dark footage measurably worse, and the
  practitioner fix is to over-expose slightly and grade down, not to deliver true-dark.** Grade
  **p** — this is repeated creator-forum wisdom, not a controlled study; treat it as informed
  folklore, not fact.
- **Never eyeball a dark frame — measure it.** A waveform monitor or false-colour overlay is the
  only reliable way to know whether a shadow is sitting at "deep but present" (roughly 2-8 IRE)
  or has already fallen off the bottom of the scale (0 IRE, clipped). Grade **A** for what the
  scopes measure; **P** for the specific IRE bands practitioners target, since exact numbers vary
  by house style.
- **A dark image needs one bright anchor for the darkness to read as intentional, and there is
  now a real perceptual mechanism for why.** Wave one's brief 02 found this craft rule; the human
  visual system computes "how dark is dark" relative to the *brightest* region it can group into
  the same scene (anchoring theory of lightness perception, Gilchrist 1999). Remove the anchor
  and the visual system has nothing to normalise against — the frame reads as underexposed noise,
  not as chosen darkness. Grade **A** for the perceptual mechanism.
- **Viewing environment changes what "near-black" even means to the viewer**, and our viewer (a
  phone, in daylight, glossy screen) is close to worst-case for a controlled-dark aesthetic:
  ambient light reflecting off the panel adds real luminance to what should be pure black,
  crushing perceived contrast further before compression even enters the picture. Grade **A**
  for the optical fact; **P**/practitioner-observed for how much it actually costs a given
  design (not independently measured for our exact device/context).

## 2. The findings

**Banding is quantisation of a smooth analog-original gradient into a finite number of digital
steps, and it is worst exactly where the tonal range is smallest — near black and in skies.**
Grade **A**. Standard 8-bit-per-channel video gives 256 levels per channel; a gradient spanning
only the bottom tenth of that range (a dark room, a black background with one dim light) may
cross fewer than 25 of those levels over hundreds of pixels, so each step becomes a visible
band. This is a description of how digital sampling works, not a claim requiring practitioner
corroboration — treat it as a hard technical fact, same status as Nyquist sampling. Multiple
independent technical explainers converge because the underlying mathematics is the same
everywhere. Source: [KTC "What Causes Color Banding on Gradients and How Is It Related to Bit
Depth?"](https://us.ktcplay.com/blogs/support-tips/color-banding-bit-depth-explained) (content-mill,
cited for the plain-English restatement only, not as evidence of the underlying claim, which is
standard digital-signal-processing textbook material).

**Dithering fixes banding by trading spatial precision for tonal precision: it adds small,
patterned or random noise before quantisation so that neighbouring pixels round to different
adjacent levels, and the eye's own spatial averaging reconstructs the smooth gradient the display
can't show directly.** Grade **A**. This is an established signal-processing technique (used in
audio bit-depth reduction long before video, same mathematics), not a stylistic opinion.
Source: [Anisoptera Games, "How to fix color banding with
dithering"](https://www.anisopteragames.com/how-to-fix-color-banding-with-dithering/) (practitioner
explainer, technique itself is textbook DSP).

**Film grain historically hid this exact problem for free, because grain IS randomised
luminance noise riding on every frame — analog dithering nobody had to add on purpose.** Grade
**A (mixed)**: the mechanism (grain = spatially/temporally random noise that masks quantisation
and low-contrast banding the same way digital dither does) is well understood and stated
directly in the dithering literature above; the historical framing ("this is *why* film never
showed banding") is a reasonable inference from that mechanism rather than a separately
cited historical claim. Practical consequence: a fully clean, denoised digital dark image is
*more* likely to band than a grainy one, because denoising removes the very noise that was
doing the dithering job.

**Compression encoders allocate bits according to where distortion will be least visible or
least costly under the rate-distortion objective, and that structurally means less-detailed,
low-contrast regions — shadows, skies, flat walls — get the fewest bits, which is why
macroblocking and banding both concentrate in dark, low-detail frames.** Grade **A (mixed)**:
the general bit-allocation principle (spend more where distortion is visible/costly, less where
it isn't) is core to how H.264/HEVC rate control and perceptual quantisation work and is stated
in technical references; which specific artifact appears (blockiness vs. banding vs. noise)
depends on the specific codec, bitrate, and content, so the *specific outcome* is contested/
variable rather than a single fixed law. Sources: [Lighterra, "Video Encoding Settings for H.264
Excellence"](https://www.lighterra.com/papers/videoencodingh264/) (practitioner/technical
reference); forum discussion at [Doom9, "Reducing Blocks in Dark
Areas"](https://forum.doom9.org/archive/index.php/t-107236.html) (practitioner anecdote, **p**
on its own, corroborating rather than establishing the claim).

**Crushing blacks (pushing shadow values down to the display's absolute black) permanently
discards the tonal information in that region once the file is delivered; lifting blacks (raising
the black point so nothing reads as pure black) preserves detail but reduces perceived contrast
and can look flat or "muddy" if overdone.** Grade **P**, standard colour-grading craft
distinction, repeatedly described in colourist-facing material, but this sweep did not reach a
single named colourist making the crush/lift distinction explicitly in their own voice — flagged
as **p**-adjacent rather than full **P** until a named source is found. The controlling fact
underneath it, however, is **A**: crushing is lossy and permanent (values collapse to one flat
level, unrecoverable), lifting is non-destructive to detail but destructive to contrast — this
is arithmetic on the tonal curve, not opinion.

**"Protecting shadow detail" in a working grading room means keeping shadow values above the
scope's zero line and confirming with a waveform or false-colour readout, not by eye** — deep
shadows that fall to or below 0 IRE lose information outright, and colourists commonly treat
"reasonably dark but not clipped" (roughly the low single-digit-to-high-single-digit IRE range for
the darkest meaningful detail) as the working target, with skin-tone and face shadow regions
treated as a special, protected case. Grade **P** — this is repeated across grading-education
sources but the specific IRE numbers vary by source and none is a single named colourist speaking
on the record in this sweep, so treat the *numbers* as convention, not law. Source:
[cinapex, "You're Reading Your Waveform Wrong: The Signal Logic Behind IRE, Stops, and Exposure
in DaVinci Resolve 21"](https://cinapex.pro/waveform-ire-davinci-resolve/) (practitioner-technical
explainer); [Hollyland, "What is a False Color Chart?"](https://www.hollyland.com/blog/tips/what-is-a-false-color-chart)
(practitioner explainer, describes the standard false-colour mapping — deep blue/blue = 0-5 IRE,
clipped or near-clipped shadow).

**Full-range vs. limited-range is a metadata/signal convention, not a look, and a mismatch is a
specific, mechanical failure: broadcast/film delivery traditionally encodes black at digital
value 16 and white at 235 ("limited"/"video" range) leaving headroom below and above; computer
displays and browsers generally expect the full 0-255 scale ("full" range). If a file is tagged
wrong, or not tagged at all, and is interpreted at the wrong range, everything below the
mismatched threshold collapses to a single flat black with no gradation** — not a grading choice,
a hard clip introduced by the playback chain, invisible until you check the file's actual range
tag or a scope. Grade **A** — this is a documented broadcast/engineering standard and a
well-known interoperability failure mode, not contested. Sources: [Sound & Vision, "Video
Dynamic Range and Color
Space"](https://www.soundandvision.com/content/video-dynamic-range-and-color-space) (trade
press, technically accurate restatement of the broadcast standard); Adobe community threads on
Premiere export range mismatches corroborate the failure mode is a known, recurring support issue
in real production pipelines, e.g. ["GPU color range 16-235 vs 0-255 & video limiter to fix washed
out
export"](https://community.adobe.com/t5/premiere-pro/gpu-color-range-16-235-vs-0-255-amp-video-limiter-to-fix-washed-out-export/m-p/11946383)
(practitioner forum, corroborating that this specific bug recurs in the wild — this is the exact
class of bug BadCode shipped once).

**Platform compression on YouTube/Instagram/TikTok specifically degrades dark footage —
reducing dynamic range, darkening midtones further, and introducing blockiness in shadow and
low-detail regions — and the informal creator-side fix is to slightly over-expose or lift before
export and let the platform's re-encode bring it back down, rather than deliver a file that is
already sitting at the platform's crush point.** Grade **p** — sourced only to
creator-forum/content material (TikTok discovery threads, general video-quality blog posts), no
named practitioner, no platform engineering documentation reached in this sweep. Treat as
plausible folk practice worth testing against our own delivery, not as established fact.
*(unverified in sweep — platform-specific compression parameters are not public and change
without notice)*.

**A dark image reads as an intentional aesthetic choice, rather than as underexposure or a
broken file, when the frame contains at least one clearly brighter region for the eye to anchor
against — and this has a real perceptual-science basis, not just craft folklore.** Grade **A**
for the underlying mechanism. Anchoring theory of lightness perception (Gilchrist et al., 1999,
*Psychological Review*) proposes that the human visual system computes perceived lightness
relative to the highest-luminance region it groups into the same illumination framework — the
"highest luminance rule" assigns the brightest element in a scene a very high perceived
reflectance value, and everything else in that frame is judged dark *relative to that anchor*.
Remove any clearly brighter region from the frame and the visual system has no anchor to
normalise against, so the whole image tends to read as flat, murky, or simply badly exposed
rather than as chosen. This directly extends wave one brief 02's top-ranked craft finding
("motivated light... is the only thing anchoring it as a believable scene") by supplying the
perceptual mechanism underneath the craft rule. Source: [Gilchrist et al., "An anchoring theory
of lightness perception," *Psychological Review*, 1999 —
PubMed](https://pubmed.ncbi.nlm.nih.gov/10560329/) (primary, peer-reviewed); see also the later
[double-anchoring extension, Howe et al. 2007,
PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2635063/) (primary, peer-reviewed, notes the
theory is refined/contested in its details but the core anchoring mechanism is not disputed).

**Viewing environment materially changes what a dark frame looks like, independent of the file
itself: ambient light in the room reflects off the display surface and adds real luminance to
areas that are digitally coded as black, which reduces perceived contrast — and this effect is
worst on glossy phone/tablet screens in bright daylight, which is precisely BadCode's default
viewing condition.** Grade **A** for the optical mechanism (reflected ambient light adding to
panel luminance is basic display physics); **P**/informed-industry-consensus for "grading suites
control this and typical phone viewing does not," which is standard broadcast-engineering
practice (calibrated dark rooms) rather than a single contested claim, though this sweep did not
reach a single named colourist stating it directly. *(unverified in sweep beyond content-mill
sources — the specific magnitude of contrast loss on a given phone in daylight was not
independently measured here)*.

## 3. What survives our constraints

Everything in this brief survives, in the strict sense that all of it is post-production,
delivery, and quality-control craft — none of it requires a crew, a set, or control over how the
shot was captured or generated. The honest breakdown is about *effort and tooling*, not
survivability:

- **Fully survives, cheap, should be automatic:** checking and correctly tagging full/limited
  range before export; adding a small, deliberate layer of grain/dither to any near-black
  sequence before final compression; running a waveform or false-colour check on every dark
  shot before it leaves the edit; keeping at least one clearly brighter element in frame for any
  shot meant to read as "intentionally dark" rather than "underlit."
- **Survives but needs a decision per shot, not a rule:** where to draw the crush/lift line —
  this is a per-shot judgment call about how much shadow detail actually matters to that
  composition, not something a QC script can fully automate (though the script can flag when a
  shot is *close* to clipping so a human makes the call).
- **Survives in principle, weak evidence for the specific numbers:** the platform-compression
  "slightly over-expose, let the re-encode bring it down" workaround. Worth testing empirically
  against our own YouTube/Instagram exports rather than trusting the p-grade forum consensus
  outright.
- **Nothing here dies against our constraints** — this is the one brief in the corpus where "no
  crew, no reshoots" is irrelevant, because the whole subject is what happens to the frame after
  it already exists.

### What our QC script should add

BadCode already runs `scripts/delivery-qc.sh` before upload because of the `camping.mp4` range
bug. Per this brief, the gate should also check:

1. **Colour range tag matches intended range** (full vs. limited) on both the source and the
   export — the exact class of bug that already shipped once. Reject untagged files outright.
2. **A waveform/histogram pass over the darkest sustained region of each shot**, flagging any
   sustained run of pixels sitting at or near 0 (clipped) so a human decides crush-vs-lift rather
   than discovering it after upload.
3. **A bit-depth/banding check on any shot with a long, low-contrast dark gradient** — visually
   or via a banding-detection pass — before it goes through platform compression, since banding
   that is marginal pre-upload can become visible after re-encode.
4. **A grain/dither presence check** on any shot that is near-black and low-detail, since a
   cleanly denoised dark frame is the one most likely to band after compression.
5. **A "bright anchor present" check** — not fully automatable, but worth a manual checklist item
   per the anchoring-theory finding above: does this near-black frame contain at least one region
   clearly brighter than its surroundings, or will it read as broken rather than as dark?

## 4. Contested

No two named practitioners were found disagreeing in this sweep — most of the material here is
either hard technical fact (bit depth, range clipping, compression bit-allocation) where
disagreement isn't meaningful, or single-source/consensus craft convention (crush-vs-lift
targets, platform workarounds) where this sweep did not surface an opposing named voice. Flagging
this honestly rather than manufacturing a contest: the closest thing to a live disagreement is
implicit, not stated by anyone directly —

- **How much grain is "enough":** the dithering/grain literature says any patterned or random
  noise helps break up banding, but grain also costs bits under compression (noise is expensive
  to encode) which can *itself* push an already bitrate-starved dark shot into more macroblocking
  elsewhere in frame. Nobody in this sweep resolved that tension explicitly — it is a real
  trade-off implied by combining the dithering finding and the compression-bit-allocation finding,
  not a claim either source makes on its own.

## 5. Myths — never cite

- **"Just crush the blacks for a moody look" as a universal rule.** It is a legitimate stylistic
  choice for a specific shot, not a technique that is free of cost — it permanently discards
  shadow detail, and doing it by eye without a scope risks doing it further than intended.
- **"More noise reduction/denoising always makes a dark shot look cleaner."** Per the
  dithering/grain finding, aggressive denoising on a near-black gradient can *increase* visible
  banding by removing the very noise that was masking the quantisation steps.
- **"If it looks fine on my monitor it will look fine everywhere."** Per the viewing-environment
  finding, a calibrated dark-room monitor and a glossy phone in daylight are close to opposite
  conditions for judging a near-black image; passing on one tells you little about the other.
- **Any specific IRE number stated as a universal target** (e.g. "shadows must sit at exactly 5
  IRE") — the sources agree on the *direction* (don't let meaningful shadow detail fall to or
  below 0 IRE) but the specific numbers circulating online are house convention dressed as
  physics law.

## 6. Vocabulary worth having

| term | plain-English gloss | what it buys you |
| --- | --- | --- |
| Banding | Visible stepped bands instead of a smooth gradient, from too few tonal steps | Names the specific defect so a colourist or QC pass knows what to look for, distinct from noise or blocking |
| Dithering | Adding small controlled noise before quantisation to break up banding | The standard fix for banding — request it explicitly rather than "make it less blocky" |
| Macroblocking | Visible square/rectangular blocks from over-aggressive compression | Names the compression-specific defect, distinct from banding (a source-signal issue) |
| Crushing (blacks) | Pushing shadow values down to pure black, discarding detail | Lets you say precisely what you don't want ("don't crush the left third of frame") rather than vaguely "make it darker" |
| Lifting (blacks) | Raising the black point so nothing reads as pure black | The opposite move — flatter contrast, but nothing lost; useful when detail matters more than punch |
| Full range / limited range | Whether black=0/white=255 or black=16/white=235 is the video's coding convention | The single most useful two words to say when a delivered file looks washed out or crushed for no visible reason in the edit |
| Waveform monitor | A scope showing luminance values across the frame as a graph | Turns "does this look dark enough" into a measurable question |
| False colour | A scope that recolours the frame by exposure zone (e.g. blue = near-black/clipped) | Fastest way to see clipped shadow regions across a whole frame at a glance, no math required |
| IRE | The unit false-colour/waveform scopes use for luminance (0 = black, 100 = white) | The shared number a colourist and a QC script can both check against |
| Anchor (lightness anchoring) | The brightest region in a scene the eye uses to judge how dark everything else is | Explains, technically, why "one bright thing in a dark frame" reads as intentional and its absence reads as broken |

## 7. Open questions

- What is our actual platform-side compression behaviour (YouTube upload, Instagram Reels,
  TikTok) for a near-black BadCode-style frame, measured rather than assumed from forum
  folklore? This would require uploading test patterns and measuring the round trip — not done
  in this sweep.
- What grain/dither amount, in practice, best survives our specific pipeline (generated or
  filmed source → Premiere export → platform re-encode) without itself becoming an expensive-to-
  encode noise source that starves bits elsewhere? This is an empirical question for our own
  files, not something the literature answers generically.
- Is there a named colourist on the record (interview, masterclass with attribution, ASC panel)
  making the crush-vs-lift and shadow-protection points in their own voice? This sweep found the
  craft consensus repeatedly but not pinned to an individual — worth a follow-up search
  specifically for ASC.org, Blackmagic's own colourist interviews, or a named DP's own writing.
- Does the anchoring-theory mechanism (Gilchrist) actually predict the *specific* threshold of
  "how much brighter does the anchor need to be" for a frame to read as intentional rather than
  broken? The theory explains the mechanism but this sweep did not find a study translating it
  into a practical contrast-ratio number for image-makers.

## Sources

| URL | what it is | grade of the source itself |
| --- | --- | --- |
| https://pubmed.ncbi.nlm.nih.gov/10560329/ | Gilchrist et al. 1999, "An anchoring theory of lightness perception," Psychological Review | primary, peer-reviewed |
| https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2635063/ | Howe et al. 2007, double-anchoring theory extension/commentary | primary, peer-reviewed |
| https://us.ktcplay.com/blogs/support-tips/color-banding-bit-depth-explained | Bit-depth/banding explainer | content-mill (cited for restating textbook DSP fact only) |
| https://www.anisopteragames.com/how-to-fix-color-banding-with-dithering/ | Dithering technique explainer | practitioner (games/graphics engineering) |
| https://www.lighterra.com/papers/videoencodingh264/ | H.264 encoding settings technical paper | practitioner/technical reference |
| https://forum.doom9.org/archive/index.php/t-107236.html | Forum thread on blocking in dark areas | practitioner forum (single anecdote, p-grade on its own) |
| https://www.soundandvision.com/content/video-dynamic-range-and-color-space | Full range vs limited range explainer | trade press |
| https://community.adobe.com/t5/premiere-pro/gpu-color-range-16-235-vs-0-255-amp-video-limiter-to-fix-washed-out-export/m-p/11946383 | Adobe community thread, range-mismatch export bug | practitioner forum, corroborates recurring real-world failure |
| https://cinapex.pro/waveform-ire-davinci-resolve/ | Waveform/IRE explainer for DaVinci Resolve | practitioner-technical |
| https://www.hollyland.com/blog/tips/what-is-a-false-color-chart | False colour chart explainer | practitioner/content-mill hybrid |
| https://www.tiktok.com/discover/why-are-my-videos-uploading-darker-on-instagram | Creator discussion of dark-upload compression | content-mill/creator forum, low grade — cited as folklore only |
