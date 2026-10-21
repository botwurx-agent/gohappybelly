import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:1400,height:1000}, deviceScaleFactor:2 });
await p.goto('file:///tmp/claude-0/-home-user-gohappybelly/58051ef3-ca53-567e-9834-a5651840f437/scratchpad/mock.html');
await p.waitForTimeout(1200);
for (const id of ['A','B','C','D']) {
  const el = await p.$('#'+id);
  await el.screenshot({ path:`mock-${id}.png`, omitBackground:false });
  console.log(id, 'ok');
}
await b.close();
