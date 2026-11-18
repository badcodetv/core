---
name: enc-artwork-not-ecosystem
description: "Kai's ruling 2026-08-12: ENC is an artwork in a frame, not an ecosystem — indifference is an acceptable outcome, and legibility beats engagement"
metadata: 
  node_type: memory
  type: project
  originSessionId: 11d2f141-7886-4a3c-81f2-9ebdea6adf7f
  modified: 2026-08-12T16:00:40.344Z
---

**2026-08-12, Kai, ruling on Emperor's New Coin's purpose.** ENC succeeds if the
joke *exists and makes sense when someone looks at it*. It does **not** need
players, volume, a market price, or a living ecosystem. Kai expects "maybe a
couple of people spending tiny amounts of transaction fees interacting with it
as a joke" and that is fine. **It is okay if it dies and nobody cares.** The
artwork does not have to stay on the wall forever; it has to make sense to
whoever looks at it.

**Why:** the point is the demonstration, not the economy. Building it for real
is what makes the joke land — a thing that actually exists on chain and actually
tracks M2. Engagement was never the deliverable.

**AMENDED 2026-08-12 (evening), by Kai, knowingly:** the blanket form is
narrowed. The **content layer** (the Gazette — what tenants write, how the
front page reads) **may court an audience; engagement is an admitted goal
there.** The bright line that survives: **no economic mechanism or parameter
may ever be justified or tuned by engagement** — that is how rent inverted the
thesis — and the **dead-state test is the floor**: the piece must still read
as a complete joke at zero participation. Recorded as Ruling D in
`design/2026-08-12-enc-architecture-decision.md` §7; see
[[enc-architecture-rulings]].

**How to apply:**
- **Never optimise economics for turnover, retention, liquidity or
  participation.** Any economic mechanism justified by "this keeps people
  playing" (rent as a turnover engine, anti-dormancy design) has lost its
  justification. Content-layer features may want an audience — but must pass
  the dead-state test. See
  [[enc-tokenomics-research]] — this ruling voids roughly half of what those
  briefs flagged as risks (dormancy, bot capture, thin liquidity, sybil farming).
- **Optimise for legibility instead.** What survives is: does the mechanism
  *read correctly* on inspection; are the claims *literally true*; does a risk
  scanner make it look like a scam; is the underlying economics defensible. Those
  matter more under this framing, not less.
- **A failed mechanism is worse than an unused one.** Rent that inverts the
  thesis is fatal (it doesn't compute when examined); rent nobody pays is merely
  quiet.
- Kai floated a **time limit** (e.g. a 3-year experiment rather than forever) to
  bound oracle risk, running costs and abandonment. Treat as a live idea, not a
  decision — the open question is what the sunset *does*.

Related: [[enc-program-build]] (the build and the open delegate ruling),
[[solana-toolchain-initiative]] (the plan this all sits under).
