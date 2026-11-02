"""Batch 43 state-page integration: RI + NM block regen; first City Pages blocks on MN, MS, NE, NJ; chips; quick notes; FAQ links; neighbor links."""
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
def first_block(h, st, intro, eyebrow):
    assert not BLOCK.search(h)
    anchor='<section class="ph-sec"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">%s</p>' % eyebrow
    assert h.count(anchor)==1, anchor
    h=h.replace(anchor, lp.state_cities_block(st, intro)+'\n'+anchor)
    assert BLOCK.search(h); return h
WA=L('auto-transport-warwick-rhode-island','Warwick'); SP=L('auto-transport-st-paul-minnesota','St. Paul')
JA=L('auto-transport-jackson-mississippi','Jackson'); OM=L('auto-transport-omaha-nebraska','Omaha')
NE=L('auto-transport-newark-new-jersey','Newark'); LC=L('auto-transport-las-cruces-new-mexico','Las Cruces')

# ---------------- Rhode Island (regen) ----------------
p=S+'rhode-island-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Cranston and Warwick have their own pages with local lanes, meeting spots, and phone lines. '
       'Providence, Pawtucket, Newport, Westerly, and every other Rhode Island town are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('RI', intro), h, count=1)
h=rep(h,'<p class="ph-quick-note"><a href="/city/auto-transport-cranston-rhode-island/">Cranston</a> has its own page. This page carries the detail for Providence, Warwick, Newport, Westerly, and the rest.</p>',
        '<p class="ph-quick-note"><a href="/city/auto-transport-cranston-rhode-island/">Cranston</a> and %s have their own pages. This page carries the detail for Providence, Newport, Westerly, and the rest.</p>' % WA)
h=rep(h,'<p>Warwick and <a href="/city/auto-transport-cranston-rhode-island/">Cranston</a> to the south are wide grids where the truck usually reaches the curb. Cranston has its own page now. The airport in Warwick makes fly-and-ship routine.</p>',
        '<p>%s and <a href="/city/auto-transport-cranston-rhode-island/">Cranston</a> to the south are wide grids where the truck usually reaches the curb. Both have their own pages now. The airport in Warwick makes fly-and-ship routine.</p>' % WA)
h=chip(h,'Warwick','auto-transport-warwick-rhode-island')
open(p,'w',encoding='utf-8').write(h); print('rhode island updated')

# ---------------- Minnesota (first block) ----------------
p=S+'minnesota-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('St. Paul has its own page with local lanes, meeting spots, and a phone line. '
       'Minneapolis, Rochester, Duluth, St. Cloud, and every other Minnesota town are covered from this page.')
h=first_block(h,'MN',intro,'The Twin Cities')
h=rep(h,'<p class="ph-quick-note">Minnesota has no city page yet. This page carries the detail for Minneapolis, St. Paul, Rochester, Duluth, St. Cloud, and the rest.</p>',
        '<p class="ph-quick-note">%s has its own page. This page carries the detail for Minneapolis, Rochester, Duluth, St. Cloud, and the rest.</p>' % SP)
h=rep(h,'<p class="ph-lead">Minneapolis and St. Paul hold more Fortune 500 headquarters per capita than almost any metro in the country.</p>',
        '<p class="ph-lead">Minneapolis and %s hold more Fortune 500 headquarters per capita than almost any metro in the country.</p>' % SP)
h=chip(h,'St. Paul','auto-transport-st-paul-minnesota')
h=faq_edit(h,'Yes, the headquarters in Minneapolis and St. Paul relocate employees from across the country on start dates. We plan the pickup around your first day at work.',
             'Yes, the headquarters in Minneapolis and St. Paul relocate employees from across the country on start dates. The %s page covers the east metro. We plan the pickup around your first day at work.' % SP)
open(p,'w',encoding='utf-8').write(h); resync(p); print('minnesota updated (first block)')

# ---------------- Mississippi (first block) ----------------
p=S+'mississippi-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Jackson has its own page with local lanes, meeting spots, and a phone line. '
       'Gulfport, Biloxi, Hattiesburg, Tupelo, Oxford, and every other Mississippi town are covered from this page.')
h=first_block(h,'MS',intro,'Jackson')
h=rep(h,'<p class="ph-quick-note">Mississippi has no city page yet. This page carries the detail for Jackson, Gulfport, Biloxi, Hattiesburg, Tupelo, Oxford, and the rest.</p>',
        '<p class="ph-quick-note">%s has its own page. This page carries the detail for Gulfport, Biloxi, Hattiesburg, Tupelo, Oxford, and the rest.</p>' % JA)
h=rep(h,'<p class="ph-lead">Jackson ships on the state, medical, and plant calendars.</p>',
        '<p class="ph-lead">%s ships on the state, medical, and plant calendars, and it has its own page now.</p>' % JA)
h=chip(h,'Jackson','auto-transport-jackson-mississippi')
h=faq_edit(h,'Because four interstates cross there and the plant in Canton keeps car carriers based nearby.',
             'Because four interstates cross there and the plant in Canton keeps car carriers based nearby. The %s page has the lanes and the meeting spots.' % JA)
open(p,'w',encoding='utf-8').write(h); resync(p); print('mississippi updated (first block)')

