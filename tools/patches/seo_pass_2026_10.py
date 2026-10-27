"""Site-wide SEO / best-practice pass (Oct 27, 2026). Idempotent where it adds blocks; asserts on one-off edits."""
import re, sys, glob, json, os
sys.path.insert(0, '/home/claude/tools'); import localpage as lp, seo_enrich as se
S = '/home/claude/build/shipguy/'
TODAY = '2026-10-27'
def rd(p): return open(S + p, encoding='utf-8').read()
def wr(p, h): open(S + p, 'w', encoding='utf-8').write(h)
def rep(h, old, new, n=1):
    c = h.count(old); assert c == n, (c, old[:80]); return h.replace(old, new)

# 1) city pages: breadcrumb + BreadcrumbList + LocalBusiness (built pages only; Corpus Christi keeps its own)
done = 0
for slug, (city, st) in sorted(lp.NAMES.items()):
    if slug == 'auto-transport-corpus-christi-texas': continue
    p = 'city/%s/index.html' % slug; h = rd(p)
    h2 = se.enrich_city(h, slug, city, lp.STATE_NAMES[st], lp.state_slug_of(slug))
    assert 'id="sg-localbusiness"' in h2, slug
    wr(p, h2); done += 1
print('city pages enriched:', done)

# 2) state pages: breadcrumb + BreadcrumbList
n = 0
for st, name in lp.STATE_NAMES.items():
    p = name.lower().replace(' ', '-') + '-auto-transport.html'
    if not os.path.exists(S + p): print('MISSING STATE PAGE', p); continue
    wr(p, se.enrich_state(rd(p), name, p[:-5])); n += 1
print('state pages enriched:', n)

# 3) home: Organization + WebSite
wr('index.html', se.enrich_home(rd('index.html'))); print('home enriched')

# 4) services.html: absolute breadcrumb items
for p, leaf in [('services.html', 'services'), ('contact.html', 'contact')]:
    h = rd(p)
    h = h.replace('"item":"index.html"', '"item":"https://shipguy.com/"').replace('"item":"%s.html"' % leaf, '"item":"https://shipguy.com/%s"' % leaf)
    wr(p, h); print('breadcrumb items made absolute:', p)

# 5) broken / overlong meta descriptions and titles (title, og:title, twitter:title are the same string x3)
h = rd('how-it-works.html')
NEWDESC = 'How auto transport works with Ship Guy, step by step: the quote, the carrier match, the pickup inspection, transit, and delivery. Free quote.'
assert 110 <= len(NEWDESC) <= 160, len(NEWDESC)
h = h.replace('content=" Free quote."', 'content="%s"' % NEWDESC)
wr('how-it-works.html', h); print('how-it-works meta fixed')
h = rd('locations.html')
old = 'Every Ship Guy city page in one place, grouped by state. One hundred sixty-six local auto transport guides with lanes, neighborhoods, and a local phone line. Free quote.'
new = 'Every Ship Guy city page in one place, grouped by state. Local auto transport guides with lanes, neighborhoods, and a phone line for each city. Free quote.'
assert 110 <= len(new) <= 160, len(new)
h = h.replace(old, new); wr('locations.html', h); print('locations meta trimmed')
TITLES = {
 'auction-car-transport.html': ('Auction &amp; Dealer Car Shipping | Nationwide Auto Auction Transport | Ship Guy', 'Auction &amp; Dealer Car Shipping Nationwide | Ship Guy'),
 'car-shipping-cost.html': ('Car Shipping Cost — How Much Does It Cost to Ship a Car? | Ship Guy', 'Car Shipping Cost — How Much to Ship a Car? | Ship Guy'),
 'cross-country-car-shipping.html': ('Cross-Country Car Shipping — Coast-to-Coast Auto Transport | Ship Guy', 'Cross-Country Car Shipping, Coast to Coast | Ship Guy'),
 'military-car-shipping.html': ('Military Car Shipping | PCS &amp; Deployment Auto Transport | Ship Guy', 'Military Car Shipping | PCS &amp; Deployment Moves | Ship Guy'),
 'open-car-transport.html': ('Open Car Transport | Affordable Nationwide Auto Shipping | Ship Guy', 'Open Car Transport | Nationwide Auto Shipping | Ship Guy'),
 'services.html': ('Car Shipping Services | Open, Enclosed, Door-to-Door &amp; More | Ship Guy', 'Car Shipping Services | Open, Enclosed &amp; Door-to-Door | Ship Guy'),
 'state-to-state-car-shipping.html': ('State-to-State Car Shipping | Interstate Auto Transport | Ship Guy', 'State-to-State Car Shipping | Interstate Transport | Ship Guy'),
 'city/auto-transport-corpus-christi-texas/index.html': ('Corpus Christi Auto Transport — Coastal Bend Car Shipping | Ship Guy', 'Car Shipping in Corpus Christi, TX — Auto Transport | Ship Guy'),
}
for p, (old, new) in TITLES.items():
    h = rd(p); c = h.count(old) + h.count(old.replace('&amp;', '&')); assert c >= 3, (p, c)
    assert len(new.replace('&amp;', '&')) <= 65, (p, len(new))
    h = h.replace(old, new).replace(old.replace('&amp;', '&'), new.replace('&amp;', '&'))
    wr(p, h); print('title trimmed', p, c)

