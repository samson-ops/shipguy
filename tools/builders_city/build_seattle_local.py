import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Seattle, Washington','Car shipping on the Sound, where Interstate 5 squeezes between the water and the hills and the trailer never gets near the house',
 ['Car shipping in Seattle runs off Interstate 5 and the two floating bridges across the lake. Ship Guy is a licensed auto transport broker with an office on Westlake Avenue by Lake Union.',
  'We book vetted carriers across the Sound, from Everett to Tacoma and across the lake to Bellevue. The trucks belong to the carriers, and we hold the authority and the bond.',
  'Interstate 5 runs north and south through downtown and over the Ship Canal Bridge. Interstate 90 crosses the lake to Bellevue and climbs Snoqualmie Pass to Spokane. The 520 bridge is the other crossing, with a toll. Interstate 405 loops the east side, and the 99 tunnel runs under downtown.',
  'This page covers 5, 90, 520, the hills, the towers, the Eastside, the south end, and the ferries. It also covers the tech campuses, the planemaker, the hospitals, the base, Seafair, the snow, and the lanes.'],
 'Seattle at a glance',
 ['Most pickups happen within 1 to 3 days. The Portland carriers come up 5 all day. The California trucks arrive on the same road every morning.',
  'Portland is a same-day haul. Spokane and Boise take a day. Sacramento, the Bay Area, and Salt Lake City take two. Los Angeles and Denver take three, and the East Coast takes four.'],
 'Tell us the neighborhood and the slope. The hills, the towers, and the old grids all need a meeting spot. The south end, the Eastside subdivisions, and the suburbs toward Everett usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 5, Interstate 90, the 520 Bridge, 405, the 99 Tunnel, and the Ship Canal Bridges',
 prose(
  L('Seattle is a city of chokepoints, and a seventy-five-foot trailer plans around every one of them.'),
  P('Interstate 5 runs through the middle of the city between the water and the hills. It runs from Tacoma through downtown to Everett. It backs up from early morning to late evening, and the express lanes change direction at noon. The Ship Canal Bridge carries it over the water north of downtown. The carriers plan a Sound stop for the middle of the morning or the early afternoon.'),
  P('Interstate 90 leaves downtown on the floating bridge to Mercer Island and Bellevue. It climbs Snoqualmie Pass to Ellensburg and Spokane. The 520 bridge is the other floating crossing. Its toll goes on a transponder and rides inside the quote. Interstate 405 loops the Eastside from Tukwila through Bellevue to Lynnwood. The 99 tunnel carries the old highway under downtown, with a toll of its own.'),
  P('Aurora Avenue is 99 north of the tunnel. The four drawbridges over the ship canal open for boats and stop traffic. They sit at Fremont, Ballard, the university, and Montlake. The West Seattle Bridge carries the peninsula across the Duwamish. It was closed for two years for cracks. Rainier Avenue, Lake City Way, and 15th Avenue are the rest of the grid. The airport is twenty minutes south on 5 or 509.'),
  P('The carriers stage in Kent, Auburn, and Fife, where the yards and the truck stops are. They come up 5 to the stadium lots in SoDo, Northgate, and the Southcenter mall in Tukwila. Those three, the Eastgate and South Kirkland park and rides, and Magnuson Park are the meeting spots. Downtown itself is never one.'),
  P('Our office is on Westlake Avenue on the west shore of Lake Union, south of the Fremont Bridge.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown and the Towers, Capitol Hill, Queen Anne, Ballard, the North End, West Seattle, the South End, the Eastside, and the Ferries',
 prose(
  L('Seattle was built on seven hills. The trailer meets you at the bottom of every one of them.'),
  P('Downtown, Belltown, and South Lake Union are towers on garages, with no curb a trailer can use. The driver meets you at the stadium lots in SoDo or at Northgate. Capitol Hill and First Hill are steep, dense, and parked solid. Queen Anne is a hill with a counterbalance grade a loaded truck will not climb. The handoff for all of them moves to the stadium lots or to Mercer Street.'),
  P('Ballard, Fremont, Wallingford, and Green Lake are the old grids north of the canal. Cars park on both sides, and the drawbridges sit in between. The driver meets you at the lots on 15th or on Aurora. The university district is the same during the quarter. Northgate, Lake City, and Shoreline have the park and ride and the big lots. The curb works on the wider streets.'),
  P('West Seattle sits across the bridge with Alki at the bottom and the junction at the top. The handoff works at the lots at the junction or at Westwood Village. Beacon Hill, Columbia City, and Rainier Valley run along the light rail. The driver meets you on Rainier or Martin Luther King. Georgetown and SoDo are industrial and easy. Burien, Tukwila, Renton, and Kent to the south are wide, and the curb works.'),
  P('Bellevue across the lake is towers downtown and wide subdivisions everywhere else. Redmond, Kirkland, Issaquah, and Sammamish are the same, and the driver reaches the house on most streets. Everett and Lynnwood to the north and Tacoma to the south price the same as Seattle. Bainbridge, Vashon, and the Kitsap towns ride the ferries. The handoff happens on the mainland at the terminal lots.'),
 )))

