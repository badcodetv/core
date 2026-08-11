import { execFileSync } from 'node:child_process'
import { readVersions, type Versions } from './paths.js'

export interface Check {
  name: string
  want: string
  got: string | null
  ok: boolean
  /** First line of stderr when the binary exists but cannot run; otherwise null. */
  broken: string | null
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

export interface Probe {
  /** stdout, when the binary ran. */
  out: string | null
  /** Set when the binary exists but could not run — e.g. a glibc mismatch. */
  broken: string | null
}

function probe(bin: string, args: string[] = ['--version']): Probe {
  try {
    return { out: execFileSync(bin, args, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }), broken: null }
  } catch (err) {
    const e = err as { code?: string; stderr?: Buffer }
    // ENOENT means genuinely absent. Anything else means it is on PATH but failed,
    // which is a different problem needing a different fix — Anchor's prebuilt
    // binaries are linked against a newer glibc than Ubuntu 22.04 ships, and
    // reporting that as "not installed" sends you off reinstalling it forever.
    if (e.code === 'ENOENT') return { out: null, broken: null }
    const stderr = e.stderr?.toString().trim() ?? ''
    return { out: null, broken: stderr.split('\n')[0] || 'failed to run' }
  }
}

/** Compare a probed version against the pin. Exported for testing. */
export function evaluate(
  name: string,
  want: string,
  raw: string | null | Probe,
  remedy: string,
  /** node is pinned as a major only ("22"), everything else is exact. */
  majorOnly = false,
): Check {
  const p: Probe = typeof raw === 'string' || raw === null ? { out: raw, broken: null } : raw
  const got = p.out === null ? null : parseVersion(p.out)
  const ok =
    got !== null && (majorOnly ? got.split('.')[0] === want.replace(/^v/, '') : got === want)
  if (!ok && p.broken) {
    return {
      name,
      want,
      got: null,
      ok: false,
      broken: p.broken,
      remedy: /GLIBC/.test(p.broken)
        ? `installed but won't run on this system's glibc — rebuild locally: avm install ${want} --from-source --force`
        : remedy,
    }
  }
  return { name, want, got, ok, broken: null, remedy: ok ? '' : remedy }
}

/**
 * One shell line that prints every pinned tool's version, separated by a marker.
 *
 * Used for the container: spawning four `docker compose run` containers to ask
 * four one-word questions costs several seconds, so ask all of them at once.
 */
export const VERSION_PROBE =
  ['rustc --version', 'solana --version', 'anchor --version', 'node --version']
    .join(' 2>&1; echo "///"; ') + ' 2>&1'

/** Turn VERSION_PROBE output into the same Checks a host probe produces. */
export function checksFromCombined(out: string, versions: Versions = readVersions()): Check[] {
  const [rust, agave, anchor, node] = out.split('///').map((s) => s.trim())
  const seen = (s: string | undefined): string | null => (s && parseVersion(s) ? s : null)
  return [
    evaluate('rust', versions.rust, seen(rust), 'rebuild the image: chain image --no-cache'),
    evaluate('agave (solana)', versions.agave, seen(agave), 'rebuild the image: chain image --no-cache'),
    evaluate('anchor', versions.anchor, seen(anchor), 'rebuild the image: chain image --no-cache'),
    evaluate('node', versions.node, seen(node), 'rebuild the image: chain image --no-cache', true),
  ]
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
    const got = c.got ?? (c.broken ? 'installed but broken' : 'not installed')
    const line = `  ${mark} ${c.name.padEnd(16)} want ${c.want.padEnd(10)} got ${got}`
    return c.broken ? `${line}\n      ${c.broken}` : line
  })
  const failed = checks.filter((c) => !c.ok)
  if (failed.length > 0) {
    lines.push('', 'To fix:')
    for (const c of failed) lines.push(`  ${c.name}:  ${c.remedy}`)
    if (!failed.every((c) => c.remedy.startsWith('rebuild the image'))) {
      lines.push('', 'Or run everything at once:  ./chain/scripts/install.sh')
      lines.push('Or skip the host install entirely and use Docker:  unset CHAIN_RUNNER')
    }
  }
  return lines.join('\n')
}
