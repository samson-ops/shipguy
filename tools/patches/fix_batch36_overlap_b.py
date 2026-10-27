D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')

fix('build_metairie_local.py', [
("The mall on Veterans, the stadium on Airline, and the lakefront by the Causeway have the usual meeting lots.","The mall on Veterans, the stadium on Airline, and the lakefront have the usual meeting lots."),
("Metairie runs on a parade route, a training camp, and a drainage system that decides if the street is dry.","Metairie runs on a parade route, a training camp, and a drainage system that decides the day."),
("The hospital system on Jefferson Highway and the hospital on Houma Boulevard bring in nurses and physicians every month.","The hospital system on Jefferson Highway and the hospital on Houma Boulevard hire nurses and physicians every month."),
("The carriers pull back from the coast days before landfall, and contraflow on 10 stops everything else. We rebook the week after the storm passes. A car already loaded keeps moving inland. A summer downpour floods the low streets for an hour until the pumps catch up. The driver waits it out. You hear from us at every change.",
 "Three days out from landfall the carriers are gone from the coast, and contraflow turns 10 one way. Your pickup moves to the week after the storm. A car already on a trailer keeps going inland. On an ordinary summer afternoon, a downpour floods the low streets until the pumps catch up, and the driver simply waits the hour. We call at every change."),
("Give the number a yes, and we pair the car with a carrier already working 10. The meeting lot and the window come back within hours. The driver walks the car at the handoff and notes every existing mark on the Bill of Lading. Both of you sign, and the sheet settles the delivery.",
 "Say yes to the number, and the car goes to a carrier already working 10. The meeting lot and the window follow within hours. At the handoff the driver and you walk around the car, and the Bill of Lading records every mark already on it. Two signatures, and the same sheet settles the delivery."),
("Together they bring in nurses on contracts all year and residents each June. Physicians arrive with a closing date and a second car. We supply the paperwork a reimbursed move needs.",
 "Between them they hire nurses on contracts all year and take residents each June. Physicians come with a closing date and a second car. The paperwork for a reimbursed move comes from us."),
("  \"Keep the fuel at about a quarter tank\",\n  \"Photograph each side of the car and the odometer before the handoff\",\n  \"Give the driver one working key and name any mechanical fault\",",
 "  \"Run the tank down to about a quarter\",\n  \"Photograph the car on all four sides, plus the mileage\",\n  \"Pass the driver one working key and point out any fault\","),
("The family SUV and the commuter car go open and arrive exactly as they left. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages lay the two side by side.",
 "The carpool SUV and the commuter car go open and arrive the way they left. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages put the two side by side."),
("Whoever prices the move is whoever you call until the car is signed for.","The coordinator who prices the move keeps it until the delivery sheet is signed."),
("The orders pay for one car, and the family’s other car rides with us. Ship Guy is a private broker and has nothing to do with the station.",
 "Orders cover one car, and the family’s other car comes with us. Ship Guy is a private broker with no tie to the station."),
("Ship Guy holds FMCSA brokerage authority, backed by a $75,000 surety bond. Both are on the federal register. The office is on North Causeway Boulevard.",
 "Ship Guy carries FMCSA brokerage authority and a $75,000 surety bond, both on the federal register. The office is on North Causeway Boulevard."),
])

fix('build_shreveport_local.py', [
("Car shipping in Shreveport runs off Interstate 20, which crosses the river into Bossier City on the way to Jackson.","Car shipping in Shreveport runs off Interstate 20, which crosses the river into Bossier City."),
("Shreveport runs on a state fair in the fall, two big Mardi Gras parades, and every kind of storm.","Shreveport runs on a fall state fair, two big Mardi Gras parades, and every kind of storm."),
("The orders cover one car, and the second one comes with us. Ship Guy is a private broker with no connection to the base. The <a href=\"military-car-shipping.html\">military</a> page covers the timing around a report date.",
 "The orders move one car, and the second one moves with us. Ship Guy is a private broker with no link to the base. Timing around a report date is on the <a href=\"military-car-shipping.html\">military</a> page."),
("Yes. The three colleges take cars in each August and send them home in May. Parents do most of the booking, and someone over eighteen signs at a campus lot. The delivery window tracks the move-in date.",
 "Yes. The three colleges fill with cars each August and empty each May. A parent usually books, and an adult signs for the car at a campus lot. We pin the delivery to the move-in date."),
("Housing on the base is gated. The driver meets you outside the gate or at a lot on Airline Drive. Ship Guy is a private broker with no connection to the base. Send the report date, and we build the window around it.",
 "Base housing sits behind a gate, so the driver meets you outside it or at a lot on Airline Drive. Ship Guy is a private broker with no link to the base. Give us the report date, and the window is built around it."),
("The mall lot on Youree or the fairgrounds lot gives the driver level ground to work from. Let us know whether it rolls, steers, and stops.",
 "The mall lot on Youree or the fairgrounds lot gives the driver room to winch. Tell us if it rolls, if it steers, and if the brakes hold."),
("  \"Leave about a quarter tank of fuel\",\n  \"Take dated photos of every panel and the mileage\",\n  \"One working key goes to the driver, with a word about any fault\",",
 "  \"Fuel at a quarter tank or less\",\n  \"Photos of every panel and the odometer, dated\",\n  \"A working key for the driver and a word about any fault\","),
("The two addresses, down to the side of the river. What the car is, year through model. Whether it starts. Open or enclosed. The week around the report date. That is everything, and the Shreveport number is back the same day.",
 "Both addresses, with the side of the river here. Year, make, and model. Whether it starts. Open or enclosed. The week around the report date. That covers it, and the Shreveport number comes back the same day."),
("The person who quotes the move is the person who sees it delivered.","The coordinator who quotes the move is the one who sees it through."),
("You hear from us before it does. A tornado warning stops the loading until it lifts, and the sirens sound a few times each spring. The driver waits it out and usually finishes the same day.",
 "We call before it happens. A tornado warning holds the loading until it expires, and the sirens are a spring routine here. The driver waits and nearly always finishes the same day."),
])
