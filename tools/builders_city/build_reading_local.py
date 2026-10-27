import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Reading, Pennsylvania','Car shipping in Berks County, an hour from Philadelphia on 422 and halfway between the Turnpike and 78',
 ['Car shipping in Reading runs off the 422 bypass around the city and the 222 expressway. Ship Guy is a licensed auto transport broker with an office on Lancaster Pike in Shillington.',
  'We book vetted carriers across Berks County, from Wyomissing and West Reading to Exeter, Muhlenberg, and Kutztown. The trucks belong to the carriers, and we hold the authority and the bond.',
  'US 422 loops the west and south sides as the bypass and runs east to King of Prussia. US 222 runs north to Allentown and south to Lancaster. Interstate 176 connects the bypass to the Turnpike at Morgantown. Route 61 runs north to Pottsville, and Route 12 is the north bypass.',
  'This page covers 422, 222, 176, Route 61, the row-house grid, Mount Penn, Wyomissing, Exeter, and the boroughs. It also covers the hospital, the colleges, the warehouses, the steel plant, the battery maker, and the lanes.'],
 'Reading at a glance',
 ['Most pickups happen within 1 to 3 days. The Philadelphia carriers come out 422 every day, and the Allentown and Lancaster trucks arrive on 222.',
  'Philadelphia, Harrisburg, Allentown, Baltimore, and New York are a same-day haul. Washington and Pittsburgh take a day. Boston takes one, and Charlotte takes one to two. Florida takes three.'],
 'Tell us the borough or the township. The row-house grid in the city, Centre Park, and Mount Penn need a meeting spot. Wyomissing, Exeter, Spring Township, and the newer subdivisions usually allow the curb.'))

