"""Batch 50 state-page integration: WY, RI, MT, NV, NM, TN block regens (no new blocks); chips; quick notes; FAQ links;
neighbor links. All six names are unique in prose, and every first mention on a neighbor page was read before linking."""
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
CA=L('auto-transport-casper-wyoming','Casper'); PA=L('auto-transport-pawtucket-rhode-island','Pawtucket'); BZ=L('auto-transport-bozeman-montana','Bozeman')
CC=L('auto-transport-carson-city-nevada','Carson City'); RR=L('auto-transport-rio-rancho-new-mexico','Rio Rancho'); KX=L('auto-transport-knoxville-tennessee','Knoxville')

# ---------------- Wyoming (regen, 2) ----------------
p=S+'wyoming-auto-transport.html'; h=open(p,encoding='utf-8').read()
CH=L('auto-transport-cheyenne-wyoming','Cheyenne')
h=regen(h,'WY','Cheyenne and Casper have their own pages with local lanes, meeting spots, and phone lines. Laramie, Gillette, Rock Springs, Jackson, and every other Wyoming town are covered from this page.')
h=rep(h,'A wide date range is the most helpful thing you can offer.</p>','A wide date range is the most helpful thing you can offer. %s and %s have their own pages.</p>'%(CH,CA))
h=rep(h,'<p>Casper sits in the middle of the state on Interstate 25. It ships on the oil fields and the hospitals.','<p>%s sits in the middle of the state on Interstate 25, and it has its own page now. It ships on the oil fields and the hospitals.'%CA)
h=chip(h,'Casper','auto-transport-casper-wyoming')
h=faq_edit(h,'Cheyenne and the corridor towns schedule in 3 to 6 days. Jackson, Cody, and the ranch country take 5 to 10.','Cheyenne and the corridor towns schedule in 3 to 6 days. The %s page covers the 25 side. Jackson, Cody, and the ranch country take 5 to 10.'%CA)
open(p,'w',encoding='utf-8').write(h); resync(p); print('wyoming updated')

# ---------------- Rhode Island (regen, 3) ----------------
p=S+'rhode-island-auto-transport.html'; h=open(p,encoding='utf-8').read()
CR=L('auto-transport-cranston-rhode-island','Cranston'); WA=L('auto-transport-warwick-rhode-island','Warwick')
h=regen(h,'RI','Cranston, Warwick, and Pawtucket have their own pages with local lanes, meeting spots, and phone lines. Providence, Newport, Westerly, and every other Rhode Island town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s and %s have their own pages. This page carries the detail for Providence, Newport, Westerly, and the rest.</p>'%(CR,WA),
        '<p class="ph-quick-note">%s, %s, and %s have their own pages. This page carries the detail for Providence, Newport, Westerly, and the rest.</p>'%(CR,WA,PA))
h=rep(h,'<p>Woonsocket, Pawtucket, and Central Falls have dense mill-era streets, and the driver meets you on a main road.','<p>Woonsocket, %s, and Central Falls have dense mill-era streets, and the driver meets you on a main road. Pawtucket has its own page now.'%PA)
h=chip(h,'Pawtucket','auto-transport-pawtucket-rhode-island')
h=faq_edit(h,'Nothing in the state is more than an hour from the corridor.','Nothing in the state is more than an hour from the corridor. The %s page covers the Blackstone Valley end of it.'%PA)
open(p,'w',encoding='utf-8').write(h); resync(p); print('rhode island updated')

# ---------------- Montana (regen, 4) ----------------
p=S+'montana-auto-transport.html'; h=open(p,encoding='utf-8').read()
BI=L('auto-transport-billings-montana','Billings'); GF=L('auto-transport-great-falls-montana','Great Falls'); MI=L('auto-transport-missoula-montana','Missoula')
h=regen(h,'MT','Billings, Bozeman, Great Falls, and Missoula have their own pages with local lanes, meeting spots, and phone lines. Helena, Butte, Kalispell, and every other Montana town are covered from this page.')
h=rep(h,'A wide date range is the biggest help you can give us.</p>','A wide date range is the biggest help you can give us. %s, %s, %s, and %s have their own pages.</p>'%(BI,BZ,GF,MI))
h=rep(h,'<p>Bozeman is the fastest-growing city in the state. Transplants','<p>%s is the fastest-growing city in the state, and it has its own page now. Transplants'%BZ)
h=chip(h,'Bozeman','auto-transport-bozeman-montana')
h=faq_edit(h,'The %s page names the lots.'%MI,'The %s page names the lots, and the %s page covers the stadium lots.'%(MI,BZ))
open(p,'w',encoding='utf-8').write(h); resync(p); print('montana updated')

