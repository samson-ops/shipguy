import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Memphis, Tennessee','Car shipping in the city that moves more freight than any in the country, on the bluff above the river',
 ['Car shipping in Memphis runs on Interstates 40 and 55 across the river and the 240 loop. Ship Guy is a licensed auto transport broker with an office on Monroe Avenue by the medical district.',
  'We book vetted carriers across Memphis, from Midtown to Collierville and across the line to Southaven. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 40 crosses the river on the new bridge and leaves east for Nashville. Interstate 55 crosses on the old bridge and runs south into Mississippi. Interstate 240 loops the south and east sides, and 269 loops farther out. Poplar Avenue, Lamar Avenue, and Elvis Presley Boulevard carry the rest.',
  'This page covers 40, 55, 240, Poplar, Lamar, downtown, Midtown, East Memphis, and the suburbs. It covers the cargo hub, the rail yards, the hospitals, the campus, the Navy base, and the ice.'],
 'Memphis at a glance',
 ['Most pickups happen within 1 to 3 days. More trucks pass through Memphis than any city its size, and the car haulers are among them. The 40 and 55 carriers cross the river all day.',
  'Little Rock, Nashville, Jackson, and Birmingham ride a single day on the truck. St. Louis and Atlanta take a day. Louisville, Dallas, and Chicago take one to two, and Houston takes two.'],
 'Tell us the neighborhood. Downtown, Central Gardens, Cooper-Young, and Harbor Town meet the truck on a main road. East Memphis, Cordova, Germantown, Collierville, and the Mississippi suburbs usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 40, Interstate 55, Interstate 240, Interstate 269, Poplar Avenue, Lamar Avenue, Elvis Presley Boulevard, and the Bridges',
 prose(
  L('Memphis is a trucking city before it is anything else, and the roads were built for trailers. A carrier picks its bridge and its loop and goes anywhere.'),
  P('Interstate 40 comes in from Little Rock on the new bridge. That bridge closed for three months in 2021 when a crack was found. It runs across the north side and leaves east for Jackson and Nashville. Interstate 55 comes in on the old bridge beside it and runs south into Mississippi. The two bridges are the only crossings for a hundred miles. A closure sends every truck to the other one.'),
  P('Interstate 240 loops the south and east sides from the airport around to the 40 split. Interstate 269 loops farther out through DeSoto County and Collierville. Poplar Avenue runs from downtown through Midtown and East Memphis to Germantown. It is the spine of the east side. Lamar Avenue is Highway 78, the truck road to the cargo hub and Mississippi. Elvis Presley Boulevard runs south through Whitehaven past the mansion. Summer Avenue, Union Avenue, and Winchester Road carry the rest.'),
  P('The carriers come off 240 at Poplar or Walnut Grove and off 40 at Sycamore View. The big-box lots on Germantown Parkway are the usual meeting spot. The mall lots in Southaven work too. So do the lots at the fairgrounds in Midtown and the lots on Winchester near the airport. The airport cell lot works for a fly-and-ship.'),
  P('Our office is on Monroe Avenue at the east edge of downtown, by the medical district.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Harbor Town, Midtown, Central Gardens, Cooper-Young, East Memphis, the University District, Whitehaven, Frayser, Cordova, Germantown, Collierville, and DeSoto County',
 prose(
  L('Memphis is an old city at the bluff, a leafy middle, and suburbs that run into another state. The truck meets the old city on a main road.'),
  P('Downtown runs along Main Street from the Pinch to South Main, trolley tracks and one-way streets. The driver meets you at the garage entrances on Union or at the lots by the arena. Harbor Town on Mud Island is one bridge and narrow lanes. The handoff happens on the island’s main road. Midtown is the city’s heart. Central Gardens is its old money, big houses on narrow streets under oaks. A trailer does not enter. The handoff moves to Union Avenue or the fairgrounds lots.'),
  P('Cooper-Young and the blocks around Overton Park are bungalows on tight grids with cars on both curbs. The driver meets you on Cooper Street or at the park lots. East Memphis along Poplar is ranch houses on wide streets, and the curb works. The university district around the campus is the same, except for move-in week. Whitehaven south of the airport is wide grids, and the curb works on most of it.'),
  P('Frayser and Raleigh north and east of the loop are postwar grids where the curb usually works. Cordova off Germantown Parkway is subdivisions from the nineties on, wide streets and cul-de-sacs. Germantown and Collierville east of the loop are the same with bigger lots. The gated sections meet the truck at the gate. Southaven, Olive Branch, and Horn Lake across the state line are the fastest-growing suburbs in the metro. The curb works nearly everywhere.'),
  P('Germantown, Collierville, and Bartlett ship with the same trucks and price the same as Memphis. So do the Mississippi suburbs and West Memphis across the river. Millington is twenty minutes north and prices with the city. Jackson is an hour east on 40.'),
 )))