BODY.append(sec('The Roads','The 422 Bypass, US 222, Interstate 176, Route 61, Route 12, and Lancaster Pike',
 prose(
  L('Reading sits inside a ring of bypasses. A carrier never has to enter the city grid to reach it.'),
  P('US 422 is the West Shore Bypass, a freeway around the west and south sides along the river. It runs east through Pottstown to King of Prussia and the Philadelphia carriers. The state is rebuilding the bypass bridges in stages through the decade, and whole ramps close for months. West of the city, 422 runs to Lebanon and Hershey.'),
  P('US 222 is a limited-access road north to Kutztown and Allentown, where it meets 78. South of the city it runs four lanes to Lancaster. Interstate 176 is the spur from the bypass south to the Turnpike at Morgantown. The toll rides inside the quote. Route 61 is the Pottsville Pike north through Muhlenberg to Schuylkill County. Route 12 is the Warren Street Bypass across the north side.'),
  P('Lancaster Pike is the old 222 through Shillington, and Penn Avenue carries West Reading and Wyomissing. Penn Street crosses the river into downtown. Fifth Street and Centre Avenue run north and south through the grid. Perkiomen Avenue runs the east side to Exeter, and Skyline Drive climbs Mount Penn to the pagoda. The Schuylkill bends around the city, and the Penn Street and Buttonwood Street bridges set the crossings.'),
  P('The carriers come off the bypass at Lancaster Avenue and off 222 at the Broadcasting Road exit. The shopping centers on Route 222 in Wyomissing and the Lancaster Avenue exit lots are the meeting spots. The centers on the Pottsville Pike work too. The ballpark lots on Route 61 work outside game nights.'),
  P('Our office is on Lancaster Pike in Shillington, minutes from the 222 and 422 interchange.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Row-House Grid, Centre Park, Mount Penn, Wyomissing, West Reading, Shillington, Exeter, Muhlenberg, and the Boroughs',
 prose(
  L('Reading is a dense old city on a slope with comfortable suburbs around it. The truck meets the city at the edge.'),
  P('Downtown along Penn Street is the arena, the courthouse, and the hotel blocks. The grid around it is row houses on a slope. The narrow one-way streets are parked solid on both sides. The driver meets you at the arena lots or on the Penn Street bridge approach. Centre Park north of downtown is big houses on narrow streets under old trees. The handoff moves to Centre Avenue.'),
  P('Mount Penn climbs behind the city with steep streets a loaded trailer will not take. The borough of Mount Penn and the hillside blocks meet the truck on Perkiomen Avenue. The 18th Ward and the Glenside grids on the west side are tighter row houses. The handoff moves to the bypass lots.'),
  P('Wyomissing across the river is the wealthy suburb, with wide streets and big trees. The shopping centers sit on Route 222. The driver reaches most curbs. West Reading along Penn Avenue is the restaurant row and tight grids. The handoff moves to the hospital lots. Shillington and Kenhorst to the south are older boroughs with narrow blocks and new subdivisions behind them. Spring Township and Sinking Spring to the west are wide, and the curb works.'),
  P('Exeter and Reiffton to the east are postwar subdivisions on wide streets, and the driver reaches the house. Muhlenberg to the north is the retail strip on the Pottsville Pike and the grids behind it. Kutztown with the university sits twenty-five minutes north. Boyertown, Birdsboro, Hamburg, and Fleetwood are the boroughs at the edges. All of them price the same as Reading. So do Lancaster and Allentown at the two ends of 222.'),
 )))

ROUTES=[("Harrisburg, PA","US-422/I-283 · ~55 mi","Same day","$140–$230"),("Philadelphia, PA","US-422/I-76 · ~60 mi","Same day","$150–$240"),
 ("Allentown, PA","US-222 · ~40 mi","Same day","$130–$210"),("Baltimore, MD","US-222/I-83 · ~100 mi","Same day","$170–$280"),
 ("New York, NY","US-222/I-78 · ~130 mi","Same day","$190–$300"),("Washington, DC","US-222/I-83/I-95 · ~150 mi","Same day","$200–$310"),
 ("Pittsburgh, PA","I-176/I-76 · ~250 mi","1 day","$250–$380"),("Boston, MA","I-78/I-84/I-90 · ~330 mi","1 day","$300–$440"),
 ("Charlotte, NC","I-83/I-81/I-77 · ~500 mi","1–2 days","$420–$600"),("Orlando, FL","I-95 · ~1,000 mi","3 days","$700–$1,000")]
BODY.append(rate_table('Lanes &amp; Costs','Reading Car Shipping Lanes and Estimated Costs',
 'The lanes Berks County cars travel most, with estimated open-trailer ranges. Your own route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Reading for a sedan that runs, on an open trailer. An SUV or a pickup adds 10 to 25 percent, and an enclosed trailer adds more. Turnpike tolls are inside the number when a carrier uses 176. The season and the carriers free on your dates set the final figure.',
 prose(
  P('Reading prices with Philadelphia on every lane, because the 422 carriers reach the city in an hour. It runs a little over Allentown to New York and a little under it to Baltimore and Washington. The Pittsburgh lane rides 176 and the Turnpike and runs a day. The Florida lane fills with retirees each fall.'),
  P('A move timed to the August move-in or a plant start date ships with the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospital, the Colleges, the Specialty Steel Plant, the Battery Maker, the Warehouses, and the Philadelphia Exurb',
 prose(
  L('Reading relocates nurses, plant engineers, students, and families priced out of the Philadelphia suburbs. The hospital in West Reading moves more people than anyone in Berks County.'),
  P('The hospital in West Reading is the largest employer in the county. It hires traveling nurses year round and takes residents each June. The physicians come with a closing date and a second car. The second hospital in Bern Township hires the same way. A reimbursed move gets its paperwork from us.'),
  P('The specialty steel plant on the east side moves metallurgists and engineers in on production schedules. The battery maker north of the city is the largest manufacturer in the county. It relocates engineers the same way. The department store chain headquartered here and the grocery chain move managers on their own schedules. The pretzel bakery down Lancaster Pike has baked in Shillington for generations.'),
  P('The distribution centers along 222 and Route 61 move managers in on start dates. The city college, the university on the south side, and the state campus take cars each August. The university in Kutztown does the same. A parent sets up the booking, and an adult over eighteen signs at a campus lot.'),
  P('Families priced out of the Main Line buy in Exeter, Wyomissing, and Spring Township on closing dates. One car rides the trailer while the other is driven. Retirees leave for Florida and the Carolinas each fall. The Guard post at Indiantown Gap rotates staff on orders. Ship Guy is a private broker with no tie to it. The <a href="military-car-shipping.html">military</a> page has the timing, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page has the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Ballpark, the Folk Festival, the Antique Cars, the Jazz Fest, the Schuylkill Floods, and the Bypass Work',
 prose(
  L('Reading runs on a ballpark on Route 61 and a county full of old cars. The river comes up in a big storm.'),
  P('The ballpark on Route 61 fills its lots on game nights from April through September. The arena downtown fills the garages on hockey nights and concert nights. The jazz festival fills Wyomissing and downtown for ten days in April. The German club’s Oktoberfest fills the east side for a September weekend. A handoff near any of them moves to the daytime.'),
  P('The folk festival fills Kutztown for nine days around the Fourth of July. The antique car show fills Boyertown on the Saturday of Labor Day weekend. The collectors ship in from three states. The county fair fills the fairgrounds in Bern Township for a week in August. The handoff moves to the next morning.'),
  P('The Schuylkill floods downtown and the river flats in a big storm. Agnes in 1972 put Penn Street under water, and Ida in 2021 closed the river bridges for days. A pickup on the flat moves up the hill until the water drops. The Tulpehocken and the smaller creeks flood the western boroughs the same way.'),
  P('Winter brings thirty inches of snow, and the January 2016 blizzard dropped more than that in a day. The November 2018 storm trapped trucks on 78 and 222 for most of a day. The hill streets ice before the plows reach them. The carriers wait in Lancaster or at the Morgantown plaza until the roads clear. A winter pickup can lose a day. The bypass rebuild closes ramps for months at a time, and the driver plans the approach around it.'),
 )+chips(["Downtown","Penn Street","Centre Park","Centre Avenue","Mount Penn","Pagoda","Skyline Drive","18th Ward","Glenside","Perkiomen Avenue","Wyomissing","Broadcasting Road","West Reading","Penn Avenue","Shillington","Lancaster Pike","Kenhorst","Spring Township","Sinking Spring","Exeter","Reiffton","Muhlenberg","Pottsville Pike","Temple","Bern Township","Leesport","Fleetwood","Kutztown","Hamburg","Birdsboro","Boyertown","Douglassville","Morgantown","Lancaster"])
 +NOTE('Serving Reading and all of Berks County, row-house block or Wyomissing cul-de-sac. Tell us the borough and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Reading?',
 prose(
  L('Most Berks County cars ride an open trailer, and the lane table above is priced for one.'),
  P('An enclosed trailer keeps off the road salt, the cinders, and the quarry dust. The collectors who fill Boyertown on Labor Day weekend book one for the antiques. Executives relocating a new car to the steel plant or the hospital book one too.'),
  P('A commuter car or a plant pickup is fine on an open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages walk through the choice.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot in Wyomissing or at the bypass exit, and a signature at the far end. The closing or the start date picks the week.'),
  P('Approve the number, and the car is booked with a carrier already running 222 or 422. The lot and the window are settled that day. The driver walks around the car with you at pickup. Every existing mark is recorded on the Bill of Lading, and you both sign. The far end is checked against that record.'),
 )+ULI([
  "Personal items cleared from the cabin and the trunk",
  "Keep the fuel to about a quarter tank",
  "Each side and the odometer photographed before the handoff",
  "One working key handed to the driver, with any fault named",
  "Aftermarket alarm shut off",
  "In the city grid or on Mount Penn, meet the truck at the arena or on the bypass",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Reading Drivers Choose Ship Guy',
 prose(
  L('We book the carriers already running 422 and 222. We know which blocks of the grid a trailer cannot enter.'),
  P('Ship Guy’s FMCSA license and $75,000 bond are both on the federal register for anyone to check. Our office is on Lancaster Pike in Shillington.'),
  P('Your coordinator stays on the move from the first call to the last signature. The <a href="services.html">services</a> page explains open, enclosed, and expedited transport.'),
 )))

BODY.append(office('Reading','2395 Lancaster Pike #599','Reading, PA 19607','+16102295982','(610) 229-5982','ET',
 '2395+Lancaster+Pike+%23599,+Reading,+PA+19607','Visit Us','Find Ship Guy in Reading',
 'Our office is on Lancaster Pike in Shillington, minutes from the 222 and 422 interchange.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4679.219198997863!2d-75.991209!3d40.3006409!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c6712acfb9e5db%3A0x75a7b9c4aac1f635!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793103556958!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Reading to New York or Florida?","New York runs one hundred ninety to three hundred dollars for a sedan. That is about one hundred thirty miles up 222 and 78. Orlando runs seven hundred to a thousand, about a thousand miles down 95. Philadelphia is an hour down 422 and the lowest of the three. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street in the city or on Mount Penn?","Usually not. The grid is row houses on a slope with narrow one-way streets parked solid. Mount Penn is too steep for a loaded trailer. The driver meets you at the arena lots, on Centre Avenue, or on Perkiomen Avenue. Wyomissing, Exeter, Spring Township, and the newer subdivisions usually allow the curb."),
 ("Do you ship cars for people relocating to the hospital or the plants?","Yes, every month. The hospital in West Reading hires traveling nurses year round and takes residents each June. The specialty steel plant and the battery maker move engineers in on production schedules. A second car usually comes along on a trailer. A reimbursed move gets its paperwork from us."),
 ("Can you deliver on the Albright, Alvernia, or Kutztown move-in date?","Yes. The campuses take cars in each August and send them home in May. A parent sets up the booking, and an adult over eighteen signs at a campus lot. The window is matched to move-in day and moves with it. The city campus is inside the grid, so the handoff happens at a lot on 13th Street."),
 ("Can you ship a car to or from Wyomissing, Exeter, or Kutztown?","Yes, and all three price the same as Reading. Wyomissing rides the same carriers off 222 at Broadcasting Road, and the curb works on most streets. Exeter rides them off 422 at Perkiomen, and the subdivisions allow the curb. Kutztown rides them up 222, and the handoff happens at a lot by the campus. Send the full address for a township street."),
 ("Does the 422 bypass construction affect my pickup?","Some weeks, yes. The state is rebuilding the bypass bridges in stages, and whole ramps close for months. The driver plans the approach around the closures. A meeting spot on the open side of the river saves an hour. We tell you which exit is open when the window is set."),
 ("What happens if the Schuylkill floods on my pickup day?","A pickup on the river flat moves up the hill until the water drops. Ida in 2021 closed the river bridges for days, and the carriers crossed at Pottstown instead. You hear it from us first. The hill streets and the suburbs never notice."),
 ("Are the Turnpike tolls in my price?","Yes. A carrier that takes 176 to the Turnpike pays by the mile with a transponder. The toll rides inside the quote. There is no separate line. The bypass, 222, Route 61, and the county roads carry no toll."),
 ("Can you ship a car that does not run from Reading?","Yes. A carrier with a winch is sent, and the quote carries the loading time from the start. The shopping centers on Route 222 or the lots at the bypass exit give the driver level ground. Say whether the car rolls, steers, and brakes."),
 ("What do you need for a Reading car shipping quote?","Pickup and delivery addresses, with the borough or the township. Year, make, model. Does it run. Open or enclosed. The week around the closing or the start date. Five answers, and the Reading number is on its way within the day."),
]
BODY.append(faq_section(FAQ,'Reading FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Reading?','A number for your lane takes two minutes on the form above. Name the borough and the week, and a carrier already on 222 takes it.','+16102295982','(610) 229-5982','Get your free Reading quote'))

build({
 'slug':'auto-transport-reading-pennsylvania',
 'title':'Car Shipping in Reading, PA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Reading, PA, in Berks County an hour from Philadelphia on 422. Hospital and plant relocations, college move-in timing, arena-lot handoffs for the row-house grid and Mount Penn, curbside pickups in Wyomissing and Exeter, Kutztown and the boroughs, the Turnpike toll, the Schuylkill floods, and the bypass rebuild. Local office on Lancaster Pike in Shillington. Free quote.',
 'h1':'Car Shipping in<br>Reading, <span class="accent">Pennsylvania</span>',
 'lede':'Open, enclosed, and expedited auto transport across Berks County, planned around the bypass, 222, the row-house grid, the plant calendars, and the river.',
 'tel':'+16102295982','disp':'(610) 229-5982','brand':'Reading','keyword':'car shipping in reading',
 'localterms':['reading','berks county','422','bypass','222','lancaster pike','shillington','wyomissing','west reading','exeter','muhlenberg','kutztown','king of prussia','allentown','lancaster','interstate 176','turnpike','morgantown','route 61','pottsville','route 12','downtown','row-house','mount penn','boroughs','hospital','colleges','warehouses','specialty steel','battery maker','floods','philadelphia','harrisburg','baltimore','new york','washington','pittsburgh','boston','charlotte','florida','centre park','spring township','west shore bypass','pottstown','lebanon','hershey','limited-access','toll','pottsville pike','schuylkill county','warren street','penn avenue','penn street','fifth street','centre avenue','perkiomen avenue','skyline drive','pagoda','schuylkill','buttonwood street','bridges','broadcasting road','shopping centers','ballpark','game nights','arena','courthouse','one-way','18th ward','glenside','restaurant row','kenhorst','sinking spring','reiffton','retail strip','boyertown','birdsboro','hamburg','fleetwood','nurses','plant engineers','students','main line','traveling nurses','residents','physicians','bern township','metallurgists','manufacturer','department store','grocery chain','pretzel bakery','distribution centers','start dates','university','state campus','retirees','carolinas','guard post','indiantown gap','jazz festival','oktoberfest','folk festival','fourth of july','antique car show','labor day','county fair','agnes','1972','ida','2021','tulpehocken','thirty inches','january 2016 blizzard','november 2018','plows','plaza','cinders','quarry','bill of lading','fmcsa','13th street','temple','leesport','douglassville'],
}, BODY, FAQ)
