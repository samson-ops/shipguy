import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Worcester, Massachusetts','Car shipping in the second city of New England, on seven hills an hour west of Boston',
 ['Car shipping in Worcester is a question of hills, snow, and which of nine colleges is moving in. Ship Guy is a licensed auto transport broker with an office on Main Street downtown.',
  'We book vetted carriers across central Massachusetts, from Shrewsbury and Auburn to Leominster and Westborough. We do not own the trucks.',
  'Interstate 290 runs through the city from the Mass Pike at Auburn to Interstate 495 at Marlborough. Interstate 190 runs north to Leominster. Route 146 runs south to Providence, and Route 9 runs east to Boston.',
  'This page covers the Pike and the expressway, the hills and the neighborhoods, and the suburbs. It also covers the medical school, the colleges, the ballpark, the snow, and the lanes.'],
 'Worcester at a glance',
 ['Most pickups happen within 1 to 3 days. The Pike carries the Boston-to-Albany carriers past the south side of the city all day.',
  'Boston, Providence, Hartford, and Springfield are same-day lanes. Albany and Manhattan are the same day too. Philadelphia and Washington take a day. Florida runs three.'],
 'Tell us the neighborhood. The hill streets, Main South, and the Canal District need a meeting spot. The West Side, Burncoat, and the suburbs often allow the curb.'))

BODY.append(sec('The Roads','Interstate 290, 190, the Pike, Route 146, and Kelley Square',
 prose(
  L('Worcester sits a few miles north of the Pike, and the expressway is the ramp that connects them.'),
  P('The Mass Pike passes the south side of the city at Auburn and Millbury. The toll is collected by transponder, and a carrier builds it into the quote. Interstate 290 leaves the Pike at Auburn and runs through downtown to Shrewsbury and Marlborough.'),
  P('Interstate 190 leaves 290 north of downtown for Leominster and Fitchburg. Route 146 runs south from Kelley Square to Providence. Route 9 runs east through Shrewsbury to Boston and west to Leicester. Route 20 crosses the south side as the old road to the Pike.'),
  P('Kelley Square was the worst intersection in the state until it became a roundabout beside the ballpark. The carriers come off 290 at Grafton Street, Plantation Street, and Kelley Square. The lots along Shrewsbury Street and off Route 20 in Auburn are the usual meeting spots.'),
  P('Our office sits on Main Street downtown, two blocks from the Common.'),
 ), alt=True))

BODY.append(sec('The Seven Hills','Downtown, the Canal District, Main South, the West Side, and the Grids',
 prose(
  L('Worcester was built on seven hills, and the hills decide where a truck can stop.'),
  P('Downtown and the Canal District run on one-way streets around the Common and the ballpark. The driver meets you on Shrewsbury Street, on Southbridge Street, or at a lot off 290. On a game night the Canal District is out altogether.'),
  P('Main South, Vernon Hill, Grafton Hill, and Union Hill are steep grids of three-deckers. Cars park on both curbs. The streets ice first in winter. The driver meets you on Main Street, on Grafton Street, or at a lot on Park Avenue.'),
  P('The West Side is wider. Tatnuck, Newton Square, and the streets off Salisbury and Pleasant have driveways and room at the curb. Burncoat and Greendale on the north side are the same. Indian Lake and Lake Quinsigamond have narrow shoreline roads. The handoff happens on the main road above them.'),
  P('Shrewsbury, Auburn, Holden, and Westborough are suburban grids where the truck usually reaches the curb. The office parks along 290 and 495 have lots that work for a handoff. So do the warehouses in Auburn.'),
 )))

ROUTES=[("Boston, MA","I-90 · ~45 mi","Same day","$120–$200"),("Providence, RI","CA-146 · ~45 mi","Same day","$120–$200"),
 ("Hartford, CT","I-84 · ~65 mi","Same day","$150–$250"),("Springfield, MA","I-90 · ~55 mi","Same day","$130–$220"),
 ("Albany, NY","I-90 · ~120 mi","Same day","$190–$300"),("Manhattan, NY","I-84/I-95 · ~170 mi","Same day","$220–$340"),
 ("Philadelphia, PA","I-84/I-95 · ~260 mi","1 day","$260–$390"),("Washington, DC","I-84/I-95 · ~400 mi","1 day","$340–$490"),
 ("Charlotte, NC","I-95/I-85 · ~800 mi","2 days","$560–$810"),("Orlando, FL","I-95 · ~1,240 mi","3 days","$820–$1,160")]
