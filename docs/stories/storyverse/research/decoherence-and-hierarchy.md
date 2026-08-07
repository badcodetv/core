# How the quantum world becomes the classical world

**Research brief for BadCode — testing the "hierarchical collapse / the set is only rendered where you look" story image against real physics.**

Prepared 2026-08-07. Everything below is labelled: **[T]** textbook, **[L]** live research, **[M]** legitimate but easily misstated, **[X]** not physics. Real quotes, real numbers, inline sources.

---

## 0. The one-paragraph verdict, up front

The physics does **not** support "the universe renders on demand." It supports something better for your purposes and stranger: **the universe is over-rendered.** The environment — air molecules, sunlight, the cosmic microwave background — is measuring everything, everywhere, continuously, on timescales like 10⁻³¹ seconds. Nothing waits for you. What the physics *does* license is (1) that "collapse" as we experience it is the environment's doing, not a mind's; (2) that a single measurement genuinely can settle a whole correlated subsystem at once, and **which** subsystem settles depends on **how** you measure — that part of your image is real; (3) that objectivity is not a global fact but many observers independently reading redundant copies of the same information off the environment. Zurek's programme calls that last one **Quantum Darwinism**, and it is the strongest real-physics support for your thesis. It is live research, not textbook. And (4) nothing propagates, ever — no-signalling is absolute and you must not imply otherwise.

The stage-set image survives if you **move the renderer**: the audience doesn't render the set; the air does, the starlight does. You're just one of ~10¹⁰⁰ ticket-holders reading the same programme.

---

## 1. Decoherence — what it does, and the wall it hits **[T]**

### The lineage

- H. D. Zeh, *"On the interpretation of measurement in quantum theory"*, Found. Phys. **1**, 69 (1970) — the founding paper.
- W. H. Zurek, Phys. Rev. D **24**, 1516 (1981); Phys. Rev. D **26**, 1862 (1982) — pointer states, einselection.
- E. Joos & H. D. Zeh, Z. Phys. B **59**, 223 (1985) — the scattering calculations that produced the famous numbers.
- W. H. Zurek, *"Decoherence, einselection, and the quantum origins of the classical"*, **Rev. Mod. Phys. 75, 715 (2003)** — the canonical review. Full text: <https://arxiv.org/abs/quant-ph/0105127>
- M. Schlosshauer, *"Decoherence, the measurement problem, and interpretations of quantum mechanics"*, **Rev. Mod. Phys. 76, 1267 (2004)** — <https://arxiv.org/abs/quant-ph/0312059>; the up-to-date successor is Phys. Rep. **831**, 1 (2019), <https://arxiv.org/abs/1911.06282>; the short pedagogical one I quote below is <https://arxiv.org/abs/1404.2635>.
- Stanford Encyclopedia of Philosophy, *"The Role of Decoherence in Quantum Mechanics"* (Bacciagaluppi): <https://plato.stanford.edu/entries/qm-decoherence/>

### What decoherence actually does

A system never sits alone. It gets entangled with a huge, uncontrolled environment. Trace the environment out and the interference terms in the system's density matrix decay away, fast. Zurek's own framing from the RMP abstract:

> "Decoherence is caused by the interaction with the environment. Environment monitors certain observables of the system, destroying interference between the pointer states corresponding to their eigenvalues." — Zurek, RMP 75, 715

and

> "Einselection enforces classicality by imposing an effective ban on the vast majority of the Hilbert space, eliminating especially the flagrantly nonlocal 'Schrödinger cat' states."

Note the verb: **monitors**. The environment is the measuring device. No human is required anywhere in the story. That is the single most useful fact in this whole document for BadCode.

### The wall — and this is where popular accounts lie

Decoherence turns a coherent superposition into an *improper mixture* — something that looks statistically exactly like "one of these, we just don't know which." It never produces the one. The global state is still a superposition, now including the environment.

The cleanest quotable statement, from Schlosshauer's pedagogical review (<https://arxiv.org/abs/1404.2635>, §VII):

> "If we understand the 'quantum measurement problem' as the question of how to reconcile the linear, deterministic evolution described by the Schrödinger equation with the occurrence of random measurement outcomes, then **decoherence has not solved this problem**. Decoherence does, however, address an aspect sometimes associated with the quantum measurement problem, namely the preferred-basis problem."

And, same section:

> "Decoherence … is not tied to any particular interpretation of quantum mechanics, nor does it supply such an interpretation, nor does it amount to a theory that could make predictions beyond those of standard quantum mechanics."

SEP puts it flatter still:

> "Decoherence … does *not* explain why we *do* observe measurement results in the first place." … "decoherence as such does not provide a solution to the measurement problem, at least not unless it is combined with an appropriate foundational approach to the theory." — <https://plato.stanford.edu/entries/qm-decoherence/>

