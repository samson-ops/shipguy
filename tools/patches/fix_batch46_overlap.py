"""Batch 46 fresh-wording pass: the five pages shared the pass-through, PCS, checklist, open-trailer and standard-block phrasings with Batches 44–45."""
D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    if pairs and all(s.count(o[0])==0 for o in pairs): print(fn,'already applied'); return
    for item in pairs:
        old,new=item[0],item[1]; k=item[2] if len(item)>2 else 1
        c=s.count(old); assert c==k, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'rewrites')
HIW='<a href="how-it-works.html">how it works</a>'; PREP='<a href="car-shipping-preparation.html">preparation</a>'
OPEN='<a href="open-car-transport.html">open</a>'; ENC='<a href="enclosed-auto-transport.html">enclosed</a>'; MIL='<a href="military-car-shipping.html">military</a>'

# ---------------- Sioux Falls (shared most with Bismarck, Fargo, Cheyenne)
fix('build_siouxfalls_local.py', [
("'Sioux City is a short hop. Omaha, Minneapolis, Fargo, and Des Moines are a day on the truck. Kansas City and Rapid City take one to two. Chicago and Denver take two, and Dallas takes three.'",
 "'Sioux City is ninety minutes. Omaha, Minneapolis, Fargo, and Des Moines ride a day on the truck. Kansas City and Rapid City ride one to two, Chicago and Denver two, and Dallas three.'"),
('The orders cover one car, and the family ships the other one with us. Ship Guy is a private broker and has no connection to either. The %s page explains how orders set the timing.'%MIL,
 'Orders pay for one car, so the second one comes to us. Ship Guy is a private broker with no tie to either base. Our %s page walks through the timing around orders.'%MIL),
('  "Everything personal out of the car, trunk and console included",\n  "Fuel at about a quarter tank",\n  "Photos of each side and the odometer, taken the morning of pickup",\n  "A key that works, plus a note about anything that sticks",\n  "Aftermarket alarm off",',
 '  "Empty the car of anything that belongs to you, trunk included",\n  "Run the gas down to a quarter tank",\n  "Shoot each side and the mileage before the truck pulls up",\n  "Hand over a working key and mention anything that sticks",\n  "Aftermarket alarm off",'),
("The sequence is laid out on the %s page, and the checklist on the %s page."%(HIW,PREP),"The %s page lays out the steps. The %s page lists what to do before the truck comes."%(HIW,PREP)),
('Yes. Both campuses take cars in late August and send them home in May. The parent books it, and an adult signs at the lot.',
 'Yes. Student cars arrive at both campuses in late August and leave in May. Parents book, and whoever meets the truck signs, as long as they are an adult.'),
('Yes. We book a carrier with a winch and build the loading time into the quote. Fewer trucks can take a non-runner on a pass-through road, so give us room on the dates. The mall lots at 41st and Louise are level. Let us know whether it rolls, steers, and brakes.',
 'Yes. The quote includes a winch carrier and the loading time, so nothing is added later. A non-runner narrows the trucks that can stop, so leave room on the dates. The mall lots at 41st and Louise are level. Does it roll, steer, and brake? Say which.'),
('Where the car is and where it goes, with the neighborhood or the town. Year, make, and model. Running or not. Open or enclosed. The widest week of dates you can live with. Answer those, and a Sioux Falls number is back the same day.',
 'Pickup and delivery, with the neighborhood or the town. The year, make, and model. Does it start. Open or enclosed. The widest week of dates you can offer. Five answers, and the Sioux Falls number lands in your inbox the same day.'),
('A closure usually lasts a day, and the truck arrives a day or two late. We tell you before the driver does. Park in the driveway and leave the block heater plugged in.',
 'A closure runs a day, and the truck shows up a day or two behind. You hear it from us first. Keep the car in the driveway with the block heater plugged in.'),
('A car from a warm state wants winter oil and a block heater before its first cold snap. An electric car wants half a charge on arrival.',
 'A car from the south needs winter oil and a block heater before the first cold snap. An electric car should arrive with half a charge.'),
("'*2026 estimates from Sioux Falls, running sedan, open trailer. Count on 10 to 25 percent more for an SUV or a pickup, and more for enclosed. Your week of dates and the trucks crossing on 29 and 90 that week set the real quote.'",
 "'*2026 estimates from Sioux Falls for a sedan that runs, on an open trailer. An SUV or a pickup runs 10 to 25 percent higher, and enclosed higher again. The dates you offer and the trucks crossing on 29 and 90 that week set the real quote.'"),
])

