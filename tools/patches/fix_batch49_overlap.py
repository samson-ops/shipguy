"""Batch 49 fresh-wording pass: the standard blocks (intro bond line, glance lead, rate intro and footnote, cost-guide
line, military/state-to-state lines, NOTE, options, basics + checklist, why, and the cost/move-in/employer/non-running/
storm/quote FAQs plus the CTA) the five pages written together shared with each other and with earlier batches are
reworded per page. Salem gets a smaller pass."""
D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    if pairs and all(s.count(o[0])==0 for o in pairs): print(fn,'already applied'); return
    for item in pairs:
        old,new=item[0],item[1]; k=item[2] if len(item)>2 else 1
        c=s.count(old); assert c==k, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'rewrites')

OP='<a href="open-car-transport.html">open</a>'; EN='<a href="enclosed-auto-transport.html">enclosed</a>'
HW='<a href="how-it-works.html">how it works</a>'; PR='<a href="car-shipping-preparation.html">preparation</a>'; SV='<a href="services.html">services</a>'
CG='<a href="car-shipping-cost.html">cost guide</a>'; MI='<a href="military-car-shipping.html">military</a>'; SS='<a href="state-to-state-car-shipping.html">state-to-state</a>'
HWLINE='See the %s page for the order of events and the %s page for pickup day.'%(HW,PR)
WHY2='One person at Ship Guy owns your move from the quote to the delivery call. The %s page explains open, enclosed, and expedited.'%SV
SSLINE='The %s page covers the paperwork for crossing a state line.'%SS
MILINE='The %s page explains how orders set the timing.'%MI
OPEN3='The %s and %s pages set the two beside each other.'%(OP,EN)