# ---------------- Nebraska (first block) ----------------
p=S+'nebraska-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Omaha has its own page with local lanes, meeting spots, and a phone line. '
       'Lincoln, Grand Island, Kearney, North Platte, and every other Nebraska town are covered from this page.')
h=first_block(h,'NE',intro,'Omaha')
h=rep(h,'<p class="ph-quick-note">Nebraska has no city page yet. This page carries the detail for Omaha, Lincoln, Grand Island, Kearney, and the rest.</p>',
        '<p class="ph-quick-note">%s has its own page. This page carries the detail for Lincoln, Grand Island, Kearney, and the rest.</p>' % OM)
h=rep(h,'<p class="ph-lead">Omaha ships on the corporate calendar and the base calendar.</p>',
        '<p class="ph-lead">%s ships on the corporate calendar and the base calendar, and it has its own page now.</p>' % OM)
h=chip(h,'Omaha','auto-transport-omaha-nebraska')
h=faq_edit(h,'Yes, the headquarters downtown relocate employees from across the country on start dates.',
             'Yes, the headquarters downtown relocate employees from across the country on start dates. The %s page covers the meeting spots and the base.' % OM)
h=faq_edit(h,'Both price among the cheapest long lanes in the region.','Both price among the lowest-cost long lanes in the region.')
open(p,'w',encoding='utf-8').write(h); resync(p); print('nebraska updated (first block)')

# ---------------- New Jersey (first block) ----------------
p=S+'new-jersey-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Newark has its own page with local lanes, meeting spots, and a phone line. '
       'Jersey City, Paterson, Elizabeth, Edison, Trenton, the Shore, and every other New Jersey town are covered from this page.')
h=first_block(h,'NJ',intro,'North Jersey')
h=rep(h,'Newark, the Oranges, and Montclair have older grids with the same answer.</p>',
        '%s, the Oranges, and Montclair have older grids with the same answer. Newark has its own page now.</p>' % NE)
h=chip(h,'Newark','auto-transport-newark-new-jersey')
open(p,'w',encoding='utf-8').write(h); print('new jersey updated (first block)')

# ---------------- New Mexico (regen) ----------------
p=S+'new-mexico-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Albuquerque and Las Cruces have their own pages with local lanes, meeting spots, and phone lines. '
       'Santa Fe, the oil patch, the Four Corners, and the rest of New Mexico are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('NM', intro), h, count=1)
h=rep(h,'and neighborhood meeting spots. This page carries Santa Fe, Las Cruces, the southeast, the northwest, and the rest of the state.</p>',
        'and neighborhood meeting spots. %s has one too. This page carries Santa Fe, the southeast, the northwest, and the rest of the state.</p>' % LC)
h=rep(h,'It also covers the oil patch, the bases, the mountain towns, and the city with its own page.',
        'It also covers the oil patch, the bases, the mountain towns, and the two cities with their own pages.')
h=rep(h,'<p>Las Cruces sits forty minutes from El Paso on Interstate 10 and 25. It shares that city’s carrier pool.',
        '<p>%s sits forty minutes from El Paso on Interstate 10 and 25. It shares that city’s carrier pool, and it has its own page now.' % LC)
h=chip(h,'Las Cruces','auto-transport-las-cruces-new-mexico')
h=faq_edit(h,'Las Cruces and Socorro allow curbside on most streets.','Las Cruces and Socorro allow curbside on most streets. The %s page has the campus meeting spots.' % LC)
open(p,'w',encoding='utf-8').write(h); resync(p); print('new mexico updated')

# ---------------- neighbor city pages: link the first plain prose mention ----------------
def link_first(path, city, slug):
    p=S+path; h=open(p,encoding='utf-8').read()
    a=h.index('<section class="ph-stats">'); b=h.index('<footer')
    pat=re.compile(r'(?<![>\w])%s(?![\w<])' % re.escape(city))
    for m in re.finditer(r'<p(?: class="ph-(?:lead|sub|quick-note)")?>(.*?)</p>', h[a:b], re.S):
        if '<table' in m.group(0): continue
        mm=pat.search(m.group(1))
        if mm and ('href="/city/%s/'%slug) not in m.group(1):
            start=a+m.start(1)+mm.start()
            h=h[:start]+'<a href="/city/%s/">%s</a>'%(slug,city)+h[start+len(city):]
            open(p,'w',encoding='utf-8').write(h); print(path.split('/')[1], '-> linked', city); return
    raise SystemExit('no plain mention of %s in %s' % (city, path))
link_first('city/auto-transport-cranston-rhode-island/index.html','Warwick','auto-transport-warwick-rhode-island')
for pg in ['baton-rouge-louisiana','lafayette-louisiana','shreveport-louisiana','metairie-louisiana','new-orleans-louisiana','tuscaloosa-alabama']:
    link_first('city/auto-transport-%s/index.html'%pg,'Jackson','auto-transport-jackson-mississippi')
for pg in ['ankeny-iowa','davenport-iowa','independence-missouri','lees-summit-missouri','olathe-kansas','kansas-city-missouri','lawrence-kansas','topeka-kansas','overland-park-kansas','sioux-city-iowa']:
    link_first('city/auto-transport-%s/index.html'%pg,'Omaha','auto-transport-omaha-nebraska')
for pg in ['albuquerque-new-mexico','el-paso-texas']:
    link_first('city/auto-transport-%s/index.html'%pg,'Las Cruces','auto-transport-las-cruces-new-mexico')
