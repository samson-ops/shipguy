import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Waterbury, Connecticut','Car shipping in the Brass City, where Interstate 84 meets Route 8 at the Mixmaster',
 ['Car shipping in Waterbury starts at the one interchange every driver in the state knows by name. Ship Guy is a licensed auto transport broker with an office on Willow Street, west of downtown.',
  'We book vetted carriers across the Naugatuck Valley, from Watertown and Wolcott to Naugatuck, Middlebury, and Southbury. We do not own the trucks.',
  'Interstate 84 crosses the city on the way from Danbury to Hartford. Route 8 runs up the valley from Bridgeport to Torrington. The two meet downtown at the Mixmaster, the stacked interchange that was rebuilt over three years.',
  'This page covers the interstate, the valley highway, the hills, downtown, and the valley towns. It also covers the hospitals, the colleges, the retirement village, the floods, the snow, and the lanes.'],
 'Waterbury at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between New York and Hartford by the inland route passes the city on 84.',
  'Hartford, New Haven, Bridgeport, and Danbury are same-day lanes. Manhattan and Boston are the same day too. Albany and Philadelphia take a day. Florida runs three.'],
 'Tell us the neighborhood. Downtown, the hill neighborhoods, and the blocks of three-family houses need a meeting spot. Watertown, Wolcott, and Middlebury usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 84, Route 8, the Mixmaster, and the Hills',
 prose(
  L('Waterbury sits where the inland interstate and the valley highway cross, and both are built for trucks.'),
  P('Interstate 84 runs across the city from Danbury to Hartford and on to Boston. Exits 17 through 25 carry Waterbury. The climb out of the valley in either direction slows a loaded trailer. The stretch through downtown backs up in both rushes.'),
  P('Route 8 runs up the Naugatuck Valley from Bridgeport through Naugatuck and Waterbury to Torrington. It is a freeway the whole way through the city, and it is the road to the shoreline. The Mixmaster carries 84 over Route 8 downtown on two stacked decks.'),
  P('Route 69, Route 73, and Route 63 climb out of the valley to Wolcott, Watertown, and Middlebury. The carriers come off 84 at Hamilton Avenue, Union Street, and Chase Parkway. The mall lot on Union Street and the lots along Wolcott Street are the usual meeting spots. No road in the valley charges a toll.'),
  P('Our office sits on Willow Street, west of downtown and minutes from Route 8 and the Mixmaster.'),
 ), alt=True))

BODY.append(sec('The Hills &amp; the Valley','Downtown, Town Plot, Bunker Hill, the East End, and the Valley Towns',
 prose(
  L('Waterbury is a downtown in a river valley with neighborhoods on seven hills. The hills decide the handoff.'),
  P('Downtown sits on the Green with one-way streets, the clock tower, and the theater. The driver meets you on Meadow Street, at the mall lot, or at a lot by the Mixmaster. The Brooklyn and South End blocks below downtown are tight grids of three-family houses.'),
  P('Town Plot, Bunker Hill, Overlook, and the Hill climb steeply on narrow streets that ice first in winter. A seventy-five-foot trailer stays on Highland Avenue, Bunker Hill Avenue, or Chase Parkway. The East End and Hopeville have wider grids where the curb often works.'),
  P('Bucks Hill, Waterville, and the north end run along Route 8 with a mix of grids and hillsides. Watertown, Wolcott, and Middlebury are suburban grids where the truck usually reaches the curb. The retirement village in Southbury meets the truck at the entrance or on Route 6.'),
  P('Naugatuck, Seymour, and Oxford run down the valley on Route 8 with the river beside them. The flood of August 2024 washed out roads in Oxford, Southbury, and Seymour. The carriers watch the river there after a heavy rain. They meet you on Route 8 when the side roads are out.'),
 )))

ROUTES=[("Hartford, CT","I-84 · ~30 mi","Same day","$110–$190"),("New Haven, CT","I-84/I-91 · ~30 mi","Same day","$110–$190"),
 ("Bridgeport, CT","CT-8 · ~30 mi","Same day","$110–$190"),("Danbury, CT","I-84 · ~30 mi","Same day","$110–$190"),
 ("Manhattan, NY","I-84/I-684 · ~90 mi","Same day","$170–$280"),("Boston, MA","I-84/I-90 · ~130 mi","Same day","$200–$320"),
 ("Albany, NY","I-84/I-87 · ~110 mi","1 day","$190–$300"),("Philadelphia, PA","I-84/I-95 · ~180 mi","1 day","$230–$350"),
 ("Charlotte, NC","I-84/I-95 · ~710 mi","2 days","$510–$730"),("Orlando, FL","I-84/I-95 · ~1,160 mi","3 days","$790–$1,110")]