fix('build_minneapolis_local.py', [
('The carriers own the trucks. Ship Guy holds the license and the bond.','The trucks belong to the carriers, and the license and the bond belong to us.'),
('Most pickups happen within 1 to 3 days. The Twin Cities pool','A Minneapolis pickup usually lands within 1 to 3 days. The Twin Cities pool'),
('The lanes Hennepin County cars run most, with estimated open-trailer ranges. Price your own route on the form above.','The ten lanes Hennepin County cars ride most often, with open-trailer estimates. Your own lane prices on the form above.'),
('*2026 estimates from Minneapolis for a sedan that runs, open trailer. Plan on 10 to 25 percent more for an SUV or a pickup, and more again for enclosed. The week you choose and the carriers on 94 that week set the real figure.','*2026 estimates from Minneapolis, running sedan, open trailer. An SUV or a pickup adds 10 to 25 percent, and enclosed adds more. Your week and the carriers on 94 that week decide the final figure.'),
('A start date at a headquarters in January or the late August move-in means a busy week. The %s explains what size, condition, and timing do to the figure.'%CG,'A January start date at a headquarters or the late August move-in means a busy week. What size, condition, and timing each do to the figure is on the %s.'%CG),
('Mom or Dad books, and an adult signs at the lots on University Avenue. The cars leave in May.','A parent books it, and an adult signs at the lots on University Avenue. The cars leave in May.'),
('The handoff happens at the cell lot or outside the gate. Ship Guy is a private broker with no tie to the Guard. '+MILINE,'The handoff happens at the cell lot or outside the gate. Ship Guy is a private company and has no connection to the Guard. How orders drive the timing is on the %s page.'%MI),
(SSLINE,'The paperwork for a state line is on the %s page.'%SS),
('Lowry Hill lane or Edina cul-de-sac. Tell us the neighborhood and whether the car runs.','Lowry Hill lane or Edina cul-de-sac. Give us the neighborhood and say whether the car runs.'),
('Open trailers carry most of the metro, and the table above is priced for one.','The metro ships open nine times in ten, and the table above is priced that way.'),
('A commuter car or a student’s car is fine in the open. '+OPEN3,'A commuter car or a student’s car does fine in the open. The differences are laid out on the %s and %s pages.'%(OP,EN)),
('A figure, a lot on Lake Street, and a signature when the car arrives. The start date or the move-in sets the week.','First a figure, then a lot on Lake Street, then a signature at the other end. Your start date or move-in picks the week.'),
('Say yes to the figure, and a carrier already running 94 that week gets the car. We settle the lot and the window the same afternoon. The driver photographs the car at pickup and writes up its condition on the Bill of Lading. You initial it, and the delivery check works from it.','Approve the figure, and the car goes to a carrier already on 94 that week. The lot and the window get fixed before the day is out. At pickup the driver photographs the car and records its condition on the Bill of Lading. Your initials go on that sheet, and delivery is checked against it.'),
('"Cabin and trunk emptied of personal items"','"Nothing personal left in the cabin or the trunk"'),
('"Fuel at a quarter tank or less"','"No more than a quarter tank of fuel"'),
('"Each side and the odometer photographed before pickup"','"Photos of every side and the odometer the morning of pickup"'),
('"A good key and a note about any known faults"','"A working key plus a note on anything that acts up"'),
('"Add-on alarms turned off"','"Aftermarket alarms disabled"'),
(HWLINE,'The order of events is on the %s page. Pickup day is on the %s page.'%(HW,PR)),
('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on 4th Street downtown.','Our FMCSA license and our $75,000 bond sit on the federal register for anyone to check. The office is on 4th Street downtown.'),
(WHY2,'The same coordinator handles your move from the quote through the delivery call. Open, enclosed, and expedited are compared on the %s page.'%SV),
('Rochester is the lowest lane on the table, ninety minutes down 52. SUVs and pickups run 10 to 25 percent more.','Rochester is the lowest lane on the table, ninety minutes down 52. Add 10 to 25 percent for an SUV or a pickup.'),
('Yes. Cars arrive in late August and leave in May. Mom or Dad books, and someone over eighteen signs at the lot. Dinkytown and the East Bank are full that week. The meeting point is the lots on University Avenue. The date sets the window.','Yes. Cars arrive in late August and leave in May. A parent books, and anyone over eighteen can sign at the lot. Dinkytown and the East Bank are full that week. The meeting point is the lots on University Avenue. The window follows the date.'),
('The handoff happens at a garage entrance or on Hiawatha. If the employer pays you back, we write up what it needs.','The handoff happens at a garage entrance or on Hiawatha. When the employer reimburses the move, we produce the paperwork it asks for.'),
('We call the moment the forecast turns. The pickup moves to the first workable morning at the same figure.','You hear from us the moment the forecast turns. The pickup slides to the first workable morning at the same figure.'),
('Yes. The carrier brings a winch, and the loading time is already in the figure. The big-box lots on Lake Street and the stadium lots are flat. Tell us whether it rolls, steers, and brakes.','Yes. A winch truck comes, and the figure already includes the loading time. The big-box lots on Lake Street and the stadium lots are flat. We need to know whether it rolls, steers, and brakes.'),
('Both addresses with the neighborhood. What it is and whether it runs. Open or enclosed, and the week around the start date or the move. With those, the Minneapolis figure comes back the same day.','Start and end, down to the neighborhood. Year, make, and model, and whether it runs. Open or enclosed, and the week around the start date or the move. With those four, the Minneapolis figure is back the same day.'),
('Two minutes on the form above gets your lane a Minneapolis figure. Name the neighborhood and the week, and a carrier already running 94 takes it.','Two minutes on the form above puts a Minneapolis figure on your lane. Give us the neighborhood and the week, and a carrier already on 94 takes the car.'),
])

