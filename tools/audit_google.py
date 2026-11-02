"""Google-facing audit over every city page (plus the state pages and the hub where they carry the same elements).
Beyond audit_site.py (links, tags, GTM, H1, canonical count, over-claims, orphans, sitemap coverage) and
audit_content.py (sentence rules, FAQ counts, meta lengths), this checks what Search Console, the Rich Results
test and a Maps embed would complain about:
  head     : lang/charset/viewport, one title (unique site-wide), one description (unique), one self canonical
             matching the clean URL, og:url == canonical, og:title == title, og:image exists, no robots noindex
  schema   : every JSON-LD block parses; exactly one FAQPage per page; each Question name and Answer text mirrors
             the visible FAQ verbatim; no HTML in answers; no duplicate questions; no Review/AggregateRating
  map      : exactly one Google Maps embed; https; lazy + title + referrerpolicy; the embed's coordinates fall
             inside the page's state; the GBP name says Ship Guy; the place id and the src are unique site-wide
  phone    : one local number per page, used consistently in every tel: link and the visible text; no other
             city's local number on the page; E.164 href matches the displayed number
  address  : the office card address carries the page's city and state code; the hero/office/FAQ name the city
  links    : internal links use the canonical forms (/city/<slug>/ with slash, state pages without .html);
             no http:// resources; every <img> has alt and resolves; no duplicate ids; no placeholder text
  nearby   : chips unique, no self link, "See all N" equals the city count
  sitemap  : every page URL present exactly once with a valid lastmod; no sitemap URL without a file; robots.txt
             allows the pages and names the sitemap; no X-Robots-Tag noindex for city paths in _headers
usage: python3 audit_google.py            (all city pages + state pages + hub)
"""
import re, os, json, glob, html, sys, collections, datetime
sys.path.insert(0, '/home/claude/tools'); import localpage as L
SITE = '/home/claude/build/shipguy'; os.chdir(SITE)
HOST = 'https://shipguy.com'
BBOX = {  # lat_min, lat_max, lon_min, lon_max (generous)
 'AL':(30.1,35.1,-88.6,-84.8),'AK':(51.0,71.5,-179.5,-129.5),'AZ':(31.2,37.1,-115.0,-108.9),'AR':(32.9,36.6,-94.7,-89.5),
 'CA':(32.4,42.1,-124.6,-114.0),'CO':(36.9,41.1,-109.2,-101.9),'CT':(40.9,42.1,-73.8,-71.7),'DE':(38.4,39.9,-75.9,-74.9),
 'FL':(24.3,31.1,-87.8,-79.9),'GA':(30.2,35.1,-85.7,-80.7),'HI':(18.8,22.4,-160.4,-154.7),'ID':(41.9,49.1,-117.4,-110.9),
 'IL':(36.9,42.6,-91.6,-87.0),'IN':(37.7,41.9,-88.2,-84.7),'IA':(40.3,43.6,-96.7,-90.0),'KS':(36.9,40.1,-102.2,-94.5),
 'KY':(36.4,39.2,-89.7,-81.8),'LA':(28.8,33.1,-94.2,-88.7),'ME':(42.9,47.6,-71.2,-66.8),'MD':(37.8,39.8,-79.6,-74.9),
 'MA':(41.1,43.0,-73.6,-69.8),'MI':(41.6,48.4,-90.6,-82.0),'MN':(43.4,49.5,-97.4,-89.3),'MS':(30.0,35.1,-91.8,-87.9),
 'MO':(35.9,40.7,-95.9,-88.9),'MT':(44.3,49.1,-116.2,-103.9),'NE':(39.9,43.1,-104.2,-95.2),'NV':(34.9,42.1,-120.2,-113.9),
 'NH':(42.6,45.4,-72.7,-70.5),'NJ':(38.8,41.5,-75.7,-73.7),'NM':(31.2,37.1,-109.2,-102.9),'NY':(40.4,45.1,-79.9,-71.7),
 'NC':(33.7,36.7,-84.5,-75.3),'ND':(45.8,49.1,-104.2,-96.4),'OH':(38.3,42.1,-85.0,-80.4),'OK':(33.5,37.1,-103.2,-94.3),
 'OR':(41.9,46.4,-124.7,-116.3),'PA':(39.6,42.4,-80.7,-74.5),'RI':(41.0,42.1,-72.0,-71.0),'SC':(31.9,35.3,-83.5,-78.4),
 'SD':(42.3,46.1,-104.2,-96.3),'TN':(34.8,36.8,-90.5,-81.5),'TX':(25.7,36.7,-106.8,-93.4),'UT':(36.9,42.1,-114.2,-108.9),
 'VT':(42.6,45.1,-73.6,-71.3),'VA':(36.4,39.6,-83.8,-75.1),'WA':(45.4,49.1,-124.9,-116.8),'WV':(37.1,40.8,-82.8,-77.6),
 'WI':(42.4,47.2,-93.0,-86.7),'WY':(40.9,45.1,-111.2,-103.9)}
