import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('The Bronx, New York','Car shipping on the Cross Bronx, the Deegan, and the roads that feed every bridge north of Manhattan',
 ['Car shipping in the Bronx runs on two expressways the whole East Coast already uses. Ship Guy is a licensed auto transport broker with an office on Waters Place in the east Bronx.',
  'We book vetted carriers for every neighborhood from Riverdale to Throgs Neck and from Mott Haven to Woodlawn. We do not own the trucks.',
  'Interstate 95 crosses the borough as the Cross Bronx and the Bruckner. Interstate 87 is the Major Deegan along the Harlem River. The Hutchinson, the Bronx River, the Pelham, and the Mosholu are parkways that ban the truck.',
  'This page covers the expressways and the parkways, the meeting spots, and the stadium. It also covers the hospitals, the colleges, the Florida lane, and the lanes up and down the corridor.'],
 'Bronx at a glance',
 ['Most pickups happen within 1 to 3 days. The meeting spot is an industrial block, a shopping-center lot, or a wide boulevard near the expressway.',
  'Hartford, Philadelphia, and Boston run the same day. Albany and Washington need a day. Florida needs three to four.'],
 'Tell us the neighborhood. Riverdale, Belmont, and the Concourse need a meeting spot. Throgs Neck, Country Club, and Morris Park often allow the curb.'))

BODY.append(sec('The Roads','The Cross Bronx, the Deegan, the Bruckner, and the Parkways',
 prose(
  L('Every carrier between New England and the rest of the country crosses the Bronx. Most of them dread it.'),
  P('The Cross Bronx Expressway carries Interstate 95 from the George Washington Bridge to the Bruckner interchange. It is the slowest stretch of interstate in the country, and carriers time it for early morning. The Bruckner continues 95 to the New England Thruway and Connecticut.'),
  P('The Major Deegan carries Interstate 87 up the Harlem River to the Thruway and Yonkers. Interstate 278 runs the Bruckner to the RFK Bridge and Queens. Interstate 295 reaches the Throgs Neck Bridge, and Interstate 678 reaches the Whitestone.'),
  P('The Hutchinson River Parkway, the Bronx River Parkway, the Pelham Parkway, and the Mosholu ban commercial vehicles. So does the Henry Hudson. A trailer that enters one meets a stone bridge it cannot clear.'),
  P('Bruckner Boulevard, the Grand Concourse, Fordham Road, and Boston Road are the surface roads a trailer can use. Every bridge charges a toll, and the carrier pays it. The quote you approve already includes the tolls.'),
 ), alt=True))

BODY.append(sec('The Meeting Spots','Hunts Point, Port Morris, Co-op City, and the Stadium Lots',
 prose(
  L('The Bronx has more trailer-sized lots than any borough. The whole city’s food comes through it on trucks.'),
  P('Hunts Point and Port Morris are industrial peninsulas built for tractor-trailers, with wide streets and loading lanes. Most handoffs for the South Bronx, Mott Haven, Melrose, and Soundview happen there.'),
  P('Co-op City and the shopping center beside it sit where Interstate 95 meets the Hutchinson. They have acres of parking. Pelham Bay, Baychester, Eastchester, and Wakefield meet the truck there. The lots on Waters Place by our office serve Westchester Square, Morris Park, and Pelham Parkway.'),
  P('The stadium lots on the Deegan work on non-game days for the Concourse, Highbridge, and Kingsbridge. Fordham, Belmont, and Tremont use Fordham Road or Webster Avenue. Throgs Neck and Country Club meet the truck at the park lots under the bridge.'),
  P('Riverdale and Fieldston sit on hills with winding streets and no truck access. The driver meets you on Broadway near Van Cortlandt Park or at a lot on the Deegan. City Island has one narrow bridge, and the handoff happens on the mainland side.'),
 )))

ROUTES=[("Hartford, CT","I-95/I-91 · ~105 mi","Same day","$190–$300"),("Philadelphia, PA","I-95 · ~110 mi","Same day","$200–$320"),
 ("Albany, NY","I-87 · ~140 mi","Same day","$210–$330"),("Boston, MA","I-95 · ~200 mi","Same day","$240–$360"),
 ("Washington, DC","I-95 · ~240 mi","1 day","$260–$380"),("Buffalo, NY","I-87/I-90 · ~395 mi","1 day","$380–$540"),
 ("Charlotte, NC","I-95/I-85 · ~645 mi","2 days","$480–$690"),("Chicago, IL","I-80 · ~800 mi","2 days","$570–$830"),
 ("Orlando, FL","I-95 · ~1,100 mi","3 days","$770–$1,090"),("Miami, FL","I-95 · ~1,300 mi","3–4 days","$810–$1,160")]
