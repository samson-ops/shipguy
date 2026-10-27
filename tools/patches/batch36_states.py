import re, sys
sys.path.insert(0,'/home/claude/tools'); import localpage as lp
S='/home/claude/build/shipguy/'
BLOCK=re.compile(r'<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">City Pages</p>.*?</section>', re.S)
def rep(h, old, new, n=1):
    c=h.count(old); assert c==n, (c, old[:80]); return h.replace(old,new)
BR='<a href="/city/auto-transport-baton-rouge-louisiana/">Baton Rouge</a>'
SH='<a href="/city/auto-transport-shreveport-louisiana/">Shreveport</a>'
ME='<a href="/city/auto-transport-metairie-louisiana/">Metairie</a>'
p=S+'louisiana-auto-transport.html'; h=open(p,encoding='utf-8').read()
intro=('New Orleans, Metairie, Baton Rouge, and Shreveport have their own pages covering the Quarter, the Causeway, the bridge, the Dallas lane, and evacuation routing. '
       'Lafayette, Lake Charles, Houma, and the rest of Louisiana are covered from this page.')
assert BLOCK.search(h); h=BLOCK.sub(lambda m: lp.state_cities_block('LA', intro), h, count=1)
h=rep(h,'<p>This page covers the corridors, Baton Rouge and the plants, Lafayette and the oil patch, and both bases. It also covers hurricane and flood seasons, the cane harvest, and the city with its own page.</p>',
        '<p>This page covers the corridors, the plants, Lafayette and the oil patch, and both bases. It also covers hurricane and flood seasons, the cane harvest, and the cities with their own pages.</p>')
h=rep(h,'<p>The petrochemical corridor along the river from Baton Rouge to New Orleans relocates engineers and contractors.',
        '<p>The petrochemical corridor along the river from %s to New Orleans relocates engineers and contractors.' % BR)
h=rep(h,'<p>Baton Rouge’s older neighborhoods have low oaks and narrow streets. The driver meets you on a main road.',
        '<p>Baton Rouge’s older neighborhoods have low oaks and narrow streets. The driver meets you on a main road. The Baton Rouge page covers the bridge, the LSU side, and the 2016 flood.')
h=rep(h,'Airmen and families rotate year round, with a summer peak, and Shreveport ships on the Dallas lane.',
        'Airmen and families rotate year round, with a summer peak, and %s ships on the Dallas lane.' % SH)
h=rep(h,'Shreveport and Bossier City ship on Interstate 20 and the Dallas lane.</p>',
        'Shreveport and Bossier City ship on Interstate 20 and the Dallas lane. The Shreveport page covers the base, the casinos, and the State Fair.</p>')
i=h.index('<div class="ph-faq-list">'); head,body=h[:i],h[i:]
body=rep(body,'<p>Yes, every part of the state without its own page is covered here. Shreveport and Bossier City ship on Interstate 20 and the Dallas lane.',
              '<p>Yes, every part of the state without its own page is covered here. %s now has its own page, and it and Bossier City ship on Interstate 20 and the Dallas lane.' % SH)
body=rep(body,'Home football Saturdays close the streets around the stadium in Baton Rouge, so we schedule around the games.',
              'Home football Saturdays close the streets around the stadium in %s, so we schedule around the games.' % BR)
h=head+body
open(p,'w',encoding='utf-8').write(h); print('louisiana updated')
# New Orleans page: link Metairie and Baton Rouge in the Across the Lake / lanes text
p=S+'city/auto-transport-new-orleans-louisiana/index.html'; h=open(p,encoding='utf-8').read()
h=rep(h,'Metairie, Kenner, Gretna, and Slidell have wide streets where the truck comes to the curb.',
        '%s, Kenner, Gretna, and Slidell have wide streets where the truck comes to the curb.' % ME)
open(p,'w',encoding='utf-8').write(h); print('new orleans updated')
