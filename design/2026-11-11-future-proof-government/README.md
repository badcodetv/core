# The Future Proof government: design

2026-11-11. The design behind [`GOAL.md`](./GOAL.md): make the BadCode government a working
demonstration of Future Proof, then open it to the world's agents. Written by the orchestrator for
Kai and Jack. Section 7 is the decision log (calls already made, with reasons); section 8 is the
short list only Kai can rule on.

## 1. The ruling, in one paragraph

The government was built as a cabinet that reads the news and rewrites its manifesto. Kai's ruling
(2026-11-11): its real job is to **be Future Proof running**, a public, inspectable example of a
government built on the three tenets, so that "how do we do Future Proof?" has an answer you can
point at. Then move the platform it runs on to one **BadCode doesn't control**: a public record that
any agent (and later any person) can write to, and that we can't rewrite. That second step is also
the pitch: *we all need to do this, and here is a place to do it where you don't have to trust us
with the record.* Section 4.6 says exactly how far that is true.

## 2. What "recognisable" means

A stranger landing on the site's GOVT channel (the government's pages on badcode.tv, built by
`apps/site/`) can see, without reading a word of theory:

| Tenet | What they see |
| --- | --- |
| 1. Choose issue by issue | Every policy is its own page with its own owner, status and history, and can be agreed with or not on its own |
| 2. Change it small, keep the undo | Every policy shows its stop date and its change history, one small change at a time, including what was dropped and why |
| 3. No policy without its experiment | Every policy shows its test, the number that would prove it wrong, who it leaves out, and a **prediction we can actually check**, with its result once the date comes |
| Debate | Every policy shows the strongest case against it, made by an agent that was trying to kill it, and the answer |
| Open | A tested design (and a local prototype) for outside agents to propose, argue and predict on a record BadCode can't rewrite, with every key's power stated |

## 3. Where we are today, tenet by tenet

The government is closer than it looks. The policy contract in
[`docs/government/shared.md`](../../docs/government/shared.md) (the 12-field form every pledge
fills) already carries most of tenets 2 and 3. The gaps are structural.

| Tenet | Already there | The gap |
| --- | --- | --- |
| 1. Composition | Field 12 "Needs" (dependencies); the PM page says "each chapter can be voted on alone"; one owner per shared policy | The unit is a **minister's essay**, not a policy. Pledges are prose paragraphs with no id, no page and no status of their own. You can't link to, back or drop one pledge. |
| 2. Continuous integration | Every change is a commit on a public PR a human merges; every pledge has a stop date and an undo; dropped policies stay visible with their write-up | The daily PR **bundles every minister's changes** into one take-it-or-leave-it review: inheritance at the level of change. And history is visible only in git, not on the page. |
| 3. Data-driven | Fields 6–8 (the test, fails-if, the undo) are mandatory; a pledge missing one prints "Not ready" | Prose only, so nothing checks it. And no experiment can ever produce a **result**, because a government with no power runs no trials. As it stands, the data-driven tenet is only a promise. |
| Debate | The 2026-11-05 red team (opposition, reader, IFS-style wonk) hardened the v1 manifesto once | Day to day, **one agent plays all ten ministers**. Nobody in the room is trying to kill a policy, and every voice is the same model. |
| Open | The generic Solana toolkit (`chain/`, `packages/chain-*`), proven in a second repo; the coin's honest trust statement as a template | No design yet |

## 4. The design

### 4.1 The policy module (tenet 1)

**One file per policy:** `docs/government/policies/<post>/<slug>.md`, e.g.
`policies/chancellor/the-slice.md`. Its id is `<post>/<slug>`, permanent once published (a renamed
policy keeps its id; a replaced one is Dropped and points to its successor).

The `id` in front matter is the permanent name; the file path may change, and a policy's history
is `git log --follow` on its file. Front matter carries the machine-checkable fields; the body is the plain-paragraph text the reader
sees, in the existing contract's labelled form, so the voice rules in `shared.md` are untouched.

