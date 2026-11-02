import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("3–6 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Great Falls, Montana','Car shipping on the Missouri, where Interstate 15 meets the base, the Hi-Line, and the wind',
 ['Car shipping in Great Falls rides Interstate 15, the road between the Canadian border and Salt Lake City. Ship Guy is a licensed auto transport broker with an office on Central Avenue downtown.',
  'We arrange vetted carriers across Great Falls and the Golden Triangle, from downtown to Malmstrom and Vaughn. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 15 passes the west side of the city between Helena and Shelby. US 87 leaves southeast for Lewistown and Billings and northeast for Havre and the Hi-Line. US 89 runs northwest to Choteau and Glacier. Highway 200 climbs Rogers Pass to Missoula.',
  'This page covers 15, 87, 89, 200, Tenth Avenue South, the river, the old neighborhoods, and the base. It also covers the hospital, the refinery, the Guard wing, the fair, the wind, and the canyon closures.'],
 'Great Falls at a glance',
 ['Most pickups happen within 3 to 6 days. Montana is a pass-through market. A carrier on 15 or 90 adds a Great Falls stop when the load lines up. A week of dates is the biggest help you can give us.',
  'Missoula and Billings are a day on the truck. Spokane takes one to two. Salt Lake City, Bismarck, Boise, and Seattle take two. Denver and Fargo take two to three, and Phoenix takes three to four.'],
 'Tell us the neighborhood and the nearest highway. The Lower North Side, downtown, and the base housing meet the truck at a lot or the gate. The West Side, Riverview, the East Side, Black Eagle, and Vaughn usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 15, US 87, US 89, Highway 200, Tenth Avenue South, Central Avenue, the Bridges, and the Canyon',
 prose(
  L('Great Falls sits on a bend of the Missouri with one interstate on its west edge. Every other road out is a two-lane highway with hours between towns.'),
  P('Interstate 15 is the Salt Lake-to-Calgary road. It comes up from Helena through Wolf Creek Canyon and passes the airport on Gore Hill. It leaves north for Conrad, Shelby, and the border. The canyon closes for rockslides and ice a few times a winter. A carrier waits it out in Helena. The exits that matter are Tenth Avenue South, Central Avenue West, and the Northwest Bypass.'),
  P('US 87 leaves the southeast corner for Stanford, Lewistown, and Billings, four hours of ranch country. It leaves the northeast corner for Fort Benton and Havre, where it meets US 2 on the Hi-Line. US 89 runs northwest past the base to Choteau, Browning, and the east gate of Glacier. Highway 200 heads west over Rogers Pass to Lincoln and Missoula. The pass is the coldest place ever measured in the lower forty-eight, and it closes in a storm.'),
  P('Tenth Avenue South is the commercial strip, from the river bridge east to the base gate. Central Avenue runs through downtown. The bridges on Central, Ninth Street, and Fifteenth Street tie the West Side and Black Eagle in. The carriers come off 15 at Tenth Avenue. The big-box lots on Tenth Avenue South and the mall lots are the usual meeting spots. The fairgrounds lots work outside fair week, and the airport lots work for a fly-and-ship.'),
  P('Our office is on Central Avenue downtown, a few blocks east of the Civic Center.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Lower North Side, the West Side, Riverview, the East Side, the Base, Black Eagle, Fox Farm, and the Valley Towns',
 prose(
  L('Great Falls is a railroad and smelter town laid out in a grid. The base sits on one edge and the river runs through the middle. The truck reaches most of it.'),
  P('Downtown runs along Central Avenue from the river to the tracks, brick blocks with angled parking. The driver meets you at the lots by the Civic Center or on First Avenue North. The Lower North Side between downtown and the river is the oldest neighborhood, narrow streets under big cottonwoods. The handoff moves to the river parks or Central Avenue West.'),
  P('The West Side across the river climbs toward the airport, wide streets where the curb works. Riverview along the bend north of downtown is the same. The East Side from the fairgrounds out to Fifty-Seventh Street is the biggest grid in the city. Ranch houses sit on wide streets. The curb works almost everywhere. The base housing beyond the gate is off limits to a carrier. The handoff happens at the gate or on Tenth Avenue.'),
  P('Black Eagle across the river is the old smelter town, small houses on a hillside grid. The driver meets you on the main road. Fox Farm and Gibson Flats to the south are newer and wider. Sand Coulee and Stockett down the coulee are old mining towns at the end of a county road. The handoff is at the highway.'),
  P('Vaughn and Sun River to the west and Cascade and Ulm down 15 ship with the same trucks. So does Belt out 87. So do Fort Benton and Choteau an hour out. Helena is ninety minutes down the canyon and rides the same carriers. Conrad, Shelby, and the Hi-Line towns run 5 to 10 days. A carrier leaves 15 for them only with a full load.'),
 )))

ROUTES=[("Missoula, MT","MT-200 · ~165 mi","1 day","$220–$340"),("Billings, MT","US-87 · ~220 mi","1 day","$240–$360"),
 ("Spokane, WA","MT-200/I-90 · ~370 mi","1–2 days","$350–$500"),("Salt Lake City, UT","I-15 · ~520 mi","2 days","$430–$620"),
 ("Bismarck, ND","MT-200/I-94 · ~580 mi","2 days","$450–$650"),("Boise, ID","I-15/I-86/I-84 · ~650 mi","2 days","$470–$680"),
 ("Seattle, WA","MT-200/I-90 · ~650 mi","2 days","$500–$720"),("Denver, CO","US-87/I-25 · ~770 mi","2–3 days","$560–$800"),
 ("Fargo, ND","US-2/I-94 · ~800 mi","2–3 days","$580–$830"),("Phoenix, AZ","I-15/US-93 · ~1,250 mi","3–4 days","$900–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Great Falls Car Shipping Lanes and Estimated Costs',
 'The lanes central Montana cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Great Falls, running sedan, open trailer. An SUV or a pickup costs 10 to 25 percent more, and enclosed more still. Your week of dates and the trucks on 15 and 90 that week set the real quote.',
 prose(
  P('Great Falls prices like a stop on 15 with a detour from 90. That is how the carriers see it. The Missoula lane rides 200 over the pass. The Salt Lake lane rides 15 straight south through Helena and Butte. The Seattle and Spokane lanes join 90 at Missoula. The Arizona lane fills each October with the base retirees and the ranchers heading south.'),
  P('A PCS report date in July or the August move-in falls in the busiest weeks of the year. The <a href="car-shipping-cost.html">cost guide</a> explains what size, condition, and the date range do to the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Missile Wing, the Hospital, the Guard Wing, the Refinery, the Malt Plant, the Colleges, and the Ranches',
 prose(
  L('Great Falls relocates airmen, nurses, refinery hands, and students. The base moves more households than the rest of the city combined.'),
  P('The missile wing at the base rotates airmen and officers on orders all year, with a summer peak. Housing is behind the gate, so the handoff happens outside it or on Tenth Avenue South. The orders cover one vehicle. The family ships the other one with us. Ship Guy is a private broker and has no connection to the Air Force. How orders shape the timing is laid out on the <a href="military-car-shipping.html">military</a> page.'),
  P('The health system on Tenth Avenue South is the largest private employer in the city. It hires traveling nurses year round and brings residents each June. The clinic across town does the same. The Guard wing at the airport flies cargo planes and rotates crews on orders. The refinery by the river and the malt plant move engineers and managers on contract dates. If an employer is paying, the receipts for the package come from us.'),
  P('The two colleges take student cars in late August and send them home in May. A parent sets it up by phone, and an adult meets the truck at a lot to sign. Campus streets are narrow, so the meeting point is Tenth Avenue South. The ranches and the grain elevators move a few managers each season. The handoff is at the highway. Retirees from the base leave for Arizona each October and come back in May. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate paperwork.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The State Fair, Western Art Week, the PCS Season, the Wind, the Canyon, the Cold, and the Sun River',
 prose(
  L('Great Falls runs on a base calendar and a fair calendar. The weather problem is wind in every season and ice in the canyon.'),
  P('The state fair fills the fairgrounds for ten days at the end of July. Third Street, Sixth Street, and the fairgrounds blocks jam from noon to midnight. A handoff in that corner moves to the week after. Western Art Week in March fills every hotel in the city for the auctions and the shows. From June through August the base turns over, and the carriers fill with second cars. A July date is a three-week-ahead booking.'),
  P('The wind blows harder here than almost anywhere in the lower forty-eight. A Chinook in January can lift the temperature fifty degrees in a day. A gust on Tenth Avenue can rock a loaded trailer. A driver loads in the lee of a building. Winter drops sixty inches of snow and a month of nights below zero. Wolf Creek Canyon on 15 closes for ice and rockslides a few times a season. The carriers wait in Helena. Rogers Pass on 200 closes in a storm, and the Missoula car goes around on 15 and 90.'),
  P('A car coming from a warm state gets winter oil and a block heater before its first night. An electric car should land with half a charge, because the cold takes a share. The driver meets you where the lot is plowed.'),
  P('The Sun River floods Vaughn and Sun River in a wet June. In 2018 both towns emptied for a week. The Missouri rose the same spring and closed the river parks. A pickup on the flood plain moves up to Tenth Avenue South until the water drops. Summer brings hail that dents a car in minutes, and an enclosed trailer avoids it. The grass fires in August close a highway for an afternoon and nothing more.'),
 )+chips(["Downtown","Central Avenue","Civic Center","Lower North Side","Upper North Side","West Side","Gore Hill","Riverview","East Side","Fifty-Seventh Street","Malmstrom","Fox Farm","Gibson Flats","Black Eagle","Sand Coulee","Stockett","Vaughn","Sun River","Ulm","Cascade","Belt","Fort Benton","Choteau","Conrad","Shelby","Helena","Lewistown","Havre"])
 +NOTE('Serving Great Falls and the whole Golden Triangle, Lower North Side block or ranch gate on 87. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Great Falls?',
 prose(
  L('Almost every Great Falls car goes out on an open trailer, and the table above assumes one.'),
  P('An enclosed trailer keeps off the gravel of the canyon, the summer hail, and the salt on 15. The collectors on the North Side and the officers moving a new car to the base book one. A car headed to Arizona ahead of the first blizzard often rides enclosed too.'),
  P('A daily driver or a student car has no need of a roof. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot on Tenth Avenue South, and a signature at delivery. The week of dates decides the truck.'),
  P('Approve the price, and we watch for a carrier on 15 or 90 that week. The lot and the window are confirmed the moment one commits. At pickup the driver walks around the car with you and logs each mark on the sheet. You sign it, and the delivery inspection is measured against it.'),
 )+ULI([
  "Your things out of the car, trunk included",
  "A quarter tank of fuel, give or take",
  "Photos of each side and the odometer before the truck arrives",
  "A key that works, plus a note about anything that sticks",
  "Aftermarket alarm turned off",
  "On the Lower North Side, downtown, or at the base, plan on a lot or the gate",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks through the sequence. The <a href="car-shipping-preparation.html">preparation</a> page has the full checklist.'))))

BODY.append(sec('Why Ship Guy','Why Great Falls Drivers Choose Ship Guy',
 prose(
  L('We know which carriers come up 15 and over from 90 each week, and when the canyon closes.'),
  P('The federal register lists our FMCSA license and our $75,000 bond, and anyone can look them up. The office is on Central Avenue downtown.'),
  P('The coordinator who prices the move is the one who tracks the truck to your lot. The <a href="services.html">services</a> page compares open, enclosed, and expedited.'),
 )))

BODY.append(office('Great Falls','721 Central Ave #852','Great Falls, MT 59401','+14066923846','(406) 692-3846','MT',
 '721+Central+Ave+%23852,+Great+Falls,+MT+59401','Visit Us','Find Ship Guy in Great Falls',
 'Our office is on Central Avenue downtown, a few blocks east of the Civic Center.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4116.285918548954!2d-111.3247882!3d47.5081861!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x534237dea29d03f1%3A0xc7735b45a2df54b5!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793300218654!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Great Falls to Salt Lake City or Seattle?","Salt Lake City runs four hundred thirty to six hundred twenty dollars for a sedan. That is about five hundred twenty miles down 15. Seattle runs five hundred to seven hundred twenty, about six hundred fifty miles over 200 and 90. Missoula and Billings are a day away and cost the least. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Why does a Great Falls pickup take 3 to 6 days?","Because Montana is a pass-through market. The carriers run 15 between Salt Lake and the border and 90 between Seattle and the Midwest. One adds a Great Falls stop when the load lines up. With a week of dates we can book the next truck through. Insist on one day, and you may wait for it."),
 ("Do you handle PCS moves for Malmstrom?","Yes, and summer is the peak. The missile wing rotates airmen and officers on orders all year. Housing is behind the gate, so the handoff happens outside it or on Tenth Avenue South. The orders cover one vehicle, and the family ships the other one with us. Ship Guy is a private broker and has no connection to the Air Force."),
 ("Can the carrier come to my street on the Lower North Side or the East Side?","The East Side, yes. The grid out to Fifty-Seventh Street is wide, and the curb works on almost every block. The Lower North Side, usually not. The streets are narrow and the cottonwoods hang low. The driver meets you at the river parks or on Central Avenue West."),
 ("Do you ship cars for the hospital and the refinery?","Yes, every month. The health system brings residents each June and hires traveling nurses year round. The refinery and the malt plant move engineers on contract dates. The Guard wing rotates crews on orders. If an employer is paying, the receipts for the package come from us."),
 ("Can you ship a car to or from Helena, Havre, or the Hi-Line?","Yes. Helena is ninety minutes down the canyon, rides the same carriers, and prices the same. Havre, Conrad, Shelby, and the Hi-Line towns take 5 to 10 days. A carrier leaves 15 for them only with a full load. The handoff up there is in town or at the highway."),
 ("What happens if Wolf Creek Canyon closes on my pickup day?","The carrier waits in Helena until the state reopens 15. A canyon closure usually lasts hours, and the truck arrives a day late. We tell you before the driver does. A westbound car can ride 200 over Rogers Pass while the canyon is shut."),
 ("Does the state fair or the PCS season affect my pickup?","Yes, in different ways. The fair jams the fairgrounds blocks for ten days at the end of July. A handoff there moves to the week after. The PCS season from June through August fills the carriers with second cars. A July pickup books three weeks ahead. The rest of the year has room."),
 ("Can you ship a car that does not run from Great Falls?","Yes. We book a carrier with a winch and build the loading time into the quote. Fewer trucks can take a non-runner on a pass-through road, so give us room on the dates. The big-box lots on Tenth Avenue South are level. Does it roll, steer, and brake? Tell us which."),
 ("What do you need for a Great Falls car shipping quote?","Pickup and delivery, with the neighborhood or the town and the nearest highway. Year, make, and model. Whether it starts. Open or enclosed. The widest week you can give us. With those, a Great Falls number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Great Falls FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Great Falls?','Two minutes on the form above, and a Great Falls number comes back. Give us the neighborhood and a week of dates, and we catch the next carrier through.','+14066923846','(406) 692-3846','Get your free Great Falls quote'))

build({
 'slug':'auto-transport-great-falls-montana',
 'title':'Car Shipping in Great Falls, MT — Auto Transport | Ship Guy',
 'meta':'Car shipping in Great Falls, MT, on Interstate 15 between the base, the Hi-Line, and the Missouri. Honest 3 to 6 day windows, Malmstrom PCS moves outside the gate, hospital and refinery relocations, lot handoffs for the Lower North Side and downtown, curbside pickups on the West Side, the East Side, Black Eagle, and Vaughn, the wind, the canyon closures, and the fair. Local office on Central Avenue downtown. Free quote.',
 'h1':'Car Shipping in<br>Great Falls, <span class="accent">Montana</span>',
 'lede':'Open, enclosed, and expedited auto transport across Great Falls and the Golden Triangle, planned around 15, the base calendar, the wind, the canyon, and the honest windows of a pass-through market.',
 'tel':'+14066923846','disp':'(406) 692-3846','brand':'Great Falls','keyword':'car shipping in great falls',
 'localterms':['great falls','missouri','interstate 15','base','hi-line','wind','canadian border','salt lake city','central avenue','downtown','golden triangle','lower north side','malmstrom','vaughn','helena','shelby','us 87','lewistown','billings','havre','us 89','choteau','glacier','highway 200','rogers pass','missoula','tenth avenue south','river','hospital','refinery','guard wing','fair','pass-through','spokane','bismarck','boise','seattle','denver','fargo','phoenix','west side','riverview','east side','black eagle','calgary','wolf creek canyon','gore hill','conrad','rockslides','northwest bypass','stanford','fort benton','us 2','browning','lincoln','coldest','bridges','ninth street','fifteenth street','big-box','mall','fairgrounds','airport','fly-and-ship','civic center','smelter','angled parking','first avenue north','cottonwoods','river parks','fifty-seventh street','gate','fox farm','gibson flats','sand coulee','stockett','coulee','sun river','cascade','ulm','belt','missile wing','orders','summer peak','traveling nurses','residents','clinic','cargo planes','malt plant','contract dates','colleges','late august','ranches','grain elevators','retirees','arizona','state fair','western art week','auctions','pcs season','chinook','fifty degrees','sixty inches','below zero','block heater','electric car','2018','hail','grass fires','fmcsa','upper north side','winch','week of dates'],
}, BODY, FAQ)
