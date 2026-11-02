import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Salem, Oregon','Car shipping in the capital, an hour down the valley from Portland and on every truck’s way to California',
 ['Car shipping in Salem runs on Interstate 5 along the east side of the city. Ship Guy is a licensed auto transport broker with an office on Commercial Street downtown.',
  'We book vetted carriers across Salem, from the Capitol Mall to West Salem and out to Keizer. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 5 runs along the east side with the Kuebler, Mission Street, Market Street, and Salem Parkway exits. Highway 22 crosses the city from the coast to the Cascades. Highway 99E is Commercial Street and Portland Road. Lancaster Drive carries the east side, and the two bridges carry West Salem.',
  'This page covers 5, 22, 99E, Lancaster, downtown, the Capitol Mall, West Salem, and Keizer. It also covers the state, the hospital, the campus, the fair, the ice storms, and the smoke.'],
 'Salem at a glance',
 ['Most pickups happen within 1 to 3 days. The Portland pool is an hour north, and the 5 carriers pass between Seattle and California all day. Half of them stop at the Kuebler exit.',
  'Portland, Eugene, and Seattle ride a single day on the truck. Spokane and Boise take a day. Sacramento and San Francisco take one to two, and Los Angeles takes two to three.'],
 'Tell us the neighborhood. Downtown, the Capitol Mall, Fairmount, and the West Salem hills meet the truck on a main road. Keizer, South Gateway, the Lancaster grids, and the subdivisions off Kuebler usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 5, Highway 22, Highway 99E, Lancaster Drive, Kuebler Boulevard, Commercial Street, Mission Street, and the Bridges',
 prose(
  L('Salem is a flat valley city with one interstate on its edge and a river through its middle. A carrier picks its exit and never crosses downtown.'),
  P('Interstate 5 runs along the east side of the city. The Kuebler exit serves the south, and Mission and Market serve the middle. The Salem Parkway serves downtown and Keizer. Portland is forty-seven miles north and Eugene sixty-five miles south. The road is the Seattle-to-California lane, and every car hauler on the coast runs it. The valley fog slows it on winter mornings. The ice closes it a day or two each winter.'),
  P('Highway 22 crosses the city as Mission Street and runs east to Stayton and the pass. West of the river it runs to Dallas and the coast. Highway 99E is Commercial Street through downtown and the south strip, and Portland Road through the north. Lancaster Drive is the east side strip from the mall to the fairgrounds. Kuebler Boulevard loops the south. The Marion and Center Street bridges carry West Salem over the river, and both back up at five.'),
  P('The carriers come off 5 at Kuebler or Market Street. The big-box lots at Keizer Station are the usual meeting spot. The mall lots on Lancaster work too. So do the lots on Commercial Street south of downtown and the fairgrounds lots outside the fair. The Portland airport is an hour up 5 for a fly-and-ship.'),
  P('Our office is on Commercial Street downtown, a few blocks from the Capitol and Riverfront Park.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Capitol Mall, Grant, Highland, Fairmount, Candalaria, South Gateway, Lancaster, Four Corners, West Salem, and Keizer',
 prose(
  L('Salem is a small downtown grid, old neighborhoods on both sides of it, and subdivisions in every direction. The truck meets the old neighborhoods on a main road.'),
  P('Downtown runs from the river east to the Capitol, one-way streets and the state office blocks. The driver meets you at the Riverfront Park lots or on Commercial Street. The Capitol Mall and the university across from it are closed streets and lawns. The handoff moves to State Street. Grant and Highland north of downtown are old grids of small houses with alley garages. The curb works on some blocks, and the driver meets you on Broadway where it does not.'),
  P('Fairmount and the Gaiety Hill blocks south of downtown are the old money. The big houses sit on a hill above the park. The streets are narrow and tree-lined, and the handoff moves to Commercial Street. Candalaria beyond them is winding and hilly, and the handoff moves to Liberty Road. South Gateway and the subdivisions off Kuebler are wide and new, and the truck reaches the curb.'),
  P('The Lancaster grids on the east side are plain postwar blocks where the curb works. Four Corners and the blocks off Cordon Road are the same. West Salem across the river climbs the hills off Wallace Road. The lower grids allow the curb, and the hill streets ice first and meet the truck on Wallace. Keizer to the north is wide grids and cul-de-sacs, and the curb works nearly everywhere.'),
  P('Keizer, Turner, and Silverton ship with the same trucks and price the same as Salem. So do Dallas, Monmouth, and Independence across the river. Woodburn is twenty minutes north and prices with the city. Albany and Corvallis ride the same 5 carriers and add a few hours.'),
 )))

