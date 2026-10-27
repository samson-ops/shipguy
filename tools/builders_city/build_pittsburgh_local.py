import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Pittsburgh, Pennsylvania','Car shipping in the city of bridges, tunnels, and hills, where the trailer meets you in the flats',
 ['Car shipping in Pittsburgh runs off the Turnpike north of the city and the Parkways through the tunnels. Ship Guy is a licensed auto transport broker with an office on Sidney Street on the South Side.',
  'We book vetted carriers across Allegheny County, from Cranberry to Monroeville and the Mon Valley. The trucks belong to the carriers, and we hold the authority and the bond.',
  'The Turnpike carries 76 across the north with exits at Cranberry and Monroeville. The Parkway East runs 376 through the Squirrel Hill tunnel. The Parkway West runs it through the Fort Pitt tunnel to the airport. Interstate 279 runs north to Cranberry, and 79 runs south to Morgantown.',
  'This page covers the Turnpike, the Parkways, the tunnels, the flats, the hill neighborhoods, and the suburbs. It also covers the hospitals, the universities, the robotics labs, game days, the landslides, and the lanes.'],
 'Pittsburgh at a glance',
 ['Most pickups happen within 1 to 3 days. The carriers between Philadelphia and Ohio pass the city on the Turnpike. The Cleveland and Columbus trucks come in on 79 and 70.',
  'Cleveland, Columbus, Washington, Baltimore, and Detroit are a same-day haul. Philadelphia, Buffalo, and New York take a day. Chicago takes one to two, and Florida takes three.'],
 'Tell us the neighborhood and whether it sits on a hill. The hillsides, the row-house streets, and the old boroughs need a meeting spot in the flats. Cranberry, the newer South Hills, Robinson, and the east suburbs usually allow the curb.'))

