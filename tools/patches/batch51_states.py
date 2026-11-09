"""Batch 51 state-page integration (Nov 9, 2026): PA, NC, TN, WV, WA block regens (no new blocks); chips; quick notes;
FAQ links; neighbor links. Name collisions handled by reading each first mention: "Lancaster Pike" is the Reading office
street (so Reading gets a targeted phrase link, not link_first), "Spokane" would match inside "Spokane Valley" on the new
page (targeted phrase there too), and "Kent" is linked only where it is plainly Kent, WA."""
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
LA=L('auto-transport-lancaster-pennsylvania','Lancaster'); HB=L('auto-transport-harrisburg-pennsylvania','Harrisburg')
CY=L('auto-transport-cary-north-carolina','Cary'); CH=L('auto-transport-chattanooga-tennessee','Chattanooga')
MO=L('auto-transport-morgantown-west-virginia','Morgantown'); KE=L('auto-transport-kent-washington','Kent'); SV=L('auto-transport-spokane-valley-washington','Spokane Valley')

# ---------------- Pennsylvania (regen, 8) ----------------
p=S+'pennsylvania-auto-transport.html'; h=open(p,encoding='utf-8').read()
PI=L('auto-transport-pittsburgh-pennsylvania','Pittsburgh'); AL=L('auto-transport-allentown-pennsylvania','Allentown'); BE=L('auto-transport-bethlehem-pennsylvania','Bethlehem'); RE=L('auto-transport-reading-pennsylvania','Reading'); ER=L('auto-transport-erie-pennsylvania','Erie')
h=regen(h,'PA','Philadelphia, Pittsburgh, Harrisburg, Lancaster, Allentown, Bethlehem, Reading, and Erie have their own pages with local lanes, meeting spots, and phone lines. Scranton, State College, York, and the rest of Pennsylvania are covered from this page.')
h=rep(h,'<p class="ph-quick-note">Philadelphia, %s, %s, %s, %s, and %s have their own pages. This page carries Harrisburg, Scranton, State College, and the rest of the state.</p>'%(PI,AL,BE,RE,ER),
        '<p class="ph-quick-note">Philadelphia, %s, %s, %s, %s, %s, %s, and %s have their own pages. This page carries Scranton, State College, York, and the rest of the state.</p>'%(PI,HB,LA,AL,BE,RE,ER))
h=rep(h,'This page covers the Turnpike and Interstate 80, Harrisburg and the warehouse hub, and the four city pages. It also covers the Lehigh Valley, Penn State, the Poconos and Erie, the posts, and the city page.',
        'This page covers the Turnpike and Interstate 80, Harrisburg and the warehouse hub, and the eight city pages. It also covers the Lehigh Valley, Penn State, the Poconos and Erie, and the posts.')
h=rep(h,'<p>Harrisburg is the capital. Carlisle and Mechanicsburg next door hold','<p>%s is the capital, and it has its own page now. Carlisle and Mechanicsburg next door hold'%HB)
h=rep(h,'Lancaster and York add the Amish country and the manufacturing plants.','%s adds the Amish country and has its own page now. York adds the manufacturing plants.'%LA)
h=chip(h,'Harrisburg','auto-transport-harrisburg-pennsylvania'); h=chip(h,'Lancaster','auto-transport-lancaster-pennsylvania')
h=faq_edit(h,'Carriers slot a private pickup into that flow easily, and Baltimore, Philadelphia, and Washington are all same-day lanes.','Carriers slot a private pickup into that flow easily, and Baltimore, Philadelphia, and Washington are all same-day lanes. The %s page names the lots and the show weeks.'%HB)
open(p,'w',encoding='utf-8').write(h); resync(p); print('pennsylvania updated')

# ---------------- North Carolina (regen, 7) ----------------
p=S+'north-carolina-auto-transport.html'; h=open(p,encoding='utf-8').read()
CL=L('auto-transport-charlotte-north-carolina','Charlotte'); DU=L('auto-transport-durham-north-carolina','Durham'); RA=L('auto-transport-raleigh-north-carolina','Raleigh'); GR=L('auto-transport-greensboro-north-carolina','Greensboro'); WS=L('auto-transport-winston-salem-north-carolina','Winston-Salem'); FA=L('auto-transport-fayetteville-north-carolina','Fayetteville')
h=regen(h,'NC','Charlotte, Durham, Raleigh, Cary, Greensboro, Winston-Salem, and Fayetteville have their own pages with local lanes, meeting spots, and phone lines. Jacksonville, Wilmington, Asheville, the coast, and the rest of North Carolina are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s, %s, %s, %s, %s, and %s have their own pages.'%(CL,DU,RA,GR,WS,FA),'<p class="ph-quick-note">%s, %s, %s, %s, %s, %s, and %s have their own pages.'%(CL,DU,RA,CY,GR,WS,FA))
h=rep(h,'<p>Interstate 85 runs the Piedmont from Charlotte through Greensboro and Durham to Virginia. Interstate 40 crosses the whole state from the Tennessee line at Asheville to the port at Wilmington.</p>',
        '<p>Interstate 85 runs the Piedmont from Charlotte through Greensboro and Durham to Virginia. Interstate 40 crosses the whole state from the Tennessee line at Asheville to the port at Wilmington. %s sits on it between the Park and Raleigh, and it has its own page now.</p>'%CY)
