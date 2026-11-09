# -*- coding: utf-8 -*-
"""
Ship Guy city-page builder (reconstructed Oct 2026 after the workspace reset).

The shell (head, CSS, header, hero + pricing tool, footer, scripts) is taken from a
finished city page and tokenised, so a rebuilt page is byte-for-byte the same shell
as every other city page. Content sections are assembled from the helpers below.

Builders do:   from localpage import *   ...   build(cfg, BODY, FAQ)
"""
import os, re, json, html as _html

SITE = os.environ.get('SG_SITE', '/home/claude/build/shipguy')
TOOLS = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_SRC = os.path.join(SITE, 'city', 'auto-transport-milwaukee-wisconsin', 'index.html')
TEMPLATE_CACHE = os.path.join(TOOLS, 'city_template.html')

from icons import SVG_CHECK, SVG_ADDR, SVG_PHONE, SVG_CLOCK

# ----------------------------------------------------------------------------------
# registry: every city page on the site  (slug -> (City, ST))
# ----------------------------------------------------------------------------------
STATE_NAMES = {
 'AL':'Alabama','AK':'Alaska','AZ':'Arizona','AR':'Arkansas','CA':'California','CO':'Colorado','CT':'Connecticut','DE':'Delaware',
 'FL':'Florida','GA':'Georgia','HI':'Hawaii','ID':'Idaho','IL':'Illinois','IN':'Indiana','IA':'Iowa','KS':'Kansas','KY':'Kentucky',
 'LA':'Louisiana','ME':'Maine','MD':'Maryland','MA':'Massachusetts','MI':'Michigan','MN':'Minnesota','MS':'Mississippi','MO':'Missouri',
 'MT':'Montana','NE':'Nebraska','NV':'Nevada','NH':'New Hampshire','NJ':'New Jersey','NM':'New Mexico','NY':'New York',
 'NC':'North Carolina','ND':'North Dakota','OH':'Ohio','OK':'Oklahoma','OR':'Oregon','PA':'Pennsylvania','RI':'Rhode Island',
 'SC':'South Carolina','SD':'South Dakota','TN':'Tennessee','TX':'Texas','UT':'Utah','VT':'Vermont','VA':'Virginia','WA':'Washington',
 'WV':'West Virginia','WI':'Wisconsin','WY':'Wyoming'}

LEGACY_SKIP = {'auto-transport-corpus-christi-texas'}   # older-generation page kept in the repo, outside the generated set

def _load_names():
    """NAMES is derived from the pages on disk (title tag: 'Car Shipping in City, ST — ...')."""
    names = {}
    cdir = os.path.join(SITE, 'city')
    for s in sorted(os.listdir(cdir)):
        p = os.path.join(cdir, s, 'index.html')
        if not s.startswith('auto-transport-') or not os.path.isfile(p) or s in LEGACY_SKIP: continue
        h = open(p, encoding='utf-8').read(200000)
        m = re.search(r'<title>(?:Car Shipping (?:in|to)|Auto Transport in) ([^,]+), ([A-Z]{2}) ', h)
        if not m and s == 'auto-transport-corpus-christi-texas': names[s] = ('Corpus Christi', 'TX'); continue
        if m: names[s] = (m.group(1), m.group(2))
    return names

NAMES = _load_names()

def register(slug, city, st):
    """Register a page that is about to be built (so counts and chips include it)."""
    NAMES[slug] = (city, st)

def state_slug_of(slug):
    """'auto-transport-tulsa-oklahoma' -> 'oklahoma-auto-transport' (via NAMES)."""
    city, st = NAMES[slug]
    return STATE_NAMES[st].lower().replace(' ', '-') + '-auto-transport'

# ----------------------------------------------------------------------------------
# nearby cities (key = slug without the 'auto-transport-' prefix)
# ----------------------------------------------------------------------------------
NEARBY = {}

def _load_nearby():
    """Read the existing nearby blocks off the finished pages so rebuilds keep them."""
    cdir = os.path.join(SITE, 'city')
    for s in NAMES:
        p = os.path.join(cdir, s, 'index.html')
        if not os.path.isfile(p): continue
        h = open(p, encoding='utf-8').read()
        m = re.search(r'<h2>Other Cities We Serve Near .*?<div class="ph-chips">(.*?)</div>', h, flags=re.S)
        if not m: continue
        NEARBY[s.replace('auto-transport-', '', 1)] = re.findall(r'href="/city/([^/"]+)/"', m.group(1))

_load_nearby()

def _s(key, lst):
    NEARBY[key] = lst

# ---- Batch 17 (Oct 2026): Tulsa, Norman, Edmond. Registered here so every build in the batch
#      (and every later rebuild) counts them and can link to them. ----
register('auto-transport-tulsa-oklahoma', 'Tulsa', 'OK')
register('auto-transport-norman-oklahoma', 'Norman', 'OK')
register('auto-transport-edmond-oklahoma', 'Edmond', 'OK')
_s('tulsa-oklahoma', ['auto-transport-oklahoma-city-oklahoma','auto-transport-edmond-oklahoma','auto-transport-norman-oklahoma','auto-transport-wichita-kansas','auto-transport-kansas-city-missouri','auto-transport-dallas-texas'])
_s('norman-oklahoma', ['auto-transport-oklahoma-city-oklahoma','auto-transport-edmond-oklahoma','auto-transport-tulsa-oklahoma','auto-transport-dallas-texas','auto-transport-fort-worth-texas','auto-transport-wichita-kansas'])
_s('edmond-oklahoma', ['auto-transport-oklahoma-city-oklahoma','auto-transport-norman-oklahoma','auto-transport-tulsa-oklahoma','auto-transport-wichita-kansas','auto-transport-kansas-city-missouri','auto-transport-dallas-texas'])
# neighbours of the new pages pick them up on their next rebuild (the live pages get a surgical edit)
NEARBY['oklahoma-city-oklahoma'] = ['auto-transport-edmond-oklahoma','auto-transport-norman-oklahoma','auto-transport-tulsa-oklahoma','auto-transport-dallas-texas','auto-transport-wichita-kansas','auto-transport-kansas-city-missouri']
for _k, _v in {'wichita-kansas':'auto-transport-tulsa-oklahoma','kansas-city-missouri':'auto-transport-tulsa-oklahoma','dallas-texas':'auto-transport-norman-oklahoma'}.items():
    if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 18 (Oct 2026): Queens, Buffalo, Yonkers, Rochester ----
register('auto-transport-queens-new-york', 'Queens', 'NY')
register('auto-transport-buffalo-new-york', 'Buffalo', 'NY')
register('auto-transport-yonkers-new-york', 'Yonkers', 'NY')
register('auto-transport-rochester-new-york', 'Rochester', 'NY')
_s('queens-new-york', ['auto-transport-manhattan-new-york','auto-transport-yonkers-new-york','auto-transport-boston-massachusetts','auto-transport-philadelphia-pennsylvania','auto-transport-baltimore-maryland','auto-transport-buffalo-new-york'])
_s('buffalo-new-york', ['auto-transport-rochester-new-york','auto-transport-cleveland-ohio','auto-transport-detroit-michigan','auto-transport-manhattan-new-york','auto-transport-queens-new-york','auto-transport-boston-massachusetts'])
_s('yonkers-new-york', ['auto-transport-manhattan-new-york','auto-transport-queens-new-york','auto-transport-boston-massachusetts','auto-transport-philadelphia-pennsylvania','auto-transport-baltimore-maryland','auto-transport-buffalo-new-york'])
_s('rochester-new-york', ['auto-transport-buffalo-new-york','auto-transport-manhattan-new-york','auto-transport-queens-new-york','auto-transport-yonkers-new-york','auto-transport-cleveland-ohio','auto-transport-boston-massachusetts'])
NEARBY['manhattan-new-york'] = ['auto-transport-queens-new-york','auto-transport-yonkers-new-york','auto-transport-philadelphia-pennsylvania','auto-transport-boston-massachusetts','auto-transport-baltimore-maryland','auto-transport-buffalo-new-york']
for _k, _v in {'boston-massachusetts':'auto-transport-queens-new-york','philadelphia-pennsylvania':'auto-transport-queens-new-york','cleveland-ohio':'auto-transport-buffalo-new-york','detroit-michigan':'auto-transport-buffalo-new-york'}.items():
    if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)
for _k, _v in {'boston-massachusetts':'auto-transport-rochester-new-york','cleveland-ohio':'auto-transport-rochester-new-york'}.items():
    if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 19 (Oct 2026): Syracuse, Albany, Brooklyn, Bronx ----
register('auto-transport-syracuse-new-york', 'Syracuse', 'NY')
register('auto-transport-albany-new-york', 'Albany', 'NY')
register('auto-transport-brooklyn-new-york', 'Brooklyn', 'NY')
register('auto-transport-bronx-new-york', 'Bronx', 'NY')
_s('syracuse-new-york', ['auto-transport-rochester-new-york','auto-transport-albany-new-york','auto-transport-buffalo-new-york','auto-transport-manhattan-new-york','auto-transport-boston-massachusetts','auto-transport-philadelphia-pennsylvania'])
_s('albany-new-york', ['auto-transport-syracuse-new-york','auto-transport-boston-massachusetts','auto-transport-yonkers-new-york','auto-transport-manhattan-new-york','auto-transport-rochester-new-york','auto-transport-philadelphia-pennsylvania'])
_s('brooklyn-new-york', ['auto-transport-manhattan-new-york','auto-transport-queens-new-york','auto-transport-bronx-new-york','auto-transport-yonkers-new-york','auto-transport-philadelphia-pennsylvania','auto-transport-boston-massachusetts'])
_s('bronx-new-york', ['auto-transport-manhattan-new-york','auto-transport-yonkers-new-york','auto-transport-queens-new-york','auto-transport-brooklyn-new-york','auto-transport-boston-massachusetts','auto-transport-albany-new-york'])
NEARBY['manhattan-new-york'] = ['auto-transport-brooklyn-new-york','auto-transport-queens-new-york','auto-transport-bronx-new-york','auto-transport-yonkers-new-york','auto-transport-philadelphia-pennsylvania','auto-transport-boston-massachusetts','auto-transport-baltimore-maryland']
NEARBY['queens-new-york'] = ['auto-transport-manhattan-new-york','auto-transport-brooklyn-new-york','auto-transport-bronx-new-york','auto-transport-yonkers-new-york','auto-transport-boston-massachusetts','auto-transport-philadelphia-pennsylvania','auto-transport-baltimore-maryland']
NEARBY['yonkers-new-york'] = ['auto-transport-bronx-new-york','auto-transport-manhattan-new-york','auto-transport-queens-new-york','auto-transport-albany-new-york','auto-transport-boston-massachusetts','auto-transport-philadelphia-pennsylvania','auto-transport-buffalo-new-york']
for _k, _v in {'buffalo-new-york':'auto-transport-syracuse-new-york','rochester-new-york':'auto-transport-syracuse-new-york','boston-massachusetts':'auto-transport-albany-new-york'}.items():
    if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 20 (Oct 2026): Cincinnati, Columbus, Akron, Dayton ----
register('auto-transport-cincinnati-ohio', 'Cincinnati', 'OH')
register('auto-transport-columbus-ohio', 'Columbus', 'OH')
register('auto-transport-akron-ohio', 'Akron', 'OH')
register('auto-transport-dayton-ohio', 'Dayton', 'OH')
_s('cincinnati-ohio', ['auto-transport-dayton-ohio','auto-transport-columbus-ohio','auto-transport-louisville-kentucky','auto-transport-lexington-kentucky','auto-transport-indianapolis-indiana','auto-transport-cleveland-ohio'])
_s('columbus-ohio', ['auto-transport-cincinnati-ohio','auto-transport-dayton-ohio','auto-transport-cleveland-ohio','auto-transport-akron-ohio','auto-transport-indianapolis-indiana','auto-transport-louisville-kentucky'])
_s('akron-ohio', ['auto-transport-cleveland-ohio','auto-transport-columbus-ohio','auto-transport-detroit-michigan','auto-transport-buffalo-new-york','auto-transport-cincinnati-ohio','auto-transport-indianapolis-indiana'])
_s('dayton-ohio', ['auto-transport-cincinnati-ohio','auto-transport-columbus-ohio','auto-transport-indianapolis-indiana','auto-transport-louisville-kentucky','auto-transport-lexington-kentucky','auto-transport-cleveland-ohio'])
NEARBY['cleveland-ohio'] = ['auto-transport-akron-ohio','auto-transport-columbus-ohio','auto-transport-cincinnati-ohio','auto-transport-detroit-michigan','auto-transport-buffalo-new-york','auto-transport-indianapolis-indiana','auto-transport-chicago-illinois']
for _k, _v in {'indianapolis-indiana':'auto-transport-cincinnati-ohio','louisville-kentucky':'auto-transport-cincinnati-ohio','lexington-kentucky':'auto-transport-cincinnati-ohio','detroit-michigan':'auto-transport-columbus-ohio'}.items():
    if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)
if 'auto-transport-dayton-ohio' not in NEARBY['indianapolis-indiana']: NEARBY['indianapolis-indiana'].append('auto-transport-dayton-ohio')

# ---- Batch 21 (Oct 2026): St. Louis, Springfield, Columbia, Independence, Lee's Summit ----
register('auto-transport-st-louis-missouri', 'St. Louis', 'MO')
register('auto-transport-springfield-missouri', 'Springfield', 'MO')
register('auto-transport-columbia-missouri', 'Columbia', 'MO')
register('auto-transport-independence-missouri', 'Independence', 'MO')
register('auto-transport-lees-summit-missouri', 'Lee’s Summit', 'MO')
_s('st-louis-missouri', ['auto-transport-columbia-missouri','auto-transport-kansas-city-missouri','auto-transport-springfield-missouri','auto-transport-chicago-illinois','auto-transport-indianapolis-indiana','auto-transport-louisville-kentucky'])
_s('springfield-missouri', ['auto-transport-tulsa-oklahoma','auto-transport-kansas-city-missouri','auto-transport-st-louis-missouri','auto-transport-columbia-missouri','auto-transport-oklahoma-city-oklahoma','auto-transport-wichita-kansas'])
_s('columbia-missouri', ['auto-transport-st-louis-missouri','auto-transport-kansas-city-missouri','auto-transport-independence-missouri','auto-transport-lees-summit-missouri','auto-transport-springfield-missouri','auto-transport-indianapolis-indiana'])
_s('independence-missouri', ['auto-transport-kansas-city-missouri','auto-transport-lees-summit-missouri','auto-transport-columbia-missouri','auto-transport-wichita-kansas','auto-transport-st-louis-missouri','auto-transport-tulsa-oklahoma'])
_s('lees-summit-missouri', ['auto-transport-kansas-city-missouri','auto-transport-independence-missouri','auto-transport-columbia-missouri','auto-transport-wichita-kansas','auto-transport-springfield-missouri','auto-transport-st-louis-missouri'])
NEARBY['kansas-city-missouri'] = ['auto-transport-independence-missouri','auto-transport-lees-summit-missouri','auto-transport-st-louis-missouri','auto-transport-columbia-missouri','auto-transport-wichita-kansas','auto-transport-tulsa-oklahoma','auto-transport-oklahoma-city-oklahoma']
for _k, _v in {'tulsa-oklahoma':'auto-transport-springfield-missouri','chicago-illinois':'auto-transport-st-louis-missouri','louisville-kentucky':'auto-transport-st-louis-missouri','wichita-kansas':'auto-transport-independence-missouri'}.items():
    if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)
NEARBY['indianapolis-indiana'] = ['auto-transport-chicago-illinois','auto-transport-louisville-kentucky','auto-transport-cincinnati-ohio','auto-transport-dayton-ohio','auto-transport-lexington-kentucky','auto-transport-st-louis-missouri','auto-transport-cleveland-ohio']

# ---- Batch 22 (Oct 2026): Madison, Green Bay, Kenosha (Milwaukee already live) ----
register('auto-transport-madison-wisconsin', 'Madison', 'WI')
register('auto-transport-green-bay-wisconsin', 'Green Bay', 'WI')
register('auto-transport-kenosha-wisconsin', 'Kenosha', 'WI')
_s('madison-wisconsin', ['auto-transport-milwaukee-wisconsin','auto-transport-green-bay-wisconsin','auto-transport-kenosha-wisconsin','auto-transport-chicago-illinois','auto-transport-indianapolis-indiana','auto-transport-st-louis-missouri'])
_s('green-bay-wisconsin', ['auto-transport-milwaukee-wisconsin','auto-transport-madison-wisconsin','auto-transport-kenosha-wisconsin','auto-transport-chicago-illinois','auto-transport-detroit-michigan','auto-transport-indianapolis-indiana'])
_s('kenosha-wisconsin', ['auto-transport-milwaukee-wisconsin','auto-transport-chicago-illinois','auto-transport-madison-wisconsin','auto-transport-green-bay-wisconsin','auto-transport-indianapolis-indiana','auto-transport-detroit-michigan'])
NEARBY['milwaukee-wisconsin'] = ['auto-transport-madison-wisconsin','auto-transport-kenosha-wisconsin','auto-transport-green-bay-wisconsin','auto-transport-chicago-illinois','auto-transport-indianapolis-indiana','auto-transport-detroit-michigan','auto-transport-cleveland-ohio']
if 'auto-transport-kenosha-wisconsin' not in NEARBY['chicago-illinois']: NEARBY['chicago-illinois'].append('auto-transport-kenosha-wisconsin')

