"""Batch 50 hub integration: nearby blocks (regenerated wherever lp.NEARBY changed), see-all counts, locations.html rows (WY, RI, MT, NV, NM, TN; no new state block), counts, sitemap, audit inbound list."""
import re, sys, glob
sys.path.insert(0,'/home/claude/tools'); import localpage as lp
S='/home/claude/build/shipguy/'
NEW=['auto-transport-casper-wyoming','auto-transport-pawtucket-rhode-island','auto-transport-bozeman-montana','auto-transport-carson-city-nevada','auto-transport-rio-rancho-new-mexico','auto-transport-knoxville-tennessee']
NB=re.compile(r'<section class="ph-sec"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">Nearby</p>.*?</section>', re.S)

# 1) nearby chips: regenerate on every city page whose block differs from the current NEARBY tables
changed=[]
for p in sorted(glob.glob(S+'city/*/index.html')):
    slug=p.split('/')[-2]
    if slug not in lp.NAMES: continue
    h=open(p,encoding='utf-8').read()
    blocks=NB.findall(h)
    if len(blocks)!=1: print('  (no single Nearby block on', slug, ')'); continue
    new=lp.nearby_block(slug)
    if blocks[0]!=new:
        h=NB.sub(lambda m: new, h, count=1); open(p,'w',encoding='utf-8').write(h); changed.append(slug)
print('nearby chips regenerated on', len(changed), 'pages:', ', '.join(s.replace('auto-transport-','') for s in changed))
for s in NEW: assert s in changed or NB.search(open(S+'city/%s/index.html'%s,encoding='utf-8').read()), s

# 2) "See all N cities we serve" on every city page
n=len(lp.NAMES); c=0; missing=[]
for p in sorted(glob.glob(S+'city/*/index.html')):
    h=open(p,encoding='utf-8').read()
    h2=re.sub(r'See all \d+ cities we serve', 'See all %d cities we serve'%n, h)
    if h2!=h: open(p,'w',encoding='utf-8').write(h2); c+=1
    if 'See all %d cities we serve'%n not in h2: missing.append(p.split('/')[-2])
print('see-all =', n, 'updated on', c, 'pages; lacking:', missing)

# 3) locations hub rows
p=S+'locations.html'; h=open(p,encoding='utf-8').read()
def chips_for(st):
    items=sorted([(name, slug) for slug,(name,s) in lp.NAMES.items() if s==st], key=lambda t: t[0])
    return ''.join('<a class="ph-chip" href="/city/%s/">%s</a>'%(slug,name) for name,slug in items)
for st, label in [('WY','Wyoming'),('RI','Rhode Island'),('MT','Montana'),('NV','Nevada'),('NM','New Mexico'),('TN','Tennessee')]:
    key='<h3>%s</h3><div class="ph-chips">'%label
    assert h.count(key)==1, label
    start=h.index(key)+len(key); end=h.index('</div>', start)
    assert '<div' not in h[start:end]
    h=h[:start]+chips_for(st)+h[end:]
def new_block(st, label, before_label):
    global h
    assert '<h3>%s</h3>'%label not in h, label
    anchor='<div class="loc-state"><h3>%s</h3>'%before_label
    assert h.count(anchor)==1, before_label
    h=h.replace(anchor, '<div class="loc-state"><h3>%s</h3><div class="ph-chips">%s</div></div>'%(label, chips_for(st)) + anchor)
assert h.count('Two hundred twelve')==1 and h.count('two hundred twelve local pages')==1
h=h.replace('Two hundred twelve local','Two hundred eighteen local').replace('two hundred twelve local pages','two hundred eighteen local pages')
open(p,'w',encoding='utf-8').write(h)
order=re.findall(r'<div class="loc-state"><h3>([^<]+)</h3>', h)
assert order==sorted(order), order
print('locations hub updated; hub chips:', len(re.findall(r'<a class="ph-chip" href="/city/',h)), '; states:', len(order))

# 4) sitemap
p=S+'sitemap.xml'; h=open(p,encoding='utf-8').read()
add=''.join('<url><loc>https://shipguy.com/city/%s/</loc><lastmod>2026-11-02</lastmod><priority>0.8</priority></url>\n'%s for s in NEW if 'https://shipguy.com/city/%s/'%s not in h)
h=h.replace('</urlset>', add+'</urlset>')
open(p,'w',encoding='utf-8').write(h); print('sitemap urls:', h.count('<url>'))

# 5) audit_site inbound list
p='/home/claude/tools/audit_site.py'; a=open(p,encoding='utf-8').read()
m=re.search(r"for c in \[[^\]]*\]:", a); assert m
a=a.replace(m.group(0), "for c in [%s]:" % ', '.join("'%s'"%s for s in NEW))
open(p,'w',encoding='utf-8').write(a); print('audit_site inbound list set')
