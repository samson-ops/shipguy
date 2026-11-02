"""Fresh wording for the standard blocks on the six Batch 43 pages (they shared Batch 42's phrasings and each other's).
Pass 1 (Warwick, applied earlier) is kept at the bottom under APPLIED for the record."""
D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    if pairs and s.count(pairs[0][0])==0 and pairs[0][1] in s:
        print(fn,'already applied'); return
    for item in pairs:
        old,new=item[0],item[1]; k=item[2] if len(item)>2 else 1
        c=s.count(old); assert c==k, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'rewrites')

HIW='<a href="how-it-works.html">how it works</a>'; PREP='<a href="car-shipping-preparation.html">preparation</a>'
SVC='<a href="services.html">services</a>'; OPEN='<a href="open-car-transport.html">open</a>'; ENC='<a href="enclosed-auto-transport.html">enclosed</a>'
MIL='<a href="military-car-shipping.html">military</a>'; MILC='<a href="military-car-shipping.html">military car shipping</a>'
STS='<a href="state-to-state-car-shipping.html">state-to-state</a>'; COST='<a href="car-shipping-cost.html">cost guide</a>'

# ---------------- Warwick (pass 2)
fix('build_warwick_local.py', [
("The %s covers vehicle size, condition, and the rest."%COST, "Size, condition, and the season are explained in the %s."%COST),
("Employer-reimbursed moves get their documentation from us.","When an employer reimburses the move, the paperwork comes from us.",2),
("The community college by the airport and the Providence campuses take cars each September and send them home in May.",
 "The community college by the airport and the Providence campuses take cars each September. They send them home in May."),
("Yes. A winch truck is assigned, and the loading time is in the quote from the start. The mall lots on Route 2 or the station lots at the airport give the driver level ground. Say whether the car rolls, steers, and brakes.",
 "Yes. A truck with a winch is assigned, and the loading time is quoted up front. The mall lots on Route 2 or the station lots at the airport give the driver level ground. Tell the coordinator whether it rolls, steers, and brakes."),
])

