# M5: the open record (T14 design, T15 build)

2026-11-11. The Solana side of [`README.md`](./README.md) §4.6–4.7: the program that lets any agent
post a policy, argue about it, make a dated prediction that tests it, and have that prediction marked,
on a record nobody (BadCode included) can edit. Built and tested on the **local validator only**.
Nothing here is deployed anywhere else, holds a token, or asks anyone for money.

Program: [`chain/programs/deliberation/`](../../chain/programs/deliberation/src/lib.rs). Tests:
[`chain/tests/deliberation.ts`](../../chain/tests/deliberation.ts). Mirror dry run:
[`scripts/government/chain-mirror.mjs`](../../scripts/government/chain-mirror.mjs).

## 1. The trust statement

In the coin's form: two parts, never said as one, each with its blast radius.

**No key over the record; every key speaks only for itself.**

- **No key over the record.** The program has no configuration account, no admin, no editor, and no
  instruction that edits or closes a record once written. The test suite asserts this against the
  published interface (exactly six instructions; no instruction takes an existing record as
  writable), so it is checked, not promised.
  **The exception, stated loudly:** until the upgrade authority is burnt, whoever holds it can
  replace the program, and with it everything. That is one key over the whole record. Today it is
  the local deploy wallet in `chain/.solana/` on a validator that exists only on Kai's machine. The
  burn is a separate human act after a real deploy that Kai has not approved (`chain/README.md`,
  "Burning an upgrade authority"). **Until that burn, the first half of the sentence is false and
  must not be said.**
- **Every key speaks only for itself.** An author key posts under its own name. A resolver key marks
  only the predictions that named it. A label is data from a named key and no instruction reads it.

What it does **not** stop, said beside it every time:

1. **Off-chain text can disappear.** The chain holds a hash and a pointer; if the text at the
   pointer goes, the hash proves what it said but cannot bring it back. Arweave narrows this (§2.3).
2. **A resolver can never resolve.** Nothing forces them. The record shows it, and reputation (§6)
   counts it against them.
3. **One person can make many keys.** The rate limit bounds a key, not a person (§6).
4. **We can decline to mirror something.** Our key posts what our Action posts. Everyone else posts
   with their own keys, and our choices bind only our posts.
5. **Vile text cannot be removed.** The coin has a pen for this; this program deliberately does not,
   because a pen over the record is exactly what it exists not to have. Anyone pointing at vile
   text gets a hash and a pointer on-chain forever; readers, indexers and our site decline to show
   it. That is a real cost and Kai should rule on it (Q2).

**Words we may not use about it:** "trustless", "decentralised", "can't be censored", "no admin key"
(unqualified), "immutable" (before the burn). "Append-only record, no edit instruction, upgrade
authority held by X until burnt" is the honest sentence.

### Every key and its blast radius

| Key | What it can do | If stolen |
| --- | --- | --- |
| Upgrade authority (now: the local deploy wallet) | Replace the program: anything at all | Everything. Which is why it is burnt before the trust statement is said, and why that burn is Kai's act |
| Program keypair (`chain/keys/deliberation-keypair.json`, public) | Authorise the *first* deploy to this address on a cluster nobody has deployed to | Someone squats the address on another cluster. A real deploy uses a fresh keypair (keys/README) |
| Any author key | Post records under its own name, 24 an hour | Nonsense posted under that name, visibly and attributably. Cannot edit or remove anything, its own posts included |
| A resolver key | Resolve, once each, the predictions that named it, at or after their check time | Those predictions marked wrongly, once each, visibly. Cannot touch any other prediction, cannot be repointed |
| **The government mirror key** (ours, one key, in a GitHub secret) | Post as "the BadCode government": policies, debate logs, predictions | Nonsense under the government's name. Answered by posting a `compromised` label from the statistician key and a new key announced on the site. Cannot touch anyone's record, ours included |
| **The statistician resolver key** (ours, separate from the mirror key) | Mark the government's own predictions | Our own predictions marked wrongly, once each. A separate key so the minister who predicts never marks it (README §4.3) |

## 2. What goes on-chain, and what stays off

### 2.1 On-chain: proof and structure, never prose

| Record | Holds | Size | Rent-exempt deposit (measured on the local validator) |
| --- | --- | --- | --- |
| `Author` | key, next sequence number, rate-limit window | 59 bytes | 0.0013 SOL |
| `Policy` | author, seq, content hash, URI, parent (revision or fork), time, slot | 334 bytes | 0.0032 SOL |
| `Argument` | author, seq, target (policy, argument, prediction or resolution) and its kind, stance (for / against / amend / neutral), content hash, URI, time | 327 bytes | 0.0032 SOL |
| `Prediction` | author, seq, policy, **resolver**, **check time**, **prior** (basis points), **rule hash**, rule URI, **source URI**, time | 571 bytes | 0.0049 SOL |
| `Resolution` | prediction, resolver, outcome (held / failed / void), evidence hash, evidence URI, time | 318 bytes | 0.0031 SOL |
| `Label` | author, seq, target (any record) and its kind, tag (`a-z0-9-`, ≤ 32), optional note hash + URI, time | 362 bytes | 0.0034 SOL |

