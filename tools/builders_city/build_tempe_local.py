import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Tempe, Arizona','Car shipping in the university city at the center of the Valley, boxed in by four freeways',
 ['Car shipping in Tempe runs off the four freeways that frame the city. Ship Guy is a licensed auto transport broker with an office on Lakeshore Drive in the Lakes.',
  'The 10 and the 60 meet at the southwest corner. We book vetted carriers across Tempe and the towns around it, from the campus to Mesa. The trucks belong to the carriers.',
  'Interstate 10 runs the west edge past the airport and the Broadway Curve. US 60 crosses the south side. Loop 101 runs the east edge, and Loop 202 follows Town Lake across the north. Rural Road, Mill Avenue, McClintock, and Priest run north and south between them.',
  'This page covers the freeways, the campus, Mill Avenue, the rail streets, the Lakes, and South Tempe. It also covers move-in week, the towers on the lake, the Ironman, the heat, and the lanes.'],
 'Tempe at a glance',
 ['Most pickups happen within 1 to 3 days, and faster outside of August. Every carrier working the Valley crosses Tempe on the 10 or the 60.',
  'Phoenix is twenty minutes. Tucson, Flagstaff, Las Vegas, and the California coast are a same-day haul. Albuquerque takes a day. Denver takes two, and Chicago and the East Coast take three to four.'],
 'Tell us the side of the 60. The campus, Mill Avenue, and the light rail streets need a meeting spot. The Lakes, South Tempe, and the grids off McClintock usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 10, US 60, Loop 101, Loop 202, Rural Road, and the Light Rail Streets',
 prose(
  L('Tempe is the one Valley city with a freeway on every side. The carriers never have to come far off one.'),
  P('Interstate 10 runs the west edge of the city past the airport. The Broadway Curve is the busiest stretch of road in Arizona. The rebuild that widened it just finished, and the Baseline and Broadway exits serve the west side. US 60 is the Superstition Freeway across the south side, with exits at Priest, Mill, Rural, and McClintock. Every carrier between the East Valley and the 10 uses it.'),
  P('Loop 101 is the Price Freeway along the east edge, from the 202 south to Chandler. Loop 202 is the Red Mountain Freeway along Town Lake across the north. Its exits are Priest, Scottsdale Road, and McClintock. The 143 runs from the 202 to the airport. The four freeways meet at every corner of the city.'),
  P('Rural Road and Scottsdale Road run north and south through the middle, from the 60 to Town Lake. Mill Avenue is downtown and the bridge over the lake. McClintock and Priest run parallel on either side. The light rail runs down Apache Boulevard and Mill, and the streetcar loops downtown. A trailer cannot stop on a rail street. Baseline, Southern, Broadway, University, Elliot, and Warner cross the city east and west.'),
  P('The carriers come off the 60 at Rural and McClintock, and off the 202 at McClintock. The marketplace on Rio Salado, the mall on Baseline, and the stadium district have the usual meeting lots. No road in the Valley charges a toll.'),
  P('Our office is on Lakeshore Drive in the Lakes, between Southern and Baseline, minutes from the 60.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Campus and Mill Avenue, Maple-Ash, North Tempe and the Lake, the Rail Corridor, the Lakes, South Tempe, and Guadalupe',
 prose(
  L('Tempe is a college town inside a grid of postwar neighborhoods. The campus sets the rules for the north half.'),
  P('The campus fills the middle of the city from University Drive to Apache. Mill Avenue beside it is downtown, a narrow strip of bars with the streetcar down the middle. A trailer cannot enter either. The driver meets you at a campus lot off Rural, at the marketplace, or at the stadium lots. Maple-Ash west of Mill is a historic district of narrow streets under old trees. The handoff moves to University Drive.'),
  P('North Tempe along the lake is the office towers, the arts center, and the apartments on Rio Salado. The lots by the lake work for a handoff. The rail corridor along Apache from Mill to the 101 is student apartments and no-stopping zones. The handoff moves to a lot on Apache or at the marketplace. Papago Park and the airport side to the west are open ground.'),
  P('The grids between Broadway and Baseline are the postwar neighborhoods, from Hughes Acres to McClintock Manor and Broadmor. The streets are wide, and the curb works. The Lakes off Baseline and Rural is a lake community with winding streets. The truck reaches the curb on the main loops. The driver meets you on Lakeshore for the rest.'),
  P('South Tempe between Baseline and the Chandler line has the bigger lots off Warner and Elliot. The research park and the Buttes sit there too. The truck reaches the curb. Guadalupe is its own town inside Tempe, with narrow streets, and the driver meets you on Priest. Ahwatukee across the 10 and Mesa across the 101 price the same as Tempe. So does Chandler to the south.'),
 )))

