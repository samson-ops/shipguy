"""Batch 49 state-page integration: OR, MN, SD, SC, WV block regens; first City Pages blocks for TN and VT; chips; quick
notes; FAQ links; neighbor links. Name collisions: three Columbias (MD, MO, SC), Salem inside Winston-Salem, Burlington NC/MA,
Huntington NY/Beach — so no neighbor page is ever linked on the bare words Salem, Columbia, Burlington, or Huntington.
Memphis, Minneapolis, and Rapid City are unique, and every first mention read on the neighbor pages is the right city."""
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
def first_block(h, st, intro, eyebrow):
    assert not BLOCK.search(h)
    anchor='<section class="ph-sec"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">%s</p>' % eyebrow
    assert h.count(anchor)==1, anchor
    h=h.replace(anchor, lp.state_cities_block(st, intro)+'\n'+anchor)
    assert BLOCK.search(h); return h
SA=L('auto-transport-salem-oregon','Salem'); ME=L('auto-transport-memphis-tennessee','Memphis'); MP=L('auto-transport-minneapolis-minnesota','Minneapolis')
RC=L('auto-transport-rapid-city-south-dakota','Rapid City'); CO=L('auto-transport-columbia-south-carolina','Columbia')
BU=L('auto-transport-burlington-vermont','Burlington'); HU=L('auto-transport-huntington-west-virginia','Huntington')

# ---------------- Oregon (regen, 3) ----------------
p=S+'oregon-auto-transport.html'; h=open(p,encoding='utf-8').read()
EU=L('auto-transport-eugene-oregon','Eugene')
h=regen(h,'OR','Portland, Eugene, and Salem have their own pages with local lanes, meeting spots, and phone lines. Bend, Medford, the coast, and every other Oregon town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">Portland has its own page covering the bridges, the West Hills, and the neighborhood meeting spots. %s has one too. This page carries Salem, Bend, Medford, the coast, and the rest of the state.</p>'%EU,
        '<p class="ph-quick-note">Portland has its own page covering the bridges, the West Hills, and the neighborhood meeting spots. %s and %s have them too. This page carries Bend, Medford, the coast, and the rest of the state.</p>'%(EU,SA))
h=rep(h,'Salem is the capital, with state government relocating people on its own calendar. ','%s is the capital, with state government relocating people on its own calendar. It has its own page now. '%SA)
h=chip(h,'Salem','auto-transport-salem-oregon')
h=faq_edit(h,'%s page names the lots.'%EU,'%s page names the lots, and the %s page covers Willamette and Chemeketa.'%(EU,SA))
open(p,'w',encoding='utf-8').write(h); resync(p); print('oregon updated')

# ---------------- Tennessee (first block, 1) ----------------
p=S+'tennessee-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=first_block(h,'TN','Memphis has its own page with local lanes, meeting spots, and a phone line. Nashville, Knoxville, Chattanooga, Clarksville, and every other Tennessee town are covered from this page.','Nashville')
h=rep(h,'<p class="ph-quick-note">Tennessee has no city page yet. This page carries the detail for Nashville, Memphis, Knoxville, Chattanooga, Clarksville, and the rest.</p>',
        '<p class="ph-quick-note">%s has its own page. This page carries the detail for Nashville, Knoxville, Chattanooga, Clarksville, and the rest.</p>'%ME)
h=rep(h,'<p class="ph-lead">Memphis moves more air cargo than any city in the world. The trucking that goes with it keeps carriers close.</p>',
        '<p class="ph-lead">%s moves more air cargo than almost any city in the world. The trucking that goes with it keeps carriers close, and the city has its own page now.</p>'%ME)
h=chip(h,'Memphis','auto-transport-memphis-tennessee')
h=faq_edit(h,'Yes, Memphis is one of our busiest lanes in the state.','Yes, Memphis is one of our busiest lanes in the state. The %s page covers the bridges, the hub, and the meeting lots.'%ME)
open(p,'w',encoding='utf-8').write(h); resync(p); print('tennessee updated (first City Pages block)')