# ---------------- Cheyenne (shared most with Great Falls)
fix('build_cheyenne_local.py', [
('The orders cover one vehicle, and the family ships the other one with us. Ship Guy is a private broker and has no connection to the Air Force. How orders shape the timing is laid out on the %s page.'%MIL,
 'The government moves one vehicle on orders, and the family sends the second one with us. Ship Guy is a private broker and has nothing to do with the Air Force. The %s page explains how orders change the timing.'%MIL),
('Yes, and summer is the peak. The missile wing rotates airmen and officers on orders all year. Housing is behind the gate, so the handoff happens outside it or at a lot on Dell Range. The orders cover one vehicle, and the family ships the other one with us. Ship Guy is a private broker and has no connection to the Air Force.',
 'Yes, with the peak in summer. Airmen and officers rotate through the missile wing on orders all year. Housing sits behind the gate, so the truck meets you outside it or at a lot on Dell Range. The government moves one vehicle, and the family sends the second one with us. Ship Guy is a private broker and has nothing to do with the Air Force.'),
('  "Everything that is yours out of the car, trunk included",\n  "Fuel at a quarter tank or so",\n  "Photos of each side and the odometer that morning",\n  "A key that works, and a word about anything that sticks",\n  "Add-on alarm switched off",',
 '  "Clear the car of your belongings, trunk and glovebox too",\n  "Gas gauge around a quarter",\n  "Take your own photos of each side and the mileage that morning",\n  "A key the driver can use, plus a heads-up on any quirks",\n  "Add-on alarm switched off",'),
("The %s page has the sequence. The %s page has the full checklist."%(HIW,PREP),"Every step is on the %s page, and the whole checklist is on the %s page."%(HIW,PREP)),
('Where the car is and where it goes, with the neighborhood and whether the road is paved. Year, make, and model. Whether it starts. Open or enclosed. The widest week of dates you can give. With those, a Cheyenne number comes back the same day.',
 'Both ends of the move, with the neighborhood and whether the road is paved. Year, make, and model. Running or not. Open or enclosed. The widest week of dates you can live with. Those five, and the Cheyenne number is back before the day ends.'),
('A car from a warm state wants winter oil and a block heater before its first night. An electric car wants half a charge on arrival, because the cold and the altitude take a share. The driver meets you in a plowed lot rather than a drifted street.',
 'Winter oil and a block heater go in before a car from the south spends its first night here. An electric car should land with half a charge, since the cold and the altitude take a share. The truck meets you in a plowed lot, not a drifted street.'),
('Yes. We book a carrier with a winch and build the loading time into the quote. Fewer trucks can take a non-runner on a pass-through road, so give us room on the dates. The mall lots on Dell Range are level. Tell us whether it rolls, steers, and brakes.',
 'Yes. A winch carrier and the loading time are built into the number from the start. A non-runner narrows which trucks can stop on 80, so give us room on the dates. The mall lots on Dell Range are level. Tell us whether it rolls, steers, and brakes.'),
('A commuter car or a student car does fine on an open trailer. The %s and %s pages show where the line falls.'%(OPEN,ENC),
 'A commuter car or a student car belongs on an open trailer. The %s and %s pages show where the line falls.'%(OPEN,ENC)),
('Nearly every Cheyenne car goes out on an open trailer, and the table above assumes one.','Almost every car in Cheyenne leaves on an open trailer, and the table above is priced that way.'),
('One coordinator handles the move from the quote to the delivery photo. The <a href="services.html">services</a> page compares open, enclosed, and expedited.',
 'A single coordinator carries the move from the quote to the delivery photo. Open, enclosed, and expedited are compared on the <a href="services.html">services</a> page.'),
])