ROUTES=[("Portland, OR","I-5 · ~175 mi","Same day","$220–$340"),("Spokane, WA","I-90 · ~280 mi","1 day","$260–$390"),
 ("Boise, ID","I-90/I-82/I-84 · ~500 mi","1 day","$430–$620"),("Sacramento, CA","I-5 · ~750 mi","2 days","$560–$820"),
 ("San Francisco, CA","I-5 · ~810 mi","2 days","$600–$880"),("Salt Lake City, UT","I-90/I-84 · ~840 mi","2 days","$600–$880"),
 ("Los Angeles, CA","I-5 · ~1,135 mi","3 days","$800–$1,150"),("Denver, CO","I-90/I-84/I-80 · ~1,320 mi","3 days","$850–$1,200"),
 ("Phoenix, AZ","I-5/US-93 · ~1,420 mi","3–4 days","$900–$1,300"),("Chicago, IL","I-90 · ~2,060 mi","4 days","$1,100–$1,550")]
BODY.append(rate_table('Lanes &amp; Costs','Seattle Car Shipping Lanes and Estimated Costs',
 'The lanes Sound cars take most often, with estimated open-trailer ranges. Your own route gets its number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Seattle for a running sedan on an open trailer. SUVs and pickups add about 10 to 25 percent, with enclosed above that. The 520 and tunnel tolls ride inside the number when a carrier uses them. Pass closures and the carriers free on your dates settle the final figure.',
 prose(
  P('Seattle prices the Interstate 5 lanes better than anything else. The carriers run the coast between here and California all day. The Spokane and Montana lanes ride 90 and wait on Snoqualmie Pass in winter. The California lane runs heaviest northbound in summer, when the tech hires arrive. The East Coast lanes take four days and ride 90 or 84 the whole way.'),
  P('A move timed to a September start date ships with the busiest month of the year. The price follows. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Tech Campuses, the Planemaker, the Hospitals, the University, the Base, and the Port',
 prose(
  L('Seattle relocates more engineers than almost any city in the country. Most of them ship a car up 5 from California.'),
  P('The retailer in South Lake Union and the software company in Redmond hire nationally on start dates. So do the cloud and social offices downtown and in Bellevue. September is the biggest month, and the California lane fills with their cars. Corporate packages usually cover a vehicle, and we supply the paperwork a reimbursed move needs. The handoff works at the stadium lots, at Northgate, or at the Eastgate park and ride.'),
  P('The planemaker’s plants in Everett and Renton move engineers and machinists between sites on program schedules. The hospital systems on First Hill and the medical campus by the university hire traveling nurses all year. They take residents each June. The cancer research center in South Lake Union relocates scientists on grant cycles. The children’s hospital in Laurelhurst recruits the same way.'),
  P('The university runs on quarters, and the cars arrive in the last week of September rather than August. They go home in the middle of June. A parent arranges the shipment, and someone over eighteen signs at a lot off Montlake. The two private universities on the hills run the same calendar.'),
  P('The joint base south of Tacoma rotates soldiers and airmen every summer. The naval station in Everett and the air station on Whidbey rotate crews the same way. The orders pay for one car, and the second one ships with us. Ship Guy is a private broker and has no tie to any base. Timing is on the <a href="military-car-shipping.html">military</a> page. The port receives imported cars, and we move them domestically once customs releases them. The ocean leg to Alaska and Hawaii is separate, and we move the car to the dock. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Seafair, Game Days, Cruise Saturdays, the Lowland Snow, the Heat Dome, and the Smoke',
 prose(
  L('Seattle runs on a summer that fills every lot on the water. Two inches of winter snow shut the hills.'),
  P('Seafair fills the lake for the first weekend of August. The jets close the 90 bridge for an hour at a time. The football and baseball stadiums in SoDo take the stadium lots on game days. The soccer and hockey crowds do the same. A SoDo handoff on a game day moves to the morning or to Tukwila. The university stadium fills Montlake on football Saturdays, and the bridge backs up for hours.'),
  P('The cruise ships sail from the two terminals on summer Saturdays and fill the waterfront roads by noon. The solstice parade closes Fremont for a June Saturday. The torchlight parade closes downtown for a July Saturday, and the Labor Day festival fills the Seattle Center. A handoff near any of them moves to the daytime or to the next morning.'),
  P('Rain falls from October through May and changes only the loading hour. The rare lowland snow is the problem. The February 2019 storms dropped twenty inches, and the hills shut for a week. The December 2022 ice did the same for three days. The carriers wait in Kent or Fife until the hills thaw. A winter pickup can lose a day or two.'),
  P('The June 2021 heat dome hit one hundred eight degrees, and the carriers ran at dawn. The September 2020 smoke gave the city the worst air in the world for a week. The November 2024 windstorm took the power out across the Eastside for days. Snoqualmie Pass closes a few times each winter. The Spokane lane waits in Ellensburg or North Bend until it reopens.'),
 )+chips(["Downtown","Belltown","South Lake Union","Westlake","Capitol Hill","First Hill","Queen Anne","Seattle Center","Magnolia","Ballard","Fremont","Wallingford","Green Lake","University District","Montlake","Laurelhurst","Northgate","Lake City","Shoreline","West Seattle","Alki","Beacon Hill","Columbia City","Rainier Valley","Georgetown","SoDo","Burien","Tukwila","Renton","Kent","Bellevue","Redmond","Kirkland","Issaquah","Sammamish","Bothell","Lynnwood","Everett","Federal Way","Tacoma","Bainbridge","Vashon"])
 +NOTE('Serving Seattle, the Eastside, and the Sound from Everett to Tacoma. Tell us the neighborhood and the slope, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Seattle?',
 prose(
  L('Open trailers carry most of the cars that leave the Sound, and the table above assumes one.'),
  P('An enclosed trailer keeps off the road spray, the pass grit, and the salt on the coast road. The collectors on Mercer Island and in Medina book one for the show cars. Engineers shipping a new electric car up from California book one too.'),
  P('A commuter car or a second family car goes open and arrives fine. Compare the two on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot in SoDo or at a park and ride, and a signature at delivery. The start date picks the week.'),
  P('Approve the price, and the car is assigned to a carrier already working 5 to the Sound. The lot and the window are set before the day is out. You and the driver circle the car at pickup. Every existing mark is written on the Bill of Lading. Two signatures seal it, and the same sheet is read again when the car comes off.'),
 )+ULI([
  "Personal items out of the cabin and the trunk",
  "Fuel down to about a quarter tank",
  "A photo of each panel and the odometer before the truck comes",
  "One working key to the driver, and a word about any mechanical fault",
  "Aftermarket alarm disarmed",
  "On a hill or downtown, meet the truck at the stadium lots or a park and ride",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Seattle Drivers Choose Ship Guy',
 prose(
  L('We book the carriers already running the coast between California and the Sound. We know which hills a trailer will not climb and where the lots are.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond. Both are on the federal register. Our office is on Westlake Avenue.'),
  P('The coordinator who prices your move is the one who sees the delivery sheet signed. Open, enclosed, and expedited transport are laid out on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Seattle','1700 Westlake Ave N #563A','Seattle, WA 98109','+12068008980','(206) 800-8980','PT',
 '1700+Westlake+Ave+N+%23563A,+Seattle,+WA+98109','Visit Us','Find Ship Guy in Seattle',
 'Our office is on Westlake Avenue on the west shore of Lake Union, south of the Fremont Bridge.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4134.342011235583!2d-122.3395156!3d47.6349255!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x549015495c4ebc37%3A0x600963d2b4191faa!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793103335412!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Seattle to Los Angeles or the Bay Area?","Los Angeles runs eight hundred to eleven hundred fifty dollars for a sedan. That is about eleven hundred thirty-five miles down 5. San Francisco runs six hundred to eight hundred eighty, about eight hundred ten miles on the same road. Portland is a same-day lane and costs the least. Figure 10 to 25 percent more for an SUV or a pickup."),
 ("Can the carrier come to my house on Capitol Hill or Queen Anne?","Rarely. The hills are steep and parked solid, and the towers downtown run on garages. A loaded trailer will not climb the counterbalance on Queen Anne. The driver meets you at the stadium lots in SoDo, at Northgate, or on Mercer Street. The south end, the Eastside subdivisions, and the suburbs toward Everett usually allow the curb."),
 ("Do you ship cars for tech relocations to Seattle and Bellevue?","Yes, every week, and September is the biggest month. The retailer, the software company, and the cloud offices hire from every state on start dates. Most ship a car up 5 from California. Corporate packages usually cover a vehicle, and we supply the paperwork a reimbursed move needs. The handoff works at the stadium lots, at Northgate, or at the Eastgate park and ride."),
 ("Can you deliver on the UW move-in date?","Yes, and the date is later than most campuses. The university runs on quarters, so the cars arrive in the last week of September. They go home in the middle of June. A parent sets it up, and an adult over eighteen signs at a lot off Montlake. The window is pinned to move-in day and travels with it."),
 ("Does Seafair or a Seahawks game affect my pickup?","On the water and in SoDo, yes. Seafair fills the lake for the first weekend of August. The jets close the 90 bridge for an hour at a time. A game day takes the stadium lots. We move a SoDo handoff those days to the morning or to Tukwila. The north end and the Eastside run normally."),
 ("Can you ship a car to or from Bellevue, Tacoma, or Everett?","Yes, and all three price the same as Seattle. Bellevue rides the same carriers across the 90 bridge, and the subdivisions allow the curb. Tacoma rides them off 5 to the south, and the carriers stage in Fife beside it. Everett rides them off 5 to the north, and the plant has lots at every gate. Send the full address for a gated community on the Eastside."),
 ("Is the 520 bridge toll in my price?","Yes. A carrier that crosses the 520 bridge or uses the 99 tunnel pays with a transponder. The toll rides inside the quote. There is no separate line. The 90 bridge, Interstate 5, and 405 carry no toll."),
 ("What happens if lowland snow or a pass closure hits on my pickup day?","Two inches of snow shuts the hills, and the carriers wait in Kent or Fife until they thaw. A winter pickup can slip a day or two, and you hear it from us first. Snoqualmie Pass closes a few times each winter. The Spokane lane waits in Ellensburg or North Bend until it reopens. The Interstate 5 lanes keep running."),
 ("Can you ship a car that arrived at the port or one bound for Alaska?","Yes to both, with one limit. The ocean leg is an international or marine process we do not arrange. Once customs releases an imported car, we move it domestically from the port. For Alaska and Hawaii, we move the car to the dock in Tacoma or Seattle. The barge line or the ferry takes it from there."),
 ("What do you need for a Seattle car shipping quote?","The pickup and delivery addresses, with the neighborhood and the slope named here. The year, make, and model. Whether it runs. Open or enclosed. The week around the start date. Five answers make a full Seattle request, and the number follows the same day."),
]
BODY.append(faq_section(FAQ,'Seattle FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Seattle?','Two minutes on the form above and the lane has a number. Tell us the neighborhood and the week, and a carrier already on 5 takes it.','+12068008980','(206) 800-8980','Get your free Seattle quote'))

build({
 'slug':'auto-transport-seattle-washington',
 'title':'Car Shipping in Seattle, WA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Seattle, WA, on the Sound where Interstate 5 squeezes between the water and the hills. Tech relocations up 5 from California, stadium-lot and park-and-ride handoffs for the hills and the towers, curbside pickups on the Eastside and the south end, UW quarter timing, the base, Seafair, the 520 toll, and the lowland snow. Local office on Westlake Avenue. Free quote.',
 'h1':'Car Shipping in<br>Seattle, <span class="accent">Washington</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Sound, planned around 5, the bridges, the hills, the September start dates, and the passes.',
 'tel':'+12068008980','disp':'(206) 800-8980','brand':'Seattle','keyword':'car shipping in seattle',
 'localterms':['seattle','the sound','interstate 5','floating bridges','westlake avenue','lake union','everett','tacoma','bellevue','redmond','issaquah','ship canal bridge','interstate 90','snoqualmie pass','spokane','520','toll','interstate 405','99 tunnel','express lanes','mercer island','ellensburg','transponder','tukwila','lynnwood','aurora avenue','drawbridges','fremont','ballard','montlake','west seattle bridge','duwamish','rainier avenue','lake city way','15th avenue','airport','509','kent','auburn','fife','stadium lots','sodo','northgate','park and ride','southcenter','eastgate','south kirkland','magnuson park','south lake union','fremont bridge','seven hills','downtown','belltown','towers','garages','capitol hill','first hill','queen anne','counterbalance','mercer street','seattle center','wallingford','green lake','university district','quarter','shoreline','alki','the junction','westwood village','beacon hill','columbia city','rainier valley','light rail','martin luther king','georgetown','burien','renton','kirkland','sammamish','federal way','bainbridge','vashon','kitsap','ferries','terminal lots','portland','boise','sacramento','san francisco','salt lake city','los angeles','denver','phoenix','chicago','montana','engineers','california','retailer','software company','cloud','social','september','start dates','corporate packages','planemaker','machinists','hospital systems','medical campus','traveling nurses','residents','cancer research','scientists','grant cycles','children’s hospital','laurelhurst','quarters','private universities','joint base','naval station','whidbey','air station','orders','port','customs','alaska','hawaii','dock','barge','seafair','jets','game days','football','baseball','soccer','hockey','cruise ships','terminals','solstice parade','torchlight parade','labor day','rain','lowland snow','february 2019','twenty inches','december 2022 ice','heat dome','one hundred eight','september 2020 smoke','november 2024 windstorm','north bend','medina','electric car','bill of lading','fmcsa','surety bond','bothell','magnolia'],
}, BODY, FAQ)
