import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Bethlehem, Pennsylvania','Car shipping in the Christmas City, between the old steel plant and the warehouses on 78',
 ['Car shipping in Bethlehem runs on Interstate 78 and Route 22, which bracket the city north and south. Ship Guy is a licensed auto transport broker with an office on Lynn Avenue on the South Side.',
  'We book vetted carriers across Bethlehem and the Lehigh Valley, from the Moravian district to Hellertown and Nazareth. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 78 runs along the south edge of the city between Harrisburg and New York. Route 22 runs along the north edge from Allentown to Easton. Route 378 crosses the city on the Hill-to-Hill Bridge, and Route 412 reaches 78 from the South Side. Route 33 leaves the east side for the Poconos.',
  'This page covers 78, 22, 378, 412, downtown, the South Side, the Moravian district, and the valley towns. It also covers the universities, the hospital, the device maker, the casino, the warehouses, Musikfest, and the ice.'],
 'Bethlehem at a glance',
 ['Most pickups happen within 1 to 3 days. The New York-to-Harrisburg carriers pass the city on 78 every day. The Philadelphia trucks come up 476 and 309.',
  'Philadelphia, Newark, New York, and Harrisburg are same-day runs. So are Baltimore, Hartford, and Washington. Pittsburgh and Boston need a day, and Florida needs three.'],
 'Tell us the neighborhood and whether the street is one-way. The Moravian district, the South Side rowhouse blocks, and the campus hill meet the truck at a lot. West Bethlehem, Bethlehem Township, Hanover Township, Hellertown, and Lower Saucon usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 78, Route 22, Route 378, Route 412, Route 33, Route 512, the Hill-to-Hill Bridge, the Fahy Bridge, and Broad Street',
 prose(
  L('Bethlehem is two cities on two banks of the Lehigh with a mountain behind each. A carrier reaches the flats from 78 or 22 and the hills from a lot.'),
  P('Interstate 78 is the New York-to-Harrisburg road. It runs along the south edge of the city past Hellertown and leaves east for the Delaware. The New York carriers ride it every day. The Philadelphia carriers come up 476 and 309 to meet it. The February 2007 ice storm shut it for a day and stranded hundreds of trucks. A carrier waits in Allentown when the state closes it.'),
  P('Route 22 is the old valley highway along the north edge, from Allentown past the airport to Easton. It jams both rush hours and backs up at every merge. Route 378 comes down from 22 through West Bethlehem and crosses the river on the Hill-to-Hill Bridge. Then it climbs the South Side to 78. Route 412 runs from the South Side through Hellertown to 78. Route 33 leaves the east side for Nazareth and the Poconos. Route 512 is Center Street, north to the airport.'),
  P('The carriers come off 78 at 412 or 378 and off 22 at Center Street or Airport Road. The casino lots on the old plant site are the usual meeting spot. The big-box lots on Route 33 and the mall lots on Route 22 work too. So do the stadium lots on the hill outside game days. The airport lots work for a fly-and-ship.'),
  P('Our office is on Lynn Avenue on the South Side, off Route 412 and minutes from 78.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Moravian District, Center City, West Bethlehem, the South Side, the Campus Hill, Fountain Hill, Bethlehem Township, Hanover Township, Hellertown, and the Valley Towns',
 prose(
  L('Bethlehem is colonial stone on narrow streets by the river and steelworkers’ rowhouses on the far bank. The truck meets both at the edge.'),
  P('The Moravian district along Main and Church Streets is the oldest part of the city. The stone buildings sit on streets laid out in 1741. A trailer does not enter, and the city closes the blocks for every festival. The driver meets you at the lots on Broad Street or across the bridge. Center City along Broad Street is brick storefronts and angled parking. The handoff happens on the same lots.'),
  P('West Bethlehem across Eighth Avenue is tree-lined streets of older houses, and the curb sometimes works. The South Side across the Fahy Bridge is the steel neighborhood. Rowhouses line narrow one-way streets from Third Street to the hill. The driver meets you on Third or Fourth Street or at the casino lots. The campus climbs the hill above it on streets a trailer cannot turn in. The handoff moves to the stadium lots or the bottom of the hill.'),
  P('Fountain Hill beside the hospital is the same rowhouses on the same narrow streets. Bethlehem Township to the east along Freemansburg Avenue is wide subdivisions and big-box lots. The driver reaches the house. Hanover Township to the north around the airport is office parks and newer streets with the same answer. Freemansburg down by the river is tight again.'),
  P('Hellertown and Lower Saucon over the mountain are wide suburbs where the curb works. Nazareth up 33, Easton down 22, and Allentown next door ship with the same trucks. All of them price the same as Bethlehem. Center Valley and Coopersburg down 309 do too. Easton adds ten minutes and nothing else.'),
 )))

