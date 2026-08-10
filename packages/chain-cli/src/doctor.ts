import { execFileSync } from 'node:child_process'
import { readVersions, type Versions } from './paths.js'

export interface Check {
  name: string
  want: string
  got: string | null
  ok: boolean
  /** What the user should actually run. Empty when the check passed. */
  remedy: string
}

/**
 * Pull the first version-shaped token out of a `--version` line.
 * The tools disagree on format: `rustc 1.90.0 (1159e78c4 ...)`,
 * `solana-cli 4.1.2 (src:... ; feat:...)`, `anchor-cli 1.1.2`.
 */
export function parseVersion(output: string): string | null {
  return output.match(/\d+\.\d+\.\d+/)?.[0] ?? null
}

function probe(bin: string, args: string[] = ['--version']): string | null {
  try {
    return execFileSync(bin, args, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] })
  } catch {
    return null
  }
}

/** Compare a probed version against the pin. Exported for testing. */
export function evaluate(
  name: string,
  want: string,
  raw: string | null,
  remedy: string,
  /** node is pinned as a major only ("22"), everything else is exact. */
  majorOnly = false,
): Check {
  const got = raw === null ? null : parseVersion(raw)
  const ok =
    got !== null && (majorOnly ? got.split('.')[0] === want.replace(/^v/, '') : got === want)
  return { name, want, got, ok, remedy: ok ? '' : remedy }
}

export function runChecks(versions: Versions = readVersions()): Check[] {
  return [
    evaluate('rust', versions.rust, probe('rustc'), `rustup toolchain install ${versions.rust} && rustup default ${versions.rust}`),
    evaluate('agave (solana)', versions.agave, probe('solana'), `sh -c "$(curl -sSfL https://release.anza.xyz/v${versions.agave}/install)"`),
    evaluate('anchor', versions.anchor, probe('anchor'), `avm install ${versions.anchor} && avm use ${versions.anchor}`),
    evaluate('node', versions.node, probe('node'), `install Node ${versions.node} (see .nvmrc)`, true),
  ]
}

export function formatReport(checks: Check[]): string {
  const lines = checks.map((c) => {
    const mark = c.ok ? '✓' : '✗'
    const got = c.got ?? 'not installed'
    return `  ${mark} ${c.name.padEnd(16)} want ${c.want.padEnd(10)} got ${got}`
  })
  const failed = checks.filter((c) => !c.ok)
  if (failed.length > 0) {
    lines.push('', 'To fix:')
    for (const c of failed) lines.push(`  ${c.name}:  ${c.remedy}`)
    lines.push('', 'Or run everything at once:  ./chain/scripts/install.sh')
  }
  return lines.join('\n')
}
