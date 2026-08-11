import { describe, expect, it } from 'vitest'
import { chainCommand, standaloneProgram } from './index.js'

const names = (c: { commands: readonly { name(): string }[] }) => c.commands.map((s) => s.name())

describe('chainCommand', () => {
  it('is a mountable group, so a host CLI gets `<host> chain <cmd>`', () => {
    const group = chainCommand()
    expect(group.name()).toBe('chain')
    expect(names(group)).toContain('doctor')
  })

  it('offers the whole loop, not just the pieces', () => {
    expect(names(chainCommand())).toEqual(
      expect.arrayContaining(['dev', 'up', 'down', 'reset', 'build', 'deploy', 'test', 'idl', 'wallet']),
    )
  })
})

describe('standaloneProgram', () => {
  it('exposes the commands at the top level', () => {
    // Mounting the group on itself would require `chain chain doctor`, which is
    // how this package first arrived in another project — broken.
    expect(names(standaloneProgram())).toContain('doctor')
    expect(names(standaloneProgram())).not.toContain('chain')
  })
})