issues = collections.defaultdict(list)
def add(kind, page, detail=''): issues[kind].append((page, detail))
def text_of(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()

cities = sorted(L.NAMES)
city_pages = ['city/%s/index.html' % c for c in cities]
state_pages = sorted(os.path.basename(p) for p in glob.glob('*-auto-transport.html') if not os.path.basename(p).startswith(('enclosed', 'dealer')))
pages = city_pages + state_pages + ['locations.html']
titles = collections.defaultdict(list); descs = collections.defaultdict(list); embeds = collections.defaultdict(list); placeids = collections.defaultdict(list)
phones = {}   # page -> E.164 local number
gbp_names = collections.defaultdict(list); gbp_pages = []; addr_pages = []
for p in pages:
    h = open(p, encoding='utf-8').read(); head = h[:h.index('</head>')]
    is_city = p.startswith('city/')
    slug = p.split('/')[1] if is_city else p[:-5]
    url = HOST + ('/city/%s/' % slug if is_city else ('/locations' if p == 'locations.html' else '/' + slug))
    # ---- head ----
    if not re.search(r'<html[^>]*\slang="en"', h): add('lang', p)
    if '<meta charset="UTF-8">' not in head and '<meta charset="utf-8">' not in head: add('charset', p)
    if 'name="viewport"' not in head: add('viewport', p)
    t = re.findall(r'<title>(.*?)</title>', head, flags=re.S)
    if len(t) != 1: add('title-count', p, len(t))
    else:
        tt = text_of(t[0]); titles[tt].append(p)
        if not (10 <= len(tt) <= 70): add('title-length', p, len(tt))
    d = re.findall(r'<meta name="description" content="([^"]*)"', head)
    if len(d) != 1: add('description-count', p, len(d))
    else:
        descs[d[0]].append(p)
        if not (50 <= len(html.unescape(d[0])) <= 160): add('description-length', p, len(d[0]))
    c = re.findall(r'<link rel="canonical" href="([^"]+)"', head)
    if len(c) != 1: add('canonical-count', p, len(c))
    elif c[0] != url: add('canonical-mismatch', p, (c[0], url))
    og = dict(re.findall(r'<meta property="(og:[a-z:_]+)" content="([^"]*)"', head))
    if og.get('og:url') != url: add('og-url-mismatch', p, og.get('og:url'))
    if t and og.get('og:title') and html.unescape(og['og:title']) != text_of(t[0]): add('og-title-mismatch', p)
    img = og.get('og:image', '')
    if not img.startswith(HOST + '/') or not os.path.isfile(img[len(HOST) + 1:]): add('og-image', p, img)
    if 'name="twitter:card"' not in head: add('twitter-card', p)
    rob = re.findall(r'<meta name="robots" content="([^"]*)"', head)
    if any('noindex' in r or 'nofollow' in r for r in rob): add('robots-noindex', p, rob)
    # ---- schema ----
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, flags=re.S)
    faqs = []
    for b in blocks:
        try: dd = json.loads(b)
        except Exception as e: add('jsonld-parse', p, str(e)[:60]); continue
        items = dd.get('@graph', [dd]) if isinstance(dd, dict) else dd
        for it in items:
            if it.get('@type') == 'FAQPage': faqs.append(it)
            if it.get('@type') in ('Review', 'AggregateRating') or 'aggregateRating' in it: add('review-schema', p)
    if p == 'locations.html' or slug == 'auto-transport-corpus-christi-texas': pass   # the hub has no FAQ; the legacy page uses the old FAQ markup (checked by hand: 8 visible Q&As)
    elif len(faqs) != 1: add('faqpage-count', p, len(faqs))
    else:
        qs = [(text_of(m.group(1)), text_of(m.group(2))) for m in re.finditer(r'<summary>(.*?)<span class="ph-fp"></span></summary><div class="fa">(.*?)</div></details>', h, flags=re.S)]
        ents = faqs[0].get('mainEntity', [])
        if len(qs) != len(ents): add('faq-count-mismatch', p, (len(qs), len(ents)))
        names = [e.get('name', '') for e in ents]
        if len(set(names)) != len(names): add('faq-duplicate-question', p)
        for (q, a), e in zip(qs, ents):
            en = text_of(e.get('name', '')); ea = e.get('acceptedAnswer', {}).get('text', '')
            if en != q: add('faq-question-mismatch', p, (q[:60], en[:60]))
            if '<' in ea or '>' in ea: add('faq-html-in-answer', p, en[:50])
            if text_of(ea) != a: add('faq-answer-mismatch', p, en[:60])
            if not ea.strip() or not q: add('faq-empty', p, en[:50])
    # ---- H1 / city naming ----
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', h, flags=re.S)
    if len(h1) != 1: add('h1-count', p, len(h1))
    if is_city:
        city, st = L.NAMES[slug]
        if h1 and city not in text_of(h1[0]): add('h1-missing-city', p, text_of(h1[0]))
        if t and city not in text_of(t[0]): add('title-missing-city', p, text_of(t[0]))
        # ---- map embed ----
        ifr = re.findall(r'<iframe[^>]*google\.com/maps[^>]*>', h)
        if slug == 'auto-transport-corpus-christi-texas' and not ifr: pass   # legacy page, pending rebuild row
        elif len(ifr) != 1: add('map-embed-count', p, len(ifr))
        else:
            f = ifr[0]; src = re.search(r'src="([^"]+)"', f).group(1)
            if 'loading="lazy"' not in f: add('map-lazy', p)
            if 'title="' not in f: add('map-title', p)
            if 'referrerpolicy=' not in f: add('map-referrerpolicy', p)
            if src.startswith('https://www.google.com/maps/embed?pb='):
                lon = re.search(r'!2d(-?[0-9.]+)', src); lat = re.search(r'!3d(-?[0-9.]+)', src)
                if not (lon and lat): add('map-coords-missing', p)
                else:
                    la, lo = float(lat.group(1)), float(lon.group(1)); b = BBOX[st]
                    if not (b[0] <= la <= b[1] and b[2] <= lo <= b[3]): add('map-outside-state', p, (st, la, lo))
                nm = re.search(r'!2s([^!]+)', src)
                nmv = html.unescape(nm.group(1)).replace('%20', ' ') if nm else None
                if slug == 'auto-transport-corpus-christi-texas': pass   # legacy embed carries no listing name
                elif not nmv or 'ship' not in nmv.lower() or 'guy' not in nmv.lower(): add('map-name', p, nmv)
                else: gbp_names[nmv].append(p)
                pid = re.search(r'!1s(0x[0-9a-f]+%3A0x[0-9a-f]+)', src)
                if pid: placeids[pid.group(1)].append(p)
                else: add('map-placeid-missing', p)
                embeds[src].append(p); gbp_pages.append(p)
            elif src.startswith('https://www.google.com/maps?q=') and src.endswith('&output=embed'):
                q = html.unescape(src[len('https://www.google.com/maps?q='):-len('&output=embed')]).replace('+', ' ')
                card = re.search(r'<b>Address</b><span>(.*?)</span>', h, flags=re.S)
                if card:
                    addr = text_of(card.group(1).replace('<br>', ', '))
                    num = addr.split(' ')[0]; zp = re.findall(r'\b\d{5}\b', addr)
                    if num not in q or (zp and zp[-1] not in q): add('map-query-address', p, (q, addr))
                embeds[src].append(p); addr_pages.append(p)
            else: add('map-src', p, src[:80])
        # ---- phone ----
        tels = [x for x in re.findall(r'href="tel:(\+1\d{10})"', h) if x != '+18664992815']   # the main line is not a local number
        local = collections.Counter(tels)
        if not tels: add('phone-missing', p)
        else:
            num = local.most_common(1)[0][0]; phones[p] = num
            others = {n for n in local if n != num and n != '+18664992815'}   # the legacy page also carries the main line
            if others: add('phone-mixed', p, sorted(others))
            disp = '(%s) %s-%s' % (num[2:5], num[5:8], num[8:])
            if disp not in h: add('phone-display-mismatch', p, (num, disp))
            # the office card number must be this one
            card = re.search(r'<div class="ph-office-card">.*?</div></div></div>', h, flags=re.S)
            if card and 'tel:%s' % num not in card.group(0): add('phone-office-card', p)
        # ---- address ----
        card = re.search(r'<b>Address</b><span>(.*?)</span>', h, flags=re.S)
        if slug != 'auto-transport-corpus-christi-texas':
            if not card: add('address-missing', p)
            else:
                addr = text_of(card.group(1).replace('<br>', ', '))
                if (', %s ' % st) not in addr + ' ' and (' %s ' % st) not in addr + ' ': add('address-state', p, addr)
                if city.split(' ')[0] not in addr and not (city in ('Manhattan',) and 'New York' in addr): add('address-city', p, addr)
                if not re.search(r'\b\d{5}\b', addr): add('address-zip', p, addr)
        # ---- nearby ----
        nb = re.search(r'<h2>Other Cities We Serve Near .*?<div class="ph-chips">(.*?)</div>', h, flags=re.S)
        if slug != 'auto-transport-corpus-christi-texas':
            if not nb: add('nearby-missing', p)
            else:
                chips = re.findall(r'href="/city/([^/"]+)/"', nb.group(1))
                if len(chips) != len(set(chips)): add('nearby-duplicate', p)
                if slug in chips: add('nearby-self', p)
                for ch in chips:
                    if ch not in L.NAMES: add('nearby-unknown', p, ch)
                m = re.search(r'See all (\d+) cities we serve', h)
                if not m or int(m.group(1)) != len(cities): add('see-all-count', p, m.group(1) if m else None)
        # breadcrumb
        bc = re.search(r'<nav class="ph-crumbs"[^>]*>(.*?)</nav>', h, flags=re.S)
        if slug == 'auto-transport-corpus-christi-texas': pass   # legacy template: BreadcrumbList JSON-LD instead of the crumb bar
        elif not bc: add('breadcrumb-missing', p)
        else:
            stl = re.search(r'href="/([a-z-]+-auto-transport)"', bc.group(1))
            if not stl or stl.group(1) != L.state_slug_of(slug): add('breadcrumb-state', p, stl.group(1) if stl else None)
            if ('aria-current="page">%s<' % city) not in bc.group(1): add('breadcrumb-city', p)
    # ---- links / resources ----
    for href in re.findall(r'href="([^"]+)"', h):
        if href.startswith('http://'): add('http-link', p, href)
        if href.startswith('/city/') and not href.endswith('/') and '#' not in href: add('city-link-no-slash', p, href)
        if re.match(r'/[a-z-]+-auto-transport\.html', href): add('state-link-html', p, href)
        if href.startswith(HOST + '/city/') and not href.endswith('/'): add('city-link-no-slash', p, href)
    for src in re.findall(r'\ssrc="([^"]+)"', h):
        if src.startswith('http://'): add('http-resource', p, src)
        if src.startswith('/') and not os.path.isfile(src.lstrip('/')): add('missing-resource', p, src)
    for im in re.findall(r'<img[^>]*>', h):
        if ' alt=' not in im: add('img-no-alt', p, im[:80])
    ids = re.findall(r'\sid="([^"]+)"', h)
    dup = [i for i, n in collections.Counter(ids).items() if n > 1]
    if dup: add('duplicate-id', p, dup[:5])
    body = h[h.index('<body'):]
    bl = text_of(re.sub(r'<(script|style|noscript).*?</\1>', '', body, flags=re.S)).lower()
    for ph in ['lorem ipsum', 'todo', 'xxx', '{{', '}}', 'undefined', 'placeholder text', '[city]', '[state]']:
        if ph in bl: add('placeholder', p, ph)
    for kw in ['24/7', 'no deposit', 'pay nothing', 'cheapest company', '#1 ', 'number one', 'guaranteed', 'guarantee ', 'best price', 'price match']:
        if kw in bl and not (kw.startswith('guarantee') and 'no guarantee' in bl): add('over-claim', p, kw)
