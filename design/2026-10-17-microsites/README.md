# Microsites: Storyverse and Future Proof

*Opened 2026-10-17. Status: **parked, with prototypes**. Kai wants to come back to
this thread; nothing here is canon yet.*

## RESUME HERE

1. Re-read **Kai's feedback** below. The Storyverse **order of the message** is the
   open question. Settle it with Kai before touching any code.
2. Rebuild the Storyverse prototype to the new order. Future Proof had no notes yet.
3. Leave the **above-the-fold** (the opening screen) for later. Kai wants something
   different there, but not yet.

## What this is

Two scroll-driven explainer sites, each one its own world, kept separate from the
main BadCode website. The main site's design is still undecided: Kai is less
convinced by the old 3D fork scene, and "The Ledger" catalogue in
[`../2026-08-07-badcode-website-reset.md`](../2026-08-07-badcode-website-reset.md)
was never built. The audience is sceptical, so honesty is built into the form of
each site instead of being added as a disclaimer.

| Site | Prototype (private artifact) | Source |
| --- | --- | --- |
| Storyverse | https://claude.ai/artifact/Gfnx9qSSM21VBKNHZHNNgu | [`storyverse-prototype.html`](./storyverse-prototype.html) |
| Future Proof | https://claude.ai/artifact/25dvbxeF7V4n7idwE3xPMr | [`future-proof-prototype.html`](./future-proof-prototype.html) |

The HTML files are artifact pages, not `apps/web` code. To update the live
prototype, publish the file again to its artifact URL.

## Directions ruled (Kai, 2026-10-17)

- **Storyverse: a dark stage with an honesty gauge.** A gauge on the stage shows
  how sure the narrator is of each step: *On the record → Settled science →
  Published, minority view → Philosophy, not physics → My bet*. The light dims as
  it falls. Every step has a button: **Show source** or **Argue against me**. The
  second one is drawn from [`refutation.md`](../../docs/stories/storyverse/refutation.md),
  so the confession never appears without its rebuttal, as canon requires.
  - The prototype order was: the Shelf (the history from
    [`telling.md`](../../docs/stories/storyverse/telling.md), apple → 1833 →
    "the split was administered"), then the coin (the physics, falling to "My
    bet"), then the afternoon (money, with the gauge climbing back to "Settled
    economics").
- **Future Proof: daylight, breaking the near-black house look on purpose.** Kai
  agreed: the good branch is the first lit place in BadCode.
  - The order: a postmortem in the dark (blank "what works instead" and action
    items), then the fork (the good branch draws itself as you scroll and fades
    out before it ends), then a blueprint building site with three toys:
    - **Bundle deal**: composition.
    - **Update slider**: continuous testing.
    - **Test gate**: no promise without its test.
  - After that: the hazard-taped **hole** ("who speaks for the person the new
    scoreboard still doesn't see?"), the seed ideas, and the empty plot (write
    one rule, from the GPOM doorway in
    [`future-proof.md`](../../docs/stories/gitpush-origin-master/future-proof.md)).

## Kai's feedback on the Storyverse prototype (2026-10-17, verbatim in spirit)

- **Likes the design.** Likes the scrolling, date-by-date feel, like moving through
  a calendar or timeline.
- **The above-the-fold should be different.** Parked.
- **Remove the money section.**
- **The order should be: here is the physics, here is the science. Then bring in
  Galileo.** *"The Galileo story kind of IS the Storyverse."* The journey went
  away from religion and into science. Science has now run its course. We need to
  put "some of that other stuff back in", in a form that doesn't take the piss.
  The point is the strapline: **the universe is a machine for turning sunlight
  into drama.**
- Kai is juggling a lot and doesn't want a long, deep discussion now. **We come
  back to this.**

## Tensions with canon to resolve when we return

These need a ruling from Kai. Claude must not resolve them silently.

1. **Removing the money section vs the scope guard.** The Storyverse README
   ([`../../docs/stories/storyverse/README.md`](../../docs/stories/storyverse/README.md#scope-guard))
   says: *"A Storyverse piece with no power or money in it is off-brief."* Choices:
   amend that rule, keep a single money beat, or let the microsite be the
   exception.
2. **"Galileo is the Storyverse" vs the Galileo canon.**
   [`docs/stories/galileo/README.md`](../../docs/stories/galileo/README.md) and the
   Storyverse README both call Galileo *"adjacent to the Storyverse, never an
   explanation of it"*. Kai's new framing promotes it to the spine. This needs a
   ruling and then a canon edit.
3. **"Out of religion, into science, now we've run out of science."** The history
   mode in `telling.md` rules that the science-versus-religion war is 1870s
   polemic that we are *correcting*. The Galileo canon says the men who wouldn't
   look were *professors, not priests*. So the journey must be told as *we
   narrowed what counts as knowledge*, never as *science beat religion*.
   "Run out of science" also needs care to pass the test *"could a physicist read
   this without wincing?"*. Science hasn't run out; it goes quiet at one specific
   hole (the measurement problem, the hard problem).

## Prototype facts to keep

- Keynes's "last of the magicians" essay was **read by his brother Geoffrey** at
  the Royal Society's Newton tercentenary in July 1946. Keynes had died in April.
  `telling.md` beat 7 is now corrected.
- Whewell proposed "scientist" in 1833, at the British Association, and put it in
  print in 1834.
- Future Proof's bundles A and B are invented and match no real party. The Amazon
  figure (about 50 million deployments a year) is Amazon's own 2014 number. UK
  general elections must be held at most five years apart.