# ---------------- Minnesota (regen, 5) ----------------
p=S+'minnesota-auto-transport.html'; h=open(p,encoding='utf-8').read()
SP=L('auto-transport-st-paul-minnesota','St. Paul'); BL=L('auto-transport-bloomington-minnesota','Bloomington'); RO=L('auto-transport-rochester-minnesota','Rochester'); DU=L('auto-transport-duluth-minnesota','Duluth')
h=regen(h,'MN','Minneapolis, St. Paul, Bloomington, Rochester, and Duluth have their own pages with local lanes, meeting spots, and phone lines. St. Cloud, Mankato, and every other Minnesota town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s, %s, %s, and %s have their own pages. This page carries the detail for Minneapolis, St. Cloud, and the rest.</p>'%(SP,BL,RO,DU),
        '<p class="ph-quick-note">%s, %s, %s, %s, and %s have their own pages. This page carries the detail for St. Cloud, Mankato, and the rest.</p>'%(MP,SP,BL,RO,DU))
h=rep(h,'Minneapolis’s older neighborhoods have narrow streets and winter parking rules.','%s’s older neighborhoods have narrow streets and winter parking rules, and the city has its own page now.'%MP)
h=chip(h,'Minneapolis','auto-transport-minneapolis-minnesota')
h=faq_edit(h,'The %s page covers the east metro.'%SP,'The %s page covers the west metro, and the %s page covers the east.'%(MP,SP))
open(p,'w',encoding='utf-8').write(h); resync(p); print('minnesota updated')

# ---------------- South Dakota (regen, 2) ----------------
p=S+'south-dakota-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=regen(h,'SD','Sioux Falls and Rapid City have their own pages with local lanes, meeting spots, and phone lines. Pierre, Aberdeen, Brookings, and every other South Dakota town are covered from this page.')
h=rep(h,'<p>Sioux Falls and Rapid City schedule in 2 to 5 days.','<p>Sioux Falls and %s schedule in 2 to 5 days, and both have their own pages.'%RC)
h=chip(h,'Rapid City','auto-transport-rapid-city-south-dakota')
h=faq_edit(h,'Housing is gated, so the driver meets you outside the fence.','Housing is gated, so the driver meets you outside the fence. The %s page covers the Box Elder lots and the base gate.'%RC)
open(p,'w',encoding='utf-8').write(h); resync(p); print('south dakota updated')

# ---------------- South Carolina (regen, 2) ----------------
p=S+'south-carolina-auto-transport.html'; h=open(p,encoding='utf-8').read()
CH=L('auto-transport-charleston-south-carolina','Charleston')
h=regen(h,'SC','Charleston and Columbia have their own pages with local lanes, meeting spots, and phone lines. Greenville, Myrtle Beach, Hilton Head, and every other South Carolina town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s has its own page. This page carries the detail for Columbia, Greenville, Myrtle Beach, Hilton Head, and the rest.</p>'%CH,
        '<p class="ph-quick-note">%s and %s have their own pages. This page carries the detail for Greenville, Myrtle Beach, Hilton Head, and the rest.</p>'%(CH,CO))
h=rep(h,'<p class="ph-lead">Columbia sits in the middle of the state where three interstates meet, and two calendars drive it.</p>',
        '<p class="ph-lead">%s sits in the middle of the state where three interstates meet, and two calendars drive it. It has its own page now.</p>'%CO)
h=chip(h,'Columbia','auto-transport-columbia-south-carolina')
h=faq_edit(h,'Housing is gated, so the driver meets you outside the installation.','Housing is gated, so the driver meets you outside the installation. The %s page covers the Fort Jackson gates and graduation Thursdays.'%CO)
open(p,'w',encoding='utf-8').write(h); resync(p); print('south carolina updated')

# ---------------- Vermont (first block, 1) ----------------
p=S+'vermont-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=first_block(h,'VT','Burlington has its own page with local lanes, meeting spots, and a phone line. Montpelier, Rutland, the ski towns, the Kingdom, and every other Vermont town are covered from this page.','Burlington')
h=rep(h,'<p class="ph-quick-note">Vermont is a small market, and carriers come up from Boston, Albany, and New York. A flexible date range matters more in Vermont than almost anywhere else in the Northeast.</p>',
        '<p class="ph-quick-note">Vermont is a small market, and carriers come up from Boston, Albany, and New York. A flexible date range matters more in Vermont than almost anywhere else in the Northeast. %s has its own page.</p>'%BU)
