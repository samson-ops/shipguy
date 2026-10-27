import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('South Bend, Indiana','Car shipping on the Toll Road, ninety minutes from Chicago, with a stadium that fills the city seven Saturdays a year',
 ['Car shipping in South Bend runs off the Toll Road and the 31 bypass. Ship Guy is a licensed auto transport broker with an office on Colfax Avenue in the East Bank.',
  'We book vetted carriers across Michiana, from Granger and Mishawaka to Elkhart and north to Niles. The trucks belong to the carriers.',
  'The Toll Road carries 80 and 90 across the north side. Its exits are at Michigan Street and the university. The US 31 bypass loops the south and west sides. US 20 rides the bypass east to Elkhart, and US 33 is Lincoln Way through the middle.',
  'This page covers the Toll Road, the bypass, downtown, the campus, the old grids, Granger, and Mishawaka. It also covers the RV plants, the hospitals, football Saturdays, the lake-effect bands, the river, and the lanes.'],
 'South Bend at a glance',
 ['Most pickups happen within 1 to 3 days. The Chicago carriers pass the city on the Toll Road. The Detroit and Indianapolis trucks come in on 31 and 20.',
  'Chicago, Fort Wayne, Grand Rapids, and Indianapolis are a same-day haul, and so is Detroit. Columbus, Cincinnati, and Milwaukee take a day. Nashville takes one, and Florida takes three.'],
 'Tell us the side of the river and whether you are near the campus. The old grids northwest and northeast of downtown need a meeting spot. Granger, the south side, and Mishawaka usually allow the curb.'))

