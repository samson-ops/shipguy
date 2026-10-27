import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Meridian, Idaho','Car shipping in the fastest-growing city in Idaho, on Eagle Road and Interstate 84',
 ['Car shipping in Meridian starts at the Eagle Road interchange, the busiest exit on Interstate 84. Ship Guy is a licensed auto transport broker with an office on South Rackham Way off Eagle Road.',
  'We book vetted carriers across the valley, from Chinden to Lake Hazel and across to Star. We do not own the trucks.',
  'Interstate 84 crosses the south side with exits at Ten Mile, Meridian Road, and Eagle Road. Eagle Road is Highway 55, the north-south spine and the busiest surface road in Idaho. Chinden Boulevard runs the north edge. The mile roads fill in the grid.',
  'This page covers the interstate, Eagle Road, Old Town, the Village, the subdivisions, and the new south. It also covers the insurer, the hospitals, the fragrance company, the transplants, the winter, and the lanes.'],
 'Meridian at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 84 brings the Portland and Salt Lake carriers past the Eagle Road exit all day.',
  'Salt Lake City, Portland, and Spokane are each about a day away. Seattle, Reno, and Sacramento run one to two days. Las Vegas, Los Angeles, and Denver run two. The Midwest and the East run three to four.'],
 'Tell us the subdivision and the gate. Old Town and the gated golf communities need a meeting spot. Almost every other subdivision in the city allows the curb.'))

