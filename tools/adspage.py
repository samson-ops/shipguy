#!/usr/bin/env python3
"""Google Ads landing-page builder (Oct 28, 2026).

Derives a city-focused copy of the /vehicle-quote page: same quote tool, same /api/quote proxy (the
vehicle-quote BeRocker lead source), same GTM container, plus
  * a city phone line on every tel: link (header, hero call block, quote result, consent text, how/CTA band,
    footer, mobile sticky bar), each tagged with data-track="call-<location>"
  * city hero copy (broker disclosure in the lede), city lanes table, pickup/access cards, city FAQ (+FAQPage
    JSON-LD generated from the same data), Miami-flavoured how-it-works and CTA band
  * Ads hooks: dataLayer events (lp_view, call_click, quote_step, quote_submit, quote_lead, quote_price,
    quote_redirect, quote_error), gclid/gbraid/wbraid/utm capture (90-day localStorage) written into the
    lead's customer_comments, `?v=` whitelisted headline variants, a 900 ms floor between quote_lead and the
    booking redirect so the conversion tag has time to fire
  * noindex,follow (the SEO page for the city is /city/<slug>/; this one is paid traffic only)
Usage: a config module in builders_ads/ calls build(CFG). The base is read from the live build tree so the
quote tool's JS stays the single source; every edit is an asserted replacement, so a changed base fails loudly.
"""
import re, json, html as H, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_content import sents, BANNED, CLAIMS

SITE = '/home/claude/build/shipguy/'
BASE = SITE + 'vehicle-quote.html'
BASE_TEL = 'tel:+18662973244'
BASE_DISP = '(866) 297-3244'
BASE_TITLE = 'Instant Car Shipping Quote | Ship Guy — Nationwide Auto Transport'
BASE_DESC = 'Get an instant vehicle shipping quote from Ship Guy — licensed, insured nationwide auto transport with transparent pricing, vetted carriers. Free quote.'
STAR = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.5l2.9 6.06 6.6.79-4.86 4.53 1.27 6.52L12 17.9l-5.9 3.5 1.27-6.52L2.5 9.35l6.6-.79L12 2.5Z"/></svg>'
CHEV = '<span class="faq-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg></span>'
PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>'
ICONS = {
  'bolt': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4.5 13.5H11l-1 8.5L19.5 10H13l1-8Z"/></svg>',
  'truck': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M10 17h4V5H2v12h3"/><path d="M20 17h2v-3.3a4 4 0 0 0-1.2-2.9L19 9h-5v8h1"/><circle cx="7.5" cy="17.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg>',
  'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
  'tower': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V5a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v16"/><path d="M14 9h5a1 1 0 0 1 1 1v11"/><path d="M2 21h20"/><path d="M7 8h2M7 12h2M7 16h2M17 13h1M17 17h1"/></svg>',
  'bridge': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20"/><path d="M4 12V8M20 12V8M8 12V7M16 12V7M12 12V6"/><path d="M2 8c3-3 7-4 10-4s7 1 10 4"/><path d="M4 12v6M20 12v6"/></svg>',
  'gate': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/><circle cx="12" cy="16" r="1.4"/></svg>',
  'home': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11 12 3l9 8"/><path d="M5 10v10a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V10"/></svg>',
  'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
  'doc': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M17 21H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h7l5 5v11a2 2 0 0 1-2 2Z"/><path d="M9 13h6M9 17h4"/></svg>',
  'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><path d="m9 10 2 2 4-4"/></svg>',
}

def rep(h, old, new, n=1):
    c = h.count(old); assert c == n, ('expected %d, found %d' % (n, c), old[:90]); return h.replace(old, new)

def _text(s):
    return H.unescape(re.sub(r'<[^>]+>', ' ', s))

def _stars(n=5):
    return STAR * n

# ----------------------------------------------------------------------------------------------- sections
def hero_badges(cfg):
    out = []
    for ic, b, s in cfg['badges']:
        out.append('<div class="hb"><span class="hb-ic">%s</span><span><b>%s</b><small>%s</small></span></div>' % (ICONS[ic], b, s))
    return '<div class="hero-badges reveal d3">\n        %s\n      </div>' % '\n        '.join(out)

