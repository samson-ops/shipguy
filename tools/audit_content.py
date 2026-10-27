"""Content-rule audit for city/state pages.
usage: python3 audit_content.py <page.html> [...]   (paths relative to the site root or absolute)
Checks: sentences <= 18 words, broker disclosure in the first 2 intro sentences, banned tokens
(e.g. / U.S. / Dr. / St. / vs. / semicolons) in prose, over-claims, one H1, FAQPage JSON-LD valid, GTM x2,
one canonical, meta length, title length."""
import sys, re, json, html, os

SITE = '/home/claude/build/shipguy'
BANNED = [('e.g.', r'\be\.g\.'), ('U.S.', r'\bU\.S\.'), ('Dr.', r'\bDr\.'), ('St.', r'\bSt\.'), ('vs.', r'\bvs\.'), (';', r';')]
CLAIMS = ['24/7', 'no deposit', 'pay nothing', 'cheapest company', '#1 ', 'number one', 'guarantee']

def sents(text):
    t = re.sub(r'<[^>]+>', ' ', text); t = html.unescape(t); t = re.sub(r'\s+', ' ', t); t = re.sub(r'\s+([,.;:!?])', r'\1', t)  # a comma right after </a> is not a word; t = re.sub(r"\s+(’s|'s)\b", r'\1', t)  # </a>’s stays one word
    t = re.sub(r'\bSt\. (?=[A-Z])', 'St ', t)   # St. Louis / St. Charles are names, not sentence ends
    return [x.strip() for x in re.split(r'(?<=[.?!])\s+', t) if x.strip()]

def prose_units(body):
    out = []
    for m in re.finditer(r'<p(?: class="ph-(?!eyebrow)[a-z-]+")?>(.*?)</p>|<li>(?:<svg.*?</svg>)?<span>(.*?)</span></li>|<div class="ph-note">(.*?)</div>|<summary>(.*?)<span class="ph-fp">', body, flags=re.S):
        out.append(next(g for g in m.groups() if g is not None))
    return out

def audit(path):
    p = path if os.path.isabs(path) else os.path.join(SITE, path)
    h = open(p, encoding='utf-8').read()
    issues = []
    a = h.index('<section class="ph-stats">'); b = h.index('<footer')
    body = re.sub(r'<style.*?</style>', '', h[a:b], flags=re.S)
    units = prose_units(body)
    S = [x for u in units for x in sents(u)]
    over = [x for x in S if len(x.split()) > 18]
    for x in over: issues.append(('long-sentence(%d)' % len(x.split()), x))
    intro = [x for u in units[:3] for x in sents(u)]
    if not any('licensed auto transport broker' in x.lower() for x in intro[:2]): issues.append(('disclosure-not-in-first-2', intro[:2]))
    flat = ' '.join(S)
    for tok, rx in BANNED:
        for m in re.finditer(rx, flat): issues.append(('banned-token ' + tok, flat[max(0, m.start() - 40):m.end() + 30]))
    low = body.lower()
    for kw in CLAIMS:
        if kw in low and not (kw == 'guarantee' and 'no guarantee' in low): issues.append(('over-claim', kw))
    if h.count('<h1') != 1: issues.append(('h1-count', h.count('<h1')))
    if h.count('GTM-MQ7HKJTJ') != 2: issues.append(('gtm', h.count('GTM-MQ7HKJTJ')))
    if h.count('rel="canonical"') != 1: issues.append(('canonical', h.count('rel="canonical"')))
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, flags=re.S):
        try:
            d = json.loads(blk)
            if d.get('@type') == 'FAQPage':
                # schema answers must mirror on-page text
                page_q = re.findall(r'<summary>(.*?)<span class="ph-fp">', body, flags=re.S)
                if len(page_q) != len(d['mainEntity']): issues.append(('faq-count-mismatch', (len(page_q), len(d['mainEntity']))))
        except Exception as e: issues.append(('bad-jsonld', str(e)[:60]))
    if 'FAQPage' not in h: issues.append(('faq-schema-missing', ''))
    t = re.search(r'<title>(.*?)</title>', h, flags=re.S).group(1)
    if not 30 <= len(t) <= 65: issues.append(('title-length', len(t)))
    m = re.search(r'<meta name="description" content="([^"]*)"', h).group(1)
    if not 110 <= len(m) <= 160: issues.append(('meta-length', len(m)))
    if 'AggregateRating' in h or '"Review"' in h: issues.append(('review-schema', ''))
    words = sum(len(x.split()) for x in S)
    return words, issues

if __name__ == '__main__':
    allok = True
    for path in sys.argv[1:]:
        words, issues = audit(path)
        print('%-55s prose words %4d | %s' % (path, words, 'CLEAR' if not issues else '%d issue(s)' % len(issues)))
        for k, v in issues: print('     ', k, '|', (v if isinstance(v, str) else repr(v))[:160]); allok = False
    sys.exit(0 if allok else 1)