ROUTES=[("Little Rock, AR","I-40 · ~135 mi","Same day","$170–$280"),("Nashville, TN","I-40 · ~210 mi","Same day","$230–$350"),
 ("Jackson, MS","I-55 · ~210 mi","Same day","$230–$350"),("Birmingham, AL","US-78/I-22 · ~240 mi","Same day","$230–$350"),
 ("St. Louis, MO","I-55 · ~285 mi","1 day","$280–$420"),("Atlanta, GA","I-22/I-20 · ~390 mi","1 day","$340–$490"),
 ("Louisville, KY","I-40/I-65 · ~380 mi","1 day","$340–$490"),("Dallas, TX","I-40/I-30 · ~450 mi","1 day","$400–$580"),
 ("Chicago, IL","I-55/I-57 · ~530 mi","1–2 days","$450–$650"),("Houston, TX","I-55/I-20/I-45 · ~580 mi","2 days","$480–$700")]
BODY.append(rate_table('Lanes &amp; Costs','Memphis Car Shipping Lanes and Estimated Costs',
 'The lanes Mid-South cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Memphis for a running sedan on an open trailer. SUVs and pickups cost 10 to 25 percent more, and enclosed costs more still. The week you offer and the carriers crossing the river that week set the final figure.',
 prose(
  P('Memphis prices like the freight hub it is, which means the lanes are long and full. The Dallas lane rides 40 and 30 and fills every day. The Chicago lane rides 55 and 57 through the Delta and Illinois. The Atlanta lane rides 22 to Birmingham and 20. The Florida lane fills each fall with the retirees, and the Texas lane fills with the warehouse transfers.'),
  P('A start date at the hub in November or the late August move-in means a busy week. How size, condition, and the date range shape the figure is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Cargo Hub, the Rail Yards, the Children’s Hospital, the Medical District, the Campus, the Navy Base, the New Truck Plant, and the Suburbs',
 prose(
  L('Memphis relocates pilots, warehouse managers, physicians, researchers, professors, and sailors. The cargo hub moves more households than anyone else.'),
  P('The overnight shipper’s hub at the airport moves more air cargo than almost any airport in the world. The company is the largest employer in the city. It relocates pilots, managers, and engineers on start dates all year, with the November peak. The warehouses along Lamar and around the hub move managers the same way. The five railroads and the river port move crews on bid cycles. If the company or an employer reimburses the shipment, the paperwork comes from us.'),
  P('The children’s research hospital downtown brings physicians and researchers from every continent on grant cycles. The medical district beside it holds the university health campus and three hospital systems. They bring residents each June. The university on Central Avenue takes student cars in late August, and the college in Midtown follows. A parent books, and an adult signs at the handoff. The cars leave in May.'),
  P('The Navy’s personnel command base in Millington rotates sailors and civilians on orders. Housing sits behind the gate, so the truck meets you outside it or on Navy Road. The Navy moves one car on orders, and the second one usually rides with us. Ship Guy is a private broker with no tie to the Navy. The <a href="military-car-shipping.html">military</a> page explains how orders set the timing.'),
  P('The new truck plant an hour up 40 at Stanton is hiring thousands. The families are landing in Bartlett, Arlington, and the suburbs. Retirees leave for Florida each November. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Memphis in May, Elvis Week, Move-In Week, the Classic, the Peak Season, the Ice, the River, the Tornadoes, and the Heat',
 prose(
  L('Memphis runs on a freight calendar and a music calendar. The weather problem is ice that arrives twice a decade and stays a week.'),
  P('Memphis in May fills the riverfront and the fairgrounds through the month. The barbecue weekend closes the streets around it. Elvis Week fills Whitehaven in August, and the candlelight vigil closes the boulevard for a night. Move-in week in late August fills the blocks around the campus. The classic fills the stadium and the fairgrounds in September. The peak season at the hub runs from November into January. The roads around the airport fill with trailers at night. Book three weeks ahead for a date in that stretch.'),
  P('Ice is the weather problem. The February 1994 storm put the city in the dark for a week. The February 2022 storm did it for days. The carriers wait in Jackson or Little Rock until the roads thaw. The windstorm of July 2003 the city calls Hurricane Elvis took the power from three hundred thousand homes. A storm shifts a pickup to the first clear morning, and the figure holds.'),
  P('The river crested at forty-eight feet in May 2011 and put Mud Island and the north end under. A handoff near the river moves to Midtown for a week. The February 2008 tornadoes crossed Hickory Hill and the east side. A tornado watch holds the truck at the truck stop until it lifts. We call before it does.'),
  P('Summer is hot and humid from May into October. The loading hour moves to the morning, and the afternoon storms move it again. The fall is the best season in the city, and the carriers know it.'),
 )+chips(["Downtown","South Main","The Pinch","Harbor Town","Mud Island","Midtown","Central Gardens","Cooper-Young","Overton Park","Crosstown","Binghampton","East Memphis","Chickasaw Gardens","White Station","The University District","Orange Mound","Whitehaven","Frayser","Raleigh","Berclair","Hickory Hill","Cordova","Germantown","Collierville","Bartlett","Arlington","Millington","Southaven","Olive Branch","West Memphis"])
 +NOTE('Serving Memphis and the whole Mid-South, Central Gardens block or Olive Branch cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Memphis?',
 prose(
  L('Open trailers carry most of the Mid-South, and the table above is priced for one.'),
  P('Enclosed keeps the pre-storm brine, the pollen, and the spring hail off the paint. Central Gardens collectors book it, and so do the pilots moving a car they care about. If ice is coming, the car takes the first truck with a slot, and we say that plainly.'),
  P('A daily driver rides open and arrives fine. See how the two differ on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, then a lot on Germantown Parkway, then a signature when the car lands. The start date or the move-in picks the week.'),
  P('Approve the figure, and the car goes to a carrier already crossing the river that week. The lot and the window get settled that afternoon. At pickup the driver shoots every panel and marks the Bill of Lading. You initial it, and both ends work from that sheet.'),
 )+ULI([
  "Nothing personal left in the cabin or the trunk",
  "Fuel at a quarter tank",
  "Pictures of every side and the odometer before the truck arrives",
  "One good key and a list of known faults",
  "Any aftermarket alarm disarmed",
  "Downtown, in Central Gardens, or on Mud Island, the handoff is on a main road",
 ])+prose(P('<a href="how-it-works.html">How it works</a> has the order of events, and <a href="car-shipping-preparation.html">preparation</a> has what to do before the truck comes.'))))

BODY.append(sec('Why Ship Guy','Why Memphis Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already cross the river every day. We know which bridge is open and which week the hub takes every driver in town.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on Monroe Avenue at the east edge of downtown.'),
  P('You deal with one coordinator from the quote to the delivery call. Open, enclosed, and expedited are compared on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Memphis','340 B Monroe Ave #325','Memphis, TN 38105','+19016985860','(901) 698-5860','CT',
 '340+B+Monroe+Ave+%23325,+Memphis,+TN+38105','Visit Us','Find Ship Guy in Memphis',
 'Our office is on Monroe Avenue at the east edge of downtown, by the medical district.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4027.2309069776725!2d-90.04535440000001!3d35.1424823!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87d57f7fff7daf27%3A0xfffec2bd774807d4!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793631496997!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Memphis to Dallas or Chicago?","Dallas runs four hundred to five hundred eighty dollars for a sedan. That is about four hundred fifty miles down 40 and 30. Chicago runs four hundred fifty to six hundred fifty, about five hundred thirty miles up 55 and 57. Little Rock is the lowest lane on the table, two hours west. SUVs and pickups run 10 to 25 percent more."),
 ("Do you ship cars for the cargo hub and the warehouses?","Yes, in every season. The hub relocates pilots, managers, and engineers on start dates ahead of the November peak. The warehouses along Lamar move managers the same way. The handoff happens on Germantown Parkway or at the lots on Winchester. When the company reimburses the move, we supply the paperwork it wants."),
 ("Can the carrier come to my street in Central Gardens or downtown?","No. Central Gardens is narrow streets under oaks, and downtown is one-way streets with trolley tracks. The driver meets you on Union Avenue, at the fairgrounds lots, or at a garage entrance. East Memphis, Whitehaven, Cordova, Germantown, Collierville, and the Mississippi suburbs usually allow the curb."),
 ("Do you handle moves for the Navy base in Millington?","Yes. The personnel command rotates sailors and civilians on orders. The handoff happens outside the gate or on Navy Road. Orders cover one car, and the second one rides with us. Millington prices the same as Memphis. Ship Guy is a private broker with no connection to the Navy."),
 ("Can you deliver on a University of Memphis or Rhodes move-in date?","Yes. The university takes cars in late August, and the college in Midtown follows the same week. Mom or Dad books, and someone over eighteen signs at the lot. The blocks around the campus are full that week, so the meeting point is the lots on Poplar. The date sets the window."),
 ("Can you ship a car to or from Southaven, Germantown, or West Memphis?","Yes. Germantown, Collierville, and Bartlett ride the same carriers and price the same as Memphis. Southaven, Olive Branch, and Horn Lake across the line do too. West Memphis is across the river and prices with the city. Jackson is an hour east on 40 and adds a few hours."),
 ("What happens if an ice storm hits on my pickup day?","The truck holds in Jackson or Little Rock until the roads thaw, usually a day or two. You get a call as soon as the forecast turns. The pickup takes the first clear morning at the figure you were quoted. A February date wants a flexible week."),
 ("What happens if a bridge closes?","Every truck uses the other one. The 40 bridge closed for three months in 2021. The carriers ran the 55 bridge with an hour of delay. A closure adds time to the day and nothing to the figure. We tell you which bridge the driver is using."),
 ("Can you ship a car that does not run from Memphis?","Yes. We send a winch truck and price the loading time in. The big-box lots on Germantown Parkway and the lots on Winchester are flat. Let us know if it rolls, steers, and brakes."),
 ("What do you need for a Memphis car shipping quote?","The two addresses with the neighborhood. What it is and whether it runs. Open or enclosed, and the week around the start date or the move. Send those, and the Memphis figure lands the same day."),
]
BODY.append(faq_section(FAQ,'Memphis FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Memphis?','Two minutes on the form above gets your lane a Memphis figure. Name the neighborhood and the week, and a carrier already crossing the river takes it.','+19016985860','(901) 698-5860','Get your free Memphis quote'))

build({
 'slug':'auto-transport-memphis-tennessee',
 'title':'Car Shipping in Memphis, TN — Auto Transport | Ship Guy',
 'meta':'Car shipping in Memphis, TN, the freight hub on the bluff above the Mississippi. Cargo hub and warehouse relocations, Navy moves at Millington, hospital and campus relocations, the two bridges, main-road handoffs for downtown and Central Gardens, curbside pickups in East Memphis, Cordova, and the suburbs, and the ice. Local office on Monroe Avenue. Free quote.',
 'h1':'Car Shipping in<br>Memphis, <span class="accent">Tennessee</span>',
 'lede':'Open, enclosed, and expedited auto transport across Memphis and the Mid-South, planned around 40, 55, the bridges, the hub’s peak season, the campus calendar, and the ice.',
 'tel':'+19016985860','disp':'(901) 698-5860','brand':'Memphis','keyword':'car shipping in memphis',
 'localterms':['memphis','freight','bluff','river','interstate 40','interstate 55','240','269','poplar','lamar','elvis presley boulevard','bridges','new bridge','old bridge','2021','crack','summer avenue','union avenue','winchester','germantown parkway','walnut grove','sycamore view','monroe avenue','downtown','main street','pinch','south main','harbor town','mud island','midtown','central gardens','cooper-young','overton park','east memphis','university district','whitehaven','frayser','raleigh','cordova','germantown','collierville','bartlett','arlington','millington','southaven','olive branch','horn lake','desoto county','west memphis','jackson','little rock','nashville','birmingham','st. louis','atlanta','louisville','dallas','chicago','houston','florida','texas','cargo hub','overnight shipper','pilots','warehouses','railroads','river port','bid cycles','children’s research hospital','medical district','residents','university','central avenue','college','student','navy','personnel command','navy road','sailors','orders','truck plant','stanton','retirees','memphis in may','riverfront','elvis week','candlelight vigil','move-in','classic','peak season','february 1994','february 2022','ice','july 2003','hurricane elvis','may 2011','forty-eight feet','february 2008','tornadoes','hickory hill','heat','brine','pollen','hail','bill of lading','fmcsa','winch','trolley','arena','fairgrounds','airport','cell lot','mansion'],
}, BODY, FAQ)