**Zurek's own careful hedge** is worth having verbatim, because he is the most bullish serious person on this and even he hedges. From RMP §VIII: "while decoherence – through einselection – **helps solve** the measurement problem…". And from his §I.D, on the appearance of collapse:

> "In this very immediate sense decoherence enforces the **apparent** 'collapse of the wavepacket': After a decoherence timescale, only the einselected memory states will exist and retain useful correlations."

He is equally blunt that Everett alone doesn't cut it, which is a nice quotable jab:

> "as long as it is unclear what singles out preferred states, perception of a unique outcome of a measurement and, hence, of a single Universe cannot be explained either… In essence, Many Worlds Interpretation does not address but only postpones the key question."

And he concedes a real circularity in deriving Born's rule from decoherence: "derivations of Born's rule that employ reduced density matrices are open to charge of circularity (Zeh, 1997)."

### The famous numbers **[T]**

This is Table I of Schlosshauer's review (<https://arxiv.org/abs/1404.2635>), derived from Joos & Zeh (1985). **Decoherence timescales in seconds**, for suppressing spatial interference over a separation Δx equal to the object's own size (Δx = a = 10⁻³ cm for a dust grain, 10⁻⁶ cm for a large molecule):

| Environment | Dust grain (10 µm) | Large molecule (10 nm) |
|---|---|---|
| Cosmic background radiation | **1** | 10²⁴ |
| Photons at room temperature | 10⁻¹⁸ | 10⁶ |
| Best laboratory vacuum | 10⁻¹⁴ | 10⁻² |
| Air at normal pressure | **10⁻³¹** | 10⁻¹⁹ |

Read those two bolded entries again. A speck of dust in ordinary air is collapsed to a definite position in **10⁻³¹ seconds** — roughly 10¹⁵ times faster than light crosses a proton. And take the dust grain to the emptiest place in the universe, shield it from everything, and the **cosmic microwave background alone still measures it in about one second.** There is no unwatched corner. That number is the single best weapon against the render-on-demand reading, and it's also, if you want it, a genuinely eerie image: the afterglow of the Big Bang is still taking attendance.

One more scale-setter from the same review: for a 1-gram object at room temperature superposed over 1 cm, the ratio of the *dissipation* timescale to the *decoherence* timescale is of order **10⁴⁰**. Decoherence is not friction. It steals no energy. It only steals the *whichness*.

---

## 2. Einselection and the pointer basis — the environment picks the questions **[T]**

"Einselection" = **environment-induced superselection**. Of all the states in Hilbert space, the environment lets only a tiny family survive: those that don't get scrambled by being watched.

The technical criterion (Zurek 1981/82; Schlosshauer §II.C): split the Hamiltonian H = H_S + H_E + H_int. Pointer states |sᵢ⟩ are those for which an initial product state |sᵢ⟩|E₀⟩ stays a product, |sᵢ⟩|Eᵢ(t)⟩ — they get *recorded* without getting *disturbed*. Equivalently the pointer observable commutes with the interaction: **[O_S, H_int] = 0**.

Why position, almost always:

> "Since the force laws describing such processes typically depend on some power of distance, the interaction Hamiltonian will then commute with the position operator. Thus, the pointer states will be approximate eigenstates of position (i.e., narrow position-space wave packets). This explains why superpositions of mesoscopically and macroscopically distinct positions are prohibitively difficult to observe." — Schlosshauer, arXiv:1404.2635 §II.C.1

Scattering — photons, air molecules — cares about *where things are*. So the environment is a machine that relentlessly asks "where?" and nothing else. The classical world is position-shaped because the questions are position-shaped.

When H_int doesn't dominate, you rank candidates with the **predictability sieve** (Zurek, Prog. Theor. Phys. 89, 281 (1993)): let each candidate state evolve, measure how fast it gains entropy, keep the most stable. For quantum Brownian motion the sieve returns minimum-uncertainty coherent wave packets — i.e. classical phase-space "points."

**Story-usable phrasing:** the environment doesn't decide what's true, it decides *what kind of thing can be true*. It's a censor, not an author. Zurek's word for this, unimprovable: **"censorship."** From the RMP — "Distinct memory/identity states of the observer … cannot be superposed: This censorship is strictly enforced by decoherence and the resulting einselection."

---

## 3. Quantum Darwinism — objectivity as a broadcast **[L, and this is your thesis]**

**Core papers:**
- H. Ollivier, D. Poulin, W. H. Zurek, *"Objective properties from subjective quantum states: environment as a witness"*, Phys. Rev. Lett. **93**, 220401 (2004).
- W. H. Zurek, *"Quantum Darwinism"*, **Nature Physics 5, 181 (2009)** — <https://arxiv.org/abs/0903.5082>
- Zurek, *Decoherence and Quantum Darwinism: From Quantum Foundations to Classical Reality*, Cambridge University Press (2025), <https://www.cambridge.org/9781009552905>

