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
  transfer,
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
  ASSET_COUNT,
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
  // Carol exists only to close her own ENC account mid-test, which needs a
  // zero balance — doing that to Alice would strand every later case.
  const carol = Keypair.generate()

  const asset = (i: number) => h.program.account.asset.fetch(h.assetPda(i))

  /**
   * The **validator's** clock, not this machine's.
   *
   * `Clock::get()` is the only clock the program has, and a local validator's
   * unix time drifts behind wall time as slots slip. Deciding "the term has
   * ended" from `Date.now()` gets `TermNotEnded` back from a chain that has not
   * caught up yet — which looks exactly like a program bug and is not one.
   */
  const now = async (): Promise<number> => {
    const slot = await h.history.getSlot()
    return (await h.history.getBlockTime(slot)) ?? Math.floor(Date.now() / 1000)
  }
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
      const t = await now()
      if (t < Number(a.termEndsAt) - 3) return a

      const reserve = priceAt(a, t + 1)
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

  /**
   * The smallest bid that clears both floors right now: the reserve, and the
   * standing high bid. Re-read rather than passed in, because an earlier case
   * in this suite may have left a bid standing on the same asset.
   */
  async function nextBid(i: number, extra = 0n) {
    const a = await asset(i)
    const reserve = priceAt(a, (await now()) + 2)
    const floor = big(a.highBid) + 1n
    // The margin is a *fraction of the price*, not a flat number of base
    // units. The reserve climbs for the whole term after any sync, so a bid
    // that only just clears it now can be underwater by settlement — which is
    // the real mechanism (and its own test), not something to trip over here.
    // A hundredth of a percent covers a full term of creep many times over.
    return (reserve > floor ? reserve : floor) + reserve / 10_000n + extra
  }

  /** Wait out the current term, by the chain's reckoning, not this machine's. */
  async function waitOutTerm(i: number) {
    const endsAt = Number((await asset(i)).termEndsAt)
    for (let i = 0; i < 60; i++) {
      const t = await now()
      if (t >= endsAt) return
      await sleep(Math.min((endsAt - t) * 1000 + 500, 5_000))
    }
    throw new Error('the validator clock never reached the end of the term')
  }

  before(async function () {
    this.timeout(180_000)
    await bootstrap(h)

    for (const who of [alice, bob, carol]) {
      const sig = await h.connection.requestAirdrop(who.publicKey, 5 * LAMPORTS_PER_SOL)
      await h.history.confirmTransaction(sig, 'confirmed')
    }
    // The dearest asset costs ten times the cheapest and several cases bid on
    // one twice, so stake against the top of the range rather than the bottom.
    // The vault is the only source of ENC until T13's faucet exists.
    const stake = big((await asset(ASSET_COUNT - 1)).priceTo) * 6n
    for (const who of [alice, bob, carol]) await mockFund(h, who.publicKey, stake)
  })

  // ── Bidding ───────────────────────────────────────────────────────────────

  it('refuses a bid below what M2 says the asset is worth', async () => {
    // Asset 7 is never successfully bid on anywhere in this suite, so it can
    // never carry a standing high bid that would fail this for another reason.
    const a = await freshTerm(7)
    // One percent under, not one base unit under. After any sync the price is
    // interpolating, so the reserve the program checks a second from now is not
    // the one read here — and `price - 1` lands *above* a rising reserve read
    // slightly ahead. A percent is far more than a curve moves in seconds
    // (30 days to travel), so this is below the reserve whichever way it runs.
    const at = priceAt(a, (await now()) + 60)
    const under = at - at / 100n
    const why = await h.failureOf(() =>
      h.program.methods
        .placeBid(7, new BN(under.toString()))
        .accounts(placeBidAccounts(h, 7, alice.publicKey))
        .signers([alice])
        .rpc(),
    )
    expect(why, 'a bid under the reserve was accepted').to.match(/BidBelowReserve/)
  })

  it('escrows a qualifying bid, and refuses one that only ties it', async () => {
    await freshTerm(0)
    const bid = await nextBid(0)

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
    await freshTerm(0)
    const first = await nextBid(0, 5_000n)
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
    await freshTerm(1)
    const bid = await nextBid(1)
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
    await freshTerm(0)
    const bid = await nextBid(0)
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
    await freshTerm(0)
    const bid = await nextBid(0, 2_000n)
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
    await freshTerm(2)
    const first = await nextBid(2)
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
    const bid = priceAt(a, (await now()) + 2)
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
    // Carol takes the tenancy first, so there is a real wallet to evict — and
    // she is the only wallet this suite can safely empty.
    await freshTerm(i)
    await h.program.methods
      .placeBid(i, new BN((await nextBid(i)).toString()))
      .accounts(placeBidAccounts(h, i, carol.publicKey))
      .signers([carol])
      .rpc()
    await waitOutTerm(i)
    await h.program.methods
      .settleAuction(i)
      .accounts(settleAccounts(h, i, carol.publicKey, (await asset(i)).holder))
      .rpc()
    expect((await asset(i)).holder.toBase58()).to.equal(carol.publicKey.toBase58())

    // Bob bids, and Carol tries the classic push-payment veto: close the
    // account the payment has to land in, and settlement can never run.
    await freshTerm(i)
    const bid = await nextBid(i)
    await h.program.methods
      .placeBid(i, new BN(bid.toString()))
      .accounts(placeBidAccounts(h, i, bob.publicKey))
      .signers([bob])
      .rpc()

    // An account can only be closed empty, so she moves her ENC out first —
    // which is exactly what someone doing this deliberately would do.
    const left = await encBalance(carol.publicKey)
    if (left > 0n) {
      await transfer(
        h.connection,
        carol,
        h.encAta(carol.publicKey),
        h.encAta(bob.publicKey),
        carol,
        left,
        [],
        undefined,
        TOKEN_PROGRAM_ID,
      )
    }
    await closeAccount(
      h.connection,
      carol,
      h.encAta(carol.publicKey),
      carol.publicKey,
      carol,
      [],
      undefined,
      TOKEN_PROGRAM_ID,
    )
    expect(await h.exists(h.encAta(carol.publicKey)), 'the veto account survived').to.equal(false)

    await waitOutTerm(i)
    await h.program.methods
      .settleAuction(i)
      .accounts(settleAccounts(h, i, bob.publicKey, carol.publicKey))
      .rpc()

    expect((await asset(i)).holder.toBase58(), 'an incumbent vetoed their own eviction').to.equal(
      bob.publicKey.toBase58(),
    )
    expect(await encBalance(carol.publicKey), 'the recreated account was not paid').to.equal(bid)
  })

  it('lets the incumbent defend with a self-bid, paying themselves', async function () {
    this.timeout(120_000)
    const i = 4 // Bob holds it from the previous case.
    await freshTerm(i)
    expect((await asset(i)).holder.toBase58()).to.equal(bob.publicKey.toBase58())

    const bid = await nextBid(i)
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
    await freshTerm(i)
    const bid = await nextBid(i)
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
    await freshTerm(i)
    const bid2 = await nextBid(i)
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
