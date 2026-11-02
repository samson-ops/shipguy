import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Greensboro, North Carolina','Car shipping in the Gate City, where 40 and 85 cross in the middle of the Piedmont',
 ['Car shipping in Greensboro runs on Interstate 40, Interstate 85, and the loop that closed around the city. Ship Guy is a licensed auto transport broker with an office on West Lewis Street downtown.',
  'We book vetted carriers across Greensboro and the Triad, from Fisher Park to High Point and Burlington. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 40 crosses the city from Winston-Salem to Burlington and Raleigh. Interstate 85 rides the southern loop between Charlotte and Durham. Interstate 73 runs the west side past the airport. Interstate 840 closes the loop around the north and east. US 29, 220, and 421 fan out to Danville, Asheboro, and Sanford.',
  'This page covers 40, 85, the loop, the airport, Wendover, the old neighborhoods, and the Triad towns. It also covers the universities, the hospital, the cargo hub, the furniture market, the ice, and the lanes.'],
 'Greensboro at a glance',
 ['Most pickups happen within 1 to 3 days. The 85 carriers pass between Charlotte and Richmond every day. The 40 carriers cross from Tennessee to the coast.',
  'Raleigh, Charlotte, Richmond, and Columbia are same-day runs. Washington, Atlanta, Nashville, and Philadelphia need a day. Orlando and New York need one to two, and Chicago needs two.'],
 'Tell us the neighborhood and whether the street has overhead oaks. Fisher Park, Irving Park, College Hill, and downtown meet the truck at a lot. Adams Farm, Lake Jeanette, Summerfield, Jamestown, and Burlington usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 40, Interstate 85, the Urban Loop, Interstate 73, US 29, US 220, US 421, Wendover, Battleground, and Gate City Boulevard',
 prose(
  L('Greensboro is a crossroads first and a city second. Two interstates and a full loop put a carrier within ten minutes of every neighborhood.'),
  P('Interstate 40 comes in from Winston-Salem past the airport and runs along the south side of town. It leaves east for Burlington, Durham, and Raleigh. The stretch between the 73 interchange and Wendover backs up both rush hours. Interstate 85 arrived from Charlotte and once shared that road. It now rides the southern loop and leaves northeast for Durham and Richmond. The Charlotte carriers and the Richmond carriers pass on it every day.'),
  P('The Urban Loop closed in 2023 after decades of building. Interstate 73 carries the west side from the airport down to the 85 interchange and on toward Asheboro. Interstate 840 carries the north and the east. It runs from Bryan Boulevard around Lake Jeanette to the 85 interchange by McLeansville. US 29 leaves north for Reidsville and Danville, and US 421 leaves south for Sanford. US 220 is Battleground Avenue north of town and rides 73 south of it.'),
  P('Wendover Avenue is the commercial spine, from the airport side past the Friendly Center to the east side. Gate City Boulevard runs from downtown past the Coliseum to Jamestown. The carriers come off 40 at Wendover or Gate City. The Coliseum lots, the Friendly Center lots, and the big-box lots on Wendover are the usual meeting spots. The depot lots downtown work on a weekday.'),
  P('Our office is on West Lewis Street at the south end of downtown, a block off South Elm.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Fisher Park, Irving Park, Sunset Hills, Lindley Park, College Hill, Glenwood, the East Side, the Northwest, and the Triad Towns',
 prose(
  L('Greensboro is old oaks over narrow streets inside the loop and wide subdivisions outside it. The truck meets the old city at the edge.'),
  P('Downtown runs along Elm Street from the Depot at the south end to Fisher Park at the north. The blocks are short, the streets are one-way, and the curb is metered. The driver meets you at the depot lots or on Gate City Boulevard. South End around our office is old warehouses turned breweries and lofts. The handoff happens on the same lots.'),
  P('Fisher Park and Irving Park are the old money blocks, winding lanes under hundred-year-old oaks. A trailer cannot clear the limbs. The driver meets you on Battleground or at the Friendly Center. Sunset Hills, Lindley Park, and Westerwood west of downtown are the same, bungalows on tree-lined streets. The handoff moves to Market Street or Friendly Avenue.'),
  P('College Hill and Glenwood sit between the campuses, student houses on tight blocks. Move-in week fills every curb. The handoff moves to the UNCG lots or Gate City Boulevard. The East Side from Dudley Heights to Rankin and Bessemer is older grids with wider streets. The curb usually works. The campus blocks around A&T meet the truck on East Market or at the stadium lots.'),
  P('The northwest is wide. Starmount Forest, Hamilton Lakes, Lake Jeanette, Adams Farm, and the Guilford College blocks are postwar and newer. The driver reaches the house. Summerfield, Oak Ridge, and Stokesdale up Battleground are horse farms and cul-de-sacs with the same answer. Jamestown and High Point down Gate City ship with the same trucks. So do Burlington and Elon to the east and Kernersville and Winston-Salem to the west. All of them price the same as Greensboro.'),
 )))