BODY.append(sec('The Roads','The Toll Road, the 31 Bypass, US 20, Lincoln Way, and the Michigan Line',
 prose(
  L('South Bend sits on the busiest toll road in the Midwest. Every carrier between Chicago and the East passes it.'),
  P('The Indiana Toll Road carries Interstate 80 and 90 across the north edge of the city. The exits at Michigan Street and at the university serve the city. The Mishawaka exit at Capital Avenue serves the east side. Every carrier between Chicago and Cleveland, Toledo, or the East Coast rides it. The tolls go on the truck’s transponder, and they ride inside the quote.'),
  P('The US 31 bypass is the St. Joseph Valley Parkway, a freeway around the south and west sides. It runs south to Indianapolis on the new freeway and north to Niles and the Michigan line. US 20 shares the bypass across the south side and runs east to Elkhart. US 33 is Lincoln Way, the old road through downtown and out to Elkhart and Goshen.'),
  P('Michigan Street and Main Street are the one-way pair through downtown. Ironwood runs the east side, and Grape Road carries the retail strip in Mishawaka. Western Avenue runs the west side. The St. Joseph River bends through the middle, and the bridges downtown and at Angela set the crossings. Edison Road and Douglas Road run the north side toward Granger.'),
  P('The carriers come off the Toll Road at the university exit and off the bypass at Ireland Road. The mall on Grape Road, the ballpark downtown, and the centers on Ireland Road are the meeting spots. The campus lots on Juniper Road work outside football weekends.'),
  P('Our office is on Colfax Avenue in the East Bank, a block from the river.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown and the East Bank, the Campus, the Old Grids, River Park, the West Side, Granger, Mishawaka, and Elkhart',
 prose(
  L('South Bend is an old factory city with a famous campus on its north edge. The handoff depends on which of the two you are near.'),
  P('Downtown is a compact grid of office towers, the ballpark, and the hotel blocks along Michigan Street. The East Bank across the river is the restaurant district and the old factory lofts. The streets are one-way and narrow. The driver meets you at the ballpark lots or on Niles Avenue. The campus to the north is closed to a trailer. The handoff happens at the lots on Juniper Road or on Eddy Street.'),
  P('The Near Northwest and the Chapin Park district are big houses on narrow streets under old trees. The Northeast Neighborhood between downtown and the campus is student rentals and small lots. Both need a meeting spot on Michigan Street or at the campus lots. River Park on the east side is a postwar grid with wider streets. The curb works on most of them.'),
  P('The west side along Western Avenue is the old Polish and Hungarian neighborhoods, a dense grid with alleys. The handoff moves to Western or to the lots at the bypass. The south side between the bypass and Ireland Road is 1950s ranches on wider streets. The curb works. Erskine and Sunnymede are the same.'),
  P('Granger to the northeast is the newest growth, with wide subdivisions off Cleveland Road and the Toll Road. The curb works almost everywhere. Mishawaka is its own city east of the river. It has the mall district on Grape Road and older grids downtown. Elkhart sits fifteen minutes east on the Toll Road with the RV plants. Niles and Edwardsburg sit ten minutes north in Michigan. The state line adds no paperwork, and all of them price the same as South Bend.'),
 )))

ROUTES=[("Chicago, IL","I-80/I-90 · ~95 mi","Same day","$160–$260"),("Fort Wayne, IN","US-31/US-30 · ~90 mi","Same day","$160–$250"),
 ("Grand Rapids, MI","US-31/I-196 · ~110 mi","Same day","$170–$280"),("Indianapolis, IN","US-31 · ~140 mi","Same day","$190–$300"),
 ("Detroit, MI","I-94 · ~190 mi","Same day","$220–$340"),("Milwaukee, WI","I-90/I-94 · ~190 mi","Same day","$220–$340"),
 ("Columbus, OH","US-30/I-75 · ~250 mi","1 day","$250–$380"),("Cincinnati, OH","US-31/I-74 · ~250 mi","1 day","$250–$380"),
 ("Nashville, TN","US-31/I-65 · ~470 mi","1 day","$400–$570"),("Orlando, FL","I-65/I-75 · ~1,130 mi","3 days","$750–$1,050")]
BODY.append(rate_table('Lanes &amp; Costs','South Bend Car Shipping Lanes and Estimated Costs',
 'The lanes Michiana cars ride most, with estimated open-trailer ranges. Put your exact route on the form above for a number.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from South Bend for a running sedan on an open trailer. Add 10 to 25 percent for an SUV or a pickup, and more for an enclosed trailer. Toll Road fees ride inside the number. The carriers free on your dates settle the final figure.',
 prose(
  P('South Bend prices with Chicago on the eastern lanes. The Toll Road carriers pass the city on every run. It prices a little under Fort Wayne to Chicago and a little over it to Columbus and Cincinnati. The Detroit lane rides 94 through Michigan and runs daily. The Florida lane fills with retirees in the fall.'),
  P('A move timed to a football weekend costs more, because the carriers avoid the city on those Saturdays. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Hospitals, the RV Plants, the Truck Plant, and the Data Center',
 prose(
  L('South Bend relocates professors, physicians, RV executives, and students. The university moves more people than anyone in Michiana.'),
  P('The university on the north edge is the largest employer in the county. Faculty hires land each summer with a closing date and a second car. The students arrive in late August and leave in May, and a parent ships the car. The two smaller colleges across the road and the state university branch run the same calendar.'),
  P('The hospital system on Michigan Street and the hospital on the bypass hire traveling nurses all year. The residents land each June, and the physicians come with a closing date. The RV makers in Elkhart build most of the recreational vehicles in the country. They move managers and engineers in from every state on product cycles, and many buy in Granger.'),
  P('The truck plant in Mishawaka builds the military vehicles and rotates engineers on contract cycles. The data center campus going up in New Carlisle moves construction managers and technicians in on build schedules. The old Studebaker plants are offices and a tech park now. The firms in them hire from Chicago. We supply the paperwork a reimbursed move needs.'),
  P('Families from Chicago buy in Granger and Mishawaka on closing dates. One car rides the trailer while the other is driven. Retirees leave for Florida each fall and come back in April. The interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page. Ship Guy is a private broker with no military tie. The <a href="military-car-shipping.html">military</a> page covers an order to Grissom or Great Lakes.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Football Saturdays, Commencement, the Fair, the Lake-Effect Bands, and the River',
 prose(
  L('South Bend runs on seven football Saturdays, a May commencement, and a winter that comes off Lake Michigan.'),
  P('The stadium holds eighty thousand, and the city doubles on a home Saturday. The Toll Road exit backs up from Friday afternoon, and every lot near the campus is sold. A handoff near the campus on a football weekend moves to Friday morning or to Mishawaka. Commencement in May fills the hotels and the campus roads for a weekend. Move-in week in late August fills Eddy Street and Juniper Road.'),
  P('The county fair fills the fairgrounds on Ireland Road for a week in July. The jazz festival fills downtown Elkhart for a June weekend. The ballpark downtown fills its lots on game nights from April through September. A handoff near any of them moves to the daytime.'),
  P('Lake Michigan sits thirty miles northwest, and the lake-effect bands bury the city most winters. Seventy inches falls in a normal year. The Toll Road and the bypass close in the bands a few times a season. The carriers park at the plazas until the plows finish. A winter pickup can lose a day, and we say so before it happens.'),
  P('The February 2018 flood put the river over its banks at a record crest. The riverside roads closed for a week. The August 2016 storm dropped eight inches in a night and flooded the underpasses. The sirens sound a few times each spring, and the 1965 tornadoes are still the measure. A warning pauses the loading until it clears.'),
 )+chips(["Downtown","East Bank","Colfax Avenue","Michigan Street","Near Northwest","Chapin Park","Northeast Neighborhood","Eddy Street","Campus","Juniper Road","River Park","Sunnymede","Erskine","Western Avenue","West Side","Ireland Road","Granger","Cleveland Road","Mishawaka","Grape Road","Capital Avenue","Osceola","Elkhart","Goshen","New Carlisle","Lakeville","Niles","Edwardsburg","Michigan City","Plymouth"])
 +NOTE('Serving South Bend, Mishawaka, Granger, Elkhart, and the Michigan towns across the line. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in South Bend?',
 prose(
  L('Most Michiana cars leave on an open trailer, and the lane table above is built around one.'),
  P('An enclosed trailer keeps off the road salt, the lake grit, and the gravel. The collectors who fill the Studebaker museum weekends book one for the show cars. Faculty shipping a new car behind a move book one too.'),
  P('A commuter car or an RV-plant pickup rides open without a worry. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two in detail.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot at the mall or the ballpark, and the car at the far end. The start date or the closing picks the week.'),
  P('Agree to the number, and the car is slotted onto a carrier already riding the Toll Road. The lot and the window come back within the day. Before the car loads, you and the driver go over it panel by panel. Anything already on it goes onto the Bill of Lading. Two signatures, and that form is the reference when the car comes off.'),
 )+ULI([
  "Cabin, trunk, and glovebox emptied of personal items",
  "Roughly a quarter tank of fuel",
  "Each side and the odometer photographed before the truck arrives",
  "A single working key for the driver, plus a note on any fault",
  "Any aftermarket alarm turned off",
  "Near the campus or the old grids, meet the truck at the campus lots or on Michigan Street",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why South Bend Drivers Choose Ship Guy',
 prose(
  L('We catch the Chicago carriers on the Toll Road before they leave the state. We plan around the football calendar and the lake-effect bands.'),
  P('Ship Guy’s FMCSA brokerage authority and $75,000 surety bond are both on the federal register. Our office is on Colfax Avenue in the East Bank.'),
  P('The same coordinator handles your move from the first number to the signed delivery sheet. Open, enclosed, and expedited options are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('South Bend','511 E Colfax Ave #445','South Bend, IN 46617','+15743285795','(574) 328-5795','ET',
 '511+E+Colfax+Ave+%23445,+South+Bend,+IN+46617','Visit Us','Find Ship Guy in South Bend',
 'Our office is on Colfax Avenue in the East Bank, a block from the river.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4582.472541295477!2d-86.2437527!3d41.6780948!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8816cd301dc8539d%3A0x9ca1f73d312d78fa!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793102845041!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from South Bend to Chicago or Indianapolis?","Chicago runs one hundred sixty to two hundred sixty dollars for a sedan. That is about ninety-five miles on the Toll Road. Indianapolis runs one hundred ninety to three hundred, about one hundred forty miles down 31. Fort Wayne is ninety miles and runs about the same as Chicago. An SUV or a pickup adds 10 to 25 percent to each. Trucks run all three lanes daily."),
 ("Can the carrier come to my street near the campus or in the Near Northwest?","Usually not. The campus is closed to a trailer. The Northeast Neighborhood and the Near Northwest are narrow streets under old trees. The driver meets you at the campus lots on Juniper Road, on Michigan Street, or at the ballpark. Granger, the south side, River Park, and Mishawaka usually allow the curb."),
 ("Can you deliver on the Notre Dame move-in date?","Yes. The campus takes cars in late August and sends them home in May. The two colleges across the road and the state university branch run the same calendar. A parent makes the booking, and someone over eighteen meets the driver at a campus lot. The window follows move-in day wherever it lands. Move-in week fills Eddy Street, so the handoff happens on Juniper Road."),
 ("Does a football Saturday affect my pickup?","Near the campus, yes. The city doubles on a home Saturday, and the Toll Road exit backs up from Friday. Every lot near the stadium is sold. We move a handoff near the campus to Friday morning or to Mishawaka. The south side and Granger run normally. Commencement weekend in May works the same way."),
 ("Can you ship a car to or from Mishawaka, Granger, or Elkhart?","Yes, and all three price the same as South Bend. Mishawaka rides the same carriers off the Capital Avenue exit. The mall lots on Grape Road are the usual handoff. Granger rides them off the Toll Road and allows the curb on most streets. Elkhart rides them fifteen minutes east, and the RV plants have lots at every gate."),
 ("Do you ship cars to Niles or the Michigan side of the line?","Yes. Niles, Edwardsburg, and Cassopolis sit ten to twenty minutes north on 31 and the county roads. The state line adds no paperwork to a domestic move. They ride the same carriers and price the same as South Bend. Send the full address, because the Michigan subdivisions are not on every map."),
 ("What happens if a lake-effect storm hits on my pickup day?","The bands close the Toll Road and the bypass a few times a winter. The carriers park at the plazas until the plows finish. A winter pickup can slip a day, and you hear it from us first. A spring flood on the river closes the riverside roads, and a pickup there moves up the hill."),
 ("Can you ship a car that does not run from South Bend?","Yes. A carrier with a winch is assigned, and the longer load time is already in the first number. The mall lots on Grape Road or the ballpark lots give the driver level ground. Say whether the car rolls, steers, and brakes."),
 ("Do you ship cars for people relocating to the RV plants or the hospitals?","Yes, every month. The RV makers in Elkhart move managers and engineers in from every state on product cycles. The hospital on Michigan Street and the hospital in Mishawaka hire traveling nurses all year. Many ship a second car behind the move. We supply the paperwork a reimbursed move needs."),
 ("What do you need for a South Bend car shipping quote?","Where the car is and where it goes, with the side of the river or the suburb. What it is, by year, make, and model. Whether it runs. Open or enclosed. The week around the start date or the closing. Five answers, and the South Bend number comes back the same day."),
]
BODY.append(faq_section(FAQ,'South Bend FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in South Bend?','The form above prices the lane while you wait. Tell us the side of the river and the week, and a Toll Road carrier takes it.','+15743285795','(574) 328-5795','Get your free South Bend quote'))

build({
 'slug':'auto-transport-south-bend-indiana',
 'title':'Car Shipping in South Bend, IN — Auto Transport | Ship Guy',
 'meta':'Car shipping in South Bend, IN, on the Toll Road ninety minutes from Chicago. Notre Dame move-in and football-Saturday timing, campus-lot handoffs for the old grids, curbside pickups in Granger and Mishawaka, Elkhart and the Michigan towns across the line, the lake-effect bands, and the river. Local office on Colfax Avenue in the East Bank. Free quote.',
 'h1':'Car Shipping in<br>South Bend, <span class="accent">Indiana</span>',
 'lede':'Open, enclosed, and expedited auto transport across Michiana, planned around the Toll Road, the bypass, the campus calendar, and the lake-effect winter.',
 'tel':'+15743285795','disp':'(574) 328-5795','brand':'South Bend','keyword':'car shipping in south bend',
 'localterms':['south bend','michiana','toll road','interstate 80','90','michigan street','university','mishawaka','capital avenue','transponder','31 bypass','st. joseph valley parkway','indianapolis','niles','michigan line','us 20','elkhart','us 33','lincoln way','goshen','main street','one-way','ironwood','grape road','western avenue','st. joseph river','angela','edison road','douglas road','granger','ireland road','mall','ballpark','juniper road','campus','colfax avenue','east bank','downtown','lofts','niles avenue','eddy street','near northwest','chapin park','northeast neighborhood','student rentals','river park','polish','hungarian','alleys','erskine','sunnymede','cleveland road','edwardsburg','state line','paperwork','fort wayne','grand rapids','detroit','milwaukee','columbus','cincinnati','nashville','orlando','professors','physicians','rv','students','faculty','closing date','colleges','state university','hospital','traveling nurses','residents','rv makers','recreational vehicles','product cycles','truck plant','military vehicles','data center','new carlisle','studebaker','tech park','chicago','retirees','florida','grissom','great lakes','football saturdays','stadium','eighty thousand','commencement','move-in','county fair','fairgrounds','jazz festival','game nights','lake michigan','lake-effect','seventy inches','plazas','february 2018 flood','record crest','august 2016','underpasses','sirens','1965 tornadoes','warning','museum','show cars','bill of lading','fmcsa','surety bond','cassopolis','michigan city','plymouth','lakeville','osceola'],
}, BODY, FAQ)
