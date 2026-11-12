/**
 * Sequence-level commands: create, list, activate, read.
 *
 * Everything that mutates returns the full refreshed dump, so the caller's clip refs are never
 * one step behind the timeline.
 */
import type { FolderItem, ProjectItem, Sequence } from 'premierepro'
import type { CommandHandler } from './index'
import { PanelError, activeProject, activeSequence, dumpSequence, ppro } from '../ppro'

const create_sequence: CommandHandler = async (args) => {
  const project = await activeProject()
  const name = String(args.name ?? '')
  if (!name) throw new PanelError('INVALID_ARGS', 'create_sequence needs a name.')

  const preset = typeof args.preset === 'string' && args.preset ? args.preset : undefined
  const fromItems = Array.isArray(args.fromItems) ? (args.fromItems as string[]) : []

  let sequence: Sequence | null = null
  let thrown: string | null = null
  try {
    if (fromItems.length > 0) {
      const root = await project.getRootItem()
      const clips = []
      for (const nameOrId of fromItems) {
        const item = await findItemByNameOrId(root, nameOrId)
        if (!item) throw new PanelError('ITEM_NOT_FOUND', `No project item named or with id "${nameOrId}".`)
        clips.push(ppro.ClipProjectItem.cast(item))
      }
      sequence = await project.createSequenceFromMedia(name, clips)
    } else if (preset) {
      // NOT createSequence(name, presetPath) — that overload is deprecated. But Premiere 25.6 (Jack's
      // version, by choice) has no createSequenceWithPresetPath at all ("is not a function", 2026-11-12),
      // so fall back to the old overload there rather than lose the preset.
      const p = project as unknown as {
        createSequenceWithPresetPath?: (n: string, path: string) => Promise<Sequence>
        createSequence: (n: string, path?: string) => Promise<Sequence>
      }
      sequence = typeof p.createSequenceWithPresetPath === 'function'
        ? await p.createSequenceWithPresetPath(name, preset)
        : await p.createSequence(name, preset)
    } else {
      sequence = await project.createSequence(name)
    }
  } catch (err) {
    if (err instanceof PanelError) throw err
    thrown = err instanceof Error ? err.message : String(err)
  }

  // Same defensive pattern as open_project: Premiere's project APIs have been caught rejecting
  // on calls that actually worked, so verify by looking the sequence up rather than trusting the
  // outcome of the call.
  if (!sequence) {
    sequence = (await project.getSequences()).find((s) => s.name === name) ?? null
  }
  if (!sequence) {
    throw new PanelError('NO_SEQUENCE', `Could not create sequence "${name}"${thrown ? `: ${thrown}` : '.'}`)
  }

  await project.openSequence(sequence)
  await project.setActiveSequence(sequence)
  return dumpSequence(project, sequence)
}

const list_sequences: CommandHandler = async () => {
  const project = await activeProject()
  const sequences = await project.getSequences()
  const active = await project.getActiveSequence()
  const activeGuid = active ? String(active.guid) : null

  return {
    sequences: sequences.map((s) => ({
      name: s.name,
      guid: String(s.guid),
      active: activeGuid !== null && String(s.guid) === activeGuid,
    })),
  }
}

const set_active: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project, String(args.name ?? ''))
  await project.openSequence(sequence)
  await project.setActiveSequence(sequence)
  return dumpSequence(project, sequence)
}

const get_sequence: CommandHandler = async (args) => {
  const project = await activeProject()
  const name = typeof args.name === 'string' && args.name ? args.name : undefined
  const sequence = await activeSequence(project, name)
  // `params: false` skips the per-param walk — useful when a caller only wants the arrangement.
  return dumpSequence(project, sequence, { params: args.params !== false })
}

async function findItemByNameOrId(folder: FolderItem, nameOrId: string): Promise<ProjectItem | null> {
  const items = await folder.getItems()
  for (const item of items) {
    if (item.name === nameOrId) return item
    try {
      if (item.getId() === nameOrId) return item
    } catch {
      /* not all items answer getId */
    }
  }
  for (const item of items) {
    if (item.type !== ppro.ProjectItem.TYPE_BIN) continue
    const nested = await findItemByNameOrId(ppro.FolderItem.cast(item), nameOrId)
    if (nested) return nested
  }
  return null
}

export const sequenceCommands = {
  create_sequence,
  list_sequences,
  set_active,
  get_sequence,
}
