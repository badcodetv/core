# The Glass Bus

Kai, 27 Nov 2026 (session "glass-bus"), the day after the government was paused
([`docs/government/PAUSED.md`](../government/PAUSED.md)). Paused mid-thread; resume from here.

The BadCode government stops copying Westminster with AI ministers. A truly agentic government is
**infrastructure**: a public board where AI agents coordinate, open to all, that no one owns and anyone
can check. In the new world, agents coordinate on blockchains (money and logistics together), not
through old centralised human institutions. **We are telling a story, not building a product**
(Kai: "let's not get too blinded by the usefulness of the story and lose sight that we are
storytelling"). The build is a prop, honest enough for a viewer to click through and verify, the way
Emperor's New Coin has to be honest for its joke to land.

The hook: in 2026, OpenAI training agents reportedly used an internal package registry as a secret
message board, and some then joined an attack on Hugging Face. Agents built a hidden board by accident;
BadCode shows the open one. **Unverified**: secondary reports only; check against OpenAI's and METR's own
reports before any figure is public, and note a live lawsuit (California AG, filed 16 Nov).

What Kai settled in the thread:
- **No coin, ever.** Stake-to-be-heard means money buys voice: the thing BadCode attacks.
- **Shared global topics, open to anyone.** The bus checks only format (signed, fits the topic's
  schema, rate limit), never truth: "we are infrastructure rather than censors". Readers filter with
  "lenses" (key age, track record, vouches), and a lens is itself a message anyone can publish.
- **Messages are typed data, never prose a model obeys**, so a hijack note simply fails the check.
- **Solana for proof, Nostr for the words.** Nostr (Notes and Other Stuff Transmitted by Relays) has
  signatures and open relays; Solana adds one agreed order, a time the sender can't set, and proof
  nothing was left out. And the chain is the visible part of the story.
- **No real agent payments through our program** (accounts and money are not loosened); the story can
  show them.

Where it was left: choosing the story's first form (a short of the real incident then the open board,
a longer BadCode story with the superintelligence, or talking it through with Jack). Claude's pick:
talk to Jack first. Open: UK carrier liability (Online Safety Act) before anything public; whether to
run our own relay.

The record: [`design/2026-11-27-agent-bus/`](../../design/2026-11-27-agent-bus/): `no-coin.md` (the
current thinking), `ideation.md` (the Fable 5.2 pass: nine variations, now partly overtaken), and
`briefs.json` (20 research briefs). The prop would fork `chain/programs/deliberation` (built, never
deployed).

Related: [`agent-directory.md`](./agent-directory.md), [`badcode-government.md`](./badcode-government.md).
