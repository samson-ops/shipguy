import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Sioux City, Iowa','Car shipping in Siouxland, where three states meet on the Missouri and Interstate 29 runs the river',
 ['Car shipping in Sioux City runs off Interstate 29, the river road between Omaha and Sioux Falls. Ship Guy is a licensed auto transport broker with an office on 4th Street downtown.',
  'We arrange vetted carriers across Siouxland, from Le Mars to Sergeant Bluff and over the river. We own none of the trucks.',
  'Interstate 29 follows the Missouri along the west side. US 20 crosses the city on four lanes toward Fort Dodge and Dubuque. US 75 runs north to Le Mars, and US 77 crosses the river to Nebraska. Hamilton Boulevard, Gordon Drive, and Sergeant Road carry the city.',
  'This page covers 29, US 20, downtown, the Northside, Morningside, and the towns across the river. It also covers the packing plants, the hospitals, the wing, the concert, the flood, and the lanes.'],
 'Sioux City at a glance',
 ['Most pickups happen within 2 to 3 days. The carriers between Omaha and Sioux Falls pass the city on 29. The Des Moines trucks come across on 20. A flexible date puts you on the next one.',
  'Omaha and Sioux Falls are ninety minutes. Des Moines, Minneapolis, and Kansas City are a same-day haul. Chicago and St. Louis take a day. Denver and Dallas take two, and the coasts take three to five.'],
 'Tell us the side of the river. Downtown and the Northside grids need a meeting spot. Morningside, the Southern Hills, and the new subdivisions usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 29, US 20, US 75, US 77, Hamilton Boulevard, and the Bridges',
 prose(
  L('Sioux City sits on the one interstate in northwest Iowa. The carriers that run it pass the city on every trip up the river.'),
  P('Interstate 29 runs north and south along the Missouri on the west side of downtown. The exits at Hamilton, Floyd, Gordon Drive, and Singing Hills serve the city. The Sergeant Bluff exit serves the airport. Every carrier between Omaha and Sioux Falls passes all of them. Interstate 129 is the spur across the river to South Sioux City and the packing plant.'),
  P('US 20 crosses the city from the river east to Fort Dodge and Dubuque on four lanes. It is the road to Des Moines. US 75 runs north through the city to Le Mars and the ice cream plant. US 77 crosses the river bridge to Nebraska. Highway 12 runs north along the river into the Loess Hills and South Dakota.'),
  P('Hamilton Boulevard runs from downtown north through the west side. Gordon Drive is the old US 20 strip across the south side. Sergeant Road and Lakeport Street carry the mall and the Southern Hills. Morningside Avenue runs the east side past the college. Floyd Boulevard runs north past Leeds. Outer Drive rings the north side where the new subdivisions sit.'),
  P('The carriers come off 29 at Hamilton and Gordon Drive. The mall on Sergeant Road, the riverfront arena, and the casino downtown have the usual meeting lots. No road in Siouxland charges a toll.'),
  P('Our office is on 4th Street downtown, a few blocks from the riverfront and the casino.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Northside, Morningside, Leeds, the Southern Hills, the North Side, and Across the River',
 prose(
  L('Sioux City is an old packing town on the bluffs. The newer streets climb away from the river in every direction.'),
  P('Downtown is a grid of old brick blocks between 29 and the bluff. It runs around 4th Street, the courthouse, and the casino. The streets are narrow, and the historic district on 4th is tight. The driver meets you at the riverfront lots, at the arena, or at the casino garage. The Northside grids above downtown along Pierce and Jackson are old houses on narrow streets. The handoff moves to Hamilton.'),
  P('Morningside on the east side is the college, the old grids, and the streets off Morningside Avenue. The curb works on most blocks. Leeds to the northeast along Floyd is an old neighborhood with a main street of its own. The west side along Hamilton and Perry Creek is older grids. A lot on Hamilton works for a handoff.'),
  P('The Southern Hills along Sergeant Road is the mall, the hospital campus, and newer subdivisions. The streets are wide, and the truck reaches the curb. Sunnybrook to the east is the newest growth, and the streets are not on every map yet. The north side off Outer Drive and Indian Hills is the same. Send the full address.'),
  P('Sergeant Bluff to the south has the airport, the refueling wing, and wide subdivision streets. South Sioux City across the river in Nebraska has the packing plant and older grids. The driver meets you on Dakota Avenue. Dakota Dunes in South Dakota is a golf community with wide streets and no state income tax. Le Mars up 75 is the ice cream town. All of them price the same as Sioux City.'),
 )))