# 6) legacy prose semicolons (house style)
SEMI = {
 'city/auto-transport-anaheim-california/index.html': [('Larger vehicles run roughly 10 to 25 percent more; enclosed runs higher still', 'Larger vehicles run roughly 10 to 25 percent more. Enclosed runs higher still')],
 'city/auto-transport-anchorage-alaska/index.html': [('The ocean leg is the constant; the highway miles are what vary', 'The ocean leg is the constant. The highway miles are what vary')],
 'city/auto-transport-atlanta-georgia/index.html': [('SUVs and pickups run 10 to 25 percent higher; enclosed higher still', 'SUVs and pickups run 10 to 25 percent higher. Enclosed runs higher still')],
 'city/auto-transport-chicago-illinois/index.html': [('SUVs and trucks add roughly 10 to 25 percent; enclosed adds more', 'SUVs and trucks add roughly 10 to 25 percent. Enclosed adds more')],
 'city/auto-transport-detroit-michigan/index.html': [('SUVs and trucks add about 10 to 25 percent; enclosed adds more', 'SUVs and trucks add about 10 to 25 percent. Enclosed adds more')],
 'city/auto-transport-durham-north-carolina/index.html': [('SUVs and pickups cost about 10 to 25 percent more; enclosed costs more still', 'SUVs and pickups cost about 10 to 25 percent more. Enclosed costs more still')],
 'city/auto-transport-honolulu-hawaii/index.html': [('The crossing is the fixed part; the highway miles are what vary', 'The crossing is the fixed part. The highway miles are what vary')],
 'city/auto-transport-key-west-florida/index.html': [('Estimated open-transport ranges below; price your exact route above', 'Estimated open-transport ranges below. Price your exact route above')],
 'city/auto-transport-lexington-kentucky/index.html': [('SUVs and pickups add roughly 10 to 25 percent; enclosed adds more', 'SUVs and pickups add roughly 10 to 25 percent. Enclosed adds more')],
 'city/auto-transport-philadelphia-pennsylvania/index.html': [('Larger vehicles add about 10 to 25 percent; enclosed adds more', 'Larger vehicles add about 10 to 25 percent. Enclosed adds more')],
 'city/auto-transport-salt-lake-city-utah/index.html': [('The trucks are not ours; we book them', 'The trucks are not ours. We book them')],
 'city/auto-transport-west-palm-beach-florida/index.html': [('Larger vehicles add roughly 10 to 25 percent; enclosed adds more', 'Larger vehicles add roughly 10 to 25 percent. Enclosed adds more')],
 'city/auto-transport-wichita-kansas/index.html': [('Ship Guy has no military affiliation; we are a private broker', 'Ship Guy has no military affiliation. We are a private broker')],
 'car-shipping-cost.html': [('open is the practical choice; enclosed is worth the premium', 'open is the practical choice. Enclosed is worth the premium')],
 'car-shipping-preparation.html': [("There's no need to wax or detail; a basic clean is all you need", "There's no need to wax or detail. A basic clean is all you need"),
                                   ('it adds weight for no benefit; a quarter tank is ideal', 'it adds weight for no benefit. A quarter tank is ideal')],
}
for p, pairs in SEMI.items():
    h = rd(p)
    for old, new in pairs:
        c = h.count(old); assert c >= 1, (p, old[:50]); h = h.replace(old, new)
    wr(p, h)
