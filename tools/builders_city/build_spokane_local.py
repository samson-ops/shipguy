import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Spokane, Washington','Car shipping in the hub of the Inland Northwest, four hours and one mountain pass from the coast',
 ['Car shipping in Spokane runs off Interstate 90 through the middle of the city. Ship Guy is a licensed auto transport broker with an office on Pacific Avenue downtown.',
  'We book vetted carriers across the Inland Northwest, from Airway Heights to the Valley and Coeur d’Alene. The trucks belong to the carriers, and we hold the authority and the bond.',
  'Interstate 90 crosses the city east and west with exits at Maple, Division, Hamilton, Sprague, and Argonne. US 2 is Division Street north and the Sunset Hill west to the airport. US 195 runs south to the Palouse. The north freeway is opening in stages between Wandermere and the river.',
  'This page covers 90, Division, downtown, the South Hill, the north side, the Valley, and the Idaho line. It also covers the base, the hospitals, the universities, Hoopfest, the passes, the smoke, and the lanes.'],
 'Spokane at a glance',
 ['Most pickups happen within 1 to 3 days. The Seattle carriers come over the pass on 90. The Boise and Montana trucks arrive on 95 and 90 from the other direction.',
  'Missoula is a same-day haul. Seattle, Portland, and Boise take a day. Salt Lake City and Sacramento take two. Denver and Los Angeles take three, and the Midwest takes three to four.'],
 'Tell us the side of the river and whether you are on the hill. The South Hill, Browne’s Addition, and the blocks around the campus need a meeting spot. The north side grids, the Valley, and the new subdivisions usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 90, Division Street, the North Freeway, US 195, US 2, and the Passes',
 prose(
  L('Spokane is the only city for three hundred miles in any direction. Every carrier crossing the northern tier passes through it.'),
  P('Interstate 90 runs through the middle of the city between the Idaho line and the Cascades. The exits at Maple, Division, Hamilton, Sprague, Argonne, and Sullivan serve the city and the Valley. Coeur d’Alene is thirty minutes east, and the Montana line is two hours. Seattle is four hours west over Snoqualmie Pass, and the pass closes a few times each winter.'),
  P('Division Street is US 2 and 395 north through the middle of the city to the Y. The new north freeway carries 395 from Wandermere south toward the river. The state is building the last link to 90 in stages. US 195 runs south to Pullman and the Palouse. US 2 climbs the Sunset Hill west to the airport, Fairchild, and Airway Heights. Trent Avenue runs east along the river to the Valley.'),
  P('Downtown is a one-way grid around Riverside, Sprague, and Main. Monroe Street crosses the river to the north side. The Maple and Ash pair carries the west side. Grand Boulevard and Bernard climb the South Hill. Sprague Avenue is the old highway through the Valley, and Pines and Sullivan cross it. The river splits the city, and the falls run through the middle of downtown.'),
  P('The carriers stage at the truck stops by the Broadway and Sullivan exits in the Valley. The airport exits on the West Plains work too. The mall lots on Division, the Valley mall at Sullivan, and the arena lots are the meeting spots. No road in the region charges a toll.'),
  P('Our office is on Pacific Avenue downtown, two blocks from the Davenport.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Browne’s Addition, the South Hill, the Campus, the North Side, Five Mile, the Valley, Liberty Lake, Airway Heights, and Coeur d’Alene',
 prose(
  L('Spokane is a railroad city with a hill on one side and a prairie on the other. The handoff follows the slope.'),
  P('Downtown is a grid of one-way streets, old brick blocks, and the hotel district around the Davenport. The driver meets you at the arena lots or on Division. Browne’s Addition west of downtown is the oldest neighborhood in the city. Its mansions sit on narrow streets under old trees. The handoff moves to Riverside or the arena. Peaceful Valley below it sits on the river flat and floods.'),
  P('The South Hill climbs from downtown to the park. The streets above 29th are steep, narrow, and shaded. The driver meets you at the shopping center on Grand or on 29th. The Perry District and the blocks around the campus on Hamilton are student rentals and small lots. The handoff moves to Hamilton or the arena. Lincoln Heights and the Moran Prairie above the hill are wide, and the curb works.'),
  P('The north side between the river and Francis is 1940s and 1950s grids with wider streets. The driver reaches the house on most of them. Shadle, Audubon, Hillyard, and Logan are the same. Five Mile, Wandermere, and Mead to the north are the newest subdivisions, with wide loops and open curbs. The West Plains and Airway Heights are flat and easy.'),
  P('Spokane Valley is its own city east of Havana Street. It has the mall, the subdivisions, and lots at every exit. Liberty Lake at the state line is newer still, with a few gated sections. Coeur d’Alene, Post Falls, and Hayden across the line in Idaho ride the same carriers. The state line adds no paperwork. Cheney with the state university sits fifteen minutes southwest on 90. All of them price the same as Spokane.'),
 )))

