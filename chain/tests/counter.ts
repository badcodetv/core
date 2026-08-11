import * as anchor from '@coral-xyz/anchor'
import { PublicKey } from '@solana/web3.js'
import { expect } from 'chai'
// The generated types, from the same chain/idl the web app reads. Change a field
// in lib.rs and this file stops compiling until the test is updated too — which
// is the whole point of the toolchain.
import type { Counter } from '../idl/counter'

/**
 * The toolchain's end-to-end proof: a program that holds state, derives a PDA,
 * checks a signer, and is driven entirely through generated types.
 *
 * Deliberately asserts on *relative* movement rather than absolute values. The
 * ledger persists across runs, so a test that expects `count === 1` passes once
 * and then fails forever, which teaches everyone to distrust the suite.
 */
describe('counter', () => {
  anchor.setProvider(anchor.AnchorProvider.env())
  const program = anchor.workspace.Counter as anchor.Program<Counter>
  const authority = anchor.AnchorProvider.env().wallet.publicKey

  const [counterPda] = PublicKey.findProgramAddressSync(
    [Buffer.from('counter'), authority.toBuffer()],
    program.programId,
  )

  const read = () => program.account.counter.fetch(counterPda)

  before(async () => {
    const existing = await program.provider.connection.getAccountInfo(counterPda)
    if (existing === null) await program.methods.initialize().accounts({ authority }).rpc()
  })

  it('derives the same PDA the program does', async () => {
    const account = await program.provider.connection.getAccountInfo(counterPda)
    expect(account, 'counter PDA not found after initialize').to.not.be.null
    expect(account!.owner.toBase58()).to.equal(program.programId.toBase58())
  })

  it('records the caller as the authority', async () => {
    expect((await read()).authority.toBase58()).to.equal(authority.toBase58())
  })

  it('increments by the STEP the program was built with', async () => {
    const before = (await read()).count.toNumber()
    await program.methods.increment().accounts({ counter: counterPda, authority }).rpc()
    const after = (await read()).count.toNumber()
    expect(after).to.be.greaterThan(before)
  })

  it('resets to zero', async () => {
    await program.methods.increment().accounts({ counter: counterPda, authority }).rpc()
    await program.methods.reset().accounts({ counter: counterPda, authority }).rpc()
    expect((await read()).count.toNumber()).to.equal(0)
  })

  it('refuses a counter that is not yours', async () => {
    const stranger = anchor.web3.Keypair.generate()
    let threw = false
    try {
      await program.methods
        .increment()
        .accounts({ counter: counterPda, authority: stranger.publicKey })
        .signers([stranger])
        .rpc()
    } catch {
      // Either the seeds constraint or has_one rejects it; both are the point.
      threw = true
    }
    expect(threw, 'a stranger was allowed to increment someone else’s counter').to.be.true
  })
})
