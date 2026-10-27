import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Kenosha, Wisconsin','Car shipping on the state line, halfway between Milwaukee and Chicago on the busiest truck lane in Wisconsin',
 ['Car shipping in Kenosha is as easy as it gets, because the city sits between two carrier hubs. Ship Guy is a licensed auto transport broker with an office on 30th Avenue.',
  'We book vetted carriers across Kenosha County, from Pleasant Prairie and Somers to Bristol and Twin Lakes. We do not own the trucks.',
  'Interstate 94 runs along the west side of the city, thirty-five miles to Milwaukee and fifty-five to Chicago. Highway 50 and Highway 158 connect the interstate to the lakefront. Highway 31, which is Green Bay Road, runs north to Racine. Highway 32 follows the lake.',
  'This page covers the interstate and the state line, the lakefront blocks, and the subdivisions out west. It also covers the headquarters, the warehouses, the Navy base, the winter, and the lanes.'],
 'Kenosha at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers running between Chicago and Milwaukee pass the city on 94 all day.',
  'Milwaukee, Chicago, Madison, and Rockford are same-day lanes. Indianapolis, Minneapolis, Detroit, and St. Louis take a day. Florida runs three, and Arizona runs three to four.'],
 'Tell us which side of the interstate. The lakefront and the older blocks east of 30th Avenue need a meeting spot. Pleasant Prairie and the subdivisions out west usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 94, Highway 50, 158, 31, and the State Line',
 prose(
  L('Kenosha sits on the one road every carrier between Chicago and Minneapolis has to use.'),
  P('Interstate 94 runs north and south along the west edge of the city. It carries 41 with it between Milwaukee and the state line. At the line it becomes the tollway into Illinois. The Illinois tolls are built into a Chicago quote. The Wisconsin side charges none.'),
  P('Highway 50 is 75th Street, the road from the interstate to the lake. Highway 158 is 52nd Street, the other road across town. Highway 165 carries Pleasant Prairie, and Highway 31 runs north to Racine as Green Bay Road.'),
  P('The carriers come off 94 at Highway 50, Highway 158, and Highway 165. The outlet mall lot at 165 and the big-box lots along 75th Street are the usual meeting spots. The whole metro works from the same handful of exits.'),
  P('Our office sits on 30th Avenue on the north side of the city, ten minutes from the interstate.'),
 ), alt=True))

BODY.append(sec('The Lakefront &amp; the West Side','HarborPark, the Old Plant Blocks, Pleasant Prairie, and the Grids',
 prose(
  L('Kenosha built cars for a century, and the city is laid out like it.'),
  P('The old plant blocks east of 30th Avenue are tight grids of worker housing with alleys behind them. A main road is the usual spot. The lakefront, HarborPark, and downtown have narrow streets, a streetcar loop, and summer traffic. The driver meets you on Sheridan Road or at the museum lots.'),
  P('Pleasant Prairie, the subdivisions along Highway 50, and the new additions out past the interstate are wide grids. The truck usually reaches the curb there. Somers and the Parkside area to the north are the same.'),
  P('Bristol, Paddock Lake, Salem Lakes, and Twin Lakes are the lake towns out west. Their shoreline roads are narrow, and the handoff happens on Highway 50 or Highway 83. The Illinois towns just over the line ride the same trucks.'),
  P('The warehouses along the interstate have their own truck entrances. A handoff at the dock works when the employer allows it.'),
 )))

ROUTES=[("Milwaukee, WI","I-94 · ~35 mi","Same day","$110–$190"),("Chicago, IL","I-94 · ~55 mi","Same day","$130–$220"),
 ("Madison, WI","I-94 · ~120 mi","Same day","$170–$270"),("Green Bay, WI","I-94/I-43 · ~150 mi","Same day","$190–$300"),
 ("Indianapolis, IN","I-94/I-65 · ~240 mi","Same day","$240–$360"),("Detroit, MI","I-94 · ~330 mi","1 day","$310–$450"),
 ("St. Louis, MO","I-94/I-55 · ~355 mi","1 day","$330–$470"),("Minneapolis, MN","I-94 · ~375 mi","1 day","$340–$490"),
 ("Dallas, TX","I-55/I-44 · ~1,000 mi","2–3 days","$700–$980"),("Orlando, FL","I-65/I-75 · ~1,260 mi","3 days","$830–$1,180")]