def lanes_section(cfg):
    rows = ''.join('<tr><td>%s</td><td class="sg-hide-m">%s</td><td>%s</td><td>%s</td></tr>' % r for r in cfg['lanes'])
    return ('<section class="sg-lanes" id="lanes">\n  <div class="container">\n    <div class="lp-head">\n      <p class="lp-eyebrow">%s</p>\n      <h2>%s</h2>\n      <p class="lp-sub">%s</p>\n    </div>\n'
            '    <div class="sg-table-wrap"><table class="sg-table"><thead><tr><th>Route</th><th class="sg-hide-m">Corridor &middot; distance</th><th>Est. transit</th><th>Est. open rate*</th></tr></thead><tbody>%s</tbody></table></div>\n'
            '    <p class="sg-foot">%s</p>\n    <p class="sg-lanes-note">%s</p>\n  </div>\n</section>\n') % (
            cfg['lanes_eyebrow'], cfg['lanes_h2'], cfg['lanes_sub'], rows, cfg['lanes_foot'], cfg['lanes_note'])

def access_section(cfg):
    cards = ''.join('<div class="sg-card"><span class="ic">%s</span><h3>%s</h3><p>%s</p></div>' % (ICONS[ic], t, p) for ic, t, p in cfg['access_cards'])
    chips = ''.join('<span class="sg-chip">%s</span>' % c for c in cfg['neighborhoods'])
    return ('<section class="sg-access" id="pickup">\n  <div class="container">\n    <div class="lp-head">\n      <p class="lp-eyebrow">%s</p>\n      <h2>%s</h2>\n      <p class="lp-sub">%s</p>\n    </div>\n'
            '    <div class="sg-cards">%s</div>\n    <div class="sg-chips">%s</div>\n    <p class="sg-chips-cap">%s</p>\n    <p class="sg-season">%s</p>\n  </div>\n</section>\n') % (
            cfg['access_eyebrow'], cfg['access_h2'], cfg['access_sub'], cards, chips, cfg['chips_cap'], cfg['season'])

def how_section(cfg):
    ics = ['doc', 'truck', 'shield']
    steps = ''.join('<div class="lp-step"><span class="lp-num">%d</span><span class="lp-ic">%s</span><h3>%s</h3><p>%s</p></div>' % (i + 1, ICONS[ics[i]], t, p) for i, (t, p) in enumerate(cfg['how_steps']))
    return ('<!-- ===================== HOW IT WORKS ===================== -->\n<section class="lp-how" id="how">\n  <div class="container">\n    <div class="lp-head">\n      <p class="lp-eyebrow">How It Works</p>\n      <h2>%s</h2>\n      <p class="lp-sub">%s</p>\n    </div>\n    <div class="lp-steps">\n      %s\n    </div>\n'
            '    <div class="lp-how-cta"><a class="lp-btn" href="#top">%s</a><span>or call <a data-track="call-how" href="tel:%s">%s</a></span></div>\n  </div>\n</section>\n') % (
            cfg['how_h2'], cfg['how_sub'], steps, cfg['cta_btn'], cfg['tel'], cfg['disp_nbsp'])

def faq_section(cfg):
    items = []
    for i, (q, a) in enumerate(cfg['faq']):
        items.append('      <details class="faq-item"%s>\n        <summary class="faq-q">%s\n          %s\n        </summary>\n        <div class="faq-a">%s</div>\n      </details>' % (' open' if i == 0 else '', q, CHEV, a))
    return ('<!-- ===================== FAQ ===================== -->\n<section class="faq-section" id="faq">\n  <div class="container">\n    <div class="faq-head">\n      <p class="faq-eyebrow">Questions?</p>\n      <h2>%s</h2>\n      <span class="faq-accent" aria-hidden="true"></span>\n      <p class="faq-sub">%s</p>\n    </div>\n\n    <div class="faq-list">\n%s\n    </div>\n  </div>\n</section>\n\n') % (
            cfg['faq_h2'], cfg['faq_sub'], '\n\n'.join(items))

