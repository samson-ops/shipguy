D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')

fix('build_kapaa_local.py', [
("The first leg looks like any domestic move. A carrier collects the car and hauls it to a West Coast port. Southern California and the Bay Area are a day or two away. Texas and the East Coast are five days or more. You sign a Bill of Lading at pickup.",
 "The first leg is a plain highway haul. A carrier picks the car up at your door and drives it to the port. From Southern California or the Bay Area, that takes a day or two. From Texas or the East Coast, allow five days or more. The Bill of Lading you sign at pickup follows the car onto the ship."),
("Count three to four weeks from a West Coast origin and four to five from the East. Add three to seven days for the barge in a week without a direct Nawiliwili call.",
 "A West Coast origin lands on Kauai in three to four weeks, and an East Coast origin in four to five. A week without a direct Nawiliwili call adds the barge, three to seven days more."),
("Southern California and the Bay Area are the shortest and least expensive origins. Seattle and Portland come next. Everything else adds a land leg first.",
 "The cheapest origins are the ones closest to a port: Los Angeles, the Bay Area, Seattle, and Portland. An inland origin pays for the highway miles first and the crossing second."),
("Outbound, the car boards at Nawiliwili and sails direct or through Honolulu to a West Coast gateway. A carrier takes it the rest of the way. The same rules apply: empty car, quarter tank, no red dirt, title in hand. One coordinator runs every leg.",
 "Outbound, the car boards at Nawiliwili, sails direct or by way of Honolulu, and lands at a West Coast port. A carrier finishes the trip to your new address. The gate rules run in reverse: nothing inside, a quarter tank, no red dirt, and the title in hand. One coordinator holds every leg."),
("The ship prices by dimensions, so a lifted truck costs more. Ask for a quote for a firm number on your sailing.",
 "Height and length set the ocean fare, so a lifted truck pays more than a sedan. The form above returns a firm number for your sailing."),
("Because every car is an invasive-species risk to the island. The inspectors check the body, the wheel wells, and the cabin for soil, seeds, and plant matter. A dirty car is refused at the gate in both directions. Wash it and vacuum it the day before pickup, and expect a reminder from us.",
 "Kauai treats every arriving car as a possible carrier of seeds, soil, and insects. The inspectors go over the body, the wheel wells, and the cabin. A dirty car is turned away at the gate, inbound or outbound. Wash it and vacuum it the day before pickup. We send a reminder so it is not forgotten."),
("The mainland pickup point and the Kauai address, district and road included. Year, make, and model. Whether it runs, whether a lender holds the title, and whether it carries a lift or a rack. We set those against the sailing and barge calendars, and the Kapaʻa quote comes back firm.",
 "Where the car is on the mainland and where it is going on Kauai, down to the road. The year, make, and model. Whether it drives, whether it is financed, and whether anything raises its height. We match those to the next sailing and the barge, and the Kapaʻa number is firm when it arrives."),
("'A quote takes about two minutes on the form above. Tell us the origin, the district, and your dates. We line the pickup up with the next sailing.'",
 "'The form above takes two minutes. Give us the mainland origin, the Kauai district, and your dates, and we aim the pickup at the next sailing.'"),
])

fix('build_evansville_local.py', [
("Yes. The campuses on Lincoln Avenue and the West Side bring cars in each August. They send them home in May. A parent books the move, and an adult signs for the car at a campus lot. We set the delivery window on the move-in date and move it when the date moves.",
 "Yes. The campus on Lincoln Avenue and the one on the West Side fill with cars each August and empty in May. A parent usually books, and someone over eighteen meets the truck at a campus lot. The delivery window follows the move-in date, and it shifts if the date shifts."),
("A commuter car or a work truck goes open and arrives fine. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages lay out the difference.",
 "A daily driver or a work truck rides open and arrives in the same shape it left. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages compare the two."),
])

fix('build_aurorail_local.py', [
("Yes. The campus on Southlake brings cars in each August and sends them home in May. The community college in Sugar Grove does the same. A parent books the move, and an adult signs for the car at a campus lot. We set the delivery window on the move-in date and move it when the date moves.",
 "Yes. The Southlake campus and the community college in Sugar Grove take cars in every August and send them out every May. A parent books, and an adult signs at a campus lot. We tie the delivery window to the move-in date and slide it when the date slides."),
("A commuter car or a work truck goes open and arrives fine. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages lay out the difference.",
 "An everyday car or a work truck goes open and comes off the trailer clean. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages explain the trade-off."),
])
