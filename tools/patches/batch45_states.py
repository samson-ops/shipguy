"""Batch 45 state-page integration: WA, MN, MT, NM, ND, OR block regens; first City Pages block on SC; chips; quick notes; FAQ links; neighbor links."""
import re, sys, subprocess
sys.path.insert(0,'/home/claude/tools'); import localpage as lp
S='/home/claude/build/shipguy/'
BLOCK=re.compile(r'<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">City Pages</p>.*?</section>', re.S)
def rep(h, old, new, n=1):
    c=h.count(old); assert c==n, (c, old[:80]); return h.replace(old,new)
def L(slug, name): return '<a href="/city/%s/">%s</a>' % (slug, name)
def chip(h, name, slug): return rep(h,'<span class="ph-chip">%s</span>'%name, '<a class="ph-chip" href="/city/%s/">%s</a>'%(slug,name))
def faq_edit(h, old, new):
    i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
    return head+rep(body,old,new)
def resync(path): subprocess.run(['python3','/home/claude/tools/patches/resync_faq.py',path],check=True)
def regen(h, st, intro):
    assert BLOCK.search(h); return BLOCK.sub(lambda m: lp.state_cities_block(st, intro), h, count=1)
def first_block(h, st, intro, eyebrow):
    assert not BLOCK.search(h)
    anchor='<section class="ph-sec"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">%s</p>' % eyebrow
    assert h.count(anchor)==1, anchor
    h=h.replace(anchor, lp.state_cities_block(st, intro)+'\n'+anchor)
    assert BLOCK.search(h); return h
BE=L('auto-transport-bellevue-washington','Bellevue'); BL=L('auto-transport-bloomington-minnesota','Bloomington'); GF=L('auto-transport-great-falls-montana','Great Falls')
SF=L('auto-transport-santa-fe-new-mexico','Santa Fe'); BI=L('auto-transport-bismarck-north-dakota','Bismarck'); EU=L('auto-transport-eugene-oregon','Eugene'); CH=L('auto-transport-charleston-south-carolina','Charleston')
SEA='<a href="/city/auto-transport-seattle-washington/">Seattle</a>'; SPO='<a href="/city/auto-transport-spokane-washington/">Spokane</a>'; VAN='<a href="/city/auto-transport-vancouver-washington/">Vancouver</a>'

# ---------------- Washington (regen, 4) ----------------
p=S+'washington-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=regen(h,'WA','Seattle, Bellevue, Spokane, and Vancouver have their own pages with local lanes, meeting spots, and phone lines. Tacoma, Everett, Olympia, the Tri-Cities, and every other Washington town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s and %s, and %s have their own pages. This page carries the detail for Bellevue, Tacoma, Everett, Olympia, the Tri-Cities, and the rest.</p>'%(SEA,SPO,VAN),
        '<p class="ph-quick-note">%s, %s, %s, and %s have their own pages. This page carries the detail for Tacoma, Everett, Olympia, the Tri-Cities, and the rest.</p>'%(SEA,SPO,VAN,BE))
h=rep(h,'<p class="ph-lead">%s and Bellevue relocate more engineers than almost any metro in the country. Most of them ship a car, and Seattle has its own page now.</p>'%SEA,
        '<p class="ph-lead">%s and %s relocate more engineers than almost any metro in the country. Most of them ship a car, and both have their own pages now.</p>'%(SEA,BE))
h=chip(h,'Bellevue','auto-transport-bellevue-washington')
h=faq_edit(h,'The %s page covers the lots and the hills.'%SEA,'The %s page covers the lots and the hills, and the %s page covers the Eastside.'%(SEA,BE))
open(p,'w',encoding='utf-8').write(h); resync(p); print('washington updated')

# ---------------- Minnesota (regen, 2) ----------------
p=S+'minnesota-auto-transport.html'; h=open(p,encoding='utf-8').read()
SP='<a href="/city/auto-transport-st-paul-minnesota/">St. Paul</a>'
h=regen(h,'MN','St. Paul and Bloomington have their own pages with local lanes, meeting spots, and phone lines. Minneapolis, Rochester, Duluth, St. Cloud, and every other Minnesota town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s has its own page. This page carries the detail for Minneapolis, Rochester, Duluth, St. Cloud, and the rest.</p>'%SP,
        '<p class="ph-quick-note">%s and %s have their own pages. This page carries the detail for Minneapolis, Rochester, Duluth, St. Cloud, and the rest.</p>'%(SP,BL))