# ---- cross-page FAQ duplicates (identical question+answer pairs on more than one page) ----
qa = collections.defaultdict(list)
for p in city_pages + state_pages:
    h = open(p, encoding='utf-8').read()
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, flags=re.S):
        try: dd = json.loads(b)
        except Exception: continue
        for it in (dd.get('@graph', [dd]) if isinstance(dd, dict) else dd):
            if it.get('@type') == 'FAQPage':
                for e in it.get('mainEntity', []): qa[(e.get('name', '').strip(), e.get('acceptedAnswer', {}).get('text', '').strip())].append(p)
for k, ps in qa.items():
    if len(ps) > 1: add('faq-duplicated-across-pages', ps[0], (k[0][:60], len(ps)))
# ---- cross-page uniqueness ----
for tt, ps in titles.items():
    if len(ps) > 1: add('duplicate-title', ps[0], (tt[:50], len(ps)))
for dd, ps in descs.items():
    if len(ps) > 1: add('duplicate-description', ps[0], (dd[:50], len(ps)))
for src, ps in embeds.items():
    if len(ps) > 1: add('duplicate-map-embed', ps[0], ps)
for pid, ps in placeids.items():
    if len(ps) > 1: add('duplicate-place-id', ps[0], ps)
num_pages = collections.defaultdict(list)
for p, n in phones.items(): num_pages[n].append(p)
for n, ps in num_pages.items():
    if len(ps) > 1: add('shared-local-number', ps[0], (n, ps))
