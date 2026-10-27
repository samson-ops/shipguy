import re, sys
sys.path.insert(0,'/home/claude/tools'); import localpage as lp
S='/home/claude/build/shipguy/'
BLOCK=re.compile(r'<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">City Pages</p>.*?</section>', re.S)
def rep(h, old, new, n=1):
    c=h.count(old); assert c==n, (c, old[:80]); return h.replace(old,new)
RO='<a href="/city/auto-transport-rockford-illinois/">Rockford</a>'
SP='<a href="/city/auto-transport-springfield-illinois/">Springfield</a>'
CH='<a href="/city/auto-transport-champaign-illinois/">Champaign</a>'
WA='<a href="/city/auto-transport-waukegan-illinois/">Waukegan</a>'
p=S+'illinois-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Chicago, Aurora, Joliet, Waukegan, Rockford, Springfield, and Champaign have their own pages with neighborhood meeting spots, the tollways, '
       'the campus calendar, and the session. The other suburbs, Peoria, the Metro East, and the rest of Illinois are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('IL', intro), h, count=1)
h=rep(h,'<p class="ph-quick-note">Chicago, Aurora, and Joliet have their own pages covering the viaducts, the tollways, and the lift bridges. This page carries the other suburbs, downstate, and the rest of the state.</p>',
        '<p class="ph-quick-note">Chicago, the collar cities, Rockford, Springfield, and Champaign have their own pages covering the viaducts, the tollways, the campus, and the session. This page carries the other suburbs, Peoria, the Metro East, and the rest of the state.</p>')
h=rep(h,'<p>Peoria ships around the heavy-equipment plants. The Quad Cities ship around the farm-equipment maker and the arsenal on the river. Springfield adds state government moves.</p>',
        '<p>Peoria ships around the heavy-equipment plants. The Quad Cities ship around the farm-equipment maker and the arsenal on the river. %s adds state government moves, and its page covers the session and the State Fair.</p>' % SP)
h=rep(h,'<p>Carbondale, Decatur, Rockford, and the Metro East sit on their own corridors.',
        '<p>Carbondale, Decatur, %s, and the Metro East sit on their own corridors. The Rockford page covers 90, 39, and the cargo airport.' % RO)
h=rep(h,'<p>The University of Illinois in Champaign-Urbana is one of the largest campuses in the country. Cars come in each August and go home each May. The handoff happens at a lot off Interstate 57 or 74.</p>',
        '<p>The University of Illinois in Champaign-Urbana is one of the largest campuses in the country. Cars come in each August and go home each May. The handoff happens at a lot off Interstate 57 or 74. The %s page covers move-in weekend and football Saturdays.</p>' % CH)
h=rep(h,'%s on the Fox River and <a href="/city/auto-transport-joliet-illinois/">Joliet</a> on the Des Plaines have their own pages.' % '<a href="/city/auto-transport-aurora-illinois/">Aurora</a>',
        '<a href="/city/auto-transport-aurora-illinois/">Aurora</a> on the Fox River, <a href="/city/auto-transport-joliet-illinois/">Joliet</a> on the Des Plaines, and %s on the lake have their own pages.' % WA)
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'<p>Yes, everything outside the <a href="/city/auto-transport-chicago-illinois/">Chicago</a> page is covered here. Champaign ships on the campus calendar, and Bloomington-Normal on the insurance and plant calendars. Peoria and the Quad Cities ship around the equipment plants. Downstate pickups run 1 to 3 days on Interstate 55 and 57. The farm counties take 2 to 4 days.</p>',
         '<p>Yes. %s and %s have their own pages, and everything else downstate is covered here. Champaign ships on the campus calendar, and Bloomington-Normal on the insurance and plant calendars. Peoria and the Quad Cities ship around the equipment plants. Downstate pickups run 1 to 3 days on Interstate 55 and 57. The farm counties take 2 to 4 days.</p>' % (SP,CH))
h=head+body
open(p,'w',encoding='utf-8').write(h); print('illinois updated')
