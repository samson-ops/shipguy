"""Batch 45 fresh-wording pass: the seven pages shared the pass-through, winter, PCS, and standard-block phrasings with each other and with Batch 44."""
D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    if pairs and all(s.count(o[0])==0 for o in pairs): print(fn,'already applied'); return
    for item in pairs:
        old,new=item[0],item[1]; k=item[2] if len(item)>2 else 1
        c=s.count(old); assert c==k, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'rewrites')
STS='<a href="state-to-state-car-shipping.html">state-to-state</a>'; OPEN='<a href="open-car-transport.html">open</a>'; ENC='<a href="enclosed-auto-transport.html">enclosed</a>'
HIW='<a href="how-it-works.html">how it works</a>'; PREP='<a href="car-shipping-preparation.html">preparation</a>'

# ---------------- Bismarck (shared most with Fargo and Great Falls)
fix('build_bismarck_local.py', [
('A car arriving from a warm state needs winter oil and a block heater. An electric car should arrive at half charge, because the cold takes the rest. The driver meets you in a plowed lot rather than a drifted street.',
 'Winter oil and a block heater go in before a car from the south spends a night here. An electric car wants half a charge on arrival, since the cold eats the rest. The handoff happens in a plowed lot, never on a drifted street.'),
('One adds a Bismarck stop when the load lines up. Give us a week of dates and we catch the next truck through. A single fixed date can mean waiting for one.',
 'One adds a Bismarck stop when the load lines up. A week of dates lets us put the car on the next one through. A single fixed date can sit and wait.'),
('Yes. The carrier brings a winch, and the loading time is in the quote from day one. On a pass-through road that narrows which trucks can stop. The mall lots on Century Avenue give the driver level ground. Say whether it rolls, steers, and brakes.',
 'Yes. The quote covers a winch-equipped carrier and the loading time from the start. On 94 that means fewer trucks can take the stop, so give us room on the dates. The mall lots on Century Avenue are level. Tell us whether it rolls, steers, and brakes.'),
('Both ends of the move, with the neighborhood or the town. The year, make, and model. Whether it runs. Open or enclosed. The widest week of dates you can give. Those five put a Bismarck number in your inbox the same day.',
 'Where the car is and where it goes, with the neighborhood or the town. Year, make, and model. Running or not. Open or enclosed. The widest week of dates you can live with. Answer those, and the Bismarck number is in your inbox the same day.'),
("'*2026 estimates from Bismarck for a sedan that runs, on an open trailer. SUVs and pickups add about 10 to 25 percent, and enclosed adds more. On a pass-through corridor your week of dates and the trucks crossing that week decide the real figure.'",
 "'*2026 estimates from Bismarck, running sedan, open trailer. Add about 10 to 25 percent for an SUV or a pickup, and more again for enclosed. Your week of dates and the trucks crossing 94 that week decide the real figure.'"),
('A car leaving for Arizona ahead of the first blizzard often rides enclosed too.',
 'Snowbirds sending a car south before the first blizzard often choose enclosed as well.'),
('A commuter car or a student car does fine in the open. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain where the line falls.',
 'A commuter car or a student car needs nothing more than an open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain where the line falls.'),
('A new governor brings an appointee class every fourth January. If the state or an employer is reimbursing the move, we produce the receipts.',
 'Every fourth January a new governor brings in a class of appointees. When the state or an employer picks up the cost, we produce the receipts.'),
('Retirees leave for Arizona each October and come back in April. The %s page covers the paperwork for an interstate move.'%STS,
 'Each October the retirees head for Arizona, and each April they come back. The paperwork for crossing state lines is on the %s page.'%STS),
("plan on a lot\",\n ])+prose(P('The %s page has the order of events. The %s page has the checklist.'))))"%(HIW,PREP),
 "plan on a lot\",\n ])+prose(P('Read the %s page for the order of events and the %s page for the checklist.'))))"%(HIW,PREP)),
('Minot and Fargo are a day away and the lowest lanes on the table. SUVs and pickups add about 10 to 25 percent.',
 'Minot and Fargo are a day away and cost the least. Add about 10 to 25 percent for an SUV or a pickup.'),
('Almost every car in the city rides open, and the lane table above is priced that way.','Nearly every Bismarck car travels on an open trailer, and the table above is priced for one.'),
])

