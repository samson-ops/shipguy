"""Batch 48 state-page integration: VA, MN, NV, NJ, NC block regens; chips; quick notes; FAQ links; neighbor links.
Two Fayettevilles exist now (AR and NC), so no neighbor page is ever linked on the bare word "Fayetteville"; no NC neighbor
page mentions it in prose anyway. Duluth GA is an Atlanta suburb, so "Duluth" is linked only on the two Minnesota pages read first."""
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
NN=L('auto-transport-newport-news-virginia','Newport News'); DU=L('auto-transport-duluth-minnesota','Duluth'); SK=L('auto-transport-sparks-nevada','Sparks')
PA=L('auto-transport-paterson-new-jersey','Paterson'); FA=L('auto-transport-fayetteville-north-carolina','Fayetteville')

# ---------------- Virginia (regen, 5) ----------------
p=S+'virginia-auto-transport.html'; h=open(p,encoding='utf-8').read()
VB=L('auto-transport-virginia-beach-virginia','Virginia Beach'); CH=L('auto-transport-chesapeake-virginia','Chesapeake'); RI=L('auto-transport-richmond-virginia','Richmond'); NO=L('auto-transport-norfolk-virginia','Norfolk')
h=regen(h,'VA','Virginia Beach, Chesapeake, Norfolk, Newport News, and Richmond have their own pages with local lanes, meeting spots, and phone lines. Arlington, Fairfax, Roanoke, Charlottesville, and every other Virginia town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s, %s, %s, and %s have their own pages. This page carries the detail for Arlington, Fairfax, Roanoke, Charlottesville, and the rest.</p>'%(VB,CH,RI,NO),
        '<p class="ph-quick-note">%s, %s, %s, %s, and %s have their own pages. This page carries the detail for Arlington, Fairfax, Roanoke, Charlottesville, and the rest.</p>'%(VB,CH,RI,NO,NN))
h=rep(h,'The shipbuilder in Newport News relocates engineers on program schedules.','The shipbuilder in %s relocates engineers on program schedules, and the city has its own page now.'%NN)
h=chip(h,'Newport News','auto-transport-newport-news-virginia')
h=faq_edit(h,'The %s page covers Oceana, and the %s page covers the naval station and Little Creek.'%(VB,NO),'The %s page covers Oceana, and the %s page covers the naval station and Little Creek. The %s page covers Fort Eustis and Langley.'%(VB,NO,NN))
open(p,'w',encoding='utf-8').write(h); resync(p); print('virginia updated')

# ---------------- Minnesota (regen, 4) ----------------
p=S+'minnesota-auto-transport.html'; h=open(p,encoding='utf-8').read()
SP=L('auto-transport-st-paul-minnesota','St. Paul'); BL=L('auto-transport-bloomington-minnesota','Bloomington'); RO=L('auto-transport-rochester-minnesota','Rochester')
h=regen(h,'MN','St. Paul, Bloomington, Rochester, and Duluth have their own pages with local lanes, meeting spots, and phone lines. Minneapolis, St. Cloud, and every other Minnesota town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s, %s, and %s have their own pages. This page carries the detail for Minneapolis, Duluth, St. Cloud, and the rest.</p>'%(SP,BL,RO),
        '<p class="ph-quick-note">%s, %s, %s, and %s have their own pages. This page carries the detail for Minneapolis, St. Cloud, and the rest.</p>'%(SP,BL,RO,DU))
h=rep(h,'<p>Duluth sits at the head of Lake Superior with a port and a campus.','<p>%s sits at the head of Lake Superior with a port and a campus. It has its own page now.'%DU)
h=chip(h,'Duluth','auto-transport-duluth-minnesota')
h=faq_edit(h,'Pickups there take 2 to 4 days as well.','Pickups there take 2 to 4 days as well, and the %s page names the flat meeting spots.'%DU)
open(p,'w',encoding='utf-8').write(h); resync(p); print('minnesota updated')

# ---------------- Nevada (regen, 3) ----------------
p=S+'nevada-auto-transport.html'; h=open(p,encoding='utf-8').read()
LV=L('auto-transport-las-vegas-nevada','Las Vegas'); HE=L('auto-transport-henderson-nevada','Henderson')
h=regen(h,'NV','Las Vegas, Henderson, and Sparks have their own pages with local lanes, meeting spots, and phone lines. Reno, Carson City, Tahoe, and the rest of Nevada are covered from this page.')
h=rep(h,'<p class="ph-quick-note">Las Vegas and Henderson have their own pages. This page carries Reno, Sparks, Carson City, Lake Tahoe, and the rest of the state.</p>',
        '<p class="ph-quick-note">%s, %s, and %s have their own pages. This page carries Reno, Carson City, Lake Tahoe, and the rest of the state.</p>'%(LV,HE,SK))
