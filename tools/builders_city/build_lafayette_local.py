import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Lafayette, Louisiana','Car shipping in the heart of Acadiana, where Interstate 10 meets Interstate 49 and the oil patch meets the campus',
 ['Car shipping in Lafayette runs off Interstate 10 on the north side and the Evangeline Thruway. Ship Guy is a licensed auto transport broker with an office on Congress Street downtown.',
  'We book vetted carriers across Acadiana, from Carencro and Scott to Broussard, Youngsville, and New Iberia. The trucks belong to the carriers, and we hold the authority and the bond.',
  'Interstate 10 crosses the north side with exits at Ambassador Caffery, the Thruway, and Louisiana Avenue. Interstate 49 runs north to Opelousas and Shreveport. US 90 runs south to New Iberia and Houma. The Thruway is the one-way pair through the city, and Ambassador Caffery is the loop.',
  'This page covers 10, 49, the Thruway, downtown, the Saint Streets, River Ranch, and the Acadiana towns. It also covers the oilfield yards, the hospitals, the campus, the festivals, hurricane season, and the lanes.'],
 'Lafayette at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between Houston and New Orleans passes the city on 10. The Dallas trucks come down 49.',
  'Baton Rouge, New Orleans, Houston, and Shreveport are a same-day haul, and so is Jackson. Mobile, Dallas, and Memphis take a day. Atlanta takes one to two, and Florida takes two.'],
 'Tell us the side of the Thruway. The Saint Streets, Freetown, and River Ranch need a meeting spot. The south side off Kaliste Saloom, Youngsville, and Broussard usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 10, Interstate 49, the Thruway, US 90, Ambassador Caffery, and the Basin Bridge',
 prose(
  L('Lafayette is the crossroads of south Louisiana. A carrier on either interstate passes within a mile of downtown.'),
  P('Interstate 10 crosses the north side of the city between Lake Charles and Baton Rouge. The exits at Ambassador Caffery, the Thruway, and Louisiana Avenue serve the city. The 49 interchange sits in the middle of them. East of the city, the eighteen-mile bridge over the Atchafalaya Basin carries 10 to Baton Rouge. It closes in fog and after a crash, and there is no quick way around it.'),
  P('Interstate 49 begins at 10 and runs north through Opelousas and Alexandria to Shreveport. The Dallas carriers come down it every day. US 90 runs south through Broussard and New Iberia to Houma. The state is building it into the southern half of 49. The Evangeline Thruway carries US 90 and 167 through the city as a one-way pair.'),
  P('Ambassador Caffery Parkway is the loop around the west and south sides, from 10 to US 90. Johnston Street is US 167 south to Abbeville and the main commercial strip. Kaliste Saloom, Pinhook, and Verot School cross the south side. Jefferson Street is downtown. University Avenue runs the west side past the campus. The Vermilion River bends through the south side, and the bridges on Pinhook and Ambassador set the crossings.'),
  P('The carriers come off 10 at Ambassador Caffery and off 49 at the Thruway. The mall on Johnston, the arena, and the truck stops at the Scott exit are the meeting spots. No road in Acadiana charges a toll.'),
  P('Our office is on Congress Street downtown, two blocks from Jefferson Street and minutes from the Thruway.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Freetown, the Saint Streets, the Oil Center, River Ranch, the South Side, Youngsville, Broussard, and New Iberia',
 prose(
  L('Lafayette is an old Cajun town that grew into an oil city. The oldest streets are the ones a trailer cannot work.'),
  P('Downtown is a tight grid along Jefferson Street with the courthouse, the cathedral, and the bars. The Thruway runs a block east of it. The driver meets you at the lots on the Thruway or by the arena. Freetown and Sterling Grove beside downtown are historic districts of narrow streets, shotgun houses, and oaks. The handoff moves to the Thruway or Johnston.'),
  P('The Saint Streets by the campus are named for saints and shaded by oaks a trailer cannot clear. The student blocks along McKinley and Johnston are the same. The driver meets you at the lots on Johnston or at the arena. The Oil Center is the office and medical district off Pinhook, with wide streets and lots everywhere. The hospital on the Thruway and the hospital on Ambassador both have lots at the gate.'),
  P('River Ranch on the south side is the new urban village. Its narrow streets, alleys, and parking courts were built for walking. The driver meets you on Camellia Boulevard or at the town square lots. The subdivisions off Kaliste Saloom, Verot School, and Ambassador south of the river are wide. The curb works. Youngsville and Broussard to the south are the fastest-growing towns in the state, with wide new streets.'),
  P('Scott to the west and Carencro to the north are small towns on 10 and 49. Each has lots at the exit. Breaux Bridge sits fifteen minutes east on the edge of the basin. New Iberia sits thirty minutes south on 90 with the sugar mills and the hot-sauce island. Opelousas, Crowley, and Abbeville are the parish seats around it. All of them price the same as Lafayette. So do Lake Charles and Baton Rouge at the two ends of 10.'),
 )))

