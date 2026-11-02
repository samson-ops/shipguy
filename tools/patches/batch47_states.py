"""Batch 47 state-page integration: first City Pages block on NH; MN, MS, MT, NE, NC block regens; chips; quick notes; FAQ links; neighbor links.
Two Rochesters exist now (NY and MN), so a neighbor page is linked on "Rochester" only after its first mention was read as the Minnesota one."""
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
RO=L('auto-transport-rochester-minnesota','Rochester'); GU=L('auto-transport-gulfport-mississippi','Gulfport'); BI=L('auto-transport-billings-montana','Billings')
LI=L('auto-transport-lincoln-nebraska','Lincoln'); NA=L('auto-transport-nashua-new-hampshire','Nashua'); WS=L('auto-transport-winston-salem-north-carolina','Winston-Salem')

# ---------------- Minnesota (regen, 3) ----------------
p=S+'minnesota-auto-transport.html'; h=open(p,encoding='utf-8').read()
SP=L('auto-transport-st-paul-minnesota','St. Paul'); BL=L('auto-transport-bloomington-minnesota','Bloomington')
h=regen(h,'MN','St. Paul, Bloomington, and Rochester have their own pages with local lanes, meeting spots, and phone lines. Minneapolis, Duluth, St. Cloud, and every other Minnesota town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s and %s have their own pages. This page carries the detail for Minneapolis, Rochester, Duluth, St. Cloud, and the rest.</p>'%(SP,BL),
        '<p class="ph-quick-note">%s, %s, and %s have their own pages. This page carries the detail for Minneapolis, Duluth, St. Cloud, and the rest.</p>'%(SP,BL,RO))
h=rep(h,'<p class="ph-lead">Rochester ships cars for a reason no other city in the country shares.</p>',
        '<p class="ph-lead">%s ships cars for a reason no other city in the country shares. It has its own page now.</p>'%RO)
h=chip(h,'Rochester','auto-transport-rochester-minnesota')
h=faq_edit(h,'The handoff happens at a lot near the medical campus.','The handoff happens at a lot near the medical campus, and the %s page names the lots.'%RO)
open(p,'w',encoding='utf-8').write(h); resync(p); print('minnesota updated')

# ---------------- Mississippi (regen, 2) ----------------
p=S+'mississippi-auto-transport.html'; h=open(p,encoding='utf-8').read()
JA=L('auto-transport-jackson-mississippi','Jackson')
h=regen(h,'MS','Jackson and Gulfport have their own pages with local lanes, meeting spots, and phone lines. Biloxi, Hattiesburg, Tupelo, Oxford, and every other Mississippi town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s has its own page. This page carries the detail for Gulfport, Biloxi, Hattiesburg, Tupelo, Oxford, and the rest.</p>'%JA,
        '<p class="ph-quick-note">%s and %s have their own pages. This page carries the detail for Biloxi, Hattiesburg, Tupelo, Oxford, and the rest.</p>'%(JA,GU))
h=rep(h,'The Seabee base in Gulfport deploys and returns battalions.','The Seabee base in %s deploys and returns battalions, and the city has its own page now.'%GU)
h=chip(h,'Gulfport','auto-transport-gulfport-mississippi')
h=faq_edit(h,'Housing is gated, so the driver meets you at the gate.','Housing is gated, so the driver meets you at the gate. The %s page covers the Seabee base and Keesler both.'%GU)
open(p,'w',encoding='utf-8').write(h); resync(p); print('mississippi updated')

# ---------------- Montana (regen, 3) ----------------
p=S+'montana-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=regen(h,'MT','Missoula, Great Falls, and Billings have their own pages with local lanes, meeting spots, and phone lines. Bozeman, Helena, the Flathead, and every other Montana town are covered from this page.')
h=rep(h,'<p>Billings is the carrier hub, where Interstate 90 and 94 meet.','<p>%s is the carrier hub, where Interstate 90 and 94 meet, and it has its own page now.'%BI)
h=chip(h,'Billings','auto-transport-billings-montana')
h=faq_edit(h,'From Missoula, Seattle is four hundred miles closer. Larger vehicles add 10 to 25 percent to the price.','From Missoula, Seattle is four hundred miles closer. Larger vehicles add 10 to 25 percent to the price. The %s page carries the full lane table.'%BI)
open(p,'w',encoding='utf-8').write(h); resync(p); print('montana updated')

# ---------------- Nebraska (regen, 2) ----------------
p=S+'nebraska-auto-transport.html'; h=open(p,encoding='utf-8').read()
OM=L('auto-transport-omaha-nebraska','Omaha')
h=regen(h,'NE','Omaha and Lincoln have their own pages with local lanes, meeting spots, and phone lines. Grand Island, Kearney, North Platte, and every other Nebraska town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s has its own page. This page carries the detail for Lincoln, Grand Island, Kearney, and the rest.</p>'%OM,
        '<p class="ph-quick-note">%s and %s have their own pages. This page carries the detail for Grand Island, Kearney, North Platte, and the rest.</p>'%(OM,LI))