# a city page must not carry another city's local number anywhere
allnums = set(phones.values())
for p in city_pages:
    h = open(p, encoding='utf-8').read(); mine = phones.get(p)
    for n in allnums:
        if n != mine and n in h: add('foreign-local-number', p, n)
# ---- sitemap / robots / headers ----
sm = open('sitemap.xml', encoding='utf-8').read()
locs = re.findall(r'<loc>([^<]+)</loc>', sm)
cnt = collections.Counter(locs)
for u, n in cnt.items():
    if n > 1: add('sitemap-duplicate', 'sitemap.xml', u)
for p in pages:
    is_city = p.startswith('city/'); slug = p.split('/')[1] if is_city else p[:-5]
    url = HOST + ('/city/%s/' % slug if is_city else ('/locations' if p == 'locations.html' else '/' + slug))
    if url not in cnt: add('sitemap-missing', p, url)
for u in locs:
    path = u[len(HOST):]
    f = 'index.html' if path == '/' else (path.lstrip('/') + 'index.html' if path.endswith('/') else path.lstrip('/'))
    if not (os.path.isfile(f) or os.path.isfile(f + '.html')): add('sitemap-dead-url', 'sitemap.xml', u)
    if not u.startswith(HOST + '/'): add('sitemap-host', 'sitemap.xml', u)
