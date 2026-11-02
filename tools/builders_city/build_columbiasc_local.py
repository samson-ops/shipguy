import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Columbia, South Carolina','Car shipping in the capital, where three interstates meet at Malfunction Junction and the Army trains its soldiers on the east side',
 ['Car shipping in Columbia runs on Interstates 26, 20, and 77, which meet northwest of downtown. Ship Guy is a licensed auto transport broker with an office on Pickens Street in the BullStreet District.',
  'We book vetted carriers across Columbia, from the Vista to Forest Acres and out to Lexington and Blythewood. The trucks are the carriers’ own. The license and the bond are ours.',
  'Interstate 26 runs from Charleston through the city to Spartanburg. Interstate 20 crosses from Augusta to Florence. Interstate 77 starts here and runs north to Charlotte. The 126 spur drops into downtown. Highway 277 runs the northeast, and 378 and 1 cross the rest.',
  'This page covers 26, 20, 77, the spur, the junction, downtown, the river, the campus, and the grids. It also covers the fort, the hospitals, the State House, the floods, the ice, and the football Saturdays.'],
 'Columbia at a glance',
 ['Pickups usually land within 1 to 3 days. Columbia sits where the 26, 20, and 77 carriers cross. The trucks between Charlotte and the coast pass through all day. The pool is deep, and the fort keeps it moving all year.',
  'Augusta, Charlotte, Charleston, Fayetteville, and Savannah ride a single day on the truck. Atlanta, Raleigh, and Jacksonville take a day. Washington takes one to two, and New York takes two.'],
 'Tell us the neighborhood. Downtown, the Vista, Five Points, the campus, and the fort gates meet the truck on a main road. Shandon, Forest Acres, the Northeast, Lexington, and Irmo usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 26, Interstate 20, Interstate 77, the 126 Spur, Malfunction Junction, Highway 277, Gervais Street, Assembly Street, and Two Notch Road',
 prose(
  L('Columbia is three interstates meeting at one bad interchange and a grid of wide streets from 1786. A carrier picks its exit and avoids the junction at rush hour.'),
  P('Interstate 26 comes up from Charleston, crosses the river west of downtown, and runs on to Spartanburg. Interstate 20 crosses from Augusta to Florence along the north side. The two meet at Malfunction Junction, the interchange with the 126 spur the state is rebuilding through 2030. Interstate 77 starts at 26 south of the city and runs up the east side to Charlotte. The 126 spur drops from the junction into downtown as Elmwood Avenue. Highway 277 runs from 77 into the north side.'),
  P('Gervais Street runs from the river bridge past the State House and through the Vista. Assembly Street is the north-south spine past the stadium and the farmers market. Harden Street runs Five Points to the campus. Devine Street and Garners Ferry carry the southeast. Forest Drive and Two Notch run northeast. Bluff Road runs the stadium and the fairgrounds. Broad River and Harbison carry the northwest to Irmo.'),
  P('The carriers come off 26 at Harbison and St. Andrews and off 20 at Two Notch. On 77 they use Garners Ferry and Forest Drive. The big-box lots on Harbison and Two Notch are the usual meeting spots. The stadium lots on Bluff work outside a Saturday. So do the fairgrounds lots and the lots at the mall on Harbison. The airport is across the river in West Columbia for a fly-and-ship.'),
  P('Our office is on Pickens Street in the BullStreet District, beside the ballpark north of the State House.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Vista, Five Points, Shandon, Rosewood, Olympia, Forest Acres, the Northeast, Eau Claire, the BullStreet District, and the River Towns',
 prose(
  L('Columbia is a grid of old neighborhoods under big oaks and suburbs that run to the lake. The core meets the truck on a main road, and the oak streets meet it at the curb.'),
  P('Downtown runs from the State House to Elmwood, government offices and the campus and one-way streets. The driver meets you on Assembly or at a garage entrance. The Vista along Gervais is old warehouses turned restaurants on cobbled streets. The handoff happens on Gervais or at the convention center lots. Five Points is bars and student apartments on tight streets, and the handoff moves to Harden Street. The BullStreet District north of downtown is the old asylum grounds rebuilt around the ballpark. The lots there work.'),
  P('Shandon is bungalows under oaks on a grid with alleys, and the curb works where the limbs clear. Rosewood and Olympia south of the campus are mill houses and student rentals. The handoff moves to Rosewood Drive or Bluff Road. Forest Acres east of town is a city of its own with wide streets. The truck reaches the curb. The Northeast along Two Notch and Clemson Road is subdivisions on open ground. The curb works nearly everywhere.'),
  P('Eau Claire and North Columbia are older grids with tight streets, and the handoff happens on North Main. Blythewood and the truck plant country north on 77 are new subdivisions, and the curb works. Irmo, Lexington, and Chapin along the lake are cul-de-sacs with covenants. The handoff moves to the entrance when a covenant bans trailers.'),
  P('West Columbia, Cayce, Lexington, Irmo, and Forest Acres ship with the same trucks and price as Columbia. Sumter, Orangeburg, and Camden add an hour on the truck and a few dollars.'),
 )))