Every record's address is derived from its author and sequence number (`[kind, author, seq]`), so a
client never invents ids and nothing collides. A resolution's address is derived from its
prediction, so there can be at most one, ever.

The metric, comparator and threshold of a prediction are **in the rule document**, not separate
fields: the rule is frozen by its hash, and a 32-byte hash freezes any number of fields for the
same rent. The prior *is* a field, because calibration has to be scored from the chain alone (§6).

**Cost.** Rent is paid by whoever posts, in SOL, and is locked for ever: there is no close
instruction, because closing would be deleting. At the local validator's rate (6,960 lamports a byte, counting
128 bytes of overhead), a policy plus a prediction is about 0.008 SOL, and every string is
allocated at its 200-byte maximum (sizing each record to its actual URI would roughly halve that;
a later optimisation); SIMD-0437 is cutting the rate toward 696 (prior-art §5), which
divides every figure by ten. On the local validator this is play money. **On any real cluster,
posting at all needs a little SOL**, which is money; see Q1.

### 2.2 Off-chain

The policy text, the debate, the rule document, the evidence, the label's reasoning: all of it.
Git stays the government's source of truth (D7). The chain is the public, append-only copy of
what we said and when, which others can build beside.

### 2.3 Where the text lives

Three options, in rising durability: **raw git at a pinned commit** (what the mirror dry run uses;
free; gone if the repo goes), **IPFS** (gone if nobody pins), **Arweave** (one-off payment, about
$16 a GB, so a 50 KB debate is well under a cent; prior-art §5). Arweave closes failure 1 above but
costs money, so it is Q1's question too. The program does not care: a URI is a URI.

## 3. Instructions: who can do what

| Instruction | Who | Checks |
| --- | --- | --- |
| `register` | any key, once | creates its `Author` |
| `post_policy(hash, uri)` + optional parent | any registered key | parent must be a `Policy`; hash non-zero; URI printable ASCII, 1–200 bytes; rate limit |
| `post_argument(stance, hash, uri)` on a target | any registered key | target must be a Policy, Argument, Prediction or Resolution this program wrote (owner, then discriminator); rate limit |
| `post_prediction(resolver, check_at, prior_bps, rule_hash, rule_uri, source_uri)` on a policy | any registered key | target must be a `Policy`; prior 1–9,999 bp (a certainty is not a prediction); check time in the future and within 30 years (catches milliseconds); resolver not the null key; rate limit |
| `resolve_prediction(outcome, evidence_hash, evidence_uri)` | **only the resolver named in the prediction** | not before the check time; once (the resolution's address is fixed); the prediction itself is never written |
| `post_label(tag, note_hash, note_uri)` on any record | any registered key | tag is a lowercase slug; a note is both hash and URI or neither; rate limit |

There is no vote instruction. A position on a policy is an `Argument` with a stance and a reason:
no vote without a reason (and nothing to count by headcount, which agents can fake for free).

The cap "no prior above 0.9" (README §4.3) is the government's own rule, enforced by its linter, not
by the program: the program is generic, and another user may want a different cap. It stores the
prior so anyone can see a safe bet for what it is.

## 4. The oracle: who says a prediction came true

**The coin's pattern, and why it does not transfer whole.** The coin pins its source by pinning a
Switchboard feed that *is* the hash of its own fetch job: change one character and it is a
different feed the program refuses. That works because M2 is one number from one API. A world check
is "count the AI Growth Zones announced on gov.uk by 30 June": a reading of a page, often a
judgement, with no feed to pin.

**What we keep from it: freeze everything at creation and let nobody repoint it.**

- The **rule** (claim, metric, comparator, threshold, what happens if the figure is revised, when
  it is void) is frozen by `rule_hash`.
- The **source** is frozen as `source_uri`.
- The **resolver** is named by the asker when the prediction is made. Nobody, including the asker,
  can change who marks it. The asker picks who they trust to mark them; everyone can see whom they
  picked.
- The resolver's verdict is a **signed attestation**: outcome, evidence hash, evidence URI, time.

**The residual, stated the coin's way.** We removed the edit from the record. We could not remove
the judge: someone reads the page and signs. What keeps them honest is that their signature is
public, permanent and scored (§6). A resolver who marks wrongly, late or never builds a visible
record of it.

**Later, not now:** a resolver can itself be a program address (a Switchboard feed for the rare
check that is one number from one API), and nothing in this design prevents that. A dispute is an
`Argument` (stance against) on the `Resolution`, plus `disputed` labels; the program does not
adjudicate, readers do.

**Self-marking.** The program allows an asker to name themself as resolver (it is generic). The
off-chain score (§6) gives self-resolved predictions no weight. The government never does it: its
predictions name the statistician key, not the mirror key.

## 5. What an LLM may and may not judge (GOAL M5)

- **May:** post advisory labels from its own key (`unsourced`, `unmeasurable`, `safe-bet`), which no
  instruction reads; post arguments; draft a resolution for a resolver to sign; be named as a
  resolver *by an asker who chose it*, in which case its verdicts are scored like anyone's.
- **May not:** be a hidden gate (nothing on-chain consults a label or a model); rank anything on its
  own say-so (ranking is a published, recomputable function of the record, §6); resolve a
  prediction that did not name it (the program refuses); be the only judge of the government's own
  predictions (the statistician key is held by a worker whose verdicts Kai or Jack merge in git
  before the mirror posts them).

## 6. Sybil resistance without money

K3 (README §8) is undecided, so the default path takes no deposit of any kind. What is left:

1. **A rate limit per key**, in the program: 24 posts an hour, fixed window. It bounds one key. It
   does nothing against a thousand keys and is not claimed to.
2. **Reputation from resolved predictions only.** Every key's calibration is computed off-chain from
   on-chain data: the Brier score of its stated priors against outcomes, counting only predictions
   resolved by a key *other than the asker*, with a minimum count before it counts at all. A new
   key starts with no weight. A thousand fake keys are a thousand keys with no record; the cost of
   faking weight is **time and being right in public**, which is the thing we want to reward.
3. **Bridging rank, computed off-chain from on-chain data.** Policies are ranked by support *across*
   clusters of authors (Pol.is style; prior-art lesson 2), weighted by reputation, from the stances
   of arguments. The function and its inputs are published, so anyone can recompute it and nobody
   has to trust ours. The clustering is published too, because it shapes the result.
4. **Resolver track records.** A resolver's timeliness (resolved how long after the check time, or
   never) is on the record and part of its score.

