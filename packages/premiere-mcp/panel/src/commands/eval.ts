/**
 * `premiere_eval` — the escape hatch, not the product.
 *
 * It runs arbitrary JS inside the panel with `ppro` and the helpers in scope, so a new plugin's
 * API (or a Premiere call that is behaving unlike its type declarations) can be tried straight
 * from the conversation. Anything used twice should be promoted to a typed tool.
 *
 * `new Function` was proven to work in the UXP runtime during the T1 spike, async form included.
 */
import type { CommandHandler } from './index'
import {
  PanelError,
  activeProject,
  activeSequence,
  appVersion,
  dumpSequence,
  plainValue,
  ppro,
  resolveClip,
  resolveComponent,
  resolveProjectItem,
  secondsToTick,
  tickToSeconds,
  uxpRequire,
  withTransaction,
} from '../ppro'

const evalCmd: CommandHandler = async (args) => {
  const code = String(args.code ?? '')
  if (!code) throw new PanelError('INVALID_ARGS', 'eval needs `code`.')

  const logs: string[] = []
  const log = (...parts: unknown[]): void => {
    logs.push(parts.map((p) => (typeof p === 'string' ? p : safeString(p))).join(' '))
  }

  const helpers = {
    withTransaction,
    secondsToTick,
    tickToSeconds,
    resolveClip,
    resolveComponent,
    resolveProjectItem,
    dumpSequence,
    activeProject,
    activeSequence,
    appVersion,
    plainValue,
    require: uxpRequire,
  }

  try {
    // Wrapped in an async IIFE so `await` works at the top level of the snippet, and so a bare
    // expression still needs an explicit `return` — same rule as a function body.
    const fn = new Function('ppro', 'helpers', 'log', `return (async () => { ${code} })()`) as (
      p: typeof ppro,
      h: typeof helpers,
      l: typeof log
    ) => Promise<unknown>
    const value = await fn(ppro, helpers, log)
    return { value: jsonSafe(value), logs }
  } catch (err) {
    throw new PanelError(
      'EVAL_ERROR',
      err instanceof Error ? err.message : String(err),
      err instanceof Error ? err.stack ?? '(no stack — native UXP error)' : undefined
    )
  }
}

/** UXP objects are frequently native handles whose fields are getters, so `JSON.stringify`
 * yields `{}`. Fall back to a readable string rather than silently returning an empty object. */
function jsonSafe(value: unknown): unknown {
  if (value === undefined) return null
  try {
    const round = JSON.parse(JSON.stringify(value)) as unknown
    if (round !== null && typeof round === 'object' && Object.keys(round as object).length === 0 && typeof value === 'object' && value !== null) {
      return describeOpaque(value)
    }
    return round
  } catch {
    return safeString(value)
  }
}

/** What an opaque native object at least *offers* — far more useful than `{}` when probing. */
function describeOpaque(value: object): Record<string, unknown> {
  const keys: string[] = []
  let proto: object | null = value
  while (proto && proto !== Object.prototype) {
    for (const k of Object.getOwnPropertyNames(proto)) if (k !== 'constructor' && !keys.includes(k)) keys.push(k)
    proto = Object.getPrototypeOf(proto) as object | null
  }
  return { __opaque: safeString(value), members: keys.sort() }
}

function safeString(value: unknown): string {
  try {
    return String(value)
  } catch {
    return '(unstringifiable)'
  }
}

export const evalCommands = { eval: evalCmd }
