import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Shreveport, Louisiana','Car shipping in the ArkLaTex, where Interstate 20 crosses the Red River three hours from Dallas',
 ['Car shipping in Shreveport runs off Interstate 20, which crosses the river into Bossier City. Ship Guy is a licensed auto transport broker with an office on Crockett Street downtown.',
  'We arrange vetted carriers across Caddo and Bossier Parishes, from Blanchard to Haughton and down to Keithville. The trucks are not ours.',
  'Interstate 20 is the Dallas and Jackson road, straight through downtown. Interstate 49 arrives from the south and picks up again north of the loop. Interstate 220 loops the north side through Bossier. Youree Drive, Line Avenue, Mansfield Road, and Airline Drive carry the two cities.',
  'This page covers 20, 49, the loop, downtown, the Highlands, the south side, Bossier, and the lake. It also covers the base, the hospitals, the casinos, the State Fair, the 2021 freeze, and the lanes.'],
 'Shreveport at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between Dallas and Atlanta passes the city on 20. The Houston trucks come up 49 and 59.',
  'Dallas, Fort Worth, Little Rock, and Jackson are all a same-day haul. Houston, Baton Rouge, and New Orleans are the same. Memphis and Atlanta take a day. Phoenix and the coasts take three to five.'],
 'Tell us the side of the river. Downtown and the Highlands need a meeting spot. The south side, Bossier, and the subdivisions off Ellerbe Road usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 20, Interstate 49, Interstate 220, the Inner Loop, Youree Drive, and the Bridges',
 prose(
  L('Shreveport is the first Louisiana city a Dallas carrier reaches. Interstate 20 runs straight through the middle of it.'),
  P('Interstate 20 crosses the city from the Texas line at Greenwood to the river and into Bossier City. The exits at Jewella, Hearne, Line, Market, and Spring cover the core. Every carrier between Dallas and Jackson passes all of them. Interstate 49 arrives from Alexandria and ends at 20 downtown. It picks up again north of the loop toward Texarkana. The gap through the city runs on 220 and the loop.'),
  P('Interstate 220 is the north loop from 20 at the west side across the river to Bossier. The Inner Loop is Highway 3132, the south loop from 20 to 49. Bert Kouns is the outer loop across the south side. US 71 and 171 run south toward Alexandria and Lake Charles. US 79 and 80 run west to Marshall and the Texas line. Highway 1 runs north to the lake and the oil towns.'),
  P('Youree Drive is Highway 1 south of downtown, the main retail strip past the mall. Line Avenue runs through the Highlands. Mansfield Road is 171 through the southwest. Kings Highway crosses the hospital district. Across the river, Barksdale Boulevard, Airline Drive, and Benton Road carry Bossier City. Clyde Fant Parkway follows the riverfront past the casinos.'),
  P('The carriers come off 20 at Line and Spring, and off the loop at Youree and Mansfield. The mall on Youree, the fairgrounds, and the casinos on the riverfront have the usual meeting lots. No road in either parish charges a toll. The bridges over the river are free.'),
  P('Our office is on Crockett Street downtown, a few blocks from the courthouse and the riverfront.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Highlands, Broadmoor, the South Side, Cross Lake, Bossier City, and the Towns Around',
 prose(
  L('Shreveport is an old cotton and oil town on a bluff. Bossier City grows faster across the river.'),
  P('Downtown is the courthouse, the office towers, and the casinos on a grid between 20 and the river. The streets are narrow and one-way, and the casino lots fill on weekends. The driver meets you at the riverfront lots or at the fairgrounds. Highland and South Highlands south of downtown are historic districts. Big houses sit on narrow streets under old oaks. The handoff moves to Line Avenue or to the hospital lots on Kings Highway.'),
  P('Broadmoor, Spring Lake, and Pierremont in the middle of the city are postwar grids with wide streets. The curb works on most blocks. The south side along Youree, Ellerbe Road, and Southern Hills is the growth side. The subdivisions run out to the loop. The truck reaches the curb. Cedar Grove and the streets off Mansfield are older grids, and the handoff moves to the main road.'),
  P('Cross Lake on the northwest is a ring of lake homes on narrow drives. The driver meets you on Lakeshore Drive. Blanchard and Mooringsport beyond it are small towns with lots on Highway 1. The west side along Jewella and Hearne is older grids and warehouses, and a lot off 20 works.'),
  P('Bossier City across the river is its own city, with the base and the casinos. Its subdivisions run north up Benton Road and Airline Drive. The streets are wide, and the curb works. Haughton and Benton beyond it are the same. Keithville and Stonewall to the south are country towns with lots on 171. All of them price the same as Shreveport, and so does Minden to the east.'),
 )))

