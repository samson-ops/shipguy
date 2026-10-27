import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–2 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Ann Arbor, Michigan','Car shipping forty miles west of Detroit, in a university town where the stadium holds more people than the city',
 ['Car shipping in Ann Arbor runs off Interstate 94 to the south and US 23 to the east. Ship Guy is a licensed auto transport broker with an office on Venture Drive on the south side.',
  'We book vetted carriers across Washtenaw County, from Dexter and Chelsea to Ypsilanti and Saline. The trucks belong to the carriers, and we hold the authority and the bond.',
  'Interstate 94 runs the south edge with exits at Jackson Road, Ann Arbor-Saline Road, and State Street. US 23 is the freeway along the east side to Toledo and Flint. M-14 crosses the north side toward Plymouth and Detroit. Washtenaw Avenue is the main road east to Ypsilanti.',
  'This page covers 94, 23, downtown, the Old West Side, Burns Park, the townships, and Ypsilanti. It also covers the hospital, the research centers, football Saturdays, the art fair, and the lanes.'],
 'Ann Arbor at a glance',
 ['Most pickups happen within 1 to 2 days. The Detroit carrier pool is forty minutes east on 94. The Chicago trucks pass the city on the same road all day.',
  'Detroit, Toledo, Grand Rapids, and Chicago are a same-day haul, and so are Cleveland and Columbus. Indianapolis and Pittsburgh take a day. New York takes two, and Florida takes three to four.'],
 'Tell us the neighborhood. Downtown, the campus, the Old West Side, and Burns Park need a meeting spot. The north side off Plymouth Road, the south side, and the townships usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 94, US 23, M-14, Washtenaw, State Street, and Stadium Boulevard',
 prose(
  L('Ann Arbor sits where the Chicago road meets the Toledo road. The carriers reach it from three directions.'),
  P('Interstate 94 runs along the south side of the city between Detroit and Chicago. The exits at Jackson Road, Ann Arbor-Saline Road, and State Street serve the city. Every carrier between the two cities passes them. The airport is twenty-five minutes east on 94, and Detroit is forty. The Chicago carriers come through Jackson and Battle Creek on the same road.'),
  P('US 23 is the freeway along the east side from Toledo to Flint. Its exits are Washtenaw, Geddes, and Plymouth Road. The state widened it with a rush-hour lane, and it still backs up at the 94 interchange. M-14 leaves 23 on the north side and runs east to Plymouth, Livonia, and the 275 corridor. Toledo and the Ohio carriers come up 23 in an hour.'),
  P('Washtenaw Avenue is the old road east to Ypsilanti, four lanes of retail the whole way. State Street and Main Street run north and south through downtown and out to 94. Stadium Boulevard loops the south and west sides past the stadium. Plymouth Road carries the north side and the research campus. Huron Street, Packard, and Jackson Road are the rest of the grid.'),
  P('The carriers come off 94 at State Street and off 23 at Washtenaw. The mall lots at State and 94 are the usual meeting spot. So are the park and rides on Plymouth Road and State Street, and the lots on Jackson Road. The stadium lots on Main work outside football Saturdays. No road in Washtenaw County charges a toll.'),
  P('Our office is on Venture Drive on the south side, a minute from the 94 exit.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown and the Campus, Kerrytown, the Old West Side, Burns Park, the North Side, the South Side, Ypsilanti, Saline, and Dexter',
 prose(
  L('Ann Arbor is a campus with a city wrapped around it. The closer you live to the Diag, the farther the truck parks.'),
  P('Downtown and the central campus share a grid of one-way streets, bus lanes, and no-stopping zones. A trailer cannot work any of it. The driver meets you at the mall lots, at a park and ride, or on Stadium Boulevard. Kerrytown north of downtown is the market district, with narrow streets and the farmers’ market. The handoff moves to the lot by the market or to Main.'),
  P('The Old West Side is a historic district of narrow streets and big houses under old trees. Burns Park south of the campus is the same. Water Hill and the Northside are older grids with parked cars on both sides. The handoff for all of them moves to Stadium Boulevard, Main Street, or the stadium lots.'),
  P('The north side along Plymouth Road is the research campus, the office parks, and newer subdivisions. The curb works on most of them. The south side off State Street and Ann Arbor-Saline Road is the same, with wide loops. The township subdivisions in Pittsfield and Scio are the widest of all, and the driver reaches the house.'),
  P('Ypsilanti sits ten minutes east with the state university, the old Depot Town, and narrow streets around both. The handoff moves to Washtenaw or Michigan Avenue. Saline to the south, Dexter to the west, and Chelsea beyond it are small towns. Each has wide new subdivisions and lots on the main road. Milan, Manchester, and Whitmore Lake are the edges of the county. All of them price the same as Ann Arbor, and so does Detroit at the end of 94.'),
 )))

