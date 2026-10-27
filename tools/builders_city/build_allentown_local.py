import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Allentown, Pennsylvania','Car shipping in the Lehigh Valley, ninety minutes from New York on Interstate 78 and an hour from Philadelphia',
 ['Car shipping in Allentown runs off Interstate 78 across the south side and Route 22 across the north. Ship Guy is a licensed auto transport broker with an office on Hausman Road in the West End.',
  'We book vetted carriers across the Lehigh Valley, from Trexlertown and Emmaus to Bethlehem, Easton, and Whitehall. The trucks belong to the carriers, and we hold the authority and the bond.',
  'Interstate 78 runs from Harrisburg through the valley to New Jersey and New York. Route 22 is the local freeway across the north side. Route 309 runs north to the Poconos, and the Turnpike’s Northeast Extension passes the west side. Hamilton Street is downtown, and MacArthur Road is the retail strip.',
  'This page covers 78, 22, 309, the row-house blocks, the West End, the warehouse corridor, Bethlehem, and Easton. It also covers the health network, the colleges, the truck plant, the commute, the fair, and the lanes.'],
 'Allentown at a glance',
 ['Most pickups happen within 1 to 3 days. The New York carriers come out 78 every day. The Philadelphia and Harrisburg trucks arrive on the Turnpike and 22.',
  'New York, Philadelphia, Harrisburg, Baltimore, and Washington are a same-day haul. Hartford, Boston, and Pittsburgh take a day. Charlotte takes one to two, and Florida takes three.'],
 'Tell us the township or the borough. The row-house blocks in center city, the East Side, and the old boroughs need a meeting spot. The West End, the township subdivisions, and the warehouse corridor usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 78, Route 22, Route 309, the Northeast Extension, Route 100, and MacArthur Road',
 prose(
  L('Allentown sits on the road between New York and Harrisburg, and the trucks never stop coming.'),
  P('Interstate 78 crosses the south side of the valley from Harrisburg to the Delaware River and New Jersey. The exits at Hamilton Boulevard, Cedar Crest, Lehigh Street, and Route 412 serve the valley. Every carrier between New York and the Midwest rides it. The state closes it to trucks in a big storm. Route 22 is the Lehigh Valley Thruway, the local freeway across the north side from Fogelsville to Easton.'),
  P('Route 309 runs north from Quakertown through the west side to the Poconos. The Turnpike’s Northeast Extension is Interstate 476, with the valley exit at Route 22. Its toll rides inside the quote. Route 33 runs from 22 to Stroudsburg and Interstate 80. Route 100 runs the warehouse corridor through Trexlertown and Fogelsville to 78.'),
  P('Hamilton Street runs through downtown past the arena. Tilghman Street and Cedar Crest Boulevard cross the West End. MacArthur Road is Route 145, the retail strip north through Whitehall. Lehigh Street climbs the south side, and Union Boulevard runs the East Side. The Lehigh River splits the city, and the Hamilton Street and Tilghman Street bridges set the crossings.'),
  P('The carriers come off 78 at Lehigh Street and Cedar Crest, and off 22 at MacArthur. The mall lots in Whitehall and the shopping centers on Hamilton Boulevard are the usual meeting spots. The lots at the Route 100 warehouses work too. The ballpark lots on the East Side work outside game nights.'),
  P('Our office is on Hausman Road in the West End, minutes from the 78 and 309 exits.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Center City, the West End, the East Side, the South Side, Whitehall, Trexlertown, Emmaus, Bethlehem, and Easton',
 prose(
  L('Allentown is a row-house city with townships growing around it. The newer the street, the easier the truck.'),
  P('Center city is a grid of row houses between the river and 15th Street. The arena and the office towers sit on Hamilton. The streets are narrow, one-way, and parked solid. The driver meets you at the arena garage exits or at the lots on American Parkway. The East Side across the river is more row houses and the ballpark. The handoff moves to the ballpark lots or Union Boulevard.'),
  P('The West End between 15th Street and Cedar Crest is 1920s and 1930s houses on wider streets. The college and the fairgrounds sit in it. The curb works on most blocks outside fair week. The South Side up Lehigh Street is older grids on the hill. The driver meets you on Lehigh. The township streets off Cedar Crest and Hamilton Boulevard are wide, and the driver reaches the house.'),
  P('Whitehall to the north is the mall district and postwar grids off MacArthur. The curb works on the side streets. Trexlertown, Breinigsville, and Fogelsville to the west are the warehouse corridor and the newest subdivisions. The streets are wide everywhere. Emmaus and Macungie to the south are old boroughs with a Main Street a trailer avoids. The new subdivisions behind them allow the curb.'),
  P('Bethlehem is its own city ten minutes east, with the steel stacks and the university on the hill. Its South Side is narrow streets. The driver meets you at the casino lots or on the Boulevard. Easton sits at the Delaware with the college on the hill and the Circle downtown. The handoff moves to Route 22. Nazareth, Hellertown, and Catasauqua are small boroughs in between. All of them price the same as Allentown.'),
 )))

