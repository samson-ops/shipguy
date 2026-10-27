"""Verbatim-overlap check across every city AND state page.
usage: python3 overlap.py [N] [--list] [--all]
  N      : report the N most recently modified city/state pages (default 5); --all reports all
  --list : for each reported page, show the longest shared passages and which page they match
Metric: share of a page's 7-word shingles (prose only: paragraphs, list items, notes, FAQ) that also
appear on some other city or state page. Target: <= 8%."""
import sys, os, re, glob, html, collections

SITE = '/home/claude/build/shipguy'
N = 7

def prose_text(h):
    a = h.index('<section class="ph-stats">') if '<section class="ph-stats">' in h else h.index('<main') if '<main' in h else 0
    b = h.index('<footer') if '<footer' in h else len(h)
    body = re.sub(r'<style.*?</style>', '', h[a:b], flags=re.S)
    units = []
    for m in re.finditer(r'<p(?: class="ph-(?!eyebrow)[a-z-]+")?>(.*?)</p>|<li>(?:<svg.*?</svg>)?<span>(.*?)</span></li>|<div class="ph-note">(.*?)</div>|<summary>(.*?)<span class="ph-fp">', body, flags=re.S):
        units.append(next(g for g in m.groups() if g is not None))
    t = html.unescape(re.sub(r'<[^>]+>', ' ', ' . '.join(units)))
    t = re.sub(r'[^a-z0-9 ]+', ' ', t.lower())
    return t.split()

def shingles(words):
    return [tuple(words[i:i + N]) for i in range(len(words) - N + 1)]

def pages():
    out = {}
    for p in glob.glob(SITE + '/city/auto-transport-*/index.html'):
        out['city/' + p.split('/')[-2]] = p
    for p in glob.glob(SITE + '/*-auto-transport.html'):
        n = os.path.basename(p).replace('.html', '')
        if n != 'enclosed-auto-transport': out[n] = p
    return out

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    want_list = '--list' in sys.argv; want_all = '--all' in sys.argv
    P = pages()
    words = {k: prose_text(open(v, encoding='utf-8').read()) for k, v in P.items()}
    sh = {k: shingles(w) for k, w in words.items()}
    owner = collections.defaultdict(set)
    for k, ss in sh.items():
        for s in set(ss): owner[s].add(k)
    order = sorted(P, key=lambda k: os.path.getmtime(P[k]), reverse=True)
    report = order if want_all else order[:int(args[0]) if args else 5]
    worst = 0
    for k in report:
        ss = sh[k]
        if not ss: print('%-50s (no prose found)' % k); continue
        shared = [s for s in ss if len(owner[s]) > 1]
        pct = 100.0 * len(shared) / len(ss); worst = max(worst, pct)
        by = collections.Counter(o for s in set(shared) for o in owner[s] if o != k)
        top = ', '.join('%s %d' % (o, c) for o, c in by.most_common(3))
        print('%-50s %4.1f%%   top matches: %s' % (k, pct, top))
        if want_list:
            # longest runs of consecutive shared shingles
            runs = []; i = 0
            while i < len(ss):
                if len(owner[ss[i]]) > 1:
                    j = i
                    while j < len(ss) and len(owner[ss[j]]) > 1: j += 1
                    txt = ' '.join(words[k][i:j + N - 1]); others = set.union(*[owner[s] for s in ss[i:j]]) - {k}
                    runs.append((j - i, txt, sorted(others)[:2])); i = j
                else: i += 1
            for ln, txt, oth in sorted(runs, reverse=True)[:8]:
                print('        [%2d] "%s"  <- %s' % (ln, txt[:150], oth))
    print('max across reported pages: %.1f%%' % worst)

if __name__ == '__main__':
    main()
