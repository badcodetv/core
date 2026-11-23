# Future Proof rework of the government (23 Nov 2026)

Kai, 23 Nov 2026: the BadCode government's goal is to **demonstrate Future Proof**, a structure of government
completely different from today's, with a cabinet layer on top as the funny, followable surface. It is art and a
thought experiment ("the way to get the right answer on the internet is to put the wrong answer on the internet"),
not a claim that this would work. Kai accepted every recommendation below.

- Visual explainer: https://claude.ai/artifact/8JJXdfsxM8PBzCBH3iWCQo (source: [`future-proof-engine.html`](./future-proof-engine.html))
- Why we changed course: [`adversarial-review-2026-11-23.md`](./adversarial-review-2026-11-23.md) (condensed)

## Why we changed course

- **The loop.** In the 11 days after the 11 Nov build, the debate looped on three policies. Two rules caused it:
  - the opposition reads only policies that changed;
  - the cabinet concedes every point into the policy text, so the policy changes again.
  - Result: 47 of 56 policies were never challenged.
- **The costume.** A cabinet arguing with an opposition is still Westminster with better policies.

## The design in one sentence

You set the test, anyone writes the answer, the calendar marks it, and a jury settles what the numbers can't.

- **The Ask (composition).**
  - People choose tests: what must get better, by when, what must not get worse.
  - They choose issue by issue. They never choose a party, a person or an expert.
  - Until real people take part, the Ask is borrowed from real polls and stamped as borrowed.
- **The Queue (CI).** A public script picks three dockets a day:
  - one the real Parliament is deciding;
  - the one that has waited longest;
  - one alarm (a check falling due or a failed number).
- **The Bench (composition).** Rival answers, each written blind on a different AI model, with no replies. This replaces the opposition.
- **The Gate (CI + data).**
  - Each answer is checked against its own test and every other field's limits.
  - Costs sit side by side, with who paid for each.
  - It prints results and never picks a winner.
- **The Jury (humans only, drawn by lot; today Kai and Jack).**
  - Settles values questions, money, and clashes between fields.
  - Decides keep-or-undo when a trial fails.
  - Every ruling goes in a book with a review date.
- **The Signer (the minister).**
  - Signs a small trial, or refuses once in public, which sends it to the jury.
  - Keeps the job for pulling a failure. Is sacked for hiding one.
- **The Clock (data).** On the date, someone who did not write the answer reads the number against a rule frozen in advance. Pass: the trial goes wider. Fail: the undo fires.
- **Expertise** buys weight in one place only: forecasting, by marked record.
- **Money** starts from the real UK split, with a floor per field. Only the jury moves it, in small steps. Popularity buys queue slots, never cash.

## Decisions (Kai, 23 Nov 2026)

1. The test is the unit people choose.
2. Kai and Jack are named as the jury: "Jury: 2. Should be 99."
3. No elections anywhere. The jury hires ministers and voters can recall them. The page labels this as the part most likely to be wrong.
4. Visitors may set their own tests, in their browser only. They are never sent or counted.
5. One "how it works" page may use the software words. Everywhere else keeps the plain-words rule.
6. Readers get four steps (set the test, write answers, check and sign, mark it). The seven parts above sit underneath.
7. Honesty stamps on every element: Real / Borrowed / Stand-in / On paper. Never "the people decided".

## Still open

- `docs/stories/gitpush-origin-master/future-proof.md` tenet 3 says competence qualifies you to "weigh in". The design narrows that to "forecast". It is a canon edit and has not been made.
- Thames Water figures come from a research pass and have not been re-checked. A single-source claim about who is Prime Minister also came up; check it before anything goes public.

## Roadmap

1. **Week 1: stop the loop, start the queue.**
   - Add the queue script, picking by staleness.
   - A policy's words change only on a failed test, a ruling or a new sourced fact.
   - At most one change per policy a fortnight, and a change cannot make a policy longer.
   - Word caps on `test.measure` and `fails_if`.
2. **Week 2: Thames Water end to end, built by hand.** Produces the Gap page: what people asked for, what Parliament did, what the engine did.
3. **Week 3: run it daily.**
   - `bench` (Claude) and `rival` (Codex) workers in Bob.
   - The cabinet becomes the read-out; a rulings book; one prediction due within 30 days on every docket.

**Kept:** policy files, world checks and the statistician's marking, the news sweep, the lint, `evidence.md`, the ten minister briefs, the vibe desk, the rolling PR and the human merge.

**Retired:** the opposition as a separate body, reviewing only what changed, and conceding into the text.

## At scale: the self-running simulation (Kai, 23 Nov 2026)

Kai and Jack won't have time to review it, so the simulation must **run and publish itself**. Human
intervention points exist as guidance, never as a requirement.

### Decisions

1. **Simulation output publishes without a merge.** Each issue page is stamped "simulated".
   Changes to the manifesto (`docs/government/policies/`) still need a human merge.
2. **Simulated citizens are allowed.**
   - They are always stamped as simulated and are never called "the public".
   - Each is built from real UK demographics.
   - Where a real poll on the same question exists, it is shown beside them.
   - This replaces the earlier "never a made-up crowd" rule, for the simulation only.
3. **Volume:** one issue a day to start, growing to five.
4. **Where it lives:** a private page first; badcode.tv once it has run cleanly for about two weeks.
5. **Idea (Kai): a live view of all issues at once.** The loop diagram, with every live issue moving
   round it at the same time, possibly in 3D: "real-time politics actually happening".

### What runs each day

| Step | What | Engine |
| --- | --- | --- |
| News | The existing news sweep | Claude (as now) |
| Clerk | Turns today's top stories into issues; the public picking script chooses which run | Claude, plus a script |
| Citizens | About 100 drawn from a fixed pool of about 1,000 simulated UK residents. Each sets tests and limits, and the answers are aggregated | Cheapest model, batched |
| Bench | Three rival answers, written blind | Claude and Codex |
| Gate | Checks each answer against every test and limit, with costs and who paid. Every claim about a real company or person must cite a published source | Claude |
| Jury | 12 to 99 citizens drawn by lot vote on the values question. A "real jury" lane is kept for Kai and Jack on headline issues | Cheapest model; Kai and Jack optional |
| Minister | The cabinet voices read out the result | Claude |
| Clock | Predictions are marked on their real dates. This is the only fully real part | Claude (the statistician) |
| Publish | One data file per issue per day; the platform page draws it | Script and site |

### Guard rails

- **The "SIMULATED" stamp is part of every card and image,** so screenshots carry it.
- **No invented facts about real people or companies.** The gate rejects any claim without a source.
- **Persona sameness is shown, not hidden.** Simulated answers are less varied than real ones, so the
  real poll appears beside them wherever one exists.
- **Cost:** guess one to two times today's daily spend at five issues a day. Bob doesn't count tokens
  yet, so measure a week before growing past one issue a day.

### Phases

1. **Template.** The Thames Water run as one data file, plus a private page that draws it with the loop animation.
2. **One a day, automated.** Real news, 100 citizens, a jury of 12. Publishes itself to the private page.
3. **Five a day.** The platform feed and the scoreboard.
4. **Live view.** All issues moving round one loop together (3D candidate). Then badcode.tv.
