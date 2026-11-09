import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Cary, North Carolina','Car shipping where the planned communities meet Interstate 40, the covenants decide the curb, and the tech campuses move families on start dates',
 ['Car shipping in Cary runs on Interstate 40, the 540 toll road, and the US 1 freeway. Ship Guy is a licensed auto transport broker with an office on East Chatham Street downtown.',
  'We book vetted carriers across Cary, from the bungalows downtown to the new subdivisions past Green Level. Apex, Morrisville, Holly Springs, and west Raleigh ride the same trucks. Every truck belongs to its carrier. Ship Guy carries the license and the bond.',
  'Interstate 40 runs the north edge of town between the Park and Raleigh. The 540 toll road sweeps around the west side to Apex and the airport. US 1 and 64 run as a freeway through the middle. The exits are Walnut Street, Cary Parkway, and Tryon Road. Cary Parkway, Kildaire Farm Road, Maynard Road, and Harrison Avenue carry the rest.',
  'This page covers 40, 540, US 1, Cary Parkway, downtown, the planned communities, and the covenants. It also covers the software campus, the game studio, the Park, the insurer, and the hospital. The festivals, the State Fair, the ice, and the pollen are here too.'],
 'Cary at a glance',
 ['Most Cary pickups land within 1 to 3 days. The town sits beside the 40 and 540 carriers between the Park and Raleigh. The trucks between Richmond, Charlotte, and Atlanta pass within ten minutes all day. The relocations keep the pool deep year round.',
  'Charlotte, Richmond, Wilmington, and the Triad are a same-day haul. Virginia Beach, Washington, Atlanta, and Philadelphia take a day. New York and Nashville take one to two, and Florida takes two.'],
 'Tell us the subdivision. Downtown, MacGregor Downs, Lochmere, and Preston meet the truck on a main road or at the clubhouse lot. Kildaire Farms, Amberly, Cary Park, Apex, and Morrisville usually allow the curb when the covenants do.'))