def faq_ld(cfg):
    d = {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": _text(q).strip(), "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'\s+', ' ', _text(a)).strip()}} for q, a in cfg['faq']]}
    return '<script type="application/ld+json">%s</script>' % json.dumps(d, ensure_ascii=False)

CSS = r'''<style id="sg-ads-css">
.hero-rating{display:inline-flex;align-items:center;gap:7px;margin:12px 0 0;text-decoration:none;color:var(--ink-2);font-size:14px;font-weight:600}
.hero-rating .hr-stars{display:inline-flex;gap:1px}.hero-rating .hr-stars svg{width:15px;height:15px;color:var(--star)}
.hero-rating b{color:var(--ink);font-size:15px}.hero-rating:hover span.hr-txt{text-decoration:underline}
.hours-dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:#b8c0d6;margin-right:6px;vertical-align:1px}
.hours-dot.is-open{background:#17a85b;box-shadow:0 0 0 3px rgba(23,168,91,.18)}
#pquote{scroll-margin-top:84px}
.sg-lanes{background:var(--bg-soft);padding:64px 0}.sg-lanes .lp-head{margin-bottom:28px}
.sg-table-wrap{max-width:900px;margin:0 auto;background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden;box-shadow:0 14px 34px -28px rgba(13,26,80,.35)}
.sg-table{width:100%;border-collapse:collapse;font-size:15px}
.sg-table th{background:var(--brand-tint);color:var(--ink);font-family:var(--font-display);font-weight:800;font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;text-align:left;padding:12px 16px}
.sg-table td{padding:12px 16px;border-top:1px solid var(--line);color:var(--ink-2);vertical-align:top}
.sg-table td:first-child{color:var(--ink);font-weight:600}.sg-table td:last-child{font-weight:700;color:var(--brand-deep);white-space:nowrap}
.sg-foot{max-width:900px;margin:14px auto 0;color:var(--muted);font-size:13.5px;line-height:1.55}
.sg-lanes-note{max-width:900px;margin:18px auto 0;color:var(--ink-2);font-size:15.5px;line-height:1.6}
.sg-access{background:#fff;padding:64px 0}
.sg-cards{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;max-width:980px;margin:0 auto}
.sg-card{border:1px solid var(--line);border-radius:16px;padding:20px 22px;background:#fff;box-shadow:0 10px 30px -26px rgba(13,26,80,.4)}
.sg-card h3{margin:0 0 8px;font-family:var(--font-display);font-size:17px;color:var(--ink)}
.sg-card p{margin:0;color:var(--ink-2);font-size:15px;line-height:1.6}
.sg-card .ic{width:38px;height:38px;border-radius:10px;background:var(--brand-tint);color:var(--brand);display:flex;align-items:center;justify-content:center;margin-bottom:12px}
.sg-card .ic svg{width:20px;height:20px}
.sg-chips{display:flex;flex-wrap:wrap;gap:8px;max-width:980px;margin:26px auto 0}
.sg-chip{display:inline-block;padding:7px 12px;border-radius:999px;background:var(--bg-soft);border:1px solid var(--line);color:var(--ink);font-size:13.5px;font-weight:600}
.sg-chips-cap{max-width:980px;margin:12px auto 0;color:var(--muted);font-size:13.5px}
.sg-season{max-width:980px;margin:26px auto 0;border-left:4px solid var(--brand);background:var(--brand-tint);border-radius:0 14px 14px 0;padding:14px 18px;color:var(--ink);font-size:15px;line-height:1.6}
.sg-sticky{display:none}
@media (max-width:760px){
  .sg-sticky{position:fixed;left:0;right:0;bottom:0;z-index:60;display:flex;gap:8px;padding:10px 12px calc(10px + env(safe-area-inset-bottom));background:rgba(255,255,255,.97);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-top:1px solid var(--line);box-shadow:0 -8px 24px rgba(13,26,80,.12);transform:translateY(110%);transition:transform .25s ease}
  .sg-sticky.show{transform:none}
  .sg-sticky a{flex:1;display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:13px 10px;border-radius:12px;font-family:var(--font-display);font-weight:800;font-size:15px;text-decoration:none;white-space:nowrap}
  .sg-sticky a svg{width:18px;height:18px}
  .sg-sticky-call{background:var(--brand);color:#fff}.sg-sticky-quote{background:var(--brand-tint);color:var(--brand-deep);border:1px solid #c9d6fb}
  body.has-sticky{padding-bottom:74px}
  .sg-cards{grid-template-columns:1fr}
}
@media (max-width:600px){.sg-table{font-size:13.5px}.sg-table th,.sg-table td{padding:10px 10px}.sg-table .sg-hide-m{display:none}.sg-lanes,.sg-access{padding:46px 0}}
</style>'''

