import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:1400,height:1400}, deviceScaleFactor:2 });
await p.goto('file:///home/user/gohappybelly/Website/diagrams/lesson-01.html');
await p.waitForLoadState('networkidle');
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(900);
for (const [id, name] of [['A','01-tract'],['B','01-villi'],['C','01-barrier']]) {
  await p.locator('#'+id).screenshot({ path:name+'.png', omitBackground:true });
  console.log('wrote', name+'.png');
}
await b.close();