h=rep(h,'<p class="ph-lead">Lincoln is the second city, and on football Saturdays it becomes the largest gathering in the state.</p>',
        '<p class="ph-lead">%s is the second city, and on football Saturdays it becomes the largest gathering in the state. It has its own page now.</p>'%LI)
h=chip(h,'Lincoln','auto-transport-lincoln-nebraska')
h=faq_edit(h,'We schedule Lincoln pickups around the games. The rest of Nebraska runs normally.','We schedule Lincoln pickups around the games, and the %s page names the game-day lots. The rest of Nebraska runs normally.'%LI)
open(p,'w',encoding='utf-8').write(h); resync(p); print('nebraska updated')

# ---------------- New Hampshire (first block) ----------------
p=S+'new-hampshire-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=first_block(h,'NH','Nashua has its own page with local lanes, meeting spots, and a phone line. Manchester, Concord, Portsmouth, Hanover, and every other New Hampshire town are covered from this page.','The Southern Tier')
h=rep(h,'<p class="ph-quick-note">New Hampshire has no city page yet. This page carries the detail for Manchester, Nashua, Concord, Portsmouth, Hanover, and the rest.</p>',
        '<p class="ph-quick-note">%s has its own page. This page carries the detail for Manchester, Concord, Portsmouth, Hanover, and the rest.</p>'%NA)
h=rep(h,'<p>Nashua and Salem sit on the Massachusetts line and fill with commuters who moved north for the taxes.',
        '<p>%s and Salem sit on the Massachusetts line and fill with commuters who moved north for the taxes. Nashua has its own page now.'%NA)
h=chip(h,'Nashua','auto-transport-nashua-new-hampshire')
h=faq_edit(h,'That keeps it the cheapest lane in the state, at one hundred fifty to two hundred forty dollars.','That keeps it the cheapest lane in the state, at one hundred fifty to two hundred forty dollars. The %s page covers the border end of that lane.'%NA)
open(p,'w',encoding='utf-8').write(h); resync(p); print('new hampshire updated (first block)')

# ---------------- North Carolina (regen, 5) ----------------
p=S+'north-carolina-auto-transport.html'; h=open(p,encoding='utf-8').read()
GB=L('auto-transport-greensboro-north-carolina','Greensboro'); CH=L('auto-transport-charlotte-north-carolina','Charlotte'); DU=L('auto-transport-durham-north-carolina','Durham'); RA=L('auto-transport-raleigh-north-carolina','Raleigh')
h=regen(h,'NC','Charlotte, Durham, Raleigh, Greensboro, and Winston-Salem have their own pages with local lanes, meeting spots, and phone lines. Fayetteville, Jacksonville, Wilmington, Asheville, the coast, and the rest of North Carolina are covered from this page.')
h=rep(h,'<p class="ph-quick-note">Charlotte, Durham, Raleigh, and %s have their own pages. This page carries Winston-Salem, Fayetteville, Jacksonville, Wilmington, Asheville, the coast, and the rest of the state.</p>'%GB,
        '<p class="ph-quick-note">%s, %s, %s, %s, and %s have their own pages. This page carries Fayetteville, Jacksonville, Wilmington, Asheville, the coast, and the rest of the state.</p>'%(CH,DU,RA,GB,WS))
h=rep(h,'<p>%s ships on the cargo airport, the universities, and the new plants along the interstate. It has its own page now. Winston-Salem ships on the medical center, the university, and the tobacco district’s old streets.'%GB,
        '<p>%s ships on the cargo airport, the universities, and the new plants along the interstate. %s ships on the medical center, the university, and the tobacco district’s old streets. Both have their own pages now.'%(GB,WS))
h=chip(h,'Winston-Salem','auto-transport-winston-salem-north-carolina')
h=faq_edit(h,'Yes, the three cities sit where Interstate 40 and 85 meet, and carriers stage there. Pickups schedule within 1 to 3 days.','Yes, the three cities sit where Interstate 40 and 85 meet, and carriers stage there. %s and %s have their own pages. Pickups schedule within 1 to 3 days.'%(GB,WS))
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
# Rochester: both first mentions were read first (the 52 road south of St. Paul; the Bloomington same-day list) and are the Minnesota city
for pg in ['st-paul-minnesota','bloomington-minnesota']:
    link_first('city/auto-transport-%s/index.html'%pg,'Rochester','auto-transport-rochester-minnesota')
for pg in ['great-falls-montana','missoula-montana','bismarck-north-dakota','cheyenne-wyoming']:
    link_first('city/auto-transport-%s/index.html'%pg,'Billings','auto-transport-billings-montana')
for pg in ['omaha-nebraska','topeka-kansas']:
    link_first('city/auto-transport-%s/index.html'%pg,'Lincoln','auto-transport-lincoln-nebraska')
link_first('city/auto-transport-greensboro-north-carolina/index.html','Winston-Salem','auto-transport-winston-salem-north-carolina')
