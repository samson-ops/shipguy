"""Batch 44 state-page integration: first City Pages blocks on MT and ND; NC block regen; chips; quick notes; FAQ links; neighbor links."""
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
MI=L('auto-transport-missoula-montana','Missoula'); GR=L('auto-transport-greensboro-north-carolina','Greensboro'); FA=L('auto-transport-fargo-north-dakota','Fargo')

# ---------------- Montana (first block) ----------------
p=S+'montana-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Missoula has its own page with local lanes, meeting spots, and a phone line. '
       'Billings, Bozeman, Great Falls, Helena, the Flathead, and every other Montana town are covered from this page.')
h=first_block(h,'MT',intro,'Billings &amp; Bozeman')
h=rep(h,'<p>This page covers the corridors and the honest windows, Billings and Bozeman, and Missoula and the Flathead.',
        '<p>This page covers the corridors and the honest windows, Billings and Bozeman, and %s and the Flathead.' % MI)
h=rep(h,'<p>Missoula sits at the junction of Interstate 90 and US 93. The university fills it each August, and the Spokane lane runs two hundred miles west.',
        '<p>Missoula sits at the junction of Interstate 90 and US 93, and it has its own page now. The university fills it each August, and the Spokane lane runs two hundred miles west.')
h=chip(h,'Missoula','auto-transport-missoula-montana')
h=faq_edit(h,'Bozeman and Missoula both have tight streets near campus, so the handoff happens at a lot nearby.',
             'Bozeman and Missoula both have tight streets near campus, so the handoff happens at a lot nearby. The %s page names the lots.' % MI)
open(p,'w',encoding='utf-8').write(h); resync(p); print('montana updated (first block)')

# ---------------- North Dakota (first block) ----------------
p=S+'north-dakota-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Fargo has its own page with local lanes, meeting spots, and a phone line. '
       'Bismarck, Grand Forks, Minot, the oil patch, and every other North Dakota town are covered from this page.')
h=first_block(h,'ND',intro,'Fargo &amp; Bismarck')
h=rep(h,'<p class="ph-lead">Fargo and Bismarck ship on the corporate, medical, and campus calendars.</p>',
        '<p class="ph-lead">%s and Bismarck ship on the corporate, medical, and campus calendars.</p>' % FA)
h=rep(h,'<p>Fargo is the largest city and shares its metro with Moorhead across the river.',
        '<p>Fargo is the largest city and shares its metro with Moorhead across the river. It has its own page now.')
h=chip(h,'Fargo','auto-transport-fargo-north-dakota')
h=faq_edit(h,'Fargo and Grand Forks both allow curbside on most streets.','Fargo and Grand Forks both allow curbside on most streets. The %s page names the campus lots.' % FA)
open(p,'w',encoding='utf-8').write(h); resync(p); print('north dakota updated (first block)')

# ---------------- North Carolina (regen) ----------------
p=S+'north-carolina-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Charlotte, Durham, Raleigh, and Greensboro have their own pages with local lanes, meeting spots, and phone lines. '
       'Winston-Salem, Fayetteville, Jacksonville, Wilmington, Asheville, the coast, and the rest of North Carolina are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('NC', intro), h, count=1)
h=rep(h,'<p class="ph-quick-note">Charlotte, Durham, and Raleigh have their own pages. This page carries Greensboro, Winston-Salem, Fayetteville, Jacksonville, Wilmington, Asheville, the coast, and the rest of the state.</p>',
        '<p class="ph-quick-note">Charlotte, Durham, Raleigh, and %s have their own pages. This page carries Winston-Salem, Fayetteville, Jacksonville, Wilmington, Asheville, the coast, and the rest of the state.</p>' % GR)
h=rep(h,'<p>Greensboro ships on the cargo airport, the universities, and the new plants along the interstate. Winston-Salem ships',
        '<p>%s ships on the cargo airport, the universities, and the new plants along the interstate. It has its own page now. Winston-Salem ships' % GR)
h=chip(h,'Greensboro','auto-transport-greensboro-north-carolina')
open(p,'w',encoding='utf-8').write(h); print('north carolina updated')

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
link_first('city/auto-transport-spokane-washington/index.html','Missoula','auto-transport-missoula-montana')
link_first('city/auto-transport-charlotte-north-carolina/index.html','Greensboro','auto-transport-greensboro-north-carolina')
link_first('city/auto-transport-durham-north-carolina/index.html','Greensboro','auto-transport-greensboro-north-carolina')
link_first('city/auto-transport-st-paul-minnesota/index.html','Fargo','auto-transport-fargo-north-dakota')