Zurek's abstract, verbatim — the whole thesis in five lines:

> "Quantum Darwinism describes the proliferation, in the environment, of multiple records of selected states of a quantum system. It explains how the fragility of a state of a single quantum system can lead to the classical robustness of states of their correlated multitude; shows how effective 'wave-packet collapse' arises as a result of proliferation throughout the environment of imprints of the states of quantum system; and provides a framework for the derivation of Born's rule… Taken together, these three advances mark **considerable progress towards** settling the quantum measurement problem." — Zurek, Nature Physics 5, 181 (2009)

("Considerable progress towards." Not "settles." Keep the hedge; a physicist will check.)

### The mechanism

Standard decoherence treats the environment as a *sink* — information falls in and is lost. Quantum Darwinism treats it as a **channel and amplifier**. Schlosshauer's summary:

> "Interactions between the system and its environment lead to the redundant storage of selected information about the system in many fragments of the environment. By measuring some of these fragments, observers can indirectly obtain information about the system without appreciably disturbing the system itself. Indeed, this represents how we typically observe objects. For example, we see an object not by directly interacting with it, but by intercepting scattered photons that encode information about the object's spatial structure."

The quantitative marker is **redundancy R_δ**: the number of *disjoint* fragments of the environment, each of which independently supplies all but δ of the classical information about the system's pointer observable. Plot mutual information between the system and a fragment against fragment size and you get the signature "**classical plateau**": a tiny fraction of the environment already tells you almost everything, and collecting more tells you almost nothing new. R_δ for a dust grain in sunlight is astronomically large — of order 10⁸ or more independent copies within a microsecond, and vastly more over any human timescale.

**Only pointer states get copied.** Superpositions cannot be cloned (no-cloning), so they cannot be broadcast, so they cannot become objective. Survival of the fittest — hence "Darwinism." Objectivity is a *selection* effect over what the environment is physically capable of duplicating.

Zurek's own strongest lines on what this means for observers, from the RMP:

> "The information encoded in states of macroscopic quantum systems (neurons) is by no means secret: As a result of lack of isolation the environment – having redundant copies of the relevant data – 'knows' in detail everything observer knows."

> "Its state is repeatedly collapsed – forced into the einselected states – and very well (very redundantly) 'known' to the rest of the Universe."

> "**The observer is what he knows.**"

> "What the observer knows is inseparable from what the observer is."

### Experimental tests **[L]**

Three landmark demonstrations, all 2018–2019, all engineered simulators rather than found-in-nature systems:

1. **Ciampini, Pinna, Mataloni & Paternostro**, *"Experimental signature of quantum Darwinism in photonic cluster states"*, **Phys. Rev. A 98, 020101(R) (2018)** — <https://arxiv.org/abs/1803.01913>. A photonic hyperentangled graph-state source, examining "the effects that correlations among the elements of a multi-party environment have on the establishment of objective reality." Key finding: correlations *within* the environment and environment-to-system back-action degrade the Darwinist picture — objectivity is not free.
2. **Chen et al. (Jian-Wei Pan group)**, *"Emergence of classical objectivity of quantum Darwinism in a photonic quantum simulator"*, **Science Bulletin 64, 580 (2019)**. A six-photon simulator; observed redundancy of the system's *classical* information across environment fragments, together with suppression of quantum correlations in those fragments.
3. **Unden et al.**, *"Revealing the emergence of classicality using nitrogen-vacancy centers"*, **Phys. Rev. Lett. 123, 140402 (2019)** — <https://arxiv.org/abs/1809.10456>. An NV centre in diamond with surrounding nuclear spins as a *natural* environment, read out via dynamical decoupling: "redundant information is imprinted onto E, giving rise to classical objectivity."

### The criticisms — you must carry these **[L]**

- **The plateau can be a mirage.** The mutual-information plateau conventionally taken as the QD signature can be substantially composed of **quantum discord** rather than genuinely classical, independently readable information. That motivated **Strong Quantum Darwinism** (Le & Olaya-Castro).
- **Horodecki, Korbicz & Horodecki** (Phys. Rev. A **91**, 032122 (2015)) showed that some entangled states satisfy the QD redundancy condition while failing to be objective in the operational sense — so QD's condition is necessary-ish, not sufficient. Their alternative, **Spectrum Broadcast Structures (SBS)**, imposes a strictly stronger structural condition on the joint system–environment state.
- Review with all three frameworks compared: **T. P. Le & A. Olaya-Castro, "Roads to objectivity: Quantum Darwinism, Spectrum Broadcast Structures, and Strong Quantum Darwinism — a review", Quantum 5, 571 (2021)** — <https://quantum-journal.org/papers/q-2021-11-08-571/> (arXiv:2007.04276). SBS is sufficient but too restrictive to be necessary; SQD sits between.
- QD is **model-dependent**: it works beautifully for photon/scattering environments where fragments are independent and freely accessible, and degrades or fails for strongly interacting, structured, or non-Markovian environments.
- **And it still does not produce a single outcome.** It explains *agreement*; it does not explain *actuality*. If ten thousand observers each read the same broadcast, you have explained the consensus, not the event.

