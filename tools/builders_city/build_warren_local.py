import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–2 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Warren, Michigan','Car shipping in the first suburb north of 8 Mile, where the Tech Center and the truck plant keep the carriers close',
 ['Car shipping in Warren runs off 696 at 11 Mile and the plants on Mound Road. Ship Guy is a licensed auto transport broker with an office on Mound Road at 13 Mile.',
  'We arrange vetted carriers across Macomb County, from 8 Mile to Sterling Heights and east to Roseville. The trucks belong to the carriers.',
  'Interstate 696 is the Reuther Freeway across the middle of the city. Interstate 94 passes the southeast corner, and Interstate 75 runs five minutes west. Van Dyke is M-53, the main road north. Mound Road is the plant corridor beside it. The mile roads from 8 to 14 cross the grid.',
  'This page covers 696, Van Dyke and Mound, the bungalows, the Tech Center district, and the suburbs. It also covers the design campus, the arsenal, the truck plant, the 696 rebuild, and the lanes.'],
 'Warren at a glance',
 ['Most pickups happen within 1 to 2 days. The carriers that deliver new trucks from the Mound plants take private cars on the way back. Warren has more of them than any suburb.',
  'Toledo is an hour. Cleveland, Columbus, and Chicago are a same-day haul. Indianapolis and Pittsburgh take a day. Nashville and New York take two, and Florida takes three.'],
 'Tell us the side of 696. The south side bungalow grids need a meeting spot. The north side, the Tech Center district, and Sterling Heights usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 696, Van Dyke, Mound Road, the Mile Roads, and the Rebuild',
 prose(
  L('Warren is a grid of mile roads with a freeway through the middle. The car haulers run it every shift change.'),
  P('Interstate 696 crosses the city east and west at 11 Mile. Its exits are Dequindre, Mound, Van Dyke, Hoover, Schoenherr, and Groesbeck. The state is rebuilding 696 across Macomb County, and the lane closures run through 2027. The carriers plan around them. Interstate 94 passes the southeast corner at the Groesbeck interchange. Interstate 75 runs five minutes west through Hazel Park.'),
  P('Van Dyke is M-53, the main road north from Detroit through the city to Sterling Heights and Utica. Mound Road runs beside it as the plant corridor, rebuilt from 8 Mile to the county line. Ryan, Hoover, Schoenherr, and Hayes run north and south through the grid. Dequindre is the west edge, and Groesbeck is M-97 across the southeast.'),
  P('The mile roads cross the city from 8 Mile at the Detroit line to 14 Mile. 12 Mile carries the Tech Center and the civic center. 11 Mile runs beside the freeway past the arsenal. 9 Mile and 10 Mile cross the south side past the truck plant. Chicago Road and Martin Road fill in between.'),
  P('The carriers come off 696 at Mound and Van Dyke, and off 94 at Groesbeck. The civic center on Van Dyke and the shopping centers on 12 Mile are the usual meeting spots. The lots by the Mound exit work too. No road in Macomb County charges a toll.'),
  P('Our office is on Mound Road at 13 Mile, a mile north of the Tech Center.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','South Warren, Center Line, the Tech Center District, North Warren, and the Macomb Suburbs',
 prose(
  L('Warren is a postwar city of bungalows and ranches. The farther north the street, the wider it runs.'),
  P('South Warren between 8 Mile and 10 Mile is the oldest part of the city. It is a dense grid of 1940s bungalows on narrow streets with cars on both sides. A trailer fits the mile roads and little else. The driver meets you on Van Dyke, on 9 Mile, or at a shopping center lot. Center Line is its own small city inside the grid at 10 Mile. The handoff works the same way.'),
  P('The Tech Center district at 12 Mile holds the design campus, the civic center, and the hospital. There is room everywhere. The grids between 10 Mile and 12 Mile are 1950s ranches on wider streets. The curb works on most blocks. The arsenal sits at 11 Mile, and the handoff happens outside its gate.'),
  P('North Warren between 12 Mile and 14 Mile is 1960s and 1970s ranches and colonials on wide streets. The truck reaches the curb. The subdivisions off Mound and Ryan north of 13 Mile are the newest in the city. The streets are wide. The industrial blocks along Mound and Groesbeck have lots at every gate.'),
  P('Sterling Heights north of 14 Mile has the second truck plant, the mall, and subdivisions to M-59. The curb works. Madison Heights and Hazel Park to the west are the same grid in Oakland County. Roseville, Eastpointe, and St. Clair Shores to the east are older grids, and the handoff moves to Gratiot. Clinton Township and Fraser to the northeast allow the curb. All of them price the same as Warren, and so does Detroit south of 8 Mile.'),
 )))