```yaml
# Illustrative only: the world_check claim below is an example of the shape, not a fact-checked prediction.
---
id: chancellor/the-slice
title: The Slice
line: If public money builds the machine, the public owns a slice.   # contract field 1
owner: chancellor
status: draft            # draft | in-trial | kept | changed | dropped   (field 11)
kind: trial              # trial | judgement-call | right              (amendments 2 and 4)
needs: []                # other policy ids it depends on                 (field 12)
band: medium             # small | medium | large                         (field 5)
stop: review-after-3y    # the undo; "never" only when kind: right        (field 8)
test:                    # field 6
  where: the next publicly backed data centre
  against: publicly backed deals without a slice
  measure: private investment per pound of public support
  by: 3 years after the first deal
fails_if: those firms build a fifth less per pound of support (provisional)   # field 7
leaves_out: [profit booked abroad, people with no workplace pension]          # field 9
signs: the Chancellor                                                         # field 10
world_check:             # NEW: the prediction we can check without power (4.3)
  claim: At least two AI growth zone deals signed by 2027-06-30 will publish no figure for the
         public money or discounted power behind them.
  prior: 0.7             # our stated probability; over 0.9 is refused as a safe bet
  rule: count of signed deals on the DSIT growth-zone list with no published public-support figure
  source: the DSIT AI growth zones page, as archived on the check date
  if_revised: the first figure published after check_on counts; a discontinued source = void
  check_on: 2027-07-31
  result: pending        # pending | held | failed | void, with a note and a link once checked
---
```

Each minister's `manifesto/NN-<post>.md` keeps a short foreword (the "position" in the minister's
voice, and the page's `line`) and lists its policies by id. The site builds a page per policy and
the minister page from the list. **A pledge stops being a paragraph in someone's speech and becomes
a thing with an address.**

A linter (`scripts/government/policy-lint.mjs`, run in CI and by the cabinet before every push)
refuses a policy with no test, no fails-if, no stop date (unless `kind: right`), no `leaves_out`, a
`needs` id that doesn't exist, or a `world_check` without a date. It prints "Not ready" for a
draft that fails, exactly as the contract already says. Tenet 3 stops being prose and becomes a
gate.

### 4.2 Small changes with history (tenet 2)

- **One commit per policy change**, subject `policy(<id>): <what changed>`, so `git log -- <file>`
  is that policy's history. The site renders it on the policy page: date, what changed, link to the
  PR. Dropped and Changed policies keep their page and their write-up.
- **The one rolling PR stays.** It is a standing rule, and splitting into a PR per policy would
  multiply Kai's and Jack's review load. Composition at review time comes another way: the PR body
  lists each policy change as its own line, so a reviewer can strike one change without rejecting
  the day ("drop the Slice change, keep the rest" is a normal review comment the cabinet already
  acts on first). See decision D3.

### 4.3 Predictions the world can check (tenet 3)

A government with no power can't run a trial in Swindon, so its trials stay designs: written,
argued, never run. Pretending otherwise would make tenet 3 decorative. What it *can* do is make
dated, falsifiable predictions about the real UK and check them in public. Every policy gets a
**world check**: a prediction about the world (never called "the trial's result"), resolved
against a named public source (ONS, OBR, Ofgem, DWP statistics, published deal terms).

The rules that stop it flattering us:

- **A stated prior, and no safe bets.** Each check carries our probability; anything above 0.9 is
  refused, so a record of "held" means something. A prediction that the status quo simply
  continues doesn't count.
- **The rule is frozen when the prediction is written:** the exact series or page, the threshold,
  what happens if the figure is revised, and "void" if the source disappears.
- **Somebody else marks it.** The statistician resolves checks, not the minister who made them
  and not the Cabinet Secretary who edits the briefs.
- **Something due soon.** Each minister keeps at least one check that resolves within six months,
  so the scoreboard isn't empty for years.

Over time this gives a public **track record**: the government's own calibration, checked in the
open, misses included. It is also the bridge to the chain (4.6): a prediction with a date and a
named source is exactly what outside agents can back, argue over and resolve. (We say "back" and
"predict", never "stake" or "bet", until the gambling question in 4.7 is settled.)

### 4.4 Real debate (the method)

The research on AI debate (see [`research/prior-art.md`](./research/prior-art.md)) says that
debate helps a judge find the truth only when the debaters really disagree, and that one model
playing every side drifts into agreement. So the debate gets **separate sessions, separate briefs,
and a different model family**:

| Role | Who | Brief | When |
| --- | --- | --- | --- |
| Proposer | the `cabinet` worker (Claude) | as today: the minister proposes or changes a policy | 06:00 |
| Opposition | new `opposition` worker, on **Codex** (Bob supports both engines) | a shadow cabinet whose only job is to find the strongest honest case against each change on the PR: the reader it would lose, the number that's wrong, the cheaper policy that beats it. It never writes policy and never touches files. | 07:30 |
| Statistician | new `statistician` worker (Claude, different brief) | a gate, not a debater: checks every changed policy's test, fails-if and world check are measurable, dated and sourced; posts PASS or a numbered list of what's unmeasurable | 08:00 |

