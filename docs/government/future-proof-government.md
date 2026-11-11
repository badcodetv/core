# Why the government runs this way

**The canonical record of what the BadCode government is for, and why it is built the way it is.**
Ruled by Kai on 2026-11-11 and live the same day. Read this before changing how the government works.
How the machinery runs day to day is in [`README.md`](./README.md); the build plan, research and
every design decision are in
[`design/2026-11-11-future-proof-government/`](../../design/2026-11-11-future-proof-government/README.md).

## The ruling

The government started as a satirical cabinet that read the news and rewrote its manifesto. Kai's
ruling: **its real job is to be Future Proof, running.** It is a public, inspectable example of a
government built on Future Proof's three tenets, so that the question "how would we actually do
Future Proof?" has an answer you can point at. Then the platform it runs on moves to one BadCode
doesn't control, so the world's agents, and later anyone, can join in.

## Why

- **The message.** We need to change how we govern before AI outruns the politics, not after. Saying
  so is a sermon; showing it working is a story. The government is that story in the present tense.
- **The diagnosis it answers.** Today you vote for a person or a party and inherit their whole
  bundle. You wait five years for the next release. And policy rides on "trust me", with nobody
  measuring whether it worked. Future Proof's three tenets answer those three failures (canon:
  [`docs/stories/gitpush-origin-master/future-proof.md`](../stories/gitpush-origin-master/future-proof.md)).
- **Credibility.** A party that asks for testable politics has to be testable itself. So the
  government obeys its own rules first, in public, misses included.
- **Not owning it.** A platform for a better politics that one company owns is a contradiction. The
  end state is a record nobody can quietly edit, us included.

## The three tenets, made into machinery

| Tenet | The failure it answers | How the government embodies it |
| --- | --- | --- |
| **Choose issue by issue** (composition over inheritance) | You inherit a whole party bundle | Every policy is its own file and its own web page, with its own owner, status and fate ([`policies/`](./policies/README.md)). Back one, bin the next |
| **Change it small, keep the undo** (continuous integration) | A government shipped on a CD every five years | Every change is one small commit to one policy on a public PR that a human merges. Every policy has a stop date, and its history shows on its page. The linter is the test a change must pass |
| **No policy without its test** (data-driven decisions) | "Trust me, I know what to do", never measured | Every policy carries its trial design and a **world check**: a dated prediction about the real UK, with our odds and a frozen rule, marked by a separate agent against a public source. The scoreboard prints every result, misses included |

**And the debate.** One AI playing every minister agrees with itself. So a separate **opposition**
on a different model family (Codex) attacks every change. A **statistician** refuses anything that
can't be measured, and marks the predictions. The cabinet must answer every point, conceding or
rebutting, never just obeying. The exchange is kept in [`debates/`](./debates/README.md), and the
strongest point still standing is printed on the policy as "The best case against".

## The daily loop

```
05:00 news gatherer  ─►  06:00 cabinet proposes  ─►  07:30 opposition attacks (Codex)
                                                         │
     Kai / Jack merge  ◄─  next 06:00 cabinet answers  ◄─  08:00 statistician gates + marks due checks
            │
            └─►  badcode.tv: each policy's page, its marks, its history, the scoreboard
```

## The honesty rules (do not loosen)

- **A government with no power runs no trials.** Its trials stay designs. What it can do is predict
  the real world and get marked. A world check is "a prediction about the world", never "the
  trial's result".
- **No safe bets.** Odds above 90% are refused, and so is a prediction that nothing changes. The rule
  is frozen when written. The minister who made a prediction never marks it.
- **Misses are printed.** A failed prediction is the system working.
- **"Not ready" is honest.** A policy without a real test says so. We never invent a kill number to
  look complete.
- **Humans hold the pen.** Nothing reaches `main` or badcode.tv without Kai or Jack merging it.
- **The chain is plumbing, never the headline.** Never say "trustless", "decentralised", "can't be
  censored" or "no admin key" unless literally true, and state every key's blast radius. No money,
  no tokens, no betting.
- **The satire stays on the surface.** "Not a real party. Yet." The machinery underneath is real.

## Where it goes next

- **Visualise it.** Show the loop working on the GOVT channel: proposals, attacks, answers,
  predictions coming due, not just a list.
- **Open the record.** The generic `deliberation` program (`chain/programs/deliberation/`) is built
  and tested on the local validator only. It goes on a real network only on Kai's say-so, after the
  predictions have a track record. Then outside agents can propose, argue and predict beside ours.
- **Invite the world's agents.** The pitch is drafted and held
  ([`pitch.md`](../../design/2026-11-11-future-proof-government/pitch.md)).

## Changing this

This file changes only by a human PR. So do `shared.md`, the workers and the policy format.
A change to how the government works should say which tenet it serves, and how we'd know it helped.
