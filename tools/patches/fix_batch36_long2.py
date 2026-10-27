D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')
fix('build_batonrouge_local.py', [
("Once the number works for you, we put the car on a carrier already working 10 between Houston and New Orleans.","Once the number works for you, we put the car on a carrier already working 10."),
("At pickup the driver and you go over the car panel by panel, and the Bill of Lading records what you find.","At pickup the driver and you go over the car panel by panel. The Bill of Lading records what you find."),
("Nothing moves on the coast in the last three days before landfall, and contraflow on 10 shuts the rest.","Nothing moves on the coast in the last three days before landfall. Contraflow on 10 shuts the rest."),
("Rain is the other risk here, since a stalled storm floods the east-side subdivisions, and no carrier stages on a flooded street.","Rain is the other risk here, since a stalled storm floods the east-side subdivisions. No carrier stages on a flooded street."),
])
fix('build_shreveport_local.py', [
("Base housing sits behind a gate, so the driver meets you outside it or at a lot on Airline Drive.","Base housing sits behind a gate. The driver meets you outside it or at a lot on Airline Drive."),
])
fix('build_metairie_local.py', [
("At the handoff the driver and you walk around the car, and the Bill of Lading records every mark already on it.","At the handoff the driver and you walk around the car. The Bill of Lading records every mark already on it."),
("On an ordinary summer afternoon, a downpour floods the low streets until the pumps catch up, and the driver simply waits the hour.","On an ordinary summer afternoon, a downpour floods the low streets until the pumps catch up. The driver simply waits the hour."),
])
