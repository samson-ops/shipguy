import re, sys
sys.path.insert(0,'/home/claude/tools'); import localpage as lp
S='/home/claude/build/shipguy/'
BLOCK=re.compile(r'<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">City Pages</p>.*?</section>', re.S)
def rep(h, old, new, n=1):
    c=h.count(old); assert c==n, (c, old[:80]); return h.replace(old,new)
PO='<a href="/city/auto-transport-portland-maine/">Portland</a>'
LE='<a href="/city/auto-transport-lewiston-maine/">Lewiston</a>'
BA='<a href="/city/auto-transport-bangor-maine/">Bangor</a>'
p=S+'maine-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Augusta, Portland, Lewiston, and Bangor have their own pages covering the capital, the carrier hub, the Twin Cities, and the top of the run. '
       'The coast, the lakes, the northern counties, and the rest of Maine are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('ME', intro), h, count=1)
h=rep(h,'<p>This page covers the corridor and where carriers turn around, Portland and the coast, and the two seasons. It also covers the shipyards, mud season, and the city with its own page.</p>',
        '<p>This page covers the corridor and where carriers turn around, the coast, and the two seasons. It also covers the shipyards, mud season, and the four cities with their own pages.</p>')
h=rep(h,'<p class="ph-lead">Portland is the carrier hub of the state, and the coast beyond it runs on a summer clock.</p>',
        '<p class="ph-lead">%s is the carrier hub of the state, and the coast beyond it runs on a summer clock.</p>' % PO)
h=rep(h,'<p class="ph-lead">Every carrier serving Maine comes up Interstate 95, and most turn around at Bangor.</p>',
        '<p class="ph-lead">Every carrier serving Maine comes up Interstate 95, and most turn around at %s.</p>' % BA)
h=rep(h,'<p>The University of Maine in Orono and the campuses in Portland and Lewiston bring cars in each September.',
        '<p>The University of Maine in Orono and the campuses in Portland and %s bring cars in each September.' % LE)
h=rep(h,'The peninsula’s streets are narrow. The driver meets you on Marginal Way or at a lot off 295.</p>',
        'The peninsula’s streets are narrow. The driver meets you on Marginal Way or at a lot off 295. The Portland page covers the peninsula, cruise season, and the January tides.</p>')
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'Pickups run 2 to 4 days south of Bangor. The coast in summer and the north take 3 to 6 days.',
              'Pickups run 2 to 4 days south of %s. The coast in summer and the north take 3 to 6 days.' % BA)
body=rep(body,'Orono sits off Interstate 95 above Bangor, and the handoff happens at a lot near campus. Portland, Lewiston, and Brunswick campuses follow the same calendar.',
              'Orono sits off Interstate 95 above Bangor, and the handoff happens at a lot near campus. %s, %s, and Brunswick campuses follow the same calendar.' % (PO,LE))
h=head+body
open(p,'w',encoding='utf-8').write(h); print('maine updated')
# Augusta page links
p=S+'city/auto-transport-augusta-maine/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'<p>Few trucks base themselves north of Portland. Most come up the Turnpike on a run to Bangor or the coast. Augusta stops get added along the way.</p>',
        '<p>Few trucks base themselves north of %s. Most come up the Turnpike on a run to %s or the coast. Augusta stops get added along the way.</p>' % (PO,BA))
h=rep(h,'<p>Colby in Waterville, Bates in Lewiston, and Bowdoin in Brunswick are all within forty miles.',
        '<p>Colby in Waterville, Bates in %s, and Bowdoin in Brunswick are all within forty miles.' % LE)
open(p,'w',encoding='utf-8').write(h); print('augusta updated')
