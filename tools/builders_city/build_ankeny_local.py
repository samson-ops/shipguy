import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Ankeny, Iowa','Car shipping in the fastest-growing city in Iowa, ten minutes up Interstate 35 from Des Moines',
 ['Car shipping in Ankeny runs off Interstate 35, which passes the east side with three exits. Ship Guy is a licensed auto transport broker with an office on Linden Street in Uptown.',
  'We book vetted carriers across the north side of the Des Moines metro, from Johnston to Bondurant. The trucks belong to the carriers we vet.',
  'Interstate 35 runs the east side with exits at Oralabor, 1st Street, and 36th Street. Interstate 80 crosses five miles south. Ankeny Boulevard is Highway 69, the road through the middle. 1st Street and Oralabor Road carry the retail, and Delaware and State run north and south.',
  'This page covers 35, Ankeny Boulevard, Uptown, Prairie Trail, the north side, and the suburbs around. It also covers the tractor plant, the convenience-store chain, the college, the State Fair, and the lanes.'],
 'Ankeny at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between Minneapolis and Kansas City passes the city on 35. The 80 trucks are five minutes away.',
  'Des Moines is fifteen minutes, and Ames is thirty. Omaha, Kansas City, and Minneapolis are a same-day haul. Chicago, St. Louis, and Milwaukee take a day. Denver, Dallas, and Nashville take two, and the coasts take three to five.'],
 'Tell us the side of Ankeny Boulevard. Uptown and the oldest grids need a meeting spot. Prairie Trail, the north side, and the subdivisions off 36th usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 35, Interstate 80, Ankeny Boulevard, Oralabor Road, 1st Street, and 36th Street',
 prose(
  L('Ankeny sits on the north-south interstate five minutes from the east-west one. The carriers reach it from four directions.'),
  P('Interstate 35 runs along the east side of the city from Des Moines to Ames and Minneapolis. The exits at Oralabor Road, 1st Street, and 36th Street cover four miles. Every carrier between Kansas City and Minneapolis passes all three. Interstate 80 crosses the metro five miles south. The Chicago and Omaha trucks come up 35 from the interchange.'),
  P('Ankeny Boulevard is Highway 69, the old road north from Des Moines through the city to Ames. Oralabor Road runs the south side past the tractor plant and the retail at the 35 exit. 1st Street is the main road across the middle, from the interstate through Uptown to the west side. 18th Street and 36th Street cross the north side.'),
  P('Delaware Avenue and State Street run north and south past the plant and the airport. Irvinedale Drive runs the west side. Prairie Trail Parkway loops the new district on the old research farm. The bike trail runs north from Uptown on the old rail line. Highway 415 runs west to Polk City and the lake.'),
  P('The carriers come off 35 at Oralabor and 1st Street. The retail center on Oralabor, the college, and Prairie Trail have the usual meeting lots. No road in the metro charges a toll.'),
  P('Our office is on Linden Street in Uptown, a block off Ankeny Boulevard.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Uptown, the Old Grids, Prairie Trail, the North Side, the East Side, and the Towns Around',
 prose(
  L('Ankeny was a farm town with a plant until the subdivisions arrived. Now it adds a new neighborhood every year.'),
  P('Uptown is the original downtown along 3rd Street, a few blocks of storefronts and small lots. The streets are narrow, and the summer festival fills them. The driver meets you at the community college lots or at a lot on Ankeny Boulevard. The oldest grids around Uptown have narrow streets, and the handoff moves to 1st Street.'),
  P('Prairie Trail on the south side is the district on the old research farm. It has the market, the restaurants, the high school, and new subdivisions. The streets are wide, and the truck reaches the curb. The subdivisions between 1st Street and 18th Street are from the 1990s and 2000s. They have wide streets and cul-de-sacs. The curb works, and the driver meets you at the mouth of a cul-de-sac.'),
  P('The north side between 18th and 36th and beyond is the newest growth. The streets are not on every map yet. Send the full address and the nearest main road. The east side along Delaware and State is the plant, the airport, and older grids with wide streets. The curb works.'),
  P('Johnston and Grimes to the west are the Guard camp, the seed company, and wide subdivisions. Bondurant and Altoona to the east have the warehouses, the data centers, the casino, and the amusement park. Polk City and the lake sit to the northwest. Ames and the university sit thirty minutes north on 35. Des Moines and West Des Moines to the south have the insurers. All of them price the same as Ankeny.'),
 )))

