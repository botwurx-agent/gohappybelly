import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1';
const URL='https://www.gohappybelly.com/gut-foundations';

const SPEC = `
/* 1. CTA button: contrast, size, case */
a[href*="/offers/"]{
  background-color:#A85F3E !important;
  font-size:16px !important;
  font-weight:600 !important;
  text-transform:none !important;
  letter-spacing:0.01em !important;
}
/* 2. eyebrow / price label: 2.43 -> 4.87 */
[style*="color: #7AAE86"]{ color:#3F7A50 !important; }
/* 3. secondary text: 3.94 -> 4.74 */
[style*="color: #6A8278"]{ color:#5E7569 !important; }
/* 4. the 'is not' column up from 14px */
[style*="color: #6A8278"][style*="14px"]{ font-size:15px !important; }
`;

async function shot(page, tag, after){
  // hero
  await page.evaluate(()=>window.scrollTo(0,0)); await page.waitForTimeout(600);
  await page.screenshot({path:`p-${tag}-hero.png`});
  // the "is and is not" section
  await page.evaluate(()=>{
    const h=[...document.querySelectorAll('h2')].find(e=>/what this is, and what it is not/i.test(e.innerText));
    if(h) h.scrollIntoView({block:'start'});
  });
  await page.waitForTimeout(700);
  await page.screenshot({path:`p-${tag}-isnot.png`});
}

const b = await chromium.launch();
for (const mode of ['before','after']){
  const p = await b.newPage({viewport:{width:430,height:932}, deviceScaleFactor:2, userAgent:UA});
  await p.goto(URL,{waitUntil:'networkidle',timeout:45000});
  await p.waitForTimeout(1200);
  if(mode==='after'){
    await p.addStyleTag({content:SPEC});
    await p.evaluate(()=>{
      document.querySelectorAll('a[href*="/offers/"]').forEach(a=>{
        if(/gut foundations/i.test(a.innerText)) a.textContent='Find your gut pattern, $27';
      });
      // bold the reframe line
      const t=[...document.querySelectorAll('p')].find(e=>/discipline problem/i.test(e.innerText));
      if(t){ t.style.fontWeight='600'; t.style.color='#162E28'; }
    });
    await p.waitForTimeout(500);
  }
  await shot(p, mode);
  await p.close();
}
await b.close();
console.log('done');