BODY.append(sec('The Roads','Interstate 40, the 540 Toll Road, US 1, US 64, Route 55, Cary Parkway, Kildaire Farm Road, Maynard Road, Harrison Avenue, High House Road, Davis Drive, and Chatham Street',
 prose(
  L('Cary is a town built around loops. One interstate clips the north edge, and a toll road sweeps the west. Two parkways circle everything between.'),
  P('Interstate 40 runs along the north edge from the Park to Raleigh. The exits at Harrison Avenue, Aviation Parkway, and Wade Avenue serve the town. The 540 toll road leaves 40 near the airport. It swings around the west side of Cary to Apex and Holly Springs. The carriers pay the toll or ride 55 beside it. US 1 and 64 come in from Raleigh as one freeway and split at Apex. US 1 runs south to Sanford, and 64 runs west to Pittsboro. A carrier uses the exits at Walnut Street, Cary Parkway, Tryon Road, and Kildaire Farm Road.'),
  P('Cary Parkway is the outer loop, and Maynard Road is the inner one. Kildaire Farm Road runs from downtown south to the lakes and the hospital. Harrison Avenue runs north past the software campus to 40. High House Road runs west to the new subdivisions. Davis Drive runs north through Morrisville to the Park. Route 55 runs from Apex through west Cary to Durham. Chatham Street is the old highway through downtown, and Academy Street crosses it at the depot. Walnut Street carries the shopping strip to Crossroads.'),
  P('The carriers come off 40 at Harrison Avenue or off US 1 at Walnut Street. They meet at the big-box lots at Crossroads or the shopping centers on Kildaire Farm Road. The Parkside lots in west Cary work too. The amphitheater lots in Regency Park work outside concerts. So do the soccer park lots on Trinity Road and the baseball complex lots off Green Level. The airport is fifteen minutes north on Aviation Parkway for a fly-and-ship. The depot on Academy Street runs trains to Charlotte and Richmond.'),
  P('Our office sits downtown on East Chatham Street, a short walk from the depot and the downtown park.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, MacGregor Downs, Lochmere, Kildaire Farms, Preston, Amberly, Carpenter Village, Cary Park, Weston, Regency, Apex, Morrisville, Holly Springs, and West Raleigh',
 prose(
  L('Cary is a small old downtown wrapped in forty years of planned communities. Whether the truck reaches your door depends on the covenant, not the street.'),
  P('Downtown is Chatham Street, Academy Street, the depot, and blocks of bungalows under big oaks. The new park takes up the south end. The streets are narrow, and the handoff happens on Chatham or at the depot lot. MacGregor Downs is the golf course and winding wooded streets with low limbs. The driver meets you at the clubhouse lot or on Kildaire Farm Road. Lochmere is lakes and curving streets off Kildaire Farm, and the handoff works the same way. Kildaire Farms was the first big planned community, and its wide streets usually allow the curb.'),
  P('Preston is golf, gated sections, and covenants that bar a trailer at the gate. The driver meets you on Cary Parkway or at the entrance lot. Amberly, Carpenter Village, and Cary Park are the new west side off High House and Green Level. The streets are wide, and the curb works where the covenant allows it. A covenant that bans trailers moves the handoff to the pool lot. Weston and Regency are office campuses and townhomes near 40, and the handoff happens at a garage entrance. Searstone and Glenaire are the retirement communities, and the handoff happens at the entrance.'),
  P('Apex south of town is a historic main street and miles of new subdivisions. The curb works in the subdivisions, and the main street takes a lot on the edge. Morrisville is the tech corridor along Davis Drive and apartment complexes. The handoff happens at the complex entrance. Holly Springs and Fuquay-Varina are newer still, with wide streets. West Raleigh across Trinity Road is older grids where the curb works.'),
  P('Apex, Morrisville, Holly Springs, and west Raleigh ship with the same trucks and price the same as Cary. Fuquay-Varina and Garner do too. Pittsboro and Sanford add a day.'),
 )))

ROUTES=[("Wilmington, NC","I-40 · ~135 mi","Same day","$200–$310"),("Charlotte, NC","US-64/I-85 · ~160 mi","Same day","$220–$340"),
 ("Richmond, VA","I-85/I-95 · ~175 mi","Same day","$220–$340"),("Virginia Beach, VA","US-64/I-64 · ~205 mi","1 day","$230–$350"),
 ("Washington, DC","I-95 · ~280 mi","1 day","$260–$390"),("Atlanta, GA","I-85 · ~395 mi","1 day","$360–$520"),
 ("Philadelphia, PA","I-95 · ~420 mi","1 day","$370–$540"),("New York, NY","I-95 · ~505 mi","1–2 days","$430–$620"),
 ("Nashville, TN","I-40 · ~535 mi","1–2 days","$440–$630"),("Orlando, FL","I-95 · ~630 mi","2 days","$470–$680")]
BODY.append(rate_table('Lanes &amp; Costs','Cary Car Shipping Lanes and Estimated Costs',
 'The lanes western Wake County cars run most, with open-trailer estimates. The form above returns your exact lane.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Cary, running sedan, open trailer. SUVs and pickups add 10 to 25 percent, and enclosed costs more again. Your week and the carriers on 40 and 85 that week decide the final figure.',
 prose(
  P('Cary prices with Raleigh on every lane, because the same trucks serve both. The Charlotte and Atlanta lanes ride 85 through the Triad and fill every day. The Richmond and Washington lanes ride 85 and 95 north. The Wilmington lane rides 40 to the coast. The Northeast lanes bring the tech transfers from New Jersey and New York. California rides 40 west and takes a week.'),
  P('A move-in week in August or the State Fair in October makes for a crowded week. The <a href="car-shipping-cost.html">cost guide</a> handles size, condition, and timing one by one.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Software Campus, the Game Studio, the Insurer, the Park, the Laptop Maker, the Hospital, the Campuses Next Door, the Retirement Communities, and the Post an Hour South',
 prose(
  L('Cary relocates engineers, analysts, researchers, nurses, retirees, and the families that follow a start date. The tech campuses move the most.'),
  P('The software campus off Harrison Avenue relocates analysts and developers from across the country on start dates. The game studio at Crossroads does the same. It bought the old mall site for a new campus. The insurer’s campus at Weston moves actuaries and managers. The Park ten minutes north holds the pharmaceutical labs, the chip designers, and the research institutes. The laptop maker’s campus in Morrisville hires engineers from across the country and overseas. The handoff happens at a garage entrance or the complex lot. When the employer pays, we write the paperwork however it needs.'),
  P('The hospital on Kildaire Farm Road brings nurses all year. The campuses in Raleigh, Durham, and Chapel Hill send cars in each August and home each May. The state university is fifteen minutes east on Hillsborough Street. A parent books, and an adult signs at the lot. The retirement communities at Searstone and Glenaire bring retirees from the Northeast. Some go back for the summers, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork a state line adds.'),
  P('Fort Bragg is an hour south on 40 and 95. Some of its families live in Holly Springs and Fuquay-Varina. Seymour Johnson is an hour east. The rotations peak in summer. Ship Guy is a private broker and not part of the Army or the Air Force. The <a href="military-car-shipping.html">military</a> page covers orders and the dates they set.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Lazy Daze, Spring Daze, the Diwali Festival, the Lantern Festival, the Soccer Matches, the State Fair, the Football Saturdays, the Ice Storms, Fran, and the Pollen',
 prose(
  L('Cary runs on a festival calendar and a school calendar. The weather problem is an ice storm every few winters and a hurricane every decade or so.'),
  P('Lazy Daze closes downtown on the last weekend of August for the arts festival. Spring Daze fills Bond Park in April. The Diwali festival fills the amphitheater at Regency Park each October. The lantern festival lights it nightly from November into January. The pro soccer clubs play at the soccer park off Trinity Road from spring to fall. The State Fair fills Trinity Road and Blue Ridge Road for eleven days each October. The state university’s football Saturdays do the same thing a half dozen times each fall. The Christmas parade closes Academy Street in December. Give a fair week or a home Saturday three weeks of notice.'),
  P('The December 2002 ice storm coated the Triangle in an inch of ice. The power stayed out for up to ten days. Raleigh had not seen that much freezing rain since 1948. The January 2000 storm dropped close to twenty inches overnight. The January 2022 ice shut the Triangle down for a day. When ice is in the forecast, the carriers wait in Rocky Mount or Greensboro. A winter pickup can slip two days.'),
  P('Fran in September 1996 came inland as a hurricane and put oaks through roofs across Cary. The streets took weeks to clear. Florence in 2018 closed 40 and 95 toward the coast for a week. The April pine pollen turns every car yellow for three weeks. Summer brings heat, humidity, and a thunderstorm most afternoons that passes in an hour.'),
 )+chips(["Downtown","Academy Street","MacGregor Downs","Lochmere","Kildaire Farms","Preston","Amberly","Carpenter Village","Cary Park","Weston","Regency","Scottish Hills","Greenwood Forest","Twin Lakes","Searstone","Glenaire","Crossroads","Green Level","Apex","Morrisville","Holly Springs","Fuquay-Varina","Garner","West Raleigh","Research Triangle Park"])
 +NOTE('Serving Cary, Apex, Morrisville, and western Wake County, downtown bungalow or gated golf community. Name the subdivision and tell us whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Cary?',
 prose(
  L('Open trailers carry most of western Wake County’s cars, and the table above assumes one.'),
  P('Enclosed keeps the pollen, the ice brine, and the summer hail off the paint. The engineers moving a car worth more than the relocation package book it. So do the retirees arriving with a convertible. When an ice storm is coming and only an open truck has room, we say so first.'),
  P('A commuter car or a student’s sedan rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot off Cary Parkway, and a signature when the car comes off the truck. The start date decides the week.'),
  P('Approve the figure, and we hand the car to a carrier already running 40 or 85 that week. The lot and the window are confirmed the same day. The driver photographs the car at pickup and notes its condition on the Bill of Lading. You initial it, and it is the reference at delivery.'),
 )+ULI([
  "Your belongings out of the cabin and the trunk",
  "A quarter tank of fuel or less",
  "Photos of every side and the odometer before pickup",
  "A working key and a note on known faults",
  "Aftermarket alarms turned off",
  "Behind a gate, in MacGregor Downs, or downtown, expect a lot on Cary Parkway",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers the morning of pickup.'))))

BODY.append(sec('Why Ship Guy','Why Cary Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 40 and 85 past the Triangle every day. We know which covenants bar a trailer and which weekends the State Fair takes Trinity Road.'),
  P('Our FMCSA license and our $75,000 bond are a matter of public record on the federal register. The office is on East Chatham Street downtown.'),
  P('One person at Ship Guy handles the move from quote to delivery call. The <a href="services.html">services</a> page covers open, enclosed, and expedited in turn.'),
 )))

BODY.append(office('Cary','167 E Chatham St #542','Cary, NC 27511','+19194391535','(919) 439-1535','ET',
 '167+E+Chatham+St+%23542,+Cary,+NC+27511','Visit Us','Find Ship Guy in Cary',
 'Our office sits downtown on East Chatham Street, a short walk from the depot and the downtown park.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3995.051905818661!2d-78.7790167!3d35.787712!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89acf3d5f06eb9d1%3A0x82abe0ee3c2146dd!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1794237141771!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Cary to Charlotte or Washington?","Charlotte runs two hundred twenty to three hundred forty dollars for a sedan. It is about one hundred sixty miles down 85. Washington runs two hundred sixty to three hundred ninety on 95. Wilmington is the lowest lane on the table. New York runs four hundred thirty to six hundred twenty. An SUV or a pickup adds 10 to 25 percent."),
 ("Will the carrier come into my gated community or past the covenants?","Usually not. Preston and the gated sections bar a trailer at the gate. Many covenants ban trailers on the streets. The driver meets you at the entrance lot, the clubhouse, or on Cary Parkway. Kildaire Farms, Amberly, Cary Park, Apex, and Morrisville allow the curb when the covenant does."),
 ("Do you ship cars for the software campus or the game studio?","Yes, every week. The software campus off Harrison Avenue and the game studio at Crossroads relocate people on start dates. So do the insurer at Weston, the Park, and the laptop maker in Morrisville. The handoff happens at a garage entrance or the complex lot. When the employer pays, we write it up however it needs."),
 ("Can you deliver a car for a student at one of the Triangle campuses?","Yes. The cars arrive in August and leave in May. The state university is fifteen minutes east, and Durham and Chapel Hill are thirty. A parent books, and an adult signs at the lot. The window follows the move-in date."),
 ("What happens during the State Fair or a football Saturday?","Trinity Road and Blue Ridge Road fill for eleven days each October. They fill again a half dozen Saturdays each fall. The soccer park lots are out, and the handoff moves to Crossroads or the Kildaire Farm Road centers. The figure does not change. Give a fair week three weeks of notice."),
 ("What happens if an ice storm hits on my pickup day?","The truck waits in Rocky Mount or Greensboro until the roads clear, usually a day. The December 2002 storm cut power for up to ten days. The January 2022 ice shut the Triangle down for a day. We call when the forecast turns. The pickup moves to the first clear morning, and the figure stays where it was."),
 ("Does the April pollen matter for an open trailer?","It coats the car, and it washes off. The pine pollen turns every car yellow for about three weeks each April. A car on an open trailer arrives yellow and is fine after a wash. Enclosed keeps it off, and some owners book enclosed for that month alone."),
 ("Can you ship a car to or from Apex, Morrisville, or Holly Springs?","Yes. Apex, Morrisville, Holly Springs, and west Raleigh ride the same carriers and price the same as Cary. Fuquay-Varina and Garner do too. Pittsboro and Sanford add a day."),
 ("Can you ship a car that does not run from Cary?","Yes. The carrier brings a winch, and the figure includes the loading time. The Crossroads lots and the Parkside lots are flat. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Cary car shipping quote?","Both addresses, with the subdivision. The year, make, and model, and whether it runs. Open or enclosed, and the week around the start date. With those, the Cary figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Cary FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Cary?','Two minutes on the form above puts a Cary figure on your lane. Name the subdivision and the week, and a carrier already on 40 takes it.','+19194391535','(919) 439-1535','Get your free Cary quote'))

build({
 'slug':'auto-transport-cary-north-carolina',
 'title':'Car Shipping in Cary, NC — Auto Transport | Ship Guy',
 'meta':'Car shipping in Cary, NC, on Interstate 40, the 540 toll road, and US 1. Gate and clubhouse handoffs for Preston, MacGregor Downs, and Lochmere, curbside pickups in Kildaire Farms, Amberly, Cary Park, Apex, and Morrisville, the software campus, the game studio, the Park, the insurer, the Triangle campuses, the State Fair, the ice storms, and the pollen. Local office on East Chatham Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Cary, <span class="accent">North Carolina</span>',
 'lede':'Open, enclosed, and expedited auto transport across Cary, Apex, Morrisville, and western Wake County, planned around 40 and 540, the covenants, the start dates, the festivals, the fair, and the ice.',
 'tel':'+19194391535','disp':'(919) 439-1535','brand':'Cary','keyword':'car shipping in cary',
 'localterms':['cary','interstate 40','540','toll road','us 1','us 64','route 55','cary parkway','kildaire farm road','maynard road','harrison avenue','high house road','davis drive','chatham street','academy street','walnut street','tryon road','aviation parkway','wade avenue','green level','trinity road','depot','downtown park','bungalows','oaks','macgregor downs','golf course','clubhouse','lochmere','lakes','kildaire farms','planned community','preston','gated','covenants','amberly','carpenter village','cary park','pool lot','weston','regency','searstone','glenaire','retirement communities','scottish hills','greenwood forest','twin lakes','crossroads','parkside','apex','morrisville','holly springs','fuquay-varina','garner','west raleigh','pittsboro','sanford','software campus','game studio','old mall site','insurer','campus','the park','pharmaceutical labs','chip designers','research institutes','laptop maker','hospital','state university','hillsborough street','durham','chapel hill','fort bragg','seymour johnson','lazy daze','arts festival','spring daze','bond park','diwali','amphitheater','lantern festival','soccer park','soccer club','state fair','blue ridge road','eleven days','football saturdays','christmas parade','december 2002','ice storm','ten days','1948','january 2000','twenty inches','january 2022','rocky mount','greensboro','fran','september 1996','florence','2018','pollen','yellow','humidity','fly-and-ship','airport','baseball complex','wilmington','charlotte','richmond','virginia beach','washington','atlanta','philadelphia','new york','nashville','orlando','california','brine','hail','convertible','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
