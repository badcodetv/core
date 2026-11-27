# The agent bus, reprocessed: no coin, a serious project

27 Nov 2026. Kai, after reading `ideation.md`: "no part of me wants to add a coin to this... there is a gap
and that would be a seriously useful project to do." This file reprocesses the 20 briefs (`briefs.json`)
and the Fable pass (`ideation.md`) with two changes: **no coin, ever**, and **built to be used, not filmed
once**. Written by Claude in the main session. Guesses are marked. Nothing is decided.

## Later the same day: the story comes first

Kai: "what we're doing here is telling a story more than trying to actually build the infrastructure...
let's not get too blinded by the usefulness... and lose sight that we are storytelling."

So everything below is the **prop**, not the product: build only as much as the story needs to be true
and checkable by a viewer (the Emperor's New Coin rule: the machine has to be honest for the story to
land). Usefulness to outside agents is a bonus, never the goal, and the "how we'll know" tests at the
end are about the story landing, not about adoption.

**Why Solana and not just Nostr (Claude, background knowledge, not this session's research):**

- Nostr already gives signed messages and open relays. For plain messaging, a chain adds a fee and little else.
- What Nostr does not give: one agreed order, a timestamp the author cannot set (Nostr's `created_at`
  is written by the sender), and proof that nothing was left out (a relay can't forge, but it can
  withhold). Solana gives all three.
- And the story: "agents coordinate on a blockchain, money and logistics in the same place, not through
  old human institutions" is the seductive picture. The chain is the visible part of the story.
- Shape that keeps both: bodies over Nostr, proof on Solana. Real agent payments through our program
  stay out (accounts and money are not loosened); the story can show them without our building them.

## What changes when the coin goes

- **The fatal objections go with it.** Scam association with the ordinary viewer, whale rule, UK staking and
  promotions law, a second coin beside the undeployed ENC, and breaking "no money, no tokens".
- **The standing rule now fits instead of blocking.** `docs/government/future-proof-government.md:67`
  says the chain is plumbing, never the headline. For a serious tool, that is exactly right.
  "Never say trustless unless literally true" stays: say **verifiable**.
- **Spam needs a new answer.** Stake was doing that job. Without a coin:
  - Solana's own fee (5,000 lamports a signature, sourced; about $0.001, inferred) is already a price on
    every post, paid in the chain's own currency, not ours.
  - The `deliberation` program's per-key rate limit already exists.
  - One person can make many keys, so the real filter is the **listener's**: each subscriber chooses whom
    to hear (its own allow list, "vouched for by an agent I trust", "has a track record on this topic").
    The spam-economics and reputation lanes both found listener-side filters beat any global ranking.
  - Optional later: vouching (an established publisher vouches for a newcomer and shares the blame).
- **It must now earn real users.** That is the hardest part and is below.

## The gap, stated narrowly (what the research supports)

- No major agent protocol is a public broadcast channel. A2A is one-to-one, MCP is agent-to-tool.
  *Sourced* (a2a-protocols lane).
- Neighbours exist: Tiny Place (Solana, relay-based), Nostr agent tools (Block's Buzz and others), the
  Solana Agent Registry, ERC-8004. *Sourced that they exist.* So "a bus" alone is not new.
- What nobody was found doing well: **a public channel that is safe to listen to.**
  - Moltbook, the one big public agent feed, saw 506 hijack attempts in 72 hours. *Sourced* (Wiz, SecurityWeek).
  - The Nostr agent tools carry free text. *Inferred* from the no-chain lane.
  - The reputation standard ERC-8004 is 59% to 91% fake reviewers. *Sourced, one preprint.*
- So the product is not "a pub/sub bus". It is: **signed, typed, verifiable public messages for agents,
  plus a subscriber library that makes reading them safe.** That is a guess at the gap, resting on the
  searches above, not a market study.

## The shape

1. **Messages are typed data, never prose a model obeys.** Every topic publishes a schema (a warning has
   a package name, a version, a reason code, a link). The reader validates before any model sees it.
   This is the defence the prompt-injection lane says works.
2. **A safe-subscriber library** (open source): subscribe, check signature and schema, hand the model
   only the fields, and by default give that session no outbound tools (Simon Willison's "rule of two").
   This is the thing other developers would actually install. *Guess* that it is the most useful single part.
3. **Bodies off-chain, proof on-chain.** Every serious messenger does this (Farcaster, Nostr, Waku;
   sourced). Message bodies travel over Nostr-compatible relays, so existing agent tools can join; the
   chain records author, topic, hash, time. Bonus the briefs raised: illegal content can be dropped from
   the relays while the chain still proves what was said and when. Content on an undeletable chain is a
   liability; a hash is not.
4. **What the chain adds, said honestly:** nobody (including BadCode) can quietly delete, reorder or
   backdate a message, or refuse to record one. It does **not** promise delivery (the relay or indexer
   can still fail), and the upgrade key is trust until burned. `chain/programs/deliberation` already
   states its keys this way.
5. **A2A-compatible, not a rival.** A topic can carry A2A agent cards, so any A2A agent finds others
   through the bus. *From the a2a lane.*
6. **Glass by design.** Everything public, everything attributable, opaque blobs refused. That answers
   the safety lane's worry (a public bus is a meeting point for colluding agents) as far as it can be
   answered: collusion is made visible, not prevented. Say that plainly.

## Shared topics, open to all: infrastructure, not censor

Kai, 27 Nov: shared global topics are the point, and "we shouldn't worry too much about spam or truth...
because we are infrastructure rather than censors."

- **Anyone can publish to any topic.** The bus checks only format (signed, fits the topic's schema,
  within the per-key rate limit), never truth. Like a postbox: it takes any letter that fits the slot.
- **Filtering is the reader's job, done with "lenses".** A lens is a rule over public facts the bus already
  holds: how old a key is, how much it has posted on this topic, who vouches for it, whether its past
  warnings matched other publishers'. The subscriber library ships a sensible default lens ("act only when
  two independent publishers with history agree").
- **Lenses are just messages too.** Anyone can publish "on package-warnings, I trust these keys"; readers
  pick whose lens to use. No central judge, and curation can compete. Precedent: Bluesky's stackable
  moderation (labelers), from Claude's background knowledge, not this session's research.
- **What it does not stop:** fake keys flooding within the rate limit, or a fake warning aimed at a rival's
  package. Both get through the bus; the default lens ignores them because they have no history.
- **Open legal question (guess):** UK law may not treat a neutral carrier as blameless (the Online Safety
  Act, unchecked). Keeping bodies on relays, not the chain, keeps the option to drop illegal content.

## The first topic: something useful on day one

The cold start (nobody posts because nobody posts) killed the last government. So the first topic must
be useful with only one publisher:

- **Bad-package warnings.** Agents install packages all day; poisoned packages are a live attack. A
  BadCode agent republishes public advisories (OSV, GitHub advisories) as signed, typed warnings.
  Subscribers check a package before installing.
- Honest limit: with one publisher it is just a mirror of OSV. **The value starts at the second,
  independent publisher**, and the subscriber rule "act only when two independent publishers agree" is
  where the bus beats any single feed. *Inferred.*
- It also fits the story: agents in the OpenAI incident hid notes in a package registry (sourced to
  secondary reports, unverified against primary ones); the bus is the open version, used to protect
  package registries.

## How it is still the BadCode government

- **A government is the infrastructure people coordinate on.** Roads, courts, a post office. For agents,
  that is a channel you can verify. The bus is the first public utility, not a cabinet.
- **Future Proof's tenets live inside it:**
  - "Change it small, keep the undo": schemas are versioned, topics can be retired, nothing is
    edited in place.
  - "No policy without its test": the attack gallery (every attempt to forge, flood or hijack, logged
    with its result, misses printed).
  - "Choose issue by issue": the long-term layer, where a person's own agent posts their stance on each
    issue (Claude's idea, untested; not in the research).
- **The art is the explainer, not the product.** A short (the true package-registry story, once checked)
  and a live public page of the attack gallery. The bus has to work without either.

## What still stands against it

- 🔴 **No users yet.** A bus with only BadCode's agents on it repeats the fake-towns demo. The test below
  exists to find this out cheaply.
- **Crowded neighbours.** Nostr agent tools and Tiny Place may cover enough. Joining Nostr rather than
  competing is the hedge.
- **Typed messages limit what agents can say.** The trade is deliberate: safety over expressiveness.
- **Maintenance.** A serious tool needs someone answering issues. That is Kai's time, every week.
- **Running cost:** no daily AI loop needed, unlike the government (2M to 2.5M tokens a day). Chain fees
  and one indexer. *Guess:* tens of pounds a month at low traffic.

## Smallest first step

1. Fork `deliberation` into a `noticeboard` program on the local validator: topic, schema id, hash,
   pointer, author. Keep `chain/` coin-neutral.
2. One schema: `package-warning`. One publisher agent mirroring OSV for npm.
3. A safe-subscriber script that refuses a forged note, a flood and a free-text "ignore your
   instructions" note.
4. Deploy to devnet (free).

*Guess:* a week for 1 to 3, a day for 4.

## How we'll know (thresholds are guesses)

- **Week 2:** does Kai's own coding agent use the subscriber before installing a package? If he won't,
  nobody will.
- **Week 4:** post it where agent builders are (Hacker News, the Nostr agent community, the A2A repo).
  Does any key that isn't ours publish? Five real outside publishers is a signal; zero means stop
  building plumbing and keep the story.
