import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Grand Rapids, Michigan','Car shipping in the second city of Michigan, where 196 and 131 cross on the Grand River',
 ['Car shipping in Grand Rapids runs off the 196 and 131 interchange downtown and the 96 loop. Ship Guy is a licensed auto transport broker with an office on Monroe Center downtown.',
  'We book vetted carriers across Kent and Ottawa Counties, from Rockford to Byron Center and west to Holland. The trucks belong to the carriers we vet.',
  'Interstate 196 runs through downtown from Holland to the 96. US 131 runs north and south through the city on the S-curve over the river. Interstate 96 loops the north and east sides toward Lansing. M-6 is the south beltway, and the East Beltline rings the east side.',
  'This page covers the three freeways, the S-curve, downtown, Heritage Hill, the suburbs, and the lakeshore. It also covers the Medical Mile, the furniture makers, the campuses, ArtPrize, the lake-effect snow, and the lanes.'],
 'Grand Rapids at a glance',
 ['Most pickups happen within 1 to 3 days. The Chicago carriers come across on 94 and 196, and the Detroit trucks come over on 96.',
  'Lansing is an hour, and Detroit and Chicago are a same-day haul. Toledo, Indianapolis, Milwaukee, and Columbus take a day. Nashville and the East Coast take two, and Florida takes three.'],
 'Tell us the side of the river. Downtown, Heritage Hill, and East Grand Rapids need a meeting spot. The east side, the suburbs, and the lakeshore towns usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 196, US 131, Interstate 96, M-6, the East Beltline, and the S-Curve',
 prose(
  L('Grand Rapids sits where the Chicago road and the Detroit road meet. The carriers reach it from both directions.'),
  P('Interstate 196 comes in from the lakeshore at Holland and runs through downtown to the 96. The exits at Lake Michigan Drive, Ottawa, College, and Fuller serve the core. US 131 runs north and south through the city. The S-curve carries it over the river beside downtown. The exits at Wealthy, Pearl, Leonard, and 28th Street serve the city.'),
  P('Interstate 96 arrives from Lansing and Detroit and loops the north and east sides. It runs past the airport road to the lakeshore at Muskegon. M-6 is the south beltway from the 96 at Cascade to the 196 at Grandville. The East Beltline runs the east side from Rockford to 28th Street. Together they ring the city.'),
  P('28th Street is the retail strip across the south side, from Grandville to Cascade. Alpine Avenue, Plainfield, and Leonard carry the north side. Wealthy, Fulton, and Michigan Street cross the east side, and Michigan Street climbs the Medical Mile. Lake Michigan Drive is M-45, the road west to the university and Allendale. Division Avenue runs the length of the city.'),
  P('The carriers come off 131 at 28th Street and off 196 at College. The mall on 28th Street, the arena downtown, and the airport have the usual meeting lots. No road in West Michigan charges a toll.'),
  P('Our office is on Monroe Center downtown, beside Rosa Parks Circle and a block from the river.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Heritage Hill, the West Side, Eastown, the Suburbs, and the Lakeshore',
 prose(
  L('Grand Rapids is a furniture town with a Victorian hill above downtown. The suburbs run to the lake.'),
  P('Downtown sits on both banks of the river around the arena, the convention center, and Monroe Center. The streets are narrow and busy, and the bridges are tight. The driver meets you at the arena lots, on the west bank, or at the Medical Mile garages. Heritage Hill above downtown is the largest historic district in the state. Its big houses sit on narrow streets under old trees. The handoff moves to Fulton or to a lot off Michigan Street.'),
  P('The West Side across the river along Bridge Street is the old Polish neighborhood. It is a dense grid with alleys. The driver meets you on Bridge or at the stadium lot. Eastown, East Hills, and Midtown along Wealthy and Cherry are streetcar grids with wider streets. The curb works on most blocks. Creston and the northeast off Plainfield are postwar grids, and the curb works there too.'),
  P('East Grand Rapids around the lake is its own city with narrow streets and a village center. The driver meets you in Gaslight Village or on Lake Drive. Kentwood and Wyoming to the south have the malls and wide subdivision streets. The truck reaches the curb. Grandville, Walker, and Comstock Park are the same. Cascade and Ada on the east have the airport, the corporate campus, and big lots on wide roads.'),
  P('Rockford to the north and Byron Center to the south are growing towns. Lots sit on every main road. Jenison, Hudsonville, and Allendale to the west are the Ottawa County growth, with the university and wide streets. Holland and Zeeland on the lakeshore have the furniture plants and the tulip festival. Muskegon sits at the end of the 96. All of them price the same as Grand Rapids, and the lakeshore towns add a day in snow.'),
 )))