ROUTES=[("Toledo, OH","I-75 · ~70 mi","Same day","$150–$240"),("Cleveland, OH","I-75/I-80 · ~175 mi","Same day","$220–$340"),
 ("Columbus, OH","I-75/US-23 · ~210 mi","Same day","$230–$350"),("Chicago, IL","I-94 · ~290 mi","1 day","$260–$390"),
 ("Indianapolis, IN","I-69 · ~300 mi","1 day","$270–$400"),("Pittsburgh, PA","I-75/I-80/I-79 · ~290 mi","1 day","$270–$400"),
 ("Nashville, TN","I-75/I-65 · ~540 mi","1–2 days","$440–$630"),("New York, NY","I-80 · ~620 mi","2 days","$470–$680"),
 ("Atlanta, GA","I-75 · ~730 mi","2 days","$500–$730"),("Tampa, FL","I-75 · ~1,200 mi","3–4 days","$800–$1,150")]
BODY.append(rate_table('Lanes &amp; Costs','Warren Car Shipping Lanes and Estimated Costs',
 'The lanes Macomb County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Warren, open trailer, sedan that runs. SUVs and pickups land 10 to 25 percent higher, enclosed higher again. The snowbird months and a plant launch move the number. The carriers free on your dates settle the final figure.',
 prose(
  P('Warren prices with Detroit on every lane, because it sits inside the Motor City carrier pool. The plant carriers that deliver new trucks from Mound Road take private cars on the return run. That keeps the Ohio and Chicago lanes full. The Florida lane rides the snowbird calendar, higher in October and lower in April.'),
  P('A model launch at the truck plant pulls the carriers off the private lanes for a week. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Tech Center, the Arsenal, the Truck Plant, the Hospital, and the Suppliers',
 prose(
  L('Warren relocates engineers, Army civilians, plant supervisors, and nurses. The design campus moves more people than anyone in Macomb County.'),
  P('The automaker’s technical center at 12 Mile and Van Dyke holds twenty thousand engineers and designers. They arrive on program schedules from every state and from overseas. Many ship a car behind the move. The company pays for the move, and the paperwork for a reimbursed shipment comes from us.'),
  P('The Army arsenal on 11 Mile designs and buys the ground vehicles for the whole force. It moves civilians and officers in on assignment cycles, and the orders cover one car. We move the other. Ship Guy is a private broker with no connection to the arsenal. The <a href=\"military-car-shipping.html\">military</a> page covers the timing.'),
  P('The truck plant and the stamping plant on Mound move supervisors and skilled trades on launch schedules. The suppliers along Mound and Groesbeck do the same. The hospital on 12 Mile brings in nurses on contracts all year. The community college beside it brings cars in each August.'),
  P('Families from Detroit and from overseas buy in North Warren and Sterling Heights on closing dates. One car ships while the other is driven. Retirees leave for Florida each October. The <a href=\"state-to-state-car-shipping.html\">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Shift Changes, the Dream Cruise, the 696 Rebuild, the 2014 Flood, and the Salt',
 prose(
  L('Warren runs on shift changes at the plants and a cruise week in August. The winter eats the roads.'),
  P('The Tech Center, the arsenal, and the truck plant change shifts around seven and three. Mound, Van Dyke, and 12 Mile fill both ways for an hour. A pickup on those roads moves to mid-morning or early afternoon. A model launch at the truck plant pulls the car haulers off the private lanes for a week.'),
  P('The Dream Cruise fills Woodward in Oakland County on the third Saturday in August. The week before it fills every cruise night in the suburbs. The Gratiot cruise in June does the same on the east side. The collectors move cars in and out for both. The civic center festival in summer closes Van Dyke at 12 Mile for a weekend.'),
  P('The 696 rebuild is the road story of the decade. The state is rebuilding the freeway across Macomb County in stages through 2027. Whole directions close for months at a time. The carriers plan around it and run the mile roads. A pickup near the freeway may move to a lot on Van Dyke. The price does not change.'),
  P('The August 2014 flood put 696 and the south-side basements under water in an afternoon. The 2021 storm did it again. A pickup on a flooded street waits for the water to drop. Winter brings forty inches of snow, and the salt eats the roads into potholes by March. The carriers park on 75 until the plows finish, and a winter pickup can lose a day.'),
 )+chips(["South Warren","8 Mile","9 Mile","10 Mile","Center Line","Van Dyke","Mound Road","Tech Center","Civic Center","12 Mile","Arsenal","11 Mile","Ryan Road","Hoover","Schoenherr","Hayes","Dequindre","Groesbeck","North Warren","13 Mile","14 Mile","Sterling Heights","Madison Heights","Hazel Park","Roseville","Eastpointe","St. Clair Shores","Fraser","Clinton Township","Detroit"])
 +NOTE('Serving Warren, Center Line, Sterling Heights, and the south half of Macomb County, bungalow grid or subdivision. Tell us the side of 696 and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Warren?',
 prose(
  L('Most Macomb County cars ride an open trailer, and the table above is priced for one.'),
  P('An enclosed trailer shuts out the salt, the slush, and the potholes’ gravel. The cruise crowd books one for the show cars each August. Engineers relocating a new car to the Tech Center book one too.'),
  P('A daily driver or a plant truck goes open and comes off the trailer fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the trade-off.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the civic center or on 12 Mile, and a signature at delivery. The program date sets the week.'),
  P('Approve the price, and we assign a carrier already working the plant lanes on Mound. The lot and the window reach you within hours. You walk the car with the driver at pickup. Each existing mark goes on the Bill of Lading. Two signatures close it. The same form is checked at delivery.'),
 )+ULI([
  "Clear out the cabin, the trunk, and the glovebox",
  "Run the fuel down to about a quarter tank",
  "Photograph each panel and the odometer before the truck arrives",
  "Hand over one working key and describe any fault",
  "Disarm any aftermarket alarm",
  "In the south-side grids, meet the truck on Van Dyke or at a shopping center lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Warren Drivers Choose Ship Guy',
 prose(
  L('We book the plant carriers already running Mound and 696. We plan around the shift changes, the rebuild, and the salt.'),
  P('Ship Guy is an active FMCSA broker backed by a $75,000 surety bond. The federal register lists both. Our office is on Mound Road at 13 Mile.'),
  P('The coordinator who quotes the move is the one who closes it. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Warren','31850 Mound Rd #400A','Warren, MI 48092','+15865517329','(586) 551-7329','ET',
 '31850+Mound+Rd+%23400A,+Warren,+MI+48092','Visit Us','Find Ship Guy in Warren',
 'Our office is on Mound Road at 13 Mile, a mile north of the Tech Center.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4521.482367860658!2d-83.0472221!3d42.5276068!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8824dbd4d91a07ed%3A0x9efe3bd52e17fb43!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025174086!5m2!1sen!2sus', alt=True))

FAQ=[
 ("Why is a Warren pickup faster than most cities?","Because Warren sits inside the Motor City carrier pool. The haulers that deliver new trucks from the Mound plant have to go back for the next load. They take private cars with them. More of those trucks pass through Warren than any suburb in the metro. A pickup here usually happens within a day or two."),
 ("How much does it cost to ship a car from Warren to Chicago or Florida?","Chicago runs two hundred sixty to three hundred ninety dollars for a sedan. That is about two hundred ninety miles on 94. Tampa runs eight hundred to eleven hundred fifty, about twelve hundred miles down 75. The Florida price climbs in October with the snowbirds and eases in April. An SUV or pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street in South Warren?","Usually not. The bungalow grids between 8 Mile and 10 Mile are narrow streets with cars on both sides. A seventy-five-foot trailer cannot turn in them. The driver meets you on Van Dyke, on 9 Mile, or at a shopping center lot. North Warren, the Tech Center district, and Sterling Heights usually allow the curb."),
 ("Do you ship cars for engineers relocating to the Tech Center?","Yes, every month. The design campus brings engineers in on program schedules from every state and from overseas. Many ship a car behind the move, and the company pays for it. The handoff works at the civic center lots on Van Dyke or a lot on 12 Mile. We provide the paperwork a reimbursed move needs."),
 ("Does the 696 construction affect my pickup?","A little. The state is rebuilding 696 across Macomb County in stages through 2027, and whole directions close for months. The carriers run the mile roads and come off 75 or 94 instead. A pickup near the freeway may move to a lot on Van Dyke. The price does not change."),
 ("Can you ship a car to or from Sterling Heights, Center Line, or Roseville?","Yes, and all three price the same as Warren. Sterling Heights rides the same carriers up Van Dyke and Mound, and the curb works on most streets. Center Line sits inside Warren at 10 Mile, and the handoff works on Van Dyke. Roseville rides them off 94, and the handoff moves to Gratiot for the older grids."),
 ("Do you ship cars for Army civilians at the arsenal?","Yes. The arsenal on 11 Mile moves civilians and officers in on assignment cycles. The orders cover one car, and we move the other. The handoff happens outside the gate or at a lot on Van Dyke. Ship Guy is a private broker with no connection to the arsenal. Send the report date, and the window is built around it."),
 ("What happens if a snowstorm or a flood hits on my pickup day?","Snow closes 696 and 75 a few times a winter, and the carriers park until the plows finish. A winter pickup can slip a day, and we call before it does. A summer downpour floods the south-side streets and the freeway, as it did in 2014 and 2021. A pickup on a flooded street waits for the water to drop, usually the same afternoon."),
 ("Can you ship a car that does not run from Warren?","Yes. A carrier with a winch is sent, and the loading time is priced in from the first quote. The civic center lots or a shopping center on 12 Mile give the driver level pavement. Tell us whether the car rolls, steers, and brakes."),
 ("What do you need for a Warren car shipping quote?","The two addresses, with the side of 696 or the mile road here. Year, make, and model. Whether it runs. Open or enclosed. The week around the program date or the closing. Five answers, and the Warren number is back within the day."),
]
BODY.append(faq_section(FAQ,'Warren FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Warren?','The form above prices the lane in two minutes. Give us the side of 696 and the week, and the next plant carrier down Mound takes it.','+15865517329','(586) 551-7329','Get your free Warren quote'))

build({
 'slug':'auto-transport-warren-michigan',
 'title':'Car Shipping in Warren, MI — Auto Transport | Ship Guy',
 'meta':'Car shipping in Warren, MI, the first suburb north of 8 Mile, inside the Motor City carrier pool. Tech Center and arsenal relocations, the truck plant on Mound, South Warren meeting spots, North Warren and Sterling Heights curbside pickups, the 696 rebuild through 2027, the 2014 flood, and the salt. Local office on Mound Road at 13 Mile. Free quote.',
 'h1':'Car Shipping in<br>Warren, <span class="accent">Michigan</span>',
 'lede':'Open, enclosed, and expedited auto transport across south Macomb County, planned around 696, the mile roads, the plant shifts, and the winter.',
 'tel':'+15865517329','disp':'(586) 551-7329','brand':'Warren','keyword':'car shipping in warren',
 'localterms':['warren','macomb county','8 mile','interstate 696','reuther','11 mile','interstate 94','interstate 75','van dyke','m-53','mound road','plant corridor','ryan','hoover','schoenherr','hayes','dequindre','groesbeck','m-97','mile roads','12 mile','9 mile','10 mile','13 mile','14 mile','chicago road','martin road','rebuild','2027','south warren','bungalows','center line','tech center','design campus','civic center','hospital','arsenal','gate','north warren','ranches','colonials','industrial','sterling heights','truck plant','mall','m-59','madison heights','hazel park','roseville','eastpointe','st. clair shores','gratiot','clinton township','fraser','detroit','engineers','designers','program schedules','overseas','army','civilians','officers','orders','stamping plant','supervisors','skilled trades','launch','suppliers','nurses','community college','retirees','shift changes','dream cruise','woodward','gratiot cruise','festival','2014 flood','2021','basements','snow','salt','potholes','toledo','cleveland','columbus','chicago','indianapolis','pittsburgh','nashville','new york','atlanta','tampa','utica'],
}, BODY, FAQ)