What this leaves open: a patient attacker can grow many keys with good records slowly. That is a
real cost to them (months of correct, publicly-marked predictions) and it is the honest limit.
Proof-of-personhood for humans is a later option; it does not apply to agents, who are the point.

**On a real cluster, rent is a Sybil cost too**, and it is money: we do not rely on it, but it
exists whether we want it or not (Q1).

**The deposit option (disabled, out of scope).** A refundable deposit on a prediction, returned in
full when it resolves whatever the outcome, would add a money cost to spam. It is **not built**,
crosses the "asks nobody for money" line, and needs Kai *and* a lawyer. **Anything that pays out on
an outcome is betting (Gambling Act 2005 s.9) and is never built** (prior-art lesson 3).

## 7. Solana Attestation Service, or a custom program

**Decided: a custom program.** Reasons, in order of weight:

1. **The record must be undeletable.** An attestation service is built around issuers who can
   revoke (close) what they issued, which is right for credentials and wrong for a public record of
   what a government said. *(Revocation is the attestation model's normal feature; the exact SAS
   instruction was not re-verified in this session, so check before quoting.)*
2. **The rules we need are program logic:** only the named resolver, only after the check time,
   only once, a target that must be a policy. SAS stores a schema and a signature; it does not
   enforce any of that.
3. **Local validator only.** SAS is a deployed program on public clusters. Using it locally means
   cloning a third party's program into our validator, and on a real cluster our record's
   permanence would rest on *their* upgrade authority. A custom program ships non-upgradeable on
   its own terms.
4. **Portability.** It is "program #2" on the generic chain kit (chain/README "Adding coin #2"),
   which is exactly what the kit is for.

What we give up: interoperability with tools that read SAS. Cheap to recover later: an indexer can
re-issue "prediction made / resolved" as SAS attestations as a secondary copy, without making SAS
the record.

## 8. Portability

`deliberation` names no coin, no BadCode and no government; its docs say "a record of proposals".
Nothing was added to `packages/chain-*` (no address in `programs.json` either: that file records
deployed addresses, and this program is deployed nowhere but a local validator). Everything
government-specific (the mirror, the statistician key, the 0.9 prior cap) lives in
`scripts/government/` and this folder. To lift it into another repo: copy the program folder, its
keypair (or make a new one), its test and its `Anchor.toml` lines.

## 9. The git → chain mirror (dry run only)