ROUTES=[("Raleigh, NC","I-40 · ~80 mi","Same day","$140–$230"),("Charlotte, NC","I-85 · ~95 mi","Same day","$150–$240"),
 ("Columbia, SC","I-85/I-77 · ~190 mi","Same day","$220–$340"),("Richmond, VA","I-85/I-95 · ~200 mi","Same day","$230–$350"),
 ("Washington, DC","I-85/I-95 · ~320 mi","1 day","$290–$420"),("Atlanta, GA","I-85 · ~330 mi","1 day","$310–$450"),
 ("Nashville, TN","I-40 · ~470 mi","1 day","$400–$570"),("New York, NY","I-85/I-95 · ~520 mi","1–2 days","$440–$630"),
 ("Orlando, FL","I-77/I-95 · ~590 mi","1–2 days","$460–$660"),("Chicago, IL","I-77/I-64/I-65 · ~770 mi","2 days","$550–$800")]
BODY.append(rate_table('Lanes &amp; Costs','Greensboro Car Shipping Lanes and Estimated Costs',
 'The lanes Triad cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Greensboro for a sedan that runs, on an open trailer. An SUV or a pickup adds about 10 to 25 percent, and enclosed adds more. The week you pick and the carriers free that week set the final number.',
 prose(
  P('Greensboro prices among the best in the Carolinas. Every carrier on the 85 lane passes the city, and the 40 carriers cross it. Raleigh and Charlotte are short hops and cost the least. The Florida lane rides 85 to Charlotte and 77 to 95, and it fills each fall with retirees. The New York lane rides 85 and 95 north.'),
  P('Move-in week and the two market weeks are the busiest days of the year. The <a href="car-shipping-cost.html">cost guide</a> explains how size, condition, and timing move the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Universities, the Hospital, the Cargo Hub, the Truck Makers, the Furniture Trade, and the Retirees',
 prose(
  L('Greensboro relocates professors, nurses, pilots, engineers, and buyers. The universities and the hospital move the most.'),
  P('Five campuses sit inside the city. The state university on Spring Garden takes cars each August. So does the largest historically Black university in the country on East Market. The three colleges do the same, and all of them send the cars home in May. A parent books it, and an adult over eighteen signs at the lot. Campus streets are jammed that week, so the meeting point is a campus lot or Gate City Boulevard.'),
  P('The hospital system on North Elm is the largest private employer in the city. It hires traveling nurses year round and brings residents each June. The cargo hub at the airport sorts packages all night and moves managers on transfer dates. The jet maker beside it and the supersonic plant across the runway move engineers on project dates. If an employer is reimbursing the move, we supply the paperwork it needs.'),
  P('The truck maker headquartered on the west side relocates engineers and executives every month. The insurer downtown, the apparel brands, the chemical company, and the chip maker do the same. The battery plant in Liberty, half an hour south on 421, moves technicians on hiring waves. The second car usually rides a trailer. The furniture trade in High Point moves buyers and designers in on market dates.'),
  P('Retirees leave for Florida each fall and come back in April. Fort Liberty sits two hours down 421, and its families buy in the Triad on orders. Ship Guy is a private broker with no connection to the post. The timing around orders is on the <a href="military-car-shipping.html">military</a> page. The interstate paperwork is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Furniture Market, Move-In Week, the Tournament, the Golf Week, Homecoming, the Ice Storms, and the Tornado',
 prose(
  L('Greensboro runs on a market calendar and a campus calendar. The weather problem is ice, not snow.'),
  P('The High Point furniture market fills every hotel in the Triad for a week in April and October. Seventy-five thousand buyers come. Gate City Boulevard and the 40 interchanges crawl. A handoff in Jamestown or High Point moves to the week after. Move-in week in mid-August fills College Hill and the blocks around A&T. Homecoming at A&T in late October fills East Market and the stadium lots for four days.'),
  P('The Coliseum on Gate City hosts the conference basketball tournament in the years it comes. The lots fill for a week in March. The golf tournament at Sedgefield fills the west side for a week in early August. The folk festival closes downtown for a weekend in September, and the Fourth closes it for a day. A handoff near any of them moves to the next morning.'),
  P('Winter brings a few inches of snow and one or two ice storms. The December 2002 storm put an inch of ice on the oaks and cut power for a week. Limbs came down on every street inside the loop. A carrier waits in Charlotte or Burlington until the roads clear, usually a day. A winter pickup can lose that day, and you hear it from us first.'),
  P('Spring brings the yellow pollen and the tornado season. The April 2018 tornado cut across the east side and shut three schools for the year. The remnants of a hurricane cross the Piedmont every few years. Michael in October 2018 dropped trees and lines across the Triad for two days. A pickup in a tornado warning or a tropical storm waits for the all-clear. Summer brings heat and afternoon thunderstorms that shift the loading hour.'),
 )+chips(["Downtown","South End","Elm Street","Depot","Fisher Park","Irving Park","Sunset Hills","Lindley Park","Westerwood","College Hill","Glenwood","Southside","Ole Asheboro","Dudley Heights","Rankin","Bessemer","Starmount Forest","Hamilton Lakes","Friendly Center","Lake Jeanette","Adams Farm","Sedgefield","Guilford College","Pleasant Garden","Summerfield","Oak Ridge","Stokesdale","Jamestown","High Point","Kernersville","Winston-Salem","Burlington","Elon","McLeansville","Whitsett"])
 +NOTE('Serving Greensboro and the whole Triad, Fisher Park lane or Adams Farm cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Greensboro?',
 prose(
  L('Nearly every Triad car rides an open trailer, and the lane table above is priced that way.'),
  P('An enclosed trailer keeps off the pollen, the limbs, and the brine sprayed before an ice storm. The collectors in Irving Park and the executives relocating a new car to the headquarters book one. A car headed to Florida ahead of the first freeze often rides enclosed too.'),
  P('A daily driver or a student car belongs on the open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages show where the line falls.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot on Gate City or at the Friendly Center, and a signature at delivery. The move-in date or the market week picks the day.'),
  P('Approve the price, and a carrier already running 85 or 40 through the city gets the job. We confirm the lot and the window before the day ends. At pickup the driver records the car’s condition on the Bill of Lading, and you initial it. At delivery the car is compared to that record.'),
 )+ULI([
  "Anything personal out of the car, including the trunk",
  "About a quarter tank of gas",
  "Photos of every side and the odometer, taken that morning",
  "One working key, and a note about anything that sticks or leaks",
  "Any add-on alarm turned off",
  "In Fisher Park, Irving Park, or College Hill, plan on a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page has the order of events. The <a href="car-shipping-preparation.html">preparation</a> page has the full checklist.'))))

BODY.append(sec('Why Ship Guy','Why Greensboro Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 85 and 40 through the city every day. We know which streets the oaks close.'),
  P('Anyone can pull our FMCSA license and our $75,000 bond from the federal register. The office is on West Lewis Street downtown.'),
  P('The coordinator who prices the move is the one who answers until the car is delivered. The <a href="services.html">services</a> page puts open, enclosed, and expedited side by side.'),
 )))

BODY.append(office('Greensboro','111 W Lewis St #745','Greensboro, NC 27406','+13365519433','(336) 551-9433','ET',
 '111+W+Lewis+St+%23745,+Greensboro,+NC+27406','Visit Us','Find Ship Guy in Greensboro',
 'Our office is on West Lewis Street at the south end of downtown, a block off South Elm.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4925.882331687509!2d-79.79139610000001!3d36.065930200000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x885319630b7e8455%3A0xfb213f24516775e0!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793293302698!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Greensboro to Florida or New York?","Orlando runs four hundred sixty to six hundred sixty dollars for a sedan. That is about five hundred ninety miles down 85, 77, and 95. New York runs four hundred forty to six hundred thirty, about five hundred twenty miles north. Raleigh and Charlotte are short hops and cost the least. Figure 10 to 25 percent more for an SUV or a pickup."),
 ("Can the carrier come to my street in Fisher Park or Irving Park?","No. Both are winding lanes under old oaks, and a trailer cannot clear the limbs. The driver meets you on Battleground, at the Friendly Center, or at the depot lots downtown. Adams Farm, Lake Jeanette, Summerfield, Jamestown, and Burlington usually allow the curb."),
 ("Why are Greensboro pickups quick to schedule?","Because two interstates and a full loop cross here. The Charlotte and Richmond carriers pass on 85 every day. The Tennessee and coast carriers cross on 40. A car anywhere inside the loop is ten minutes from a truck already going your way. Most pickups schedule in 1 to 3 days."),
 ("Do you ship cars for the hospital and the airport employers?","Yes, every week. The hospital system brings residents each June and hires traveling nurses year round. The cargo hub moves managers on transfer dates. The jet maker and the supersonic plant move engineers on project dates. The second car usually rides a trailer. If an employer is reimbursing the move, we supply the paperwork."),
 ("Can you deliver on a UNCG or A&T move-in date?","Yes. The campuses take cars in mid-August and send them home in May. A parent books it, and an adult over eighteen signs at the lot. College Hill and East Market are jammed that week. The meeting point is a campus lot or Gate City Boulevard. The window follows the date."),
 ("Does the High Point furniture market affect my pickup?","Yes, in Jamestown and High Point. Seventy-five thousand buyers fill the Triad for a week in April and again in October. Gate City Boulevard and the 40 interchanges crawl. A handoff down there moves to the week after. Greensboro itself runs normally apart from the hotels."),
 ("Can you ship a car to or from High Point, Winston-Salem, or Burlington?","Yes, and all three price the same as Greensboro. High Point rides the same carriers off 85 and 74. Its old streets meet the truck on a main road. Winston-Salem rides them off 40 at Silas Creek Parkway. Burlington rides them off 40 at University Drive, and the curb works. Send the full address for a suburb."),
 ("What happens if an ice storm hits on my pickup day?","The carrier waits in Charlotte or Burlington until the roads clear. Ice brings the oaks down inside the loop. A side street can stay blocked for a day after the highway opens. The handoff moves to a cleared lot on Wendover or Gate City. You hear it from us before the driver does."),
 ("Can you ship a car that does not run from Greensboro?","Yes. A winch carrier takes it, and the loading time is priced from the start. The Coliseum lots or the big-box lots on Wendover give the driver level ground. Say whether it rolls, steers, and brakes."),
 ("What do you need for a Greensboro car shipping quote?","Both ends of the trip, with the neighborhood or the Triad town. The year, make, and model. Whether it runs. Open or enclosed. The week you have in mind. With those five, a Greensboro number is back the same day."),
]
BODY.append(faq_section(FAQ,'Greensboro FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Greensboro?','Two minutes on the form above and your lane has a Greensboro number. Give us the neighborhood and the week, and a carrier already on 85 or 40 takes it.','+13365519433','(336) 551-9433','Get your free Greensboro quote'))

build({
 'slug':'auto-transport-greensboro-north-carolina',
 'title':'Car Shipping in Greensboro, NC — Auto Transport | Ship Guy',
 'meta':'Car shipping in Greensboro, NC, the Gate City where Interstate 40 and 85 cross and the Urban Loop closes the ring. University move-in timing, hospital and airport relocations, the furniture market weeks, lot handoffs for Fisher Park and Irving Park, curbside pickups in Adams Farm, Lake Jeanette, Summerfield, and Burlington, the ice storms, and the tornado season. Local office on West Lewis Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Greensboro, <span class="accent">North Carolina</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Triad, planned around 40, 85, the loop, the campus calendar, the market weeks, and the ice.',
 'tel':'+13365519433','disp':'(336) 551-9433','brand':'Greensboro','keyword':'car shipping in greensboro',
 'localterms':['greensboro','gate city','interstate 40','interstate 85','loop','west lewis street','downtown','triad','fisher park','high point','burlington','winston-salem','raleigh','charlotte','durham','interstate 73','airport','interstate 840','us 29','us 220','us 421','danville','asheboro','sanford','wendover','universities','hospital','cargo hub','furniture market','ice storms','richmond','columbia','washington','atlanta','nashville','philadelphia','orlando','new york','chicago','oaks','irving park','college hill','adams farm','lake jeanette','summerfield','jamestown','rush hours','reidsville','battleground','friendly center','coliseum','depot','elm street','south end','breweries','lofts','sunset hills','lindley park','westerwood','market street','friendly avenue','glenwood','dudley heights','rankin','bessemer','east market','stadium','starmount forest','hamilton lakes','guilford college','oak ridge','stokesdale','elon','kernersville','retirees','spring garden','historically black','traveling nurses','residents','transfer dates','jet maker','supersonic','truck maker','insurer','apparel','chemical','chip maker','battery plant','liberty','buyers','fort liberty','seventy-five thousand','homecoming','tournament','sedgefield','folk festival','december 2002','an inch of ice','pollen','april 2018','michael','thunderstorms','brine','bill of lading','fmcsa','southside','ole asheboro','sedgefield','pleasant garden','mcleansville','whitsett','silas creek parkway','university drive','winch','urban loop'],
}, BODY, FAQ)
