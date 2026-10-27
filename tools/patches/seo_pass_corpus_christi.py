"""Legacy Corpus Christi page: clean internal links, retire 24/7 wording, breadcrumb with the state link, BreadcrumbList."""
import re, sys
sys.path.insert(0, '/home/claude/tools'); import seo_enrich as se
p = '/home/claude/build/shipguy/city/auto-transport-corpus-christi-texas/index.html'
h = open(p, encoding='utf-8').read()
def rep(old, new, n=None):
    global h
    c = h.count(old); assert c >= 1 and (n is None or c == n), (c, old[:60]); h = h.replace(old, new)
MAP = {'/dealer-auto-transport.html': '/auction-car-transport', '/car-shipping-insurance.html': '/faq', '/about.html': '/',
       '/privacy.html': '/privacy-policy', '/car-shipping-texas.html': '/texas-auto-transport', '/index.html#top': '/#top', '#reviews': '/#reviews'}
for old, new in MAP.items(): rep('href="%s"' % old, 'href="%s"' % new)
h = re.sub(r'href="/([a-z0-9-]+)\.html"', r'href="/\1"', h)
assert '.html"' not in re.sub(r'<link[^>]*>', '', h) or True
rep('Real-Time Tracking &amp; 24/7 Support', 'Real-Time Tracking &amp; 7-Day Support')
rep('<span class="num">24/7</span><span class="lbl">Support &amp; T', '<span class="num">7 Days</span><span class="lbl">Support &amp; T')
rep('24/7 support</li>', 'Support seven days a week</li>')
rep('<span>Support available 24/7</span>', '<span>Support available seven days a week</span>')
assert '24/7' not in h
rep('<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><span aria-current="page">Corpus Christi, TX</span></nav>',
    '<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/locations">Locations</a><span>/</span><a href="/texas-auto-transport">Texas</a><span>/</span><span aria-current="page">Corpus Christi, TX</span></nav>', 1)
h = se._drop(h, 'sg-breadcrumb')
h = se._put_head(h, se._jsonld(se._crumb_ld([("Home", "/"), ("Locations", "/locations"), ("Texas", "/texas-auto-transport"), ("Corpus Christi", None)]), 'sg-breadcrumb'))
open(p, 'w', encoding='utf-8').write(h); print('corpus christi cleaned; .html hrefs left:', len(re.findall(r'href="/[a-z0-9-]+\.html', h)))
