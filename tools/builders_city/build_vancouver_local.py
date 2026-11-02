import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Vancouver, Washington','Car shipping on the north bank of the Columbia, across two bridges from Portland and on the Interstate 5 lane',
 ['Car shipping in Vancouver depends on two bridges and the Portland carrier pool across them. Ship Guy is a licensed auto transport broker with an office on Broadway in downtown Vancouver.',
  'We book vetted carriers across Clark County, from the waterfront to Salmon Creek and Camas to Ridgefield. The trucks belong to the carriers. Ship Guy holds the license and the bond.',
  'Interstate 5 crosses the Columbia on the Interstate Bridge. It runs north through Hazel Dell and Salmon Creek to Seattle. Interstate 205 crosses on the Glenn Jackson Bridge and loops the east side. State Route 14 runs the river east to Camas and the Gorge, and 500 cuts across the middle.',
  'This page covers the bridges, 500 and 503, downtown, the waterfront, Hazel Dell, Orchards, and Camas. It also covers the Portland commute, the port, the hospitals, the fireworks, the ice storms, and the lanes.'],
 'Vancouver at a glance',
 ['Most pickups happen within 1 to 3 days. Vancouver ships through the Portland carrier pool, and the carriers cross the bridges a dozen times a day.',
  'Portland is the same trip, and Seattle and Eugene are a same-day haul. Spokane and Boise take a day. Sacramento takes one to two, and the Bay Area takes two. Los Angeles takes two to three, and Denver and Phoenix take three.'],
 'Tell us which side of 205 you are on and whether the street climbs. Downtown, Uptown Village, and the waterfront meet the truck at a lot. Hazel Dell, Orchards, Cascade Park, and Camas usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 5, Interstate 205, the Two Bridges, State Route 14, 500, 503, and Mill Plain',
 prose(
  L('Every carrier that serves Vancouver crosses the Columbia, and the two bridges set the schedule.'),
  P('Interstate 5 crosses on the Interstate Bridge, a pair of lift spans from 1917 and 1958. Neither has a shoulder. The spans lift for river traffic, and the bridge backs up into Portland every afternoon. The replacement is planned for the next decade. Interstate 205 crosses on the Glenn Jackson Bridge downstream, eight lanes and never a lift. Most carriers take 205 and come up the east side through Cascade Park and Orchards.'),
  P('State Route 14 runs the north bank from the bridge east through Camas and Washougal into the Gorge. State Route 500 runs from 5 at 39th Street east across the county to Orchards and 503. State Route 503 runs north from Orchards to Battle Ground. Mill Plain Boulevard and Fourth Plain Boulevard are the east-west arterials, and 164th Avenue carries the east side.'),
  P('The carriers come off 205 at Mill Plain and off 5 at 78th Street in Hazel Dell. The mall lots at Vancouver Mall on 205 are the usual meeting spot. The centers along 164th Avenue and the Hazel Dell lots on Highway 99 work too. The fairgrounds lots at the 179th Street exit work outside fair week and the amphitheater season.'),
  P('Our office is on Broadway in downtown Vancouver, a few blocks from Esther Short Park.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Waterfront, Uptown Village, Hazel Dell, Salmon Creek, Orchards, Cascade Park, Camas, Battle Ground, and Ridgefield',
 prose(
  L('Vancouver is an old river town with a new waterfront and a county of subdivisions behind it. The truck reaches most of them.'),
  P('Downtown around Esther Short Park is a compact grid of storefronts and new apartment blocks. The waterfront below it is towers on a riverwalk. A seventy-five-foot trailer meets neither. The driver meets you at the lots by the Interstate 5 ramps or along Columbia Way. Uptown Village on Main Street is the same, with the handoff on Fourth Plain.'),
  P('The old fort grounds and Officers Row sit east of downtown, with Pearson Field beside them. The Hudson neighborhoods around them are narrow streets of older houses. The handoff moves to Mill Plain. Hazel Dell along Highway 99 is wide postwar streets, and the curb works. Salmon Creek north of it holds the state university campus and the second hospital, with subdivisions behind.'),
  P('Orchards and Sifton on the east side are the newest subdivisions, built on wide streets around 503. The driver reaches the house. Cascade Park and Fisher’s Landing along 164th are the same. Camas and Washougal east on 14 sit on the hills above the river. The older blocks in Camas climb hard, and the handoff moves to the mill town flats.'),
  P('Battle Ground north on 503 is a small town with wide new subdivisions around it. Ridgefield, La Center, and Woodland along 5 are the same, and Ridgefield has grown fastest. Felida and Lake Shore to the northwest sit on the lake and the bluffs. The curb works on most of their streets. All of them price the same as Vancouver, and so does Portland across the river.'),
 )))

