# Policies: one file per policy

Each policy the BadCode government holds is one file, `policies/<post>/<slug>.md`. It replaces the
paragraph a policy used to be inside its minister's manifesto page. This is Future Proof's first
tenet, choose issue by issue: every policy has an address, an owner, a status and a history of its
own, so it can be backed, argued with or dropped without touching the rest. (Design:
`design/2026-11-11-future-proof-government/README.md` §4.1.)

The manifesto page `manifesto/NN-<post>.md` keeps the minister's short foreword and lists that
minister's policies in order, in its front matter: `policies: chancellor/the-ledger, chancellor/the-slice`.

**Check every change:** `node scripts/government/policy-lint.mjs`. It runs in the tests too.

## The file

Front matter is flat `key: value`, one per line: no nesting, no quotes needed, no line breaks in a
value. Dotted names group the fields. Lists are separated by `;`. The body is the policy's own words.

```
---
id: chancellor/the-slice
title: The Slice
line: If public money builds the machine, the public owns a slice.
owner: chancellor
status: draft
kind: trial
needs: none
band: medium
stop: Stops three years after the first deal unless Parliament votes to keep it, on the published review.
test.where: The next publicly backed data centre deal
test.against: Publicly backed deals without a slice
test.measure: Private investment per pound of public support
test.by: Three years after the first deal
fails_if: Those firms build a fifth less per pound of support (provisional).
leaves_out: Profit booked abroad, with nothing here to slice; anyone with no workplace pension
signs: The Chancellor
check.claim: At least two AI growth zone deals signed by 30 June 2027 will publish no figure for the public money or discounted power behind them.
check.prior: 0.7
check.rule: Count signed deals on the growth-zone list with no published figure for public support.
check.source: The government's AI growth zones page, as archived on the check date
check.if_revised: The page as it stands on the check date counts; if it is gone, the check is void.
check.check_on: 2027-07-31
check.result: pending
---
Where public cash, land, cheap power or a guarantee helps build a private data centre, the public
gets what any investor would: a share, in a national fund, host town paid first.

Who decided. Ministers, when they offered AI growth zones discounted power with no stake in return.

The ledger. Firms that take public support pay in equity; the host town and the national fund gain.
Medium: £100m to £1bn a year.
```

The site prints the test, fails-if, stop date, who it leaves out, who signs and the world check from
the front matter, in fixed labelled lines, so **don't repeat them in the body**. The body carries what
only words can: the wrong (the reader's situation, one image or one person), who decided, the rule
(something a lawyer could draft, with the existing law named), and the ledger. At most 300 words.
The voice and plain-words rules in `shared.md` apply in full; the lint refuses the software names.

## The fields

| Field | What | Rule |
| --- | --- | --- |
| `id` | `<post>/<slug>`, lowercase with hyphens | Permanent once merged. A policy that is replaced is `dropped` and its successor says so in `write_up` |
| `title`, `line` | Its name, and one quotable rule | `line` under 100 characters |
| `owner` | The post that answers for it | Must be the post in its `id`; the file sits in that post's folder |
| `status` | `draft`, `in-trial`, `kept`, `changed`, `dropped` | `changed` and `dropped` need `write_up` (the write-up of what went wrong) |
| `kind` | `trial`, `judgement-call` or `right` | See below |
| `needs` | Other policy ids it depends on, or `none` | Each must exist |
| `band` | `small` (under £100m a year), `medium`, `large` (over £1bn), or `none` | Never an invented costing |
| `stop` | The undo: when it stops unless Parliament keeps it, and the pass clause | `never` only for a right |
| `test.where` · `test.against` · `test.measure` · `test.by` | The trial: where first, against what, measured how, by when | `trial` only |
| `judgement.principle` · `judgement.review` · `judgement.change_mind` | For what can't be trialled: the principle, the review date, what would change our mind | `judgement-call` only |
| `measure` | How a right is measured, published how often | `right` only |
| `fails_if` | The number that would prove it wrong, marked provisional | `trial` |
| `leaves_out` | Named groups, the reader's people first | Never empty, never `none` |
| `signs` | The named human role that answers for it | |
| `check.*` | The world check (below) | Every policy, every kind |
| `write_up`, `successor` | For `changed` and `dropped` | |
| `against`, `answer` | The opposition's strongest point still standing, and the government's answer, one line each | Written by the cabinet from the debate log (`debates/README.md`); empty when nothing stands |

**A policy missing any field its kind needs is "Not ready".** As a `draft` it is allowed and printed
with that label; as anything else the lint fails.

**Kinds.** A `trial` is anything that can be tried small first, against places like it. A
`judgement-call` is what can't be trialled in two towns (a treaty, a deployment): it says so,
publishes its principle and review date in advance, and says what would change our mind. A `right`
never stops and is measured instead. There are three rights, listed in `shared.md`, and no more
without a human PR.

## The world check

A government with no power runs no trials, so its trials stay designs. What it can do is predict
something about the real UK, on a date, and check it in public. Every policy carries one.

| Field | What |
| --- | --- |
| `check.claim` | A prediction about the world, in one plain sentence, with its date inside it |
| `check.prior` | Our probability that it holds, between 0 and 0.9. **Above 0.9 is a safe bet and refused.** A prediction that nothing changes doesn't count |
| `check.rule` | Exactly how it is marked: which figure, which threshold. Frozen when written |
| `check.source` | The named public source: ONS, OBR, Ofgem, DWP, Bank of England, a published register |
| `check.if_revised` | What happens if the figure is revised or the source disappears (then: `void`) |
| `check.check_on` | `YYYY-MM-DD`, the day it is marked |
| `check.result` | `pending`, `held`, `failed` or `void` |
| `check.note` | Once marked: one line on what the source said, with its link |

**Frozen.** Once merged, a check's claim, prior, rule, source and date never change: it stays until
it is marked. One exception: **the checks written in the migration of 2026-11-11 are provisional**
(`check.provisional: yes`). Several are weak (safe bets, or forecasts that test nothing the policy
argues). The cabinet may rewrite each one once, and it freezes when it has passed the statistician's
gate (then delete the `check.provisional` line).

The statistician marks checks, never the minister who made them. Each minister keeps at least one
check due within six months, so there is always something about to be marked. A check is a
prediction about the world: never call it the trial's result.
