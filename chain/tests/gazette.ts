/**
 * The Imperial Gazette — the tenant's column, and the editor's pen.
 *
 * The ten assets are the ten slots of a newspaper front page. Whoever holds a
 * tenancy writes that slot **once per term**, and the editor may strike any
 * slot to a fixed redaction marker **once per term**. The property every case
 * here defends is the two-part claim the program makes about itself: **no key
 * over the money; one pen over the words.** A stolen pen vandalises ten columns
 * a month and cannot move a single token, which is asserted twice over — as a
 * shape test against the IDL in `initialize.ts`, and as balances that do not
 * budge at the bottom of this file.
 *
 * **The last case is one-way.** `break_the_pen` is irrevocable by design, so
 * once it passes, this ledger has no editor and the pen cases below skip
 * themselves on a re-run rather than passing for the wrong reason. That is the
 * same bargain `retire.ts` makes, but cheaper: nothing outside this suite uses
 * the pen, so the run-everything script keeps this file. **`./stack reset`** if
 * you want the pen cases back.
 *
 * Terms run for `TERM_SECONDS` on this ledger rather than the shipped 30 days,
 * so an edition genuinely has to be waited out — real time is the only clock
 * the program has.
 */
import { expect } from 'chai'
import { Keypair, PublicKey, LAMPORTS_PER_SOL } from '@solana/web3.js'
import { getAccount } from '@solana/spl-token'

import {
  BN,
  big,
  harness,
  bootstrap,
  mockFund,
  placeBidAccounts,
  settleAccounts,
  fileCopyAccounts,
  spikeAccounts,
  penAccounts,
  readCopy,
  ASSET_COUNT,
  COPY_BYTES,
  SPIKE_MARKER,
} from './enc-harness.js'

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms))

/**
 * The column this suite rents. Deliberately not one of the indices `auction.ts`
 * fights over — these suites share a ledger, and a stale high bid left on the
 * same asset would make `nextEdition` settle when it meant to roll.
 */
const COLUMN = 3
/**
 * A column nobody here ever bids on **or strikes**, so the Emperor keeps it and
 * it stays untouched. Kept clean deliberately: it is the only witness to what a
 * slot nobody has ever won looks like.
 */
const EMPERORS = 9
/**
 * The column the pen cases practise on.
 *
 * Separate from `EMPERORS` because **the editor may strike a vault-held column
 * like any other** — the pen is aimed at a column, not at a tenant, and nothing
 * in `spike` branches on who holds the slot. Striking the Emperor's own column
 * writes the marker over nothing, which is harmless and left permitted, but it
 * would leave a witness that had been tampered with.
 */
const SCRATCH = 8

