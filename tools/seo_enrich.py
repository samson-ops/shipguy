#!/usr/bin/env python3
"""SEO enrichment applied to built pages (idempotent — every block it adds carries an id and is
replaced on re-run):
  * city pages  : visible breadcrumb (Home › Locations › State › City) + BreadcrumbList JSON-LD
                  + LocalBusiness JSON-LD built from the office card (address, phone, hours, map coords)
  * state pages : visible breadcrumb (Home › Locations › State) + BreadcrumbList JSON-LD
  * home page   : Organization + WebSite JSON-LD
localpage.build() calls enrich_city() on every new build; patches/seo_pass_2026_10.py ran it over the site."""
import re, json, html as H
from urllib.parse import quote_plus

SITE = 'https://shipguy.com'
ORG_PHONE = '+1-866-499-2815'          # the header/footer line used on 70 pages (the hero's 297-3244 is an open owner question)
ORG_EMAIL = 'quotes@shipguy.com'
ORG_SAMEAS = ['https://www.facebook.com/shipguylogistics/', 'https://www.instagram.com/ship_guy_logistics/']
ORG = {"@type": "Organization", "@id": SITE + '/#organization', "name": "Ship Guy", "legalName": "Ship Guy Logistics LLC",
       "url": SITE + '/', "logo": SITE + '/assets/favicon-512.png', "telephone": ORG_PHONE, "email": ORG_EMAIL, "sameAs": ORG_SAMEAS}

CRUMB_CSS = ('<style id="sg-crumbs-css">.ph-crumbs{margin:0 0 14px;font-size:13.5px;line-height:1.4}'
             '.ph-crumbs ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;align-items:center;gap:4px 0}'
             '.ph-crumbs li{display:inline-flex;align-items:center;color:#5b6690}'
             '.ph-crumbs li+li::before{content:"\\203A";margin:0 8px;color:#9aa5c7;font-size:15px}'
             '.ph-crumbs a{color:#2f4bd1;text-decoration:none;font-weight:600}.ph-crumbs a:hover{text-decoration:underline}'
             '.ph-crumbs [aria-current]{color:#5b6690;font-weight:500}</style>')

H1_ANCHOR = '<h1 class="reveal d2">'

def _jsonld(obj, id_):
    return '<script type="application/ld+json" id="%s">%s</script>' % (id_, json.dumps(obj, ensure_ascii=False))

def _drop(h, id_):
    return re.sub(r'<script type="application/ld\+json" id="%s">.*?</script>\n?' % re.escape(id_), '', h, flags=re.S)

def _put_head(h, block):
    assert h.count('</head>') == 1
    return h.replace('</head>', block + '\n</head>')

def _crumb_nav(items):
    lis = []
    for name, url in items:
        name = H.escape(name, quote=False)
        lis.append('<li><a href="%s">%s</a></li>' % (url, name) if url else '<li><span aria-current="page">%s</span></li>' % name)
    return '<nav class="ph-crumbs" aria-label="Breadcrumb"><ol>%s</ol></nav>' % ''.join(lis)

def _crumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [dict({"@type": "ListItem", "position": i + 1, "name": name}, **({"item": SITE + url} if url else {}))
                                for i, (name, url) in enumerate(items)]}

def _apply_crumbs(h, items):
    h = re.sub(r'<nav class="ph-crumbs" aria-label="Breadcrumb">.*?</nav>\n?', '', h, count=1, flags=re.S)
    assert h.count(H1_ANCHOR) == 1, h.count(H1_ANCHOR)
    h = h.replace(H1_ANCHOR, _crumb_nav(items) + '\n' + H1_ANCHOR)
    h = re.sub(r'<style id="sg-crumbs-css">.*?</style>\n?', '', h, count=1, flags=re.S)
    h = _put_head(h, CRUMB_CSS)
    h = _drop(h, 'sg-breadcrumb')
    return _put_head(h, _jsonld(_crumb_ld(items), 'sg-breadcrumb'))

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def _to24(t, ampm):
    hh, mm = t.split(':'); hh = int(hh) % 12 + (12 if ampm == 'PM' else 0)
    return '%02d:%s' % (hh, mm)

