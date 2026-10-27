D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')

fix('build_tempe_local.py', [
("['Car shipping in Tempe runs off the four freeways that frame the city. The 10 and the 60 meet at its southwest corner. Ship Guy is a licensed auto transport broker with an office on Lakeshore Drive in the Lakes.',\n  'We book vetted carriers across Tempe and the towns around it, from the campus to Guadalupe and over to Mesa. The trucks belong to the carriers.',",
 "['Car shipping in Tempe runs off the four freeways that frame the city. Ship Guy is a licensed auto transport broker with an office on Lakeshore Drive in the Lakes.',\n  'The 10 and the 60 meet at the southwest corner. We book vetted carriers across Tempe and the towns around it, from the campus to Mesa. The trucks belong to the carriers.',"),
("It also covers move-in week, the towers on the lake, the Angels, the Ironman, the heat, and the lanes.","It also covers move-in week, the towers on the lake, the Ironman, the heat, and the lanes."),
("Mill Avenue beside it is downtown, a narrow strip of bars and restaurants with the streetcar down the middle.","Mill Avenue beside it is downtown, a narrow strip of bars with the streetcar down the middle."),
("The campus roads, Mill Avenue, and the rail streets on Apache are closed to a trailer or have nowhere to stop.","The campus roads, Mill Avenue, and the rail streets on Apache give a trailer nowhere to stop."),
("A flash flood closes the low crossings and sometimes the Broadway Curve, as it did in 2014. The pickup moves to the next morning. In summer the loading hour moves to dawn because of the heat. You hear from us before anything changes.",
 "A flash flood closes the low crossings and sometimes the Broadway Curve, as it did in 2014, and the pickup slides to the next morning. Summer loading happens at dawn, before the heat. Any change reaches you before it happens."),
("Approve the price, and we match the car to a carrier already crossing the Valley. The lot and the window reach you the same day. At pickup, the driver inspects the car with you and notes every mark on a Bill of Lading. Both of you sign, and the sheet is checked again at the far end.",
 "Once you approve the price, the car goes to a carrier already crossing the Valley. The meeting lot and the window follow the same day. At pickup you and the driver go around the car together, and every existing mark goes on the Bill of Lading. Two signatures close it, and the far end is checked against it."),
("The pickup and delivery addresses, with the side of the 60 or the campus lot here. Year, make, and model. Whether it runs. Open or enclosed. The week around move-in or the start date. That is a full Tempe request, and the number comes back the same day.",
 "Where the car is and where it is going, with the side of the 60 or the campus lot. What it is, year through model. Whether it starts. Open or enclosed. The week around move-in or the start date. Five answers, and the Tempe number is back within the day."),
("The coordinator who quotes the move is the one who closes it.","One coordinator carries the move from the first number to the last signature."),
("August and the snowbird months run higher than the rest of the year. An SUV or pickup adds 10 to 25 percent.",
 "August and the snowbird months price above the rest of the year. Figure 10 to 25 percent more for an SUV or a pickup."),
("Yes. Graduates leave for California, Texas, and the East Coast each May. We ship the car the week after finals. The handoff works at a campus lot or the marketplace. Book in April, because the May carriers fill early. An adult signs at pickup if the graduate has already left.",
 "Yes. The graduates scatter to California, Texas, and the East Coast each May, and the car follows the week after finals. The handoff happens at a campus lot or the marketplace. Reserve in April, since the May trucks are spoken for early. If the graduate has already flown, an adult signs at pickup."),
("The faculty arrive each summer with a closing date and a second car. We supply the paperwork a reimbursed move needs.",
 "Faculty hires land each summer with a closing date and a second car. The paperwork for a reimbursed move comes from us."),
("'Two minutes on the form above prices your lane. Send the side of the 60 and your dates, and a carrier already crossing the Valley takes it.'",
 "'The form above prices the lane in two minutes. Give us the side of the 60 and the week, and a carrier already crossing the Valley takes it.'"),
])

fix('build_surprise_local.py', [
("The stadium on Bell, the shopping centers by the 303, and the civic center have the usual meeting lots.","The stadium on Bell, the shopping centers by the 303, and the civic center have the meeting lots."),
("The driver meets you at the curb in Sun City Grand or at the gate of a gated section.","The driver meets you at the curb in Sun City Grand or at the gate."),
("A flash flood closes the Agua Fria crossings and the washes west of Reems. The pickup moves to the next morning. In summer the loading hour moves to dawn because of the heat. You hear from us before anything changes.",
 "A flash flood shuts the Agua Fria crossings and the washes west of Reems, and the pickup waits for the next morning. From June through September the loading happens at dawn. We call before any of it changes your window."),
("The person who quotes the move is the person on the phone until it is delivered.","The coordinator who prices the move stays with it until the car is signed for."),
("Housing on the base is gated, and the driver meets you outside the gate. Ship Guy is a private broker with no connection to the base. The <a href=\"military-car-shipping.html\">military</a> page covers the timing.",
 "Base housing sits behind a gate, so the handoff happens outside it. Ship Guy is a private broker with no tie to the base. The timing around a report date is on the <a href=\"military-car-shipping.html\">military</a> page."),
("Ship Guy is a private broker with no connection to the base. Send the report date, and we build the window around it.",
 "Ship Guy is a private broker with no link to the base. Give us the report date, and the window is built around it."),
("Ship Guy is an active FMCSA broker backed by a $75,000 surety bond. The federal register lists both. Our office is on Bell Road by the stadium.",
 "Ship Guy carries FMCSA brokerage authority and a $75,000 surety bond, both on the federal register. Our office is on Bell Road by the stadium."),
("  \"In a gated section, meet the truck at the gate or send the code ahead\",","  \"In a gated section, the handoff waits at the gate, so send the code ahead\","),
("Surprise prices under the rest of the Valley on the Las Vegas lane. The carriers pass the door. An SUV or pickup adds 10 to 25 percent.",
 "Surprise prices under the rest of the Valley on the Las Vegas lane, since the carriers pass the door. Count on 10 to 25 percent more for an SUV or a pickup."),
])
