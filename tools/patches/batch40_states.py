import re, sys
sys.path.insert(0,'/home/claude/tools'); import localpage as lp
S='/home/claude/build/shipguy/'
BLOCK=re.compile(r'<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">City Pages</p>.*?</section>', re.S)
def rep(h, old, new, n=1):
    c=h.count(old); assert c==n, (c, old[:80]); return h.replace(old,new)
def L(slug, name): return '<a href="/city/%s/">%s</a>' % (slug, name)
def chip(h, name, slug): return rep(h,'<span class="ph-chip">%s</span>'%name, '<a class="ph-chip" href="/city/%s/">%s</a>'%(slug,name))
SB=L('auto-transport-south-bend-indiana','South Bend'); LW=L('auto-transport-lawrence-kansas','Lawrence'); LF=L('auto-transport-lafayette-louisiana','Lafayette')
AA=L('auto-transport-ann-arbor-michigan','Ann Arbor'); SE=L('auto-transport-seattle-washington','Seattle'); SP=L('auto-transport-spokane-washington','Spokane')

# ---------------- Washington (first City Pages block) ----------------
p=S+'washington-auto-transport.html'; h=open(p,encoding='utf-8').read()
assert not BLOCK.search(h)
intro=('Seattle and Spokane have their own pages with local lanes, meeting spots, and phone lines. '
       'Bellevue, Tacoma, Everett, Olympia, the Tri-Cities, and every other Washington town are covered from this page.')
anchor='<section class="ph-sec"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">Seattle &amp; the East Side</p>'
assert h.count(anchor)==1
h=h.replace(anchor, lp.state_cities_block('WA', intro)+'\n'+anchor)
assert BLOCK.search(h)
h=rep(h,'<p class="ph-quick-note">Washington has no city page yet. This page carries the detail for Seattle, Bellevue, Tacoma, Everett, Olympia, Spokane, the Tri-Cities, and the rest.</p>',
        '<p class="ph-quick-note">%s and %s have their own pages. This page carries the detail for Bellevue, Tacoma, Everett, Olympia, the Tri-Cities, and the rest.</p>' % (SE, SP))
h=rep(h,'<p>This page covers the corridor, Seattle and the tech relocations, the bases on the Sound, and the passes. It also covers Spokane and the east, the ferries and the peninsula, the ports, and the weather.</p>',
        '<p>This page covers the corridor, the tech relocations, the bases on the Sound, and the passes. It also covers the east side of the state, the ferries and the peninsula, the ports, the weather, and the two city pages.</p>')
h=rep(h,'<p class="ph-lead">Seattle and Bellevue relocate more engineers than almost any metro in the country. Most of them ship a car.</p>',
        '<p class="ph-lead">%s and Bellevue relocate more engineers than almost any metro in the country. Most of them ship a car, and Seattle has its own page now.</p>' % SE)
h=rep(h,'Spokane is the second-largest city in the state and the hub for eastern Washington and the Idaho panhandle.',
        '%s is the second-largest city in the state and the hub for eastern Washington and the Idaho panhandle. It has its own page now.' % SP)
h=chip(h,'Seattle','auto-transport-seattle-washington'); h=chip(h,'Spokane','auto-transport-spokane-washington')
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,"<p>Rarely on the hills or downtown. Seattle's streets are steep and narrow, and the towers run on garages.",
              "<p>Rarely on the hills or downtown, and the %s page goes through it street by street. Seattle's streets are steep and narrow, and the towers run on garages." % SE)
body=rep(body,'<p>Yes, Spokane is the second-largest market in the state for us.','<p>Yes, %s is the second-largest market in the state for us, and it has its own page.' % SP)
body=rep(body,'Many east-side subdivisions have gates, so send the community name.</p>','Many east-side subdivisions have gates, so send the community name. The %s page covers the lots and the hills.</p>' % SE)
open(p,'w',encoding='utf-8').write(head+body); print('washington updated')

# ---------------- Indiana ----------------
p=S+'indiana-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Indianapolis, Fort Wayne, Evansville, and South Bend have their own pages with local lanes, meeting spots, and phone lines. '
       'Bloomington, Lafayette, Gary, and the rest of Indiana are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('IN', intro), h, count=1)
h=rep(h,'<p class="ph-quick-note">Indianapolis, Fort Wayne, and Evansville have their own pages covering the loop, the 469 bypass, and the Lloyd. This page carries South Bend, the campuses, and the rest of the state.</p>',
        '<p class="ph-quick-note">Indianapolis, Fort Wayne, Evansville, and %s have their own pages. This page carries the campuses and the rest of the state.</p>' % SB)
