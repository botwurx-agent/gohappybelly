import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:450,height:975}, deviceScaleFactor:2 });
await p.goto('file:///home/user/gohappybelly/Website/mockups/foundations-phone-ui.html');
await p.waitForLoadState('networkidle');
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(1200);
await p.locator('#ui').screenshot({ path:'foundations-phone-ui.png' });
await b.close(); console.log('ok');
