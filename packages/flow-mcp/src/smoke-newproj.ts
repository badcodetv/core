/** Create a fresh Flow project and print its id. Usage: npx tsx …/smoke-newproj.ts [name] */
import { FlowClient } from './flow-client'
const c = await FlowClient.connect()
try {
  console.log(JSON.stringify(await c.createProject(process.argv[2])))
} finally {
  await c.close()
}