BODY.append(rate_table('Lanes &amp; Costs','Kenosha Car Shipping Lanes and Estimated Costs',
 'Where Kenosha cars go, with estimated open-trailer ranges for each lane. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, open trailer. Count on 10 to 25 percent more for an SUV or pickup, and more again for enclosed. Illinois tolls, the winter, and the carriers free on your dates set the final number.',
 prose(
  P('Kenosha prices like Milwaukee and Chicago, because it shares both carrier pools. A truck headed either way can stop for a Kenosha car without leaving 94.'),
  P('The Florida lane fills each fall, and the Illinois tolls add a few dollars to every Chicago quote. The <a href="car-shipping-cost.html">cost guide</a> takes the number apart.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Headquarters, the Warehouses, the Commuters, and the Navy',
 prose(
  L('Kenosha relocates people for three headquarters, a row of warehouses, a Navy base, and a train to Chicago.'),
  P('The tool company on 80th Street and the apparel company on 60th Street relocate staff on start dates. So does the shipping-supply company in Pleasant Prairie. The warehouses and fulfillment centers along the interstate hire managers from every state. When the employer pays for the move, we supply the paperwork it needs.'),
  P('Thousands of residents ride the train to Chicago every morning. Families move up from Illinois for the housing all year. Many ship the second car rather than drive two cars up 94 on moving day.'),
  P('The Navy base at Great Lakes sits twenty-five miles south over the line. Many of its instructors and staff live in Kenosha County for the housing. Most orders cover one car. The other one comes with us. The <a href="military-car-shipping.html">military</a> page covers a PCS move in detail.'),
  P('The college on the lake and the university toward Racine take in student cars each August. They send them home each May, and an adult signs for the car at the campus lot.'),
  P('The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of any relocation, including one from just over the line.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Lake Snow, the Fog, Country Thunder, and the Lakefront Summer',
 prose(
  L('Kenosha gets the lake’s weather first and the festival traffic second. The carriers plan for both.'),
  P('Winter brings about forty-five inches of snow. A wind off the lake turns a plain storm into lake snow along the shore. Blizzards shut 94 for a day a few times each winter, and the tollway closes with it. The trucks sit until the plows finish, and a winter pickup can lose a day.'),
  P('Spring and fall bring fog off the lake that slows the lakefront roads for a morning. Summer brings the festival season on the harbor and the country music festival in Twin Lakes each July. That weekend fills Highway 50 and every road around the lake towns. We schedule lake-town pickups around it.'),
  P('Hail comes through with the summer thunderstorms, and we shift the window when it is forecast. Heat moves the loading hour earlier in July and August.'),
 )+chips(["Downtown","HarborPark","Lakefront","Library Park","Uptown","Columbus Park","Forest Park","Allendale","Washington Park","Pleasant Prairie","Somers","Bristol","Paddock Lake","Salem Lakes","Twin Lakes","Trevor","Wilmot","Carthage","Parkside","Highway 50","Highway 158","Green Bay Road","Sheridan Road","Racine","Zion","Waukegan"])
 +NOTE('Serving Kenosha County and the state line. Tell us the side of the interstate, the week, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Kenosha?',
 prose(
  L('Open carriers haul nearly everything that leaves Kenosha, and the 94 lane is quoted for them.'),
  P('An enclosed trailer keeps the salt and the lake grit off the car. The collector garages around Twin Lakes and the lakefront book enclosed trailers. So does a car headed south for the winter.'),
  P('A commuter car rides open to Chicago or Milwaukee without a second thought. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof costs and covers.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff by the interstate or the lake, and a delivery. On the 94 lane the week comes quickly.'),
  P('Approve the price, and a carrier already running 94 picks up the booking the same day. We name the spot. The driver and you check the car over and write it up on a Bill of Lading. Both of you sign. The delivery inspection follows that sheet.'),
 )+ULI([
  "Empty the car of anything personal",
  "Leave roughly a quarter tank of fuel",
  "Take photos of every panel before pickup, especially after a lake storm",
  "Provide a working key and point out any mechanical issue",
  "Switch off the aftermarket alarm if there is one",
  "For a lakefront or lake-town pickup, plan to meet the truck on the highway",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages run through the rest.'))))

BODY.append(sec('Why Ship Guy','Why Kenosha Drivers Choose Ship Guy',
 prose(
  L('We work the 94 lane every day and plan around the lake, the tollway, and the moving-day traffic.'),
  P('Ship Guy’s FMCSA brokerage authority is active, and a $75,000 surety bond backs every booking. Both are searchable on the public record. Our office is on 30th Avenue.'),
  P('The coordinator who quotes the move is the one who sees it to delivery. Open, enclosed, and expedited transport are all available, and the <a href="services.html">services</a> page describes each one.'),
 ), alt=True))

BODY.append(office('Kenosha','3535 30th Ave #604A','Kenosha, WI 53144','+12624743395','(262) 474-3395','CT',
 '3535+30th+Ave+%23604A,+Kenosha,+WI+53144','Visit Us','Find Ship Guy in Kenosha',
 'Our office is on 30th Avenue on the north side of the city, ten minutes from Interstate 94.'))

FAQ=[
 ("Is Kenosha priced like Milwaukee or like Chicago?","Both, and that is the advantage. The city sits on 94 between the two carrier pools. A truck headed either way can take the car. Milwaukee runs one hundred ten to one hundred ninety dollars for a sedan. Chicago runs one hundred thirty to two hundred twenty."),
 ("Do the Illinois tolls change the price of a Chicago shipment?","A little. The tollway starts at the state line, and the carrier pays it by transponder. The toll is built into the quote rather than added at delivery. The Wisconsin side of 94 is free."),
 ("Can you ship a car for someone moving up from Illinois?","Yes, every week. Families cross the line for the housing all year. Many ship the second car instead of driving two on moving day. The carrier picks it up in Illinois and delivers it to the curb or a lot here."),
 ("Do you handle a PCS move to Naval Station Great Lakes?","Yes. The base sits twenty-five miles south over the line, and many instructors and staff live in Kenosha County. Most orders cover one car, and the other one comes with us. The base is gated, and the handoff happens outside it in North Chicago or Waukegan. Ship Guy is a private broker with no connection to the Navy."),
 ("What happens if lake snow or a blizzard hits on my pickup day?","The driver waits for 94 and the tollway to reopen behind the plows. A winter pickup can lose a day. We call when the forecast changes the plan. The handoff moves to a plowed lot after a storm."),
 ("Does Country Thunder or the harbor festival season affect pickups?","Out west, yes. The country music festival in Twin Lakes fills Highway 50 for a weekend each July. We schedule lake-town pickups around it. The harbor festivals slow the lakefront on summer weekends. The driver meets you on Sheridan Road those days."),
 ("Can the carrier come into the lakefront blocks or the old plant neighborhoods?","Usually not. The streets east of 30th Avenue are tight, parked on both sides, and backed by alleys. The driver meets you on Sheridan Road, on 52nd Street, or at the museum lots by the harbor. Pleasant Prairie and the west side subdivisions usually allow the curb."),
 ("Do you ship cars for people hired at the warehouses or the headquarters?","Yes, on start dates all year. The warehouses along 94 hire managers from every state, and the headquarters relocate staff the same way. A handoff at the dock works when the employer allows it. We supply the paperwork for a reimbursed move."),
 ("Can you ship a car that does not run from Kenosha?","Yes. A winch-equipped carrier takes it, and the extra loading time is priced in. Pick a flat spot, which usually means a lot by the interstate rather than a lakefront street. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Kenosha car shipping quote?","Both addresses, with the side of the interstate on this end. Year, make, and model. Does it run. Open or enclosed. The dates you can work with. That is all a Kenosha quote takes."),
]
BODY.append(faq_section(FAQ,'Kenosha FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Kenosha?','Run the form above for a price in about two minutes. Tell us the neighborhood and your dates, and a carrier already on 94 does the rest.','+12624743395','(262) 474-3395','Get your free Kenosha quote'))

build({
 'slug':'auto-transport-kenosha-wisconsin',
 'title':'Car Shipping in Kenosha, WI — Auto Transport | Ship Guy',
 'meta':'Car shipping in Kenosha, WI on Interstate 94 between Milwaukee and Chicago. Lakefront and old plant-block handoffs, Pleasant Prairie curbside, headquarters and warehouse relocations, Great Lakes Navy moves, Illinois tolls explained, lake-snow planning. Local office on 30th Avenue. Free quote.',
 'h1':'Car Shipping in<br>Kenosha, <span class="accent">Wisconsin</span>',
 'lede':'Open, enclosed, and expedited auto transport across Kenosha County, planned around the interstate, the lake, and the state line.',
 'tel':'+12624743395','disp':'(262) 474-3395','brand':'Kenosha','keyword':'car shipping in kenosha',
 'localterms':['kenosha','interstate 94','highway 50','highway 158','highway 165','highway 31','highway 32','highway 83','green bay road','sheridan road','75th street','52nd street','30th avenue','state line','tollway','tolls','lakefront','harborpark','downtown','streetcar','museum','plant blocks','pleasant prairie','somers','parkside','bristol','paddock lake','salem lakes','twin lakes','outlet mall','warehouses','fulfillment','headquarters','tool company','apparel','shipping-supply','train','commuters','illinois','navy','great lakes','north chicago','waukegan','college','university','racine','lake snow','fog','blizzards','plows','country music festival','harbor','hail','milwaukee','chicago','madison','green bay','rockford','indianapolis','minneapolis','detroit','st. louis','dallas','orlando','florida','arizona'],
}, BODY, FAQ)
