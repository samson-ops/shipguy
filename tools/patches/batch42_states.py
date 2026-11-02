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
LA=L('auto-transport-lansing-michigan','Lansing'); VA=L('auto-transport-vancouver-washington','Vancouver')
CH=L('auto-transport-chesapeake-virginia','Chesapeake'); RI=L('auto-transport-richmond-virginia','Richmond')
ER=L('auto-transport-erie-pennsylvania','Erie'); CR=L('auto-transport-cranston-rhode-island','Cranston')

# ---------------- Michigan ----------------
p=S+'michigan-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Detroit, Grand Rapids, Warren, Ann Arbor, and Lansing have their own pages with local lanes, meeting spots, and phone lines. '
       'Flint, Kalamazoo, the north, and the Upper Peninsula are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('MI', intro), h, count=1)
h=rep(h,'have their own pages. This page carries Lansing, Flint, the north, and the Upper Peninsula.</p>',
        'have their own pages, and so does %s. This page carries Flint, Kalamazoo, the north, and the Upper Peninsula.</p>' % LA)
h=rep(h,'<p>Lansing has the capital and the state university in East Lansing.','<p>%s has the capital and the state university in East Lansing, and its own page now.' % LA)
h=chip(h,'Lansing','auto-transport-lansing-michigan')
h=faq_edit(h,'Move-in week in East Lansing clogs every road, and <a href="/city/auto-transport-ann-arbor-michigan/">Ann Arbor</a> is tight year round.',
             'Move-in week in East Lansing clogs every road, and the %s page covers it. <a href="/city/auto-transport-ann-arbor-michigan/">Ann Arbor</a> is tight year round.' % LA)
open(p,'w',encoding='utf-8').write(h); resync(p); print('michigan updated')

# ---------------- Washington ----------------
p=S+'washington-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Seattle, Spokane, and Vancouver have their own pages with local lanes, meeting spots, and phone lines. '
       'Bellevue, Tacoma, Everett, Olympia, the Tri-Cities, and every other Washington town are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('WA', intro), h, count=1)
h=rep(h,'<a href="/city/auto-transport-spokane-washington/">Spokane</a> have their own pages. This page carries the detail for Bellevue, Tacoma, Everett, Olympia, the Tri-Cities, and the rest.</p>',
        '<a href="/city/auto-transport-spokane-washington/">Spokane</a>, and %s have their own pages. This page carries the detail for Bellevue, Tacoma, Everett, Olympia, the Tri-Cities, and the rest.</p>' % VA)
h=rep(h,'<p>Vancouver at the south end ships through the Portland carrier pool.','<p>%s at the south end ships through the Portland carrier pool, and it has its own page.' % VA)
h=rep(h,'Spokane sits closer to the Mountain West, and Vancouver follows Portland lanes.','Spokane sits closer to the Mountain West, and %s follows Portland lanes.' % VA)
h=chip(h,'Vancouver','auto-transport-vancouver-washington')
open(p,'w',encoding='utf-8').write(h); print('washington updated')

# ---------------- Virginia ----------------
p=S+'virginia-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Virginia Beach, Chesapeake, and Richmond have their own pages with local lanes, meeting spots, and phone lines. '
       'Arlington, Fairfax, Norfolk, Roanoke, Charlottesville, and every other Virginia town are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('VA', intro), h, count=1)
h=rep(h,'<p class="ph-quick-note"><a href="/city/auto-transport-virginia-beach-virginia/">Virginia Beach</a> has its own page. This page carries the detail for Arlington, Fairfax, Richmond, Norfolk, Roanoke, Charlottesville, and the rest.</p>',
        '<p class="ph-quick-note"><a href="/city/auto-transport-virginia-beach-virginia/">Virginia Beach</a>, %s, and %s have their own pages. This page carries the detail for Arlington, Fairfax, Norfolk, Roanoke, Charlottesville, and the rest.</p>' % (CH, RI))
h=rep(h,'Virginia Beach</a>, Chesapeake, and Suffolk are wide suburbs where the truck reaches the curb. Virginia Beach has its own page now.',
        'Virginia Beach</a>, %s, and Suffolk are wide suburbs where the truck reaches the curb. Virginia Beach and Chesapeake have their own pages now.' % CH)
h=rep(h,'<p class="ph-lead">Richmond sits where Interstate 95 and 64 cross, and carriers stage there for the whole state.</p>',
        '<p class="ph-lead">%s sits where Interstate 95 and 64 cross, and carriers stage there for the whole state. It has its own page now.</p>' % RI)
for name, slug in [('Chesapeake','auto-transport-chesapeake-virginia'),('Richmond','auto-transport-richmond-virginia')]: h=chip(h,name,slug)
open(p,'w',encoding='utf-8').write(h); print('virginia updated')