BODY.append(rate_table('Lanes &amp; Costs','Waterbury Car Shipping Lanes and Estimated Costs',
 'The lanes that leave the valley most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, on an open trailer. An SUV or pickup runs 10 to 25 percent higher, and enclosed higher again. The snow, the hills, and the carriers free on your dates settle the final figure.',
 prose(
  P('Waterbury prices like Hartford, because the same 84 carriers pass both cities half an hour apart. Route 8 brings the shoreline trucks up the valley to meet them. Manhattan rides 84 to 684, and Boston rides 84 to the Pike.'),
  P('The Florida lane fills each fall. The retirement village and the hill towns send their cars south together. The <a href="car-shipping-cost.html">cost guide</a> walks through the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospitals, the Colleges, the Retirement Village, and the Valley Plants',
 prose(
  L('Waterbury relocates people on the residency match, the semester, the retirement calendar, and the plant schedule.'),
  P('The two hospitals bring in residents and nurses every June and July. Most arrive from out of state with a car. The handoff happens on Robbins Street or Franklin Street rather than in a hospital garage.'),
  P('The state university campus downtown and the private university on the east side bring cars in each August. The community college on Chase Parkway does too. The campus lots work for the handoff, and an adult signs for a student car.'),
  P('The retirement village in Southbury is one of the largest in New England. Its residents ship cars to Florida each fall and home each spring. The hill towns do the same on a smaller scale. Our <a href="snowbird-car-shipping.html">snowbird</a> page covers the timing.'),
  P('The watchmaker in Middlebury, the valley plants, and the distribution centers in Cheshire relocate staff on start dates. If the plant or the employer reimburses the shipment, we provide the records. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
  P('Families move up from Fairfield County and the city for the housing all year. The second car often rides a truck instead. The submarine base sits ninety minutes east, and the <a href="military-car-shipping.html">military</a> page covers a PCS move.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Snow on the Hills, the River, and the Mixmaster Rush',
 prose(
  L('Waterbury gets the inland winter and the valley’s floods, and the hills make both harder.'),
  P('Waterbury gets about forty-five inches of snow a year. The hill neighborhoods ice before the valley floor does. Nor’easters close 84 for a morning a few times each winter. The carriers wait for the plows and the sand, and a winter pickup can slide a day.'),
  P('The Naugatuck River floods after a heavy rain. The August 2024 storm washed out roads across the lower valley. A pickup in Oxford, Seymour, or Southbury waits for the roads to reopen after a storm like that. The handoff moves to Route 8 or a lot off 84.'),
  P('Interstate 84 through the Mixmaster backs up from six to ten and from three to seven. A Waterbury pickup happens between the rushes. The driver names the spot the day before.'),
  P('Summer heat moves the loading hour earlier, and thunderstorms with hail roll through in July. The fall foliage traffic fills Route 8 north toward Litchfield County on October weekends.'),
 )+chips(["Downtown","The Green","Brooklyn","South End","Town Plot","Bunker Hill","Overlook","The Hill","East End","Hopeville","Bucks Hill","Waterville","East Mountain","Fairmount","Highland Avenue","Wolcott Street","Union Street","Chase Parkway","Watertown","Wolcott","Middlebury","Naugatuck","Prospect","Cheshire","Southbury","Thomaston"])
 +NOTE('Serving Waterbury and the whole Naugatuck Valley. Tell us the hill, the street, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Waterbury?',
 prose(
  L('Open is how the valley ships, and the 84 and Route 8 lanes are priced for it.'),
  P('An enclosed trailer keeps the salt, the sand, and attention off the car. The garages in Middlebury, Watertown, and Southbury book enclosed trailers. So does a collector car headed to Florida for the winter shows.'),
  P('A commuter car rides open and arrives the way it left. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof is worth.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the mall lot or on a wide avenue, and a delivery. The snow sets the day in winter.'),
  P('Approve the price, and a carrier already running 84 or Route 8 takes the booking. We name the spot the same day. The driver looks the car over with you and lists its condition on a Bill of Lading. Both sign, and delivery is checked against that record.'),
 )+ULI([
  "Get your belongings out of the car",
  "About a quarter tank of fuel is right",
  "Photograph the car before the truck arrives, especially in winter",
  "Give the driver a working key and name any mechanical issue",
  "Disable the aftermarket alarm, if any",
  "On a hill street, plan to meet the truck on the avenue below",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages spell out the rest.'))))

BODY.append(sec('Why Ship Guy','Why Waterbury Drivers Choose Ship Guy',
 prose(
  L('We work 84 and Route 8 every day and plan around the hills, the river, and the snow.'),
  P('The FMCSA register shows Ship Guy as an active broker. The $75,000 surety bond is on file there too. Our office is on Willow Street, west of downtown.'),
  P('Whoever quotes your move is the person who sees it delivered. Open, enclosed, and expedited transport are all bookable, and the <a href="services.html">services</a> page explains them.'),
 ), alt=True))

BODY.append(office('Waterbury','45 Willow St #202','Waterbury, CT 06710','+14753774756','(475) 377-4756','ET',
 '45+Willow+St+%23202,+Waterbury,+CT+06710','Visit Us','Find Ship Guy in Waterbury',
 'Our office is on Willow Street, west of downtown and minutes from Route 8 and the Mixmaster.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4590.930664374838!2d-73.04685909999999!3d41.559169000000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e7c104ed1859e9%3A0xe88c115a94c61a5b!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792153140465!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come up Town Plot or Bunker Hill?","Usually not. The hill streets are narrow, steep, and parked on both sides, and they ice first in winter. The driver meets you on Highland Avenue, Bunker Hill Avenue, or Chase Parkway. The East End, Watertown, and Wolcott usually allow the curb."),
 ("How much does it cost to ship a car from Waterbury to Florida or Boston?","Orlando runs seven hundred ninety to eleven hundred ten dollars for a sedan. That is about eleven hundred sixty miles down 84 and 95. Boston runs two hundred to three hundred twenty, about one hundred thirty miles on 84 and the Pike. Fall southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Is Waterbury priced like Hartford or like the shoreline?","Like Hartford. The same 84 carriers pass both cities half an hour apart. Route 8 brings the shoreline trucks up the valley to meet them. Hartford runs one hundred ten to one hundred ninety dollars for a sedan, and so does Bridgeport."),
 ("What happens if snow or ice hits on my pickup day?","The trucks sit until the plows and the sanders are through on 84 and the hills. The hill neighborhoods ice before the valley floor. The handoff moves to the mall lot or an avenue. A winter pickup can slide a day, and we call when it does."),
 ("Do you ship cars for residents moving into the retirement village in Southbury?","Yes, every month. Residents arrive from across New England, and many ship the car rather than drive it in. The handoff happens at the village entrance or on Route 6. We also ship those cars to Florida each fall and home each spring."),
 ("What happens if the river floods the valley on my pickup day?","The pickup waits for the roads to reopen. The August 2024 storm washed out roads in Oxford, Southbury, and Seymour. The lower valley floods after any heavy rain. The handoff moves to Route 8 or a lot off 84 until the side roads are clear."),
 ("Do you ship cars for residents at Waterbury Hospital or Saint Mary’s?","Yes, every June and July. Residents and nurses arrive from every state, and most bring a car. The handoff happens on Robbins Street or Franklin Street, not in a hospital garage."),
 ("Can you ship a car for a UConn Waterbury, Post, or Naugatuck Valley student?","Yes. The cars come in each August and leave each May. The campus lots work for the handoff, and the mall lot is the backup downtown. An adult signs for the car at pickup."),
 ("Can you ship a car that does not run from Waterbury?","Yes. A winch carrier is dispatched, and the extra loading time is in the price. Pick a flat spot, which means the mall lot rather than a hill street. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Waterbury car shipping quote?","Where the car is and where it is going, with the hill on this end. The year, make, and model, and whether it runs. Open or enclosed. Your dates, snow season included. That is everything a Waterbury quote needs."),
]
BODY.append(faq_section(FAQ,'Waterbury FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Waterbury?','Price the move on the form above in about two minutes. Tell us the hill and your dates, and a carrier already crossing the Mixmaster takes it from there.','+14753774756','(475) 377-4756','Get your free Waterbury quote'))

build({
 'slug':'auto-transport-waterbury-connecticut',
 'title':'Car Shipping in Waterbury, CT — Auto Transport | Ship Guy',
 'meta':'Car shipping in Waterbury, CT where Interstate 84 meets Route 8 at the Mixmaster. Hill-neighborhood meeting spots, mall-lot handoffs, hospital residents, UConn Waterbury and Post students, the Southbury retirement village and the Florida lane, valley floods and snow planning. Local office on Willow Street. Free quote.',
 'h1':'Car Shipping in<br>Waterbury, <span class="accent">Connecticut</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Naugatuck Valley, planned around 84, Route 8, the hills, and the snow.',
 'tel':'+14753774756','disp':'(475) 377-4756','brand':'Waterbury','keyword':'car shipping in waterbury',
 'localterms':['waterbury','interstate 84','route 8','mixmaster','route 69','route 73','route 63','route 6','hamilton avenue','union street','chase parkway','wolcott street','highland avenue','bunker hill avenue','meadow street','robbins street','franklin street','willow street','downtown','the green','clock tower','theater','brooklyn','south end','town plot','bunker hill','overlook','the hill','east end','hopeville','bucks hill','waterville','mall','watertown','wolcott','middlebury','naugatuck','prospect','cheshire','southbury','seymour','oxford','thomaston','torrington','danbury','naugatuck river','flood','august 2024','hospitals','residents','state university','private university','community college','retirement village','watchmaker','plants','distribution centers','submarine base','snow','ice','sand','hills','foliage','hartford','new haven','bridgeport','manhattan','boston','albany','philadelphia','charlotte','orlando','florida'],
}, BODY, FAQ)
