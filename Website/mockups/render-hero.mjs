import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:1700,height:1100}, deviceScaleFactor:2 });
await p.goto('file:///tmp/claude-0/-home-user-gohappybelly/58051ef3-ca53-567e-9834-a5651840f437/scratchpad/mock2.html');
await p.waitForTimeout(1500);
const el = await p.$('#E');
await el.screenshot({ path:'mock-E.png' });
await b.close();
console.log('ok');
