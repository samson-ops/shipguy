D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')
fix('build_portlandme_local.py', [("A sedan to Boston runs one hundred seventy to two hundred eighty dollars, for about one hundred ten miles down 95.","A sedan to Boston runs one hundred seventy to two hundred eighty dollars. That covers about one hundred ten miles down 95.")])
fix('build_lewiston_local.py', [("Give us the side of the river and a range of dates, and the next carrier up the Turnpike takes it.","Give us the side of the river and a range of dates. The next carrier up the Turnpike takes it.")])
fix('build_bangor_local.py', [("The mall on Stillwater, the arena at Bass Park, and the Hermon truck stop have the usual meeting lots.","The mall on Stillwater, the Bass Park arena, and the Hermon truck stop have the usual meeting lots.")])
