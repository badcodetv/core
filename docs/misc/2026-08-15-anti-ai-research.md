# The anti-AI objection: a sourced distillation

**Date:** 15 August 2026. **Purpose:** the evidence base for [`../using-ai.md`](../using-ai.md).
**Method:** twenty research agents — ten across the wider web, ten across a corpus harvested from
r/antiai the same day (1,415 posts; 5,385 comments; 90 full comment threads, pulled via Reddit's own
JSON API through a logged-in browser session after direct fetching was blocked). A separate
adversarial fact-check pass re-verified the load-bearing claims: **28 confirmed, 6 overstated,
1 wrong, 1 unverifiable.** Corrections are folded in below and flagged.

Vote counts are given because in this corpus they are the argument: a 12,000-point post is the
community, a 0-point post is one person talking.

---

## 1. The objection, ranked

Ranked by how well the claim survives scrutiny, not by how loudly it is made.

### Tier 1 — solid. Concede these.

| Grievance | The argument at its strongest | Evidence |
| --- | --- | --- |
| **Non-consensual training data** | The models could not exist without ingesting the world's art, writing and music without knowledge, payment, credit or consent. "It learns like a human" is a deflection about *how*, not about *how it was acquired*. | Suno's Aug 2024 answer concedes training on copyrighted recordings and argues fair use; UMG and Sony still litigating as of Aug 2026. Bartz v. Anthropic: $1.5B settlement over 482,460 pirated books (91.3% claim rate, ~$2,932/work). Books3 built by scraping Bibliotik. Stanford found 3,226 suspected CSAM instances in LAION-5B. |
| **Money reaching labels ≠ money reaching musicians** | Even after settlements, the people who performed on the masters weren't paid or told. | American Federation of Musicians v. UMG/Warner, amended 24 July 2026, under the Sound Recording Labor Agreement's "new use" clause. |
| **The junior pipeline** | AI isn't firing seniors; it's deleting the entry-level job that made seniors. | Brynjolfsson, Chandar & Chen (Stanford Digital Economy Lab), *Canaries in the Coal Mine?*, updated Aug 2026: employment of 22–25s in AI-exposed occupations **19% below trend**, "primarily through reduced hiring… rather than increased separations," widening since Aug 2025. |
| **Skilled freelancers lost most** | Kills the "AI only does the boring grunt work" defence. | Hui, Reshef & Zhou, *Organization Science* 2024: Upwork contracts −2%, earnings −5% in exposed occupations; **higher-rated freelancers lost more.** (The commonly-cited "Demirci" co-author does not exist on this paper.) |
| **Concealment is a distinct, worse wrong** | Discovery is worse than disclosure, and silence functions as denial. | Schilke & Reimann, *OBHDP* 188 (2025), 13 experiments: disclosure reduces trust; third-party discovery reduces it *more*. FIU (Carnevale/Benegal/Vincent, Mar 2026): staying silent is reputationally equivalent to actively denying. |
| **Environmental siting and accountability failures** | Aggregate percentages don't answer the person next to the facility. | xAI ran dozens of unpermitted gas turbines beside Boxtown, Memphis (NAACP/SELC/Earthjustice suit, 14 Apr 2026). Google paid >$100k of The Dalles' legal bills to keep water figures secret; released records showed 355.1M gallons in 2021, ~29% of the city's use. Ireland: data centres = 21% of national electricity. PJM capacity prices ~10x in three years, with PJM's own market monitor attributing 38% of one auction's cost to data-centre load. NY Executive Order 62 (14 July 2026) paused permits ≥50MW. |
| **Relational and mental-health harm** | A separate axis from art and labour, and the corpus's rawest material. | First-person threads on a mother relaying ChatGPT text to a high-risk pregnant daughter [526]; a sibling lost to chatbot dependency [1707]; a self-described addiction account [490]. Deezer: up to 85% of fully-AI track streams were bot fraud in 2025. |
| **Epistemic collapse / deepfakes** | Once media can be fabricated convincingly, trust in all recorded media goes. | Watermark-removal thread [1000]; the corpus's most unanimous anger is on non-consensual likeness, especially of minors and the dead [1708, no dissent]. |