ROUTES=[("Omaha, NE","I-80 · ~145 mi","Same day","$190–$300"),("Kansas City, MO","I-35 · ~205 mi","Same day","$220–$340"),
 ("Minneapolis, MN","I-35 · ~235 mi","Same day","$250–$380"),("Chicago, IL","I-80 · ~345 mi","1 day","$310–$450"),
 ("St. Louis, MO","I-35/US-36 · ~360 mi","1 day","$320–$460"),("Milwaukee, WI","I-80/I-88 · ~385 mi","1 day","$340–$490"),
 ("Indianapolis, IN","I-80/I-74 · ~490 mi","1 day","$400–$580"),("Denver, CO","I-80 · ~680 mi","2 days","$500–$730"),
 ("Dallas, TX","I-35 · ~710 mi","2 days","$520–$750"),("Nashville, TN","I-80/I-57/I-24 · ~710 mi","2 days","$520–$750")]
BODY.append(rate_table('Lanes &amp; Costs','Ankeny Car Shipping Lanes and Estimated Costs',
 'The lanes north-metro cars use most, with estimated open-trailer ranges. Put your exact route on the form above for a number.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Ankeny for a running sedan on an open trailer. SUVs and pickups add 10 to 25 percent, and enclosed adds more. Harvest and the winter move the number. Carrier availability on your dates sets the final price.',
 prose(
  P('Ankeny prices with Des Moines on every lane. The carriers pass the city on 35 on the way to and from the 80 interchange. The Minneapolis and Kansas City lanes run daily in both directions and price the lowest per mile. The Chicago and Omaha lanes ride 80 and run most days. The Dallas lane runs full with the relocations south.'),
  P('A ground blizzard on 35 north of the metro shuts the Minneapolis lane for a day. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Tractor Plant, the Convenience-Store Chain, the Insurers, the Community College, and the Guard',
 prose(
  L('Ankeny relocates plant engineers, corporate staff, insurance analysts, and students. The insurers downtown move more people than anyone in Iowa.'),
  P('The tractor maker’s plant on the southeast side builds the big sprayers and the cotton pickers. It moves engineers and supervisors in from the other plants on program schedules. The convenience-store chain headquartered on the north side moves managers and analysts in from every state. We supply the paperwork a reimbursed move needs.'),
  P('The insurance and financial companies downtown and in West Des Moines relocate employees on start dates. Many of them buy in Ankeny and ship a second car behind the move. The hospitals downtown bring in nurses on contracts all year. The clinic on the north side does the same.'),
  P('The community college on Ankeny Boulevard is the largest in the state. It brings cars in each August. The university in Ames sits thirty minutes north on 35 and runs the same calendar. The parent books the car, and an adult meets the driver at a campus lot. The high schools draw families from across the metro for the sports programs.'),
  P('The Guard camp in Johnston moves soldiers and staff on orders. The orders pay for one car, and the other one ships with us. Ship Guy is a private broker and has no tie to the camp. Timing is on the <a href="military-car-shipping.html">military</a> page, and the interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','SummerFest, the State Fair, the Derecho, the Saylorville Spillway, and the Ground Blizzards',
 prose(
  L('Ankeny runs on a July festival in Uptown and a state fair that fills the whole metro. The winter closes 35 to the north.'),
  P('SummerFest fills Uptown for a weekend in July. The carnival sits on the Uptown streets, the parade closes Ankeny Boulevard, and the lots fill by noon. A pickup in Uptown that weekend moves to Prairie Trail or to the Oralabor retail center. The Fourth of July fills the parks the week before it.'),
  P('The State Fair fills the east side of Des Moines for eleven days in August. The 35 and 80 interchange backs up every afternoon, and the fairgrounds roads gridlock. A pickup on the south side those days moves to the morning. The amusement park in Altoona fills the east side all summer. The Drake Relays close the streets by the stadium for an April weekend.'),
  P('The 2020 derecho crossed the metro in an August afternoon and took the trees down across Ankeny. The sirens sound a few times each spring. The 2018 tornado crossed Bondurant a mile east of the city. A pickup waits for the warning to lift. The Saylorville spillway opens in a wet spring, as it did in 2008 and 2018. The river roads south of the lake close.'),
  P('Winter is the ground blizzard. The wind blows the snow across the open ground north of the metro. Interstate 35 closes between here and Ames a few times a winter. The carriers park at the truck stops by the 80 interchange until the plows finish. A winter pickup can lose a day. Ice is the bigger problem on the overpasses. Summer heat and humidity move the loading hour to the morning.'),
 )+chips(["Uptown","3rd Street","Ankeny Boulevard","Linden Street","Old Grids","1st Street","Prairie Trail","The District","Oralabor","Southeast","Delaware","State Street","Tractor Plant","Airport","18th Street","36th Street","North Side","Irvinedale","West Side","Briarwood","Otter Creek","High Trestle Trail","Johnston","Grimes","Polk City","Saylorville","Bondurant","Altoona","Elkhart","Ames","Des Moines","West Des Moines"])
 +NOTE('Serving Ankeny and the north side of the Des Moines metro, Uptown block or new subdivision. Tell us the side of Ankeny Boulevard and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Ankeny?',
 prose(
  L('Open trailers carry most of the cars that leave the north metro, and the table above assumes one.'),
  P('An enclosed trailer keeps a car out of the salt, the gravel dust, and the hail. Collectors in the lake communities book one for the show cars. Executives relocating a new car to the chain’s headquarters book one too.'),
  P('A commuter car or a farm pickup rides open and arrives in the shape it left. Compare the two on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a handoff on Oralabor or at the college, and a car at the far end. The start date sets the week.'),
  P('Give the number a yes, and the car is paired with a carrier already running 35. The meeting lot and the window follow within hours. At the handoff the driver looks over the car with you. Each existing mark is listed on the Bill of Lading. You both sign, and that sheet decides any question at delivery.'),
 )+ULI([
  "Personal items out of the cabin and the trunk",
  "Fuel down to about a quarter tank",
  "A photo of each panel and the odometer before the truck comes",
  "One working key to the driver, and a word about any mechanical fault",
  "Kill any aftermarket alarm before the handoff",
  "On a cul-de-sac, meet the truck at the mouth of the street",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Ankeny Drivers Choose Ship Guy',
 prose(
  L('We load the carriers already running 35 between Kansas City and Minneapolis. We plan around the start date, the fair, and the ground blizzards.'),
  P('Ship Guy’s FMCSA brokerage authority and $75,000 surety bond are both searchable on the federal register. Our office is on Linden Street in Uptown.'),
  P('The coordinator who prices your move is the one who sees the delivery sheet signed. Open, enclosed, and expedited transport are laid out on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Ankeny','106 SW Linden St #199A','Ankeny, IA 50023','+15153732431','(515) 373-2431','CT',
 '106+SW+Linden+St+%23199A,+Ankeny,+IA+50023','Visit Us','Find Ship Guy in Ankeny',
 'Our office is on Linden Street in Uptown, a block off Ankeny Boulevard.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4578.709688475117!2d-93.62975879999999!3d41.7309135!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87ee85f17871a20d%3A0x4f617eed8a67f6be!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025235789!5m2!1sen!2sus'))

FAQ=[
 ("Can you time delivery to my closing date in Ankeny?","Yes. Closings drive most Ankeny bookings. Families relocating to the insurers downtown and the plant buy in the north-side subdivisions. The car arrives the week of the closing. The delivery window is pinned to the closing date, and when the closing slides, so does the window. The newest streets are not on every map yet, so send the full address."),
 ("How much does it cost to ship a car from Ankeny to Minneapolis or Dallas?","Minneapolis runs two hundred fifty to three hundred eighty dollars for a sedan. That is about two hundred thirty-five miles up 35. Dallas runs five hundred twenty to seven hundred fifty, about seven hundred ten miles down the same road. Kansas City and Omaha land between the two. Figure 10 to 25 percent more for an SUV or a pickup. The 35 lanes see trucks daily in both directions."),
 ("Can the carrier come to my street in Uptown or on a cul-de-sac?","Uptown, usually not. The streets are narrow, and the festival fills them in July. The driver meets you at the college lots or on Ankeny Boulevard. The subdivisions allow the curb, but a seventy-five-foot trailer cannot turn in a cul-de-sac. The driver meets you at the mouth of the street."),
 ("Do you ship cars for people relocating to the plant or the convenience-store chain?","Yes, all year. The tractor plant moves engineers and supervisors in from the other plants on program schedules. The chain headquartered on the north side moves managers and analysts from every state. Many ship a second car behind the move. The handoff works at the Oralabor retail center or the college lots. We provide the paperwork a reimbursed move needs."),
 ("Does the State Fair affect my pickup?","On the south side, yes. The fair fills the east side of Des Moines for eleven days in August. The 35 and 80 interchange backs up every afternoon. We move a south-side pickup those days to the morning. Uptown and the north side run normally. SummerFest does the same thing to Uptown for a weekend in July."),
 ("Can you ship a car to or from Johnston, Bondurant, or Ames?","Yes, and all three price the same as Ankeny. Johnston rides the same carriers off 35 and 80 at Merle Hay. Bondurant rides them off 80 to the east, and the warehouses there have lots at every gate. Ames rides them up 35, and the handoff happens at a lot near campus. Send the full address for a new subdivision."),
 ("What happens if a ground blizzard or a tornado warning hits on my pickup day?","Snow closes 35 north of the metro a few times a winter. The carriers park at the truck stops by the 80 interchange until the plows finish. If a winter pickup slides a day, you hear it from us first. The sirens go off a few times each spring, and a warning halts the loading until it passes. The driver waits in the cab and nearly always finishes that afternoon."),
 ("Can you ship a car that does not run from Ankeny?","Yes. We dispatch a carrier with a winch. The extra loading time is inside the quote from the start. The Oralabor retail center or the college lots give the driver level pavement. Let us know whether it rolls, steers, and brakes."),
 ("Can you deliver on the DMACC or Iowa State move-in date?","Yes. The community college on Ankeny Boulevard takes cars in each August and sends them home in May. The university in Ames runs the same calendar thirty minutes north. A parent sets it up, and an adult over eighteen signs at a campus lot. The window is pinned to move-in day and travels with it."),
 ("What do you need for an Ankeny car shipping quote?","Both addresses, with the side of Ankeny Boulevard and the nearest main road here. Year, make, and model. Whether it runs. Open or enclosed. The week around the closing or the start date. Those five make a full Ankeny request, and the number follows within the day."),
]
BODY.append(faq_section(FAQ,'Ankeny FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Ankeny?','The form above puts a number on your lane in two minutes. Give us the side of Ankeny Boulevard and the week, and a carrier already on 35 takes it.','+15153732431','(515) 373-2431','Get your free Ankeny quote'))

build({
 'slug':'auto-transport-ankeny-iowa',
 'title':'Car Shipping in Ankeny, IA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Ankeny, IA, the fastest-growing city in Iowa, ten minutes up Interstate 35 from Des Moines. Closing-date deliveries for insurer and plant relocations, Uptown meeting spots, Prairie Trail and north-side curbside pickups, DMACC and Iowa State students, SummerFest, the State Fair, the derecho, and the ground blizzards. Local office on Linden Street in Uptown. Free quote.',
 'h1':'Car Shipping in<br>Ankeny, <span class="accent">Iowa</span>',
 'lede':'Open, enclosed, and expedited auto transport across the north side of the Des Moines metro, planned around 35, the closing date, the fair, and the winter.',
 'tel':'+15153732431','disp':'(515) 373-2431','brand':'Ankeny','keyword':'car shipping in ankeny',
 'localterms':['ankeny','des moines','metro','interstate 35','interstate 80','interchange','ankeny boulevard','highway 69','oralabor','1st street','18th street','36th street','delaware','state street','irvinedale','prairie trail','parkway','bike trail','rail line','highway 415','polk city','uptown','3rd street','linden','storefronts','old grids','the district','market','high school','cul-de-sacs','north side','east side','airport','plant','johnston','grimes','guard camp','seed company','bondurant','altoona','warehouses','data centers','casino','amusement park','saylorville','lake','ames','university','west des moines','insurers','tractor maker','sprayers','cotton pickers','engineers','supervisors','convenience-store chain','headquarters','managers','analysts','hospitals','nurses','clinic','community college','largest','parent','campus lot','soldiers','orders','summerfest','carnival','parade','fourth of july','state fair','fairgrounds','drake relays','stadium','2020 derecho','sirens','2018 tornado','spillway','2008','ground blizzard','truck stops','ice','humidity','omaha','kansas city','minneapolis','chicago','st. louis','milwaukee','indianapolis','denver','dallas','nashville','merle hay'],
}, BODY, FAQ)
