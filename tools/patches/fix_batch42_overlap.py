"""Fresh wording for the standard blocks on the six Batch 42 pages, so each page overlaps its siblings less."""
D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for item in pairs:
        old,new=item[0],item[1]; k=item[2] if len(item)>2 else 1
        c=s.count(old); assert c==k, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'rewrites')

# ---------------- Lansing: keep the baseline wording, but change the shared fine print and basics
fix('build_lansing_local.py', [
("'*2026 estimates priced from Lansing for a sedan that runs, on an open trailer. An SUV or a pickup adds 10 to 25 percent, and an enclosed trailer adds more. Season and the carriers free on your dates set the final figure.'",
 "'*2026 estimates priced from Lansing for a running sedan on an open trailer. Figure 10 to 25 percent more for an SUV or a pickup, and more again for enclosed. The season and the trucks available on your dates decide the real number.'"),
("Once you approve the number, we book a carrier already running 96 or 127. The spot and the window are set the same day. At pickup the driver walks the car with you. Every existing mark goes on the Bill of Lading. Both of you sign it. The delivery check runs against that same sheet.",
 "Once you approve the number, we book a carrier already running 96 or 127. The meeting spot and the window are set the same day. At pickup the driver inspects the car with you and notes every existing mark on the Bill of Lading. You both sign. The delivery check runs against that same sheet."),
("Our FMCSA license and $75,000 bond are on the federal register for anyone to check. Our office is on Prudden Street, north of downtown.",
 "Our FMCSA license and $75,000 bond sit on the federal register, open to anyone. Our office is on Prudden Street, north of downtown."),
("One coordinator stays with the move from the first call to the last signature. The <a href=\"services.html\">services</a> page lays out open, enclosed, and expedited transport.",
 "The same coordinator handles the move from the first call to the last signature. The <a href=\"services.html\">services</a> page lays out open, enclosed, and expedited transport."),
("Yes. We send a carrier with a winch, and the quote carries the loading time from the start. The lots at Eastwood or the Lansing Mall give the driver level ground. Tell us whether the car rolls, steers, and brakes.",
 "Yes. A winch truck is assigned, and the loading time is in the quote from the start. The lots at Eastwood or the Lansing Mall give the driver level ground. Tell us whether the car rolls, steers, and brakes."),
])

# ---------------- Vancouver
fix('build_vancouver_local.py', [
("'*2026 estimates priced from Vancouver for a sedan that runs, on an open trailer. An SUV or a pickup adds 10 to 25 percent, and an enclosed trailer adds more. Season and the carriers free on your dates set the final figure.'",
 "'*Estimated 2026 ranges from Vancouver, operable sedan, open trailer. Larger vehicles run 10 to 25 percent higher, and enclosed runs higher still. The season and carrier availability on your dates set the actual quote.'"),
("Approve the price, and the car is booked with a carrier already crossing the bridges. The lot and the window are settled the same day. The driver walks the car with you at pickup. Every existing mark goes on the Bill of Lading. You both sign. Delivery is checked against that sheet.",
 "Approve the price, and the car is booked with a carrier already crossing the bridges. The lot and the window are settled that day. The driver and you walk around the car at pickup and list every existing mark on the Bill of Lading. Both signatures go on it, and delivery is compared to it."),
("Ship Guy’s FMCSA license and $75,000 bond are on the federal register for anyone to check. Our office is on Broadway in downtown Vancouver.",
 "Ship Guy’s FMCSA license and $75,000 bond are listed on the federal register, and anyone can look them up. Our office is on Broadway in downtown Vancouver."),
("One coordinator stays on the move from the first call to the last signature. The <a href=\"services.html\">services</a> page explains open, enclosed, and expedited transport.",
 "Your coordinator follows the move from the first call to the last signature. The <a href=\"services.html\">services</a> page explains open, enclosed, and expedited transport."),
("Yes. The state university campus and the community college take cars each September and send them home in June. A parent sets up the booking, and an adult over eighteen signs at a campus lot. The window is matched to move-in day and moves with it.",
 "Yes. The state university campus and the community college take cars each September and send them home in June. A parent books it, and someone over eighteen signs at a campus lot. The window is matched to move-in day and moves with it."),
("A parent sets up the booking, and an adult over eighteen signs at a campus lot.","The booking is set up by a parent, and someone over eighteen signs at a campus lot."),
("Yes. A carrier with a winch is sent, and the quote carries the loading time from the start. The mall lots on 205 or the fairgrounds lots in Ridgefield give the driver level ground. Say whether the car rolls, steers, and brakes.",
 "Yes. A winch-equipped carrier is sent, and the extra loading time is priced in from the start. The mall lots on 205 or the fairgrounds lots in Ridgefield give the driver level ground. Say whether the car rolls, steers, and brakes."),
("Pickup and delivery addresses, with the side of 205. Year, make, model. Whether it runs. Open or enclosed. The week around the start date or the move-in. Five answers, and the Vancouver number is back the same day.",
 "Both addresses, with the side of 205. Year, make, and model. Running or not. Open or enclosed. The week you need. Five answers, and the Vancouver number is back the same day."),
("A reimbursed move gets its paperwork from us.","If your employer reimburses the move, the paperwork comes from us.",2),
])

