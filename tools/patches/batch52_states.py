"""Batch 52 state-page integration (Nov 9, 2026): NJ, VA, OR block regens (no new blocks); quick notes; chips; FAQ
links; neighbor links. Name collisions: "Elizabeth" also appears as the Elizabeth River, "Hampton" inside "Hampton Roads"
and "Hampton Boulevard", "Suffolk" and "Lakewood" are shared with other states, so every link to those pages is a
targeted phrase replacement (link_phrase), never a bare first-mention regex. Gresham and Portland are safe for link_first."""
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
LK=L('auto-transport-lakewood-new-jersey','Lakewood'); EL=L('auto-transport-elizabeth-new-jersey','Elizabeth')
HA=L('auto-transport-hampton-virginia','Hampton'); SU=L('auto-transport-suffolk-virginia','Suffolk'); GR=L('auto-transport-gresham-oregon','Gresham')

# ---------------- New Jersey (regen, 4) ----------------
p=S+'new-jersey-auto-transport.html'; h=open(p,encoding='utf-8').read()
NE=L('auto-transport-newark-new-jersey','Newark'); PA=L('auto-transport-paterson-new-jersey','Paterson')
h=regen(h,'NJ','Newark, Paterson, Elizabeth, and Lakewood have their own pages with local lanes, meeting spots, and phone lines. Jersey City, Edison, Trenton, the Shore, and every other New Jersey town are covered from this page.')
h=rep(h,'%s, %s, the Oranges, and Montclair have older grids with the same answer. Newark and Paterson have their own pages now.</p>'%(NE,PA),
        '%s, %s, %s, the Oranges, and Montclair have older grids with the same answer. Newark, Paterson, and Elizabeth have their own pages now.</p>'%(NE,PA,EL))
h=rep(h,'<p>The port in Newark and Elizabeth is the largest on the East Coast. Imported cars clear customs there. We ship them domestically once released, with the ocean leg handled separately.</p>',
        '<p>The port in Newark and Elizabeth is the largest on the East Coast. Imported cars clear customs there. We ship them domestically once released, with the ocean leg handled separately. The %s page covers the port exits and the release lots.</p>'%EL)
h=rep(h,'Asbury Park, Red Bank, and the Monmouth towns have older grids. The truck meets you on a main road.</p>',
        'Asbury Park, Red Bank, and the Monmouth towns have older grids. The truck meets you on a main road. %s inland has its own page, with the Sabbath and school-bus calendar.</p>'%LK)
h=faq_edit(h,'South of 105, the Parkway carries the Shore traffic and trucks are allowed.</p>',
             'South of 105, the Parkway carries the Shore traffic and trucks are allowed. The %s page covers the exits at 88 and 91.</p>'%LK)
open(p,'w',encoding='utf-8').write(h); resync(p); print('new jersey updated')

# ---------------- Virginia (regen, 7) ----------------
p=S+'virginia-auto-transport.html'; h=open(p,encoding='utf-8').read()
VB=L('auto-transport-virginia-beach-virginia','Virginia Beach'); CH=L('auto-transport-chesapeake-virginia','Chesapeake'); RI=L('auto-transport-richmond-virginia','Richmond'); NO=L('auto-transport-norfolk-virginia','Norfolk'); NN=L('auto-transport-newport-news-virginia','Newport News')
h=regen(h,'VA','Virginia Beach, Chesapeake, Norfolk, Newport News, Hampton, Suffolk, and Richmond have their own pages with local lanes, meeting spots, and phone lines. Arlington, Fairfax, Roanoke, Charlottesville, and every other Virginia town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s, %s, %s, %s, and %s have their own pages.'%(VB,CH,RI,NO,NN),'<p class="ph-quick-note">%s, %s, %s, %s, %s, %s, and %s have their own pages.'%(VB,CH,RI,NO,NN,HA,SU))
h=rep(h,'It also covers Hampton Roads and its bases, the valley, the southwest, the weather, and the city page.</p>','It also covers Hampton Roads and its bases, the valley, the southwest, the weather, and the city pages.</p>')
h=rep(h,'Langley Air Force Base and Fort Eustis share a joint base across the water.</p>','Langley Air Force Base and Fort Eustis share a joint base across the water. The %s page covers Langley.</p>'%HA)
h=rep(h,'<p>%s, %s, and Suffolk are wide suburbs where the truck reaches the curb. Virginia Beach and Chesapeake have their own pages now.'%(VB,CH),
        '<p>%s, %s, and %s are wide suburbs where the truck reaches the curb. All three have their own pages now.'%(VB,CH,SU))
h=chip(h,'Hampton','auto-transport-hampton-virginia'); h=chip(h,'Suffolk','auto-transport-suffolk-virginia')
h=faq_edit(h,'The %s page covers Fort Eustis and Langley.'%NN,'The %s page covers Fort Eustis, and the %s page covers Langley.'%(NN,HA))
h=faq_edit(h,'The Hampton Roads and Monitor-Merrimac tunnels back up every rush hour, so carriers plan crossings for mid-morning.',
             'The Hampton Roads and Monitor-Merrimac tunnels back up every rush hour, so carriers plan crossings for mid-morning. The %s page covers the Monitor-Merrimac side.'%SU)