fix('build_rapidcity_local.py', [
('The carriers own the trucks. Ship Guy holds the license and the bond.','The carriers run their own trucks. Ship Guy carries the license and the bond.'),
('Most pickups happen within 2 to 5 days. Rapid City sits','Plan on 2 to 5 days for a pickup. Rapid City sits'),
('The lanes Pennington County cars run most, with estimated open-trailer ranges. Price your own route on the form above.','The lanes Pennington County cars take most, each with an open-trailer estimate. The form above prices your own.'),
('*2026 estimates from Rapid City for a sedan that runs, open trailer. Plan on 10 to 25 percent more for an SUV or a pickup, and more again for enclosed. The week you choose and the carriers on 90 that week set the real figure.','*2026 estimates out of Rapid City, sedan that runs, open trailer. Figure 10 to 25 percent more for an SUV or a pickup and a step up again for enclosed. The week and the carriers on 90 that week settle the real number.'),
('A report date at the base or a rally week in August means a busy week. The %s explains what size, condition, and timing do to the figure.'%CG,'A report date at the base or a rally week in August means a busy week. The %s walks through size, condition, and timing.'%CG),
('Orders set the dates, and the handoff happens at the Box Elder lots or outside the gate. Ship Guy is a private broker with no tie to the Air Force. '+MILINE,'Orders set the dates, and the handoff happens at the Box Elder lots or outside the gate. Ship Guy is a private broker, not part of the Air Force. The %s page shows how a report date shapes the window.'%MI),
('Mom or Dad books, and an adult signs at the lots on St. Joseph.','A parent books, and anyone over eighteen signs at the lots on St. Joseph.'),
(SSLINE,'Crossing a state line adds paperwork, and the %s page lists it.'%SS),
('Book three weeks ahead for a date in August.','Give an August date three weeks of notice.'),
('West Boulevard curb or Hill City cabin road. Tell us the neighborhood and whether the car runs.','West Boulevard curb or Hill City cabin road. Name the neighborhood and say whether the car runs.'),
('Open trailers carry most of the Hills, and the table above is priced for one.','Nearly everything out of the Hills rides open, and the table above assumes it does.'),
('A commuter car or an airman’s pickup is fine in the open. '+OPEN3,'A commuter car or an airman’s pickup rides open without trouble. Compare the two on the %s and %s pages.'%(OP,EN)),
('A figure, a lot off 90, and a signature when the car arrives. The orders or the move-in sets the week.','You get a figure, a lot off 90, and a signature at delivery. Orders or the move-in decide the week.'),
('Say yes to the figure, and a carrier already crossing 90 that week gets the car. We settle the lot and the window the same day. The driver photographs the car at pickup and writes up its condition on the Bill of Lading. You initial it, and the delivery check works from it.','Once you accept the figure, a carrier already crossing 90 that week takes the car. The lot and the window are pinned down the same day. The driver walks the car with a camera at pickup and notes its condition on the Bill of Lading. You initial it, and delivery is checked against that sheet.'),
('"Cabin and bed emptied of personal items"','"Personal items cleared from the cabin and the bed"'),
('"Fuel at a quarter tank or less"','"A quarter tank of fuel at most"'),
('"Each side and the odometer photographed before pickup"','"Pictures of all four sides and the odometer before the truck comes"'),
('"A good key and a note about any known faults"','"One good key and a list of anything that does not work"'),
('"Add-on alarms turned off"','"Any add-on alarm switched off"'),
(HWLINE,'Read %s for the steps and %s for the morning of pickup.'%(HW,PR)),
('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on St. Joseph Street downtown.','Our FMCSA license and $75,000 bond are listed on the federal register, where anyone can look them up. The office is on St. Joseph Street downtown.'),
(WHY2,'One coordinator stays with your move from the first figure to the delivery call. The %s page lays out open, enclosed, and expedited.'%SV),
('Cheyenne is the lowest lane on the table, about three hundred ten miles. SUVs and pickups run 10 to 25 percent more.','Cheyenne is the lowest lane on the table, about three hundred ten miles. An SUV or a pickup runs 10 to 25 percent above those figures.'),
('Ship Guy is a private broker with no tie to the Air Force.','Ship Guy is a private broker and not part of the Air Force.'),
('Yes. Students arrive in late August and leave in May. Mom or Dad books, and someone over eighteen signs at the lot. The campus blocks are tight that week. The meeting point is the lots on St. Joseph or the civic center. The date sets the window.','Yes. Students arrive in late August and leave in May. A parent sets it up, and an adult signs at the lot. The campus blocks are tight that week. The meeting point is the lots on St. Joseph or the civic center. The window comes from the date.'),
('Yes. The carrier brings a winch, and the loading time is already in the figure. The mall lots and the big-box lots on LaCrosse are flat. Tell us whether it rolls, steers, and brakes.','Yes. The carrier comes with a winch, and the figure covers the loading time. The mall lots and the big-box lots on LaCrosse are flat. Say whether it rolls, steers, and brakes.'),
('Both addresses with the neighborhood or the Hills town. What it is and whether it runs. Open or enclosed, and the week around the orders or the move. With those, the Rapid City figure comes back the same day.','Pickup and delivery addresses, with the neighborhood or the Hills town. The vehicle, and whether it runs. Open or enclosed, and the week around the orders or the move. Those four lines get a Rapid City figure back the same day.'),
('Two minutes on the form above gets your lane a Rapid City figure. Name the neighborhood and the week, and a carrier already crossing 90 takes it.','Two minutes on the form above and your lane has a Rapid City figure. Tell us the neighborhood and the week, and the next carrier across 90 takes the car.'),
])