ROUTES=[("Phoenix, AZ","I-10/Loop 202 · ~10 mi","Same day","$120–$200"),("Tucson, AZ","I-10 · ~105 mi","Same day","$150–$240"),
 ("Flagstaff, AZ","I-17 · ~150 mi","1 day","$170–$280"),("Las Vegas, NV","US-60/US-93 · ~295 mi","1 day","$280–$410"),
 ("San Diego, CA","I-10/I-8 · ~355 mi","1 day","$340–$490"),("Los Angeles, CA","I-10 · ~375 mi","1 day","$350–$500"),
 ("Albuquerque, NM","I-17/I-40 · ~450 mi","1 day","$400–$570"),("Denver, CO","I-17/I-40/I-25 · ~820 mi","2 days","$560–$800"),
 ("Chicago, IL","I-40/I-44/I-55 · ~1,750 mi","3–4 days","$1,000–$1,450"),("Seattle, WA","I-10/I-5 · ~1,430 mi","3 days","$950–$1,350")]
BODY.append(rate_table('Lanes &amp; Costs','Tempe Car Shipping Lanes and Estimated Costs',
 'The lanes Tempe cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Tempe for a sedan that runs, open trailer. SUVs and pickups add 10 to 25 percent, and enclosed adds more. August and the snowbird months run higher. Carrier availability on your dates sets the final number.',
 prose(
  P('Tempe prices with Phoenix on every lane. The carriers cross the city on the 10 and the 60 on every Valley run. The California lanes run daily in both directions. The Chicago and East Coast lanes fill with student cars each August and May. The price climbs with them.'),
  P('From October through April, the inbound snowbird cars take the space, and outbound space runs short. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Insurer on the Lake, the Tech Campuses, the Car Retailer, and the Utility',
 prose(
  L('Tempe moves on the academic calendar first and the corporate calendar second. The university accounts for more cars than anyone.'),
  P('The university is the largest campus in the country. It brings tens of thousands of students in each August. Many ship a car from California, Chicago, Texas, or the East Coast. A parent books, and an adult signs at a campus lot or the marketplace. The handoff never happens on Mill Avenue or a rail street. Faculty hires land each summer with a closing date and a second car. The paperwork for a reimbursed move comes from us.'),
  P('The insurer’s regional headquarters on the lake holds thousands of employees. It moves claims staff and analysts in from every state. The technology companies in the research park and on Rio Salado relocate engineers on their own calendars. The online car retailer headquartered in town moves its own people constantly.'),
  P('The utility headquartered on the east side moves linemen and engineers between service areas. The hospital on Apache brings in nurses on contracts all year. The airline operations center on the west side rotates staff on the flight calendar. The hotels along the lake hire managers on short notice.'),
  P('Graduates leave for the coasts and Texas each May, and the car goes ahead of them. Snowbirds fill the apartments on the lake from October through April. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side. Ship Guy is a private broker with no military connection, and the <a href="military-car-shipping.html">military</a> page covers the Luke timing.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Move-In Week, Football Saturdays, the Ironman, Spring Training, the Monsoon, and the Heat',
 prose(
  L('Tempe runs on an August move-in, a fall of football Saturdays, and a summer that bends the schedule.'),
  P('Move-in week in August brings thousands of cars onto the campus streets in a few days. The university closes the campus roads to trucks, and the police run one-way loops around the dorms. A carrier delivering that week meets you at the marketplace or a lot off the 60. We book move-in deliveries for the week before or after when the dates allow.'),
  P('Football Saturdays fill the stadium lots and every street between Mill and Rural from September through November. The arts festival closes Mill Avenue for a weekend in December and again in March. The Ironman takes over the lake and the bridges on a Sunday in November. The marathon in February does the same. The music festival fills the beach park in late winter. A handoff downtown on any of those days moves to the morning or to another lot.'),
  P('Spring training brings the Angels to the stadium on 48th Street from February into March. The lots fill by ten. The run around the stadium in April puts thirty thousand people on the streets for a morning. Graduation in May fills the hotels and sends cars out in every direction.'),
  P('The heat is the weather. Summer passes one hundred ten degrees for weeks, and the loading hour moves to dawn. The monsoon runs July into September, and a dust storm closes the freeways for an hour. The 2014 storm put the Broadway Curve under water, and a flash flood still closes the low crossings. Winter is the easy season, and the snowbirds take the carrier space from October through April.'),
 )+chips(["Downtown","Mill Avenue","ASU","Campus","Maple-Ash","Mitchell Park","University Park","North Tempe","Town Lake","Rio Salado","Marina Heights","Marketplace","Papago Park","Apache Boulevard","Rail Corridor","Escalante","Hughes Acres","McClintock Manor","Broadmor","Tempe Gardens","Clark Park","Shalimar","The Lakes","Lakeshore","Kiwanis Park","Baseline","Arizona Mills","South Tempe","Warner Ranch","The Buttes","Research Park","Guadalupe","Ahwatukee","Mesa","Chandler"])
 +NOTE('Serving Tempe, Guadalupe, and the center of the Valley, campus block or lake loop. Tell us the side of the 60 and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Tempe?',
 prose(
  L('Open trailers carry most of the cars that leave Tempe, and the table above assumes one.'),
  P('An enclosed trailer keeps the sun, the dust, and the road grit off a car. Parents sending a new car to a student from the coast book one. Collectors in the Lakes and on the Buttes book one for the shows in Scottsdale each January.'),
  P('A student commuter or a work truck goes open and arrives fine, dust and all. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the marketplace or a campus lot, and a signature at delivery. The move-in date sets the week.'),
  P('Once you approve the price, the car goes to a carrier already crossing the Valley. The meeting lot and the window follow the same day. At pickup you and the driver go around the car together. Every existing mark goes on the Bill of Lading. Two signatures close it, and the far end is checked against it.'),
 )+ULI([
  "Clear the cabin and the trunk of everything personal, including the dorm boxes",
  "Leave the fuel near a quarter tank",
  "Photograph every panel and the odometer before the handoff",
  "Give the driver one working key and name any mechanical fault",
  "Disarm any aftermarket alarm",
  "On the campus or a rail street, meet the truck at a campus lot or the marketplace",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Tempe Drivers Choose Ship Guy',
 prose(
  L('We load the carriers already crossing the Valley on the 10 and the 60. We plan around move-in week, the football Saturdays, and the heat.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both on the federal register. Our office is on Lakeshore Drive in the Lakes.'),
  P('One coordinator carries the move from the first number to the last signature. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Tempe','4500 S Lakeshore Dr #458B','Tempe, AZ 85282','+19284926068','(928) 492-6068','MST',
 '4500+S+Lakeshore+Dr+%23458B,+Tempe,+AZ+85282','Visit Us','Find Ship Guy in Tempe',
 'Our office is on Lakeshore Drive in the Lakes, between Southern and Baseline, minutes from the 60.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5123.2199476349815!2d-111.92610859999999!3d33.3812131!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x872b07536a88701f%3A0xaba22445f694ccdf!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025142549!5m2!1sen!2sus'))

FAQ=[
 ("Can you ship my student’s car to ASU for move-in?","Yes, and it is the move we make most. Cars come from California, Chicago, Texas, and the East Coast each August. A parent books, and an adult signs for the car at a campus lot or the marketplace. We deliver the week before or after move-in week when the dates allow. The campus roads close to trucks that week. Graduation in May sends the cars home the same way."),
 ("How much does it cost to ship a car from Los Angeles or Chicago to Tempe?","Los Angeles runs three hundred fifty to five hundred dollars for a sedan. That is about three hundred seventy-five miles on the 10. Chicago runs one thousand to fourteen hundred fifty, about seventeen hundred fifty miles on 40 and 55. August and the snowbird months price above the rest of the year. Figure 10 to 25 percent more for an SUV or a pickup."),
 ("Can the carrier come to my street on the campus or Mill Avenue?","No. The campus roads, Mill Avenue, and the rail streets on Apache give a trailer nowhere to stop. The driver meets you at a campus lot off Rural, at the marketplace, or at the stadium lots. The Lakes, South Tempe, and the grids off McClintock usually allow the curb."),
 ("Do you ship cars for people relocating to the insurer on the lake or the tech campuses?","Yes, every month. The regional headquarters on the lake moves claims staff and analysts from every state. The research park and the towers on Rio Salado move engineers on their own calendars. Many ship a second car behind the move. The handoff works at the lake lots or the marketplace. We provide the paperwork a reimbursed move needs."),
 ("Do football Saturdays or the Ironman affect my pickup?","Downtown and around the stadium, yes. Football Saturdays fill every street between Mill and Rural from the morning. The Ironman closes the lake and the bridges on a Sunday in November. We move a downtown handoff on those days to the morning or to a lot off the 60. The rest of the city runs normally."),
 ("Can you ship a car to or from Guadalupe, Ahwatukee, or Mesa?","Yes, and all three price the same as Tempe. Guadalupe sits inside Tempe, and the driver meets you on Priest. Ahwatukee rides the same carriers off the 10, and Mesa rides them off the 60 and the 101. Send the full address, and we tell you which handoff applies."),
 ("What happens if a dust storm or a flash flood hits on my pickup day?","A dust storm closes the freeways for an hour, and the driver waits it out. A flash flood closes the low crossings and sometimes the Broadway Curve, as it did in 2014. The pickup slides to the next morning. Summer loading happens at dawn, before the heat. Any change reaches you before it happens."),
 ("Can you ship a car that does not run from Tempe?","Yes. We send a carrier with a winch, and the loading time is in the quote from the start. The marketplace lot or the mall lot on Baseline gives the driver level pavement. Tell us whether the car rolls, steers, and brakes."),
 ("Can you ship a graduate’s car out of Tempe in May?","Yes. The graduates scatter to California, Texas, and the East Coast each May. The car follows the week after finals. The handoff happens at a campus lot or the marketplace. Reserve in April, since the May trucks are spoken for early. If the graduate has already flown, an adult signs at pickup."),
 ("What do you need for a Tempe car shipping quote?","Where the car is and where it goes, with the side of the 60 or the campus lot. What it is, year through model. Whether it starts. Open or enclosed. The week around move-in or the start date. Five answers, and the Tempe number is back within the day."),
]
BODY.append(faq_section(FAQ,'Tempe FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Tempe?','The form above prices the lane in two minutes. Give us the side of the 60 and the week. A carrier already crossing the Valley takes it.','+19284926068','(928) 492-6068','Get your free Tempe quote'))

build({
 'slug':'auto-transport-tempe-arizona',
 'title':'Car Shipping in Tempe, AZ — Auto Transport | Ship Guy',
 'meta':'Car shipping in Tempe, AZ, the university city framed by the 10, the 60, the 101, and the 202. ASU move-in and graduation moves, relocations to the insurer on the lake and the tech campuses, campus and Mill Avenue meeting spots, Lakes and South Tempe curbside pickups, football Saturdays, the Ironman, the monsoon, and the heat. Local office on Lakeshore Drive. Free quote.',
 'h1':'Car Shipping in<br>Tempe, <span class="accent">Arizona</span>',
 'lede':'Open, enclosed, and expedited auto transport at the center of the Valley, planned around the four freeways, move-in week, football Saturdays, and the heat.',
 'tel':'+19284926068','disp':'(928) 492-6068','brand':'Tempe','keyword':'car shipping in tempe',
 'localterms':['tempe','valley','interstate 10','broadway curve','us 60','superstition','loop 101','price freeway','loop 202','red mountain','town lake','143','airport','rural road','scottsdale road','mill avenue','mcclintock','priest','apache','light rail','streetcar','baseline','southern','broadway','university drive','elliot','warner','downtown','campus','asu','university','maple-ash','north tempe','office towers','arts center','rio salado','marketplace','papago','rail corridor','student apartments','hughes acres','mcclintock manor','broadmor','the lakes','lakeshore','south tempe','research park','buttes','guadalupe','ahwatukee','mesa','chandler','stadium','students','parent','campus lot','faculty','insurer','headquarters','claims','technology','engineers','car retailer','utility','linemen','hospital','nurses','airline','operations center','hotels','graduates','snowbirds','move-in week','football saturdays','arts festival','ironman','marathon','music festival','spring training','angels','48th street','run','graduation','heat','one hundred ten','monsoon','dust storm','2014','flash flood','phoenix','tucson','flagstaff','las vegas','san diego','los angeles','albuquerque','denver','chicago','seattle','california','texas','east coast','scottsdale'],
}, BODY, FAQ)
