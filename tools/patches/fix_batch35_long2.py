D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')
fix('build_overlandpark_local.py', [
("Snow adds up to twenty inches in a normal year, and the 2011 blizzard shut 35 for a day.","Snow adds up to twenty inches in a normal year. The 2011 blizzard shut 35 for a day."),
("You and the driver go over the car together at pickup, and every existing mark goes on the Bill of Lading.","You and the driver go over the car together at pickup. Every existing mark goes on the Bill of Lading."),
])
fix('build_olathe_local.py', [
("Timing around a report date is on the <a href=\"military-car-shipping.html\">military</a> page, and the interstate side is on the <a href=\"state-to-state-car-shipping.html\">state-to-state</a> page.",
 "Timing around a report date is on the <a href=\"military-car-shipping.html\">military</a> page. The interstate side is on the <a href=\"state-to-state-car-shipping.html\">state-to-state</a> page."),
("The carriers wait it out at the Gardner truck stops, and a pickup that week can slip a day.","The carriers wait it out at the Gardner truck stops. A pickup that week can slip a day."),
("Cars arrive at the College Boulevard campus each August and leave each May, and the community college in Overland Park keeps the same dates.","Cars arrive at the College Boulevard campus each August and leave each May. The community college in Overland Park keeps the same dates."),
])
fix('build_topeka_local.py', [
("Ship Guy holds FMCSA brokerage authority, backed by a $75,000 surety bond, and both are on the federal register.","Ship Guy holds FMCSA brokerage authority, backed by a $75,000 surety bond. Both are on the federal register."),
("The agencies pull staff in from every corner of Kansas, and the session adds staffers and lobbyists each January.","The agencies pull staff in from every corner of Kansas. The session adds staffers and lobbyists each January."),
("Tell us the side of the river and the week, and the next carrier clearing the Turnpike gate takes it.","Tell us the side of the river and the week. The next carrier clearing the Turnpike gate takes it."),
])