ROUTES=[("Baton Rouge, LA","I-10 · ~55 mi","Same day","$140–$230"),("New Orleans, LA","I-10 · ~135 mi","Same day","$190–$300"),
 ("Houston, TX","I-10 · ~215 mi","Same day","$230–$350"),("Shreveport, LA","I-49 · ~230 mi","Same day","$240–$360"),
 ("Jackson, MS","I-49/US-190/I-55 · ~220 mi","Same day","$240–$360"),("Mobile, AL","I-10 · ~280 mi","1 day","$270–$400"),
 ("Dallas, TX","I-49/I-20 · ~400 mi","1 day","$380–$540"),("Memphis, TN","I-49/I-55 · ~430 mi","1 day","$400–$570"),
 ("Atlanta, GA","I-10/I-65/I-85 · ~590 mi","1–2 days","$460–$660"),("Orlando, FL","I-10/I-75 · ~775 mi","2 days","$560–$800")]
BODY.append(rate_table('Lanes &amp; Costs','Lafayette Car Shipping Lanes and Estimated Costs',
 'The lanes Acadiana cars travel most, with estimated open-trailer ranges. Price your exact route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Lafayette for a sedan that runs, on an open trailer. An SUV or a pickup adds 10 to 25 percent, and an enclosed trailer adds more again. Storm season and the carriers free on your dates set the final number.',
 prose(
  P('Lafayette prices with Baton Rouge on the eastern lanes and a little under it to Houston and Dallas. The city sits closer to Texas. The Houston lane runs all day in both directions. The Shreveport lane rides 49 and runs daily. The Florida lane fills with snowbirds each fall. The carriers avoid the coast for a week when a storm enters the Gulf.'),
  P('A move timed to a rig rotation or an oil-patch start date ships with the Houston traffic. The price follows. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Oil Patch, the Heliports, the Hospitals, the Campus, the Jewelry Maker, and the Tech Center',
 prose(
  L('Lafayette relocates engineers, rig crews, nurses, and students. The oilfield service companies move more people than anyone in Acadiana.'),
  P('The oilfield service yards along US 90 and in Broussard hire engineers and crews from every oil state. The helicopter companies by the airport fly the crews offshore on two-week rotations. A worker on rotation ships the car rather than drive it between hitches. The pipeline firms and the fabrication yards in New Iberia hire the same way. We supply the paperwork a reimbursed move needs.'),
  P('The two hospital systems bring in traveling nurses all year and physicians around a closing date. The medical campus in the Oil Center rotates residents each June. The university on the west side holds nineteen thousand students. The cars arrive each August and leave each May. The parent handles the booking, and an adult meets the driver at a campus lot.'),
  P('The jewelry maker headquartered on the south side moves designers and managers in on its own calendar. The tech services center by the campus hires analysts from every state on contract cycles. The utility and the bank headquartered downtown move staff on start dates. The sugar mills and the salt mine south of the city rotate engineers on harvest and maintenance schedules.'),
  P('Families from Houston and Baton Rouge buy in Youngsville and Broussard on closing dates. One car rides the trailer while the other is driven. The Army post at Fort Johnson sits two hours northwest, and the orders cover one car. Ship Guy is a private broker and not part of the post. The <a href="military-car-shipping.html">military</a> page has the timing, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page has the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Festival International, Mardi Gras, Football Saturdays, Hurricane Season, the 2016 Flood, and the Fog',
 prose(
  L('Lafayette runs on a festival calendar that closes downtown twice a year. The hurricane season closes the coast.'),
  P('The international festival closes downtown for five days at the end of April. It draws three hundred thousand people. The Thruway lots are gone, and a handoff downtown moves to the mall or to the week before. The Cajun and Creole festival fills Girard Park for an October weekend. Mardi Gras closes Jefferson Street and Johnston for the parades from the Thursday through Fat Tuesday.'),
  P('The campus stadium fills the west side on football Saturdays. The arena fills its lots on basketball nights. The boudin festival fills Scott for an April weekend, and the sugarcane festival fills New Iberia in September. A handoff near any of them moves to the daytime or to the next morning.'),
  P('Hurricane season runs from June through November. When a storm enters the Gulf, the carriers pull north days before landfall. The coast waits a week. Lili in 2002, Rita in 2005, and Laura and Delta in 2020 each shut the city for days. The evacuation traffic from the coast fills 49 north and 10 west. A pickup booked inside a storm window is rebooked for the week after.'),
  P('The August 2016 flood dropped two feet of rain in three days. The Vermilion crested at a record, and Youngsville and the south side went under water for a week. The basin bridge closes in fog a few mornings each winter. A carrier crossing to Baton Rouge loses hours. The February 2021 ice storm shut 10 and 49 for three days. Summer brings ninety-five degrees and a storm every afternoon.'),
 )+chips(["Downtown","Jefferson Street","Congress Street","Freetown","Sterling Grove","Thruway","Saint Streets","McKinley","Campus","Girard Park","Oil Center","Pinhook","Johnston Street","Ambassador Caffery","River Ranch","Camellia Boulevard","Kaliste Saloom","Verot School","Vermilion River","Youngsville","Broussard","Milton","Scott","Carencro","Duson","Breaux Bridge","New Iberia","Abbeville","Crowley","Opelousas","Rayne","Lake Charles"])
 +NOTE('Serving Lafayette and all of Acadiana, Saint Street or new subdivision in Youngsville. Tell us the side of the Thruway and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Lafayette?',
 prose(
  L('Most Acadiana cars ride an open trailer, and the lane table above is priced for one.'),
  P('An enclosed trailer keeps off the road grime, the salt air, and the gravel on the oilfield roads. The collectors who fill the downtown cruise nights book one for the show cars. Executives relocating a new car to the Oil Center book one too.'),
  P('A commuter car or an oilfield pickup rides open and arrives none the worse. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the full comparison.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot at the mall or the arena, and the car at the far end. The rotation date or the closing picks the week.'),
  P('Say yes to the number, and the car is placed with a carrier already running 10. The lot and the window come back that afternoon. The driver inspects the car with you before it loads. Every existing mark is written on the Bill of Lading. Both of you sign, and the far end is compared against that sheet.'),
 )+ULI([
  "The cabin and the trunk emptied of personal things",
  "A quarter tank of fuel, give or take",
  "Timestamped photos of every panel and the mileage",
  "One key that works, handed to the driver with any fault described",
  "Aftermarket alarm shut off",
  "In the Saint Streets or River Ranch, meet the truck on Johnston or at the town square lots",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Lafayette Drivers Choose Ship Guy',
 prose(
  L('We book the carriers already running 10 between Houston and New Orleans. We watch the Gulf in storm season and the basin bridge in fog season.'),
  P('Ship Guy carries FMCSA brokerage authority and a $75,000 surety bond, and the federal register lists both. Our office is on Congress Street downtown.'),
  P('The person who quotes your move stays with it until the delivery sheet is signed. Open, enclosed, and expedited transport are covered on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Lafayette','116 E Congress St #359A','Lafayette, LA 70501','+13373579845','(337) 357-9845','CT',
 '116+E+Congress+St+%23359A,+Lafayette,+LA+70501','Visit Us','Find Ship Guy in Lafayette',
 'Our office is on Congress Street downtown, two blocks from Jefferson Street and minutes from the Thruway.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5301.299653133558!2d-92.0180003!3d30.225215299999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86249df91ae2271b%3A0xc30016c034240869!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793102915677!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Lafayette to Houston or Dallas?","Houston runs two hundred thirty to three hundred fifty dollars for a sedan. That is about two hundred fifteen miles west on 10. Dallas runs three hundred eighty to five hundred forty, about four hundred miles up 49 and 20. Baton Rouge is an hour away and the lowest of the three. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street in the Saint Streets or River Ranch?","Usually not. The Saint Streets are shaded by oaks a trailer cannot clear. River Ranch was built with narrow streets and alleys. The driver meets you at the lots on Johnston, at the arena, or on Camellia Boulevard. The subdivisions off Kaliste Saloom and Verot School, Youngsville, and Broussard usually allow the curb."),
 ("Do you ship cars for offshore workers and the oilfield companies?","Yes, every week. The service yards on US 90 and in Broussard hire crews from Texas and every oil state. The helicopter companies fly the crews out on two-week rotations. A worker on rotation ships the car rather than drive it. Many relocations ship a second car behind the move. We supply the paperwork a reimbursed move needs."),
 ("Can you deliver on the UL Lafayette move-in date?","Yes. The campus takes cars in each August and sends them home in May. A parent makes the arrangements, and an adult signs for the car at a campus lot. The window is set to move-in day and moves with it. The Saint Streets fill that week, so the handoff happens at the lots on Johnston."),
 ("Does Festival International or Mardi Gras affect my pickup?","Downtown, yes. The festival closes downtown for five days at the end of April. Mardi Gras closes Jefferson Street and Johnston for the parades. We move a downtown handoff those weeks to the mall or to the days before. The south side, Youngsville, and Broussard run normally."),
 ("Can you ship a car to or from Youngsville, Broussard, or New Iberia?","Yes, and all three price the same as Lafayette. Youngsville and Broussard ride the same carriers off Ambassador Caffery and US 90. The curb works on the new streets. New Iberia rides them thirty minutes down 90, and the handoff works at a lot on the highway. Send the full address for a new subdivision, because the maps lag the growth."),
 ("What happens if a hurricane enters the Gulf on my pickup day?","The carriers pull north days before landfall, and the coast waits a week. A pickup booked inside the storm window is rebooked for the week after. You hear it from us first. The evacuation traffic fills 49 north and 10 west for two days. When the roads reopen, the trucks come back in the order the loads were booked."),
 ("Does the basin bridge affect my delivery?","Some mornings, yes. The eighteen-mile bridge over the Atchafalaya closes in fog and after a crash. There is no quick way around it. A carrier crossing to Baton Rouge can lose hours. We build a cushion into windows that cross the basin in winter. The Houston and Shreveport lanes never touch it."),
 ("Can you ship a car that does not run from Lafayette?","Yes. A winch carrier is assigned, and the loading time is in the quote from the first number. The mall lot on Johnston or the arena lot gives the driver level pavement. Say whether the car rolls, steers, and brakes."),
 ("What do you need for a Lafayette car shipping quote?","Where it is and where it goes, with the side of the Thruway or the town. Year, make, and model. Running or not. Open or enclosed. The week around the rotation date or the closing. Nothing else is needed, and the Lafayette number is back within the day."),
]
BODY.append(faq_section(FAQ,'Lafayette FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Lafayette?','A number for your lane is two minutes away on the form above. Name the side of the Thruway and the week, and a carrier already on 10 takes it.','+13373579845','(337) 357-9845','Get your free Lafayette quote'))

build({
 'slug':'auto-transport-lafayette-louisiana',
 'title':'Car Shipping in Lafayette, LA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Lafayette, LA, where Interstate 10 meets Interstate 49 in the heart of Acadiana. Oilfield and offshore relocations, UL Lafayette move-in timing, Thruway-lot handoffs for the Saint Streets and River Ranch, curbside pickups in Youngsville and Broussard, Festival International, hurricane season, and the basin bridge. Local office on Congress Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Lafayette, <span class="accent">Louisiana</span>',
 'lede':'Open, enclosed, and expedited auto transport across Acadiana, planned around 10, 49, the Thruway, the rig rotations, the festivals, and the Gulf.',
 'tel':'+13373579845','disp':'(337) 357-9845','brand':'Lafayette','keyword':'car shipping in lafayette',
 'localterms':['lafayette','acadiana','interstate 10','interstate 49','evangeline thruway','one-way pair','congress street','jefferson street','carencro','scott','broussard','youngsville','new iberia','ambassador caffery','louisiana avenue','opelousas','shreveport','us 90','houma','loop','lake charles','baton rouge','atchafalaya','basin','eighteen-mile','fog','alexandria','dallas','us 167','johnston street','abbeville','kaliste saloom','pinhook','verot school','university avenue','campus','vermilion river','mall','arena','truck stops','toll','downtown','courthouse','cathedral','freetown','sterling grove','shotgun houses','oaks','saint streets','mckinley','oil center','medical','hospital','river ranch','urban village','alleys','camellia boulevard','town square','breaux bridge','sugar mills','hot-sauce','crowley','new orleans','houston','jackson','mobile','memphis','atlanta','orlando','snowbirds','gulf','rig rotation','oilfield service','rig crews','helicopter','airport','offshore','two-week rotations','hitches','pipeline','fabrication yards','traveling nurses','physicians','residents','nineteen thousand','students','jewelry maker','tech services','utility','bank','salt mine','fort johnson','festival international','international festival','three hundred thousand','cajun and creole','girard park','mardi gras','fat tuesday','football saturdays','basketball','boudin festival','sugarcane festival','hurricane season','lili','rita','laura','delta','evacuation','august 2016 flood','two feet of rain','record','february 2021 ice storm','ninety-five degrees','cruise nights','bill of lading','fmcsa','surety bond','milton','duson','rayne'],
}, BODY, FAQ)
