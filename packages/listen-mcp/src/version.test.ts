import { describe, it, expect } from 'vitest'
import { NAME } from './version'

describe('version', () => {
  it('exposes the server name', () => {
    expect(NAME).toBe('badcode-listen')
  })
})
