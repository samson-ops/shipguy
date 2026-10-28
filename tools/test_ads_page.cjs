// Functional + visual check of a Google Ads landing page on the local preview server (python3 -m http.server 8765 in the build tree).
// usage: node test_ads_page.cjs vehicle-quote-miami-florida +13056769433
const { chromium } = require('playwright');
const OUT = '/tmp/claude-0/-home-claude/4242216d-7b3b-527b-ae0a-9f0d0d263145/scratchpad/';
const SLUG = process.argv[2]; const TEL = process.argv[3];
if (!SLUG || !/^\+1\d{10}$/.test(TEL || '')) { console.log('usage: node test_ads_page.cjs <slug> <+1XXXXXXXXXX>'); process.exit(2); }
const URL = 'http://127.0.0.1:8765/' + SLUG + '.html';
let fails = 0;
function ok(cond, msg){ console.log((cond ? 'PASS ' : 'FAIL ') + msg); if(!cond) fails++; }

(async () => {
  const browser = await chromium.launch();
  // ---------- desktop, variant + gclid
  let ctx = await browser.newContext({ viewport: { width: 1366, height: 900 } });
  let page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/ERR_TUNNEL|ERR_NAME|quote-config|404|501|net::/.test(m.text())) errors.push('console: ' + m.text()); });
  await page.goto(URL + '?v=enclosed&gclid=TESTGCLID123&utm_campaign=test-enclosed', { waitUntil: 'load' });
  await page.waitForTimeout(600);
  const h1 = await page.$eval('#heroH1', e => e.innerText.replace(/\s+/g, ' ').trim());
  ok(/Enclosed Car Shipping/.test(h1) && /Quote/.test(h1), 'H1 variant applied: ' + h1);
  let dl = await page.evaluate(() => window.dataLayer.filter(x => x && x.event && !/^gtm\./.test(x.event)));
  const lp = dl.find(x => x.event === 'lp_view');
  ok(lp && lp.ads_gclid === 'TESTGCLID123' && lp.page_variant === 'enclosed' && lp.ads_campaign === 'test-enclosed', 'lp_view carries gclid/variant/campaign: ' + JSON.stringify(lp));
  const stored = await page.evaluate(() => localStorage.getItem('sg_ads'));
  ok(stored && stored.includes('TESTGCLID123'), 'gclid persisted in localStorage');
  const note = await page.evaluate(() => window.sgAds.note());
  ok(note === 'Landing page: /' + SLUG + ' | variant=enclosed | gclid=TESTGCLID123 | utm_campaign=test-enclosed.', 'lead note: ' + note);
  const hours = await page.$eval('#hoursNow', e => e.textContent);
  ok(/Open now|Closed now/.test(hours), 'hours indicator: ' + hours);
  const step = await page.$eval('#pqStepCount', e => e.textContent);
  ok(/Step 1 of 3/.test(step), 'step counter: ' + step);
  // call click tracking (block navigation)
  await page.evaluate(() => document.querySelectorAll('a[href^="tel:"]').forEach(a => a.addEventListener('click', e => e.preventDefault())));
  await page.click('#heroCallBtn');
  await page.click('.btn-call');
  dl = await page.evaluate(() => window.dataLayer.filter(x => x && x.event === 'call_click'));
  ok(dl.length === 2 && dl[0].call_location === 'call-hero' && dl[1].call_location === 'call-header' && dl[0].phone === TEL, 'call_click events: ' + JSON.stringify(dl));
  // step 1 -> 2 with ZIPs
  await page.click('[data-panel="1"] [data-next]');
  let s = await page.evaluate(() => window.dataLayer.filter(x => x && x.event === 'quote_step').length);
  ok(s === 0, 'empty step 1 does not advance');
  await page.fill('#pq-pickup', '33131'); await page.fill('#pq-delivery', '10001');
  await page.click('[data-panel="1"] [data-next]');
  await page.waitForTimeout(200);
  let st = await page.evaluate(() => window.dataLayer.filter(x => x && x.event === 'quote_step').map(x => x.step));
  ok(st.length === 1 && st[0] === 2, 'quote_step 2 fired: ' + JSON.stringify(st));
  ok(/Step 2 of 3/.test(await page.$eval('#pqStepCount', e => e.textContent)), 'step counter updates to 2');
  // force through step 2 (vehicle lists come from an external API that is blocked locally)
  await page.evaluate(() => {
    ['pq-year', 'pq-make', 'pq-model'].forEach(id => { const el = document.getElementById(id); el.disabled = false; el.innerHTML = '<option value="2020">2020</option>'; el.value = '2020'; });
  });
  await page.click('[data-panel="2"] [data-next]');
  await page.waitForTimeout(200);
  ok(/Step 3 of 3/.test(await page.$eval('#pqStepCount', e => e.textContent)), 'step counter updates to 3');
  await page.fill('#pq-firstname', 'Test'); await page.fill('#pq-lastname', 'User'); await page.fill('#pq-email', 'test@example.com'); await page.fill('#pq-phone', '3055550100');
  await page.check('#pq-consent');
  await page.click('[data-panel="3"] button[type="submit"]');
  await page.waitForTimeout(3500);
  dl = await page.evaluate(() => window.dataLayer.filter(x => x && x.event && /^quote_/.test(x.event)).map(x => x.event));
  ok(dl.includes('quote_submit') && dl.includes('quote_error') && dl.includes('quote_price'), 'submit path events (local API is absent, so demo fallback): ' + JSON.stringify(dl));
  const shown = await page.$eval('#pqQuote', e => e.classList.contains('show'));
  ok(shown, 'quote result rendered (sample estimate locally)');
  const resultTel = await page.$eval('#pqCallBtn', e => e.getAttribute('href'));
  ok(resultTel === 'tel:' + TEL, 'result call button uses the city line');
  await page.goto(URL, { waitUntil: 'load' }); await page.waitForTimeout(500);
  ok(!/Enclosed/.test(await page.$eval('#heroH1', e => e.innerText)), 'default H1 without ?v: ' + (await page.$eval('#heroH1', e => e.innerText.replace(/\s+/g,' '))));
  await page.screenshot({ path: OUT + SLUG + '-desktop.png', fullPage: false });
  await page.screenshot({ path: OUT + SLUG + '-desktop-full.png', fullPage: true });
  await ctx.close();

  // ---------- mobile: sticky bar + layout
  ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
  page = await ctx.newPage();
  page.on('pageerror', e => errors.push('pageerror(m): ' + e.message));
  await page.goto(URL, { waitUntil: 'load' }); await page.waitForTimeout(600);
  const hScroll = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
  ok(!hScroll, 'no horizontal scroll on mobile');
  let bar = await page.$eval('#sgSticky', e => e.classList.contains('show'));
  ok(!bar, 'sticky bar hidden at top');
  await page.evaluate(() => window.scrollTo(0, 2200)); await page.waitForTimeout(700);
  bar = await page.$eval('#sgSticky', e => e.classList.contains('show'));
  ok(bar, 'sticky bar shows after the quote card scrolls away');
  const barBox = await page.$eval('#sgSticky', e => { const r = e.getBoundingClientRect(); return { top: Math.round(r.top), h: Math.round(r.height), w: Math.round(r.width) }; });
  ok(barBox.top + barBox.h >= 840 && barBox.w >= 380, 'sticky bar pinned to the bottom: ' + JSON.stringify(barBox));
  await page.screenshot({ path: OUT + SLUG + '-mobile-scrolled.png' });
  await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(500);
  await page.screenshot({ path: OUT + SLUG + '-mobile.png' });
  const callBox = await page.$eval('#heroCallBtn', e => { const r = e.getBoundingClientRect(); return { top: Math.round(r.top + window.scrollY), w: Math.round(r.width) }; });
  console.log('mobile hero call button at', JSON.stringify(callBox));
  await ctx.close();
  await browser.close();
  errors.forEach(e => console.log('ERR ' + e));
  ok(errors.length === 0, 'no page/console errors (excluding blocked external resources)');
  console.log('TOTAL FAILS', fails);
})();