ROUTES=[("Augusta, GA","I-20 · ~75 mi","Same day","$150–$240"),("Charlotte, NC","I-77 · ~95 mi","Same day","$170–$280"),
 ("Charleston, SC","I-26 · ~115 mi","Same day","$170–$280"),("Fayetteville, NC","I-20/US-1/I-95 · ~160 mi","Same day","$200–$310"),
 ("Savannah, GA","I-26/I-95 · ~160 mi","Same day","$200–$310"),("Atlanta, GA","I-20 · ~215 mi","1 day","$230–$350"),
 ("Raleigh, NC","I-77/US-1/I-85 · ~230 mi","1 day","$230–$350"),("Jacksonville, FL","I-26/I-95 · ~290 mi","1 day","$280–$410"),
 ("Washington, DC","I-77/I-85/I-95 · ~480 mi","1–2 days","$400–$580"),("New York, NY","I-77/I-85/I-95 · ~710 mi","2 days","$500–$730")]
BODY.append(rate_table('Lanes &amp; Costs','Columbia Car Shipping Lanes and Estimated Costs',
 'Where Richland County cars go most often, with open-trailer ranges for each. Price your own lane on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Columbia, sedan that runs, open trailer. Expect 10 to 25 percent more for an SUV or a pickup, and enclosed above that. The real figure comes from the week you pick and the carriers on 26 and 77 that week.',
 prose(
  P('Columbia prices close to Charlotte on every lane, because the same 77 carriers serve both. The Charlotte lane rides 77 and fills every day. The Atlanta lane rides 20 west. The Florida lane rides 26 to 95 and fills each fall with the retirees. The Northeast lanes ride 77 and 85 to 95, and the price follows the fort’s graduation calendar.'),
  P('A PCS report date at the fort or a mid-August move-in means a busy week. Size, condition, and timing are each explained on the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','Fort Jackson, the University, the State Government, the Hospitals, the Truck Plant, the Insurance Offices, and the Retirees',
 prose(
  L('Columbia relocates soldiers, drill sergeants, students, state employees, nurses, and engineers. The fort moves the most.'),
  P('Fort Jackson on the east side trains half the Army’s new soldiers. The trainees do not bring cars. The drill sergeants, the cadre, and the permanent party do. They PCS in and out on orders in every month. The handoff happens at the Garners Ferry lots or outside Gate 2. Graduation Thursdays fill the roads around the fort with families. Ship Guy is a private broker with no connection to the Army. See the <a href="military-car-shipping.html">military</a> page for how orders set the window.'),
  P('The university downtown takes thirty-five thousand students, and the cars arrive in mid-August. A parent sets it up, and someone over eighteen signs at the lots on Assembly or Bluff Road. The cars leave in May. The two colleges on the north side move their students the same weeks. The State House and the agencies around it relocate employees with every administration.'),
  P('The hospital system downtown, the veterans hospital, and the one across the river bring residents each June. They hire traveling nurses year round. The electric truck plant in Blythewood is hiring engineers from Detroit and Germany on start dates. The insurance offices on the Northeast relocate staff from the Midwest. The handoff happens in the lot nearest the office.'),
  P('Retirees come to the lake and to the Northeast and go to Florida in the winter. What a state line adds is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Football Saturdays, Move-In Week, Graduation Thursdays, the State Fair, Soda City, the Floods, the Ice, the Heat, and the Evacuations',
 prose(
  L('Columbia runs on an Army calendar and a football calendar. The weather problem is a flood or an ice storm every few years. The summer is what the city calls famously hot.'),
  P('Football Saturdays close Bluff Road and the fairgrounds from the morning on. The carriers stay off the south side until the stadium empties. Move-in week in mid-August fills the campus blocks and Five Points. Graduation Thursdays at the fort fill Garners Ferry with families. The State Fair runs twelve days in October and takes the fairgrounds lots with it. Soda City closes Main Street every Saturday morning. Book three weeks ahead for a date in mid-August or a home game.'),
  P('The October 2015 flood dropped twenty inches of rain in three days. Gills Creek took out the dams on the east side, and the canal breach cut the city’s water. Forest Drive and Garners Ferry closed for weeks. A flood watch on Gills Creek moves the handoff off the creek roads. The February 2014 ice storm dropped a half inch of ice. Most of the city lost power for three days. The carriers wait a day for the limbs to come down and the roads to clear.'),
  P('A hurricane on the coast reverses 26 and sends Charleston to Columbia, and the carriers come with it. Hugo in 1989 reached the city with hurricane winds. We hold the car on the lot until the lanes reopen and call when they do. The summer heat holds in the upper nineties for weeks, and a driver loads in the morning.'),
  P('Tornadoes cross the county a few times a decade. A warning holds the truck at the lot until it lifts.'),
 )+chips(["Downtown","The Vista","Five Points","Shandon","Rosewood","Olympia","Wales Garden","Heathwood","Forest Acres","Arcadia Lakes","The Northeast","Spring Valley","Eau Claire","North Columbia","Earlewood","Elmwood Park","The BullStreet District","Cottontown","West Columbia","Cayce","Lexington","Irmo","Chapin","Blythewood","Elgin"])
 +NOTE('Serving Columbia, Lexington, and the Midlands, Shandon curb or Lake Murray cul-de-sac. Let us know the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Columbia?',
 prose(
  L('The Midlands ship open most of the time, and the table above is figured that way.'),
  P('Enclosed keeps the pollen, the sap, and the summer sun off the paint. Heathwood collectors book it. So do the engineers moving a car from Germany worth more than the rest of the household. When a hurricane evacuation is in the forecast, the car rides the first truck with room. We say so first.'),
  P('A commuter car or a soldier’s pickup goes open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages weigh one against the other.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure up front, a lot off 77 or 26, and a signature at the far end. Orders or the move-in set the week.'),
  P('Accept the figure, and we place the car with a carrier already running 77 that week. The lot and the window are agreed that afternoon. The driver photographs the car at pickup and enters its condition on the Bill of Lading. You initial the sheet, and it is the reference at delivery.'),
 )+ULI([
  "Cabin and trunk cleared out",
  "Fuel down to a quarter tank",
  "Your own photos of each side and the odometer",
  "A key that works and a note on known faults",
  "Aftermarket alarms off",
  "In the Vista, Five Points, or on the campus blocks, expect a main road or a garage entrance",
 ])+prose(P('Every step is on the <a href="how-it-works.html">how it works</a> page, and pickup day is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Columbia Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 77 and 26 every day. We know which gate the fort opens for a pickup and which Saturdays close Bluff Road.'),
  P('Our FMCSA license and our $75,000 bond are on the federal register, open to anyone. The office is on Pickens Street in the BullStreet District.'),
  P('You get one coordinator from the quote to the delivery call, not a queue. The <a href="services.html">services</a> page covers open, enclosed, and expedited.'),
 )))

BODY.append(office('Columbia','2191 Pickens St Suite 533','Columbia, SC 29201','+18037212691','(803) 721-2691','ET',
 '2191+Pickens+St+Suite+533,+Columbia,+SC+29201','Visit Us','Find Ship Guy in Columbia',
 'Our office is on Pickens Street in the BullStreet District, beside the ballpark north of the State House.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4082.080435655787!2d-81.03423830000001!3d34.0181629!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88f8a5d820f77da3%3A0x62628c1b7681f7b5!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793631556521!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Columbia to Charlotte or Atlanta?","Charlotte runs one hundred seventy to two hundred eighty dollars for a sedan. That is about ninety-five miles up 77. Atlanta runs two hundred thirty to three hundred fifty, about two hundred fifteen miles down 20. Augusta is the lowest lane on the table, about seventy-five miles. SUVs and pickups add 10 to 25 percent."),
 ("Do you ship cars for Fort Jackson PCS moves?","Yes, in every month of the year. The drill sergeants, the cadre, and the permanent party PCS in and out on orders. We plan the pickup around the report date. The handoff happens at the Garners Ferry lots or outside Gate 2. Trainees do not bring cars. Ship Guy is a private broker and not part of the Army."),
 ("Can the carrier come to my street in Shandon or Five Points?","Shandon, usually, where the oak limbs clear the trailer. Five Points, no. The streets are tight and the student apartments fill both curbs. The driver meets you on Harden Street. Forest Acres, the Northeast, Lexington, and Irmo allow the curb outside a covenant."),
 ("Can you deliver on a University of South Carolina move-in date?","Yes. Cars arrive in mid-August and leave in May. A parent books, and an adult signs at the lot. The campus blocks and Five Points are full that week. The meeting point is the lots on Assembly or Bluff Road. The date fixes the window."),
 ("What happens on a football Saturday or during the State Fair?","The south side closes. Bluff Road and the fairgrounds lots fill from the morning on a home Saturday. The fair takes the fairgrounds for twelve days in October. The handoff moves to the Harbison or Two Notch lots, and the figure does not change. Book three weeks ahead for those weeks."),
 ("What happens if a flood, an ice storm, or a hurricane evacuation hits on my pickup day?","The truck waits a day. The 2015 flood closed Forest Drive and Garners Ferry for weeks. The 2014 ice storm took the power for three days. A coastal hurricane reverses 26 and sends Charleston to Columbia. We call when the forecast turns. The pickup takes the first open morning after, and the figure holds."),
 ("Do you ship cars for the hospitals or the truck plant?","Yes, in every season. The hospital system downtown, the veterans hospital, and the hospital in West Columbia bring residents each June. The traveling nurses come in every season. The truck plant in Blythewood hires engineers on start dates. The handoff happens at the lots nearest the office. Employers that reimburse get the paperwork they ask for."),
 ("Can you ship a car to or from Lexington, Irmo, or Sumter?","Yes. West Columbia, Cayce, Lexington, Irmo, and Forest Acres ride the same carriers and price the same as Columbia. Sumter, Orangeburg, and Camden add an hour on the truck and a few dollars. The lake cul-de-sacs meet the truck at the entrance when a covenant bans trailers."),
 ("Can you ship a car that does not run from Columbia?","Yes. A winch truck handles it, and the loading time is built into the figure. The big-box lots on Harbison and Two Notch are flat. We only need to know whether it rolls, steers, and brakes."),
 ("What do you need for a Columbia car shipping quote?","The two addresses, with the neighborhood. The year, make, and model, and whether it runs. Open or enclosed, and the week around the orders or the move. Send those, and the Columbia figure is back the same day."),
]
BODY.append(faq_section(FAQ,'Columbia FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Columbia?','Two minutes on the form above gets a Columbia figure on your lane. Give the neighborhood and the week, and a carrier already on 77 takes the car.','+18037212691','(803) 721-2691','Get your free Columbia quote'))

build({
 'slug':'auto-transport-columbia-south-carolina',
 'title':'Car Shipping in Columbia, SC — Auto Transport | Ship Guy',
 'meta':'Car shipping in Columbia, SC, the capital where 26, 20, and 77 meet. Fort Jackson PCS moves, University of South Carolina dates, hospital and truck-plant hires, main-road handoffs for the Vista, Five Points, and the campus, curbside pickups in Shandon, Forest Acres, Lexington, and Irmo, the floods, the ice, and football Saturdays. Local office on Pickens Street. Free quote.',
 'h1':'Car Shipping in<br>Columbia, <span class="accent">South Carolina</span>',
 'lede':'Open, enclosed, and expedited auto transport across Columbia and the Midlands, planned around 26, 20, 77, the fort’s orders, the campus dates, the football Saturdays, and the storms.',
 'tel':'+18037212691','disp':'(803) 721-2691','brand':'Columbia','keyword':'car shipping in columbia',
 'localterms':['columbia','capital','interstate 26','interstate 20','interstate 77','126','spur','malfunction junction','highway 277','378','elmwood','gervais','assembly','harden','devine','garners ferry','forest drive','two notch','bluff road','broad river','harbison','st. andrews','clemson road','north main','rosewood drive','state house','1786','river','the vista','five points','shandon','rosewood','olympia','wales garden','heathwood','forest acres','arcadia lakes','the northeast','spring valley','eau claire','north columbia','earlewood','elmwood park','bullstreet district','cottontown','ballpark','asylum','pickens street','west columbia','cayce','lexington','irmo','chapin','blythewood','elgin','sumter','orangeburg','camden','lake murray','lake','covenants','oaks','limbs','fort jackson','army','trainees','drill sergeants','cadre','permanent party','orders','pcs','gate 2','graduation thursdays','university','thirty-five thousand','students','colleges','state government','agencies','administration','hospital system','veterans hospital','residents','traveling nurses','truck plant','electric','engineers','detroit','germany','insurance offices','midwest','retirees','florida','football saturdays','stadium','fairgrounds','move-in','state fair','soda city','main street','october 2015','twenty inches','gills creek','dams','canal breach','february 2014','ice storm','half inch','hugo','1989','hurricane','evacuation','reverses','famously hot','upper nineties','tornadoes','pollen','sap','augusta','charlotte','charleston','fayetteville','savannah','atlanta','raleigh','jacksonville','washington','new york','convention center','airport','farmers market','mill houses','cobbled','bill of lading','fmcsa','winch','fly-and-ship','2030'],
}, BODY, FAQ)
