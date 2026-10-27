import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Waukegan, Illinois','Car shipping on the Lake Michigan bluff, between the Tri-State Tollway and the Wisconsin line',
 ['Car shipping in Waukegan runs off the Tri-State Tollway and Route 41 west of the city. Ship Guy is a licensed auto transport broker with an office on Genesee Street downtown.',
  'We book vetted carriers across Lake County, from Zion to North Chicago and west to Gurnee and Grayslake. The trucks are not ours.',
  'Interstate 94 is the Tri-State, the tollway between Chicago and Milwaukee. Its exits are Grand Avenue, Belvidere Road, and Buckley Road. Route 41 is the free road beside it. Green Bay Road, Lewis Avenue, and Sheridan Road run north and south through the city. Belvidere, Grand, and Washington cross it.',
  'This page covers the tollway, Route 41, downtown, the lakefront, Gurnee, and the naval station. It also covers the pharmaceutical corridor, the hospitals, Six Flags traffic, the lake snow, and the lanes.'],
 'Waukegan at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between Chicago and Milwaukee passes the city on 94 or 41.',
  'Chicago and Milwaukee are an hour each way. Madison and Rockford are two. Indianapolis, Detroit, St. Louis, and Minneapolis are a same-day haul. The coasts need three to five.'],
 'Tell us the side of Green Bay Road. Downtown and the south side need a meeting spot. The northwest subdivisions, Gurnee, and Beach Park usually allow the curb.'))

