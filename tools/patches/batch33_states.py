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
    h=head+body
    open(p,'w',encoding='utf-8').write(h); print('updated',fn)

FW='<a href="/city/auto-transport-fort-wayne-indiana/">Fort Wayne</a>'
EV='<a href="/city/auto-transport-evansville-indiana/">Evansville</a>'
do('indiana-auto-transport.html','IN',
 'Indianapolis, Fort Wayne, and Evansville have their own pages with the loop, the 469 bypass, the Lloyd Expressway, and neighborhood meeting spots. South Bend, the campuses, and the rest of Indiana are covered from this page.',
 [('<p class="ph-quick-note">Indianapolis has its own page covering the race month, the Carmel roundabouts, and the loop. This page carries Fort Wayne, Evansville, the campuses, and the rest of the state.</p>',
   '<p class="ph-quick-note">Indianapolis, Fort Wayne, and Evansville have their own pages covering the loop, the 469 bypass, and the Lloyd Expressway. This page carries South Bend, the campuses, and the rest of the state.</p>'),
  ('<p>Fort Wayne is the second-largest city and sits on Interstate 69 between Indianapolis and Detroit. Its streets are wide, and the truck generally reaches the curb.</p>',
   '<p>%s is the second-largest city and sits on Interstate 69 between Indianapolis and Detroit. Its streets are wide, and the truck generally reaches the curb. Its page covers the 469 loop, Electric Works, and the festival week.</p>' % FW),
  ('<p>Evansville anchors the southwest on Interstate 64 and 69. The Toyota plant is nearby, and Nashville is a day south.',
   '<p>%s anchors the southwest on Interstate 64 and 69. The Toyota plant is nearby, and Nashville is a day south. Its page covers the Lloyd Expressway, the West Side, and the Fall Festival.' % EV),
 ],
 [('<p>Yes, both are covered from this page. Fort Wayne sits on Interstate 69 with wide streets where the truck reaches the curb. Evansville anchors the southwest on Interstate 64 and 69, with Nashville a day south. Pickups in both run 1 to 3 days.</p>',
   '<p>Yes, and both have their own pages. %s sits on Interstate 69 and the 469 loop, with wide streets where the truck reaches the curb. %s anchors the southwest on Interstate 64 and 69, with Nashville a day south. Pickups in both run 1 to 3 days.</p>' % (FW,EV)),
 ])

AU='<a href="/city/auto-transport-aurora-illinois/">Aurora</a>'
JO='<a href="/city/auto-transport-joliet-illinois/">Joliet</a>'
do('illinois-auto-transport.html','IL',
 'Chicago, Aurora, and Joliet have their own pages with neighborhood meeting spots, the tollways, the lift bridges, and snow-route timing. The other suburbs, downstate, and the rest of Illinois are covered from this page.',
 [('<p class="ph-quick-note">Chicago has its own page covering the viaducts, the Lake Shore Drive truck ban, and the snow routes. This page carries the suburbs, downstate, and the rest of the state.</p>',
   '<p class="ph-quick-note">Chicago, Aurora, and Joliet have their own pages covering the viaducts, the tollways, and the lift bridges. This page carries the other suburbs, downstate, and the rest of the state.</p>'),
  ('<p class="ph-lead">The intermodal yards around Joliet and Elwood move more containers than any inland site in the country.',
   '<p class="ph-lead">The intermodal yards around %s and Elwood move more containers than any inland site in the country.' % JO),
  ('<p>The suburbs from Naperville to Schaumburg are wide grids where the truck reaches the curb.',
   '<p>The suburbs from Naperville to Schaumburg are wide grids where the truck reaches the curb. %s on the Fox River and %s on the Des Plaines have their own pages.' % (AU,JO)),
 ],
 [('The intermodal yards around Joliet keep thousands of trucks based nearby.',
   'The intermodal yards around %s keep thousands of trucks based nearby.' % JO),
 ])

KP='<a href="/city/auto-transport-kapaa-hawaii/">Kapaʻa</a>'
do('hawaii-auto-transport.html','HI',
 'Honolulu, Hilo, Kahului, and Kapaʻa have their own pages with the terminal process, the barge, and island handoffs. Molokai, Lanai, and the Kona side are covered here.',
 [('and Kauai into Nawiliwili. Some sailings from the mainland go direct, and others transfer to the inter-island barge in Honolulu.</p>',
   'and Kauai into Nawiliwili. Kauai has its own page under %s. Some sailings from the mainland go direct, and others transfer to the inter-island barge in Honolulu.</p>' % KP),
 ],
 [('Kawaihae, or Nawiliwili. Others transfer to the inter-island barge in Honolulu.',
   'Kawaihae, or Nawiliwili for %s. Others transfer to the inter-island barge in Honolulu.' % KP),
 ])