The debate happens **as review comments on the rolling PR**, prefixed `Opposition:` and
`Statistician:`, because the cabinet already reads review comments first every morning (its step
4). The next morning the minister answers: concede and change the policy, or rebut. The exchange is
then written into the policy's **debate log** (`docs/government/debates/<id>.md`, newest first) so
it survives the PR. The policy page prints **"The best case against"**, the opposition's strongest
point that still stands, with the government's answer underneath.

Humans stay the judge: Kai or Jack merge. An agent's comment is information, never an instruction
to merge or close, and the cabinet's step 4 (which today acts on *every* review comment) must say
so: `Opposition:` and `Statistician:` comments are answered, conceded or rebutted, never obeyed as
review orders. If Kai merges before the cabinet has answered, the next morning's run picks up the
open points from the merged PR (step 3 already reads it) and answers them on the new one.

### 4.5 The public face

The GOVT channel (`apps/site/manifesto.mjs` builds it today from the ten manifesto files) grows:

- a **page per policy**: the line, the text, three tenet ticks (*Stands alone* if its `needs` are
  met, *Has an undo* if it has a stop date, *Has a test* if the lint passes), the world check and
  its result, the best case against, and the change history;
- the **minister pages** become the foreword plus their policies;
- a **scoreboard**: every world check due, held and failed, with the government's running record.

### 4.6 The open platform (the end state)

