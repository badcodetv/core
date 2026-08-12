/**
 * The tenancy auction: bidding, settlement, and the certificate.
 *
 * The property every case here is really defending: **no token leaves any
 * wallet without that wallet owner's signature.** Settlement is permissionless
 * and moves the winner's escrow by design, so the invariant cannot be "no
 * instruction moves tokens the caller does not own" — that was the earlier,
 * unsatisfiable phrasing. It is about signatures, and it is why bids are
 * escrowed by the bidder rather than debited by a delegate.
 *
 * Terms run for `TERM_SECONDS` on this ledger rather than the shipped 30 days —
 * see the note there. Real time is the only clock the program has, so the
 * settlement cases genuinely sit and wait.
 */
import { expect } from 'chai'
import { Keypair, PublicKey, LAMPORTS_PER_SOL } from '@solana/web3.js'
import {
  TOKEN_PROGRAM_ID,
  TOKEN_2022_PROGRAM_ID,
  getAccount,
  getMint,
  getTokenMetadata,
  closeAccount,
} from '@solana/spl-token'

import {
  BN,
  big,
  harness,
  bootstrap,
  mockFund,
  setMockM2,
  placeBidAccounts,
  withdrawBidAccounts,
  settleAccounts,
  certAccounts,
  assetMetas,
  syncAccounts,
  TERM_SECONDS,
  ATA_PROGRAM,
  type Harness,
} from './enc-harness.js'

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms))

interface Curve {
  priceFrom: { toString(): string }
  priceTo: { toString(): string }
  interpStart: { toNumber(): number }
  interpEnd: { toNumber(): number }
}

/** Mirrors `PriceCurve::price_at` in math.rs. */
function priceAt(a: Curve, now: number) {
  const from = big(a.priceFrom)
  const to = big(a.priceTo)
  const start = a.interpStart.toNumber()
  const end = Math.max(a.interpEnd.toNumber(), start)
  if (now >= end) return to
  if (now <= start) return from
  const span = BigInt(end - start)
  const elapsed = BigInt(now - start)
  return from + ((to - from) * elapsed) / span
}