h=chip(h,'Bloomington','auto-transport-bloomington-minnesota')
h=faq_edit(h,'Fly-and-ship through the airport is routine.','Fly-and-ship through the airport is routine. The airport sits in Bloomington, which has its own %s.'%L('auto-transport-bloomington-minnesota','page'))
open(p,'w',encoding='utf-8').write(h); resync(p); print('minnesota updated')

# ---------------- Montana (regen, 2) ----------------
p=S+'montana-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=regen(h,'MT','Missoula and Great Falls have their own pages with local lanes, meeting spots, and phone lines. Billings, Bozeman, Helena, the Flathead, and every other Montana town are covered from this page.')
h=rep(h,'<p>Malmstrom Air Force Base in Great Falls runs the missile wing.','<p>Malmstrom Air Force Base in %s runs the missile wing, and the city has its own page now.'%GF)
h=chip(h,'Great Falls','auto-transport-great-falls-montana')
h=faq_edit(h,'Housing is gated, so the driver meets you outside the base. Ship Guy is a private broker with no connection to the base.',
             'Housing is gated, so the driver meets you outside the base. The %s page covers the gate handoff. Ship Guy is a private broker with no connection to the base.'%GF)
open(p,'w',encoding='utf-8').write(h); resync(p); print('montana updated')

# ---------------- New Mexico (regen, 3) ----------------
p=S+'new-mexico-auto-transport.html'; h=open(p,encoding='utf-8').read()
LC='<a href="/city/auto-transport-las-cruces-new-mexico/">Las Cruces</a>'
h=regen(h,'NM','Albuquerque, Las Cruces, and Santa Fe have their own pages with local lanes, meeting spots, and phone lines. Taos, the oil patch, the Four Corners, and the rest of New Mexico are covered from this page.')
h=rep(h,'%s has one too. This page carries Santa Fe, the southeast, the northwest, and the rest of the state.</p>'%LC,
        '%s and %s have them too. This page carries Taos, the southeast, the northwest, and the rest of the state.</p>'%(LC,SF))
h=rep(h,'It also covers the oil patch, the bases, the mountain towns, and the two cities with their own pages.','It also covers the oil patch, the bases, the mountain towns, and the three cities with their own pages.')
h=rep(h,'<p class="ph-lead">Santa Fe is an hour up Interstate 25, and its downtown was laid out four centuries before trucks.</p>',
        '<p class="ph-lead">%s is an hour up Interstate 25, and its downtown was laid out four centuries before trucks. It has its own page now.</p>'%SF)
h=chip(h,'Santa Fe','auto-transport-santa-fe-new-mexico')
h=faq_edit(h,'The newer subdivisions south of town allow curbside.','The newer subdivisions south of town allow curbside. The %s page names the lots.'%SF)
open(p,'w',encoding='utf-8').write(h); resync(p); print('new mexico updated')

# ---------------- North Dakota (regen, 2) ----------------
p=S+'north-dakota-auto-transport.html'; h=open(p,encoding='utf-8').read()
FA='<a href="/city/auto-transport-fargo-north-dakota/">Fargo</a>'
h=regen(h,'ND','Fargo and Bismarck have their own pages with local lanes, meeting spots, and phone lines. Grand Forks, Minot, the oil patch, and every other North Dakota town are covered from this page.')
h=rep(h,'<p class="ph-lead">%s and Bismarck ship on the corporate, medical, and campus calendars.</p>'%FA,'<p class="ph-lead">%s and %s ship on the corporate, medical, and campus calendars.</p>'%(FA,BI))
h=rep(h,'Mandan across the river shares its carrier pool.</p>','Mandan across the river shares its carrier pool. Bismarck has its own page now.</p>')
h=chip(h,'Bismarck','auto-transport-bismarck-north-dakota')
open(p,'w',encoding='utf-8').write(h); print('north dakota updated')