open(p,'w',encoding='utf-8').write(h); resync(p); print('virginia updated')

# ---------------- Oregon (regen, 4) ----------------
p=S+'oregon-auto-transport.html'; h=open(p,encoding='utf-8').read()
EU=L('auto-transport-eugene-oregon','Eugene'); SA=L('auto-transport-salem-oregon','Salem'); PO=L('auto-transport-portland-oregon','Portland')
h=regen(h,'OR','Portland, Gresham, Eugene, and Salem have their own pages with local lanes, meeting spots, and phone lines. Bend, Medford, the coast, and every other Oregon town are covered from this page.')
h=rep(h,'%s and %s have them too. This page carries Bend, Medford, the coast, and the rest of the state.</p>'%(EU,SA),'%s, %s, and %s have them too. This page carries Bend, Medford, the coast, and the rest of the state.</p>'%(GR,EU,SA))
h=rep(h,'<p>The valley towns have older grids where the truck usually reaches the curb. %s is covered on its own page.</p>'%PO,
        '<p>The valley towns have older grids where the truck usually reaches the curb. %s is covered on its own page, and so is %s on the east side.</p>'%(PO,GR))
h=rep(h,'Carriers wait out a closure rather than chain a loaded trailer.</p><p>Hood River,','Carriers wait out a closure rather than chain a loaded trailer. The %s page covers Troutdale, where the gates close the freeway.</p><p>Hood River,'%GR)
h=faq_edit(h,'Carriers wait out a closure rather than chain a loaded trailer. We let you know whenever the gorge is in play.</p>',
             'Carriers wait out a closure rather than chain a loaded trailer. We let you know whenever the gorge is in play. The %s page covers the Troutdale end.</p>'%GR)
open(p,'w',encoding='utf-8').write(h); resync(p); print('oregon updated')

# ---------------- neighbor city pages ----------------
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
def link_phrase(path, old, new):
    p=S+path; h=open(p,encoding='utf-8').read()
    a=h.index('<section class="ph-stats">'); b=h.index('<div class="ph-faq-list">')
    body=h[a:b]; assert body.count(old)==1, (path, old[:60])
    h=h[:a]+body.replace(old,new)+h[b:]; open(p,'w',encoding='utf-8').write(h); print(path.split('/')[1], '-> phrase linked')
# Elizabeth <-> Newark
link_phrase('city/auto-transport-newark-new-jersey/index.html','Elizabeth and the port towns to the south ship with the same trucks.','%s and the port towns to the south ship with the same trucks.'%EL)
link_phrase('city/auto-transport-elizabeth-new-jersey/index.html','Elizabeth prices with Newark on every lane','Elizabeth prices with %s on every lane'%NE)
# Lakewood -> Newark (the only Newark mention is the fly-and-ship line, and the Newark page covers the airport)
link_first('city/auto-transport-lakewood-new-jersey/index.html','Newark','auto-transport-newark-new-jersey')
# Hampton <-> Newport News, Virginia Beach
link_phrase('city/auto-transport-newport-news-virginia/index.html','Hampton next door ships with the same trucks and prices the same as Newport News.','%s next door ships with the same trucks and prices the same as Newport News.'%HA)
link_phrase('city/auto-transport-virginia-beach-virginia/index.html','</a> and over to Hampton.','</a> and over to %s.'%HA)
link_phrase('city/auto-transport-hampton-virginia/index.html','Newport News next door is covered on its own page','%s next door is covered on its own page'%NN)
link_phrase('city/auto-transport-hampton-virginia/index.html','Interstate 664 leaves 64 at the west edge and crosses to Suffolk on the Monitor-Merrimac.','Interstate 664 leaves 64 at the west edge and crosses to %s on the Monitor-Merrimac.'%SU)
# Suffolk <-> Newport News, Chesapeake, Virginia Beach
link_phrase('city/auto-transport-newport-news-virginia/index.html','It crosses on the Monitor-Merrimac bridge-tunnel to Suffolk.','It crosses on the Monitor-Merrimac bridge-tunnel to %s.'%SU)
link_phrase('city/auto-transport-chesapeake-virginia/index.html','Portsmouth, Norfolk, Suffolk, and Virginia Beach surround the city','Portsmouth, Norfolk, %s, and Virginia Beach surround the city'%SU)
link_phrase('city/auto-transport-virginia-beach-virginia/index.html','Norfolk, Portsmouth, Suffolk, and the Peninsula ride the same carriers','Norfolk, Portsmouth, %s, and the Peninsula ride the same carriers'%SU)
link_phrase('city/auto-transport-suffolk-virginia/index.html','Chesapeake, Portsmouth, Smithfield, Windsor, and Carrollton ship with the same trucks and price the same as Suffolk.','%s, Portsmouth, Smithfield, Windsor, and Carrollton ship with the same trucks and price the same as Suffolk.'%CH)
# Gresham <-> Portland
link_first('city/auto-transport-portland-oregon/index.html','Gresham','auto-transport-gresham-oregon')
link_phrase('city/auto-transport-gresham-oregon/index.html','Gresham prices with Portland on the valley lanes','Gresham prices with %s on the valley lanes'%PO)
print('done')
