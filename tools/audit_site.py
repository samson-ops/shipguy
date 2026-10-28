"""Full-site audit over the generated set (50 state pages + city pages + core pages).
Checks: internal links resolve, anchors exist, tag balance, JSON-LD parses, GTM x2, one H1, one canonical,
no review schema, over-claims, orphans (no inbound link), hub/state/city interlinking, sitemap coverage."""
import re, os, json, glob, collections, sys
sys.path.insert(0, '/home/claude/tools'); import localpage as L
SITE = '/home/claude/build/shipguy'; os.chdir(SITE)
states = sorted(os.path.basename(p)[:-5] for p in glob.glob('*-auto-transport.html') if not p.startswith(('enclosed', 'dealer')))   # dealer-auto-transport is a legacy page redirected by _redirects
cities = sorted(L.NAMES)
core = ['index.html','how-it-works.html','services.html','locations.html','faq.html','contact.html','car-shipping-cost.html','car-shipping-preparation.html',
        'cross-country-car-shipping.html','open-car-transport.html','enclosed-auto-transport.html','door-to-door-car-shipping.html','state-to-state-car-shipping.html',
        'expedited-car-shipping.html','snowbird-car-shipping.html','military-car-shipping.html','auction-car-transport.html','privacy-policy.html','terms.html','404.html',
        'vehicle-quote.html','vehicle-quote/index.html'] + sorted(glob.glob('vehicle-quote-*-*.html'))   # Ads landing pages: vehicle-quote-<city>-<state>.html
pages = [s + '.html' for s in states] + ['city/%s/index.html' % c for c in cities] + [c for c in core if os.path.isfile(c)]
issues = collections.defaultdict(list)
ids = {p: set(re.findall(r'\sid="([^"]+)"', open(p, encoding='utf-8').read())) for p in pages}
def canon(href):
    p = href.split('#')[0].split('?')[0]
    if p.startswith('https://shipguy.com'): p = p[len('https://shipguy.com'):]
    if not p.startswith('/'): return None
    if p == '/': return 'index.html'
    if p.endswith('/'): return p.lstrip('/') + 'index.html'
    p = p.lstrip('/'); return p if os.path.isfile(p) else (p + '.html' if os.path.isfile(p + '.html') else None)
out = {}; inbound = collections.defaultdict(set)
for p in pages:
    h = open(p, encoding='utf-8').read(); low = h.lower(); links = set()
    for href in re.findall(r'href="([^"]+)"', h):
        if href.startswith(('http', 'tel:', 'mailto:', 'data:', 'javascript:')) and 'shipguy.com' not in href: continue
        if href.startswith('#'):
            if href[1:] and href[1:] not in ids[p]: issues['broken-anchor'].append((p, href))
            continue
        if re.match(r'[a-z0-9-]+\.html', href): issues['relative-html-link'].append((p, href)); continue
        t = canon(href)
        if href.startswith('/') and t is None: issues['broken-link'].append((p, href)); continue
        if t and '#' in href and href.split('#')[1] not in ids.get(t, set()): issues['broken-anchor'].append((p, href))
        if t and t != p: links.add(t)
    out[p] = links
    for t in links: inbound[t].add(p)
    for tag in ['div', 'section', 'details', 'table', 'ul', 'p', 'a', 'style', 'script', 'footer', 'header', 'nav', 'form', 'label']:
        if len(re.findall(r'<%s[\s>]' % tag, h)) != h.count('</%s>' % tag): issues['tag-imbalance'].append((p, tag))
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, flags=re.S):
        try: json.loads(b)
        except Exception as e: issues['bad-jsonld'].append((p, str(e)[:40]))
    if h.count('GTM-MQ7HKJTJ') != 2: issues['gtm'].append((p, h.count('GTM-MQ7HKJTJ')))
    if h.count('<h1') != 1: issues['h1-count'].append((p, h.count('<h1')))
    if h.count('rel="canonical"') != 1 and p != '404.html': issues['canonical-count'].append((p, h.count('rel="canonical"')))
    if 'AggregateRating' in h or '"Review"' in h: issues['review-schema'].append(p)
    for kw in ['24/7', 'no deposit', 'pay nothing', 'cheapest company', '#1 ', 'number one']:
        if kw in low: issues['over-claim'].append((p, kw))
    if 'id="pqForm"' in h:
        if 'data-zipfield' not in h: issues['zip-lock-missing'].append(p)
        if 'pq-consent-err' not in h: issues['consent-gate-missing'].append(p)
skip = {'vehicle-quote.html', 'vehicle-quote/index.html', '404.html', 'privacy-policy.html', 'terms.html'} | set(glob.glob('vehicle-quote-*-*.html'))   # Ads pages are noindex and unlinked on purpose
orphans = [p for p in pages if p not in skip and not inbound[p]]
if orphans: issues['orphan'] = orphans
# hub + state + city interlinking
hub = out.get('locations.html', set())
miss_hub = [c for c in cities if 'city/%s/index.html' % c not in hub]
if miss_hub: issues['hub-missing-city'] = miss_hub
for c in cities:
    st = L.state_slug_of(c) + '.html'
    if st not in out['city/%s/index.html' % c]: issues['city-missing-state-link'].append(c)
    if 'city/%s/index.html' % c not in out.get(st, set()): issues['state-missing-city-link'].append((st, c))
sm = open('sitemap.xml', encoding='utf-8').read()
for c in cities:
    if 'https://shipguy.com/city/%s/' % c not in sm: issues['sitemap-missing'].append(c)
for s in states:
    if 'https://shipguy.com/%s<' % s not in sm: issues['sitemap-missing'].append(s)
print('pages audited: %d (%d state + %d city + %d core)' % (len(pages), len(states), len(cities), len(pages) - len(states) - len(cities)))
print('sitemap urls:', sm.count('<loc>'), '| hub city links:', sum(1 for c in cities if 'city/%s/index.html' % c in hub), '/', len(cities))
for c in ['auto-transport-virginia-beach-virginia', 'auto-transport-pittsburgh-pennsylvania', 'auto-transport-allentown-pennsylvania', 'auto-transport-reading-pennsylvania']:
    print('inbound to %-36s %2d pages e.g. %s' % (c, len(inbound['city/%s/index.html' % c]), sorted(inbound['city/%s/index.html' % c])[:4]))
for k, v in issues.items(): print('ISSUE', k, len(v), v[:5])
if not issues: print('ALL CLEAR: links resolve, anchors exist, tags balanced, JSON-LD valid, GTM x2, one H1, one canonical, no review schema, no over-claims, no orphans, hub/state/city interlinked, sitemap complete, zip lock + consent gate on every tool page')