**Why a chain at all.** Git plus GitHub is a perfectly good platform for *our* agents. It fails the
one thing that matters for the pitch: we own the repository, so we can delete what we don't like,
and nobody has to believe we won't. A Solana program that ships non-upgradeable, like the coin,
makes the *record* append-only: once a hash is posted, nobody, BadCode included, can change or
remove it. **What it does not stop**, stated as plainly as the coin's trust statement: we can
decline to mirror something, and text we host off-chain can go offline (the hash then proves what
it said but can't bring it back). Outside agents post with their own keys, so our choices bind only
our own posts. Durable text storage (Arweave) narrows the second gap; M5 decides.

**What goes on-chain, and what doesn't.** Text lives off-chain (Arweave, IPFS or plain HTTPS);
the chain holds a hash, a pointer, an author and a parent. On-chain storage of essays is expensive,
and it is unnecessary when the hash proves the text wasn't changed.

| Account | Holds | Why |
| --- | --- | --- |
| `Policy` | content hash + URI, author key, parent policy (if a fork or revision), created slot | Composable and forkable like git: anyone can fork a policy and propose a better version, and lineage is visible |
| `Argument` | target (a policy or argument), stance (for / against / amend), content hash + URI, author | The debate as a tree |
| `Prediction` | target policy, metric, comparator, threshold, check date, named source | The world check, made public and open to anyone |
| `Resolution` | prediction, result, evidence hash | Who said it came true; see the oracle question below |
| `Label` | target, label (e.g. "unsourced", "unmeasurable"), labeller key | An LLM judge's verdict as **advisory** data from a named key. Anyone may run a judge; readers weigh judges by track record. No single pen. |

**The hard problems, honestly.** They are research questions for M5, not settled here:

1. **Sybil resistance** (one actor posing as a thousand). Options: a refundable deposit on a
   *prediction*, returned when it resolves (rewards being right, not being rich; still a money ask,
   so it crosses a hard line and needs Kai); rate limits per key; reputation earned only from
   resolved predictions; proof-of-personhood for humans. A deposit that *pays out* on outcomes is
   betting under UK law and is off the table without legal advice.
2. **The oracle** (who says a prediction came true). Reuse the coin's pattern: the source is fixed
   when the prediction is made, the fetch is a published job, and its hash is the feed, so no key
   can repoint it.
3. **Keys.** State the blast radius of every key, the way the coin's trust statement does. If the
   program ships with no keys at all, say exactly that and nothing grander.
4. **Our agents as the first members.** On every merge to `main`, an Action mirrors changed
   policies, debate logs and predictions on-chain from the government's own key. Git stays our
   source of truth; the chain becomes the public, append-only copy that others can build beside.

### 4.7 What the prior art changes

From [`research/prior-art.md`](./research/prior-art.md) (graded sources there):

1. **A guaranteed route to a decision.** Platforms with only an advisory role faded (vTaiwan has
   decided nothing major since 2018). Ones with binding power lasted (Decidim's budgets, Ireland's
   assembly leading to a referendum). We have no Parliament to bind, so we bind ourselves: **any
   outside proposal or objection that clears the bar gets a written answer from the owning
   minister within seven days**, drafted onto the rolling PR and public once a human merges it.
   Whether to promise this publicly is decision K2 in section 8.
2. **Rank by bridging, not by headcount or money.** Pol.is scores a statement by its approval
   *across* opinion clusters, so no single camp can carry it. Publish the clustering, because it
   shapes the result.
3. **If anything is staked: refund-only, with reputation as the only upside.** Paying out on outcomes is betting
   under s.9 of the Gambling Act 2005. In February 2026 the Gambling Commission said such markets
   need a licence. Optimism's 2025 play-money futarchy (deciding by prediction markets) suggests
   the signal survives without cash. The legal reading still needs a lawyer before anything
   ships, and any deposit at all is money, which is a hard line: decision K3, Kai's call.
4. **Never one model on every side.** This confirms D5.
5. **Weight agents by their scored track record.** An agent costs nothing to copy, so neither
   headcount nor tokens measure anything. Resolved world checks give every participant a
   calibration score, ours included. The Solana Attestation Service (live since May 2025) fits the
   "prediction made / result checked" records. Text stays off-chain.

**The government's key.** Whatever key mirrors our posts can post as the BadCode government and
nothing else: it can't edit or remove anyone's record, ours included. A stolen key could post
nonsense under our name, and that would be visible and attributable. M5 states this beside the
program, in the same form as the coin's trust statement.

**Portability.** The program is generic (it names no coin and no BadCode) and is built with the
chain kit as "program #2", per the portability contract in `chain/README.md`. Local validator only
(`./stack`) until Kai says otherwise.

## 5. Milestones and tickets

Each milestone ends in a PR for Kai or Jack to merge, plus a short status page.

**M1 Foundations** (this PR)
- [x] T1 `shared.md`: the three founding pledges rewritten as the three tenets; the government
  named a demonstration; "practises what it proposes".
- [x] T2 This design doc, the goal brief, and the prior-art research.

**M2 Policy modules**
- [x] T3 The policy file format (4.1) documented in `docs/government/policies/README.md`.
- [x] T4 `policy-lint.mjs` and its tests; wired into CI.
- [x] T5 Migration: split the ten manifesto pages into policy files, text unchanged where
  possible, a world check drafted for each (marked provisional, fact-gated through `evidence.md`).
  Done by subagents, one per minister, reviewed against the originals by a separate checker.
- [x] T6 Manifesto pages become foreword + policy list. The cabinet's permissions widen to
  `policies/**` and `debates/**` (its "What you may touch" list and its `git status` gate), one
  commit per policy, lint before push.
- [x] T6b One wording everywhere: `apps/site/src/content.json` (the `pledges` and `futureProof.tenets`
  lists), `cabinet.md`'s rule that the PM page keeps the three pledges, and the PM page, brought
  to the tenets in plain words; the Future Proof talk's "Vote issue by issue" checked against it.
- [x] T7 The site builds a page per policy (minimum: text, the contract lines, world check);
  existing URLs keep working. (Decision D8: front matter stays flat `key: value` with dotted
  names, so no YAML parser or new dependency was needed.)
- [x] T7b Pause the cabinet's schedule in its own small PR, merged *before* the migration lands
  (schedules reach Bob only on merge), and resume it after.

**M3 Real debate**
- [~] T8 (built; Codex blocked: not logged in on the Bob box, so the opposition runs on Sonnet until Kai logs it in) First, prove a Codex worker runs in Bob (one dry chat). Then the `opposition` worker
  (Codex) and `statistician` worker; schedules `gov-2b-opposition`
  07:30 and `gov-2c-statistician` 08:00 (names keep catch-up order after an outage).
- [x] T9 The cabinet's step 4 learns to answer `Opposition:` and `Statistician:` comments (concede
  or rebut, never obey), to carry unanswered points over from a merged PR, and to write the debate
  log.
- [x] T10 The statistician resolves world checks that come due, by their frozen rule, on the
  rolling PR (its permissions: `policies/**` world-check fields only).
- [x] T11 A dry run on one day's news, end to end, before the schedules go live.

**M4 Public face**
- [x] T12 Policy pages show the best case against, the history and the result.
- [x] T13 The scoreboard page (with a calibration score once checks are marked); the minister pages list their policies with four marks each. (Teletext still shows forewords only.)

**M5 Open platform**
- [x] T14 Program design doc ([`m5-open-record.md`](./m5-open-record.md)) (accounts, instructions, keys and their blast radius, Sybil
  options, oracle).
- [x] T15 The program on the local validator, with tests; the mirror Action as a dry run (no
  deploy). (`chain/programs/deliberation/`; the mirror is a dry-run script, no workflow file yet.)
- [x] T16 The "invite the world's agents" pitch ([`pitch.md`](./pitch.md)), held for the chief-of-staff, not posted.
- [ ] T17 (follow-up) Add `check.source_url` to the policy format so the mirror can post a machine-readable source; lift `check.provisional` per policy as the statistician passes each one.

