import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–4 Days","Honest Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Lewiston, Maine','Car shipping in the Twin Cities on the Androscoggin, thirty-five miles up the Turnpike from Portland',
 ['Car shipping in Lewiston runs off the Turnpike exits on the Auburn side of the river. Ship Guy is a licensed auto transport broker with an office on Park Street downtown.',
  'We arrange vetted carriers across Androscoggin County, from Lisbon to Turner and over the river to Auburn. We do not own the trucks.',
  'The Maine Turnpike passes the Twin Cities on the Auburn side. Its exits are Washington Street and the Plourde Parkway. Route 196 is Lisbon Street, the road to Brunswick. Route 4 is Center Street in Auburn, the road to Portland and the lakes. Route 202 runs to Augusta.',
  'This page covers the Turnpike, Lisbon Street, downtown and the mills, the college, Auburn, and the towns around. It also covers the hospitals, the plants, the balloon festival, mud season, the ice, and the lanes.'],
 'Lewiston at a glance',
 ['Most pickups happen within 2 to 4 days. The carriers pass the Twin Cities on every run up the Turnpike. A Lewiston stop joins a truck already headed north.',
  'Portland is forty minutes, and Boston is a same-day haul. Manchester, Hartford, and Albany take a day. New York takes a day too. Philadelphia and Washington take two, and Florida takes four.'],
 'Tell us the side of the river. Downtown, the mill blocks, and the college streets need a meeting spot. The outer streets, Auburn, and the towns around usually allow the curb.'))

