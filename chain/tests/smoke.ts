import * as anchor from '@coral-xyz/anchor'
import { expect } from 'chai'

/**
 * The program builds, deploys, and is executable at the id it declares.
 *
 * Deliberately the cheapest possible check. It used to send a `ping`
 * transaction too, but `ping` was scaffolding and died when `initialize`
 * arrived — behaviour lives in `initialize.ts` now. If *this* fails, nothing
 * downstream is worth debugging.
 */
describe('emperors-new-coin: scaffold', () => {
  anchor.setProvider(anchor.AnchorProvider.env())
  const program = anchor.workspace.EmperorsNewCoin as anchor.Program

  it('is deployed at the id declared in the program', async () => {
    const info = await program.provider.connection.getAccountInfo(program.programId)
    expect(info, 'program account not found — did anchor deploy run?').to.not.be.null
    expect(info!.executable).to.be.true
  })

  it('declares the id its IDL was generated with', () => {
    expect(program.idl.address).to.equal(program.programId.toBase58())
  })
})