**How to say it in BadCode voice, without error:** "You never touched the world. You caught the light that bounced off it, along with everybody else in the room. Objectivity isn't a property of the thing. It's a circulation figure."

---

## 4. Does measuring one thing settle a whole subsystem? **[T for the mechanics, M for the phrasing]**

Yes — with two hard conditions, and one absolute prohibition.

### GHZ: the exact shape of your image **[T]**

Take N qubits in the Greenberger–Horne–Zeilinger state
|GHZ⟩ = (|00…0⟩ + |11…1⟩)/√2.

Measure **one** qubit in the computational basis. The remaining N−1 are instantly left in a **product** state — all definitely 0, or all definitely 1. One measurement, entire subsystem settled, no matter how large N is. That is genuinely, textbook-ly, "measuring one thing collapses a whole hierarchy." Good lecture treatment: Scott Aaronson's notes, <https://www.scottaaronson.com/qclec/10.pdf>.

**Condition 1 — the correlation had to be there already.** Nothing was *created*. The subsystem was pre-wired to agree; the measurement only fixed which way. You are not sculpting the set; you are opening an envelope whose contents were correlated at manufacture.

**Condition 2 — and this is the gift for your story: which subsystem settles depends on how you measure.** Measure that same GHZ qubit in the *X* basis instead and the remaining N−1 are **not** settled at all; they're left in a GHZ-like entangled state of their own. So the user's line — *"entire subsystems collapse based on the way something's measured"* — is not loose talk. It is exactly right, and it is the strangest true thing here. The choice of question determines the *shape* of what settles.

### Monogamy **[T]**

Entanglement can't be shared around. Coffman–Kundu–Wootters: C²(A|BC) ≥ C²(A|B) + C²(A|C). In the GHZ state, tracing out any one qubit leaves a **separable** mixed state and all pairwise concurrences vanish — the entanglement is irreducibly N-partite. Maximally entangle with one partner and you are *forbidden* from correlating with anyone else. This is why decoherence is irreversible in practice: once the environment is entangled with the system, the system's coherence with anything else is gone.

**Story-usable:** entanglement is monogamous, and the environment is always the one who gets there first.

### The prohibition: no-signalling **[T — do not break this]**

The **no-communication theorem** is exact: no local operation on one part of an entangled state can change the reduced density matrix — hence any statistics whatsoever — of a distant part. Alice measuring her GHZ qubit produces *no observable change* at Bob's end. Bob sees perfectly random 50/50 results with or without Alice's measurement. The correlation only becomes visible when the two *records* are brought together over an ordinary classical channel, at or below light speed.

So: **nothing propagates. Nothing travels. No influence, no wave, no news.** The "settling" is a statement about the *joint description*, not about a physical thing sweeping outward through the set. If BadCode's imagery has anything moving down the hierarchy, a physicist stops reading. Write the settling as *simultaneity of the record*, never as *transmission*.

### Entanglement swapping **[T]**

A Bell-state measurement on one photon from pair (1,2) and one from pair (3,4) leaves photons 1 and 4 — which have never met, never interacted, never shared a light cone with each other — entangled. Entanglement is not a wire you have to have run in advance between two specific things; it can be established retroactively-in-bookkeeping between parties who were never in contact. Still no signalling: you have to *tell* Alice and Bob what the Bell measurement gave, classically, before they can see it.

### Superselection and collective coordinates **[T/L] — the honest version of "hierarchical"**

Fundamental **superselection rules** (electric charge, baryon number, mass in Galilean quantum mechanics) forbid coherent superposition between sectors outright — the world is already partitioned into boxes you cannot superpose across. Einselection is the *emergent* cousin, and Zurek explicitly speculates the fundamental ones might be emergent too:

> "Einselection should be included in this program, as it decides which of the observables are accessible and useful – which are effectively classical. It is conceivable that also the 'fundamental' superselection may emerge in this manner." — Zurek, RMP §VI

The genuinely important structural point for your story: **what goes classical is a collective degree of freedom, not every particle.** A SQUID's classical variable is the total trapped flux, carried by the collective centre-of-mass motion of ~10⁹ Cooper pairs. A dust grain's classical variable is its centre of mass. The microscopic degrees of freedom underneath remain as quantum as ever. So the honest form of "hierarchical collapse" is: *the environment monitors one coarse-grained collective coordinate of a huge assembly, and that coordinate — the whole assembly's one shared handle — is what gets pinned.* The chorus gets a definite pitch; the individual singers do not each get a definite anything.

That is, I think, precisely the image you want, and it's real physics.

---