def parse_office(h):
    """Address / phone / hours / coordinates from the office card; None when the page has no card."""
    m = re.search(r'<div class="ph-office-card">(.*?)</div><div class="ph-map">(.*?)</div>', h, re.S)
    if not m: return None
    card, mp = m.group(1), m.group(2)
    a = re.search(r'<b>Address</b><span>(.*?)<br>(.*?)</span>', card)
    p = re.search(r'<a href="tel:(\+1\d{10})">', card)
    if not (a and p): return None
    line1 = H.unescape(a.group(1)).strip(); line2 = H.unescape(a.group(2)).strip()
    cm = re.match(r'^(.*?),\s*([A-Z]{2})\s+(\d{5})(?:-\d{4})?$', line2)
    if not cm: return None
    out = {"street": line1, "city": cm.group(1), "state": cm.group(2), "zip": cm.group(3), "tel": p.group(1)}
    hm = re.search(r'<b>Hours</b><span>(.*?)</span>', card)
    if hm:
        hours = H.unescape(hm.group(1))
        tm = re.search(r'(\d{1,2}:\d{2})\s*(AM|PM)\s*[–-]\s*(\d{1,2}:\d{2})\s*(AM|PM)', hours)
        if tm and 'Monday' in hours and 'Sunday' in hours:
            out['opens'] = _to24(tm.group(1), tm.group(2)); out['closes'] = _to24(tm.group(3), tm.group(4))
    gm = re.search(r'!2d(-?\d+\.\d+)!3d(-?\d+\.\d+)', mp)
    if gm: out['lng'] = float(gm.group(1)); out['lat'] = float(gm.group(2))
    return out

def _meta_desc(h):
    m = re.search(r'<meta name="description" content="([^"]*)"', h)
    return H.unescape(m.group(1)) if m else ''

def local_business_ld(h, url, city):
    o = parse_office(h)
    if not o: return None
    d = {"@context": "https://schema.org", "@type": "LocalBusiness", "@id": url + '#office',
         "name": "Ship Guy Auto Transports", "image": SITE + '/assets/hero.jpg', "url": url,
         "telephone": o['tel'], "email": ORG_EMAIL, "description": _meta_desc(h),
         "address": {"@type": "PostalAddress", "streetAddress": o['street'], "addressLocality": o['city'],
                     "addressRegion": o['state'], "postalCode": o['zip'], "addressCountry": "US"},
         "areaServed": {"@type": "City", "name": city},
         "parentOrganization": {"@type": "Organization", "@id": SITE + '/#organization', "name": "Ship Guy", "url": SITE + '/'}}
    if 'lat' in o:
        d["geo"] = {"@type": "GeoCoordinates", "latitude": o['lat'], "longitude": o['lng']}
    d["hasMap"] = 'https://www.google.com/maps?q=' + quote_plus(o['street'] + ', ' + o['city'] + ', ' + o['state'] + ' ' + o['zip'])
    if 'opens' in o:
        d["openingHoursSpecification"] = [{"@type": "OpeningHoursSpecification", "dayOfWeek": DAYS, "opens": o['opens'], "closes": o['closes']}]
    return d

def enrich_city(h, slug, city, state_name, state_slug):
    url = '%s/city/%s/' % (SITE, slug)
    h = _apply_crumbs(h, [("Home", "/"), ("Locations", "/locations"), (state_name, "/" + state_slug), (city, None)])
    h = _drop(h, 'sg-localbusiness')
    lb = local_business_ld(h, url, city)
    if lb: h = _put_head(h, _jsonld(lb, 'sg-localbusiness'))
    return h

def enrich_state(h, state_name, state_slug):
    return _apply_crumbs(h, [("Home", "/"), ("Locations", "/locations"), (state_name, None)])

def enrich_home(h):
    h = _drop(h, 'sg-organization'); h = _drop(h, 'sg-website')
    org = dict(ORG, **{"@context": "https://schema.org",
                       "contactPoint": [{"@type": "ContactPoint", "telephone": ORG_PHONE, "contactType": "customer service",
                                         "areaServed": "US", "availableLanguage": "English"}]})
    h = _put_head(h, _jsonld(org, 'sg-organization'))
    return _put_head(h, _jsonld({"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + '/#website',
                                 "name": "Ship Guy", "url": SITE + '/', "publisher": {"@type": "Organization", "@id": SITE + '/#organization', "name": "Ship Guy"}}, 'sg-website'))
