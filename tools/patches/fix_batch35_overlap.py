D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')

fix('build_overlandpark_local.py', [
("Ice stops the trucks before snow does. The carriers park by the Turnpike until the salt trucks finish. A winter pickup can slip a day. We call before it does. A tornado warning stops the loading until it lifts, and the sirens sound a few times each spring. The driver waits it out and usually finishes the same day.",
 "Ice, more than snow, is what parks the trucks here. When it glazes 435, the carriers hold by the Turnpike until the salt trucks have been through. Expect a day of delay at most, with a call from us ahead of it. Under a tornado warning the loading pauses until the all-clear. The sirens are a spring ritual, and the driver usually finishes the same afternoon."),
("Approve the price, and we place the car with a carrier already running the loop. You get the lot and the window the same day. At pickup, the driver inspects the car with you and records its condition on a Bill of Lading. Both of you sign, and the sheet comes out again at delivery.",
 "Once you approve the price, we assign a carrier that is already circling the loop. The meeting lot and the pickup window follow within hours. You and the driver go over the car together at pickup, and every existing mark goes on the Bill of Lading. Two signatures close it, and the same form is checked at delivery."),
("We build the delivery window around the closing, and it moves when the closing does. Tell us as soon as the date changes.",
 "The delivery window is pinned to the closing date, and when the closing slides, so does the window. One call with the new date is all it takes."),
("The orders cover one car, and the second one comes with us. Ship Guy is a private broker with no connection to the post. The <a href=\"military-car-shipping.html\">military</a> page covers the timing.",
 "Orders pay for one car, and the family’s second car rides with us. Ship Guy is a private broker and has no connection to the post. The <a href=\"military-car-shipping.html\">military</a> page explains the timing."),
("A commuter car or a family SUV goes open and arrives in the same shape it left. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages compare the two.",
 "The family SUV and the commuter car go open and arrive exactly as they left. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages lay the two side by side."),
("Tulsa, Oklahoma City, and Chicago take a day. Dallas and Denver take one to two, and the coasts take three to five.",
 "Tulsa, Oklahoma City, and Chicago are a day out. Dallas and Denver run one to two days, and either coast runs three to five."),
("Snow runs twenty inches a year, and the 2011 blizzard closed 35 for a day. The carriers park at the truck stops by the Turnpike until the plows finish. A winter pickup can lose a day.",
 "Snow adds up to twenty inches in a normal year, and the 2011 blizzard shut 35 for a day. The carriers sit at the truck stops by the Turnpike while the plows work. A pickup that week can lose a day."),
])

fix('build_olathe_local.py', [
("Ice stops the carriers before snow does. They park at the truck stops in Gardner until the salt trucks finish. A winter pickup can slip a day. You hear from us before it does. A tornado warning stops the loading until it lifts, and the sirens sound a few times each spring. The driver waits it out and usually finishes the same day.",
 "Ice is what stops the trucks here, long before the snow does. The carriers hold at the Gardner truck stops until the salt trucks have run 35. That can cost a day, and we tell you before it does. A tornado warning pauses the loading until it expires. Sirens come a few times every spring, and the driver generally finishes the same afternoon."),
("The orders cover one car, and the second comes with us. Ship Guy is a private broker with no connection to the post. The <a href=\"military-car-shipping.html\">military</a> page covers the timing. The <a href=\"state-to-state-car-shipping.html\">state-to-state</a> page covers the interstate side.",
 "The orders pay for one car, and the other rides with us. Ship Guy is a private broker and has nothing to do with the post. Timing around a report date is on the <a href=\"military-car-shipping.html\">military</a> page, and the interstate side is on the <a href=\"state-to-state-car-shipping.html\">state-to-state</a> page."),
("Yes. The campus on College Boulevard takes cars in each August and sends them home in May. The community college in Overland Park runs the same calendar. A parent books, and an adult signs at a campus lot. The delivery window follows the move-in date and shifts with it.",
 "Yes. Cars arrive at the College Boulevard campus each August and leave each May, and the community college in Overland Park keeps the same dates. The booking usually comes from a parent, and someone over eighteen signs at a campus lot. We pin the delivery to the move-in date and move it if the date moves."),
("The activity center lots or a lot on 151st give the driver flat pavement. Tell us whether the car rolls, steers, and brakes.",
 "The activity center lots or a lot on 151st give the driver somewhere flat to winch from. Say whether the wheels turn, the steering works, and the brakes hold."),
("One coordinator owns the move from the first number to the last signature.","The person who quotes the move is the person who sees it delivered."),
("Oklahoma City and Chicago take a day. Dallas and Denver take one to two, and the coasts take three to five.",
 "Oklahoma City and Chicago are a day. Dallas and Denver are one to two, and the coasts are three to five."),
("Snow runs twenty inches a year, and the 2011 blizzard closed 35 for a day. The carriers park at the truck stops in Gardner until the plows finish. A winter pickup can lose a day.",
 "Twenty inches of snow falls in a normal winter, and the 2011 blizzard closed 35 for a day. The carriers wait it out at the Gardner truck stops, and a pickup that week can slip a day."),
])