print('semicolons fixed on', len(SEMI), 'pages')

# 7) legacy Corpus Christi page: home crumb link to the clean URL
h = rd('city/auto-transport-corpus-christi-texas/index.html')
h = rep(h, '<a href="/index.html">Home</a>', '<a href="/">Home</a>')
wr('city/auto-transport-corpus-christi-texas/index.html', h); print('corpus christi crumb fixed')

# 8) Texas City Pages block + hub row + counts + sitemap now that Corpus Christi is registered (167)
BLOCK = re.compile(r'<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">City Pages</p>.*?</section>', re.S)
h = rd('texas-auto-transport.html')
intro = ('Eight Texas cities have their own pages with local lanes, meeting spots, and phone lines. '
         'The Valley, the Permian Basin, Lubbock, Amarillo, Waco, College Station, Killeen, and the rest of Texas are covered from this page.')
assert BLOCK.search(h); h = BLOCK.sub(lambda m: lp.state_cities_block('TX', intro), h, count=1)
wr('texas-auto-transport.html', h); print('texas block regenerated (8)')
h = rd('locations.html')
key = '<h3>Texas</h3><div class="ph-chips">'; assert h.count(key) == 1
start = h.index(key) + len(key); end = h.index('</div>', start); assert '<div' not in h[start:end]
items = sorted([(name, slug) for slug, (name, s) in lp.NAMES.items() if s == 'TX'])
h = h[:start] + ''.join('<a class="ph-chip" href="/city/%s/">%s</a>' % (slug, name) for name, slug in items) + h[end:]
assert h.count('One hundred sixty-six') == 1 and h.count('one hundred sixty-six local pages') == 1, (h.count('One hundred sixty-six'), h.count('one hundred sixty-six local pages'))
h = h.replace('One hundred sixty-six', 'One hundred sixty-seven').replace('one hundred sixty-six local pages', 'one hundred sixty-seven local pages')
wr('locations.html', h); print('hub: Texas row + counts 167; hub chips', len(re.findall(r'<a class="ph-chip" href="/city/', h)))
c = 0
for p in glob.glob(S + 'city/*/index.html'):
    h = open(p, encoding='utf-8').read(); h2 = re.sub(r'See all \d+ cities we serve', 'See all %d cities we serve' % len(lp.NAMES), h)
    if h2 != h: open(p, 'w', encoding='utf-8').write(h2); c += 1
print('see-all 167 on', c, 'pages')
h = rd('sitemap.xml'); loc = 'https://shipguy.com/city/auto-transport-corpus-christi-texas/'
if loc not in h:
    h = h.replace('</urlset>', '<url><loc>%s</loc><lastmod>%s</lastmod><priority>0.8</priority></url>\n</urlset>' % (loc, TODAY))
wr('sitemap.xml', h); print('sitemap urls', h.count('<url>'))

# 9) headers / robots / redirects
h = rd('_headers')
if 'Strict-Transport-Security' not in h:
    h = rep(h, '  X-Content-Type-Options: nosniff\n', '  X-Content-Type-Options: nosniff\n  Strict-Transport-Security: max-age=31536000\n')
wr('_headers', h)
h = rd('robots.txt')
if '/tools/' not in h: h = rep(h, 'Allow: /\n', 'Allow: /\nDisallow: /tools/\n')
wr('robots.txt', h)
h = rd('_redirects')
if '/tools/*' not in h: h += '\n# ---- Oct 2026: build tooling is versioned in the repo but never served ----\n/tools/*                                         /  301\n'
wr('_redirects', h); print('headers/robots/redirects updated')