fix('build_columbiasc_local.py', [
('The carriers own the trucks. Ship Guy holds the license and the bond.','The trucks are the carriers’ own. The license and the bond are ours.'),
('Most pickups happen within 1 to 3 days. Columbia sits','Pickups usually land within 1 to 3 days. Columbia sits'),
('The lanes Richland County cars run most, with estimated open-trailer ranges. Price your own route on the form above.','Where Richland County cars go most often, with open-trailer ranges for each. Price your own lane on the form above.'),
('*2026 estimates from Columbia for a sedan that runs, open trailer. Plan on 10 to 25 percent more for an SUV or a pickup, and more again for enclosed. The week you choose and the carriers on 26 and 77 that week set the real figure.','*2026 estimates from Columbia, sedan that runs, open trailer. Expect 10 to 25 percent more for an SUV or a pickup, and enclosed above that. The real figure comes from the week you pick and the carriers on 26 and 77 that week.'),
('A PCS report date at the fort or a mid-August move-in means a busy week. The %s explains what size, condition, and timing do to the figure.'%CG,'A PCS report date at the fort or a mid-August move-in means a busy week. Size, condition, and timing are each explained on the %s.'%CG),
('Graduation Thursdays fill the roads around the fort with families. Ship Guy is a private broker with no tie to the Army. '+MILINE,'Graduation Thursdays fill the roads around the fort with families. Ship Guy is a private broker with no connection to the Army. See the %s page for how orders set the window.'%MI),
('Mom or Dad books, and an adult signs at the lots on Assembly or Bluff Road. The cars leave in May.','A parent sets it up, and someone over eighteen signs at the lots on Assembly or Bluff Road. The cars leave in May.'),
('The insurance offices on the Northeast relocate staff from the Midwest. The handoff happens at the lots nearest the office.','The insurance offices on the Northeast relocate staff from the Midwest. The handoff happens in the lot nearest the office.'),
(SSLINE,'What a state line adds is on the %s page.'%SS),
('Shandon curb or Lake Murray cul-de-sac. Tell us the neighborhood and whether the car runs.','Shandon curb or Lake Murray cul-de-sac. Let us know the neighborhood and whether the car runs.'),
('Open trailers carry most of the Midlands, and the table above is priced for one.','The Midlands ship open most of the time, and the table above is figured that way.'),
('A commuter car or a soldier’s pickup is fine in the open. '+OPEN3,'A commuter car or a soldier’s pickup goes open and arrives fine. The %s and %s pages weigh one against the other.'%(OP,EN)),
('A figure, a lot off 77 or 26, and a signature when the car arrives. The orders or the move-in sets the week.','A figure up front, a lot off 77 or 26, and a signature at the far end. Orders or the move-in set the week.'),
('Say yes to the figure, and a carrier already running 77 that week gets the car. We settle the lot and the window that afternoon. The driver photographs the car at pickup and writes up its condition on the Bill of Lading. You initial it, and the delivery check works from it.','Accept the figure, and we place the car with a carrier already running 77 that week. The lot and the window are agreed that afternoon. The driver photographs the car at pickup and enters its condition on the Bill of Lading. You initial the sheet, and it is the reference at delivery.'),
('"Cabin and trunk emptied of personal items"','"Cabin and trunk cleared out"'),
('"Fuel at a quarter tank or less"','"Fuel down to a quarter tank"'),
('"Each side and the odometer photographed before pickup"','"Your own photos of each side and the odometer"'),
('"A good key and a note about any known faults"','"A key that works and a note on known faults"'),
('"Add-on alarms turned off"','"Aftermarket alarms off"'),
(HWLINE,'Every step is on the %s page, and pickup day is on the %s page.'%(HW,PR)),
('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on Pickens Street in the BullStreet District.','Our FMCSA license and our $75,000 bond are on the federal register, open to anyone. The office is on Pickens Street in the BullStreet District.'),
(WHY2,'You get one coordinator from the quote to the delivery call, not a queue. The %s page covers open, enclosed, and expedited.'%SV),
('Augusta is the lowest lane on the table, about seventy-five miles. SUVs and pickups run 10 to 25 percent more.','Augusta is the lowest lane on the table, about seventy-five miles. SUVs and pickups add 10 to 25 percent.'),
('Trainees do not bring cars. Ship Guy is a private broker with no tie to the Army.','Trainees do not bring cars. Ship Guy is a private broker and not part of the Army.'),
('Yes. Cars arrive in mid-August and leave in May. Mom or Dad books, and someone over eighteen signs at the lot. The campus blocks and Five Points are full that week. The meeting point is the lots on Assembly or Bluff Road. The date sets the window.','Yes. Cars arrive in mid-August and leave in May. A parent books, and an adult signs at the lot. The campus blocks and Five Points are full that week. The meeting point is the lots on Assembly or Bluff Road. The date fixes the window.'),
('We call the moment the forecast turns. The pickup moves to the first open morning, and the figure holds.','We call when the forecast turns. The pickup takes the first open morning after, and the figure holds.'),
('The handoff happens at the lots nearest the office. If the employer pays you back, we write up what it needs.','The handoff happens at the lots nearest the office. Employers that reimburse get the paperwork they ask for.'),
('Yes. The carrier brings a winch, and the loading time is already in the figure. The big-box lots on Harbison and Two Notch are flat. Tell us whether it rolls, steers, and brakes.','Yes. A winch truck handles it, and the loading time is built into the figure. The big-box lots on Harbison and Two Notch are flat. We only need to know whether it rolls, steers, and brakes.'),
('Both addresses with the neighborhood. What it is and whether it runs. Open or enclosed, and the week around the orders or the move. With those, the Columbia figure comes back the same day.','The two addresses, with the neighborhood. The year, make, and model, and whether it runs. Open or enclosed, and the week around the orders or the move. Send those, and the Columbia figure is back the same day.'),
('Two minutes on the form above gets your lane a Columbia figure. Name the neighborhood and the week, and a carrier already running 77 takes it.','Two minutes on the form above gets a Columbia figure on your lane. Give the neighborhood and the week, and a carrier already on 77 takes the car.'),
])

