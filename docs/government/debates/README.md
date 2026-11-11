# Debates: the case against each policy, and the answer

One file per policy that has been argued over, `debates/<post>/<slug>.md`, matching its policy file
`policies/<post>/<slug>.md`. The **opposition** (a separate agent on a different model, worker
`opposition`) attacks each changed policy on the rolling PR; the **statistician** checks it can be
measured; the **cabinet** answers every point the next morning, conceding or rebutting, and writes
the exchange here. The PR is where the argument happens; this file is where it is kept, because a PR
closes and this doesn't. (Design: `design/2026-11-11-future-proof-government/README.md` §4.4.)

The cabinet writes these files. Newest exchange first; never edit an old entry.

```
# <policy title> (<post>/<slug>)

## <YYYY-MM-DD> · PR #<n>

**Opposition:** <the point, quoted as posted>
**Answer (<minister>):** <the reply, quoted as posted>
**Outcome:** Conceded: <what changed, commit sha> | Rebutted | Open

## <earlier date> · PR #<n>
…
```

The point still standing that is strongest goes onto the policy itself, as two front-matter lines
the site prints under the policy ("The best case against" and "Our answer"):

```
against: <the opposition's strongest standing point, one line>
answer: <the government's answer, one line>
```