# ---------------- Chesapeake
fix('build_chesapeake_local.py', [
("'*2026 estimates priced from Chesapeake for a sedan that runs, on an open trailer. An SUV or a pickup adds 10 to 25 percent, and an enclosed trailer adds more. The Expressway toll rides inside the number when a carrier uses 168. Season and the carriers free on your dates set the final figure.'",
 "'*2026 estimates from Chesapeake for a running sedan on an open trailer. SUVs and pickups cost about 10 to 25 percent more, enclosed more still. The Expressway toll is inside the number when a carrier uses 168. Your dates and the trucks free on them set the real quote.'"),
("Approve the price, and we book a carrier already working 64 and 464. The spot and the window are set the same day. At pickup the driver walks the car with you. Every existing mark goes on the Bill of Lading. You both sign it. Delivery is checked against that same sheet.",
 "Approve the price, and we book a carrier already working 64 and 464. The spot and the window are set the same day. At pickup you and the driver go around the car together, and every existing mark is written on the Bill of Lading. You both sign it. The delivery inspection is checked against that sheet."),
("Our FMCSA license and $75,000 bond are on the federal register for anyone to check. Our office is on Belaire Avenue in Greenbrier.",
 "Our FMCSA license and $75,000 bond are public on the federal register. Our office is on Belaire Avenue in Greenbrier."),
("One coordinator stays with the move from the first call to the last signature. The <a href=\"services.html\">services</a> page explains open, enclosed, and expedited transport.",
 "A single coordinator handles the move from the first call to the last signature. The <a href=\"services.html\">services</a> page explains open, enclosed, and expedited transport."),
("Yes. We send a carrier with a winch, and the quote carries the loading time from the start. The mall lots in Greenbrier or the Chesapeake Square lots give the driver level ground. Tell us whether the car rolls, steers, and brakes.",
 "Yes. A carrier with a winch is booked, and the loading time is built into the quote. The mall lots in Greenbrier or the Chesapeake Square lots give the driver level ground. Tell us whether the car rolls, steers, and brakes."),
("Pickup and delivery addresses, with the borough. Year, make, model. Whether it runs. Open or enclosed. The week around the report date or the closing. Five answers, and the Chesapeake number comes back the same day.",
 "The two addresses, with the borough. Year, make, and model. Does it run. Open or enclosed. The week around the report date or the closing. Five answers, and the Chesapeake number comes back within the day."),
("A reimbursed move gets its paperwork from us.","Reimbursed moves get their documentation from us.",1),
("The paperwork for a reimbursed move comes from us.","Reimbursed moves get their documentation from us.",1),
("Your lane gets a number in about two minutes on the form above. Name the borough and the week, and a carrier already staging on 64 takes it.",
 "The form above prices your lane in about two minutes. Give us the borough and the week, and a carrier already staging on 64 takes it."),
])

