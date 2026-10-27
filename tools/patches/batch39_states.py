import re, sys
sys.path.insert(0,'/home/claude/tools'); import localpage as lp
S='/home/claude/build/shipguy/'
BLOCK=re.compile(r'<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">City Pages</p>.*?</section>', re.S)
def rep(h, old, new, n=1):
    c=h.count(old); assert c==n, (c, old[:80]); return h.replace(old,new)
def L(slug, name): return '<a href="/city/%s/">%s</a>' % (slug, name)
GR=L('auto-transport-grand-rapids-michigan','Grand Rapids'); WA=L('auto-transport-warren-michigan','Warren')
DA=L('auto-transport-davenport-iowa','Davenport'); SC=L('auto-transport-sioux-city-iowa','Sioux City'); AN=L('auto-transport-ankeny-iowa','Ankeny')
CO=L('auto-transport-columbia-maryland','Columbia'); GE=L('auto-transport-germantown-maryland','Germantown')

# ---------------- Michigan ----------------
p=S+'michigan-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Detroit, Grand Rapids, and Warren have their own pages with local lanes, meeting spots, and phone lines. '
       'Lansing, Ann Arbor, Flint, the north, and the Upper Peninsula are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('MI', intro), h, count=1)
h=rep(h,'<p class="ph-quick-note">Detroit has its own page covering the Motor City carrier pool, the Canada answer, and Selfridge. This page carries Grand Rapids, Lansing, Ann Arbor, Flint, the north, and the Upper Peninsula.</p>',
        '<p class="ph-quick-note">Detroit, %s, and %s have their own pages. This page carries Lansing, Ann Arbor, Flint, the north, and the Upper Peninsula.</p>' % (GR, WA))
h=rep(h,'<p>This page covers the corridors, Grand Rapids and the west side, and Lansing and the campuses. It also covers the north, the bridge, the Upper Peninsula, the snowbird lane, and the city page.</p>',
        '<p>This page covers the corridors, the west side, and Lansing and the campuses. It also covers the north, the bridge, the Upper Peninsula, the snowbird lane, and the city pages.</p>')
h=rep(h,'<p>Grand Rapids is the second-largest metro and one of the fastest-growing in the Midwest. The furniture makers and the hospitals relocate people on start dates. Its streets are wide, and the truck reaches the curb on most of them.</p>',
        '<p>%s is the second-largest metro and one of the fastest-growing in the Midwest. It has its own page now. The furniture makers and the hospitals relocate people on start dates. Its streets are wide, and the truck reaches the curb on most of them.</p>' % GR)
h=rep(h,'Assembly plants in Flint, Lansing, Orion, Warren, Sterling Heights, Wayne, and Dearborn load carriers every day.',
        'Assembly plants in Flint, Lansing, Orion, %s, Sterling Heights, Wayne, and Dearborn load carriers every day.' % WA)
h=rep(h,'Retirees from the Detroit suburbs, Grand Rapids, and the north ship cars to Florida from October through December.',
        'Retirees from the Detroit suburbs, %s, and the north ship cars to Florida from October through December.' % GR)
h=rep(h,'<span class="ph-chip">Grand Rapids</span>','<a class="ph-chip" href="/city/auto-transport-grand-rapids-michigan/">Grand Rapids</a>')
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'<p>Yes, Grand Rapids is the second-largest metro and one of the fastest-growing in the Midwest. Its streets are wide, and the truck reaches the curb on most of them. Chicago is a same-day lane from the west side, and lake-effect snow adds a day in winter.</p>',
              '<p>Yes, %s has its own page now. It is the second-largest metro and one of the fastest-growing in the Midwest. Its streets are wide, and the truck reaches the curb on most of them. Chicago is a same-day lane from the west side. Lake-effect snow adds a day in winter.</p>' % GR)
open(p,'w',encoding='utf-8').write(head+body); print('michigan updated')

# ---------------- Iowa (first City Pages block) ----------------
p=S+'iowa-auto-transport.html'; h=open(p,encoding='utf-8').read()
assert not BLOCK.search(h)
intro=('Davenport, Sioux City, and Ankeny have their own pages with local lanes, meeting spots, and phone lines. '
       'Des Moines, Cedar Rapids, Iowa City, Council Bluffs, and every other Iowa town are covered from this page.')
anchor='<section class="ph-sec"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">Des Moines</p>'
assert h.count(anchor)==1
h=h.replace(anchor, lp.state_cities_block('IA', intro)+'\n'+anchor)
assert BLOCK.search(h)
h=rep(h,'<p class="ph-quick-note">Iowa has no city page yet. This page carries the detail for Des Moines, Cedar Rapids, Iowa City, the Quad Cities, and the rest.</p>',
        '<p class="ph-quick-note">%s, %s, and %s have their own pages. This page carries the detail for Des Moines, Cedar Rapids, Iowa City, and the rest.</p>' % (DA, SC, AN))
