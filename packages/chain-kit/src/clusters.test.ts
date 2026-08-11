import { describe, expect, it } from 'vitest'
import { explorerUrl, isCluster, isMainnet, parseCluster, rpcEndpoint, wsEndpoint } from './clusters.js'

describe('parseCluster', () => {
  it('accepts the three real clusters', () => {
    expect(parseCluster('localnet')).toBe('localnet')
    expect(parseCluster('devnet')).toBe('devnet')
    expect(parseCluster('mainnet-beta')).toBe('mainnet-beta')
  })

  it('rejects a typo before it reaches the network, and says what is valid', () => {
    expect(() => parseCluster('mainnet')).toThrow(/mainnet-beta/)
    expect(isCluster('mainnet')).toBe(false)
  })
})

describe('endpoints', () => {
  it('points localnet at the standard test-validator ports', () => {
    expect(rpcEndpoint('localnet')).toBe('http://127.0.0.1:8899')
    expect(wsEndpoint('localnet')).toBe('ws://127.0.0.1:8900')
  })

  it('uses tls for the public clusters', () => {
    expect(rpcEndpoint('devnet')).toMatch(/^https:/)
    expect(wsEndpoint('mainnet-beta')).toMatch(/^wss:/)
  })

  it('lets a caller override, since the public mainnet endpoint is rate-limited', () => {
    expect(rpcEndpoint('mainnet-beta', 'https://my-provider.example/rpc')).toBe('https://my-provider.example/rpc')
  })
})

describe('isMainnet', () => {
  it('is true only where mistakes cost real money', () => {
    expect(isMainnet('mainnet-beta')).toBe(true)
    expect(isMainnet('devnet')).toBe(false)
    expect(isMainnet('localnet')).toBe(false)
  })
})

describe('explorerUrl', () => {
  const sig = '5Yx9k1'

  it('needs no cluster param on mainnet', () => {
    expect(explorerUrl('mainnet-beta', 'tx', sig)).toBe(`https://explorer.solana.com/tx/${sig}`)
  })

  it('names devnet explicitly', () => {
    expect(explorerUrl('devnet', 'address', sig)).toBe(`https://explorer.solana.com/address/${sig}?cluster=devnet`)
  })

  it('passes localnet as a custom url, since it has no named cluster', () => {
    const url = explorerUrl('localnet', 'tx', sig)
    expect(url).toContain('cluster=custom')
    expect(url).toContain(encodeURIComponent('http://127.0.0.1:8899'))
  })
})