fix('build_topeka_local.py', [
("Where the car is and where it is going, with the side of the river or the suburb. The year, make, and model. Whether it starts. Open or enclosed. The week you have in mind. With those five, the Topeka quote comes back within the day.",
 "The two addresses, down to the side of the river. What the car is, year through model. Whether it starts. Open or enclosed. The week you are aiming for. That is everything, and the Topeka number is back the same day."),
("'Two minutes on the form above prices your lane. Send the side of the river and your dates, and a carrier already on 70 takes it.'",
 "'The form above prices the lane in two minutes. Tell us the side of the river and the week, and the next carrier clearing the Turnpike gate takes it.'"),
("A commuter car or a state fleet sedan goes open and arrives in the shape it left.","A commuter car or a fleet sedan rides open and comes off the trailer unchanged."),
("*2026 estimates priced from Topeka for a running sedan on an open trailer. Figure 10 to 25 percent more for an SUV or a pickup and more again for enclosed.",
 "*2026 estimates priced from Topeka, open trailer, sedan that runs. SUVs and pickups land 10 to 25 percent higher, enclosed higher again."),
("The agencies move staff in from across Kansas. The session brings staffers and lobbyists with a car each winter. Many ship a second car behind the move. The handoff works at the expo center or a lot on Wanamaker.",
 "The agencies pull staff in from every corner of Kansas, and the session adds staffers and lobbyists each January. A second car often follows the move. The expo center or a lot on Wanamaker works for the handoff."),
("The orders cover one car, and the second one comes with us. Ship Guy is a private broker with no connection to the wing or the post.",
 "Orders move one car, and we move the other. Ship Guy is a private broker with no tie to the wing or the post."),
("Ship Guy is an FMCSA-licensed broker with a $75,000 surety bond behind it. The federal register carries both. Our office is on Quincy Street downtown.",
 "Ship Guy holds FMCSA brokerage authority, backed by a $75,000 surety bond, and both are on the federal register. The office is on Quincy Street downtown."),
("The sirens sound a few times each spring. A pickup waits for the warning to lift. Ice is the winter problem, and the 2007 storm",
 "Sirens go off a few times every spring, and a pickup waits until the warning expires. Ice is the winter problem, and the 2007 storm"),
])

fix('build_owensboro_local.py', [
("Confirm the number, and we match the car to a carrier already running 64 or 65. The lot and the pickup window reach you that day. At the handoff, the driver inspects the car and lists every mark on a Bill of Lading. You both sign it, and the same sheet closes the delivery.",
 "Give the number a yes, and we pair the car with a carrier already working 64 or 65. The meeting lot and the window come back within hours. The driver walks the car at the handoff and notes every existing mark on the Bill of Lading. Both of you sign, and the sheet settles the delivery."),
("  \"Photograph each panel and the odometer before the truck arrives\",\n  \"Hand the driver one working key and describe any fault\",\n  \"Shut off any aftermarket alarm\",",
 "  \"Take dated photos of every panel and the mileage\",\n  \"One working key goes to the driver, with a word about any fault\",\n  \"Kill any aftermarket alarm before the handoff\","),
("The orders cover one car, and the second one comes with us. Ship Guy is a private broker with no connection to the post. The <a href=\"military-car-shipping.html\">military</a> page covers the timing.",
 "The orders pay for one car, and the family’s other car rides with us. Ship Guy is a private broker with no link to the post. The <a href=\"military-car-shipping.html\">military</a> page walks through the timing."),
("Families shipping a new car to a student book one too.","Parents sending a new car to a student book one too."),
("An everyday car or a work truck goes open and comes off the trailer clean.","A daily driver or a farm truck goes open and arrives none the worse."),
("A parent books, and an adult signs at a campus lot. The delivery window follows the move-in date and shifts with it.",
 "Parents do most of the booking, and someone over eighteen signs at a campus lot. The delivery window tracks the move-in date."),
("A tornado warning stops the loading until it lifts, and the sirens sound a few times each spring. The driver waits it out and usually finishes the same day. An ice storm costs a day, and the call comes before it does.",
 "A tornado warning pauses the loading until it expires, and the sirens are a spring fixture here. The driver waits it out and nearly always finishes the same day. An ice storm costs a day, and you hear from us before it does."),
("The coordinator who prices the move answers for it until the car is signed for.","Whoever prices the move is whoever you call until the car is signed for."),
("The mall lot on Frederica or the sportscenter lot gives the driver flat pavement. Tell us whether the car rolls, steers, and brakes.",
 "The mall lot on Frederica or the sportscenter lot gives the driver level ground to work from. Let us know whether it rolls, steers, and stops."),
])