fix('build_burlington_local.py', [
('The carriers own the trucks. Ship Guy holds the license and the bond.','The carriers drive their own trucks. The license and the bond are Ship Guy’s.'),
('Most pickups happen within 2 to 5 days. Burlington is','A pickup here usually takes 2 to 5 days. Burlington is'),
('The lanes Chittenden County cars run most, with estimated open-trailer ranges. Price your own route on the form above.','The lanes Chittenden County cars travel most, with an open-trailer estimate for each. Use the form above for your own.'),
('*2026 estimates from Burlington for a sedan that runs, open trailer. Plan on 10 to 25 percent more for an SUV or a pickup, and more again for enclosed. The week you choose and the carriers on 89 that week set the real figure.','*2026 estimates from Burlington for a running sedan, open trailer. Add 10 to 25 percent for an SUV or a pickup, and more for an enclosed trailer. The week you choose and the carriers coming up 89 that week fix the real figure.'),
('A late August move-in at the university or a foliage week in October means a busy week. The %s explains what size, condition, and timing do to the figure.'%CG,'A late August move-in at the university or a foliage week in October means a busy week. For what size, condition, and timing do to a figure, read the %s.'%CG),
('Mom or Dad books, and an adult signs at the lots on Colchester Avenue. The cars leave in May.','A parent books, and an adult signs at the lots on Colchester Avenue. The cars go home in May.'),
('The handoff happens at the airport lots. Ship Guy is a private broker with no tie to the Guard. '+MILINE,'The handoff happens at the airport lots. Ship Guy is a private broker and has nothing to do with the Guard. The %s page covers how orders set the dates.'%MI),
(SSLINE,'The %s page has the paperwork a state line adds.'%SS),
('Book three weeks ahead for a date in late August.','A late August date wants three weeks of notice.'),
('New North End curb or Jericho dirt road. Tell us the neighborhood and whether the car runs.','New North End curb or Jericho dirt road. Tell us the street and whether the car runs.'),
('Open trailers carry most of the valley, and the table above is priced for one.','Open trailers do most of the valley’s work, and the table above assumes one.'),
('A commuter car or a student’s hatchback is fine in the open. '+OPEN3,'A commuter car or a student’s hatchback rides open and arrives fine. The %s and %s pages explain where the two part ways.'%(OP,EN)),
('A figure, a lot off exit 14, and a signature when the car arrives. The move-in or the start date sets the week.','A figure, then a lot off exit 14, then a signature when the car lands. Move-in or the start date decides the week.'),
('Say yes to the figure, and a carrier already coming up 89 that week gets the car. We settle the lot and the window the same day. The driver photographs the car at pickup and writes up its condition on the Bill of Lading. You initial it, and the delivery check works from it.','Say yes, and the car is placed with a carrier already coming up 89 that week. The lot and the window follow the same day. The driver takes photos at pickup and fills in the condition on the Bill of Lading. You initial it, and that record settles delivery.'),
('"Cabin and hatch emptied of personal items"','"Nothing of yours left in the cabin or the hatch"'),
('"Fuel at a quarter tank or less"','"Fuel at a quarter tank, no more"'),
('"Each side and the odometer photographed before pickup"','"Photos of each side and the odometer, taken before the truck comes"'),
('"A good key and a note about any known faults"','"A key that works and a line about any known faults"'),
('"Add-on alarms turned off"','"Add-on alarms disarmed"'),
(HWLINE,'The order of events is on %s, and the morning-of list is on %s.'%(HW,PR)),
('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on North Street in the Old North End.','Our FMCSA license and our $75,000 bond are posted on the federal register for anyone to check. The office is on North Street in the Old North End.'),
(WHY2,'One coordinator takes your move from the quote all the way to the delivery call. Open, enclosed, and expedited are explained on the %s page.'%SV),
('Albany is the lowest lane on the table, about one hundred fifty-five miles. SUVs and pickups run 10 to 25 percent more.','Albany is the lowest lane on the table, about one hundred fifty-five miles. An SUV or a pickup costs 10 to 25 percent more.'),
('Yes. Cars arrive in late August and leave in May. Mom or Dad books, and someone over eighteen signs at the lot. The hill and the student streets are closed that week. The meeting point is the lots on Colchester Avenue. The date sets the window.','Yes. Cars arrive in late August and leave in May. A parent books, and someone over eighteen signs at the lot. The hill and the student streets are closed that week. The meeting point is the lots on Colchester Avenue. The window is built around the date.'),
('We call as soon as the forecast turns, and the pickup moves to the first plowed morning. The figure stays.','Our call goes out as soon as the forecast turns, and the pickup moves to the first plowed morning. The figure stays.'),
('The handoff happens at the lots nearest the site. If the employer pays you back, we write up what it needs.','The handoff happens at the lots nearest the site. When the employer reimburses you, we supply the paperwork it wants.'),
('Yes. The carrier brings a winch, and the loading time is already in the figure. The mall lots on Williston Road and the big-box lots on Shelburne Road are flat. Tell us whether it rolls, steers, and brakes.','Yes. The truck brings a winch, and the figure includes the extra loading time. The mall lots on Williston Road and the big-box lots on Shelburne Road are flat. Let us know whether it rolls, steers, and brakes.'),
('Both addresses with the neighborhood or the town. What it is and whether it runs. Open or enclosed, and the week around the move-in or the start date. With those, the Burlington figure comes back the same day.','Where it starts and where it ends, with the neighborhood or the town. The car, and whether it runs. Open or enclosed, and the week around the move-in or the start date. From those, a Burlington figure comes back the same day.'),
('Two minutes on the form above gets your lane a Burlington figure. Name the neighborhood and the week, and a carrier already coming up 89 takes it.','Two minutes on the form above gets your lane priced for Burlington. Name the street and the week, and a carrier already coming up 89 takes the car.'),
])

