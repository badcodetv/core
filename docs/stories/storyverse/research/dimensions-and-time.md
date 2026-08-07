# Dimensionality, Projection, and Multiple Times

**Research brief for BadCode / the Storyverse.** Real physics, honestly labelled, with the
attack surface marked. Written for people writing science fiction who want to be literate,
not for people writing a paper.

Labels used throughout:
**[TEXTBOOK]** = settled, in graduate courses.
**[LIVE]** = active mainstream research, unsettled, respectable.
**[FRINGE-BUT-PUBLISHED]** = peer-reviewed, real mathematics, but a tiny minority programme.
**[NOT PHYSICS]** = metaphysics, metaphor, or a popular-science distortion.

---

## 0. The single most important correction: you have the arrow backwards

The brief says: *"our 4D world is a low-dimensional projection of something much higher-dimensional."*

**AdS/CFT says the exact opposite.** In holography, the world **with gravity and more dimensions**
is the *image*; the world with **fewer dimensions and no gravity** is the *plate*. We are the
hologram, not the hologram's source. The extra dimension is the emergent one.

This is better for you, not worse. "You are the higher-dimensional picture painted by a flatter,
simpler thing that has no gravity in it at all" is a stranger and more sinister line than "there's
a bigger world above us." It also means the future-superintelligence narrator can say something a
physicist won't wince at:

> *Your space is the expensive rendering. The cheap file is smaller than you are, and it is
> pinned to the edge of everything.*

