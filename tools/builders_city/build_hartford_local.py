import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Hartford, Connecticut','Car shipping in the insurance capital, where Interstate 84 crosses Interstate 91 on the river',
 ['Car shipping in Hartford runs on the insurers’ start dates and the engine plant’s program schedules. Ship Guy is a licensed auto transport broker with an office on Church Street downtown.',
  'We book vetted carriers across greater Hartford, from West Hartford and Glastonbury to Manchester, Farmington, and Windsor. We do not own the trucks.',
  'Interstate 91 runs north and south along the river between New Haven and Springfield. Interstate 84 crosses it downtown on the way from Waterbury to Boston. Route 2 leaves for Glastonbury and the casinos, and Route 9 runs south to Middletown.',
  'This page covers the two interstates and the river, downtown and the neighborhoods, and the suburbs. It also covers the insurers, the engine plant, the hospitals, the universities, the snow, and the lanes.'],
 'Hartford at a glance',
 ['Most pickups happen within 1 to 3 days. Two interstates bring carriers through the city from four directions all day.',
  'New Haven, Springfield, and Providence are same-day lanes. Boston and Albany are the same day too. Manhattan takes a day. Philadelphia takes one to two, and Florida runs three.'],
 'Tell us the neighborhood. Downtown towers, the West End, and the South End need a meeting spot. West Hartford, Glastonbury, and the suburban grids usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 84, 91, Route 2, Route 9, and the River Bridges',
 prose(
  L('Hartford is the crossroads of New England. Every carrier taking the inland route between New York and Boston passes it.'),
  P('Interstate 91 runs along the west bank of the river from New Haven to Springfield. Interstate 84 comes in from Waterbury on the viaduct over downtown. It crosses the river on the Bulkeley Bridge to East Hartford. The interchange between them sits by the river, and it backs up in both rushes.'),
  P('Route 2 leaves 84 in East Hartford for Glastonbury and the casinos. Route 9 leaves 91 south of town for Middletown and the shore. Route 15 crosses the river on the Charter Oak Bridge. The Berlin Turnpike carries the retail strip south of the city.'),
  P('The carriers come off 91 at Trumbull Street and Brainard Road. On 84 they use Sisson Avenue and Flatbush Avenue. The lots along Brainard Road are the usual meeting spot. The Manchester mall and Corbins Corner in West Hartford are the backups. No road in the region charges a toll.'),
  P('Our office sits on Church Street downtown, a block from Main Street.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the West End, the South End, West Hartford, and the Suburbs',
 prose(
  L('Hartford is a small downtown of towers, a ring of old neighborhoods, and a wide circle of suburbs. The handoff follows the ring.'),
  P('Downtown is towers, garages, and one-way streets around the arena and the ballpark. The garage brings the car out. The driver meets you at a lot on Brainard Road or by the river. Asylum Hill holds the insurers’ headquarters and their own garages.'),
  P('The West End has big houses on narrow streets under old trees. The South End, Frog Hollow, and Parkville are tight grids of three-family houses with cars on both curbs. The driver meets you on Farmington Avenue, on Franklin Avenue, or at a lot off 84.'),
  P('West Hartford, Wethersfield, Newington, and Glastonbury are wide suburban grids where the truck usually reaches the curb. West Hartford Center and Old Wethersfield are the exceptions, with tight historic streets. Farmington, Avon, and Simsbury wind through the valley on roads with no shoulders.'),
  P('East Hartford holds the engine plant. Manchester holds the mall and the warehouses off 84. Windsor and Windsor Locks hold the airport, the aerospace plants, and the warehouses off 91. A handoff at a plant gate or an office lot works when the employer allows it.'),
 )))

ROUTES=[("New Haven, CT","I-91 · ~40 mi","Same day","$120–$200"),("Springfield, MA","I-91 · ~25 mi","Same day","$110–$190"),
 ("Providence, RI","I-84/US-6 · ~75 mi","Same day","$160–$260"),("Boston, MA","I-84/I-90 · ~100 mi","Same day","$180–$290"),
 ("Albany, NY","I-91/I-90 · ~110 mi","Same day","$190–$300"),("Manhattan, NY","I-91/I-95 · ~115 mi","1 day","$190–$300"),
 ("Philadelphia, PA","I-84/I-95 · ~210 mi","1 day","$240–$360"),("Washington, DC","I-91/I-95 · ~340 mi","1 day","$300–$440"),
 ("Charlotte, NC","I-95/I-85 · ~730 mi","2 days","$520–$750"),("Orlando, FL","I-95 · ~1,180 mi","3 days","$800–$1,130")]
