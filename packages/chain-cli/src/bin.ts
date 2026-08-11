#!/usr/bin/env -S npx tsx
import { standaloneProgram } from './index.js'

// Standalone entry point, so this package works when lifted into a project that
// has no host CLI to mount it on.
standaloneProgram().parse()