h=rep(h,'The Toll Road carries Interstate 80 and 90 across the north through Gary, South Bend, and Elkhart.',
        'The Toll Road carries Interstate 80 and 90 across the north through Gary, %s, and Elkhart.' % SB)
h=chip(h,'South Bend','auto-transport-south-bend-indiana')
open(p,'w',encoding='utf-8').write(h); print('indiana updated')

# ---------------- Kansas ----------------
p=S+'kansas-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Wichita, Overland Park, Olathe, Topeka, and Lawrence have their own pages with local lanes, meeting spots, and phone lines. '
       'Manhattan, Kansas City, Kansas, and the rest of the state are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('KS', intro), h, count=1)
h=rep(h,'<p class="ph-quick-note">Wichita, Overland Park, Olathe, and Topeka have their own pages. This page carries Lawrence, Manhattan, Kansas City, Kansas, and the rest of the state.</p>',
        '<p class="ph-quick-note">Wichita, Overland Park, Olathe, Topeka, and %s have their own pages. This page carries Manhattan, Kansas City, Kansas, and the rest of the state.</p>' % LW)
h=rep(h,'Interstate 70 runs from Kansas City through Lawrence, <a href="/city/auto-transport-topeka-kansas/">Topeka</a>, Salina, and Hays to the Colorado line.',
        'Interstate 70 runs from Kansas City through %s, <a href="/city/auto-transport-topeka-kansas/">Topeka</a>, Salina, and Hays to the Colorado line.' % LW)
h=rep(h,'The University of Kansas in Lawrence and Kansas State in Manhattan bring cars in each August.',
        'The University of Kansas in %s and Kansas State in Manhattan bring cars in each August. Lawrence has its own page.' % LW)
h=chip(h,'Lawrence','auto-transport-lawrence-kansas')
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'Lawrence and Manhattan have older, hilly streets near campus, so the handoff happens at a lot nearby.',
              '%s and Manhattan have older, hilly streets near campus, so the handoff happens at a lot nearby.' % LW)
open(p,'w',encoding='utf-8').write(head+body); print('kansas updated')

# ---------------- Louisiana ----------------
p=S+'louisiana-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('New Orleans, Metairie, Baton Rouge, Shreveport, and Lafayette have their own pages with local lanes, meeting spots, and phone lines. '
       'Lake Charles, Houma, Alexandria, and the rest of Louisiana are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('LA', intro), h, count=1)
h=rep(h,'Interstate 10 crosses the south from Lake Charles through Lafayette and Baton Rouge to New Orleans.',
        'Interstate 10 crosses the south from Lake Charles through %s and Baton Rouge to New Orleans.' % LF)
h=rep(h,'This page covers the corridors, the plants, Lafayette and the oil patch, and both bases.',
        'This page covers the corridors, the plants, the oil patch, and both bases.')
h=rep(h,'Lafayette is the center of the oil patch, and offshore workers rotate through Houma and the bayou towns.',
        '%s is the center of the oil patch, and it has its own page now. Offshore workers rotate through Houma and the bayou towns.' % LF)
h=rep(h,'The University of Louisiana in Lafayette follows the same calendar.','The University of Louisiana in %s follows the same calendar.' % LF)
h=chip(h,'Lafayette','auto-transport-lafayette-louisiana')
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'A carrier crossing between Lafayette and Baton Rouge can lose hours.','A carrier crossing between %s and Baton Rouge can lose hours.' % LF)
body=rep(body,'The handoff happens at a lot near campus. An adult signs for the vehicle when it loads.</p>',
              'The handoff happens at a lot near campus, and the %s page covers the Cajun side. An adult signs for the vehicle when it loads.</p>' % LF)
open(p,'w',encoding='utf-8').write(head+body); print('louisiana updated')

# ---------------- Michigan ----------------
p=S+'michigan-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Detroit, Grand Rapids, Warren, and Ann Arbor have their own pages with local lanes, meeting spots, and phone lines. '
       'Lansing, Flint, the north, and the Upper Peninsula are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('MI', intro), h, count=1)
