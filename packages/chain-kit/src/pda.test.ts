import { PublicKey } from '@solana/web3.js'
import { describe, expect, it } from 'vitest'
import { derive, deriveAddress, encodeSeed, u64le, u8 } from './pda.js'

// A fixed program id so the expected addresses below are stable forever.
const PID = new PublicKey('5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT')

describe('seed encoding', () => {
  it('encodes strings as utf-8, matching Rust b"literal"', () => {
    expect(encodeSeed('config')).toEqual(Buffer.from([99, 111, 110, 102, 105, 103]))
  })

  it('encodes a pubkey as its 32 raw bytes', () => {
    expect(encodeSeed(PID)).toHaveLength(32)
    expect(encodeSeed(PID)).toEqual(PID.toBuffer())
  })

  it('writes u64 little-endian, matching Rust to_le_bytes', () => {
    expect([...u64le(1n)]).toEqual([1, 0, 0, 0, 0, 0, 0, 0])
    expect([...u64le(256n)]).toEqual([0, 1, 0, 0, 0, 0, 0, 0])
  })

  it('refuses out-of-range integers rather than silently truncating', () => {
    expect(() => u8(256)).toThrow(/out of range/)
    expect(() => u8(-1)).toThrow(/out of range/)
    expect(() => u64le(-1n)).toThrow(/out of range/)
  })

  it('refuses a non-integer u8, which would otherwise round silently', () => {
    expect(() => u8(1.5)).toThrow(/out of range/)
  })
})

describe('derive', () => {
  // These are the contract. The Rust program must derive exactly these for the
  // same seeds; if a later change breaks them, the client and program disagree
  // about where state lives and every account lookup returns nothing.
  it('derives stable, pinned addresses', () => {
    expect(deriveAddress(['config'], PID).toBase58()).toBe('DVrFUZxQNxLWM5Rwsk92sBQDmUNY4njHE4nri5d4cMdm')
    expect(deriveAddress(['printer'], PID).toBase58()).toBe('96PpBLCBHeWXUmCZ5YRdLFmBL75ZqJjMRWBoCarasJNY')
    expect(deriveAddress(['vault'], PID).toBase58()).toBe('BpAvBQGwMuVsPyaPmPUmSY4p1zrp3Wxd5P3SWsrEHZJH')
  })

  it('gives a different address per index, so assets never collide', () => {
    const a = deriveAddress(['asset', u8(0)], PID)
    const b = deriveAddress(['asset', u8(1)], PID)
    expect(a.toBase58()).not.toBe(b.toBase58())
  })

  it('returns a bump in the valid range', () => {
    const [, bump] = derive(['config'], PID)
    expect(bump).toBeGreaterThanOrEqual(0)
    expect(bump).toBeLessThanOrEqual(255)
  })

  it('is deterministic', () => {
    expect(deriveAddress(['config'], PID).toBase58()).toBe(deriveAddress(['config'], PID).toBase58())
  })

  it('distinguishes seed types that would otherwise look alike', () => {
    // u8(1) is one byte; u64le(1) is eight. Confusing them is a classic bug.
    const asU8 = deriveAddress(['epoch', u8(1)], PID)
    const asU64 = deriveAddress(['epoch', u64le(1n)], PID)
    expect(asU8.toBase58()).not.toBe(asU64.toBase58())
  })
})