# ---------------- St. Paul
fix('build_stpaul_local.py', [
("Approve the price, and we book a carrier already running 94 through the city. The lot and the window are fixed the same day. At pickup the driver and you inspect the car together. The Bill of Lading records every existing mark. Both of you sign. Delivery is compared to that record.",
 "Approve the price, and a carrier already running 94 through the city is booked. The meeting lot and the window are confirmed that day. The driver photographs the car and logs its condition on the Bill of Lading with you watching. That log is the reference at delivery."),
('  "Cabin and trunk emptied of personal items",\n  "About a quarter tank of fuel",\n  "Photos of every side and the odometer before the truck arrives",\n  "A working key for the driver, with any fault named",\n  "Aftermarket alarm turned off",\n  "On Summit Hill, in Lowertown, or on the West Side, meet the truck at a lot",',
 '  "Clear out the glovebox, the console, and the trunk",\n  "A quarter tank is plenty",\n  "Take your own photos of the car and the mileage that morning",\n  "Hand over a working key and mention anything that sticks or leaks",\n  "Disable any add-on alarm",\n  "On Summit Hill, in Lowertown, or on the West Side, plan on a lot",'),
("Each step is covered on the %s and %s pages."%(HIW,PREP), "The sequence is on the %s page, and the checklist is on the %s page."%(HIW,PREP)),
("Our FMCSA license and $75,000 bond sit on the federal register, open to anyone. Our office is on Minnesota Street downtown.",
 "Look us up on the federal register and you will find the FMCSA license and the $75,000 bond. The office is on Minnesota Street downtown."),
("You get one coordinator from the first call to the last signature. The %s page lays out open, enclosed, and expedited transport."%SVC,
 "The coordinator who quotes the move answers the phone until the car is delivered. The %s page puts open, enclosed, and expedited next to each other."%SVC),
("A commuter sedan or a student car does fine in the open. The difference is spelled out on the %s and %s pages."%(OPEN,ENC),
 "A commuter sedan or a student car is a natural fit for the open trailer. The %s and %s pages explain the difference."%(OPEN,ENC)),
("A parent sets up the booking, and someone over eighteen signs at a lot. Campus streets are tight, so the handoff happens in the Midway or on Grand.",
 "The parent handles the booking by phone, and any adult can sign at the lot. Campus streets are tight, so the meeting point is the Midway or Grand Avenue."),
("Yes. The campuses take cars in each September and send them home in May. A parent sets up the booking, and someone over eighteen signs at a lot. Campus streets are tight that week, so the handoff happens in the Midway or on Grand Avenue. The window moves with the date.",
 "Yes. Cars arrive on the campuses each September and leave each May. The parent handles the booking by phone, and any adult can sign at the lot. Campus streets are jammed that week, so the meeting point is the Midway or Grand Avenue. The window follows the date."),
("Every four years a new administration moves an appointee class in January. The county and the city add their own transfers. If your employer reimburses the move, the paperwork comes from us.",
 "A new governor brings an appointee class to town every fourth January. The county and the city add their own transfers. Reimbursed by an employer? We supply the receipts the package needs."),
("The agencies transfer staff on start dates all year and move an appointee class every fourth January.",
 "The agencies transfer staff on start dates all year. A new governor brings an appointee class every fourth January."),
("Employer-reimbursed moves get their paperwork from us.","If an employer is reimbursing you, we supply the receipts."),
("Ship Guy is a private broker with no tie to them. PCS timing is on the %s page, and the interstate side is on the %s page."%(MIL,STS),
 "Ship Guy is a private broker with no tie to them. Orders and their timing are covered on the %s page. Crossing state lines is covered on the %s page."%(MIL,STS)),
("Both addresses, with the neighborhood or the suburb. Year, make, and model. Running or not. Open or enclosed. The week around the start date or the move-in. Five answers, and the St. Paul number is back within the day.",
 "Where it sits and where it goes, with the neighborhood or the suburb. The year, make, and model. Whether it drives. Open or enclosed. Your week. Those five, and the St. Paul price is in your inbox the same day."),
("The form above puts a number on your lane in about two minutes. Give us the neighborhood and the week, and a carrier already on 94 takes it.",
 "The form above takes two minutes and comes back with a price. Name the neighborhood and the week, and a carrier already on 94 does the rest."),
("A move timed to the September move-in or a January start date ships with the busiest weeks. The %s covers vehicle size, condition, and the rest."%COST,
 "A September move-in or a January start date lands in the busiest weeks of the year. Vehicle size, condition, and the other factors are explained in the %s."%COST),
("Yes. A winch truck is assigned, and the loading time is in the quote from the start. The Midway lots or the Rosedale lots give the driver level ground. Say whether the car rolls, steers, and brakes.",
 "Yes. The quote includes a winch truck and the extra loading time, so nothing is added later. The Midway lots or the Rosedale lots give the driver level ground. Tell us whether it rolls, steers, and brakes."),
])

