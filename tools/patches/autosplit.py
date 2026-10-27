#!/usr/bin/env python3
"""Split over-long sentences (>18 words) in a city builder at a natural conjunction.
Usage: python3 autosplit.py builders_city/build_x_local.py city/auto-transport-x/index.html
Reads audit_content.py's long-sentence list for the built page, finds each sentence verbatim in the builder,
and splits it at ', and ' / ', so ' / ', but ' / ', which ' when both halves end up <= 18 words.
Prints the ones it could not fix so they can be done by hand."""
import re, subprocess, sys
builder, page = sys.argv[1], sys.argv[2]
out = subprocess.run(['python3', '/home/claude/tools/audit_content.py', page], capture_output=True, text=True).stdout
sents = [l.split('|', 1)[1].strip() for l in out.splitlines() if 'long-sentence' in l]
s = open(builder, encoding='utf-8').read()
wc = lambda t: len(t.split())
fixed, manual = 0, []
for sent in sents:
    if s.count(sent) != 1:
        manual.append(('not-found' if s.count(sent) == 0 else 'ambiguous', sent)); continue
    best = None
    for conj, repl in [(', and ', ''), (', but ', ''), (', so ', ''), (', which ', 'That ')]:
        for m in re.finditer(re.escape(conj), sent):
            a, b = sent[:m.start()], sent[m.end():]
            if re.search(r',\s[^,]{1,30}$', a): continue   # 'X, Y, and Z' list -> not a clause break
            if wc(a) <= 18 and wc(b) + (1 if repl else 0) <= 18 and wc(a) >= 4 and wc(b) >= 3:
                b2 = repl + (b[0].upper() + b[1:] if not repl else b)
                score = abs(wc(a) - wc(b))
                if best is None or score < best[0]:
                    best = (score, a + '. ' + b2)
    if best:
        s = s.replace(sent, best[1]); fixed += 1
    else:
        manual.append(('no-split', sent))
open(builder, 'w', encoding='utf-8').write(s)
print(f'{builder}: split {fixed}, manual {len(manual)}')
for why, sent in manual: print('  ', why, '|', sent)
