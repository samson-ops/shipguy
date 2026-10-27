import re, sys
sys.path.insert(0,'/home/claude/tools'); import localpage as lp
S='/home/claude/build/shipguy/'
BLOCK=re.compile(r'<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">City Pages</p>.*?</section>', re.S)
def rep(h, old, new, n=1):
    c=h.count(old); assert c==n, (c, old[:80]); return h.replace(old,new)
def L(slug, name): return '<a href="/city/%s/">%s</a>' % (slug, name)
def chip(h, name, slug): return rep(h,'<span class="ph-chip">%s</span>'%name, '<a class="ph-chip" href="/city/%s/">%s</a>'%(slug,name))
VB=L('auto-transport-virginia-beach-virginia','Virginia Beach'); PI=L('auto-transport-pittsburgh-pennsylvania','Pittsburgh')
AL=L('auto-transport-allentown-pennsylvania','Allentown'); RD=L('auto-transport-reading-pennsylvania','Reading')

# ---------------- Virginia (first City Pages block) ----------------
p=S+'virginia-auto-transport.html'; h=open(p,encoding='utf-8').read()
assert not BLOCK.search(h)
intro=('Virginia Beach has its own page with local lanes, meeting spots, and a phone line. '
       'Arlington, Fairfax, Richmond, Norfolk, Roanoke, Charlottesville, and every other Virginia town are covered from this page.')
anchor='<section class="ph-sec"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">Northern Virginia</p>'
assert h.count(anchor)==1
h=h.replace(anchor, lp.state_cities_block('VA', intro)+'\n'+anchor)
assert BLOCK.search(h)
h=rep(h,'<p class="ph-quick-note">Virginia has no city page yet. This page carries the detail for Arlington, Fairfax, Richmond, Norfolk, Virginia Beach, Roanoke, Charlottesville, and the rest.</p>',
        '<p class="ph-quick-note">%s has its own page. This page carries the detail for Arlington, Fairfax, Richmond, Norfolk, Roanoke, Charlottesville, and the rest.</p>' % VB)
h=rep(h,'It also covers Hampton Roads and its bases, the valley and the campuses, the southwest, and the weather.</p>',
        'It also covers Hampton Roads and its bases, the valley and the campuses, the southwest, the weather, and the city page.</p>')
h=rep(h,'Virginia Beach, Chesapeake, and Suffolk are wide suburbs where the truck reaches the curb.',
        '%s, Chesapeake, and Suffolk are wide suburbs where the truck reaches the curb. Virginia Beach has its own page now.' % VB)
h=chip(h,'Virginia Beach','auto-transport-virginia-beach-virginia')
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'Every installation in the state is a steady lane for us. Many ship a second vehicle with us, since orders may cover a single car.',
              'Every installation in the state is a steady lane for us, and the %s page covers Oceana and Little Creek. Many ship a second vehicle with us, since orders may cover a single car.' % VB)
open(p,'w',encoding='utf-8').write(head+body); print('virginia updated')

# ---------------- Pennsylvania ----------------
p=S+'pennsylvania-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Philadelphia, Pittsburgh, Allentown, and Reading have their own pages with local lanes, meeting spots, and phone lines. '
       'Harrisburg, Scranton, Erie, State College, and the rest of Pennsylvania are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('PA', intro), h, count=1)
h=rep(h,'<p class="ph-quick-note">Philadelphia has its own page covering the rowhouse streets, the Main Line, and the Schuylkill. This page carries Pittsburgh, Harrisburg, Allentown, Scranton, Erie, State College, and the rest of the state.</p>',
        '<p class="ph-quick-note">Philadelphia, %s, %s, and %s have their own pages. This page carries Harrisburg, Scranton, Erie, State College, and the rest of the state.</p>' % (PI, AL, RD))
h=rep(h,'This page covers the Turnpike and Interstate 80, Pittsburgh and its hills, and Harrisburg and the warehouse hub.',
        'This page covers the Turnpike and Interstate 80, Harrisburg and the warehouse hub, and the four city pages.')
h=rep(h,'<p class="ph-lead">Pittsburgh is the hardest big city in the country for a seventy-five-foot trailer, and carriers plan every stop.</p>',
        '<p class="ph-lead">%s is the hardest big city in the country for a seventy-five-foot trailer, and carriers plan every stop. It has its own page now.</p>' % PI)
h=rep(h,'Allentown, Bethlehem, and Easton fill with households commuting to New York and Philadelphia.',
        '%s, Bethlehem, and Easton fill with households commuting to New York and Philadelphia. Allentown has its own page.' % AL)
h=rep(h,'Lancaster and York add the Amish country and the manufacturing plants.',
        'Lancaster and York add the Amish country and the manufacturing plants. %s has its own page for Berks County.' % RD)
for name, slug in [('Pittsburgh','auto-transport-pittsburgh-pennsylvania'),('Allentown','auto-transport-allentown-pennsylvania'),('Reading','auto-transport-reading-pennsylvania')]:
    h=chip(h,name,slug)
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'<p>Rarely on the hills. Steep, narrow streets, the bridges, and the tunnels keep a seventy-five-foot trailer in the flats.',
              '<p>Rarely on the hills, and the %s page goes through it neighborhood by neighborhood. Steep, narrow streets, the bridges, and the tunnels keep a seventy-five-foot trailer in the flats.' % PI)
open(p,'w',encoding='utf-8').write(head+body); print('pennsylvania updated')

# ---------------- neighbor city pages ----------------
def one(path, old, new, faq=False):
    p=S+path; h=open(p,encoding='utf-8').read()
    if faq:
        i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
        body=rep(body,old,new); h=head+body
    else:
        h=rep(h,old,new)
    open(p,'w',encoding='utf-8').write(h); print(path.split('/')[1] if '/' in path else path, 'updated')
one('city/auto-transport-philadelphia-pennsylvania/index.html','The Turnpike west to Pittsburgh is steady.','The Turnpike west to %s is steady.' % PI)
one('city/auto-transport-cleveland-ohio/index.html','Columbus, Pittsburgh, Detroit, and Buffalo are same-day lanes.','Columbus, %s, Detroit, and Buffalo are same-day lanes.' % PI)
one('city/auto-transport-akron-ohio/index.html','Carriers running between Cleveland and Pittsburgh pass the city every day.','Carriers running between Cleveland and %s pass the city every day.' % PI)
one('city/auto-transport-columbus-ohio/index.html','Interstate 70 runs from Pittsburgh and Washington through the city to Indianapolis and beyond.','Interstate 70 runs from %s and Washington through the city to Indianapolis and beyond.' % PI)
one('city/auto-transport-buffalo-new-york/index.html','Rochester, Cleveland, and Pittsburgh are same-day lanes.','Rochester, Cleveland, and %s are same-day lanes.' % PI)
