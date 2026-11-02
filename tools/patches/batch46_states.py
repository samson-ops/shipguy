"""Batch 46 state-page integration: first City Pages blocks on SD, WV, WY; VA and PA block regens; chips; quick notes; FAQ links; neighbor links.
Two Charlestons exist now, so no neighbor page is ever linked on the bare word "Charleston"."""
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
SF=L('auto-transport-sioux-falls-south-dakota','Sioux Falls'); CW=L('auto-transport-charleston-west-virginia','Charleston'); CY=L('auto-transport-cheyenne-wyoming','Cheyenne')
NO=L('auto-transport-norfolk-virginia','Norfolk'); BE=L('auto-transport-bethlehem-pennsylvania','Bethlehem')

# ---------------- South Dakota (first block) ----------------
p=S+'south-dakota-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=first_block(h,'SD','Sioux Falls has its own page with local lanes, meeting spots, and a phone line. Rapid City, Pierre, Aberdeen, Brookings, and every other South Dakota town are covered from this page.','Sioux Falls')
h=rep(h,'<p class="ph-lead">Sioux Falls holds half the state’s growth, and it ships on the corporate and medical calendars.</p>',
        '<p class="ph-lead">%s holds half the state’s growth, and it ships on the corporate and medical calendars. It has its own page now.</p>'%SF)
h=chip(h,'Sioux Falls','auto-transport-sioux-falls-south-dakota')
h=faq_edit(h,'Sioux Falls and Rapid City schedule in 2 to 5 days.','Sioux Falls and Rapid City schedule in 2 to 5 days, and the %s page names the meeting lots.'%SF)
open(p,'w',encoding='utf-8').write(h); resync(p); print('south dakota updated (first block)')

# ---------------- West Virginia (first block) ----------------
p=S+'west-virginia-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=first_block(h,'WV','Charleston has its own page with local lanes, meeting spots, and a phone line. Huntington, Morgantown, Martinsburg, Beckley, Wheeling, and every other West Virginia town are covered from this page.','Charleston &amp; Huntington')
h=rep(h,'<p class="ph-quick-note">West Virginia has no city page yet. This page carries the detail for Charleston, Huntington, Morgantown, Martinsburg, Beckley, Wheeling, and the rest.</p>',
        '<p class="ph-quick-note">%s has its own page. This page carries the detail for Huntington, Morgantown, Martinsburg, Beckley, Wheeling, and the rest.</p>'%CW)
h=rep(h,'<p>Charleston holds state government and the chemical plants along the Kanawha.','<p>%s holds state government and the chemical plants along the Kanawha, and it has its own page now.'%CW)
h=chip(h,'Charleston','auto-transport-charleston-west-virginia')
h=faq_edit(h,'Carriers pay the Turnpike between Charleston and Princeton by the axle and price accordingly.','Carriers pay the Turnpike between Charleston and Princeton by the axle and price accordingly. The %s page covers the valley end of it.'%CW)
open(p,'w',encoding='utf-8').write(h); resync(p); print('west virginia updated (first block)')

# ---------------- Wyoming (first block) ----------------
p=S+'wyoming-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=first_block(h,'WY','Cheyenne has its own page with local lanes, meeting spots, and a phone line. Casper, Laramie, Gillette, Rock Springs, Jackson, and every other Wyoming town are covered from this page.','Cheyenne')
h=rep(h,'<p class="ph-lead">Cheyenne is the carrier hub of the state, an hour from Denver and sitting on two interstates.</p>',
        '<p class="ph-lead">%s is the carrier hub of the state, an hour from Denver and sitting on two interstates. It has its own page now.</p>'%CY)
h=chip(h,'Cheyenne','auto-transport-cheyenne-wyoming')
h=faq_edit(h,'Housing is gated, so the driver meets you outside the fence line.','Housing is gated, so the driver meets you outside the fence line. The %s page covers the gate handoff.'%CY)
open(p,'w',encoding='utf-8').write(h); resync(p); print('wyoming updated (first block)')