ROUTES=[("Dallas, TX","I-20 · ~190 mi","Same day","$220–$330"),("Fort Worth, TX","I-20 · ~220 mi","Same day","$230–$350"),
 ("Little Rock, AR","I-49/I-30 · ~220 mi","Same day","$230–$350"),("Jackson, MS","I-20 · ~220 mi","Same day","$230–$350"),
 ("Houston, TX","US-59 · ~245 mi","Same day","$240–$360"),("Baton Rouge, LA","I-49/I-10 · ~250 mi","Same day","$250–$370"),
 ("New Orleans, LA","I-49/I-10 · ~330 mi","1 day","$300–$440"),("Memphis, TN","I-30/I-40 · ~350 mi","1 day","$320–$460"),
 ("Atlanta, GA","I-20 · ~560 mi","1–2 days","$450–$640"),("Phoenix, AZ","I-20/I-10 · ~1,200 mi","3 days","$850–$1,150")]
BODY.append(rate_table('Lanes &amp; Costs','Shreveport Car Shipping Lanes and Estimated Costs',
 'The lanes ArkLaTex cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates out of Shreveport for a sedan that starts, open trailer. Count on 10 to 25 percent more for an SUV or a pickup and more for enclosed. The season and the carriers free on your dates fix the final price.',
 prose(
  P('Shreveport prices on the Dallas pool, not the New Orleans one. The Dallas and Fort Worth lanes run daily and price the lowest per mile in the state. The Atlanta and Phoenix lanes ride 20 end to end and pick the car up without a detour. The Baton Rouge and New Orleans lanes ride 49 and run lighter.'),
  P('A storm on the Gulf coast moves the southern lanes for a week. The Dallas lane never notices. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Base, the Hospitals, the Casinos, the Medical School, the Cyber Campus, and the Oil Patch',
 prose(
  L('Shreveport relocates airmen, nurses, casino managers, and oilfield crews. The base across the river moves more people than anyone.'),
  P('The bomber base in Bossier City is the largest employer in the region. It is also home to the global strike command. Airmen and families rotate on orders all year, with a summer peak. They settle from Haughton to the south side. The orders move one car, and the second one moves with us. Ship Guy is a private broker with no link to the base. Timing around a report date is on the <a href="military-car-shipping.html">military</a> page.'),
  P('The hospital system on Kings Highway and Greenwood Road is the largest private employer in the city. It brings in nurses on contracts all year, and the medical school adds residents each June. Physicians arrive with a closing date and a second car. We supply the paperwork a reimbursed move needs.'),
  P('The six casinos on the river hire managers from Las Vegas and Mississippi on short notice. The cyber campus in Bossier moves engineers in on contract schedules. The refinery, the steel mill at the port, and the west-side warehouse relocate staff the same way. The oil patch to the north still sends crews through on the drilling calendar.'),
  P('The three colleges bring cars in each August, and a parent ships the car. An adult signs at a campus lot. Families leaving for Dallas and Houston ship the second car ahead of the move. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The State Fair, Mardi Gras, Mudbug Madness, the Bowl Game, the Freeze, and the Tornadoes',
 prose(
  L('Shreveport runs on a fall state fair, two big Mardi Gras parades, and every kind of storm.'),
  P('The State Fair of Louisiana fills the fairgrounds for three weeks from late October. Greenwood Road and Hearne gridlock every evening, and the fairgrounds lots are gone. A pickup near the fairgrounds those weeks moves to the south side. The bowl game in December fills the stadium next door for a day.'),
  P('The Mardi Gras parades roll on the Saturdays before Fat Tuesday. The two big ones run Clyde Fant Parkway and the Shreveport-Barksdale bridge. The riverfront closes on both sides. Mudbug Madness fills downtown for the Memorial Day weekend, and the arts festival does the same in October. A downtown handoff on any of those days moves to the fairgrounds or to Youree.'),
  P('The 2021 freeze shut the city for a week. The pipes burst, the water system failed, and the carriers parked on 20 for three days. Ice returns most winters for a day or two, and the bridges glaze first. Snow is rare. Summer heat passes one hundred degrees for weeks, and the loading hour moves to the morning.'),
  P('Tornadoes cross the ArkLaTex every spring and some winters. The 2022 storm crossed Keithville south of the city in December. The sirens sound a few times each spring. A pickup waits for the warning to lift. The Red River flooded the riverfront and the parkway in 2015. Hurricane remnants reach the city a day after landfall, as Laura did in 2020. They take the power down for days.'),
 )+chips(["Downtown","Courthouse","Riverfront","Casinos","Red River District","Highland","South Highlands","Line Avenue","Kings Highway","Fairfield","Broadmoor","Spring Lake","Pierremont","Youree Drive","Mall","Shreve Island","South Side","Ellerbe Road","Southern Hills","Cedar Grove","Mansfield Road","West Side","Jewella","Hearne","Fairgrounds","Cross Lake","Lakeshore","Blanchard","Greenwood","Bossier City","Barksdale","Airline Drive","Benton Road","Haughton","Benton","Keithville","Stonewall","Minden"])
 +NOTE('Serving Shreveport, Bossier City, and all of Caddo and Bossier Parishes, lake drive or subdivision. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Shreveport?',
 prose(
  L('Nine cars in ten leave the ArkLaTex on an open trailer. The table above is priced that way.'),
  P('An enclosed trailer shuts out the rain, the gravel, and the summer sun. The collectors in South Highlands book one for the show cars. Airmen shipping a new car to the next base book one too.'),
  P('A daily driver or an oilfield truck rides open and arrives none the worse. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the trade-off.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the mall or the fairgrounds, and a car at the far end. The report date sets the week.'),
  P('Approve the price, and we assign a carrier already running 20 between Dallas and Jackson. The lot and the window reach you within hours. At pickup, the driver inspects the car with you and notes every mark on a Bill of Lading. You both sign, and the delivery is compared against it.'),
 )+ULI([
  "Empty the car of anything personal, trunk included",
  "Fuel at a quarter tank or less",
  "Photos of every panel and the odometer, dated",
  "A working key for the driver and a word about any fault",
  "Switch off any aftermarket alarm",
  "In the Highlands or downtown, meet the truck on Line Avenue or at the riverfront lots",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Shreveport Drivers Choose Ship Guy',
 prose(
  L('We put your car on the Dallas carriers as they cross the state line. We plan around the base calendar, the fair, and the freeze.'),
  P('Ship Guy is an active FMCSA broker backed by a $75,000 surety bond. The federal register lists both. Our office is on Crockett Street downtown.'),
  P('The coordinator who quotes the move is the one who sees it through. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Shreveport','717 Crockett St #473A','Shreveport, LA 71101','+13185836904','(318) 583-6904','CT',
 '717+Crockett+St+%23473A,+Shreveport,+LA+71101','Visit Us','Find Ship Guy in Shreveport',
 'Our office is on Crockett Street downtown, a few blocks from the courthouse and the riverfront.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5174.003147738847!2d-93.7503217!3d32.509172500000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8636cd17d9d5cc11%3A0xc6450d34b0434d16!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793024994215!5m2!1sen!2sus', alt=True))

FAQ=[
 ("Do you ship cars for airmen at Barksdale?","Yes, all year and especially in summer. Airmen and families arrive on orders and settle from Haughton to the south side of Shreveport. The orders cover one car, and we move the second. Base housing sits behind a gate. The driver meets you outside it or at a lot on Airline Drive. Ship Guy is a private broker with no link to the base. Give us the report date, and the window is built around it."),
 ("How much does it cost to ship a car from Shreveport to Dallas or Houston?","Dallas runs two hundred twenty to three hundred thirty dollars for a sedan. That is about one hundred ninety miles down 20. Houston runs two hundred forty to three hundred sixty, about two hundred forty-five miles down 59. Fort Worth, Little Rock, and Jackson price about the same as Houston. An SUV or pickup adds 10 to 25 percent. All of them run daily."),
 ("Can the carrier come to my street downtown or in the Highlands?","Usually not. Downtown is narrow one-way streets, and the Highlands have big oaks over narrow streets. The driver meets you at the riverfront lots, on Line Avenue, or at the hospital lots. The south side, Bossier City, and the subdivisions off Ellerbe Road usually allow the curb."),
 ("Does the State Fair affect my pickup?","Near the fairgrounds, yes. The fair runs three weeks from late October, and Greenwood Road and Hearne gridlock every evening. We move a pickup near the fairgrounds to the south side or to Youree. The rest of the city runs normally, and so does Bossier."),
 ("Do you ship cars for people relocating to the hospitals or the casinos?","Yes, every month. The hospital system brings in nurses, residents, and physicians all year. The casinos hire managers from Las Vegas and Mississippi on short notice. The cyber campus in Bossier moves engineers on contract schedules. Many ship a second car behind the move. The handoff works at the mall lot or the riverfront. We provide the paperwork a reimbursed move needs."),
 ("Can you ship a car to or from Bossier City, Haughton, or Minden?","Yes, and all three price the same as Shreveport. Bossier City rides the same carriers off 20 and 220. The handoff works at a lot on Airline Drive. Haughton rides them off 20 to the east, and Minden rides them off 20 at Highway 371. Send the full address for a new subdivision up Benton Road."),
 ("What happens if ice or a tornado warning hits on my pickup day?","Ice glazes the bridges first, and the carriers park on 20 until the sand trucks finish. The 2021 freeze cost a week, but a normal ice day costs one. We call before it happens. A tornado warning holds the loading until it expires, and the sirens are a spring routine here. The driver waits and nearly always finishes the same day."),
 ("Can you ship a car that does not run from Shreveport?","Yes. A carrier with a winch is sent, and the loading time is in the quote from the start. The mall lot on Youree or the fairgrounds lot gives the driver room to winch. Tell us if it rolls, if it steers, and if the brakes hold."),
 ("Can you time delivery to a student move at the colleges?","Yes. The three colleges fill with cars each August and empty each May. A parent usually books, and an adult signs for the car at a campus lot. We pin the delivery to the move-in date."),
 ("What do you need for a Shreveport car shipping quote?","Both addresses, with the side of the river here. Year, make, and model. Whether it starts. Open or enclosed. The week around the report date. That covers it, and the Shreveport number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Shreveport FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Shreveport?','The form above prices the lane in two minutes. Tell us the side of the river and the week, and the next Dallas carrier through takes it.','+13185836904','(318) 583-6904','Get your free Shreveport quote'))

build({
 'slug':'auto-transport-shreveport-louisiana',
 'title':'Car Shipping in Shreveport, LA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Shreveport, LA, where Interstate 20 crosses the Red River three hours from Dallas. Barksdale moves, hospital and casino relocations, downtown and Highlands meeting spots, south side and Bossier City curbside pickups, the State Fair, Mardi Gras on the parkway, the 2021 freeze, and the tornado season. Local office on Crockett Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Shreveport, <span class="accent">Louisiana</span>',
 'lede':'Open, enclosed, and expedited auto transport across Caddo and Bossier Parishes, planned around 20, 49, the base calendar, the fair, and the freeze.',
 'tel':'+13185836904','disp':'(318) 583-6904','brand':'Shreveport','keyword':'car shipping in shreveport',
 'localterms':['shreveport','arklatex','red river','interstate 20','interstate 49','interstate 220','inner loop','3132','bert kouns','us 71','us 171','us 79','us 80','highway 1','youree','line avenue','mansfield','kings highway','jewella','hearne','market','spring','barksdale boulevard','airline drive','benton road','clyde fant','greenwood','downtown','courthouse','riverfront','casinos','highland','south highlands','oaks','broadmoor','spring lake','pierremont','south side','ellerbe','southern hills','cedar grove','cross lake','lakeshore','blanchard','mooringsport','west side','warehouses','bossier city','base','haughton','benton','keithville','stonewall','minden','bomber','global strike','airmen','orders','gated','hospital system','nurses','medical school','residents','casinos','cyber campus','refinery','steel mill','port','warehouse','oil patch','colleges','state fair','fairgrounds','bowl game','stadium','mardi gras','parades','mudbug madness','arts festival','2021 freeze','pipes','ice','heat','tornadoes','2022','sirens','2015','laura','2020','dallas','fort worth','little rock','jackson','houston','baton rouge','new orleans','memphis','atlanta','phoenix','texarkana','alexandria','marshall','lake charles'],
}, BODY, FAQ)
