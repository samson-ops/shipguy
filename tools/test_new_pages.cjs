// Browser checks for new/changed city pages: layout, ZIP lock, consent gate, full quote flow with stubbed APIs.
// usage: node test_new_pages.cjs slug1 slug2 ...   (expects a static server on http://127.0.0.1:8765 serving the site root)
const { chromium } = require('/home/claude/.npm-global/lib/node_modules/playwright');
const BASE = 'http://127.0.0.1:8765';
const slugs = process.argv.slice(2);
const EXPECT_COUNT = String(require('fs').readdirSync('/home/claude/build/shipguy/city').filter(d => d.startsWith('auto-transport-') && require('fs').existsSync('/home/claude/build/shipguy/city/' + d + '/index.html')).length);   // Corpus Christi counts since the Oct 27, 2026 SEO pass registered it
(async () => {
  const browser = await chromium.launch();
  let failures = 0;
  for (const slug of slugs) {
    const url = slug.includes('/') || slug.endsWith('.html') ? `${BASE}/${slug}` : `${BASE}/city/${slug}/`;
    const log = [];
    const ok = (name, cond, extra='') => { log.push(`${cond ? 'PASS' : 'FAIL'} ${name}${extra ? ' ' + extra : ''}`); if (!cond) failures++; };
    for (const [w, h, label] of [[1280, 900, 'desktop'], [390, 844, 'mobile']]) {
      const ctx = await browser.newContext({ viewport: { width: w, height: h } });
      const page = await ctx.newPage();
      const posts = [];
      await page.route('**/*', async (route) => {
        const u = route.request().url();
        if (u.startsWith(BASE)) {
          if (/\/api\/quote2?\/quote-config/.test(u)) return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ pickupTimeframes: [{ value: 'asap', label: 'As soon as possible', isDefault: true }, { value: 'within_1_week', label: 'Within 1 week' }] }) });
          if (/\/api\/quote2?\/save/.test(u)) { posts.push(JSON.parse(route.request().postData() || '{}')); return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ id: 'L1', bookingLink: BASE + '/booked-stub' }) }); }
          if (/\/api\/quote2?\/L1\/booking-status/.test(u)) return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ priceReady: true, price: 845, bookingLink: BASE + '/booked-stub' }) });
          if (u.endsWith('/booked-stub')) return route.fulfill({ contentType: 'text/html', body: '<html><body><h1 id="booked">BOOKED</h1></body></html>' });
          return route.continue();
        }
        if (u.includes('app.berocker.com/api/v1/vehicles')) {
          const q = new URL(u);
          if (u.includes('/years')) return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ data: [2024, 2023, 2022] }) });
          if (u.includes('/makes')) return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ data: [{ name: 'Toyota' }, { name: 'Ford' }] }) });
          if (u.includes('/models')) return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ data: [{ name: 'Camry', type: 'Car' }, { name: 'RAV4', type: 'SUV' }] }) });
        }
        return route.abort(); // google maps, fonts, GTM: offline
      });
      const errors = [];
      page.on('pageerror', e => errors.push(e.message));
      await page.goto(url, { waitUntil: 'domcontentloaded' });
      await page.waitForTimeout(600);
      const m = await page.evaluate(() => ({
        sw: document.documentElement.scrollWidth, iw: window.innerWidth,
        h1: (document.querySelector('h1') || {}).innerText, tool: !!document.getElementById('pqForm'),
        canon: document.querySelectorAll('link[rel=canonical]').length,
        rows: [...document.querySelectorAll('.ph-office-card b')].map(b => b.textContent),
        dir: (document.querySelector('.ph-office-card a[href^="https://maps.app.goo.gl"]') || {}).href || '',
        nearby: document.querySelectorAll('.ph-chips a.ph-chip[href^="/city/"]').length,
        seeAll: (document.body.innerText.match(/See all (\d+) cities/) || [])[1],
        ctaBtns: [...document.querySelectorAll('.ph-tcta .btn')].map(b => { const r = b.getBoundingClientRect(); return [Math.round(r.left), Math.round(r.top), Math.round(r.width)]; }),
        placeholder: document.getElementById('pq-pickup').placeholder,
        gtm: document.documentElement.outerHTML.split('GTM-MQ7HKJTJ').length - 1,
      }));
      ok(`${label} no horizontal overflow`, m.sw <= m.iw, `(${m.sw}/${m.iw})`);
      ok(`${label} h1 + tool + one canonical`, m.h1 && m.tool && m.canon === 1, `h1="${(m.h1 || '').replace(/\n/g, ' ')}"`);
      if (!slug.includes('/') && !slug.endsWith('.html')) ok(`${label} office card rows`, m.rows.length >= 3, m.rows.join('/'));
      if (slug.includes('florida')) ok(`${label} directions link`, m.dir.startsWith('https://maps.app.goo.gl/'), m.dir);
      if (!slug.includes('/') && !slug.endsWith('.html')) ok(`${label} nearby chips + count`, m.nearby >= 5 && m.seeAll === EXPECT_COUNT, `(${m.nearby} chips, see all ${m.seeAll})`);
      ok(`${label} ZIP placeholder`, m.placeholder === 'Enter 5-digit ZIP code');
      if (label === 'desktop') ok('desktop CTA buttons side by side', m.ctaBtns.length === 2 && m.ctaBtns[0][1] === m.ctaBtns[1][1] && m.ctaBtns[0][2] < 500, JSON.stringify(m.ctaBtns));
      if (label === 'mobile') ok('mobile CTA buttons stacked full width', m.ctaBtns.length === 2 && m.ctaBtns[0][1] !== m.ctaBtns[1][1], JSON.stringify(m.ctaBtns));

      if (label === 'desktop') {
        // --- ZIP lock ---
        await page.fill('#pq-pickup', 'Tulsa');
        ok('letters stripped from ZIP field', (await page.inputValue('#pq-pickup')) === '');
        await page.fill('#pq-pickup', '7411'); await page.fill('#pq-delivery', '75201');
        await page.click('[data-panel="1"] [data-next]'); await page.waitForTimeout(200);
        const st1 = await page.evaluate(() => ({ err: getComputedStyle(document.getElementById('pq-pickup-err')).display, panel: document.querySelector('.pq-panel.is-current').dataset.panel }));
        ok('4-digit ZIP blocked with message', st1.err === 'block' && st1.panel === '1', JSON.stringify(st1));
        await page.fill('#pq-pickup', '74119'); await page.click('[data-panel="1"] [data-next]'); await page.waitForTimeout(200);
        ok('5-digit ZIPs advance to vehicle step', (await page.evaluate(() => document.querySelector('.pq-panel.is-current').dataset.panel)) === '2');
        // --- vehicle (stubbed API) ---
        await page.waitForFunction(() => document.querySelectorAll('#pq-year option').length > 1, null, { timeout: 5000 }).catch(() => {});
        await page.selectOption('#pq-year', '2023');
        await page.waitForFunction(() => !document.getElementById('pq-make').disabled && document.querySelectorAll('#pq-make option').length > 1, null, { timeout: 5000 }).catch(() => {});
        await page.selectOption('#pq-make', 'Toyota');
        await page.waitForFunction(() => !document.getElementById('pq-model').disabled && document.querySelectorAll('#pq-model option').length > 1, null, { timeout: 5000 }).catch(() => {});
        await page.selectOption('#pq-model', 'RAV4');
        await page.click('[data-panel="2"] [data-next]'); await page.waitForTimeout(200);
        ok('vehicle step advances to contact', (await page.evaluate(() => document.querySelector('.pq-panel.is-current').dataset.panel)) === '3');
        // --- consent gate ---
        await page.fill('#pq-firstname', 'Test'); await page.fill('#pq-lastname', 'Driver'); await page.fill('#pq-email', 'test@example.com'); await page.fill('#pq-phone', '9185550100');
        await page.click('[data-panel="3"] button[type=submit]'); await page.waitForTimeout(300);
        const st3 = await page.evaluate(() => ({ err: getComputedStyle(document.getElementById('pq-consent-err')).display, wrapErr: document.querySelector('.pq-consent').classList.contains('err'), formShown: document.getElementById('pqForm').style.display !== 'none' }));
        ok('submit blocked without consent', st3.err === 'block' && st3.wrapErr && st3.formShown && posts.length === 0, JSON.stringify(st3));
        await page.check('#pq-consent');
        ok('consent error clears on check', (await page.evaluate(() => getComputedStyle(document.getElementById('pq-consent-err')).display)) === 'none');
        await page.click('[data-panel="3"] button[type=submit]');
        await page.waitForURL('**/booked-stub', { timeout: 8000 }).catch(() => {});
        const booked = await page.evaluate(() => !!document.getElementById('booked'));
        ok('lead posted + redirected to booking', booked && posts.length === 1, `posts=${posts.length}`);
        if (posts[0]) {
          const p0 = posts[0];
          ok('payload: ZIPs + vehicle + consent', p0.origin_postal_code === '74119' && p0.destination_postal_code === '75201' && p0.vehicle_make === undefined && p0.vehicles[0].vehicle_make === 'Toyota' && p0.vehicles[0].vehicle_type === 'SUV' && /YES/.test(p0.customer_comments) && /^WEB-\d+$/.test(p0.secondary_id), JSON.stringify({ o: p0.origin_postal_code, d: p0.destination_postal_code, v: p0.vehicles[0], c: p0.customer_comments }));
        }
      }
      ok(`${label} no JS errors`, errors.length === 0, errors.join(' | ').slice(0, 200));
      await ctx.close();
    }
    console.log(`\n=== ${slug} ===`); console.log(log.join('\n'));
  }
  await browser.close();
  console.log(`\nTOTAL FAILURES: ${failures}`);
  process.exit(failures ? 1 : 0);
})();
