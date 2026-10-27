#!/usr/bin/env python3
"""Rebuild a page's FAQPage JSON-LD from its on-page <details class="ph-faq"> list.
Usage: python3 resync_faq.py page.html [page2.html ...]
Edit the on-page FAQ first, then run this so the schema mirrors the visible text (tags stripped)."""
import re, sys, json, html as H

def resync(path):
    h = open(path, encoding='utf-8').read()
    strip = lambda s: H.unescape(re.sub(r'<[^>]+>', '', s)).strip()
    faqs = []
    for q, a in re.findall(r'<details class="ph-faq"><summary>(.*?)<span class="ph-fp"></span></summary><div class="fa">(.*?)</div></details>', h, re.S):
        paras = [strip(x) for x in re.findall(r'<p>(.*?)</p>', a, re.S)] or [strip(a)]
        faqs.append({"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": " ".join(paras)}})
    m = re.search(r'(<script type="application/ld\+json">\s*)(\{"@context": "https://schema.org", "@type": "FAQPage".*?\})(\s*</script>)', h, re.S)
    assert m and faqs, path
    old = json.loads(m.group(2))
    assert len(old['mainEntity']) == len(faqs), (path, len(old['mainEntity']), len(faqs))
    new = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faqs}, ensure_ascii=False)
    changed = new != m.group(2)
    if changed:
        h = h[:m.start(2)] + new + h[m.end(2):]
        open(path, 'w', encoding='utf-8').write(h)
    print(('resynced ' if changed else 'already in sync ') + path + ' (%d questions)' % len(faqs))

if __name__ == '__main__':
    for p in sys.argv[1:]:
        resync(p)
