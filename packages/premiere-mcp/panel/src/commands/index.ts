/**
 * The dispatch table. `main.ts` looks a command up here by name and calls it; anything not in
 * this map comes back as `INVALID_ARGS`, which is how a panel that is older than the server
 * announces itself.
 *
 * Each ticket adds its own module (`project.ts`, `sequence.ts`, `clips.ts`, …) and registers it
 * here. T5 ships only `ping`.
 */
import type { CmdName } from '../../../src/protocol'
import { activeProject, appVersion, ppro } from '../ppro'
import { clipCommands } from './clips'
import { effectCommands } from './effects'
import { evalCommands } from './eval'
import { exportCommands } from './export'
import { markerCommands } from './markers'
import { mogrtCommands } from './mogrt'
import { projectCommands } from './project'
import { sequenceCommands } from './sequence'
import { transitionCommands } from './transitions'

export type CommandHandler = (args: Record<string, unknown>) => Promise<unknown>

/**
 * Liveness + orientation in one call: is the panel alive, what host, what is open. The project
 * **path** matters as much as the name — `premiere_status` reports it and nothing else on the
 * wire carries it.
 */
const ping: CommandHandler = async () => {
  const result: { appVersion: string; project?: { name: string; path: string }; sequence?: string } = {
    appVersion: appVersion(),
  }
  try {
    const project = await activeProject()
    result.project = { name: project.name, path: project.path }
    const seq = await project.getActiveSequence()
    if (seq) result.sequence = seq.name
  } catch {
    // No project open is a normal state for ping — report the host and stop there.
  }
  return result
}

export const commands: Partial<Record<CmdName, CommandHandler>> = {
  ping,
  ...projectCommands,
  ...sequenceCommands,
  ...clipCommands,
  ...transitionCommands,
  ...markerCommands,
  ...effectCommands,
  ...mogrtCommands,
  ...exportCommands,
  ...evalCommands,
}

/** Used by the log line the panel prints on load, so a stale panel is obvious at a glance. */
export const panelCapabilities = (): Record<string, unknown> => ({
  commands: Object.keys(commands),
  hasPpro: Boolean(ppro),
})