ROUTES=[("Lansing, MI","I-96 · ~65 mi","Same day","$150–$240"),("Detroit, MI","I-96 · ~160 mi","Same day","$200–$310"),
 ("Chicago, IL","I-196/I-94 · ~180 mi","Same day","$220–$340"),("Toledo, OH","I-96/US-23 · ~220 mi","1 day","$230–$350"),
 ("Indianapolis, IN","US-131/I-69 · ~260 mi","1 day","$260–$380"),("Milwaukee, WI","I-94 · ~275 mi","1 day","$260–$390"),
 ("Columbus, OH","I-96/US-23 · ~320 mi","1 day","$300–$440"),("Nashville, TN","I-65 · ~600 mi","2 days","$470–$680"),
 ("Atlanta, GA","I-65/I-24/I-75 · ~790 mi","2 days","$540–$780"),("Tampa, FL","I-75 · ~1,250 mi","3 days","$830–$1,180")]
BODY.append(rate_table('Lanes &amp; Costs','Grand Rapids Car Shipping Lanes and Estimated Costs',
 'The lanes West Michigan cars run most often, with estimated open-trailer ranges. Price your exact route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Grand Rapids for a sedan that runs, open trailer. SUVs and pickups add 10 to 25 percent, and enclosed adds more. Lake-effect weeks and the snowbird months move the number. The carriers free on your dates set the final price.',
 prose(
  P('Grand Rapids prices with Detroit on the southern lanes and a little under it to Chicago. The west side sits closer. The Chicago carriers come across 94 and 196 daily. The Detroit trucks come over on 96 and fill the last spot here. The Florida lane rides the snowbird calendar, higher in October and lower in April.'),
  P('A lake-effect week adds a day to anything leaving the lakeshore. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Medical Mile, the Furniture Makers, the Grocer, the Campuses, and the Lakeshore Plants',
 prose(
  L('Grand Rapids relocates physicians, designers, grocery executives, and students. The Medical Mile moves more people than anyone in West Michigan.'),
  P('The hospital system on Michigan Street is the largest employer in the region. The research institute and the medical school sit beside it. Traveling nurses arrive all year, and the residents land every June. The physicians show up with a closing date and a second car to ship. The second hospital system downtown hires the same way. We supply the paperwork a reimbursed move needs.'),
  P('The furniture makers headquartered here and on the lakeshore relocate designers and engineers on program schedules. The grocer headquartered in Walker and the food distributor in Wyoming move managers in from every state. The direct-sales company in Ada and the shoemaker in Rockford relocate staff on their own calendars. The mirror plant and the furniture plants in Zeeland do the same.'),
  P('The state university brings cars to Allendale and the downtown campus each August. The two private colleges and the community college run the same calendar. The parent arranges the car, and someone over eighteen signs at a campus lot. Faculty hires land each summer with a closing date.'),
  P('Families from Chicago and Detroit buy in Rockford, Byron Center, and Ottawa County on closing dates. One car rides the trailer while the family drives the other. Each October the retirees head for Florida, and each April they come back. The interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page. Ship Guy is a private broker with no military tie. The Guard timing is on the <a href="military-car-shipping.html">military</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','ArtPrize, the Festival, Tulip Time, the Lake-Effect Snow, and the 2013 Flood',
 prose(
  L('Grand Rapids runs on an art competition each fall and a tulip festival on the lakeshore. The winter comes off the lake.'),
  P('ArtPrize fills downtown for most of September and October. The venues line Monroe Center and the river, and the lots downtown fill every evening and weekend. A downtown pickup those weeks moves to the arena lots in the morning or to 28th Street. The arts festival closes the downtown blocks for a weekend in June.'),
  P('Tulip Time fills Holland for a week in May, and the lakeshore roads back up from the 196. The hockey team fills the arena lots from October through April. The ballpark in Comstock Park fills its lots in summer. The marathon closes the river trail on an October Sunday. A handoff near any of them moves to the daytime or to another lot.'),
  P('Lake-effect snow is the weather. Seventy-five inches falls in a normal winter, most of it in bands off the lake. A band buries one town and misses the next. The 196 and 131 close a few times a season. The carriers park at the truck stops on 96 until the plows finish. A winter pickup can lose a day or two, and the lakeshore loses more. The 2013 ice storm took the power out across the city for a week.'),
  P('The river floods. The 2013 flood brought the Grand to a record crest and tested the flood walls downtown. The low streets along the river and the Plaster Creek neighborhoods flood in a wet April. A pickup there moves up the hill for a day. Summer brings thunderstorms and the occasional tornado watch, and the loading goes on.'),
 )+chips(["Downtown","Monroe Center","Arena District","Heartside","Medical Mile","Heritage Hill","West Side","Bridge Street","Belknap","Midtown","East Hills","Eastown","Wealthy Street","Creston","Northeast","Plainfield","Alger Heights","Garfield Park","Burton Heights","Roosevelt Park","East Grand Rapids","Gaslight Village","Kentwood","Wyoming","Grandville","Walker","Standale","Comstock Park","Cascade","Ada","Forest Hills","Rockford","Byron Center","Jenison","Hudsonville","Allendale","Holland","Zeeland","Muskegon"])
 +NOTE('Serving Grand Rapids, the suburbs, and the lakeshore across Kent and Ottawa Counties, hill street or subdivision. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Grand Rapids?',
 prose(
  L('Open trailers carry most of the cars that leave West Michigan, and the table above assumes one.'),
  P('An enclosed trailer keeps a car out of the salt, the slush, and the lake grit. Collectors in East Grand Rapids and Ada book one for the show cars. Snowbirds with a new car book one for the Florida run.'),
  P('A commuter car or a plant truck rides open and arrives the way it left. Read the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages for the full comparison.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('One number, one meeting spot at the mall or the arena, one car at the far end. The start date or the closing picks the week.'),
  P('Take the number, and the car is matched to a carrier already running 96 or 196. The lot and the window are confirmed before the day ends. The driver circles the car with you at pickup and records its condition on the Bill of Lading. You both sign, and that record is the yardstick when the car comes off.'),
 )+ULI([
  "Empty the cabin and the trunk of personal items",
  "Fuel to about a quarter tank",
  "Shoot all four sides and the odometer before the truck arrives",
  "One working key to the driver, with any mechanical issue named",
  "Aftermarket alarm off",
  "In Heritage Hill or downtown, meet the truck at the arena lots or on Fulton",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Grand Rapids Drivers Choose Ship Guy',
 prose(
  L('We catch the Chicago carriers on 196 and the Detroit carriers on 96. We plan around ArtPrize, the lake-effect bands, and the river.'),
  P('Ship Guy’s FMCSA brokerage authority and $75,000 surety bond are both on the federal register. Our office is on Monroe Center downtown.'),
  P('The coordinator who gives you the number stays on the move until the last signature. The <a href="services.html">services</a> page lists open, enclosed, and expedited transport.'),
 )))

BODY.append(office('Grand Rapids','77 Monroe Center St NW #775A','Grand Rapids, MI 49503','+16168832952','(616) 883-2952','ET',
 '77+Monroe+Center+St+NW+%23775A,+Grand+Rapids,+MI+49503','Visit Us','Find Ship Guy in Grand Rapids',
 'Our office is on Monroe Center downtown, beside Rosa Parks Circle and a block from the river.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4489.723316513145!2d-85.6695893!3d42.9645643!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8819ad72be7d40a5%3A0xbfd469332eb652e!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025185775!5m2!1sen!2sus'))

FAQ=[
 ("How much does it cost to ship a car from Grand Rapids to Chicago or Detroit?","Chicago runs two hundred twenty to three hundred forty dollars for a sedan. That is about one hundred eighty miles on 196 and 94. Detroit runs two hundred to three hundred ten, about one hundred sixty miles on 96. Lansing is an hour away and costs the least. Add 10 to 25 percent for an SUV or a pickup. All three lanes see trucks daily."),
 ("Can the carrier come to my street in Heritage Hill or East Grand Rapids?","Usually not. Heritage Hill has narrow streets under old trees, and East Grand Rapids is tight around the lake. The driver meets you on Fulton, at a lot off Michigan Street, or in Gaslight Village. The east side grids, the suburbs, and the lakeshore towns usually allow the curb."),
 ("Do you ship cars for people relocating to the Medical Mile or the furniture makers?","Yes, all year. The hospital system on Michigan Street brings in nurses, residents, and physicians every month. The furniture makers move designers and engineers on program schedules. Many ship a second car behind the move. The handoff works at the Medical Mile garages or the mall lot on 28th Street. We provide the paperwork a reimbursed move needs."),
 ("Does ArtPrize affect my pickup?","Downtown, yes. The venues fill Monroe Center and the riverfront for most of September and October. The downtown lots are gone every evening and weekend. We move a downtown pickup those weeks to the arena lots in the morning or to 28th Street. The rest of the city runs normally."),
 ("Can you ship a car to or from Holland, Rockford, or Allendale?","Yes, and all three price the same as Grand Rapids. Holland rides the same carriers off 196, and the lakeshore adds a day in a lake-effect week. Rockford rides them off 131 to the north, and Allendale rides them off Lake Michigan Drive. Send the full address for a new subdivision in Ottawa County."),
 ("What happens if a lake-effect storm hits on my pickup day?","The bands close 196 and 131 a few times a winter. The carriers park at the truck stops on 96 until the plows finish. A winter pickup can slip a day or two, and the lakeshore slips more. We tell you before it happens. In a wet April the river floods the low streets, and a pickup there moves up the hill."),
 ("Can you ship a car that does not run from Grand Rapids?","Yes. We send a winch-equipped carrier and build the loading time into the first number. The mall lot on 28th Street or the arena lots give the driver flat ground. Say whether the car rolls, steers, and brakes."),
 ("Can you deliver on the Grand Valley or Calvin move-in date?","Yes. The campuses in Allendale and downtown take cars in each August and send them home in May. The private colleges run the same calendar. A parent sets it up, and someone over eighteen signs at a campus lot. The window tracks the move-in date and moves with it."),
 ("Can you ship a snowbird’s car to Florida each fall?","Yes, and it is the busiest lane out of West Michigan from October through December. Tampa runs eight hundred thirty to eleven hundred eighty dollars for a sedan. The cars come home from March through May. Book two weeks ahead in the fall, because the southbound trucks fill early. The <a href=\"/snowbird-car-shipping\">snowbird</a> page covers the seasonal lane."),
 ("What do you need for a Grand Rapids car shipping quote?","The two addresses, with the side of the river or the suburb named. The year, make, and model. Whether it runs. Open or enclosed. The week around the start date. With those five, the Grand Rapids number is back the same day."),
]
BODY.append(faq_section(FAQ,'Grand Rapids FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Grand Rapids?','The form above returns a number in about two minutes. Tell us the side of the river and the week, and a 196 carrier takes it.','+16168832952','(616) 883-2952','Get your free Grand Rapids quote'))

build({
 'slug':'auto-transport-grand-rapids-michigan',
 'title':'Car Shipping in Grand Rapids, MI — Auto Transport | Ship Guy',
 'meta':'Car shipping in Grand Rapids, MI, where 196 and 131 cross on the Grand River. Medical Mile and furniture-maker relocations, downtown and Heritage Hill meeting spots, suburb and lakeshore curbside pickups, Holland and Rockford, ArtPrize, the lake-effect snow, the 2013 flood, and the snowbird lane. Local office on Monroe Center downtown. Free quote.',
 'h1':'Car Shipping in<br>Grand Rapids, <span class="accent">Michigan</span>',
 'lede':'Open, enclosed, and expedited auto transport across West Michigan, planned around 196, 131, 96, ArtPrize, and the lake-effect snow.',
 'tel':'+16168832952','disp':'(616) 883-2952','brand':'Grand Rapids','keyword':'car shipping in grand rapids',
 'localterms':['grand rapids','west michigan','grand river','interstate 196','us 131','s-curve','interstate 96','m-6','beltway','east beltline','28th street','alpine','plainfield','leonard','wealthy','fulton','michigan street','medical mile','lake michigan drive','m-45','division','downtown','monroe center','rosa parks circle','arena','convention center','heritage hill','historic district','west side','bridge street','polish','eastown','east hills','midtown','cherry','creston','northeast','east grand rapids','gaslight village','lake drive','kentwood','wyoming','malls','grandville','walker','comstock park','cascade','ada','airport','rockford','byron center','jenison','hudsonville','allendale','ottawa county','holland','zeeland','muskegon','lakeshore','hospital system','research institute','medical school','nurses','residents','furniture makers','designers','grocer','food distributor','direct-sales','shoemaker','mirror plant','state university','private colleges','community college','retirees','snowbirds','artprize','arts festival','tulip time','hockey','ballpark','marathon','lake-effect','seventy-five inches','2013 ice storm','2013 flood','plaster creek','lansing','detroit','chicago','toledo','indianapolis','milwaukee','columbus','nashville','atlanta','tampa'],
}, BODY, FAQ)
