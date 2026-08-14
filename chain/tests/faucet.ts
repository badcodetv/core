/**
 * The faucet: register now, collect next epoch.
 *
 * The property every case here defends is the one that lets this coin have no
 * identity system at all: **total payout during any epoch is at most one pot
 * plus the capped welcome grants, however many wallets show up.** A sybil farm
 * therefore dilutes itself and everyone else equally and cannot increase what
 * leaves the vault. Get that wrong and the only route into the economy is also
 * a drain on it.
 *
 * Epochs run for `EPOCH_SECONDS` on this ledger rather than the shipped day —
 * see the note there. Real time is the only clock the program has, so these
 * cases genuinely sit and wait, and every "which epoch is it" question is put
 * to the **validator**, never to `Date.now()`.
 */
import { expect } from 'chai'
import { Keypair, PublicKey, LAMPORTS_PER_SOL } from '@solana/web3.js'
import { TOKEN_PROGRAM_ID, getAccount, transfer } from '@solana/spl-token'

import {
  BN,
  big,
  harness,
  bootstrap,
  mockFund,
  claimAccounts,
  closeEpochAccounts,
  EPOCH_SECONDS,
  GRANTS_PER_EPOCH,
} from './enc-harness.js'

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms))

/**
 * Chai's ordering assertions reject a BigInt outright ("expected N to be a
 * number or a date"), and every amount in this program is one — u64 base units
 * do not survive a Number. So ordering is asserted as a boolean with both
 * operands printed, which reads the same in a failure message.
 */
const atLeast = (actual: bigint, bound: bigint, what: string) =>
  expect(actual >= bound, `${what}: ${actual} < ${bound}`).to.equal(true)
const atMost = (actual: bigint, bound: bigint, what: string) =>
  expect(actual <= bound, `${what}: ${actual} > ${bound}`).to.equal(true)
const above = (actual: bigint, bound: bigint, what: string) =>
  expect(actual > bound, `${what}: ${actual} <= ${bound}`).to.equal(true)

/** Mirrors `faucet_pot` in math.rs. */
function faucetPot(vault: bigint, supply: bigint, floorBps: number, alphaBps: number) {
  const floor = (supply * BigInt(floorBps)) / 10_000n
  const surplus = vault > floor ? vault - floor : 0n
  return (surplus * BigInt(alphaBps)) / 10_000n
}

/** Mirrors `PriceCurve::price_at` in math.rs. */
function priceAt(
  a: {
    priceFrom: { toString(): string }
    priceTo: { toString(): string }
    interpStart: { toNumber(): number }
    interpEnd: { toNumber(): number }
  },
  now: number,
) {
  const from = big(a.priceFrom)
  const to = big(a.priceTo)
  const start = a.interpStart.toNumber()
  const end = Math.max(a.interpEnd.toNumber(), start)
  if (now >= end) return to
  if (now <= start) return from
  return from + ((to - from) * BigInt(now - start)) / BigInt(end - start)
}