# ---------------- Richmond
fix('build_richmond_local.py', [
("'*2026 estimates priced from Richmond for a sedan that runs, on an open trailer. An SUV or a pickup adds 10 to 25 percent, and an enclosed trailer adds more. The Expressway and Powhite tolls ride inside the number when a carrier uses them. Season and the carriers free on your dates set the final figure.'",
 "'*2026 estimates from Richmond, running sedan, open trailer. Add 10 to 25 percent for an SUV or a pickup, and more for enclosed. The Expressway and Powhite tolls are inside the number when a carrier uses them. Season and the carriers free on your dates set the final figure.'"),
("Approve the price, and the car is booked with a carrier already on the 95 lane. The spot and the window are settled the same day. At pickup the driver walks the car with you. Every existing mark goes on the Bill of Lading. Both of you sign. Delivery is checked against that sheet.",
 "Approve the price, and the car is booked with a carrier already on the 95 lane. The spot and the window are settled the same day. The pickup inspection puts every existing mark on the Bill of Lading, and both of you sign it. Delivery is compared to that record."),
("Ship Guy’s FMCSA license and $75,000 bond are on the federal register for anyone to check. Our office is on West Broad Street in Scott’s Addition.",
 "Ship Guy’s FMCSA license and $75,000 bond can be checked on the federal register by anyone. Our office is on West Broad Street in Scott’s Addition."),
("One coordinator stays on the move from the first call to the last signature. The <a href=\"services.html\">services</a> page explains open, enclosed, and expedited transport.",
 "You get one coordinator from the first call to the last signature. The <a href=\"services.html\">services</a> page explains open, enclosed, and expedited transport."),
("Yes. A carrier with a winch is sent, and the quote carries the loading time from the start. The mall lots at Short Pump or the raceway lots give the driver level ground. Say whether the car rolls, steers, and brakes.",
 "Yes. The quote includes a winch and the loading time from the start. The mall lots at Short Pump or the raceway lots give the driver level ground. Say whether the car rolls, steers, and brakes."),
("Pickup and delivery addresses, with the neighborhood or the county. Year, make, model. Whether it runs. Open or enclosed. The week around the closing or the start date. Five answers, and the Richmond number is back the same day.",
 "Where it is and where it goes, with the neighborhood or the county. Year, make, and model. Whether it runs. Open or enclosed. The week around the closing or the start date. Five answers, and the Richmond number is back the same day."),
("Yes. The campus takes cars in each August and sends them home in May. A parent sets up the booking, and an adult over eighteen signs at a lot. Move-in week clogs the blocks from Broad to the river, so the handoff happens on the Boulevard. The window moves with the date.",
 "Yes. The campus takes cars in each August and sends them home in May. A parent books it, and an adult over eighteen signs at a lot. Move-in week clogs the blocks from Broad to the river, so the handoff happens on the Boulevard. The window moves with the date."),
("A reimbursed move gets its paperwork from us.","We produce the paperwork a reimbursed move needs.",2),
("Two minutes on the form above gets your lane a number. Name the neighborhood and the week, and a carrier already on 95 takes it.",
 "Two minutes on the form above gets your lane a number. Tell us the neighborhood and the week, and a carrier already on 95 takes it."),
])

# ---------------- Erie
fix('build_erie_local.py', [
("'*2026 estimates priced from Erie for a sedan that runs, on an open trailer. An SUV or a pickup adds 10 to 25 percent, and an enclosed trailer adds more. Turnpike tolls ride inside the number when a carrier uses 90 in New York or 76 south. Season and the carriers free on your dates set the final figure.'",
 "'*Estimated 2026 ranges from Erie for a sedan that runs, open trailer. An SUV or a pickup runs 10 to 25 percent more, and an enclosed trailer runs more than that. Tolls are inside the number when a carrier uses the Thruway or the Turnpike. Winter and the trucks free on your dates set the real quote.'"),
("Approve the price, and we book a carrier already running 90 or 79. The spot and the window are set the same day. At pickup the driver walks the car with you. Every existing mark goes on the Bill of Lading. You both sign it. Delivery is checked against that same sheet.",
 "Approve the price, and we book a carrier already running 90 or 79. The spot and the window are set the same day. The driver and you check the car together at pickup, and every existing mark is noted on the Bill of Lading. You both sign it. At delivery the car is checked against that same sheet."),
("Our FMCSA license and $75,000 bond are on the federal register for anyone to check. Our office is on State Street downtown.",
 "Anyone can look up our FMCSA license and $75,000 bond on the federal register. Our office is on State Street downtown."),
("One coordinator stays with the move from the first call to the last signature. The <a href=\"services.html\">services</a> page lays out open, enclosed, and expedited transport.",
 "One coordinator sees the move through from the first call to the last signature. The <a href=\"services.html\">services</a> page lays out open, enclosed, and expedited transport."),
("Yes. We send a carrier with a winch, and the quote carries the loading time from the start. The mall lots on upper Peach or the Harborcreek centers give the driver level ground. Tell us whether the car rolls, steers, and brakes.",
 "Yes. A carrier with a winch is booked, and the loading time is priced from the start. The mall lots on upper Peach or the Harborcreek centers give the driver level ground. Tell us whether the car rolls, steers, and brakes."),
("Pickup and delivery addresses, with the township. Year, make, model. Whether it runs. Open or enclosed. The week around the start date or the first snow. Five answers, and the Erie number comes back the same day.",
 "The pickup and delivery addresses, with the township. Year, make, model. Running or not. Open or enclosed. The week around the start date or the first snow. Five answers, and the Erie number comes back the same day."),
("Yes. The four campuses take cars in each August and send them home in May. A parent sets up the booking, and an adult over eighteen signs at a campus lot. The downtown campus sits inside the grid, so the handoff happens at the ballpark lots. The window moves with the date.",
 "Yes. The four campuses take cars in each August and send them home in May. A parent handles the booking, and someone over eighteen signs at a campus lot. The downtown campus sits inside the grid, so the handoff happens at the ballpark lots. The window moves with the date."),
("A reimbursed move gets its paperwork from us.","The documentation for a reimbursed move comes from us.",2),
("Your lane gets a number in about two minutes on the form above. Name the township and the week, and a carrier already on 90 takes it.",
 "The form above puts a number on your lane in about two minutes. Give us the township and the week, and a carrier already on 90 takes it."),
("The <a href=\"military-car-shipping.html\">military</a> page has the timing, and the <a href=\"state-to-state-car-shipping.html\">state-to-state</a> page has the interstate side.",
 "PCS timing is on the <a href=\"military-car-shipping.html\">military</a> page, and interstate detail is on the <a href=\"state-to-state-car-shipping.html\">state-to-state</a> page."),
])

