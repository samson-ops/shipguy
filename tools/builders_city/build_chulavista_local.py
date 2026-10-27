import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Chula Vista, California','Car shipping in the South Bay, ten minutes from the Navy piers and ten minutes from the border',
 ['Car shipping in Chula Vista follows the Navy calendar more than any other. Ship Guy is a licensed auto transport broker with an office on Fenton Street in Eastlake.',
  'We book vetted carriers across the South Bay, from the bayfront to Otay Ranch and Imperial Beach. We do not own the trucks.',
  'Interstate 5 runs up the bayfront and Interstate 805 runs up the middle of the city. Highway 54 crosses the north edge to the 125, the toll road up the east side. Highway 905 and the 125 reach the Otay Mesa crossing in ten minutes.',
  'This page covers the freeways and the toll road, the west side, the east side, and the gates. It also covers the Navy, the border, the hospitals, the college, the fire season, and the lanes.'],
 'Chula Vista at a glance',
 ['Most pickups happen within 1 to 3 days. The San Diego carrier pool is one of the largest in the state. The 5 and the 805 bring it through the city.',
  'Los Angeles, Riverside, and Orange County are same-day lanes. Phoenix and Las Vegas take a day. The Bay Area takes one to two. The Navy lanes to Norfolk and Jacksonville run six to eight.'],
 'Tell us the neighborhood and the gate. The west side streets and Bonita need a meeting spot. Eastlake, Otay Ranch, and the newer villages meet the truck at the gate or the town center lot.'))

BODY.append(sec('The Roads','Interstate 5, 805, Highway 54, 905, and the 125 Toll Road',
 prose(
  L('Chula Vista sits on the last twenty miles of Interstate 5. Every carrier serving San Diego passes it.'),
  P('Interstate 5 runs along the bayfront from downtown San Diego to the border at San Ysidro. Interstate 805 runs up the middle of the city and rejoins the 5 north of downtown. The two carry the whole South Bay, and the Navy piers sit a few exits north on both.'),
  P('Highway 54 runs along the Sweetwater River across the north edge of the city. The 125 is the toll road up the east side from Otay Mesa to Spring Valley. Carriers pay it by transponder, and the toll goes into a quote that uses it. Most pickups use the 805 instead, with no toll.'),
  P('Highway 905 runs from the 5 and the 805 to the truck crossing at Otay Mesa. The carriers come off the 805 at E Street, H Street, Telegraph Canyon, and Olympic Parkway. The town center lots in Eastlake and Otay Ranch are the usual meeting spots.'),
  P('Our office sits on Fenton Street in the Eastlake business center, minutes from the 125 and Olympic Parkway.'),
 ), alt=True))

BODY.append(sec('West Side, East Side','Third Avenue, the Bayfront, Bonita, Eastlake, Otay Ranch, and the Gates',
 prose(
  L('Chula Vista is two cities, an old one by the bay and a planned one on the mesa. The handoff follows the side.'),
  P('The west side is the old city, from Third Avenue and the bayfront to the blocks along Broadway. The streets are narrow, parked solid, and lined with alleys. The driver meets you on Broadway, on H Street, or at the marina lots. The new resort and the bayfront construction close the waterfront roads now and then.'),
  P('Bonita is horse country, with narrow roads, no curbs, and low trees along the Sweetwater. The driver meets you on Bonita Road or at the shopping center by the 805.'),
  P('The east side is the planned city. Eastlake, Rolling Hills Ranch, San Miguel Ranch, and the newer villages in Otay Ranch are gated or association-run. A seventy-five-foot trailer cannot wait on a village street. The handoff happens at the gate, the clubhouse, or the town center lot.'),
  P('Millenia and the newest villages south of Olympic Parkway are still being built. The streets are not on a carrier’s map yet. Send the full address and the nearest arterial. Rancho del Rey, Sunbow, and Terra Nova are open grids where a curb handoff usually works.'),
 )))

ROUTES=[("Los Angeles, CA","I-5 · ~130 mi","Same day","$160–$260"),("Riverside, CA","I-15 · ~110 mi","Same day","$150–$250"),
 ("Irvine, CA","I-5 · ~90 mi","Same day","$140–$230"),("Phoenix, AZ","I-8/I-10 · ~360 mi","1 day","$330–$480"),
 ("Las Vegas, NV","I-15 · ~340 mi","1 day","$320–$460"),("San Jose, CA","I-5 · ~480 mi","1–2 days","$400–$570"),
 ("Sacramento, CA","I-5 · ~520 mi","1–2 days","$420–$600"),("Dallas, TX","I-10/I-20 · ~1,360 mi","3 days","$900–$1,250"),
 ("Jacksonville, FL","I-10 · ~2,400 mi","5–7 days","$1,300–$1,800"),("Norfolk, VA","I-10/I-40 · ~2,700 mi","6–8 days","$1,500–$2,000")]