ROUTES=[("Missoula, MT","I-90 · ~200 mi","Same day","$220–$340"),("Seattle, WA","I-90 · ~280 mi","1 day","$260–$390"),
 ("Portland, OR","US-395/I-84 · ~350 mi","1 day","$320–$460"),("Boise, ID","US-95 · ~420 mi","1 day","$370–$530"),
 ("Salt Lake City, UT","US-95/I-84 · ~700 mi","2 days","$500–$730"),("Sacramento, CA","US-97/I-5 · ~900 mi","2 days","$650–$920"),
 ("Denver, CO","I-90/I-25 · ~1,100 mi","3 days","$750–$1,050"),("Los Angeles, CA","US-95/I-15 · ~1,200 mi","3 days","$800–$1,150"),
 ("Minneapolis, MN","I-90/I-94 · ~1,400 mi","3 days","$900–$1,250"),("Chicago, IL","I-90 · ~1,800 mi","3–4 days","$1,050–$1,450")]
BODY.append(rate_table('Lanes &amp; Costs','Spokane Car Shipping Lanes and Estimated Costs',
 'The lanes Inland Northwest cars ride most, with estimated open-trailer ranges. Price your exact route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Spokane, open trailer, sedan that runs. SUVs and pickups land 10 to 25 percent higher, enclosed higher again. Pass closures and the carriers free on your dates settle the final figure.',
 prose(
  P('Spokane prices a little over Seattle on the lanes south and east. The carriers that reach it are the ones crossing the northern tier on 90. The Seattle lane is the busiest and waits on the pass in winter. The Boise and Salt Lake lanes ride 95 through the Palouse. The Montana lane runs daily, and the Midwest lanes ride 90 and 94 the whole way.'),
  P('A move timed to a summer start date at the base or the hospitals ships with the peak. The price follows. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Base, the Hospitals, the Universities, the Aluminum Mill, the Meter Maker, and the Lake Retirees',
 prose(
  L('Spokane relocates airmen, nurses, students, and the retirees who buy on the lakes. The base on the West Plains moves more people than anyone in the region.'),
  P('The tanker wing at the base west of the city rotates airmen on orders every summer. The survival school rotates instructors with them. Many families settle in Airway Heights, Cheney, and the north side. One car goes on the orders, and the other goes with us. Ship Guy is a private broker and not part of the base. The timing is laid out on the <a href="military-car-shipping.html">military</a> page.'),
  P('The two hospital systems downtown and on the South Hill are the largest in the Inland Northwest. They hire traveling nurses all year and bring in physicians around a closing date. The medical schools on the riverfront campus take residents each June. The private university by the river holds seven thousand students. The state university in Cheney holds twice that. The cars arrive in late August and go home in the middle of June. The state campus runs on quarters. The parent books the shipment, and an adult meets the truck at a campus lot.'),
  P('The aluminum mill in the Valley and the aerospace suppliers on the West Plains relocate engineers regularly. The meter maker headquartered in Liberty Lake hires from every state. The utility and the railroads downtown move staff on start dates. The fulfillment center on the West Plains rotates managers each fall. We supply the paperwork a reimbursed move needs.'),
  P('Retirees from California and the coast buy on Lake Coeur d’Alene and the lakes north of the city. They ship the second car behind the moving van. Families from Seattle buy in the Valley and on the north side for the price of a garage. One car rides the trailer while the other is driven. The interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Hoopfest, Bloomsday, the Fair, the Passes, the Windstorm, the Heat, and the Smoke',
 prose(
  L('Spokane runs on two weekends that close downtown and a pass that closes the coast lane. The fire season closes the sky.'),
  P('Hoopfest closes forty blocks of downtown for the last weekend of June. A quarter million people fill the streets. Bloomsday closes downtown and the Doomsday Hill for the first Sunday in May. A downtown handoff on either weekend moves to the Valley or to the week before. The lilac parade closes downtown for a May Saturday. The Labor Day food festival fills the riverfront park.'),
  P('The county fair fills the fairgrounds in the Valley for ten days in September. The basketball crowds fill the campus lots on winter nights, and the hockey crowds fill the arena. The auto show and the home shows fill the arena lots in spring. A handoff near any of them moves to the daytime.'),
  P('Winter brings forty-five inches of snow. The December 2008 storms dropped sixty in a month and collapsed roofs across the city. Snoqualmie Pass closes a few times each winter. The Seattle lane waits in Ellensburg or Spokane until it reopens. Fourth of July Pass and Lookout Pass close the Montana lane the same way. The Sunset Hill ices on winter mornings, and the carriers climb it after ten.'),
  P('The November 2015 windstorm was the worst in the city’s history. It took the power out for a week. The June 2021 heat dome hit one hundred nine degrees, and the carriers ran at dawn. The August 2023 fires burned hundreds of homes at Medical Lake and north of Elk. The smoke shut the sky for weeks. A fire closure on 90 or 2 reroutes the carrier, and we say so the moment it does.'),
 )+chips(["Downtown","Davenport District","Pacific Avenue","Riverfront Park","Browne’s Addition","Peaceful Valley","South Hill","Manito","Grand Boulevard","29th Avenue","Perry District","Lincoln Heights","Moran Prairie","Logan","Gonzaga","Hamilton","North Side","Shadle","Audubon","Hillyard","Five Mile","Wandermere","Mead","Colbert","West Plains","Airway Heights","Fairchild","Medical Lake","Cheney","Spokane Valley","Millwood","Liberty Lake","Deer Park","Post Falls","Coeur d’Alene","Hayden","Pullman"])
 +NOTE('Serving Spokane, the Valley, the West Plains, and the Idaho towns across the line. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Spokane?',
 prose(
  L('Most Inland Northwest cars ride an open trailer, and the lane table above is priced for one.'),
  P('An enclosed trailer keeps off the road salt, the pass gravel, and the smoke residue in fire season. The collectors who fill the summer car shows in the Valley book one. Retirees shipping a new car to the lake book one too.'),
  P('A commuter car or a ranch pickup goes open and arrives without a mark. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot at the mall or the arena, and the car at the far end. The report date or the closing picks the week.'),
  P('Say yes to the number, and the car is booked with a carrier already crossing on 90. The lot and the window arrive within hours. The driver examines the car with you at the handoff. Every blemish is marked on the Bill of Lading. Two signatures close it, and the delivery is judged against that sheet.'),
 )+ULI([
  "Personal belongings out of the cabin and the trunk",
  "Fuel somewhere near a quarter tank",
  "A dated photo of every panel and the odometer",
  "One working key passed to the driver, with any fault pointed out",
  "Aftermarket alarm switched off before the truck comes",
  "On the South Hill or downtown, meet the truck at the arena lots or on Grand",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Spokane Drivers Choose Ship Guy',
 prose(
  L('We catch the carriers crossing the northern tier on 90 before they reach the pass. We tell you when the pass is in play and plan around the smoke.'),
  P('Ship Guy’s brokerage authority and $75,000 surety bond are both listed with the FMCSA. Our office is on Pacific Avenue downtown.'),
  P('The coordinator who gives you the number is the one who closes the file at delivery. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Spokane','304 W Pacific Ave #477','Spokane, WA 99201','+15093695265','(509) 369-5265','PT',
 '304+W+Pacific+Ave+%23477,+Spokane,+WA+99201','Visit Us','Find Ship Guy in Spokane',
 'Our office is on Pacific Avenue downtown, two blocks from the Davenport.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4132.725956906152!2d-117.4168315!3d47.6553476!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x549e1994ff91c445%3A0xc583340529f93f57!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793103347683!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Spokane to Seattle or Boise?","Seattle runs two hundred sixty to three hundred ninety dollars for a sedan. That is about two hundred eighty miles west over the pass. Boise runs three hundred seventy to five hundred thirty, about four hundred twenty miles down 95. Missoula is a same-day lane and the lowest of the three. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street on the South Hill or in Browne’s Addition?","Usually not. The streets above 29th are steep, narrow, and shaded. Browne’s Addition is mansions on narrow streets under old trees. The driver meets you at the shopping center on Grand, at the arena lots, or on Division. The north side grids, the Valley, Five Mile, and the new subdivisions usually allow the curb."),
 ("Do you ship cars for airmen at Fairchild?","Yes, every summer. The tanker wing rotates airmen on orders, and the survival school rotates instructors with them. Many families settle in Airway Heights, Cheney, and the north side. The orders move one car, and the other one rides with us. Ship Guy is a private broker and not part of the base. Tell us the report date, and the window wraps around it."),
 ("Can you deliver on the Gonzaga or Eastern move-in date?","Yes. The private university by the river takes cars in late August and sends them home in May. The state university in Cheney runs on quarters. Its cars arrive in late September and go home in June. A parent arranges the car, and an adult over eighteen signs for it at a campus lot. The window is set by move-in day and follows it."),
 ("Does Hoopfest or Bloomsday affect my pickup?","Downtown, yes. Hoopfest closes forty blocks for the last weekend of June. Bloomsday closes downtown and the Doomsday Hill on the first Sunday in May. We move a downtown handoff those weekends to the Valley or to the days before. The South Hill, the north side, and the Valley run normally."),
 ("Can you ship a car to or from Spokane Valley, Cheney, or Coeur d’Alene?","Yes, and all three price the same as Spokane. The Valley rides the same carriers off the Sullivan and Argonne exits. The mall lots are the usual handoff. Cheney rides them fifteen minutes southwest on 90. Coeur d’Alene, Post Falls, and Hayden ride them across the Idaho line. The line adds no paperwork. Send the full address for a lake road."),
 ("What happens if Snoqualmie Pass closes on my pickup day?","The Seattle lane waits in Ellensburg or Spokane until the pass reopens, and the window stretches a day. You hear it from us before it does. The Boise, Montana, and Salt Lake lanes keep running, because they never touch the pass. A ground blizzard on the Palouse closes 195 the same way a few times a winter."),
 ("Can you ship a car that does not run from Spokane?","Yes. A winch carrier is booked, and the extra loading time is part of the number from the start. The mall lots on Division or the arena lots give the driver flat ground. Say whether the car rolls, steers, and brakes."),
 ("Does wildfire smoke or a fire closure affect my delivery?","Some summers, yes. The August 2023 fires closed roads west of the city and north of Elk for days. The smoke shut the sky for weeks. A fire closure on 90 or 2 reroutes the carrier. We tell you the moment the route changes. The smoke itself only changes the loading hour."),
 ("What do you need for a Spokane car shipping quote?","The pickup and the destination, with the side of the river or the town. Year, make, model. Whether it starts. Open or enclosed. The week around the report date or the closing. With those, the Spokane number is on its way the same day."),
]
BODY.append(faq_section(FAQ,'Spokane FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Spokane?','The form above has a number for you in about two minutes. Tell us the side of the river and the week, and a carrier already on 90 takes it.','+15093695265','(509) 369-5265','Get your free Spokane quote'))

build({
 'slug':'auto-transport-spokane-washington',
 'title':'Car Shipping in Spokane, WA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Spokane, WA, the hub of the Inland Northwest on Interstate 90. Fairchild PCS moves, hospital and university relocations, arena-lot handoffs for the South Hill and Browne’s Addition, curbside pickups on the north side and in the Valley, Coeur d’Alene across the line, Hoopfest, Snoqualmie Pass closures, and the smoke. Local office on Pacific Avenue downtown. Free quote.',
 'h1':'Car Shipping in<br>Spokane, <span class="accent">Washington</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Inland Northwest, planned around 90, the pass, the base calendar, the hill, and the fire season.',
 'tel':'+15093695265','disp':'(509) 369-5265','brand':'Spokane','keyword':'car shipping in spokane',
 'localterms':['spokane','inland northwest','interstate 90','north freeway','pacific avenue','davenport','airway heights','cheney','the valley','liberty lake','coeur d’alene','maple','division','hamilton','sprague','argonne','us 2','sunset hill','airport','us 195','palouse','wandermere','river','south hill','north side','idaho line','base','hospitals','universities','hoopfest','passes','smoke','seattle','boise','montana','missoula','portland','salt lake city','sacramento','denver','los angeles','midwest','browne’s addition','campus','sullivan','cascades','snoqualmie pass','395','the y','deer park','pullman','fairchild','trent avenue','one-way','riverside','main','monroe street','ash','grand boulevard','bernard','pines','falls','truck stops','broadway','west plains','mall','arena','toll','railroad','prairie','brick','hotel district','mansions','peaceful valley','29th','shopping center','perry district','student rentals','lincoln heights','moran prairie','francis','shadle','audubon','hillyard','logan','five mile','mead','havana street','gated','post falls','hayden','state line','paperwork','state university','minneapolis','chicago','northern tier','airmen','nurses','students','retirees','lakes','tanker wing','survival school','orders','traveling nurses','physicians','medical schools','residents','seven thousand','quarters','aluminum mill','aerospace suppliers','meter maker','utility','railroads','fulfillment center','california','bloomsday','doomsday hill','quarter million','lilac parade','labor day','food festival','county fair','fairgrounds','basketball','hockey','auto show','home shows','forty-five inches','december 2008','sixty','roofs','ellensburg','fourth of july pass','lookout pass','november 2015 windstorm','june 2021 heat dome','one hundred nine','august 2023 fires','medical lake','elk','car shows','bill of lading','fmcsa','surety bond','manito','millwood','colbert','gonzaga','riverfront park'],
}, BODY, FAQ)