# ---------------- Charleston WV
fix('build_charlestonwv_local.py', [
('Open trailers carry most of the valley, and the table above is priced for one.','Most Kanawha Valley cars go out on an open trailer, and the table above assumes one.'),
('A car headed over the mountains in January often rides enclosed too.','A car crossing the mountains in January often goes enclosed as well.'),
('A commuter car or a student car needs nothing more than an open trailer. The %s and %s pages lay the two side by side.'%(OPEN,ENC),
 'A commuter car or a student car is an open-trailer car. The %s and %s pages lay the two side by side.'%(OPEN,ENC)),
('  "Your things out of the car, trunk included",\n  "A quarter tank of gas, give or take",\n  "Photos of each side and the odometer before the truck comes",\n  "A key the driver can use, and a note about anything that sticks",\n  "Any add-on alarm turned off",',
 '  "Belongings out, trunk included",\n  "About a quarter tank of gas",\n  "Your own photos of the car and the mileage, taken the day of pickup",\n  "A working key, and a word about anything that sticks or leaks",\n  "Aftermarket alarm disabled",'),
('The orders cover one car, and the family ships the other one with us. Ship Guy is a private broker and has no connection to the Guard. The %s page explains how orders set the timing.'%MIL,
 'Orders move one car, and the second one rides with us. Ship Guy is a private broker with no tie to the Guard. Our %s page covers the timing around orders.'%MIL),
('Yes. Both campuses take cars in late August and send them home in May. The parent books it, and an adult signs at a lot. The river campus is tight that week, so the meeting point is the Capitol lots. Give us a range around the date.',
 'Yes. Student cars reach both campuses in late August and head home in May. A parent sets it up, and any adult can sign at the lot. The river campus is tight that week, so the truck meets you at the Capitol lots. Give us a range around the date.'),
('Yes. We book a carrier with a winch and build the loading time into the quote. The Southridge lots or the Kanawha City lots give the driver level ground. Does it roll, steer, and brake? Tell us which.',
 'Yes. The carrier brings a winch, and the loading time is priced in from the start. The Southridge lots or the Kanawha City lots are level. Does it roll, steer, and brake? Tell us which.'),
('Yes, every week. The agencies transfer staff on start dates all year, and the session brings a crowd each January. The medical center brings residents each June and hires traveling nurses year round. When the state or an employer reimburses the move, we supply the receipts.',
 'Yes, every week. The agencies move staff on start dates all year, and the session brings a crowd each January. Residents reach the medical center each June, and traveling nurses arrive year round. When the state or an employer reimburses the move, we supply the receipts.'),
])