ROUTES=[("Portland, OR","I-5 · ~47 mi","Same day","$130–$220"),("Eugene, OR","I-5 · ~65 mi","Same day","$140–$230"),
 ("Seattle, WA","I-5 · ~220 mi","Same day","$240–$360"),("Spokane, WA","I-5/I-84 · ~400 mi","1 day","$340–$490"),
 ("Boise, ID","I-5/I-84 · ~480 mi","1 day","$400–$570"),("Sacramento, CA","I-5 · ~535 mi","1–2 days","$450–$650"),
 ("San Francisco, CA","I-5 · ~590 mi","1–2 days","$490–$700"),("Salt Lake City, UT","I-84 · ~810 mi","2 days","$580–$840"),
 ("Los Angeles, CA","I-5 · ~920 mi","2–3 days","$680–$950"),("Phoenix, AZ","I-5/US-93 · ~1,300 mi","3 days","$900–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Salem Car Shipping Lanes and Estimated Costs',
 'The lanes mid-valley cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Salem, sedan that runs, open trailer. An SUV or a pickup runs 10 to 25 percent above these, and enclosed runs above that. The week you pick and the carriers on 5 that week set the real figure.',
 prose(
  P('Salem prices like a Portland suburb on the short lanes. On the long ones it prices as a stop on the 5 pool. The Portland and Eugene lanes ride 5 and fill every day. The Seattle lane rides 5 north through the Portland pool. The California lanes ride 5 over the Siskiyou, and the pass sets the winter days. The Arizona lane fills each October with the snowbirds.'),
  P('A session start in January or the late August move-in means a busy week. Size, condition, and timing each move the figure, and the <a href="car-shipping-cost.html">cost guide</a> says how much.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State, the Hospital, the University, the Food Plants, the Chip Plant, the Prison, the Colleges, and the Retirees',
 prose(
  L('Salem relocates state employees, nurses, professors, food plant managers, and retirees. The state moves the most.'),
  P('State government fills the Capitol Mall and the office blocks around it. It is the largest employer in the city. The agencies move staff in on start dates all year. The legislature brings members and staff to town for a long session in odd years. Even years bring a short one. The handoff for all of them happens on State Street or at the Riverfront Park lots. If the state or an employer reimburses the shipment, the paperwork comes from us.'),
  P('The hospital on Winter Street brings residents each June and hires traveling nurses year round. The university across from the Capitol takes student cars in late August and sends them home in May. The community college on Lancaster and the college on the southeast side do the same. A parent sets it up, and someone over eighteen signs at the lot. The state university in Monmouth across the river follows the same calendar.'),
  P('The food plants on the north and east sides move managers on contract dates. The kettle chip plant does the same. The state hospital on Center Street and the prison on State Street relocate staff on start dates. There is no base in the city. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line.'),
  P('Retirees come down from Portland for the prices and the quiet. Many of them leave for Arizona each October and come back in April. The snowbird lane fills the fall.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The State Fair, the Art Fair, the Session, Move-In Week, the Cherry Trees, the Rain, the Ice, the Floods, and the Smoke',
 prose(
  L('Salem runs on a state calendar and a fair calendar. The weather problem is a valley that holds whatever arrives in it.'),
  P('The state fair fills the fairgrounds on 17th Street for eleven days through Labor Day. It takes Lancaster with it. The art fair fills the park on the hill for a weekend in July. The session fills the Capitol Mall from January. Move-in week in late August fills the blocks around the university. The cherry trees on the Capitol Mall draw a crowd for two weeks in March. Book three weeks ahead for a date in the last week of August.'),
  P('The rain runs from October into May, and a carrier loads in it. The ice is the real problem. The February 2021 storm put an inch of ice on the city. Half of it stayed dark for ten days. The January 2024 storm did it again for three. The carriers wait in Portland until the roads thaw. A storm shifts a pickup to the first clear morning, and the figure holds. The West Salem hills and the Candalaria hills ice first.'),
  P('The river floods in a warm winter rain. The February 1996 flood put the Willamette over Riverfront Park and the low streets of the north end. A handoff near the river moves to Lancaster for a day. The September 2020 fires burned the canyon east of the city. Salem had the worst air in the world for a week. The carriers kept moving, and the handoffs moved indoors.'),
  P('The June 2021 heat dome put the city at one hundred seventeen degrees, a record for the state. A carrier does not load in that, and the day moves to dawn. Most summers are dry and mild, and the afternoon is the loading hour.'),
 )+chips(["Downtown","The Capitol Mall","State Street","Riverfront Park","Grant","Highland","Englewood","Fairmount","Gaiety Hill","Bush’s Pasture","Candalaria","Morningside","South Gateway","Kuebler","Sunnyslope","Lancaster","Four Corners","East Salem","Hayesville","West Salem","Wallace Road","Keizer","Keizer Station","Turner","Silverton","Stayton","Dallas","Monmouth","Independence","Woodburn"])
 +NOTE('Serving Salem and the whole mid-valley, Fairmount hill or Keizer cul-de-sac. Tell us the neighborhood and say whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Salem?',
 prose(
  L('Most of the valley ships open, and the figures above assume an open trailer.'),
  P('Enclosed keeps the winter rain, the fir needles, and the ash of a smoke year off the paint. Fairmount collectors book it, and so do the retirees moving a car they restored. Ahead of an ice storm, the car rides the first truck with a slot. We tell you so.'),
  P('A commuter car rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages show what separates the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, then a lot at Keizer Station, then a signature at the far end. The start date or the move-in picks the week.'),
  P('Once you approve the figure, the car goes to a carrier already running 5 that week. The lot and the window are agreed that afternoon. The driver walks the car with a camera at pickup and fills in the Bill of Lading. You initial it, and that sheet settles any question at delivery.'),
 )+ULI([
  "Personal items out of the cabin and the trunk",
  "A quarter tank of fuel or less",
  "Photos of each side and the odometer before the truck comes",
  "A working key and a note about anything that does not work",
  "Add-on alarms switched off",
  "Downtown, on the Fairmount hill, or in the West Salem hills, we meet on a main road",
 ])+prose(P('The steps are on the <a href="how-it-works.html">how it works</a> page, and the day-of list is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Salem Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 5 every day. We know which week the state hires and which week the fair takes the east side.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on Commercial Street downtown.'),
  P('The coordinator who quotes your move is the one who answers until it is delivered. The <a href="services.html">services</a> page lays out open, enclosed, and expedited.'),
 )))

BODY.append(office('Salem','216 Commercial St NE #435','Salem, OR 97301','+15037826495','(503) 782-6495','PT',
 '216+Commercial+St+NE+%23435,+Salem,+OR+97301','Visit Us','Find Ship Guy in Salem',
 'Our office is on Commercial Street downtown, a few blocks from the Capitol and Riverfront Park.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3485.995555185729!2d-123.03947790000001!3d44.941682500000006!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54bfff4748ae01d9%3A0xd5982271de946055!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793631398690!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Salem to California or Seattle?","Sacramento runs four hundred fifty to six hundred fifty dollars for a sedan. That is about five hundred thirty-five miles down 5. Seattle runs two hundred forty to three hundred sixty, about two hundred twenty miles north. Portland, an hour up the interstate, is the lowest lane on the table. An SUV or a pickup runs 10 to 25 percent more."),
 ("Do you ship cars for state employees?","Yes, in every season. The agencies move staff in on start dates, and the session brings members and staff each January. The handoff happens on State Street or at the Riverfront Park lots. If the state reimburses the move, the paperwork comes from us."),
 ("Can the carrier come to my street in Fairmount or West Salem?","West Salem, yes, in the lower grids off Wallace Road. The hill streets ice first and meet the truck on Wallace. Fairmount, no. The streets are narrow and tree-lined, and the driver meets you on Commercial Street. Keizer, South Gateway, Lancaster, and the subdivisions off Kuebler usually allow the curb."),
 ("Can you deliver on a Willamette or Chemeketa move-in date?","Yes. The university takes cars in late August, and the community college follows the same week. A parent books, and an adult signs at the lot. The blocks around the Capitol are full that week, so the meeting point is the Riverfront Park lots. The window is set by the date."),
 ("Does the state fair affect my pickup?","Yes, for eleven days through Labor Day. The fair takes the fairgrounds lots and fills Lancaster and 17th Street. The handoff moves to Keizer Station that week. The rest of the city runs normally, and the Kuebler exit is unaffected."),
 ("Can you ship a car to or from Keizer, Woodburn, or Corvallis?","Yes. Keizer, Turner, and Silverton ride the same carriers and price the same as Salem. Dallas, Monmouth, and Independence do too. Woodburn is twenty minutes north and prices with the city. Corvallis and Albany ride the 5 carriers and add a few hours on the day."),
 ("What happens if an ice storm hits on my pickup day?","The truck waits in Portland until the roads thaw, usually a day or two. We call as soon as the forecast turns. The pickup takes the first clear morning, and the figure does not change. A January date wants a flexible week."),
 ("Does the smoke in fire season delay a shipment?","Rarely. The carriers keep moving through the smoke, and the handoff moves indoors or to a garage entrance. A closure on 5 or Highway 22 for a fire is the exception. We call the moment one posts. The September 2020 week was the worst, and the trucks still ran."),
 ("Can you ship a car that does not run from Salem?","Yes. A winch truck takes it, and the loading time is priced in from the start. The Keizer Station lots and the mall lots on Lancaster are flat. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Salem car shipping quote?","Where it starts and ends, with the neighborhood. The year, make, and model, and whether it runs. Open or enclosed, and the week around the start date or the move. That is enough for a Salem figure the same day."),
]
BODY.append(faq_section(FAQ,'Salem FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Salem?','Two minutes on the form above gets your lane a Salem figure. Name the neighborhood and the week, and a carrier already running 5 takes it.','+15037826495','(503) 782-6495','Get your free Salem quote'))

build({
 'slug':'auto-transport-salem-oregon',
 'title':'Car Shipping in Salem, OR — Auto Transport | Ship Guy',
 'meta':'Car shipping in Salem, OR, the capital on Interstate 5. State and hospital relocations, campus move-in, main-road handoffs for downtown, Fairmount, and the West Salem hills, curbside pickups in Keizer and South Gateway, the state fair, the ice storms, and the smoke. Local office on Commercial Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Salem, <span class="accent">Oregon</span>',
 'lede':'Open, enclosed, and expedited auto transport across Salem and the mid-valley, planned around 5, Highway 22, the state calendar, the campus dates, the fair, and the winter ice.',
 'tel':'+15037826495','disp':'(503) 782-6495','brand':'Salem','keyword':'car shipping in salem',
 'localterms':['salem','capital','portland','california','interstate 5','highway 22','99e','commercial street','portland road','lancaster','kuebler','mission street','market street','salem parkway','bridges','downtown','capitol mall','state street','riverfront park','grant','highland','fairmount','gaiety hill','candalaria','south gateway','four corners','cordon road','west salem','wallace road','keizer','keizer station','turner','silverton','dallas','monmouth','independence','woodburn','albany','corvallis','eugene','seattle','spokane','boise','sacramento','san francisco','salt lake','los angeles','phoenix','arizona','snowbirds','siskiyou','fog','state employees','agencies','session','legislature','hospital','winter street','residents','traveling nurses','university','community college','student','food plants','kettle chip','state hospital','prison','retirees','state fair','17th street','art fair','move-in','cherry trees','rain','ice','february 2021','january 2024','february 1996','flood','willamette','september 2020','fires','canyon','smoke','june 2021','heat dome','one hundred seventeen','fir needles','ash','bill of lading','fmcsa','winch','mall','fairgrounds','broadway','liberty road','stayton','pass'],
}, BODY, FAQ)