h=rep(h,'<p class="ph-lead">Burlington is the largest city in the state, and it ships on the medical and campus calendars.</p>',
        '<p class="ph-lead">%s is the largest city in the state, and it ships on the medical and campus calendars. It has its own page now.</p>'%BU)
h=chip(h,'Burlington','auto-transport-burlington-vermont')
h=faq_edit(h,'Miami runs a little more.','Miami runs a little more, and the %s page has the full lane table.'%BU)
open(p,'w',encoding='utf-8').write(h); resync(p); print('vermont updated (first City Pages block)')

# ---------------- West Virginia (regen, 2) ----------------
p=S+'west-virginia-auto-transport.html'; h=open(p,encoding='utf-8').read()
CW=L('auto-transport-charleston-west-virginia','Charleston')
h=regen(h,'WV','Charleston and Huntington have their own pages with local lanes, meeting spots, and phone lines. Morgantown, Martinsburg, Beckley, Wheeling, and every other West Virginia town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s has its own page. This page carries the detail for Huntington, Morgantown, Martinsburg, Beckley, Wheeling, and the rest.</p>'%CW,
        '<p class="ph-quick-note">%s and %s have their own pages. This page carries the detail for Morgantown, Martinsburg, Beckley, Wheeling, and the rest.</p>'%(CW,HU))
h=rep(h,'<p>Huntington sits on the Ohio River with the university and the hospitals, and residents arrive every June. Its streets are a grid where the truck usually reaches the curb.',
        '<p>%s sits on the Ohio River with the university and the hospitals, and residents arrive every June. Its streets are a grid where the truck usually reaches the curb. The city has its own page now.'%HU)
h=chip(h,'Huntington','auto-transport-huntington-west-virginia')
h=faq_edit(h,'Huntington allows curbside on most streets.','Huntington allows curbside on most streets, and the %s page names the campus lots.'%HU)
open(p,'w',encoding='utf-8').write(h); resync(p); print('west virginia updated')

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
# Memphis: the nearby pages that mention it (all read as the Tennessee city)
for pg in ['little-rock-arkansas','jackson-mississippi','tuscaloosa-alabama','huntsville-alabama','st-louis-missouri','shreveport-louisiana']:
    link_first('city/auto-transport-%s/index.html'%pg,'Memphis','auto-transport-memphis-tennessee')
# Minneapolis: the nearby pages that mention it, plus the new Rapid City page
for pg in ['st-paul-minnesota','bloomington-minnesota','fargo-north-dakota','madison-wisconsin','sioux-falls-south-dakota','ankeny-iowa','rapid-city-south-dakota']:
    link_first('city/auto-transport-%s/index.html'%pg,'Minneapolis','auto-transport-minneapolis-minnesota')
# Rapid City: the two nearby pages that mention it
for pg in ['sioux-falls-south-dakota','billings-montana']:
    link_first('city/auto-transport-%s/index.html'%pg,'Rapid City','auto-transport-rapid-city-south-dakota')

# ---------------- pass 2: two long sentences (one pre-existing in the SD FAQ, one created by the MN link) ----------------
p=S+'minnesota-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'%s’s older neighborhoods have narrow streets and winter parking rules, and the city has its own page now.'%MP,
        '%s’s older neighborhoods have narrow streets and winter parking rules. The city has its own page now.'%MP)
open(p,'w',encoding='utf-8').write(h); print('minnesota pass 2')
p=S+'south-dakota-auto-transport.html'; h=open(p,encoding='utf-8').read()
SF=L('auto-transport-sioux-falls-south-dakota','Sioux Falls')
h=faq_edit(h,'Sioux Falls and Rapid City schedule in 2 to 5 days, and the %s page names the meeting lots.'%SF,
             'Sioux Falls and Rapid City schedule in 2 to 5 days. The %s page names the meeting lots, and the %s page covers the Hills.'%(SF,RC))
open(p,'w',encoding='utf-8').write(h); resync(p); print('south dakota pass 2')