# ---------------- Norfolk (shared with Charleston SC and Virginia Beach)
fix('build_norfolk_local.py', [
("'Richmond, Raleigh, Washington, and Baltimore are same-day runs. Philadelphia, Charlotte, and New York need a day. Atlanta needs one to two, and Florida needs two.'",
 "'Richmond, Raleigh, Washington, and Baltimore ride a single day on the truck. Philadelphia, Charlotte, and New York take a day. Atlanta takes one to two, and Florida takes two.'"),
('  "Personal items out of the car, including the trunk",\n  "Gas at about a quarter tank",\n  "Your own photos of each side and the odometer that morning",\n  "A working key, and a note about anything that sticks or leaks",\n  "Any add-on alarm turned off",',
 '  "Everything personal out of the cabin and the trunk",\n  "Fuel down to a quarter tank",\n  "Photograph each side and the odometer before the truck comes",\n  "One good key, and a note about any known faults",\n  "Any add-on alarm turned off",'),
("The sequence is on the %s page, and the checklist is on the %s page."%(HIW,PREP),"Read the %s page for the sequence and the %s page for the pickup checklist."%(HIW,PREP)),
('Yes. A carrier with a winch is booked, and the loading time is priced from the start. The Wards Corner lots or the big-box lots on Military Highway give the driver level ground. Say whether it rolls, steers, and brakes.',
 'Yes. We send a carrier with a winch and quote the loading time up front. The Wards Corner lots or the big-box lots on Military Highway are level. Tell us whether it rolls, steers, and brakes.'),
('We tell you the moment a watch is posted. A car leaving ahead of the storm rides whatever is available.','You hear from us the moment a watch goes up. A car leaving ahead of the storm takes whatever truck is available.'),
('A pickup in an evacuation waits for the all-clear. You hear it from us the moment a watch is posted.','A pickup in an evacuation waits for the all-clear, and we call the moment a watch goes up.'),
('A car leaving ahead of a hurricane rides whatever is available, and we say so.','A car leaving ahead of a hurricane takes whatever truck is available, and we say so.'),
('Both addresses, with the neighborhood and the base if there is one. The year, make, and model. Whether it runs. Open or enclosed. The week around the report date or the move. Five answers, and a Norfolk number is back the same day.',
 'Start and finish, with the neighborhood and the base if there is one. Year, make, and model. Running or not. Open or enclosed. The week around the report date or the move. Give us those five, and the Norfolk number is back before the day ends.'),
('Most pickups happen within 1 to 3 days. The Richmond carriers come down 64 every day, and the 95 trucks turn east at Petersburg. The port keeps more based on the Southside.',
 'Most pickups happen within 1 to 3 days. The Richmond carriers come down 64 daily, the 95 trucks turn east at Petersburg, and the port keeps a pool based on the Southside.'),
('At pickup the driver photographs the car and records its condition on the Bill of Lading. You initial the sheet, and the delivery inspection is held to it.',
 'At pickup the driver photographs the car and writes its condition on the Bill of Lading. You initial the sheet, and it is the reference at delivery.'),
])

# ---------------- Bethlehem (shared with Eugene, Greensboro, Allentown)
fix('build_bethlehem_local.py', [
('Open trailers carry most of the valley, and the table above is priced for one.','Most Lehigh Valley cars travel on an open trailer, and the table above is priced for one.'),
('A commuter car or a student car does fine on an open trailer. The %s and %s pages explain where enclosed earns its price.'%(OPEN,ENC),
 'A commuter car or a student car has no need of a roof. The %s and %s pages explain where enclosed earns its price.'%(OPEN,ENC)),
('  "Anything personal out of the car, trunk included",\n  "Fuel near a quarter tank",\n  "Photos of each side and the odometer, taken that morning",\n  "One working key, and a note about anything that sticks or leaks",\n  "Any add-on alarm turned off",',
 '  "Personal things out of the car, glovebox and trunk included",\n  "Roughly a quarter tank of gas",\n  "Snap each side and the mileage the morning of pickup",\n  "A key that works, plus a note about anything that leaks",\n  "Aftermarket alarm switched off",'),
("The %s page has the order of events. The %s page has the full checklist."%(HIW,PREP),"The order of events is on the %s page, and the full checklist is on the %s page."%(HIW,PREP)),
('New York runs one hundred seventy to two hundred eighty dollars for a sedan. That is about eighty-five miles out 78.','New York is about eighty-five miles out 78 and runs one hundred seventy to two hundred eighty dollars for a sedan.'),
('At pickup the driver circles the car with you and notes every mark on the Bill of Lading. You countersign, and delivery is checked against that sheet.',
 'At pickup the driver circles the car with you and marks every blemish on the Bill of Lading. You countersign, and the delivery inspection is checked against those marks.'),
('Yes. A winch truck is booked, and the loading time is in the price from the start. The casino lots or the Route 33 big-box lots give the driver level ground. Say whether it rolls, steers, and brakes.',
 'Yes. The quote covers a winch truck and the loading time, with nothing added later. The casino lots or the Route 33 big-box lots are level. Let us know whether it rolls, steers, and brakes.'),
('Both ends of the move, with the neighborhood or the township. The year, make, and model. Whether it runs. Open or enclosed. The week around the move-in or the start date. Five answers, and a Bethlehem number is back the same day.',
 'Where the car is and where it goes, with the neighborhood or the township. The year, make, and model. Whether it drives. Open or enclosed. The week around the move-in or the start date. With those five, a Bethlehem number is back the same day.'),
('The hospital network brings residents each June and hires traveling nurses year round. The device maker, the diagnostics company, and the warehouses relocate staff on start dates all year. When an employer reimburses the move, we produce the receipts it needs.',
 'Residents reach the hospital network each June, and traveling nurses arrive year round. The device maker, the diagnostics company, and the warehouses relocate staff all year. When an employer reimburses the move, the receipts come from us.'),
])

