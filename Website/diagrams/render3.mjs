import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:1300,height:1000}, deviceScaleFactor:2 });
await p.goto('file:///home/user/gohappybelly/Website/diagrams/lessons-05-b2.html');
await p.waitForLoadState('networkidle');
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(900);
const map = [['D1','b2-under-pressure'],['D2','b2-what-stress-spends'],['D3','l05-fiber-to-fuel'],['D4','b1-liver-gallbladder'],['D5','b3-many-surfaces']];
for (const [id,name] of map) {
  await p.locator('#'+id).screenshot({ path:name+'.png', omitBackground:true });
  console.log('wrote', name+'.png');
}
await b.close();