describe('the faucet', () => {
  const h = harness()
  const WELCOME = BigInt(h.params.faucet.welcomeGrant)
  const FLOOR_BPS = h.params.vault.floorBps
  const ALPHA_BPS = h.params.faucet.alphaBps

  /** Nine wallets: two regulars, four newcomers, and three scratch parts. */
  const wallets = Array.from({ length: 9 }, () => Keypair.generate())
  const [ann, bea, ...rest] = wallets
  const newcomers = rest.slice(0, 4)
  const lateArrival = rest[4]
  const whale = rest[5]

  /** Every epoch this suite has opened, for `close_epoch` to sweep up. */
  const opened: bigint[] = []

  const epochOf = (t: number) => BigInt(Math.floor(t / EPOCH_SECONDS))
  const nowEpoch = async () => epochOf(await h.chainNow())
  const encBalance = async (owner: PublicKey) =>
    (await h.exists(h.encAta(owner)))
      ? BigInt((await getAccount(h.connection, h.encAta(owner))).amount.toString())
      : 0n
  const epochAccount = (n: bigint) => h.program.account.faucetEpoch.fetch(h.epochPda(n))

  /**
   * Sit until we are early inside an epoch nobody has claimed in yet.
   *
   * Every case needs to know exactly who registered in "its" epoch, so it has
   * to start one that no earlier case has already put registrants into. The
   * *early* part matters too: several cases fire six claims in a row, and a
   * transaction that crosses a boundary mid-flight is refused by design.
   */
  async function freshEpoch(): Promise<bigint> {
    for (let attempt = 0; attempt < 40; attempt++) {
      const t = await h.chainNow()
      const epoch = epochOf(t)
      const into = t % EPOCH_SECONDS
      if (into <= EPOCH_SECONDS * 0.4 && !(await h.exists(h.epochPda(epoch)))) return epoch
      await sleep((EPOCH_SECONDS - into) * 1000 + 400)
    }
    throw new Error('the validator clock never reached a clean epoch')
  }

  /** Wait until the chain agrees the epoch has rolled past `epoch`. */
  async function waitPast(epoch: bigint) {
    for (let attempt = 0; attempt < 40; attempt++) {
      if ((await nowEpoch()) > epoch) return
      await sleep(1_500)
    }
    throw new Error(`the validator clock never left epoch ${epoch}`)
  }

  /**
   * Claim, naming the epoch the chain is actually in.
   *
   * The epoch is an instruction argument because a PDA seed cannot read the
   * clock, and the program checks it — so a transaction that straddles a
   * boundary comes back `WrongEpoch`. That is correct behaviour, not a flake,
   * and the fix is to resubmit with the new number, which is what this does.
   */
  async function claim(who: Keypair): Promise<bigint> {
    for (let attempt = 0; attempt < 3; attempt++) {
      const epoch = await nowEpoch()
      const prev = epoch > 0n && (await h.exists(h.epochPda(epoch - 1n)))
        ? h.epochPda(epoch - 1n)
        : null
      try {
        await h.program.methods
          .claim(new BN(epoch.toString()))
          .accounts(claimAccounts(h, who.publicKey, epoch, prev))
          .signers([who])
          .rpc()
        if (!opened.includes(epoch)) opened.push(epoch)
        return epoch
      } catch (err) {
        if (!String(err).includes('WrongEpoch')) throw err
      }
    }
    throw new Error('claim kept landing in a different epoch than it named')
  }

  before(async function () {
    this.timeout(300_000)
    await bootstrap(h)
    for (const who of wallets) {
      const sig = await h.connection.requestAirdrop(who.publicKey, 2 * LAMPORTS_PER_SOL)
      await h.history.confirmTransaction(sig, 'confirmed')
    }
  })

  // ── One claim ─────────────────────────────────────────────────────────────

  it('pays a first-timer the welcome grant, registers them, and mints nothing', async function () {
    this.timeout(120_000)
    const epoch = await freshEpoch()
    const vaultBefore = await h.vaultBalance()
    const supplyBefore = await h.supply()

    const at = await claim(ann)
    expect(at, 'the claim landed in a different epoch than the one prepared').to.equal(epoch)

    expect(await encBalance(ann.publicKey), 'a first visit paid the wrong amount').to.equal(WELCOME)
    // No previous epoch account existed, so there was nothing to share — and
    // nothing divided by nobody either.
    const player = await h.program.account.player.fetch(h.playerPda(ann.publicKey))
    expect(big(player.lastRegisteredEpoch)).to.equal(epoch)
    expect(player.welcomeGrantTaken).to.equal(true)

    const ledger = await epochAccount(epoch)
    expect(big(ledger.epoch)).to.equal(epoch)
    expect(ledger.registrants).to.equal(1)
    expect(ledger.grantsIssued).to.equal(1)

    // The whole distinction the design rests on: the faucet moves money the
    // Fed's number already created. It cannot create any.
    expect(await h.supply(), 'the faucet changed the money supply').to.equal(supplyBefore)
    expect(await h.vaultBalance()).to.equal(vaultBefore - WELCOME)
  })

  it('snapshots the pot from the vault before paying the caller who opened the epoch', async function () {
    this.timeout(120_000)
    const epoch = await freshEpoch()
    const vaultBefore = await h.vaultBalance()
    const supply = await h.supply()

    await claim(bea)

    const expected = faucetPot(vaultBefore, supply, FLOOR_BPS, ALPHA_BPS)
    expect(big((await epochAccount(epoch)).pot), 'the pot was snapshotted after the payout').to.equal(
      expected,
    )
    above(expected, 0n, 'the vault is too empty for this suite to mean anything')
  })

  it('refuses a second claim in the same epoch', async function () {
    this.timeout(120_000)
    await freshEpoch()
    const epoch = await claim(ann)
    const why = await h.failureOf(() =>
      h.program.methods
        .claim(new BN(epoch.toString()))
        .accounts(claimAccounts(h, ann.publicKey, epoch, h.epochPda(epoch - 1n)))
        .signers([ann])
        .rpc(),
    )
    expect(why, 'a wallet claimed twice in one epoch').to.match(/AlreadyClaimedThisEpoch/)
  })

  it('refuses a claim that names an epoch the chain is not in', async function () {
    this.timeout(60_000)
    const epoch = (await nowEpoch()) + 5n
    const why = await h.failureOf(() =>
      h.program.methods
        .claim(new BN(epoch.toString()))
        .accounts(claimAccounts(h, bea.publicKey, epoch, null))
        .signers([bea])
        .rpc(),
    )
    // Without this the caller would choose which pot they were paid from.
    expect(why, 'a claimant picked their own epoch').to.match(/WrongEpoch/)
  })

  // ── Collecting ────────────────────────────────────────────────────────────

  it('pays a registrant their share of the previous epoch, and only theirs', async function () {
    this.timeout(180_000)
    const first = await freshEpoch()
    await claim(ann)
    await claim(bea)
    const pot = big((await epochAccount(first)).pot)
    const registrants = (await epochAccount(first)).registrants
    expect(registrants, 'the setup epoch did not have the two registrants it needs').to.equal(2)
    const share = pot / BigInt(registrants)

    await waitPast(first)
    const annBefore = await encBalance(ann.publicKey)
    const beaBefore = await encBalance(bea.publicKey)
    await claim(ann)
    await claim(bea)

    expect(await encBalance(ann.publicKey), 'a registrant was paid the wrong share').to.equal(
      annBefore + share,
    )
    expect(await encBalance(bea.publicKey)).to.equal(beaBefore + share)
    // Both grants were taken on the first visit, so nothing here is a grant.
    above(share, 0n, 'the pot is too small for this to be measuring anything')
  })

  it('pays nothing to somebody who skipped an epoch', async function () {
    this.timeout(180_000)
    const registered = await freshEpoch()
    await claim(lateArrival)
    const balance = await encBalance(lateArrival.publicKey)
    expect(balance, 'the first visit should have been the grant alone').to.equal(WELCOME)

    // Skip one entirely, then come back. Eligibility is "registered in exactly
    // the previous epoch": the share they did not collect stays in the vault,
    // which is why outflow is *at most* a pot rather than exactly one.
    await waitPast(registered)
    await waitPast(registered + 1n)
    await claim(lateArrival)

    expect(await encBalance(lateArrival.publicKey), 'a skipped epoch still paid out').to.equal(
      balance,
    )
  })

  // ── The bound the whole design rests on ───────────────────────────────────

  it('gives latecomers the capped grant and no share, so a farm dilutes only itself', async function () {
    this.timeout(300_000)
    // The 1,000-wallet version of this is a unit test —
    // `a_sybil_farm_cannot_extract_more_than_the_pot` in math.rs — because a
    // thousand airdrops and a thousand claims will not run on a local
    // validator. What is proven here is the part arithmetic cannot: that the
    // *program* pays yesterday's pot only to yesterday's registrants, and that
    // arriving late gets you the capped grant and nothing else.
    const first = await freshEpoch()
    await claim(ann)
    await claim(bea)
    const potAccount = await epochAccount(first)
    const pot = big(potAccount.pot)
    expect(potAccount.registrants, 'the setup epoch has the wrong headcount').to.equal(2)
    const share = pot / 2n

    await waitPast(first)
    const vaultBefore = await h.vaultBalance()
    await claim(ann)
    await claim(bea)
    // Four newcomers against a cap of three.
    for (const who of newcomers) await claim(who)
    const collect = await nowEpoch()

    const granted = newcomers.slice(0, GRANTS_PER_EPOCH)
    const capped = newcomers.slice(GRANTS_PER_EPOCH)
    expect(capped, 'this case needs more newcomers than the cap allows').to.not.be.empty

    for (const who of granted) {
      expect(await encBalance(who.publicKey), 'a newcomer took a share of a pot they never registered for')
        .to.equal(WELCOME)
    }
    for (const who of capped) {
      expect(await encBalance(who.publicKey), 'the grant cap was exceeded').to.equal(0n)
      // Refused the money, still counted: they can collect tomorrow like
      // anyone else, and their grant is still owed.
      const player = await h.program.account.player.fetch(h.playerPda(who.publicKey))
      expect(big(player.lastRegisteredEpoch), 'a capped claimant was not registered').to.equal(collect)
      expect(player.welcomeGrantTaken, 'a grant that was never paid was marked taken').to.equal(false)
    }

    const epochNow = await epochAccount(collect)
    expect(epochNow.grantsIssued, 'more grants were issued than the cap').to.equal(GRANTS_PER_EPOCH)

    // The headline bound, measured against the vault itself.
    const outflow = vaultBefore - (await h.vaultBalance())
    const bound = pot + BigInt(GRANTS_PER_EPOCH) * WELCOME
    atMost(outflow, bound, 'six wallets drew more than one pot plus the capped grants')
    // And it really did pay out, rather than passing by paying nothing.
    expect(outflow).to.equal(2n * share + BigInt(GRANTS_PER_EPOCH) * WELCOME)
  })

  // ── The loop closes ───────────────────────────────────────────────────────

  it('funds a patient claimant past the cheapest tenancy reserve', async function () {
    this.timeout(60_000)
    // Ruling C made the faucet the only route in that we control, so "can a
    // claimant ever afford anything" stops being a tuning preference and
    // becomes the difference between an economy and a shop window. T14 measures
    // how many epochs it takes at the shipped parameters; this asserts the
    // cheaper fact that the two numbers are even in the same universe.
    const cheapest = await h.program.account.asset.fetch(h.assetPda(0))
    const reserve = priceAt(cheapest, (await h.chainNow()) + 60)
    const held = await encBalance(ann.publicKey)
    atLeast(held, reserve, 'a claimant cannot reach the cheapest reserve — the loop does not close')
  })

  // ── Housekeeping ──────────────────────────────────────────────────────────

  it('closes only epochs nobody can still be paid from', async function () {
    this.timeout(120_000)
    const current = await nowEpoch()

    for (const n of [current, current - 1n]) {
      const why = await h.failureOf(() =>
        h.program.methods
          .closeEpoch(new BN(n.toString()))
          .accounts(closeEpochAccounts(h, n, h.authority))
          .rpc(),
      )
      // N−1 is what today's claims are paid from; closing it would delete a pot
      // people are still owed.
      expect(why, `epoch ${n} was closed while it could still be collected against`).to.match(
        /EpochNotSettled/,
      )
    }

    const settled = opened.filter((n) => n + 2n <= current)
    expect(settled, 'no epoch is old enough to close yet').to.not.be.empty
    const target = settled[0]
    const before = await h.connection.getBalance(h.authority)
    await h.program.methods
      .closeEpoch(new BN(target.toString()))
      .accounts(closeEpochAccounts(h, target, h.authority))
      .rpc()

    expect(await h.exists(h.epochPda(target)), 'the epoch account survived its closure').to.equal(
      false,
    )
    expect(
      await h.connection.getBalance(h.authority),
      'the closer was not paid the rent they reclaimed',
    ).to.be.greaterThan(before)
  })

  // ── Austerity ─────────────────────────────────────────────────────────────

  it('pays nothing at all below the floor, and does not revert', async function () {
    this.timeout(180_000)
    // Drive the vault under its floor by moving money out of it, which is the
    // only thing that lowers the vault's *share* — burning lowers supply too.
    const supply = await h.supply()
    const floor = (supply * BigInt(FLOOR_BPS)) / 10_000n
    const vault = await h.vaultBalance()
    above(vault, floor, 'the vault is already below the floor')
    const moved = vault - floor + 1n
    await mockFund(h, whale.publicKey, moved)
    atMost(await h.vaultBalance(), floor, 'the vault did not go below the floor')

    try {
      const epoch = await freshEpoch()
      const before = await encBalance(ann.publicKey)
      await claim(ann)

      // Below the floor **nothing** pays out — not a share, and not a grant.
      // Arrive during the tightening and there is nothing for you.
      expect(await encBalance(ann.publicKey), 'the faucet paid below the floor').to.equal(before)
      expect(big((await epochAccount(epoch)).pot), 'a pot was snapshotted below the floor').to.equal(
        0n,
      )
      // And it succeeded: a claim below the floor registers you for a better
      // day rather than reverting.
      const player = await h.program.account.player.fetch(h.playerPda(ann.publicKey))
      expect(big(player.lastRegisteredEpoch), 'a below-floor claim did not register').to.equal(epoch)

      // A first-timer below the floor is refused the grant and keeps the right
      // to it — the field says "never resets" and this is what that buys.
      const virgin = newcomers[3]
      const heldBefore = await encBalance(virgin.publicKey)
      await claim(virgin)
      expect(await encBalance(virgin.publicKey), 'a grant was paid below the floor').to.equal(
        heldBefore,
      )
      expect(
        (await h.program.account.player.fetch(h.playerPda(virgin.publicKey))).welcomeGrantTaken,
        'a grant that was refused was marked taken',
      ).to.equal(false)
    } finally {
      // Put it back, or every later run of this suite finds an empty Emperor
      // and fails for a reason that has nothing to do with the code. The vault
      // ATA is an ordinary token account: anyone may pay *into* it.
      await transfer(
        h.connection,
        whale,
        h.encAta(whale.publicKey),
        h.vaultEncAta,
        whale,
        moved,
        [],
        undefined,
        TOKEN_PROGRAM_ID,
      )
      above(await h.vaultBalance(), floor, 'the vault was left below its floor')
    }
  })
})