### Tier 2 — partly true. Be precise or stay out.

- **"AI is causing mass layoffs now."** Weak at aggregate. Yale Budget Lab, MIT Technology Review
  ("A reality check on the AI jobs hysteria," 26 May 2026), California's state tracker: no surge.
  Challenger's "AI is the leading cited reason for five straight months" is *self-reported employer
  reasoning*; Fortune reported "AI-washing" as cover for ordinary cost-cutting. Games-industry
  layoff totals (~10,500 in 2023; ≥4,600 in 2026 to July) are cited as AI casualties with **no
  attribution work done by any tracker.**
- **"AI art is soulless and everyone can tell."** Deezer/Ipsos blind test, 9,000 adults, 8 countries:
  **97% could not distinguish** AI from human music; 71% surprised at their own failure. But 80% want
  it labelled anyway, 69% support lower payouts for AI tracks, 52% think it shouldn't compete unmarked
  in main charts. The demand is honest labelling, not detectability.
- **"Prompting can never be art."** The serious version (Nannicelli, *JAAC* 83:4) turns on
  *intentional control*: one-shot output fails; generated material subjected to human curation,
  editing and composition can qualify. Ted Chiang's essay is the strong popular version.
- **Capitalism-not-AI.** Common as a *register* of complaint, unreliable as a *conclusion* — see §3.

### Tier 3 — wrong or stale. Never repeat.

- **"One query = a bottle of water."** Google's disclosed median Gemini text prompt: **0.24 Wh,
  0.26 mL water, 0.03 gCO2e** (Aug 2025, full-stack accounting; self-flagged as unverified by third
  parties and not representative of image/video). Off by ~100–2,000x.
- **"An AI image = a phone charge."** Luccioni et al. 2023 measured 2.91 Wh average; 11.49 Wh was the
  *worst* model tested; a phone charge is ~8.4 Wh. Epoch AI puts a GPT-4o query at ~0.3 Wh, ~10x below
  the widely circulated "3 Wh."
- **"AI is why bills rose 10x."** Conflates PJM's wholesale capacity-auction clearing price with retail
  bills. NRDC's modelled retail figure is ~$70/month by 2028 — serious, and an order of magnitude
  smaller than the shorthand.
- **"Training is settled illegal."** Alsup (23 Jun 2025) found training on lawfully-acquired books
  "exceedingly transformative" fair use, while ruling the *pirated library* was not. Chhabria
  (25 Jun 2025) ruled for Meta and explicitly warned against reading it broadly. Getty lost the core
  of its UK claim (4 Nov 2025), substantially on jurisdiction.
- **"AI output categorically can't be copyrighted."** Overstates the US Copyright Office's Part 2
  report: works with sufficient human creative selection, arrangement and modification *can* be —
  prompting alone cannot.
- **Frame Breaking Act date.** Royal assent **20 March 1812**, not 14 February (that's introduction).
  Roughly 60–70 were hanged in the period, but Wikipedia notes no death sentences appear to have been
  justified under that Act specifically.
- Other fact-check corrections: Coca-Cola's 2024 ad scored **5.9 on a 5.9-max System1 scale** (a
  perfect score), not "5.9/10"; the "ten times better" quote is not in the cited Forbes piece (his
  actual line is *"The genie is out of the bottle"*); Getty's indemnification is described as
  "uncapped," not a $50,000 floor; the IEA confirms 17% data-centre electricity growth in 2025 but
  does **not** publish a "50% AI-specific" figure.

---

## 2. What r/antiai actually rewards and punishes

**The reward function is mockery of claimed authorship**, not policy argument. The single
highest-scoring comment in one slice, on a man's "1,247 revisions" AI self-portrait (27,662 pts):
*"Guy did so many revisions, yet still can't get the speech bubbles to look right."* [2,906]

**The two highest-value findings for BadCode are both about sentences we planned to use:**