fix('build_huntington_local.py', [
('The carriers own the trucks. Ship Guy holds the license and the bond.','The trucks belong to the carriers. The license and the bond are held by Ship Guy.'),
('Most pickups happen within 2 to 4 days. Huntington sits','Count on 2 to 4 days for a pickup. Huntington sits'),
('The lanes Cabell County cars run most, with estimated open-trailer ranges. Price your own route on the form above.','The lanes Cabell County cars run most, each with an open-trailer range. Your own lane gets a figure on the form above.'),
('*2026 estimates from Huntington for a sedan that runs, open trailer. Plan on 10 to 25 percent more for an SUV or a pickup, and more again for enclosed. The week you choose and the carriers on 64 that week set the real figure.','*2026 estimates from Huntington for a sedan that runs on an open trailer. SUVs and pickups come in 10 to 25 percent higher, and enclosed higher than that. The week and the carriers on 64 that week set the actual figure.'),
('A mid-August move-in at the university or a residency start in June means a busy week. The %s explains what size, condition, and timing do to the figure.'%CG,'A mid-August move-in at the university or a residency start in June means a busy week. The %s goes through size, condition, and timing one at a time.'%CG),
('Mom or Dad books, and an adult signs at the lots on 5th Avenue. The cars leave in May.','A parent books, and an adult signs at the lots on 5th Avenue. The cars head home in May.'),
('The refinery across the river in Kentucky and the new steel mill upriver are hiring on start dates. The handoff happens at the lots nearest the site.','The refinery across the river in Kentucky and the new steel mill upriver are hiring on start dates. The handoff happens in the lot closest to the job.'),
('The Guard units in the county rotate people on orders, and the handoff happens at the armory lots. Ship Guy is a private broker with no tie to the Guard. '+MILINE,'The Guard units in the county rotate people on orders, and the handoff happens at the armory lots. Ship Guy is a private broker, unconnected to the Guard. How a set of orders shapes the dates is on the %s page.'%MI),
(SSLINE,'Three states meet here, and the %s page covers the paperwork for crossing a line.'%SS),
('Book three weeks ahead for a date in mid-August or a home Saturday.','Three weeks of notice covers a mid-August date or a home Saturday.'),
('Highlawn curb or Barboursville cul-de-sac. Tell us the neighborhood and whether the car runs.','Highlawn curb or Barboursville cul-de-sac. Say which neighborhood and whether the car runs.'),
('Open trailers carry most of the Tri-State, and the table above is priced for one.','The Tri-State ships open nearly every time, and the table above is built on an open trailer.'),
('A commuter car or a student’s sedan is fine in the open. '+OPEN3,'A commuter car or a student’s sedan is fine open. What separates the two is on the %s and %s pages.'%(OP,EN)),
('A figure, a lot on Route 60, and a signature when the car arrives. The move-in or the start date sets the week.','A figure, a lot on Route 60, and a signature at delivery, in that order. The move-in or the start date picks the week.'),
('Say yes to the figure, and a carrier already running 64 that week gets the car. We settle the lot and the window that day. The driver photographs the car at pickup and writes up its condition on the Bill of Lading. You initial it, and the delivery check works from it.','Approve the figure, and a carrier already on 64 that week is assigned the car. The lot and the window are set that day. The driver photographs the car at pickup and lists its condition on the Bill of Lading. You initial it there, and the same sheet is the check at delivery.'),
('"Cabin and trunk emptied of personal items"','"Everything personal out of the cabin and the trunk"'),
('"Fuel at a quarter tank or less"','"A quarter tank of fuel or under"'),
('"Each side and the odometer photographed before pickup"','"Each side and the odometer in your own photos before pickup"'),
('"A good key and a note about any known faults"','"A good key and a word about anything that does not work"'),
('"Add-on alarms turned off"','"Aftermarket alarms shut off"'),
(HWLINE,'Read %s for the order of things and %s for what to do the morning the truck comes.'%(HW,PR)),
('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on 5th Avenue downtown.','Our FMCSA license and our $75,000 bond are on file in the federal register, where anyone can see them. The office is on 5th Avenue downtown.'),
(WHY2,'A single coordinator carries your move from the quote to the delivery call. The %s page sets out open, enclosed, and expedited.'%SV),
('Charleston is the lowest lane on the table, fifty miles up 64. SUVs and pickups run 10 to 25 percent more.','Charleston is the lowest lane on the table, fifty miles up 64. For an SUV or a pickup, add 10 to 25 percent.'),
('Yes. Cars arrive in mid-August and leave in May. Mom or Dad books, and someone over eighteen signs at the lot. The campus blocks are full that week. The meeting point is the lots on 5th Avenue or Hal Greer. The date sets the window.','Yes. Cars arrive in mid-August and leave in May. A parent books, and anyone over eighteen signs at the lot. The campus blocks are full that week. The meeting point is the lots on 5th Avenue or Hal Greer. The date decides the window.'),
('We call the moment the forecast turns. The pickup moves to the first clear morning at the same figure.','We phone the moment the forecast turns, and the pickup moves to the first clear morning. The figure stays put.'),
('The handoff happens at the lots nearest the site. If the employer pays you back, we write up what it needs.','The handoff happens at the lots nearest the site. If the employer covers the move, we write it up the way it wants.'),
('Yes. The carrier brings a winch, and the loading time is already in the figure. The big-box lots on Route 60 and the mall lots in Barboursville are flat. Tell us whether it rolls, steers, and brakes.','Yes. The carrier arrives with a winch, and the loading time is part of the figure. The big-box lots on Route 60 and the mall lots in Barboursville are flat. Tell us if it rolls, if it steers, and if it brakes.'),
('Both addresses with the neighborhood or the river town. What it is and whether it runs. Open or enclosed, and the week around the move-in or the start date. With those, the Huntington figure comes back the same day.','The pickup and delivery addresses, with the neighborhood or the river town. The vehicle and whether it runs. Open or enclosed, and the week around the move-in or the start date. Give us those, and the Huntington figure comes back the same day.'),
('Two minutes on the form above gets your lane a Huntington figure. Name the neighborhood and the week, and a carrier already running 64 takes it.','Two minutes on the form above returns a Huntington figure for your lane. Name the neighborhood and the week, and the next carrier on 64 takes the car.'),
])