ROUTES=[("Eugene, OR","I-5 · ~120 mi","Same day","$180–$290"),("Seattle, WA","I-5 · ~165 mi","Same day","$220–$340"),
 ("Spokane, WA","I-84/US-395 · ~360 mi","1 day","$320–$460"),("Boise, ID","I-84 · ~440 mi","1 day","$380–$540"),
 ("Sacramento, CA","I-5 · ~590 mi","1–2 days","$480–$700"),("San Francisco, CA","I-5 · ~645 mi","2 days","$520–$750"),
 ("Salt Lake City, UT","I-84 · ~780 mi","2 days","$560–$820"),("Los Angeles, CA","I-5 · ~975 mi","2–3 days","$700–$980"),
 ("Denver, CO","I-84/I-80 · ~1,250 mi","3 days","$850–$1,200"),("Phoenix, AZ","I-5/I-10 · ~1,350 mi","3 days","$900–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Vancouver Car Shipping Lanes and Estimated Costs',
 'The lanes Clark County cars run most, with estimated open-trailer ranges. Your own route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*Estimated 2026 ranges from Vancouver, operable sedan, open trailer. Larger vehicles run 10 to 25 percent higher, and enclosed runs higher still. The season and carrier availability on your dates set the actual quote.',
 prose(
  P('Vancouver prices with Portland on every lane, because the carriers are the same trucks ten miles south. The Seattle lane is the busiest and the easiest to fill. The California lanes ride 5 the whole way and fill with retirees each fall. The Boise and Salt Lake lanes ride 84 up the Gorge. The Gorge closes a few days each winter.'),
  P('A move timed to the September move-in or a fall transfer date ships with the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Portland Commute, the Port, the Hospitals, the Software Firms, and the State University',
 prose(
  L('Vancouver relocates Portland commuters, nurses, engineers, and retirees who want the tax math of the north bank.'),
  P('A big share of the county works across the river. Washington charges no income tax and Oregon charges no sales tax, so people live here and shop there. Transfers to the chip plants and the sportswear campus west of Portland land here all year. If your employer reimburses the move, the paperwork comes from us.'),
  P('The port on the river west of downtown lands a Japanese automaker’s imports by the shipload. Those cars leave by rail and truck, and we do not move them. A private car that arrived by ship and has been released is a domestic move like any other. The ocean leg is booked separately.'),
  P('The two hospitals, one on Mill Plain and one in Salmon Creek, hire traveling nurses year round. The software firms downtown and the wafer makers on the east side move engineers in on offer dates. The state university campus in Salmon Creek and the community college take cars each September. The booking is set up by a parent, and someone over eighteen signs at a campus lot.'),
  P('Retirees arrive from California and leave for Arizona each fall. PCS moves to the bases near Tacoma ride the same 5 lane. Ship Guy has no military tie. The <a href="military-car-shipping.html">military</a> page has the timing, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page has the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Fireworks, the Fair, the Amphitheater, the Gorge Wind, the Ice Storms, and the Snow Days',
 prose(
  L('Vancouver runs on a river calendar and a Gorge forecast. The east wind decides the winter.'),
  P('The Fourth of July fireworks at the old fort draw one of the largest crowds in the Northwest. Downtown closes for the day. The county fair fills the Ridgefield fairgrounds for ten days in August. The amphitheater beside it runs concerts from May through September. The 179th Street exit backs up on show nights. A handoff near any of them moves to the next morning.'),
  P('The farmers market fills the streets around Esther Short Park every weekend from March through October. The parade of bands fills Hazel Dell in May. The Oregon side adds its own calendar. A Portland marathon or a Blazers playoff night slows the bridges, and the carriers cross before noon.'),
  P('Winter is rain, and the Gorge east wind turns it to ice. A silver thaw coats every road east of 205 in an hour. The January 2024 ice storm shut the county for most of a week. It closed 84 through the Gorge for days. Snow is rare, but two inches shuts the bridges and the hills in Camas. The carriers wait in Portland until the ramps clear. A winter pickup can lose a day.'),
  P('The Columbia rises with the spring melt. In a big year it climbs the waterfront steps, but the dams upstream keep it off the streets. Wildfire smoke drifts in from the Gorge in a dry September. Neither shifts more than the loading hour.'),
 )+chips(["Downtown","Esther Short","Waterfront","Uptown Village","Main Street","Officers Row","Hudson's Bay","Pearson Field","Fruit Valley","Hazel Dell","Highway 99","Salmon Creek","Felida","Lake Shore","Minnehaha","Walnut Grove","Fourth Plain","Orchards","Sifton","Mill Plain","Cascade Park","Fisher's Landing","164th Avenue","Vancouver Mall","Camas","Washougal","Battle Ground","Brush Prairie","Ridgefield","La Center","Woodland","Portland"])
 +NOTE('Serving Vancouver and all of Clark County, waterfront tower or Battle Ground acreage. Tell us which side of 205 you are on and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Vancouver?',
 prose(
  L('Most Clark County cars ride an open trailer, and the lane table above is priced that way.'),
  P('An enclosed trailer keeps off the road grit, the winter de-icer, and the Gorge grime. The collectors in Felida and Camas book one for the show cars. Executives relocating a new car to the software firms book one too.'),
  P('A commuter car headed over the bridge rides open without a worry. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages walk through the choice.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot at the mall or in Hazel Dell, and a signature at the other end. The start date picks the week.'),
  P('Approve the price, and the car is booked with a carrier already crossing the bridges. The lot and the window are settled that day. At pickup you and the driver list every existing mark on the Bill of Lading. Both signatures go on it, and delivery is compared to it.'),
 )+ULI([
  "Clear the cabin and the trunk of personal items",
  "Leave about a quarter tank of fuel",
  "Photograph every side and the odometer before the handoff",
  "Give the driver one working key and name any fault",
  "Turn off an aftermarket alarm",
  "Downtown, on the waterfront, or on the Camas hills, meet the truck at a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages cover each step.'))))

BODY.append(sec('Why Ship Guy','Why Vancouver Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already cross the Columbia every day. We know which bridge to send them over.'),
  P('Ship Guy’s FMCSA license and $75,000 bond are listed on the federal register. Anyone can look them up. Our office is on Broadway in downtown Vancouver.'),
  P('Your coordinator follows the move from the first call to the last signature. The <a href="services.html">services</a> page explains open, enclosed, and expedited transport.'),
 )))

BODY.append(office('Vancouver','915 Broadway St #574','Vancouver, WA 98660','+13608452434','(360) 845-2434','PT',
 '915+Broadway+St+%23574,+Vancouver,+WA+98660','Visit Us','Find Ship Guy in Vancouver',
 'Our office is on Broadway in downtown Vancouver, a few blocks from Esther Short Park.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3444.0467003098684!2d-122.6700536!3d45.62845050000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5495a92e4b1e845b%3A0x9fd72c5fd0bffcb2!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793287436877!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Vancouver to Seattle or California?","Seattle runs two hundred twenty to three hundred forty dollars for a sedan. That is about one hundred sixty-five miles up 5. Los Angeles runs seven hundred to nine hundred eighty, close to a thousand miles down 5. Sacramento sits between them at four hundred eighty to seven hundred. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street downtown or on the waterfront?","Usually not. Downtown is a tight grid and the waterfront is towers on a riverwalk. The driver meets you at the lots by the Interstate 5 ramps or along Columbia Way. Hazel Dell, Orchards, Cascade Park, Battle Ground, and most of Camas allow the curb."),
 ("Which bridge does the carrier use?","Almost always the Glenn Jackson Bridge on 205. It has eight lanes and never lifts. The Interstate Bridge on 5 lifts for river traffic and backs up into Portland every afternoon. A carrier takes 5 only for Hazel Dell and Salmon Creek, and it crosses before noon."),
 ("Do you ship cars for people moving here from Portland or the Oregon suburbs?","Yes, every week. Transfers to the chip plants and the sportswear campus west of Portland land here all year. Most ship one car and drive the other. If your employer reimburses the move, the paperwork comes from us. Portland deliveries price the same as Vancouver."),
 ("Can you pick up a car that came through the port?","Yes, once it has been released to you. The automaker shipments leave by rail and truck, and we do not move those. A private car that arrived by ship ships domestically like any other. Tell us the release date and the location. The ocean leg is booked separately if you need it."),
 ("Can you ship a car to or from Camas, Battle Ground, or Ridgefield?","Yes, and all three price the same as Vancouver. Camas rides the same carriers east on 14. The older hill blocks meet the truck on the flats. Battle Ground rides them up 503, and the curb works. Ridgefield rides them up 5 to the 179th Street exit. Send the full address for a county road."),
 ("What happens if an ice storm hits on my pickup day?","The driver waits in Portland until the ramps clear. The Gorge east wind coats every road east of 205 in an hour. The January 2024 storm shut the county for most of a week. A winter pickup can lose a day. You hear it from us before the driver does."),
 ("Can you deliver on the move-in date at the Salmon Creek campus?","Yes. The state university campus and the community college take cars each September and send them home in June. A parent books it, and someone over eighteen signs at a campus lot. The window is matched to move-in day and moves with it."),
 ("Can you ship a car that does not run from Vancouver?","Yes. A winch-equipped carrier is sent, and the extra loading time is priced in from the start. The mall lots on 205 or the fairgrounds lots in Ridgefield give the driver level ground. Say whether the car rolls, steers, and brakes."),
 ("What do you need for a Vancouver car shipping quote?","Both addresses, with the side of 205. Year, make, and model. Running or not. Open or enclosed. The week you need. Five answers, and the Vancouver number is back the same day."),
]
BODY.append(faq_section(FAQ,'Vancouver FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Vancouver?','Two minutes on the form above gets your lane a number. Name the neighborhood and the week, and a carrier already crossing the bridges takes it.','+13608452434','(360) 845-2434','Get your free Vancouver quote'))

build({
 'slug':'auto-transport-vancouver-washington',
 'title':'Car Shipping in Vancouver, WA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Vancouver, WA, on the north bank of the Columbia across two bridges from Portland. Portland commuter relocations, hospital and software moves, the port, lot handoffs downtown and on the waterfront, curbside pickups in Hazel Dell, Orchards, Camas, and Battle Ground, the Glenn Jackson Bridge, the Gorge ice storms, and the fireworks. Local office on Broadway downtown. Free quote.',
 'h1':'Car Shipping in<br>Vancouver, <span class="accent">Washington</span>',
 'lede':'Open, enclosed, and expedited auto transport across Clark County, planned around the two bridges, 205, the Portland carrier pool, the hospitals, and the Gorge wind.',
 'tel':'+13608452434','disp':'(360) 845-2434','brand':'Vancouver','keyword':'car shipping in vancouver',
 'localterms':['vancouver','columbia','portland','interstate 5','broadway','clark county','waterfront','salmon creek','camas','ridgefield','interstate bridge','hazel dell','seattle','interstate 205','glenn jackson bridge','state route 14','washougal','gorge','500','503','downtown','orchards','commute','port','hospitals','fireworks','ice storms','eugene','spokane','boise','sacramento','bay area','los angeles','denver','phoenix','uptown village','cascade park','lift spans','1917','1958','shoulder','replacement','eight lanes','battle ground','mill plain','fourth plain','164th avenue','78th street','vancouver mall','highway 99','fairgrounds','179th street','amphitheater','esther short park','main street','columbia way','officers row','pearson field','hudson','state university','sifton','fisher','mill town','la center','woodland','felida','lake shore','bluffs','retirees','move-in','transfer','income tax','sales tax','chip plants','sportswear','automaker','imports','rail','traveling nurses','software firms','wafer','offer dates','community college','arizona','pcs','fourth of july','county fair','august','concerts','farmers market','parade of bands','marathon','blazers','silver thaw','january 2024','two inches','spring melt','wildfire smoke','de-icer','bill of lading','fmcsa','fruit valley','minnehaha','walnut grove','brush prairie'],
}, BODY, FAQ)