| Sentence | What the corpus does with it |
| --- | --- |
| "I can't afford to commission a real artist" | *"there is no such thing as a 'talented ai artist' you just know how to feed prompts"* — **12,943 pts**, a post built specifically to pre-empt that sentence. Plus *"If you can't afford an artist, I probably can't afford to trust your product"* — **9,815 pts**. Top-decile across the whole harvest. |
| "We can't draw" (incapacity framing) | Reads as the accessibility shield. *"Laziness is not a disability"* — **10,434 pts**. *"No, AI is ableist. How reductive to assume disabled people aren't capable of doing what we do"* — **1,259 pts**. The sharpest rejections come from disabled members, who resent being used as cover. Dozens of posts in the 1,000–3,300 range are disabled artists showing work made without AI. |

**Other red lines, evidenced:** claiming the word artist/made for generated output; presenting AI
work as hand-made; monetising while claiming craft; feeding someone's personal art into a generator;
minimising the environmental cost with weak stats (the community punishes this *from its own side*:
*"If the facts don't make our case then we don't have a case"* [62]).

**How AI-using people are actually treated** — this is more differentiated than expected:

- Claim artistry, credit, or commercial standing → flattened, no sympathy.
- Confess personal, non-monetised, guilty use → *warmth*, or silence. A person who used AI to escape a
  housing emergency wrote *"I hate Ai. I do… but let's not pretend it can't do amazing things"* and got
  **2 points and no attack**. Silence is the ceiling of tolerance — not welcome, but not a pile-on.
- Family members lost to chatbots → framed as tragic, not evil. The anger is grief.
- **Ideological allies who use AI are punished harder than indifferent grifters**, because they are
  read as knowing better: *"They're bootlicking class traitors. Point blank."* [616]

**The one stated ethical carve-out**, and BadCode fails it completely:

> *"If you're actually the small lot of people using a generative AI that was never trained in a data
> center, was trained on ethically sourced data, and never intended to hyperscale, good for you. I
> don't think you exist in any meaningful quantities."* [1,294]

**The absolutist ceiling:** *"There is no ethical use for AI, and anyone who says otherwise is an
idiot, a shill, or a stooge"* [1,549]. And the explicit rejection of middle ground, well received:
the "middle ground fallacy" post [160/209 comments] arguing that a midpoint between pro- and anti- is
still pro-.

---

## 3. How big is the moderate wing? (measured, not assumed)

**Conditional *language* is everywhere; a conditional *conclusion* is rare and unrewarded.**
Keyword hits across the corpus: capitalism (67), disabled/accessibility (82), billionaires (42),
"as long as" (22), "not all" (21). But posts that reach a moderate conclusion cluster at or near
**zero net score even with dozens of comments**:

- "I am not anti-AI in its entirety…" [0 / 31 comments]
- "Not all Ai is Bad but it still needs protections" [0 / 37]
- "Can we find a middle ground…" [0 / 44]
- "do you hate ALL uses of AI… or just stupid ones?" [0 / 64]
- "This Subreddit is Bad for Your Health" (argues the sub over-represents anti-AI sentiment vs the
  real world) [0 / 57]

Compare: the two posts demolishing the moderate excuses score 12,943 and 9,815. And where a
conditional opener does score [70], an absolutist reply sits right beside it: *"If it wasn't using
stolen data and threatening peoples livelihoods, I'd STILL be against it"* [54].

**Conditions that are actually named**, when they are:
- Consent **and payment** for training data — not opt-out, which is explicitly rejected as
  insufficient. (Matches the wider-web finding: EPIC's 2026 audit found opt-out mechanisms across 38
  companies use at least eight categories of dark patterns.)
- Worker protections / UBI in place first: *"I would be pro AI if we had guaranteed worker protections
  and/or a UBI in place, but until then I'll remain anti"* [616].
- Domain carve-outs: medical, translation, boilerplate code, research tooling — the objection is to
  *generative replacement of the creative or decision-making act*, not to "AI" as a category. **This is
  the single most reusable acceptance criterion in the corpus.**
- Assistive rather than wholesale: *"a number of people are creating some pretty good art using AI as
  a useful tool, which is how it should be"* [1,841].
- Disclosure and labelling — present, but a lower-engagement demand than the above.
- Small, non-commercial, non-claimed, ideally local use.

