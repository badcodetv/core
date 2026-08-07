# The Measurement Problem, the Interpretation Landscape, and a Stress-Test of the BadCode Thesis

Research brief for BadCode. Written for fiction writers who want the physics under the fiction to be
right, and who want to know exactly where they are departing from it.

**How to read the quotes.** Quotes marked ✅ were pulled verbatim from primary abstracts or full
texts and are safe to print. Quotes marked ⚠️ came to me relayed through the Stanford Encyclopedia
of Philosophy or a secondary summariser — the substance is right, but **verify the exact wording
against the linked source before you put it on a page or in a lyric.** Attribution is correct in
both cases.

---

## 1. The measurement problem, stated precisely

Quantum mechanics has two rules, and they contradict each other.

**Rule 1 — the Schrödinger equation.** An isolated system's quantum state evolves smoothly,
deterministically and *linearly*. Linearity is the killer: if input A produces output A′, and input
B produces output B′, then input (A + B) produces (A′ + B′). Feed a superposition in, get a
superposition out. Always. Forever.

**Rule 2 — the Born rule.** When you *measure*, you get one outcome, with probability equal to the
squared magnitude of the corresponding amplitude (|ψ|²). The state "collapses" to match what you
saw.

Rule 1 never produces a single outcome. Rule 2 asserts one. Nothing in the formalism says when to
stop using Rule 1 and start using Rule 2. That gap is **the measurement problem**.

John Bell's compression of it is the most quotable line in the field:

