import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Support")]))

BODY.append(intro_block('Tennessee','Tennessee auto transport across the crossroads of the South',
 ['Tennessee auto transport sits where the Chicago-to-Florida lane crosses the Carolinas-to-Texas lane, and the state fills with newcomers who came for the same reason the carriers do.',
  'Ship Guy is a licensed auto transport broker. We book vetted carriers across Tennessee, and we do not own the trucks.',
  'Interstate 40 crosses the whole state from Memphis through Nashville to Knoxville and the Smokies. Interstate 65 carries Nashville between Louisville and Alabama, Interstate 24 links Chattanooga to Clarksville, and Interstate 75 and 81 reach Knoxville and the Tri-Cities.',
  'This page covers the corridors, Nashville and the newcomers, Memphis and the cargo hub, Knoxville and Chattanooga, the plants, the post, the Smokies, and the weather that stops a hilly state.'],
 'Tennessee at a glance',
 ['Most pickups happen within 1 to 3 days in Nashville, Memphis, Knoxville, and Chattanooga, and within 2 to 4 days in the Smokies, the Cumberland Plateau, and the farm counties.',
  'Louisville, Birmingham, Atlanta, and Memphis are same-day lanes from Nashville. St. Louis, Indianapolis, and Charlotte take a day. Florida, Texas, and Chicago run two.'],
 'Tennessee has no city page yet, so this page carries the detail for Nashville, Memphis, Knoxville, Chattanooga, Clarksville, and the rest.'))

BODY.append(sec('The Corridors','Interstate 40, 65, 24, 75, and 81',
 prose(
  L('Nashville sits where four interstates meet, and carriers stage there for the whole mid-South.'),
  P('Interstate 40 runs from Memphis through Jackson, Nashville, Cookeville, and Knoxville to the Pigeon River gorge and North Carolina. The gorge was torn apart by a hurricane in 2024 and has run with restrictions since.'),
  P('Interstate 65 carries the Chicago-to-Florida lane through Nashville and Franklin to Alabama. Interstate 24 runs from Clarksville through Nashville to Chattanooga and Georgia.'),
  P('Interstate 75 carries the Detroit-to-Florida lane through Chattanooga and Knoxville, and Interstate 81 runs from Knoxville through the Tri-Cities to Virginia. Interstate 26 climbs from Kingsport into North Carolina.'),
  P('Towns on those roads schedule fast. The Cumberland Plateau, the Smokies, and the West Tennessee farm counties take an extra day or two.'),
 ), alt=True))

