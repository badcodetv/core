/**
 * `retire` — the coin notices its own end.
 *
 * **THIS SUITE IS TERMINAL. It ends the ledger it runs on.** Retirement is
 * irreversible by design, so once these cases pass, `sync_m2` refuses on this
 * validator forever and the auction and sync suites have nothing to sync. That
 * is why `retire.ts` is excluded from the run-everything script in
 * `Anchor.toml` and lives behind `./stack test test-retire`. Run
 * **`./stack reset`** afterwards.
 *
 * If it finds an already-retired ledger it proves what it still can — that the
 * peg stays stopped and that a second `retire` is harmless — and skips the rest
 * rather than passing for the wrong reason.
 *
 * The silence window is `RETIREMENT_SILENCE_SECONDS` here rather than the
 * shipped year. Nothing about the mechanism cares how long it is; the shipped
 * value is long precisely because the flag cannot be taken back.
 */
import { expect } from 'chai'
import {
  Keypair,
  LAMPORTS_PER_SOL,
  Transaction,
  sendAndConfirmTransaction,
} from '@solana/web3.js'

import {
  BN,
  big,
  harness,
  bootstrap,
  mockFund,
  setMockM2,
  syncAccounts,
  assetMetas,
  placeBidAccounts,
  withdrawBidAccounts,
  RETIREMENT_SILENCE_SECONDS,
} from './enc-harness.js'

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms))

