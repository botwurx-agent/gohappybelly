import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:1300,height:1000}, deviceScaleFactor:2 });
await p.goto('file:///home/user/gohappybelly/Website/diagrams/lessons-02-06-07.html');
await p.waitForLoadState('networkidle');
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(900);
const map = [['D1','l02-wired-in'],['D2','l02-five-areas'],['D3','l06-gut-brain'],
             ['D4','l06-two-modes'],['D5','l07-loop'],['D6','l07-two-ways-out']];
for (const [id,name] of map) {
  await p.locator('#'+id).screenshot({ path:name+'.png', omitBackground:true });
  console.log('wrote', name+'.png');
}
await b.close();
