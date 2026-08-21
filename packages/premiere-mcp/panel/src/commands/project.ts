/**
 * Project-level commands: open/create, save, import, list.
 *
 * Every path crossing this boundary is a **Windows** path — `server.ts` translates at the wire,
 * so nothing in here should ever see `/mnt/…`.
 */
import type { ClipProjectItem, FolderItem, Project, ProjectItem } from 'premierepro'
import type { CommandHandler } from './index'
import { PanelError, activeProject, ppro, samePath, withTransaction } from '../ppro'

/* ---- open / create ---------------------------------------------------------------------------- */

const open_project: CommandHandler = async (args) => {
  const path = String(args.path ?? '')
  if (!path) throw new PanelError('INVALID_ARGS', 'open_project needs a Windows project path.')
  const create = args.create === true

  // The panel does NOT decide create-vs-open. `ppro.Project.isProject()` looks like an existence
  // check and is not one — it returned `true` for two paths that did not exist (live, 2026-08-21),
  // which sent us down the `open` branch for a file Premiere then refused to open, with the
  // useless message "Failed to open the project". The server checks the real filesystem instead.
  // 🔴 `Project.open()` REJECTS WITH THE BARE STRING "Failed to open the project" EVEN WHEN IT
  // WORKED. Measured live 2026-08-21: after the rejection, `getActiveProject()` was the project
  // we asked for, both when it was already open and when it was not. The throw is not an Error
  // either — it is a string, which is why it arrives with no stack and no `.message`.
  //
  // So: attempt, swallow, then VERIFY against the active project. Never trust either the return
  // value or the rejection on its own.
  let project: Project | null = null
  let thrown: string | null = null
  try {
    if (create) {
      project = await ppro.Project.createProject(path)
    } else {
      // These dialogs would otherwise put up UI, which reaches the caller as an unexplained
      // TIMEOUT rather than an error.
      const options = new ppro.OpenProjectOptions()
        .setShowConvertProjectDialog(false)
        .setShowLocateFileDialog(false)
        .setShowWarningDialog(false)
      project = await ppro.Project.open(path, options)
    }
  } catch (err) {
    thrown = err instanceof Error ? err.message : String(err)
  }

  if (!project) {
    const active = await ppro.Project.getActiveProject()
    if (active && samePath(active.path, path)) project = active
  }

  if (!project) {
    throw new PanelError(
      'NO_PROJECT',
      `Project.${create ? 'createProject' : 'open'}("${path}") failed: ${thrown ?? 'returned nothing'}. ` +
        'The active project afterwards was not the one requested.',
      { create, path, thrown }
    )
  }

  const sequences = await project.getSequences()
  return {
    project: { name: project.name, path: project.path },
    created: create,
    sequences: sequences.map((s) => s.name),
  }
}

/* ---- save ------------------------------------------------------------------------------------- */

const save: CommandHandler = async () => {
  const project = await activeProject()
  const saved = await project.save()
  if (!saved) throw new PanelError('PANEL_ERROR', 'Premiere reported that the save did not complete.')
  return { path: project.path }
}

/* ---- import ------------------------------------------------------------------------------------ */

/**
 * `Project.importFiles` returns **only a boolean** — it will not tell you what arrived. So:
 * snapshot the target bin's item ids, import, re-list, and diff. That is the only way to learn
 * what the import actually produced.
 */
const importCmd: CommandHandler = async (args) => {
  const project = await activeProject()
  const paths = Array.isArray(args.paths) ? (args.paths as string[]) : []
  if (paths.length === 0) throw new PanelError('INVALID_ARGS', 'import needs at least one path.')

  const binName = typeof args.bin === 'string' && args.bin ? args.bin : undefined
  const root = await project.getRootItem()
  const target = binName ? await ensureBin(project, root, binName) : root

  const before = new Set((await target.getItems()).map(idOf))
  const imported = await project.importFiles(paths, true, ppro.ProjectItem.cast(target))
  if (!imported) {
    throw new PanelError(
      'IMPORT_FAILED',
      `Premiere refused to import ${paths.length} file${paths.length === 1 ? '' : 's'}. ` +
        'Check the paths exist on the Windows side and the codecs are supported.'
    )
  }

  const fresh = (await target.getItems()).filter((item) => !before.has(idOf(item)))
  const items = []
  for (const item of fresh) {
    items.push({ id: idOf(item), name: item.name, mediaPath: (await mediaPathOf(item)) ?? '' })
  }
  return { items, bin: binName }
}

/**
 * `createBinAction` is an Action: it returns nothing useful, so the bin has to be found again by
 * name once the transaction has committed.
 */
async function ensureBin(project: Project, root: FolderItem, name: string): Promise<FolderItem> {
  const existing = await findBin(root, name)
  if (existing) return existing

  withTransaction(project, `create bin ${name}`, (ca) => {
    ca.addAction(root.createBinAction(name, false))
  })

  const created = await findBin(root, name)
  if (!created) throw new PanelError('PANEL_ERROR', `Created bin "${name}" but could not find it afterwards.`)
  return created
}

async function findBin(folder: FolderItem, name: string): Promise<FolderItem | null> {
  const items = await folder.getItems()
  for (const item of items) {
    if (item.type === ppro.ProjectItem.TYPE_BIN && item.name === name) return ppro.FolderItem.cast(item)
  }
  for (const item of items) {
    if (item.type !== ppro.ProjectItem.TYPE_BIN) continue
    const nested = await findBin(ppro.FolderItem.cast(item), name)
    if (nested) return nested
  }
  return null
}

/* ---- list ------------------------------------------------------------------------------------- */

const list_items: CommandHandler = async (args) => {
  const project = await activeProject()
  const root = await project.getRootItem()
  const binName = typeof args.bin === 'string' && args.bin ? args.bin : undefined

  const start = binName ? await findBin(root, binName) : root
  if (!start) throw new PanelError('ITEM_NOT_FOUND', `No bin named "${binName}".`)

  const items: Record<string, unknown>[] = []
  await walk(start, binName ?? null, items)
  return { items }
}

async function walk(folder: FolderItem, binName: string | null, out: Record<string, unknown>[]): Promise<void> {
  for (const item of await folder.getItems()) {
    const isBin = item.type === ppro.ProjectItem.TYPE_BIN
    const row: Record<string, unknown> = {
      id: idOf(item),
      name: item.name,
      type: isBin ? 'bin' : (await isSequence(item)) ? 'sequence' : 'clip',
    }
    if (binName) row.bin = binName
    if (!isBin) {
      const media = await mediaPathOf(item)
      if (media) row.mediaPath = media
    }
    out.push(row)
    if (isBin) await walk(ppro.FolderItem.cast(item), item.name, out)
  }
}

/* ---- shared helpers ------------------------------------------------------------------------------ */

function idOf(item: ProjectItem): string {
  try {
    return item.getId()
  } catch {
    return ''
  }
}

function asClip(item: ProjectItem): ClipProjectItem | null {
  try {
    return ppro.ClipProjectItem.cast(item)
  } catch {
    return null
  }
}

async function mediaPathOf(item: ProjectItem): Promise<string | null> {
  const clip = asClip(item)
  if (!clip) return null
  try {
    return (await clip.getMediaFilePath()) || null
  } catch {
    // Bins, sequences and synthetic items have no media file — not an error.
    return null
  }
}

async function isSequence(item: ProjectItem): Promise<boolean> {
  const clip = asClip(item)
  if (!clip) return false
  try {
    return await clip.isSequence()
  } catch {
    return false
  }
}

export const projectCommands = {
  open_project,
  save,
  import: importCmd,
  list_items,
}