# ---------------- second pass (22.4–24.3% after the first)
fix('build_siouxfalls_local.py', [
("A number, a lot at the mall, and a signature at delivery. The week of dates decides which truck.","A price, a meeting spot at the mall, and a signature at delivery. Your week of dates picks the truck."),
("Approve the price, and we watch for a carrier crossing on 29 or 90 that week. The lot and the window are confirmed once one commits. At pickup the driver circles the car with you and lists every mark on the Bill of Lading. You sign the sheet, and delivery is measured against it.",
 "Say yes, and we line up a carrier crossing on 29 or 90 that week. Once one commits, the lot and the window are set. The driver photographs the car at pickup and lists every mark on the Bill of Lading, and you sign the sheet. Delivery is measured against it."),
("Our FMCSA license and our $75,000 bond are listed on the federal register for anyone to read. The office is on South Reid Street.","Look up our FMCSA license and our $75,000 bond on the federal register any time. The office is on South Reid Street."),
("A car heading south before the first blizzard often rides enclosed too.","Snowbirds sending a car south before the first blizzard often choose enclosed as well."),
("A commuter car or a student car is fine on an open trailer. The %s and %s pages explain where enclosed earns its price."%('<a href="open-car-transport.html">open</a>','<a href="enclosed-auto-transport.html">enclosed</a>'),
 "A commuter car or a student car travels open and arrives fine. Where enclosed earns its price is explained on the %s and %s pages."%('<a href="open-car-transport.html">open</a>','<a href="enclosed-auto-transport.html">enclosed</a>')),
("They send them home in May. The parent books it, and an adult signs at the lot.","They send them home in May. Mom or Dad books, and an adult at the lot signs."),
("A start date at the card centers or the late August move-in lands in a busy week. The <a href=\"car-shipping-cost.html\">cost guide</a> explains what size, condition, and the date range do to the number.",
 "A start date at the card centers or the late August move-in means a busy week. How size, condition, and the date range shape the number is in the <a href=\"car-shipping-cost.html\">cost guide</a>."),
("  \"Empty the car of anything that belongs to you, trunk included\",","  \"Empty the car of anything that belongs to you, trunk and console included\","),
])
fix('build_cheyenne_local.py', [
("A number, a lot on Dell Range, and a signature at delivery. The week of dates decides the truck.","A price, a meeting spot on Dell Range, and a signature at delivery. Your dates pick the truck."),
("Approve the price, and we watch for a carrier on 80 or the Denver pool that week. The lot and the window are confirmed the moment one commits. At pickup the driver walks the car with you and notes every mark on the Bill of Lading. You initial it, and the delivery inspection is held to it.",
 "Say yes, and we line up a carrier on 80 or from the Denver pool that week. The moment one commits, the lot and the window are set. The driver goes around the car with you at pickup and notes each mark on the Bill of Lading. Your initials go on it, and delivery is held to it."),
("A car headed over the Summit in January often rides enclosed too.","A car crossing the Summit in January often goes enclosed as well."),
("The parent books it, and an adult signs at a lot. The university over the Summit","Mom or Dad books, and an adult signs at a lot. The university over the Summit"),
("The parent books it, and an adult signs at a lot. The college lots on College Drive are the meeting point.","Mom or Dad books, and an adult signs at a lot. The college lots on College Drive are the meeting point."),
("State government fills the Capitol and the office blocks around it. The agencies transfer staff on start dates all year, and the legislature brings a crowd each winter.",
 "State government fills the Capitol and the blocks around it. The agencies move staff in on start dates all year, and the legislature brings a crowd each winter."),
("Housing sits behind the gate, so the truck meets you outside it or at a lot on Dell Range.","Housing sits behind the gate, so the truck meets you outside it or on Dell Range."),
("Winter oil and a block heater go in before a car from the south spends its first night here.","A car from the south gets winter oil and a block heater before its first night here."),
])
fix('build_charlestonwv_local.py', [
("A number, a lot at Southridge or in Kanawha City, and a signature at delivery. The session or the start date picks the week.","A price, a meeting spot at Southridge, and a signature at delivery. The session or the start date picks the week."),
("Our FMCSA license and our $75,000 bond sit on the federal register for anyone to read. The office is on Capitol Street downtown.","The federal register carries our FMCSA license and our $75,000 bond for anyone to see. The office is on Capitol Street downtown."),
("The parent books it, and an adult signs at a lot. The Guard wing","Mom or Dad books, and an adult signs at a lot. The Guard wing"),
("A session start in January or the June move-out lands in a busy week. The <a href=\"car-shipping-cost.html\">cost guide</a> explains what size, condition, and the date range do to the number.",
 "A session start in January or the June move-out means a busy week. How size, condition, and the dates shape the number is in the <a href=\"car-shipping-cost.html\">cost guide</a>."),
("State government fills the Capitol complex on the East End and the office blocks downtown. The agencies transfer staff on start dates all year.",
 "State government fills the Capitol complex on the East End and the office blocks downtown. The agencies move staff in on start dates all year."),
])
fix('build_norfolk_local.py', [
("A number, a lot at Wards Corner, and a signature at delivery. The report date or the move-in picks the week.","A price, a meeting spot at Wards Corner, and a signature at delivery. The report date or the move-in picks the week."),
("The parent books it, and an adult signs at a lot.'),","Mom or Dad books, and an adult signs at a lot.'),"),
("The parent books it, and an adult signs at a lot. Lambert’s Point","Mom or Dad books, and an adult signs at a lot. Lambert’s Point"),
("The Richmond carriers come down 64 daily, the 95 trucks turn east at Petersburg, and the port keeps a pool based on the Southside.","The Richmond carriers come down 64 daily, and the 95 trucks turn east at Petersburg. The port keeps a pool based on the Southside."),
("From that point it is a domestic move like any other. Give us the release date and the terminal name.","From that point it moves like any other car. Send the release date and the terminal name."),
("A private car that arrived by ship and cleared customs is a domestic move from that point. Give us the release date and the terminal.","A private car that arrived by ship and cleared customs moves like any other car from that point. Send the release date and the terminal."),
])
fix('build_bethlehem_local.py', [
("A number, a lot at the casino or on Route 33, and a signature at delivery. The move-in date or the start date picks the week.","A price, a meeting spot at the casino, and a signature at delivery. The move-in date or the start date picks the week."),
("Our FMCSA license and our $75,000 bond are on the federal register, open to anyone. The office is on Lynn Avenue on the South Side.","The federal register shows our FMCSA license and our $75,000 bond to anyone who looks. The office is on Lynn Avenue on the South Side."),
("The parent books it, and an adult signs at a lot. The campus hill is closed","Mom or Dad books, and an adult signs at a lot. The campus hill is closed"),
("The parent books it, and an adult signs at a lot. The hill is closed","Mom or Dad books, and an adult signs at a lot. The hill is closed"),
("The order of events is on the <a href=\"how-it-works.html\">how it works</a> page, and the full checklist is on the <a href=\"car-shipping-preparation.html\">preparation</a> page.",
 "The <a href=\"how-it-works.html\">how it works</a> page walks the steps. The <a href=\"car-shipping-preparation.html\">preparation</a> page has the full checklist."),
("New York is about eighty-five miles out 78 and runs one hundred seventy to two hundred eighty dollars for a sedan.","New York is eighty-five miles out 78 and runs one hundred seventy to two hundred eighty dollars for a sedan."),
("The university on the hill takes student cars in late August and sends them home in May. The university on the north side does the same.","Student cars reach the hill in late August and leave in May. The university on the north side runs the same calendar."),
])