## 5. How far up the ladder does quantum behaviour actually reach? **[T for the results, L for the frontier]**

Real numbers you can say out loud without lying:

| Achievement | Scale | Source |
|---|---|---|
| Molecule interference, current record | **>25,000 Da**, up to ~2,000 atoms (largest molecule >40,000 protons+neutrons+electrons), 2-metre Talbot–Lau interferometer, de Broglie wavelength ~1000× smaller than a hydrogen atom's diameter, **>7 ms** in superposition | Fein *et al.*, **Nature Physics 15, 1242 (2019)**, <https://www.nature.com/articles/s41567-019-0663-9> |
| Previous record | 10,000 amu (2013), C₆₀ fullerene (720 amu, 60 atoms) in 1999 | Arndt group; review: Hornberger *et al.*, RMP **84**, 157 (2012) |
| Heaviest Schrödinger-cat state | **16 micrograms** of sapphire, ~10¹⁷ atoms, superposition of two opposite-phase acoustic oscillations, coupled to a superconducting qubit | Bild *et al.*, **Science 380, 274 (2023)**, <https://arxiv.org/abs/2211.00449>; ETH writeup: <https://ethz.ch/en/news-and-events/eth-news/news/2023/04/fat-quantum-cats.html> |
| Entangled *macroscopic* mechanical objects | two vibrating drumheads, ~10 µm across, tens of picograms (~10¹²–10¹³ atoms), deterministically entangled | Kotler *et al.*, **Science 372, 622 (2021)**, <https://www.science.org/doi/10.1126/science.abf2998>; Mercier de Lépinay *et al.*, Science **372**, 625 (2021). Physics World 2021 Breakthrough of the Year |
| Superconducting circuits | collective flux state of ~10⁹ Cooper pairs; cavity-QED cat states of several tens of photons with decoherence watched in real time | Schlosshauer review §VI; Haroche/Raimond group |
| Catching collapse mid-act | a quantum jump in a superconducting atom shown to be **continuous, predictable, and reversible in flight** | Minev *et al.*, *"To catch and reverse a quantum jump mid-flight"*, **Nature 570, 200 (2019)** |

**The caveat you must not skip.** Mass alone is a bad figure of merit and physicists will call it out. The 16-µg sapphire cat is enormously heavier than the molecules, but its two superposed states differ by a *minuscule* oscillation amplitude; the molecule interferometer separates paths by hundreds of nanometres — far more than the molecule's own size. The field's actual yardstick is a **"macroscopicity"** measure combining mass, separation, and coherence time (Nimmrichter & Hornberger, PRL **110**, 160403 (2013)). So: *"a speck you could weigh on a good balance has been put in two vibrational states at once"* is true. *"A 16-microgram object was in two places a centimetre apart"* is false.

**The frontier [L]:** does *gravity* itself decohere superpositions, and is gravity quantum? The flagship proposal is **gravitationally induced entanglement (BMV)**:

- S. Bose, A. Mazumdar, G. W. Morley, H. Ulbricht, M. Toroš, M. Paternostro, A. Geraci, P. Barker, M. S. Kim, G. Milburn, *"A spin entanglement witness for quantum gravity"*, **PRL 119, 240401 (2017)** — <https://arxiv.org/abs/1707.06050>:
  > "We show that despite the weakness of gravity, the phase evolution induced by the gravitational interaction of two micron size test masses in adjacent matter-wave interferometers can detectably entangle them… We provide a prescription for witnessing this entanglement, which certifies gravity as a quantum coherent mediator."
- C. Marletto & V. Vedral, PRL **119**, 240402 (2017) — the complementary argument: *two systems cannot be entangled by a classical mediator*, so observed gravitational entanglement is sufficient evidence that gravity is non-classical.

**Status as of 2026: not performed.** No definitive experimental confirmation exists. The field is extremely active — levitated nanoparticles, diamagnetic microchip traps, pulsed optomechanics, space-based interferometer proposals — but this is a *proposed* experiment, and BadCode should say so.

Also live: **objective collapse models** (GRW, CSL, Diósi–Penrose), which modify quantum mechanics so that collapse is a real physical process with a real rate. Every increase in interference mass tightens the bounds on them; none has been confirmed, several parameter regions have been excluded.

---

## 6. Delayed choice and the quantum eraser — what is actually licensed **[T for results, M for the popular reading]**

### The experiments