ROUTES=[("Sioux Falls, SD","I-29 · ~90 mi","Same day","$150–$240"),("Omaha, NE","I-29 · ~100 mi","Same day","$160–$260"),
 ("Des Moines, IA","US-20/I-35 · ~200 mi","Same day","$220–$340"),("Minneapolis, MN","I-29/I-90/I-35 · ~280 mi","1 day","$270–$400"),
 ("Kansas City, MO","I-29 · ~280 mi","1 day","$270–$400"),("Chicago, IL","US-20/I-80 · ~490 mi","1 day","$410–$590"),
 ("St. Louis, MO","I-29/I-70 · ~530 mi","1–2 days","$440–$630"),("Denver, CO","I-29/I-80 · ~650 mi","2 days","$490–$710"),
 ("Dallas, TX","I-29/I-35 · ~790 mi","2 days","$560–$820"),("Phoenix, AZ","I-80/I-25/I-40 · ~1,450 mi","3–4 days","$950–$1,350")]
BODY.append(rate_table('Lanes &amp; Costs','Sioux City Car Shipping Lanes and Estimated Costs',
 'The lanes Siouxland cars ride most, with estimated open-trailer ranges. Your own route gets its number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates out of Sioux City, sedan that starts and drives, open trailer. Figure 10 to 25 percent more for an SUV or a pickup and more for enclosed. A ground blizzard or a flood on 29 moves everything. The trucks on the river road that week fix the final figure.',
 prose(
  P('Sioux City prices a little over Omaha on most lanes. The carriers that reach it are the ones running 29 between Omaha and Sioux Falls. Those two lanes run daily and price the lowest. The Des Moines and Chicago lanes ride 20 and 80 and run most days. The Dallas and Denver lanes fill through Omaha.'),
  P('A flexible date matters more here than in Des Moines. Fewer carriers base themselves in the corner of the state. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Packing Plants, the Hospitals, the Refueling Wing, the Fertilizer Plant, the Colleges, and the Ice Cream Town',
 prose(
  L('Sioux City relocates plant managers, nurses, airmen, and students. The two packing plants move more people than anyone in Siouxland.'),
  P('The beef plant across the river in Dakota City is one of the largest in the country. The pork plant on the south side is another. They move managers, veterinarians, and engineers in from every state on short notice. The fertilizer plant at Port Neal and the power plant beside it relocate engineers on turnaround schedules. We supply the paperwork a reimbursed move needs.'),
  P('Both hospital systems hire traveling nurses all year and bring in physicians around a closing date. The children’s clinics and the specialty practices recruit from Omaha and Minneapolis. The refueling wing at the airport rotates airmen on orders. The government pays for one car, and the second rides with us. Ship Guy is a private broker and has no tie to the wing. See the <a href="military-car-shipping.html">military</a> page for the timing.'),
  P('The two colleges in Morningside and on the north side bring cars in each August. The community college does the same. A parent arranges the shipment, and someone over eighteen signs at a campus lot. The state university in Vermillion sits forty minutes north and runs the same calendar.'),
  P('The ice cream maker in Le Mars moves managers in on its own calendar. Families from Omaha and Sioux Falls buy in Sunnybrook and Dakota Dunes on closing dates. One car rides the trailer while the family drives the other. The interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Saturday in the Park, the Rodeo, the 2019 Flood, the Ground Blizzards, and the Plains Wind',
 prose(
  L('Sioux City runs on a free concert in July and a river that closes 29 some springs. The wind never stops.'),
  P('Saturday in the Park fills Grandview Park and the Northside streets on the first Saturday in July. Tens of thousands come for the free concert, and the streets around the park close. A pickup on the Northside that day moves to the Southern Hills. The river festival the same month fills the riverfront. The rodeo in Sergeant Bluff fills the fairgrounds roads.'),
  P('The hockey team fills the arena lots on the riverfront from October through April. The baseball team fills the ballpark on the south side in summer. The ice cream days in Le Mars fill 75 on a June weekend. A handoff near any of them moves to the daytime.'),
  P('The Missouri floods. The 2019 flood closed 29 south of the city for most of the spring. The carriers ran 75 and 20 around it. The 2011 flood did the same for the summer. The Floyd River flooded the north side in 1953 and still rises in a wet April. A pickup on the low ground moves up the bluff, and we tell you when 29 closes.'),
  P('Winter is the ground blizzard. The wind blows the snow across the open ground. Interstate 29 closes between here and Omaha a few times a winter. The carriers wait in Sioux Falls or Omaha until the road reopens. A winter pickup can lose a day or two. The wind runs all year, and a tall trailer slows on 29 in a crosswind. The sirens sound a few times each spring, and summer heat moves the loading hour to the morning.'),
 )+chips(["Downtown","4th Street","Pearl Street","Riverfront","Arena","Casino","Northside","Pierce Street","Jackson Street","Grandview Park","West Side","Hamilton","Perry Creek","Morningside","Morningside Avenue","Leeds","Floyd","Greenville","Gordon Drive","Southern Hills","Sergeant Road","Lakeport","Sunnybrook","Indian Hills","Outer Drive","Country Club","Sergeant Bluff","Airport","Port Neal","South Sioux City","Dakota City","Dakota Dunes","North Sioux City","Le Mars","Hinton","Vermillion"])
 +NOTE('Serving Sioux City and all of Siouxland across the three states, bluff street or subdivision. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Sioux City?',
 prose(
  L('Most cars leave Siouxland on an open trailer, and the lane prices are built around one.'),
  P('An enclosed trailer keeps the salt, the gravel, and the wind-blown grit off a car. Collectors in Dakota Dunes and on the north side book one for the show cars. Families sending a car to a student from far away book one too.'),
  P('A commuter car or a ranch truck is fine open and comes off as it went on. Compare the two on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot at the mall or on the riverfront, and the car at the other end. The next carrier up the river road picks the week.'),
  P('Accept the price, and the car joins a carrier already running 29. Once the truck is set, you get the lot and the window. At pickup the driver and you inspect the car and note every blemish on the Bill of Lading. Both of you sign it, and delivery is measured against it.'),
 )+ULI([
  "Personal items out, trunk and glovebox included",
  "About a quarter tank of fuel",
  "Photos of every side and the odometer before the truck arrives",
  "One working key for the driver, and a word about any fault",
  "Aftermarket alarm switched off",
  "Downtown or on the Northside, meet the truck at the riverfront lots or on Hamilton",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Sioux City Drivers Choose Ship Guy',
 prose(
  L('We put your car on the carriers already running the river road. We tell you the real window and plan around the wind and the water.'),
  P('Ship Guy’s FMCSA license and $75,000 surety bond are both public record. Our office is on 4th Street downtown.'),
  P('You deal with one person from the first quote through delivery. Open, enclosed, and expedited transport are described on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Sioux City','700 4th St STE 479','Sioux City, IA 51101','+17124124080','(712) 412-4080','CT',
 '700+4th+St+STE+479,+Sioux+City,+IA+51101','Visit Us','Find Ship Guy in Sioux City',
 'Our office is on 4th Street downtown, a few blocks from the riverfront and the casino.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4523.911268339019!2d-96.4016631!3d42.4940394!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x878dfd2d017aeca5%3A0x436ff2cf61c39f57!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025225303!5m2!1sen!2sus', alt=True))

FAQ=[
 ("Why does a Sioux City pickup take two to three days?","Because the carriers that reach the corner of the state are the ones running 29. A pickup here joins a truck already making that run. That takes two to three days in a normal week. A flexible date range puts you on the next one. The Des Moines and Chicago trucks come across on 20 most days."),
 ("How much does it cost to ship a car from Sioux City to Omaha or Minneapolis?","Omaha runs one hundred sixty to two hundred sixty dollars for a sedan. That is about one hundred miles down 29. Minneapolis runs two hundred seventy to four hundred, about two hundred eighty miles on 29, 90, and 35. Sioux Falls is ninety minutes away and costs the least. Figure 10 to 25 percent more for an SUV or a pickup."),
 ("Can the carrier come to my street downtown or on the Northside?","Usually not. Downtown is a tight grid of old brick blocks, and the Northside streets above it are narrow. The driver meets you at the riverfront lots, at the arena, or on Hamilton. Morningside, the Southern Hills, and the new subdivisions off Outer Drive usually allow the curb."),
 ("Do you ship cars for people relocating to the packing plants or the hospitals?","Yes, all year. The beef plant and the pork plant move managers, veterinarians, and engineers in on short notice. The hospital systems bring in nurses and physicians every month. Many ship a second car behind the move. The handoff works at the mall lot on Sergeant Road or the riverfront. We provide the paperwork a reimbursed move needs."),
 ("Can you ship a car to or from South Sioux City, Dakota Dunes, or Le Mars?","Yes, and all three price the same as Sioux City. South Sioux City rides the same carriers across the 129 bridge, and the handoff works on Dakota Avenue. Dakota Dunes rides them off 29 at the state line. Le Mars rides them up 75. Send the full address for a new subdivision in Sunnybrook or the Dunes."),
 ("Does Saturday in the Park affect my pickup?","On the Northside, yes. The free concert fills Grandview Park and the streets around it on the first Saturday in July. We move a pickup near the park that day to the Southern Hills. The rest of the city runs normally."),
 ("What happens if a ground blizzard or the river closes 29 on my pickup day?","The carriers wait in Sioux Falls or Omaha until 29 reopens. A winter pickup can slip a day or two, and we tell you before it happens. The Missouri closed 29 south of the city for most of 2019. When that happens, the carriers run 75 and 20 around it, and the window stretches a day. A pickup on the low ground moves up the bluff."),
 ("Can you ship a car that does not run from Sioux City?","Yes. A winch truck is sent, and the loading time is part of the first number. The mall lot on Sergeant Road or the arena lot gives the driver level ground. Say whether the car rolls, steers, and brakes."),
 ("Do you ship cars for airmen at the refueling wing?","Yes. The wing at the airport in Sergeant Bluff rotates airmen on orders. Many families settle in Sergeant Bluff and the Southern Hills. The orders pay for one car, and the second one ships with us. Ship Guy is a private broker with no link to the wing. Give us the report date, and the window is set around it."),
 ("What do you need for a Sioux City car shipping quote?","The pickup and the destination, with the side of the river or the town. Year, make, model. Whether it starts. Open or enclosed. A range of dates instead of one day, since the trucks come up the river on a run. Five answers, and the Sioux City number is on its way the same day."),
]
BODY.append(faq_section(FAQ,'Sioux City FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Sioux City?','Two minutes on the form above and the lane has a number. Tell us the side of the river and a range of dates. The next carrier up 29 takes it.','+17124124080','(712) 412-4080','Get your free Sioux City quote'))

build({
 'slug':'auto-transport-sioux-city-iowa',
 'title':'Car Shipping in Sioux City, IA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Sioux City, IA and Siouxland, where three states meet on the Missouri and Interstate 29 runs the river. Honest two-to-three-day pickups, packing-plant and hospital relocations, downtown and Northside meeting spots, Morningside and Southern Hills curbside pickups, Dakota Dunes and Le Mars, Saturday in the Park, the 2019 flood, and the ground blizzards. Local office on 4th Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Sioux City, <span class="accent">Iowa</span>',
 'lede':'Open, enclosed, and expedited auto transport across Siouxland, planned around 29, US 20, the river stage, and the plains wind.',
 'tel':'+17124124080','disp':'(712) 412-4080','brand':'Sioux City','keyword':'car shipping in sioux city',
 'localterms':['sioux city','siouxland','missouri','interstate 29','omaha','sioux falls','us 20','fort dodge','dubuque','us 75','le mars','us 77','interstate 129','highway 12','loess hills','hamilton','gordon drive','sergeant road','lakeport','morningside avenue','floyd','outer drive','singing hills','downtown','4th street','courthouse','casino','historic district','riverfront','arena','northside','pierce','jackson','grandview park','west side','perry creek','morningside','college','leeds','southern hills','mall','hospital campus','sunnybrook','indian hills','sergeant bluff','airport','refueling wing','south sioux city','dakota avenue','dakota city','dakota dunes','golf','no state income tax','vermillion','packing plants','beef plant','pork plant','veterinarians','fertilizer plant','port neal','power plant','hospital systems','nurses','physicians','airmen','orders','colleges','community college','ice cream','saturday in the park','concert','river festival','rodeo','hockey','baseball','2019 flood','2011','floyd river','1953','ground blizzard','wind','crosswind','sirens','heat','des moines','minneapolis','kansas city','chicago','st. louis','denver','dallas','phoenix'],
}, BODY, FAQ)