# ---------------- third pass: Norfolk (vs Charleston SC) and Bethlehem (vs Charleston WV / Eugene)
fix('build_norfolk_local.py', [
("The orders pay for one car. The family ships the second one with us. Ship Guy is a private broker and has no tie to the Navy.","The Navy moves one car on orders. The family sends the second one with us, and Ship Guy is a private broker with no tie to the Navy."),
("The orders pay for one car, and the family ships the second one with us. Housing is behind the gates, so the handoff happens outside them or at Wards Corner.","The Navy moves one car on orders, and the family sends the second one with us. Housing sits behind the gates, so the truck meets you outside them or at Wards Corner."),
("Housing is behind the gates, so the handoff happens outside them or at Wards Corner. The Navy moves one car on orders.","Housing sits behind the gates, so the truck meets you outside them or at Wards Corner. The Navy moves one car on orders."),
("Hurricane season runs June through November. Isabel in 2003 is the benchmark.","The storms run June through November. Isabel in 2003 is still the benchmark."),
("When the governor orders an evacuation, the tunnels close and the carriers stage in Richmond.","An evacuation order closes the tunnels, and the carriers stage in Richmond."),
("Summer is the moving season, so book three weeks ahead.","Summer is the Navy’s moving season, so a July date wants three weeks of notice."),
("Yes, once customs has released it and the terminal has signed it out. From that point it moves like any other car. Send the release date and the terminal name.","Yes. Once customs releases it and the terminal signs it out, it moves like any other car. We need the release date and the terminal name."),
])
fix('build_bethlehem_local.py', [
("Winter brings thirty inches of snow and more ice than the hills can take.","Winter drops thirty inches of snow on the valley and more ice than its hills can take."),
("A winter pickup can lose a day, and you hear it from us before the driver does.","A winter pickup can slip a day, and the word comes from us before the driver."),
("Retirees leave for Florida each October and come back in April.","The retirees go to Florida in October and return in April."),
("Move-in week in late August fills the hill and the north side campus.","Move-in week in late August packs the hill and the north side campus."),
("New York is eighty-five miles out 78 and runs one hundred seventy to two hundred eighty dollars for a sedan.","New York is eighty-five miles out 78 and runs one hundred seventy to two hundred eighty dollars."),
])
fix('build_siouxfalls_local.py', [
("The driver photographs the car at pickup and lists every mark on the Bill of Lading, and you sign the sheet.","The driver photographs the car at pickup and lists every mark on the Bill of Lading. You sign the sheet."),
])
fix('build_cheyenne_local.py', [
("The driver goes around the car with you at pickup and notes each mark on the Bill of Lading.","The driver goes around the car with you and notes each mark on the Bill of Lading."),
])