- **Wheeler (1978, 1983)**: choose *after* the photon is past the beamsplitter whether to measure wave or particle behaviour. His conclusion was epistemic, not causal: no particle-propagation model consistent with relativity reproduces quantum theory.
- **Jacques *et al.*, Science 315, 966 (2007)**: first full realisation — single photons from an NV centre in diamond, Mach–Zehnder, output beamsplitter inserted/removed by a quantum-random-number-driven electro-optic modulator, space-like separated from the photon's entry.
- **Manning *et al.*, Nature Physics 11, 539 (2015)**: same, with a single **helium atom** — a massive particle.
- **Ma *et al.*, "Experimental delayed-choice entanglement swapping", Nature Physics 8, 479 (2012)** — <https://arxiv.org/abs/1203.4834>. Realises Peres's gedankenexperiment. Their own abstract, verbatim:
  > "Peres has put forward the radical idea of delayed-choice entanglement swapping. There, entanglement can be 'produced a posteriori, after the entangled particles have been measured and may no longer exist'… Using four photons, we can actively delay the choice of measurement… on two of the photons into the time-like future of the registration of the other two photons. This effectively projects the two already registered photons onto one definite of two mutually exclusive quantum states in which either the photons are entangled (quantum correlations) or separable (classical correlations). This can also be viewed as **'quantum steering into the past'**."
- **Cosmic-scale delayed choice / freedom-of-choice:** Handsteiner *et al.*, PRL **118**, 060401 (2017) used Milky Way starlight (~600 light-years) to pick settings; **Rauch *et al.*, PRL 121, 080403 (2018)** — <https://link.aps.org/doi/10.1103/PhysRevLett.121.080403> — used **high-redshift quasars**, with the detector settings determined by photons emitted **7.78 and 12.21 billion years ago**. Bell violation by **9.3σ**, p ≲ 7.4×10⁻²¹, "excluding any such mechanism from **96% of the space-time volume of the past light cone** of the experiment, extending from the Big Bang to today."

### The standard correction — say this, or a physicist eats you **[M→T]**

The popular reading ("the choice now changes what happened then") is **wrong**, and the corrective literature is explicit:

- R. E. Kastner, *"The 'delayed choice quantum eraser' neither erases nor delays"*, Found. Phys. **49**, 717 (2019) — <https://arxiv.org/abs/1905.03137>. Quantum erasers "do not erase any information, nor do they demonstrate retrocausation or 'temporal nonlocality' in their 'delayed choice' form, beyond standard EPR correlations." The error is assuming the improper mixed state of the signal photon "physically prefers" either the which-way or the both-ways basis. It doesn't; expressing a state in a different basis "neither adds nor removes information."
- D. Ellerman, *"Why delayed choice experiments do NOT imply retrocausality"*, Quantum Stud.: Math. Found. (2015) — <https://link.springer.com/article/10.1007/s40509-014-0026-2>; the "separation fallacy."

**The mechanism of the illusion, in one sentence:** the raw pattern at the signal detector *never changes* — it never shows fringes. Fringes appear only when you take the idler's later record, ship it over an ordinary classical channel, and use it to **sort the earlier data into subensembles** by coincidence counting. The sorting key arrives from the future; the data does not change. Remove the coincidence counter and the "retrocausality" evaporates — which is exactly what no-signalling guarantees must happen.

**What *is* licensed**, and it's plenty: there was no fact of the matter about "which path" that was sitting in the world waiting to be found. Ma/Zeilinger's own conclusion is the safe quotable one — that these results teach us "we should not have any naive realistic picture" of what the particle was doing. The past isn't *changed*; it was never *specified* in the first place, in the way naive realism assumed.

**BadCode-safe phrasing:** "You didn't change the past. There simply wasn't as much past there as you assumed."

---

## 7. Rendering-on-demand — where it comes from, why it's wrong, and what's legitimately nearby

### Where the trope comes from **[X as physics]**

Three tributaries: (i) sloppy Copenhagen popularisation — Einstein's "is the moon there when nobody looks?", filtered through decades of paperbacks into "observation creates reality"; (ii) Wheeler's genuinely provocative **"participatory universe"** and **"it from bit"**, which he meant much more carefully than it gets quoted; (iii) the **simulation hypothesis** (Bostrom 2003) crossed with gamers' intuitions about frustum culling and level-of-detail rendering, plus the word "holographic" borrowed from a completely unrelated technical result.

### Why physicists dislike it — three fatal problems

1. **The measurer is not a mind.** Decoherence identifies the "observer" as the environment: photons, air molecules, phonons. Zurek's programme removes consciousness from the account entirely. Any framing where a *person looking* is the trigger is not merely unsupported, it's contradicted by the numbers in §1.
2. **The numbers run the wrong way.** Render-on-demand posits *saving effort* on the unobserved. Physics says the unobserved is measured just as hard: 10⁻³¹ s for a dust grain in air, ~1 second for the same grain in intergalactic vacuum with nothing but the CMB touching it. Worse, Quantum Darwinism says the world isn't rendered once — it's rendered **redundantly**, in an astronomical number of independent copies scattered into the photon field. That is the opposite of a compute optimisation. It is comically wasteful.
3. **It smuggles in signalling.** Every "the world builds itself where I look" story implies my looking makes a difference *out there*. No-communication says it provably doesn't.