> ⚠️ "Either the wavefunction, as given by the Schrödinger equation, is not everything, or it is not
> right."
> — J.S. Bell, *Speakable and Unspeakable in Quantum Mechanics* (1987), p. 41, quoted in
> [SEP: Philosophical Issues in Quantum Theory](https://plato.stanford.edu/entries/qt-issues/)

The modern statement is a **trilemma**. These three claims are individually plausible and jointly
inconsistent:

1. **Completeness** — the quantum state is a complete description of the system.
2. **Unitarity** — the state always evolves by the Schrödinger equation, with no exceptions.
3. **Definiteness** — measurements have single, determinate outcomes.

Every interpretation is a choice of which leg to saw off. Hidden-variable theories (Bohm) deny
completeness. Collapse theories (GRW, Penrose) deny unitarity. Many-Worlds denies definiteness.
Relational QM and QBism do something subtler — they keep all three but *relativise* (3) to an
observer. Hold that thought; it is the load-bearing move for your thesis.

### What "collapse" is and isn't

**"Collapse" is not a physical process described anywhere in the formalism.** There is no equation
for it, no timescale, no mechanism, no field. It is a bookkeeping instruction: when you get a
result, update your state assignment. Whether that update corresponds to something happening *out
there* is precisely what interpretations disagree about. In Bohm nothing collapses. In Everett
nothing collapses. In QBism the collapse is you changing your mind. In GRW collapse is a real
stochastic physical event with new constants of nature.

### Superposition is not "in two places at once"

Say this out loud once and then never write the popular version again. A superposition is a single
definite quantum state — a vector — that happens not to be an eigenstate of the observable you
chose to measure. "In two places at once" imports a classical picture (there's a little ball, and
it's somehow at both spots) that no interpretation actually endorses. The honest gloss is: *the
question "where is it?" has no answer of the kind you were expecting, because the state is not the
kind of thing that answers it.*

### Decoherence — and the crucial thing it does not do

Decoherence is real, calculated, experimentally confirmed, and universally accepted. A system
entangles with its environment (photons, air molecules, phonons); interference between branches
becomes unmeasurable in practice, astronomically fast. Zurek's **einselection** explains *which*
states survive: the pointer states, those that entangle least with the environment, hence the ones
that get copied rather than scrambled.

But:

> ⚠️ "decoherence *does* explain why we do *not* observe superpositions of measurement results, it
> does *not* explain why we *do* observe measurement results in the first place."
> — [SEP: The Role of Decoherence in Quantum Mechanics](https://plato.stanford.edu/entries/qm-decoherence/)

Decoherence turns a superposition into an **improper mixture** — a thing that *looks* like "one of
these, we just don't know which" but is provably not that. It moves the problem outward into the
environment; it does not solve it. Anyone who tells you decoherence solved the measurement problem
is either being sloppy or is quietly an Everettian.

**Zurek's quantum Darwinism** is the follow-on and it matters a lot for your thesis (see §6). The
environment doesn't just destroy coherence, it *broadcasts*: a one-micrometre dust grain lit by the
sun for one microsecond has its position imprinted about **100 million times** in the scattered
photons. Objectivity is redundancy. We all agree the grain is *there* because we're each reading a
different copy of the same environmental press release.

> ✅ "Tracing flows of information in our quantum Universe explains why we see the world as
> classical."
> — W.H. Zurek, [*Quantum Darwinism, Classical Reality, and the Randomness of Quantum Jumps*](https://arxiv.org/abs/1412.5206)

---

## 2. The interpretation landscape

**Context first:** there is no consensus and there never has been. A 2025 *Nature* survey of 1,100+
researchers found Copenhagen 36%, Many-Worlds 15%, epistemic/QBist views ~17%, Bohmian 7%. Nearly
half said that asking what happens at the double slit is a *meaningless question*.
([The Quantum Insider on the Nature survey](https://thequantuminsider.com/2025/08/02/a-century-into-quantum-mechanics-physicists-still-cant-agree-what-it-means-nature-survey-shows/))

> ⚠️ "It's just embarrassing that we don't have a story to tell people about what reality is."
> — Carlton Caves, University of New Mexico, in the *Nature* survey coverage

That quote is a gift. BadCode is in the business of telling people stories about what reality is.
Physics has publicly conceded it doesn't have one.

### Copenhagen — and the historiographical scandal

**Strongest advocate:** nobody, exactly. That's the point.

The single most useful fact here: **"the Copenhagen interpretation" is a retcon.** The term was not
used by Bohr. Don Howard's research established that

> ⚠️ "the Copenhagen interpretation is an invention of the mid-1950s, for which Heisenberg is
> chiefly responsible."
> — Don Howard, *Who Invented the "Copenhagen Interpretation"? A Study in Mythology*, Philosophy of
> Science 71 (2004), p. 669, quoted in
> [SEP: Copenhagen Interpretation](https://plato.stanford.edu/entries/qm-copenhagen/)

Heisenberg coined it in 1955 and retroactively unified a set of views that were never unified.
Bohr and Heisenberg *disagreed*. Bohr's complementarity was about the necessity of classical
language for reporting evidence; Heisenberg's was about the wave function collapsing relative to an
observer. The textbook "Copenhagen" everyone learned is closer to Heisenberg-1955 than to anything
Bohr wrote.

And Bohr explicitly rejected consciousness-causes-collapse:

> ⚠️ "It is certainly not possible for the observer to influence the events."
> — Bohr, quoted in [SEP: Copenhagen Interpretation](https://plato.stanford.edu/entries/qm-copenhagen/)

For Bohr the wave function had "only a symbolic meaning and does not represent anything real."
**Appeal:** it works, you can shut up and calculate, and it correctly refuses to say more than the
evidence supports. **Problem:** it draws an unspecifiable line between "quantum system" and
"classical apparatus," and it is not one view but a family of incompatible ones flying a shared
flag.

### Everett / Many-Worlds

**Strongest advocates:** David Wallace, David Deutsch, Lev Vaidman, Sean Carroll.

**Everett's move is deletion, not addition.** He removed the collapse postulate. What remains is
Rule 1, universally applied. The universal wave function evolves unitarily forever; decoherence
carves it into non-interfering branches; each branch contains a copy of you who saw one outcome.

> ⚠️ "there are myriads of worlds in the Universe in addition to the world we are aware of."
> — [SEP: Many-Worlds Interpretation](https://plato.stanford.edu/entries/qm-manyworlds/)

**Two things the popular version gets wrong, both of which matter for your thesis (see §6A):**

1. **There is no collapse in Many-Worlds.** "It collapses here in our universe and there in another"
   is not MWI. It's a mash-up of collapse-talk and branch-talk that no Everettian holds.
2. **Branching is not a global instantaneous event.** On Wallace's account branching is *local* and
   spreads outward at light speed, carried by decoherence: "The new worlds might differ only in the
   states of systems which were entangled with the local system that was measured."
   The universe does not audibly *crack* everywhere at once. Carroll goes further and treats the
   branch decomposition as a description humans impose for convenience — the fundamental theory is
   just a wave function obeying one equation.

**Appeal:** one equation, no extra postulates, no nonlocal spookiness, manifestly relativistic.
**Problems:** (a) probability — if everything happens, what does "70% chance" mean? Deutsch–Wallace
decision theory, Vaidman's self-locating uncertainty and the Sebens–Carroll symmetry argument all
try; critics (Kent, Albert, Price) say each smuggles in what it derives. (b) the preferred basis
problem, largely answered by decoherence. (c) ontological extravagance.

### de Broglie–Bohm (pilot wave)

**Strongest advocate:** John Bell, later Dürr/Goldstein/Zanghì, Valentini.

Particles have definite positions *always*. The wave function is a real field that guides them via
the guiding equation. Randomness is ignorance of initial conditions (quantum equilibrium: if the
initial distribution is |ψ|², it stays |ψ|²). Fully deterministic. No measurement problem: "in
Bohmian mechanics pointers always point."

Bell was ferocious about its neglect:

> ⚠️ "vagueness, subjectivity, and indeterminism are not forced on us by experimental facts, but by
> deliberate theoretical choice."
> — Bell, quoted in [SEP: Bohmian Mechanics](https://plato.stanford.edu/entries/qm-bohm/)

**Crucially for you:** Bohm is **explicitly, unashamedly nonlocal**, and non-position observables
(spin, momentum) are **contextual** — the "value" you get depends on the apparatus, and is not a
pre-existing property being revealed. Bohmian spin isn't sitting there waiting.
**Problems:** relativistic extension is genuinely hard (it needs a preferred foliation, which is
exactly the global simultaneity Einstein deleted — note the irony for your thesis); "empty branches"
of the wave function still exist and do nothing.

### GRW / objective collapse (and Penrose–Diósi)

**Advocates:** Ghirardi, Rimini, Weber, Pearle, Bassi; Penrose and Diósi for the gravitational
version.

**These are not interpretations. They are rival theories with different predictions.** GRW adds
spontaneous localisation with two new constants: a rate ~10⁻¹⁶ s⁻¹ and a width ~10⁻⁵ cm. A single
particle collapses roughly once every hundred million years; a macroscopic object with 10²³ of them
collapses instantly. The measurement problem evaporates because the dynamics is nonlinear.

**And they get falsified.** Underground experiments in 2020 ruled out the parameter-free
Diósi–Penrose model in its simplest form; spontaneous X-ray emission searches and optomechanical
tests continue to squeeze the CSL parameter space.
([SEP: Collapse Theories](https://plato.stanford.edu/entries/qm-collapse/))

This is the honest scientific rebuttal to "it's all just interpretation, none of it is testable."
Some of it is testable, and some of it has been tested and killed.

### Relational Quantum Mechanics (Rovelli) — **your closest home, see §3**

### QBism (Fuchs, Mermin, Schack) — **your other closest home, see §3**

### Consistent / Decoherent Histories

**Advocates:** Griffiths, Omnès, Gell-Mann & Hartle.

Assign probabilities to *histories* — sequences of events — but only to families of histories
satisfying a mathematical consistency condition (interference between distinct histories vanishes).
Measurement is not special. The governing principle is the **single-framework rule**: "incompatible
frameworks are never to be combined into a single quantum description."
**Appeal:** dissolves the paradoxes as illegal framework-mixing; claims full compatibility with
special relativity. **Problem (Dowker & Kent):** there are *enormously many* consistent frameworks,
including ones in which the quasi-classical world we see is not present, and the theory gives no
principle for picking the one we inhabit. It tells you which stories are *allowed*, not which one is
*true*. ([SEP: Consistent Histories](https://plato.stanford.edu/entries/qm-consistent-histories/))

### Transactional Interpretation (Cramer)

The wave function ψ and its conjugate ψ* are both real waves: an **offer wave** going forward in
time from the emitter, a **confirmation wave** going backward from the absorber. A quantum event is
a completed **handshake** between them. Kastner's Relativistic/Possibilist TI puts the waves
"outside of physical spacetime" as possibilities, with spacetime emerging from transactions. The
Born rule falls out as ψψ*, which is elegant.
**Problems:** Maudlin's 1996 delayed-choice objection (contested by Kastner); the persistent worry
that it's a *picture* laid over the formalism rather than a distinct theory, since it makes no new
predictions. ([Transactional interpretation](https://en.wikipedia.org/wiki/Transactional_interpretation))

### Two-State Vector / retrocausal accounts

**Advocates:** Aharonov (TSVF), Huw Price (time-symmetry argument), Ken Wharton (all-at-once /
Lagrangian).

A complete description needs *two* state vectors — one from the past boundary condition, one from
the future. Price's argument: the fundamental laws are time-symmetric (CPT), so if you're a realist
about the ontic level, causal dependence should be time-symmetric too — which means retrocausality.
The prize is enormous: **retrocausality exploits a loophole in Bell's theorem.** If future
measurement settings influence past hidden variables, the Statistical Independence assumption fails,
and you can have locality *and* realism.
**Problems:** the bilking argument (Dummett shows it's survivable in the quantum case); the
fine-tuning objection (Wood & Spekkens: the backward influences must conspire to be undetectable);
Shrapnel & Costa showing retrocausal models still require contextuality, which undercuts the whole
motivation; and no independent evidence.
([SEP: Retrocausality in Quantum Mechanics](https://plato.stanford.edu/entries/qm-retrocausality/))

### Wheeler's participatory universe

Wheeler's slogan, adapted from Bohr: **"no phenomenon is a phenomenon until it is an observed
phenomenon."** In the **delayed-choice** experiment, the decision whether to measure which-path or
interference can be made *after* the photon has passed the slits — and the outcome statistics
match the choice you made later. Wheeler's image is the **great smoky dragon**: the tail is sharp
where the photon starts, the mouth is sharp where it bites the detector, and the body in between is
smoke. "What the dragon does or looks like in between we have no right to speak."

He pushed it further with **"law without law"** — that even the regularities are participatory —
and **"it from bit."** This is the most *usable* material in the whole field for a story, and also
the most dangerous, because it is one careless sentence away from woo. Wheeler was not saying human
minds create reality; delayed-choice does **not** let you change the past, and cannot be used to
signal. ([Wheeler, "Law Without Law"](https://gwern.net/doc/science/physics/1983-wheeler.pdf))

### Zurek's quantum Darwinism / einselection

Not a rival interpretation so much as a mechanism that any interpretation can adopt, and the
strongest *deflationary* answer to your thesis. Objectivity is not primitive — it is
**manufactured by redundancy**. Selected information (pointer-state information) proliferates into
the environment in many independent copies; many observers can each sample a different fragment and
agree, without disturbing the system. What looks like an objective classical fact is a fact that has
been copied so many times that disagreement is impossible in practice.
([Quanta on quantum Darwinism](https://www.quantamagazine.org/quantum-darwinism-an-idea-to-explain-objective-reality-passes-first-tests-20190722/))

---

## 3. The two academic homes for your thesis

### 3a. Relational Quantum Mechanics

**This is your thesis, already written, by a good physicist, thirty years ago.** Rovelli's 1996
abstract is the single most important text in this brief. Verbatim, in full:

> ✅ "I suggest that the common unease with taking quantum mechanics as a fundamental description of
> nature (the "measurement problem") could derive from the use of an incorrect notion, as the unease
> with the Lorentz transformations before Einstein derived from the notion of observer-independent
> time. I suggest that this incorrect notion is the notion of observer-independent state of a system
> (or observer-independent values of physical quantities). I reformulate the problem of the
> "interpretation of quantum mechanics" as the problem of deriving the formalism from a few simple
> physical postulates. I consider a reformulation of quantum mechanics in terms of information
> theory. All systems are assumed to be equivalent, there is no observer-observed distinction, and
> the theory describes only the information that systems have about each other; nevertheless, the
> theory is complete."
> — Carlo Rovelli, [*Relational Quantum Mechanics*](https://arxiv.org/abs/quant-ph/9609002),
> Int. J. Theor. Phys. 35 (1996) 1637

Read that again. The Einstein move — "the unease derived from the notion of observer-independent
time" — is *exactly* the user's framing, and it is Rovelli's opening sentence.

**The postulates.** Variables take values only during interactions, not continuously. All values are
relational — a variable has a value *relative to* another system, the way velocity is relative to a
frame. The **Main Assumption**: probabilities for future values relative to S depend on past values
relative to S, and not on values relative to some other system S′.

**The observer is not a person.** This is the tripwire and RQM clears it explicitly:

> ⚠️ "Subjects, or agents play no special role in RQM... There is nothing subjective, idealistic, or
> mentalistic, in RQM."
> — [SEP: Relational Quantum Mechanics](https://plato.stanford.edu/entries/qm-relational/)

And the line you should steal, because it is a perfect BadCode sentence:

> ⚠️ "When we say that our speed is 11km/second with respect to the Sun, we are not attributing
> subjectivity to the Sun."
> — SEP: Relational Quantum Mechanics

An electron can be an observer. A rock can be an observer. A photon's polarisation can be an
observer. "Observer" means *the other end of an interaction*.

**Relative facts vs stable facts.** The 2021 refinement is important because it explains why we
nonetheless agree about everything:

> ✅ "Facts happen at every interaction, but they are not absolute: they are relative to the systems
> involved in the interaction. Stable facts are those whose relativity can effectively be ignored."
> — Di Biagio & Rovelli, [*Stable Facts, Relative Facts*](https://arxiv.org/abs/2006.15543),
> Found. Phys. 51, 30 (2021)

Decoherence is what makes relative facts stable. So: the world is made of perspective-bound events,
and the classical world is the thin crust of events so heavily copied that everyone's version
matches. That is a *story*.

**The criticisms, and they are serious:**

- **Solipsism / loss of intersubjectivity (Adlam 2022).** If facts are perspectival, how does
  science — which runs on shared results — work at all? RQM's answer is that comparison is itself a
  physical interaction, and quantum theory predicts the agreements.
- **The repair — Cross-Perspective Links (Adlam & Rovelli 2023):**

  > ✅ "we propose a new postulate for RQM which requires that all of the information possessed by a
  > certain observer is stored in physical variables of that observer and thus accessible by
  > measurement to other observers, so observers can reach intersubjective agreement about quantum
  > events which have occurred in the past."
  > — Adlam & Rovelli, [*Information is Physical: Cross-Perspective Links in RQM*](https://arxiv.org/abs/2203.13342)

  Critics (Riedel) say the strong reading of this postulate quietly reintroduces absolute facts and
  therefore abandons the very thing RQM was for.
- **Brukner's no-go, "Qubits are not observers":**

  > ✅ "In RQM the physical description of a system relative to an observer cannot represent
  > knowledge about the observer in the conventional sense of this term."
  > — Č. Brukner, [arXiv:2107.03513](https://arxiv.org/abs/2107.03513)

  The bite is **basis ambiguity**: relative to a bare qubit, in *which basis* does the fact obtain?
  A lab setup fixes the basis; a lone electron doesn't.
- **The relativity analogy is only partial — and Rovelli concedes it.** This is the attack you most
  need to pre-empt (see §6C).

  > ⚠️ "the relationalism on which RQM is based is far more radical that the relationalism that
  > underpins classical relativity"
  > and
  > ⚠️ "It is meaningless to compare events relative to different systems, unless this is done
  > relative to a (possibly third) system."
  > — Di Biagio & Rovelli, [*RQM is About Facts, Not States: A Reply to Pienaar and Brukner*](https://arxiv.org/abs/2110.03610),
  > Found. Phys. 52, 62 (2022)

  Their defence of the whole programme is the cleanest one-liner available:

  > ⚠️ RQM "claims that there exists a coherent and complete way of thinking about quantum phenomena
  > that makes sense without requiring many worlds, hidden variables, cognitive agents, or a
  > macroscopic classical world."

### 3b. QBism

Where RQM relativises facts to *any physical system*, QBism relativises them to an **agent** who
takes actions and has experiences.

- A quantum state is not a property of a system. It is **your** state — your personal, Bayesian
  degrees of belief about what you will experience if you act on the world.
  > ⚠️ "a quantum state represents the epistemic state of the one who assigns it concerning that
  > agent's possible future experiences" — [SEP: QBism](https://plato.stanford.edu/entries/quantum-bayesian/)
- The **Born rule is not a law of nature**. It is an addition to the rules of probability — a norm
  of rational consistency. Fuchs describes it as "an addition to the rules of probability theory,
  applicable when an agent considers gambling on the consequences of his interactions with a newly
  recognized universal capacity: dimension." ✅
  ([Fuchs, *QBism, the Perimeter of Quantum Bayesianism*](https://arxiv.org/abs/1003.5209))
- **A measurement outcome is an experience**, created in the agent's interaction with the world, not
  a passive reading of a pre-existing value.
- **Nonlocality dissolves.** Fuchs, Mermin & Schack's abstract, verbatim: ✅ "We give an introduction
  to the QBist interpretation of quantum mechanics. We note that it removes the paradoxes, conundra,
  and pseudo-problems that have plagued quantum foundations for the past nine decades. As an
  example, we show in detail how it eliminates quantum 'nonlocality'."
  ([arXiv:1311.5253](https://arxiv.org/abs/1311.5253), Am. J. Phys. 82, 749)

**Participatory realism** is Fuchs's name for the family, and his abstract is the best single
paragraph of prose in the entire literature for your purposes. Verbatim, in full:

> ✅ "In the Philosophical Investigations, Ludwig Wittgenstein wrote, "'I' is not the name of a
> person, nor 'here' of a place, .... But they are connected with names. ... [And] it is
> characteristic of physics not to use these words." This statement expresses the dominant way of
> thinking in physics: Physics is about the impersonal laws of nature; the "I" never makes an
> appearance in it. Since the advent of quantum theory, however, there has always been a nagging
> pressure to insert a first-person perspective into the heart of physics. In incarnations of lesser
> or greater strength, one may consider the "Copenhagen" views of Bohr, Heisenberg, and Pauli, the
> observer-participator view of John Wheeler, the informational interpretation of Anton Zeilinger and
> Caslav Brukner, the relational interpretation of Carlo Rovelli, and, most radically, the QBism of
> N. David Mermin, Ruediger Schack, and the present author, as acceding to the pressure. These views
> have lately been termed "participatory realism" to emphasize that rather than relinquishing the
> idea of reality (as they are often accused of), they are saying that reality is more than any
> third-person perspective can capture. Thus, far from instances of instrumentalism or antirealism,
> these views of quantum theory should be regarded as attempts to make a deep statement about the
> nature of reality."
> — C.A. Fuchs, [*On Participatory Realism*](https://arxiv.org/abs/1601.04360)

**"Reality is more than any third-person perspective can capture."** That is your thesis in nine
words, from a working physicist, in a citable paper.

**Objections and Mermin's answer.** The standard charge is solipsism. Mermin:

> ⚠️ "Science is a collaborative human effort to find, through our individual actions on the world
> and our verbal communications with each other, a model for what is common to all of our privately
> constructed external worlds." — quoted in [SEP: QBism](https://plato.stanford.edu/entries/quantum-bayesian/)

The sharper objection is **explanatory emptiness** (Timpson): QBism tells you how to bet, not why
anything happens. QBists partly concede this and argue quantum theory contributes to realism
*indirectly*. The cost is real.

**RQM vs QBism, in one line:** RQM says facts are relative to *any interacting physical system* and
is scrupulously non-mentalistic. QBism says quantum states are relative to *agents with experiences*
and is unapologetically first-person. **For BadCode, RQM is the safer chassis and QBism is the
better poetry.** Build on RQM, quote Fuchs.

---

## 4. Wigner's friend, Frauchiger–Renner, and the experiments

**Wigner's friend (1961).** The friend, inside a sealed lab, measures a spin and sees a definite
result. Wigner, outside, has no result yet and must describe friend+system as an entangled
superposition. Two descriptions of the same world. Copenhagen has no principled answer for where the
cut goes. RQM says: both are correct, relative to different systems — the friend's outcome is a fact
*relative to the friend*, not a fact *relative to Wigner*.

**Frauchiger–Renner (2018).** Abstract, verbatim:

> ✅ "Quantum theory provides an extremely accurate description of fundamental processes in physics.
> It thus seems likely that the theory is applicable beyond the, mostly microscopic, domain in which
> it has been tested experimentally. Here we propose a Gedankenexperiment to investigate the question
> whether quantum theory can, in principle, have universal validity. The idea is that, if the answer
> was yes, it must be possible to employ quantum theory to model complex systems that include agents
> who are themselves using quantum theory. Analysing the experiment under this presumption, we find
> that one agent, upon observing a particular measurement outcome, must conclude that another agent
> has predicted the opposite outcome with certainty. The agents' conclusions, although all derived
> within quantum theory, are thus inconsistent. This indicates that quantum theory cannot be
> extrapolated to complex systems, at least not in a straightforward manner."
> — Frauchiger & Renner, [arXiv:1604.07422](https://arxiv.org/abs/1604.07422), Nat. Commun. 9, 3711 (2018)

Three assumptions, at most two of which survive: **Q** (an agent may use quantum theory to predict
outcomes), **C** (consistency — agents' conclusions can be chained without contradiction), **S**
(single outcome — a measurement has one result, full stop). Many-Worlds drops **S**. Bohm and
collapse theories drop **Q** (quantum theory isn't universally applicable as stated). **RQM and
QBism drop C** — because chaining reasoning across different observers' perspectives is exactly the
illegitimate move. Di Biagio & Rovelli's relative/stable-facts paper claims to dissolve FR on
precisely these grounds.

**Local Friendliness (Bong et al., Nature Physics 2020).** Three assumptions:
**Absoluteness of Observed Events** (an observed event is a single, absolute, observer-independent
fact), **Locality**, **No-Superdeterminism**. Quantum correlations violate the resulting inequality,
so at least one must go. The authors state it "places strictly stronger constraints on physical
reality than Bell's theorem" ⚠️ — stronger because the assumptions are *weaker* (no determinism, no
hidden variables assumed). ([arXiv:1907.05607](https://arxiv.org/abs/1907.05607))

**Proietti et al. (2019).** Abstract, verbatim:

> ✅ "The scientific method relies on facts, established through repeated measurements and agreed
> upon universally, independently of who observed them. In quantum mechanics, the objectivity of
> observations is not so clear, most dramatically exposed in Eugene Wigner's eponymous thought
> experiment where two observers can experience seemingly different realities. The question whether
> these realities can be reconciled in an observer-independent way has long remained inaccessible to
> empirical investigation, until recent no-go-theorems constructed an extended Wigner's friend
> scenario with four observers that allows us to put it to the test. In a state-of-the-art 6-photon
> experiment, we realise this extended Wigner's friend scenario, experimentally violating the
> associated Bell-type inequality by 5 standard deviations. If one holds fast to the assumptions of
> locality and free-choice, this result implies that quantum theory should be interpreted in an
> observer-dependent way."
> — Proietti et al., [arXiv:1902.05080](https://arxiv.org/abs/1902.05080), Sci. Adv. 5, eaaw9832 (2019)

**Do not overclaim this.** Six photons. The "friends" were photon paths — single-photon memories,
not conscious beings, not even a computer. The result is a conditional: *if* you keep locality and
free choice, *then* observer-dependence follows. You may instead give up locality or free choice and
keep absolute facts.

The authors' own careful framing is the one to borrow, because it makes the point without the woo:

> ⚠️ the lack of objectivity "does not arise in anyone's consciousness, but between the recorded
> facts."

And their fair warning to sceptics: denying photonic memories observer status "would require a
convincing revision of our minimal definition of what qualifies as an observer, which typically
comes at the cost of introducing new physics that is not described by standard quantum theory." ⚠️

**What all three actually establish:** that "every observed event is a single absolute fact for
everybody" is not a free assumption. It costs something. That is a genuine, hard-won, experimentally
supported result and it is the empirical spine of your story.

---

## 5. Contextuality: what "the value didn't exist before you measured it" is licensed to mean

**Bell's theorem.** Assumptions: local causality (factorizability), statistical independence (the
settings aren't correlated with the hidden state), no-superdeterminism. Quantum predictions violate
the resulting inequalities. Loophole-free experiments in 2015 closed both the locality and detection
loopholes simultaneously, with violations at ~11.5σ; the 2022 Nobel went to Aspect, Clauser and
Zeilinger. ([SEP: Bell's Theorem](https://plato.stanford.edu/entries/bell-theorem/))

**Ruled out:** local hidden-variable theories. Full stop. This one is settled.

**NOT ruled out, and you will get caught if you claim otherwise:** nonlocal hidden variables (Bohm
is alive and well); superdeterminism (unpopular, not refuted); retrocausality; Many-Worlds.
**Bell does not show that consciousness collapses anything, that observers create reality, or that
you can signal faster than light.** Entanglement is provably no-signalling: Alice's marginal
statistics are completely unaffected by what Bob does. You only see the correlation after you
classically compare notes — at or below light speed.

**Kochen–Specker.** For Hilbert spaces of dimension ≥ 3, you cannot consistently assign
pre-existing values to all observables while requiring that a value not depend on *which compatible
set of observables you measure it alongside*. The two assumptions:

- **Value Definiteness (VD)** — ⚠️ "All observables defined for a QM system have definite values at
  all times."
- **Noncontextuality (NC)** — ⚠️ "If a QM system possesses a property (value of an observable), then
  it does so independently of any measurement context, i.e. independently of *how* that value is
  eventually measured."

The conclusion, in the SEP's words: ⚠️ "acceptance of QM logically forces us to renounce either VD or
NC." ([SEP: Kochen–Specker](https://plato.stanford.edu/entries/kochen-specker/))

**So what is "the value didn't exist before you measured it" licensed to mean?**

Licensed: *There is no assignment of definite values to all observables that is independent of the
measurement context. Whatever a measurement is, it is not the passive revelation of a
pre-existing, context-free property.* That is rock solid.

Not licensed: *nothing exists until observed*; *the electron has no properties*; *you choose the
outcome*; *your mind makes it real*. Bohm keeps definite values by making them contextual. Everett
keeps everything by dropping single outcomes. The theorems constrain the space; they don't hand you
idealism.

**The best available metaphor for contextuality is musical, and you already own it.** A single pitch
— a C — is a root, a third, a fifth or a seventh depending on the chord underneath it. The note has
no context-free harmonic function. Play the chord, the function appears; play a different chord, a
different function appears; and it is not that the "true" function was hiding. *That* is
contextuality, and it is real physics, not analogy-stretching.

---

## 6. Honest verdict on the thesis, element by element

### A. "Many-Worlds says the particle collapses here in our universe and there in another."
**(d) Simply wrong** — and wrong in the way that gets you dismissed in the first sentence.
Many-Worlds' defining move is *deleting* collapse. There is no "our universe" and "another" as
pre-existing containers; branches are structures that decoherence carves inside one universal wave
function, and on the mainstream (Wallace) account branching is local and propagates at light speed,
not global and instantaneous.

**Fix:** if the story needs a foil, attack the *right* Many-Worlds. The honest attack is: "Everett's
price is that 'you' is no longer a well-defined thing, and that probability stops meaning anything —
if every outcome happens with certainty, what is a 70% chance a chance *of*?" That's the live
critique, and it's better drama anyway.

### B. "It isn't in many places at once — it simply hasn't been decided/measured by you yet."
**(b) A live minority interpretation — but only under one of its two readings, and the wrong reading
is (d) wrong.**

- ❌ **If "hasn't been decided by you" means "it already has a value and you don't know it yet"** —
  that is naive hidden variables, and Kochen–Specker plus Bell kill it. This is the trap. It is also
  the reading a casual audience will default to, so you must actively block it.
- ✅ **If it means "no value obtains at all until an interaction occurs, and when it does, it obtains
  relative to the interacting system"** — that is Relational QM. Published, defended, in the
  Stanford Encyclopedia, ~30 years old, with an experimental literature behind it.

**Say "undetermined," never "unknown." Say "no fact yet," never "hidden."** That one word choice is
the difference between the story being smart and the story being wrong.

### C. "Just as Einstein removed the global clock, there may be no global bifurcation."
**(b) A live minority interpretation — and it is Rovelli's own headline argument.** You can quote his
1996 abstract directly; the Einstein analogy is his, not yours.

**But know the counterpunch, because it is the best one available and Rovelli concedes it.** In
special relativity, observers disagree about simultaneity *but there is a Lorentz transformation* —
an exact, invertible dictionary converting my frame to yours — and there are **invariants** (the
spacetime interval, proper time, rest mass) that every observer agrees on. Relativity relativises
the *coordinates* while preserving an absolute *geometry*. RQM has **no such dictionary and no such
invariants**: you cannot transform Alice's facts into Bob's facts; you can only ask a third system,
which yields yet another set of relative facts. Pienaar pressed exactly this; Di Biagio and Rovelli
answered ⚠️ "the relationalism on which RQM is based is far more radical that the relationalism that
underpins classical relativity."

**This is good news for the story, not bad.** Don't claim the analogy is exact. Claim it is
*insufficient* — Einstein took away the global clock but left the master geometry; quantum theory
takes away the master geometry too. That is a bigger, darker, more BadCode line, and it is what the
literature actually says.

### D. "Only measurement relative to an observer."
**(b) Live, conditional on the definition of "observer."** In RQM, an observer is any physical
system on the other end of an interaction — a rock, an electron, a photon's polarisation. If your
story ever implies "observer = a mind," you have left physics and entered the woo zone, and the
first physicist to read it will say so. Guard this in the text explicitly. Steal SEP's Sun line.

### E. The music analogy: "music is a wave until you hear it; one thing that lands differently
depending on who's listening and their mood."
**(c) A metaphor with no physical content — and it leans toward (d), because it smuggles in the
picture the theorems rule out.** Three specific failures:

1. **Sound is a wave before, during and after you hear it.** Hearing changes nothing. There is a
   perfectly determinate pressure field in an empty room. That's classical physics — the *opposite*
   of the point.
2. **"Lands differently depending on your mood" is about differing interpretations of one shared,
   observer-independent signal.** That's psychoacoustics. RQM says the *fact itself* is relative,
   not the *reading* of an agreed fact. The analogy accidentally asserts exactly the absolute fact
   you were trying to deny.
3. It hands the audience the hidden-variable picture: one real determinate thing, differently
   perceived. Kochen–Specker says no.

**Repairs, in ascending order of accuracy — all still musical, so you keep the register:**

- **"There is no master recording."** Every listener holds a different dubplate, and there is no
  studio original to appeal to — *and no mixing desk that can convert one cut into another*. The
  missing desk is the missing Lorentz transformation. This is the best one: it carries both the
  relational claim and the disanalogy that makes it radical.
- **"A jam, not a pressing."** A record is a fixed thing heard differently. A jam has no take until
  it's played, and there's no take that exists apart from the playing.
- **"The note doesn't exist until it's answered."** Call and response as interaction-makes-the-fact.
- **For contextuality specifically: the C that is a root, a third, or a seventh depending on what's
  under it.** This one is not a stretch at all — it's a fair rendering of real physics.

### F. Overall
Your thesis, stated carefully, is **a live minority interpretation with reputable academic
advocates, experimental relevance, and a Stanford Encyclopedia entry.** It is not fringe. It is also
not consensus, and it makes no novel predictions — which is the ceiling on how strongly you can
assert it. As fiction premised on real physics, it is unusually well-founded. The three things that
would sink it are the Many-Worlds caricature, the "unknown vs undetermined" slip, and the
music-as-wave metaphor.

### The strongest attack a working physicist would make, in order

1. **"You've garbled Many-Worlds — there is no collapse in it. If you can't state the view you're
   rejecting, why should I trust the view you're selling?"** *(Fatal if unfixed; trivially fixed.)*
2. **"'Relative to an observer' isn't physics until you tell me what an observer is and hand me the
   dynamics. RQM makes no new predictions. It's a way of talking."** *(Fair. Concede it. RQM is an
   interpretation and Rovelli says so; its virtue is dissolving paradoxes, not predicting new
   effects. Note that FR and Local Friendliness give the position real teeth.)*
3. **"Your relativity analogy has no Lorentz transformation and no invariants. That isn't relativity,
   it's fragmentation."** *(Real. Rovelli concedes it. Turn it into the point — see §6C.)*
4. **"'Not decided by you yet' is just ignorance of a pre-existing value. Kochen–Specker and Bell
   killed that in 1964 and 1967."** *(Fatal if you use the word "unknown." Say "undetermined.")*
5. **"Brukner: qubits aren't observers. Relative to a bare electron, in which basis does your fact
   even obtain?"** *(Genuinely open. Rovelli's reply is that "knowledge" plays no fundamental role
   in RQM. Don't pretend it's settled.)*
6. **"Decoherence and quantum Darwinism already explain why we all agree, and they're actual physics
   with actual calculations. You don't need your story."** *(The deflationary attack. The answer:
   quantum Darwinism explains agreement about the outcomes; it does not explain why there is an
   outcome. Cite the SEP decoherence line.)*
7. **"The moment your 'observer' is a person, you're doing Deepak Chopra."** *(Pre-empt it in the
   text.)*

---

## 7. Glossary — safe to use

- **Superposition** — a definite quantum state that is not an eigenstate of the observable being
  measured. *Not* "in two places at once."
- **Born rule** — outcome probabilities are the squared magnitudes of amplitudes.
- **Decoherence** — loss of interference through entanglement with the environment. Real,
  calculated, universally accepted. Does not by itself produce outcomes.
- **Einselection** — environment-induced selection of the pointer states that survive decoherence.
- **Pointer states** — the states robust under environmental monitoring; the ones that get copied.
- **Quantum Darwinism** — objectivity as redundancy: the environment holds many independent copies
  of pointer-state information.
- **Improper mixture** — looks like classical ignorance, provably isn't.
- **Contextuality** — the value of an observable depends on which compatible observables are
  measured with it. Kochen–Specker, 1967.
- **Noncontextual hidden variables** — ruled out (dim ≥ 3).
- **Local hidden variables** — ruled out (Bell, loophole-free 2015, Nobel 2022).
- **No-signalling** — entanglement cannot transmit information. Non-negotiable.
- **Relative fact / stable fact** — Di Biagio & Rovelli's distinction. Use freely; it's the most
  quotable machinery you have.
- **Absoluteness of Observed Events (AOE)** — the assumption that an observed event is a single
  observer-independent fact. The one RQM and QBism reject. Precise, current, citable.
- **Local Friendliness** — the Bong et al. no-go. Stronger than Bell.
- **Participatory realism** — Fuchs's umbrella. "Reality is more than any third-person perspective
  can capture."
- **Wigner's friend / extended Wigner's friend** — the canonical scenario.
- **Relational quantum mechanics** — name it. It gives you a citation instead of a vibe.
- **Delayed choice** — Wheeler's experiment. Real, done, no retrocausal signalling.
- **Preferred basis problem**, **the measurement problem**, **unitary evolution**, **eigenstate**,
  **Hilbert space** — all safe if used correctly.

## 8. Blacklist — words that mark you as a crank

- ❌ **"Quantum consciousness."** Tegmark computed neural decoherence times of **10⁻¹³–10⁻²⁰ s**
  against neural process times of **10⁻³–10⁻¹ s** — off by ten or more orders of magnitude — and
  concluded ✅ "the degrees of freedom of the human brain that relate to cognitive processes should
  be thought of as a classical rather than quantum system."
  ([quant-ph/9907009](https://arxiv.org/abs/quant-ph/9907009), Phys. Rev. E 61, 4194)
- ❌ **"Observer = human mind" / "consciousness collapses the wave function."** Von Neumann and
  Wigner flirted with it; Wigner abandoned it; Bohr explicitly denied it. It is not the mainstream
  and never was.
- ❌ **"Energy," "vibration," "frequency," "resonance"** used metaphysically. Instant credibility
  loss.
- ❌ **"Quantum leap" meaning "a big jump."** It means the smallest possible change.
- ❌ **"Quantum entanglement lets you communicate / influence at a distance."** No-signalling.
- ❌ **"Observation creates reality" / "nothing exists until observed"** as a flat assertion. What is
  licensed is far more specific and far more interesting.
- ❌ **"Many-Worlds means the universe splits into copies of you."** Sloppy; branching is local and
  decoherence-driven.
- ❌ **"Science proves we create our own reality."** No survey of physicists supports this framing.
- ❌ **"Quantum" as an adjective for anything that isn't quantum.** Quantum healing, quantum
  manifestation, quantum leadership.
- ❌ **"The wave function is a physical wave in space."** It lives in 3N-dimensional configuration
  space; whether it's "physical" is exactly what's disputed.
- ❌ **"Decoherence solved the measurement problem."** It didn't.
- ❌ **"Heisenberg's uncertainty principle means the observer disturbs the system."** That's the
  discredited "observer effect" gloss; uncertainty is a structural property of conjugate variables,
  true even with no measurement at all.

---

## Source list

**Primary papers**
- Rovelli, *Relational Quantum Mechanics* (1996) — https://arxiv.org/abs/quant-ph/9609002
- Di Biagio & Rovelli, *Stable Facts, Relative Facts* (2021) — https://arxiv.org/abs/2006.15543
- Di Biagio & Rovelli, *RQM is About Facts, Not States: Reply to Pienaar and Brukner* (2022) — https://arxiv.org/abs/2110.03610
- Adlam & Rovelli, *Information is Physical: Cross-Perspective Links in RQM* (2022) — https://arxiv.org/abs/2203.13342
- Brukner, *Qubits are not observers — a no-go theorem* (2021) — https://arxiv.org/abs/2107.03513
- Fuchs, *On Participatory Realism* (2016) — https://arxiv.org/abs/1601.04360
- Fuchs, *QBism, the Perimeter of Quantum Bayesianism* (2010) — https://arxiv.org/abs/1003.5209
- Fuchs, Mermin & Schack, *An Introduction to QBism…* (2013) — https://arxiv.org/abs/1311.5253
- Frauchiger & Renner, *Quantum theory cannot consistently describe the use of itself* (2018) — https://arxiv.org/abs/1604.07422
- Bong et al., *A strong no-go theorem on the Wigner's friend paradox* (2020) — https://arxiv.org/abs/1907.05607
- Proietti et al., *Experimental test of local observer independence* (2019) — https://arxiv.org/abs/1902.05080
- Zurek, *Quantum Darwinism, Classical Reality, and the Randomness of Quantum Jumps* (2014) — https://arxiv.org/abs/1412.5206
- Tegmark, *The importance of quantum decoherence in brain processes* (2000) — https://arxiv.org/abs/quant-ph/9907009
- Wheeler, *Law Without Law* (1983) — https://gwern.net/doc/science/physics/1983-wheeler.pdf

**Stanford Encyclopedia of Philosophy**
- Relational QM — https://plato.stanford.edu/entries/qm-relational/
- QBism / Quantum Bayesianism — https://plato.stanford.edu/entries/quantum-bayesian/
- Copenhagen Interpretation — https://plato.stanford.edu/entries/qm-copenhagen/
- Many-Worlds — https://plato.stanford.edu/entries/qm-manyworlds/
- Bohmian Mechanics — https://plato.stanford.edu/entries/qm-bohm/
- Collapse Theories — https://plato.stanford.edu/entries/qm-collapse/
- Consistent Histories — https://plato.stanford.edu/entries/qm-consistent-histories/
- Retrocausality in QM — https://plato.stanford.edu/entries/qm-retrocausality/
- Decoherence — https://plato.stanford.edu/entries/qm-decoherence/
- Bell's Theorem — https://plato.stanford.edu/entries/bell-theorem/
- Kochen–Specker Theorem — https://plato.stanford.edu/entries/kochen-specker/
- Philosophical Issues in Quantum Theory — https://plato.stanford.edu/entries/qt-issues/

**Journalism and surveys**
- Quanta, *Quantum Darwinism… Passes First Tests* — https://www.quantamagazine.org/quantum-darwinism-an-idea-to-explain-objective-reality-passes-first-tests-20190722/
- Quanta, *Quantum Mischief Rewrites the Laws of Cause and Effect* — https://www.quantamagazine.org/quantum-mischief-rewrites-the-laws-of-cause-and-effect-20210311/
- *Nature* 2025 interpretation survey, coverage — https://thequantuminsider.com/2025/08/02/a-century-into-quantum-mechanics-physicists-still-cant-agree-what-it-means-nature-survey-shows/
- Science News on the same poll — https://www.sciencenews.org/article/poll-quantum-physicists-shows-agreement-disagreement-and-something-between
- *Has Anything Changed? Tracking Long-Term Interpretational Preferences* — https://arxiv.org/pdf/2507.09988
- Transactional interpretation overview — https://en.wikipedia.org/wiki/Transactional_interpretation
- Howard, *Who Invented the "Copenhagen Interpretation"?*, Phil. Sci. 71 (2004) 669–682

**Not obtained.** Nature and Science full texts (paywalled/redirect-blocked): Frauchiger–Renner and
Bong et al. were read via arXiv preprints, Proietti via the arXiv HTML. Rovelli 1996 full text was
not machine-readable; the abstract is verbatim from arXiv and the body is summarised via SEP.
Web-search budget for the session was exhausted before I could reach Adlam's *Does science need
intersubjectivity?* directly — its argument is relayed accurately via the SEP RQM entry but the
paper itself is worth a follow-up read.