fix('build_salem_local.py', [
('*2026 estimates from Salem for a sedan that runs, open trailer. Count on 10 to 25 percent more for an SUV or a pickup, and more for enclosed. The week you pick and the carriers on 5 that week set the real figure.','*2026 estimates from Salem, sedan that runs, open trailer. An SUV or a pickup runs 10 to 25 percent above these, and enclosed runs above that. The week you pick and the carriers on 5 that week set the real figure.'),
('A session start in January or the late August move-in means a busy week. The %s explains what size, condition, and timing do to the figure.'%CG,'A session start in January or the late August move-in means a busy week. Size, condition, and timing each move the figure, and the %s says how much.'%CG),
('Fairmount hill or Keizer cul-de-sac. Tell us the neighborhood and whether the car runs.','Fairmount hill or Keizer cul-de-sac. Tell us the neighborhood and say whether the car runs.'),
('Open trailers carry most of the valley, and the table above is priced for one.','Most of the valley ships open, and the figures above assume an open trailer.'),
('Portland is the lowest lane on the table, an hour up the interstate. SUVs and pickups run 10 to 25 percent more.','Portland, an hour up the interstate, is the lowest lane on the table. An SUV or a pickup runs 10 to 25 percent more.'),
('Yes. The university takes cars in late August, and the community college follows the same week. Mom or Dad books, and an adult signs at the lot. The blocks around the Capitol are full that week, so the meeting point is the Riverfront Park lots. The date sets the window.','Yes. The university takes cars in late August, and the community college follows the same week. A parent books, and an adult signs at the lot. The blocks around the Capitol are full that week, so the meeting point is the Riverfront Park lots. The window is set by the date.'),
('Where it starts and ends, with the neighborhood. What it is and whether it runs. Open or enclosed, and the week around the start date or the move. That is enough for a Salem figure the same day.','Where it starts and ends, with the neighborhood. The year, make, and model, and whether it runs. Open or enclosed, and the week around the start date or the move. That is enough for a Salem figure the same day.'),
])