# ---------------- Great Falls (shared with Missoula, Fargo, Charleston)
fix('build_greatfalls_local.py', [
('A car arriving from a warm state needs winter oil and a block heater. An electric car should arrive at half charge, because the cold takes the rest. The driver meets you in a plowed lot rather than a drifted street.',
 'A car coming from a warm state gets winter oil and a block heater before its first night. An electric car should land with half a charge, because the cold takes a share. The driver meets you where the lot is plowed.'),
('One adds a Great Falls stop when the load lines up. Give us a week of dates and we catch the next truck through. A single fixed date can mean waiting for one.',
 'One adds a Great Falls stop when the load lines up. With a week of dates we can book the next truck through. Insist on one day, and you may wait for it.'),
('The PCS season at the base runs June through August, and the carriers fill with second cars. Book three weeks ahead for a July date.',
 'From June through August the base turns over, and the carriers fill with second cars. A July date is a three-week-ahead booking.'),
('Orders pay to move one vehicle, and the second one ships with us. Ship Guy is a private broker with no connection to the Air Force. The timing around orders is laid out on the <a href="military-car-shipping.html">military</a> page.',
 'The orders cover one vehicle. The family ships the other one with us. Ship Guy is a private broker and has no connection to the Air Force. How orders shape the timing is laid out on the <a href="military-car-shipping.html">military</a> page.'),
('Orders pay to move one vehicle, and the second one ships with us. Ship Guy is a private broker with no connection to the Air Force."',
 'The orders cover one vehicle, and the family ships the other one with us. Ship Guy is a private broker and has no connection to the Air Force."'),
('Yes. A carrier with a winch takes it, and the loading time is in the quote from day one. On a pass-through road that narrows which trucks can stop. The big-box lots on Tenth Avenue South give the driver level ground. Say whether it rolls, steers, and brakes.',
 'Yes. We book a carrier with a winch and build the loading time into the quote. Fewer trucks can take a non-runner on a pass-through road, so give us room on the dates. The big-box lots on Tenth Avenue South are level. Does it roll, steer, and brake? Tell us which.'),
('The two addresses, with the neighborhood or the town and the nearest highway. The year, make, and model. Whether it runs. Open or enclosed. The widest week of dates you can give. Those five put a Great Falls number in your inbox the same day.',
 'Pickup and delivery, with the neighborhood or the town and the nearest highway. Year, make, and model. Whether it starts. Open or enclosed. The widest week you can give us. With those, a Great Falls number comes back the same day.'),
("'*2026 estimates from Great Falls for a sedan that runs, on an open trailer. Figure 10 to 25 percent more for an SUV or a pickup, and more for enclosed. On a pass-through corridor your week of dates and the trucks crossing that week set the real quote.'",
 "'*2026 estimates from Great Falls, running sedan, open trailer. An SUV or a pickup costs 10 to 25 percent more, and enclosed more still. The week you can give us and the trucks on 15 and 90 that week set the real quote.'"),
('A daily driver or a student car rides open and arrives fine. The difference is laid out on the %s and %s pages.'%(OPEN,ENC),
 'A daily driver or a student car has no need of a roof. The %s and %s pages lay out the difference.'%(OPEN,ENC)),
('Nearly every car in the city rides open, and the lane table above is priced that way.','Almost every Great Falls car goes out on an open trailer, and the table above assumes one.'),
('Missoula and Billings are a day away and the lowest lanes on the table. Figure 10 to 25 percent more for an SUV or a pickup.',
 'Missoula and Billings are a day away and cost the least. An SUV or a pickup runs 10 to 25 percent higher.'),
])