# ---------------- Nevada (regen, 4) ----------------
p=S+'nevada-auto-transport.html'; h=open(p,encoding='utf-8').read()
LV=L('auto-transport-las-vegas-nevada','Las Vegas'); HE=L('auto-transport-henderson-nevada','Henderson'); SK=L('auto-transport-sparks-nevada','Sparks')
h=regen(h,'NV','Las Vegas, Henderson, Sparks, and Carson City have their own pages with local lanes, meeting spots, and phone lines. Reno, Lake Tahoe, Elko, and the rest of Nevada are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s, %s, and %s have their own pages. This page carries Reno, Carson City, Lake Tahoe, and the rest of the state.</p>'%(LV,HE,SK),
        '<p class="ph-quick-note">%s, %s, %s, and %s have their own pages. This page carries Reno, Lake Tahoe, and the rest of the state.</p>'%(LV,HE,SK,CC))
h=rep(h,'Households leaving California for Reno, Sparks, and Carson City keep the Sacramento and Bay Area lanes full.','Households leaving California for Reno, Sparks, and %s keep the Sacramento and Bay Area lanes full. The capital has its own page now.'%CC)
h=chip(h,'Carson City','auto-transport-carson-city-nevada')
h=faq_edit(h,'Lake deliveries run 2 to 4 days, and second-home owners ship up in November and June.','Lake deliveries run 2 to 4 days, and second-home owners ship up in November and June. The %s page covers Spooner Summit and the Nevada shore.'%CC)
open(p,'w',encoding='utf-8').write(h); resync(p); print('nevada updated')

# ---------------- New Mexico (regen, 4) ----------------
p=S+'new-mexico-auto-transport.html'; h=open(p,encoding='utf-8').read()
LC=L('auto-transport-las-cruces-new-mexico','Las Cruces'); SF=L('auto-transport-santa-fe-new-mexico','Santa Fe'); AB=L('auto-transport-albuquerque-new-mexico','Albuquerque')
h=regen(h,'NM','Albuquerque, Rio Rancho, Santa Fe, and Las Cruces have their own pages with local lanes, meeting spots, and phone lines. Taos, Farmington, Roswell, and every other New Mexico town are covered from this page.')
h=rep(h,'%s and %s have them too. This page carries Taos'%(LC,SF),'%s, %s, and %s have them too. This page carries Taos'%(LC,SF,RR))
h=rep(h,'The Balloon Fiesta in Albuquerque each October is covered on the city page.</p>','The Balloon Fiesta in Albuquerque each October is covered on the city page. The west mesa is covered on the %s page.</p>'%RR)
h=chip(h,'Rio Rancho','auto-transport-rio-rancho-new-mexico')
h=faq_edit(h,'Kirtland is covered on the %s page.'%AB,'Kirtland is covered on the %s page. The %s page covers the chip plant and the families across the river.'%(AB,RR))
open(p,'w',encoding='utf-8').write(h); resync(p); print('new mexico updated')

# ---------------- Tennessee (regen, 2) ----------------
p=S+'tennessee-auto-transport.html'; h=open(p,encoding='utf-8').read()
ME=L('auto-transport-memphis-tennessee','Memphis')
h=regen(h,'TN','Memphis and Knoxville have their own pages with local lanes, meeting spots, and phone lines. Nashville, Chattanooga, Clarksville, and every other Tennessee town are covered from this page.')
h=rep(h,'<p class="ph-quick-note">%s has its own page. This page carries the detail for Nashville, Knoxville, Chattanooga, Clarksville, and the rest.</p>'%ME,
        '<p class="ph-quick-note">%s and %s have their own pages. This page carries the detail for Nashville, Chattanooga, Clarksville, and the rest.</p>'%(ME,KX))
h=rep(h,'Home football Saturdays close the streets around the Knoxville stadium. The national laboratory','Home football Saturdays close the streets around the %s stadium, and the city has its own page now. The national laboratory'%KX)
h=chip(h,'Knoxville','auto-transport-knoxville-tennessee')
h=faq_edit(h,'Home football Saturdays close the streets around the Knoxville stadium, so we schedule around the games.','Home football Saturdays close the streets around the Knoxville stadium, so we schedule around the games. The %s page names the game-day lots.'%KX)
open(p,'w',encoding='utf-8').write(h); resync(p); print('tennessee updated')

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
link_first('city/auto-transport-cheyenne-wyoming/index.html','Casper','auto-transport-casper-wyoming')
link_first('city/auto-transport-billings-montana/index.html','Bozeman','auto-transport-bozeman-montana')
link_first('city/auto-transport-sparks-nevada/index.html','Carson City','auto-transport-carson-city-nevada')
link_first('city/auto-transport-albuquerque-new-mexico/index.html','Rio Rancho','auto-transport-rio-rancho-new-mexico')
for pg in ['cincinnati-ohio','huntsville-alabama','lexington-kentucky']:
    link_first('city/auto-transport-%s/index.html'%pg,'Knoxville','auto-transport-knoxville-tennessee')
# Pawtucket has no plain prose mention on any neighbor page; its inbound links are the nearby chips, the state page and the hub.

# ---------------- pass 2: the New Mexico intro counted three city pages (and ran 19 words) ----------------
p=S+'new-mexico-auto-transport.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'It also covers the oil patch, the bases, the mountain towns, and the three cities with their own pages.','It also covers the oil patch, the bases, the mountain towns, and the four city pages.')
open(p,'w',encoding='utf-8').write(h); print('new mexico pass 2')