# ---- Batch 23 (Oct 2026): Fresno, Bakersfield, Stockton, Irvine ----
register('auto-transport-fresno-california', 'Fresno', 'CA')
register('auto-transport-bakersfield-california', 'Bakersfield', 'CA')
register('auto-transport-stockton-california', 'Stockton', 'CA')
register('auto-transport-irvine-california', 'Irvine', 'CA')
_s('fresno-california', ['auto-transport-bakersfield-california','auto-transport-stockton-california','auto-transport-sacramento-california','auto-transport-san-jose-california','auto-transport-los-angeles-california','auto-transport-oakland-california'])
_s('bakersfield-california', ['auto-transport-fresno-california','auto-transport-los-angeles-california','auto-transport-long-beach-california','auto-transport-riverside-california','auto-transport-las-vegas-nevada','auto-transport-stockton-california'])
_s('stockton-california', ['auto-transport-sacramento-california','auto-transport-oakland-california','auto-transport-san-jose-california','auto-transport-san-francisco-california','auto-transport-fresno-california','auto-transport-bakersfield-california'])
_s('irvine-california', ['auto-transport-santa-ana-california','auto-transport-anaheim-california','auto-transport-long-beach-california','auto-transport-los-angeles-california','auto-transport-riverside-california','auto-transport-san-diego-california'])
for _k, _vs in {'sacramento-california':['auto-transport-stockton-california','auto-transport-fresno-california'],
               'san-jose-california':['auto-transport-stockton-california','auto-transport-fresno-california'],
               'oakland-california':['auto-transport-stockton-california','auto-transport-fresno-california'],
               'san-francisco-california':['auto-transport-stockton-california'],
               'los-angeles-california':['auto-transport-bakersfield-california','auto-transport-irvine-california'],
               'riverside-california':['auto-transport-irvine-california'],
               'las-vegas-nevada':['auto-transport-bakersfield-california'],
               'san-diego-california':['auto-transport-irvine-california'],
               'santa-ana-california':['auto-transport-irvine-california'],
               'anaheim-california':['auto-transport-irvine-california'],
               'long-beach-california':['auto-transport-irvine-california']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 24 (Oct 2026): Chula Vista, Fremont, San Bernardino ----
register('auto-transport-chula-vista-california', 'Chula Vista', 'CA')
register('auto-transport-fremont-california', 'Fremont', 'CA')
register('auto-transport-san-bernardino-california', 'San Bernardino', 'CA')
_s('chula-vista-california', ['auto-transport-san-diego-california','auto-transport-irvine-california','auto-transport-riverside-california','auto-transport-long-beach-california','auto-transport-los-angeles-california','auto-transport-phoenix-arizona'])
_s('fremont-california', ['auto-transport-san-jose-california','auto-transport-oakland-california','auto-transport-san-francisco-california','auto-transport-stockton-california','auto-transport-sacramento-california','auto-transport-fresno-california'])
_s('san-bernardino-california', ['auto-transport-riverside-california','auto-transport-los-angeles-california','auto-transport-anaheim-california','auto-transport-irvine-california','auto-transport-las-vegas-nevada','auto-transport-san-diego-california'])
for _k, _vs in {'san-diego-california':['auto-transport-chula-vista-california'],
               'irvine-california':['auto-transport-chula-vista-california','auto-transport-san-bernardino-california'],
               'riverside-california':['auto-transport-san-bernardino-california'],
               'san-jose-california':['auto-transport-fremont-california'],
               'oakland-california':['auto-transport-fremont-california'],
               'san-francisco-california':['auto-transport-fremont-california'],
               'stockton-california':['auto-transport-fremont-california'],
               'las-vegas-nevada':['auto-transport-san-bernardino-california'],
               'anaheim-california':['auto-transport-san-bernardino-california']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 25 (Oct 2026): Staten Island ----
register('auto-transport-staten-island-new-york', 'Staten Island', 'NY')
_s('staten-island-new-york', ['auto-transport-brooklyn-new-york','auto-transport-manhattan-new-york','auto-transport-queens-new-york','auto-transport-bronx-new-york','auto-transport-philadelphia-pennsylvania','auto-transport-yonkers-new-york'])
for _k in ['brooklyn-new-york','manhattan-new-york','queens-new-york','bronx-new-york','philadelphia-pennsylvania']:
    if _k in NEARBY and 'auto-transport-staten-island-new-york' not in NEARBY[_k]: NEARBY[_k].append('auto-transport-staten-island-new-york')

# ---- Batch 26 (Oct 2026): Connecticut — Bridgeport, Stamford, New Haven, Hartford, Waterbury, Norwalk ----
register('auto-transport-bridgeport-connecticut', 'Bridgeport', 'CT')
register('auto-transport-stamford-connecticut', 'Stamford', 'CT')
register('auto-transport-new-haven-connecticut', 'New Haven', 'CT')
register('auto-transport-hartford-connecticut', 'Hartford', 'CT')
register('auto-transport-waterbury-connecticut', 'Waterbury', 'CT')
register('auto-transport-norwalk-connecticut', 'Norwalk', 'CT')
_s('bridgeport-connecticut', ['auto-transport-norwalk-connecticut','auto-transport-new-haven-connecticut','auto-transport-stamford-connecticut','auto-transport-waterbury-connecticut','auto-transport-hartford-connecticut','auto-transport-yonkers-new-york'])
_s('stamford-connecticut', ['auto-transport-norwalk-connecticut','auto-transport-bridgeport-connecticut','auto-transport-new-haven-connecticut','auto-transport-yonkers-new-york','auto-transport-bronx-new-york','auto-transport-manhattan-new-york'])
_s('new-haven-connecticut', ['auto-transport-bridgeport-connecticut','auto-transport-hartford-connecticut','auto-transport-waterbury-connecticut','auto-transport-norwalk-connecticut','auto-transport-stamford-connecticut','auto-transport-boston-massachusetts'])
_s('hartford-connecticut', ['auto-transport-new-haven-connecticut','auto-transport-waterbury-connecticut','auto-transport-bridgeport-connecticut','auto-transport-boston-massachusetts','auto-transport-albany-new-york','auto-transport-stamford-connecticut'])
_s('waterbury-connecticut', ['auto-transport-hartford-connecticut','auto-transport-new-haven-connecticut','auto-transport-bridgeport-connecticut','auto-transport-norwalk-connecticut','auto-transport-stamford-connecticut','auto-transport-albany-new-york'])
_s('norwalk-connecticut', ['auto-transport-stamford-connecticut','auto-transport-bridgeport-connecticut','auto-transport-new-haven-connecticut','auto-transport-yonkers-new-york','auto-transport-manhattan-new-york','auto-transport-hartford-connecticut'])
for _k, _vs in {'yonkers-new-york':['auto-transport-stamford-connecticut'],
               'bronx-new-york':['auto-transport-stamford-connecticut'],
               'boston-massachusetts':['auto-transport-hartford-connecticut'],
               'albany-new-york':['auto-transport-hartford-connecticut']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 27 (Oct 2026): Worcester, Springfield MA, Little Rock, Fayetteville, Fort Smith ----
register('auto-transport-worcester-massachusetts', 'Worcester', 'MA')
register('auto-transport-springfield-massachusetts', 'Springfield', 'MA')
register('auto-transport-little-rock-arkansas', 'Little Rock', 'AR')
register('auto-transport-fayetteville-arkansas', 'Fayetteville', 'AR')
register('auto-transport-fort-smith-arkansas', 'Fort Smith', 'AR')
_s('worcester-massachusetts', ['auto-transport-boston-massachusetts','auto-transport-springfield-massachusetts','auto-transport-hartford-connecticut','auto-transport-albany-new-york','auto-transport-new-haven-connecticut','auto-transport-manhattan-new-york'])
_s('springfield-massachusetts', ['auto-transport-hartford-connecticut','auto-transport-worcester-massachusetts','auto-transport-boston-massachusetts','auto-transport-albany-new-york','auto-transport-new-haven-connecticut','auto-transport-waterbury-connecticut'])
_s('little-rock-arkansas', ['auto-transport-fayetteville-arkansas','auto-transport-fort-smith-arkansas','auto-transport-tulsa-oklahoma','auto-transport-dallas-texas','auto-transport-st-louis-missouri','auto-transport-springfield-missouri'])
_s('fayetteville-arkansas', ['auto-transport-fort-smith-arkansas','auto-transport-little-rock-arkansas','auto-transport-tulsa-oklahoma','auto-transport-springfield-missouri','auto-transport-kansas-city-missouri','auto-transport-oklahoma-city-oklahoma'])
_s('fort-smith-arkansas', ['auto-transport-fayetteville-arkansas','auto-transport-little-rock-arkansas','auto-transport-tulsa-oklahoma','auto-transport-oklahoma-city-oklahoma','auto-transport-dallas-texas','auto-transport-springfield-missouri'])
NEARBY['boston-massachusetts'] = ['auto-transport-worcester-massachusetts','auto-transport-manhattan-new-york','auto-transport-hartford-connecticut','auto-transport-albany-new-york','auto-transport-philadelphia-pennsylvania','auto-transport-augusta-maine','auto-transport-baltimore-maryland','auto-transport-rochester-new-york']
for _k, _vs in {'hartford-connecticut':['auto-transport-springfield-massachusetts','auto-transport-worcester-massachusetts'],
               'albany-new-york':['auto-transport-springfield-massachusetts'],
               'tulsa-oklahoma':['auto-transport-fort-smith-arkansas'],
               'springfield-missouri':['auto-transport-fayetteville-arkansas'],
               'dallas-texas':['auto-transport-little-rock-arkansas'],
               'st-louis-missouri':['auto-transport-little-rock-arkansas']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ----------------------------------------------------------------------------------
# content helpers (markup matches the finished pages exactly)
# ----------------------------------------------------------------------------------
def stats(items):
    return ('<section class="ph-stats"><div class="ph-wrap">' +
            ''.join('<div class="ph-stat"><b>%s</b><span>%s</span></div>' % (b, s) for b, s in items) +
            '</div></section>')

def intro_block(eyebrow, h2, paras, quick_head, quick_paras, quick_note):
    return ('<section class="ph-sec"><div class="ph-wrap ph-intro-grid"><div class="ph-intro-copy">'
            '<p class="ph-eyebrow">%s</p><h2>%s</h2>%s</div>'
            '<div class="ph-quick"><span class="ph-quick-head">%s</span>%s<p class="ph-quick-note">%s</p></div></div></section>'
            % (eyebrow, h2, ''.join('<p>%s</p>' % p for p in paras), quick_head,
               ''.join('<p>%s</p>' % p for p in quick_paras), quick_note))

def sec(eyebrow, h2, inner, alt=False, sub=None):
    return ('<section class="ph-sec%s"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">%s</p><h2>%s</h2>%s</div>%s</div></section>'
            % (' ph-alt' if alt else '', eyebrow, h2, ('<p class="ph-sub">%s</p>' % sub) if sub else '', inner))

def prose(*parts):
    return '<div class="ph-prose">' + ''.join(parts) + '</div>'

def L(t):  return '<p class="ph-lead">%s</p>' % t
def P(t):  return '<p>%s</p>' % t
def NOTE(t): return '<div class="ph-note">%s</div>' % t
def ULI(items):
    return '<ul>' + ''.join('<li>%s<span>%s</span></li>' % (SVG_CHECK, t) for t in items) + '</ul>'
def chips(items):
    return '<div class="ph-chips">' + ''.join('<span class="ph-chip">%s</span>' % c for c in items) + '</div>'

def rate_table(eyebrow, h2, sub, headers, rows, fine, after='', alt=False):
    thead = '<thead><tr>' + ''.join('<th>%s</th>' % x for x in headers) + '</tr></thead>'
    tbody = '<tbody>' + ''.join('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>' for r in rows) + '</tbody>'
    return ('<section class="ph-sec%s"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">%s</p><h2>%s</h2><p class="ph-sub">%s</p></div>'
            '<div class="ph-table-wrap"><table class="ph-rates">%s%s</table></div><p class="ph-fine">%s</p>%s</div></section>'
            % (' ph-alt' if alt else '', eyebrow, h2, sub, thead, tbody, fine, after))

def faq_section(FAQ, eyebrow, h2):
    items = ''.join('<details class="ph-faq"><summary>%s<span class="ph-fp"></span></summary><div class="fa"><p>%s</p></div></details>' % (q, a) for q, a in FAQ)
    return ('<section class="ph-sec"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">%s</p><h2>%s</h2></div><div class="ph-faq-list">%s</div></div></section>'
            % (eyebrow, h2, items))

def cta(h2, sub, tel, disp, btn):
    return ('<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">Get Started</p><h2>%s</h2><p class="ph-sub">%s</p></div>'
            '<div class="ph-tcta"><a href="#pquote" class="btn btn-primary">%s</a> <a href="tel:%s" class="btn btn-ghost">Call %s</a></div></div></section>'
            % (h2, sub, btn, tel, disp))

def office(city_label, addr1, addr2, tel, disp, hours_tz, map_q, eyebrow, h2, sub, alt=False, map_src=None, map_link=None):
    src = map_src or ('https://www.google.com/maps?q=' + map_q + '&output=embed')
    rows = ('<div class="ph-office-row"><span class="ph-office-ic">%s</span><div><b>Address</b><span>%s<br>%s</span></div></div>' % (SVG_ADDR, addr1, addr2) +
            '<div class="ph-office-row"><span class="ph-office-ic">%s</span><div><b>Local phone</b><a href="tel:%s">%s</a></div></div>' % (SVG_PHONE, tel, disp) +
            '<div class="ph-office-row"><span class="ph-office-ic">%s</span><div><b>Hours</b><span>Monday&ndash;Sunday<br>6:00 AM &ndash; 11:00 PM %s</span></div></div>' % (SVG_CLOCK, hours_tz))
    if map_link:
        rows += directions_row(map_link)
    return ('<section class="ph-sec%s"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">%s</p><h2>%s</h2><p class="ph-sub">%s</p></div>'
            '<div class="ph-office"><div class="ph-office-card"><h3>Ship Guy Auto Transport &mdash; %s</h3>%s</div>'
            '<div class="ph-map"><iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="%s" title="Ship Guy %s office map"></iframe></div></div></div></section>'
            % (' ph-alt' if alt else '', eyebrow, h2, sub, city_label, rows, src, city_label))

def directions_row(map_link):
    """Google Business Profile share link, rendered as a fourth row of the office card."""
    return ('<div class="ph-office-row"><span class="ph-office-ic">%s</span><div><b>Directions</b>'
            '<a href="%s" target="_blank" rel="noopener">Open in Google Maps</a></div></div>' % (SVG_ADDR, map_link))

NEARBY_STYLE = '<style>.ph-chips a.ph-chip{display:inline-block;text-decoration:none;color:inherit}.ph-chips a.ph-chip:hover{background:var(--brand-tint);border-color:#c7d2fb}</style>'

def state_guide_link(slug):
    city, st = NAMES[slug]
    return 'Statewide guide: <a href="/%s">%s auto transport</a> &nbsp;&middot;&nbsp; ' % (state_slug_of(slug), STATE_NAMES[st])

def nearby_block(slug):
    key = slug.replace('auto-transport-', '', 1)
    city = NAMES[slug][0]
    lst = NEARBY.get(key, [])
    chips_html = ''.join('<a class="ph-chip" href="/city/%s/">%s, %s</a>' % (s, NAMES[s][0], NAMES[s][1]) for s in lst if s in NAMES)
    return ('<section class="ph-sec"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">Nearby</p><h2>Other Cities We Serve Near %s</h2></div>%s'
            '<p style="text-align:center;max-width:820px;margin:0 auto 18px">Carriers that work %s also cover these nearby cities.</p>'
            '<div class="ph-chips">%s</div>'
            '<p style="text-align:center;margin:22px 0 0">%s<a href="/locations">See all %d cities we serve &rarr;</a></p></div></section>'
            % (city, NEARBY_STYLE, city, chips_html, state_guide_link(slug), len(NAMES)))

def state_cities_block(st, intro_text):
    """The 'City Pages' section on a state page: chips for every city page in that state (alphabetical)."""
    cities = sorted((v[0], k) for k, v in NAMES.items() if v[1] == st)
    chips_html = ''.join('<a class="ph-chip" href="/city/%s/">%s</a>' % (k, c) for c, k in cities)
    return ('<section class="ph-sec ph-alt"><div class="ph-wrap"><div class="ph-head"><p class="ph-eyebrow">City Pages</p><h2>Cities We Serve in %s</h2></div>%s'
            '<p style="text-align:center;max-width:820px;margin:0 auto 18px">%s</p><div class="ph-chips">%s</div>'
            '<p style="text-align:center;margin:22px 0 0"><a href="/locations">See every city we serve &rarr;</a></p></div></section>'
            % (STATE_NAMES[st], NEARBY_STYLE, intro_text, chips_html))

# ----------------------------------------------------------------------------------
# shell template
# ----------------------------------------------------------------------------------
def _make_template():
    h = open(TEMPLATE_SRC, encoding='utf-8').read()
    # strip the post-build SEO enrichment (breadcrumb nav/css, BreadcrumbList, LocalBusiness) — build() re-adds it
    h = re.sub(r'<nav class="ph-crumbs" aria-label="Breadcrumb">.*?</nav>\n?', '', h, count=1, flags=re.S)
    h = re.sub(r'<style id="sg-crumbs-css">.*?</style>\n?', '', h, count=1, flags=re.S)
    h = re.sub(r'<script type="application/ld\+json" id="sg-[a-z]+">.*?</script>\n?', '', h, flags=re.S)
    # --- head: keep one canonical / OG block (the duplicate homepage block was a template bug) ---
    head_end = h.index('</head>')
    head = h[:head_end]
    if '<link rel="canonical" href="https://shipguy.com/">' in head:   # already fixed on the live pages
        dup_start = head.index('<link rel="canonical" href="https://shipguy.com/">')
        dup_end = head.index('<meta name="description"')
        head = head[:dup_start] + head[dup_end:]
    h = head + h[head_end:]
    T = 'Car Shipping in Milwaukee, WI — Auto Transport | Ship Guy'
    D = re.search(r'<meta name="description" content="([^"]*)"', h).group(1)
    assert h.count(T) == 3 and h.count(D) == 3, (h.count(T), h.count(D))
    h = h.replace(T, '{{TITLE}}').replace(D, '{{DESC}}')
    h = h.replace('https://shipguy.com/city/auto-transport-milwaukee-wisconsin/', '{{URL}}')
    # --- json-ld ---
    h = re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">\n{{JSONLD}}\n</script>', h, count=1, flags=re.S)
    # --- phone / brand / hero ---
    assert h.count('+14144859612') == 6, h.count('+14144859612')
    h = h.replace('+14144859612', '{{TEL}}').replace('(414)&nbsp;485-9612', '{{DISP_NBSP}}').replace('(414) 485-9612', '{{DISP}}')
    h = h.replace('Milwaukee moves<br>with us', '{{BRAND}} moves<br>with us')
    h = re.sub(r'<h1 class="reveal d2">.*?</h1>', '<h1 class="reveal d2">{{H1}}</h1>', h, count=1, flags=re.S)
    h = re.sub(r'<p class="lede reveal d2">.*?</p>', '<p class="lede reveal d2">{{LEDE}}</p>', h, count=1, flags=re.S)
    # --- body content: from the stats band to the footer ---
    a = h.index('<section class="ph-stats">'); b = h.index('<footer')
    h = h[:a] + '{{BODY}}' + h[b:]
    for tok in ['{{TITLE}}', '{{DESC}}', '{{URL}}', '{{JSONLD}}', '{{TEL}}', '{{DISP}}', '{{BRAND}}', '{{H1}}', '{{LEDE}}', '{{BODY}}']:
        assert tok in h, tok
    assert 'Milwaukee' not in h, [m.start() for m in re.finditer('Milwaukee', h)][:3]
    assert h.count('rel="canonical"') == 1 and h.count('GTM-MQ7HKJTJ') == 2
    open(TEMPLATE_CACHE, 'w', encoding='utf-8').write(h)
    return h

def template():
    if os.path.isfile(TEMPLATE_CACHE):
        return open(TEMPLATE_CACHE, encoding='utf-8').read()
    return _make_template()

# ----------------------------------------------------------------------------------
# build
# ----------------------------------------------------------------------------------
def short_meta(meta, limit=160, tail=' Free quote.'):
    """First sentence whole, then comma-clauses greedily while the result stays within the limit."""
    m = re.sub(r'\s*Free quote\.?\s*$', '', meta.strip())
    parts = re.split(r'(?<=\.)(?<!\bSt\.)(?<!\bMt\.)(?<!\bFt\.)\s+', m, maxsplit=1)   # "St. Paul" is not a sentence end (Nov 2, 2026)
    out = parts[0]
    if len(parts) > 1:
        clauses = re.split(r',\s*', parts[1])
        for i, c in enumerate(clauses):
            c = c.rstrip('.')
            cand = out + (' ' if i == 0 else ', ') + c
            if len(cand) + 1 + len(tail) <= limit:
                out = cand
            else:
                break
    out = out.rstrip(',. ')
    return out + '.' + tail

def clean_links(h):
    """Builders may write site-relative 'page.html' links; pages use clean root URLs."""
    h = re.sub(r'href="index\.html"', 'href="/"', h)
    return re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"', lambda m: 'href="/%s%s"' % (m.group(1), m.group(2) or ''), h)

def strip_tags(t):
    return _html.unescape(re.sub(r'<[^>]+>', '', t)).replace(' ', ' ')

def faq_jsonld(FAQ):
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                       "mainEntity": [{"@type": "Question", "name": strip_tags(q),
                                       "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in FAQ]},
                      ensure_ascii=False)

def build(cfg, BODY, FAQ, out_path=None):
    slug = cfg['slug']
    if slug not in NAMES:
        m = re.search(r'Car Shipping in ([^,]+), ([A-Z]{2})', cfg['title'])
        register(slug, m.group(1), m.group(2))
    blocks = list(BODY)
    # nearby block goes right before the office section (or before the FAQ if there is no office)
    idx = next((i for i, b in enumerate(blocks) if 'class="ph-office"' in b), None)
    if idx is None:
        idx = next((i for i, b in enumerate(blocks) if 'ph-faq-list' in b), len(blocks))
    blocks.insert(idx, nearby_block(slug))
    body = '\n'.join(blocks)
    h = template()
    url = 'https://shipguy.com/city/%s/' % slug
    h = (h.replace('{{TITLE}}', cfg['title']).replace('{{DESC}}', short_meta(cfg['meta'])).replace('{{URL}}', url)
          .replace('{{JSONLD}}', faq_jsonld(FAQ)).replace('{{TEL}}', cfg['tel']).replace('{{DISP}}', cfg['disp'])
          .replace('{{DISP_NBSP}}', cfg['disp'].replace(' ', '&nbsp;')).replace('{{BRAND}}', cfg['brand'])
          .replace('{{H1}}', cfg['h1']).replace('{{LEDE}}', cfg['lede']).replace('{{BODY}}', body))
    h = clean_links(h)
    assert '{{' not in h, re.findall(r'\{\{[A-Z_]+\}\}', h)
    import seo_enrich                                   # breadcrumb + BreadcrumbList + LocalBusiness (Oct 27, 2026)
    h = seo_enrich.enrich_city(h, slug, NAMES[slug][0], STATE_NAMES[NAMES[slug][1]], state_slug_of(slug))
    out = out_path or os.path.join(os.environ.get('SG_OUT_DIR', os.path.join(SITE, 'city')), slug, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(h)
    # quick self-check
    text = strip_tags(re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', h, flags=re.S))
    words = len(re.sub(r'\s+', ' ', body_text(h)).split())
    kw = text.lower().count(cfg.get('keyword', '').lower()) if cfg.get('keyword') else 0
    missing = [t for t in cfg.get('localterms', []) if t.lower() not in text.lower()]
    print('built %s | content words %d | keyword x%d | GTM x%d | canonical x%d | local terms missing: %s'
          % (out.replace(SITE + '/', ''), words, kw, h.count('GTM-MQ7HKJTJ'), h.count('rel="canonical"'), missing or 'none'))
    return out

def body_text(h):
    a = h.index('<section class="ph-stats">'); b = h.index('<footer')
    return strip_tags(re.sub(r'<style[^>]*>.*?</style>', ' ', h[a:b], flags=re.S))

def refresh_footer_states(*a, **k):
    """No-op: the shell template already carries the final 50-state footer."""
    return None

# ---- Batch 28 (Oct 2026): Wilmington, Dover (Delaware's first city pages) ----
register('auto-transport-wilmington-delaware', 'Wilmington', 'DE')
register('auto-transport-dover-delaware', 'Dover', 'DE')
_s('wilmington-delaware', ['auto-transport-philadelphia-pennsylvania','auto-transport-dover-delaware','auto-transport-baltimore-maryland','auto-transport-staten-island-new-york','auto-transport-manhattan-new-york','auto-transport-brooklyn-new-york'])
_s('dover-delaware', ['auto-transport-wilmington-delaware','auto-transport-philadelphia-pennsylvania','auto-transport-baltimore-maryland','auto-transport-staten-island-new-york','auto-transport-manhattan-new-york','auto-transport-raleigh-north-carolina'])
# neighbours: Philadelphia and Baltimore pick up the Delaware pages (surgical edit on the live pages)
for _k, _vs in {'philadelphia-pennsylvania':['auto-transport-wilmington-delaware'],
               'baltimore-maryland':['auto-transport-wilmington-delaware','auto-transport-dover-delaware']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 29 (Oct 2026): Denver, Colorado Springs, Aurora (Colorado's first city pages) ----
register('auto-transport-denver-colorado', 'Denver', 'CO')
register('auto-transport-colorado-springs-colorado', 'Colorado Springs', 'CO')
register('auto-transport-aurora-colorado', 'Aurora', 'CO')
_s('denver-colorado', ['auto-transport-aurora-colorado','auto-transport-colorado-springs-colorado','auto-transport-salt-lake-city-utah','auto-transport-albuquerque-new-mexico','auto-transport-kansas-city-missouri','auto-transport-wichita-kansas'])
_s('colorado-springs-colorado', ['auto-transport-denver-colorado','auto-transport-aurora-colorado','auto-transport-albuquerque-new-mexico','auto-transport-salt-lake-city-utah','auto-transport-wichita-kansas','auto-transport-oklahoma-city-oklahoma'])
_s('aurora-colorado', ['auto-transport-denver-colorado','auto-transport-colorado-springs-colorado','auto-transport-salt-lake-city-utah','auto-transport-albuquerque-new-mexico','auto-transport-kansas-city-missouri','auto-transport-wichita-kansas'])
# neighbours pick up Denver (surgical edit on the live pages)
for _k in ['albuquerque-new-mexico','salt-lake-city-utah','kansas-city-missouri','wichita-kansas']:
    if _k in NEARBY and 'auto-transport-denver-colorado' not in NEARBY[_k]: NEARBY[_k].append('auto-transport-denver-colorado')

# ---- Batch 30 (Oct 2026): Columbus GA, Augusta GA, Macon, Savannah, Athens (Georgia beyond Atlanta) ----
#      NOTE: 'Augusta' and 'Columbus' now exist in two states; chips print "City, ST", and _s() needs the full slug.
register('auto-transport-columbus-georgia', 'Columbus', 'GA')
register('auto-transport-augusta-georgia', 'Augusta', 'GA')
register('auto-transport-macon-georgia', 'Macon', 'GA')
register('auto-transport-savannah-georgia', 'Savannah', 'GA')
register('auto-transport-athens-georgia', 'Athens', 'GA')
_s('columbus-georgia', ['auto-transport-atlanta-georgia','auto-transport-macon-georgia','auto-transport-augusta-georgia','auto-transport-savannah-georgia','auto-transport-tuscaloosa-alabama','auto-transport-tallahassee-florida'])
_s('augusta-georgia', ['auto-transport-atlanta-georgia','auto-transport-athens-georgia','auto-transport-savannah-georgia','auto-transport-macon-georgia','auto-transport-charlotte-north-carolina','auto-transport-columbus-georgia'])
_s('macon-georgia', ['auto-transport-atlanta-georgia','auto-transport-columbus-georgia','auto-transport-savannah-georgia','auto-transport-augusta-georgia','auto-transport-athens-georgia','auto-transport-jacksonville-florida'])
_s('savannah-georgia', ['auto-transport-jacksonville-florida','auto-transport-macon-georgia','auto-transport-augusta-georgia','auto-transport-atlanta-georgia','auto-transport-charlotte-north-carolina','auto-transport-daytona-beach-florida'])
_s('athens-georgia', ['auto-transport-atlanta-georgia','auto-transport-augusta-georgia','auto-transport-macon-georgia','auto-transport-charlotte-north-carolina','auto-transport-savannah-georgia','auto-transport-columbus-georgia'])
# Atlanta's chips re-cut around the new in-state pages (Louisville and Mobile dropped as the farthest)
NEARBY['atlanta-georgia'] = ['auto-transport-athens-georgia','auto-transport-macon-georgia','auto-transport-augusta-georgia','auto-transport-columbus-georgia','auto-transport-charlotte-north-carolina','auto-transport-tuscaloosa-alabama','auto-transport-jacksonville-florida','auto-transport-orlando-florida']
for _k, _vs in {'jacksonville-florida':['auto-transport-savannah-georgia'],
               'tallahassee-florida':['auto-transport-columbus-georgia'],
               'charlotte-north-carolina':['auto-transport-augusta-georgia'],
               'tuscaloosa-alabama':['auto-transport-columbus-georgia']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 31 (Oct 2026): Huntsville, Montgomery (AL); Mesa, Chandler, Glendale (AZ) ----
#      NOTE: the three Arizona numbers are 928 (northern/western AZ code), used exactly as supplied.
register('auto-transport-huntsville-alabama', 'Huntsville', 'AL')
register('auto-transport-montgomery-alabama', 'Montgomery', 'AL')
register('auto-transport-mesa-arizona', 'Mesa', 'AZ')
register('auto-transport-chandler-arizona', 'Chandler', 'AZ')
register('auto-transport-glendale-arizona', 'Glendale', 'AZ')
_s('huntsville-alabama', ['auto-transport-tuscaloosa-alabama','auto-transport-montgomery-alabama','auto-transport-atlanta-georgia','auto-transport-louisville-kentucky','auto-transport-lexington-kentucky','auto-transport-mobile-alabama'])
_s('montgomery-alabama', ['auto-transport-tuscaloosa-alabama','auto-transport-mobile-alabama','auto-transport-huntsville-alabama','auto-transport-atlanta-georgia','auto-transport-columbus-georgia','auto-transport-tallahassee-florida'])
_s('mesa-arizona', ['auto-transport-phoenix-arizona','auto-transport-gilbert-arizona','auto-transport-chandler-arizona','auto-transport-glendale-arizona','auto-transport-tucson-arizona','auto-transport-las-vegas-nevada'])
_s('chandler-arizona', ['auto-transport-gilbert-arizona','auto-transport-mesa-arizona','auto-transport-phoenix-arizona','auto-transport-glendale-arizona','auto-transport-tucson-arizona','auto-transport-san-diego-california'])
_s('glendale-arizona', ['auto-transport-phoenix-arizona','auto-transport-mesa-arizona','auto-transport-chandler-arizona','auto-transport-gilbert-arizona','auto-transport-tucson-arizona','auto-transport-las-vegas-nevada'])
# Phoenix re-cut around the metro pages (Henderson dropped; Las Vegas kept)
NEARBY['phoenix-arizona'] = ['auto-transport-mesa-arizona','auto-transport-chandler-arizona','auto-transport-glendale-arizona','auto-transport-gilbert-arizona','auto-transport-tucson-arizona','auto-transport-las-vegas-nevada','auto-transport-albuquerque-new-mexico','auto-transport-san-diego-california']
for _k, _vs in {'tuscaloosa-alabama':['auto-transport-huntsville-alabama','auto-transport-montgomery-alabama'],
               'mobile-alabama':['auto-transport-montgomery-alabama'],
               'gilbert-arizona':['auto-transport-mesa-arizona','auto-transport-chandler-arizona','auto-transport-glendale-arizona'],
               'tucson-arizona':['auto-transport-mesa-arizona','auto-transport-chandler-arizona']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 32 (Oct 2026): Hilo, Kahului (HI); Boise, Meridian, Nampa (ID) ----
register('auto-transport-hilo-hawaii', 'Hilo', 'HI')
register('auto-transport-kahului-hawaii', 'Kahului', 'HI')
register('auto-transport-boise-idaho', 'Boise', 'ID')
register('auto-transport-meridian-idaho', 'Meridian', 'ID')
register('auto-transport-nampa-idaho', 'Nampa', 'ID')
_s('hilo-hawaii', ['auto-transport-kahului-hawaii','auto-transport-honolulu-hawaii','auto-transport-long-beach-california','auto-transport-los-angeles-california','auto-transport-oakland-california','auto-transport-san-diego-california'])
_s('kahului-hawaii', ['auto-transport-hilo-hawaii','auto-transport-honolulu-hawaii','auto-transport-long-beach-california','auto-transport-los-angeles-california','auto-transport-oakland-california','auto-transport-san-diego-california'])
_s('boise-idaho', ['auto-transport-meridian-idaho','auto-transport-nampa-idaho','auto-transport-salt-lake-city-utah','auto-transport-portland-oregon','auto-transport-west-valley-city-utah','auto-transport-sacramento-california'])
_s('meridian-idaho', ['auto-transport-boise-idaho','auto-transport-nampa-idaho','auto-transport-salt-lake-city-utah','auto-transport-portland-oregon','auto-transport-west-jordan-utah','auto-transport-provo-utah'])
_s('nampa-idaho', ['auto-transport-meridian-idaho','auto-transport-boise-idaho','auto-transport-salt-lake-city-utah','auto-transport-portland-oregon','auto-transport-west-valley-city-utah','auto-transport-sacramento-california'])
# Honolulu gains the two neighbor-island pages; Salt Lake City re-cut (Henderson and Sacramento dropped) so Boise fits
NEARBY['honolulu-hawaii'] = ['auto-transport-hilo-hawaii','auto-transport-kahului-hawaii','auto-transport-long-beach-california','auto-transport-los-angeles-california','auto-transport-oakland-california','auto-transport-anchorage-alaska']
NEARBY['salt-lake-city-utah'] = ['auto-transport-provo-utah','auto-transport-west-jordan-utah','auto-transport-west-valley-city-utah','auto-transport-boise-idaho','auto-transport-denver-colorado','auto-transport-las-vegas-nevada','auto-transport-phoenix-arizona','auto-transport-portland-oregon']
if 'auto-transport-boise-idaho' not in NEARBY['portland-oregon']: NEARBY['portland-oregon'].append('auto-transport-boise-idaho')

# ---- Batch 33 (Oct 26, 2026): Fort Wayne, Evansville (IN); Kapaʻa / Kauai (HI); Aurora, Joliet (IL) ----
#      NOTE: 'Aurora' now exists in IL and CO; chips print "Aurora, IL" / "Aurora, CO".
register('auto-transport-fort-wayne-indiana', 'Fort Wayne', 'IN')
register('auto-transport-evansville-indiana', 'Evansville', 'IN')
register('auto-transport-kapaa-hawaii', 'Kapaʻa', 'HI')
register('auto-transport-aurora-illinois', 'Aurora', 'IL')
register('auto-transport-joliet-illinois', 'Joliet', 'IL')
_s('fort-wayne-indiana', ['auto-transport-indianapolis-indiana','auto-transport-dayton-ohio','auto-transport-detroit-michigan','auto-transport-columbus-ohio','auto-transport-chicago-illinois','auto-transport-cincinnati-ohio'])
_s('evansville-indiana', ['auto-transport-louisville-kentucky','auto-transport-st-louis-missouri','auto-transport-indianapolis-indiana','auto-transport-lexington-kentucky','auto-transport-cincinnati-ohio','auto-transport-chicago-illinois'])
_s('kapaa-hawaii', ['auto-transport-honolulu-hawaii','auto-transport-kahului-hawaii','auto-transport-hilo-hawaii','auto-transport-long-beach-california','auto-transport-los-angeles-california','auto-transport-oakland-california'])
_s('aurora-illinois', ['auto-transport-chicago-illinois','auto-transport-joliet-illinois','auto-transport-kenosha-wisconsin','auto-transport-milwaukee-wisconsin','auto-transport-madison-wisconsin','auto-transport-indianapolis-indiana'])
_s('joliet-illinois', ['auto-transport-chicago-illinois','auto-transport-aurora-illinois','auto-transport-kenosha-wisconsin','auto-transport-indianapolis-indiana','auto-transport-milwaukee-wisconsin','auto-transport-st-louis-missouri'])
# re-cuts so the in-state pages lead (Cleveland dropped from Indianapolis; Wichita and Louisville dropped from Chicago)
NEARBY['indianapolis-indiana'] = ['auto-transport-fort-wayne-indiana','auto-transport-evansville-indiana','auto-transport-chicago-illinois','auto-transport-louisville-kentucky','auto-transport-cincinnati-ohio','auto-transport-dayton-ohio','auto-transport-lexington-kentucky','auto-transport-st-louis-missouri']
NEARBY['chicago-illinois'] = ['auto-transport-aurora-illinois','auto-transport-joliet-illinois','auto-transport-milwaukee-wisconsin','auto-transport-kenosha-wisconsin','auto-transport-indianapolis-indiana','auto-transport-detroit-michigan','auto-transport-st-louis-missouri','auto-transport-cleveland-ohio']
for _k, _vs in {'louisville-kentucky':['auto-transport-evansville-indiana'], 'st-louis-missouri':['auto-transport-evansville-indiana'],
               'dayton-ohio':['auto-transport-fort-wayne-indiana'], 'detroit-michigan':['auto-transport-fort-wayne-indiana'],
               'kenosha-wisconsin':['auto-transport-aurora-illinois'],
               'honolulu-hawaii':['auto-transport-kapaa-hawaii'], 'hilo-hawaii':['auto-transport-kapaa-hawaii'], 'kahului-hawaii':['auto-transport-kapaa-hawaii']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 34 (Oct 26, 2026): Rockford, Springfield, Champaign, Waukegan (IL) ----
#      NOTE: 'Springfield' now exists in MA, MO and IL; chips print the state.
register('auto-transport-rockford-illinois', 'Rockford', 'IL')
register('auto-transport-springfield-illinois', 'Springfield', 'IL')
register('auto-transport-champaign-illinois', 'Champaign', 'IL')
register('auto-transport-waukegan-illinois', 'Waukegan', 'IL')
_s('rockford-illinois', ['auto-transport-chicago-illinois','auto-transport-madison-wisconsin','auto-transport-milwaukee-wisconsin','auto-transport-aurora-illinois','auto-transport-kenosha-wisconsin','auto-transport-waukegan-illinois'])
_s('springfield-illinois', ['auto-transport-st-louis-missouri','auto-transport-champaign-illinois','auto-transport-chicago-illinois','auto-transport-indianapolis-indiana','auto-transport-columbia-missouri','auto-transport-kansas-city-missouri'])
_s('champaign-illinois', ['auto-transport-springfield-illinois','auto-transport-indianapolis-indiana','auto-transport-chicago-illinois','auto-transport-st-louis-missouri','auto-transport-joliet-illinois','auto-transport-louisville-kentucky'])
_s('waukegan-illinois', ['auto-transport-kenosha-wisconsin','auto-transport-chicago-illinois','auto-transport-milwaukee-wisconsin','auto-transport-madison-wisconsin','auto-transport-aurora-illinois','auto-transport-rockford-illinois'])
# re-cuts: Chicago leads with its own collar pages; St. Louis swaps Little Rock for Springfield IL
NEARBY['chicago-illinois'] = ['auto-transport-aurora-illinois','auto-transport-joliet-illinois','auto-transport-waukegan-illinois','auto-transport-rockford-illinois','auto-transport-milwaukee-wisconsin','auto-transport-kenosha-wisconsin','auto-transport-indianapolis-indiana','auto-transport-st-louis-missouri']
NEARBY['st-louis-missouri'] = ['auto-transport-columbia-missouri','auto-transport-kansas-city-missouri','auto-transport-springfield-missouri','auto-transport-springfield-illinois','auto-transport-chicago-illinois','auto-transport-indianapolis-indiana','auto-transport-louisville-kentucky','auto-transport-evansville-indiana']
for _k, _vs in {'kenosha-wisconsin':['auto-transport-waukegan-illinois'], 'milwaukee-wisconsin':['auto-transport-waukegan-illinois'],
               'madison-wisconsin':['auto-transport-rockford-illinois'],
               'aurora-illinois':['auto-transport-rockford-illinois','auto-transport-waukegan-illinois'],
               'joliet-illinois':['auto-transport-champaign-illinois']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 35 (Oct 26, 2026): Overland Park, Olathe, Topeka (KS); Owensboro (KY) ----
register('auto-transport-overland-park-kansas', 'Overland Park', 'KS')
register('auto-transport-olathe-kansas', 'Olathe', 'KS')
register('auto-transport-topeka-kansas', 'Topeka', 'KS')
register('auto-transport-owensboro-kentucky', 'Owensboro', 'KY')
_s('overland-park-kansas', ['auto-transport-kansas-city-missouri','auto-transport-olathe-kansas','auto-transport-lees-summit-missouri','auto-transport-independence-missouri','auto-transport-topeka-kansas','auto-transport-wichita-kansas'])
_s('olathe-kansas', ['auto-transport-overland-park-kansas','auto-transport-kansas-city-missouri','auto-transport-lees-summit-missouri','auto-transport-topeka-kansas','auto-transport-independence-missouri','auto-transport-wichita-kansas'])
_s('topeka-kansas', ['auto-transport-kansas-city-missouri','auto-transport-overland-park-kansas','auto-transport-olathe-kansas','auto-transport-wichita-kansas','auto-transport-independence-missouri','auto-transport-columbia-missouri'])
_s('owensboro-kentucky', ['auto-transport-evansville-indiana','auto-transport-louisville-kentucky','auto-transport-lexington-kentucky','auto-transport-indianapolis-indiana','auto-transport-st-louis-missouri','auto-transport-cincinnati-ohio'])
# re-cuts so the metro pages lead
NEARBY['kansas-city-missouri'] = ['auto-transport-overland-park-kansas','auto-transport-olathe-kansas','auto-transport-independence-missouri','auto-transport-lees-summit-missouri','auto-transport-topeka-kansas','auto-transport-columbia-missouri','auto-transport-st-louis-missouri','auto-transport-wichita-kansas']
NEARBY['wichita-kansas'] = ['auto-transport-oklahoma-city-oklahoma','auto-transport-kansas-city-missouri','auto-transport-overland-park-kansas','auto-transport-topeka-kansas','auto-transport-tulsa-oklahoma','auto-transport-dallas-texas','auto-transport-denver-colorado','auto-transport-albuquerque-new-mexico']
NEARBY['louisville-kentucky'] = ['auto-transport-lexington-kentucky','auto-transport-evansville-indiana','auto-transport-owensboro-kentucky','auto-transport-indianapolis-indiana','auto-transport-cincinnati-ohio','auto-transport-st-louis-missouri','auto-transport-chicago-illinois','auto-transport-atlanta-georgia']
for _k, _vs in {'independence-missouri':['auto-transport-overland-park-kansas'], 'lees-summit-missouri':['auto-transport-olathe-kansas','auto-transport-overland-park-kansas'],
               'columbia-missouri':['auto-transport-topeka-kansas'], 'evansville-indiana':['auto-transport-owensboro-kentucky'], 'lexington-kentucky':['auto-transport-owensboro-kentucky']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 36 (Oct 26, 2026): Baton Rouge, Shreveport, Metairie (LA) ----
register('auto-transport-baton-rouge-louisiana', 'Baton Rouge', 'LA')
register('auto-transport-shreveport-louisiana', 'Shreveport', 'LA')
register('auto-transport-metairie-louisiana', 'Metairie', 'LA')
_s('baton-rouge-louisiana', ['auto-transport-new-orleans-louisiana','auto-transport-metairie-louisiana','auto-transport-houston-texas','auto-transport-mobile-alabama','auto-transport-shreveport-louisiana','auto-transport-dallas-texas'])
_s('shreveport-louisiana', ['auto-transport-dallas-texas','auto-transport-fort-worth-texas','auto-transport-little-rock-arkansas','auto-transport-baton-rouge-louisiana','auto-transport-houston-texas','auto-transport-new-orleans-louisiana'])
_s('metairie-louisiana', ['auto-transport-new-orleans-louisiana','auto-transport-baton-rouge-louisiana','auto-transport-mobile-alabama','auto-transport-houston-texas','auto-transport-shreveport-louisiana','auto-transport-atlanta-georgia'])
NEARBY['new-orleans-louisiana'] = ['auto-transport-metairie-louisiana','auto-transport-baton-rouge-louisiana','auto-transport-mobile-alabama','auto-transport-houston-texas','auto-transport-shreveport-louisiana','auto-transport-atlanta-georgia','auto-transport-tuscaloosa-alabama']
for _k, _vs in {'houston-texas':['auto-transport-baton-rouge-louisiana'], 'dallas-texas':['auto-transport-shreveport-louisiana'],
               'fort-worth-texas':['auto-transport-shreveport-louisiana'], 'little-rock-arkansas':['auto-transport-shreveport-louisiana'],
               'mobile-alabama':['auto-transport-baton-rouge-louisiana']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 37 (Oct 26, 2026): Portland, Lewiston, Bangor (ME) ----
#      NOTE: 'Portland' now exists in OR and ME; chips print the state.
register('auto-transport-portland-maine', 'Portland', 'ME')
register('auto-transport-lewiston-maine', 'Lewiston', 'ME')
register('auto-transport-bangor-maine', 'Bangor', 'ME')
_s('portland-maine', ['auto-transport-augusta-maine','auto-transport-lewiston-maine','auto-transport-bangor-maine','auto-transport-boston-massachusetts','auto-transport-worcester-massachusetts','auto-transport-hartford-connecticut'])
_s('lewiston-maine', ['auto-transport-portland-maine','auto-transport-augusta-maine','auto-transport-bangor-maine','auto-transport-boston-massachusetts','auto-transport-worcester-massachusetts','auto-transport-hartford-connecticut'])
_s('bangor-maine', ['auto-transport-augusta-maine','auto-transport-portland-maine','auto-transport-lewiston-maine','auto-transport-boston-massachusetts','auto-transport-worcester-massachusetts','auto-transport-hartford-connecticut'])
NEARBY['augusta-maine'] = ['auto-transport-portland-maine','auto-transport-lewiston-maine','auto-transport-bangor-maine','auto-transport-boston-massachusetts','auto-transport-manhattan-new-york','auto-transport-philadelphia-pennsylvania','auto-transport-baltimore-maryland']
NEARBY['boston-massachusetts'] = ['auto-transport-worcester-massachusetts','auto-transport-portland-maine','auto-transport-manhattan-new-york','auto-transport-hartford-connecticut','auto-transport-albany-new-york','auto-transport-philadelphia-pennsylvania','auto-transport-augusta-maine','auto-transport-baltimore-maryland']
for _k, _vs in {'worcester-massachusetts':['auto-transport-portland-maine']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 38 (Oct 26, 2026): Tempe, Surprise (AZ) ----
register('auto-transport-tempe-arizona', 'Tempe', 'AZ')
register('auto-transport-surprise-arizona', 'Surprise', 'AZ')
_s('tempe-arizona', ['auto-transport-phoenix-arizona','auto-transport-mesa-arizona','auto-transport-chandler-arizona','auto-transport-gilbert-arizona','auto-transport-glendale-arizona','auto-transport-tucson-arizona'])
_s('surprise-arizona', ['auto-transport-glendale-arizona','auto-transport-phoenix-arizona','auto-transport-tempe-arizona','auto-transport-mesa-arizona','auto-transport-las-vegas-nevada','auto-transport-tucson-arizona'])
NEARBY['phoenix-arizona'] = ['auto-transport-tempe-arizona','auto-transport-mesa-arizona','auto-transport-chandler-arizona','auto-transport-glendale-arizona','auto-transport-gilbert-arizona','auto-transport-surprise-arizona','auto-transport-tucson-arizona','auto-transport-las-vegas-nevada']
NEARBY['gilbert-arizona'] = ['auto-transport-phoenix-arizona','auto-transport-tempe-arizona','auto-transport-mesa-arizona','auto-transport-chandler-arizona','auto-transport-glendale-arizona','auto-transport-tucson-arizona','auto-transport-henderson-nevada','auto-transport-las-vegas-nevada']
for _k, _vs in {'mesa-arizona':['auto-transport-tempe-arizona'], 'chandler-arizona':['auto-transport-tempe-arizona'],
               'glendale-arizona':['auto-transport-surprise-arizona'], 'tucson-arizona':['auto-transport-tempe-arizona']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 39 (Oct 26, 2026): Grand Rapids, Warren (MI); Davenport, Sioux City, Ankeny (IA); Columbia, Germantown (MD) ----
#      NOTE: 'Columbia' now exists in MO and MD; chips print the state.
register('auto-transport-grand-rapids-michigan', 'Grand Rapids', 'MI')
register('auto-transport-warren-michigan', 'Warren', 'MI')
register('auto-transport-davenport-iowa', 'Davenport', 'IA')
register('auto-transport-sioux-city-iowa', 'Sioux City', 'IA')
register('auto-transport-ankeny-iowa', 'Ankeny', 'IA')
register('auto-transport-columbia-maryland', 'Columbia', 'MD')
register('auto-transport-germantown-maryland', 'Germantown', 'MD')
_s('grand-rapids-michigan', ['auto-transport-detroit-michigan','auto-transport-warren-michigan','auto-transport-chicago-illinois','auto-transport-milwaukee-wisconsin','auto-transport-fort-wayne-indiana','auto-transport-indianapolis-indiana'])
_s('warren-michigan', ['auto-transport-detroit-michigan','auto-transport-grand-rapids-michigan','auto-transport-cleveland-ohio','auto-transport-fort-wayne-indiana','auto-transport-columbus-ohio','auto-transport-chicago-illinois'])
_s('davenport-iowa', ['auto-transport-ankeny-iowa','auto-transport-chicago-illinois','auto-transport-rockford-illinois','auto-transport-madison-wisconsin','auto-transport-milwaukee-wisconsin','auto-transport-st-louis-missouri'])
_s('sioux-city-iowa', ['auto-transport-ankeny-iowa','auto-transport-davenport-iowa','auto-transport-kansas-city-missouri','auto-transport-overland-park-kansas','auto-transport-denver-colorado','auto-transport-chicago-illinois'])
_s('ankeny-iowa', ['auto-transport-davenport-iowa','auto-transport-sioux-city-iowa','auto-transport-kansas-city-missouri','auto-transport-chicago-illinois','auto-transport-st-louis-missouri','auto-transport-madison-wisconsin'])
_s('columbia-maryland', ['auto-transport-baltimore-maryland','auto-transport-germantown-maryland','auto-transport-wilmington-delaware','auto-transport-dover-delaware','auto-transport-philadelphia-pennsylvania','auto-transport-manhattan-new-york'])
_s('germantown-maryland', ['auto-transport-columbia-maryland','auto-transport-baltimore-maryland','auto-transport-wilmington-delaware','auto-transport-philadelphia-pennsylvania','auto-transport-dover-delaware','auto-transport-manhattan-new-york'])
NEARBY['detroit-michigan'] = ['auto-transport-warren-michigan','auto-transport-grand-rapids-michigan','auto-transport-cleveland-ohio','auto-transport-chicago-illinois','auto-transport-fort-wayne-indiana','auto-transport-columbus-ohio','auto-transport-indianapolis-indiana','auto-transport-milwaukee-wisconsin']
NEARBY['baltimore-maryland'] = ['auto-transport-columbia-maryland','auto-transport-germantown-maryland','auto-transport-philadelphia-pennsylvania','auto-transport-wilmington-delaware','auto-transport-dover-delaware','auto-transport-manhattan-new-york','auto-transport-boston-massachusetts','auto-transport-charlotte-north-carolina']
NEARBY['milwaukee-wisconsin'] = ['auto-transport-madison-wisconsin','auto-transport-kenosha-wisconsin','auto-transport-green-bay-wisconsin','auto-transport-chicago-illinois','auto-transport-waukegan-illinois','auto-transport-grand-rapids-michigan','auto-transport-detroit-michigan','auto-transport-indianapolis-indiana']
for _k, _vs in {'fort-wayne-indiana':['auto-transport-grand-rapids-michigan'], 'wilmington-delaware':['auto-transport-columbia-maryland'],
               'dover-delaware':['auto-transport-columbia-maryland'], 'madison-wisconsin':['auto-transport-davenport-iowa'], 'rockford-illinois':['auto-transport-davenport-iowa']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 40 (Oct 27, 2026): South Bend (IN); Lawrence (KS); Lafayette (LA); Ann Arbor (MI); Seattle, Spokane (WA) ----
#      NOTE: Seattle and Spokane are Washington's first city pages (the Washington page gets its first City Pages block).
register('auto-transport-south-bend-indiana', 'South Bend', 'IN')
register('auto-transport-lawrence-kansas', 'Lawrence', 'KS')
register('auto-transport-lafayette-louisiana', 'Lafayette', 'LA')
register('auto-transport-ann-arbor-michigan', 'Ann Arbor', 'MI')
register('auto-transport-seattle-washington', 'Seattle', 'WA')
register('auto-transport-spokane-washington', 'Spokane', 'WA')
_s('south-bend-indiana', ['auto-transport-fort-wayne-indiana','auto-transport-chicago-illinois','auto-transport-indianapolis-indiana','auto-transport-grand-rapids-michigan','auto-transport-joliet-illinois','auto-transport-detroit-michigan'])
_s('lawrence-kansas', ['auto-transport-topeka-kansas','auto-transport-kansas-city-missouri','auto-transport-overland-park-kansas','auto-transport-olathe-kansas','auto-transport-wichita-kansas','auto-transport-lees-summit-missouri'])
_s('lafayette-louisiana', ['auto-transport-baton-rouge-louisiana','auto-transport-new-orleans-louisiana','auto-transport-metairie-louisiana','auto-transport-houston-texas','auto-transport-shreveport-louisiana','auto-transport-dallas-texas'])
_s('ann-arbor-michigan', ['auto-transport-detroit-michigan','auto-transport-warren-michigan','auto-transport-grand-rapids-michigan','auto-transport-fort-wayne-indiana','auto-transport-cleveland-ohio','auto-transport-chicago-illinois'])
_s('seattle-washington', ['auto-transport-spokane-washington','auto-transport-portland-oregon','auto-transport-boise-idaho','auto-transport-anchorage-alaska','auto-transport-sacramento-california','auto-transport-san-francisco-california'])
_s('spokane-washington', ['auto-transport-seattle-washington','auto-transport-boise-idaho','auto-transport-portland-oregon','auto-transport-meridian-idaho','auto-transport-nampa-idaho','auto-transport-salt-lake-city-utah'])
NEARBY['detroit-michigan'] = ['auto-transport-warren-michigan','auto-transport-ann-arbor-michigan','auto-transport-grand-rapids-michigan','auto-transport-cleveland-ohio','auto-transport-chicago-illinois','auto-transport-fort-wayne-indiana','auto-transport-columbus-ohio','auto-transport-indianapolis-indiana']
NEARBY['indianapolis-indiana'] = ['auto-transport-fort-wayne-indiana','auto-transport-evansville-indiana','auto-transport-south-bend-indiana','auto-transport-chicago-illinois','auto-transport-louisville-kentucky','auto-transport-cincinnati-ohio','auto-transport-dayton-ohio','auto-transport-lexington-kentucky']
NEARBY['chicago-illinois'] = ['auto-transport-aurora-illinois','auto-transport-joliet-illinois','auto-transport-waukegan-illinois','auto-transport-rockford-illinois','auto-transport-milwaukee-wisconsin','auto-transport-kenosha-wisconsin','auto-transport-south-bend-indiana','auto-transport-indianapolis-indiana']
NEARBY['kansas-city-missouri'] = ['auto-transport-overland-park-kansas','auto-transport-olathe-kansas','auto-transport-lawrence-kansas','auto-transport-independence-missouri','auto-transport-lees-summit-missouri','auto-transport-topeka-kansas','auto-transport-columbia-missouri','auto-transport-wichita-kansas']
NEARBY['portland-oregon'] = ['auto-transport-seattle-washington','auto-transport-spokane-washington','auto-transport-sacramento-california','auto-transport-san-francisco-california','auto-transport-oakland-california','auto-transport-salt-lake-city-utah','auto-transport-boise-idaho','auto-transport-anchorage-alaska']
NEARBY['boise-idaho'] = ['auto-transport-meridian-idaho','auto-transport-nampa-idaho','auto-transport-salt-lake-city-utah','auto-transport-portland-oregon','auto-transport-spokane-washington','auto-transport-seattle-washington','auto-transport-west-valley-city-utah','auto-transport-sacramento-california']
for _k, _vs in {'warren-michigan':['auto-transport-ann-arbor-michigan'], 'grand-rapids-michigan':['auto-transport-ann-arbor-michigan'],
               'fort-wayne-indiana':['auto-transport-south-bend-indiana'],
               'topeka-kansas':['auto-transport-lawrence-kansas'], 'overland-park-kansas':['auto-transport-lawrence-kansas'], 'olathe-kansas':['auto-transport-lawrence-kansas'],
               'baton-rouge-louisiana':['auto-transport-lafayette-louisiana'], 'new-orleans-louisiana':['auto-transport-lafayette-louisiana'],
               'metairie-louisiana':['auto-transport-lafayette-louisiana'], 'shreveport-louisiana':['auto-transport-lafayette-louisiana'],
               'meridian-idaho':['auto-transport-spokane-washington'], 'nampa-idaho':['auto-transport-spokane-washington'],
               'anchorage-alaska':['auto-transport-seattle-washington']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 41 (Oct 27, 2026): Virginia Beach (VA); Pittsburgh, Allentown, Reading (PA) ----
#      NOTE: Virginia Beach is Virginia's first city page (the Virginia page gets its first City Pages block).
register('auto-transport-virginia-beach-virginia', 'Virginia Beach', 'VA')
register('auto-transport-pittsburgh-pennsylvania', 'Pittsburgh', 'PA')
register('auto-transport-allentown-pennsylvania', 'Allentown', 'PA')
register('auto-transport-reading-pennsylvania', 'Reading', 'PA')
_s('virginia-beach-virginia', ['auto-transport-raleigh-north-carolina','auto-transport-durham-north-carolina','auto-transport-baltimore-maryland','auto-transport-columbia-maryland','auto-transport-charlotte-north-carolina','auto-transport-philadelphia-pennsylvania'])
_s('pittsburgh-pennsylvania', ['auto-transport-philadelphia-pennsylvania','auto-transport-cleveland-ohio','auto-transport-akron-ohio','auto-transport-columbus-ohio','auto-transport-buffalo-new-york','auto-transport-baltimore-maryland'])
_s('allentown-pennsylvania', ['auto-transport-philadelphia-pennsylvania','auto-transport-reading-pennsylvania','auto-transport-pittsburgh-pennsylvania','auto-transport-manhattan-new-york','auto-transport-wilmington-delaware','auto-transport-bridgeport-connecticut'])
_s('reading-pennsylvania', ['auto-transport-philadelphia-pennsylvania','auto-transport-allentown-pennsylvania','auto-transport-wilmington-delaware','auto-transport-baltimore-maryland','auto-transport-pittsburgh-pennsylvania','auto-transport-dover-delaware'])
NEARBY['philadelphia-pennsylvania'] = ['auto-transport-pittsburgh-pennsylvania','auto-transport-allentown-pennsylvania','auto-transport-reading-pennsylvania','auto-transport-manhattan-new-york','auto-transport-baltimore-maryland','auto-transport-wilmington-delaware','auto-transport-staten-island-new-york','auto-transport-boston-massachusetts']
NEARBY['baltimore-maryland'] = ['auto-transport-columbia-maryland','auto-transport-germantown-maryland','auto-transport-philadelphia-pennsylvania','auto-transport-wilmington-delaware','auto-transport-dover-delaware','auto-transport-virginia-beach-virginia','auto-transport-manhattan-new-york','auto-transport-charlotte-north-carolina']
NEARBY['wilmington-delaware'] = ['auto-transport-philadelphia-pennsylvania','auto-transport-dover-delaware','auto-transport-baltimore-maryland','auto-transport-allentown-pennsylvania','auto-transport-reading-pennsylvania','auto-transport-columbia-maryland','auto-transport-staten-island-new-york','auto-transport-manhattan-new-york']
for _k, _vs in {'cleveland-ohio':['auto-transport-pittsburgh-pennsylvania'], 'akron-ohio':['auto-transport-pittsburgh-pennsylvania'], 'columbus-ohio':['auto-transport-pittsburgh-pennsylvania'],
               'buffalo-new-york':['auto-transport-pittsburgh-pennsylvania'],
               'dover-delaware':['auto-transport-reading-pennsylvania'], 'raleigh-north-carolina':['auto-transport-virginia-beach-virginia'], 'durham-north-carolina':['auto-transport-virginia-beach-virginia'],
               'charlotte-north-carolina':['auto-transport-virginia-beach-virginia'], 'columbia-maryland':['auto-transport-virginia-beach-virginia'], 'bridgeport-connecticut':['auto-transport-allentown-pennsylvania']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 42 (Nov 2, 2026): Lansing (MI); Vancouver (WA); Chesapeake, Richmond (VA); Erie (PA); Cranston (RI) ----
#      NOTE: Cranston is Rhode Island's first city page (the Rhode Island page gets its first City Pages block).
register('auto-transport-lansing-michigan', 'Lansing', 'MI')
register('auto-transport-vancouver-washington', 'Vancouver', 'WA')
register('auto-transport-chesapeake-virginia', 'Chesapeake', 'VA')
register('auto-transport-richmond-virginia', 'Richmond', 'VA')
register('auto-transport-erie-pennsylvania', 'Erie', 'PA')
register('auto-transport-cranston-rhode-island', 'Cranston', 'RI')
_s('lansing-michigan', ['auto-transport-grand-rapids-michigan','auto-transport-ann-arbor-michigan','auto-transport-detroit-michigan','auto-transport-warren-michigan','auto-transport-fort-wayne-indiana','auto-transport-south-bend-indiana','auto-transport-chicago-illinois'])
_s('vancouver-washington', ['auto-transport-portland-oregon','auto-transport-seattle-washington','auto-transport-spokane-washington','auto-transport-boise-idaho','auto-transport-sacramento-california','auto-transport-san-francisco-california'])
_s('chesapeake-virginia', ['auto-transport-virginia-beach-virginia','auto-transport-richmond-virginia','auto-transport-raleigh-north-carolina','auto-transport-durham-north-carolina','auto-transport-columbia-maryland','auto-transport-baltimore-maryland','auto-transport-charlotte-north-carolina'])
_s('richmond-virginia', ['auto-transport-virginia-beach-virginia','auto-transport-chesapeake-virginia','auto-transport-columbia-maryland','auto-transport-germantown-maryland','auto-transport-baltimore-maryland','auto-transport-raleigh-north-carolina','auto-transport-durham-north-carolina','auto-transport-charlotte-north-carolina'])
_s('erie-pennsylvania', ['auto-transport-pittsburgh-pennsylvania','auto-transport-buffalo-new-york','auto-transport-cleveland-ohio','auto-transport-akron-ohio','auto-transport-rochester-new-york','auto-transport-columbus-ohio'])
_s('cranston-rhode-island', ['auto-transport-boston-massachusetts','auto-transport-worcester-massachusetts','auto-transport-hartford-connecticut','auto-transport-new-haven-connecticut','auto-transport-springfield-massachusetts','auto-transport-manhattan-new-york','auto-transport-bridgeport-connecticut'])
NEARBY['detroit-michigan'] = ['auto-transport-warren-michigan','auto-transport-ann-arbor-michigan','auto-transport-grand-rapids-michigan','auto-transport-lansing-michigan','auto-transport-cleveland-ohio','auto-transport-chicago-illinois','auto-transport-fort-wayne-indiana','auto-transport-columbus-ohio']
NEARBY['grand-rapids-michigan'] = ['auto-transport-lansing-michigan','auto-transport-detroit-michigan','auto-transport-warren-michigan','auto-transport-ann-arbor-michigan','auto-transport-chicago-illinois','auto-transport-milwaukee-wisconsin','auto-transport-fort-wayne-indiana','auto-transport-indianapolis-indiana']
NEARBY['seattle-washington'] = ['auto-transport-spokane-washington','auto-transport-portland-oregon','auto-transport-vancouver-washington','auto-transport-boise-idaho','auto-transport-anchorage-alaska','auto-transport-sacramento-california','auto-transport-san-francisco-california']
NEARBY['portland-oregon'] = ['auto-transport-vancouver-washington','auto-transport-seattle-washington','auto-transport-spokane-washington','auto-transport-sacramento-california','auto-transport-san-francisco-california','auto-transport-oakland-california','auto-transport-salt-lake-city-utah','auto-transport-boise-idaho']
NEARBY['virginia-beach-virginia'] = ['auto-transport-chesapeake-virginia','auto-transport-richmond-virginia','auto-transport-raleigh-north-carolina','auto-transport-durham-north-carolina','auto-transport-baltimore-maryland','auto-transport-columbia-maryland','auto-transport-charlotte-north-carolina','auto-transport-philadelphia-pennsylvania']
NEARBY['boston-massachusetts'] = ['auto-transport-worcester-massachusetts','auto-transport-cranston-rhode-island','auto-transport-manhattan-new-york','auto-transport-hartford-connecticut','auto-transport-portland-maine','auto-transport-albany-new-york','auto-transport-philadelphia-pennsylvania','auto-transport-baltimore-maryland']
NEARBY['pittsburgh-pennsylvania'] = ['auto-transport-philadelphia-pennsylvania','auto-transport-erie-pennsylvania','auto-transport-cleveland-ohio','auto-transport-akron-ohio','auto-transport-columbus-ohio','auto-transport-buffalo-new-york','auto-transport-baltimore-maryland']
for _k, _vs in {'warren-michigan':['auto-transport-lansing-michigan'], 'ann-arbor-michigan':['auto-transport-lansing-michigan'], 'fort-wayne-indiana':['auto-transport-lansing-michigan'],
               'spokane-washington':['auto-transport-vancouver-washington'],
               'raleigh-north-carolina':['auto-transport-richmond-virginia'], 'durham-north-carolina':['auto-transport-richmond-virginia'], 'charlotte-north-carolina':['auto-transport-richmond-virginia'],
               'columbia-maryland':['auto-transport-richmond-virginia'], 'germantown-maryland':['auto-transport-richmond-virginia'], 'baltimore-maryland':['auto-transport-richmond-virginia'],
               'buffalo-new-york':['auto-transport-erie-pennsylvania'], 'cleveland-ohio':['auto-transport-erie-pennsylvania'], 'akron-ohio':['auto-transport-erie-pennsylvania'], 'rochester-new-york':['auto-transport-erie-pennsylvania'],
               'worcester-massachusetts':['auto-transport-cranston-rhode-island'], 'hartford-connecticut':['auto-transport-cranston-rhode-island'],
               'new-haven-connecticut':['auto-transport-cranston-rhode-island'], 'springfield-massachusetts':['auto-transport-cranston-rhode-island']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 43 (Nov 2, 2026): Warwick (RI); St. Paul (MN); Jackson (MS); Omaha (NE); Newark (NJ); Las Cruces (NM) ----
#      NOTE: St. Paul, Jackson, Omaha and Newark are their states' first city pages (first City Pages blocks on MN, MS, NE, NJ).
#      The row said "Saint Paul"; the slug and the display follow the St. Louis / St. Petersburg precedent ("St. Paul").
register('auto-transport-warwick-rhode-island', 'Warwick', 'RI')
register('auto-transport-st-paul-minnesota', 'St. Paul', 'MN')
register('auto-transport-jackson-mississippi', 'Jackson', 'MS')
register('auto-transport-omaha-nebraska', 'Omaha', 'NE')
register('auto-transport-newark-new-jersey', 'Newark', 'NJ')
register('auto-transport-las-cruces-new-mexico', 'Las Cruces', 'NM')
_s('warwick-rhode-island', ['auto-transport-cranston-rhode-island','auto-transport-boston-massachusetts','auto-transport-worcester-massachusetts','auto-transport-hartford-connecticut','auto-transport-new-haven-connecticut','auto-transport-springfield-massachusetts','auto-transport-manhattan-new-york'])
_s('st-paul-minnesota', ['auto-transport-madison-wisconsin','auto-transport-ankeny-iowa','auto-transport-sioux-city-iowa','auto-transport-milwaukee-wisconsin','auto-transport-green-bay-wisconsin','auto-transport-davenport-iowa','auto-transport-chicago-illinois','auto-transport-omaha-nebraska'])
_s('jackson-mississippi', ['auto-transport-new-orleans-louisiana','auto-transport-baton-rouge-louisiana','auto-transport-mobile-alabama','auto-transport-shreveport-louisiana','auto-transport-little-rock-arkansas','auto-transport-tuscaloosa-alabama','auto-transport-montgomery-alabama','auto-transport-metairie-louisiana'])
_s('omaha-nebraska', ['auto-transport-ankeny-iowa','auto-transport-sioux-city-iowa','auto-transport-kansas-city-missouri','auto-transport-davenport-iowa','auto-transport-st-paul-minnesota','auto-transport-topeka-kansas','auto-transport-denver-colorado','auto-transport-wichita-kansas'])
_s('newark-new-jersey', ['auto-transport-manhattan-new-york','auto-transport-staten-island-new-york','auto-transport-brooklyn-new-york','auto-transport-yonkers-new-york','auto-transport-philadelphia-pennsylvania','auto-transport-allentown-pennsylvania','auto-transport-stamford-connecticut','auto-transport-wilmington-delaware'])
_s('las-cruces-new-mexico', ['auto-transport-el-paso-texas','auto-transport-albuquerque-new-mexico','auto-transport-tucson-arizona','auto-transport-phoenix-arizona','auto-transport-denver-colorado','auto-transport-san-antonio-texas'])
NEARBY['cranston-rhode-island'] = ['auto-transport-warwick-rhode-island','auto-transport-boston-massachusetts','auto-transport-worcester-massachusetts','auto-transport-hartford-connecticut','auto-transport-new-haven-connecticut','auto-transport-springfield-massachusetts','auto-transport-manhattan-new-york']
NEARBY['el-paso-texas'] = ['auto-transport-las-cruces-new-mexico','auto-transport-albuquerque-new-mexico','auto-transport-tucson-arizona','auto-transport-san-antonio-texas','auto-transport-austin-texas','auto-transport-phoenix-arizona']
NEARBY['albuquerque-new-mexico'] = ['auto-transport-las-cruces-new-mexico','auto-transport-el-paso-texas','auto-transport-phoenix-arizona','auto-transport-tucson-arizona','auto-transport-denver-colorado','auto-transport-oklahoma-city-oklahoma','auto-transport-salt-lake-city-utah']
NEARBY['manhattan-new-york'] = ['auto-transport-brooklyn-new-york','auto-transport-queens-new-york','auto-transport-bronx-new-york','auto-transport-newark-new-jersey','auto-transport-yonkers-new-york','auto-transport-staten-island-new-york','auto-transport-philadelphia-pennsylvania','auto-transport-boston-massachusetts']
NEARBY['staten-island-new-york'] = ['auto-transport-brooklyn-new-york','auto-transport-manhattan-new-york','auto-transport-newark-new-jersey','auto-transport-queens-new-york','auto-transport-bronx-new-york','auto-transport-philadelphia-pennsylvania','auto-transport-yonkers-new-york']
NEARBY['ankeny-iowa'] = ['auto-transport-davenport-iowa','auto-transport-sioux-city-iowa','auto-transport-omaha-nebraska','auto-transport-kansas-city-missouri','auto-transport-st-paul-minnesota','auto-transport-chicago-illinois','auto-transport-st-louis-missouri','auto-transport-madison-wisconsin']
NEARBY['sioux-city-iowa'] = ['auto-transport-omaha-nebraska','auto-transport-ankeny-iowa','auto-transport-st-paul-minnesota','auto-transport-davenport-iowa','auto-transport-kansas-city-missouri','auto-transport-overland-park-kansas','auto-transport-denver-colorado','auto-transport-chicago-illinois']
NEARBY['new-orleans-louisiana'] = ['auto-transport-metairie-louisiana','auto-transport-baton-rouge-louisiana','auto-transport-jackson-mississippi','auto-transport-mobile-alabama','auto-transport-houston-texas','auto-transport-shreveport-louisiana','auto-transport-lafayette-louisiana','auto-transport-atlanta-georgia']
NEARBY['davenport-iowa'] = ['auto-transport-ankeny-iowa','auto-transport-chicago-illinois','auto-transport-rockford-illinois','auto-transport-st-paul-minnesota','auto-transport-omaha-nebraska','auto-transport-madison-wisconsin','auto-transport-milwaukee-wisconsin','auto-transport-st-louis-missouri']
NEARBY['denver-colorado'] = ['auto-transport-aurora-colorado','auto-transport-colorado-springs-colorado','auto-transport-salt-lake-city-utah','auto-transport-albuquerque-new-mexico','auto-transport-las-cruces-new-mexico','auto-transport-kansas-city-missouri','auto-transport-omaha-nebraska','auto-transport-wichita-kansas']
NEARBY['kansas-city-missouri'] = ['auto-transport-overland-park-kansas','auto-transport-olathe-kansas','auto-transport-lawrence-kansas','auto-transport-independence-missouri','auto-transport-lees-summit-missouri','auto-transport-topeka-kansas','auto-transport-omaha-nebraska','auto-transport-columbia-missouri']
NEARBY['milwaukee-wisconsin'] = ['auto-transport-madison-wisconsin','auto-transport-kenosha-wisconsin','auto-transport-green-bay-wisconsin','auto-transport-chicago-illinois','auto-transport-waukegan-illinois','auto-transport-st-paul-minnesota','auto-transport-grand-rapids-michigan','auto-transport-detroit-michigan']
NEARBY['madison-wisconsin'] = ['auto-transport-milwaukee-wisconsin','auto-transport-green-bay-wisconsin','auto-transport-kenosha-wisconsin','auto-transport-chicago-illinois','auto-transport-st-paul-minnesota','auto-transport-rockford-illinois','auto-transport-davenport-iowa','auto-transport-indianapolis-indiana']
NEARBY['philadelphia-pennsylvania'] = ['auto-transport-pittsburgh-pennsylvania','auto-transport-allentown-pennsylvania','auto-transport-reading-pennsylvania','auto-transport-newark-new-jersey','auto-transport-manhattan-new-york','auto-transport-baltimore-maryland','auto-transport-wilmington-delaware','auto-transport-staten-island-new-york']
NEARBY['wilmington-delaware'] = ['auto-transport-philadelphia-pennsylvania','auto-transport-dover-delaware','auto-transport-baltimore-maryland','auto-transport-allentown-pennsylvania','auto-transport-reading-pennsylvania','auto-transport-newark-new-jersey','auto-transport-columbia-maryland','auto-transport-staten-island-new-york']
NEARBY['queens-new-york'] = ['auto-transport-manhattan-new-york','auto-transport-brooklyn-new-york','auto-transport-bronx-new-york','auto-transport-yonkers-new-york','auto-transport-staten-island-new-york','auto-transport-newark-new-jersey','auto-transport-boston-massachusetts','auto-transport-philadelphia-pennsylvania']
NEARBY['bronx-new-york'] = ['auto-transport-manhattan-new-york','auto-transport-yonkers-new-york','auto-transport-queens-new-york','auto-transport-brooklyn-new-york','auto-transport-newark-new-jersey','auto-transport-stamford-connecticut','auto-transport-boston-massachusetts','auto-transport-albany-new-york']
NEARBY['tucson-arizona'] = ['auto-transport-phoenix-arizona','auto-transport-gilbert-arizona','auto-transport-mesa-arizona','auto-transport-chandler-arizona','auto-transport-tempe-arizona','auto-transport-las-cruces-new-mexico','auto-transport-el-paso-texas','auto-transport-albuquerque-new-mexico']
NEARBY['phoenix-arizona'] = [x for x in NEARBY['phoenix-arizona'] if x != 'auto-transport-las-vegas-nevada'][:7] + ['auto-transport-las-cruces-new-mexico']
NEARBY['wichita-kansas'] = ['auto-transport-oklahoma-city-oklahoma','auto-transport-kansas-city-missouri','auto-transport-overland-park-kansas','auto-transport-topeka-kansas','auto-transport-tulsa-oklahoma','auto-transport-omaha-nebraska','auto-transport-dallas-texas','auto-transport-denver-colorado']
NEARBY['boston-massachusetts'] = ['auto-transport-worcester-massachusetts','auto-transport-cranston-rhode-island','auto-transport-warwick-rhode-island','auto-transport-manhattan-new-york','auto-transport-hartford-connecticut','auto-transport-portland-maine','auto-transport-albany-new-york','auto-transport-philadelphia-pennsylvania']
NEARBY['worcester-massachusetts'] = ['auto-transport-boston-massachusetts','auto-transport-cranston-rhode-island','auto-transport-warwick-rhode-island','auto-transport-springfield-massachusetts','auto-transport-hartford-connecticut','auto-transport-albany-new-york','auto-transport-new-haven-connecticut','auto-transport-manhattan-new-york']
NEARBY['yonkers-new-york'] = ['auto-transport-bronx-new-york','auto-transport-manhattan-new-york','auto-transport-queens-new-york','auto-transport-newark-new-jersey','auto-transport-stamford-connecticut','auto-transport-albany-new-york','auto-transport-boston-massachusetts','auto-transport-philadelphia-pennsylvania']
for _k, _vs in {'green-bay-wisconsin':['auto-transport-st-paul-minnesota'],
               'baton-rouge-louisiana':['auto-transport-jackson-mississippi'], 'mobile-alabama':['auto-transport-jackson-mississippi'], 'shreveport-louisiana':['auto-transport-jackson-mississippi'],
               'little-rock-arkansas':['auto-transport-jackson-mississippi'], 'tuscaloosa-alabama':['auto-transport-jackson-mississippi'], 'montgomery-alabama':['auto-transport-jackson-mississippi'], 'metairie-louisiana':['auto-transport-jackson-mississippi'],
               'topeka-kansas':['auto-transport-omaha-nebraska'],
               'brooklyn-new-york':['auto-transport-newark-new-jersey'], 'yonkers-new-york':['auto-transport-newark-new-jersey'], 'allentown-pennsylvania':['auto-transport-newark-new-jersey'], 'stamford-connecticut':['auto-transport-newark-new-jersey'],
               'san-antonio-texas':['auto-transport-las-cruces-new-mexico']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 44 (Nov 2, 2026): Missoula (MT); Greensboro (NC); Fargo (ND) ----
#      NOTE: Missoula and Fargo are their states' first city pages (first City Pages blocks on MT and ND; new hub blocks
#      Montana before Nebraska and North Dakota before Ohio). Pass-through markets: stats rows "3–6 Days" to match the state pages.
register('auto-transport-missoula-montana', 'Missoula', 'MT')
register('auto-transport-greensboro-north-carolina', 'Greensboro', 'NC')
register('auto-transport-fargo-north-dakota', 'Fargo', 'ND')
_s('missoula-montana', ['auto-transport-spokane-washington','auto-transport-seattle-washington','auto-transport-boise-idaho','auto-transport-meridian-idaho','auto-transport-nampa-idaho','auto-transport-salt-lake-city-utah','auto-transport-portland-oregon','auto-transport-fargo-north-dakota'])
_s('greensboro-north-carolina', ['auto-transport-durham-north-carolina','auto-transport-raleigh-north-carolina','auto-transport-charlotte-north-carolina','auto-transport-richmond-virginia','auto-transport-chesapeake-virginia','auto-transport-virginia-beach-virginia','auto-transport-atlanta-georgia','auto-transport-augusta-georgia'])
_s('fargo-north-dakota', ['auto-transport-st-paul-minnesota','auto-transport-sioux-city-iowa','auto-transport-omaha-nebraska','auto-transport-ankeny-iowa','auto-transport-green-bay-wisconsin','auto-transport-madison-wisconsin','auto-transport-milwaukee-wisconsin','auto-transport-missoula-montana'])
# explicit re-cuts (8 max)
NEARBY['boise-idaho'] = ['auto-transport-meridian-idaho','auto-transport-nampa-idaho','auto-transport-salt-lake-city-utah','auto-transport-portland-oregon','auto-transport-spokane-washington','auto-transport-seattle-washington','auto-transport-missoula-montana','auto-transport-west-valley-city-utah']
NEARBY['salt-lake-city-utah'] = ['auto-transport-provo-utah','auto-transport-west-jordan-utah','auto-transport-west-valley-city-utah','auto-transport-boise-idaho','auto-transport-denver-colorado','auto-transport-las-vegas-nevada','auto-transport-phoenix-arizona','auto-transport-missoula-montana']
NEARBY['richmond-virginia'] = ['auto-transport-virginia-beach-virginia','auto-transport-chesapeake-virginia','auto-transport-columbia-maryland','auto-transport-baltimore-maryland','auto-transport-raleigh-north-carolina','auto-transport-durham-north-carolina','auto-transport-greensboro-north-carolina','auto-transport-charlotte-north-carolina']
NEARBY['virginia-beach-virginia'] = ['auto-transport-chesapeake-virginia','auto-transport-richmond-virginia','auto-transport-raleigh-north-carolina','auto-transport-durham-north-carolina','auto-transport-baltimore-maryland','auto-transport-columbia-maryland','auto-transport-charlotte-north-carolina','auto-transport-greensboro-north-carolina']
NEARBY['st-paul-minnesota'] = ['auto-transport-fargo-north-dakota','auto-transport-madison-wisconsin','auto-transport-ankeny-iowa','auto-transport-sioux-city-iowa','auto-transport-milwaukee-wisconsin','auto-transport-green-bay-wisconsin','auto-transport-omaha-nebraska','auto-transport-chicago-illinois']
NEARBY['sioux-city-iowa'] = ['auto-transport-omaha-nebraska','auto-transport-ankeny-iowa','auto-transport-st-paul-minnesota','auto-transport-fargo-north-dakota','auto-transport-davenport-iowa','auto-transport-kansas-city-missouri','auto-transport-overland-park-kansas','auto-transport-denver-colorado']
# appends (lists under 8)
for _k, _vs in {'spokane-washington':['auto-transport-missoula-montana'], 'seattle-washington':['auto-transport-missoula-montana'],
               'meridian-idaho':['auto-transport-missoula-montana'], 'nampa-idaho':['auto-transport-missoula-montana'],
               'durham-north-carolina':['auto-transport-greensboro-north-carolina'], 'raleigh-north-carolina':['auto-transport-greensboro-north-carolina'],
               'charlotte-north-carolina':['auto-transport-greensboro-north-carolina'], 'chesapeake-virginia':['auto-transport-greensboro-north-carolina'],
               'augusta-georgia':['auto-transport-greensboro-north-carolina'],
               'green-bay-wisconsin':['auto-transport-fargo-north-dakota']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 45 (Nov 2, 2026): Bellevue (WA); Bloomington (MN); Great Falls (MT); Santa Fe (NM); Bismarck (ND); Eugene (OR); Charleston (SC) ----
#      NOTE: Charleston is South Carolina's first city page (first City Pages block on SC; new hub block before Texas).
#      Great Falls and Bismarck are pass-through markets like Missoula and Fargo (stats rows "3–6 Days"); Santa Fe reads "2–4 Days" like Albuquerque.
A='auto-transport-'
register('auto-transport-bellevue-washington', 'Bellevue', 'WA')
register('auto-transport-bloomington-minnesota', 'Bloomington', 'MN')
register('auto-transport-great-falls-montana', 'Great Falls', 'MT')
register('auto-transport-santa-fe-new-mexico', 'Santa Fe', 'NM')
register('auto-transport-bismarck-north-dakota', 'Bismarck', 'ND')
register('auto-transport-eugene-oregon', 'Eugene', 'OR')
register('auto-transport-charleston-south-carolina', 'Charleston', 'SC')
_s('bellevue-washington', [A+x for x in ['seattle-washington','portland-oregon','vancouver-washington','spokane-washington','eugene-oregon','missoula-montana','boise-idaho','sacramento-california']])
_s('bloomington-minnesota', [A+x for x in ['st-paul-minnesota','ankeny-iowa','sioux-city-iowa','fargo-north-dakota','madison-wisconsin','milwaukee-wisconsin','omaha-nebraska','chicago-illinois']])
_s('great-falls-montana', [A+x for x in ['missoula-montana','spokane-washington','bismarck-north-dakota','salt-lake-city-utah','boise-idaho','fargo-north-dakota','seattle-washington','denver-colorado']])
_s('santa-fe-new-mexico', [A+x for x in ['albuquerque-new-mexico','las-cruces-new-mexico','el-paso-texas','colorado-springs-colorado','denver-colorado','aurora-colorado','phoenix-arizona','tucson-arizona']])
_s('bismarck-north-dakota', [A+x for x in ['fargo-north-dakota','st-paul-minnesota','bloomington-minnesota','sioux-city-iowa','great-falls-montana','missoula-montana','omaha-nebraska','denver-colorado']])
_s('eugene-oregon', [A+x for x in ['portland-oregon','vancouver-washington','seattle-washington','bellevue-washington','sacramento-california','san-francisco-california','boise-idaho','spokane-washington']])
_s('charleston-south-carolina', [A+x for x in ['savannah-georgia','augusta-georgia','charlotte-north-carolina','jacksonville-florida','atlanta-georgia','raleigh-north-carolina','greensboro-north-carolina','macon-georgia']])
# explicit re-cuts (8 max)
NEARBY['seattle-washington'] = [A+x for x in ['bellevue-washington','spokane-washington','portland-oregon','vancouver-washington','eugene-oregon','boise-idaho','missoula-montana','anchorage-alaska']]
NEARBY['spokane-washington'] = [A+x for x in ['seattle-washington','bellevue-washington','boise-idaho','portland-oregon','meridian-idaho','salt-lake-city-utah','vancouver-washington','missoula-montana']]
NEARBY['portland-oregon'] = [A+x for x in ['vancouver-washington','eugene-oregon','seattle-washington','bellevue-washington','spokane-washington','sacramento-california','san-francisco-california','boise-idaho']]
NEARBY['st-paul-minnesota'] = [A+x for x in ['bloomington-minnesota','fargo-north-dakota','madison-wisconsin','ankeny-iowa','sioux-city-iowa','milwaukee-wisconsin','green-bay-wisconsin','omaha-nebraska']]
NEARBY['fargo-north-dakota'] = [A+x for x in ['bismarck-north-dakota','st-paul-minnesota','bloomington-minnesota','sioux-city-iowa','omaha-nebraska','ankeny-iowa','madison-wisconsin','missoula-montana']]
NEARBY['ankeny-iowa'] = [A+x for x in ['davenport-iowa','sioux-city-iowa','omaha-nebraska','kansas-city-missouri','st-paul-minnesota','bloomington-minnesota','chicago-illinois','madison-wisconsin']]
NEARBY['sioux-city-iowa'] = [A+x for x in ['omaha-nebraska','ankeny-iowa','st-paul-minnesota','bloomington-minnesota','fargo-north-dakota','davenport-iowa','kansas-city-missouri','denver-colorado']]
NEARBY['madison-wisconsin'] = [A+x for x in ['milwaukee-wisconsin','green-bay-wisconsin','kenosha-wisconsin','chicago-illinois','st-paul-minnesota','bloomington-minnesota','rockford-illinois','davenport-iowa']]
NEARBY['missoula-montana'] = [A+x for x in ['great-falls-montana','spokane-washington','seattle-washington','boise-idaho','meridian-idaho','salt-lake-city-utah','portland-oregon','fargo-north-dakota']]
NEARBY['denver-colorado'] = [A+x for x in ['aurora-colorado','colorado-springs-colorado','salt-lake-city-utah','albuquerque-new-mexico','santa-fe-new-mexico','las-cruces-new-mexico','kansas-city-missouri','omaha-nebraska']]
NEARBY['charlotte-north-carolina'] = [A+x for x in ['raleigh-north-carolina','durham-north-carolina','greensboro-north-carolina','charleston-south-carolina','atlanta-georgia','augusta-georgia','richmond-virginia','virginia-beach-virginia']]
# appends (lists under 8)
for _k, _vs in {'vancouver-washington':[A+'bellevue-washington',A+'eugene-oregon'],
               'albuquerque-new-mexico':[A+'santa-fe-new-mexico'], 'el-paso-texas':[A+'santa-fe-new-mexico'], 'las-cruces-new-mexico':[A+'santa-fe-new-mexico'],
               'colorado-springs-colorado':[A+'santa-fe-new-mexico'], 'aurora-colorado':[A+'santa-fe-new-mexico'],
               'savannah-georgia':[A+'charleston-south-carolina'], 'jacksonville-florida':[A+'charleston-south-carolina'], 'macon-georgia':[A+'charleston-south-carolina'],
               'augusta-georgia':[A+'charleston-south-carolina'], 'raleigh-north-carolina':[A+'charleston-south-carolina'],
               'sacramento-california':[A+'eugene-oregon'], 'san-francisco-california':[A+'eugene-oregon']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 46 (Nov 2, 2026): Sioux Falls (SD); Charleston (WV); Cheyenne (WY); Norfolk (VA); Bethlehem (PA) ----
#      NOTE: Sioux Falls, Charleston (WV) and Cheyenne are their states' first city pages (first City Pages blocks on SD, WV, WY;
#      new hub blocks South Dakota before Texas, West Virginia before Wisconsin, Wyoming at the end). Two Charlestons now exist:
#      the chips carry the state, and neighbor linking by the bare word "Charleston" is never done. Pass-through windows:
#      Sioux Falls "2–5 Days" (SD page), Cheyenne "3–6 Days" (WY page), Charleston WV "2–4 Days" (WV page).
#      The Cheyenne row carried a 304 (WV) area code; used as given and flagged to the owner.
register('auto-transport-sioux-falls-south-dakota', 'Sioux Falls', 'SD')
register('auto-transport-charleston-west-virginia', 'Charleston', 'WV')
register('auto-transport-cheyenne-wyoming', 'Cheyenne', 'WY')
register('auto-transport-norfolk-virginia', 'Norfolk', 'VA')
register('auto-transport-bethlehem-pennsylvania', 'Bethlehem', 'PA')
_s('sioux-falls-south-dakota', [A+x for x in ['sioux-city-iowa','omaha-nebraska','fargo-north-dakota','bloomington-minnesota','st-paul-minnesota','ankeny-iowa','kansas-city-missouri','bismarck-north-dakota']])
_s('charleston-west-virginia', [A+x for x in ['columbus-ohio','lexington-kentucky','cincinnati-ohio','pittsburgh-pennsylvania','dayton-ohio','louisville-kentucky','akron-ohio','richmond-virginia']])
_s('cheyenne-wyoming', [A+x for x in ['denver-colorado','aurora-colorado','colorado-springs-colorado','salt-lake-city-utah','omaha-nebraska','sioux-falls-south-dakota','albuquerque-new-mexico','kansas-city-missouri']])
_s('norfolk-virginia', [A+x for x in ['virginia-beach-virginia','chesapeake-virginia','richmond-virginia','raleigh-north-carolina','durham-north-carolina','greensboro-north-carolina','baltimore-maryland','columbia-maryland']])
_s('bethlehem-pennsylvania', [A+x for x in ['allentown-pennsylvania','reading-pennsylvania','philadelphia-pennsylvania','newark-new-jersey','wilmington-delaware','manhattan-new-york','staten-island-new-york','yonkers-new-york']])
# explicit re-cuts (8 max)
NEARBY['sioux-city-iowa'] = [A+x for x in ['sioux-falls-south-dakota','omaha-nebraska','ankeny-iowa','st-paul-minnesota','bloomington-minnesota','fargo-north-dakota','kansas-city-missouri','denver-colorado']]
NEARBY['omaha-nebraska'] = [A+x for x in ['ankeny-iowa','sioux-city-iowa','sioux-falls-south-dakota','kansas-city-missouri','davenport-iowa','st-paul-minnesota','topeka-kansas','denver-colorado']]
NEARBY['fargo-north-dakota'] = [A+x for x in ['bismarck-north-dakota','st-paul-minnesota','bloomington-minnesota','sioux-falls-south-dakota','sioux-city-iowa','omaha-nebraska','ankeny-iowa','missoula-montana']]
NEARBY['bloomington-minnesota'] = [A+x for x in ['st-paul-minnesota','ankeny-iowa','sioux-city-iowa','sioux-falls-south-dakota','fargo-north-dakota','madison-wisconsin','omaha-nebraska','chicago-illinois']]
NEARBY['st-paul-minnesota'] = [A+x for x in ['bloomington-minnesota','fargo-north-dakota','sioux-falls-south-dakota','madison-wisconsin','ankeny-iowa','sioux-city-iowa','milwaukee-wisconsin','omaha-nebraska']]
NEARBY['bismarck-north-dakota'] = [A+x for x in ['fargo-north-dakota','st-paul-minnesota','bloomington-minnesota','sioux-falls-south-dakota','sioux-city-iowa','great-falls-montana','omaha-nebraska','denver-colorado']]
NEARBY['denver-colorado'] = [A+x for x in ['cheyenne-wyoming','aurora-colorado','colorado-springs-colorado','salt-lake-city-utah','albuquerque-new-mexico','santa-fe-new-mexico','kansas-city-missouri','omaha-nebraska']]
NEARBY['virginia-beach-virginia'] = [A+x for x in ['norfolk-virginia','chesapeake-virginia','richmond-virginia','raleigh-north-carolina','durham-north-carolina','baltimore-maryland','columbia-maryland','greensboro-north-carolina']]
NEARBY['chesapeake-virginia'] = [A+x for x in ['norfolk-virginia','virginia-beach-virginia','richmond-virginia','raleigh-north-carolina','durham-north-carolina','columbia-maryland','baltimore-maryland','greensboro-north-carolina']]
NEARBY['richmond-virginia'] = [A+x for x in ['virginia-beach-virginia','norfolk-virginia','chesapeake-virginia','columbia-maryland','baltimore-maryland','raleigh-north-carolina','durham-north-carolina','greensboro-north-carolina']]
NEARBY['philadelphia-pennsylvania'] = [A+x for x in ['pittsburgh-pennsylvania','allentown-pennsylvania','bethlehem-pennsylvania','reading-pennsylvania','newark-new-jersey','manhattan-new-york','baltimore-maryland','wilmington-delaware']]
# appends (lists under 8)
for _k, _vs in {'columbus-ohio':[A+'charleston-west-virginia'], 'lexington-kentucky':[A+'charleston-west-virginia'], 'cincinnati-ohio':[A+'charleston-west-virginia'],
               'pittsburgh-pennsylvania':[A+'charleston-west-virginia'], 'dayton-ohio':[A+'charleston-west-virginia'],
               'aurora-colorado':[A+'cheyenne-wyoming'], 'colorado-springs-colorado':[A+'cheyenne-wyoming'],
               'allentown-pennsylvania':[A+'bethlehem-pennsylvania'], 'reading-pennsylvania':[A+'bethlehem-pennsylvania']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 47 (Nov 2, 2026): Rochester (MN); Gulfport (MS); Billings (MT); Lincoln (NE); Nashua (NH); Winston-Salem (NC) ----
#      NOTE: Nashua is New Hampshire's first city page (first City Pages block on NH; new hub block New Hampshire before New Jersey).
#      Two Rochesters now exist (NY since the early batches, MN now): the chips carry the state, and neighbor linking by the bare
#      word "Rochester" is never done. Pass-through window: Billings "3–6 Days" (MT page). The Nashua row carried an 802 (Vermont)
#      area code; used as given and flagged to the owner.
register('auto-transport-rochester-minnesota', 'Rochester', 'MN')
register('auto-transport-gulfport-mississippi', 'Gulfport', 'MS')
register('auto-transport-billings-montana', 'Billings', 'MT')
register('auto-transport-lincoln-nebraska', 'Lincoln', 'NE')
register('auto-transport-nashua-new-hampshire', 'Nashua', 'NH')
register('auto-transport-winston-salem-north-carolina', 'Winston-Salem', 'NC')
_s('rochester-minnesota', [A+x for x in ['st-paul-minnesota','bloomington-minnesota','madison-wisconsin','ankeny-iowa','davenport-iowa','sioux-falls-south-dakota','milwaukee-wisconsin','chicago-illinois']])
_s('gulfport-mississippi', [A+x for x in ['new-orleans-louisiana','metairie-louisiana','mobile-alabama','jackson-mississippi','baton-rouge-louisiana','lafayette-louisiana','montgomery-alabama','tallahassee-florida']])
_s('billings-montana', [A+x for x in ['great-falls-montana','missoula-montana','bismarck-north-dakota','cheyenne-wyoming','denver-colorado','salt-lake-city-utah','spokane-washington','fargo-north-dakota']])
_s('lincoln-nebraska', [A+x for x in ['omaha-nebraska','sioux-city-iowa','ankeny-iowa','kansas-city-missouri','topeka-kansas','sioux-falls-south-dakota','wichita-kansas','denver-colorado']])
_s('nashua-new-hampshire', [A+x for x in ['boston-massachusetts','worcester-massachusetts','portland-maine','cranston-rhode-island','warwick-rhode-island','springfield-massachusetts','hartford-connecticut','albany-new-york']])
_s('winston-salem-north-carolina', [A+x for x in ['greensboro-north-carolina','charlotte-north-carolina','durham-north-carolina','raleigh-north-carolina','richmond-virginia','charleston-south-carolina','virginia-beach-virginia','atlanta-georgia']])
# explicit re-cuts (8 max)
NEARBY['st-paul-minnesota'] = [A+x for x in ['bloomington-minnesota','rochester-minnesota','fargo-north-dakota','sioux-falls-south-dakota','madison-wisconsin','ankeny-iowa','sioux-city-iowa','milwaukee-wisconsin']]
NEARBY['bloomington-minnesota'] = [A+x for x in ['st-paul-minnesota','rochester-minnesota','ankeny-iowa','sioux-city-iowa','sioux-falls-south-dakota','fargo-north-dakota','madison-wisconsin','omaha-nebraska']]
NEARBY['sioux-falls-south-dakota'] = [A+x for x in ['sioux-city-iowa','omaha-nebraska','fargo-north-dakota','bloomington-minnesota','st-paul-minnesota','rochester-minnesota','ankeny-iowa','bismarck-north-dakota']]
NEARBY['jackson-mississippi'] = [A+x for x in ['gulfport-mississippi','new-orleans-louisiana','baton-rouge-louisiana','mobile-alabama','shreveport-louisiana','little-rock-arkansas','metairie-louisiana','montgomery-alabama']]
NEARBY['mobile-alabama'] = [A+x for x in ['gulfport-mississippi','new-orleans-louisiana','montgomery-alabama','tuscaloosa-alabama','tallahassee-florida','baton-rouge-louisiana','jackson-mississippi','atlanta-georgia']]
NEARBY['new-orleans-louisiana'] = [A+x for x in ['metairie-louisiana','baton-rouge-louisiana','gulfport-mississippi','jackson-mississippi','mobile-alabama','houston-texas','shreveport-louisiana','lafayette-louisiana']]
NEARBY['metairie-louisiana'] = [A+x for x in ['new-orleans-louisiana','baton-rouge-louisiana','gulfport-mississippi','mobile-alabama','houston-texas','shreveport-louisiana','lafayette-louisiana','jackson-mississippi']]
NEARBY['baton-rouge-louisiana'] = [A+x for x in ['new-orleans-louisiana','metairie-louisiana','gulfport-mississippi','mobile-alabama','lafayette-louisiana','shreveport-louisiana','houston-texas','jackson-mississippi']]
NEARBY['great-falls-montana'] = [A+x for x in ['billings-montana','missoula-montana','spokane-washington','bismarck-north-dakota','salt-lake-city-utah','boise-idaho','fargo-north-dakota','seattle-washington']]
NEARBY['missoula-montana'] = [A+x for x in ['great-falls-montana','billings-montana','spokane-washington','seattle-washington','boise-idaho','meridian-idaho','salt-lake-city-utah','portland-oregon']]
NEARBY['bismarck-north-dakota'] = [A+x for x in ['fargo-north-dakota','billings-montana','st-paul-minnesota','bloomington-minnesota','sioux-falls-south-dakota','sioux-city-iowa','great-falls-montana','omaha-nebraska']]
NEARBY['cheyenne-wyoming'] = [A+x for x in ['denver-colorado','aurora-colorado','colorado-springs-colorado','salt-lake-city-utah','billings-montana','omaha-nebraska','sioux-falls-south-dakota','kansas-city-missouri']]
NEARBY['omaha-nebraska'] = [A+x for x in ['lincoln-nebraska','ankeny-iowa','sioux-city-iowa','sioux-falls-south-dakota','kansas-city-missouri','davenport-iowa','st-paul-minnesota','topeka-kansas']]
NEARBY['sioux-city-iowa'] = [A+x for x in ['sioux-falls-south-dakota','omaha-nebraska','lincoln-nebraska','ankeny-iowa','st-paul-minnesota','bloomington-minnesota','fargo-north-dakota','kansas-city-missouri']]
NEARBY['topeka-kansas'] = [A+x for x in ['kansas-city-missouri','overland-park-kansas','olathe-kansas','wichita-kansas','independence-missouri','lincoln-nebraska','lawrence-kansas','omaha-nebraska']]
NEARBY['ankeny-iowa'] = [A+x for x in ['davenport-iowa','sioux-city-iowa','omaha-nebraska','lincoln-nebraska','kansas-city-missouri','st-paul-minnesota','bloomington-minnesota','chicago-illinois']]
NEARBY['boston-massachusetts'] = [A+x for x in ['nashua-new-hampshire','worcester-massachusetts','cranston-rhode-island','warwick-rhode-island','manhattan-new-york','hartford-connecticut','portland-maine','albany-new-york']]
NEARBY['worcester-massachusetts'] = [A+x for x in ['boston-massachusetts','nashua-new-hampshire','cranston-rhode-island','warwick-rhode-island','springfield-massachusetts','hartford-connecticut','albany-new-york','new-haven-connecticut']]
NEARBY['greensboro-north-carolina'] = [A+x for x in ['winston-salem-north-carolina','durham-north-carolina','raleigh-north-carolina','charlotte-north-carolina','richmond-virginia','chesapeake-virginia','virginia-beach-virginia','atlanta-georgia']]
NEARBY['charlotte-north-carolina'] = [A+x for x in ['raleigh-north-carolina','durham-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','charleston-south-carolina','atlanta-georgia','augusta-georgia','richmond-virginia']]
NEARBY['raleigh-north-carolina'] = [A+x for x in ['durham-north-carolina','charlotte-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','baltimore-maryland','virginia-beach-virginia','richmond-virginia','charleston-south-carolina']]
# appends (lists under 8)
for _k, _vs in {'portland-maine':[A+'nashua-new-hampshire'], 'warwick-rhode-island':[A+'nashua-new-hampshire'], 'cranston-rhode-island':[A+'nashua-new-hampshire'],
               'springfield-massachusetts':[A+'nashua-new-hampshire'], 'durham-north-carolina':[A+'winston-salem-north-carolina']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 48 (Nov 2, 2026): Newport News (VA); Duluth (MN); Sparks (NV); Paterson (NJ); Fayetteville (NC) ----
#      NOTE: all five states already had City Pages blocks (regens only; no new hub block). Two Fayettevilles now exist (AR since
#      the early batches, NC now): the chips carry the state, and neighbor linking by the bare word "Fayetteville" is never done.
#      Duluth GA is an Atlanta suburb, so "Duluth" is never linked without reading the mention first. The Sparks row spelled the
#      city "Spraks"; built as Sparks. Area codes all match their states.
register('auto-transport-newport-news-virginia', 'Newport News', 'VA')
register('auto-transport-duluth-minnesota', 'Duluth', 'MN')
register('auto-transport-sparks-nevada', 'Sparks', 'NV')
register('auto-transport-paterson-new-jersey', 'Paterson', 'NJ')
register('auto-transport-fayetteville-north-carolina', 'Fayetteville', 'NC')
_s('newport-news-virginia', [A+x for x in ['norfolk-virginia','virginia-beach-virginia','chesapeake-virginia','richmond-virginia','raleigh-north-carolina','durham-north-carolina','baltimore-maryland','columbia-maryland']])
_s('duluth-minnesota', [A+x for x in ['st-paul-minnesota','bloomington-minnesota','rochester-minnesota','fargo-north-dakota','madison-wisconsin','milwaukee-wisconsin','green-bay-wisconsin','bismarck-north-dakota']])
_s('sparks-nevada', [A+x for x in ['sacramento-california','stockton-california','san-francisco-california','oakland-california','san-jose-california','fresno-california','las-vegas-nevada','salt-lake-city-utah']])
_s('paterson-new-jersey', [A+x for x in ['newark-new-jersey','manhattan-new-york','bronx-new-york','yonkers-new-york','staten-island-new-york','brooklyn-new-york','queens-new-york','allentown-pennsylvania']])
_s('fayetteville-north-carolina', [A+x for x in ['raleigh-north-carolina','durham-north-carolina','charlotte-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','richmond-virginia','charleston-south-carolina','virginia-beach-virginia']])
# explicit re-cuts (8 max)
NEARBY['norfolk-virginia'] = [A+x for x in ['virginia-beach-virginia','chesapeake-virginia','newport-news-virginia','richmond-virginia','raleigh-north-carolina','durham-north-carolina','greensboro-north-carolina','baltimore-maryland']]
NEARBY['virginia-beach-virginia'] = [A+x for x in ['norfolk-virginia','chesapeake-virginia','newport-news-virginia','richmond-virginia','raleigh-north-carolina','durham-north-carolina','baltimore-maryland','columbia-maryland']]
NEARBY['chesapeake-virginia'] = [A+x for x in ['norfolk-virginia','virginia-beach-virginia','newport-news-virginia','richmond-virginia','raleigh-north-carolina','durham-north-carolina','columbia-maryland','baltimore-maryland']]
NEARBY['richmond-virginia'] = [A+x for x in ['virginia-beach-virginia','norfolk-virginia','chesapeake-virginia','newport-news-virginia','columbia-maryland','baltimore-maryland','raleigh-north-carolina','durham-north-carolina']]
NEARBY['st-paul-minnesota'] = [A+x for x in ['bloomington-minnesota','rochester-minnesota','duluth-minnesota','fargo-north-dakota','sioux-falls-south-dakota','madison-wisconsin','ankeny-iowa','sioux-city-iowa']]
NEARBY['bloomington-minnesota'] = [A+x for x in ['st-paul-minnesota','rochester-minnesota','duluth-minnesota','ankeny-iowa','sioux-city-iowa','sioux-falls-south-dakota','fargo-north-dakota','madison-wisconsin']]
NEARBY['rochester-minnesota'] = [A+x for x in ['st-paul-minnesota','bloomington-minnesota','duluth-minnesota','madison-wisconsin','ankeny-iowa','davenport-iowa','sioux-falls-south-dakota','milwaukee-wisconsin']]
NEARBY['fargo-north-dakota'] = [A+x for x in ['bismarck-north-dakota','st-paul-minnesota','bloomington-minnesota','duluth-minnesota','sioux-falls-south-dakota','sioux-city-iowa','omaha-nebraska','ankeny-iowa']]
NEARBY['green-bay-wisconsin'] = [A+x for x in ['milwaukee-wisconsin','madison-wisconsin','kenosha-wisconsin','chicago-illinois','duluth-minnesota','st-paul-minnesota','detroit-michigan','indianapolis-indiana']]
NEARBY['sacramento-california'] = [A+x for x in ['sparks-nevada','san-francisco-california','oakland-california','san-jose-california','stockton-california','portland-oregon','salt-lake-city-utah','fresno-california']]
NEARBY['newark-new-jersey'] = [A+x for x in ['manhattan-new-york','paterson-new-jersey','staten-island-new-york','brooklyn-new-york','yonkers-new-york','philadelphia-pennsylvania','allentown-pennsylvania','stamford-connecticut']]
NEARBY['manhattan-new-york'] = [A+x for x in ['brooklyn-new-york','queens-new-york','bronx-new-york','newark-new-jersey','paterson-new-jersey','yonkers-new-york','staten-island-new-york','philadelphia-pennsylvania']]
NEARBY['bronx-new-york'] = [A+x for x in ['manhattan-new-york','yonkers-new-york','queens-new-york','brooklyn-new-york','newark-new-jersey','paterson-new-jersey','stamford-connecticut','boston-massachusetts']]
NEARBY['yonkers-new-york'] = [A+x for x in ['bronx-new-york','manhattan-new-york','queens-new-york','newark-new-jersey','paterson-new-jersey','stamford-connecticut','albany-new-york','boston-massachusetts']]
NEARBY['raleigh-north-carolina'] = [A+x for x in ['durham-north-carolina','charlotte-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','fayetteville-north-carolina','virginia-beach-virginia','richmond-virginia','charleston-south-carolina']]
NEARBY['durham-north-carolina'] = [A+x for x in ['raleigh-north-carolina','charlotte-north-carolina','fayetteville-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','virginia-beach-virginia','richmond-virginia','atlanta-georgia']]
NEARBY['charlotte-north-carolina'] = [A+x for x in ['raleigh-north-carolina','durham-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','fayetteville-north-carolina','charleston-south-carolina','atlanta-georgia','richmond-virginia']]
NEARBY['greensboro-north-carolina'] = [A+x for x in ['winston-salem-north-carolina','durham-north-carolina','raleigh-north-carolina','charlotte-north-carolina','fayetteville-north-carolina','richmond-virginia','virginia-beach-virginia','atlanta-georgia']]
NEARBY['winston-salem-north-carolina'] = [A+x for x in ['greensboro-north-carolina','charlotte-north-carolina','durham-north-carolina','raleigh-north-carolina','fayetteville-north-carolina','richmond-virginia','charleston-south-carolina','atlanta-georgia']]
# appends (lists under 8)
for _k, _vs in {'las-vegas-nevada':[A+'sparks-nevada'], 'henderson-nevada':[A+'sparks-nevada'], 'stockton-california':[A+'sparks-nevada'],
               'san-francisco-california':[A+'sparks-nevada'], 'oakland-california':[A+'sparks-nevada'], 'san-jose-california':[A+'sparks-nevada'],
               'fresno-california':[A+'sparks-nevada'], 'staten-island-new-york':[A+'paterson-new-jersey']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 49 (Nov 2, 2026): Salem (OR); Memphis (TN); Minneapolis (MN); Rapid City (SD); Columbia (SC); Burlington (VT); Huntington (WV) ----
#      NOTE: Memphis and Burlington are their states' first city pages (first City Pages blocks on TN and VT; new hub blocks
#      Tennessee before Texas and Vermont before Virginia). Name collisions: three Columbias (MD, MO, SC), "Salem" sits inside
#      "Winston-Salem", Burlington NC/MA and Huntington NY/Beach exist as towns and streets, so none of those four is ever linked
#      on the bare word. Windows: Rapid City "2–5 Days" and Burlington "2–5 Days" (SD and VT pages), Huntington "2–4 Days" (WV page).
#      The Memphis row spelled the state "Tenneesee"; Minneapolis carries a 763 (northwest-metro) area code, left as given.
register('auto-transport-salem-oregon', 'Salem', 'OR')
register('auto-transport-memphis-tennessee', 'Memphis', 'TN')
register('auto-transport-minneapolis-minnesota', 'Minneapolis', 'MN')
register('auto-transport-rapid-city-south-dakota', 'Rapid City', 'SD')
register('auto-transport-columbia-south-carolina', 'Columbia', 'SC')
register('auto-transport-burlington-vermont', 'Burlington', 'VT')
register('auto-transport-huntington-west-virginia', 'Huntington', 'WV')
_s('salem-oregon', [A+x for x in ['portland-oregon','eugene-oregon','vancouver-washington','seattle-washington','bellevue-washington','sacramento-california','boise-idaho','spokane-washington']])
_s('memphis-tennessee', [A+x for x in ['little-rock-arkansas','jackson-mississippi','tuscaloosa-alabama','huntsville-alabama','st-louis-missouri','shreveport-louisiana','louisville-kentucky','springfield-missouri']])
_s('minneapolis-minnesota', [A+x for x in ['st-paul-minnesota','bloomington-minnesota','rochester-minnesota','duluth-minnesota','fargo-north-dakota','madison-wisconsin','sioux-falls-south-dakota','ankeny-iowa']])
_s('rapid-city-south-dakota', [A+x for x in ['sioux-falls-south-dakota','billings-montana','cheyenne-wyoming','bismarck-north-dakota','denver-colorado','sioux-city-iowa','omaha-nebraska','fargo-north-dakota']])
_s('columbia-south-carolina', [A+x for x in ['charleston-south-carolina','charlotte-north-carolina','augusta-georgia','fayetteville-north-carolina','savannah-georgia','greensboro-north-carolina','atlanta-georgia','raleigh-north-carolina']])
_s('burlington-vermont', [A+x for x in ['albany-new-york','boston-massachusetts','nashua-new-hampshire','worcester-massachusetts','springfield-massachusetts','hartford-connecticut','portland-maine','manhattan-new-york']])
_s('huntington-west-virginia', [A+x for x in ['charleston-west-virginia','lexington-kentucky','cincinnati-ohio','columbus-ohio','louisville-kentucky','dayton-ohio','pittsburgh-pennsylvania','akron-ohio']])
# explicit re-cuts (8 max)
NEARBY['portland-oregon'] = [A+x for x in ['vancouver-washington','salem-oregon','eugene-oregon','seattle-washington','bellevue-washington','spokane-washington','sacramento-california','boise-idaho']]
NEARBY['eugene-oregon'] = [A+x for x in ['salem-oregon','portland-oregon','vancouver-washington','seattle-washington','sacramento-california','san-francisco-california','boise-idaho','spokane-washington']]
NEARBY['vancouver-washington'] = [A+x for x in ['portland-oregon','salem-oregon','seattle-washington','spokane-washington','boise-idaho','sacramento-california','bellevue-washington','eugene-oregon']]
NEARBY['little-rock-arkansas'] = [A+x for x in ['memphis-tennessee','fayetteville-arkansas','fort-smith-arkansas','tulsa-oklahoma','dallas-texas','st-louis-missouri','springfield-missouri','shreveport-louisiana']]
NEARBY['jackson-mississippi'] = [A+x for x in ['gulfport-mississippi','memphis-tennessee','new-orleans-louisiana','baton-rouge-louisiana','mobile-alabama','shreveport-louisiana','little-rock-arkansas','metairie-louisiana']]
NEARBY['tuscaloosa-alabama'] = [A+x for x in ['mobile-alabama','memphis-tennessee','atlanta-georgia','new-orleans-louisiana','huntsville-alabama','montgomery-alabama','jackson-mississippi','louisville-kentucky']]
NEARBY['st-louis-missouri'] = [A+x for x in ['columbia-missouri','kansas-city-missouri','springfield-missouri','springfield-illinois','chicago-illinois','indianapolis-indiana','louisville-kentucky','memphis-tennessee']]
NEARBY['shreveport-louisiana'] = [A+x for x in ['dallas-texas','fort-worth-texas','little-rock-arkansas','memphis-tennessee','baton-rouge-louisiana','houston-texas','new-orleans-louisiana','jackson-mississippi']]
NEARBY['louisville-kentucky'] = [A+x for x in ['lexington-kentucky','evansville-indiana','owensboro-kentucky','indianapolis-indiana','cincinnati-ohio','st-louis-missouri','memphis-tennessee','chicago-illinois']]
NEARBY['st-paul-minnesota'] = [A+x for x in ['minneapolis-minnesota','bloomington-minnesota','rochester-minnesota','duluth-minnesota','fargo-north-dakota','sioux-falls-south-dakota','madison-wisconsin','ankeny-iowa']]
NEARBY['bloomington-minnesota'] = [A+x for x in ['minneapolis-minnesota','st-paul-minnesota','rochester-minnesota','duluth-minnesota','ankeny-iowa','sioux-falls-south-dakota','fargo-north-dakota','madison-wisconsin']]
NEARBY['rochester-minnesota'] = [A+x for x in ['minneapolis-minnesota','st-paul-minnesota','bloomington-minnesota','duluth-minnesota','madison-wisconsin','ankeny-iowa','sioux-falls-south-dakota','davenport-iowa']]
NEARBY['duluth-minnesota'] = [A+x for x in ['minneapolis-minnesota','st-paul-minnesota','bloomington-minnesota','rochester-minnesota','fargo-north-dakota','madison-wisconsin','green-bay-wisconsin','bismarck-north-dakota']]
NEARBY['fargo-north-dakota'] = [A+x for x in ['bismarck-north-dakota','minneapolis-minnesota','st-paul-minnesota','bloomington-minnesota','duluth-minnesota','sioux-falls-south-dakota','sioux-city-iowa','omaha-nebraska']]
NEARBY['madison-wisconsin'] = [A+x for x in ['milwaukee-wisconsin','green-bay-wisconsin','kenosha-wisconsin','chicago-illinois','minneapolis-minnesota','st-paul-minnesota','rockford-illinois','davenport-iowa']]
NEARBY['ankeny-iowa'] = [A+x for x in ['davenport-iowa','sioux-city-iowa','omaha-nebraska','lincoln-nebraska','kansas-city-missouri','minneapolis-minnesota','st-paul-minnesota','chicago-illinois']]
NEARBY['sioux-falls-south-dakota'] = [A+x for x in ['sioux-city-iowa','omaha-nebraska','fargo-north-dakota','minneapolis-minnesota','st-paul-minnesota','bloomington-minnesota','rochester-minnesota','rapid-city-south-dakota']]
NEARBY['billings-montana'] = [A+x for x in ['great-falls-montana','missoula-montana','bismarck-north-dakota','rapid-city-south-dakota','cheyenne-wyoming','denver-colorado','salt-lake-city-utah','spokane-washington']]
NEARBY['cheyenne-wyoming'] = [A+x for x in ['denver-colorado','aurora-colorado','colorado-springs-colorado','salt-lake-city-utah','billings-montana','rapid-city-south-dakota','omaha-nebraska','sioux-falls-south-dakota']]
NEARBY['bismarck-north-dakota'] = [A+x for x in ['fargo-north-dakota','billings-montana','rapid-city-south-dakota','st-paul-minnesota','bloomington-minnesota','sioux-falls-south-dakota','sioux-city-iowa','great-falls-montana']]
NEARBY['charleston-south-carolina'] = [A+x for x in ['columbia-south-carolina','savannah-georgia','augusta-georgia','charlotte-north-carolina','jacksonville-florida','atlanta-georgia','raleigh-north-carolina','greensboro-north-carolina']]
NEARBY['charlotte-north-carolina'] = [A+x for x in ['raleigh-north-carolina','durham-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','fayetteville-north-carolina','columbia-south-carolina','charleston-south-carolina','atlanta-georgia']]
NEARBY['augusta-georgia'] = [A+x for x in ['atlanta-georgia','columbia-south-carolina','athens-georgia','savannah-georgia','macon-georgia','charlotte-north-carolina','columbus-georgia','charleston-south-carolina']]
NEARBY['fayetteville-north-carolina'] = [A+x for x in ['raleigh-north-carolina','durham-north-carolina','charlotte-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','columbia-south-carolina','richmond-virginia','charleston-south-carolina']]
NEARBY['greensboro-north-carolina'] = [A+x for x in ['winston-salem-north-carolina','durham-north-carolina','raleigh-north-carolina','charlotte-north-carolina','fayetteville-north-carolina','richmond-virginia','columbia-south-carolina','atlanta-georgia']]
NEARBY['boston-massachusetts'] = [A+x for x in ['nashua-new-hampshire','worcester-massachusetts','cranston-rhode-island','manhattan-new-york','hartford-connecticut','portland-maine','albany-new-york','burlington-vermont']]
NEARBY['nashua-new-hampshire'] = [A+x for x in ['boston-massachusetts','worcester-massachusetts','portland-maine','cranston-rhode-island','burlington-vermont','springfield-massachusetts','hartford-connecticut','albany-new-york']]
NEARBY['albany-new-york'] = [A+x for x in ['syracuse-new-york','boston-massachusetts','burlington-vermont','yonkers-new-york','manhattan-new-york','rochester-new-york','hartford-connecticut','springfield-massachusetts']]
NEARBY['charleston-west-virginia'] = [A+x for x in ['huntington-west-virginia','columbus-ohio','lexington-kentucky','cincinnati-ohio','pittsburgh-pennsylvania','dayton-ohio','louisville-kentucky','akron-ohio']]
NEARBY['lexington-kentucky'] = [A+x for x in ['louisville-kentucky','huntington-west-virginia','charleston-west-virginia','cincinnati-ohio','indianapolis-indiana','cleveland-ohio','charlotte-north-carolina','owensboro-kentucky']]
NEARBY['columbus-ohio'] = [A+x for x in ['cincinnati-ohio','dayton-ohio','cleveland-ohio','akron-ohio','indianapolis-indiana','huntington-west-virginia','charleston-west-virginia','pittsburgh-pennsylvania']]
# appends (lists under 8)
for _k, _vs in {'huntsville-alabama':[A+'memphis-tennessee'], 'springfield-missouri':[A+'memphis-tennessee'], 'evansville-indiana':[A+'memphis-tennessee'],
               'savannah-georgia':[A+'columbia-south-carolina'], 'portland-maine':[A+'burlington-vermont'], 'cincinnati-ohio':[A+'huntington-west-virginia']}.items():
    for _v in _vs:
        if _k in NEARBY and _v not in NEARBY[_k]: NEARBY[_k].append(_v)

# ---- Batch 50 (Nov 2, 2026): Casper (WY); Pawtucket (RI); Bozeman (MT); Carson City (NV); Rio Rancho (NM); Knoxville (TN) ----
#      NOTE: all six states already carry City Pages blocks (Cheyenne; Cranston/Warwick; Billings/Great Falls/Missoula;
#      Las Vegas/Henderson/Sparks; Albuquerque/Las Cruces/Santa Fe; Memphis), so this batch adds no hub block. Windows:
#      Casper and Bozeman "3–6 Days" (the WY and MT pages' pass-through figure), Rio Rancho "2–4 Days" (the Albuquerque
#      figure), Pawtucket, Carson City and Knoxville "1–3 Days". The Knoxville row spelled the state "Tenneesee"; Casper
#      carries a 304 (West Virginia) area code like the Cheyenne line, flagged to the owner and used as given.
#      Names are unique (no Casper, Pawtucket, Bozeman, Carson City, Rio Rancho or Knoxville collisions in prose), but
#      "Carson" alone is a Reno-area surname and street, so neighbor links use the full "Carson City" only.
register('auto-transport-casper-wyoming', 'Casper', 'WY')
register('auto-transport-pawtucket-rhode-island', 'Pawtucket', 'RI')
register('auto-transport-bozeman-montana', 'Bozeman', 'MT')
register('auto-transport-carson-city-nevada', 'Carson City', 'NV')
register('auto-transport-rio-rancho-new-mexico', 'Rio Rancho', 'NM')
register('auto-transport-knoxville-tennessee', 'Knoxville', 'TN')
_s('casper-wyoming', [A+x for x in ['cheyenne-wyoming','billings-montana','rapid-city-south-dakota','denver-colorado','aurora-colorado','colorado-springs-colorado','salt-lake-city-utah','sioux-falls-south-dakota']])
_s('pawtucket-rhode-island', [A+x for x in ['cranston-rhode-island','warwick-rhode-island','boston-massachusetts','worcester-massachusetts','hartford-connecticut','new-haven-connecticut','springfield-massachusetts','manhattan-new-york']])
_s('bozeman-montana', [A+x for x in ['billings-montana','missoula-montana','great-falls-montana','spokane-washington','boise-idaho','salt-lake-city-utah','meridian-idaho','seattle-washington']])
_s('carson-city-nevada', [A+x for x in ['sparks-nevada','sacramento-california','stockton-california','san-francisco-california','san-jose-california','fresno-california','las-vegas-nevada','salt-lake-city-utah']])
_s('rio-rancho-new-mexico', [A+x for x in ['albuquerque-new-mexico','santa-fe-new-mexico','las-cruces-new-mexico','el-paso-texas','denver-colorado','phoenix-arizona','tucson-arizona','colorado-springs-colorado']])
_s('knoxville-tennessee', [A+x for x in ['memphis-tennessee','lexington-kentucky','louisville-kentucky','cincinnati-ohio','atlanta-georgia','huntsville-alabama','charlotte-north-carolina','winston-salem-north-carolina']])
# explicit re-cuts (8 max)
NEARBY['cheyenne-wyoming'] = [A+x for x in ['denver-colorado','casper-wyoming','aurora-colorado','colorado-springs-colorado','salt-lake-city-utah','billings-montana','rapid-city-south-dakota','omaha-nebraska']]
NEARBY['billings-montana'] = [A+x for x in ['bozeman-montana','great-falls-montana','missoula-montana','bismarck-north-dakota','rapid-city-south-dakota','casper-wyoming','cheyenne-wyoming','salt-lake-city-utah']]
NEARBY['great-falls-montana'] = [A+x for x in ['billings-montana','bozeman-montana','missoula-montana','spokane-washington','bismarck-north-dakota','salt-lake-city-utah','boise-idaho','fargo-north-dakota']]
NEARBY['missoula-montana'] = [A+x for x in ['bozeman-montana','great-falls-montana','billings-montana','spokane-washington','seattle-washington','boise-idaho','meridian-idaho','salt-lake-city-utah']]
NEARBY['rapid-city-south-dakota'] = [A+x for x in ['sioux-falls-south-dakota','billings-montana','casper-wyoming','cheyenne-wyoming','bismarck-north-dakota','denver-colorado','omaha-nebraska','fargo-north-dakota']]
NEARBY['sparks-nevada'] = [A+x for x in ['carson-city-nevada','sacramento-california','stockton-california','san-francisco-california','oakland-california','san-jose-california','las-vegas-nevada','salt-lake-city-utah']]
NEARBY['albuquerque-new-mexico'] = [A+x for x in ['rio-rancho-new-mexico','santa-fe-new-mexico','las-cruces-new-mexico','el-paso-texas','phoenix-arizona','tucson-arizona','denver-colorado','oklahoma-city-oklahoma']]
NEARBY['santa-fe-new-mexico'] = [A+x for x in ['albuquerque-new-mexico','rio-rancho-new-mexico','las-cruces-new-mexico','el-paso-texas','colorado-springs-colorado','denver-colorado','phoenix-arizona','tucson-arizona']]
NEARBY['cranston-rhode-island'] = [A+x for x in ['warwick-rhode-island','pawtucket-rhode-island','boston-massachusetts','worcester-massachusetts','hartford-connecticut','new-haven-connecticut','springfield-massachusetts','manhattan-new-york']]
NEARBY['warwick-rhode-island'] = [A+x for x in ['cranston-rhode-island','pawtucket-rhode-island','boston-massachusetts','worcester-massachusetts','hartford-connecticut','new-haven-connecticut','springfield-massachusetts','manhattan-new-york']]
NEARBY['worcester-massachusetts'] = [A+x for x in ['boston-massachusetts','nashua-new-hampshire','cranston-rhode-island','warwick-rhode-island','pawtucket-rhode-island','springfield-massachusetts','hartford-connecticut','albany-new-york']]
NEARBY['memphis-tennessee'] = [A+x for x in ['little-rock-arkansas','jackson-mississippi','knoxville-tennessee','tuscaloosa-alabama','huntsville-alabama','st-louis-missouri','shreveport-louisiana','louisville-kentucky']]
NEARBY['lexington-kentucky'] = [A+x for x in ['louisville-kentucky','knoxville-tennessee','huntington-west-virginia','charleston-west-virginia','cincinnati-ohio','indianapolis-indiana','charlotte-north-carolina','owensboro-kentucky']]
# the four lists that were under 8 are re-cut explicitly (an unguarded append here would stack a copy on every import,
# because _load_nearby() seeds NEARBY from the finished pages)
NEARBY['las-cruces-new-mexico'] = [A+x for x in ['el-paso-texas','albuquerque-new-mexico','tucson-arizona','phoenix-arizona','denver-colorado','san-antonio-texas','santa-fe-new-mexico','rio-rancho-new-mexico']]
NEARBY['huntsville-alabama'] = [A+x for x in ['tuscaloosa-alabama','montgomery-alabama','atlanta-georgia','louisville-kentucky','lexington-kentucky','mobile-alabama','memphis-tennessee','knoxville-tennessee']]
NEARBY['new-haven-connecticut'] = [A+x for x in ['bridgeport-connecticut','hartford-connecticut','waterbury-connecticut','norwalk-connecticut','stamford-connecticut','boston-massachusetts','cranston-rhode-island','pawtucket-rhode-island']]
NEARBY['henderson-nevada'] = [A+x for x in ['las-vegas-nevada','phoenix-arizona','gilbert-arizona','salt-lake-city-utah','riverside-california','sparks-nevada','carson-city-nevada']]

# ---- Batch 51 (Nov 9, 2026): Lancaster (PA); Harrisburg (PA); Cary (NC); Chattanooga (TN); Morgantown (WV); Kent (WA); Spokane Valley (WA) ----
#      NOTE: all five states already carry City Pages blocks (Allentown/Bethlehem/Erie/Philadelphia/Pittsburgh/Reading;
#      Charlotte/Durham/Fayetteville/Greensboro/Raleigh/Winston-Salem; Memphis/Knoxville; Charleston/Huntington;
#      Bellevue/Seattle/Spokane/Vancouver), so this batch adds no hub block. Windows: Morgantown "2–4 Days" (the WV
#      pass-through figure used by Charleston and Huntington), the other six "1–3 Days". The Chattanooga row spelled the
#      state "Tenneesee" again (flagged, used as given). Name collisions: "Lancaster" is also a Reading street (Lancaster
#      Pike) and a Philadelphia avenue, "Kent" is a Seattle staging yard in prose and a county in DE and MI, "Spokane
#      Valley" must stay a full phrase (the Spokane page says "the Valley" alone) — neighbor links read the mention first.
register('auto-transport-lancaster-pennsylvania', 'Lancaster', 'PA')
register('auto-transport-harrisburg-pennsylvania', 'Harrisburg', 'PA')
register('auto-transport-cary-north-carolina', 'Cary', 'NC')
register('auto-transport-chattanooga-tennessee', 'Chattanooga', 'TN')
register('auto-transport-morgantown-west-virginia', 'Morgantown', 'WV')
register('auto-transport-kent-washington', 'Kent', 'WA')
register('auto-transport-spokane-valley-washington', 'Spokane Valley', 'WA')
_s('lancaster-pennsylvania', [A+x for x in ['harrisburg-pennsylvania','reading-pennsylvania','philadelphia-pennsylvania','allentown-pennsylvania','bethlehem-pennsylvania','wilmington-delaware','baltimore-maryland','columbia-maryland']])
_s('harrisburg-pennsylvania', [A+x for x in ['lancaster-pennsylvania','reading-pennsylvania','allentown-pennsylvania','bethlehem-pennsylvania','philadelphia-pennsylvania','pittsburgh-pennsylvania','baltimore-maryland','columbia-maryland']])
_s('cary-north-carolina', [A+x for x in ['raleigh-north-carolina','durham-north-carolina','fayetteville-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','charlotte-north-carolina','richmond-virginia','virginia-beach-virginia']])
_s('chattanooga-tennessee', [A+x for x in ['knoxville-tennessee','atlanta-georgia','huntsville-alabama','athens-georgia','macon-georgia','tuscaloosa-alabama','memphis-tennessee','lexington-kentucky']])
_s('morgantown-west-virginia', [A+x for x in ['pittsburgh-pennsylvania','charleston-west-virginia','huntington-west-virginia','columbus-ohio','akron-ohio','cleveland-ohio','germantown-maryland','baltimore-maryland']])
_s('kent-washington', [A+x for x in ['seattle-washington','bellevue-washington','vancouver-washington','portland-oregon','spokane-washington','spokane-valley-washington','salem-oregon','boise-idaho']])
_s('spokane-valley-washington', [A+x for x in ['spokane-washington','seattle-washington','bellevue-washington','kent-washington','missoula-montana','boise-idaho','meridian-idaho','portland-oregon']])
# explicit re-cuts (8 max; explicit lists, never appends — _load_nearby() seeds NEARBY from the finished pages on import)
NEARBY['allentown-pennsylvania'] = [A+x for x in ['philadelphia-pennsylvania','bethlehem-pennsylvania','reading-pennsylvania','harrisburg-pennsylvania','lancaster-pennsylvania','manhattan-new-york','newark-new-jersey','wilmington-delaware']]
NEARBY['bethlehem-pennsylvania'] = [A+x for x in ['allentown-pennsylvania','reading-pennsylvania','philadelphia-pennsylvania','harrisburg-pennsylvania','lancaster-pennsylvania','newark-new-jersey','manhattan-new-york','wilmington-delaware']]
NEARBY['reading-pennsylvania'] = [A+x for x in ['philadelphia-pennsylvania','allentown-pennsylvania','lancaster-pennsylvania','harrisburg-pennsylvania','bethlehem-pennsylvania','wilmington-delaware','baltimore-maryland','pittsburgh-pennsylvania']]
NEARBY['philadelphia-pennsylvania'] = [A+x for x in ['wilmington-delaware','allentown-pennsylvania','bethlehem-pennsylvania','reading-pennsylvania','lancaster-pennsylvania','harrisburg-pennsylvania','newark-new-jersey','baltimore-maryland']]
NEARBY['pittsburgh-pennsylvania'] = [A+x for x in ['philadelphia-pennsylvania','harrisburg-pennsylvania','morgantown-west-virginia','erie-pennsylvania','cleveland-ohio','akron-ohio','columbus-ohio','buffalo-new-york']]
NEARBY['wilmington-delaware'] = [A+x for x in ['philadelphia-pennsylvania','dover-delaware','baltimore-maryland','lancaster-pennsylvania','reading-pennsylvania','allentown-pennsylvania','newark-new-jersey','columbia-maryland']]
NEARBY['germantown-maryland'] = [A+x for x in ['columbia-maryland','baltimore-maryland','wilmington-delaware','philadelphia-pennsylvania','dover-delaware','harrisburg-pennsylvania','lancaster-pennsylvania','richmond-virginia']]
NEARBY['raleigh-north-carolina'] = [A+x for x in ['cary-north-carolina','durham-north-carolina','charlotte-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','fayetteville-north-carolina','richmond-virginia','virginia-beach-virginia']]
NEARBY['durham-north-carolina'] = [A+x for x in ['raleigh-north-carolina','cary-north-carolina','charlotte-north-carolina','fayetteville-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','virginia-beach-virginia','richmond-virginia']]
NEARBY['fayetteville-north-carolina'] = [A+x for x in ['raleigh-north-carolina','cary-north-carolina','durham-north-carolina','charlotte-north-carolina','greensboro-north-carolina','winston-salem-north-carolina','columbia-south-carolina','richmond-virginia']]
NEARBY['greensboro-north-carolina'] = [A+x for x in ['winston-salem-north-carolina','durham-north-carolina','raleigh-north-carolina','cary-north-carolina','charlotte-north-carolina','fayetteville-north-carolina','richmond-virginia','columbia-south-carolina']]
NEARBY['knoxville-tennessee'] = [A+x for x in ['chattanooga-tennessee','memphis-tennessee','lexington-kentucky','louisville-kentucky','cincinnati-ohio','atlanta-georgia','huntsville-alabama','charlotte-north-carolina']]
NEARBY['atlanta-georgia'] = [A+x for x in ['chattanooga-tennessee','athens-georgia','macon-georgia','augusta-georgia','columbus-georgia','charlotte-north-carolina','tuscaloosa-alabama','jacksonville-florida']]
NEARBY['huntsville-alabama'] = [A+x for x in ['chattanooga-tennessee','tuscaloosa-alabama','montgomery-alabama','atlanta-georgia','memphis-tennessee','knoxville-tennessee','louisville-kentucky','lexington-kentucky']]
NEARBY['athens-georgia'] = [A+x for x in ['atlanta-georgia','augusta-georgia','macon-georgia','chattanooga-tennessee','charlotte-north-carolina','savannah-georgia','columbus-georgia']]
NEARBY['macon-georgia'] = [A+x for x in ['atlanta-georgia','columbus-georgia','savannah-georgia','augusta-georgia','athens-georgia','chattanooga-tennessee','jacksonville-florida','charleston-south-carolina']]
NEARBY['charleston-west-virginia'] = [A+x for x in ['huntington-west-virginia','morgantown-west-virginia','columbus-ohio','lexington-kentucky','cincinnati-ohio','pittsburgh-pennsylvania','dayton-ohio','louisville-kentucky']]
NEARBY['huntington-west-virginia'] = [A+x for x in ['charleston-west-virginia','morgantown-west-virginia','lexington-kentucky','cincinnati-ohio','columbus-ohio','louisville-kentucky','dayton-ohio','pittsburgh-pennsylvania']]
NEARBY['seattle-washington'] = [A+x for x in ['bellevue-washington','kent-washington','spokane-washington','spokane-valley-washington','portland-oregon','vancouver-washington','eugene-oregon','boise-idaho']]
NEARBY['bellevue-washington'] = [A+x for x in ['seattle-washington','kent-washington','portland-oregon','vancouver-washington','spokane-washington','spokane-valley-washington','eugene-oregon','boise-idaho']]
NEARBY['spokane-washington'] = [A+x for x in ['spokane-valley-washington','seattle-washington','bellevue-washington','kent-washington','boise-idaho','meridian-idaho','missoula-montana','portland-oregon']]
NEARBY['vancouver-washington'] = [A+x for x in ['portland-oregon','salem-oregon','seattle-washington','kent-washington','bellevue-washington','spokane-washington','eugene-oregon','boise-idaho']]
NEARBY['missoula-montana'] = [A+x for x in ['bozeman-montana','great-falls-montana','billings-montana','spokane-washington','spokane-valley-washington','seattle-washington','boise-idaho','meridian-idaho']]

# ---- Oct 27, 2026 SEO pass: the legacy Corpus Christi page (old-generation template, pending a rebuild row)
#      is registered so the hub, the Texas City Pages block, the sitemap and the counts include it. It is NOT
#      rebuilt by localpage (no builder); patches/seo_pass_2026_10.py left its own breadcrumb/schema in place.
register('auto-transport-corpus-christi-texas', 'Corpus Christi', 'TX')