# ---------------- Oregon (regen, 2) ----------------
p=S+'oregon-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=regen(h,'OR','Portland and Eugene have their own pages with local lanes, meeting spots, and phone lines. Salem, Bend, Medford, the coast, and the rest of Oregon are covered from this page.')
h=rep(h,'and the neighborhood meeting spots. This page carries Salem, Eugene, Bend, Medford, the coast, and the rest of the state.</p>',
        'and the neighborhood meeting spots. %s has one too. This page carries Salem, Bend, Medford, the coast, and the rest of the state.</p>'%EU)
h=rep(h,'Eugene and Corvallis ship on the two big campuses, and Albany on the metals plants between them.','%s and Corvallis ship on the two big campuses, and Albany on the metals plants between them.'%EU)
h=chip(h,'Eugene','auto-transport-eugene-oregon')
h=faq_edit(h,'Campus streets are tight in Eugene and Corvallis, so the handoff happens at a lot nearby.','Campus streets are tight in Eugene and Corvallis, so the handoff happens at a lot nearby. The %s page names the lots.'%EU)
open(p,'w',encoding='utf-8').write(h); resync(p); print('oregon updated')

# ---------------- South Carolina (first block) ----------------
p=S+'south-carolina-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=first_block(h,'SC','Charleston has its own page with local lanes, meeting spots, and a phone line. Columbia, Greenville, Myrtle Beach, Hilton Head, and every other South Carolina town are covered from this page.','The Upstate')
h=rep(h,'<p class="ph-quick-note">South Carolina has no city page yet. This page carries the detail for Charleston, Columbia, Greenville, Myrtle Beach, Hilton Head, and the rest.</p>',
        '<p class="ph-quick-note">%s has its own page. This page carries the detail for Columbia, Greenville, Myrtle Beach, Hilton Head, and the rest.</p>'%CH)
h=rep(h,'<p class="ph-lead">Charleston ships on a port, a joint base, two aircraft plants, and a peninsula laid out before trucks.</p>',
        '<p class="ph-lead">%s ships on a port, a joint base, two aircraft plants, and a peninsula laid out before trucks. It has its own page now.</p>'%CH)
h=chip(h,'Charleston','auto-transport-charleston-south-carolina')
h=faq_edit(h,'Mount Pleasant, Summerville, and Daniel Island allow curbside on most streets.','Mount Pleasant, Summerville, and Daniel Island allow curbside on most streets. The %s page names the lots.'%CH)
open(p,'w',encoding='utf-8').write(h); resync(p); print('south carolina updated (first block)')

# ---------------- neighbor city pages: link the first plain prose mention (before the FAQ list) ----------------
def link_first(path, city, slug):
    p=S+path; h=open(p,encoding='utf-8').read()
    a=h.index('<section class="ph-stats">'); b=h.index('<div class="ph-faq-list">') if '<div class="ph-faq-list">' in h else h.index('<footer')
    pat=re.compile(r'(?<![>\w])%s(?![\w<])' % re.escape(city))
    for m in re.finditer(r'<p(?: class="ph-(?:lead|sub|quick-note)")?>(.*?)</p>', h[a:b], re.S):
        if '<table' in m.group(0): continue
        mm=pat.search(m.group(1))
        if mm and ('href="/city/%s/'%slug) not in m.group(1):
            start=a+m.start(1)+mm.start()
            h=h[:start]+'<a href="/city/%s/">%s</a>'%(slug,city)+h[start+len(city):]
            open(p,'w',encoding='utf-8').write(h); print(path.split('/')[1], '-> linked', city); return
    raise SystemExit('no plain mention of %s in %s' % (city, path))
link_first('city/auto-transport-missoula-montana/index.html','Great Falls','auto-transport-great-falls-montana')
link_first('city/auto-transport-albuquerque-new-mexico/index.html','Santa Fe','auto-transport-santa-fe-new-mexico')
link_first('city/auto-transport-fargo-north-dakota/index.html','Bismarck','auto-transport-bismarck-north-dakota')
link_first('city/auto-transport-portland-oregon/index.html','Eugene','auto-transport-eugene-oregon')
link_first('city/auto-transport-vancouver-washington/index.html','Eugene','auto-transport-eugene-oregon')
for pg in ['augusta-georgia','jacksonville-florida','savannah-georgia']:
    link_first('city/auto-transport-%s/index.html'%pg,'Charleston','auto-transport-charleston-south-carolina')