### What *is* legitimately nearby **[T]**

- **Asher Peres, "Unperformed experiments have no results", Am. J. Phys. 46, 745 (1978).** The title is the quote and it is the most useful five words in this document. Peres's companion line, from *Quantum Theory: Concepts and Methods* (1995), p. 373: **"Quantum phenomena do not occur in a Hilbert space. They occur in a laboratory."** And on consciousness-based accounts, p. 26–27: *"Some authors state that the last stage… involves 'consciousness'… I shall refrain from using concepts that I do not understand."* (Quotes collected at <https://en.wikiquote.org/wiki/Asher_Peres>.)
- **Kochen–Specker contextuality (1967)** — <https://plato.stanford.edu/entries/kochen-specker/>. You cannot consistently assign definite pre-existing values to all observables of a quantum system while keeping those values independent of *which other compatible observables you measure alongside*. SEP: "acceptance of QM logically forces us to renounce either [value definiteness] or [noncontextuality]"; and, on the surviving option, "a property (value of an observable) might be ontologically context-dependent in the sense that its specification requires reference to how it is measured."

  **This is the real physics under your stage-set image.** Not "the set is built when you look" but "**there is no answer to a question that was never asked, and the answer you get depends on what else you asked at the same time.**" Contextuality is the licensed version of "the way something's measured determines what settles."
- **Bell nonlocality** — the correlations exceed anything a pre-set local script can produce; Rauch *et al.* pushed the last loophole back 7.8 billion years.

### Information limits — real, but they don't do what you want **[T]**

The **Bekenstein bound**: S ≤ 2πkRE/ℏc, i.e. the entropy — equivalently the information needed to specify a system exactly — inside a sphere of radius R containing energy E is finite and bounded. In bits, I ≤ 2πRE/(ℏc ln 2). Black holes saturate it exactly (Bekenstein–Hawking entropy = A/4 in Planck units). This generalises to the **holographic principle** ('t Hooft 1993, Susskind 1995) and **Bousso's covariant entropy bound** (Rev. Mod. Phys. 74, 825 (2002)). Overview: <https://en.wikipedia.org/wiki/Bekenstein_bound>, <http://www.scholarpedia.org/article/Bekenstein_bound>.

So *"the world can only hold finitely much detail per unit of space and energy"* is **true and quotable** — a real, hard, physical ceiling on resolution. The information content of any bounded region is proportional to the **area** of its boundary, not its volume.

But: it is a bound on **capacity**, not a **rendering policy**. It says the set has a maximum resolution; it does not say the set is drawn lazily, or that anything is withheld until observed. Use it for "the universe has a finite texture budget." Do not use it for "the universe spends that budget only where the camera points."

---

## 8. Honest labels, the strongest objection, and how to phrase it

### Label sheet

**(a) Textbook — say freely:**
decoherence and its timescales; einselection and the pointer basis; position as the usual pointer observable; the improper-mixture limitation; GHZ correlations and basis-dependent settling; entanglement monogamy; entanglement swapping; the no-communication theorem; Kochen–Specker contextuality; Bell violations including the cosmic tests; all the macroscopic-superposition records in §5; the Bekenstein/holographic bounds.

**(b) Live research — say "physicists are currently arguing about / testing this":**
Quantum Darwinism, Spectrum Broadcast Structures, Strong Quantum Darwinism, and whether objectivity is universal or model-dependent; objective-collapse models (GRW/CSL/Diósi–Penrose); gravitational decoherence and BMV gravity-induced entanglement (proposed, **not yet performed**); the derivation of Born's rule from envariance; macroscopicity measures.

**(c) Legitimate but easily misstated — handle with the exact phrasings below:**
- "Measuring one thing settles a whole subsystem." *True in a pre-correlated state, for a specific measurement basis. False as any claim about propagation.*
- "Which subsystem settles depends on how you measure." *True — GHZ in Z vs X. This is your best real support.*
- "Objectivity is many observers reading the same broadcast." *This is Quantum Darwinism's claim, and it is live research, not settled.*
- "The past isn't fixed until measured." *Licensed only as: there was no pre-existing fact of the matter. Never as: the measurement changed what happened.*
- "Decoherence explains collapse." *Only apparent collapse. Never the single outcome.*
- "The universe has a maximum resolution." *True (Bekenstein). Not a rendering policy.*

**(d) Not physics — do not put these in the narrator's mouth as fact (they can be in a character's mouth, as error):**
consciousness collapses the wavefunction; the universe economises computation on the unobserved; measurement transmits anything anywhere; "the moon isn't there when nobody looks"; observation by a mind is required for anything; wavefunction collapse is a signal.

### The strongest objection a working physicist would make to the stage-set image