h=rep(h,'<p class="ph-quick-note">Detroit, <a href="/city/auto-transport-grand-rapids-michigan/">Grand Rapids</a>, and <a href="/city/auto-transport-warren-michigan/">Warren</a> have their own pages. This page carries Lansing, Ann Arbor, Flint, the north, and the Upper Peninsula.</p>',
        '<p class="ph-quick-note">Detroit, <a href="/city/auto-transport-grand-rapids-michigan/">Grand Rapids</a>, <a href="/city/auto-transport-warren-michigan/">Warren</a>, and %s have their own pages. This page carries Lansing, Flint, the north, and the Upper Peninsula.</p>' % AA)
h=rep(h,'Ann Arbor ships on the university calendar, and Kalamazoo, Mount Pleasant, and Ypsilanti add smaller waves.',
        '%s ships on the university calendar and has its own page. Kalamazoo, Mount Pleasant, and Ypsilanti add smaller waves.' % AA)
h=chip(h,'Ann Arbor','auto-transport-ann-arbor-michigan')
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'Move-in week in East Lansing clogs every road, and Ann Arbor is tight year round.',
              'Move-in week in East Lansing clogs every road, and %s is tight year round.' % AA)
open(p,'w',encoding='utf-8').write(head+body); print('michigan updated')

# ---------------- Detroit ----------------
p=S+'city/auto-transport-detroit-michigan/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'The University of Michigan in Ann Arbor and Wayne State downtown both send cars in each September.',
        'The University of Michigan in %s and Wayne State downtown both send cars in each September.' % AA)
h=rep(h,'Serving Wayne, Oakland, and Macomb Counties and Ann Arbor.','Serving Wayne, Oakland, and Macomb Counties and %s.' % AA)
h=chip(h,'Ann Arbor','auto-transport-ann-arbor-michigan')
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'Ann Arbor is forty miles west and easy to reach.','%s is forty miles west and easy to reach, and it has its own page.' % AA)
open(p,'w',encoding='utf-8').write(head+body); print('detroit updated')

# ---------------- Portland OR ----------------
p=S+'city/auto-transport-portland-oregon/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'Interstate 5 runs from Seattle to California through the middle of the city.','Interstate 5 runs from %s to California through the middle of the city.' % SE)
open(p,'w',encoding='utf-8').write(h); print('portland updated')

# ---------------- Boise ----------------
p=S+'city/auto-transport-boise-idaho/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'Salt Lake City and Portland are a day out, and so is Spokane.','Salt Lake City and Portland are a day out, and so is %s.' % SP)
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'Seattle runs four hundred to five hundred seventy, about five hundred miles on 90 and 84.','%s runs four hundred to five hundred seventy, about five hundred miles on 90 and 84.' % SE)
open(p,'w',encoding='utf-8').write(head+body); print('boise updated')

# ---------------- Topeka ----------------
p=S+'city/auto-transport-topeka-kansas/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'Lawrence sits twenty-five minutes east on the Turnpike.','%s sits twenty-five minutes east on the Turnpike.' % LW)
h=chip(h,'Lawrence','auto-transport-lawrence-kansas')
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'Lawrence rides the same carriers off the Turnpike, and the handoff happens at a lot near campus.','%s rides the same carriers off the Turnpike, and the handoff happens at a lot near campus. It has its own page.' % LW)
open(p,'w',encoding='utf-8').write(head+body); print('topeka updated')

# ---------------- Olathe ----------------
p=S+'city/auto-transport-olathe-kansas/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'K-10 crosses the north edge of the city from 435 to Lawrence, and the Lawrence carriers use it.','K-10 crosses the north edge of the city from 435 to %s, and the Lawrence carriers use it.' % LW)
open(p,'w',encoding='utf-8').write(h); print('olathe updated')

# ---------------- Kansas City MO ----------------
p=S+'city/auto-transport-kansas-city-missouri/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'The University of Kansas in Lawrence sits forty minutes west on Interstate 70.','The University of Kansas in %s sits forty minutes west on Interstate 70.' % LW)
h=chip(h,'Lawrence','auto-transport-lawrence-kansas')
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'Lawrence fills on move-in weekend, and campus streets on both sides of the line are tight.','%s fills on move-in weekend, and campus streets on both sides of the line are tight.' % LW)
open(p,'w',encoding='utf-8').write(head+body); print('kansas city updated')

# ---------------- Baton Rouge ----------------
p=S+'city/auto-transport-baton-rouge-louisiana/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'Interstate 10 comes across the Atchafalaya Basin from Lafayette and crosses the river on the bridge downtown.','Interstate 10 comes across the Atchafalaya Basin from %s and crosses the river on the bridge downtown.' % LF)
open(p,'w',encoding='utf-8').write(h); print('baton rouge updated')
