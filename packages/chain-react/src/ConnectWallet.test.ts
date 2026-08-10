import { describe, expect, it } from 'vitest'
import { shortAddress } from './ConnectWallet.js'

describe('shortAddress', () => {
  it('keeps both ends so an address stays recognisable', () => {
    expect(shortAddress('5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT')).toBe('5YSz…8XCT')
  })

  it('leaves a short string alone rather than making it longer', () => {
    expect(shortAddress('abc')).toBe('abc')
  })

  it('honours a custom keep length', () => {
    expect(shortAddress('5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT', 6)).toBe('5YSzNE…y58XCT')
  })
})