describe('the tenancy auction', () => {
  const h = harness()
  const alice = Keypair.generate()
  const bob = Keypair.generate()

  const asset = (i: number) => h.program.account.asset.fetch(h.assetPda(i))
  const now = () => Math.floor(Date.now() / 1000)
  const escrowBalance = async () =>
    (await h.exists(h.escrowEncAta))
      ? BigInt((await getAccount(h.connection, h.escrowEncAta)).amount.toString())
      : 0n
  const encBalance = async (owner: PublicKey) =>
    (await h.exists(h.encAta(owner)))
      ? BigInt((await getAccount(h.connection, h.encAta(owner))).amount.toString())
      : 0n

  /**
   * Bring asset `i` to the start of a live term, whatever state it was left in.
   *
   * Bootstrap happens once per ledger and every suite shares it, so by the time
   * this runs a term has usually already lapsed. Settling or rolling it is not
   * setup noise — it is the same permissionless path a stranger would use.
   */
  async function freshTerm(i: number) {
    for (let attempt = 0; attempt < 4; attempt++) {
      const a = await asset(i)
      if (now() < Number(a.termEndsAt) - 3) return a

      const reserve = priceAt(a, now() + 1)
      const qualifies = big(a.highBid) > 0n && big(a.highBid) >= reserve
      if (qualifies) {
        await h.program.methods
          .settleAuction(i)
          .accounts(settleAccounts(h, i, a.highBidder, a.holder))
          .rpc()
      } else {
        await h.program.methods.rollTerm(i).accounts({ asset: h.assetPda(i) }).rpc()
      }
    }
    throw new Error(`asset ${i} would not settle into a fresh term`)
  }

  /** Wait out the current term so it becomes settleable. */
  async function waitOutTerm(i: number) {
    const a = await asset(i)
    const remaining = Number(a.termEndsAt) - now()
    if (remaining > 0) await sleep((remaining + 2) * 1000)
  }

  before(async function () {
    this.timeout(180_000)
    await bootstrap(h)

    for (const who of [alice, bob]) {
      const sig = await h.connection.requestAirdrop(who.publicKey, 5 * LAMPORTS_PER_SOL)
      await h.history.confirmTransaction(sig, 'confirmed')
    }
    // Enough to clear the cheapest asset's reserve several times over. The
    // vault is the only source of ENC until T13's faucet exists.
    const stake = big((await asset(0)).priceTo) * 4n
    await mockFund(h, alice.publicKey, stake)
    await mockFund(h, bob.publicKey, stake)
  })

  // ── Bidding ───────────────────────────────────────────────────────────────

  it('refuses a bid below what M2 says the asset is worth', async () => {
    const a = await freshTerm(0)
    const under = priceAt(a, now() + 2) - 1n
    const why = await h.failureOf(() =>
      h.program.methods
        .placeBid(0, new BN(under.toString()))
        .accounts(placeBidAccounts(h, 0, alice.publicKey))
        .signers([alice])
        .rpc(),
    )
    expect(why, 'a bid under the reserve was accepted').to.match(/BidBelowReserve/)
  })

  it('escrows a qualifying bid, and refuses one that only ties it', async () => {
    const a = await freshTerm(0)
    const bid = priceAt(a, now() + 2) + 1_000n

    const before = await escrowBalance()
    const aliceBefore = await encBalance(alice.publicKey)
    await h.program.methods
      .placeBid(0, new BN(bid.toString()))
      .accounts(placeBidAccounts(h, 0, alice.publicKey))
      .signers([alice])
      .rpc()

    expect(await escrowBalance()).to.equal(before + bid)
    expect(await encBalance(alice.publicKey)).to.equal(aliceBefore - bid)
    const after = await asset(0)
    expect(big(after.highBid)).to.equal(bid)
    expect(after.highBidder.toBase58()).to.equal(alice.publicKey.toBase58())

    // Ties lose: the earlier bidder keeps the position they paid a fee for.
    const why = await h.failureOf(() =>
      h.program.methods
        .placeBid(0, new BN(bid.toString()))
        .accounts(placeBidAccounts(h, 0, bob.publicKey))
        .signers([bob])
        .rpc(),
    )
    expect(why, 'a tying bid was accepted').to.match(/BidNotHighEnough/)
  })

  it('charges only the difference when a bidder raises their own bid', async () => {
    const a = await freshTerm(0)
    const first = priceAt(a, now() + 2) + 5_000n
    await h.program.methods
      .placeBid(0, new BN(first.toString()))
      .accounts(placeBidAccounts(h, 0, alice.publicKey))
      .signers([alice])
      .rpc()

    const paidSoFar = await encBalance(alice.publicKey)
    const raised = first + 7_000n
    await h.program.methods
      .placeBid(0, new BN(raised.toString()))
      .accounts(placeBidAccounts(h, 0, alice.publicKey))
      .signers([alice])
      .rpc()

    expect(await encBalance(alice.publicKey), 'the raise cost more than the raise').to.equal(
      paidSoFar - 7_000n,
    )
    expect(big((await h.program.account.bid.fetch(h.bidPda(0, alice.publicKey))).amount)).to.equal(
      raised,
    )
  })

  it('refuses to let a stranger bid out of somebody else\'s account', async () => {
    const a = await freshTerm(1)
    const bid = priceAt(a, now() + 2) + 1_000n
    // Bob signs, but names Alice's token account as the source.
    const why = await h.failureOf(() =>
      h.program.methods
        .placeBid(1, new BN(bid.toString()))
        .accounts({
          ...placeBidAccounts(h, 1, bob.publicKey),
          bidderTokenAccount: h.encAta(alice.publicKey),
        } as never)
        .signers([bob])
        .rpc(),
    )
    expect(why, 'a bidder spent an account they do not own').to.not.equal('')
  })

  // ── Settlement ────────────────────────────────────────────────────────────

  it('refuses to settle before the term ends', async () => {
    const a = await freshTerm(0)
    const bid = priceAt(a, now() + 2) + 1_000n
    await h.program.methods
      .placeBid(0, new BN(bid.toString()))
      .accounts(placeBidAccounts(h, 0, alice.publicKey))
      .signers([alice])
      .rpc()

    const holder = (await asset(0)).holder
    const why = await h.failureOf(() =>
      h.program.methods
        .settleAuction(0)
        .accounts(settleAccounts(h, 0, alice.publicKey, holder))
        .rpc(),
    )
    expect(why, 'a term settled early').to.match(/TermNotEnded/)
  })

  it('pays the outgoing holder the entire winning bid, and never changes supply', async function () {
    this.timeout(120_000)
    const a = await freshTerm(0)
    const bid = priceAt(a, now() + 2) + 2_000n
    await h.program.methods
      .placeBid(0, new BN(bid.toString()))
      .accounts(placeBidAccounts(h, 0, alice.publicKey))
      .signers([alice])
      .rpc()

    const outgoing = (await asset(0)).holder
    const outgoingBefore = await encBalance(outgoing)
    const supplyBefore = await h.supply()
    const term = big((await asset(0)).termNumber)

    await waitOutTerm(0)
    await h.program.methods
      .settleAuction(0)
      .accounts(settleAccounts(h, 0, alice.publicKey, outgoing))
      .rpc()

    const after = await asset(0)
    expect(after.holder.toBase58(), 'the winner did not get the tenancy').to.equal(
      alice.publicKey.toBase58(),
    )
    expect(await encBalance(outgoing), '100% of the bid did not reach the outgoing holder').to.equal(
      outgoingBefore + bid,
    )
    expect(big(after.highBid)).to.equal(0n)
    expect(big(after.termNumber)).to.equal(term + 1n)
    expect(await h.supply(), 'the auction moved the money supply').to.equal(supplyBefore)
    // The winner's escrow record is gone, its rent returned.
    expect(await h.exists(h.bidPda(0, alice.publicKey))).to.equal(false)
  })

  it('lets a superseded bidder recover their escrow in full', async () => {
    const a = await freshTerm(2)
    const first = priceAt(a, now() + 2) + 1_000n
    await h.program.methods
      .placeBid(2, new BN(first.toString()))
      .accounts(placeBidAccounts(h, 2, alice.publicKey))
      .signers([alice])
      .rpc()

    // While she is the standing high bid, the escrow is locked — the one lock
    // in the program, and it expires by itself when the term does.
    const locked = await h.failureOf(() =>
      h.program.methods
        .withdrawBid(2)
        .accounts(withdrawBidAccounts(h, 2, alice.publicKey))
        .signers([alice])
        .rpc(),
    )
    expect(locked, 'the standing high bid was withdrawable').to.match(/BidIsStanding/)

    await h.program.methods
      .placeBid(2, new BN((first + 500n).toString()))
      .accounts(placeBidAccounts(h, 2, bob.publicKey))
      .signers([bob])
      .rpc()

    const aliceBefore = await encBalance(alice.publicKey)
    await h.program.methods
      .withdrawBid(2)
      .accounts(withdrawBidAccounts(h, 2, alice.publicKey))
      .signers([alice])
      .rpc()
    expect(await encBalance(alice.publicKey), 'a superseded bidder lost money').to.equal(
      aliceBefore + first,
    )
  })

  it('releases a stale high bid at a no-winner rollover, recoverable in full', async function () {
    this.timeout(120_000)
    const i = 3
    const a = await freshTerm(i)
    // Exactly the reserve: any upward price move leaves this bid underwater.
    const bid = priceAt(a, now() + 2)
    await h.program.methods
      .placeBid(i, new BN(bid.toString()))
      .accounts(placeBidAccounts(h, i, bob.publicKey))
      .signers([bob])
      .rpc()

    // The Fed prints, every price rescales upward, and the reserve climbs away
    // from a bid that qualified when it was placed. This is the *expected*
    // state of the design, not an exotic one — ~94% of months move this way.
    const printer = await h.program.account.printer.fetch(h.printerPda)
    await setMockM2(h, big(printer.m2Value) + big(printer.m2Value) / 100n, Number(printer.m2ReleaseDate) + 86_400)
    await h.program.methods.syncM2().accounts(syncAccounts(h)).remainingAccounts(assetMetas(h)).rpc()

    await waitOutTerm(i)

    const stillHolder = (await asset(i)).holder
    const cantSettle = await h.failureOf(() =>
      h.program.methods.settleAuction(i).accounts(settleAccounts(h, i, bob.publicKey, stillHolder)).rpc(),
    )
    expect(cantSettle, 'an underwater bid won the asset').to.match(/NoQualifyingBid/)

    await h.program.methods.rollTerm(i).accounts({ asset: h.assetPda(i) }).rpc()
    const after = await asset(i)
    expect(after.holder.toBase58(), 'a no-winner rollover moved the asset').to.equal(
      stillHolder.toBase58(),
    )
    expect(big(after.highBid), 'the stale bid was not released').to.equal(0n)

    const bobBefore = await encBalance(bob.publicKey)
    await h.program.methods
      .withdrawBid(i)
      .accounts(withdrawBidAccounts(h, i, bob.publicKey))
      .signers([bob])
      .rpc()
    expect(await encBalance(bob.publicKey), 'stranded escrow').to.equal(bobBefore + bid)
  })

  it('settles even when the outgoing holder has closed their ENC account', async function () {
    this.timeout(120_000)
    const i = 4
    // Alice takes the tenancy first, so there is a real wallet to evict.
    let a = await freshTerm(i)
    let bid = priceAt(a, now() + 2) + 1_000n
    await h.program.methods
      .placeBid(i, new BN(bid.toString()))
      .accounts(placeBidAccounts(h, i, alice.publicKey))
      .signers([alice])
      .rpc()
    await waitOutTerm(i)
    await h.program.methods
      .settleAuction(i)
      .accounts(settleAccounts(h, i, alice.publicKey, (await asset(i)).holder))
      .rpc()

    // Now Bob bids, and Alice closes her ENC account to try to freeze it.
    a = await freshTerm(i)
    bid = priceAt(a, now() + 2) + 1_000n
    await h.program.methods
      .placeBid(i, new BN(bid.toString()))
      .accounts(placeBidAccounts(h, i, bob.publicKey))
      .signers([bob])
      .rpc()
    await closeAccount(
      h.connection,
      alice,
      h.encAta(alice.publicKey),
      alice.publicKey,
      alice,
      [],
      undefined,
      TOKEN_PROGRAM_ID,
    )
    expect(await h.exists(h.encAta(alice.publicKey)), 'the veto account survived').to.equal(false)

    await waitOutTerm(i)
    await h.program.methods
      .settleAuction(i)
      .accounts(settleAccounts(h, i, bob.publicKey, alice.publicKey))
      .rpc()

    expect((await asset(i)).holder.toBase58(), 'an incumbent vetoed their own eviction').to.equal(
      bob.publicKey.toBase58(),
    )
    expect(await encBalance(alice.publicKey), 'the recreated account was not paid').to.equal(bid)
  })

  it('lets the incumbent defend with a self-bid, paying themselves', async function () {
    this.timeout(120_000)
    const i = 4 // Bob holds it from the previous case.
    const a = await freshTerm(i)
    expect((await asset(i)).holder.toBase58()).to.equal(bob.publicKey.toBase58())

    const bid = priceAt(a, now() + 2) + 1_000n
    const before = await encBalance(bob.publicKey)
    await h.program.methods
      .placeBid(i, new BN(bid.toString()))
      .accounts(placeBidAccounts(h, i, bob.publicKey))
      .signers([bob])
      .rpc()
    await waitOutTerm(i)
    await h.program.methods
      .settleAuction(i)
      .accounts(settleAccounts(h, i, bob.publicKey, bob.publicKey))
      .rpc()

    expect((await asset(i)).holder.toBase58(), 'a self-bid lost the asset').to.equal(
      bob.publicKey.toBase58(),
    )
    // Paid himself: the escrow came back, so defending costs only the fee.
    expect(await encBalance(bob.publicKey), 'a self-bid was not made whole').to.equal(before)
  })

  // ── The certificate ───────────────────────────────────────────────────────

  it('issues an immutable certificate to the holder, and never takes it back', async function () {
    this.timeout(120_000)
    const i = 5
    const a = await freshTerm(i)
    const bid = priceAt(a, now() + 2) + 1_000n
    await h.program.methods
      .placeBid(i, new BN(bid.toString()))
      .accounts(placeBidAccounts(h, i, alice.publicKey))
      .signers([alice])
      .rpc()
    await waitOutTerm(i)
    await h.program.methods
      .settleAuction(i)
      .accounts(settleAccounts(h, i, alice.publicKey, (await asset(i)).holder))
      .rpc()

    const term = big((await asset(i)).termNumber)
    await h.program.methods
      .mintCertificate(i, new BN(term.toString()))
      .accounts(certAccounts(h, i, term, alice.publicKey))
      .rpc()

    const certMint = h.certPda(i, term)
    const certAta = PublicKey.findProgramAddressSync(
      [alice.publicKey.toBuffer(), TOKEN_2022_PROGRAM_ID.toBuffer(), certMint.toBuffer()],
      ATA_PROGRAM,
    )[0]
    expect((await getAccount(h.connection, certAta, undefined, TOKEN_2022_PROGRAM_ID)).amount).to.equal(
      1n,
    )

    // Immutable at issue, structurally: nothing can print another, freeze it,
    // or rewrite what it says.
    const mint = await getMint(h.connection, certMint, undefined, TOKEN_2022_PROGRAM_ID)
    expect(mint.mintAuthority, 'the certificate can be reprinted').to.be.null
    expect(mint.freezeAuthority, 'the certificate can be frozen').to.be.null
    const meta = await getTokenMetadata(h.connection, certMint, undefined, TOKEN_2022_PROGRAM_ID)
    expect(meta?.updateAuthority ?? null, 'the certificate can be rewritten').to.be.null
    expect(meta?.name).to.contain(`Term ${term}`)

    // A second issue of the same term is impossible.
    const twice = await h.failureOf(() =>
      h.program.methods
        .mintCertificate(i, new BN(term.toString()))
        .accounts(certAccounts(h, i, term, alice.publicKey))
        .rpc(),
    )
    expect(twice, 'a term issued two certificates').to.not.equal('')

    // Settle a further term away from her and the clipping is untouched.
    const next = await freshTerm(i)
    const bid2 = priceAt(next, now() + 2) + 1_000n
    await h.program.methods
      .placeBid(i, new BN(bid2.toString()))
      .accounts(placeBidAccounts(h, i, bob.publicKey))
      .signers([bob])
      .rpc()
    await waitOutTerm(i)
    await h.program.methods
      .settleAuction(i)
      .accounts(settleAccounts(h, i, bob.publicKey, alice.publicKey))
      .rpc()

    expect((await asset(i)).holder.toBase58()).to.equal(bob.publicKey.toBase58())
    expect(
      (await getAccount(h.connection, certAta, undefined, TOKEN_2022_PROGRAM_ID)).amount,
      'a previous holder lost their certificate',
    ).to.equal(1n)
  })

  it('issues no certificate for a tenancy the Emperor holds', async () => {
    const i = 9 // Never auctioned in this suite.
    const a = await asset(i)
    expect(a.holder.toBase58(), 'asset 9 was expected to be unsold').to.equal(h.vaultPda.toBase58())
    const why = await h.failureOf(() =>
      h.program.methods
        .mintCertificate(i, new BN(big(a.termNumber).toString()))
        .accounts(certAccounts(h, i, big(a.termNumber), h.vaultPda))
        .rpc(),
    )
    expect(why, 'the Emperor was issued a receipt').to.match(/NoCertificateDue/)
  })
})
