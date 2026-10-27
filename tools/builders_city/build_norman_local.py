import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Norman, Oklahoma','Car shipping on the Sooner calendar, twenty miles down Interstate 35',
 ['Car shipping in Norman follows the university year and the football schedule. Ship Guy is a licensed auto transport broker with an office on East Main Street downtown.',
  'We book vetted carriers across Cleveland County, from Moore to Noble and out to Lake Thunderbird. We do not own the trucks.',
  'Interstate 35 runs along the west side of the city. Every carrier between Kansas City and Dallas uses it. Highway 9 crosses the south end, and Lindsey Street and Main Street connect the campus to the interstate.',
  'This page covers the interstate and the exits, the campus, the move-in weeks, and the fall Saturdays. It also covers the forecasters who study the storms, the neighborhoods, the Tinker commuters, and the lanes.'],
 'Norman at a glance',
 ['Most pickups happen within 1 to 3 days. The Interstate 35 lane brings carriers past the city all day.',
  'Oklahoma City is local. Dallas, Tulsa, Wichita, and Fort Worth are same-day lanes. Kansas City, Austin, and Little Rock take a day. Denver runs two.'],
 'Tell us the week. August move-in, May move-out, and seven home Saturdays each fall decide where the truck can meet you.'))

BODY.append(sec('The Interstate','Interstate 35, Highway 9, and the Exits',
 prose(
  L('Norman has one interstate, and the whole city schedules around the exits off it.'),
  P('Interstate 35 runs north to Oklahoma City, Wichita, and Kansas City. It runs south to Dallas and Austin. The Main Street, Lindsey Street, Robinson, and Tecumseh exits carry the city traffic. Carriers run this lane in both directions every day.'),
  P('Highway 9 runs east and west along the south end of the city. It passes the campus on its way from the interstate toward Lake Thunderbird and Tecumseh. Highway 77 is Classen Boulevard and Flood Avenue through the middle of town.'),
  P('The BNSF tracks run north and south along the west edge of downtown. The crossings back up when a train rolls through. The driver meets you on the side of the tracks you live on.'),
  P('Interstate 40 is twenty-five minutes north through Oklahoma City. The Turner Turnpike to Tulsa starts there too. Both lanes leave Norman on Interstate 35.'),
 ), alt=True))

BODY.append(sec('The Campus','Move-In, Move-Out, and the Fall Saturdays',
 prose(
  L('The University of Oklahoma brings tens of thousands of cars to Norman each August. It sends most of them home in May.'),
  P('Move-in week fills Lindsey Street, Jenkins Avenue, and the streets around Campus Corner. The driver meets you at a lot near the interstate instead of at the dorm. An adult signs for a student car. The same thing happens in reverse in May.'),
  P('Seven home football Saturdays each fall fill Interstate 35 for hours in both directions. Lindsey Street closes near the stadium, and the campus lots turn into tailgates. We schedule Norman pickups on another day.'),
  P('The conference move raised the game-day crowds. The hotels from Norman to Moore sell out on those weekends. A car arriving on a game Saturday waits until Sunday.'),
  P('Graduate students, faculty, and the research campus south of Lindsey arrive on their own calendar. Many of them ship from the coasts. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the longer move.'),
 )))

ROUTES=[("Tulsa, OK","I-35/Turner Tpk · ~125 mi","Same day","$180–$290"),("Fort Worth, TX","I-35 · ~175 mi","Same day","$210–$330"),
 ("Wichita, KS","I-35 · ~180 mi","Same day","$210–$320"),("Dallas, TX","I-35 · ~185 mi","Same day","$220–$340"),
 ("Amarillo, TX","I-40 · ~280 mi","1 day","$250–$380"),("Little Rock, AR","I-40 · ~360 mi","1 day","$320–$460"),
 ("Austin, TX","I-35 · ~370 mi","1 day","$320–$470"),("Kansas City, MO","I-35 · ~370 mi","1 day","$320–$470"),
 ("Houston, TX","I-35/I-45 · ~430 mi","1 day","$370–$530"),("Denver, CO","I-40/US-287 · ~700 mi","2 days","$520–$740")]
