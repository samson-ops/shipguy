import re, sys
sys.path.insert(0,'/home/claude/tools'); import localpage as lp
S='/home/claude/build/shipguy/'
BLOCK=re.compile(r'<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">City Pages</p>.*?</section>', re.S)
def rep(h, old, new, n=1):
    c=h.count(old); assert c==n, (c, old[:80]); return h.replace(old,new)
TE='<a href="/city/auto-transport-tempe-arizona/">Tempe</a>'
SU='<a href="/city/auto-transport-surprise-arizona/">Surprise</a>'
p=S+'arizona-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('Phoenix, Tempe, Mesa, Chandler, Gilbert, Glendale, Surprise, and Tucson have their own pages with local lanes, meeting spots, and phone lines. '
       'Flagstaff, Yuma, Prescott, and every other Arizona town are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('AZ', intro), h, count=1)
# metro chips: turn the span chips for cities with pages into links
for name, slug in [('Tempe','auto-transport-tempe-arizona'),('Surprise','auto-transport-surprise-arizona'),('Mesa','auto-transport-mesa-arizona'),('Chandler','auto-transport-chandler-arizona'),('Gilbert','auto-transport-gilbert-arizona'),('Glendale','auto-transport-glendale-arizona')]:
    h=rep(h,'<span class="ph-chip">%s</span>'%name, '<a class="ph-chip" href="/city/%s/">%s</a>'%(slug,name))
h=rep(h,'They fill Sun City, <a href="/city/auto-transport-mesa-arizona/">Mesa</a>, Green Valley, Oro Valley, Yuma, and Lake Havasu until April.</p>',
        'They fill Sun City, %s, <a href="/city/auto-transport-mesa-arizona/">Mesa</a>, Green Valley, Oro Valley, Yuma, and Lake Havasu until April.</p>' % SU)
open(p,'w',encoding='utf-8').write(h); print('arizona updated')
p=S+'city/auto-transport-phoenix-arizona/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'<p>Arizona State University in Tempe pulls students from across the country.','<p>Arizona State University in %s pulls students from across the country.' % TE)
open(p,'w',encoding='utf-8').write(h); print('phoenix updated')
p=S+'city/auto-transport-glendale-arizona/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'<p>Retirees fill Sun City, Sun City West, and Surprise from October through April.','<p>Retirees fill Sun City, Sun City West, and %s from October through April.' % SU)
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'They ride the same 101 and Grand Avenue carriers. Surprise has gates on many subdivisions, so the driver meets you at the entrance.',
              'They ride the same 101 and Grand Avenue carriers. %s has its own page now, and it has gates on many subdivisions, so the driver meets you at the entrance.' % SU)
open(p,'w',encoding='utf-8').write(head+body); print('glendale updated')