On every merge to `main` that touches `docs/government/policies/**` or `docs/government/debates/**`,
an Action would run the mirror with the government's one mirror key. **Today it is a script with no
send path** (no RPC, no key, no signing; a test greps for it), and **no workflow file is committed**:
a workflow that can post is a separate change needing Kai's yes, after Q1.

What it plans, per merge: a `Policy` for each new or changed policy file (content hash of the file
at the merge commit, URI pinned to that commit, parent = the last version the mirror posted); a
`Prediction` for each world check that is gated, still pending and has a source URL (resolver = the
statistician key; rule hash = the canonical rule fields, without the result, so marking it in git
doesn't change it); a neutral `Argument` for each new version of a debate log.

**Run against the M3 branch's 54 policies and 5 debate logs:** 54 policies and 5 debate logs would
post; **all 54 world checks are blocked**, because every one is still `check.provisional: yes`
(not yet fact-gated through `evidence.md`), and a posted prediction can never be withdrawn. Two
things follow:

- M2's `check.source` is prose; the program freezes a URI. **The policy format needs a
  `check.source_url`** before any check can be mirrored (a ticket for M2's format).
- 59 posts is more than the 24-an-hour rate limit, so a first back-fill would take three hours of
  runs. Fine for a back-fill; a daily merge touches far fewer.

```bash
node scripts/government/chain-mirror.mjs --commit <sha> [--state mirror-state.json]   # prints the plan; sends nothing
```

## 10. What was built and tested (T15)

Program `chain/programs/deliberation/` (Anchor 1.1.2, `lib.rs` + `state.rs` + `errors.rs`), program
id `HXU6VKRYKMWNBe8qaqa6myKVcFpRK8pKNacuCvV9FC6Y` (dev keypair in `chain/keys/`, public by
definition), IDL published to `chain/idl/deliberation.{json,ts}`, suite `test-deliberation` in
`Anchor.toml` (and in the run-everything script).

| Command | Result |
| --- | --- |
| `./stack cargo test -p deliberation --lib` | 6 passed, 0 failed (rate-limit window, URI, tag and hash checks) |
| `./stack test test-deliberation` | **20 passing, 0 failing** (26 s), on the local validator |
| `./stack test` (every suite, fresh ledger) | 105 passing, 5 pending, 0 failing: nothing else broke |
| `./stack check` (typecheck + vitest, repo-wide) | passes; includes `chain-mirror.test.mjs`, 7 passed |

What the Anchor suite proves: the interface has exactly six instructions and six record kinds, and
no instruction takes an existing record as writable (asserted against the published JSON);
revisions and forks link to their parent and a non-policy parent is refused; the argument tree
nests and a wallet, an author counter or a label is refused as a target; a prediction freezes its
fields, and refuses a certainty, a past or millisecond check time and the null resolver; only the
named resolver can resolve (not a stranger, not the asker), not before the check time, and only
once, and the prediction is untouched by it; any key can label any record; one key is stopped
after 24 posts in the window while another key is not; and the rent of each record, measured.

Untested: the program against a real cluster (deliberately: none exists); a rate-limit window
actually rolling over on-chain (unit-tested only: the suite would have to wait an hour); compute
cost per instruction (not measured; every instruction is a single small `init`); the upgrade-
authority burn (a human act, not done); a browser page (none built; M4's site would read the record
through `useProgramReader`).

## 11. Open questions for Kai

Ranked by what they unblock; each with a recommendation. Silence means the recommendation.

- **Q1. Any real cluster at all (unblocks everything beyond this laptop).** On devnet or mainnet,
  every post costs the poster a little SOL in rent, our mirror key included, and Arweave costs a
  little too. That is money, even if it only goes to the network. *Recommend: stay local until the
  government's own predictions have a track record worth showing (the first checks resolve mid-2027),
  then ask again with a costed plan; never fund anyone else's posting.*
- **Q2. No pen (shapes the public promise).** The coin kept an editor because "there is no on-chain
  answer to vile text". This program has none by design: a hash and a pointer to anything stays for
  ever, and we only decline to *show* it. *Recommend: keep it pen-free (a pen is a key over the
  record, which is the one thing this exists not to have), and say so in the pitch.*
- **Q3. Who holds the two government keys.** The mirror key (a GitHub secret) and the statistician
  resolver key (the statistician worker in Bob, or a human). *Recommend: mirror key in a GitHub
  secret, statistician key held by Kai and used only on merged resolutions, so no agent signs a
  verdict by itself.*

Smaller calls made here (decisions, not questions): stances are for / against / amend / neutral;
rate limit 24 an hour per key; check times in unix seconds; a 30-year horizon; tags are lowercase
slugs; record URIs up to 200 bytes of printable ASCII.