ROUTES[1]=("Providence, RI","MA-146 · ~45 mi","Same day","$120–$200")
BODY.append(rate_table('Lanes &amp; Costs','Worcester Car Shipping Lanes and Estimated Costs',
 'The lanes out of Worcester we price most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer. Figure about 10 to 25 percent more for an SUV or pickup, and more again for enclosed. The Pike toll, the snow, and the carriers free on your dates set the final figure.',
 prose(
  P('Worcester prices like Boston with a few dollars off. The Pike carriers pass it without entering the city. Boston and Albany ride the Pike, Providence rides 146, and Hartford rides 84.'),
  P('The Florida lane fills from October into December, and the student lanes fill in September and May. The <a href="car-shipping-cost.html">cost guide</a> shows where the number comes from.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Medical School, Nine Colleges, the Hospitals, and the Biotech Park',
 prose(
  L('Worcester relocates people on the residency match, the semester, the grant cycle, and the Florida season.'),
  P('The medical school and its hospital are the largest employer in the city. They bring in residents every late June, and most arrive from out of state with a car. The handoff happens on Plantation Street or at a lot off 290 rather than in the hospital garage.'),
  P('Nine colleges move students in over Labor Day weekend and out again in May. The campus streets on the hills are tight on move-in day. The driver meets you at a lot nearby, and an adult signs for a student car. Two to three weeks of notice keeps the price steady in late August.'),
  P('The biotech park, the insurer downtown, and the plants in the south end relocate staff on start dates. The abrasives plant and the pharmaceutical plant move engineers on program schedules. When an employer reimburses the move, the records come from us.'),
  P('Thousands of residents ride the commuter rail to Boston every morning. Families move out from the city for the housing all year. The second car usually rides a truck.'),
  P('Retirees leave for Florida and the Carolinas each fall, and the <a href="snowbird-car-shipping.html">snowbird</a> page covers the timing. The reserve base in Chicopee is an hour west, and the <a href="military-car-shipping.html">military</a> page covers a PCS move. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Snow, the Ice Storm, Game Nights, and Move-In Weekend',
 prose(
  L('Worcester gets more snow than any big city on the East Coast. The hills make every inch count.'),
  P('Worcester gets about sixty-five inches of snow a year, two feet more than Boston. Nor’easters close 290 and the Pike for a morning a few times each winter. The hill streets ice first and clear last. The carriers wait for the plows, and a winter pickup can slide a day.'),
  P('The December 2008 ice storm took the county down for a week. Ice is still the risk the carriers respect most. A snow emergency clears the parked cars off the main roads. The handoff moves to a plowed lot.'),
  P('Ballgames fill the Canal District and Kelley Square from April through September. Move-in weekend fills the hills around the colleges over Labor Day. The street festival closes Park Avenue for a day in September. We move a pickup near any of them to another day.'),
  P('Summer heat moves the loading hour earlier, and thunderstorms with hail roll through in July. Interstate 290 backs up from six to ten and from three to seven. A Worcester pickup happens between the rushes.'),
 )+chips(["Downtown","Canal District","Shrewsbury Street","Main South","Vernon Hill","Grafton Hill","Union Hill","Elm Park","West Side","Tatnuck","Newton Square","Salisbury Street","Burncoat","Greendale","Indian Lake","Lake Quinsigamond","Webster Square","Quinsigamond Village","Kelley Square","Shrewsbury","Auburn","Holden","Westborough","Millbury","Leicester","Grafton"])
 +NOTE('Serving Worcester and all of central Massachusetts. Tell us the hill, the street, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Worcester?',
 prose(
  L('Open trailers carry most of what leaves Worcester, and the Pike lanes are priced for them.'),
  P('An enclosed trailer keeps the road salt and the sand off the paint. It keeps the car out of sight too. The garages on Salisbury Street and in Holden book enclosed trailers. So does a collector car headed to Florida for the winter.'),
  P('A student car or a commuter car rides open and arrives the way it left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages show the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on a wide street or at a lot off 290, and a delivery. The snow sets the day in winter.'),
  P('Accept the price, and a carrier already on the Pike takes the booking. We set the spot the same day. The driver and you look over the car and note its condition on a Bill of Lading. Both sign, and delivery is checked against it.'),
 )+ULI([
  "Bring your belongings in from the car",
  "Leave the fuel around a quarter tank",
  "Photograph the car before pickup, salt and sand included",
  "Give the driver a working key and mention anything mechanical",
  "Turn any aftermarket alarm off",
  "On a hill street, plan to meet the truck on the main road below",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages have the rest.'))))

BODY.append(sec('Why Ship Guy','Why Worcester Drivers Choose Ship Guy',
 prose(
  L('We work the Pike and 290 every day and plan around the hills, the snow, and the colleges.'),
  P('Ship Guy’s brokerage license is current with the FMCSA. The $75,000 surety bond behind it is on file. Both are public. Our office is on Main Street downtown.'),
  P('Your coordinator stays with the booking from the quote to the last signature. Open, enclosed, and expedited transport are all on the table here, and the <a href="services.html">services</a> page describes them.'),
 ), alt=True))

BODY.append(office('Worcester','446 Main St #321','Worcester, MA 01608','+15082906094','(508) 290-6094','ET',
 '446+Main+St+%23321,+Worcester,+MA+01608','Visit Us','Find Ship Guy in Worcester',
 'Our office is on Main Street downtown, two blocks from the Common and minutes from Interstate 290.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4540.563871750182!2d-71.8034784!3d42.2633192!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e407f7a9252f0f%3A0xc2bf215a83396288!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792153719044!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come to my street in Worcester?","On the West Side, in Burncoat, and in the suburbs, usually. On the hill streets, in Main South, and in the Canal District, the streets are too tight. The driver meets you on Main Street, on Shrewsbury Street, or at a lot off 290. It is a few minutes from the house."),
 ("How much does it cost to ship a car from Worcester to Boston or Florida?","Boston runs one hundred twenty to two hundred dollars for a sedan, about forty-five miles down the Pike. Orlando runs eight hundred twenty to eleven hundred sixty, about twelve hundred forty miles down 84 and 95. Fall southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Can you ship a car for a Worcester college student?","Yes, every September and May. The colleges move in over Labor Day weekend, and the hill streets around them are tight that day. The driver meets you at a lot nearby. An adult signs at pickup, and a parent can take the far end."),
 ("Do you ship cars for residents at the medical school?","Yes, every late June. Residents arrive from every state, and most bring a car. The handoff happens on Plantation Street or at a lot off 290, not in the hospital garage. The pickup is timed to the report date."),
 ("What happens when a snowstorm hits Worcester on my pickup day?","The carriers sit until the plows and the sanders finish. Worcester gets two feet more snow than Boston, and the hills ice first. A winter pickup can lose a day. The handoff moves to a plowed lot, and you hear from us as the forecast changes."),
 ("Is the Pike toll added to my price?","It is built in. Carriers pay the Pike by transponder and price the trip with the toll inside. There is no separate line. Interstate 290, 190, and Route 146 carry no toll."),
 ("Does a ballgame or move-in weekend affect my pickup?","Near the ballpark and the colleges, yes. Game nights fill the Canal District and Kelley Square from April through September. Labor Day weekend fills the hills around the campuses. We move a pickup near either to another day, and the rest of the city runs normally."),
 ("Is Worcester priced like Boston?","Close to it, and a little under. The Pike carriers pass Worcester without entering Boston. A Worcester car rides a truck already making the trip. Providence and Hartford price the same way at one hundred twenty to two hundred fifty dollars."),
 ("Can you ship a car that does not run from Worcester?","Yes. We book a carrier with a winch, and the slower loading is in the quote. Pick a flat spot, which in Worcester means a lot off 290 rather than a hill street. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Worcester car shipping quote?","Both addresses, with the neighborhood and the hill on this end. The year, make, and model, and whether it runs. Open or enclosed. Your dates, with move-in weekend or the snow in mind. That is a complete Worcester request."),
]
BODY.append(faq_section(FAQ,'Worcester FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Worcester?','Quote the trip on the form above, which takes about two minutes. Tell us the hill and your dates, and a carrier already on the Pike takes it from there.','+15082906094','(508) 290-6094','Get your free Worcester quote'))

build({
 'slug':'auto-transport-worcester-massachusetts',
 'title':'Car Shipping in Worcester, MA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Worcester, MA off the Mass Pike and Interstate 290. Hill-street meeting spots, West Side curbside, medical school residents, nine colleges and Labor Day move-in, the biotech park, Pike toll built in, sixty-five inches of snow planned for. Local office on Main Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Worcester, <span class="accent">Massachusetts</span>',
 'lede':'Open, enclosed, and expedited auto transport across central Massachusetts, planned around the Pike, the hills, and the snow.',
 'tel':'+15082906094','disp':'(508) 290-6094','brand':'Worcester','keyword':'car shipping in worcester',
 'localterms':['worcester','interstate 290','interstate 190','mass pike','interstate 495','route 146','route 9','route 20','kelley square','shrewsbury street','southbridge street','grafton street','plantation street','park avenue','main street','downtown','the common','canal district','ballpark','main south','vernon hill','grafton hill','union hill','three-deckers','west side','tatnuck','newton square','salisbury','burncoat','greendale','indian lake','lake quinsigamond','shrewsbury','auburn','holden','westborough','leominster','marlborough','medical school','hospital','residents','colleges','labor day','move-in','biotech park','insurer','abrasives','pharmaceutical','commuter rail','snowbird','reserve base','snow','ice storm','nor’easters','plows','snow emergency','boston','providence','hartford','springfield','albany','manhattan','philadelphia','washington','charlotte','orlando','florida'],
}, BODY, FAQ)