h=rep(h,'<p>The industrial center east of Sparks holds the battery plant and the data centers.','<p>The industrial center east of %s holds the battery plant and the data centers. Sparks has its own page now.'%SK)
h=chip(h,'Sparks','auto-transport-sparks-nevada')
h=faq_edit(h,'New subdivisions outpace carrier maps, so send the full address.','New subdivisions outpace carrier maps, so send the full address. The %s page covers the meeting lots and the pass.'%SK)
open(p,'w',encoding='utf-8').write(h); resync(p); print('nevada updated')

# ---------------- New Jersey (regen, 2) ----------------
p=S+'new-jersey-auto-transport.html'; h=open(p,encoding='utf-8').read()
NE=L('auto-transport-newark-new-jersey','Newark')
h=regen(h,'NJ','Newark and Paterson have their own pages with local lanes, meeting spots, and phone lines. Jersey City, Elizabeth, Edison, Trenton, the Shore, and every other New Jersey town are covered from this page.')
h=rep(h,'%s, the Oranges, and Montclair have older grids with the same answer. Newark has its own page now.</p>'%NE,
        '%s, %s, the Oranges, and Montclair have older grids with the same answer. Newark and Paterson have their own pages now.</p>'%(NE,PA))
h=faq_edit(h,'A carrier reaches Bergen, Essex, and the northern suburbs from the Turnpike, Route 17, or Route 3 instead.','A carrier reaches Bergen, Essex, and the northern suburbs from the Turnpike, Route 17, or Route 3 instead. The %s page covers the 80 side of that.'%PA)
open(p,'w',encoding='utf-8').write(h); resync(p); print('new jersey updated (no Paterson chip on this page)')

# ---------------- North Carolina (regen, 6) ----------------
p=S+'north-carolina-auto-transport.html'; h=open(p,encoding='utf-8').read()
GB=L('auto-transport-greensboro-north-carolina','Greensboro'); CL=L('auto-transport-charlotte-north-carolina','Charlotte'); DR=L('auto-transport-durham-north-carolina','Durham'); RA=L('auto-transport-raleigh-north-carolina','Raleigh'); WS=L('auto-transport-winston-salem-north-carolina','Winston-Salem')
h=regen(h,'NC','Charlotte, Durham, Raleigh, Greensboro, Winston-Salem, and Fayetteville have their own pages with local lanes, meeting spots, and phone lines. Jacksonville, Wilmington, Asheville, the coast, and the rest of North Carolina are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s, %s, %s, %s, and %s have their own pages. This page carries Fayetteville, Jacksonville, Wilmington, Asheville, the coast, and the rest of the state.</p>'%(CL,DR,RA,GB,WS),
        '<p class="ph-quick-note">%s, %s, %s, %s, %s, and %s have their own pages. This page carries Jacksonville, Wilmington, Asheville, the coast, and the rest of the state.</p>'%(CL,DR,RA,GB,WS,FA))
h=rep(h,'<p>Fort Bragg in Fayetteville is the largest Army post in the country.','<p>Fort Bragg in %s is the largest Army post in the country. The city has its own page now.'%FA)
h=chip(h,'Fayetteville','auto-transport-fayetteville-north-carolina')
h=faq_edit(h,'Housing is gated, so the handoff takes place outside the gate.','Housing is gated, so the handoff takes place outside the gate. The %s page covers the Fort Bragg gates and the PCS season.'%FA)
open(p,'w',encoding='utf-8').write(h); resync(p); print('north carolina updated')

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
for pg in ['norfolk-virginia','virginia-beach-virginia']:
    link_first('city/auto-transport-%s/index.html'%pg,'Newport News','auto-transport-newport-news-virginia')
# Duluth: both first mentions were read first (the St. Paul and Bloomington same-day lists) and are the Minnesota city
for pg in ['st-paul-minnesota','bloomington-minnesota']:
    link_first('city/auto-transport-%s/index.html'%pg,'Duluth','auto-transport-duluth-minnesota')
