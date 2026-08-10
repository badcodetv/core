#!/usr/bin/env -S npx tsx
import { Command } from 'commander'
import { chainCommand } from './index.js'

// Standalone entry point, so this package works when lifted into a project that
// has no host CLI to mount it on.
const program = new Command()
program.name('chain').description('Solana dev-chain toolchain and local cluster.')
program.addCommand(chainCommand())
program.parse()