BODY.append(rate_table('Lanes &amp; Costs','Hartford Car Shipping Lanes and Estimated Costs',
 'The lanes out of Hartford we book most, north, south, and west, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. Plan on about 10 to 25 percent more for an SUV or pickup, and more for enclosed. The snow, the season, and the carriers free on your dates set the final price.',
 prose(
  P('Hartford prices well for an inland city. The two interstates cross here, and the Boston trucks pass through. Boston and Albany ride 84 and 90. New Haven and Springfield ride 91, and Manhattan rides 91 to 95.'),
  P('The Florida lane fills from October into December. The Carolinas lane fills with insurance transfers all year. The <a href="car-shipping-cost.html">cost guide</a> covers the rest of the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Insurers, the Engine Plant, the Hospitals, and the Universities',
 prose(
  L('Hartford relocates people on the start date, the program schedule, the residency match, and the semester.'),
  P('The insurers in Asylum Hill and downtown relocate staff from every state on start dates. The health-insurance headquarters in Bloomfield does the same. The engine plant in East Hartford and the aerospace plants in Windsor Locks move engineers on program schedules. The records an employer needs for reimbursement come from us.'),
  P('The two hospitals in the city and the medical center in Farmington bring in residents every late June. Most arrive from out of state with a car. The handoff happens on Seymour Street, on Farmington Avenue, or at a lot off 84. The hospital garage is out.'),
  P('The state university in Storrs sits thirty miles east. Its downtown campus sits a block from our office. The college on the hill in the South End brings cars in each August too. So does the state university in New Britain. The campus lots work for the handoff, and an adult signs for a student car.'),
  P('State government hires on the fiscal year in July and relocates staff on the session calendar. The airport in Windsor Locks and the warehouses around it hire on start dates all year. Many of those employers allow a handoff at the dock.'),
  P('The Air National Guard wing at the airport rotates airmen on a smaller scale. The submarine base sits an hour southeast. The <a href="military-car-shipping.html">military</a> page covers a PCS move, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of any relocation.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Snow, Ice, the River, the Marathon, and the Golf Tournament',
 prose(
  L('Hartford gets more winter than the shoreline and less wind off the water. The river adds a season of its own.'),
  P('Hartford gets about forty-five inches of snow a year. Nor’easters close 84 and 91 for a morning a few times each winter. Ice storms are worse than snow for a trailer. The carriers wait for the plows and the sand, and a winter pickup can slide a day.'),
  P('The river rises with the spring melt and after a tropical storm. The dikes protect downtown. Riverside Park, the East Hartford flats, and the low roads along the river go under. A pickup there moves to Brainard Road until the water falls.'),
  P('The marathon closes downtown on a Saturday in October. The golf tournament fills Route 9 and 91 around Cromwell for a week each June. The big fair in West Springfield fills 91 for two weeks each September. We move a pickup near any of them to another day.'),
  P('Summer heat runs into the nineties, and the loading hour moves earlier in July and August. Ballpark and arena nights bring traffic to downtown. The 84 viaduct backs up in both rushes.'),
 )+chips(["Downtown","Asylum Hill","West End","Frog Hollow","Parkville","South End","Barry Square","Behind the Rocks","Blue Hills","Upper Albany","Sheldon Charter Oak","West Hartford","Elmwood","Wethersfield","Newington","Glastonbury","East Hartford","Manchester","Farmington","Bloomfield","Windsor","Windsor Locks","Avon","Simsbury","New Britain","Middletown"])
 +NOTE('Serving Hartford and the whole capital region. Tell us the neighborhood, the garage, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Hartford?',
 prose(
  L('Open trailers carry most of what leaves Hartford, and the two interstates are priced for them.'),
  P('An enclosed trailer keeps the salt, the sand, and attention off the car. The garages in West Hartford, Avon, and Glastonbury book enclosed trailers. So does a collector car headed to the shows in Florida each winter.'),
  P('A commuter car rides open and arrives the way it left, salt included. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at a lot off 84 or 91, and a delivery. The snow decides the day from December on.'),
  P('Accept the price, and a carrier already crossing Hartford on 84 or 91 takes the booking. We settle the spot the same day. You and the driver inspect the car together, and the Bill of Lading records what you see. Both sign, and the same sheet is used at delivery.'),
 )+ULI([
  "Take your things out of the car",
  "Leave the fuel at roughly a quarter",
  "Photograph the car before pickup, especially after a salt or sand storm",
  "A working key goes to the driver, along with a note on any mechanical issue",
  "Aftermarket alarms off, please",
  "In a downtown tower, ask the garage to stage the car an hour ahead",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages take it from there.'))))

BODY.append(sec('Why Ship Guy','Why Hartford Drivers Choose Ship Guy',
 prose(
  L('We work 84 and 91 every day and plan around the snow, the river, and the start dates.'),
  P('Our FMCSA brokerage license is active, and the $75,000 surety bond behind it is on file. Both are public record. Our office is on Church Street downtown.'),
  P('The same coordinator handles your quote, your booking, and your delivery. Open, enclosed, and expedited transport are all here, and the <a href="services.html">services</a> page covers each one.'),
 ), alt=True))

BODY.append(office('Hartford','20 Church St Ste 547','Hartford, CT 06103','+18605909072','(860) 590-9072','ET',
 '20+Church+St+Ste+547,+Hartford,+CT+06103','Visit Us','Find Ship Guy in Hartford',
 'Our office is on Church Street downtown, a block from Main Street.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4576.013643727772!2d-72.67360599999999!3d41.768724000000006!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e6531ccd703c5b%3A0xcbc976c04b98ec47!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792153188255!5m2!1sen!2sus'))

FAQ=[
 ("Do you handle relocations to the insurers or the engine plant?","Yes, on start dates and program schedules all year. The insurers downtown and in Asylum Hill relocate staff from every state. The engine plant in East Hartford moves engineers the same way. Most ship a car rather than drive it. We provide the records a reimbursed move needs."),
 ("How much does it cost to ship a car from Hartford to Boston or Florida?","Boston runs one hundred eighty to two hundred ninety dollars for a sedan. That is about one hundred miles on 84 and the Pike. Orlando runs eight hundred to eleven hundred thirty, about eleven hundred eighty miles down 91 and 95. Fall southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Can the carrier come to my house in the West End or the South End?","Usually not. The West End streets are narrow under old trees. The South End blocks are parked on both curbs. The driver meets you on Farmington Avenue, on Franklin Avenue, or at a lot off 84. West Hartford, Wethersfield, and Glastonbury usually allow the curb."),
 ("Do you ship cars for residents at Hartford Hospital or UConn Health?","Yes, every late June. Residents arrive from every state, and most bring a car. The handoff happens on Seymour Street or Farmington Avenue, not in a hospital garage. We plan the pickup around the report date."),
 ("What happens if a nor’easter or an ice storm hits on my pickup day?","The driver waits for the plows and the sand trucks before running 84 or 91. Ice is worse than snow for a loaded trailer. A winter pickup can slide a day, and the handoff moves to a plowed lot. We call when the forecast changes the plan."),
 ("Can you ship a car for a UConn, Trinity, or CCSU student?","Yes. The cars come in each August and leave each May. Storrs is rural, so the driver meets you on Route 195 or in the town center. Trinity and the New Britain campus use their lots. An adult signs for the car at pickup."),
 ("Is Hartford priced like New Haven or like Boston?","Closer to New Haven. Two interstates cross here, and the Boston trucks pass through on 84. A Hartford car rides a truck already making the trip. New Haven runs one hundred twenty to two hundred dollars for a sedan. Boston runs one hundred eighty to two hundred ninety."),
 ("What happens if the river floods on my pickup day?","The pickup moves to higher ground. Riverside Park, the East Hartford flats, and the low roads along the river go under. A spring melt or a tropical storm does it. The handoff moves to Brainard Road or a lot off 84 until the water falls."),
 ("Can you ship a car that does not run from Hartford?","Yes. We line up a winch carrier, and the slower loading is in the quote. Pick a flat, open spot, which in Hartford means a lot on Brainard Road. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Hartford car shipping quote?","Pickup and delivery addresses, with the neighborhood and the garage here. Year, make, and model. Does it run. Open or enclosed. Your dates, with the start date or the snow in mind. That is all a Hartford quote takes."),
]
BODY.append(faq_section(FAQ,'Hartford FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Hartford?','Two minutes on the form above produces a price. Tell us the neighborhood and your dates, and a carrier already crossing Hartford takes it from there.','+18605909072','(860) 590-9072','Get your free Hartford quote'))

build({
 'slug':'auto-transport-hartford-connecticut',
 'title':'Car Shipping in Hartford, CT — Auto Transport | Ship Guy',
 'meta':'Car shipping in Hartford, CT where Interstate 84 crosses 91. Insurance and Pratt & Whitney relocations, hospital residents, UConn and Trinity students, downtown garage handoffs, West End and South End meeting spots, West Hartford curbside, snow, ice, and river-flood planning. Local office on Church Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Hartford, <span class="accent">Connecticut</span>',
 'lede':'Open, enclosed, and expedited auto transport across the capital region, planned around 84, 91, the snow, and the river.',
 'tel':'+18605909072','disp':'(860) 590-9072','brand':'Hartford','keyword':'car shipping in hartford',
 'localterms':['hartford','interstate 84','interstate 91','route 2','route 9','route 15','charter oak bridge','bulkeley bridge','viaduct','berlin turnpike','brainard road','trumbull street','sisson avenue','flatbush avenue','farmington avenue','franklin avenue','seymour street','church street','main street','downtown','asylum hill','west end','frog hollow','parkville','south end','barry square','behind the rocks','blue hills','upper albany','west hartford','elmwood','wethersfield','newington','glastonbury','east hartford','manchester','farmington','bloomfield','windsor','windsor locks','avon','simsbury','new britain','middletown','storrs','buckland hills','corbins corner','insurers','engine plant','aerospace','health-insurance','hospitals','residents','medical center','university','college','state government','airport','warehouses','air national guard','submarine base','snow','ice','river','dikes','marathon','golf tournament','fair','ballpark','arena','new haven','springfield','providence','boston','albany','manhattan','philadelphia','washington','charlotte','orlando','florida','carolinas'],
}, BODY, FAQ)