def sticky_bar(cfg):
    return ('<div class="sg-sticky" id="sgSticky" aria-hidden="true"><a class="sg-sticky-call" data-track="call-sticky" href="tel:%s">%sCall %s</a>'
            '<a class="sg-sticky-quote" href="#pquote">Get my quote</a></div>\n') % (cfg['tel'], PHONE_SVG, cfg['disp_nbsp'])

def ads_script(cfg):
    variants = json.dumps(cfg['variants'], ensure_ascii=False)
    return r'''<script>
/* Ads landing-page hooks: gclid/utm capture, dataLayer events, hours indicator, step counter, sticky bar */
(function(){
  var dl=window.dataLayer=window.dataLayer||[];
  var LP='%(slug)s', KEYS=['gclid','gbraid','wbraid','utm_source','utm_medium','utm_campaign','utm_term','utm_content'];
  var q={}; try{ location.search.replace(/^\?/,'').split('&').forEach(function(kv){ if(!kv) return; var p=kv.split('='); q[decodeURIComponent(p[0])]=decodeURIComponent((p[1]||'').replace(/\+/g,' ')); }); }catch(e){}
  var saved={}; try{ saved=JSON.parse(localStorage.getItem('sg_ads')||'{}')||{}; }catch(e){ saved={}; }
  if(saved.ts && Date.now()-saved.ts > 90*864e5) saved={};
  var fresh=false; KEYS.forEach(function(k){ if(q[k]){ saved[k]=String(q[k]).slice(0,200); fresh=true; } });
  if(fresh){ saved.ts=Date.now(); saved.lp=LP; try{ localStorage.setItem('sg_ads',JSON.stringify(saved)); }catch(e){} }
  var v=window.sgVariant||'default';
  window.sgAds={variant:v, params:saved, note:function(){
    var parts=['Landing page: /'+LP]; if(v!=='default') parts.push('variant='+v);
    KEYS.forEach(function(k){ if(saved[k]) parts.push(k+'='+saved[k]); }); return parts.join(' | ')+'.';
  }};
  dl.push({event:'lp_view', page_variant:v, ads_gclid:saved.gclid||'', ads_campaign:saved.utm_campaign||'', ads_source:saved.utm_source||''});

  /* every tel: link on the page, by location */
  document.addEventListener('click', function(e){
    var t=e.target; while(t && t.nodeType===1 && !(t.tagName==='A' && /^tel:/i.test(t.getAttribute('href')||''))) t=t.parentNode;
    if(!t || t.nodeType!==1) return;
    dl.push({event:'call_click', call_location:t.getAttribute('data-track')||'call-other', phone:(t.getAttribute('href')||'').replace(/^tel:/i,''), page_variant:v});
  }, true);

  /* hours indicator (%(hours_open)d:00-%(hours_close)d:00 %(tz_label)s, seven days) */
  try{
    var f=new Intl.DateTimeFormat('en-US',{timeZone:'%(tz)s',hour:'numeric',hour12:false});
    var hr=parseInt(f.format(new Date()),10); if(hr===24) hr=0;
    var open=hr>=%(hours_open)d && hr<%(hours_close)d, el=document.getElementById('hoursNow'), dot=document.getElementById('hoursDot');
    if(el){ el.textContent=open?'Open now · real people until %(close_label)s %(tz_label)s':'Closed now · opens %(open_label)s %(tz_label)s, quote online any time'; }
    if(dot){ dot.classList.toggle('is-open', open); }
  }catch(e){}

  /* "Step N of 3" on the quote card */
  var card=document.getElementById('pquote'), sc=document.getElementById('pqStepCount');
  if(card && sc){
    var panels=card.querySelectorAll('.pq-panel');
    var upd=function(){ var i=0; for(var x=0;x<panels.length;x++){ if(panels[x].classList.contains('is-current')) i=x; } sc.textContent='Step '+(i+1)+' of '+panels.length+' · free, no obligation'; };
    if(window.MutationObserver) new MutationObserver(upd).observe(card,{attributes:true,subtree:true,attributeFilter:['class']});
    upd();
  }

  /* mobile sticky bar once the quote card scrolls away */
  var bar=document.getElementById('sgSticky');
  if(bar && card && 'IntersectionObserver' in window){
    var vis=true, tick=function(){ var on=!vis && window.scrollY>240; bar.classList.toggle('show',on); bar.setAttribute('aria-hidden',on?'false':'true'); document.body.classList.toggle('has-sticky',on); };
    new IntersectionObserver(function(es){ for(var i=0;i<es.length;i++) vis=es[i].isIntersecting; tick(); },{threshold:0.05}).observe(card);
    window.addEventListener('scroll', tick, {passive:true});
  }
})();
</script>
''' % dict(slug=cfg['slug'], tz=cfg['tz'], tz_label=cfg['tz_label'], hours_open=cfg['hours_open'], hours_close=cfg['hours_close'],
           open_label=cfg['open_label'], close_label=cfg['close_label'])