BODY.append(rate_table('Lanes &amp; Costs','Norman Car Shipping Lanes and Estimated Costs',
 'The lanes Norman students, families, and faculty ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups add roughly 10 to 25 percent, and enclosed adds more. Move-in week, game weekends, and carrier availability on your dates set the real quote.',
 prose(
  P('Dallas and Fort Worth are the busiest lanes out of Norman. Both sit three hours south on an interstate carriers never leave. Wichita and Tulsa run the same day in the other directions.'),
  P('Oklahoma City is a local trip rather than a lane. A car headed to Edmond or Tinker rides with a metro pickup. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Weather Center','Storm Season in the City That Forecasts It',
 prose(
  L('The federal storm forecasters work from Norman, and the storms they track come through town.'),
  P('The weather center on the research campus houses the forecasters who issue the severe-weather outlooks for the country. The worst stretch runs from April into June. Norman and Moore have both taken direct tornado hits in that window.'),
  P('A warning means the driver stops and waits for the all-clear. The pickup slides by a few hours or a day, and every spring booking carries room for that.'),
  P('Hailstones do more harm to a car sitting outside than the wind does. A collector car rides enclosed through the storm months for that reason. Ice closes Interstate 35 for a day a few winters out of ten.'),
  P('The heat in July and August sits past a hundred for weeks. A car coming in from the coast wants a fresh battery and a checked cooling system first.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Campus Corner, the Historic Blocks, East Norman, and Moore',
 prose(
  L('Norman is an easy grid outside the campus, and the campus is the part that needs planning.'),
  P('Campus Corner, the Greek houses, and the apartment blocks along Lindsey Street have narrow streets. Student parking fills both sides. The driver meets you at a lot on Lindsey or near the interstate.'),
  P('The historic blocks between downtown and the campus have low trees and alley garages. Downtown along Main Street runs on street parking and the Saturday market. The handoff happens on Porter Avenue, Flood, or a lot near the depot.'),
  P('West Norman along the interstate is wide and simple, and the truck reaches the curb. East Norman past Twelfth Avenue runs to acreages and gravel roads toward the lake. The trailer stays on the pavement out there.'),
  P('Moore, Noble, and the subdivisions along Highway 9 are open grids. Many of those households commute to Tinker, and the base handoff happens outside the gate.'),
  P('Our office is on East Main Street downtown, a few blocks from the depot and the campus.'),
 )+chips(["Downtown","Campus Corner","Lindsey Street","Greek Row","Historic Miller District","Porter Avenue","West Norman","University North Park","Hall Park","East Norman","Lake Thunderbird","Research Campus","Moore","Noble","Goldsby","Slaughterville","Little Axe","Newcastle","Blanchard","Purcell"])
 +NOTE('Serving Cleveland and McClain Counties. Tell us the week, the neighborhood, and whether the car runs.')))

BODY.append(sec('Who Moves Here','Tinker, the Hospital, the Plant, and the Weather Companies',
 prose(
  L('Norman ships on orders, on residency match days, and on the weather industry that grew up here.'),
  P('Tinker Air Force Base is twenty-five minutes northeast. Thousands of airmen and civilians live in Norman and Moore. Orders usually pay to move one vehicle, so the second car in the driveway comes to us. The <a href="military-car-shipping.html">military</a> page covers the planning.'),
  P('The regional hospital on Porter Avenue and its new campus by the interstate hire clinicians on start dates. The heating and cooling plant on the south side hires engineers on production cycles.'),
  P('The private weather companies and the federal labs recruit meteorologists from every coast. Most arrive with a car. If your employer reimburses the shipment, we send the documentation.'),
 ), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Norman?',
 prose(
  L('Open transport carries most of Norman, and the Interstate 35 lanes run on it.'),
  P('Enclosed transport keeps a car covered against hail, road grit, and the spring storms. A collector car or a new graduation gift usually rides enclosed through the storm months.'),
  P('A student car rides open without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out each option.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading near the interstate, and a delivery. The calendar decides the timing.'),
  P('Once you approve the price, a carrier already running Interstate 35 takes the booking. The driver writes up the car’s condition on a Bill of Lading at the lot. You sign it there. Check the car against that form when it arrives.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a hail storm",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "For the campus or Campus Corner, plan to meet the truck at a lot near Lindsey Street",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides take it step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Norman Drivers Choose Ship Guy',
 prose(
  L('We work the Interstate 35 lane every day and plan around move-in, the games, and the storms.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond stand behind every booking we make. Our office is on East Main Street.'),
  P('One coordinator carries your shipment from quote to delivery and can book open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows the full lineup.'),
 )))

BODY.append(office('Norman','104 E Main St Ste 498','Norman, OK 73069','+14058604763','(405) 860-4763','CT',
 '104+E+Main+St+Ste+498,+Norman,+OK+73069','Visit Us','Find Ship Guy in Norman',
 'Our office is on East Main Street downtown, a few blocks from the depot and the campus.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5513.01275711802!2d-97.4428987!3d35.2207751!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87b2690f44a2f823%3A0x55508e1364399f94!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792022819974!5m2!1sen!2sus'))

FAQ=[
 ("Can you ship a car for an OU student?","Yes, student cars arrive each August and leave each May. Move-in week fills Lindsey Street and Campus Corner. The driver meets you at a lot near the interstate. An adult signs for the car at pickup, and a parent can sign at the far end."),
 ("Does a home football game affect my pickup?","Yes, if it falls on a Saturday with a home game. Interstate 35 fills for hours, Lindsey Street closes near the stadium, and the lots become tailgates. We schedule Norman pickups on another day of that week."),
 ("How much does it cost to ship a car from Norman to Dallas?","A sedan usually runs two hundred twenty to three hundred forty dollars. That is about one hundred eighty-five miles down Interstate 35. Fort Worth runs about the same, and Austin runs three hundred twenty to four hundred seventy. Larger vehicles add 10 to 25 percent."),
 ("Do you ship to Oklahoma City or Edmond from Norman?","We do, but it is a local trip rather than a lane. A car headed across the metro rides with a pickup already scheduled nearby. Most Norman customers ship much farther, and the metro leg is usually a drive."),
 ("What happens if a tornado warning is issued during my pickup?","The driver stops and waits for the all-clear. The pickup can slide a few hours or a day. The worst stretch runs April into June. The forecasters who track it work right here on the research campus."),
 ("Can the carrier reach my house in Campus Corner or the historic blocks?","Usually not. The streets are narrow, the trees hang low, and student parking fills both sides. The driver meets you on Lindsey Street, Porter Avenue, or a lot near the depot. West Norman and Moore usually allow curbside."),
 ("Do you handle a PCS move to Tinker from Norman?","Yes. Many Tinker families live in Norman and Moore. Orders usually pay to move one vehicle, and the second one comes to us. The base is gated, so the meeting spot sits outside it. Ship Guy is a private broker with no connection to the base."),
 ("Can you pick up out by Lake Thunderbird or on an acreage?","Yes, on the paved road. East Norman runs to gravel roads past Twelfth Avenue, and a seventy-five-foot trailer stays on the pavement. We meet you at the nearest paved intersection or a lot on Highway 9."),
 ("Can you ship a car that does not run from Norman?","Yes. A winch-equipped carrier loads a car that will not start. The extra loading time is priced into the quote. Tell us whether it rolls, steers, and brakes, because that decides which truck we send."),
 ("What do you need for a Norman car shipping quote?","The pickup and delivery addresses, with the neighborhood. The year, make, and model. Whether it runs and rolls. Open or enclosed, and your dates, with the game schedule in mind. That is everything an accurate Norman quote needs."),
]
BODY.append(faq_section(FAQ,'Norman FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Norman?','The form above takes about two minutes. Tell us the week and the neighborhood. We will match you with a carrier already on Interstate 35.','+14058604763','(405) 860-4763','Get your free Norman quote'))

build({
 'slug':'auto-transport-norman-oklahoma',
 'title':'Car Shipping in Norman, OK — Auto Transport | Ship Guy',
 'meta':'Car shipping in Norman, OK on the Interstate 35 lane. OU move-in and move-out timing, game-day planning, Campus Corner handoffs, Tinker families, the weather center and storm season. Local office on East Main Street. Free quote.',
 'h1':'Car Shipping in<br>Norman, <span class="accent">Oklahoma</span>',
 'lede':'Open, enclosed, and expedited auto transport across Cleveland County, planned around the campus, the games, and the storms.',
 'tel':'+14058604763','disp':'(405) 860-4763','brand':'Norman','keyword':'car shipping in norman',
 'localterms':['norman','interstate 35','highway 9','lindsey street','main street','robinson','tecumseh','classen','flood','bnsf','depot','campus corner','greek','historic','porter avenue','west norman','east norman','twelfth avenue','lake thunderbird','research campus','moore','noble','goldsby','university of oklahoma','move-in','football','saturday','stadium','tailgate','weather center','forecasters','tornado','hail','ice','tinker','hospital','plant','weather companies','dallas','fort worth','wichita','tulsa','kansas city','austin','denver'],
}, BODY, FAQ)
