D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')
fix('build_rockford_local.py', [
("Nine cars in ten leave the Rock River valley on an open trailer, and the table above is priced that way.","Nine cars in ten leave the Rock River valley on an open trailer. The table above is priced that way."),
("A few times each winter the tollway shuts, and the carriers sit at the Cherry Valley truck stops until it reopens.","A few times each winter the tollway shuts. The carriers sit at the Cherry Valley truck stops until it reopens."),
("Where the car is and where it is going, with the Rockford side of the river or the suburb.","Where the car is and where it is going, with the side of the river or the suburb."),
])
fix('build_champaign_local.py', [
("Open trailers carry most of the cars that leave Champaign County, and the lane table is priced for one.","Open trailers carry most of the cars that leave Champaign County. The lane table is priced for one."),
("Ice shuts 57 and 74 a few times each winter, and the carriers hold at the interchange truck stops until the salt trucks pass.","Ice shuts 57 and 74 a few times each winter. The carriers hold at the interchange truck stops until the salt trucks pass."),
])