describe('the Imperial Gazette', () => {
  const h = harness()
  const tenant = Keypair.generate()
  const stranger = Keypair.generate()
  const successor = Keypair.generate()

  /** Whether this ledger still has an editor. `false` after any earlier run. */
  let penBroken = false

  const asset = (i: number) => h.program.account.asset.fetch(h.assetPda(i))
  const config = () => h.program.account.config.fetch(h.configPda)
  const column = async (i: number) => readCopy(await asset(i))

  /** The validator's clock. Never `Date.now()` — see `enc-harness.ts`. */
  const now = async (): Promise<number> => {
    const slot = await h.history.getSlot()
    return (await h.history.getBlockTime(slot)) ?? Math.floor(Date.now() / 1000)
  }

  const encBalance = async (owner: PublicKey) =>
    (await h.exists(h.encAta(owner)))
      ? BigInt((await getAccount(h.connection, h.encAta(owner))).amount.toString())
      : 0n

  /** Mirrors `PriceCurve::price_at` in math.rs. */
  function priceAt(
    a: {
      priceFrom: { toString(): string }
      priceTo: { toString(): string }
      interpStart: { toNumber(): number }
      interpEnd: { toNumber(): number }
    },
    at: number,
  ) {
    const from = big(a.priceFrom)
    const to = big(a.priceTo)
    const start = a.interpStart.toNumber()
    const end = Math.max(a.interpEnd.toNumber(), start)
    if (at >= end) return to
    if (at <= start) return from
    return from + ((to - from) * BigInt(at - start)) / BigInt(end - start)
  }

  async function waitOutTerm(i: number) {
    const endsAt = Number((await asset(i)).termEndsAt)
    for (let attempt = 0; attempt < 60; attempt++) {
      const t = await now()
      if (t >= endsAt) return
      await sleep(Math.min((endsAt - t) * 1000 + 500, 5_000))
    }
    throw new Error('the validator clock never reached the end of the term')
  }

  /**
   * Run the presses: end this edition and start the next, leaving the tenancy
   * where it is.
   *
   * A rollover is the right instruction here because nothing in this suite
   * leaves a qualifying bid standing after the one it places to win the column
   * — but the state is shared with every other suite, so settle when there is a
   * winner rather than assuming there is not.
   */
  async function nextEdition(i: number) {
    await waitOutTerm(i)
    const a = await asset(i)
    const qualifies = big(a.highBid) > 0n && big(a.highBid) >= priceAt(a, (await now()) + 2)
    if (qualifies) {
      await h.program.methods
        .settleAuction(i)
        .accounts(settleAccounts(h, i, a.highBidder, a.holder))
        .rpc()
    } else {
      await h.program.methods.rollTerm(i).accounts({ asset: h.assetPda(i) }).rpc()
    }
  }

  /** Win column `i` at auction, the only way a wallet ever becomes a tenant. */
  async function rentColumn(i: number, who: Keypair) {
    for (let attempt = 0; attempt < 5; attempt++) {
      const a = await asset(i)
      if (a.holder.toBase58() === who.publicKey.toBase58()) return

      // A live term to bid into. `place_bid` refuses once the term has ended.
      if ((await now()) >= Number(a.termEndsAt) - 3) {
        await nextEdition(i)
        continue
      }

      const fresh = await asset(i)
      const reserve = priceAt(fresh, (await now()) + 2)
      const floor = big(fresh.highBid) + 1n
      // A hundredth of a percent of margin, because the reserve keeps climbing
      // for the whole term after any sync and settlement re-checks it.
      const bid = (reserve > floor ? reserve : floor) + reserve / 10_000n
      await h.program.methods
        .placeBid(i, new BN(bid.toString()))
        .accounts(placeBidAccounts(h, i, who.publicKey))
        .signers([who])
        .rpc()

      await waitOutTerm(i)
      const ready = await asset(i)
      await h.program.methods
        .settleAuction(i)
        .accounts(settleAccounts(h, i, who.publicKey, ready.holder))
        .rpc()
    }
    const held = (await asset(i)).holder.toBase58()
    if (held !== who.publicKey.toBase58()) {
      throw new Error(`could not rent column ${i}: it is held by ${held}`)
    }
  }

  const file = (i: number, who: Keypair, text: string) =>
    h.program.methods
      .fileCopy(i, text)
      .accounts(fileCopyAccounts(h, i, who.publicKey))
      .signers([who])
      .rpc()

  const spike = (i: number, who: Keypair | PublicKey) =>
    who instanceof Keypair
      ? h.program.methods
          .spike(i)
          .accounts(spikeAccounts(h, i, who.publicKey))
          .signers([who])
          .rpc()
      : h.program.methods.spike(i).accounts(spikeAccounts(h, i, who)).rpc()

  before(async function () {
    this.timeout(300_000)
    await bootstrap(h)

    penBroken = (await config()).editor === null

    for (const who of [tenant, stranger, successor]) {
      const sig = await h.connection.requestAirdrop(who.publicKey, 5 * LAMPORTS_PER_SOL)
      await h.history.confirmTransaction(sig, 'confirmed')
    }
    // The vault is the only source of ENC until the faucet has been running,
    // and the column has to be paid for at whatever M2 says it is worth.
    const stake = big((await asset(ASSET_COUNT - 1)).priceTo) * 4n
    await mockFund(h, tenant.publicKey, stake)

    await rentColumn(COLUMN, tenant)
  })

  // ── Filing ────────────────────────────────────────────────────────────────

  /**
   * A slot nobody has won is held by the vault, which is a PDA with no private
   * key — so there is no signer that could ever satisfy `file_copy`'s tenancy
   * check. The Emperor's columns are structurally unwritable, and the front
   * page renders its own default copy for them.
   */
  it("leaves the Emperor's own columns unwritable", async function () {
    const a = await asset(EMPERORS)
    if (a.holder.toBase58() !== h.vaultPda.toBase58()) this.skip()

    expect(a.copyFiled, 'a vault-held column carries a filing').to.equal(false)
    const why = await h.failureOf(() => file(EMPERORS, stranger, 'mine now'))
    expect(why, "a stranger filed the Emperor's column").to.match(/NotTheTenant/)
  })

  /**
   * `copy_len == 0` is the signal the front page reads as "nobody has ever
   * written here, print the Emperor's own default copy". Only meaningful on a
   * slot that has genuinely never been touched, so skip rather than assert
   * something a live ledger is entitled to have falsified.
   */
  it('marks a column nobody has ever won as never written', async function () {
    const a = await asset(EMPERORS)
    if (a.holder.toBase58() !== h.vaultPda.toBase58() || a.copyLen !== 0) this.skip()
    expect(await column(EMPERORS)).to.equal('')
  })

  it('lets the tenant file their column, and reads back exactly what was filed', async () => {
    await nextEdition(COLUMN)
    const text = 'THERE IS NO MAGIC MONEY TREE — cont. p.94'
    await file(COLUMN, tenant, text)

    const a = await asset(COLUMN)
    expect(a.copyFiled, 'the filing was not recorded').to.equal(true)
    expect(a.copySpiked).to.equal(false)
    expect(a.copyLen).to.equal(Buffer.byteLength(text, 'utf8'))
    expect(readCopy(a)).to.equal(text)
    // Zero-padded, so nothing of a previous edition survives past copyLen.
    expect(a.copy.slice(a.copyLen).every((b) => b === 0), 'the tail is not blank').to.equal(true)
  })

  it('refuses a second filing in the same term', async () => {
    const before = await column(COLUMN)
    const why = await h.failureOf(() => file(COLUMN, tenant, 'actually, ignore that'))
    expect(why, 'the tenant filed twice in one term').to.match(/AlreadyFiled/)
    expect(await column(COLUMN), 'the refused filing changed the column').to.equal(before)
  })

  it('refuses a stranger', async () => {
    const before = await column(COLUMN)
    const why = await h.failureOf(() => file(COLUMN, stranger, 'squatting'))
    expect(why, 'a stranger wrote in a column they do not rent').to.match(/NotTheTenant/)
    expect(await column(COLUMN)).to.equal(before)
  })

  it('holds a column to 280 bytes, and counts bytes rather than characters', async function () {
    this.timeout(120_000)
    await nextEdition(COLUMN)

    const tooLong = 'x'.repeat(COPY_BYTES + 1)
    expect(await h.failureOf(() => file(COLUMN, tenant, tooLong))).to.match(/CopyTooLong/)

    // Ninety-four block characters are 282 bytes and would fit if the bound
    // were on characters. It is not.
    expect(await h.failureOf(() => file(COLUMN, tenant, '█'.repeat(94)))).to.match(/CopyTooLong/)

    // The refusals cost the tenant nothing: the term's one filing is still theirs.
    const exact = 'y'.repeat(COPY_BYTES)
    await file(COLUMN, tenant, exact)
    expect(await column(COLUMN)).to.equal(exact)
  })

  it("keeps yesterday's news standing across an edition, and hands back a blank slate", async function () {
    this.timeout(120_000)
    const standing = await column(COLUMN)
    expect(standing, 'nothing was filed to carry over').to.not.equal('')

    await nextEdition(COLUMN)

    const a = await asset(COLUMN)
    expect(readCopy(a), 'settlement wiped the page').to.equal(standing)
    expect(a.copyFiled, 'the new edition did not reset the filing flag').to.equal(false)
    expect(a.copySpiked).to.equal(false)

    // And the flag reset is real: this term's filing is available again.
    await file(COLUMN, tenant, 'STOP PRESS')
    expect(await column(COLUMN)).to.equal('STOP PRESS')
  })

  // ── The pen ───────────────────────────────────────────────────────────────

  it('gives the editor no way to say anything', function () {
    // The acceptance criterion is "spike writes the marker, never
    // caller-supplied text", and the strongest form of that is an interface
    // with nowhere to put text: `spike` takes an index and nothing else.
    const ix = h.program.idl.instructions.find((i) => i.name === 'spike')
    expect(ix, 'spike is missing from the IDL').to.not.be.undefined
    expect(ix!.args.map((a) => a.name)).to.deep.equal(['index'])
    expect(ix!.args[0].type).to.equal('u8')
  })

  it('strikes a column to the marker, and only to the marker', async function () {
    this.timeout(120_000)
    if (penBroken) this.skip()

    await nextEdition(COLUMN)
    await file(COLUMN, tenant, 'something the editor would rather not print')

    await spike(COLUMN, h.authority)

    const a = await asset(COLUMN)
    expect(a.copySpiked).to.equal(true)
    expect(readCopy(a), 'the pen wrote something other than the marker').to.equal(SPIKE_MARKER)
  })

  it('refuses a second spike in the same term', async function () {
    if (penBroken) this.skip()
    const why = await h.failureOf(() => spike(COLUMN, h.authority))
    expect(why, 'the editor struck the same column twice in one term').to.match(/ColumnSpiked/)
  })

  it('will not let a spiked column be re-filed until the term rolls', async function () {
    this.timeout(120_000)
    if (penBroken) this.skip()

    // Spiked *before* the tenant files, which is the harder case: the term's
    // filing is forfeit, not merely overwritten.
    await nextEdition(COLUMN)
    await spike(COLUMN, h.authority)
    expect(await column(COLUMN)).to.equal(SPIKE_MARKER)

    const why = await h.failureOf(() => file(COLUMN, tenant, 'let me try that again'))
    expect(why, 'a spiked column was re-filed inside its own term').to.match(/ColumnSpiked/)

    // Next edition, fresh page. The marker stands until something replaces it.
    await nextEdition(COLUMN)
    expect((await asset(COLUMN)).copySpiked).to.equal(false)
    expect(await column(COLUMN), 'the marker did not stand into the next edition').to.equal(
      SPIKE_MARKER,
    )
    await file(COLUMN, tenant, 'and we are back')
    expect(await column(COLUMN)).to.equal('and we are back')
  })

  it('refuses the pen to anyone who does not hold it', async function () {
    if (penBroken) this.skip()
    const why = await h.failureOf(() => spike(SCRATCH, stranger))
    expect(why, 'a stranger struck a column').to.match(/NotTheEditor/)
  })

  it('passes the pen, and takes it from whoever held it', async function () {
    this.timeout(120_000)
    if (penBroken) this.skip()

    await h.program.methods
      .passThePen(successor.publicKey)
      .accounts(penAccounts(h, h.authority))
      .rpc()
    expect((await config()).editor?.toBase58()).to.equal(successor.publicKey.toBase58())

    // The old holder is now a stranger, which is the whole point of rotation:
    // a stolen key stops working the moment the pen moves.
    const why = await h.failureOf(() => spike(SCRATCH, h.authority))
    expect(why, 'the previous editor still holds the pen').to.match(/NotTheEditor/)

    // And the new one really has it.
    await spike(SCRATCH, successor)
    expect(await column(SCRATCH)).to.equal(SPIKE_MARKER)

    // Hand it back, so this suite leaves the ledger where it found it.
    await h.program.methods
      .passThePen(h.authority)
      .accounts(penAccounts(h, successor.publicKey))
      .signers([successor])
      .rpc()
    expect((await config()).editor?.toBase58()).to.equal(h.authority.toBase58())
  })

  it('refuses to pass the pen to nobody', async function () {
    if (penBroken) this.skip()
    // The all-zero key would leave `editor` set to something no hand can sign
    // for — an account claiming an editor exists when none does. Breaking the
    // pen says that honestly; this refuses to say it by accident.
    const why = await h.failureOf(() =>
      h.program.methods
        .passThePen(PublicKey.default)
        .accounts(penAccounts(h, h.authority))
        .rpc(),
    )
    expect(why, 'the pen was passed to the void').to.match(/NotTheEditor/)
    expect((await config()).editor?.toBase58()).to.equal(h.authority.toBase58())
  })

  // ── The money, which none of this touches ─────────────────────────────────

  /**
   * The claim is "one pen over the words", and it is only worth making because
   * "no key over the money" survives it. Every balance in sight, across a
   * filing and a strike.
   */
  it('moves no token on any Gazette path', async function () {
    this.timeout(120_000)
    await nextEdition(COLUMN)

    const supplyBefore = await h.supply()
    const vaultBefore = await h.vaultBalance()
    const tenantBefore = await encBalance(tenant.publicKey)
    const escrowBefore = (await h.exists(h.escrowEncAta))
      ? BigInt((await getAccount(h.connection, h.escrowEncAta)).amount.toString())
      : 0n

    await file(COLUMN, tenant, 'the front page, sold monthly')
    if (!penBroken) await spike(COLUMN, h.authority)

    expect(await h.supply(), 'the Gazette changed the supply').to.equal(supplyBefore)
    expect(await h.vaultBalance(), "the Gazette moved the Emperor's money").to.equal(vaultBefore)
    expect(await encBalance(tenant.publicKey), "the Gazette moved the tenant's money").to.equal(
      tenantBefore,
    )
    const escrowAfter = (await h.exists(h.escrowEncAta))
      ? BigInt((await getAccount(h.connection, h.escrowEncAta)).amount.toString())
      : 0n
    expect(escrowAfter, 'the Gazette moved escrowed money').to.equal(escrowBefore)
  })

  // ── The end of the editorship ─────────────────────────────────────────────

  /**
   * **Last, and one-way.** After this the pen cases above skip themselves on a
   * re-run — see the note at the top of the file. `./stack reset` to get them
   * back.
   */
  it('breaks the pen, and there is no way back', async function () {
    this.timeout(120_000)

    if (!penBroken) {
      const why = await h.failureOf(() =>
        h.program.methods
          .breakThePen()
          .accounts(penAccounts(h, stranger.publicKey))
          .signers([stranger])
          .rpc(),
      )
      expect(why, 'a stranger broke the pen').to.match(/NotTheEditor/)

      await h.program.methods.breakThePen().accounts(penAccounts(h, h.authority)).rpc()
      penBroken = true
    }

    expect((await config()).editor, 'the pen survived being broken').to.equal(null)

    // Nothing can strike a column now, and nothing can appoint a new editor —
    // `pass_the_pen` needs a current editor to sign, and no other instruction
    // writes the field. The paper is feral.
    expect(await h.failureOf(() => spike(SCRATCH, h.authority))).to.match(/PenBroken/)
    expect(
      await h.failureOf(() =>
        h.program.methods
          .passThePen(h.authority)
          .accounts(penAccounts(h, h.authority))
          .rpc(),
      ),
      'a new editor was appointed after the pen broke',
    ).to.match(/PenBroken/)

    // And the tenant still owns their column. Breaking the pen ends the
    // editorship, not the paper.
    await nextEdition(COLUMN)
    await file(COLUMN, tenant, 'nobody is reading this now')
    expect(await column(COLUMN)).to.equal('nobody is reading this now')
  })
})