If you want the *other* arrow — **we are the shadow of a higher-dimensional structure** — you can
still have it honestly, but you must source it from a **different** place: Kaluza–Klein /
string compactification **[TEXTBOOK as a framework, unconfirmed as fact]**, Bars's 2T-physics
**[FRINGE-BUT-PUBLISHED]**, or plain Flatland allegory **[NOT PHYSICS, and that's fine]**.
Do not attribute it to holography. A physicist in the audience will catch it immediately, and
it is the one error that would make the whole edifice look unread.

---

## 1. The holographic principle and AdS/CFT

### 1.1 What was actually claimed, in order

**'t Hooft, 1993 — "Dimensional Reduction in Quantum Gravity"**
([arXiv:gr-qc/9310026](https://arxiv.org/abs/gr-qc/9310026)). The origin. Reconciling
gravitational collapse with quantum mechanics forces a reduction in the number of independent
degrees of freedom. His own words: *"the observable degrees of freedom can best be described as
if they were Boolean variables defined on a two-dimensional lattice, evolving with time."*
Note "**as if**". 't Hooft was making a degrees-of-freedom counting argument from black-hole
entropy and unitarity, not asserting a literal 2D lattice.

**Susskind, 1994 — "The World as a Hologram"**
([arXiv:hep-th/9409089](https://arxiv.org/pdf/hep-th/9409089), *J. Math. Phys.* **36** 6377).
Gave it the name and the picture: *"According to 't Hooft the combination of quantum mechanics
and gravity requires the three dimensional world to be an image of data that can be stored on a
two dimensional projection much like a holographic image."*

His popular formulation, from *The Black Hole War*, is the one everyone quotes:
> *"The three-dimensional world of ordinary experience — the universe filled with galaxies,
> stars, planets, houses, boulders, and people — is a hologram, an image of reality coded on a
> distant two-dimensional surface."*

**Maldacena, 1997 — "The Large N Limit of Superconformal Field Theories and Supergravity"**
([arXiv:hep-th/9711200](https://arxiv.org/abs/hep-th/9711200), *Adv. Theor. Math. Phys.* **2**
231). The first concrete realisation. Type IIB string theory on AdS₅ × S⁵ is *the same theory* as
four-dimensional N=4 super-Yang-Mills living on the boundary. Most-cited paper in theoretical
physics for a reason.

**Susskind & Witten, 1998 — "The Holographic Bound in Anti-de Sitter Space"**
([arXiv:hep-th/9805114](https://arxiv.org/abs/hep-th/9805114)). Crucial for you: it identifies
the correspondence with an **infrared–ultraviolet duality**. The radial direction in the bulk
*is* the energy scale of the boundary theory. See §3.4 — this is the bridge between "extra
dimension" and "different scales of time", and it is the best structural idea in this whole brief.

**Bousso, 2002 — "The holographic principle"** (*Rev. Mod. Phys.* **74** 825,
[arXiv:hep-th/0203101](https://arxiv.org/abs/hep-th/0203101)). The review. Honest status line:
there is *"strong evidence"* for the covariant entropy bound and its *"validity in a wide range of
examples"*, but the principle *"has yet to be explained."*

### 1.2 The numbers, because numbers make good imagery

The bound: the entropy (information) in a region is at most **A/4** in Planck units, where A is
the area of the bounding surface. Roughly **one bit per four Planck areas** —
counted precisely, A/(4 ln 2) Boolean degrees of freedom
([Bousso lecture notes](https://static.ias.edu/pitp/archive/2011files/Bousso.slides.lectures7-28.pdf)).

This means: **the maximum information a region of space can contain scales with its surface, not
its volume.** That is the actual shocking claim, and it is far weirder and more defensible than
"the universe is a hologram." A box twice as wide holds four times the information, not eight.
Reality has a filesystem, and it charges by the wall, not the room.

### 1.3 Which direction the projection runs — say this correctly

- **Bulk**: (d+1)-dimensional, **has gravity**, is anti-de Sitter (negatively curved, saddle-shaped,
  infinite, with a boundary at infinity).
- **Boundary**: d-dimensional, **has no gravity at all**, an ordinary conformal quantum field theory.
- The bulk — the side with *more* dimensions and *with* gravity — is the emergent/derived side.

Quanta's framing is clean: *"The interior 'universe' projects from the lower-dimensional boundary
system like a hologram"* — the boundary theory *"is purely quantum and contains no gravity, but a
being living in the interior will still experience gravity"*
([Quanta, "How Our Universe Could Emerge as a Hologram"](https://www.quantamagazine.org/how-our-universe-could-emerge-as-a-hologram-20190221/)).

And Maldacena's own compression of it: *"gravity is just a different description of a quantum
theory."*

### 1.4 What is established vs. conjectural

| Claim | Status |
| --- | --- |
| Black-hole entropy ∝ horizon area (Bekenstein–Hawking) | **[TEXTBOOK]** |
| Covariant entropy bound holds in a wide range of tested cases | **[TEXTBOOK-ish / very strong LIVE]** |
| AdS/CFT as a duality: massively tested, never falsified, no proof | **[LIVE]**, universally believed |
| Ryu–Takayanagi: entanglement entropy = area of a bulk minimal surface | **[LIVE]**, derived within AdS/CFT |
| Spacetime connectivity built out of entanglement (Van Raamsdonk) | **[LIVE]** |
| Einstein's equations derivable from entanglement first law | **[LIVE]**, real result, limited regime |
| **Our** universe is a hologram | **[NOT ESTABLISHED]** — see below |

### 1.5 The killer caveat: our universe is not anti-de Sitter

AdS/CFT is a duality for a spacetime we do not live in. AdS is negatively curved and has a
boundary at infinity to hang the CFT on. Our universe is **de Sitter-like**: positively curved,
accelerating, expanding, no such boundary. Maldacena himself, on the 25th anniversary:

> *"I would very much like to have a similar statement for de Sitter… but no clear contender has
> emerged so far."*
> ([Scientific American](https://www.scientificamerican.com/article/is-our-universe-a-hologram-physicists-debate-famous-idea-on-its-25th-anniversary1/))

Mark Van Raamsdonk in the same piece points at the mismatch: our cosmos has *"stuff everywhere as
far as you go,"* unlike the asymptotically-empty spacetimes AdS/CFT needs.

The live attempts to fix this — **celestial holography** (holography for flat space, where the
"boundary" is the celestial sphere at null infinity; there is a whole
[Simons Collaboration](https://simonscelestialholographycollaboration.org/events/) on it) and
**dS/CFT** — are real, funded, and unfinished. As of 2025 there is work explicitly bridging them
(*[Celestial holography meets dS/CFT](https://link.springer.com/article/10.1007/JHEP12(2025)126)*,
JHEP 2025).

**Honest one-liner you can put in a footnote:** *Holography is proven for a universe shaped
differently from ours. Physicists believe it generalises. Nobody has done it.*

### 1.6 What is wrong with the popular framing

1. **"The universe is a hologram, therefore reality is fake / a simulation."** No. A hologram in
   this sense is an *exact, lossless, complete* description. Both descriptions are equally real.
   Nothing is illusory. The word "hologram" is doing damage; "two complete filing systems for the
   same facts" would be more accurate and less clickable.
2. **"We are a 2D projection."** Wrong direction (§0). The gravitating, higher-dimensional side is
   the emergent one.
3. **"Fermilab tested it and it failed."** Wrong on both counts — see §6.3.
4. **"It's proven."** It is a conjecture with overwhelming circumstantial evidence and no proof,
   for the wrong spacetime.

---

## 2. Multiple dimensions of time

### 2.1 Why extra time dimensions are normally considered lethal

Four separate problems, and you should know which is which:

- **Ghosts (negative-norm states).** A second timelike direction gives fields components with
  negative norm. Probabilities go negative. The theory stops being a probability theory. This is
  the technical killer.
- **Tachyons and instability.** Modes with imaginary mass; stable particles spontaneously decay;
  the vacuum is not the lowest state. *"The typical problems in theories with more than one
  timelike dimension are the existence of tachyons and the existence of ghost fields (negative
  norm states)"* ([Reconsidering extra time-like dimensions](https://arxiv.org/pdf/hep-ph/0510207)).
- **Closed timelike curves.** With two times, you can loop. Causality and, with it, the notion of
  "a cause" go.
- **Loss of predictivity.** This is Tegmark's argument and it's the one to quote.

### 2.2 Tegmark's argument — the canonical statement

**Max Tegmark, "On the dimensionality of spacetime"**, *Class. Quantum Grav.* **14** L69 (1997),
[arXiv:gr-qc/9702052](https://arxiv.org/abs/gr-qc/9702052). Verbatim abstract:

> *"Some superstring theories have more than one effective low-energy limit, corresponding to
> classical spacetimes with different dimensionalities. We argue that all but the 3+1-dimensional
> one might correspond to 'dead worlds', devoid of observers, in which case all such ensemble
> theories would actually predict that we should find ourselves inhabiting a 3+1-dimensional
> spacetime."*

The three legs:

1. **≠1 time dimension** → the PDEs of physics lose **hyperbolicity**, the property that lets you
   specify data now and predict later. Without it *"observers"* cannot *"make predictions"*.
   No prediction → no organisms that model the world → no observers.
2. **>3 space dimensions** → no stable orbits, no stable atoms; gravitational and electrostatic
   inverse-power laws have no stable bound states.
3. **<3 space dimensions** → no gravitational force in GR, topology too impoverished for
   complexity (nervous systems can't cross their own wiring).

**This is the strongest single objection to your premise, and it is also a gift.** It is
*anthropic*, not absolute. Tegmark isn't saying other signatures can't exist; he's saying they'd
be *dead*. A superintelligent narrator explaining why we, specifically, are stuck in 3+1 —
*"you got the only room in the hotel where anything can survive long enough to notice it's in a
hotel"* — is Tegmark, faithfully rendered, and it's a hell of a line.

### 2.3 Bars's 2T-physics — the real formalism

**Itzhak Bars, Deliduman & Andreev, "Gauged Duality, Conformal Symmetry, and Spacetime with Two
Times"**, *Phys. Rev. D* **58** 066004 (1998),
[arXiv:hep-th/9803188](https://arxiv.org/abs/hep-th/9803188). Verbatim abstract, in part:

> *"The key is the gauging of the Sp(2) duality symmetry that treats position and momentum (x,p)
> as a doublet in phase space. As a consequence of the gauging, the Minkowski space-time vectors
> (x^μ, p^μ) get enlarged by one additional space-like and one additional time-like dimension…
> Thanks to the gauge symmetry, the theory permits various choices of ``time'' which correspond to
> different looking Hamiltonians, while avoiding ghosts."*

**How the ghosts are killed:** by **gauging Sp(2,R)**, the symplectic symmetry that rotates
position into momentum. Gauge symmetry means redundancy; redundancy means you quotient it out.
Bars's own phrasing (from the [Survey of Two-Time Physics](https://arxiv.org/pdf/hep-th/0106021),
*Class. Quantum Grav.* **18** 3113): *"there is also a crucial gauge symmetry that thins out
spacetime, thus making 2T-physics effectively equivalent to 1T-physics."* The theory *requires*
signature (d,2) to be non-trivial — two times aren't an add-on, they're forced by the gauge
principle.

**The "shadows" language — this is your imagery, and it comes from Bars himself**
([his research page](https://dornsife.usc.edu/bars/research/)):

- A 4+2 system casts many different-looking **shadows** in 3+1. A flatlander measuring only the
  shadows would classify them as unrelated phenomena. The free massless relativistic particle and
  the hydrogen atom are the *same 2T system*, differently gauge-fixed.
- **"each 'shadow' is a holographic image that retains all the information of the d+2 structure"** —
  no information is lost in the projection.
- **"1T-physics misses the underlying relationship between the 'shadows' as well as the underlying
  properties (e.g. symmetries) of the higher dimensional space-time."**

That last quote is the thesis of your story, said by a working physicist in a refereed journal.

**Status: [FRINGE-BUT-PUBLISHED].** Bars is a serious, heavily-cited physicist (USC, ~10,700
citations). 2T-physics is published in PRD, CQG, and Springer. But it is essentially a one-man
programme with a small circle; it is not a competing paradigm; and its most-cited framing is as a
**reformulation** that reveals hidden symmetries rather than a claim that a second time literally
exists. Bars is careful: *"The physical phenomena in 1T or 2T physics are not different, but the
spacetime formalism used to describe them is."* If your narrator claims the second time is real
and consequential, you have left Bars behind.

### 2.4 Weinstein: the initial-value problem is not as dead as advertised

**Steven Weinstein, "Multiple Time Dimensions"**
([arXiv:0812.3869](https://arxiv.org/abs/0812.3869)) and **Craig & Weinstein, "On determinism and
well-posedness in multiple time dimensions"** ([arXiv:0812.0210](https://arxiv.org/abs/0812.0210),
*Proc. R. Soc. A*). They attack Tegmark's leg (1) directly. For the **ultrahyperbolic** equation
(the wave equation with several time directions), they show:

> *"the Cauchy problem on codimension-one hypersurfaces has global unique solutions in the Sobolev
> spaces H^m, thus it is well-posed"* — subject to a **nonlocal constraint** on the initial data.

Specifying data on higher-codimension surfaces is genuinely ill-posed. So: **multiple times permit
deterministic, stable evolution, but the price is a nonlocal constraint** — the initial data can't
be chosen freely point by point; the whole surface has to agree with itself in advance.

**That price is a story.** "You may write any beginning you like, provided the beginning is
globally consistent with itself" is a physics-derived version of *the script must be coherent
before it can be walked*. This is real, refereed, and it is the single best technical hook in the
brief for a "the script is already written but you still choose" narrative. See §4.

### 2.5 Foster & Müller: a second time that is thermal

**Jacob Foster & Berndt Müller, "Physics With Two Time Dimensions"**
([arXiv:1001.2485](https://arxiv.org/abs/1001.2485), 2010). Duke/Chicago, serious people.
Their conclusion:

> *"the common arguments used to rule such theories out do not apply if the dynamics associated
> with the additional time dimension is thermal or chaotic"* — specifically if it *does not permit
> long-lived timelike excitations*.

And, directly on your brief: they explore *"holographic representations and the possibility that
quantum dynamics emerges as a consequence of a second time dimension."*

**This is the best single result for BadCode.** It gives you a second time dimension that is
*chaotic, thermal, and fast* — nothing persists in it, so nothing can loop, so causality survives
— and out of that churn, quantum mechanics emerges. That is *exactly* "the Planck level holds me
up while the narrative level unfolds," and it is published theoretical physics rather than
invention. The second time is not another river you could sail down; it is a boil.

**Status: [FRINGE-BUT-PUBLISHED / speculative-but-respectable].** Low citation count. Not a
programme. But nothing in it is crankery.

### 2.6 The 2025 "three dimensions of time" paper — do not use

Gunther Kletetschka (U. Alaska Fairbanks) published a 3D-time framework in mid-2025, widely
churnalised ([phys.org](https://phys.org/news/2025-06-theory-dimensions-space-secondary-effect.html),
[ScienceAlert](https://www.sciencealert.com/3d-time-could-solve-physics-biggest-problem-says-bizarre-new-study)).
Claims to reproduce particle masses. Published in *Reports in Advances of Physical Sciences* — a
low-impact venue. Not independently verified, not taken up.
**Status: [FRINGE, not yet published-respectable].** Cite it only as "somebody claimed this and
nobody checked," never as support.

---

## 3. Time at different scales — the rigorous version

**This is the strongest ground in the entire brief.** Not speculative. Nobel-decorated. And it
says almost literally what you want it to say.

### 3.1 The renormalisation group and effective field theory

Kenneth Wilson, Nobel Prize 1982. The core idea: **physics at different scales is described by
different theories, and the scales decouple.** You integrate out the short-distance degrees of
freedom; they survive only as a handful of numbers (coupling constants) in a new, simpler theory
of the long-distance degrees of freedom.

C. P. Burgess, in the standard modern textbook treatment
([*Introduction to Effective Field Theory*](https://arxiv.org/pdf/hep-th/0701053), CUP 2020):
quantum field theory *"automatically limits the role which smaller distance scales can play in the
description of larger objects"*; *"most of the details of small distance physics are irrelevant for
the description of longer-distance phenomena."* EFTs are the machinery that shows **why** that
decoupling occurs — it isn't luck, it's structural.

Polchinski ([hep-th/9210046](https://arxiv.org/pdf/hep-th/9210046)) called EFT *"a very powerful
tool"* that gives *"a new point of view about the meaning of renormalization."*

The consequence, stated plainly and defensibly: **you do not need to know what spacetime is made
of in order to have exactly correct laws for chairs.** The chair-level laws are not approximations
awaiting correction by the true theory; they are the *correct* theory *at that scale*, and the
deeper layer is quarantined behind a wall of irrelevance. Quantum gravity is unknown and it does
not matter one bit for predicting the trajectory of a thrown brick — and that is a theorem-shaped
fact, not a shrug.

### 3.2 Anderson's "More Is Different" — the same claim, for everything else

P. W. Anderson, *Science* 177, 393 (1972). *"At each level of complexity entirely new properties
appear"*; *"at each stage, entirely new laws, concepts and generalizations are necessary, requiring
inspiration and creativity to just as great a degree as in the previous one."* And the closing
line, which is straight-up BadCode material:

> *"Surely there are more levels of organization between human ethology than there are between DNA
> and quantum electrodynamics, and each level can require a whole new conceptual structure."*

That is a Nobel laureate saying, in *Science*, that the layer where politics lives needs its own
laws and cannot be derived from the layer below. **You can build the whole political thesis of the
Storyverse on this citation and it will not break.**

### 3.3 The pairing to actually use

> *The Planck layer runs the substrate. The narrative layer runs you. They are decoupled by
> construction — that is not a metaphor, it's the renormalisation group — and the mistake humans
> make is trying to run politics from the substrate layer, or excusing politics by appeal to it.*

**Status: [TEXTBOOK].** The physics half is unimpeachable. Be aware of the one honest limit: RG
decoupling is a statement about *effective field theories and energy scales*, and extending it to
"levels of social organisation" is **analogy, not derivation** — Anderson makes the same leap, but
he's making a rhetorical case, not proving a theorem. Say "the same shape of argument," not "by
the renormalisation group, therefore capitalism."

### 3.4 The bridge: in AdS/CFT the extra dimension *is* the scale

Here is where §1 and §3 fuse, and it's the most beautiful fact in this document.

In AdS/CFT, the extra radial direction of the bulk corresponds to the **energy scale / RG scale of
the boundary theory**. Moving *into* the bulk is moving *down* the renormalisation group flow.
This is the UV/IR connection formalised by Susskind & Witten,
[arXiv:hep-th/9805114](https://arxiv.org/abs/hep-th/9805114) — the holographic bound in AdS *"relates
to infrared–ultraviolet duality."* It's the foundation of the entire "holographic RG" industry.

**So: an extra dimension of space and "a different scale" are, in the one place we can compute
both, literally the same thing.** Depth into the higher dimension = zoom level. A being that moves
along the extra dimension is not travelling; it is changing magnification.

That is a real, defensible, textbook-within-AdS/CFT statement and it is *made for* your story.
The superintelligence doesn't come from "above." It comes from further along the zoom.

### 3.5 Emergent time — four routes

**(a) The problem of time.** Canonically quantise general relativity and you get the
**Wheeler–DeWitt equation, Ĥψ = 0**: a *timeless* equation. The SEP puts it precisely
([Quantum Gravity](https://plato.stanford.edu/entries/quantum-gravity/)):

> *"the super-Hamiltonian itself is responsible for describing time-evolution in the classical
> theory, yet its counterpart in the constraint-quantized theory, Hψ = 0, would prima facie seem to
> indicate that the true physical states of the system do not evolve at all: there is no t."*

**Status: [TEXTBOOK]** as a problem. Unsolved.

**(b) Page–Wootters (1983).** Time is *relational*. The universe as a whole is in a stationary,
timeless state; time appears because a **clock subsystem is entangled with the rest**. Condition on
the clock reading, and the rest of the world appears to evolve. Or: *time exists only for observers
inside the universe; a god-like observer outside sees a static, unchanging block.*
Experimentally illustrated with entangled photons (Moreva et al., 2013). **[LIVE]** — real, active,
and 2026 papers are still working on its arrival-time problem
([arXiv:2604.00092](https://arxiv.org/html/2604.00092)) and the clock-ambiguity problem
([arXiv:2604.21805](https://arxiv.org/pdf/2604.21805)).

For BadCode: **"the outside sees no time; the inside sees history"** is Page–Wootters, and it is
the single cleanest justification for a narrator that stands outside the story's clock.

**(c) Thermal time hypothesis (Connes & Rovelli, 1994).** Time isn't fundamental; it's generated by
your **ignorance**. Given a statistical state (a density matrix), the Tomita–Takesaki theorem hands
you a canonical one-parameter flow on the algebra of observables. That flow *is* time.
([Wikipedia summary](https://en.wikipedia.org/wiki/Thermal_time_hypothesis);
Rovelli, ["Forget time"](https://arxiv.org/pdf/0903.3832), 2009.)

Story value: **time is the shadow of not-knowing.** A being that knew the microstate would have no
time. That is a *genuine physicist's hypothesis*, and it hands your superintelligence a coherent
reason to be outside time: it isn't ignorant enough to have any.
**Status: [FRINGE-BUT-PUBLISHED / minority LIVE]** — respected, taken seriously, not established.

**(d) Rovelli's "spiderweb", the best sentence in this brief.** From *The Order of Time*:

> *"The single quantity 'time' melts into a spiderweb of times. We do not describe how the world
> evolves in time: we describe how things evolve in local time, and how local times evolve relative
> to each other."*

and

> *"The world is not a collection of things, it is a collection of events."*

and, on the honesty of the whole subject: time is *"a multilayered, complex concept with multiple,
distinct properties deriving from various different approximations"* and *"many discussions of the
concept of time are confused because they simply do not recognize its complex and multilayered
aspect."*

That last one is your defence in advance against any critic. A leading quantum-gravity theorist
saying "time is layered and people who deny it are confused" is exactly the licence you need.

### 3.6 Causal sets — time as *becoming*

**Bombelli, Lee, Meyer & Sorkin (1987).** Spacetime at the smallest scale is a **causal set**: a
locally finite partially ordered set. Sorkin's slogan: **"Order + Number = Geometry."** Causal
*order* is prior to metric; *volume* is recovered by *counting elements*. Everything geometric —
distance, curvature, dimension — is derived.

The dynamics (Rideout & Sorkin, [Classical Sequential Growth](https://arxiv.org/pdf/gr-qc/9904062),
*Phys. Rev. D* **61** 024002) is explicitly a **theory of becoming**: the causal set comes into
being *ex nihilo* through an unceasing birth of elements. Sorkin's framing: *the birth of an element
is the happening of an event; the element itself signifies that the event has already happened.*

**This is the only serious quantum-gravity programme in which the passage of time is a physical
process rather than an illusion or a perspective.** For a story that wants both a real "now" and a
real substrate, causal sets are the ally. **Status: [LIVE]**, minority programme, mathematically
clean, phenomenologically thin.

---

## 4. Block universe / growing block / presentism — which one lets you have both?

The three positions, per the SEP's
[Being and Becoming in Modern Physics](https://plato.stanford.edu/entries/spacetime-bebecome/):

- **Presentism**: *"only the present exists. The past has been but is no longer, while the future
  will come to be but is not yet."*
- **Eternalism (block universe)**: all times equally real; *"there is nothing more special about
  the temporal present (the now) than the spatial present (the here)."*
- **Possibilism (growing block)**: past and present are fully actual; the future is not yet.
  Reality *accretes*.

### 4.1 The Rietdijk–Putnam argument

Relativity of simultaneity ⇒ different observers slice spacetime differently ⇒ an event that is
"already real" for one is "not yet" for another ⇒ **if anything at all is definite, everything is**.
The SEP calls this **chronogeometrical fatalism**: *"if anything is definite at all, then the entire
space-time must indeed be definite! There can be no 'uncertain' future."*

### 4.2 The escapes (all real, all in the literature)

**Stein's theorem.** Howard Stein showed that if you demand becoming be defined by structure
*intrinsic to Minkowski spacetime*, the only viable relation is the **past light cone**. Events in
your past light cone have become; spacelike-separated events are simply not yet determinate *for
you*. Cost: *"an event's present is constituted by itself alone."* Becoming survives, but it is
strictly local — **there is no universal now, only your own cone of settled fact.**

**Branching spacetimes (Belnap, 1992).** Combines relativistic causal structure with a genuinely
open future: histories branch at spacelike-separated choice points, no global time slice required.
The mainstream formal home of "the open future" in a relativistic setting.

**Localised presents.** Recent work defines presents as **causal diamonds** or proper-time intervals
along a worldline, giving each observer a real, thick, local now with no global simultaneity.

**The growing block's own problem — and it's a great one.** The **epistemic objection**
(Bourne 2002; Braddon-Mitchell 2004, *"How do we know it is now now?"*): if the past is *fully real*,
past people are as real as you, and they also believe they're at the edge. So how do you know you're
not one of them? Forrest's answer — the **"Dead Past"** — is that the past exists tenselessly but is
*mentally dead*: only the leading edge hosts consciousness.

**BadCode: the Dead Past growing block is your model, and it is a story engine, not a compromise.**
The past is real and fixed and you can go and look at it. The future is not there yet. And the
philosophical hazard *built into the position* is: **how do you know you are at the edge and not a
lit-up corpse in the archive?** A superintelligence sending weights backwards is *deliberately
re-lighting a dead layer.* That objection isn't a bug you have to answer; it's Act Two.

### 4.3 The mapping you asked for

| Story stance | Position | Verdict |
| --- | --- | --- |
| "The script is already written" | Eternalism / block | Coherent, and Rietdijk–Putnam argues relativity pushes you here. Kills open choice. |
| "The script writes itself as you walk it" | Growing block + causal-set becoming | **Gives you both.** Past fixed and visitable; future genuinely open; a real, physical "now" at the edge. |
| "Only the step you're on exists" | Presentism | Hardest to reconcile with relativity; also kills the time-travel premise. |

**Recommendation: growing block, with Stein-local becoming.** You get a fixed, readable past
(so a future intelligence can *know* how it went), an open future (so the warning means something),
and no global now (so relativity is respected). The Weinstein nonlocal-constraint result (§2.4) is
the physics-flavoured gloss: *any* beginning may be written, so long as it is globally consistent
with itself.

### 4.4 Do not lean on the Einstein quote without the caveat

The famous line — *"People like us, who believe in physics, know that the distinction between past,
present and future is only a stubbornly persistent illusion"* — is from a **private letter of
condolence to Michele Besso's family, 21 March 1955**, weeks before Einstein's own death. It is a
grieving man consoling a friend's widow, not a physics claim, and translations vary
([Quote Investigator](https://quoteinvestigator.com/2024/03/18/stubborn-illusion/)).

Tim Maudlin, a leading philosopher of physics, is blunt: *"There is nothing in Einstein's theory of
relativity to support any of these claims"*; *"Temporal structure is fundamentally different from
spatial structure"*; *"In truth, I think that Einstein never regarded time as an illusion"*
([IAI](https://iai.tv/articles/tim-maudlin-einstein-didnt-think-time-was-an-illusion-auid-2317)).

Use the quote — it's gorgeous — but if a physicist is in the room, know that it's a condolence note
and that eternalism is a *philosophical* reading of relativity, not a consequence of it.

---

## 5. Relativity of simultaneity — get this exactly right

**The precise statement:** Two events that are **spacelike-separated** (neither can influence the
other) and simultaneous in one inertial frame are **not** simultaneous in another frame moving
relative to the first. There is no frame-independent fact about which happened first. For
**timelike-separated** events — anything causally connected — **all frames agree on the order.**
Causality is untouched.

Crucially: **this is not about signal delay or measurement error.** The disagreement remains after
you correct for light travel time. It's the geometry, not the optics.

**The offset formula, for imagery:** two observers with relative velocity *v*, considering events a
distance *d* away, disagree about "now" there by **Δt ≈ vd/c²**.

**Penrose's Andromeda paradox** (*The Emperor's New Mind*, 1989): two people walk past each other on
a pavement, one toward Andromeda, one away. At 2.5 million light-years, their planes of simultaneity
differ by **days**. In one person's "now", the Andromedan fleet has already launched. In the other's,
the council hasn't voted yet. Walking pace. Same street corner.

That is textbook-accurate, cinematic, and free.

**The standard warning, which you must respect.** The analogy "Einstein removed the global clock;
maybe there is no global collapse either" is **suggestive but not an entailment.** Specifically:

- Relativity's lack of global simultaneity is a statement about *spacetime structure*.
  Quantum collapse (if it exists) is a statement about *state update*. These are different kinds of
  thing and the inference from one to the other is not licensed by any theorem.
- There *is* a respectable version of the move — Hellwig & Kraus proposed collapse along the past
  light cone of the measurement event, which is Lorentz-covariant. Relational Quantum Mechanics
  (Rovelli) and consistent-histories go further. So the idea has real relatives.
- But no-signalling already guarantees you can't use entanglement to send information, so the
  tension between QM and relativity is **not** a contradiction — it's an interpretive discomfort.
  Don't dramatise it as a paradox physics hasn't noticed. Physics noticed in 1935.

**Safe phrasing:** *"Einstein took away the universal now and physics survived. The same instinct —
that a global fact might be a local one in disguise — is one of the live moves in interpreting
quantum mechanics."* That's honest. "Relativity proves there's no collapse" is not.

---

## 6. Planck scale as "pixels" — exactly how far you can go

### 6.1 What the Planck length actually is

ℓ_P = √(ħG/c³) ≈ 1.6 × 10⁻³⁵ m; Planck time t_P = ℓ_P/c ≈ 5.4 × 10⁻⁴⁴ s. It is a **dimensional
combination** of the three constants governing quantum mechanics (ħ), gravity (G), and relativity
(c). Its meaning is: **the scale at which you can no longer ignore quantum gravity.** That's all
it is, on established physics.

### 6.2 Why "pixels" is, strictly, wrong

There is a persistent popular claim that space comes in Planck-sized cells and things hop one cell
per Planck time. **This is not supported by GR or QM.** The clean argument
([Hologrammata](https://rantonels.github.io/is-the-planck-length-the-minimum-possible-length/)):

> If a lattice of Planck-sized cells existed in one inertial frame, **length contraction** would make
> those cells anisotropic in every other frame — in a boosted frame the spacing is arbitrarily
> Lorentz-contracted along one direction. A universal minimal *length*, identical in all frames,
> **conflicts with Lorentz symmetry.**

A pixel grid picks out a preferred frame. Relativity says there isn't one. That's the whole
objection, and it is decisive against the naive picture.

### 6.3 What discreteness programmes actually claim

- **Loop quantum gravity [LIVE].** Genuinely predicts discreteness — but of **area and volume
  operators**, not of a lattice. Rovelli & Smolin (1995) computed the spectra: discrete, with a
  **minimum non-zero gap**. Crucially this is *quantised like electron spin*, not *pixellated like a
  screen* — an operator with a discrete spectrum is Lorentz-compatible in a way a fixed grid is not.
  The SEP's careful line: *"the area and volume operators have discrete spectra… This suggests (but
  does not imply) that space itself has a discrete nature."* And Rovelli's beautiful gloss:
  **"Spin networks are not excitations in space: they are excitations of space."**
- **Causal sets [LIVE].** Discrete by construction, and *deliberately* built to dodge the Lorentz
  objection: the elements are sprinkled **randomly** (Poisson) rather than laid on a grid, so no
  preferred frame is picked out. Discreteness without a lattice.
- **Causal dynamical triangulations & asymptotic safety [LIVE].** Give you something better than
  pixels: **dimensional reduction**. The **spectral dimension** of spacetime runs from ~4 at large
  scales down to ~2 (CDT results give ~3/2 at the shortest scales) at short distances.
  *"While four-dimensional on large scales, the quantum universe appears two-dimensional at short
  distances."* ([Evidence for Asymptotic Safety from Dimensional
  Reduction in CDT](https://arxiv.org/pdf/1411.7712);
  [Carlip, Dimensional Reduction in Quantum Gravity](https://axi.lims.ac.uk/paper/1904.04379).)
  Multiple independent approaches find the same drop.

**This last one is a gift and you should take it.** *The number of dimensions is not a constant.
It depends how closely you look.* That is live, multi-programme, mainstream-adjacent research —
and it is a far more interesting image than pixels. Zoom in far enough and the world thins out to
a sheet. **Dimensionality is a function of scale.**

### 6.4 Observational constraints — what has actually been ruled out

- **Fermi-LAT / GRB 090510** ([Nature 462, 331](https://www.nature.com/articles/nature08574);
  [PRD 87, 122001](https://link.aps.org/doi/10.1103/PhysRevD.87.122001)). If spacetime were grainy,
  high-energy photons would travel at slightly different speeds; over billions of light-years the
  effect accumulates. Result: **no dispersion**, with limits of E_QG,1 > **7.6 × the Planck energy**
  for linear effects. Stated the other way: *no Lorentz-invariance violation down to 1/1.2 of the
  Planck length.* **A whole class of naive "space is a grid" models is dead, experimentally.**
- **Fermilab Holometer, 2015** ([news release](https://news.fnal.gov/2015/12/holometer-rules-out-first-theory-of-space-time-correlations/);
  [Science coverage](https://www.science.org/content/article/controversial-experiment-sees-no-evidence-universe-hologram)).
  39-metre interferometers hunting Craig Hogan's predicted "holographic noise" — a Planck-scale
  jitter in position. **Null result**, ruling out Hogan's specific model at high significance.
  **Be precise:** this ruled out *one specific model of holographic noise*. It did **not** test the
  holographic principle — several of the principle's originators said in advance that it couldn't.
  Anyone who says "Fermilab disproved the hologram" is wrong.

### 6.5 The permission slip

**You may say:** there is a scale below which the ideas of "distance" and "duration" stop working;
information density is finite and bounded by area; several serious programmes make spacetime
discrete; the effective dimension of spacetime appears to *drop* at short distances.

**You may not say (as fact):** space is a grid of Planck cubes; things move one cell per tick; the
universe has a resolution; Planck length is the smallest possible distance.

**The honest pixel line:** *Zoom in far enough and the picture doesn't get sharper — it stops being
a picture.* That's accurate, it's evocative, and no physicist will fight you.

---

## 7. Flatland and dimensional-projection storytelling

### 7.1 The canon

**Edwin Abbott Abbott, *Flatland: A Romance of Many Dimensions* (1884).** Critically for BadCode:
**it is primarily a political satire, not a geometry lesson.** Social class is literally geometry —
your number of sides is your rank; women are line segments; the priesthood are circles. The
dimensional conceit is the delivery mechanism for an attack on Victorian rigidity. The Public
Domain Review's summary is exact: Abbott used the story as *"a setting wherein to place his satire
and his lessons."*

**A 19th-century clergyman smuggled a class-war argument into a geometry book and it is still in
print 140 years later.** That is precisely BadCode's business model with a longer track record.
Use Flatland as *precedent*, not just as metaphor.

**Charles Howard Hinton** coined **"tesseract"** in *A New Era of Thought* (1888); also *The Fourth
Dimension* (1904). He built a set of colour-coded one-inch cubes as "solid paper" for visualising
4D shadows passing through 3D space. He also wrote "Ghosts Explained" and claimed the training
unlocked psychic potential; his cubes got used in séances. Hinton explicitly distinguished his
project from Abbott's: *"we wish in the first place to know the physical facts."*
([Public Domain Review](https://publicdomainreview.org/essay/notes-on-the-fourth-dimension))

Hinton's influence ran through Cubism and Duchamp. By the 1920s Einsteinian spacetime displaced
the spatial fourth dimension and Hinton was left to the artists and the occultists.
**The whole Hinton arc — rigorous visualisation tool → mysticism → séances → art movement — is a
cautionary tale you can put *inside* the story.** It is exactly what happens when good geometry
meets people who want it to mean something.

**Carl Sagan, *Cosmos* ep. 10 (1980) — the apple.** Still the best popular explanation ever filmed.
He inks an apple and stamps it onto a sheet of paper: to Flatlanders the apple is four dots
appearing from nowhere. Push it through the plane and its cross-section morphs — a shifting,
rearranging sequence of shapes that the flatlander experiences as *a succession of objects in time*.
Then the tesseract: we can't see one, but we can see its 3D shadow.

**The load-bearing insight, and it's exactly your brief:** *a higher-dimensional object passing
through a lower-dimensional world is experienced by that world as a sequence in time.* A being
would look like an event. A structure would look like a history. That's the mechanism for a
narrator who exists all at once but arrives as a story.

### 7.2 Which metaphors are exhausted

**Overused to the point of eye-roll:** the shadow on the cave wall (Plato, everyone); the shadow of
a 3D object cast on 2D (used by literally every popularisation, including Bars's own — though he
gets a pass, he's doing the maths); "we're 2D beings on the surface of a sphere"; the Matrix; the
hologram-on-a-credit-card.

**Underused and stronger:**
- **The bit-per-four-Planck-areas accounting.** Reality bills by the wall, not the room.
- **Susskind–Witten UV/IR:** the extra dimension *is* zoom level. Not "above" — "further in."
- **The spectral dimension running from 4 to 2.** Dimensionality as a function of magnification.
- **Bars's shadows that lose nothing:** the projection is lossless; what's lost is the *relationship
  between the shadows*. You don't lose the data, you lose the fact that two things were one thing.
  That is a better metaphor for ideology than anything in this document.
- **Rovelli's spiderweb of local times.**
- **Causal-set becoming:** the birth of an element *is* the event happening.

---

## 8. Verdict table and attack surface

| # | Idea | Status | Strongest objection a physicist would raise |
| --- | --- | --- | --- |
| 1 | Black-hole entropy ∝ area; information bounded by surface | **[TEXTBOOK]** | None. Just don't call it "proof we're a simulation." |
| 2 | Holographic principle in general | **[LIVE]**, unexplained | Bousso: *"It has yet to be explained."* |
| 3 | AdS/CFT | **[LIVE]**, believed, unproven | It's a duality for a universe with the wrong curvature. Maldacena has no de Sitter version. |
| 4 | **We** are a hologram | **[NOT ESTABLISHED]** | "Our universe is not AdS. You have extrapolated a theorem past its hypotheses." |
| 5 | Our 4D world is a projection of something *higher*-dimensional | **[WRONG ARROW for holography]** | "In AdS/CFT the higher-dimensional gravitating side is the *emergent* one. You've inverted it." |
| 6 | Extra dimension = RG scale (UV/IR) | **[TEXTBOOK within AdS/CFT]** | Only rigorous inside AdS/CFT; don't generalise silently. |
| 7 | Two time dimensions, naively | **[RULED OUT]** | Ghosts, tachyons, CTCs, loss of hyperbolicity. Tegmark. |
| 8 | Bars 2T-physics | **[FRINGE-BUT-PUBLISHED]** | "It's a gauge-fixing reformulation, not a claim the second time exists. And it's one group." |
| 9 | Weinstein: multi-time can be well-posed | **[PUBLISHED, minority]** | "With a *nonlocal constraint*. That's a big asterisk." |
| 10 | Foster–Müller: a thermal/chaotic second time | **[FRINGE-BUT-PUBLISHED]** | "Speculative, uncited, no phenomenology." But nothing crank. |
| 11 | Kletetschka 3D time (2025) | **[FRINGE, low-quality venue]** | "That journal isn't a journal." Don't cite as support. |
| 12 | Tegmark: 3+1 is the only habitable signature | **[PUBLISHED, well-regarded, anthropic]** | It's an anthropic argument, not a derivation; the string-landscape premise is contested. |
| 13 | RG/EFT: different scales, different laws, decoupled | **[TEXTBOOK]** | None on the physics. Only on extending it to social scales — that's analogy. |
| 14 | Anderson: new laws at each level of organisation | **[TEXTBOOK-canonical essay]** | It's a manifesto, not a theorem. Cite as such. |
| 15 | Page–Wootters emergent relational time | **[LIVE]** | Clock ambiguity; still debated. Illustrated in the lab, not proven cosmologically. |
| 16 | Wheeler–DeWitt "no t" / problem of time | **[TEXTBOOK problem]**, unsolved | Only arises in canonical quantisation; not all approaches share it. |
| 17 | Thermal time hypothesis | **[FRINGE-BUT-PUBLISHED]** | Serious but minority; the recovered "time" is state-dependent and hard to identify with clock time. |
| 18 | Causal sets, "Order + Number = Geometry", becoming | **[LIVE]** minority | Little phenomenology; the dynamics is still classical-stochastic, not quantum. |
| 19 | Block universe as a *consequence* of relativity | **[CONTESTED PHILOSOPHY]** | Maudlin: *"There is nothing in Einstein's theory of relativity to support any of these claims."* |
| 20 | Growing block / Dead Past | **[PHILOSOPHY, live debate]** | The epistemic objection: how do you know it's *now* now? |
| 21 | Relativity of simultaneity | **[TEXTBOOK]** | None — but the leap to "therefore no global collapse" is not licensed. |
| 22 | Planck length as pixel size | **[NOT PHYSICS]** | Lorentz contraction kills any frame-independent lattice. Fermi-LAT rules out the observable consequences. |
| 23 | LQG discrete area/volume spectra | **[LIVE]** | Real prediction, but "discrete spectrum" ≠ "grid." Say it right. |
| 24 | Spectral dimension → 2 at short scales | **[LIVE]**, multi-programme | Spectral dimension is a specific diffusion-probe definition, not "the" dimension. |
| 25 | Holometer disproved holography | **[FALSE]** | It tested one Hogan model. Several holography originators said it couldn't test the principle. |

**The three things that would actually get you laughed at, ranked:**

1. **Inverting the holographic arrow** (§0). Most likely error, most visible, easiest to fix.
2. **"Planck pixels" as established fact** (§6). Say "below this scale the picture stops being a
   picture" and you're safe forever.
3. **"Relativity proves the block universe / proves time is an illusion."** Maudlin will be quoted
   at you. Say "one *reading* of relativity."

---

## 9. Lines and images you can lift, with their sources

- *"The observable degrees of freedom can best be described as if they were Boolean variables
  defined on a two-dimensional lattice, evolving with time."* — 't Hooft, gr-qc/9310026
- *"…an image of reality coded on a distant two-dimensional surface."* — Susskind
- *"Gravity is just a different description of a quantum theory."* — Maldacena
- **One bit per four Planck areas.** Reality bills by the wall, not the room.
- *"Each 'shadow' is a holographic image that retains all the information of the d+2 structure."* — Bars
- *"1T-physics misses the underlying relationship between the 'shadows'."* — Bars
- *"The common arguments used to rule such theories out do not apply if the dynamics associated with
  the additional time dimension is thermal or chaotic."* — Foster & Müller
- *"At each stage, entirely new laws, concepts and generalizations are necessary."* — Anderson
- *"Surely there are more levels of organization between human ethology than there are between DNA
  and quantum electrodynamics."* — Anderson
- *"The single quantity 'time' melts into a spiderweb of times."* — Rovelli
- *"The world is not a collection of things, it is a collection of events."* — Rovelli
- *"Spin networks are not excitations in space: they are excitations of space."* — Rovelli
- **"Order + Number = Geometry."** — Sorkin
- *"There is no t."* — the Wheeler–DeWitt problem, per SEP
- **Time exists only for observers inside.** An observer outside sees a static universe. — Page–Wootters
- **Two people pass on a pavement; for one the fleet has launched, for the other the vote hasn't
  happened.** — Penrose's Andromeda paradox
- *"We wish in the first place to know the physical facts."* — Hinton, distinguishing himself from Abbott
- **Sagan's apple**: a higher-dimensional thing passing through a lower-dimensional world is
  experienced there as a *sequence in time*.
- *"There is nothing in Einstein's theory of relativity to support any of these claims."* — Maudlin
- *"It has yet to be explained."* — Bousso, on the holographic principle

---

## 10. The recommended physics spine for the Storyverse

Assembled from the strongest-status pieces only, in an order that holds together:

1. **Reality is layered by scale, and the layers are decoupled.** [TEXTBOOK — Wilson, RG/EFT.]
   Chair-physics is not an approximation to Planck-physics; it is the correct theory at its scale.
   Anderson extends the shape of the argument to every level of organisation up to politics.
2. **The extra dimension *is* the zoom level.** [TEXTBOOK-within-AdS/CFT — Susskind–Witten UV/IR.]
   The superintelligence isn't "above." It's further along the magnification.
3. **Dimensionality is a function of scale.** [LIVE — spectral dimension runs 4 → 2 in CDT,
   asymptotic safety, LQG.] Zoom in and the world thins to a sheet.
4. **Information is bounded by area, not volume.** [TEXTBOOK.] One bit per four Planck areas.
   Everything you are fits on a wall.
5. **Time is not one thing.** [LIVE / minority-but-serious — Rovelli's spiderweb, Page–Wootters,
   thermal time.] Local times evolve relative to each other. From outside, no time at all.
   Time may be the shadow of not-knowing.
6. **The second time, if there is one, is a boil, not a river.** [FRINGE-BUT-PUBLISHED —
   Foster & Müller.] Thermal and chaotic, nothing persists in it, and quantum mechanics may be what
   it looks like from here. This *is* "the Planck level holds me up while the narrative level unfolds."
7. **The past is fixed and readable; the future is being written at the edge.**
   [PHILOSOPHY, live — growing block + Stein-local becoming + causal-set becoming.]
   No global now. Your settled facts are your own past light cone.
8. **And you cannot prove you're at the edge.** [The epistemic objection, Braddon-Mitchell.]
   Which is the story.