def variant_script(cfg):
    return ('<script>(function(){var V=%s;var m=/[?&]v=([a-z-]+)/.exec(location.search);var v=m&&V[m[1]]?m[1]:\'default\';window.sgVariant=v;'
            'if(v!==\'default\'){var h=document.getElementById(\'heroH1\');if(!h)return;h.textContent=\'\';h.appendChild(document.createTextNode(V[v][0]));h.appendChild(document.createElement(\'br\'));'
            'h.appendChild(document.createTextNode(V[v][1]));var s=document.createElement(\'span\');s.className=\'accent\';s.textContent=V[v][2];h.appendChild(s);}})();</script>') % json.dumps(cfg['variants'], ensure_ascii=False)

# ----------------------------------------------------------------------------------------------- build
def build(cfg):
    h = open(BASE, encoding='utf-8').read()
    base_index = open(SITE + 'vehicle-quote/index.html', encoding='utf-8').read()
    assert h == base_index, 'vehicle-quote.html and vehicle-quote/index.html differ'
    url = 'https://shipguy.com/' + cfg['slug']

    # ---- phone line everywhere
    h = rep(h, BASE_TEL, 'tel:' + cfg['tel'], 7)
    h = rep(h, BASE_DISP.replace(' ', '&nbsp;'), cfg['disp_nbsp'], 3)
    h = rep(h, BASE_DISP, cfg['disp'], 5)
    assert '297-3244' not in h and '18662973244' not in h
    h = rep(h, '<a class="btn-call" href="tel:', '<a class="btn-call" data-track="call-header" href="tel:')
    h = rep(h, '<a class="pq-btn-ghost" id="pqCallBtn" href="tel:', '<a class="pq-btn-ghost" id="pqCallBtn" data-track="call-quote-result" href="tel:')
    h = rep(h, 'For support, call <a href="tel:', 'For support, call <a data-track="call-consent" href="tel:')
    h = rep(h, '<a class="cta-secondary" href="tel:', '<a class="cta-secondary" data-track="call-cta-band" href="tel:')
    h = rep(h, '<a class="lp-foot-call" href="tel:', '<a class="lp-foot-call" data-track="call-footer" href="tel:')

    # ---- head
    assert 30 <= len(cfg['title']) <= 65, len(cfg['title'])
    assert 110 <= len(cfg['meta']) <= 160, len(cfg['meta'])
    h = rep(h, BASE_TITLE, cfg['title'], 3)
    h = rep(h, BASE_DESC, cfg['meta'], 3)
    h = rep(h, '<link rel="canonical" href="https://shipguy.com/vehicle-quote">', '<link rel="canonical" href="%s">\n<meta name="robots" content="noindex, follow">' % url)
    h = rep(h, '<meta property="og:url" content="https://shipguy.com/vehicle-quote">', '<meta property="og:url" content="%s">' % url)
    h = rep(h, '</head>', faq_ld(cfg) + '\n' + CSS + '\n</head>')

    # ---- hero
    h = rep(h, '<p class="eyebrow reveal">Nationwide Auto Transport</p>', '<p class="eyebrow reveal">%s</p>' % cfg['eyebrow'])
    d = cfg['variants']['default']
    h = rep(h, '<h1 class="reveal d2">Get an Instant<br>Car Shipping <span class="accent">Quote</span></h1>',
            '<h1 class="reveal d2" id="heroH1">%s<br>%s<span class="accent">%s</span></h1>\n      %s\n      <a class="hero-rating reveal d2" href="#reviews" aria-label="Rated 4.9 out of 5, see customer reviews"><span class="hr-stars" aria-hidden="true">%s</span><b>4.9</b><span class="hr-txt">&middot; 487+ reviews</span></a>' % (
                H.escape(d[0], quote=False), H.escape(d[1], quote=False), H.escape(d[2], quote=False), variant_script(cfg), _stars()))
    h = rep(h, '<p class="lede reveal d2">Fully insured, door-to-door car shipping anywhere in the U.S. — fast, transparent pricing in seconds.</p>',
            '<p class="lede reveal d2">%s</p>' % cfg['lede'])
    h = re.sub(r'<div class="hero-badges reveal d3">.*?</div>\n      </div>', lambda m: hero_badges(cfg), h, count=1, flags=re.S)
    assert 'Fully Insured Transport' not in h
    h = rep(h, '<small>Prefer to talk? Call now</small>', '<small>%s</small>' % cfg['call_small'])
    h = rep(h, '<p class="hero-call-note">Real people, seven days a week &middot; Quotes in minutes &middot; No obligation</p>',
            '<p class="hero-call-note"><span class="hours-dot" id="hoursDot"></span><span id="hoursNow">%s</span> &middot; No obligation</p>' % cfg['hours_static'])

    # ---- quote card copy
    h = rep(h, '<p class="pq-sub">Fast, secure pricing in 30 seconds.</p>', '<p class="pq-sub">%s</p>' % cfg['pq_sub'])
    h = rep(h, '<span id="pqStepCount">Free &middot; No obligation</span>', '<span id="pqStepCount">Step 1 of 3 &middot; free, no obligation</span>')

    # ---- middle sections: reviews stay; how/why/faq are rebuilt (why is reused with its US-abbreviation lines fixed)
    why = re.search(r'<!-- ===================== WHY CHOOSE ===================== -->.*?</section>\n', h, re.S).group(0)
    why = rep(why, '<span>Dedicated U.S.-Based<br>Support</span>', '<span>Dedicated Phone<br>Support</span>')
    why = rep(why, '<p>Real, U.S.-based representatives by phone to guide your shipment.</p>', '<p>%s</p>' % cfg['why_support'])
    why = rep(why, '<h2>Why Choose Ship Guy</h2>', '<h2>%s</h2>' % cfg['why_h2'])
    why = rep(why, '<p class="wc-sub">A licensed, insured brokerage that treats your vehicle — and your time — like it matters.</p>', '<p class="wc-sub">%s</p>' % cfg['why_sub'])
    a = h.index('<!-- ===================== HOW IT WORKS ===================== -->'); b = h.index('<!-- ===================== FINAL CTA ===================== -->')
    h = h[:a] + lanes_section(cfg) + '\n' + access_section(cfg) + '\n' + how_section(cfg) + '\n' + why + '\n' + faq_section(cfg) + h[b:]
    h = rep(h, '<p>Trusted by vehicle owners nationwide.</p>', '<p>%s</p>' % cfg['reviews_sub'])

    # ---- CTA band + footer
    h = rep(h, '<h2>Ready to Ship Your Vehicle?</h2>', '<h2>%s</h2>' % cfg['cta_h2'])
    h = rep(h, '<p class="cta-sub">Get a free, no-obligation quote in about 60 seconds — or call and talk to a real specialist right now.</p>', '<p class="cta-sub">%s</p>' % cfg['cta_sub'])
    h = rep(h, '<a class="cta-primary" href="#top">\n        Get Your Free Quote', '<a class="cta-primary" href="#top">\n        %s' % cfg['cta_btn'])
    h = rep(h, '<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg> Dedicated support</li>',
            '<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg> %s</li>' % cfg['cta_trust3'])
    h = rep(h, '<p>Licensed &amp; insured nationwide car shipping &mdash; transparent pricing, vetted carriers, door to door.</p>', '<p>%s</p>' % cfg['foot_tag'])
    h = rep(h, '<span>Serving all 50 states</span>', '<span>%s</span>' % cfg['foot_serving'])
    h = rep(h, '</footer>\n', '</footer>\n' + sticky_bar(cfg))

    # ---- quote tool: tag the lead, fire the events, hold the redirect for the conversion tag
    h = rep(h, "secondary_id: 'WEB-'+Date.now(),", "secondary_id: '%s-'+Date.now()," % cfg['lead_prefix'])
    h = rep(h, "customer_comments: 'SMS consent: '+(data.sms_consent?'YES (opted in via web form)':'not given')+'.',",
            "customer_comments: 'SMS consent: '+(data.sms_consent?'YES (opted in via web form)':'not given')+'. '+((window.sgAds&&window.sgAds.note)?window.sgAds.note():''),")
    h = rep(h, "        var lead=res.body;\n", "        var lead=res.body;\n        try{ window.sgLeadAt=Date.now(); (window.dataLayer=window.dataLayer||[]).push({event:'quote_lead', lead_id:String(lead.id), transport:(data.transport||'Open'), timeframe:data.timeframe||data.date||'', page_variant:(window.sgAds&&window.sgAds.variant)||'default'}); }catch(e){}\n")
    h = rep(h, "if(res && res.bookingLink && !res.demo && (res.price || res.timedOut)){ setLoading('Taking you to your booking page...'); window.location.href=res.bookingLink; return; }",
            "if(res && res.bookingLink && !res.demo && (res.price || res.timedOut)){ setLoading('Taking you to your booking page...'); try{ (window.dataLayer=window.dataLayer||[]).push({event:'quote_redirect', price:res.price?String(res.price):''}); }catch(e){} var hold=Math.max(0, 900-(Date.now()-(window.sgLeadAt||0))); setTimeout(function(){ window.location.href=res.bookingLink; }, hold); return; }")
    h = rep(h, "  function render(res, data){\n    if(res && res.redirecting){ return; }\n",
            "  function render(res, data){\n    if(res && res.redirecting){ return; }\n    try{ (window.dataLayer=window.dataLayer||[]).push({event:'quote_price', price:(res&&res.price)?String(res.price):'', demo:!!(res&&res.demo), manual:!!(res&&res.manual), failed:!!(res&&res.failed), timed_out:!!(res&&res.timedOut)}); }catch(e){}\n")
    h = rep(h, "    var data={}; new FormData(form).forEach(function(v,k){data[k]=v;});\n",
            "    var data={}; new FormData(form).forEach(function(v,k){data[k]=v;});\n    try{ (window.dataLayer=window.dataLayer||[]).push({event:'quote_submit', transport:(data.transport||'Open'), timeframe:data.timeframe||data.date||''}); }catch(e){}\n")
    h = rep(h, "    }).catch(function(err){\n      // fall back to a sample estimate",
            "    }).catch(function(err){\n      try{ (window.dataLayer=window.dataLayer||[]).push({event:'quote_error', message:String((err&&err.message)||err).slice(0,120)}); }catch(e){}\n      // fall back to a sample estimate")
    h = rep(h, "form.querySelectorAll('[data-next]').forEach(function(b){b.addEventListener('click',function(){if(validate(cur))show(cur+1);});});",
            "form.querySelectorAll('[data-next]').forEach(function(b){b.addEventListener('click',function(){if(validate(cur)){show(cur+1); try{ (window.dataLayer=window.dataLayer||[]).push({event:'quote_step', step:cur+1}); }catch(e){}}});});")
    h = rep(h, '</body>', ads_script(cfg) + '</body>')

    out = SITE + cfg['slug'] + '.html'
    open(out, 'w', encoding='utf-8').write(h)
    return out, check(out, cfg)