# ---------------- Pennsylvania ----------------
p=S+'pennsylvania-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Philadelphia, Pittsburgh, Allentown, Reading, and Erie have their own pages with local lanes, meeting spots, and phone lines. '
       'Harrisburg, Scranton, State College, and the rest of Pennsylvania are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('PA', intro), h, count=1)
h=rep(h,'<a href="/city/auto-transport-reading-pennsylvania/">Reading</a> have their own pages. This page carries Harrisburg, Scranton, Erie, State College, and the rest of the state.</p>',
        '<a href="/city/auto-transport-reading-pennsylvania/">Reading</a>, and %s have their own pages. This page carries Harrisburg, Scranton, State College, and the rest of the state.</p>' % ER)
h=rep(h,'Scranton follows the Interstate 81 lanes, and Erie follows Buffalo and Cleveland.','Scranton follows the Interstate 81 lanes, and %s follows Buffalo and Cleveland.' % ER)
h=rep(h,'<p>Erie sits on the lake and gets buried by lake-effect snow from November through March.','<p>%s sits on the lake and gets buried by lake-effect snow from November through March. It has its own page now.' % ER)
h=chip(h,'Erie','auto-transport-erie-pennsylvania')
h=faq_edit(h,'Erie gets buried by lake-effect snow. Carriers wait for the plows.','Erie gets buried by lake-effect snow, and the %s page covers the winter. Carriers wait for the plows.' % ER)
open(p,'w',encoding='utf-8').write(h); resync(p); print('pennsylvania updated')

# ---------------- Rhode Island (first City Pages block) ----------------
p=S+'rhode-island-auto-transport.html'; h=open(p,encoding='utf-8').read()
assert not BLOCK.search(h)
intro=('Cranston has its own page with local lanes, meeting spots, and a phone line. '
       'Providence, Warwick, Pawtucket, Newport, Westerly, and every other Rhode Island town are covered from this page.')
anchor='<section class="ph-sec"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">Providence</p>'
assert h.count(anchor)==1
h=h.replace(anchor, lp.state_cities_block('RI', intro)+'\n'+anchor)
assert BLOCK.search(h)
h=rep(h,'<p class="ph-quick-note">Rhode Island has no city page yet. This page carries the detail for Providence, Warwick, Cranston, Newport, Westerly, and the rest.</p>',
        '<p class="ph-quick-note">%s has its own page. This page carries the detail for Providence, Warwick, Newport, Westerly, and the rest.</p>' % CR)
h=rep(h,'<p>Warwick and Cranston to the south are wide grids where the truck usually reaches the curb.','<p>Warwick and %s to the south are wide grids where the truck usually reaches the curb. Cranston has its own page now.' % CR)
h=chip(h,'Cranston','auto-transport-cranston-rhode-island')
open(p,'w',encoding='utf-8').write(h); print('rhode island updated (first block)')

# ---------------- neighbor city pages: link the first plain prose mention ----------------
def link_first(path, city, slug):
    p=S+path; h=open(p,encoding='utf-8').read()
    a=h.index('<section class="ph-stats">'); b=h.index('<footer')
    pat=re.compile(r'(?<![>\w])%s(?![\w<])' % re.escape(city))
    for m in re.finditer(r'<p(?: class="ph-(?:lead|sub|quick-note)")?>(.*?)</p>', h[a:b], re.S):
        if '<table' in m.group(0): continue
        mm=pat.search(m.group(1))
        if mm and ('href="/city/%s/'%slug) not in m.group(1):
            start=a+m.start(1)+mm.start()
            h=h[:start]+'<a href="/city/%s/">%s</a>'%(slug,city)+h[start+len(city):]
            open(p,'w',encoding='utf-8').write(h); print(path.split('/')[1], '-> linked', city); return
    raise SystemExit('no plain mention of %s in %s' % (city, path))
link_first('city/auto-transport-grand-rapids-michigan/index.html','Lansing','auto-transport-lansing-michigan')
link_first('city/auto-transport-portland-oregon/index.html','Vancouver','auto-transport-vancouver-washington')
link_first('city/auto-transport-virginia-beach-virginia/index.html','Chesapeake','auto-transport-chesapeake-virginia')
link_first('city/auto-transport-virginia-beach-virginia/index.html','Richmond','auto-transport-richmond-virginia')
for pg in ['raleigh-north-carolina','durham-north-carolina','columbia-maryland','germantown-maryland','charlotte-north-carolina']:
    link_first('city/auto-transport-%s/index.html'%pg,'Richmond','auto-transport-richmond-virginia')
link_first('city/auto-transport-pittsburgh-pennsylvania/index.html','Erie','auto-transport-erie-pennsylvania')
