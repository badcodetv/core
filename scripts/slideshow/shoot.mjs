// Screenshot slides of a built preview, headless.
//   node scripts/slideshow/shoot.mjs <preview.html> <outdir> [id[:clicks] ...]
// Each id loads fresh (no state carried between shots); ":2" presses → twice first.
// SHOOT_CHROME=<path to chrome-headless-shell> if Playwright's default browser isn't installed.
// Prints any page errors and the slide state, so a blank shot is explained.
import { chromium } from "playwright";
import { pathToFileURL } from "url";
import { resolve } from "path";
const [, , file, out, ...ids] = process.argv;
const exe = process.env.SHOOT_CHROME;
const b = await chromium.launch({ ...(exe ? { executablePath: exe } : {}), args: ["--use-gl=swiftshader", "--enable-webgl", "--ignore-gpu-blocklist"] });
const errs = [];
for (const raw of ids.length ? ids : ["1"]) {
  const [id, clicks = "0"] = raw.split(":");
  const p = await b.newPage({ viewport: { width: 1600, height: 900 } });
  p.on("pageerror", e => errs.push(`${id}: ${e.message}`));
  p.on("console", m => m.type() === "error" && errs.push(`${id}: ${m.text()}`));
  await p.goto(pathToFileURL(resolve(file)).href + "#s-" + id);
  await p.waitForTimeout(1200);
  await p.keyboard.press("h");
  for (let i = 0; i < +clicks; i++) { await p.keyboard.press("ArrowRight"); await p.waitForTimeout(300); }
  await p.waitForTimeout(1800);
  const state = await p.evaluate(() => ({ html: document.querySelector("#stage").innerHTML.length, pos: document.querySelector("#pos").textContent }));
  if (!state.html) errs.push(`${id}: stage is empty (${state.pos})`);
  await p.screenshot({ path: `${out}/s-${id}${clicks !== "0" ? "-" + clicks : ""}.png` });
  await p.close();
}
console.log(errs.length ? "ERRORS:\n" + [...new Set(errs)].join("\n") : "no errors");
await b.close();
