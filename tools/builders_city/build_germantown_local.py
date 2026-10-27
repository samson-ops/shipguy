import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Germantown, Maryland','Car shipping up the 270 corridor, where the tech firms, the biotech labs, and the newest subdivisions in Montgomery County meet the farmland',
 ['Car shipping in Germantown runs up and down Interstate 270 between the Beltway and Frederick. Ship Guy is a licensed auto transport broker with an office on Frederick Road at Milestone.',
  'We book vetted carriers across upper Montgomery County, from Gaithersburg to Clarksburg and out to Poolesville and Damascus. The trucks belong to the carriers, and we hold the authority and the bond.',
  'Interstate 270 is the whole story, a twelve-lane highway at the Beltway that narrows to four by Clarksburg. The exits at Route 118, Father Hurley, Middlebrook, and Route 121 serve the city. MD 355 is Frederick Road, the old main road underneath it. Route 27 runs north to Damascus, Route 118 crosses to Darnestown, and the Intercounty Connector starts in Gaithersburg.',
  'This page covers 270, Frederick Road, the subdivisions, Town Center, Clarksburg, Gaithersburg, and the farm roads. It also covers the energy campus, the satellite firm, the labs, the hospital, Oktoberfest, and the lanes.'],
 'Germantown at a glance',
 ['Most pickups happen within 1 to 3 days. The Washington carrier pool is forty minutes down 270. The Baltimore pool is an hour across the ICC. Both work the corridor daily.',
  'Washington and Baltimore are a same-day haul, and so are Richmond and Philadelphia. Pittsburgh and New York take a day. Raleigh takes one, and Charlotte and Boston take one to two. Florida takes three.'],
 'Tell us the subdivision. The newer streets off Great Seneca Highway and in Clarksburg are wide, and the curb works on most. The older townhouse loops off Middlebrook need the shopping center lot or the park-and-ride.'))