BODY.append(rate_table('Lanes &amp; Costs','Chula Vista Car Shipping Lanes and Estimated Costs',
 'The lanes Chula Vista ships most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, open trailer. Add about 10 to 25 percent for an SUV or pickup, and more for enclosed. PCS season, fire season, and the carriers free on your dates set the final figure.',
 prose(
  P('Chula Vista prices like San Diego, because the same carrier pool serves both. Los Angeles and Orange County ride the 5 north, and Phoenix rides the 8 east.'),
  P('The Navy lanes to Norfolk, Jacksonville, and Pensacola run every month, and the summer rotation fills them. The <a href="car-shipping-cost.html">cost guide</a> goes through the rest of the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Navy, the Border, the Hospitals, and the College',
 prose(
  L('Chula Vista relocates sailors, nurses, border workers, and students, and the Navy sets the pace.'),
  P('Naval Base San Diego sits fifteen minutes north on the 5. Coronado and the air station sit across the bay. More Navy families live in Chula Vista than in most cities in the county. Most orders move one car, and the family car comes with us. The base gates stop the truck. The handoff happens on Main Street or at a lot off the 5.'),
  P('Sailors ship cars in from Norfolk, Jacksonville, and Pensacola every summer and back out when the orders come. The <a href="military-car-shipping.html">military</a> page covers a PCS move in detail. Ship Guy is a private broker with no connection to the Navy.'),
  P('The border is ten minutes south, and thousands of residents cross it for work every day. We ship within the United States only. A car coming up from Tijuana meets the truck on this side after it clears customs. The warehouses in Otay Mesa hire managers on start dates all year.'),
  P('The two hospitals on the east side bring in nurses and residents every summer. The college on Otay Lakes Road fills each August and empties each May. The campus lots work for the handoff. The athlete training center on the lake brings in athletes and coaches on a calendar of its own.'),
  P('A reimbursed move gets its paperwork from us, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','PCS Season, Fire Season, May Gray, and the Border Traffic',
 prose(
  L('Chula Vista has the easiest weather on this site and the hardest calendar.'),
  P('The Navy rotates on a summer peak, and June through August fill the lanes in both directions. A car booked for the Norfolk lane in July needs two to three weeks of notice. The rest of the year the lanes run with room to spare.'),
  P('Santa Ana winds blow from September into December, and fire season comes with them. The east side has burned up to the villages before, and the 125 closes when it does. Evacuation orders and smoke push a pickup to the west side for a day. We call when that happens.'),
  P('May gray and June gloom keep the mornings cool by the bay. The mesa runs ten degrees warmer. Winter rain is rare and heavy when it comes. The Sweetwater and Otay rivers flood the low roads for a day. Summer heat on the east side moves the loading hour earlier.'),
  P('Border traffic fills the 5 and the 805 south of the city every morning. The truck crossing at Otay Mesa backs up onto the 905. A pickup near the border happens mid-morning or early afternoon for that reason.'),
 )+chips(["Third Avenue","Bayfront","Broadway","Harborside","Otay","Bonita","Rancho del Rey","Terra Nova","Sunbow","Eastlake","Rolling Hills Ranch","San Miguel Ranch","Otay Ranch","Millenia","Olympic Parkway","Telegraph Canyon","Otay Lakes Road","Otay Mesa","San Ysidro","National City","Imperial Beach","Spring Valley","La Mesa","Coronado"])
 +NOTE('Serving Chula Vista and the whole South Bay. Tell us the village, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Chula Vista?',
 prose(
  L('Open trailers carry most of what leaves the South Bay, and the Navy lanes are priced for them.'),
  P('An enclosed trailer keeps the salt air, the sun, and attention off the car. The garages in Eastlake and San Miguel Ranch book enclosed trailers. So does a car headed across the country to a new duty station in winter.'),
  P('A commuter car rides open to Los Angeles or Phoenix and arrives the way it left. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages show what the roof adds and what it costs.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the gate or by the freeway, and a delivery. The orders usually pick the week.'),
  P('Say yes to the price, and a carrier already serving the South Bay gets the booking. The spot is set with the gate in mind. You and the driver go over the car and record it on a Bill of Lading. Both sign, and delivery is inspected against it.'),
 )+ULI([
  "Take your personal items out of the car",
  "Keep the fuel to about a quarter tank",
  "Photograph every panel before pickup, salt air included",
  "Leave a working key with the driver and mention any mechanical issue",
  "Shut off the aftermarket alarm if it has one",
  "Bring your orders and the gate pass if the handoff is near the base",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages walk through the rest.'))))

BODY.append(sec('Why Ship Guy','Why Chula Vista Drivers Choose Ship Guy',
 prose(
  L('We work the 5 and the 805 every day. We plan around the gates, the orders, and the fire season.'),
  P('The FMCSA lists Ship Guy as an active broker. A $75,000 surety bond is on file behind every booking. Our office is on Fenton Street in Eastlake.'),
  P('One coordinator stays with the booking from the quote to the delivery signature. You can book open, enclosed, or expedited transport, and the <a href="services.html">services</a> page describes each one.'),
 ), alt=True))

BODY.append(office('Chula Vista','2434 Fenton St #487','Chula Vista, CA 91914','+16199326392','(619) 932-6392','PT',
 '2434+Fenton+St+%23487,+Chula+Vista,+CA+91914','Visit Us','Find Ship Guy in Chula Vista',
 'Our office is on Fenton Street in the Eastlake business center, minutes from the 125 and Olympic Parkway.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4146.6611178502235!2d-116.9574643!3d32.650917!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80d94502a0ad4fe3%3A0x8f7958262e4fa38a!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792077087391!5m2!1sen!2sus'))

FAQ=[
 ("Do you handle a PCS move to Naval Base San Diego or Coronado from Chula Vista?","Yes, every week. More Navy families live in Chula Vista than in most cities in the county. Most orders move one car, and the family car comes with us. The gates stop the truck. The handoff happens on Main Street or at a lot off the 5. Ship Guy is a private broker with no connection to the Navy."),
 ("How much does it cost to ship a car from Chula Vista to Norfolk or Jacksonville?","Norfolk runs fifteen hundred to two thousand dollars for a sedan, about twenty-seven hundred miles across the south. Jacksonville runs thirteen hundred to eighteen hundred, about twenty-four hundred miles on Interstate 10. Summer orders season costs more than winter. SUVs and pickups add 10 to 25 percent."),
 ("Can the carrier come into Eastlake, Otay Ranch, or another gated village?","Not past the gate or onto a village street. The driver meets you at the gate, the clubhouse, or the town center lot. Send the gate code or the guard’s name with the booking."),
 ("Can you ship a car that is coming from Tijuana?","Only once it is on this side of the border. We ship within the United States, and the ocean and border legs are separate. The car meets the truck in Chula Vista or San Ysidro after it clears customs. Tell us which plate it carries, because it changes the paperwork."),
 ("What happens if a fire closes the 125 or the east side on my pickup day?","The pickup moves to the west side for a day. Santa Ana winds push fire toward the villages from September into December. Evacuation orders close the toll road and the canyon streets. We call as soon as the plan changes. A car already loaded keeps moving."),
 ("Does the 125 toll change the price?","Only if the carrier uses it. The toll road up the east side is paid by transponder. The toll goes into the quote when a route needs it. Most Chula Vista pickups use the 805 and the 5 with no toll."),
 ("Can you ship a car for a Southwestern College student?","Yes. The cars come in each August and leave each May. The campus lots on Otay Lakes Road work for the handoff. An adult signs for the car at pickup, and a parent can sign at the far end."),
 ("Do you ship cars for nurses hired at the hospitals on the east side?","Yes, on start dates every summer and all year. Nurses and residents arrive from every state, and most bring a car. The handoff happens on Medical Center Drive or at the town center lot, not in a hospital garage."),
 ("Can you ship a car that does not run from Chula Vista?","Yes. We send a winch carrier, and the longer loading is part of the price. Pick a flat spot, which here means the town center lot rather than a village street. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Chula Vista car shipping quote?","Both addresses, with the village and the gate on this end. The year, make, and model. Whether it runs. Open or enclosed. Your dates, with the report date in mind if orders are involved. That is everything a Chula Vista quote needs."),
]
BODY.append(faq_section(FAQ,'Chula Vista FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Chula Vista?','The form above gives you a price in about two minutes. Tell us the village and your dates. A carrier already in the South Bay takes it from there.','+16199326392','(619) 932-6392','Get your free Chula Vista quote'))

build({
 'slug':'auto-transport-chula-vista-california',
 'title':'Car Shipping in Chula Vista, CA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Chula Vista, CA on the 5 and the 805 in the South Bay. Navy PCS second vehicles to Norfolk and Jacksonville, Eastlake and Otay Ranch gate handoffs, west side meeting spots, border and customs rules, the 125 toll explained, fire season planning. Local office on Fenton Street. Free quote.',
 'h1':'Car Shipping in<br>Chula Vista, <span class="accent">California</span>',
 'lede':'Open, enclosed, and expedited auto transport across the South Bay, planned around the gates, the orders, and the border.',
 'tel':'+16199326392','disp':'(619) 932-6392','brand':'Chula Vista','keyword':'car shipping in chula vista',
 'localterms':['chula vista','interstate 5','805','highway 54','905','125','toll road','otay mesa','san ysidro','border','customs','tijuana','e street','h street','telegraph canyon','olympic parkway','otay lakes road','fenton street','main street','broadway','third avenue','bayfront','marina','resort','bonita','sweetwater','rancho del rey','sunbow','terra nova','eastlake','rolling hills ranch','san miguel ranch','otay ranch','millenia','town center','gate','village','navy','naval base','coronado','air station','norfolk','jacksonville','pensacola','orders','hospitals','nurses','college','training center','warehouses','santa ana winds','fire','may gray','june gloom','los angeles','riverside','irvine','orange county','phoenix','las vegas','san jose','sacramento','dallas','national city','imperial beach'],
}, BODY, FAQ)