BODY.append(sec('The Roads','Interstate 84, Eagle Road, Ten Mile, Chinden, and the Mile Roads',
 prose(
  L('Meridian was a farm town on a rail siding. The roads still run on the old section lines a mile apart.'),
  P('Interstate 84 runs the south side of the city from the Nampa line to the Boise line. The Eagle Road exit is the busiest in the state. The Ten Mile and Meridian Road exits take the overflow. Every carrier between Portland and Salt Lake City passes all three.'),
  P('Eagle Road is Highway 55. It runs north from the interstate past the hospitals and the Village to Chinden and Eagle. It carries more traffic than any surface street in Idaho. Chinden Boulevard is US 20 and 26, the north edge of the city. Meridian Road runs through Old Town, and Ten Mile and Linder run parallel on the west.'),
  P('Fairview, Franklin, Overland, Victory, Amity, and Lake Hazel are the east-west mile roads. Overland and Franklin carry the business parks along the interstate. Amity and Lake Hazel reach the new subdivisions in the south. The pavement sometimes ends where the map does. Ustick and McMillan cross the north side.'),
  P('The carriers come off 84 at Eagle Road, Meridian Road, and Ten Mile. The lots at the Village, along Overland, and at the Ten Mile crossing are the usual meeting spots. No road in the valley charges a toll.'),
  P('Our office sits on South Rackham Way in the business park off Eagle Road.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Old Town, the Village, Paramount, the Golf Communities, and the New South',
 prose(
  L('Meridian went from thirty thousand people to well past a hundred thousand in a generation. Almost all of it is subdivisions.'),
  P('Old Town along Main Street and Meridian Road has the city hall and the speedway. A few blocks of narrow streets survive from the farm-town days. The driver meets you on Meridian Road or at a lot on Fairview. The blocks around the old center are postwar grids where the truck reaches the curb.'),
  P('Paramount, Bridgetower, and the subdivisions along Chinden and McMillan are the north side. They were built with wide streets and cul-de-sacs. The curb works on most of them. Where it does not, the driver meets you at the entrance. The Village at Eagle Road and Fairview has garages and lots for a handoff.'),
  P('Spurwing, Tuscany, and the golf communities have gates on their entrances. Pass along the gate code, and we clear access ahead of time. If the truck cannot enter, you meet the driver at the gate. The business parks along Overland and the interstate have room everywhere.'),
  P('South Meridian along Amity and Lake Hazel is where the city is still being built. The subdivisions there are newer than most carrier maps, and newly paved streets can be tight. Send the full address and the nearest mile road. If the streets inside are narrow, the driver meets you at the entrance. Kuna beyond the south edge is the same.'),
 )))

ROUTES=[("Salt Lake City, UT","I-84 · ~350 mi","1 day","$320–$460"),("Portland, OR","I-84 · ~420 mi","1 day","$370–$530"),
 ("Spokane, WA","US-95 · ~430 mi","1 day","$370–$530"),("Seattle, WA","I-84/I-90 · ~490 mi","1 day","$400–$570"),
 ("Reno, NV","I-84/US-95 · ~410 mi","1 day","$370–$530"),("Sacramento, CA","I-84/I-80 · ~550 mi","1–2 days","$450–$650"),
 ("Las Vegas, NV","I-84/US-93 · ~640 mi","2 days","$470–$680"),("Los Angeles, CA","I-84/I-15 · ~860 mi","2 days","$580–$830"),
 ("Denver, CO","I-84/I-80 · ~830 mi","2 days","$560–$800"),("Dallas, TX","I-84/I-80/I-25 · ~1,500 mi","3 days","$900–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Meridian Car Shipping Lanes and Estimated Costs',
 'Where valley cars go most, with estimated open-trailer ranges. Your exact lane prices above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Meridian for a sedan that runs, open trailer. An SUV or pickup runs 10 to 25 percent higher, enclosed higher again. Demand from the coast, the winter, and carrier availability on your dates fix the final number.',
 prose(
  P('Meridian prices the same as Boise. The Eagle Road exit sits on the same interstate ten minutes west. The lanes from California, Washington, and Oregon run full with transplants, and the return legs run lighter. Salt Lake City rides 84 straight down.'),
  P('Texas and the Midwest ride 84 and 80 through Wyoming. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Insurer, the Hospitals, the Fragrance Company, and the Transplants',
 prose(
  L('Meridian relocates more households per year than any city in the state. Most of them come from the coast.'),
  P('Households from California, Washington, and Oregon land in Meridian on closing dates every month of the year. One car ships, and the other is driven. Remote workers come for the schools and the prices, and retirees come for the same reasons. Nearly every Meridian booking is pinned to a closing, and the window follows the closing when it moves.'),
  P('The health insurer headquartered here and the fragrance company off Ten Mile bring in staff from every state. They arrive on start dates. The memory company’s consumer division does the same. The two hospitals on Eagle Road bring in nurses all year and residents each June. We supply the paperwork a reimbursed move needs.'),
  P('The state police headquarters and the state agencies in the business parks hire on their own calendar. The university in Boise and the college in Nampa bring cars in each August. Meridian students meet the driver at a lot on Eagle Road. An adult signs for a student car.'),
  P('The Air Force base an hour southeast rotates families year round, and many settle in Meridian. One car moves on the orders, and the other moves with us. Ship Guy is a private broker and is not connected to the base. Timing is on the <a href="military-car-shipping.html">military</a> page, and the interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Inversion, Snow, Smoke, Dairy Days, and the Speedway',
 prose(
  L('Meridian shares the valley weather with Boise and adds a racetrack downtown.'),
  P('The inversion settles cold fog on the valley for weeks in December and January. The roads stay open, and the carriers run through it. A few times each winter, snow glazes the overpasses on 84 and the mile roads. The 2017 storm closed the valley for days. The carriers wait on the interstate, and a winter pickup may lose a day.'),
  P('Fire smoke settles into the valley from July through September. Interstate 84 stays open, and a valley pickup runs normally. Summer heat passes one hundred degrees in July, and the loading hour moves to the morning. Spring wind across the open ground south of the interstate slows a tall trailer.'),
  P('Dairy Days closes Main Street and Old Town for a weekend in June for the parade and carnival. The speedway runs Saturday nights from April through September, and the blocks around it fill. A pickup in Old Town moves to another day or to Fairview.'),
  P('The fair fills Garden City next door in August. Home football Saturdays in Boise fill the interstate on fall afternoons. The holiday lights fill the Village in December. None of it stops a pickup, but each one moves the meeting spot.'),
 )+chips(["Old Town","Main Street","Meridian Road","The Village","Eagle Road","Fairview","Paramount","Bridgetower","Settlers Park","Linder Village","Ten Mile","Silverstone","Overland","Spurwing","Tuscany","Reflection Ridge","Hillsdale","Amity","Lake Hazel","South Meridian","Ustick","McMillan","Chinden","Star","Kuna","Eagle"])
 +NOTE('Serving Meridian and every subdivision in it, paved or still being paved. Tell us the gate code, the nearest mile road, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Meridian?',
 prose(
  L('Open is how the valley ships, and the transplant lanes are priced for it.'),
  P('An enclosed trailer keeps the road salt, the smoke, and attention off a car. The garages in Spurwing and Tuscany book them for collector cars. So does a family bringing a restored car up from California.'),
  P('A commuter car travels open and arrives fine. See the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages for the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the Village or a lot on Overland, and a delivery. The closing date sets the week.'),
  P('Once the price is approved, we book a carrier already passing the Eagle Road exit. The meeting spot and the window are confirmed that afternoon. The driver and you look the car over together, and its condition goes on a Bill of Lading. Both of you sign it, and it is read again at delivery.'),
 )+ULI([
  "Empty the car of personal items",
  "Leave about a quarter tank of fuel",
  "Photograph the car before the handoff",
  "Provide a working key and disclose any mechanical issue",
  "Turn off any aftermarket alarm",
  "In a new subdivision, send the nearest mile road and meet the truck at the entrance",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages walk through the rest.'))))

BODY.append(sec('Why Ship Guy','Why Meridian Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already pass the Eagle Road exit. We plan around the closing date, the new streets, and the winter.'),
  P('The FMCSA lists Ship Guy as an active broker, with a $75,000 surety bond on file. Our office is on South Rackham Way off Eagle Road.'),
  P('You get one coordinator from the quote until the delivery call. The <a href="services.html">services</a> page explains open, enclosed, and expedited transport.'),
 ), alt=True))

BODY.append(office('Meridian','1120 S Rackham Way Ste 429A','Meridian, ID 83642','+12087429621','(208) 742-9621','MT',
 '1120+S+Rackham+Way+Ste+429A,+Meridian,+ID+83642','Visit Us','Find Ship Guy in Meridian',
 'Our office is on South Rackham Way in the business park off Eagle Road, beside Interstate 84.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4443.484884211944!2d-116.35160809999998!3d43.594421399999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54ae57ecaf8cbb13%3A0x6333896ec7ca4b8a!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792170036267!5m2!1sen!2sus'))

FAQ=[
 ("My Meridian subdivision is brand new. Can the carrier find it?","Yes, if you send the full address and the nearest mile road. South Meridian adds streets faster than the carrier maps update, and we route the driver ourselves. Newly paved streets can be tight, so the driver may meet you at the entrance. Add the gate code if the subdivision has one."),
 ("Can you time delivery to my closing date?","Yes. More Meridian bookings are tied to a closing than to anything else. The delivery window wraps around the closing date, and a moved closing moves the window with it. Let us know the moment the date changes."),
 ("How much does it cost to ship a car from California or Oregon to Meridian?","Sacramento runs four hundred fifty to six hundred fifty dollars for a sedan. That is about five hundred fifty miles on 80 and 84. Portland runs three hundred seventy to five hundred thirty, about four hundred twenty miles down 84. Los Angeles comes in at five hundred eighty to eight hundred thirty. Full trailers on the inbound lanes keep the prices steady. An SUV or pickup adds 10 to 25 percent."),
 ("Can the carrier come into Spurwing or Tuscany?","Often, when the gate allows trucks. Give us the community and the code, and we verify access before the truck is dispatched. If it cannot enter, the handoff happens at the gate. The ungated subdivisions on the north side allow the curb."),
 ("Do you ship cars for employees relocating to the insurer or the fragrance company?","Yes, all year, on start dates. Both bring in staff from every state, and many ship a second car behind the move. The handoff works at a lot on Overland or at the Village. We provide the paperwork a reimbursed move needs."),
 ("What happens if snow or the inversion hits on my pickup day?","The inversion is fog, and fog slows the trucks without stopping them. Snow is different. It glazes the overpasses and the mile roads. The carriers sit on 84 until the plows are through. Expect a winter pickup to lose a day, with a call from us first."),
 ("Does Dairy Days or the speedway affect my pickup?","Only in Old Town. Dairy Days closes Main Street for a weekend in June. The speedway fills the blocks around it on summer Saturday nights. We move an Old Town pickup to another day or to Fairview. The rest of the city runs normally."),
 ("Can you handle a PCS move to Mountain Home for a family living in Meridian?","Yes, on every rotation. Many base families settle in Meridian for the schools, and the drive is an hour. One car travels on the orders, and the other travels with us. The report date fixes the pickup. Ship Guy is a private broker with no tie to the base."),
 ("Can you ship a car that does not run from Meridian?","Yes. A winch truck handles it, and the quote already includes the slower loading. A lot on Overland or at the Village gives the driver a flat spot. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Meridian car shipping quote?","Pickup and delivery addresses, plus the subdivision, the gate code, or the nearest mile road here. Year, make, and model, and whether it runs. Open or enclosed. Dates built around the closing. Nothing more is needed for a Meridian quote."),
]
BODY.append(faq_section(FAQ,'Meridian FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Meridian?','A price takes about two minutes on the form above. Tell us the subdivision and your dates, and a carrier already passing Eagle Road takes it from there.','+12087429621','(208) 742-9621','Get your free Meridian quote'))

build({
 'slug':'auto-transport-meridian-idaho',
 'title':'Car Shipping in Meridian, ID — Auto Transport | Ship Guy',
 'meta':'Car shipping in Meridian, ID at the Eagle Road exit on Interstate 84. Closing-date deliveries for transplants from California, Washington, and Oregon, new-subdivision routing, Spurwing and Tuscany gates, Old Town meeting spots, insurer and hospital relocations, inversion and snow planning. Local office on South Rackham Way off Eagle Road. Free quote.',
 'h1':'Car Shipping in<br>Meridian, <span class="accent">Idaho</span>',
 'lede':'Open, enclosed, and expedited auto transport across the valley, planned around 84, Eagle Road, the closing date, and the streets still being paved.',
 'tel':'+12087429621','disp':'(208) 742-9621','brand':'Meridian','keyword':'car shipping in meridian',
 'localterms':['meridian','interstate 84','eagle road','highway 55','ten mile','meridian road','chinden','us 20','linder','fairview','franklin','overland','victory','amity','lake hazel','ustick','mcmillan','mile roads','section lines','rackham','business park','old town','main street','speedway','city hall','the village','paramount','bridgetower','spurwing','tuscany','golf','gate code','south meridian','newly paved','entrance','kuna','star','eagle','insurer','fragrance','memory','hospitals','nurses','residents','state police','university','college','air force base','orders','closing date','transplants','california','washington','oregon','remote workers','retirees','inversion','snow','2017','smoke','spring wind','dairy days','parade','fair','football','holiday lights','salt lake city','portland','spokane','seattle','reno','sacramento','las vegas','los angeles','denver','dallas'],
}, BODY, FAQ)
