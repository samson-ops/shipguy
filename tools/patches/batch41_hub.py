import re, sys
sys.path.insert(0,'/home/claude/tools'); import localpage as lp
S='/home/claude/build/shipguy/'
NEW=['auto-transport-virginia-beach-virginia','auto-transport-pittsburgh-pennsylvania','auto-transport-allentown-pennsylvania','auto-transport-reading-pennsylvania']
NEIGH=['auto-transport-philadelphia-pennsylvania','auto-transport-baltimore-maryland','auto-transport-wilmington-delaware','auto-transport-cleveland-ohio','auto-transport-akron-ohio',
       'auto-transport-columbus-ohio','auto-transport-buffalo-new-york','auto-transport-dover-delaware','auto-transport-raleigh-north-carolina','auto-transport-durham-north-carolina',
       'auto-transport-charlotte-north-carolina','auto-transport-columbia-maryland','auto-transport-bridgeport-connecticut']
NB=re.compile(r'<section class="ph-sec"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">Nearby</p>.*?</section>', re.S)

# 1) neighbor chips on the new pages and the pages whose NEARBY lists changed
for slug in NEW+NEIGH:
    p=S+'city/%s/index.html'%slug; h=open(p,encoding='utf-8').read()
    assert len(NB.findall(h))==1, slug
    h=NB.sub(lambda m: lp.nearby_block(slug), h, count=1)
    open(p,'w',encoding='utf-8').write(h)
print('nearby chips regenerated on', len(NEW+NEIGH), 'pages')

# 2) "See all N cities we serve" on every city page
import glob
n=len(lp.NAMES); c=0; missing=[]
for p in sorted(glob.glob(S+'city/*/index.html')):
    h=open(p,encoding='utf-8').read()
    h2=re.sub(r'See all \d+ cities we serve', 'See all %d cities we serve'%n, h)
    if h2!=h: open(p,'w',encoding='utf-8').write(h2); c+=1
    if 'See all %d cities we serve'%n not in h2: missing.append(p.split('/')[-2])
print('see-all updated on', c, 'pages; lacking:', missing)

# 3) locations hub rows
p=S+'locations.html'; h=open(p,encoding='utf-8').read()
def chips_for(st):
    items=sorted([(name, slug) for slug,(name,s) in lp.NAMES.items() if s==st], key=lambda t: t[0])
    return ''.join('<a class="ph-chip" href="/city/%s/">%s</a>'%(slug,name) for name,slug in items)
for st, label in [('PA','Pennsylvania')]:
    key='<h3>%s</h3><div class="ph-chips">'%label
    assert h.count(key)==1, label
    start=h.index(key)+len(key); end=h.index('</div>', start)
    assert '<div' not in h[start:end]
    h=h[:start]+chips_for(st)+h[end:]
assert '<h3>Virginia</h3>' not in h
anchor='<div class="loc-state"><h3>Washington</h3>'
assert h.count(anchor)==1
h=h.replace(anchor, '<div class="loc-state"><h3>Virginia</h3><div class="ph-chips">%s</div></div>'%chips_for('VA') + anchor)
assert h.count('One hundred sixty-two')==4 and h.count('one hundred sixty-two local pages')==1
h=h.replace('One hundred sixty-two','One hundred sixty-six').replace('one hundred sixty-two local pages','one hundred sixty-six local pages')
open(p,'w',encoding='utf-8').write(h); print('locations hub updated; hub chips:', len(re.findall(r'<a class="ph-chip" href="/city/',h)))

# 4) sitemap
p=S+'sitemap.xml'; h=open(p,encoding='utf-8').read()
add=''.join('<url><loc>https://shipguy.com/city/%s/</loc><lastmod>2026-10-27</lastmod><priority>0.8</priority></url>\n'%s for s in NEW if 'https://shipguy.com/city/%s/'%s not in h)
h=h.replace('</urlset>', add+'</urlset>')
open(p,'w',encoding='utf-8').write(h); print('sitemap urls:', h.count('<url>'))

# 5) audit_site inbound list
p='/home/claude/tools/audit_site.py'; a=open(p,encoding='utf-8').read()
m=re.search(r"for c in \[[^\]]*\]:", a); assert m
a=a.replace(m.group(0), "for c in [%s]:" % ', '.join("'%s'"%s for s in NEW))
open(p,'w',encoding='utf-8').write(a); print('audit_site inbound list set')