# ---------------- Jackson
fix('build_jackson_local.py', [
("Say yes to the number, and we book a carrier already crossing at the Stack. The lot and the window are fixed the same day. At pickup you and the driver go around the car together. The Bill of Lading records every existing mark. Both of you sign it. Delivery is compared to that record.",
 "Say yes to the number, and a carrier already crossing at the Stack is booked. The lot and the window are nailed down before the day is out. At pickup the driver logs the car’s condition on the Bill of Lading, and you initial it. At delivery the car is checked against the same log."),
('  "Personal items out of the cabin and the trunk",\n  "Roughly a quarter tank of fuel",\n  "Each side and the odometer photographed before the truck comes",\n  "A working key for the driver, and a note of any fault",\n  "Any aftermarket alarm disabled",\n  "In Belhaven, Fondren, or West Jackson, meet the truck on a main road",',
 '  "Take everything out of the cabin and the trunk",\n  "Fuel around a quarter full",\n  "Your own photos of the car and the mileage that morning",\n  "A key that works, and a word about anything that leaks or sticks",\n  "Add-on alarm shut off",\n  "In Belhaven, Fondren, or West Jackson, plan on a main road, not the curb",'),
("Each step is laid out on the %s and %s pages."%(HIW,PREP), "Every step is on the %s page, and the %s page lists what to do before pickup."%(HIW,PREP)),
("Anyone can look up our FMCSA license and $75,000 bond on the federal register. Our office is on Bounds Street in Northeast Jackson.",
 "The federal register lists our FMCSA license and our $75,000 bond for anyone to check. The office is on Bounds Street in Northeast Jackson."),
("A single coordinator handles the move from the first call to the last signature. The %s page explains open, enclosed, and expedited transport."%SVC,
 "Whoever quotes your move stays on it until the car is delivered. The %s page compares open, enclosed, and expedited service."%SVC),
("A commuter car or a student car does fine in the open. The choice is spelled out on the %s and %s pages."%(OPEN,ENC),
 "A commuter car or a student car needs no roof. The %s and %s pages compare the two."%(OPEN,ENC)),
("A parent sets up the booking, and someone over eighteen signs at a lot. Campus streets are tight, so the handoff happens at the lots on Highway 80 or State Street.",
 "Parents book it, and whoever meets the truck signs, as long as they are an adult. Campus streets are tight, so the meeting point is a lot on Highway 80 or State Street."),
("Yes. The campuses take cars in each August and send them home in May. A parent sets up the booking, and someone over eighteen signs at a lot. Campus streets are tight that week. The handoff happens at the lots on Highway 80 or State Street. The window moves with the date.",
 "Yes. Cars reach the campuses each August and leave again in May. Parents book it, and whoever meets the truck signs, as long as they are an adult. Campus streets are jammed that week. The truck meets you at a lot on Highway 80 or State Street. The date sets the window."),
("Every four years a new administration moves an appointee class in January.","Each new governor brings a class of appointees in with the January inauguration."),
("The agencies transfer staff on start dates all year and move an appointee class every fourth January.",
 "The agencies transfer staff on start dates all year. Each new governor brings a class of appointees in January."),
("We produce the paperwork a reimbursed move needs.","If your employer reimburses moves, the receipts come from us.",2),
("Orders timing is on the %s page, and the interstate side is on the %s page."%(MIL,STS),
 "The %s page covers moves on orders. The %s page covers the interstate rules."%(MIL,STS)),
("The two addresses, with the side of town or the suburb. Year, make, and model. Does it run. Open or enclosed. The week around the start date or the move-in. Five answers, and the Jackson number comes back within the day.",
 "Pickup and delivery addresses, with the side of town. The year, make, and model. Whether it drives. Open or enclosed. The week you want. With those five we price the Jackson lane the same day."),
("The form above prices your lane in about two minutes. Give us the side of town and the week. A carrier already crossing at the Stack takes it.",
 "Price the lane on the form above in two minutes. Tell us the side of town and the week, and a carrier crossing at the Stack handles it."),
("A move timed to the August move-in or a plant hiring wave ships with the busiest weeks. The %s covers vehicle size, condition, and the rest."%COST,
 "An August move-in or a plant hiring wave falls in the busiest weeks. What size, condition, and season do to the price is in the %s."%COST),
("Yes. We assign a winch truck, and the loading time is in the quote from the start. The mall lots on County Line Road or the outlet lots in Pearl give the driver level ground. Say whether the car rolls, steers, and brakes.",
 "Yes. We book a truck with a winch and price the loading time up front. The mall lots on County Line Road or the outlet lots in Pearl give the driver level ground. Does it roll, steer, and brake? Tell us which."),
])

fix('build_jackson_local.py', [
("Every step is on the %s page, and the %s page lists what to do before pickup."%(HIW,PREP),
 "Every step is on the %s page. The %s page lists what to do before pickup."%(HIW,PREP)),
])