# ---------------- Virginia (regen, 4) ----------------
p=S+'virginia-auto-transport.html'; h=open(p,encoding='utf-8').read()
VB='<a href="/city/auto-transport-virginia-beach-virginia/">Virginia Beach</a>'; CH='<a href="/city/auto-transport-chesapeake-virginia/">Chesapeake</a>'; RI='<a href="/city/auto-transport-richmond-virginia/">Richmond</a>'
h=regen(h,'VA','Virginia Beach, Chesapeake, Norfolk, and Richmond have their own pages with local lanes, meeting spots, and phone lines. Arlington, Fairfax, Roanoke, Charlottesville, and every other Virginia town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s, %s, and %s have their own pages. This page carries the detail for Arlington, Fairfax, Norfolk, Roanoke, Charlottesville, and the rest.</p>'%(VB,CH,RI),
        '<p class="ph-quick-note">%s, %s, %s, and %s have their own pages. This page carries the detail for Arlington, Fairfax, Roanoke, Charlottesville, and the rest.</p>'%(VB,CH,RI,NO))
h=rep(h,'<p>Naval Station Norfolk is the largest naval base in the world.','<p>Naval Station %s is the largest naval base in the world, and the city has its own page now.'%NO)
h=chip(h,'Norfolk','auto-transport-norfolk-virginia')
h=faq_edit(h,'The %s page covers Oceana and Little Creek.'%VB,'The %s page covers Oceana, and the %s page covers the naval station and Little Creek.'%(VB,NO))
open(p,'w',encoding='utf-8').write(h); resync(p); print('virginia updated')

# ---------------- Pennsylvania (regen, 6) ----------------
p=S+'pennsylvania-auto-transport.html'; h=open(p,encoding='utf-8').read()
PI='<a href="/city/auto-transport-pittsburgh-pennsylvania/">Pittsburgh</a>'; AL='<a href="/city/auto-transport-allentown-pennsylvania/">Allentown</a>'; RE='<a href="/city/auto-transport-reading-pennsylvania/">Reading</a>'; ER='<a href="/city/auto-transport-erie-pennsylvania/">Erie</a>'
h=regen(h,'PA','Philadelphia, Pittsburgh, Allentown, Bethlehem, Reading, and Erie have their own pages with local lanes, meeting spots, and phone lines. Harrisburg, Scranton, State College, and the rest of Pennsylvania are covered from this page.')
h=rep(h,'<p class="ph-quick-note">Philadelphia, %s, %s, and %s, and %s have their own pages. This page carries Harrisburg, Scranton, State College, and the rest of the state.</p>'%(PI,AL,RE,ER),
        '<p class="ph-quick-note">Philadelphia, %s, %s, %s, %s, and %s have their own pages. This page carries Harrisburg, Scranton, State College, and the rest of the state.</p>'%(PI,AL,BE,RE,ER))
h=rep(h,'<p>%s, Bethlehem, and Easton fill with households commuting to New York and Philadelphia. Allentown has its own page.'%AL,
        '<p>%s, %s, and Easton fill with households commuting to New York and Philadelphia. Allentown and Bethlehem have their own pages.'%(AL,BE))
h=chip(h,'Bethlehem','auto-transport-bethlehem-pennsylvania')
open(p,'w',encoding='utf-8').write(h); print('pennsylvania updated')

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
for pg in ['bismarck-north-dakota','fargo-north-dakota','omaha-nebraska','sioux-city-iowa']:
    link_first('city/auto-transport-%s/index.html'%pg,'Sioux Falls','auto-transport-sioux-falls-south-dakota')
link_first('city/auto-transport-denver-colorado/index.html','Cheyenne','auto-transport-cheyenne-wyoming')
for pg in ['chesapeake-virginia','virginia-beach-virginia','richmond-virginia','dover-delaware','san-diego-california']:
    link_first('city/auto-transport-%s/index.html'%pg,'Norfolk','auto-transport-norfolk-virginia')
link_first('city/auto-transport-allentown-pennsylvania/index.html','Bethlehem','auto-transport-bethlehem-pennsylvania')
