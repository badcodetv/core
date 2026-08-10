import { describe, expect, it } from 'vitest'
import { humanizeError } from './useSendTransaction.js'

describe('humanizeError', () => {
  it('says plainly when the user cancelled, which is not an error to apologise for', () => {
    expect(humanizeError(new Error('User rejected the request.'))).toBe('You cancelled the transaction.')
  })

  it('names the actual problem when the wallet is empty', () => {
    expect(humanizeError(new Error('Attempt to debit an account but found no record of a prior credit. insufficient lamports'))).toBe(
      'Not enough SOL to pay the fee.',
    )
  })

  it('tells you to retry on a stale blockhash rather than showing the raw text', () => {
    expect(humanizeError(new Error('Transaction simulation failed: Blockhash not found'))).toMatch(/Try again/)
  })

  it('surfaces a custom program error code, so it can be looked up', () => {
    expect(humanizeError(new Error('custom program error: 0x1770'))).toContain('0x1770')
  })

  it('passes through anything it does not recognise, rather than hiding it', () => {
    expect(humanizeError(new Error('something entirely new'))).toBe('something entirely new')
  })

  it('copes with a non-Error being thrown', () => {
    expect(humanizeError('a bare string')).toBe('a bare string')
  })
})
