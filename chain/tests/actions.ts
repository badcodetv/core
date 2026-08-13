/**
 * T20: everything the ENC page asks a wallet to sign, against a real validator.
 *
 * **This suite exists because the page cannot be tested where it lives.** The
 * acceptance criteria are a two-wallet Phantom run-through, and a browser
 * extension cannot be driven here — so every instruction the page sends is sent
 * from this file instead, through the *same* account maps
 * (`@badcode/enc`'s `actions.ts`) and checked against the *same* predictions
 * (`claimView`, `bidView`, `withdrawView`). A derivation that drifts fails here
 * rather than in somebody's wallet, which is the only place it would otherwise
 * show up.
 *
 * The other suites prove the program. This one proves the client: that the
 * addresses resolve, that the amounts are what the page said they would be, and
 * that every refusal a person can reach by clicking comes back as a sentence
 * instead of a hex code.
 *
 * It runs the ticket's whole loop in order — claim, claim again for a share,
 * bid, outbid, withdraw in full, settle from an uninvolved third wallet,
 * certificate to the winner, file once and be refused twice.
 *
 * Slots 5 and 6 are used here because nothing else does: `auction.ts` works on
 * 0, 1, 2 and 7, `gazette.ts` on 3 and 9, `sync_m2.ts` on 0.
 */
import { expect } from 'chai'
import {
  Keypair,
  LAMPORTS_PER_SOL,
  PublicKey,
  Transaction,
  sendAndConfirmTransaction,
} from '@solana/web3.js'
import { TOKEN_2022_PROGRAM_ID, getAccount, getMint } from '@solana/spl-token'

import {
  assetView,
  bidView,
  claimAccounts,
  claimView,
  encAddresses,
  encErrorMessage,
  fileCopyAccounts,
  mintCertificateAccounts,
  placeBidAccounts,
  rollTermAccounts,
  settleAuctionAccounts,
  withdrawBidAccounts,
  withdrawView,
} from '@badcode/enc'

import {
  BN,
  EPOCH_SECONDS,
  big,
  bootstrap,
  harness,
  mockFund,
  readCopy,
} from './enc-harness.js'

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms))

/** Chai's ordering assertions reject a BigInt; every amount here is one. */
const above = (actual: bigint, bound: bigint, what: string) =>
  expect(actual > bound, `${what}: ${actual} <= ${bound}`).to.equal(true)

/** The auction slot, and the one used for the no-bid path. */
const SLOT = 5
const DORMANT = 6