# ----------------------------------------------------------------------------------------------- checks
def check(path, cfg):
    h = open(path, encoding='utf-8').read(); issues = []
    body = h[h.index('<body'):]
    vis = re.sub(r'<script.*?</script>|<style.*?</style>|<svg.*?</svg>', ' ', body, flags=re.S)
    vis = re.sub(r'<[^>]+>', ' ', vis); vis = H.unescape(re.sub(r'\s+', ' ', vis))
    scan = vis.replace('Dr. Phillips', 'Dr Phillips')   # a neighborhood name, not an abbreviation in prose
    for tok, rx in BANNED:
        for m in re.finditer(rx, scan): issues.append(('banned-token ' + tok, scan[max(0, m.start() - 50):m.end() + 30]))
    low = vis.lower()
    for kw in CLAIMS:
        if kw in low and not (kw == 'guarantee' and 'no guarantee' in low): issues.append(('over-claim', kw))
    # sentence length on everything the config authored + the sections built from it
    authored = [cfg['lede'], cfg['lanes_sub'], cfg['lanes_foot'], cfg['lanes_note'], cfg['access_sub'], cfg['chips_cap'], cfg['season'], cfg['how_sub'],
                cfg['why_sub'], cfg['why_support'], cfg['cta_sub'], cfg['reviews_sub'], cfg['foot_tag']]
    authored += [p for _, _, p in cfg['access_cards']] + [p for _, p in cfg['how_steps']] + [a for _, a in cfg['faq']] + [s for _, _, s in cfg['badges']]
    for u in authored:
        for s in sents(u):
            if len(s.split()) > 18: issues.append(('long-sentence(%d)' % len(s.split()), s))
    if not any('licensed auto transport broker' in s.lower() for s in sents(cfg['lede'])[:2]): issues.append(('disclosure-not-in-first-2', cfg['lede']))
    if h.count('GTM-MQ7HKJTJ') != 2: issues.append(('gtm', h.count('GTM-MQ7HKJTJ')))
    if h.count('rel="canonical"') != 1: issues.append(('canonical', h.count('rel="canonical"')))
    if h.count('<h1') != 1: issues.append(('h1-count', h.count('<h1')))
    if 'content="noindex, follow"' not in h: issues.append(('noindex-missing', ''))
    # FAQ JSON-LD mirrors the on-page FAQ
    ld = [json.loads(b) for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, flags=re.S)]
    faq = [d for d in ld if d.get('@type') == 'FAQPage']
    if len(faq) != 1: issues.append(('faq-schema-count', len(faq)))
    else:
        qs = [re.sub(r'\s+', ' ', _text(x)).strip() for x in re.findall(r'<summary class="faq-q">(.*?)<span class="faq-ic">', body, flags=re.S)]
        ans = [re.sub(r'\s+', ' ', _text(x)).strip() for x in re.findall(r'<div class="faq-a">(.*?)</div>', body, flags=re.S)]
        ent = faq[0]['mainEntity']
        if qs != [e['name'] for e in ent] or ans != [e['acceptedAnswer']['text'] for e in ent]: issues.append(('faq-mirror', (len(qs), len(ent))))
    for tag in ['div', 'section', 'details', 'table', 'ul', 'p', 'a', 'style', 'script', 'footer', 'header', 'nav', 'form', 'label', 'span', 'h2', 'h3']:
        if len(re.findall(r'<%s[\s>]' % tag, h)) != h.count('</%s>' % tag): issues.append(('tag-imbalance', tag))
    tels = set(re.findall(r'href="tel:([^"]+)"', h))
    if tels != {cfg['tel']}: issues.append(('tel-mismatch', sorted(tels)))
    untracked = re.findall(r'<a (?![^>]*data-track)[^>]*href="tel:', h)
    if untracked: issues.append(('tel-untracked', len(untracked)))
    for ev in ['lp_view', 'call_click', 'quote_step', 'quote_submit', 'quote_lead', 'quote_price', 'quote_redirect', 'quote_error']:
        if ("event:'%s'" % ev) not in h: issues.append(('event-missing', ev))
    return issues

if __name__ == '__main__':
    print(__doc__)