ROUTES=[("Detroit, MI","I-94 · ~40 mi","Same day","$130–$210"),("Toledo, OH","US-23 · ~50 mi","Same day","$140–$230"),
 ("Grand Rapids, MI","I-94/I-96 · ~130 mi","Same day","$190–$300"),("Cleveland, OH","US-23/I-80 · ~170 mi","Same day","$220–$340"),
 ("Columbus, OH","US-23 · ~190 mi","Same day","$230–$350"),("Chicago, IL","I-94 · ~240 mi","Same day","$250–$370"),
 ("Indianapolis, IN","I-94/I-69 · ~260 mi","1 day","$260–$390"),("Pittsburgh, PA","US-23/I-80/I-79 · ~280 mi","1 day","$270–$400"),
 ("New York, NY","I-80 · ~600 mi","2 days","$470–$680"),("Tampa, FL","US-23/I-75 · ~1,150 mi","3–4 days","$800–$1,150")]
BODY.append(rate_table('Lanes &amp; Costs','Ann Arbor Car Shipping Lanes and Estimated Costs',
 'The lanes Washtenaw County cars run most often, with estimated open-trailer ranges. Put your exact route on the form above for a number.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Ann Arbor, sedan that runs, open trailer. An SUV or a pickup lands 10 to 25 percent higher, and enclosed lands higher again. The week, the direction, and the carriers free on your dates set the final number.',
 prose(
  P('Ann Arbor prices with Detroit on every lane. The Motor City carriers reach it in forty minutes on 94. It runs a little under Detroit to Chicago and about the same to Ohio. The Toledo lane is an hour down 23 and runs all day. The Florida lane fills with snowbirds and retiring faculty each fall.'),
  P('A move timed to a football Saturday or the art fair costs more. The carriers avoid the city those days. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Hospital, the Research Centers, the Suppliers, and the Pizza Chain',
 prose(
  L('Ann Arbor relocates professors, physicians, engineers, and fifty thousand students. The university is the largest employer in the county by a wide margin.'),
  P('The university brings its students in during the last week of August. It sends them home in late April. The parent sets up the shipment, and an adult meets the driver at a campus lot. Faculty and staff hires land each summer with a closing date and a second car. The state university in Ypsilanti and the community college on the south side run the same calendar.'),
  P('The hospital system on the medical campus hires traveling nurses all year and takes new residents each June. The physicians and the researchers come with a closing date and a second car to ship. The hospital in Superior Township recruits the same way. We supply the paperwork a reimbursed move needs.'),
  P('The automakers keep their research centers here. The Japanese automaker’s technical center south of the city rotates engineers on program schedules. So do the Korean automaker’s center in Superior Township and the mobility test track at Willow Run. The seat and electronics suppliers in Saline and the tech firms downtown hire from every state. The pizza chain headquartered on the north side moves managers in on its own calendar.'),
  P('Families from Detroit and Chicago buy in Saline, Dexter, and the townships on closing dates. One car rides the trailer while the other is driven. Retirees and emeritus faculty leave for Florida and Arizona each fall. The <a href="state-to-state-car-shipping.html">state-to-state</a> page has the interstate side. Ship Guy is a private broker and not part of any base. An order to Selfridge is covered on the <a href="military-car-shipping.html">military</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Football Saturdays, Move-In, Commencement, the Art Fair, the Ice Storms, and the Snow',
 prose(
  L('Ann Arbor runs on seven football Saturdays and a four-day art fair. The winter comes with ice as often as snow.'),
  P('The stadium holds one hundred ten thousand, more people than live in the city. On a home Saturday the roads close around it from the morning. Every lot within two miles is sold. A handoff near the stadium on a football weekend moves to Friday or to the north side. The night games empty the city after midnight.'),
  P('The art fair closes downtown and the campus streets for four days in July. It draws half a million people. A downtown handoff that week moves to the mall lots or to the week before. Move-in week at the end of August fills every campus street. Commencement fills the stadium and the hotels for a weekend at the start of May.'),
  P('Winter brings sixty inches of snow and an ice storm every few years. The February 2023 ice storm took the power out across the county for most of a week. It brought the trees down on the Old West Side. The March 2017 windstorm did the same. The carriers wait at the Baker Road truck stop until the plows and the crews finish. A winter pickup can lose a day.'),
  P('The 2014 polar vortex froze the diesel in the trucks, and the carriers lost a week. The Huron floods the river parks in a wet spring. A pickup on the river road moves up the hill. Summer brings a storm every few afternoons and the occasional siren. A warning pauses the loading until it clears.'),
 )+chips(["Downtown","Central Campus","The Diag","Kerrytown","Old West Side","Burns Park","Water Hill","Northside","North Campus","Plymouth Road","Medical Campus","State Street","Briarwood","Stadium Boulevard","Main Street","Packard","Washtenaw","Jackson Road","Pittsfield","Scio","Ypsilanti","Depot Town","Saline","Dexter","Chelsea","Milan","Manchester","Whitmore Lake","Superior Township","Willow Run","Canton","Plymouth"])
 +NOTE('Serving Ann Arbor and all of Washtenaw County, campus block or township subdivision. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Ann Arbor?',
 prose(
  L('Open trailers carry most cars that leave Washtenaw County, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the road salt, the gravel, and the ice. The collectors who fill the rolling sculpture show downtown book one. Engineers shipping a prototype or a new car to the research centers book one too.'),
  P('A commuter car or a student’s sedan does fine on an open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages put the two next to each other.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot at the mall or a park and ride, and a signature at delivery. The start date or the move-in date picks the week.'),
  P('Take the number, and the car is matched to a carrier already running 94 between Detroit and Chicago. The lot and the window are confirmed the same day. At pickup the driver goes around the car with you and writes down every existing mark. That Bill of Lading gets two signatures and is checked again at delivery.'),
 )+ULI([
  "Personal items removed from the cabin and the trunk",
  "Tank at about a quarter",
  "Four sides and the odometer photographed before the truck comes",
  "One working key for the driver, with any mechanical issue mentioned",
  "Aftermarket alarm disabled",
  "Downtown or in the Old West Side, meet the truck at the mall lots or on Stadium Boulevard",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Ann Arbor Drivers Choose Ship Guy',
 prose(
  L('We book the Detroit carriers before they leave the metro and the Chicago carriers passing on 94. We plan around the football calendar and the ice.'),
  P('Ship Guy’s FMCSA brokerage authority and $75,000 surety bond are a matter of public record. Our office is on Venture Drive.'),
  P('From the first quote through delivery, you deal with one person. The <a href="services.html">services</a> page covers open, enclosed, and expedited transport.'),
 )))

BODY.append(office('Ann Arbor','4750 Venture Dr #522','Ann Arbor, MI 48108','+17342121989','(734) 212-1989','ET',
 '4750+Venture+Dr+%23522,+Ann+Arbor,+MI+48108','Visit Us','Find Ship Guy in Ann Arbor',
 'Our office is on Venture Drive on the south side, a minute from the 94 exit.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4543.839548487155!2d-83.73266679999999!3d42.2178147!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x883ca5255495afd5%3A0xc6d82bd48732240d!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793103227633!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Ann Arbor to Chicago or New York?","Chicago runs two hundred fifty to three hundred seventy dollars for a sedan. That is about two hundred forty miles west on 94. New York runs four hundred seventy to six hundred eighty, about six hundred miles on 80. Detroit is forty minutes away and the lowest of the three. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street downtown, in Burns Park, or on the Old West Side?","Usually not. Downtown and the campus are one-way streets and no-stopping zones. Burns Park and the Old West Side are narrow streets under old trees. The driver meets you at the mall lots, at a park and ride, or on Stadium Boulevard. The north side off Plymouth Road, the south side, and the townships usually allow the curb."),
 ("Can you deliver on the Michigan move-in date?","Yes. The university takes cars in during the last week of August and sends them home in late April. A parent books the car, and an adult over eighteen signs for it at a campus lot. The window is matched to move-in day and moves with it. The campus streets close that week, so the handoff happens at the park and ride on State Street."),
 ("Does a football Saturday or the art fair affect my pickup?","Near the stadium and downtown, yes. The stadium holds one hundred ten thousand. The roads around it close from the morning on a home Saturday. The art fair closes downtown for four days in July. We move a handoff near either to Friday, to the north side, or to the week before. The townships run normally."),
 ("Can you ship a car to or from Ypsilanti, Saline, or Dexter?","Yes, and all three price the same as Ann Arbor. Ypsilanti rides the same carriers off 94 and Washtenaw. The handoff moves off the narrow streets by the campus and Depot Town. Saline rides them off Ann Arbor-Saline Road, and the curb works on the new streets. Dexter rides them off 94 at Baker Road. Send the full address for a township subdivision."),
 ("Do you ship cars for people relocating to the hospital or the research centers?","Yes, every month. The hospital system hires traveling nurses all year and takes residents each June. The automakers’ research centers rotate engineers on program schedules. Many ship a second car behind the move. The handoff works at the park and ride on Plymouth Road or the mall lots. We supply the paperwork a reimbursed move needs."),
 ("What happens if an ice storm hits on my pickup day?","The carriers wait at the Baker Road truck stop until the plows and the line crews finish. A winter pickup can slip a day, and you hear it from us first. The February 2023 storm took the power out for most of a week. The trees came down on the older streets. A pickup on a blocked street moves to the main road."),
 ("Can you ship a car that does not run from Ann Arbor?","Yes. A carrier with a winch is booked, and the longer loading is inside the number from the start. The mall lots at State and 94 or the park and ride lots give the driver level ground. Say whether the car rolls, steers, and brakes."),
 ("Can you ship a snowbird’s car to Florida each fall?","Yes, and from October through December it is the busiest lane out of the county. A sedan to Tampa runs eight hundred to eleven hundred fifty dollars. The cars return between March and May. In the fall, book two weeks out, since the southbound trucks fill first. The seasonal lane is covered on the <a href=\"/snowbird-car-shipping\">snowbird</a> page."),
 ("What do you need for an Ann Arbor car shipping quote?","The two addresses, with the neighborhood or the township. The year, make, and model. Whether it runs. Open or enclosed. The week around the start date or move-in day. That is the whole request, and the Ann Arbor number is back within the day."),
]
BODY.append(faq_section(FAQ,'Ann Arbor FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Ann Arbor?','Your lane gets a number on the form above in about two minutes. Give us the neighborhood and the week, and a carrier already on 94 takes it.','+17342121989','(734) 212-1989','Get your free Ann Arbor quote'))

build({
 'slug':'auto-transport-ann-arbor-michigan',
 'title':'Car Shipping in Ann Arbor, MI — Auto Transport | Ship Guy',
 'meta':'Car shipping in Ann Arbor, MI, forty miles west of Detroit on Interstate 94. Michigan move-in and commencement timing, mall-lot and park-and-ride handoffs for downtown, Burns Park, and the Old West Side, curbside pickups on the north and south sides, Ypsilanti and Saline, football Saturdays, the art fair, and the ice storms. Local office on Venture Drive. Free quote.',
 'h1':'Car Shipping in<br>Ann Arbor, <span class="accent">Michigan</span>',
 'lede':'Open, enclosed, and expedited auto transport across Washtenaw County, planned around 94, 23, the campus calendar, the stadium, and the winter.',
 'tel':'+17342121989','disp':'(734) 212-1989','brand':'Ann Arbor','keyword':'car shipping in ann arbor',
 'localterms':['ann arbor','washtenaw county','interstate 94','us 23','venture drive','state street','dexter','chelsea','ypsilanti','saline','jackson road','ann arbor-saline road','toledo','flint','m-14','plymouth','washtenaw avenue','airport','detroit','chicago','battle creek','geddes','plymouth road','rush-hour lane','livonia','275','four lanes','main street','stadium boulevard','research campus','huron street','packard','mall','park and ride','stadium','toll','downtown','central campus','the diag','one-way','bus lanes','no-stopping','kerrytown','farmers’ market','old west side','burns park','water hill','northside','office parks','pittsfield','scio','state university','depot town','michigan avenue','milan','manchester','whitmore lake','grand rapids','cleveland','columbus','indianapolis','pittsburgh','new york','tampa','snowbirds','professors','physicians','engineers','fifty thousand','students','faculty','community college','hospital','medical campus','traveling nurses','residents','superior township','automakers','technical center','korean','willow run','test track','suppliers','tech firms','pizza chain','emeritus','selfridge','football saturdays','one hundred ten thousand','night games','art fair','half a million','move-in','commencement','sixty inches','ice storm','february 2023','march 2017 windstorm','baker road','2014 polar vortex','diesel','huron','river parks','siren','rolling sculpture','prototype','bill of lading','fmcsa','surety bond','canton','briarwood','north campus'],
}, BODY, FAQ)