BODY.append(sec('The Roads','The Turnpike, the Parkways, the Tunnels, Route 28, Route 51, and the Bridges',
 prose(
  L('Pittsburgh is the hardest big city in the country for a seventy-five-foot trailer. The driver plans every stop.'),
  P('The Turnpike carries Interstate 76 across the north of the metro from Ohio to Harrisburg. The exits at Cranberry, Butler Valley, Allegheny Valley, and Monroeville serve the suburbs. The tolls ride inside every quote. Interstate 79 runs from Erie past the airport to Morgantown. Interstate 70 crosses the south through Washington and New Stanton.'),
  P('The Parkway East is 376 from Monroeville through the Squirrel Hill tunnel to downtown. The Parkway West is 376 through the Fort Pitt tunnel to the airport. Both tunnels back up every rush hour, and a crash in either one stops the city. Interstate 279 is the Parkway North from downtown to Cranberry. Route 28 runs the Allegheny to Kittanning, and Route 65 runs the Ohio to Sewickley.'),
  P('Route 51 runs the South Hills to the Liberty tunnel. Route 19 runs the North Hills as McKnight Road. Carson Street runs the South Side, and Butler Street runs Lawrenceville. Penn and Liberty run the Strip and East Liberty. The city has more bridges than any other in the world. A few of them carry weight limits a loaded trailer cannot meet. The 2022 collapse of the Forbes Avenue bridge closed the east end for most of a year.'),
  P('The carriers come off the Turnpike at Cranberry and Monroeville and off 79 at Robinson. The Waterfront in Homestead, the Robinson mall, and the Monroeville mall have the usual meeting lots. The SouthSide Works lots and the stadium lots on the North Shore work outside game days. The Ross Park mall and the South Hills Village serve the two sets of hills.'),
  P('Our office is on Sidney Street on the South Side Flats, two blocks from Carson Street.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Strip, the South Side, Lawrenceville, Oakland, Squirrel Hill, the South Hills, the North Hills, the East Suburbs, and the Mon Valley',
 prose(
  L('Pittsburgh is ninety neighborhoods on three rivers and a hundred hills. The handoff happens on the flat ground between them.'),
  P('Downtown is the triangle between the rivers, a tight grid of towers and garages a trailer cannot enter. The Strip District beside it is the produce row and the robotics offices, with lots along the river. The South Side Flats along Carson Street are row houses parked solid. The driver meets you at the SouthSide Works lots. The South Side Slopes above them are steps and switchbacks, and no truck goes up.'),
  P('Lawrenceville, Bloomfield, and Polish Hill are narrow row-house streets with cars on both sides. The driver meets you on Butler Street or at a lot by the river. Oakland is the universities and the hospitals. The handoff happens at a garage exit or on the Boulevard of the Allies. Squirrel Hill and Shadyside are big houses on tight streets. The driver meets you on Forbes or at the Parkway exit.'),
  P('Mount Washington and the hilltop neighborhoods sit above the inclines, and the handoff moves to the flats. The South Hills through Brookline, Dormont, and Mount Lebanon are old grids on steep streets. The driver meets you on Route 19 or at the village lots. Bethel Park, Upper St. Clair, and Peters are newer and wider, and the curb works. The North Hills through Ross and McCandless are the same. Cranberry and Wexford are the easiest in the metro.'),
  P('Monroeville, Penn Hills, and Murrysville to the east are postwar suburbs on rolling ground. Most streets allow the curb. Robinson and Moon by the airport are wide and simple. The Mon Valley towns from Homestead to McKeesport are old grids on the river flats. A lot by the mill site works. Sewickley and Fox Chapel have the old money and the narrow lanes. The driver meets you at the village. All of them price the same as Pittsburgh.'),
 )))

ROUTES=[("Cleveland, OH","I-76/I-80 · ~130 mi","Same day","$200–$320"),("Columbus, OH","I-70 · ~185 mi","Same day","$220–$340"),
 ("Washington, DC","I-70/I-270 · ~245 mi","Same day","$250–$380"),("Baltimore, MD","I-70 · ~250 mi","Same day","$250–$380"),
 ("Detroit, MI","I-79/I-80/I-75 · ~285 mi","Same day","$270–$400"),("Philadelphia, PA","I-76 Turnpike · ~305 mi","1 day","$270–$400"),
 ("Buffalo, NY","I-79/I-90 · ~215 mi","1 day","$240–$360"),("New York, NY","I-76/I-78 · ~370 mi","1 day","$340–$490"),
 ("Chicago, IL","I-76/I-80 · ~460 mi","1–2 days","$400–$580"),("Orlando, FL","I-79/I-77/I-95 · ~1,000 mi","3 days","$700–$1,000")]
BODY.append(rate_table('Lanes &amp; Costs','Pittsburgh Car Shipping Lanes and Estimated Costs',
 'The lanes western Pennsylvania cars take most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Pittsburgh for a running sedan on an open trailer. SUVs and pickups add roughly 10 to 25 percent, and an enclosed trailer adds more. Turnpike tolls are built in. The season and the carriers free on your dates set the final number.',
 prose(
  P('Pittsburgh prices its Ohio lanes almost as low as the East Coast cities price theirs. The Cleveland and Columbus carriers come through every day. The Philadelphia lane rides the Turnpike and runs daily. The Florida lane is the busiest long haul out of the city from October through December. The New York lane rides 76 and 78 and runs a day.'),
  P('A move timed to the June residency changeover or the August move-in ships with the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospitals, the Universities, the Robotics Labs, the Banks, the Gas Fields, and the Steelmaker',
 prose(
  L('Pittsburgh relocates residents, professors, roboticists, and bankers. The two hospital systems move more people than anyone in western Pennsylvania.'),
  P('The two hospital systems take new residents each June and hire nurses on contracts all year. The physicians come with a closing date and a second car. The two universities in Oakland bring fifty thousand students in each August. The parent books the car, and an adult signs at a lot off the Parkway. Faculty hires land each summer with a closing date.'),
  P('The robotics and self-driving labs in the Strip and Lawrenceville hire engineers from every state on start dates. The software offices in Bakery Square and East Liberty do the same. The bank headquartered downtown and the steelmaker beside it move staff on their own calendars. The gas producers in the Marcellus fields rotate engineers through the city on project schedules. The paperwork for a reimbursed relocation comes from us.'),
  P('The airlift wing at the airport rotates reservists on orders, and the orders cover one car. Ship Guy is a private broker with no military connection. The <a href="military-car-shipping.html">military</a> page covers an order to the wing or beyond.'),
  P('Retirees leave for Florida and the Carolinas each fall and come back in April. Families from the East Coast buy in Cranberry and the South Hills on closing dates. One car rides the trailer while the other is driven. The interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Game Days, the Marathon, the Regatta, the Arts Festival, the Landslides, and the Tunnels in Snow',
 prose(
  L('Pittsburgh runs on three teams and a marathon that closes every bridge. Spring sends the hillsides into the road.'),
  P('The football and baseball stadiums on the North Shore take the lots and the bridges on game days. The hockey arena uptown does the same on winter nights. A North Shore handoff on a game day moves to the morning or to the Waterfront. The marathon closes the bridges and the Parkway ramps for the first Sunday in May. The arts festival fills the Point for ten days in June.'),
  P('The regatta fills the rivers and the North Shore for an August weekend. The pickle festival closes downtown blocks for a July weekend. Light Up Night fills downtown on a November Saturday. Move-in weekend in August fills Oakland, and the residency changeover fills it again in June. A handoff near any of them moves to the daytime or to the flats.'),
  P('Winter brings forty inches of snow, and the hills ice before the plows reach them. A storm closes the Parkways for a morning. The carriers wait at the Turnpike plazas until the tunnels clear. The Allegheny tunnels on the Turnpike close for a crash a few times each winter. The Philadelphia lane waits. A winter pickup on a hill moves to the flats or slips a day.'),
  P('Spring is landslide season. A week of rain sends the hillsides onto Route 51, Route 28, and the Parkway. The 2018 slide closed Route 30 for months. The rivers flood the Strip and the Mon Valley in a wet spring, as Ivan did in 2004. The sirens are rare. Summer brings a storm every few afternoons and ninety degrees in the flats.'),
 )+chips(["Downtown","Strip District","South Side Flats","Sidney Street","Carson Street","South Side Slopes","Lawrenceville","Bloomfield","Polish Hill","Oakland","Squirrel Hill","Shadyside","East Liberty","Bakery Square","Mount Washington","Brookline","Dormont","Mount Lebanon","Bethel Park","Upper St. Clair","Peters","Ross","McCandless","Wexford","Cranberry","Monroeville","Penn Hills","Murrysville","Robinson","Moon","Homestead","McKeesport","Sewickley","Fox Chapel","Washington"])
 +NOTE('Serving Pittsburgh and all of Allegheny County, hillside street or Cranberry cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Pittsburgh?',
 prose(
  L('Open trailers carry most cars that leave Allegheny County, and the table above assumes one.'),
  P('An enclosed trailer keeps off the road salt, the slag grit, and the gravel the hillsides shed. The collectors who fill the vintage race in Schenley Park book one. Executives relocating a new car to the bank or the labs book one too.'),
  P('A commuter car or a second family car goes open without any trouble. The difference is on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot at the Waterfront or Robinson, and a signature at the far end. The start date or the closing picks the week.'),
  P('Once the price is approved, the car is placed with a carrier already running the Turnpike or 79. The lot and the window follow by the end of the day. At pickup the driver inspects the car with you, panel by panel. What is already there goes on the Bill of Lading. Both of you sign it, and the delivery is checked against it.'),
 )+ULI([
  "Nothing of yours left inside the cabin or the trunk",
  "Fuel down around a quarter tank",
  "Every panel and the odometer photographed beforehand",
  "A single working key to the driver, plus any known fault",
  "Aftermarket alarm turned off",
  "On a hill or a row-house street, meet the truck in the flats or at a mall lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Pittsburgh Drivers Choose Ship Guy',
 prose(
  L('We book the carriers already running the Turnpike and 79. We know which hills a trailer will not climb.'),
  P('Ship Guy holds FMCSA brokerage authority and a $75,000 surety bond, and the register shows both. Our office is on Sidney Street on the South Side.'),
  P('One coordinator sees the move through from the first number to the signed delivery sheet. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Pittsburgh','2681 Sidney St #399','Pittsburgh, PA 15203','+14123142407','(412) 314-2407','ET',
 '2681+Sidney+St+%23399,+Pittsburgh,+PA+15203','Visit Us','Find Ship Guy in Pittsburgh',
 'Our office is on Sidney Street on the South Side Flats, two blocks from Carson Street.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4670.384683894724!2d-79.96631029999999!3d40.4280282!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8834f174ccf7e749%3A0x2afb80c59b8d625e!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793103547399!5m2!1sen!2sus', alt=True))

FAQ=[
 ("Can the carrier come to my house on a Pittsburgh hill?","Rarely. The hillside streets are steep and narrow, and the row-house blocks are parked solid. Some bridges carry weight limits a loaded trailer cannot meet. The driver meets you in the flats, at a mall lot, or at a lot off the Parkway. Cranberry, the newer South Hills, Robinson, and the east suburbs usually allow the curb."),
 ("How much does it cost to ship a car from Pittsburgh to Philadelphia or Florida?","Philadelphia runs two hundred seventy to four hundred dollars for a sedan. That is about three hundred five miles across the Turnpike. Orlando runs seven hundred to a thousand, about a thousand miles down 79, 77, and 95. Cleveland is the shortest lane and the lowest priced. Add 10 to 25 percent for an SUV or a pickup."),
 ("Do you ship cars for residents and nurses coming to the hospitals?","Yes, every month, and most of all in June. The two hospital systems take new residents the same week each summer. They hire nurses on contracts all year. A second car usually follows the move on a trailer. The handoff works at a garage exit in Oakland or at the Waterfront lots. The paperwork for a reimbursed relocation comes from us."),
 ("Can you deliver on the Pitt or Carnegie Mellon move-in date?","Yes. Both campuses take cars in each August and send them home in May. A parent arranges the shipment, and someone over eighteen signs at a lot off the Parkway. The window is keyed to move-in weekend and shifts with it. Oakland is closed to a trailer that weekend. The handoff happens at the Waterfront or on the Boulevard."),
 ("Does a Steelers game or the marathon affect my pickup?","On the North Shore and downtown, yes. A game day takes the stadium lots and the bridges. The marathon closes the bridges and the Parkway ramps for the first Sunday in May. We move a North Shore handoff on those days to the morning or to the Waterfront. The suburbs run normally."),
 ("Can you ship a car to or from Cranberry, Monroeville, or the Mon Valley?","Yes, and all three price the same as Pittsburgh. Cranberry rides the same carriers off the Turnpike and 79, and the curb works almost everywhere. Monroeville rides them off the Turnpike and the Parkway East, and the mall lots are the usual handoff. The Mon Valley towns ride them down Route 837, and a lot by the mill site works."),
 ("Are the Turnpike tolls in my price?","Yes. The carrier pays the Turnpike by the mile with a transponder, and the toll rides inside the quote. There is no separate line for it. The Parkways, 79, 279, and the state routes carry no toll."),
 ("What happens if snow or a landslide closes the road on my pickup day?","A storm closes the Parkways for a morning. The carriers wait at the Turnpike plazas until the tunnels clear. A pickup on a hill moves to the flats or slips a day. You hear it from us first. A spring slide closes Route 51 or Route 28 for days. The carrier comes in on the other side of the river."),
 ("Can you ship a car that does not run from Pittsburgh?","Yes. We book a winch carrier and include the extra loading time in the first number. The Waterfront lots or the Robinson mall lots give the driver level ground. That matters more here than anywhere. Say whether the car rolls, steers, and brakes."),
 ("What do you need for a Pittsburgh car shipping quote?","Both addresses, with the neighborhood and whether it sits on a hill. Year, make, and model. Running or not. Open or enclosed. The week around the start date. Those five, and the Pittsburgh number comes back within the day."),
]
BODY.append(faq_section(FAQ,'Pittsburgh FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Pittsburgh?','Two minutes on the form above, and your lane has a number. Tell us the neighborhood and the week, and a carrier already on the Turnpike takes it.','+14123142407','(412) 314-2407','Get your free Pittsburgh quote'))

build({
 'slug':'auto-transport-pittsburgh-pennsylvania',
 'title':'Car Shipping in Pittsburgh, PA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Pittsburgh, PA, the city of bridges, tunnels, and hills. Hospital and university relocations, robotics-lab start dates, handoffs in the flats and at the mall lots for the hillside and row-house streets, curbside pickups in Cranberry and the South Hills, the Turnpike tolls, game days, the marathon, the landslides, and the snow. Local office on the South Side. Free quote.',
 'h1':'Car Shipping in<br>Pittsburgh, <span class="accent">Pennsylvania</span>',
 'lede':'Open, enclosed, and expedited auto transport across Allegheny County, planned around the Turnpike, the tunnels, the hills, the hospital calendar, and the winter.',
 'tel':'+14123142407','disp':'(412) 314-2407','brand':'Pittsburgh','keyword':'car shipping in pittsburgh',
 'localterms':['pittsburgh','allegheny county','turnpike','parkways','tunnels','sidney street','south side flats','cranberry','north hills','monroeville','mon valley','interstate 76','parkway east','376','squirrel hill tunnel','parkway west','fort pitt tunnel','airport','interstate 279','79','morgantown','flats','south hills','east suburbs','hospitals','universities','robotics','game days','marathon','landslides','philadelphia','ohio','cleveland','columbus','washington','baltimore','detroit','buffalo','new york','chicago','florida','hill','row-house','boroughs','robinson','seventy-five-foot','harrisburg','butler valley','allegheny valley','erie','interstate 70','new stanton','rush hour','parkway north','route 28','kittanning','route 65','sewickley','route 51','liberty tunnel','route 19','mcknight road','carson street','butler street','lawrenceville','penn','liberty','strip','east liberty','bridges','weight limits','2022 collapse','forbes avenue','waterfront','homestead','mall','southside works','stadium lots','north shore','ross park','south hills village','ninety neighborhoods','three rivers','downtown','triangle','towers','garages','produce row','slopes','steps','switchbacks','bloomfield','polish hill','oakland','boulevard of the allies','shadyside','forbes','mount washington','inclines','brookline','dormont','mount lebanon','bethel park','upper st. clair','peters','ross','mccandless','wexford','penn hills','murrysville','moon','mckeesport','fox chapel','residents','professors','roboticists','bankers','nurses','physicians','fifty thousand','students','faculty','self-driving','engineers','bakery square','bank','steelmaker','gas producers','marcellus','airlift wing','reservists','orders','retirees','carolinas','football','baseball','hockey','arena','uptown','the point','arts festival','regatta','pickle festival','light up night','move-in','residency','forty inches','plazas','allegheny tunnels','rain','route 30','2018','ivan','2004','sirens','ninety degrees','slag','schenley park','vintage race','bill of lading','fmcsa','surety bond','route 837','transponder'],
}, BODY, FAQ)