# ---------------- Omaha
fix('build_omaha_local.py', [
("Approve the price, and the car is booked with a carrier already running 80 through the city. The lot and the window are settled the same day. The pickup inspection puts every existing mark on the Bill of Lading, and both of you sign it. Delivery is compared to that record.",
 "Approve the price, and we put the car on a carrier already running 80 through the city. The lot and the window are set before you hang up. The driver walks the car with you and marks every blemish on the Bill of Lading. The delivery inspection is checked against those marks."),
('  "Nothing personal left in the cabin or the trunk",\n  "Fuel at about a quarter tank",\n  "Every side and the odometer photographed before the handoff",\n  "One working key handed to the driver, with any fault named",\n  "Aftermarket alarm shut off",\n  "In the Old Market, Dundee, or South Omaha, meet the truck at a lot",',
 '  "Belongings out of the car, including the trunk",\n  "Fuel down to a quarter tank or so",\n  "Snap each side and the mileage before the driver comes",\n  "A key the driver can use, plus a heads-up on any quirks",\n  "Any add-on alarm switched off",\n  "In the Old Market, Dundee, or South Omaha, plan on a lot",'),
("The %s and %s pages go through each step."%(HIW,PREP), "Read the %s page for the sequence and the %s page for the checklist."%(HIW,PREP)),
("Ship Guy’s FMCSA license and $75,000 bond can be checked on the federal register by anyone. Our office is on Howard Street downtown.",
 "The federal register shows our FMCSA license and our $75,000 bond to anyone who looks. The office is on Howard Street downtown."),
("One coordinator sees the move through from the first call to the last signature. The %s page lays out open, enclosed, and expedited transport."%SVC,
 "One person at Ship Guy owns your move from quote to delivery. The %s page sets open, enclosed, and expedited side by side."%SVC),
("A commuter car or a student car rides open without a worry. The difference is spelled out on the %s and %s pages."%(OPEN,ENC),
 "A commuter car or a student car belongs on the open trailer. The %s and %s pages lay out the difference."%(OPEN,ENC)),
("Yes. The campuses take cars in each August and send them home in May. A parent sets up the booking, and someone over eighteen signs at a lot. Campus streets are tight that week. The handoff happens at the lots on Dodge or by the ballpark. The window moves with the date.",
 "Yes. The campuses fill with cars each August and empty each May. Mom or Dad books, and an adult at the lot signs the paperwork. Campus streets are packed that week. The truck meets you at a lot on Dodge or by the ballpark. The window tracks the date."),
("A parent sets up the booking, and someone over eighteen signs at a lot.","Mom or Dad books, and an adult at the lot signs the paperwork."),
("Orders usually cover one vehicle, so the second one ships privately. Ship Guy is a private broker with no connection to the Air Force. PCS timing is on our %s page."%MILC,
 "The government pays to move one car, and the family ships the second one with us. Ship Guy is a private broker with no connection to the Air Force. How orders change the timing is on our %s page."%MILC),
("Orders usually cover one vehicle, and the second one ships privately. Ship Guy is a private broker with no connection to the Air Force.",
 "The government pays to move one car, and the family ships the second one with us. Ship Guy is a private broker and has no connection to the Air Force."),
("Employer-reimbursed moves get their documentation from us.","The documentation for an employer-paid move is ours to provide.",2),
("Both addresses, with the side of 72nd Street or the suburb. Year, make, and model. Running or not. Open or enclosed. The week around the report date or the start date. Five answers, and the Omaha number is back within the day.",
 "Both ends of the trip, with the side of 72nd Street. The year, make, and model. Whether it drives. Open or enclosed. Your week. Five answers put an Omaha price in front of you the same day."),
("Two minutes on the form above gets your lane a number. Tell us the neighborhood and the week, and a carrier already on 80 takes it.",
 "Two minutes on the form above and we price your lane. Give us the neighborhood and the week, and a truck already on 80 takes the car."),
("A move timed to a PCS report date or the August move-in ships with the busiest weeks. The %s covers vehicle size, condition, and the rest."%COST,
 "A report date at the base or an August move-in means the busiest weeks of the year. The %s walks through size, condition, and the other factors."%COST),
("The interstate side is on the %s page."%STS, "Crossing a state line is covered on the %s page."%STS),
("Yes. A winch-equipped carrier is sent, and the extra loading time is priced in from the start. The outlet lots in Gretna or the mall lots at 144th and Center give the driver level ground. Say whether the car rolls, steers, and brakes.",
 "Yes. A carrier with a winch takes it, and the loading time is part of the quote. The outlet lots in Gretna or the mall lots at 144th and Center give the driver level ground. Let us know if it rolls, steers, and brakes."),
])