describe('T20: the actions the page sends', () => {
  const h = harness()
  const addresses = encAddresses(h.program.programId)

  // Alice bids, Bob outbids, Carol settles without ever having been involved —
  // which is the point of settlement being permissionless.
  const alice = Keypair.generate()
  const bob = Keypair.generate()
  const carol = Keypair.generate()

  const asset = (i: number) => h.program.account.asset.fetch(h.assetPda(i))
  const config = () => h.program.account.config.fetch(h.configPda)

  const encBalance = async (owner: PublicKey) =>
    (await h.exists(h.encAta(owner)))
      ? BigInt((await getAccount(h.connection, h.encAta(owner))).amount.toString())
      : 0n

  const supply = async () => BigInt((await h.connection.getTokenSupply(h.mintPda)).value.amount)

  /**
   * The page's own view of a slot, from the accounts the page subscribes to.
   *
   * Deliberately built with `assetView` rather than read field by field: that
   * function is what decides which button the browser draws, so anything
   * asserted here is asserted about the real decision.
   */
  const slotView = async (i: number) => assetView(await asset(i), h.vaultPda, await h.chainNow())

  /** Everything `claimView` needs, read live. */
  async function predictClaim(who: PublicKey) {
    const t = await h.chainNow()
    const epoch = BigInt(Math.floor(t / EPOCH_SECONDS))
    const read = async (pda: PublicKey) =>
      (await h.exists(pda)) ? await h.program.account.faucetEpoch.fetch(pda) : null
    return {
      epoch,
      view: claimView({
        epoch,
        config: (await config()) as never,
        player: (await h.exists(h.playerPda(who)))
          ? ((await h.program.account.player.fetch(h.playerPda(who))) as never)
          : null,
        current: (await read(h.epochPda(epoch))) as never,
        previous: epoch > 0n ? ((await read(h.epochPda(epoch - 1n))) as never) : null,
        supply: await supply(),
        vaultBalance: await h.vaultBalance(),
      }),
    }
  }

  /** Claim exactly as the page does, including the optional previous epoch. */
  async function claim(who: Keypair, epoch: bigint) {
    const previousPda = epoch > 0n ? addresses.epoch(epoch - 1n) : null
    const previous = previousPda && (await h.exists(previousPda)) ? previousPda : null
    return h.program.methods
      .claim(new BN(epoch.toString()) as never)
      .accounts(claimAccounts(addresses, who.publicKey, epoch, previous))
      .signers([who])
      .rpc()
  }

  /** Sit until we are early inside a clean epoch, by the validator's clock. */
  async function freshEpoch(): Promise<bigint> {
    for (let attempt = 0; attempt < 40; attempt++) {
      const t = await h.chainNow()
      const into = t % EPOCH_SECONDS
      if (into <= EPOCH_SECONDS * 0.4) return BigInt(Math.floor(t / EPOCH_SECONDS))
      await sleep((EPOCH_SECONDS - into) * 1_000 + 400)
    }
    throw new Error('the validator clock never reached a clean epoch')
  }

  async function waitPastEpoch(epoch: bigint) {
    for (let attempt = 0; attempt < 40; attempt++) {
      if (BigInt(Math.floor((await h.chainNow()) / EPOCH_SECONDS)) > epoch) return
      await sleep(1_500)
    }
    throw new Error(`the validator clock never left epoch ${epoch}`)
  }

  /**
   * Bring a slot to the start of a live term, whichever permissionless call it
   * qualifies for — which is also the first proof that `nextAction` picks the
   * right one, since choosing wrong is an immediate refusal.
   */
  async function freshTerm(i: number) {
    for (let attempt = 0; attempt < 5; attempt++) {
      const v = await slotView(i)
      if (!v.termEnded && v.secondsToTermEnd > 3) return v
      if (v.nextAction === 'settle' && v.highBidder) {
        await h.program.methods
          .settleAuction(i)
          .accounts(settleAuctionAccounts(addresses, i, v.highBidder, v.holder, h.authority))
          .rpc()
      } else {
        await h.program.methods.rollTerm(i).accounts(rollTermAccounts(addresses, i)).rpc()
      }
    }
    throw new Error(`slot ${i} would not settle into a fresh term`)
  }

  async function waitOutTerm(i: number) {
    const endsAt = (await slotView(i)).termEndsAt
    for (let attempt = 0; attempt < 60; attempt++) {
      const t = await h.chainNow()
      if (t >= endsAt) return
      await sleep(Math.min((endsAt - t) * 1_000 + 500, 5_000))
    }
    throw new Error('the validator clock never reached the end of the term')
  }

  /**
   * The minimum the page would offer, plus a margin.
   *
   * The margin is a fraction of the price rather than a flat number of units:
   * the reserve climbs for a whole term after any sync, so a bid that only just
   * clears it now can be under it by the time the transaction lands. That is
   * the coin's real mechanism and has its own case below; it is not something
   * to trip over while setting one up.
   */
  async function opening(i: number, of: PublicKey, bid = null as never) {
    const v = await slotView(i)
    const min = bidView(v, of, bid).minimum
    return min + min / 10_000n
  }

  before(async function () {
    this.timeout(240_000)
    await bootstrap(h)

    for (const who of [alice, bob, carol]) {
      const sig = await h.connection.requestAirdrop(who.publicKey, 5 * LAMPORTS_PER_SOL)
      await h.history.confirmTransaction(sig, 'confirmed')
    }
    // Alice and Bob have to be able to outbid each other on the same column
    // several times over. Carol deliberately gets no ENC at all: settlement
    // must cost her nothing but a fee.
    const stake = big((await asset(SLOT)).priceTo) * 8n
    for (const who of [alice, bob]) await mockFund(h, who.publicKey, stake)
  })

  // ── The faucet ────────────────────────────────────────────────────────────

  describe('the faucet, as the page explains it', () => {
    let registered: bigint

    it('pays a first-ever claimant the welcome grant and no share', async function () {
      this.timeout(120_000)
      registered = await freshEpoch()
      const before = await encBalance(carol.publicKey)
      const { view } = await predictClaim(carol.publicKey)

      // The single most confusing thing on the page: register today, collect
      // tomorrow. A first claim pays the grant only.
      expect(view.case, 'a never-seen wallet was not read as first-ever').to.equal('first-ever')
      expect(view.share.toString()).to.equal('0')
      above(view.grant, 0n, 'the welcome grant')

      await claim(carol, registered)
      const paid = (await encBalance(carol.publicKey)) - before
      expect(paid.toString(), 'the page predicted the wrong payout').to.equal(view.total.toString())
    })

    it('refuses a second claim in the same epoch, in English', async () => {
      const { view } = await predictClaim(carol.publicKey)
      expect(view.case).to.equal('already-claimed')
      expect(view.claimable, 'the page offered a claim the program refuses').to.equal(false)

      const why = await h.failureOf(() => claim(carol, registered))
      expect(why).to.match(/AlreadyClaimedThisEpoch/)
      const said = encErrorMessage(why)
      expect(said, 'the refusal did not map to a sentence').to.be.a('string')
      expect(said).to.match(/already claimed/i)
      expect(said, 'a raw error name reached the page').to.not.match(/AlreadyClaimedThisEpoch/)
    })

    it('pays a share of the previous epoch’s pot on the next claim', async function () {
      this.timeout(120_000)
      await waitPastEpoch(registered)
      const next = BigInt(Math.floor((await h.chainNow()) / EPOCH_SECONDS))

      const before = await encBalance(carol.publicKey)
      const { view } = await predictClaim(carol.publicKey)
      expect(view.case, 'a returning claimant was not offered their share').to.equal('share-due')
      above(view.share, 0n, 'the share of yesterday’s pot')

      await claim(carol, next)
      const paid = (await encBalance(carol.publicKey)) - before
      expect(paid.toString(), 'the share the page promised is not what arrived').to.equal(
        view.total.toString(),
      )
    })

    it('names the wrong epoch the way a transaction that straddles one would', async () => {
      // The epoch is an argument because a PDA seed cannot read the clock, and
      // the program checks it rather than trusting it. A person only ever meets
      // this by sitting on a boundary, so it is worth having a sentence ready.
      const wrong = BigInt(Math.floor((await h.chainNow()) / EPOCH_SECONDS)) + 5n
      const why = await h.failureOf(() => claim(alice, wrong))
      expect(why).to.match(/WrongEpoch/)
      expect(encErrorMessage(why)).to.match(/epoch turned over|not the epoch/i)
    })
  })

  // ── The auction ───────────────────────────────────────────────────────────

  describe('the auction, from the page’s buttons', () => {
    let aliceBid: bigint
    let bobBid: bigint

    it('escrows a bid at the minimum the page computed', async function () {
      this.timeout(120_000)
      await freshTerm(SLOT)
      aliceBid = await opening(SLOT, alice.publicKey)

      const before = await encBalance(alice.publicKey)
      await h.program.methods
        .placeBid(SLOT, new BN(aliceBid.toString()) as never)
        .accounts(placeBidAccounts(addresses, SLOT, alice.publicKey))
        .signers([alice])
        .rpc()

      expect(((await encBalance(alice.publicKey)) - before).toString()).to.equal(
        (-aliceBid).toString(),
      )
      const v = await slotView(SLOT)
      expect(v.highBidder?.toBase58()).to.equal(alice.publicKey.toBase58())
      expect(v.highBid.toString()).to.equal(aliceBid.toString())
    })

    it('refuses a bid that only ties, and says ties lose', async () => {
      const why = await h.failureOf(() =>
        h.program.methods
          .placeBid(SLOT, new BN(aliceBid.toString()) as never)
          .accounts(placeBidAccounts(addresses, SLOT, bob.publicKey))
          .signers([bob])
          .rpc(),
      )
      expect(why).to.match(/BidNotHighEnough/)
      expect(encErrorMessage(why)).to.match(/Ties lose/i)
    })

    it('refuses a bid under the reserve, and says the reserve moves', async () => {
      const v = await slotView(SLOT)
      // A percent under, not a base unit: the reserve is interpolating, so a
      // figure one unit below the price read here can land above the one the
      // program reads a moment later.
      const under = v.price - v.price / 100n
      const why = await h.failureOf(() =>
        h.program.methods
          .placeBid(SLOT, new BN(under.toString()) as never)
          .accounts(placeBidAccounts(addresses, SLOT, bob.publicKey))
          .signers([bob])
          .rpc(),
      )
      expect(why).to.match(/BidBelowReserve/)
      expect(encErrorMessage(why)).to.match(/under the reserve/i)
    })

    it('refuses to withdraw the standing bid — and the page says it is not stuck', async () => {
      const v = await slotView(SLOT)
      const w = withdrawView(v, alice.publicKey, await bidAccount(SLOT, alice.publicKey))
      expect(w.withdrawable, 'the page offered a withdrawal the program locks').to.equal(false)
      expect(w.fromEarlierTerm).to.equal(false)

      const why = await h.failureOf(() => withdraw(alice))
      expect(why).to.match(/BidIsStanding/)
      // The sentence has to carry the way out, because "my money is stuck" is
      // the question and the answer is "anyone can settle it, including you".
      expect(encErrorMessage(why)).to.match(/settles|anyone/i)
    })

    it('lets a second wallet outbid the first', async () => {
      bobBid = await opening(SLOT, bob.publicKey)
      above(bobBid, aliceBid, 'the outbid')
      await h.program.methods
        .placeBid(SLOT, new BN(bobBid.toString()) as never)
        .accounts(placeBidAccounts(addresses, SLOT, bob.publicKey))
        .signers([bob])
        .rpc()

      const v = await slotView(SLOT)
      expect(v.highBidder?.toBase58()).to.equal(bob.publicKey.toBase58())
    })

    it('returns the outbid escrow in full', async () => {
      const v = await slotView(SLOT)
      const w = withdrawView(v, alice.publicKey, await bidAccount(SLOT, alice.publicKey))
      expect(w.withdrawable, 'an outbid bid was still reported as locked').to.equal(true)
      expect(w.amount.toString()).to.equal(aliceBid.toString())

      const before = await encBalance(alice.publicKey)
      await withdraw(alice)
      expect(
        ((await encBalance(alice.publicKey)) - before).toString(),
        'the refund was not the whole bid',
      ).to.equal(aliceBid.toString())
      expect(await h.exists(addresses.bid(SLOT, alice.publicKey))).to.equal(false)
    })

    it('settles from a third wallet that was never involved', async function () {
      this.timeout(120_000)
      await waitOutTerm(SLOT)
      const v = await slotView(SLOT)
      expect(v.nextAction, 'the page would have offered the wrong call').to.equal('settle')

      const outgoing = v.holder
      const paidTo = await encBalance(outgoing)
      const carolBefore = await encBalance(carol.publicKey)

      await h.program.methods
        .settleAuction(SLOT)
        .accounts(settleAuctionAccounts(addresses, SLOT, bob.publicKey, outgoing, carol.publicKey))
        .signers([carol])
        .rpc()

      const after = await slotView(SLOT)
      expect(after.holder.toBase58(), 'the winner did not get the column').to.equal(
        bob.publicKey.toBase58(),
      )
      expect(after.highBid.toString()).to.equal('0')
      // Carol paid a fee and possibly an account rent, and received no ENC.
      expect((await encBalance(carol.publicKey)).toString()).to.equal(carolBefore.toString())
      if (!outgoing.equals(h.vaultPda)) {
        expect(((await encBalance(outgoing)) - paidTo).toString()).to.equal(bobBid.toString())
      }
    })

    it('mints the certificate into the holder’s wallet, paid for by someone else', async () => {
      const v = await slotView(SLOT)
      const certMint = addresses.cert(SLOT, v.termNumber)
      const holderAta = PublicKey.findProgramAddressSync(
        [v.holder.toBuffer(), TOKEN_2022_PROGRAM_ID.toBuffer(), certMint.toBuffer()],
        new PublicKey('ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL'),
      )[0]

      await h.program.methods
        .mintCertificate(SLOT, new BN(v.termNumber.toString()) as never)
        // Carol pays; it lands in Bob's wallet, because it always does.
        .accounts(
          mintCertificateAccounts(addresses, SLOT, v.termNumber, v.holder, carol.publicKey),
        )
        .signers([carol])
        .rpc()

      const account = await getAccount(h.connection, holderAta, undefined, TOKEN_2022_PROGRAM_ID)
      expect(account.amount.toString(), 'the certificate did not land with the holder').to.equal('1')
      expect(account.owner.toBase58()).to.equal(v.holder.toBase58())
      // Supply of one, mint authority dropped: it can never be reissued.
      const mint = await getMint(h.connection, certMint, undefined, TOKEN_2022_PROGRAM_ID)
      expect(mint.supply.toString()).to.equal('1')
      expect(mint.mintAuthority).to.equal(null)
    })

    it('rolls a term nobody bid on, with no signer of its own', async function () {
      this.timeout(120_000)
      await freshTerm(DORMANT)
      await waitOutTerm(DORMANT)

      const v = await slotView(DORMANT)
      expect(v.nextAction, 'a slot with no bid was offered settlement').to.equal('roll')
      const holder = v.holder.toBase58()

      // **`roll_term` takes no signer at all**, so `.signers([carol])` is not
      // how a stranger runs it — web3.js rejects the extra signature outright
      // ("unknown signer"), because nothing in the instruction requires her.
      // What a stranger actually does, and what the page does, is pay the fee:
      // the transaction's fee payer signs and the instruction asks nothing of
      // anyone. Carol holds no ENC and has never touched this column.
      const instruction = await h.program.methods
        .rollTerm(DORMANT)
        .accounts(rollTermAccounts(addresses, DORMANT))
        .instruction()
      const tx = new Transaction().add(instruction)
      tx.feePayer = carol.publicKey
      await sendAndConfirmTransaction(h.history, tx, [carol], { commitment: 'confirmed' })

      const after = await slotView(DORMANT)
      expect(after.termNumber.toString()).to.equal((v.termNumber + 1n).toString())
      expect(after.holder.toBase58(), 'a dormant column changed hands').to.equal(holder)
    })

    it('refuses to end a term early, in English', async function () {
      this.timeout(120_000)
      // Nobody gets to end one early, including us — so the page has to be able
      // to say that rather than showing a code.
      const v = await freshTerm(DORMANT)
      expect(v.termEnded).to.equal(false)
      const early = await h.failureOf(() =>
        h.program.methods
          .rollTerm(DORMANT)
          .accounts(rollTermAccounts(addresses, DORMANT))
          .rpc(),
      )
      expect(early).to.match(/TermNotEnded/)
      expect(encErrorMessage(early)).to.match(/not ended yet/i)
    })
  })

  // ── The Gazette ───────────────────────────────────────────────────────────

  describe('the tenant’s one filing', () => {
    it('files once and refuses the second, naming the right reason', async function () {
      this.timeout(120_000)
      const v = await slotView(SLOT)
      if (v.heldByEmperor) this.skip()

      // Whoever ended up holding it after settlement — Bob, unless an earlier
      // suite left this ledger somewhere unexpected.
      const tenant = v.holder.equals(bob.publicKey) ? bob : alice
      if (!v.holder.equals(tenant.publicKey)) this.skip()
      if (v.copyFiled || v.spiked) await freshTerm(SLOT)

      const text = 'THE EMPEROR HAS NOTHING TO SAY — cont. p.94'
      await h.program.methods
        .fileCopy(SLOT, text)
        .accounts(fileCopyAccounts(addresses, SLOT, tenant.publicKey))
        .signers([tenant])
        .rpc()
      expect(readCopy(await asset(SLOT))).to.equal(text)

      const again = await h.failureOf(() =>
        h.program.methods
          .fileCopy(SLOT, 'and again')
          .accounts(fileCopyAccounts(addresses, SLOT, tenant.publicKey))
          .signers([tenant])
          .rpc(),
      )
      expect(again).to.match(/AlreadyFiled/)
      expect(encErrorMessage(again)).to.match(/One filing per term/i)

      const stranger = await h.failureOf(() =>
        h.program.methods
          .fileCopy(SLOT, 'mine now')
          .accounts(fileCopyAccounts(addresses, SLOT, carol.publicKey))
          .signers([carol])
          .rpc(),
      )
      expect(stranger).to.match(/NotTheTenant/)
      expect(encErrorMessage(stranger)).to.match(/do not hold this column/i)
    })
  })

  // ── Helpers that need the harness ─────────────────────────────────────────

  async function bidAccount(i: number, who: PublicKey) {
    const pda = addresses.bid(i, who)
    return (await h.exists(pda))
      ? ((await h.program.account.bid.fetch(pda)) as never)
      : null
  }

  function withdraw(who: Keypair) {
    return h.program.methods
      .withdrawBid(SLOT)
      .accounts(withdrawBidAccounts(addresses, SLOT, who.publicKey))
      .signers([who])
      .rpc()
  }
})