# ---------------- Charleston
fix('build_charleston_local.py', [
('Orders pay to move one vehicle, and the second one ships with us. Ship Guy is a private broker with no connection to the base. The <a href="military-car-shipping.html">military</a> page explains the timing around orders.',
 'The orders pay for one car, and the family ships the second one with us. Ship Guy is a private broker and has no tie to the base. The <a href="military-car-shipping.html">military</a> page explains how orders set the timing.'),
('Orders pay to move one vehicle, and the second one ships with us. Ship Guy is a private broker with no connection to the base."',
 'The orders pay for one car, and the family ships the second one with us. Ship Guy is a private broker and has no tie to the base."'),
('The PCS season at the base runs June through August, and the carriers fill with second cars. Book three weeks ahead for a July date.',
 'The base turns over from June through August, and second cars fill the carriers. A July pickup wants three weeks of notice.'),
('A parent books it from home, and an adult meets the truck at a lot to sign. The window follows the date.',
 'The parent handles the booking, and any adult can sign at the lot. The date sets the window.'),
('A parent books it from home, and an adult meets the truck at a lot to sign. The software companies',
 'The parent handles the booking, and any adult can sign at the lot. The software companies'),
('Most Lowcountry cars ride open, and the lane table above assumes an open trailer.','Open trailers carry most of the cars in the Lowcountry, and the table above is priced for one.'),
('A daily driver or a student car rides open and arrives fine. The %s and %s pages compare the two.'%(OPEN,ENC),
 'A daily driver or a student car is fine on an open trailer. Compare the two on the %s and %s pages.'%(OPEN,ENC)),
('Approve the price, and a carrier already coming over on 26 that week takes the car. The lot and the window are confirmed before the day ends. At pickup the driver walks the car with you and logs its condition on the Bill of Lading. You countersign, and the delivery inspection is held to that sheet.',
 'Approve the price, and a carrier already coming over on 26 that week gets the job. Lot and window are settled by the end of the day. The driver photographs the car at pickup and writes up its condition on the Bill of Lading. You countersign, and the delivery inspection is held to that sheet.'),
('The second car usually rides a trailer. If an employer is reimbursing the move, the paperwork comes from us."','The second car usually rides a trailer. Reimbursed by an employer? The paperwork comes from us."'),
('If an employer is reimbursing the move, the paperwork comes from us.\'),','When an employer reimburses the move, we supply the paperwork it asks for.\'),'),
('Savannah and Columbia are two hours away and the lowest lanes on the table. An SUV or a pickup adds about 10 to 25 percent.',
 'Savannah and Columbia are two hours away and cost the least. Add about 10 to 25 percent for an SUV or a pickup.'),
])

# ---------------- Bloomington
fix('build_bloomington_local.py', [
("'Rochester, Duluth, Fargo, and Des Moines are same-day runs. Milwaukee, Omaha, Chicago, and Kansas City need a day. Denver needs two, and Phoenix and Florida need three to four.'",
 "'Rochester, Duluth, Des Moines, and Fargo ride a single day on the truck. Milwaukee, Omaha, Chicago, and Kansas City take a day. Denver takes two, and Arizona and Florida take three to four.'"),
('Most south-metro cars ride open, and the lane table above assumes an open trailer.','Open trailers carry most of the south metro, and the table above is priced for one.'),
('A daily driver or a student car rides open and arrives fine. The %s and %s pages compare the two.'%(OPEN,ENC),
 'A daily driver or a student car belongs on an open trailer. The %s and %s pages explain where enclosed earns its price.'%(OPEN,ENC)),
('Approve the price, and a carrier already riding 494 that week is booked. The lot and the window are confirmed before the day ends. At pickup the driver walks the car with you and records its condition on the Bill of Lading. You countersign, and delivery is checked against that sheet.',
 'Approve the price, and we book a carrier already riding 494 that week. Lot and window are settled the same afternoon. At pickup the driver and you go over the car together, and every mark goes on the Bill of Lading. You countersign, and delivery is checked against it.'),
('Rochester and Duluth are short hops and the lowest lanes on the table. SUVs and pickups run 10 to 25 percent more.',
 'Rochester and Duluth are short hops and cost the least. An SUV or a pickup runs 10 to 25 percent higher.'),
('Retirees leave for Arizona and Florida each October and come back in April. Families moving across the river to Burnsville or Eagan ship one car and drive the other. The %s page covers the paperwork for an interstate move.'%STS,
 'The snowbirds head for Arizona and Florida each October and return in April. Families moving across the river to Burnsville or Eagan ship one car and drive the other. Crossing a state line is covered on the %s page.'%STS),
])

