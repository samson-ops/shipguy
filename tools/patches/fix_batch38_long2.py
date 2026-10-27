D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')
fix('build_tempe_local.py', [
("At pickup you and the driver go around the car together, and every existing mark goes on the Bill of Lading.","At pickup you and the driver go around the car together. Every existing mark goes on the Bill of Lading."),
("A flash flood closes the low crossings and sometimes the Broadway Curve, as it did in 2014, and the pickup slides to the next morning.","A flash flood closes the low crossings and sometimes the Broadway Curve, as it did in 2014. The pickup slides to the next morning."),
("The graduates scatter to California, Texas, and the East Coast each May, and the car follows the week after finals.","The graduates scatter to California, Texas, and the East Coast each May. The car follows the week after finals."),
("Where the car is and where it is going, with the side of the 60 or the campus lot.","Where the car is and where it goes, with the side of the 60 or the campus lot."),
("Give us the side of the 60 and the week, and a carrier already crossing the Valley takes it.","Give us the side of the 60 and the week. A carrier already crossing the Valley takes it."),
])
fix('build_surprise_local.py', [
("Surprise prices under the rest of the Valley on the Las Vegas lane, since the carriers pass the door.","Surprise prices under the rest of the Valley on the Las Vegas lane, since the carriers pass by."),
("A flash flood shuts the Agua Fria crossings and the washes west of Reems, and the pickup waits for the next morning.","A flash flood shuts the Agua Fria crossings and the washes west of Reems. The pickup waits for the next morning."),
])
