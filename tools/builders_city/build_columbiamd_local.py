import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Columbia, Maryland','Car shipping in the planned city between Baltimore and Washington, where Route 29 meets Route 32 beside Interstate 95',
 ['Car shipping in Columbia runs off Interstate 95 and the two state routes that cross the villages. Ship Guy is a licensed auto transport broker with an office on Guilford Road, minutes from Route 32.',
  'We book vetted carriers across Howard County, from Ellicott City to Fulton and east to Fort Meade. The trucks belong to the carriers.',
  'Interstate 95 runs the east edge with exits at Route 175 and Route 32. US 29 is the spine through the villages from Silver Spring to Ellicott City. Route 32 is the Patuxent Freeway east to Fort Meade and west to the 70. Route 175 is the loop, and Route 108 and Route 100 cross the north.',
  'This page covers 95, Route 29, the villages and their cul-de-sacs, Town Center, Ellicott City, and Fulton. It also covers the base, the lab, the cyber firms, Merriweather, the floods, and the lanes.'],
 'Columbia at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between New York and Richmond passes the city on 95. The Baltimore and Washington trucks are both thirty minutes away.',
  'Baltimore and Washington are a same-day haul, and so are Philadelphia, Richmond, and New York. Pittsburgh and Raleigh take a day. Boston and Charlotte take one to two. Florida takes three, and Chicago takes two.'],
 'Tell us the village. The cul-de-sacs and the loop streets need a meeting spot at the village center. Town Center, the Route 1 corridor, and the newer subdivisions in Fulton usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, Route 29, Route 32, Route 175, Route 100, and the Village Loops',
 prose(
  L('Columbia was laid out for cars and against through traffic, and a trailer has to learn the difference.'),
  P('Interstate 95 runs along the east edge of the city between Baltimore and the Washington Beltway. The exits at Route 175 and Route 32 serve the city. Every carrier on the East Coast passes both. The Baltimore-Washington Parkway runs parallel five miles east, and trucks are banned from it. The carriers stay on 95.'),
  P('US 29 is the spine, a limited-access road through the middle of the villages. Route 32 crosses it as the Patuxent Freeway. It runs east to Fort Meade, the agency, and 95, and west to Clarksville and the 70. Route 175 is Little Patuxent Parkway, the loop around Town Center and the road east to Jessup. Route 100 crosses the north edge, and Route 108 runs the west side.'),
  P('Broken Land Parkway, Cedar Lane, Hickory Ridge Road, and Snowden River Parkway are the collector roads. Everything off them is a loop or a cul-de-sac with a wooded name. Dobbin Road carries the retail on the east side. Guilford Road and Gateway Drive carry the business parks. Route 1 runs the warehouse corridor through Jessup and Elkridge.'),
  P('The carriers come off 95 at 175 and 32, and off 29 at Broken Land. The mall in Town Center, the village centers, and the Gateway park have the usual meeting lots. No road in Howard County charges a toll. The Intercounty Connector to the south does, and the carriers rarely use it.'),
  P('Our office is on Guilford Road on the east side, minutes from Route 32 and the 95 exit.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Town Center, the Villages, Ellicott City, Clarksville and River Hill, Fulton, and the Route 1 Corridor',
 prose(
  L('Columbia is ten villages around a lake and a mall. The truck meets you at the village center more often than at the house.'),
  P('Town Center is the mall, the lakefront, the concert pavilion, and the new apartments downtown. The streets are wide, and the lots are everywhere. The handoff works any day except a concert night. Wilde Lake, Harper’s Choice, and Oakland Mills are the original villages around it. Their loop streets and cul-de-sacs sit under forty years of trees. A trailer cannot turn in a cul-de-sac. The driver meets you at the village center or on the collector road.'),
  P('Long Reach, Owen Brown, Hickory Ridge, and Kings Contrivance to the east and south are the same pattern. The driver meets you at the village center, at the pool lot, or on Broken Land. Dorsey’s Search and River Hill to the west are newer, with wider loops. The curb works on some streets. Send the address, and we tell you which applies.'),
  P('Ellicott City to the north is the county seat. It has a historic Main Street in a river gorge and subdivisions on the hills above it. Main Street is closed to a trailer, and the handoff moves to the Route 40 lots. Clarksville and the horse country to the west sit on narrow roads. The driver meets you on Route 108. Fulton and Maple Lawn to the south are the newest town center. The streets are wide, and the curb works.'),
  P('Jessup and Elkridge along Route 1 are the warehouse corridor, with lots at every gate. Laurel to the south has the lab and the racetrack. Savage has the old mill. Odenton and the base sit ten minutes east on Route 32. All of them price the same as Columbia. So do Baltimore and Washington at the ends of 95.'),
 )))