BODY.append(sec('The Roads','The Tri-State Tollway, Route 41, Green Bay Road, Belvidere Road, and Sheridan Road',
 prose(
  L('Waukegan sits on the lane between Chicago and Milwaukee. The car haulers run it in both directions all day.'),
  P('Interstate 94 is the Tri-State Tollway, and it runs north and south four miles west of downtown. The exits at Grand Avenue, Belvidere Road, Buckley Road, and Rosecrans serve the city. The tolls are electronic, and the carriers pay them with a transponder. Route 41 is the Skokie Highway, the free four-lane between the tollway and the city. Many carriers prefer it.'),
  P('Green Bay Road is Route 131, the north-south road through the west side of the city. Lewis Avenue runs the middle. Sheridan Road runs the lakefront south through North Chicago to the naval station. Belvidere Road is Route 120, the main road across the city from the lake to the tollway. Grand Avenue is Route 132, the road to Gurnee and the amusement park.'),
  P('Washington Street runs from the tollway to downtown and down the bluff to the harbor. Glen Flora Avenue and Yorkhouse Road cross the north side. Delany Road carries the far west. The Amstutz Expressway runs along the lakefront from downtown to North Chicago. Genesee Street is the downtown spine, with the courthouse and the theater on it.'),
  P('The carriers come off 94 at Belvidere and Grand, and off 41 at Washington and Belvidere. Fountain Square on Belvidere, the mall in Gurnee, and the lakefront have the usual meeting lots. The tollway is the only toll in the county. Route 41 and every city street are free.'),
  P('Our office is on Genesee Street downtown, a block from the courthouse and the theater.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown and the Bluff, the Lakefront, the South Side, the North Side, the Northwest, Gurnee, and North Chicago',
 prose(
  L('Waukegan is an old port city on a bluff. The lake sits below it, and the suburbs fill in to the west.'),
  P('Downtown sits on the bluff above the lake. It is a grid around Genesee Street, the courthouse, and the theater. The streets are narrow and busy on court days. A trailer cannot stop on Genesee. The driver meets you at the station lots, the county garage, or the lakefront. The harbor and the marina sit below the bluff with wide lots along the Amstutz.'),
  P('The south side between Sheridan and Lewis is the oldest part of the city. It is a dense grid of small lots and narrow streets. The driver meets you on Sheridan, on 10th Street, or at the shopping center on Belvidere. The north side around Bowen Park and Glen Flora is older grids with alleys. The handoff moves to Glen Flora or Lewis.'),
  P('The northwest off Yorkhouse, Lewis, and Delany is subdivisions from the last forty years, with wide streets. The truck reaches the curb. The west side along Green Bay Road and Belvidere is the retail strip. Fountain Square and the big lots sit there. Beach Park, Zion, and Winthrop Harbor to the north are wide-street suburbs with lots on every main road.'),
  P('Gurnee to the west has the amusement park, the mall, and subdivisions with wide streets. Grayslake, Libertyville, and Wadsworth beyond it are the same. North Chicago to the south holds the naval station and the pharmaceutical campus. The base gates open onto Sheridan. Lake Bluff and Lake Forest farther south have narrow lanes under old trees. The driver meets you on Route 41. All of them price the same as Waukegan.'),
 )))

ROUTES=[("Chicago, IL","I-94 · ~40 mi","Same day","$120–$200"),("Milwaukee, WI","I-94 · ~50 mi","Same day","$130–$210"),
 ("Rockford, IL","IL-120/I-90 · ~90 mi","Same day","$150–$240"),("Madison, WI","I-94/I-90 · ~130 mi","Same day","$170–$280"),
 ("Indianapolis, IN","I-94/I-65 · ~220 mi","Same day","$230–$350"),("Detroit, MI","I-94 · ~320 mi","1 day","$300–$440"),
 ("St. Louis, MO","I-94/I-55 · ~340 mi","1 day","$320–$460"),("Minneapolis, MN","I-94 · ~370 mi","1 day","$340–$490"),
 ("Dallas, TX","I-55/I-44 · ~1,000 mi","2–3 days","$700–$980"),("Orlando, FL","I-65/I-75 · ~1,250 mi","3 days","$830–$1,170")]
BODY.append(rate_table('Lanes &amp; Costs','Waukegan Car Shipping Lanes and Estimated Costs',
 'The lanes Lake County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates leaving Waukegan, sedan in running order, open trailer. SUVs and pickups add 10 to 25 percent, enclosed adds more, and the tollway charge is already in. The week, the direction, and the carriers free on your dates decide the final figure.',
 prose(
  P('Waukegan prices with Chicago on the long lanes. The carriers fill in the city and top off here on the way to Milwaukee. The Milwaukee and Madison lanes price the lowest of any suburb. The trucks pass the door on 94. The Minneapolis lane runs the same way.'),
  P('Florida and Texas rise with the snowbirds each fall and ease off in the spring. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Naval Station, the Pharmaceutical Corridor, the Hospitals, the County, and the Warehouses',
 prose(
  L('Waukegan relocates sailors, pharmaceutical staff, nurses, and county employees. The base and the corridor move more people than anyone.'),
  P('The naval station in North Chicago is the Navy’s only boot camp. It trains sailors by the thousand. Instructors and the families at the technical schools arrive on orders all year. They settle from Waukegan to Gurnee. The orders cover one car, and the second one comes with us. Ship Guy is a private broker with no connection to the base. The <a href="military-car-shipping.html">military</a> page covers the timing around a report date.'),
  P('The pharmaceutical campus in North Chicago and the corridor south to Deerfield hire from every state. Scientists, managers, and sales staff arrive every month. Many ship a second car behind the move. The medical-supply warehouses along the tollway move managers the same way. We supply the paperwork a reimbursed move needs.'),
  P('The east side hospital and the ones in Libertyville and Lake Forest bring in nurses all year. The county government downtown moves attorneys and staff in every month. The medical university in North Chicago brings students in each August, and a parent ships the car. An adult signs at a campus lot.'),
  P('Families priced out of the North Shore buy on the northwest side, in Beach Park, and in Gurnee. One car ships while the other is driven. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Six Flags Season, Graduation Fridays, the Lakefront, the Lake Snow, and the Des Plaines',
 prose(
  L('Waukegan runs on an amusement-park summer, a Navy graduation every Friday, and a lake-effect winter.'),
  P('The amusement park in Gurnee opens in May and runs through the October haunt. Grand Avenue backs up from the tollway to the gates on summer weekends. The mall lots fill by noon. A pickup on Grand that season moves to the morning or to Belvidere Road. Fright Fest weekends in October are the worst of it.'),
  P('The naval station graduates a class of recruits most Fridays. The families fill the hotels from Gurnee to the lakefront. Sheridan Road and the base gates run slow from dawn. A handoff on Sheridan on a Friday moves to the west side. The lakefront fills for the Fourth of July and the summer concerts, and the harbor lots go early.'),
  P('The lake makes the weather. Snow comes off the water, and Waukegan gets more of it than the inland suburbs. The 2011 blizzard buried the lakefront and closed 94 for a day. Fog sits on the bluff in spring and fall. The carriers park at the truck stops by the Wisconsin line until the plows finish. A winter pickup can lose a day.'),
  P('The Des Plaines River floods Gurnee. The 2017 flood closed Grand Avenue and Belvidere Road at the river for a week. The 2013 flood did the same. A pickup on the river side of Gurnee moves to the mall or to Route 41. The bluff never floods. Summer storms off the lake take the trees down a few times a year. The sirens sound a few times each spring.'),
 )+chips(["Downtown","Genesee Street","Courthouse","Station","Bluff","Lakefront","Harbor","Marina","Amstutz","South Side","Sheridan","10th Street","North Side","Bowen Park","Glen Flora","Lewis Avenue","Northwest","Yorkhouse","Delany","West Side","Green Bay Road","Belvidere Road","Fountain Square","Beach Park","Zion","Winthrop Harbor","Gurnee","Grand Avenue","Park City","Grayslake","Libertyville","Wadsworth","North Chicago","Naval Station","Lake Bluff","Lake Forest"])
 +NOTE('Serving Waukegan, Gurnee, North Chicago, and all of Lake County, bluff street or subdivision. Tell us the side of Green Bay Road and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Waukegan?',
 prose(
  L('Open trailers move most Lake County cars, and the lane table is priced for one.'),
  P('An enclosed trailer keeps the salt, the lake grit, and the weather off. The North Shore collectors book one for the show cars. Sailors shipping a new car to the next duty station book one too.'),
  P('A commuter car or a work van goes open and arrives in the shape it left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a handoff at Fountain Square or the lakefront, and a signature at the other end. The report date sets the week.'),
  P('Confirm the number, and we hand the car to a carrier already running 94 or 41. The lot and the window reach you that day. At the handoff, the driver goes over the car and writes its condition on a Bill of Lading. You both sign, and the delivery uses the same sheet.'),
 )+ULI([
  "Take everything personal out of the car, sea bag included",
  "Keep the fuel at about a quarter tank",
  "Photograph every side of the car and the mileage before pickup",
  "Give the driver one working key and name any fault",
  "Turn off any aftermarket alarm",
  "Downtown or on the south side, meet the truck at the station lots or at the lakefront",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Waukegan Drivers Choose Ship Guy',
 prose(
  L('We put your car on the carriers already running between Chicago and Milwaukee. We plan around the base calendar, the park traffic, and the lake snow.'),
  P('Ship Guy holds active FMCSA brokerage authority with a $75,000 surety bond, and the federal register lists both. Our office is on Genesee Street downtown.'),
  P('The coordinator who prices the move is the one on the phone until the car is signed for. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Waukegan','13 N Genesee St #452','Waukegan, IL 60085','+12244972802','(224) 497-2802','CT',
 '13+N+Genesee+St+%23452,+Waukegan,+IL+60085','Visit Us','Find Ship Guy in Waukegan',
 'Our office is on Genesee Street downtown, a block from the courthouse and the theater.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4533.587264826198!2d-87.8310389!3d42.3601034!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880fed7160d9ea4b%3A0xb6dfb1dd47d7baee!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793024733304!5m2!1sen!2sus'))

FAQ=[
 ("Do you ship cars for sailors at Great Lakes?","Yes, all year. Instructors and the families of the technical schools arrive on orders and settle from Waukegan to Gurnee. The orders cover one car, and we move the second. Recruits in boot camp cannot keep a car, so a family car waits until the orders come. Ship Guy is a private broker with no connection to the base. Send the report date, and we build the window around it."),
 ("How much does it cost to ship a car from Waukegan to Chicago or Milwaukee?","Chicago runs one hundred twenty to two hundred dollars for a sedan, about forty miles down the tollway. Milwaukee runs one hundred thirty to two hundred ten, about fifty miles up 94. Madison and Rockford price a little higher. Tolls are included. Figure 10 to 25 percent more for an SUV or a pickup."),
 ("Can the carrier come to my street downtown or on the south side?","Usually not. Genesee Street is narrow and busy on court days. The south side is small lots on tight streets. The driver meets you at the station lots, the county garage, Sheridan, or the lakefront. The northwest subdivisions, Gurnee, and Beach Park usually allow the curb."),
 ("Does Six Flags traffic affect my pickup?","On Grand Avenue, yes. The park backs Grand up from the tollway to the gates on summer weekends. The Fright Fest weekends in October are worse. We move a pickup on Grand to the morning or to Belvidere Road. The rest of the county runs normally."),
 ("Do you ship cars for people relocating to the pharmaceutical companies?","Yes, every month. The campus in North Chicago and the corridor south to Deerfield bring in scientists, managers, and sales staff. They come from every state. Many ship a second car behind the move. The handoff works at Fountain Square or a lot off 41. We provide the paperwork a reimbursed move needs."),
 ("Can you ship a car to or from Gurnee, Zion, or North Chicago?","Yes, and all three price the same as Waukegan. Gurnee rides the same carriers off 94 at Grand. Zion and Beach Park ride them off 41 and Green Bay Road. North Chicago rides them off 41 at Buckley, and the handoff sits outside the base gates. Send the full address for a new subdivision."),
 ("What happens if lake snow or the river hits on my pickup day?","Snow off the lake closes 94 a few times a winter. The carriers wait at the truck stops by the state line for the plows. A winter pickup can slip a day, and we call before it does. The Des Plaines closes Grand and Belvidere at the river in Gurnee after a big storm. A pickup on the river side moves to the mall or to Route 41."),
 ("Can you ship a car that does not run from Waukegan?","Yes. A winch truck is sent, and the quote carries the loading time from the first number. The lakefront lots or Fountain Square give the driver level pavement. Tell us whether the car rolls, steers, and brakes."),
 ("Does the carrier use the tollway, and do I pay the toll?","The carrier chooses. Many take Route 41, which is free and runs beside the tollway. The ones that take 94 pay with a transponder, and the toll sits inside the quote. You never see a separate charge either way."),
 ("What do you need for a Waukegan car shipping quote?","Pickup and delivery addresses, with the side of Green Bay Road or the suburb. Year, make, model. Whether it drives. Open or enclosed. The week around the report date or the closing. With those five, the Waukegan quote comes back within the day."),
]
BODY.append(faq_section(FAQ,'Waukegan FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Waukegan?','Two minutes on the form above prices your lane. Send the side of Green Bay Road and your dates, and a carrier already on 94 takes it.','+12244972802','(224) 497-2802','Get your free Waukegan quote'))

build({
 'slug':'auto-transport-waukegan-illinois',
 'title':'Car Shipping in Waukegan, IL — Auto Transport | Ship Guy',
 'meta':'Car shipping in Waukegan, IL on the Lake Michigan bluff, between the Tri-State Tollway and the Wisconsin line. Great Lakes Navy moves, pharmaceutical-corridor relocations, downtown and south side meeting spots, northwest and Gurnee curbside pickups, Six Flags traffic, graduation Fridays, and the lake snow. Local office on Genesee Street. Free quote.',
 'h1':'Car Shipping in<br>Waukegan, <span class="accent">Illinois</span>',
 'lede':'Open, enclosed, and expedited auto transport across Lake County, planned around 94, Route 41, the base calendar, the park traffic, and the lake snow.',
 'tel':'+12244972802','disp':'(224) 497-2802','brand':'Waukegan','keyword':'car shipping in waukegan',
 'localterms':['waukegan','lake michigan','bluff','tri-state','tollway','interstate 94','route 41','skokie highway','transponder','green bay road','route 131','lewis avenue','sheridan road','belvidere road','route 120','grand avenue','route 132','washington street','glen flora','yorkhouse','delany','amstutz','genesee street','buckley','rosecrans','downtown','courthouse','theater','station','harbor','marina','lakefront','south side','10th street','north side','bowen park','northwest','west side','fountain square','beach park','zion','winthrop harbor','gurnee','mall','grayslake','libertyville','wadsworth','north chicago','naval station','base gates','lake bluff','lake forest','north shore','sailors','boot camp','instructors','technical schools','orders','report date','pharmaceutical','scientists','deerfield','warehouses','hospital','nurses','county','attorneys','medical university','amusement park','six flags','fright fest','graduation','fridays','fourth of july','snow','2011 blizzard','fog','truck stops','des plaines','2017','2013','storms','sirens','chicago','milwaukee','rockford','madison','indianapolis','detroit','st. louis','minneapolis','dallas','orlando','wisconsin'],
}, BODY, FAQ)