h=rep(h,'<p>Davenport and Bettendorf are the Iowa half of the Quad Cities. Moline and Rock Island sit across the Mississippi in Illinois. The Army arsenal on the island rotates civilians.</p>',
        '<p>%s and Bettendorf are the Iowa half of the Quad Cities, and Davenport has its own page. Moline and Rock Island sit across the Mississippi in Illinois. The Army arsenal on the island rotates civilians.</p>' % DA)
h=rep(h,'Interstate 29 runs the western edge from Council Bluffs through Sioux City to South Dakota.',
        'Interstate 29 runs the western edge from Council Bluffs through %s to South Dakota.' % SC)
h=rep(h,'US 20 crosses the northern tier from Dubuque to Sioux City on four lanes.',
        'US 20 crosses the northern tier from Dubuque to Sioux City on four lanes. Sioux City has its own page.')
h=rep(h,'<p>West Des Moines, Ankeny, Waukee, and Urbandale add subdivisions faster than carrier maps update. Send the full address and the closest main road.</p>',
        '<p>West Des Moines, %s, Waukee, and Urbandale add subdivisions faster than carrier maps update. Ankeny has its own page. Send the full address and the closest main road.</p>' % AN)
for name, slug in [('Davenport','auto-transport-davenport-iowa'),('Sioux City','auto-transport-sioux-city-iowa'),('Ankeny','auto-transport-ankeny-iowa')]:
    h=rep(h,'<span class="ph-chip">%s</span>'%name, '<a class="ph-chip" href="/city/%s/">%s</a>'%(slug,name))
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'Davenport and Bettendorf ship with the Illinois half of the Quad Cities. Pricing follows the neighboring metro in each case.',
              '%s and Bettendorf ship with the Illinois half of the Quad Cities, and Davenport has its own page. Pricing follows the neighboring metro in each case.' % DA)
body=rep(body,'West Des Moines, Ankeny, and Waukee add subdivisions faster than carrier maps update, so send the full address.',
              'West Des Moines, %s, and Waukee add subdivisions faster than carrier maps update, so send the full address.' % AN)
open(p,'w',encoding='utf-8').write(head+body); print('iowa updated')

# ---------------- Maryland ----------------
p=S+'maryland-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Baltimore, Columbia, and Germantown have their own pages with local lanes, meeting spots, and phone lines. '
       'The rest of the Washington suburbs, Annapolis, Frederick, the Eastern Shore, and western Maryland are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('MD', intro), h, count=1)
h=rep(h,'<p class="ph-quick-note">Baltimore has its own page covering the port, the tunnels, and the rowhouse neighborhoods. This page carries Montgomery and Prince George’s counties, Annapolis, Frederick, the shore, and the west.</p>',
        '<p class="ph-quick-note">Baltimore, %s, and %s have their own pages. This page carries the rest of Montgomery and Prince George’s counties, Annapolis, Frederick, the shore, and the west.</p>' % (CO, GE))
h=rep(h,'Columbia and Howard County sit between the two cities.','%s and Howard County sit between the two cities, and Columbia has its own page.' % CO)
h=rep(h,'The newer suburbs toward Germantown and Clarksburg are wide grids.','The newer suburbs toward %s and Clarksburg are wide grids, and Germantown has its own page.' % GE)
for name, slug in [('Columbia','auto-transport-columbia-maryland'),('Germantown','auto-transport-germantown-maryland')]:
    h=rep(h,'<span class="ph-chip">%s</span>'%name, '<a class="ph-chip" href="/city/%s/">%s</a>'%(slug,name))
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'Gaithersburg, Germantown, and the newer suburbs allow curbside on most streets.',
              'Gaithersburg, %s, and the newer suburbs allow curbside on most streets.' % GE)
open(p,'w',encoding='utf-8').write(head+body); print('maryland updated')

# ---------------- Detroit city page ----------------
p=S+'city/auto-transport-detroit-michigan/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'The assembly plants in Dearborn, Sterling Heights, Warren, and Hamtramck load new vehicles onto trailers every day.',
        'The assembly plants in Dearborn, Sterling Heights, %s, and Hamtramck load new vehicles onto trailers every day.' % WA)
open(p,'w',encoding='utf-8').write(h); print('detroit updated')

# ---------------- Baltimore city page ----------------
p=S+'city/auto-transport-baltimore-maryland/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'Towson, Catonsville, Columbia, and the county suburbs are wide and simple.',
        'Towson, Catonsville, %s, and the county suburbs are wide and simple.' % CO)
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'Columbia and Towson are wide, easy deliveries.','%s and Towson are wide, easy deliveries, and Columbia has its own page.' % CO)
open(p,'w',encoding='utf-8').write(head+body); print('baltimore updated')