# ---------------- Newark
fix('build_newark_local.py', [
("Say yes to the number, and we book a carrier already running the Turnpike past the airport. The lot and the window are fixed the same day. At pickup you and the driver list every existing mark on the Bill of Lading. Both signatures go on it, and delivery is compared to it.",
 "Say yes to the number, and a carrier already running the Turnpike past the airport takes the job. Lot and window are locked in the same afternoon. The driver photographs the car and writes its condition on the Bill of Lading, and you initial it. The delivery inspection is held to that sheet."),
('  "Cabin and trunk emptied of personal items",\n  "About a quarter tank of fuel",\n  "Photos of every side and the odometer before the truck arrives",\n  "A working key for the driver, with any fault named",\n  "Aftermarket alarm turned off",\n  "In the Ironbound, downtown, or the wards, meet the truck at a lot",',
 '  "Everything personal out of the car, trunk included",\n  "Gas gauge near a quarter",\n  "Photograph the car and the odometer yourself before the driver arrives",\n  "One good key, and tell the driver about any known faults",\n  "Turn off any alarm that was added after the factory",\n  "In the Ironbound, downtown, or the wards, plan on a lot",'),
("Each step is covered on the %s and %s pages."%(HIW,PREP), "Step by step detail is on the %s page, and the pickup checklist is on the %s page."%(HIW,PREP)),
("Our FMCSA license and $75,000 bond are public on the federal register. Our office is on Broad Street downtown.",
 "Pull our FMCSA license and $75,000 bond on the federal register any time. The office is on Broad Street downtown."),
("Your coordinator follows the move from the first call to the last signature. The %s page explains open, enclosed, and expedited transport."%SVC,
 "The same coordinator answers from the first call to the delivery call. Open, enclosed, and expedited options are side by side on the %s page."%SVC),
("A commuter car or a student car does fine in the open. The choice is spelled out on the %s and %s pages."%(OPEN,ENC),
 "A daily driver or a student car rides open without a second thought. Read the %s and %s pages to decide."%(OPEN,ENC)),
("Yes. The campuses in University Heights take cars each September and send them home in May. A parent sets up the booking, and someone over eighteen signs at a campus lot. Move-in week clogs the Heights, so the handoff happens at the river lots. The window moves with the date.",
 "Yes. University Heights fills with student cars each September and empties in May. The booking comes from a parent, and an adult signs at the campus lot. Move-in week clogs the Heights, so the truck meets you at the river lots. Give us the date and the window follows."),
("A parent sets up the booking, and someone over eighteen signs at a campus lot.","The booking comes from a parent, and an adult signs at the campus lot."),
("We produce the paperwork a reimbursed move needs.","A reimbursed move gets its receipts and its invoice from us.",2),
("Orders timing is on the %s page, and the interstate side is on the %s page."%(MIL,STS),
 "Moves on orders are explained on the %s page, and interstate moves on the %s page."%(MIL,STS)),
("The two addresses, with the ward or the town. Year, make, and model. Does it run. Open or enclosed. The week around the closing or the move-in. Five answers, and the Newark number comes back within the day.",
 "Start and finish addresses, with the ward or the town. The year, make, and model. Whether it drives. Open or enclosed. Your week. Give us those five and the Newark price is back before the day ends."),
("The form above gives your lane a number in two minutes. Name the ward and the week, and a carrier already on the Turnpike takes it.",
 "Your lane gets a price two minutes after you finish the form above. Name the ward and the week, and a Turnpike carrier does the rest."),
("A move timed to the September move-in or a January start date ships with the busiest weeks. The %s covers vehicle size, condition, and the rest."%COST,
 "September move-ins and January start dates ship in the busiest weeks. How size, condition, and season move the number is in the %s."%COST),
("Yes. A carrier with a winch is booked, and the loading time is built into the quote. The outlet lots in Elizabeth or the park lots in the North Ward give the driver level ground. Say whether the car rolls, steers, and brakes.",
 "Yes. A winch carrier is booked, with the loading time already in the price. The outlet lots in Elizabeth or the park lots in the North Ward give the driver level ground. We need to know whether it rolls, steers, and brakes."),
])