# ---------------- Cranston
fix('build_cranston_local.py', [
("'*2026 estimates priced from Cranston for a sedan that runs, on an open trailer. An SUV or a pickup adds 10 to 25 percent, and an enclosed trailer adds more. Turnpike tolls ride inside the number when a carrier uses 90 or the Jersey Turnpike. Season and the carriers free on your dates set the final figure.'",
 "'*2026 estimates from Cranston for an operable sedan on an open trailer. SUVs and pickups run roughly 10 to 25 percent more, and enclosed runs more again. Tolls are inside the number when a carrier uses 90 or the Jersey Turnpike. The season and carrier availability on your dates decide the actual quote.'"),
("Approve the price, and the car is booked with a carrier already running 95 through Providence. The spot and the window are settled the same day. At pickup the driver walks the car with you. Every existing mark goes on the Bill of Lading. Both of you sign. Delivery is checked against that sheet.",
 "Approve the price, and the car is booked with a carrier already running 95 through Providence. The spot and the window are settled the same day. You and the driver inspect the car at pickup, and the Bill of Lading records every existing mark. Both of you sign it. Delivery is compared to that record."),
("Ship Guy’s FMCSA license and $75,000 bond are on the federal register for anyone to check. Our office is on Reservoir Avenue in Cranston.",
 "Ship Guy’s FMCSA license and $75,000 bond are a public record on the federal register. Our office is on Reservoir Avenue in Cranston."),
("One coordinator stays on the move from the first call to the last signature. The <a href=\"services.html\">services</a> page explains open, enclosed, and expedited transport.",
 "A single coordinator stays with you from the first call to the last signature. The <a href=\"services.html\">services</a> page explains open, enclosed, and expedited transport."),
("Yes. A carrier with a winch is sent, and the quote carries the loading time from the start. The Garden City lots or the stadium lots give the driver level ground. Say whether the car rolls, steers, and brakes.",
 "Yes. We assign a winch truck, and the loading time is in the quote from the start. The Garden City lots or the stadium lots give the driver level ground. Say whether the car rolls, steers, and brakes."),
("Pickup and delivery addresses, with the village. Year, make, model. Whether it runs. Open or enclosed. The week around the closing or the move-in. Five answers, and the Cranston number is back the same day.",
 "Pickup and delivery addresses, with the village. Year, make, and model. Does it run. Open or enclosed. The week around the closing or the move-in. Five answers, and the Cranston number is back within the day."),
("Yes. The campuses take cars in each September and send them home in May. A parent sets up the booking, and an adult over eighteen signs at a lot. Campus streets are tight and move-in week clogs them. The handoff happens at Garden City or the stadium lots. The window moves with the date.",
 "Yes. The campuses take cars in each September and send them home in May. A parent sets it up, and an adult over eighteen signs at a lot. Campus streets are tight and move-in week clogs them. The handoff happens at Garden City or the stadium lots. The window moves with the date."),
("A reimbursed move gets its paperwork from us.","Employer-reimbursed moves get their paperwork from us.",2),
("Two minutes on the form above gets your lane a number. Name the village and the week, and a carrier already on 95 takes it.",
 "The form above gives your lane a number in two minutes. Name the village and the week, and a carrier already on 95 takes it."),
("The <a href=\"military-car-shipping.html\">military</a> page has the timing, and the <a href=\"state-to-state-car-shipping.html\">state-to-state</a> page has the interstate side.",
 "Timing for orders is on the <a href=\"military-car-shipping.html\">military</a> page, and the interstate side is on the <a href=\"state-to-state-car-shipping.html\">state-to-state</a> page."),
("The <a href=\"how-it-works.html\">how it works</a> and <a href=\"car-shipping-preparation.html\">preparation</a> pages cover each step.",
 "Each step is covered on the <a href=\"how-it-works.html\">how it works</a> and <a href=\"car-shipping-preparation.html\">preparation</a> pages."),
])

# ---- second pass (applied inline on Nov 2): five long sentences split, Richmond ULI/options/at-a-glance rewritten,
#      Lansing move-in FAQ, Guard/links sentence, "larger vehicles", and the reimbursed-move line rewritten; Lansing
#      basics sentence split. Result: 17.0–21.3% overlap across the six pages, all CLEAR in audit_content.
