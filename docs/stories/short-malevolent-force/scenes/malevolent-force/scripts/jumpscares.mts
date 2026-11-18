// Malevolent Force jumpscare stills, 2026-11-18, run on the repo's fixed flow-client (upload retry + copy threshold 0.5).
import { FlowClient } from '../../../../../../packages/flow-mcp/src/flow-client'
const M = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/malevolent-force/moodboard/'
export const JOBS = [
  { out: 'JS3-top.jpg', ref: 'PR2-c.jpg', prompt: `Leave this narrow shop aisle just as photographed and add a single presence: perched high above the tall right-hand shelving unit, pressed into the gap just under the ceiling tiles beside the strip light, something crouches folded up like a spider, long limbs bent too sharply, peering down the aisle. No face, only a smooth dark hollow where one should be. Soot-black skin split like dry tarmac, a dull ember glow in the splits, a curl of smoke. Mostly in shadow, the light only grazing one shoulder and two hooked fingers over the top shelf. Everything below and around it is untouched, with the same grain and tired, faded colour.\nThanks.` },
  { out: 'JS2-door.jpg', ref: 'PR2-e.jpg', prompt: `Leave this view of the open glass shop door exactly as photographed and add a single presence: outside in the black street, right behind the half-open door, a tall thin figure stands half hidden by the metal door frame, only a sliver of it showing, as if it stepped back the instant the door swung. No face, only smooth darkness. Soot-black skin split like dry tarmac with a faint ember glow, a breath of smoke. It is barely lit, brushed by a sliver of the shop's teal spill, easy to miss. The door, the sign, the mat, the bread crate and the wet street are untouched, with the same grain and tired, faded colour.\nThanks.` },
  { out: 'JS5-mirror.jpg', ref: 'FO2-d.jpg', prompt: `Leave this ceiling security mirror and the corner around it exactly as photographed and add a single presence, seen only inside the mirror's curved reflection: standing far down the reflected aisle, among the scattered blank notes on the floor, a tall thin figure with no face, only smooth darkness, its body soot-black and split like dry tarmac with a faint ember glow. In the real corner of the room outside the mirror, nothing is there. Small and warped by the convex glass, easy to miss. Everything else untouched, with the same grain and tired, faded colour.\nThanks.` },
]
const c: any = await FlowClient.connect('http://localhost:9222')
await c.openProject({ id: '0153219b-e10c-46ac-b2a7-5b50200e19fe' })
for (const j of JOBS) {
  try {
    const r = await c.editImage(j.prompt, [M + j.ref], M + j.out, { numOutputs: 2, model: 'Nano Banana 2.1', aspect: '9:16' })
    console.log('OK', j.out, JSON.stringify(r.candidates.map((x: any) => x.path.split('/').pop())))
  } catch (e) { console.log('FAIL', j.out, String((e as Error).message).slice(0, 400)) }
}
await c.close()