BODY.append(sec('The Roads','Interstate 270, Frederick Road, Route 118, Route 27, Great Seneca, and the ICC',
 prose(
  L('Germantown is a 270 town, and every carrier arrives and leaves on it.'),
  P('Interstate 270 runs from the Beltway in Bethesda to Frederick, where it meets 70. It carries twelve lanes with local and express roadways through Rockville and Gaithersburg. It narrows to four lanes north of Clarksburg. The Germantown exits are Route 118, Father Hurley Boulevard, Middlebrook Road, and Route 121 at Clarksburg. The morning rush south and the evening rush north run two hours each. A trailer plans around both.'),
  P('MD 355 is Frederick Road, the old main road beside 270 from Rockville to Frederick. It carries the shopping centers, the car dealers, and the office parks. It is the road a driver uses when 270 stops. Route 118 crosses the city from Darnestown to the Town Center and on to Route 27. Route 27 is Ridge Road, north to Damascus and the farm country. Great Seneca Highway runs the newer subdivisions on the south side to Gaithersburg.'),
  P('Route 117 runs to Poolesville and the river, and Route 119 is Great Seneca itself. The Intercounty Connector begins at 370 in Gaithersburg and runs east to 95 and Laurel. It is a toll road with no booths. A carrier bound for Baltimore or the port uses it with a transponder. The toll rides inside the quote when a driver chooses it. No other road in the county charges one.'),
  P('The carriers come off 270 at 118 and Father Hurley. The Town Center, the shopping centers on Frederick Road, and the Milestone park-and-ride are the meeting spots. The outlets at Clarksburg and the big lots at the SoccerPlex in Boyds work for the north side.'),
  P('Our office is on Frederick Road at Milestone, by the 270 exit and Route 27.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Town Center, Milestone, Kingsview, Churchill, Clarksburg, Gaithersburg, Boyds, and Damascus',
 prose(
  L('Germantown was farmland until the eighties, and the subdivisions came all at once. The newer the street, the easier the handoff.'),
  P('The Town Center along Century Boulevard holds the library, the arts center, and the college campus. The MARC station sits there on the old main line. The streets are wide, and the lots are everywhere. There is no Metro here. The nearest station is Shady Grove, twenty minutes down 270, and a trailer never meets anyone there.'),
  P('Milestone along Route 27 is the shopping center and the park-and-ride, and the handoff works there any day. Kingsview, Churchill, and the subdivisions off Great Seneca and Clopper Road are the nineties and later. They have wide loops and open curbs. The driver reaches the house on most of them. The older townhouse loops off Middlebrook and Route 118 are tighter. The driver meets you at the shopping center.'),
  P('Clarksburg to the north is the newest town, with a town center and the outlets at 121. Its subdivisions grew faster than the roads. Its streets are wide, and the curb works. Boyds and Germantown Park hold the SoccerPlex and the lake. Darnestown and Poolesville to the west are the agricultural reserve, with narrow roads and no shoulders. The driver meets you on Route 28 or Route 107.'),
  P('Gaithersburg to the south is the older city, with the biotech firms, the federal lab, and the fairgrounds. Montgomery Village is its planned suburb with loop streets. Damascus to the north is the small town at the top of Route 27. All of them price the same as Germantown. So do Rockville and Frederick at the two ends of the corridor.'),
 )))

ROUTES=[("Washington, DC","I-270/I-495 · ~30 mi","Same day","$140–$230"),("Baltimore, MD","ICC/I-95 · ~45 mi","Same day","$150–$240"),
 ("Richmond, VA","I-270/I-95 · ~130 mi","Same day","$200–$310"),("Philadelphia, PA","ICC/I-95 · ~150 mi","Same day","$200–$310"),
 ("Pittsburgh, PA","I-270/I-70/I-76 · ~210 mi","1 day","$230–$350"),("New York, NY","ICC/I-95 · ~240 mi","1 day","$250–$370"),
 ("Raleigh, NC","I-95 · ~290 mi","1 day","$270–$400"),("Charlotte, NC","I-95/I-85 · ~400 mi","1–2 days","$360–$520"),
 ("Boston, MA","I-95 · ~450 mi","1–2 days","$370–$540"),("Orlando, FL","I-95 · ~880 mi","3 days","$650–$920")]
BODY.append(rate_table('Lanes &amp; Costs','Germantown Car Shipping Lanes and Estimated Costs',
 'The lanes upper Montgomery County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Germantown, Maryland, open trailer, sedan that runs. SUVs and pickups land 10 to 25 percent higher, enclosed higher again. The ICC toll is inside the number when a carrier uses it. The carriers free on your dates settle the final figure.',
 prose(
  P('Germantown prices with Washington on most lanes. It runs a little over Baltimore on the lanes that ride 95 north. The carrier has to cross the county to reach them. The Pittsburgh lane runs 270 to 70 and 76 and prices better here than anywhere else in Maryland. The Florida lane fills with federal retirees in the fall. The Richmond lane runs daily.'),
  P('A move on a federal transfer or a biotech contract ships with the summer peak. The price follows. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Energy Campus, the Satellite Firm, the Labs, the Hospital, the College, and the Federal Transfers',
 prose(
  L('Germantown relocates engineers, scientists, physicians, and federal families up the corridor on start dates.'),
  P('The energy department campus on Germantown Road has held thousands of federal staff since the fifties. It transfers people in from the national labs and the regional offices on start dates. The satellite company headquartered beside 270 moves engineers in on program schedules. The diagnostics firm on the north side and the labs along Clopper Road hire scientists from every state. The paperwork for a reimbursed move comes from us.'),
  P('Gaithersburg down the road holds the standards lab, the pharmaceutical campus, and the defense contractor. Together they move hundreds of families a year into the Germantown subdivisions. The medical campus in Bethesda relocates researchers each summer. Many settle up the corridor where the houses are newer. The hospital on Observation Drive brings in nurses on contracts all year and physicians with a closing date.'),
  P('The college campus in the Town Center brings cars in each August. The county schools draw families from every state, and the closing date drives the move. Federal employees transfer in from every region, and the agency packages often cover the car.'),
  P('Retirees leave the corridor for the Carolinas, Florida, and Delaware each fall and ship the second car. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side. The <a href="military-car-shipping.html">military</a> page covers an order to the base in Bethesda or Fort Detrick.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Oktoberfest, Germantown Glory, the Fair, the Orchard, the Derecho, and the Snow',
 prose(
  L('Germantown runs on a festival calendar at the Town Center and a soccer calendar in Boyds. The winter shuts 270 a day or two a year.'),
  P('Oktoberfest fills the Town Center for a Saturday each September. The Glory fireworks fill it on the Fourth of July. The county fair fills the Gaithersburg fairgrounds for a week in August. It backs up Frederick Road to Montgomery Village. The tournaments at the SoccerPlex fill Boyds on spring and fall weekends. A handoff near any of them moves to the daytime or to Milestone.'),
  P('The orchard in Germantown fills Route 118 on fall weekends, and the lanes to it are narrow. The farm tours and the harvest festivals fill the reserve roads west of the city in October. A trailer avoids those roads on a Saturday, and the handoff moves to Route 28.'),
  P('The 2012 derecho crossed the corridor on a June night at eighty miles an hour. It took the power out for a week in a heat wave. The summer storms knock out traffic signals on Frederick Road a few times a year. The creek floods at the low crossings on Clopper and Route 118 in a big storm. A pickup there moves up the hill.'),
  P('Winter brings twenty inches of snow in a normal year and more than forty in a bad one. The 2010 blizzards and the 2016 storm shut 270 for two days each. The corridor sits higher and colder than Washington, and a storm that rains on the Beltway snows here. The carriers wait in Frederick or Gaithersburg until the plows finish. A winter pickup can lose a day.'),
 )+chips(["Town Center","Century Boulevard","MARC Station","Milestone","Park-and-Ride","Kingsview","Churchill","Clopper Road","Great Seneca","Middlebrook","Route 118","Father Hurley","Route 27","Frederick Road","Germantown Road","Seneca Creek","Clarksburg","Clarksburg Outlets","Boyds","SoccerPlex","Black Hill","Darnestown","Poolesville","Damascus","Gaithersburg","Montgomery Village","Kentlands","Shady Grove","Rockville","Observation Drive","Frederick","Urbana"])
 +NOTE('Serving Germantown and upper Montgomery County, Clarksburg to the Kentlands. Tell us the subdivision and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Germantown?',
 prose(
  L('Most cars leave the corridor on an open trailer, and that is how the table above is priced.'),
  P('An enclosed trailer keeps off the salt, the gravel, and the pollen. The collectors in the reserve and the new-car buyers in Clarksburg book one. So do families shipping a lease return the other way.'),
  P('A commuter car or a second family car goes open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the trade-off.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a meeting spot or a curb, and a signature at each end. The start date or the closing sets the week.'),
  P('Once you approve the price, the car goes to a carrier already running 270 or the ICC. The meeting spot and the window follow the same day. You and the driver walk the car at pickup. Each existing mark goes on the Bill of Lading. Two signatures close it, and the delivery is checked against the same sheet.'),
 )+ULI([
  "Clear the cabin and the trunk of everything personal",
  "Leave about a quarter tank",
  "Photograph all four sides and the mileage",
  "Hand over one working key and name any fault",
  "Disarm any aftermarket alarm",
  "On a townhouse loop, meet the truck at the shopping center or the park-and-ride",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Germantown Drivers Choose Ship Guy',
 prose(
  L('We book the carriers already running the 270 corridor. We know which subdivisions take a trailer and where the rest meet.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond. Both are in the federal register. Our office is on Frederick Road at Milestone.'),
  P('One coordinator owns the move from the first number to the last signature. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Germantown','20900 N Frederick Rd #485A','Germantown, MD 20876','+13013217641','(301) 321-7641','ET',
 '20900+N+Frederick+Rd+%23485A,+Germantown,+MD+20876','Visit Us','Find Ship Guy in Germantown',
 'Our office is on Frederick Road at Milestone, by the 270 exit and Route 27.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4754.623755656889!2d-77.2461288!3d39.1993911!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89b62bbe2ecf2a6f%3A0x133db6b539a03225!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025308335!5m2!1sen!2sus', alt=True))

FAQ=[
 ("Can the carrier come to my house in Germantown?","On most of the newer streets, yes. Kingsview, Churchill, Clarksburg, and the subdivisions off Great Seneca and Clopper have wide loops and open curbs. The older townhouse loops off Middlebrook and Route 118 are tighter. The driver meets you at the shopping center or the park-and-ride at Milestone. Send the address, and we tell you which applies before the truck is booked."),
 ("How much does it cost to ship a car from Germantown to New York or Florida?","New York runs two hundred fifty to three hundred seventy dollars for a sedan. That is about two hundred forty miles up the ICC and 95. Orlando runs six hundred fifty to nine hundred twenty, about eight hundred eighty miles south. Washington is thirty miles down 270 and prices the lowest of all. An SUV or pickup adds 10 to 25 percent."),
 ("Do you ship cars for federal transfers and the labs?","Yes, every month. The energy campus, the standards lab, and the medical campus transfer people in on start dates. The satellite firm, the diagnostics firm, and the biotech labs hire scientists from every state. Many ship a second car behind the move. We provide the paperwork a reimbursed move needs."),
 ("Is there a Metro station in Germantown?","No. The MARC train stops at the Town Center on the old main line. The nearest Metro is Shady Grove, twenty minutes down 270. A trailer never meets anyone at either station. The Town Center, Milestone, and the shopping centers on Frederick Road have the usual meeting lots."),
 ("Does the 270 rush hour affect my pickup?","It sets the window. The morning rush south and the evening rush north each run two hours. A trailer plans around both. We book the pickup for the middle of the day or for the early morning. A storm that shuts 270 slides the pickup a day, and we call before it does."),
 ("Can you ship a car to or from Clarksburg, Gaithersburg, or Damascus?","Yes, and all three price the same as Germantown. Clarksburg rides the same carriers off the 121 exit, and its streets are wide. Gaithersburg rides them off 270 at Route 124 and the ICC. Damascus rides them up Route 27, and the driver meets you in town. Poolesville and the reserve meet the truck on Route 28 or Route 107. Send the full address."),
 ("What happens if a snowstorm hits on my pickup day?","The corridor sits higher and colder than Washington, and a storm that rains on the Beltway snows here. The carriers wait in Frederick or Gaithersburg until the plows finish, and the pickup slips a day. We call before it does, not after. A big summer storm floods the creek crossings on Clopper and Route 118. A pickup there moves up the hill."),
 ("Can you ship a car that does not run from Germantown?","Yes. A winch carrier is dispatched, with the loading time built into the first quote. The park-and-ride at Milestone or the Town Center lots give the driver level pavement. Tell us whether the car rolls, steers, and brakes."),
 ("Is the ICC toll in my price?","Yes. A carrier bound for Baltimore, the port, or 95 north pays the Intercounty Connector with a transponder. The toll rides inside the quote. There is no separate line. Interstate 270, Frederick Road, and the county roads carry no toll."),
 ("What do you need for a Germantown car shipping quote?","Both addresses, with the subdivision here. Year, make, and model. Whether it runs. Open or enclosed. The week around the start date or the closing. Those five answers are the whole request, and the Germantown number is back within the day."),
]
BODY.append(faq_section(FAQ,'Germantown FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Germantown?','The form above prices the lane in two minutes. Give us the subdivision and the week, and a carrier already on 270 takes it.','+13013217641','(301) 321-7641','Get your free Germantown quote'))

build({
 'slug':'auto-transport-germantown-maryland',
 'title':'Car Shipping in Germantown, MD — Auto Transport | Ship Guy',
 'meta':'Car shipping in Germantown, MD, up the Interstate 270 corridor in upper Montgomery County. Federal, biotech, and satellite-firm relocations, curbside pickups in Kingsview, Churchill, and Clarksburg, shopping-center handoffs on the older townhouse loops, Gaithersburg and Damascus, the 270 rush hour, the ICC toll, and the snow. Local office on Frederick Road at Milestone. Free quote.',
 'h1':'Car Shipping in<br>Germantown, <span class="accent">Maryland</span>',
 'lede':'Open, enclosed, and expedited auto transport across upper Montgomery County, planned around 270, Frederick Road, the subdivisions, the start dates, and the winter.',
 'tel':'+13013217641','disp':'(301) 321-7641','brand':'Germantown','keyword':'car shipping in germantown',
 'localterms':['germantown','montgomery county','interstate 270','corridor','beltway','frederick','twelve lanes','express','clarksburg','route 118','germantown road','father hurley','route 27','ridge road','middlebrook','route 121','md 355','frederick road','darnestown','great seneca','route 119','clopper','route 117','poolesville','intercounty connector','icc','toll','transponder','rush','town center','century boulevard','library','arts center','marc','main line','no metro','shady grove','milestone','park-and-ride','shopping center','kingsview','churchill','townhouse loops','outlets','boyds','soccerplex','black hill','lake','agricultural reserve','route 28','route 107','gaithersburg','biotech','federal lab','standards lab','fairgrounds','montgomery village','kentlands','damascus','rockville','energy department','campus','satellite','diagnostics','pharmaceutical','defense contractor','medical campus','bethesda','researchers','hospital','observation drive','nurses','physicians','college','county schools','federal employees','retirees','oktoberfest','glory','fireworks','county fair','tournaments','orchard','farm tours','harvest','2012 derecho','signals','creek','2010','2016','snow','washington','baltimore','richmond','philadelphia','pittsburgh','new york','raleigh','charlotte','boston','orlando','fort detrick','urbana','seneca creek'],
}, BODY, FAQ)
