import re, sys
sys.path.insert(0,'/home/claude/tools'); import localpage as lp
S='/home/claude/build/shipguy/'
BLOCK=re.compile(r'<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">City Pages</p>.*?</section>', re.S)
def rep(h, old, new, n=1):
    c=h.count(old); assert c==n, (c, old[:80]); return h.replace(old,new)
def do(fn, st, intro, edits, faq_edits):
    p=S+fn; h=open(p,encoding='utf-8').read()
    assert BLOCK.search(h), fn
    h=BLOCK.sub(lambda m: lp.state_cities_block(st, intro), h, count=1)
    for old,new in edits: h=rep(h,old,new)
    i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
    for old,new in faq_edits: body=rep(body,old,new)
    open(p,'w',encoding='utf-8').write(head+body); print('updated',fn)

OP='<a href="/city/auto-transport-overland-park-kansas/">Overland Park</a>'
OL='<a href="/city/auto-transport-olathe-kansas/">Olathe</a>'
TO='<a href="/city/auto-transport-topeka-kansas/">Topeka</a>'
do('kansas-auto-transport.html','KS',
 'Wichita, Overland Park, Olathe, and Topeka have their own pages with the aerospace plants, McConnell, the 435 loop, the Turnpike, and neighborhood meeting spots. Lawrence, Manhattan, Kansas City, Kansas, and the rest of the state are covered from this page.',
 [('<p class="ph-quick-note">Wichita has its own page covering the aerospace plants and McConnell. This page carries Johnson County, Topeka, Lawrence, Manhattan, and the rest of the state.</p>',
   '<p class="ph-quick-note">Wichita, Overland Park, Olathe, and Topeka have their own pages. This page carries Lawrence, Manhattan, Kansas City, Kansas, and the rest of the state.</p>'),
  ('<p>Overland Park, Olathe, Lenexa, Shawnee, and Leawood make up Johnson County. It is the wealthiest and fastest-growing part of the state. Kansas City, Kansas, sits along the river with the speedway and the rail yards.</p>',
   '<p>%s, %s, Lenexa, Shawnee, and Leawood make up Johnson County. It is the wealthiest and fastest-growing part of the state. Overland Park and Olathe have their own pages. Kansas City, Kansas, sits along the river with the speedway and the rail yards.</p>' % (OP,OL)),
  ('<p>Interstate 70 runs from Kansas City through Lawrence, Topeka, Salina, and Hays to the Colorado line. West of Salina, it is the only fast road for two hundred miles.</p>',
   '<p>Interstate 70 runs from Kansas City through Lawrence, %s, Salina, and Hays to the Colorado line. West of Salina, it is the only fast road for two hundred miles. The Topeka page covers the Capitol, the session, and the end of the Turnpike.</p>' % TO),
 ],
 [('<p>Yes, Johnson County is the busiest part of the state for us. The metro shares one carrier pool across the state line, and pricing follows Kansas City lanes. Send the full address and any gate code, since new subdivisions outpace carrier maps.</p>',
   '<p>Yes, Johnson County is the busiest part of the state for us, and %s and %s have their own pages. The metro shares one carrier pool across the state line, and pricing follows Kansas City lanes. Send the full address and any gate code, since new subdivisions outpace carrier maps.</p>' % (OP,OL)),
  ('Carriers pay the Kansas Turnpike between Kansas City, Topeka, Emporia, and Wichita and price accordingly.',
   'Carriers pay the Kansas Turnpike between Kansas City, %s, Emporia, and Wichita and price accordingly.' % TO),
 ])

OW='<a href="/city/auto-transport-owensboro-kentucky/">Owensboro</a>'
do('kentucky-auto-transport.html','KY',
 'Louisville, Lexington, and Owensboro have their own pages with the freight hub, the horse farms, the river bridges, and neighborhood meeting spots. Bowling Green, Paducah, Ashland, and the rest of Kentucky are covered from this page.',
 [('<p class="ph-quick-note">Louisville and Lexington have their own pages. This page carries Bowling Green, Fort Campbell, Paducah, Owensboro, Ashland, and the rest of the state.</p>',
   '<p class="ph-quick-note">Louisville, Lexington, and Owensboro have their own pages. This page carries Bowling Green, Fort Campbell, Paducah, Ashland, and the rest of the state.</p>'),
  ('Owensboro and Henderson ship across the river to Evansville and through Interstate 69.</p>',
   '%s and Henderson ship across the river to Evansville and through Interstate 69. The Owensboro page covers the bypass, the two bridges, and the barbecue weekend.</p>' % OW),
 ],
 [('Yes, Paducah sits on Interstate 24 between St. Louis and Nashville. Owensboro and Henderson ship across the river to Evansville.',
   'Yes, Paducah sits on Interstate 24 between St. Louis and Nashville. %s has its own page, and it and Henderson ship across the river to Evansville.' % OW),
 ])