h=faq_edit(h,'The Triangle campuses are covered on the %s and %s pages.'%(DU,RA),'The Triangle campuses are covered on the %s and %s pages. The %s page covers the planned communities west of them.'%(DU,RA,CY))
open(p,'w',encoding='utf-8').write(h); resync(p); print('north carolina updated')

# ---------------- Tennessee (regen, 3) ----------------
p=S+'tennessee-auto-transport.html'; h=open(p,encoding='utf-8').read()
ME=L('auto-transport-memphis-tennessee','Memphis'); KX=L('auto-transport-knoxville-tennessee','Knoxville')
h=regen(h,'TN','Memphis, Knoxville, and Chattanooga have their own pages with local lanes, meeting spots, and phone lines. Nashville, Clarksville, Johnson City, and every other Tennessee town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s and %s have their own pages. This page carries the detail for Nashville, Chattanooga, Clarksville, and the rest.</p>'%(ME,KX),
        '<p class="ph-quick-note">%s, %s, and %s have their own pages. This page carries the detail for Nashville, Clarksville, and the rest.</p>'%(ME,KX,CH))
h=rep(h,'<p>Chattanooga builds cars at the German plant on the east side and relocates engineers on program dates. The city sits between ridges,','<p>%s builds cars at the German plant on the east side and relocates engineers on program dates. It has its own page now. The city sits between ridges,'%CH)
h=chip(h,'Chattanooga','auto-transport-chattanooga-tennessee')
h=faq_edit(h,'Nobody moves a loaded trailer on Tennessee ice. We tell you the moment the forecast changes the plan, and we reschedule once the roads clear.','Nobody moves a loaded trailer on Tennessee ice. We tell you the moment the forecast changes the plan, and we reschedule once the roads clear. The %s page covers the fog and ice on Monteagle.'%CH)
open(p,'w',encoding='utf-8').write(h); resync(p); print('tennessee updated')

# ---------------- West Virginia (regen, 3) ----------------
p=S+'west-virginia-auto-transport.html'; h=open(p,encoding='utf-8').read()
CW=L('auto-transport-charleston-west-virginia','Charleston'); HU=L('auto-transport-huntington-west-virginia','Huntington')
h=regen(h,'WV','Charleston, Huntington, and Morgantown have their own pages with local lanes, meeting spots, and phone lines. Martinsburg, Beckley, Wheeling, Parkersburg, and every other West Virginia town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s and %s have their own pages. This page carries the detail for Morgantown, Martinsburg, Beckley, Wheeling, and the rest.</p>'%(CW,HU),
        '<p class="ph-quick-note">%s, %s, and %s have their own pages. This page carries the detail for Martinsburg, Beckley, Wheeling, and the rest.</p>'%(CW,HU,MO))
h=rep(h,'<p class="ph-lead">Morgantown is the fastest-growing city in the state, and one campus fills it every August.</p>','<p class="ph-lead">%s is the fastest-growing city in the state, and it has its own page now. One campus fills it every August.</p>'%MO)
h=chip(h,'Morgantown','auto-transport-morgantown-west-virginia')
h=faq_edit(h,'It usually costs one hundred fifty to two hundred forty dollars for a sedan. Martinsburg to Washington works the same way on Interstate 81 and 66.','It usually costs one hundred fifty to two hundred forty dollars for a sedan. The %s page covers that lane and the campus lots. Martinsburg to Washington works the same way on Interstate 81 and 66.'%MO)
open(p,'w',encoding='utf-8').write(h); resync(p); print('west virginia updated')

# ---------------- Washington (regen, 6) ----------------
p=S+'washington-auto-transport.html'; h=open(p,encoding='utf-8').read()
SE=L('auto-transport-seattle-washington','Seattle'); SP=L('auto-transport-spokane-washington','Spokane'); VA=L('auto-transport-vancouver-washington','Vancouver'); BV=L('auto-transport-bellevue-washington','Bellevue')
h=regen(h,'WA','Seattle, Bellevue, Kent, Spokane, Spokane Valley, and Vancouver have their own pages with local lanes, meeting spots, and phone lines. Tacoma, Everett, Olympia, the Tri-Cities, and every other Washington town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s, %s, %s, and %s have their own pages. This page carries the detail for Tacoma, Everett, Olympia, the Tri-Cities, and the rest.</p>'%(SE,SP,VA,BV),
        '<p class="ph-quick-note">%s, %s, %s, %s, %s, and %s have their own pages. This page carries the detail for Tacoma, Everett, Olympia, the Tri-Cities, and the rest.</p>'%(SE,BV,KE,SP,SV,VA))
