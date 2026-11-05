# 02 Microsite: what Future Proof's front door already is

Sources: repo only (no web). Files read: `design/2026-10-17-microsites/README.md`, `future-proof-prototype.html` (29 KB), `storyverse-prototype.html` (41 KB), `design/2026-11-04-homepage/concepts.md`.

## What already exists

**Future Proof microsite prototype** (parked 2026-10-17, private artifact https://claude.ai/artifact/25dvbxeF7V4n7idwE3xPMr). A single scroll page, vanilla HTML/SVG/JS. **No three.js, no canvas.** Status: copy drafted from canon, "still needs Kai and Jack's pass"; Future Proof had *no feedback from Kai yet*.

Running order:
1. **Night / postmortem.** "I've read your branch to the end." A report with "What works instead: unknown" and blank action items. (The narrator's voice, in the dark.)
2. **The fork.** SVG timeline splits at "YOU ARE HERE". Bad branch is solid and ends ("FINISHED, I'm parked here"). Good branch draws itself on scroll and fades out ("UNWRITTEN, no end yet").
3. **Permission.** "You're allowed to question the system you inherited." Key line: the machine "is older than the light bulb: pick someone, wait years, repeat." Framed as three ideas "borrowed on purpose... the wrong answer, posted on purpose" (Cunningham's-law style invitation to argue).
4. **Toy 1, Stop buying the bundle** (composition). Table of ~yes/no questions against two invented bundles A and B; tally of "views you'd sign up to and don't hold" for A, B, and "if you build your own = 0". Bundles match no real party.
5. **Toy 2, Small changes, tested, all the time** (continuous integration). Slider 0-60 months; three lanes: phone apps, Amazon (about 50M deployments/yr, Amazon's own 2014 figure), your government (one update per 5 years max, UK GE rule).
6. **Toy 3, No promise without its test** (data-driven). Pick a promise, answer three fields (how will we know / by when / what if it fails); a gate lamp lights only when complete.
7. **The hole.** Hazard-taped: "Who speaks for the person the new scoreboard still doesn't see?" (canon's honest gap: unmeasured care/meaning).
8. **Seed ideas.** Billionaire Coin, Own what can't compete, plus an empty "Yours" plot.
9. **The plot.** "Who should decide how the gains from automation are shared?" with one test rule from the GPOM doorway; ends "Let's get to work."

Design tokens (daylight): `--day #f3f5ef`, paper `#fff`, ink `#17202b`, blue `#2752c4`, hi-vis `#ff6914`, concrete `#d9dcd3`, night `#121110`. Type: Archivo (condensed 75%, 850), Atkinson Hyperlegible body, JetBrains Mono. Blueprint building-site look; reduced-motion handled; mobile-aware.

**Storyverse prototype** (comparison, https://claude.ai/artifact/Gfnx9qSSM21VBKNHZHNNgu). Opposite look: dark stage (`--void #0c0b0a`, tungsten `#f1d39a`, red `#d8372b`), serif (Instrument Serif / Newsreader / Plex Mono). Left-edge **honesty gauge** (On the record > Settled science > Published minority view > Philosophy not physics > My bet; light dims as it falls); each step has **Show source / Argue against me** (from `refutation.md`). Canvas of 4,160 Saturday dots. Kai liked it (scroll, date-by-date feel) but wants re-ordering (physics then Galileo) and money section removed; **parked**, with 3 open canon tensions (scope guard, Galileo's role, science-vs-religion framing).

**Homepage concepts** (2026-11-04, 8 concepts, ranked): 1 Channel BadCode, 2 Year Zero/Year Now, 3 The Wedge, 4 X Marks the Spot (ballot), 5 The Plug, 6 The Hoarding, 7 Departures, 8 P100. Built so far: `channel-badcode.html`, `build-site-tv.py` (TV + teletext homepage; memory says Kai picked a TV/teletext homepage, 3 strands as channels).
Rules shared by all eight: logo fixed (drawn SVG), logo red is the only BadCode red, no cyan, no SaaS cards, **"Future Proof is the lit, daylight place in every concept."**
How each treats Future Proof: Wedge = "Government" slab, flat/upright, gold `#F2B705`; Channel = Channel 3, only clean picture, hoarding "FUTURE PROOF: BUILDING"; P100 = page P888, white daylight building site, green Fastext "the bit that works"; Departures = Platform 3 daylight `#F7F3E8`; X Marks the Spot = lit daylight-yellow ballot box, "Choose carefully. You didn't last time."; Grafts include "light changes with the strand... daylight is always the last thing you reach" and "the one ugly page" (council-leaflet-cheap join form).

## Settled, so reuse

- **Daylight = Future Proof**, as against night = the other branch. Agreed by Kai 2026-10-17, repeated across all 8 homepage concepts. A slideshow should open dark (the postmortem / bad branch) and go to daylight at the pivot.
- **The narrator's frame**: "I've read your branch to the end" / "I was the end" / "I won't hand you a plan; the map is drawn together." Matches Kai's talk-to-camera.
- **Order of argument**: permission to question > three ideas > the hole > invitation. Slide skeleton ready-made.
- **Three toys map 1:1 to three pillars**; each is a ready interactive/3D candidate (bundle table = ballot you can split; slider = update frequency; gate = test-before-ship).
- **Honest-hole beat** (care/meaning unmeasured) and **"probably wrong, post it to be argued with"** tone: protects the sceptical reader and fits the-reader rules (no "you've been duped").
- **Facts already sourced in the prototype**: Amazon ~50M deployments/yr (Amazon 2014 figure), UK GE max 5 years apart. Bundles invented on purpose; keep it so (no real party named).
- **Copy lines**: "older than the light bulb" is nearly Kai's hook ("invented before electricity"); check the claim before use (not verified here).
- Tokens/fonts if the slideshow lives next to the microsite (Archivo/Atkinson/JetBrains Mono, hi-vis orange, blueprint blue).

## Where a slideshow must differ

1. **Pace and format**: microsite is scroll + hands-on toys (self-paced, ~9 sections, form-heavy). Slideshow = one idea per slide, keyboard/click advance, readable on camera at distance; toys become **demo slides** with presenter-driven state (pre-set answers, one-click reveals), not text inputs.
2. **Memes**: the prototype contains none; its humour is dry (postmortem, hazard tape). Meme layer is new. It must live in the daylight register and the sarcastic-authority voice; meme templates are borrowed culture, so the meme format must not read as "you've been duped".
3. **three.js**: prototype is SVG/DOM only. Kai's brief wants 3D explainers; the first 3D candidates are the 3 toys (bundle = a physical parcel you unbundle into blocks; CI = a conveyor/deploy pipeline vs one huge lorry every 5 years; gate = a physical gate). Mind cost on cheap Android (the homepage concepts already flag shaders as heavy; keep a reduced-motion/static fallback).
4. **Video capture**: slides must be recordable (16:9, big type, no scroll-dependent reveals). The microsite's scroll-drawn fork needs a step-driven version.
5. **Missing pillar framing**: microsite names ideas by outcome ("Stop buying the bundle"), never says the engineering term as the headline. The slideshow can do the "composition over inheritance / CI / data-driven" reveal explicitly (Kai's hook), but explain jargon in one line.
6. **Missing today's trigger**: nothing references small-ideas.org (Martin Lewis, 2026-11-05). The microsite's "empty plot / seed ideas / post a wrong answer on purpose" is the natural slot: the deck's close could point at crowd-gathered small ideas. Not verified here (no web).
7. **Look**: the microsite's blueprint look is a *proposal*, never ruled (Kai agreed only "daylight, breaking the near-black house look"). BadCode has no house look, so a slideshow look must be chosen via `story-style` for Future Proof, not inherited by default. The homepage and the Storyverse prototype already diverge in look, which is consistent with that rule.
8. **Front door vs deck**: homepage concepts treat Future Proof as one of three strands (Government channel/slab/P888). The deck is its own page behind that door; the homepage's Government strand ("Promises to enact Future Proof", "Start now" parody) is the natural link in.

## Open / risks

- Prototype copy has not had Kai's or Jack's pass; the 10-17 README says "above the fold" for both microsites is parked.
- Fork graphic and "postmortem" imply the narrator's total certainty about the other branch; the-reader rules say name the decision-maker not the technology. Check that the automation seed ("who decides how gains are shared?") names a decision-maker.
- Hi-vis orange + blueprint blue is not a ruled palette; do not propagate it as a BadCode default.