ROUTES=[("Philadelphia, PA","I-476/I-76 · ~60 mi","Same day","$150–$240"),("Harrisburg, PA","I-78 · ~80 mi","Same day","$150–$240"),
 ("New York, NY","I-78 · ~90 mi","Same day","$170–$280"),("Baltimore, MD","I-78/I-83 · ~160 mi","Same day","$210–$320"),
 ("Hartford, CT","I-78/I-287/I-84 · ~190 mi","Same day","$220–$340"),("Washington, DC","I-78/I-83/I-95 · ~200 mi","Same day","$230–$350"),
 ("Pittsburgh, PA","I-78/I-76 · ~280 mi","1 day","$270–$400"),("Boston, MA","I-78/I-84/I-90 · ~290 mi","1 day","$270–$400"),
 ("Charlotte, NC","I-78/I-81/I-77 · ~560 mi","1–2 days","$440–$630"),("Orlando, FL","I-95 · ~1,050 mi","3 days","$720–$1,020")]
BODY.append(rate_table('Lanes &amp; Costs','Allentown Car Shipping Lanes and Estimated Costs',
 'The lanes Lehigh Valley cars run most often, with estimated open-trailer ranges. Put your own route on the form above for a number.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Allentown, running sedan, open trailer. SUVs and pickups run 10 to 25 percent more, enclosed more still. Turnpike tolls are built in. The season and the carriers free on your dates set the final number.',
 prose(
  P('Allentown prices with Philadelphia on every lane and a little under it to New York. Interstate 78 puts the valley closer. The New York lane runs all day in both directions, and the New Jersey suburbs price the same. The Harrisburg lane rides 78 west and runs daily. The Florida lane fills with retirees each fall.'),
  P('A move timed to a Manhattan start date or an August move-in ships with the heaviest weeks. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Health Network, the Warehouses, the Colleges, the Truck Plant, the Gas Company, and the New York Commute',
 prose(
  L('Allentown relocates nurses, warehouse managers, students, and families priced out of New Jersey. The health network at Cedar Crest moves more people than anyone in the valley.'),
  P('The health network at Cedar Crest is the largest employer in the region. It hires nurses on contracts all year and takes residents each June. The physicians come with a closing date and a second car. The second hospital system in Bethlehem and Fountain Hill hires the same way. We handle the paperwork when an employer pays for the move.'),
  P('The distribution centers along 78 and Route 100 form one of the biggest warehouse clusters in the Northeast. They move managers in on start dates and rotate them between sites. The truck plant in Macungie and the industrial gas company off Hamilton Boulevard move engineers on program schedules. The utility downtown and the imaging company in Center Valley hire from every state.'),
  P('The West End college, the university in Bethlehem, and the college in Easton take cars each August. The campuses in Center Valley and Kutztown do the same. A parent books it, and an adult signs for the car at a campus lot. The community college in Schnecksville runs the same calendar.'),
  P('Families from New Jersey and New York buy in the townships on closing dates and keep the commute. One car rides the trailer while the other is driven. Retirees leave for Florida and the Carolinas each fall. The Army depot in the Poconos rotates civilians on program dates. Ship Guy is a private broker with no tie to it. The <a href="military-car-shipping.html">military</a> page has the timing, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page has the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Fair, Musikfest, the Ballpark, Christmas City, the Nor’easters, and the 78 Shutdowns',
 prose(
  L('Allentown runs on a fair in its own West End and a ten-day music festival next door. The winter shuts 78 to trucks.'),
  P('The fair fills the fairgrounds at 17th and Chew for the week before Labor Day. The West End streets around it are closed or full. A West End handoff that week moves to the mall lots in Whitehall. Musikfest fills Bethlehem for ten days in August, and the bridges and the South Side streets close. The Christmas markets fill Bethlehem every weekend in December.'),
  P('The ballpark on the East Side fills its lots on game nights from April through September. The arena downtown fills the garages on hockey nights and concert nights. The amusement park on Hamilton Boulevard fills the road on summer weekends. A handoff near any of them moves to the daytime.'),
  P('Winter brings thirty inches of snow and a nor’easter or two. The January 2016 blizzard dropped thirty inches in a day. The November 2018 storm trapped trucks on 78 for twelve hours. The state closes 78 to commercial traffic in a big storm. The carriers wait in Harrisburg or New Jersey until it reopens. A winter pickup can lose a day, and you hear it from us first.'),
  P('The Lehigh floods the low ground in a wet storm. Ida in 2021 put the river roads under water, and Diane in 1955 is still the measure. A pickup on the river flat moves up the hill. Summer brings ninety degrees and a storm most afternoons. The sirens are rare.'),
 )+chips(["Center City","Hamilton Street","PPL Center","West End","Hausman Road","Tilghman Street","Cedar Crest","East Side","Union Boulevard","South Side","Lehigh Street","Whitehall","MacArthur Road","Trexlertown","Breinigsville","Fogelsville","Route 100","Emmaus","Macungie","Center Valley","Coopersburg","Schnecksville","Catasauqua","Bethlehem","Fountain Hill","Hellertown","Nazareth","Easton","Kutztown","Quakertown"])
 +NOTE('Serving Allentown, Bethlehem, Easton, and all of the Lehigh Valley, row-house block or township cul-de-sac. Tell us the township and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Allentown?',
 prose(
  L('Open trailers move most Lehigh Valley cars, and the lane table above is priced for one.'),
  P('An enclosed trailer keeps off the road salt, the cinders, and the gravel from the quarries. The collectors who fill the Macungie car shows book one. Executives relocating a new car to the gas company or the health network book one too.'),
  P('A commuter car or a warehouse pickup rides open and shows up as it went on. See the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages for the trade-off.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot in Whitehall or on Hamilton Boulevard, and a signature at the far end. The start date or the closing picks the week.'),
  P('Say the word, and the car is assigned to a carrier already running 78. The lot and the window are confirmed the same afternoon. You and the driver go over the car before it loads. Existing marks go on the Bill of Lading, and two signatures close it. The same page is compared at delivery.'),
 )+ULI([
  "Cabin and trunk emptied of personal items",
  "Fuel at a quarter tank or so",
  "Photos of all four sides and the mileage before pickup",
  "One key that works, and a note on any fault, for the driver",
  "Any aftermarket alarm disabled",
  "On a row-house block, meet the truck at the arena garages or on American Parkway",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Allentown Drivers Choose Ship Guy',
 prose(
  L('We book the carriers already running 78 between New York and Harrisburg. We watch the fair week, the storm closures, and the Turnpike.'),
  P('Ship Guy is licensed as a broker by the FMCSA and bonded for $75,000. Both filings are public. Our office is on Hausman Road in the West End.'),
  P('The person who prices the move is the person who closes it. Open, enclosed, and expedited transport are spelled out on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Allentown','1320 Hausman Rd #473','Allentown, PA 18104','+16108397989','(610) 839-7989','ET',
 '1320+Hausman+Rd+%23473,+Allentown,+PA+18104','Visit Us','Find Ship Guy in Allentown',
 'Our office is on Hausman Road in the West End, minutes from the 78 and 309 exits.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4658.174145576984!2d-75.56589610000002!3d40.60355010000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c43106d351cbab%3A0xa8da398fc536a7e3!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793103567178!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Allentown to New York or Florida?","New York runs one hundred seventy to two hundred eighty dollars for a sedan. That is about ninety miles out 78. Orlando runs seven hundred twenty to a thousand twenty, about a thousand fifty miles down 95. Philadelphia is an hour down the Turnpike and the lowest of the three. SUVs and pickups run 10 to 25 percent more."),
 ("Can the carrier come to my street in center city or on the East Side?","Usually not. The row-house blocks are narrow, one-way, and parked solid. The driver meets you at the arena garage exits, on American Parkway, or at the ballpark lots. The West End, the township subdivisions, Whitehall, and the warehouse corridor usually allow the curb."),
 ("Do you ship cars for people relocating to the health network or the warehouses?","Yes, every month. The health network at Cedar Crest hires nurses on contracts all year and takes residents each June. The distribution centers along 78 and Route 100 move managers in on start dates. A second car usually follows the move on a trailer. We handle the paperwork when an employer pays for the move."),
 ("Can you deliver on the Lehigh, Lafayette, or Muhlenberg move-in date?","Yes. The campuses take cars in each August and send them home in May. A parent books it, and an adult signs for the car at a campus lot. The window follows the move-in date and moves if it does. The hill in Bethlehem is tight that week, so the handoff happens at the lots on the Boulevard."),
 ("Does the fair or Musikfest affect my pickup?","In the West End and in Bethlehem, yes. The fair fills the fairgrounds at 17th and Chew for the week before Labor Day. Musikfest closes the bridges and the South Side streets in Bethlehem for ten days in August. We move a handoff near either to the mall lots in Whitehall or to the week before. The townships run normally."),
 ("Can you ship a car to or from Bethlehem, Easton, or Emmaus?","Yes, and all three price the same as Allentown. Bethlehem rides the same carriers off 78 and 22, and the casino lots are the usual handoff. Easton rides them off 22 at the Delaware, and the driver meets you off the Circle. Emmaus rides them off 29, and the new subdivisions allow the curb. Send the full address for a township street."),
 ("Is the Turnpike toll in my price?","Yes. A carrier that uses the Northeast Extension pays by the mile with a transponder. The toll rides inside the quote. There is no separate line. Interstate 78, Route 22, Route 309, and the valley roads carry no toll."),
 ("What happens if a storm closes 78 on my pickup day?","The state closes 78 to commercial traffic in a big storm. The carriers wait in Harrisburg or New Jersey until it reopens. A winter pickup can lose a day, and you hear it from us first. The November 2018 storm trapped trucks on the road for twelve hours. We plan around a forecast like it."),
 ("Can you ship a car that does not run from Allentown?","Yes. A winch-equipped truck is assigned, and the loading time is already in the quote. The mall lots in Whitehall or the shopping centers on Hamilton Boulevard give the driver level pavement. Say whether the car rolls, steers, and brakes."),
 ("What do you need for an Allentown car shipping quote?","The two addresses, with the borough or the township named. The year, make, and model. Whether it runs. Open or enclosed. The week around the start date or the closing. Nothing more, and the Allentown number is back the same day."),
]
BODY.append(faq_section(FAQ,'Allentown FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Allentown?','The form above quotes the lane in about two minutes. Give us the township and the week, and a carrier already on 78 takes it.','+16108397989','(610) 839-7989','Get your free Allentown quote'))

build({
 'slug':'auto-transport-allentown-pennsylvania',
 'title':'Car Shipping in Allentown, PA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Allentown, PA, in the Lehigh Valley on Interstate 78, ninety minutes from New York. Health-network and warehouse relocations, college move-in timing, arena-garage handoffs for the row-house blocks, curbside pickups in the West End and the townships, Bethlehem and Easton, the fair, Musikfest, and the 78 storm closures. Local office on Hausman Road. Free quote.',
 'h1':'Car Shipping in<br>Allentown, <span class="accent">Pennsylvania</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Lehigh Valley, planned around 78, Route 22, the row-house blocks, the New York commute, and the winter.',
 'tel':'+16108397989','disp':'(610) 839-7989','brand':'Allentown','keyword':'car shipping in allentown',
 'localterms':['allentown','lehigh valley','interstate 78','route 22','hausman road','west end','trexlertown','emmaus','bethlehem','easton','whitehall','harrisburg','new jersey','new york','route 309','poconos','turnpike','northeast extension','hamilton street','macarthur road','downtown','row-house','east side','warehouse corridor','health network','colleges','truck plant','commute','fair','snow','philadelphia','baltimore','washington','hartford','boston','pittsburgh','charlotte','florida','township','borough','center city','delaware river','hamilton boulevard','cedar crest','lehigh street','route 412','midwest','thruway','fogelsville','quakertown','interstate 476','toll','route 33','stroudsburg','interstate 80','route 100','arena','tilghman street','route 145','union boulevard','lehigh river','bridges','mall','ballpark','game nights','american parkway','15th street','office towers','one-way','college','fairgrounds','hill','breinigsville','macungie','main street','steel stacks','university','casino','the boulevard','the circle','nazareth','hellertown','catasauqua','nurses','warehouse managers','students','distribution centers','start dates','residents','physicians','fountain hill','industrial gas','utility','imaging company','center valley','kutztown','schnecksville','community college','retirees','carolinas','army depot','musikfest','christmas','17th and chew','labor day','amusement park','hockey','concert','thirty inches','nor’easter','january 2016 blizzard','november 2018','twelve hours','commercial traffic','ida','2021','diane','1955','ninety degrees','sirens','cinders','quarries','car shows','bill of lading','fmcsa','coopersburg','ppl center'],
}, BODY, FAQ)