ROUTES=[("Baltimore, MD","US-29/I-95 · ~20 mi","Same day","$130–$210"),("Washington, DC","US-29/I-95 · ~25 mi","Same day","$140–$230"),
 ("Philadelphia, PA","I-95 · ~115 mi","Same day","$170–$280"),("Richmond, VA","I-95 · ~130 mi","Same day","$200–$310"),
 ("New York, NY","I-95 · ~210 mi","Same day","$220–$340"),("Pittsburgh, PA","I-70/I-76 · ~235 mi","1 day","$250–$380"),
 ("Raleigh, NC","I-95 · ~270 mi","1 day","$260–$390"),("Boston, MA","I-95 · ~420 mi","1 day","$350–$520"),
 ("Charlotte, NC","I-95/I-85 · ~410 mi","1–2 days","$370–$540"),("Orlando, FL","I-95 · ~870 mi","3 days","$650–$920")]
BODY.append(rate_table('Lanes &amp; Costs','Columbia Car Shipping Lanes and Estimated Costs',
 'The lanes Howard County cars run most often, with estimated open-trailer ranges. Price your exact route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Columbia, Maryland, open trailer, sedan that runs. SUVs and pickups land 10 to 25 percent higher, enclosed higher again. Tunnel and bridge tolls are inside the number when a carrier uses them. The carriers free on your dates settle the final figure.',
 prose(
  P('Columbia prices with Baltimore and Washington on every lane. It sits between the two on 95 and shares both carrier pools. The New York and Richmond lanes run daily. The Florida lane fills with federal retirees each fall and runs higher in October than in April. The Pittsburgh lane rides 70 and 76 and runs lighter.'),
  P('A move on orders to the base ships with the summer peak, and the price follows. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Base and the Agency, the Lab, the Hospital, the Cyber Firms, and the Federal Workforce',
 prose(
  L('Columbia relocates analysts, engineers, physicians, and federal families. The base at the end of Route 32 moves more people than anyone in Maryland.'),
  P('The base ten minutes east holds the signals agency and the cyber command. It moves tens of thousands of civilians and service members on assignment cycles. Many families settle in the villages and Fulton. The orders cover one car, and we move the other. Housing on the base is gated, and the handoff happens outside it. Ship Guy is a private broker with no connection to the base or the agency. The <a href="military-car-shipping.html">military</a> page covers the timing.'),
  P('The cyber firms in the Gateway business park and along Route 32 hire from every state. They move engineers in on contract cycles. The physics lab in Laurel relocates scientists on program schedules. The chemical company and the office landlord headquartered in Town Center move staff on their own calendars. The paperwork for a reimbursed move comes from us.'),
  P('The hospital on Cedar Lane hires traveling nurses all year and takes new residents each June. Physicians come with a closing date and a second car to ship. The community college brings cars in each August. The county schools draw families from both cities, and the closing date drives the move.'),
  P('Federal employees transfer in from every region on start dates, and the agency packages often cover the car. Retirees leave for Florida and the Carolinas each fall. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Merriweather Nights, the Festivals, the Ellicott City Floods, the Derecho, and the Snow',
 prose(
  L('Columbia runs on a concert season at the pavilion and a village calendar of festivals. The river has twice torn through Main Street.'),
  P('The pavilion in Town Center hosts concerts from May through October. The big nights fill Little Patuxent Parkway and Broken Land from five o’clock. A handoff in Town Center on a concert night moves to the daytime or to a village center. The jazz festival and the wine festival each fill the woods around the pavilion for a weekend.'),
  P('The arts festival closes the lakefront for a June weekend. The Fourth of July fills it at night. The county fair fills West Friendship for a week in August. The triathlon closes the roads around Centennial Park on a May morning. A handoff near any of them moves to the daytime.'),
  P('The Ellicott City floods are the weather story. The 2016 and 2018 storms sent the river down Main Street and tore the historic blocks apart. Main Street stays closed to a trailer, and a wet forecast closes the gorge roads. The low crossings on the Patuxent and the Little Patuxent flood in a big storm. A pickup there moves up the hill.'),
  P('The 2012 derecho crossed the county on a June night. It took the power out for a week in a heat wave. The sirens are rare, but the summer storms are not. Winter brings twenty inches of snow in a normal year and forty in a bad one. The 2010 and 2016 blizzards shut 95 for two days each. The carriers park in Jessup until the plows finish, and a winter pickup can lose a day.'),
 )+chips(["Town Center","The Mall","Lakefront","Merriweather","Wilde Lake","Harper’s Choice","Oakland Mills","Long Reach","Owen Brown","Hickory Ridge","Kings Contrivance","Dorsey’s Search","River Hill","Clarksville","Broken Land","Cedar Lane","Snowden River","Dobbin Road","Gateway","Guilford Road","Ellicott City","Main Street","Route 40","Columbia Hills","Fulton","Maple Lawn","Scaggsville","Highland","Savage","Jessup","Elkridge","Laurel","Odenton","Fort Meade","Catonsville"])
 +NOTE('Serving Columbia and all of Howard County, village loop or Route 1 warehouse. Tell us the village and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Columbia?',
 prose(
  L('Nine in ten Howard County cars go open, and the table above is priced that way.'),
  P('An enclosed trailer shuts out the salt, the gravel, and the pollen. The collectors in River Hill and the horse country book one for the shows. Families on orders shipping a new car to the next duty station book one too.'),
  P('A commuter car or an agency sedan is fine on an open trailer. The trade-off is explained on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot at the village center or the mall, and a signature at the far end. The report date or the closing picks the week.'),
  P('Approve the price, and the car is assigned to a carrier already working 95 between Baltimore and Washington. The lot and the window are set before the day is out. You and the driver circle the car at pickup. Every existing mark is written on the Bill of Lading. Two signatures seal it, and the same sheet is read again when the car comes off.'),
 )+ULI([
  "Everything personal out of the cabin and the trunk",
  "Run the tank down to about a quarter",
  "Photograph the car on all four sides, plus the mileage",
  "Pass the driver one working key and point out any fault",
  "Aftermarket alarm disarmed",
  "On a cul-de-sac or a loop, meet the truck at the village center or the pool lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Columbia Drivers Choose Ship Guy',
 prose(
  L('We book the carriers already running 95 between the two cities. We know which villages take a trailer and which do not.'),
  P('Ship Guy’s FMCSA brokerage authority and $75,000 surety bond are both on file with the federal register. Our office is on Guilford Road.'),
  P('One person handles your move from the first call to the final signature. Open, enclosed, and expedited transport are explained on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Columbia','9160 Guilford Rd #568','Columbia, MD 21046','+14107097449','(410) 709-7449','ET',
 '9160+Guilford+Rd+%23568,+Columbia,+MD+21046','Visit Us','Find Ship Guy in Columbia',
 'Our office is on Guilford Road on the east side of Columbia, minutes from Route 32.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4756.801149971379!2d-76.84361770000001!3d39.16720739999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89b7dffb8abc1641%3A0xa9368a4e3871e974!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025298178!5m2!1sen!2sus', alt=True))

FAQ=[
 ("Can the carrier come to my house in the villages?","Rarely. The villages are loop streets and cul-de-sacs under forty years of trees. A seventy-five-foot trailer cannot turn in them. The driver meets you at the village center, at the pool lot, or on the collector road. All are a few minutes from the house. Town Center, the Route 1 corridor, and the newer streets in Fulton allow the curb."),
 ("How much does it cost to ship a car from Columbia to New York or Florida?","New York runs two hundred twenty to three hundred forty dollars for a sedan. That is about two hundred ten miles up 95. Orlando runs six hundred fifty to nine hundred twenty, about eight hundred seventy miles down the same road. Baltimore and Washington are thirty minutes away and cost the least. Figure 10 to 25 percent more for an SUV or a pickup."),
 ("Do you ship cars for people on orders to Fort Meade?","Yes, all year and especially in summer. The base and the agency move tens of thousands of people on assignment cycles. Many families settle in the villages and Fulton. The orders cover one car, and we move the other. Housing on the base is gated, so the driver meets you outside it or at a village center. Ship Guy is a private broker with no connection to the base. Send the report date, and the window is built around it."),
 ("Do you ship cars for people relocating to the cyber firms or the lab?","Yes, every month. The firms in the Gateway business park and along Route 32 hire engineers from every state. The lab in Laurel relocates scientists on program schedules. Many ship a second car behind the move. The handoff works at the Gateway lots or the mall. We provide the paperwork a reimbursed move needs."),
 ("Does a Merriweather concert affect my pickup?","In Town Center, yes. The big nights fill Little Patuxent Parkway and Broken Land from five o’clock. We move a Town Center handoff on a concert night to the daytime or to a village center. The villages themselves run normally."),
 ("Can you ship a car to or from Ellicott City, Fulton, or Laurel?","Yes, and all three price the same as Columbia. Ellicott City rides the same carriers off Route 29 and Route 100. Main Street is closed to a trailer, so the handoff moves to the Route 40 lots. Fulton rides them off 29 at Route 216, and the curb works. Laurel rides them off 95 and Route 1. Send the full address, and we tell you which applies."),
 ("What happens if a snowstorm or a flood hits on my pickup day?","Snow closes 95 a day or two a winter. The carriers park in Jessup until the plows finish. A winter pickup can slip a day, and we call before it does. A big summer storm floods the river gorge in Ellicott City and the low crossings on the Patuxent. A pickup there moves up the hill until the water drops."),
 ("Can you ship a car that does not run from Columbia?","Yes. We send a carrier with a winch and price the loading time into the first quote. The mall lot in Town Center or the Gateway business park gives the driver level pavement. Say whether the car rolls, steers, and brakes."),
 ("Are the tunnel and bridge tolls in my price?","Yes. A carrier bound for the port or the shore pays the tunnels or the Bay Bridge by transponder. The toll rides inside the quote. There is no separate line. Interstate 95 through Howard County and Route 29 carry no toll."),
 ("What do you need for a Columbia car shipping quote?","The two addresses, with the village named. The year, make, and model. Running or not. Open or enclosed. The week around the report date or the closing. Those five answers are the whole request, and the Columbia number is back within the day."),
]
BODY.append(faq_section(FAQ,'Columbia FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Columbia?','Two minutes on the form above gets the lane priced. Name the village and the week, and a carrier already on 95 takes it.','+14107097449','(410) 709-7449','Get your free Columbia quote'))

build({
 'slug':'auto-transport-columbia-maryland',
 'title':'Car Shipping in Columbia, MD — Auto Transport | Ship Guy',
 'meta':'Car shipping in Columbia, MD, the planned city between Baltimore and Washington on Interstate 95. Fort Meade and cyber-firm relocations, village-center handoffs where the cul-de-sacs will not take a trailer, Town Center and Fulton curbside pickups, Ellicott City and Laurel, Merriweather nights, the Ellicott City floods, and the snow. Local office on Guilford Road. Free quote.',
 'h1':'Car Shipping in<br>Columbia, <span class="accent">Maryland</span>',
 'lede':'Open, enclosed, and expedited auto transport across Howard County, planned around 95, Route 29, the village loops, the base calendar, and the winter.',
 'tel':'+14107097449','disp':'(410) 709-7449','brand':'Columbia','keyword':'car shipping in columbia',
 'localterms':['columbia','howard county','planned city','baltimore','washington','interstate 95','route 29','spine','route 32','patuxent freeway','route 175','little patuxent parkway','route 100','route 108','parkway','broken land','cedar lane','hickory ridge','snowden river','dobbin','guilford','gateway','route 1','jessup','elkridge','intercounty connector','town center','mall','lakefront','pavilion','villages','wilde lake','harper’s choice','oakland mills','long reach','owen brown','kings contrivance','dorsey’s search','river hill','cul-de-sac','loop','village center','pool lot','collector road','ellicott city','main street','gorge','route 40','clarksville','horse country','fulton','maple lawn','laurel','lab','racetrack','savage','mill','odenton','base','fort meade','agency','cyber command','civilians','service members','orders','gated','cyber firms','engineers','contract cycles','physics lab','scientists','chemical company','office landlord','hospital','nurses','residents','community college','county schools','federal employees','retirees','concerts','jazz festival','wine festival','arts festival','fourth of july','county fair','west friendship','triathlon','centennial park','2016','2018','floods','2012 derecho','snow','2010','blizzards','philadelphia','richmond','new york','pittsburgh','raleigh','boston','charlotte','orlando','chicago','silver spring','catonsville'],
}, BODY, FAQ)
