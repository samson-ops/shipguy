import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("3–6 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Billings, Montana','Car shipping in the one Montana city a carrier passes through on purpose, under the Rims where 90 meets 94',
 ['Car shipping in Billings runs on Interstate 90 and 94, which meet at the east edge of town. Ship Guy is a licensed auto transport broker with an office on Poly Drive.',
  'We book vetted carriers across Billings, from the South Side to the Heights and out to Laurel. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 90 runs along the south side with the Shiloh, King Avenue, 27th Street, and Lockwood exits. Interstate 94 splits off at Lockwood for North Dakota. Highway 87 is Main Street through the Heights to Roundup. 27th Street climbs the Rims to the airport, and Highway 3 runs west from there.',
  'This page covers 90, 94, 87, the Rims, downtown, the West End, the South Side, and the Heights. It also covers the honest window, the hospitals, the refineries, the railroad, the fair, and the winter.'],
 'Billings at a glance',
 ['Most pickups happen within 3 to 6 days, and Billings runs the fastest end of that. Every carrier crossing Montana on 90 passes the city, and the 94 trucks from Fargo end here. A wide date range is the biggest help.',
  'Bozeman and Great Falls ride a single day on the truck. Missoula, Rapid City, and Bismarck take a day. Denver, Salt Lake, and Spokane take about two. Seattle and Fargo take two to three.'],
 'Tell us the neighborhood. Downtown, the blocks under the Rims, and the South Side meet the truck on a main road. The West End, the Heights, Grand Avenue, and the Lockwood lots usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 90, Interstate 94, Highway 87, Highway 3, 27th Street, King Avenue, Grand Avenue, Main Street, and the Rims',
 prose(
  L('Billings is the only Montana city where two interstates meet. The Rims decide how a truck gets anywhere else. A carrier picks its exit and stays below the cliffs.'),
  P('Interstate 90 runs along the south side of the city between the tracks and the river. The Shiloh exit serves the West End, King Avenue serves the strip, and 27th Street serves downtown. Interstate 94 leaves at Lockwood and runs east through Miles City to Fargo and the Twin Cities. Bozeman is a hundred forty miles west on 90, and Missoula is three hundred forty. Interstate 25 to Denver starts at Buffalo in Wyoming, three hours south on 90.'),
  P('Highway 87 is Main Street through the Heights and the road north to Roundup. 27th Street runs from the river through downtown and climbs the Rims to the airport. Highway 3 runs west from the airport along the top of the cliffs. Zimmerman Trail climbs the Rims from the West End. The two cliff roads ice first and close first. King Avenue is the commercial strip along 90, and Grand Avenue is the residential one a mile north. Rimrock Road runs along the foot of the cliffs.'),
  P('The carriers come off 90 at King Avenue or 27th Street. The big-box lots on King Avenue are the usual meeting spot. The fairgrounds lots at MetraPark work outside the fair. So do the truck stops at Lockwood and the lots on Main Street in the Heights. The airport cell lot on the Rims works for a fly-and-ship.'),
  P('Our office is on Poly Drive, across from the college and below the Rims.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the North Side, Poly Drive, the West End, Grand Avenue, the South Side, the Heights, Lockwood, and Laurel',
 prose(
  L('Billings is an old grid below the Rims and a boom of subdivisions to the west. The Heights is a second city on the plateau above. The truck meets the old grid on a main road.'),
  P('Downtown runs from the tracks north to the hospitals. It is towers and one-way streets around the tallest building in the state. The driver meets you at the garage entrances or the fairgrounds lots. The North Side between downtown and the Rims is the old neighborhood. The streets around Pioneer Park are narrow and lined with brick houses. The hospitals sit at the east end of it. The handoff moves to 27th Street or Rimrock Road. Poly Drive and the streets around the college are wider, and the curb usually works.'),
  P('The West End off Shiloh Road is the newest part of the city. The subdivisions outrun the maps every year. The streets are wide, and the truck reaches the curb. Send the full address, because the carrier’s map may not have it. Grand Avenue and the Central neighborhood between the two strips are plain postwar grids where the curb works. The streets under the Rims on Rimrock Road have steep driveways, and the handoff moves to the road.'),
  P('The South Side across the tracks is the oldest grid. It is small houses on narrow streets near the beet plant and the refinery. The driver meets you on State Avenue or at the lots on 27th. The Heights across the airport is a second city on the plateau, Alkali Creek to Lake Elmo. The grids off Main Street are wide, and the curb usually works. The road up is 27th or Main, and both ice first.'),
  P('Lockwood east of the city is the refinery, the truck stops, and rural lots with long driveways. The handoff happens at the truck stops. Laurel fifteen miles west is the rail yard and the second refinery. It ships with the same trucks and prices the same as Billings. Red Lodge, Columbus, and Hardin are an hour out and add a few hours on the day.'),
 )))

ROUTES=[("Bozeman, MT","I-90 · ~140 mi","Same day","$150–$240"),("Great Falls, MT","US-87/I-15 · ~220 mi","Same day","$240–$360"),
 ("Rapid City, SD","I-90 · ~320 mi","1 day","$310–$450"),("Missoula, MT","I-90 · ~340 mi","1 day","$320–$460"),
 ("Bismarck, ND","I-94 · ~420 mi","1 day","$380–$540"),("Spokane, WA","I-90 · ~540 mi","2 days","$380–$540"),
 ("Salt Lake City, UT","I-90/I-15 · ~540 mi","2 days","$400–$570"),("Denver, CO","I-90/I-25 · ~550 mi","2 days","$450–$650"),
 ("Fargo, ND","I-94 · ~620 mi","2–3 days","$470–$680"),("Seattle, WA","I-90 · ~820 mi","2–3 days","$600–$880")]
BODY.append(rate_table('Lanes &amp; Costs','Billings Car Shipping Lanes and Estimated Costs',
 'The lanes Yellowstone County cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Billings, running sedan, open trailer. An SUV or a pickup runs 10 to 25 percent higher, and enclosed higher again. The date range you give and the trucks crossing on 90 that week set the real figure.',
 prose(
  P('Billings prices like a hub on a pass-through road, which is what it is. The Seattle and Minneapolis trucks cross on 90 and 94 and stop here when the load justifies it. The Denver lane rides 90 and 25 through Wyoming and fills with the Front Range traffic. The Salt Lake lane rides 90 to Butte and 15 south. The Arizona lane fills each October with the snowbirds.'),
  P('A July date at the hospitals or the August fair week means a busy week. How size, condition, and the date range shape the figure is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Two Hospitals, the Refineries, the Railroad, the Oil Offices, the Beet Plant, the Colleges, and the Ranch Families',
 prose(
  L('Billings relocates physicians, nurses, refinery hands, railroaders, and students. The two hospitals move more households than the rest of the city combined.'),
  P('The two hospitals on the north side of downtown serve Montana, northern Wyoming, and the western Dakotas. Both bring residents each June and hire traveling nurses year round. Physicians arrive from everywhere on contract dates. The handoff for all of them happens at the fairgrounds lots or on 27th Street. If the hospital or an employer pays you back for the move, we write up what it needs.'),
  P('The refineries on the south side, at Lockwood, and in Laurel bring turnaround crews every spring and fall. The railroad’s yard in Laurel moves crews on bid cycles. The oil and gas offices downtown run the Bakken from here and move engineers on project dates. The beet plant on the south side runs its campaign from October into February and hires for it. The livestock auctions and the ranch supply houses move managers the same way.'),
  P('The state university campus below the Rims takes student cars in late August. The college on Poly Drive does the same. A parent books, and an adult signs at a lot. The cars leave in May. There is no base in the city, and the airmen go to Great Falls. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the paperwork for a state line.'),
  P('Ranch families retire into the city from every county in the east. Half of northern Wyoming shops, flies, and sees its doctors here, and some of it moves here. Retirees leave for Arizona each October and come back in April.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Fair, the Stock Show, the Car Cruise, the Strawberry Festival, Move-In Week, Hunting Season, the Chinooks, the Wind, and the Cold',
 prose(
  L('Billings runs on a fair calendar and a hospital calendar. The weather problem is a winter that arrives in October and leaves in May.'),
  P('The fair fills MetraPark for nine days in August and takes the fairgrounds lots with it. The stock show fills them again in October. The car cruise closes Montana Avenue on a Saturday in September. The strawberry festival closes downtown on a Saturday in July. Move-in week in late August fills the blocks around both campuses. Hunting season in October and November fills 90 and 94 with pickups and trailers. The carriers slow down. Book three weeks ahead for an August date.'),
  P('Winter brings cold snaps of twenty and thirty below, and a carrier does not load a frozen car. The February 2019 cold held the city below zero for days at a time. A chinook clears the snow in an afternoon and turns the streets to slush. The wind on the Rims closes the airport road and Zimmerman Trail before anything else. A blizzard closes 90 over the pass at Bozeman and 94 east of Miles City. The carriers wait in the city until the plows finish.'),
  P('The Father’s Day tornado in June 2010 tore the roof off the arena at MetraPark. It crossed the Heights. The June 2022 flood on the Yellowstone shut the water plant for two days. It cut the road to Red Lodge. Hail comes most summers, and a carrier does not load under a hail warning. The fire smoke in August settles under the Rims some years and stays for weeks.'),
  P('Summer is hot and dry, and the afternoon storms are short. They shift the loading hour and nothing else.'),
 )+chips(["Downtown","Montana Avenue","The North Side","Pioneer Park","Poly Drive","The Hospitals","Rimrock Road","Zimmerman Trail","The Airport","The West End","Shiloh","Rehberg Ranch","Ironwood","Josephine Crossing","Grand Avenue","King Avenue","Central","The South Side","State Avenue","The Heights","Alkali Creek","Lake Elmo","Main Street","MetraPark","Lockwood","Laurel","Red Lodge","Columbus","Hardin","Roundup"])
 +NOTE('Serving Billings and the whole Yellowstone valley, North Side block or Heights cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Billings?',
 prose(
  L('Open trailers carry most of eastern Montana, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the road salt, the gravel the state spreads, and the hail. The collectors on the West End book one. So do the ranch families moving a restored pickup. A car leaving ahead of a blizzard goes on whatever truck has room. We say so up front.'),
  P('A commuter car or a student’s car does fine in the open. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages put the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot on King Avenue, and a signature when the car arrives. The date range decides the week more than anything else.'),
  P('Approve the figure, and a carrier already crossing on 90 that week gets the car. We settle the lot and the window the same afternoon. The driver photographs the car at pickup and writes up its condition on the Bill of Lading. You initial it, and delivery is checked against it.'),
 )+ULI([
  "Everything personal out of the cabin and the trunk",
  "Fuel down to a quarter tank",
  "Photograph each side and the odometer before the truck comes",
  "One good key, and a note about any known faults",
  "Any add-on alarm turned off",
  "On the North Side, the South Side, or under the Rims, expect a main road",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page has the sequence, and the <a href="car-shipping-preparation.html">preparation</a> page has the checklist for pickup day.'))))

BODY.append(sec('Why Ship Guy','Why Billings Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already cross on 90 every week. We know which ones stop in Billings and which ones only pass.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on Poly Drive below the Rims.'),
  P('Your coordinator stays on the move from the quote to the delivery signature. The <a href="services.html">services</a> page sets out open, enclosed, and expedited.'),
 )))

BODY.append(office('Billings','1500 Poly Dr #753','Billings, MT 59102','+14066292642','(406) 629-2642','MT',
 '1500+Poly+Dr+%23753,+Billings,+MT+59102','Visit Us','Find Ship Guy in Billings',
 'Our office is on Poly Drive, across from the college and below the Rims.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3433.834082209845!2d-108.55286699999999!3d45.7944277!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x53487df19cdcf06d%3A0x26b6a075d9f7fd4f!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629863594!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Billings to Denver or Seattle?","Denver runs four hundred fifty to six hundred fifty dollars for a sedan. That is about five hundred fifty miles down 25 through Wyoming. Seattle runs six hundred to eight hundred eighty, about eight hundred twenty miles west on 90. Bozeman is the lowest lane on the table. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Why does a Billings pickup take 3 to 6 days?","Because Montana is a pass-through market, and the carriers cross on 90 between Seattle and the Midwest. Billings is the one city they pass on purpose, so it runs the fastest end of the window. A carrier adds a Billings stop when the load justifies it. A wide date range is the biggest help you can give us, and a tight one costs more."),
 ("Can the carrier come to my street on the North Side or in the Heights?","The Heights, yes. The grids off Main Street from Alkali Creek to Lake Elmo are wide. The curb works on most blocks. The North Side, no. The streets around Pioneer Park are narrow, and the driver meets you on 27th Street or Rimrock Road. The West End and Grand Avenue allow the curb nearly everywhere."),
 ("Do you ship cars for the hospitals and the refineries?","Yes, every week of the year. The two hospitals bring residents each June and traveling nurses all year. The handoff happens at the fairgrounds lots. The refineries bring turnaround crews each spring and fall, and the railroad moves crews on bid cycles. When the employer reimburses the move, we supply the paperwork it asks for."),
 ("Can you deliver on an MSU Billings or Rocky move-in date?","Yes. The state university takes cars in late August, and the college on Poly Drive follows the same week. Mom or Dad books, and an adult signs at a lot. The blocks around both campuses are full that week, so the meeting point is the fairgrounds lots. The date sets the window."),
 ("Can you ship a car to or from Laurel, Red Lodge, or Hardin?","Yes. Laurel rides the same carriers and prices the same as Billings. Red Lodge, Columbus, and Hardin are an hour out and add a few hours on the day. The road to Red Lodge is two lanes. A trailer meets you in town rather than up a ranch road."),
 ("What happens if a blizzard or the cold hits on my pickup day?","The truck holds in the city until the plows open 90 or 94, usually a day. A carrier does not load a car at thirty below, because the hydraulics slow and the straps stiffen. We call the moment the closure posts. The pickup moves to the next clear morning, and the figure holds."),
 ("Does the fair affect my pickup?","Yes, for nine days in August. The fair takes the fairgrounds lots and fills the roads around MetraPark and the Heights interchange. The handoff moves to King Avenue that week. The stock show in October does the same for a shorter stretch. The rest of the city runs normally."),
 ("Can you ship a car that does not run from Billings?","Yes. A carrier with a winch takes it, and the loading time is part of the quote. The big-box lots on King Avenue and the truck stops at Lockwood are flat. Tell us if it rolls, steers, and brakes."),
 ("What do you need for a Billings car shipping quote?","Both addresses with the neighborhood. The year, make, and model, and whether it runs. Open or enclosed, and the widest date range you can give. With those, the Billings figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Billings FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Billings?','Two minutes on the form above gets your lane a Billings figure. Name the neighborhood and the date range, and a carrier already crossing on 90 takes it.','+14066292642','(406) 629-2642','Get your free Billings quote'))

build({
 'slug':'auto-transport-billings-montana',
 'title':'Car Shipping in Billings, MT — Auto Transport | Ship Guy',
 'meta':'Car shipping in Billings, MT, the carrier hub where 90 meets 94 under the Rims. The honest 3 to 6 day window, hospital and refinery relocations, campus move-in, main-road handoffs for the North Side and the South Side, curbside pickups on the West End and in the Heights, the fair, and the winter. Local office on Poly Drive. Free quote.',
 'h1':'Car Shipping in<br>Billings, <span class="accent">Montana</span>',
 'lede':'Open, enclosed, and expedited auto transport across Billings and the Yellowstone valley, planned around 90, 94, the Rims, the hospital calendar, the fair, and the cold.',
 'tel':'+14066292642','disp':'(406) 629-2642','brand':'Billings','keyword':'car shipping in billings',
 'localterms':['billings','rims','interstate 90','interstate 94','highway 87','highway 3','27th street','king avenue','grand avenue','main street','zimmerman trail','rimrock road','poly drive','airport','downtown','north side','pioneer park','west end','shiloh','south side','state avenue','heights','alkali creek','lake elmo','lockwood','laurel','metrapark','fairgrounds','bozeman','missoula','great falls','miles city','roundup','hardin','red lodge','columbus','rapid city','bismarck','fargo','spokane','salt lake','denver','seattle','wyoming','arizona','snowbirds','hospitals','residents','traveling nurses','physicians','refineries','turnaround','railroad','bid cycles','oil and gas','bakken','beet plant','campaign','livestock auctions','ranch','state university','college','students','move-in','fair','stock show','car cruise','montana avenue','strawberry festival','hunting season','chinook','cold snaps','february 2019','blizzard','father','june 2010','tornado','arena','june 2022','flood','yellowstone','water plant','hail','smoke','road salt','gravel','bill of lading','fmcsa','winch','truck stops','tallest building','pass'],
}, BODY, FAQ)
