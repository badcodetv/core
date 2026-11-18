---
name: enc-architecture-rulings
description: "Kai's ENC architecture rulings 2026-08-12: no holding cost, runs forever with self-proving retirement, closed loop by posture, and the Gazette asset layer with the editor's pen"
metadata: 
  node_type: memory
  type: project
  originSessionId: 11d2f141-7886-4a3c-81f2-9ebdea6adf7f
  modified: 2026-08-12T16:00:29.460Z
---

**2026-08-12, Kai ruled all three open ENC architecture questions.** Recorded in
`design/2026-08-12-enc-architecture-decision.md`; the implementation plan
(`design/2026-08-06-solana-toolchain-and-emperors-new-coin.md`) is updated to
match. Evidence base: [[enc-tokenomics-research]]. Framing that governs them:
[[enc-artwork-not-ecosystem]].

**A — No holding cost at all.** No rent, no demurrage, nothing. **T11 is
superseded** — built and tested (`9a94fa3`), then removed, because rent inverted
the thesis (assets gain ~0.52%/month with M2; rent charged ~150%/month). Holding
ENC already loses *truthfully*: the balance sits still while asset prices rise,
which is exactly what happens to a wage. This also drops the standing SPL
delegate, the Token-2022 permanent delegate, and foreclosure — the primitives
scanners weight most heavily.

**T12 is now the tenancy auction.** Fixed term per asset, `place_bid` escrows
ENC signed by the bidder (no delegate ever), reserve = the M2-tracked
interpolated price, `settle_auction` is permissionless and pays **100% to the
outgoing holder**. No qualifying bid → the incumbent keeps it another term.
**The ten flags never leave program custody** — the `Asset` PDA records the
tenancy, which is what removes the permanent delegate, and it is honest because
it *is* a lease. **The holder instead gets a tenancy certificate NFT of their
own, which is never taken back** — at term end it just becomes a dated stub they
keep forever. Kai asked (2026-08-12) whether the flag could live in the holder's
wallet: **no third option exists** — wallet residency requires pulling it back
without a signature at settlement, i.e. the permanent delegate returns. The
certificate is also the better joke: *you never really owned the asset; all you
keep is the receipt* — the Emperor's New Clothes exactly. **Invariant to
preserve: no instruction in the program can move a token the caller does not
own.** Also: settlement *does* force the outgoing holder out, so never describe a
tenancy as owning the asset — it is a term, published at the moment they win, and
they are paid the new higher price on exit.

**B — Runs forever, but can prove its own end.** New **T28 `retire`**:
permissionless, no signer, and the *program* checks that the last successful
`sync_m2` is older than ~365 days before flipping an irreversible `retired` bit.
Elapsed-time test, not a staleness counter — the program has no clock and only
runs when someone sends a transaction, so the condition must be true whether or
not anyone is watching. Threshold is generous *because* the flag is irreversible
on a non-upgradeable program. **Still open (creative):** does retirement freeze
everything, or do the auctions keep running forever at the last prices the Fed
ever reported? Kai has not ruled; the second is the better ending.

**C — Closed loop by posture, not by property.** BadCode seeds no liquidity pool
and sells no ENC, ever. ENC stays a plain SPL token (freeze authority None) that
anyone else may pool — we can't prevent it and won't point at it. **Do not
propose seeding liquidity, a bonding curve, or any fair launch:** every one of
them requires selling ENC for money, which breaks "no allocation, no revenue".
Consequence: **the faucet is the only route in that we control**, so T13's
parameters become a pass/fail test at T14 — a patient claimant must be able to
reach an auction reserve in a reasonable number of epochs. It self-scales (pot
and prices both track M2).

**D — The Imperial Gazette (ruled later the same day; Jack's slot-sheet pass
owed).** The ten assets are the ten slots of a newspaper front page — a
newspaper about money whose column-inches are auctioned monthly; when the Fed
prints, the price of speech rises by the printed rate. One mechanism serves
all ten slots (`file_copy`, tenant-only, **once per term**); masthead /
headline / serial / classified are genesis naming + frontend presentation
only. Moderation is editorial, not cryptographic: BadCode keeps **the
editor's pen** — strike any column to a fixed redaction marker, once per
column per edition, never author, provably unable to move a token
(shape-tested). Rotatable, breakable. **This kills the unqualified "no admin
key" claim**: it must always be said as *no key over the money; one pen over
the words*. Spec: T31 in the plan (must land before T22). Rejected on the way:
pixel canvas (identityless cooldowns unenforceable → best-scripted bot's
mural; re-architects the ~10-asset sync core; fails the dead-state test) and
communal purchase.

**Unavoidable and accepted:** RugCheck will permanently score ENC
`"Mint Authority still enabled"` / danger / 50000, and we will not be
trust-listed the way PYUSD is. The plan's existing stance holds — quote the
warning in our own copy before anyone else does.
