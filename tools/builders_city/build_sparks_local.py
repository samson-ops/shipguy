import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Sparks, Nevada','Car shipping in the rail city next to Reno, where the warehouses meet the pass and the California lane never stops',
 ['Car shipping in Sparks runs on Interstate 80, which crosses the city between the warehouses and the river. Ship Guy is a licensed auto transport broker with an office on Vista Boulevard by the Marina.',
  'We book vetted carriers across Sparks, from Victorian Square to Spanish Springs and out to the industrial center. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 80 runs east and west through the city with the Rock, Pyramid, Sparks, and Vista exits. Over the pass it reaches Sacramento in a hundred thirty miles. Interstate 580 and 395 run south through Reno to Carson City. Pyramid Way runs north to Spanish Springs, and McCarran Boulevard loops the two cities.',
  'This page covers 80, 580, Pyramid, McCarran, Vista, Victorian Square, the Marina, and Spanish Springs. It also covers the warehouses, the industrial center, the casinos, the car week, the pass, and the smoke.'],
 'Sparks at a glance',
 ['Most pickups happen within 1 to 3 days. The Sacramento and Bay Area carriers cross the pass daily. The 80 trucks between California and Salt Lake pass the city all day. The Reno pool stages along Greg Street.',
  'Sacramento and San Francisco ride a single day on the truck. Boise, Salt Lake, Los Angeles, and Las Vegas take a day. Portland and Seattle take one to two, and Phoenix and Denver take two.'],
 'Tell us the neighborhood. Victorian Square, the old grid, and the Spanish Springs horse properties meet the truck on a main road. The Vistas, Wingfield Springs, Kiley Ranch, and the subdivisions off Sparks Boulevard usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 80, Interstate 580, Pyramid Way, McCarran Boulevard, Sparks Boulevard, Vista Boulevard, Prater Way, and the Pass',
 prose(
  L('Sparks is a strip of city between the interstate and the hills. The pass to the west sets the calendar. A carrier picks its exit and never crosses the rail yard.'),
  P('Interstate 80 runs through the middle of the city. The Rock Boulevard and Pyramid Way exits serve the old town. Sparks Boulevard serves the middle, and Vista Boulevard serves the east side and the Marina. East of the city it runs through Fernley to the industrial center and the Utah line. West it runs through Reno and climbs Donner Pass to Truckee and Sacramento. The pass closes a few times each winter, and the chain controls slow every trailer on it.'),
  P('Interstate 580 is 395, the road south through Reno to Carson City and north to Susanville. Pyramid Way is Route 445, north through the city to Spanish Springs and the lake. McCarran Boulevard loops both cities and carries the Reno pool from one side to the other. Sparks Boulevard and Vista Boulevard run north from the interstate to the newer subdivisions. Prater Way and Victorian Avenue are the old main streets through downtown. Greg Street and Glendale Avenue run the warehouse belt along the tracks.'),
  P('The carriers come off 80 at Sparks Boulevard or Vista. The lots at the Marina and the outlets are the usual meeting spot. The big-box lots on Sparks Boulevard work too. So do the casino lots on Victorian Avenue outside the rib cook-off and the Pyramid Way shopping centers. The airport in Reno is ten minutes down McCarran for a fly-and-ship.'),
  P('Our office is on Vista Boulevard by the Marina, just off 80 at the Vista exit.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Victorian Square, the Old Grid, the Marina, the Vistas, Wingfield Springs, D’Andrea, Kiley Ranch, Spanish Springs, Sun Valley, and the Industrial Center',
 prose(
  L('Sparks is a rail town at the bottom and a gravel-pit lake in the middle. The subdivisions climb the hills. The truck meets the old town on a main road.'),
  P('Victorian Square is the old downtown along Victorian Avenue, the casino and the theater and the plaza. The driver meets you in the casino lots or on Prater Way. The old grid south of Prater down to the tracks is small houses on narrow streets. The handoff moves to Prater or Rock Boulevard. The rail yard below it is the reason the city exists, and nothing crosses it.'),
  P('The Marina east of Sparks Boulevard is the lake, the outlets, and the apartments around them. The lots there take the handoff. The Vistas and D’Andrea up Vista Boulevard are subdivisions from the nineties on, wide streets and cul-de-sacs. The curb works on most blocks. Wingfield Springs around the golf course is the same with bigger houses. Kiley Ranch off Sparks Boulevard is the newest part of the city, and the streets outrun the maps. Send the full address.'),
  P('Spanish Springs north of the city line is horse properties and new subdivisions along Pyramid Way. The subdivisions allow the curb, and the horse properties meet the truck on the highway. Sun Valley over the hill to the west is a working valley of manufactured homes on dirt streets. The handoff happens on Sun Valley Boulevard.'),
  P('Reno next door ships with the same trucks and prices the same as Sparks. So do Spanish Springs and Sun Valley. Fernley is thirty miles east and adds a few hours. Carson City is thirty miles south and prices with the city. Truckee is over the pass, and the pass decides the day.'),
 )))

