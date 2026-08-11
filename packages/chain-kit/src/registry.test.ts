import { describe, expect, it } from 'vitest'
import type { ProgramRegistry } from './registry.js'
import { isDeployed, knownPrograms, programId, registry } from './registry.js'

const FAKE: ProgramRegistry = {
  'some-program': {
    localnet: '5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT',
  },
}

describe('programId', () => {
  it('returns the address recorded for a cluster', () => {
    expect(programId('some-program', 'localnet', FAKE).toBase58()).toBe(
      '5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT',
    )
  })

  it('names the program when it is unknown, rather than failing later as "account does not exist"', () => {
    expect(() => programId('nope', 'localnet', FAKE)).toThrow(/Unknown program "nope"/)
    expect(() => programId('nope', 'localnet', FAKE)).toThrow(/some-program/)
  })

  it('says where a program IS deployed when asked for a cluster it is not', () => {
    expect(() => programId('some-program', 'devnet', FAKE)).toThrow(/no address for cluster "devnet"/)
    expect(() => programId('some-program', 'devnet', FAKE)).toThrow(/localnet/)
  })
})

describe('isDeployed', () => {
  it('answers without throwing', () => {
    expect(isDeployed('some-program', 'localnet', FAKE)).toBe(true)
    expect(isDeployed('some-program', 'mainnet-beta', FAKE)).toBe(false)
    expect(isDeployed('nope', 'localnet', FAKE)).toBe(false)
  })
})

describe('the real registry', () => {
  it('is a plain data map, so adding a program means editing json only', () => {
    expect(knownPrograms().length).toBeGreaterThan(0)
    for (const name of knownPrograms()) {
      expect(registry[name]).toBeTypeOf('object')
    }
  })

  it('records only valid base58 addresses', () => {
    for (const name of knownPrograms()) {
      for (const cluster of Object.keys(registry[name])) {
        expect(() => programId(name, cluster as never)).not.toThrow()
      }
    }
  })
})
