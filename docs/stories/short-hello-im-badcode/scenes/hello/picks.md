- **2026-11-12 (Jack):** "#17 Hello, I'm BadCode … lets mess around with this." Media folder Desktop `Youtube Vids\animation\shorts\hello-im-badcode` (same pattern as Same Bench).
- **2026-11-12 (Jack):** who = **mix of both** (open on the future in voice-over, cut to the balaclava figure for the punchline); angle = **deadpan intro**; **9:16, explore looks** (clean room).
- **2026-11-12:** mood board r1 (clean room, 9 looks) https://claude.ai/artifact/YMxBMusYT79tk2XsADbNAL. Balaclava fix pass: B1-c improved; B1-a ring grew round the whole face and B1-b returned the reference image, so the raw stills are on the board (fix after the pick).
- **2026-11-12 (Jack, mood board r1):** C1-a **yes** (blue hour). Figure: "mask is wrong thanks". Future: "please come up with more thanks". Then: "there is a weird old 00s/90s nostalgia, videos, where it is a compilation of happy things from that time. please find stuff like that and that be the vibe of the whole thing … Please clean room it all and research the internet to achieve it."
- **2026-11-12:** my mistake: rounds 1 and 2 briefed a small ring round one eye hole with eyes showing; the brand rule is a large ring round the whole face, the triangle high inside it on the right of the picture, no eye holes. Corrected in README/look.md; figure stills re-fixed with mask-reference.
- **2026-11-12:** mood board r2 (nostalgia) up. Flow edit uploads jammed (stuck overlay, 6 tries incl. flow-operator), so the 3 figure stills were remade from their writers' prompts with ONLY the mask sentences corrected (variations/r2/figure-mask-corrected.json); best of each pair kept.
- **2026-11-12 (Jack):** nostalgia = internet meme edits of the best of those years, not childhood. Research: research/nostalgia-meme-formats.md (~30 formats). Picked to try: Frutiger Aero future, 2026-is-the-new-2016, chill guy from the future, + 'more happy nostalgic meme stuff'. Clean room r3.
- **2026-11-12:** meme round r3 failed the gate after two rewrites only on the mandatory mask wording (brand rule, must match); run anyway from writers/*.json under "rules are a loose guide". Lesson: put the brand mask sentence in preamble.txt so the gate exempts it.
- **2026-11-12 (Jack):** structure ruled: hook (warm, "Hello. I'm from the future.") → figure ("It didn't go well.") → NEW: "real footage of ai data centers and basically evil shit happeing now falshing on screen in a horror compiliation with cinematic music, then the music slows down to nothing and says heres what to do then badcode logo." Button: no words other than "here is what to do next", then the logo.
- **2026-11-12 (Jack):** horror reel = "a combination of all of them in rapid fire" (AI and the machine; climate and disaster; cost of living; war and power). Last line spoken on a black screen: "Here's what to do next." then the logo. Footage researcher running (research/footage-shortlist.md).
- **2026-11-12:** rough cut 1 (24.9 s) on https://claude.ai/artifact/B5f8vmPozGXf7f9CpFNGBP. Reel = 22 shots, 0.5 s each, ordered bright→dark (0.38 s and random order failed the photosensitivity gate; now passes at 3 flashes/s). 9 green real-footage items (docs/footage/README.md) + 8 Flow gap stills (high street, food bank, robots, drone, DC build, missile, pylons, meter). Voice TEMP (Sadaltager), music TEMP (ffmpeg synth), hook A3-a and figure B3-b placeholders.
- **2026-11-18 (Jack): "Hello, I'm BadCode … let's start the script and all the scenes … start everything".** Library
  question: tricks **balaclava** and **real photo (Unsplash)** (he also ticked "nothing from tricks"; read as these two);
  look/sound: **his own meme-edit direction plus synthwave**. Script: **options to pick from** (scene-dialogue: ten
  writers, a judge, three drafts). Voice: **cast options** (voice-casting). Kai's notes still standing: 13 Nov "a very basic
  interpretation … BadCode wouldn't say that", give it character; 17 Nov morning: move away from repetitive narration voices.
- **2026-11-18:** script options round 1 (scene-dialogue, ten writers incl. 'chill guy from the future' and 'meme captions'): three drafts, 1A Receipts, 1B The good part, 1C One place, one task. Page https://claude.ai/artifact/Lvi2jXqY249k52Ss9Ja8x8 (`design/2026-11-18-hello-im-badcode-dialogue-script/`).
- **2026-11-18 (Jack):** "After the footage and all the video stuff, when it cuts to badcode guy, maybe he says something
  like, 'What do you think in your mind, what the worst-case scenario is?… I'll be patiently waiting to correct your
  bullshit' i dont know if this fits but yeah." Added verbatim as a new beat (cut back to BadCode after the reel), two
  drafts on the script page: 1D (then "Here's what to do next." on black) and 1E (his line ends it, then the logo).
- **2026-11-18 (Jack), on the script page:** quoting 1B's hook ("Hello. Enjoy this.") and figure line ("I'm from the
  future. [beat] That was the good part."): "i dont like these parts, i think we will know what to say once we have the
  video so lets start on that proccess thanks". Words wait for the picture; the script page stays as the record (1D/1E
  hold his after-the-reel line). Picture round 1 next: the warm opening from real photos, the figure with the mask reference.
- **2026-11-18, picture + music round 1** (page https://claude.ai/artifact/NcX2aNGxH65LjjMdXs2oxa, spec `r4-picks.json`):
  openings HO1-a..d (from Unsplash photos with no faces), figure FG2-a..c (short mask line) and FG1-a..c (long, comparison),
  music `songs/r1-track/` (4 ideas, 14 takes, players). The 7 first stills rendered but lost their downloads because the Suno
  recording ran on the same browser at the same time (two Playwright clients fight over the download folder); collected
  from the Flow gallery with recipe cards. Lesson: never run two browser scripts at once.
- **2026-11-18 (Jack), the mask wording:** "if the reference image works with this text, I think just do that, because I
  think the problem with polluting stuff before was just the amount of sheer text". Tested: FG2 (short line + the mask photo)
  vs FG1 (the 53-word sentence), three settings: every mask right in both. `docs/brand/balaclava/shared-wording.txt` is now
  the short line; the long one is kept as `shared-wording-long.txt` for prompts with no image. Seen in the test: unsaid
  clothes copy the reference photo's cream suit, so say what BadCode wears.
- **2026-11-18, Jack's round-1 picks (page dump, `feedback/picks-r1/`):** opening **d** (skatepark at sunset); figure: the
  long-sentence **c** (park bench) with "remove the bubbles thanks"; music, no pick: "lets try accoustic guitar synth stuff,
  there has been a few meme like songs for that kind of thing so lets try varied appraoches thanks". And: "fuck around with
  more warm openings and bad code settings. Like, not just the park bench and all that." Round 2: more openings, more
  settings, the bench without bubbles, music r2 (acoustic guitar + synth, meme-song approaches).
- **2026-11-18, picture + music round 2** (same page, https://claude.ai/artifact/NcX2aNGxH65LjjMdXs2oxa): openings HO2-a..f
  (Ferris wheel, dolphins, fireworks, ice-cream van, arcade, mall fountain; Unsplash refs, no faces) beside the picked HO1-d;
  figures FG3-a..g (the bench without bubbles, launderette, video shop, sofa + CRT, kitchen tea, escalator, skatepark bowl;
  short mask line + mask photo, clothes stated); music `songs/r2-track/` (acoustic guitar + synth: freeze-frame prog,
  nylon bossa, folktronica glitch, twinkle emo; gate sent two back once; 60 credits, every Create first time with the new
  workspace retry; 7 takes). Three stills were saved under the wrong names (a late tile picked up as the next result; one
  was a stray old armchair figure, moved to `<media>/moodboard/_rejected/`); re-collected from the gallery.
