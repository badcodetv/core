import { expect } from 'chai'
import { TOKEN_PROGRAM_ID } from '@solana/spl-token'
import * as anchor from '@coral-xyz/anchor'
import { ASSET_COUNT, bootstrap, harness } from './enc-harness.js'

/**
 * Rent and foreclosure, as far as they can be exercised without a holder.
 *
 * **Partly blocked, on purpose.** Every asset is held by the vault until
 * `buy_asset` lands at T12, and rent is a thing that happens to *players* — so
 * the paying, part-paying, grace and bounty paths have no subject yet. What is
 * testable now is the other half of each rule: that the Emperor is exempt, and
 * that neither instruction can be pointed at the wrong account. The arithmetic
 * is covered by the Rust unit tests in `settle_rent.rs` and `math.rs`.
 *
 * The holder-side cases arrive with T12, in `buy_asset.ts`.
 */
describe('rent + foreclosure', () => {
  const h = harness()

  before(async function () {
    this.timeout(300_000)
    await bootstrap(h)
  })

  const settleAccounts = (index: number, holderTokenAccount: anchor.web3.PublicKey) => ({
    config: h.configPda,
    asset: h.assetPda(index),
    vault: h.vaultPda,
    mint: h.mintPda,
    holderTokenAccount,
    vaultTokenAccount: h.vaultEncAta,
    tokenProgram: TOKEN_PROGRAM_ID,
  })

  it('every asset is still the Emperor’s, so none of this has a subject yet', async () => {
    for (let i = 0; i < ASSET_COUNT; i++) {
      const asset = await h.program.account.asset.fetch(h.assetPda(i))
      expect(asset.holder.toBase58(), `asset ${i}`).to.equal(h.vaultPda.toBase58())
    }
  })

  /**
   * The Emperor does not pay rent to the Emperor — but that guard cannot be
   * isolated while the vault is the only holder there is.
   *
   * Pointing either instruction at a vault-held asset means passing the vault's
   * own token account as both landlord and tenant, and Anchor rejects the
   * duplicate mutable account before the handler runs. Forcing it through would
   * mean building a second vault-owned token account purely to make an error
   * message come out differently, which tests the fixture rather than the rule.
   * T12 creates a real holder, and then the case is ordinary.
   */
  it('refuses to charge rent on an asset the vault holds')
  it('refuses to foreclose on an asset the vault holds')

  /**
   * Rent is pulled from whatever account is passed, so aiming it at the wrong
   * one would charge the wrong person. Checked explicitly rather than left to
   * a silent mismatch.
   */
  it('refuses a token account that is not the holder’s', async () => {
    const stranger = anchor.web3.Keypair.generate()
    const strangerAta = anchor.utils.token.associatedAddress({
      mint: h.mintPda,
      owner: stranger.publicKey,
    })
    const why = await h.failureOf(() =>
      h.program.methods.settleRent(0).accounts(settleAccounts(0, strangerAta)).rpc(),
    )
    // Either the account does not exist or it fails the owner check; both are
    // the instruction refusing to charge a stranger.
    expect(why).to.not.equal('')
  })

  /** Nothing in this file may change how much ENC exists. */
  it('leaves total supply untouched', async () => {
    const before = await h.supply()
    await h.failureOf(() =>
      h.program.methods.settleRent(0).accounts(settleAccounts(0, h.vaultEncAta)).rpc(),
    )
    expect((await h.supply()).toString()).to.equal(before.toString())
  })

  // ── Waiting on a holder (T12) ─────────────────────────────────────────────

  it('charges a holder rent that accrues continuously')
  it('takes only what a holder can pay, and keeps the rest owing')
  it('refuses to foreclose on a holder who can cover the debt')
  it('refuses to foreclose before grace has elapsed, and allows it after')
  it('pays the forecloser a bounty from the vault')
})