h=rep(h,'<p>Bothell, Issaquah, Sammamish, and the newer suburbs allow curbside on most streets. Many have gates, so send the community name.','<p>Bothell, Issaquah, Sammamish, and the newer suburbs allow curbside on most streets. Many have gates, so send the community name. %s, where the Sound carriers stage, has its own page now.'%KE)
h=rep(h,'It has its own page now. The hospitals, the universities, and Fairchild relocate people year round, and pickups schedule in 1 to 3 days.</p>','It has its own page now, and so does %s next door. The hospitals, the universities, and Fairchild relocate people year round, and pickups schedule in 1 to 3 days.</p>'%SV)
h=chip(h,'Kent','auto-transport-kent-washington'); h=chip(h,'Spokane Valley','auto-transport-spokane-valley-washington')
h=faq_edit(h,'Pickups schedule in 1 to 3 days, and Boise and the Mountain West are the natural lanes. The Tri-Cities, Yakima, and Walla Walla run 2 to 4 days.','Pickups schedule in 1 to 3 days, and Boise and the Mountain West are the natural lanes. The %s page covers the Valley and the Idaho line. The Tri-Cities, Yakima, and Walla Walla run 2 to 4 days.'%SV)
open(p,'w',encoding='utf-8').write(h); resync(p); print('washington updated')

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
def link_phrase(path, old, new):
    p=S+path; h=open(p,encoding='utf-8').read()
    a=h.index('<section class="ph-stats">'); b=h.index('<div class="ph-faq-list">')
    body=h[a:b]; assert body.count(old)==1, (path, old[:60])
    h=h[:a]+body.replace(old,new)+h[b:]; open(p,'w',encoding='utf-8').write(h); print(path.split('/')[1], '-> phrase linked')
# Harrisburg
for pg in ['allentown-pennsylvania','bethlehem-pennsylvania','pittsburgh-pennsylvania','lancaster-pennsylvania']:
    link_first('city/auto-transport-%s/index.html'%pg,'Harrisburg','auto-transport-harrisburg-pennsylvania')
# Lancaster: Reading's first mention is its own office street ("Lancaster Pike"), so the 222 sentence is linked instead
link_phrase('city/auto-transport-reading-pennsylvania/index.html','US 222 runs north to Allentown and south to Lancaster.','US 222 runs north to Allentown and south to %s.'%LA)
# Cary
link_first('city/auto-transport-raleigh-north-carolina/index.html','Cary','auto-transport-cary-north-carolina')
link_first('city/auto-transport-cary-north-carolina/index.html','Raleigh','auto-transport-raleigh-north-carolina')
# Chattanooga
for pg in ['knoxville-tennessee','huntsville-alabama']:
    link_first('city/auto-transport-%s/index.html'%pg,'Chattanooga','auto-transport-chattanooga-tennessee')
link_first('city/auto-transport-chattanooga-tennessee/index.html','Knoxville','auto-transport-knoxville-tennessee')
# Morgantown
for pg in ['pittsburgh-pennsylvania','charleston-west-virginia']:
    link_first('city/auto-transport-%s/index.html'%pg,'Morgantown','auto-transport-morgantown-west-virginia')
link_first('city/auto-transport-morgantown-west-virginia/index.html','Pittsburgh','auto-transport-pittsburgh-pennsylvania')
# Kent (Seattle's "The carriers stage in Kent, Auburn, and Fife" is plainly Kent, WA)
link_first('city/auto-transport-seattle-washington/index.html','Kent','auto-transport-kent-washington')
link_first('city/auto-transport-kent-washington/index.html','Seattle','auto-transport-seattle-washington')
# Spokane Valley (the Spokane page says "the Valley" in prose; the full name replaces it once, and the new page links Spokane by phrase)
link_phrase('city/auto-transport-spokane-washington/index.html','from Airway Heights to the Valley and Coeur d’Alene.','from Airway Heights to %s and Coeur d’Alene.'%SV)
link_phrase('city/auto-transport-spokane-valley-washington/index.html','Interstate 90 enters from Spokane at the Havana line','Interstate 90 enters from %s at the Havana line'%L('auto-transport-spokane-washington','Spokane'))
print('done')