# ---------------- Las Cruces
fix('build_lascruces_local.py', [
("Approve the price, and the car is booked with a carrier already running 10 through the valley. The lot and the window are settled the same day. At pickup the driver and you inspect the car together. The Bill of Lading records every existing mark. Both of you sign. Delivery is compared to that record.",
 "Approve the price, and the car goes on a carrier already running 10 through the valley. Lot and window are settled before the day ends. At pickup you go over the car with the driver. Every mark goes on the Bill of Lading. You countersign it, and delivery is judged against it."),
('  "Personal items out of the cabin and the trunk",\n  "Roughly a quarter tank of fuel",\n  "Each side and the odometer photographed before the truck comes",\n  "One working key for the driver, with any fault named",\n  "Any aftermarket alarm disabled",\n  "In Mesilla, the Mesquite district, or downtown, meet the truck at a lot",',
 '  "Empty the car of anything that is yours",\n  "Run the tank down to about a quarter",\n  "Photos of the car and the odometer, taken the day of pickup",\n  "A key the driver can use, and a note of anything that does not work",\n  "Aftermarket alarm off",\n  "In Mesilla, the Mesquite district, or downtown, plan on a lot",'),
("The %s and %s pages go through each step."%(HIW,PREP), "The full sequence is on the %s page. The pickup checklist is on the %s page."%(HIW,PREP)),
("Ship Guy’s FMCSA license and $75,000 bond are listed on the federal register. Anyone can look them up. Our office is on Roadrunner Parkway on the East Mesa.",
 "Check the federal register and you will see Ship Guy’s FMCSA license and $75,000 bond. The office is on Roadrunner Parkway on the East Mesa."),
("One coordinator stays with the move from the first call to the last signature. The %s page lays out open, enclosed, and expedited transport."%SVC,
 "The coordinator who prices the move is the one who tracks the truck. See open, enclosed, and expedited compared on the %s page."%SVC),
("A commuter car or a student car is fine in the open. The difference is spelled out on the %s and %s pages."%(OPEN,ENC),
 "A commuter car or a student car is an open-trailer car. The %s and %s pages explain where the line falls."%(OPEN,ENC)),
("Yes. The campus takes cars in each August and sends them home in May. A parent sets up the booking, and someone over eighteen signs at a campus lot. Move-in week clogs University Avenue, so the handoff happens at the arena lots. The window moves with the date.",
 "Yes. Student cars arrive each August and go home each May. A parent sets it up, and any adult can meet the truck and sign. Move-in week clogs University Avenue, so the truck meets you at the arena lots. The window is built around the date."),
("A parent sets up the booking, and someone over eighteen signs at a campus lot. The community college shares the calendar.",
 "A parent sets it up, and any adult can meet the truck and sign. The community college shares the calendar."),
("Orders usually cover one vehicle, so the second one ships privately. Fort Bliss in El Paso and the air base in Alamogordo send families here too. Ship Guy is a private broker with no connection to any of them. PCS timing is on our %s page."%MILC,
 "Orders pay for one car, so families bring the second one to us. Fort Bliss in El Paso and the air base in Alamogordo send families here too. Ship Guy is a private broker with no connection to any of them. Timing around orders is explained on our %s page."%MILC),
("Orders usually cover one vehicle, and the second one ships privately. Ship Guy is a private broker with no connection to the Army.",
 "Orders pay for one car, and the second one comes to us. Ship Guy is a private broker and has no connection to the Army."),
("Employer-reimbursed moves get their documentation from us.","Employer reimbursement? We send the documents the HR package asks for."),
("The interstate side is on the %s page."%STS, "The %s page explains the interstate side."%STS),
("Both addresses, with the side of the river or the town. Year, make, and model. Running or not. Open or enclosed. The week around the report date or the move-in. Five answers, and the Las Cruces number is back within the day.",
 "The two ends of the trip, with the side of the river. The year, make, and model. Whether it drives. Open or enclosed. The week that works. Five answers and the Las Cruces price lands in your inbox that day."),
("Two minutes on the form above gets your lane a number. Tell us the neighborhood and the week, and a carrier already on 10 takes it.",
 "Fill in the form above and a price follows in about two minutes. Name the neighborhood and the week, and a truck already on 10 carries it."),
("A move timed to the August move-in or a range start date ships with the busiest weeks. The %s covers vehicle size, condition, and the rest."%COST,
 "An August move-in or a start date at the range falls in the busiest weeks. The %s explains what size, condition, and timing do to the price."%COST),
("Yes. We assign a winch truck, and the loading time is in the quote from the start. The mall lots on Telshor or the Lohman and Walton lots give the driver level ground. Say whether the car rolls, steers, and brakes.",
 "Yes. A winch truck handles it, and the loading time is priced from the start. The mall lots on Telshor or the Lohman and Walton lots give the driver level ground. Rolls, steers, brakes: tell us which of those it does."),
])

APPLIED_WARWICK_PASS1 = """
Basics paragraph, ULI items, how-it-works line, FMCSA line, coordinator line, open/enclosed line, campus body + FAQ,
military/state-to-state sentence, 'what do you need' FAQ, Boston lane sentence, winter storm paragraph, CTA sub, cost-guide lead sentence.
"""

fix('build_newark_local.py', [
("Step by step detail is on the %s page, and the pickup checklist is on the %s page."%(HIW,PREP),
 "Step by step detail is on the %s page. The pickup checklist is on the %s page."%(HIW,PREP)),
])

# fact/phrasing follow-up: Manhattan is the lowest lane in the Newark table, so the FAQ compares only the three named; "ten hundred" -> "one thousand"
fix('build_newark_local.py', [
("Orlando runs seven hundred sixty to ten hundred eighty dollars for a sedan. That is about ten hundred sixty miles down 95.",
 "Orlando runs seven hundred sixty to one thousand eighty dollars for a sedan. That is about one thousand sixty miles down 95."),
("Philadelphia is ninety minutes down the Turnpike and costs the least.","Philadelphia is ninety minutes down the Turnpike and costs far less than either."),
])
