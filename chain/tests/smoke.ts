import * as anchor from '@coral-xyz/anchor'
import { expect } from 'chai'

/**
 * Proves the whole loop works: the program builds, deploys to a local validator,
 * and answers a transaction. If this fails, nothing downstream is worth debugging.
 */
describe('emperors-new-coin: scaffold', () => {
  anchor.setProvider(anchor.AnchorProvider.env())
  const program = anchor.workspace.EmperorsNewCoin as anchor.Program

  it('is deployed at the id declared in the program', async () => {
    const info = await program.provider.connection.getAccountInfo(program.programId)
    expect(info, 'program account not found — did anchor deploy run?').to.not.be.null
    expect(info!.executable).to.be.true
  })

  it('answers a transaction', async () => {
    const sig = await program.methods.ping().rpc()
    expect(sig).to.be.a('string')
  })

  it('records the message on-chain, so logs are readable from tests', async () => {
    // Confirm before reading. Passing a commitment straight to rpc() races the
    // validator's blockhash cache and fails simulation with "Blockhash not found".
    const { connection } = program.provider
    const sig = await program.methods.ping().rpc()
    const bh = await connection.getLatestBlockhash()
    await connection.confirmTransaction({ signature: sig, ...bh }, 'confirmed')

    const tx = await connection.getTransaction(sig, {
      commitment: 'confirmed',
      maxSupportedTransactionVersion: 0,
    })
    const logs = tx?.meta?.logMessages?.join('\n') ?? ''
    expect(logs).to.contain('the cloth was always invisible')
  })
})