ROUTES=[("Sacramento, CA","I-80 · ~130 mi","Same day","$180–$290"),("San Francisco, CA","I-80 · ~225 mi","Same day","$230–$350"),
 ("Boise, ID","US-95/I-84 · ~420 mi","1 day","$380–$540"),("Salt Lake City, UT","I-80 · ~520 mi","1 day","$380–$540"),
 ("Los Angeles, CA","US-395/I-15 · ~470 mi","1 day","$400–$570"),("Las Vegas, NV","US-95 · ~450 mi","1 day","$400–$560"),
 ("Portland, OR","US-395/I-5 · ~570 mi","1–2 days","$460–$670"),("Seattle, WA","US-395/I-5 · ~700 mi","1–2 days","$520–$750"),
 ("Phoenix, AZ","US-95/I-10 · ~740 mi","2 days","$600–$850"),("Denver, CO","I-80/I-25 · ~900 mi","2 days","$650–$920")]
BODY.append(rate_table('Lanes &amp; Costs','Sparks Car Shipping Lanes and Estimated Costs',
 'The lanes Truckee Meadows cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Sparks for a sedan that runs, open trailer. Count on 10 to 25 percent more for an SUV or a pickup, and more for enclosed. The week you pick and the state of the pass that week set the final figure.',
 prose(
  P('Sparks prices with Reno on every lane, because the same trucks serve both cities. The California lanes ride 80 over the pass and fill both ways every day. The Salt Lake lane rides 80 east and fills with the warehouse traffic. The Las Vegas lane rides 95 across the desert and fills on the weekends. The Arizona lane fills each October with the snowbirds.'),
  P('A start date at the industrial center or the August car week lands in the busiest days. The <a href="car-shipping-cost.html">cost guide</a> explains how size, condition, and timing move the figure.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The California Transplants, the Warehouses, the Industrial Center, the Casino, the Railroad, the Hospital, the Campus, and the Retirees',
 prose(
  L('Sparks relocates warehouse managers, engineers, dealers, railroaders, and families from over the pass. The households leaving California move the most.'),
  P('No income tax and a house that costs half as much pull households over the pass every month. Most ship one car and drive the other. The Sacramento and Bay Area lanes run full both ways. The subdivisions off Sparks Boulevard and in Spanish Springs fill with them. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line.'),
  P('The warehouses along Greg Street and at the industrial center are the largest employers in the valley. The battery plant and the data centers out there relocate engineers on start dates from across the country. The distribution centers move managers on opening dates. The casino on Victorian Avenue moves dealers and managers between properties. The railroad’s yard moves crews on bid cycles. If an employer reimburses the shipment, the paperwork comes from us.'),
  P('The hospital on Prater Way brings nurses and residents each summer. The state university in Reno takes student cars in late August and sends them home in May. So does the community college. A parent sets it up, and an adult signs at the handoff. The naval air station at Fallon rotates squadrons an hour east. The officers ship cars through the city.'),
  P('Retirees come for the taxes and the dry air and leave for Arizona each October. Some of them come back in April, and some of them stay.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Rib Cook-Off, the Car Week, the Rodeo, the Balloons, the Desert Festival, Move-In Week, the Pass, the Smoke, the Floods, and the Wind',
 prose(
  L('Sparks runs on a festival calendar and a pass calendar. The weather problem is a mountain between the city and California.'),
  P('The rib cook-off fills Victorian Square for a week around Labor Day, and half a million people come. The car week in August fills both cities with classic cars. Every enclosed trailer in the valley is booked. The rodeo fills Reno in June, and the balloons fill it in September. The desert festival at the end of August sends tens of thousands of trailers east on 80. They come back a week later. Move-in week in late August fills the campus blocks in Reno. Book three weeks ahead for an August date.'),
  P('The pass closes a few times each winter, and the chain controls slow every trailer on it. The California lanes wait in Sacramento or Sparks until it reopens. The valley gets snow a few times a winter, and it melts in a day. The February 2023 storms closed the pass for days at a time. A storm shifts a pickup to the first clear morning, and the figure does not move.'),
  P('The Truckee floods in a warm winter rain. The January 1997 flood put the river through the warehouse belt and the old grid. The January 2017 flood did it again on a smaller scale. A handoff near the river moves up the hill for a day. The fire smoke in August and September settles in the valley some years and stays for weeks.'),
  P('Summer is hot and dry, a hundred degrees in July. The afternoon wind off the Sierra shifts the loading hour and rattles an open trailer. The carriers load early.'),
 )+chips(["Victorian Square","Victorian Avenue","Prater Way","The Old Grid","Rock Boulevard","The Rail Yard","Greg Street","Glendale Avenue","The Marina","The Outlets","Sparks Boulevard","Vista Boulevard","The Vistas","D'Andrea","Wingfield Springs","Kiley Ranch","Pioneer Meadows","Pyramid Way","Spanish Springs","Sun Valley","McCarran","The Industrial Center","Fernley","Reno","Carson City","Truckee","Tahoe","Fallon","Virginia City"])
 +NOTE('Serving Sparks and the whole of the Truckee Meadows, old grid block or Spanish Springs horse property. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Sparks?',
 prose(
  L('Open trailers carry most of the valley, and the table above is priced for one.'),
  P('Enclosed keeps the pass gravel, the chain spray, and the ash of a smoke year off the paint. The car week crowd books it, and so do Wingfield Springs collectors. Ahead of a pass closure, the car takes the first truck with a slot. We tell you that first.'),
  P('A daily driver rides open without a second thought. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two in detail.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot at the Marina, and a signature at the far end. The start date or the closing sets the week, and the pass sets the day.'),
  P('Say yes to the figure, and a carrier already planning a pass crossing that week takes the car. The lot and the window get agreed that afternoon. The driver shoots each panel at pickup and fills in the Bill of Lading. You sign it, and the delivery check works from it.'),
 )+ULI([
  "Everything personal out of the cabin and the trunk",
  "Fuel down to a quarter tank",
  "Photograph each side and the odometer before the truck comes",
  "One good key, and a note about any known faults",
  "Any add-on alarm turned off",
  "In the old grid, on Victorian Square, or on a horse property, we meet on the highway",
 ])+prose(P('<a href="how-it-works.html">How it works</a> walks through the steps, and <a href="car-shipping-preparation.html">preparation</a> covers what to do before the truck comes.'))))

BODY.append(sec('Why Ship Guy','Why Sparks Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already cross the pass every day. We know which week the car crowd takes every enclosed trailer in the valley.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on Vista Boulevard by the Marina.'),
  P('The person who quotes your move is the person who answers until it is delivered. Open, enclosed, and expedited are compared on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Sparks','250 Vista Blvd #447','Sparks, NV 89434','+17752565954','(775) 256-5954','PT',
 '250+Vista+Blvd+%23447,+Sparks,+NV+89434','Visit Us','Find Ship Guy in Sparks',
 'Our office is on Vista Boulevard by the Marina, just off 80 at the Vista exit.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3798.4173770856255!2d-119.70291150000001!3d39.5325671!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80993f761f1b4257%3A0x76f9f7a34c89a56b!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793631057614!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Sparks to Sacramento or Los Angeles?","Sacramento runs one hundred eighty to two hundred ninety dollars for a sedan. That is a hundred thirty miles over the pass and the lowest lane on the table. Los Angeles runs four hundred to five hundred seventy, about four hundred seventy miles down 395 and 15. An SUV or a pickup runs 10 to 25 percent higher."),
 ("What happens if Donner Pass closes on my pickup day?","The California lanes wait in Sacramento or Sparks until the state reopens it, usually a day. Chain controls slow every trailer even when it stays open. We call the moment the pass closes. The pickup moves to the first clear morning at the same figure. A winter date on a California lane wants a flexible week."),
 ("Do you handle relocations to the industrial center east of Sparks?","Yes, every week of the year. The battery plant and the data centers relocate engineers from across the country on start dates. The distribution centers move managers the same way. We plan the pickup around the first day on the job. When the employer reimburses the move, we supply the paperwork. New subdivisions outrun the maps, so send the full address."),
 ("Can the carrier come to my street in the old grid or Spanish Springs?","Spanish Springs, yes, in the subdivisions. The horse properties meet the truck on Pyramid Way. The old grid south of Prater, no. The streets are narrow, and the driver meets you on Prater Way or Rock Boulevard. The Vistas, Wingfield Springs, Kiley Ranch, and the subdivisions off Sparks Boulevard usually allow the curb."),
 ("Does the car week in August affect my pickup?","Yes. Classic cars take over both cities for a week in early August. The enclosed trailers in the valley are spoken for. A commuter car still ships that week on an open trailer with a day of slack. A show car for the week should be booked by June."),
 ("Why do so many people ship cars into Sparks from California?","Because households come over the pass for the taxes and the housing every month. Most ship one car while driving the other. The Sacramento and Bay Area lanes run full both ways. That keeps them the lowest-cost lanes out of the valley. The Marina lots and the Sparks Boulevard exits are the usual meeting spots."),
 ("Can you ship a car to or from Reno, Carson City, or Fernley?","Yes. Reno rides the same carriers and prices the same as Sparks on every lane. Carson City is thirty miles south and prices with the city. Fernley is thirty miles east and adds a few hours on the day. Truckee is over the pass, and the pass decides the day."),
 ("Can you deliver on a University of Nevada move-in date?","Yes. Cars reach the Reno campus in late August and leave in May. Mom or Dad books, and an adult signs at the lot. The campus blocks are jammed that week, so the Marina lots are the meeting point. Your date fixes the window."),
 ("Can you ship a car that does not run from Sparks?","Yes. A winch truck handles it, and the loading time is in the figure. The Marina lots and the big-box lots on Sparks Boulevard are flat. Tell us up front whether it rolls, steers, and brakes."),
 ("What do you need for a Sparks car shipping quote?","Where it starts and ends, with the neighborhood. What it is and whether it runs. Open or enclosed, and the week around the start date or the closing. That gets you a Sparks figure the same day."),
]
BODY.append(faq_section(FAQ,'Sparks FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Sparks?','Two minutes on the form above gets your lane a Sparks figure. Name the neighborhood and the week, and a carrier already crossing the pass takes it.','+17752565954','(775) 256-5954','Get your free Sparks quote'))

build({
 'slug':'auto-transport-sparks-nevada',
 'title':'Car Shipping in Sparks, NV — Auto Transport | Ship Guy',
 'meta':'Car shipping in Sparks, NV, the rail city beside Reno on Interstate 80. California transplant moves over the pass, industrial center and warehouse relocations, the August car week, main-road handoffs for the old grid and Spanish Springs horse properties, curbside pickups in the Vistas and Kiley Ranch, and the pass closures. Local office on Vista Boulevard. Free quote.',
 'h1':'Car Shipping in<br>Sparks, <span class="accent">Nevada</span>',
 'lede':'Open, enclosed, and expedited auto transport across Sparks and the Truckee Meadows, planned around 80, the pass, the warehouse calendar, the festival weeks, and the smoke.',
 'tel':'+17752565954','disp':'(775) 256-5954','brand':'Sparks','keyword':'car shipping in sparks',
 'localterms':['sparks','reno','rail','warehouses','pass','interstate 80','580','395','pyramid way','mccarran','sparks boulevard','vista boulevard','prater way','victorian avenue','victorian square','marina','outlets','old grid','rock boulevard','rail yard','greg street','glendale avenue','vistas','wingfield springs','kiley ranch','spanish springs','sun valley','industrial center','fernley','carson city','truckee','donner','sacramento','bay area','san francisco','boise','salt lake','los angeles','las vegas','portland','seattle','phoenix','denver','arizona','snowbirds','california','transplants','income tax','warehouse managers','engineers','dealers','railroaders','battery plant','data centers','distribution centers','casino','bid cycles','hospital','nurses','residents','state university','community college','student','fallon','squadrons','retirees','rib cook-off','labor day','car week','classic cars','rodeo','balloons','desert festival','move-in','chain controls','february 2023','snow','truckee','january 1997','january 2017','flood','smoke','wind','sierra','gravel','chain spray','ash','bill of lading','fmcsa','winch','horse properties','manufactured homes','gravel-pit','theater','plaza','fly-and-ship','susanville','utah line','tahoe','virginia city','pioneer meadows'],
}, BODY, FAQ)