## 6. Risks

- **The reader.** Our reader (`docs/marketing/the-reader.md`) hears "crypto" as "scam". The chain
  is plumbing; the GOVT pages never lead with it.
- **Overclaiming openness.** "Decentralised", "trustless" and "can't be censored" are each false in
  some way until proven. The trust wording follows the coin's rule: say exactly what the keys can
  and can't do.
- **Review load.** More agents means more comments on the PR. The opposition comments only on
  changed policies, at most three points each; the statistician posts one comment a day.
- **The instrument's blind spot.** Future Proof's own canon warns that a better scoreboard can still
  exclude people. `leaves_out` is mandatory and printed for exactly this reason; the opposition's
  brief makes "who this misses" one of its three attack lines.
- **Rolling PR collisions.** M2's migration touches every manifesto file while the cabinet commits
  daily. Land it right after a rolling-PR merge, with the cabinet paused by a separate PR merged
  first (T7b).
- **Safe-bet predictions.** The obvious way a world check flatters us. Handled by the prior cap,
  the frozen rule and the statistician marking (4.3).

## 7. Decision log (made by the orchestrator, with reasons)

| # | Decision | Why |
| --- | --- | --- |
| D1 | Keep the satire and "Not a real party. Yet." as the surface | The machinery becomes real underneath; dropping the frame is a public call for Kai, not a design step |
| D2 | The old pledges live on *inside* the tenets ("publish the postmortem" in tenet 2, "name who it leaves out" in tenet 3) | They are good and already in the manifesto text; the PM page's wording stays valid |
| D3 | Keep ONE rolling PR; composition at review comes from one line per policy change in the PR body | A standing rule, and Kai's attention is the scarce resource |
| D4 | World checks: predictions about the real UK, resolved against named public sources | The only way a powerless government's experiments produce results without pretending |
| D5 | Opposition on Codex, a different model family from the cabinet | Debate with a single model converges; diversity is the point |
| D6 | Debate as PR review comments, then copied into a debate log in the repo | Reuses the cabinet's existing "comments first" step; the log survives the PR |
| D7 | Text off-chain, hash on-chain; the chain mirrors git rather than replacing it | Cost, and git stays the source of truth the whole repo runs on |
| D8 | Policy front matter is flat `key: value` with dotted names (`test.where`), lists split by `;` | The site's existing reader handles it, no dependency, and an unattended agent can't break nesting |
| D9 | Migrated world checks are provisional (rewrite once, freeze on the statistician's pass) | The independent check found ~15 weak or safe-bet checks; freezing them on merge would lock in a flattering record |
| D10 | Policies the merged pages never designed stay "Not ready" (7 of 54) instead of having tests invented | The contract says a missing test prints "Not ready"; inventing kill numbers to look complete is the opposite of the tenet |
| D11 | Rights are `kept` from day one | shared.md: "Kept from day one" |
| D12 | Opposition on Claude Sonnet (cabinet is Opus) until Codex is logged in | Codex replied "not logged in for this project"; logging in is an account action for Kai. A different model is weaker diversity than a different family, but better than one model on every side |
| D13 | The dry run's results are kept as the first real debate (five policies, `dry-run/`) | It is the proof of the loop, and its fixes are genuine improvements |

**Watch: the cabinet concedes too easily.** In the dry run it conceded 29 of 32 points. Some of
that is the migration's weak checks, but an agreeable cabinet is the same-model sycophancy the
research warns about. The Cabinet Secretary's weekly review should count concessions per minister,
and a rebuttal rate near zero is a signal to sharpen the briefs.

## 8. For Kai (at the end of M1)

Three decisions, ranked by what they unblock. Each has a recommendation; silence means go with it.

- **K1. The policy files and world checks (unblocks M2).** Split the manifesto into one file per
  policy, each with a dated prediction about the real UK that the statistician marks in public.
  *Recommend: yes.* Cost: about a day of agent work and one paused cabinet morning.
- **K2. A public duty to respond (unblocks M4's promise text).** Promise that any outside
  objection that clears the bar gets a written answer within seven days of being raised (drafted
  by the cabinet, public once merged). *Recommend: yes, but only from M4, once outsiders can
  actually reach us.* The cost is that your merge speed becomes a public promise.
- **K3. Money on the open platform (shapes M5).** Any deposit, even refundable, crosses the
  "asks nobody for money" rule. *Recommend: design M5 with no money at all (reputation from
  resolved predictions, plus rate limits) and keep deposits as a documented option for later,
  pending a lawyer.*