> *"Your metaphor has the causality exactly backwards. The set isn't rendered because you looked — it was rendered 10³¹ times per second by the air in the room, and a billion times over by the sunlight in it, long before you got there, and it would go on being rendered in an empty universe by the cosmic microwave background alone. Decoherence isn't a spotlight you carry; it's a flood. And the reason you and I agree about the set is not that we share a renderer, it's that the scenery has been shedding identical copies of itself into the photon field all afternoon and we each picked up a different one. If anything, quantum mechanics says the world is grotesquely over-rendered. Also, and this is the part I'll actually get angry about: whatever you do at your seat has no effect whatsoever on my seat, and no ordering of your imagery may suggest otherwise."*

### How to keep the image and stay true

**Move the renderer, keep the theatre.** The audience does not render the set. The *air* renders it. The *starlight* renders it. You are not the projectionist; you are one of a hundred million people who bought a ticket to the same broadcast and are each holding a different photocopy of the programme.

Four lines that are metaphor, not false claim:

- *"The set was never built for you. It was built by everything that touched it. You just caught the light coming off it, along with everyone else in the room — and that's the only reason you all agree about the furniture."* (Quantum Darwinism, correctly stated.)
- *"One question, asked once, can settle an entire chorus — if the chorus was already singing in unison. And which chorus settles depends on which question you ask. What it cannot do, ever, is send word down the line."* (GHZ + basis dependence + no-signalling, all correct.)
- *"There was never as much past there as you assumed. Nobody rewrote it. It simply hadn't been specified."* (Delayed choice, correctly stated.)
- *"The world has a maximum resolution — a real one, in bits, set by the size of the room and the energy in it. It just isn't stingy with it."* (Bekenstein, correctly stated.)

And if you want the coldest one, straight from Zurek and dressed for BadCode:

> *"The environment has redundant copies of everything you know. It knew before you did. You are not the observer of this universe. You are one of its more recent, and more forgetful, filing cabinets."*

---

## Source list

Zurek RMP 75, 715 (2003) <https://arxiv.org/abs/quant-ph/0105127> · Schlosshauer RMP 76, 1267 (2004) <https://arxiv.org/abs/quant-ph/0312059> · Schlosshauer pedagogical review <https://arxiv.org/abs/1404.2635> · Schlosshauer Phys. Rep. 831, 1 (2019) <https://arxiv.org/abs/1911.06282> · SEP, Role of Decoherence <https://plato.stanford.edu/entries/qm-decoherence/> · SEP, Kochen–Specker <https://plato.stanford.edu/entries/kochen-specker/> · Zeh, Decoherence: Concepts and Examples <https://arxiv.org/abs/quant-ph/9803052> · Zurek, Quantum Darwinism, Nature Physics 5, 181 (2009) <https://arxiv.org/abs/0903.5082> · Zurek, *Decoherence and Quantum Darwinism* (CUP 2025) <https://www.cambridge.org/9781009552905> · Ciampini et al., PRA 98, 020101 (2018) <https://arxiv.org/abs/1803.01913> · Unden et al., PRL 123, 140402 (2019) <https://arxiv.org/abs/1809.10456> · Chen et al., Sci. Bull. 64, 580 (2019) <https://www.sciencedirect.com/science/article/abs/pii/S2095927319301847> · Le & Olaya-Castro, Quantum 5, 571 (2021) <https://quantum-journal.org/papers/q-2021-11-08-571/> · Horodecki/Korbicz/Horodecki, PRA 91, 032122 (2015) <https://arxiv.org/abs/1803.00765> (comparison paper) · Aaronson lecture notes on GHZ/monogamy <https://www.scottaaronson.com/qclec/10.pdf> · Fein et al., Nature Physics 15, 1242 (2019) <https://www.nature.com/articles/s41567-019-0663-9>, summary <https://phys.org/news/2019-09-atoms-quantum-superposition.html> · Bild et al., Science 380, 274 (2023) <https://arxiv.org/abs/2211.00449>, <https://ethz.ch/en/news-and-events/eth-news/news/2023/04/fat-quantum-cats.html> · Kotler et al., Science 372, 622 (2021) <https://www.science.org/doi/10.1126/science.abf2998> · Bose et al., PRL 119, 240401 (2017) <https://arxiv.org/abs/1707.06050> · Ma et al., Nature Physics 8, 479 (2012) <https://arxiv.org/abs/1203.4834> · Rauch et al., PRL 121, 080403 (2018) <https://link.aps.org/doi/10.1103/PhysRevLett.121.080403> · Kastner, Found. Phys. 49, 717 (2019) <https://arxiv.org/abs/1905.03137> · Ellerman <https://link.springer.com/article/10.1007/s40509-014-0026-2> · Peres, Am. J. Phys. 46, 745 (1978); quotes <https://en.wikiquote.org/wiki/Asher_Peres> · Bekenstein bound <http://www.scholarpedia.org/article/Bekenstein_bound>, <https://en.wikipedia.org/wiki/Bekenstein_bound>