ROUTES=[("Philadelphia, PA","PA-309/I-476 · ~65 mi","Same day","$150–$240"),("Newark, NJ","I-78 · ~75 mi","Same day","$160–$260"),
 ("New York, NY","I-78 · ~85 mi","Same day","$170–$280"),("Harrisburg, PA","I-78/I-81 · ~90 mi","Same day","$150–$240"),
 ("Baltimore, MD","I-78/I-83 · ~165 mi","Same day","$210–$320"),("Hartford, CT","I-78/I-287/I-84 · ~185 mi","Same day","$220–$340"),
 ("Washington, DC","I-78/I-83/I-95 · ~205 mi","Same day","$230–$350"),("Boston, MA","I-78/I-84/I-90 · ~285 mi","1 day","$270–$400"),
 ("Pittsburgh, PA","I-78/I-76 · ~290 mi","1 day","$270–$400"),("Orlando, FL","I-95 · ~1,045 mi","3 days","$720–$1,020")]
BODY.append(rate_table('Lanes &amp; Costs','Bethlehem Car Shipping Lanes and Estimated Costs',
 'The lanes Lehigh Valley cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Bethlehem, running sedan, open trailer. An SUV or a pickup adds about 10 to 25 percent, and enclosed adds more. The week you choose and the carriers free on 78 that week set the final number.',
 prose(
  P('Bethlehem prices with Allentown on every lane, because the same trucks serve the whole valley. The New York and Newark lanes ride 78 east and fill every day. The Philadelphia lane rides 309 and 476 south. The Baltimore and Washington lanes ride 78 west to 83. The Florida lane fills each fall with the valley’s retirees, and the New England lanes fill each spring.'),
  P('A late August move-in or a Musikfest week lands in the busiest days of the year. What size, condition, and timing do to the number is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Universities, the Hospital, the Device Maker, the Casino, the Warehouses, the Commuters, and the Retirees',
 prose(
  L('Bethlehem relocates professors, nurses, engineers, dealers, and warehouse managers. The universities and the hospital move the most.'),
  P('Student cars reach the hill in late August and leave in May. The university on the north side runs the same calendar. The community college in the township follows a week later. Mom or Dad books, and an adult signs at a lot. The campus hill is closed to a trailer in move-in week. The meeting point is the stadium lots.'),
  P('The hospital network headquartered in Fountain Hill is the largest employer in the valley. It brings residents each June and hires traveling nurses year round. The other network’s campus on the north side does the same. The medical device maker with its headquarters on the South Side moves engineers on project dates. So do the diagnostics company beside it and the candy maker on Stefko. When an employer reimburses the move, we produce the receipts it needs.'),
  P('The casino on the old plant site moves dealers and managers on opening schedules. The warehouses along 78 and 33 relocate managers on start dates every month. Commuters to New York and Philadelphia buy in the valley for the prices. They ship one car behind the moving truck. The second car usually rides a trailer. The Guard post at Indiantown Gap sends a few families east on orders. Ship Guy is a private broker with no connection to it. The <a href="military-car-shipping.html">military</a> page covers the timing.'),
  P('The retirees go to Florida in October and return in April. Families moving over the mountain to Hellertown ship one car and drive the other. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for an interstate move.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Musikfest, Christkindlmarkt, the Celtic Classic, Move-In Week, the Rivalry, the Nor’easters, the Ice, and the River',
 prose(
  L('Bethlehem runs on a festival calendar and a campus calendar. The weather problem is ice on the hills and water in the creek.'),
  P('Musikfest closes the Moravian district and the South Side waterfront for ten days in early August. A million people come, and the bridges crawl from noon to midnight. A handoff anywhere near downtown moves to the week before or the week after. Christkindlmarkt fills the plant site from Thanksgiving to Christmas. The Christmas City lights fill Main Street every December weekend. The Celtic Classic closes downtown for a weekend in late September.'),
  P('Move-in week in late August packs the hill and the north side campus. The rivalry game in November fills the stadium on the hill every other year. The other years it fills the roads to Easton. The valley fair in Allentown fills Route 22 for a week in late August. A handoff near any of them moves to the next morning.'),
  P('Winter drops thirty inches of snow on the valley and more ice than its hills can take. The campus hill, the Wyandotte hill on 378, and Fountain Hill close to a trailer until it melts. The January 2016 storm dropped thirty inches and shut the valley for three days. The carriers wait in Allentown or on the Jersey side of 78 until the roads clear. A winter pickup can slip a day, and the word comes from us before the driver.'),
  P('The Monocacy runs through the Moravian district, and it floods in a hurricane’s remnants. Ida in September 2021 put the historic quarter and the creek-side lots under for two days. Irene and Lee in 2011 did the same. A pickup in the district or along the creek waits for the water to drop. The handoff moves to Broad Street. Summer brings heat and the odd storm that shifts the loading hour.'),
 )+chips(["Moravian District","Main Street","Center City","Broad Street","West Bethlehem","Eighth Avenue","South Side","Third Street","Fourth Street","Campus Hill","SteelStacks","Fountain Hill","Saucon Park","Bethlehem Township","Freemansburg Avenue","Hanover Township","Airport","Freemansburg","Hellertown","Lower Saucon","Center Valley","Coopersburg","Nazareth","Easton","Allentown","Emmaus"])
 +NOTE('Serving Bethlehem and the whole Lehigh Valley, South Side rowhouse or Hellertown cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Bethlehem?',
 prose(
  L('Most Lehigh Valley cars travel on an open trailer, and the table above is priced for one.'),
  P('An enclosed trailer keeps off four months of salt and brine and the cinders of a mountain winter. The collectors in West Bethlehem book one. So do the executives bringing a new car to the headquarters on the South Side. A car headed to Florida ahead of the first ice often rides enclosed too.'),
  P('A commuter car or a student car has no need of a roof. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain where enclosed earns its price.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a meeting spot at the casino, and a signature at delivery. The move-in date or the start date picks the week.'),
  P('Approve the price, and a carrier already riding 78 that week takes the car. We confirm the lot and the window before the day ends. At pickup the driver circles the car with you and marks every blemish on the Bill of Lading. You countersign, and the delivery inspection is checked against those marks.'),
 )+ULI([
  "Personal things out of the car, glovebox and trunk included",
  "Roughly a quarter tank of gas",
  "Snap each side and the mileage the morning of pickup",
  "A key that works, plus a note about anything that leaks",
  "Aftermarket alarm switched off",
  "In the Moravian district, on the South Side, or on the hill, plan on a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps. The <a href="car-shipping-preparation.html">preparation</a> page has the full checklist.'))))

BODY.append(sec('Why Ship Guy','Why Bethlehem Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already ride 78 and 22 through the valley every day. We know which streets the festivals close.'),
  P('The federal register shows our FMCSA license and our $75,000 bond to anyone who looks. The office is on Lynn Avenue on the South Side.'),
  P('The coordinator who quotes the move stays with it until the car is delivered. The <a href="services.html">services</a> page puts open, enclosed, and expedited side by side.'),
 )))

BODY.append(office('Bethlehem','1349 Lynn Ave #547','Bethlehem, PA 18015','+16106157620','(610) 615-7620','ET',
 '1349+Lynn+Ave+%23547,+Bethlehem,+PA+18015','Visit Us','Find Ship Guy in Bethlehem',
 'Our office is on Lynn Avenue on the South Side, off Route 412 and minutes from 78.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3739.030647627125!2d-75.3503765!3d40.605879400000006!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c43fbac2185493%3A0xefb590780332c613!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629175798!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Bethlehem to New York or Florida?","New York is eighty-five miles out 78 and runs one hundred seventy to two hundred eighty dollars. Orlando runs seven hundred twenty to one thousand twenty, about one thousand forty-five miles down 95. Philadelphia and Harrisburg are an hour away and cost the least. An SUV or a pickup adds about 10 to 25 percent."),
 ("Can the carrier come to my street in the Moravian district or on the South Side?","No. The Moravian district is colonial streets a trailer cannot enter. The South Side is rowhouses on narrow one-way streets. The driver meets you at the Broad Street lots, on Third Street, or at the casino lots. West Bethlehem sometimes allows the curb, and the townships and Hellertown usually do."),
 ("Can you deliver on a Lehigh or Moravian move-in date?","Yes. The university on the hill takes cars in late August. The university on the north side does the same. Both send them home in May. Mom or Dad books, and an adult signs at a lot. The hill is closed to a trailer that week, so the meeting point is the stadium lots. The date sets the window."),
 ("Do you ship cars for the hospital and the device maker?","Yes, every week. Residents reach the hospital network each June, and traveling nurses arrive year round. The device maker, the diagnostics company, and the warehouses relocate staff all year. When an employer reimburses the move, the receipts come from us."),
 ("Does Musikfest affect my pickup?","Yes, for ten days in early August. A million people come, the Moravian district and the South Side waterfront close, and the bridges crawl. A handoff anywhere near downtown moves to the week before or the week after. The townships and Hellertown run normally."),
 ("Can you ship a car to or from Allentown, Easton, or Nazareth?","Yes, and all three price the same as Bethlehem. Allentown rides the same carriers off 22 and 78. Its row-house blocks meet the truck on a main road. Easton rides them off 78 at the Delaware, and Nazareth rides them off 33. Send the full address for a township subdivision."),
 ("What happens if ice closes 78 or the hills on my pickup day?","The carrier waits in Allentown or on the Jersey side until the state reopens 78. The hills stay closed to a trailer until the ice melts. The handoff moves to a lot on the flats. A closure usually lasts a day, and the truck arrives a day late. You hear it from us before the driver does."),
 ("What happens if the Monocacy floods?","The handoff moves to Broad Street. The creek runs through the Moravian district and floods in a hurricane’s remnants. Ida did it in 2021. A pickup in the district or along the creek waits for the water to drop. The rest of the city sits well above it."),
 ("Can you ship a car that does not run from Bethlehem?","Yes. The quote covers a winch truck and the loading time, with nothing added later. The casino lots or the Route 33 big-box lots are level. Let us know whether it rolls, steers, and brakes."),
 ("What do you need for a Bethlehem car shipping quote?","Where the car is and where it goes, with the neighborhood or the township. The year, make, and model. Whether it drives. Open or enclosed. The week around the move-in or the start date. With those five, a Bethlehem number is back the same day."),
]
BODY.append(faq_section(FAQ,'Bethlehem FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Bethlehem?','The form above takes two minutes and comes back with a Bethlehem number. Name the neighborhood and the week, and a carrier already on 78 takes it.','+16106157620','(610) 615-7620','Get your free Bethlehem quote'))

build({
 'slug':'auto-transport-bethlehem-pennsylvania',
 'title':'Car Shipping in Bethlehem, PA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Bethlehem, PA, the Christmas City between the old steel plant and the warehouses on 78. University move-in timing, hospital and device-maker relocations, Musikfest week, lot handoffs for the Moravian district and the South Side, curbside pickups in West Bethlehem, Bethlehem Township, Hanover Township, and Hellertown, the ice, and the creek. Local office on Lynn Avenue on the South Side. Free quote.',
 'h1':'Car Shipping in<br>Bethlehem, <span class="accent">Pennsylvania</span>',
 'lede':'Open, enclosed, and expedited auto transport across Bethlehem and the Lehigh Valley, planned around 78, 22, the bridges, the campus calendar, the festivals, and the ice on the hills.',
 'tel':'+16106157620','disp':'(610) 615-7620','brand':'Bethlehem','keyword':'car shipping in bethlehem',
 'localterms':['bethlehem','christmas city','steel plant','warehouses','interstate 78','route 22','lynn avenue','south side','lehigh valley','moravian district','hellertown','nazareth','harrisburg','new york','allentown','easton','route 378','hill-to-hill bridge','route 412','route 33','poconos','bridges','downtown','universities','hospital','device maker','casino','musikfest','ice','476','309','philadelphia','newark','baltimore','hartford','washington','pittsburgh','boston','florida','one-way','rowhouse','campus hill','west bethlehem','bethlehem township','hanover township','lower saucon','lehigh','mountain','delaware','february 2007','stranded','rush hours','airport','eighth avenue','center street','airport road','big-box','mall','stadium','fly-and-ship','colonial','main','church','1741','festival','broad street','angled parking','fahy bridge','third street','fourth street','fountain hill','freemansburg avenue','office parks','freemansburg','center valley','coopersburg','retirees','commuters','late august','community college','residents','traveling nurses','project dates','diagnostics','candy maker','stefko','dealers','indiantown gap','christkindlmarkt','thanksgiving','celtic classic','rivalry','valley fair','thirty inches','wyandotte','january 2016','jersey','monocacy','ida','2021','irene','lee','2011','salt','brine','cinders','bill of lading','fmcsa','steelstacks','saucon park','emmaus','winch'],
}, BODY, FAQ)