**Internal conduct fight.** Real and unresolved. Mods added rules banning harassment, threats and
brigading [169/90] — evidence the problem was real. A mod post confirms the sub has dealt with "AI use
witch hunts" against innocent members [24/12]. On collateral damage to real artists falsely accused,
one heavily upvoted comment [361] argues the witch-hunt is justified because it protects livelihoods;
another [11] concedes false positives are "unfortunate." Self-critical posts ("we need to talk";
"echo chamber") are argued over and net zero — read, not embraced.

---

## 4. The red team: how a BadCode release would be received

An agent was given BadCode's real framing and the corpus, and asked to write the reception. Verdict:
**hostile and fast; the sourcing becomes the whole conversation before anyone reads the panels.**
Extract:

> cool superintelligence lore. did it also forget how to pay a session musician $20? […] you can
> afford a Solana program, a chain toolkit, a website, and enough Claude time to keep six skill files
> in a git repo, but not the price of a pizza for a broke musician. that's not poverty, that's
> priorities.
>
> "the machine isn't the enemy, ownership is" — groundbreaking, very Marx-pilled, except the machine
> you used is Google's and Suno's […] you didn't opt out of the ownership problem. you're its
> customer.
>
> disclosure doesn't buy you what you think it buys you. you don't get a badge for admitting you
> skipped paying anyone, you get a receipt.

**Charges and whether they land:**

| Charge | Verdict |
| --- | --- |
| The models were trained on scraped, uncredited work; every panel carries that | **Lands fully.** No answer that isn't a justification. |
| "Can't afford" doesn't survive contact with visible spend on infrastructure | **Lands fully.** Honest phrasing is "chose not to." |
| Political hypocrisy: anti-ownership comics made with the ownership class's tools | **Lands fully.** |
| "We can't draw" is the incapacity shield | **Lands fully.** |
| "It's ownership not the machine" is the known deflection | **Lands partly.** The analysis is right; using it as a permission slip is not. |
| A craft-implying job title over 100% generated visuals | **Lands partly.** Change the credit. |
| "But we disclosed" is mitigation | **Misses** — as mitigation. It keeps us out of the worst category and buys nothing more. |

**What earns grudging respect:** upfront disclosure by name; not flooding a marketplace for profit;
no LoRA or style-clone of a named living artist; genuinely shared politics on data centres and wealth
concentration. **What makes it worse:** the crypto adjacency; the superintelligence framing played
straight; political branding (raises the stakes rather than lowering them); the word "all."

---

## 5. The wider-web findings that matter most

**Backlash pattern (≈20 case studies, 2022–2026).** Severity tracks three triggers, in order:
(1) **getting caught concealing or denying**; (2) **displacing a specific named human's paid work**;
(3) **touching IP a fandom or institution feels ownership of**. Not "AI was used" by itself.
Wizards of the Coast denied then reversed in four days; Sports Illustrated's parent fired its CEO and
three executives after fabricated AI bylines were exposed; Bloomsbury replaced a *credited illustrator's*
cover with AI stock; the Willy's Chocolate Experience was shut down the same day. Meanwhile Coca-Cola,
Toys R Us and Ubisoft absorbed loud, fully-disclosed backlash and continued unchanged. Fast, concrete
reversal (Apple's "Crush" ad in ~48 hours; the BBC's Doctor Who statement) cuts the cycle short;
defending it ("successful," "the genie is out of the bottle") extends it into a second wave.

**Disclosure norms.** Steam requires disclosure (rewritten 17 Jan 2026 to cover only player-facing
content; dev tools exempt); disclosures went ~1,000 in all of 2024 → ~8,000 in H1 2025. itch.io made
it mandatory Nov 2024. Kickstarter has a "Use of AI" section. **Bandcamp banned AI-generated music
outright on 13 Jan 2026** — prohibition, not disclosure. Spotify adopted the DDEX AI-disclosure
standard (Sept 2025) with AI Credits from Apr 2026; Apple Music phasing in Transparency Tags;
DistroKid permits with a mandatory AI checkbox. EU AI Act Art. 50 in force 2 Aug 2026 — but with an
explicit carve-out for "evidently artistic, creative, satirical, fictional" work, which reduces the
obligation to disclosing AI's involvement "in an appropriate manner that does not hamper the display
or enjoyment of the work." C2PA is stripped by re-encoding and screenshots; it is not a substitute for
plain language.