BODY.append(sec('Nashville','The Newcomers, the Hospitals, and Williamson County',
 prose(
  L('Nashville grew faster than almost any city in the country this decade, and most of the newcomers shipped a car.'),
  P('Households from California, Illinois, and New York fill Franklin, Brentwood, Mount Juliet, and Murfreesboro on closing dates all year, drawn by the absence of a state income tax. Most ship one car and drive the other.'),
  P('The healthcare headquarters, the music industry, and the tech campuses relocate employees on start dates. The medical center moves residents every June, and the campuses send cars in each August.'),
  P('The older neighborhoods in East Nashville and Hillsboro have narrow streets and hills, and the driver meets you on a main road. Williamson County subdivisions are wide but gated, so send the community name.'),
  P('If your employer reimburses the shipment, we provide the documentation. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 )))

ROUTES=[("Louisville, KY","I-65 · ~175 mi","Same day","$220–$340"),("Birmingham, AL","I-65 · ~190 mi","Same day","$220–$340"),
 ("Memphis, TN","I-40 · ~210 mi","Same day","$230–$350"),("Atlanta, GA","I-24/I-75 · ~250 mi","Same day","$250–$380"),
 ("Indianapolis, IN","I-65 · ~290 mi","1 day","$270–$400"),("St. Louis, MO","I-24/I-57 · ~310 mi","1 day","$280–$420"),
 ("Charlotte, NC","I-40/I-77 · ~410 mi","1 day","$370–$540"),("Chicago, IL","I-65 · ~470 mi","1–2 days","$400–$580"),
 ("Dallas, TX","I-40/I-30 · ~660 mi","2 days","$480–$700"),("Orlando, FL","I-24/I-75 · ~690 mi","2 days","$500–$730")]
BODY.append(rate_table('Lanes &amp; Costs','Tennessee Car Shipping Lanes and Estimated Costs',
 'Common lanes out of Nashville, with estimated open-transport ranges. Memphis sits closer to Texas and Arkansas, and Knoxville closer to the Carolinas. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from Nashville. SUVs and pickups add about 10 to 25 percent, enclosed more. Season and carrier availability on your dates set the real quote.',
 prose(
  P('Louisville, Birmingham, Atlanta, and Memphis are the cheapest lanes, because Interstate 65, 24, and 40 carry carriers between them all day. The Florida lane swings with the fall migration.'),
  P('The inbound lanes from California, Illinois, and New York run full year round. The <a href="car-shipping-cost.html">cost guide</a> explains the other variables.'),
 ), alt=True))

BODY.append(sec('Memphis','The Cargo Hub, the River, and the New Plant',
 prose(
  L('Memphis moves more air cargo than any city in the world, and the trucking that goes with it keeps carriers close.'),
  P('The package hub at the airport, the distribution centers along Interstate 40 and 55, and the river port keep thousands of trucks based in the metro. A private pickup in Memphis, Germantown, or Collierville slots into that flow.'),
  P('The children\u2019s research hospital and the medical district move residents and staff every June. The new electric-vehicle plant east of the city relocates engineers and workers on hiring schedules.'),
  P('The naval support activity in Millington rotates personnel and civilians on program dates. Memphis ships on the Interstate 40 lane to Little Rock, Dallas, and Oklahoma City, and on Interstate 55 to St. Louis and Jackson.'),
  P('The Mississippi and Arkansas suburbs share the Memphis carrier pool.'),
 )))

BODY.append(sec('Knoxville &amp; Chattanooga','The University, the Lab, the Plant, and the Ridges',
 prose(
  L('East Tennessee ships on a campus, a national laboratory, a car plant, and terrain that bends every road.'),
  P('The University of Tennessee sends cars in each August and home each May, and home football Saturdays close the streets around the stadium. The national laboratory in Oak Ridge relocates scientists on program schedules.'),
  P('Chattanooga builds cars at the German plant on the east side and relocates engineers on program dates. The city sits between ridges, and its older neighborhoods climb them, so the driver meets you on a main road.'),
  P('The Tri-Cities of Bristol, Kingsport, and Johnson City ship on Interstate 81 and 26, and the speedway fills Bristol twice a year. Campus handoffs happen at a lot nearby, and an adult signs for a student car.'),
 ), alt=True))

BODY.append(sec('The Plants &amp; the Post','Smyrna, Spring Hill, and Fort Campbell',
 prose(
  L('Middle Tennessee builds vehicles and trains soldiers, and both keep carriers busy.'),
  P('The Japanese plant in Smyrna and the American plant in Spring Hill load carriers every day, and those carriers take private cars on the return run. The battery plants around them relocate engineers on program schedules.'),
  P('Fort Campbell straddles the Kentucky line at Clarksville and deploys and returns whole brigades. Families rotate year round, with the heaviest moves from May through August, and Clarksville grew into one of the fastest-growing cities in the state because of it.'),
  P('Housing is gated, so the driver meets you outside it. Many families ship a second vehicle through us, since orders may cover only one.'),
  P('Ship Guy is a private broker with no military affiliation. Our <a href="military-car-shipping.html">military</a> page covers PCS timing.'),
 )))

BODY.append(sec('The Smokies &amp; the Weather','Gatlinburg, the Plateau, Ice, and Floods',
 prose(
  L('The mountains and the weather shape Tennessee shipping more than the distances do.'),
  P('Gatlinburg, Pigeon Forge, and Sevierville fill with tourists from spring through the holidays, and the parkway crawls. The mountain roads are steep and narrow, so the driver meets you on the parkway or in Sevierville.'),
  P('Ice is the big one. Nashville and its hills shut down on a light glaze, and an ice storm closes the whole state for days a few times a decade. No one moves a loaded trailer on it.'),
  P('Tornado season runs March through May, with a second season in December. When a warning is issued, the driver pulls over and waits.'),
  P('Floods hit the state hard, from the rivers in Middle Tennessee to the hurricane damage in the northeast corner. A flooded road waits for the water to drop, and fog closes Interstate 75 near the Georgia line on fall mornings.'),
 )+chips(["Nashville","Franklin","Brentwood","Murfreesboro","Mount Juliet","Hendersonville","Clarksville","Smyrna","Spring Hill","Memphis","Germantown","Collierville","Bartlett","Jackson","Knoxville","Oak Ridge","Maryville","Sevierville","Gatlinburg","Chattanooga","Cleveland","Cookeville","Johnson City","Kingsport","Bristol"])
 +NOTE('Serving all ninety-five Tennessee counties. For a gated community, a mountain address, or a farm road, tell us the town and we will name the meeting spot.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Tennessee?',
 prose(
  L('Open transport is the everyday choice, and the inbound lanes and the Florida lane run on it.'),
  P('Enclosed transport keeps a car covered against ice, pollen, and storm debris. Belle Meade, Brentwood, and the lake communities keep enclosed carriers busy with collector cars.'),
  P('A commuter car rides open without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on the corridor, and a delivery, with the hills and the ice deciding the timing in winter.'),
  P('Once the price is approved, a carrier on Interstate 40, 65, or 24 takes the booking. The driver notes the car\u2019s condition on a Bill of Lading, and you sign it before loading. That note is your checklist at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "For a gated community or a mountain address, plan to meet the truck at the entrance or on the parkway",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides go step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Tennessee Drivers Choose Ship Guy',
 prose(
  L('We use the traffic that already crosses at Nashville and plan around the ice, the games, and the gorge.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both verifiable in federal records.'),
  P('One coordinator handles the shipment from quote to delivery and can set up open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows the full range.'),
 )))

FAQ=[
 ("How much does it cost to ship a car to Nashville from California or the Northeast?","Los Angeles to Nashville usually runs a thousand fifty to fourteen hundred fifty dollars for a sedan, about two thousand miles on Interstate 40. New York runs six hundred twenty to eight hundred eighty, about eight hundred ninety miles. Both lanes run full with newcomers, which keeps them competitive. Larger vehicles add 10 to 25 percent."),
 ("Can you handle a PCS move to Fort Campbell?","Yes, the post at Clarksville rotates brigades year round, with the heaviest moves from May through August. Many families ship a second vehicle through us, since orders may cover only one. Housing is gated, so the driver meets you outside it. Ship Guy has no military affiliation."),
 ("What happens if ice hits Nashville during my shipment?","Carriers wait it out. Nashville's hills shut down on a light glaze, and an ice storm closes the whole state for days a few times a decade. No one moves a loaded trailer on it. We tell you the moment the forecast changes the plan and reschedule when the roads clear."),
 ("Do you serve Memphis?","Yes, Memphis is one of our busiest lanes in the state. The cargo hub and the distribution centers keep thousands of trucks based in the metro, and a private pickup slots into that flow. Little Rock, Dallas, St. Louis, and Jackson are the natural lanes, and the Mississippi and Arkansas suburbs share the carrier pool."),
 ("Can you ship a car for a University of Tennessee or Vanderbilt student?","Yes, student cars move each August and again in May. Home football Saturdays close the streets around the Knoxville stadium, so we schedule around the games. Nashville campus streets are tight, so the handoff happens at a lot nearby. An adult signs for the car."),
 ("Can you deliver to Gatlinburg or Pigeon Forge?","Yes, with a meeting spot. The mountain roads are steep and narrow, and the parkway crawls in tourist season. The driver meets you on the parkway or in Sevierville, and Smokies pickups run 2 to 4 days."),
 ("Is Interstate 40 through the gorge open?","It has run with restrictions since the 2024 hurricane tore apart the Pigeon River gorge at the North Carolina line. A carrier headed east from Knoxville plans for it, and some route through Interstate 81 and 26 instead. We tell you when the gorge is in play."),
 ("Can the carrier come inside my community in Franklin or Brentwood?","It depends on the community. Williamson County subdivisions are wide but often gated, and where the truck cannot enter, the driver meets you at the entrance. Send the community name and the gate code when you book."),
 ("Can you ship a car that does not run?","Yes, non-running cars ship from every part of Tennessee. A winch-equipped carrier loads it, and the extra time carries a fee. Tell us whether it can roll, steer, and brake."),
 ("What do you need for a Tennessee car shipping quote?","Both addresses, with the community name for a gated address. The year, make, and model. Whether it runs and rolls. Open or enclosed, and a date range. That is a complete Tennessee quote request."),
]
BODY.append(faq_section(FAQ,'Tennessee FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book auto transport in Tennessee?','A quote takes about two minutes. Then tell us your town and dates, and we will match you with a carrier already crossing the state.','+18664992815','(866) 499-2815','Get your free Tennessee quote'))

build_state({
 'slug':'tennessee-auto-transport',
 'title':'Tennessee Auto Transport &amp; Car Shipping | Ship Guy',
 'meta':'Tennessee auto transport across the crossroads of the South. Nashville newcomers and Williamson County gates, the Memphis cargo hub, Knoxville and Chattanooga, Fort Campbell moves, the Smokies, ice and flood planning, the Interstate 40 gorge. Free quote.',
 'h1':'Tennessee<br>Auto <span class="accent">Transport</span>',
 'lede':'Open, enclosed, and expedited car shipping across Tennessee, using the lanes that already cross at Nashville.',
 'brand':'Tennessee','keyword':'tennessee auto transport','abbr':'TN',
 'localterms':['tennessee','interstate 40','interstate 65','interstate 24','interstate 75','interstate 81','interstate 26','interstate 55','nashville','franklin','brentwood','williamson','murfreesboro','clarksville','fort campbell','smyrna','spring hill','plant','memphis','germantown','collierville','cargo','hub','millington','knoxville','oak ridge','laboratory','university of tennessee','chattanooga','tri-cities','bristol','kingsport','johnson city','sevierville','gatlinburg','pigeon forge','smokies','cumberland plateau','pigeon river','gorge','ice','tornado','flood','no income tax','california'],
}, BODY, FAQ)
