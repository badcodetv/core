# Evidence — grades, corrections, and the never-cite list

The sweep's own critics caught wave one inflating grades: building **P** (practitioner
consensus) out of three content-mill sites agreeing, when three restatements of one uncredited
claim is not independent corroboration. This file is the ledger, and it is the authority when a
brief and this file disagree.

**Grades.** **A** academic/empirical or hard optical fact · **A (mixed)** peer-reviewed but
contested or single-study · **P** practitioner consensus, multiple independent named humans ·
**p** one practitioner or one case · **myth** · *(unverified in sweep)* where the primary source
was not reached.

---

## 1. Corrections applied during distillation

| Claim | Brief's grade | Our grade | Why |
| --- | --- | --- | --- |
| "50–75 characters per line" for captions | **P** | **dropped** | Zero citation anywhere in brief 19 — not a weak source, *no* source. Nothing to trace |
| Corrected verticals as architectural photography's baseline | **P** | **p** | Two blog-tier sources agreeing. The underlying lens geometry stays **A**; the convention riding on it does not |
| Foreground/midground/background = depth | **P** | **P**, kept | Content-mill sourced, but the brief's own caveat is honest and the claim is uncontroversial trade practice |
| "Low angle = powerful" | **P** (briefs 07, 13) | **A (mixed)**, and weaker than stated | Brief 05's controlled studies beat content-mill convergence. One study found eye-level trusted *more*; one found the effect reversed |
| Kuleshov, popular form | **A (mixed)** (brief 09) | **myth** in its popular form | Prince & Hensley 1992 controlled replication failed. The narrow version (adjacency shapes inference) survives at **A** |
| Murch's Rule of Six percentages | **P**, repeated in 08/09/10 | *(unverified)* | The same secondary paraphrase cited three times from one page, never against Murch's own text. Repetition made it look solid; it isn't |
| *Metropolis*/*Brazil* dystopian architecture | **A (mixed)** | **p** | One ResearchGate paper, abstract only. A grade of A for an unread source |
| "Blue hour produces the monumental read" | flagged and self-downgraded in brief 18 | **p** | Brief 18 caught itself. Noted as good practice |

## 2. The strongest claims — what we can lean on

| Claim | Grade | What the evidence is |
| --- | --- | --- |
| Perspective distortion is a function of camera *distance*, not focal length | **A** | Optical geometry. Uncontested; most film-education sources have it wrong |
| Hard vs soft light shadow character | **A** | Source size relative to subject. Optics |
| Lightness anchoring — darkness is judged relative to the brightest region groupable into the scene | **A** | Gilchrist's anchoring theory of lightness perception. **The mechanism under our #1 craft rule** |
| Banding in dark gradients is bit-depth quantisation | **A** | Arithmetic: 8-bit gives 256 steps per channel; dark gradients occupy a small slice |
| Dither/grain fixes banding by breaking quantisation edges | **A** | Signal processing. Film grain did this free for a century |
| Full/limited range mismatch clips everything below a threshold to black | **A** | Metadata/signal fact, documented across broadcast and GPU engineering. **We shipped this bug in `camping.mp4`** |
| Compression allocates fewest bits to dark, low-detail regions | **A (mixed)** | Rate-distortion principle is fact; which artifact dominates depends on codec and bitrate |
| Atmospheric perspective as a depth cue | **A** | Vision science and landscape painting alike |
| Awe = vastness + need for accommodation | **A (mixed)** | Keltner & Haidt — the standard citation, but theoretical/prototype-based, not itself an experiment |
| The small-self effect increases prosocial behaviour | **A** | Piff et al. 2015 — five studies, N=2,078, lab + field + national survey. One of the better-replicated results in the field |
| Threat-based awe as a distinct variant, ~1 in 5 awe experiences | **A (mixed)** | Gordon et al. 2017, single core study with follow-up work |
| Audiences track actions and goals, not camera geometry | **A** | Magliano & Zacks; Smith & Henderson — real cognitive-science work on continuity editing |
| Viewers only notice continuity errors where they are already looking | **A** | Same literature |
| Adjacency shapes inferred meaning (the narrow Kuleshov) | **A** | Cao et al. 2024, PLoS One, fMRI |
| Average shot length has shortened across a century | **A** | Statistical film analysis (Cutting, Salt). A measured trend, not a law |
| Leading lines increase purposeful fixation | **A (mixed)** | Eye-tracking work; viewers fixate longer when a line leads to a clear subject |
| Bazin's centripetal/centrifugal framing | **A (mixed)** | Canonical film theory — interpretive scholarship, not an empirical study |
| Barthes on anchorage (text fixes an image's meaning) | **A** | Canonical semiotics, widely cited. Counter-position "relay" also exists |
| Burke on the sublime — darkness and obscurity as instruments | **A** as intellectual history | What the 1757 text says. Not a claim about brains |
| WCAG 4.5:1 contrast minimum | **A** | W3C standard grounded in vision-science testing. A floor, not a target |
| White-on-black halation slows reading | **A** for the mechanism | Optical irradiation. The astigmatism prevalence figure is *(unverified)* |
| Aspirational reading — satire of power read as celebration | **A (mixed)** | Documented repeatedly: Verhoeven on *Starship Troopers*, Harron on *American Psycho*, *Fight Club*, *Wolf of Wall Street* |

## 3. 🔴 Never cite these

| Claim | Status |
| --- | --- |
| "The eye naturally goes to the rule-of-thirds intersections" | **myth** — no supporting study. Evidence points to motion, faces, and lines leading to a subject |
| "Science proves the rule of thirds is more pleasing" | **myth** — generic uncited SEO material |
| "Symmetry is calm and pleasing" / any fixed meaning for symmetry | **myth** — Kubrick's dread vs Anderson's whimsy, identical device |
| Three-point lighting as mandatory | **myth** — a teaching diagram |
| Genre-to-ratio lookup tables (comedy 2:1, horror 8:1) | **myth** — a loose teaching convention presented as a rule |
| "Red means passion" / any fixed colour-to-emotion code | **myth** — lab evidence is single swatches on blank grounds |
| "Orange advances, blue recedes" | **myth** — folklore riding on the real complementary-contrast fact |
| A confirmed inventor or origin film for teal-and-orange | **myth** — no single origin exists |
| "Wide lenses distort faces more than telephoto" | **myth** — it is shooting distance |
| "Anamorphic is more cinematic" | **myth** — a specific optical mechanism with tradeoffs, not a quality stamp |
| Low angle = power, as a universal law | **myth as stated** — real but weak, context-dependent, and reversed in direct address |
| "A POV shot creates identification" | **myth** — explicitly rejected in cognitive film theory (Smith, Carroll) |
| "Handheld is more truthful" / "vérité captures reality unmediated" | **myth** — a reproducible style; the movement's own definition concedes construction |
| "Dolly and zoom are interchangeable" | **myth** — parallax versus flat magnification is a hard optical difference |
| The dolly zoom as a safe universal big-moment trick | **myth** — reads as cliché exactly when reached for generically |
| Kuleshov as "one face reads as three emotions" | **myth in its popular form** — Prince & Hensley 1992 replication failed |
| "Faster cutting is objectively more exciting" | **myth** — a historical trend, not a quality law |
| "More coverage is safer" | **myth for us** — contradicted by Fincher's own method and unaffordable under our cost model |
| Murch's Rule of Six as a flat unordered checklist | **wrong** — it is explicitly hierarchical with a stated sacrifice order (but the percentages are *unverified*) |
| "Never cross the 180-degree line" applied to a single generated shot | **category error** — it only means something when cutting between angles of one continuous action |
| "The 30-degree rule is a measured perceptual threshold" | **myth** — it is convention |
| "Godard invented the jump cut" | **myth** — he popularised a pre-existing device |
| "An establishing shot is mandatory" | **myth** — a convenience |
| "The decisive moment means catching peak action" | **myth** — contradicted by Cartier-Bresson's own definition |
| "Ken Burns invented pan-and-zoom on stills" | *(unverified — commonly claimed, not sourced)* |
| "Higher resolution fixes a flat shot" | **myth** — flatness is depth-layer separation, not detail density |
| "Brutalism is inherently oppressive" | **myth** — the oppression is framing and lighting, not the concrete |
| "Monumental scale + symmetry = inherently fascist grammar" | **myth** — same vocabulary indicts in *Metropolis* and *Brazil* |
| "If the intent is satirical, the imagery is safe" | **myth** — contradicted by the directors' own accounts of reception |
| "Aerial/drone is the natural way to show scale" | **myth** — elevation collapses legible scale into pattern |
| "An empty room is automatically eerie" | **myth** — needs legible human-scaled proportions |
| "White on black is most readable because max contrast" | **myth** — halation makes it worse than off-white on dark grey |
| Any fixed sound-off viewing percentage stated as universal | **unsourced** — direction is consistent, magnitude is disputed vendor marketing |
| Caption-engagement lift percentages (80% more likely, 12% longer) | **unsourced vendor marketing** |
| Kinetic-type motion-to-emotion mappings (shaking = fear) | **design lore**, not findings |
| "Just crush the blacks for a moody look" | **myth** — destructive once baked in |
| "More denoising makes a dark shot cleaner" | **wrong** — removing masking noise increases banding |
| "If it looks fine on my monitor it looks fine on a phone" | **wrong** — ambient light on a glossy panel is close to worst case for us |
| Any specific IRE number as a universal target | **house convention, not physics** — the direction (don't clip to 0) is real |
| "Awe expands subjective time" | **contested** — one study yes, one replication no |
| "Audiences don't consciously notice motifs, they just feel it" | **unmeasured** — do not state as science |
| "Rule of three" as a scientific minimum for motif recognition | **folklore** — no supporting study |

## 4. Known weaknesses in the corpus itself

- **Single-source dependency on Roger Deakins.** Cited in 8 of 14 wave-one briefs, largely via
  his own forum. Good sourcing discipline, but "what does Deakins say" risks standing in for
  "what is craft consensus."
- **Content-mill convergence** was the structural failure of wave one. Wave two largely defended
  against it; several briefs downgraded themselves inline.
- **Nothing here has been tested on BadCode work.** Brief 17's visible-cost checklist in
  particular has never been run against a shipped frame. Its own recommendation is to try it on
  three or four before it becomes doctrine.
- **No evidence exists either way on our actual reader.** Neither our register nor social realism
  has been measured on a working-class UK audience. See `principles.md` §R1.