BODY.append(sec('The Roads','The Turnpike, Lisbon Street, Center Street, Route 202, and the Bridges',
 prose(
  L('Lewiston sits a mile off the Turnpike. The carriers reach it on the Auburn side without losing much time.'),
  P('The Maine Turnpike runs past the Twin Cities on the Auburn side of the river. The Washington Street exit serves Auburn and the industrial park, and the Plourde Parkway exit serves Lewiston. Every carrier between Portland and Augusta passes both. The tolls are built into every quote.'),
  P('Lisbon Street is Route 196, the main street of downtown and the road southeast to Lisbon and Brunswick. Main Street runs north to Greene as Route 202, and Route 202 continues to Augusta. Sabattus Street is Route 126, the road east to Sabattus. East Avenue and Russell Street cross the east side past the college.'),
  P('Across the river, Center Street is Route 4, the Auburn strip from the mall south to Gray. Court Street runs through downtown Auburn. Minot Avenue is Route 11 and 121 west to Mechanic Falls. Washington Street is Route 202 south past the airport to the Turnpike. The Longley Bridge and the South Bridge cross the Androscoggin between the two downtowns.'),
  P('The carriers come off the Turnpike at Washington Street and the parkway. The mall on Center Street, the parkway, and the riverfront park have the usual meeting lots. The Turnpike is the only toll. The bridges and every city street are free.'),
  P('Our office is on Park Street downtown, across from Kennedy Park and a short walk from Lisbon Street.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown and the Mills, the College Streets, the Outer Streets, Auburn, and the Towns Around',
 prose(
  L('Lewiston is a mill city on one bank and Auburn a shoe city on the other. The streets between the mills are tight.'),
  P('Downtown Lewiston is the Lisbon Street blocks and the mill complex along the canals. A dense grid of three-deckers surrounds Kennedy Park. The streets are narrow and the parking is on both sides. A trailer cannot work the downtown grid. The driver meets you at the riverfront park, at the mill lots, or on the parkway. The streets up the hill toward the college are the same.'),
  P('The college sits above downtown on a campus of its own. The handoff happens at a campus lot. The outer streets along Sabattus, East Avenue, and Pleasant Street are postwar grids with wider roads. The curb works on most of them. The subdivisions off Pond Road and Old Greene Road allow the curb.'),
  P('Auburn across the river has its own downtown on Court Street and the mall strip on Center Street. The industrial park sits by the Turnpike. New Auburn below the falls is a tight old grid, and the handoff moves to the main road. The streets off Minot Avenue and around Lake Auburn are wider, and the truck reaches the curb.'),
  P('Lisbon and Lisbon Falls down Route 196 are mill villages with lots on the main road. Sabattus, Greene, and Turner to the north are farm towns. The driver meets you on the state route. Poland and the lakes to the west run on a summer clock. Mechanic Falls and Minot are the same. All of them price the same as Lewiston, and so does Auburn.'),
 )))

ROUTES=[("Portland, ME","I-95 · ~35 mi","Same day","$130–$210"),("Boston, MA","I-95 · ~145 mi","Same day","$200–$310"),
 ("Manchester, NH","US-202/I-93 · ~120 mi","1 day","$220–$340"),("Hartford, CT","I-95/I-84 · ~235 mi","1 day","$260–$390"),
 ("Albany, NY","I-95/I-90 · ~295 mi","1 day","$270–$400"),("New York, NY","I-95 · ~355 mi","1 day","$340–$490"),
 ("Philadelphia, PA","I-95 · ~445 mi","1–2 days","$400–$570"),("Washington, DC","I-95 · ~585 mi","2 days","$460–$660"),
 ("Charlotte, NC","I-95/I-85 · ~935 mi","3 days","$700–$980"),("Orlando, FL","I-95 · ~1,435 mi","4 days","$900–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Lewiston Car Shipping Lanes and Estimated Costs',
 'The lanes Androscoggin County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates out of Lewiston, sedan that starts and drives, open trailer. Figure 10 to 25 percent more for an SUV or a pickup and more for enclosed. Turnpike tolls are inside the number. The season and the trucks on the Maine run that week fix the final figure.',
 prose(
  P('Lewiston prices with Portland on every lane, because the carriers pass the Turnpike exits on the same run. The Boston lane runs most days. The New York and Philadelphia lanes run on the trucks that come this far north, most weeks. The Florida lane climbs in October with the snowbirds and eases in April.'),
  P('Manchester prices over Boston on fewer miles, because fewer trucks cross New Hampshire that way. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospitals, the College, the Plants, the Distribution Center, and the Mill Tenants',
 prose(
  L('Lewiston relocates nurses, professors, plant engineers, and warehouse managers. The two hospitals move more people than anyone.'),
  P('The medical center on Main Street is the trauma center for central Maine. The second hospital sits a few blocks away. Between them they hire nurses on contracts all year and take residents each June. Physicians come with a closing date and a second car. The paperwork for a reimbursed move comes from us.'),
  P('The college above downtown brings cars in each late August and sends them home each May. A parent ships the car from New York, Connecticut, or farther. An adult signs at a campus lot. The faculty arrive each summer. The community college in Auburn and the university campus on the river run the same calendar.'),
  P('The consumer-products plant in Auburn and the forming plants by the Turnpike move engineers on program schedules. The distribution center in Lewiston brings in managers from every state. The promotional-products company and the bank headquartered downtown relocate staff on their own calendars. The mill tenants move small teams in as the old buildings fill.'),
  P('Families priced out of Portland buy in Lewiston and Auburn and ship a second car behind the move. The lake towns to the west run on a summer clock. The interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page. Ship Guy is a private broker with no military connection, and Guard timing is on the <a href="military-car-shipping.html">military</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Balloon Festival, the Dempsey Challenge, Move-In Week, the Ice Storm, and Mud Season',
 prose(
  L('Lewiston runs on a balloon weekend in August, a cycling weekend in October, and a long winter.'),
  P('The balloon festival fills the riverfront parks on both banks for a weekend in August. The launches go at dawn and dusk, and the streets by the river close. A pickup near the river that weekend moves to the mall or to the parkway. The cycling challenge in October does the same to the riverfront and the roads north of town.'),
  P('Move-in week at the college brings a thousand cars up the hill in late August. The streets around the campus fill, and the handoff moves to a campus lot. The Fourth of July fills the riverfront for the fireworks. The Moxie festival in Lisbon Falls closes the village on a July Saturday. A handoff near any of them moves to the daytime.'),
  P('The 1998 ice storm took the power out across the Twin Cities for two weeks. The carriers parked in Portland for most of it. Seventy inches of snow is a normal winter here, and the Turnpike shuts a few times a season. A pickup in a storm week can slip a day or two, with a call from us first. In a wet April the river climbs into the low streets, as it did in 1987.'),
  P('Mud season is the local wrinkle. From March into May, the towns post weight limits on the back roads. A loaded carrier cannot use them. The driver meets you on a paved state route or at a lot in town. Frost heaves follow the posted roads into June. Summer is the easy season, and the carriers run on time.'),
 )+chips(["Downtown","Lisbon Street","Kennedy Park","The Mills","Canal Street","Bates","College Street","Russell Street","Sabattus Street","East Avenue","Pleasant Street","Main Street","Pond Road","Old Greene Road","Auburn","Court Street","Center Street","Auburn Mall","New Auburn","Minot Avenue","Lake Auburn","Washington Street","Industrial Park","Lisbon","Lisbon Falls","Sabattus","Greene","Turner","Poland","Mechanic Falls","Minot","Durham"])
 +NOTE('Serving Lewiston, Auburn, and all of Androscoggin County, mill block or farm road. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Lewiston?',
 prose(
  L('Nine cars in ten leave Androscoggin County on an open trailer. The table above is priced that way.'),
  P('An enclosed trailer shuts out the salt, the slush, and the gravel. Parents shipping a car to the college from a long way off book one. Snowbirds with a new car book one for the Florida run.'),
  P('A daily driver or a plant truck goes open and comes off the trailer fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the trade-off.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the mall or the riverfront park, and a signature at the far end. The next truck up the Turnpike sets the week.'),
  P('Accept the price, and we add the car to a carrier already making the run north from Portland. The lot and the window reach you once the truck is set. At pickup, the driver inspects the car with you and marks every blemish on a Bill of Lading. You both sign, and the delivery is checked against it.'),
 )+ULI([
  "Clear out the cabin, the trunk, and the glovebox",
  "Run the fuel down to about a quarter tank",
  "Photograph each panel and the odometer before the truck comes",
  "Hand over one working key and describe any fault",
  "Switch off any aftermarket alarm",
  "Downtown or by the college, meet the truck at the riverfront park or a campus lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Lewiston Drivers Choose Ship Guy',
 prose(
  L('We add the Twin Cities stop to the carriers already headed up the Turnpike. We plan around the balloons, the ice, and mud season.'),
  P('Ship Guy is an active FMCSA broker with a $75,000 surety bond on file. The federal register lists both. Our office is on Park Street downtown.'),
  P('The person who quotes the move is the person on the phone until it is delivered. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Lewiston','75 Park St #452A','Lewiston, ME 04240','+12079948972','(207) 994-8972','ET',
 '75+Park+St+%23452A,+Lewiston,+ME+04240','Visit Us','Find Ship Guy in Lewiston',
 'Our office is on Park Street downtown, across from Kennedy Park and a short walk from Lisbon Street.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4406.201229257195!2d-70.2167144!3d44.0970458!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cb26bbe789de537%3A0x9aef33cf3a5a6665!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025058459!5m2!1sen!2sus', alt=True))

FAQ=[
 ("Why does a Lewiston pickup take two to four days?","Because the carriers come up the Turnpike from Portland and Boston on a run. A Lewiston stop joins a truck already making it. That is two to four days in a normal week. A flexible date range puts you on the next truck north. A rigid date is possible on the Portland and Boston lanes. It narrows the pool and can raise the price."),
 ("How much does it cost to ship a car from Lewiston to Boston or New York?","Boston runs two hundred to three hundred ten dollars for a sedan. That is about one hundred forty-five miles down the Turnpike and 95. New York runs three hundred forty to four hundred ninety, about three hundred fifty-five miles the same way. Portland is forty minutes away and the least expensive lane. Count on 10 to 25 percent more for an SUV or a pickup."),
 ("Can the carrier come to my street downtown or by the college?","Usually not. The downtown grid around Kennedy Park is narrow three-deckers with cars on both sides. The college streets are the same. The driver meets you at the riverfront park, at the mill lots, or at a campus lot. The outer streets, Auburn, and the towns around usually allow the curb."),
 ("Can you ship my student’s car to Bates?","Yes, and it is the move we make most each August. Cars come from New York, Connecticut, and farther. A parent books, and an adult signs at a campus lot. The campus streets fill during move-in week, so the handoff happens at a lot. The cars go home the same way in May. Book a couple of weeks ahead, because the late-August trucks fill fast."),
 ("Does the balloon festival affect my pickup?","Along the river, yes. The festival fills the riverfront parks on both banks for a weekend in August. The streets by the river close for the launches. We move a pickup near the river that weekend to the mall or to the parkway. The rest of the Twin Cities runs normally."),
 ("Can you ship a car to or from Auburn, Lisbon, or Poland?","Yes, and all three price the same as Lewiston. Auburn rides the same carriers off the Turnpike at Washington Street. The mall lot works for a handoff. Lisbon rides them down Route 196, and Poland rides them off Route 26. In mud season the driver meets you on the paved state route."),
 ("What happens if an ice storm or a blizzard hits on my pickup day?","The carriers park in Portland until the Turnpike reopens. A winter pickup can slip a day or two. You hear from us before it does. The 1998 ice storm cost two weeks, but a normal storm costs a day. In a wet April the river floods the low streets, and a pickup there moves up the hill."),
 ("Can you ship a car that does not run from Lewiston?","Yes. We send a carrier with a winch, and the loading time is in the quote from the start. The mall lot on Center Street or the riverfront park gives the driver level ground. Tell us whether the car rolls, steers, and brakes."),
 ("What is mud season, and does it change my pickup?","From March into May, the towns post weight limits on the back roads as the frost comes out. A loaded carrier cannot use them. A pickup on a posted road meets the truck on a paved state route or in town. The Turnpike, Lisbon Street, and Center Street never post. It is a normal part of spring here."),
 ("What do you need for a Lewiston car shipping quote?","Where the car is and where it goes, with the side of the river here. What it is, year through model. Whether it starts. Open or enclosed. A range of dates rather than one, since the trucks come north on a run. Five answers, and the Lewiston number is back within the day."),
]
BODY.append(faq_section(FAQ,'Lewiston FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Lewiston?','The form above prices the lane in two minutes. Give us the side of the river and a range of dates. The next carrier up the Turnpike takes it.','+12079948972','(207) 994-8972','Get your free Lewiston quote'))

build({
 'slug':'auto-transport-lewiston-maine',
 'title':'Car Shipping in Lewiston, ME — Auto Transport | Ship Guy',
 'meta':'Car shipping in Lewiston, ME, the Twin Cities on the Androscoggin a mile off the Turnpike. Honest two-to-four-day pickups, hospital and plant relocations, Bates move-in, downtown and mill-block meeting spots, Auburn and the outer streets curbside, the balloon festival, the 1998 ice storm, and mud season. Local office on Park Street. Free quote.',
 'h1':'Car Shipping in<br>Lewiston, <span class="accent">Maine</span>',
 'lede':'Open, enclosed, and expedited auto transport across Androscoggin County, planned around the Turnpike, the river, the college calendar, and the winter.',
 'tel':'+12079948972','disp':'(207) 994-8972','brand':'Lewiston','keyword':'car shipping in lewiston',
 'localterms':['lewiston','auburn','twin cities','androscoggin','turnpike','washington street','plourde parkway','lisbon street','route 196','main street','route 202','sabattus street','route 126','east avenue','russell street','center street','route 4','court street','minot avenue','longley bridge','south bridge','downtown','kennedy park','park street','mills','canals','three-deckers','riverfront park','college','campus','pleasant street','pond road','old greene road','auburn mall','industrial park','new auburn','lake auburn','lisbon','lisbon falls','sabattus','greene','turner','poland','lakes','mechanic falls','minot','gray','medical center','trauma','hospital','nurses','residents','professors','community college','university campus','consumer-products plant','forming plants','distribution center','promotional-products','bank','mill tenants','balloon festival','launches','cycling challenge','move-in week','fourth of july','moxie','1998 ice storm','snow','1987','flood','mud season','posted','frost heaves','portland','boston','manchester','hartford','albany','new york','philadelphia','washington','charlotte','orlando','augusta','brunswick'],
}, BODY, FAQ)