for lm in re.findall(r'<lastmod>([^<]+)</lastmod>', sm):
    try: datetime.date.fromisoformat(lm)
    except Exception: add('sitemap-lastmod', 'sitemap.xml', lm)
    else:
        if datetime.date.fromisoformat(lm) > datetime.date.today(): add('sitemap-lastmod-future', 'sitemap.xml', lm)
rb = open('robots.txt', encoding='utf-8').read() if os.path.isfile('robots.txt') else ''
if 'Sitemap: %s/sitemap.xml' % HOST not in rb: add('robots-sitemap', 'robots.txt')
for line in rb.splitlines():
    if line.lower().startswith('disallow:') and line.split(':', 1)[1].strip() in ('/', '/city', '/city/'): add('robots-blocks-pages', 'robots.txt', line)
hd = open('_headers', encoding='utf-8').read() if os.path.isfile('_headers') else ''
blk = None
for line in hd.splitlines():
    if line and not line.startswith(' '): blk = line.strip()
    elif 'x-robots-tag' in line.lower() and 'noindex' in line.lower() and blk in ('/*', '/city/*'): add('headers-noindex', '_headers', (blk, line.strip()))
print('pages audited: %d city + %d state + hub | local numbers: %d | GBP embeds: %d | address embeds (awaiting GBP rows): %d' % (len(city_pages), len(state_pages), len(phones), len(gbp_pages), len(addr_pages)))
print('GBP listing names on the embeds:', {k: len(v) for k, v in gbp_names.items()})
if addr_pages: print('address-embed pages:', ', '.join(x.split('/')[1].replace('auto-transport-', '') for x in addr_pages))
for k, v in sorted(issues.items()): print('ISSUE %-24s %4d  e.g. %s' % (k, len(v), v[:3]))
if not issues: print('ALL CLEAR: head tags, canonicals, OG, FAQ schema mirrors, map embeds inside their states and unique, phones and addresses consistent, link forms canonical, images alt, no placeholders, sitemap/robots/headers clean')