BODY.append(rate_table('Lanes &amp; Costs','Bronx Car Shipping Lanes and Estimated Costs',
 'Where Bronx cars go most often, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, bridge tolls included. An SUV or pickup adds about 10 to 25 percent, enclosed more again. The season and the carriers available on your dates decide the final number.',
 prose(
  P('The Bronx sits on the corridor itself, so Hartford, Philadelphia, and Boston price like local trips. The Deegan puts Albany and the Thruway cities a day away.'),
  P('Florida prices by the calendar more than the mileage, and the fall rush starts in October. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospitals, the Colleges, the Market, and the Florida Lane',
 prose(
  L('The Bronx relocates people on residency match day and the college calendar. A snowbird season empties Pelham Bay every fall.'),
  P('The medical center in Norwood and the hospital campus in Morris Park take in residents every summer. So do the hospitals in Mott Haven and Belmont. Most arrive from out of state with a car. The handoff happens on Pelham Parkway’s service road, on Eastchester Road, or at the Waters Place lots.'),
  P('The university in Fordham and the college in Bedford Park bring cars in each August. They send them home in May. The college in Riverdale and the maritime college in Throgs Neck do the same. An adult signs for a student car. The driver meets you on a wide road nearby.'),
  P('The produce, meat, and fish markets in Hunts Point employ thousands on overnight shifts. The distributors transfer managers in on start dates. If your employer reimburses the shipment, we send the documentation.'),
  P('Co-op City, Throgs Neck, and Country Club send a wave of cars to Boca and Tampa each fall. The wave comes back in the spring. Our <a href="snowbird-car-shipping.html">snowbird</a> page has the planning tips, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page covers a permanent move.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Game Days, the Zoo Traffic, Storm Flooding, and Snow',
 prose(
  L('The Bronx closes for baseball and floods in a heavy rain, and the carriers plan for both.'),
  P('Home games fill the Deegan, the Concourse, and the streets around the stadium for hours. Concourse and Highbridge pickups move to a non-game day. The zoo and the botanical garden fill Fordham Road and Southern Boulevard on summer weekends.'),
  P('Heavy rain floods the Deegan and the Cross Bronx underpasses. A tropical storm floods the low ground in Throgs Neck, Pelham Bay, and City Island. We move the handoff to high ground when the forecast calls for it.'),
  P('A few nor’easters each winter park the carriers on the Bruckner until the plows pass. Alternate-side parking is suspended, and the side streets stay buried for a day or two. Road salt runs all winter.'),
 )+chips(["Mott Haven","Port Morris","Melrose","Morrisania","Hunts Point","Longwood","Soundview","Castle Hill","Parkchester","Unionport","Westchester Square","Morris Park","Pelham Parkway","Van Nest","Throgs Neck","Country Club","Pelham Bay","City Island","Co-op City","Baychester","Eastchester","Wakefield","Williamsbridge","Woodlawn","Norwood","Bedford Park","Fordham","Belmont","Tremont","Kingsbridge","Riverdale","Fieldston","Highbridge","Concourse"])
 +NOTE('Serving all of the Bronx. Tell us the neighborhood and whether the car lives in a garage, a driveway, or on the street.')))

BODY.append(sec('Your Options','Open or Enclosed in the Bronx?',
 prose(
  L('Most Bronx cars ride open, and the corridor lanes are built around it.'),
  P('An enclosed trailer keeps salt, grit, and attention off the car. The garages in Riverdale, Fieldston, and Country Club book enclosed trailers. Many cars headed south for the winter ride the same way.'),
  P('An everyday car is fine in the open. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('Settle the price, drive a few minutes to the spot, and collect the car at the other end. The parkways and the game schedule decide the spot.'),
  P('When you approve the price, we assign a carrier already working the corridor and tell you the spot. At the spot, the driver and you fill in a Bill of Lading and both sign. The delivery inspection is measured against that sheet.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Take photos before the car leaves the garage or the block",
  "Leave a working key and tell us about any mechanical issues",
  "Switch off any aftermarket alarm",
  "Pick a pickup morning that is not an alternate-side day or a home game",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages cover the rest.'))))

BODY.append(sec('Why Ship Guy','Why Bronx Drivers Choose Ship Guy',
 prose(
  L('We know which Bronx roads carry the truck and which lots can host it. The spot is settled before the driver leaves the yard.'),
  P('Every booking is backed by active FMCSA brokerage authority and a $75,000 surety bond. Our office is on Waters Place by the Hutchinson Metro Center.'),
  P('The same coordinator stays with the shipment from quote to delivery. Open, enclosed, and expedited transport are all available. The <a href="services.html">services</a> page covers the whole range.'),
 ), alt=True))

BODY.append(office('Bronx','1250 Waters Pl Suite 477','Bronx, NY 10461','+19297021459','(929) 702-1459','ET',
 '1250+Waters+Pl+Suite+477,+Bronx,+NY+10461','Visit Us','Find Ship Guy in the Bronx',
 'Our office is on Waters Place by the Hutchinson Metro Center, minutes from the Bruckner.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5104.414202195183!2d-73.8375873!3d40.853167!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c28d0d4a815405%3A0xc3636be6c9346168!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792023085311!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come to my block in the Bronx?","On a driveway block in Throgs Neck, Country Club, Morris Park, or Woodlawn, often yes. On the Concourse, in Belmont, in Riverdale, or anywhere the parkways are the only way in, no. The driver waits at an industrial block, a shopping-center lot, or a wide boulevard a few minutes away."),
 ("Where are the usual meeting spots in the Bronx?","Hunts Point and Port Morris for the South Bronx. The Co-op City shopping center for the northeast. The Waters Place lots for Westchester Square and Morris Park. The stadium lots on non-game days for the Concourse. Broadway by Van Cortlandt Park for Riverdale. The park lots under the Throgs Neck Bridge for the east shore."),
 ("How much does it cost to ship a car from the Bronx to Florida?","Plan on seven hundred seventy to one thousand ninety dollars for a sedan to Orlando. Miami adds a little. The trip covers about eleven hundred miles of Interstate 95. Fall southbound prices run above spring. SUVs and pickups add 10 to 25 percent."),
 ("Are the bridge tolls added to my price?","No. The carrier pays whichever crossing the route uses, from the George Washington to the Throgs Neck. It prices the trip with the tolls inside. The number you approve is the number you pay."),
 ("Does a Yankees home game affect my pickup?","Around the stadium, yes. The Deegan, the Concourse, and the streets around 161st fill for hours. We schedule Concourse, Highbridge, and Kingsbridge pickups for non-game days. The east and north Bronx run normally."),
 ("Do you ship cars for residents at the Bronx hospitals?","Yes, every June and July. The medical center in Norwood and the hospital campus in Morris Park bring in residents from every state. Most come with a car. The handoff happens on Eastchester Road, on the Pelham Parkway service road, or at the Waters Place lots."),
 ("Can you ship a car for a Fordham, Lehman, Manhattan College, or Maritime student?","Yes. Student cars come in each August and go home each May. The campus streets are tight. The driver meets you on Fordham Road, on Broadway, or at the park lots by Throgs Neck. An adult signs for the car at pickup."),
 ("Can you pick up on City Island or in Riverdale?","Yes, with a short drive. City Island has one narrow bridge, and the handoff happens on the mainland side by Pelham Bay Park. Riverdale sits on hills with no truck access. The driver meets you on Broadway near Van Cortlandt Park or at a lot on the Deegan."),
 ("Can you ship a car that does not run from the Bronx?","Yes. We send a carrier with a winch, and the slower loading is reflected in the quote. The spot has to be flat and wide, which usually means Hunts Point or the Co-op City lots. Say whether it rolls, steers, and brakes."),
 ("What do you need for a Bronx car shipping quote?","Where the car is and where it is going, with the neighborhood on the Bronx end. Garage, driveway, or street. Year, make, and model. Whether it runs. Open or enclosed, and the dates you can work with. That covers a Bronx quote."),
]
BODY.append(faq_section(FAQ,'Bronx FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in the Bronx?','The form above prices the lane in about two minutes. Give us the neighborhood and your dates, and the spot is settled before the driver leaves the yard.','+19297021459','(929) 702-1459','Get your free Bronx quote'))

build({
 'slug':'auto-transport-bronx-new-york',
 'title':'Car Shipping in the Bronx, NY — Auto Transport | Ship Guy',
 'meta':'Car shipping in the Bronx, NY on the Cross Bronx, the Deegan, and the Bruckner. Meeting spots at Hunts Point, Co-op City, and Waters Place, Riverdale and City Island pickups, hospital and college timing, Yankees game days, the Florida lane, tolls built in. Free quote.',
 'h1':'Car Shipping in<br>the Bronx, <span class="accent">New York</span>',
 'lede':'Open, enclosed, and expedited auto transport across the borough, planned around the expressways, the parkways, and the game schedule.',
 'tel':'+19297021459','disp':'(929) 702-1459','brand':'The Bronx','keyword':'car shipping in the bronx',
 'localterms':['bronx','cross bronx','major deegan','bruckner','interstate 95','interstate 87','interstate 278','interstate 295','interstate 678','hutchinson','bronx river','pelham parkway','mosholu','henry hudson','george washington','rfk','throgs neck','whitestone','grand concourse','fordham road','tremont','boston road','waters place','hutchinson metro center','hunts point','port morris','mott haven','melrose','soundview','co-op city','pelham bay','baychester','eastchester','wakefield','westchester square','morris park','country club','city island','riverdale','fieldston','van cortlandt','kingsbridge','highbridge','concourse','fordham','belmont','norwood','bedford park','woodlawn','stadium','yankees','zoo','botanical garden','medical center','hospital','residents','university','maritime','market','florida','boca','snowbird','hartford','philadelphia','boston','albany','washington'],
}, BODY, FAQ)