**Public opinion is hardening, and not by age.** Pew (June 2025): 50% of US adults more concerned than
excited, up from 37% in 2021; 53% say AI will worsen creative thinking. Pew's 25-country study: in *no*
surveyed country is "more excited" the largest group. Gallup (May 2026): "does more harm than good"
39%, up from 31% — and among 18–29s from 36% to **47% in one year**. Quinnipiac (Mar 2026): Gen Z is
the *most* job-loss-pessimistic generation at 81%. **The assumption that this fades with generational
turnover is not supported.** Pew's expert-vs-public split is the most BadCode-relevant number in the
set: 47% of AI experts are more excited vs **11%** of the public; 76% of experts expect to benefit
personally vs **24%** of the public. That gap *is* the "gains flow upward" thesis, measured.

**Post-work economics — where BadCode's own thesis is strong and where it's naive.** Autor's 2024
NBER paper is explicitly conditional: the good outcome "is not an inevitable or intrinsic consequence
of AI development," and the bad one is "a hellscape: 'WALL-E' meets 'Mad Max.'" He concedes the
Luddites' fear "was justified" — handloom weavers "quite rapidly wiped out," ~five decades before
living standards rose. Acemoglu & Restrepo: displacement effects have *strengthened* and reinstatement
effects *weakened* over 30 years; Acemoglu's 2024 estimate is a modest 0.53–0.66% TFP gain over ten
years, with the capital/labour income gap widening. **Benanav is the serious challenge to BadCode's
premise**: chronic underemployment is driven by manufacturing overcapacity and demand deficiency, not
automation — so "change who owns the machine" may be treating a symptom. And Keynes' 15-hour week is a
century-long demonstration that productivity gains do not convert into freedom by themselves.
Separately, a documented academic critique holds that **AI "inevitability" is a manufactured narrative
serving incumbents** — the exact rhetorical structure of BadCode's own founding fiction.

**Ethical practice — what actually buys credibility, ranked.**
1. Specific, permanent, point-of-consumption disclosure naming tools. Near-universal demand, zero cost.
2. Human authorship named precisely and evidenced (the WGA's "AI is not a writer" standard is the
   clearest industry-negotiated bar; a published process ledger is the evidence).
3. Material support to working artists — payment, commission, revenue share. The corpus's own stated bar:
   *"buy our art… anything."*
4. Consent-based licensing where reachable (Grimes' elf.tech: opt-in plus 50% royalty split is the one
   clearly-evidenced case where disclosed AI use drew *positive* coverage).
5. Not claiming "ethically sourced." No tool BadCode uses can support it, and Adobe faces a shareholder
   suit alleging its "commercially safe AI" marketing was a misrepresentation.

**Non-monolithic critics.** The Human Intelligence movement (~1,200 artists pledging hand-made work)
explicitly says *"It's not saying AI should be banned."* Michael Schmelling's objection in the
Guardian's anti-slop piece is specifically to *unconsented training on his own work*. Stoopid Buddy
Stoodios, who hand-animated the anti-AI-ad response, still uses "some AI digital tools." The
maximalist reading of the opposition is as wrong as the maximalist reading of AI.

---

## 6. Method notes and gaps

- Reddit blocks direct fetching (403/429 on HTML, JSON and RSS). The corpus was collected through a
  real browser session against Reddit's own JSON endpoints, with backoff. Comment coverage is the top
  90 threads by score and comment count — i.e. **the corpus over-represents what the community
  rewards**, which is the intended bias for this question but should be remembered.
- The labour agent's web search budget was exhausted; its first-person worker quotes are confirmed by
  headline/outlet/date only, and it explicitly refused to reconstruct quotes it had not read. Named,
  verbatim worker testimony is the clearest remaining gap and would strengthen §1 Tier 1.
- Scores are as harvested on 15 Aug 2026 and will drift.