# pass 2: six 19-20 word sentences introduced by the rewrites above
fix('build_minneapolis_local.py', [
('The county hospital, the one in Phillips, the university medical center, and the veterans hospital bring residents each June. Traveling nurses come all year.','The county hospital, the one in Phillips, the university hospital, and the veterans hospital bring residents each June. Traveling nurses come all year.'),
])
fix('build_rapidcity_local.py', [
('Figure 10 to 25 percent more for an SUV or a pickup and a step up again for enclosed.','Figure 10 to 25 percent more for an SUV or a pickup, and a step up for enclosed.'),
('The driver walks the car with a camera at pickup and notes its condition on the Bill of Lading.','The driver walks the car with a camera at pickup and fills in the Bill of Lading.'),
])
fix('build_burlington_local.py', [
('Our call goes out as soon as the forecast turns, and the pickup moves to the first plowed morning.','Our call goes out when the forecast turns, and the pickup moves to the first plowed morning.'),
])
fix('build_huntington_local.py', [
('Read %s for the order of things and %s for what to do the morning the truck comes.'%(HW,PR),'Read %s for the order of things and %s for the morning the truck comes.'%(HW,PR)),
('Our FMCSA license and our $75,000 bond are on file in the federal register, where anyone can see them.','Our FMCSA license and our $75,000 bond are on file in the federal register for anyone to see.'),
])

# pass 3 (fact): the Rapid City office is in the 400 block of St. Joseph, a mile west of the School of Mines campus
fix('build_rapidcity_local.py', [
('Our office is on St. Joseph Street downtown, a block from Main Street and near the engineering school.','Our office sits downtown on St. Joseph, a block off Main Street and a mile from SD Mines.',2),
('The engineering school downtown brings students in late August and graduates them in May.','The engineering school east of downtown brings students in late August and sends them home in May.'),
])