describe('retire', () => {
  const h = harness()

  const config = () => h.program.account.config.fetch(h.configPda)
  const printer = () => h.program.account.printer.fetch(h.printerPda)
  const retire = (caller = h.authority) =>
    h.program.methods
      .retire()
      .accounts({ config: h.configPda, printer: h.printerPda })
      .rpc()

  const sync = () =>
    h.program.methods.syncM2().accounts(syncAccounts(h)).remainingAccounts(assetMetas(h)).rpc()

  /** Push a fresh figure through, which restarts the silence clock. */
  async function syncNow() {
    const p = await printer()
    await setMockM2(h, big(p.m2Value) + 1_000_000n, p.m2ReleaseDate.toNumber() + 86_400)
    await sync()
  }

  /** Wait, by the **validator's** clock, until the program has been silent long enough. */
  async function waitOutTheSilence() {
    const until = Number((await printer()).lastSyncAt) + RETIREMENT_SILENCE_SECONDS
    for (let attempt = 0; attempt < 60; attempt++) {
      const now = await h.chainNow()
      if (now >= until) return
      await sleep(Math.min((until - now) * 1000 + 500, 5_000))
    }
    throw new Error('the validator clock never reached the end of the silence')
  }

  let alreadyRetired = false

  before(async function () {
    this.timeout(300_000)
    await bootstrap(h)
    alreadyRetired = (await config()).retired
  })

  it('starts its silence clock at genesis, not at zero', async function () {
    // Left at zero, the coin would be decades overdue for retirement the
    // instant it was born and the first stranger to look could end it.
    const p = await printer()
    const at = Number(p.lastSyncAt)
    expect(at, 'the retirement clock was never started').to.be.greaterThan(1_600_000_000)
    expect(at, 'the retirement clock is in the future').to.be.at.most((await h.chainNow()) + 5)
  })

  it('refuses while the program has heard about money recently', async function () {
    if (alreadyRetired) this.skip()
    this.timeout(120_000)
    await syncNow()
    const why = await h.failureOf(() => retire())
    expect(why, 'the coin was retired while its peg was current').to.match(/NotSilentEnough/)
  })

  it('needs no signer beyond whoever pays the fee', async function () {
    if (alreadyRetired) this.skip()
    // The account list is two PDAs and nothing else — no authority, no owner,
    // no key of ours. Asserted against the shape of the instruction rather
    // than its behaviour, because "there is no key" is a claim about the shape.
    const ix = h.program.idl.instructions.find((i) => i.name === 'retire')
    expect(ix, 'retire is missing from the interface').to.not.be.undefined
    const signers = (ix!.accounts as { name: string; signer?: boolean }[]).filter((a) => a.signer)
    expect(signers.map((a) => a.name), 'retire consults a signer').to.be.empty
  })

  it('lets a stranger end it once the silence has run, and stops the peg', async function () {
    if (alreadyRetired) this.skip()
    this.timeout(180_000)
    await waitOutTheSilence()

    // A wallet with no relationship to this program at all: no bootstrap
    // authority, no tenancy, nothing but a fee.
    //
    // Sent as a raw transaction with the stranger as **fee payer**, rather than
    // through `.signers([...])`. The instruction takes no signer account at
    // all, so Anchor rejects an extra one outright ("unknown signer") — which
    // is itself the proof, and this is the only way to actually execute it as
    // somebody else.
    const stranger = Keypair.generate()
    const drop = await h.connection.requestAirdrop(stranger.publicKey, LAMPORTS_PER_SOL)
    await h.history.confirmTransaction(drop, 'confirmed')

    const before = await printer()
    const ix = await h.program.methods
      .retire()
      .accounts({ config: h.configPda, printer: h.printerPda })
      .instruction()
    await sendAndConfirmTransaction(h.connection, new Transaction().add(ix), [stranger], {
      commitment: 'confirmed',
    })

    const after = await config()
    expect(after.retired, 'the coin did not retire').to.equal(true)
    // The final numbers are left exactly as the Fed last reported them. The
    // auctions go on trading at these forever.
    const still = await printer()
    expect(still.m2Value.toString()).to.equal(before.m2Value.toString())
    expect(still.m2ReleaseDate.toString()).to.equal(before.m2ReleaseDate.toString())
  })

  it('refuses every later sync, forever', async function () {
    this.timeout(120_000)
    expect((await config()).retired, 'this case needs a retired ledger').to.equal(true)
    const p = await printer()
    // A perfectly good, genuinely newer release — refused because the peg has
    // stopped, not because anything is wrong with the number.
    await setMockM2(h, big(p.m2Value) + 1_000_000n, p.m2ReleaseDate.toNumber() + 86_400)
    const why = await h.failureOf(sync)
    expect(why, 'the peg kept running after retirement').to.match(/Retired/)
  })

  it('is harmless to call twice', async () => {
    expect((await config()).retired).to.equal(true)
    // No error: "anyone can walk up and observe that it ended" should not throw
    // at the second person who looks.
    await retire()
    expect((await config()).retired).to.equal(true)
  })

  it('goes on auctioning flags at the prices of a vanished world', async function () {
    this.timeout(180_000)
    // The ending Ruling B leaned toward, and it costs nothing: `PriceCurve`
    // already flattens at `price_to`, so after the final sync the machine holds
    // those numbers and the auction keeps running on them.
    //
    // This is also the *safety* case, not just the poetry. A freeze ending
    // would have had to keep `withdraw_bid` and every other escrow exit alive
    // anyway, or it would strand live bids permanently — the exact harm the
    // auction's criteria forbid. So the thing to prove is not that the
    // instructions still exist in the interface; it is that **money still gets
    // out**. Proven by doing it, on a retired chain.
    expect((await config()).retired, 'this case needs a retired ledger').to.equal(true)

    const i = 0
    const alice = Keypair.generate()
    const bob = Keypair.generate()
    for (const who of [alice, bob]) {
      const drop = await h.connection.requestAirdrop(who.publicKey, 2 * LAMPORTS_PER_SOL)
      await h.history.confirmTransaction(drop, 'confirmed')
    }

    // Every term has long since lapsed while we sat out the silence. Rolling it
    // is the same permissionless path a stranger would use, and it still works.
    const lapsed = await h.program.account.asset.fetch(h.assetPda(i))
    if ((await h.chainNow()) >= Number(lapsed.termEndsAt)) {
      await h.program.methods.rollTerm(i).accounts({ asset: h.assetPda(i) }).rpc()
    }

    const asset = await h.program.account.asset.fetch(h.assetPda(i))
    const reserve = big(asset.priceTo)
    expect(reserve > 0n, 'the last price the Fed ever reported was zero').to.equal(true)
    const stake = reserve * 4n
    for (const who of [alice, bob]) await mockFund(h, who.publicKey, stake)

    // Both bids clear a reserve nothing will ever move again.
    const first = reserve + reserve / 1_000n
    await h.program.methods
      .placeBid(i, new BN(first.toString()))
      .accounts(placeBidAccounts(h, i, alice.publicKey))
      .signers([alice])
      .rpc()
    await h.program.methods
      .placeBid(i, new BN((first + 1_000n).toString()))
      .accounts(placeBidAccounts(h, i, bob.publicKey))
      .signers([bob])
      .rpc()

    // And the superseded bidder gets her money back, after the end of the
    // world. No escrow is stranded by retirement.
    const balance = await h.connection.getTokenAccountBalance(h.encAta(alice.publicKey))
    await h.program.methods
      .withdrawBid(i)
      .accounts(withdrawBidAccounts(h, i, alice.publicKey))
      .signers([alice])
      .rpc()
    const after = await h.connection.getTokenAccountBalance(h.encAta(alice.publicKey))
    expect(
      BigInt(after.value.amount) - BigInt(balance.value.amount),
      'escrow was stranded by retirement',
    ).to.equal(first)

    // And the faucet is untouched too — retirement stops the peg, not the game.
    expect((await config()).retired).to.equal(true)
  })
})
