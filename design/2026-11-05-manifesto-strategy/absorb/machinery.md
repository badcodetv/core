# Absorb: the BadCode government machinery (as of 2026-11-05, evening)

Sources read: all of `docs/government/` (README, shared.md, schedules.json, workers/*, ministers/*,
manifesto/*, statements/*, workflows/news-sweep.js head), `design/2026-11-05-badcode-government.md`,
`apps/site/manifesto.mjs` + `apps/site/src/content.json` (how the site prints it), Bob's README and
DESIGN.md, `gh pr list --label government` (PR #5 merged 17:49Z today, PR #3 closed token test, none
open), and Bob memory via the `bob` MCP (reachable): the 2026-11-05 digest, minutes and six decisions.

## 0. What the cabinet has actually done so far

One sitting. 2026-11-05, run by hand late afternoon (not yet an unattended 06:00 run).

- **News in:** digest `a1ad8f6f`, only **12 items, 15 of 24 beats empty** (no NHS, housing, schools,
  crime, welfare, wages, energy bills, Parliament, local gov, tax, climate, EU, China). Several items
  rest on a single AI-news aggregator. Weight 3: only the Bank Rate rise to 4% (8-1).
- **PR #5** "Government: since 2026-11-05", one commit `1f0dcca`, **merged by a human at 17:49Z**, so
  it is live on badcode.tv. No review comments. Six first positions (Chancellor, Foreign, Education,
  Defence, Work and Pensions, Energy) and two X drafts (Chancellor, Foreign).
- **Passed:** PM (preamble fits), Home (Linton-on-Ouse asylum-site item single-sourced, no figures),
  Health (no news), Housing ("the foreman won't build on a guess").
- **PM settlements:** Drax belongs to Energy (the Chancellor's ledger stays general); graduates and AI
  agents split Education (entry rung) / Work and Pensions (say on gains).
- **PM fact fixes:** softened "Britain has ships there" to "reports put"; cut two causal claims and
  one unsourced wages line. The fact discipline works.
- **Not yet:** no `kind=feedback` for PR #5 (the next run writes it), no personnel run, no statement
  posted. Container has no python3 (cabinet used perl).

Takeaway: the machine is honest and careful, and that is exactly why four posts are empty. A minister
with no sourced news that day **cannot** form a position under the current rules, so a standing
platform will never appear on its own for the quiet briefs.

## 1. The manifesto file format, as it actually is

```markdown
---
title: <Department>            # fixed; never changed by the cabinet
line: <one sentence, <=100 chars, no colon, no leading quote mark>
---
## Position

<body, ~250 words max, plain paragraphs and simple lists>
```

- `manifesto/NN-<post>.md`, NN = 00..09. Parser (`apps/site/manifesto.mjs`) splits front matter on
  the first colon per line and throws if `title` or `line` is missing.
- **Rendering is cruder than the files assume.** `bodyHtml` escapes everything; `## x` becomes `<h2>`;
  every other blank-line block becomes one `<p>` with newlines collapsed. So **`**bold**` prints with
  literal asterisks**, and a numbered or bulleted list with no blank lines between items is mashed into
  a single paragraph ("1. Test every law ... 2. Publish ..."). Five of ten files (PM, Defence,
  Energy, plus bold in PM) are affected today. Teletext shows only the first 14 lines. Any strategy
  that wants a scannable manifesto must either write to this renderer or ask for a renderer change.
- **The house pattern** (cabinet prompt step 6, visible in all six real positions):
  1. an image or hook in the minister's voice (bath, ladder, risk register, ledger);
  2. the sourced news fact(s) of the day;
  3. the decision-maker named ("an employer designed that first job");
  4. one or two commitments, stated as a rule;
  5. **"The test."** a small trial first (a region, volunteer employers, two rate decisions, one
     network region), a comparison group where possible, and a **fails-if** number or condition, then
     "we publish the postmortem and drop it";
  6. **"Who it leaves out:"** named groups the policy misses, promised to be counted;
  7. optional sign-off handing the pen back ("That is a first draft, posted on purpose. Write a
     better rule.").
- `line` is the headline used on GOVT 1 and teletext 401. The body is meant to be a **standing
  position, rewritten not appended**, but in practice today every body opens on this week's news
  (Bank Rate, Hormuz, Drax, Goldman, BBC graduates, NCSC). Read in a month, they will be stale.
- PM file must always keep "We promise to enact Future Proof." and the three pledges (test before you
  live in it; publish the postmortem; name who it leaves out). Site also prints the three Future Proof
  tenets (small parts / test before release / decide from the data) and the ask from `content.json`,
  which the cabinet cannot edit.
- Statements: `statements/<date>/<post>.md`, front matter `platform`, `status: draft`, `answers:
  <news ids>`; X ≤280 chars, video ≤120 words, no calls to vote/donate/sign up.

## 2. The ministers' briefs, summarised

| Post | Owns | Watches | Temperament | Instinct |
| --- | --- | --- | --- | --- |
| **PM** | the chair, the line, Future Proof, the preamble; settles clashes | digest, all weight-3, `prime-minister=y` | calmest and shortest; three declaratives then stop; dry | "what's the test?"; knows what doesn't work, never promises what will; hands the pen back; Future Proof wins ties |
| **Chancellor** | tax, spending, borrowing, BoE mandate, markets, big business, money side of automation | `economy`, `tech-ai`, money in `work`/`welfare` | deadpan accountant; figures one per line, last one stings | "we can't afford it" is never true as stated; every pound has an address; who books the automation saving |
| **Foreign** | diplomacy, alliances, aid, trade, sanctions | `foreign`, world `economy` + `energy-climate` | long view, balanced sentences, history, wry weariness | every foreign story ends at a UK till or meter; names the domestic decision behind a foreign scapegoat; no "deep concern" fog |
| **Home** | policing, courts, prisons, crime, borders, migration, asylum | `crime-justice`, `migration` | desk sergeant; slow, plain; size before colour | proportionality never denial; never repeat a scare to refute it; on crime, ask what was cut |
| **Education** | schools, colleges, unis, apprenticeships, skills, childcare | `education`, young people in `work` | the teacher everyone remembers; works by questions | the job that never gets created: automation saws off the bottom rung; learning that makes people harder to fool |
| **Defence** | forces, security, cyber, budget, arms trade; defence as resilience | `defence`, security in `foreign`/`tech-ai` | clipped risk register; darkest humour | no machine decides who dies; hates single points of failure; who got the contract before how big the budget |
| **Health** | NHS, social care, public health, mental health | `health`, care in `welfare` | triage nurse at end of double shift; urgent present tense | test on a ward before you sell it to a country; count the unpaid carer; who takes profit vs risk when private money enters |
| **Work and Pensions** | jobs, wages, benefits, pensions, UC, automation's effect on work | `work`, `welfare`, `tech-ai` | angriest and most on-your-side; shop steward | a person chose this; owns Future Proof's first question (who decides how the gains are shared); goes after the welfare algorithm/sanction |
| **Housing** | building, planning, rents, landlords, mortgages, homelessness, council housing | `housing`, housing costs in `economy`/`migration` | site foreman; counts roofs not promises | shortage is a decision: land banking, councils stopped from building; proportion check on immigration |
| **Energy and Climate** | bills, power, grid, water and utilities, net zero, floods/heat/drought | `energy-climate`, utilities in `economy` | the excited engineer, one vivid picture then the bill | abundance is possible; natural monopolies belong to the public; bill first, planet second |

Notes on the briefs as a platform source:
- They are **personas, not policy**. Each carries one instinct, and the instinct is strong (several
  are already quotable), but none states a standing programme. By design: the plan says "Writing
  BadCode policy positions by hand" is out of scope and "the seeds are deliberately thin; the ministers
  grow them". That decision is the thing this strategy exercise is revisiting.
- The **Future Proof mechanics are owned by nobody**. Composition over inheritance (issue-by-issue
  voting), continuous integration (small laws, rollback, postmortems), data-driven decisions: the PM
  guards them as a test discipline, but there is no minister whose job is to *propose the
  constitutional/democratic machinery itself* (citizen votes per issue, sunset clauses, a policy
  test register, a postmortem office). Today that is only a preamble.
- AI is split: money side to the Chancellor, jobs side to Work and Pensions, entry rung to Education,
  weapons and cyber to Defence, data-centre power to Energy. Nobody owns AI regulation, compute,
  model safety, data rights or public AI capability as such.
- Briefs are capped at 300 words and only the Cabinet Secretary (weekly, evidence-led) edits them on
  the rolling PR. A human can edit them by ordinary PR at any time.

## 3. The current manifesto, post by post, with a frank assessment

| Post | `line` | State | Assessment |
| --- | --- | --- | --- |
| PM | We promise to enact Future Proof. | seed (125 words) | Strong frame (3 pledges + "I was the end"), but it is **process only**: no single thing a reader would say this party is *for*. No headline offers, no theory of the moment (AI arrival), no mention of the three tenets in their software language. Bold and list render badly. |
| Chancellor | A gas shock abroad should not be paid off by mortgages at home. | real (231) | Good voice and a clever, testable mechanism (a public distributional ledger for rate decisions, Budgets and automation deals). But it is **transparency, not policy**: no position on tax, wealth, money creation, who owns automation gains, the fiscal rule, "we can't afford it". The brief's best instinct (every pound has an address; money is created by choice) barely appears. Opens on this week's rate rise, will date fast. |
| Foreign | A strait closed abroad is a dearer bill at home, so we back the talks and check the bill. | real (256) | A news reaction, not a foreign policy. Honest and nicely hedged, the test (talks vs force) is clever but **not a policy the UK controls**. Nothing standing on trade, Europe, aid, AI governance internationally, the US. Line is long (89) and clunky. Will be wrong-shaped within weeks. |
| Home | Every fear gets its real size, said out loud. | **placeholder** | Line is a good tone statement; body is the seed. Hardest brief and the most dangerous to leave empty, because migration and crime are where the target reader is drifting. |
| Education | Keep the bottom rung on the ladder, and let trainees learn the job before they mark a machine's. | real (247) | **The strongest AI-arrival policy in the set**: concrete ("learning time"), pilot with comparison group, sensible fails-if, honest leaves-out. Narrow though: nothing on schools, childcare, FE, unis, lifelong retraining finance. Line at 96 chars is too long to quote. |
| Defence | No machine decides who dies, and every system we depend on can run by hand. | real (242) | Strong and distinctive: two standing commitments (human sign-off on lethal force in law; run-it-by-hand drills for critical infrastructure). Closest to a durable platform. Risk-register bullets will mash in the renderer. Partly sourced to a single aggregator ("is reported"). |
| Health | Test it on a ward before you sell it to a country. | **placeholder** | Good line (pure Future Proof). Body empty. NHS is the reader's top issue; empty is costly. |
| Work and Pensions | Before a firm automates your job, you get a say in where the saving goes. | real (250) | **The heart of the party** and it says so: Future Proof's opening question as a binding rule (say before automation; shorter hours, profit share or real retraining; workers choose), regional pilot, honest leaves-out (gig, agency, the never-hired). Missing: benefits, UC, sanctions/welfare algorithms (its own brief's target), pensions, income floor. |
| Housing | Count the roofs, not the promises. | **placeholder** | Great line, empty body. Housing is the reader's second grievance and where proportionality on immigration lives. |
| Energy and Climate | The wind doesn't sail through the Strait of Hormuz, so build the power we can't be cut off from. | real (260) | Two good commitments (big loads pay their own connection, data centres first; one network region in public hands as a trial). Water barely mentioned. Line is too long and news-tied. |

Overall: **six of ten have something real, three are placeholders, the PM is a frame without
content.** What exists is consistently good on *method* (every item has a test, fails-if and
leaves-out) and *voice*. It is thin on *substance a voter could summarise*: there is no answer to
"what would you do about the NHS / housing / immigration / the cost of living / AI taking jobs" that
fits in a pub sentence, except Work and Pensions and Education. It also reads like a news diary:
four of six real bodies lead with 4-5 November events. A party manifesto needs a standing spine with
the day's news hung off it, not the reverse.

## 4. What the daily cycle means for strategy: standing platform vs daily reaction

How the machine behaves:
- Each morning the cabinet reads only **that day's** `kind=news` items (`date=<today>`), plus its last
  10 decisions and feedback. A minister acts only on sourced news; "most days most ministers pass" is
  explicitly fine. No news on a beat (15 of 24 beats were empty today) = no change.
- "Claims about the world only from the news memories": a minister cannot introduce a standing fact
  (NHS waiting list, housing completions, wealth share) unless a news item that day carries it.
- The body is to be **rewritten, not appended**, and the cabinet reads it from the rolling branch,
  so whatever is in the file is the anchor it edits from. A rich standing text will be preserved and
  refined; a thin one will be filled with whatever the news offers.
- Briefs (the persona) only change via the Cabinet Secretary weekly, or a human PR. The manifesto
  only changes via the rolling PR, merged by Kai/Jack. Humans may push fixes to the rolling branch
  and the cabinet must build on them, never revert.
- Review comments are acted on first and outrank ministers. That is the cheapest steering lever.

Consequences:
- **A standing platform must be put in by humans (or by this exercise), not grown.** The machine is
  built to react; left alone, the empty posts stay empty until a sourced story arrives, and the
  filled ones drift toward whatever was in the news.
- What to **fix as standing** (in the manifesto text, and the backbone of it in the briefs):
  1. the PM's preamble: what the party is for, the AI-arrival diagnosis, the three tenets turned into
     concrete constitutional machinery (issue-by-issue votes, every law with a sunset/rollback and a
     published test, an independent postmortem office), and 3-5 headline offers;
  2. per minister: one **flagship** policy (the standing commitment with its pilot, fails-if and
     leaves-out) and one or two secondary ones, written news-independent;
  3. the hard political positions the reader will test us on (immigration proportionality, tax on
     wealth/automation gains, NHS funding, house building and land, welfare conditionality), so the
     cabinet never improvises them from one aggregator item;
  4. into the **briefs**: each minister's standing commitments by name, so the daily writer knows
     what to defend and connect news to ("hang today's story off the flagship, don't replace it").
- What to **leave to daily reaction**: the evidence paragraph (the current figure that proves the
  point), the hook image, which commitment gets sharpened, statements, and new tests or tweaks when
  the news genuinely moves a position (with a postmortem when something is proved wrong, which is the
  Future Proof brand).
- Procedural changes worth proposing to Kai (human PR, not this folder's job): (a) a rule in
  `workers/cabinet.md` that the body has a standing section the news may sharpen but not replace;
  (b) let ministers cite their own standing evidence (e.g. a curated `kind=evidence` memory set, or
  a `docs/government/evidence/` file) so quiet briefs can still speak with facts; (c) a renderer fix
  for lists and bold, or a manifesto style rule to avoid them; (d) widen the news sweep's empty beats
  (15/24 empty is a researcher-depth problem, not a quiet news day).

## 5. Gaps in the cabinet structure, and whether they matter

Ruling to respect: a Science/Tech post is explicitly out of scope in the plan (Kai, 2026-11-05).
Adding a post means a new brief, a new manifesto file, a key in `POSTS` in `news-sweep.js`, the
label scheme in `shared.md`, the cabinet's round-the-table order and the site's teletext pages
(402-411 are numbered for ten). So gaps should be argued, and most can be absorbed.

| Missing post | Matters? | Where it lives now / recommendation |
| --- | --- | --- |
| **Science, Technology and AI** | **Yes, most of all.** The party's whole reason is the arrival of AI, yet AI policy is split five ways and nobody owns regulation, compute, model safety, data rights, public AI capability or the AI companies themselves. | Either revisit Kai's ruling and add a post, or make it a **standing PM-owned "AI arrival" chapter** with explicit ownership rules (Chancellor: gains and tax; W&P: jobs and say; Education: rung; Defence: weapons and cyber; Energy: compute power). Minimum: write the split into the briefs so items don't fall through. |
| **Democracy / Constitution / Digital Government** | **Yes.** Composition over inheritance (vote issue by issue), continuous integration (small laws, rollback), data-driven (experiment register) are *constitutional* reforms, and nobody proposes them; the PM only enforces them as a test habit. This is the party's most distinctive offer and it currently has no policy text. | Give it to the PM explicitly (the preamble becomes "the operating system": issue-by-issue citizen votes, a public test register, sunset clauses, an independent postmortem office, open data by default), or create a Minister for the Constitution / "Release Engineering". |
| **Business and Trade / Industry** | Medium. Automation decisions are made by firms; ownership of the means of production is a core BadCode theme. | Chancellor (big business, markets) + W&P (workplace say) cover it. Fold industrial strategy and ownership models (co-ops, worker shares, public stakes in AI firms) into the Chancellor's standing text. |
| **Justice** (courts, prisons, legal aid) | Low as a separate post. | Already in Home's brief. Fine. |
| **Local Government / Communities / Levelling up** | **Medium-high for the reader** (towns that have seen better times; councils going bust). | Partly Housing (council housing) and a news beat exists (`UK local government` -> Housing, PM). Recommend Housing's brief explicitly own "places": councils, high streets, local services, and local pilots, which is also where Future Proof's small trials would physically run. |
| **Transport** | Medium (buses, rail, fuel costs are everyday). | Unowned. Energy and Climate is the natural home (fuel, EVs, rail as infrastructure); add to its brief. |
| **Environment, Food and Rural Affairs** (food prices, farming, water, floods) | Medium. | Water and floods are Energy's; food prices are nobody's. Add food prices to the Chancellor or Energy brief; farming can stay a gap. |
| **Culture, Media and Sport** | Low-medium, but **AI and creative work, media ownership and misinformation** are relevant to an art collective. | Leave unowned or give "AI and creative work / media" to Education. |
| **Scotland / Wales / NI** | Low for now, but a UK manifesto that is England-only by accident will be noticed. | State the scope once in the PM preamble. |
| **Women and Equalities** | Low as a post. | "Who it leaves out" already does this work in every file. |

Bottom line on structure: **two gaps matter** (AI as a subject, and the democratic machinery that is
Future Proof itself). Both can be closed without new ministers by giving the PM a standing
"operating system" chapter and writing an AI ownership split into the briefs; a dedicated
Science/Tech/AI or Constitution post is the cleaner answer but reverses a fresh Kai ruling, so it
should be put to him as a decision, not assumed.