# ---------------- Bellevue
fix('build_bellevue_local.py', [
('Los Angeles runs eight hundred to eleven hundred fifty dollars for a sedan. That is about eleven hundred thirty-five miles down 5. San Francisco runs six hundred to eight hundred eighty, about eight hundred ten miles. Spokane runs two hundred sixty to three hundred ninety over the pass. Portland is the lowest lane on the table. An SUV or a pickup runs 10 to 25 percent more.',
 'Los Angeles is about eleven hundred thirty-five miles down 5 and runs eight hundred to eleven hundred fifty dollars for a sedan. San Francisco is eight hundred ten miles and runs six hundred to eight hundred eighty. Spokane over the pass runs two hundred sixty to three hundred ninety. Portland costs the least of all. An SUV or a pickup runs 10 to 25 percent more.'),
('Most Eastside cars ride open, and the lane table above assumes an open trailer.','Open trailers carry most of the Eastside, and the table above is priced for one.'),
('the second one rides a trailer with us. If an employer is reimbursing the move, we produce the paperwork it wants."','the second one rides a trailer with us. Reimbursed by an employer? We produce the paperwork it wants."'),
])

# ---------------- Eugene
fix('build_eugene_local.py', [
('Retirees leave for Arizona each October and come back in April. The %s page covers the paperwork for an interstate move.'%STS,
 'Retirees go south to Arizona in October and return in April. Crossing state lines is covered on the %s page.'%STS),
('Most valley cars ride open, and the lane table above assumes an open trailer.','Open trailers carry most of the valley, and the table above is priced for one.'),
('A commuter car or a student car rides open and arrives fine. The %s and %s pages put the two side by side.'%(OPEN,ENC),
 'A commuter car or a student car has no need of a roof. The %s and %s pages put the two side by side.'%(OPEN,ENC)),
('A parent books it from home, and an adult meets the truck at the stadium lots to sign. Fairmount and the campus blocks are closed to a trailer that week. The window follows the date.',
 'The parent books from home, and an adult signs at the stadium lots. Fairmount and the campus blocks are closed to a trailer that week. The date sets the window.'),
('Portland is two hours away and the lowest lane on the table. An SUV or a pickup adds about 10 to 25 percent.',
 'Portland is two hours away and costs the least. Add about 10 to 25 percent for an SUV or a pickup.'),
])

# ---------------- Santa Fe
fix('build_santafe_local.py', [
('A new governor brings an appointee class every fourth January. If the state or an employer is reimbursing the move, the receipts come from us.',
 'Every fourth January a new governor arrives with a class of appointees. When the state or an employer reimburses the move, the receipts come from us.'),
('Most Santa Fe cars ride open, and the lane table above assumes an open trailer.','Open trailers carry most of Santa Fe, and the table above is priced for one.'),
('A commuter car or a student car rides open and arrives fine. The %s and %s pages set the two side by side.'%(OPEN,ENC),
 'A commuter car or a student car is an open-trailer car. The %s and %s pages set the two side by side.'%(OPEN,ENC)),
("plan on a lot\",\n ])+prose(P('The order of events is on the %s page. The checklist is on the %s page.'))))"%(HIW,PREP),
 "plan on a lot\",\n ])+prose(P('The %s page covers the sequence, and the %s page covers the checklist.'))))"%(HIW,PREP)),
('Albuquerque is an hour away and the lowest lane on the table. An SUV or a pickup adds roughly 10 to 25 percent.',
 'Albuquerque is an hour away and costs the least. An SUV or a pickup adds roughly 10 to 25 percent.'),
])
