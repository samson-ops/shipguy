import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Rochester, Minnesota','Car shipping in the clinic city, where the calendar runs on residency years and treatment stays',
 ['Car shipping in Rochester runs up Highway 52 to the Twin Cities and along 90 across the south. Ship Guy is a licensed auto transport broker with an office on 3rd Avenue Southeast downtown.',
  'We book vetted carriers across Rochester, from Pill Hill to the Northwest subdivisions and out to Byron. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Highway 52 is the freeway through town, eighty-five miles to the Twin Cities. Highway 14 crosses east to Winona and west to Owatonna. Highway 63 is Broadway, south to the airport and north to Red Wing. Interstate 90 runs ten miles south with the 52 and 63 exits.',
  'This page covers 52, 14, 63, 90, downtown, Pill Hill, Kutzky Park, and the subdivisions. It also covers the clinic calendar, the old computer campus, the colleges, the snowbird lane, and the blizzards.'],
 'Rochester at a glance',
 ['Most pickups happen within 1 to 3 days. The 52 carriers come down from the Twin Cities daily. The 90 carriers pass between Sioux Falls and Chicago. The Twin Cities pool is an hour and a half north.',
  'The Twin Cities ride a single day on the truck. Madison, Des Moines, and Sioux Falls take a day. Chicago and Milwaukee take one to two, and Denver takes two.'],
 'Tell us the neighborhood. Pill Hill, Kutzky Park, and the downtown blocks meet the truck on a main road. The Northwest subdivisions, Northern Hills, Meadow Park, and the Southeast grids usually allow the curb.'))

BODY.append(sec('The Roads','Highway 52, Highway 14, Highway 63, Interstate 90, Broadway, Civic Center Drive, and 2nd Street',
 prose(
  L('Rochester is a freeway through a prairie town, and the clinic sits in the middle. The carriers come off 52 and go no farther than they have to.'),
  P('Highway 52 enters from the north past the old computer campus. It runs as a freeway down the west side of downtown. It meets Highway 14 at the south end by the mall and continues to 90. The Twin Cities are eighty-five miles up it. The road is open prairie for most of that, and the wind blows it shut in a blizzard. Highway 14 runs east through the hills to Winona and the river. It runs west through Byron and Kasson to Owatonna and 35.'),
  P('Highway 63 is Broadway through downtown. It runs south past the airport to Iowa and north to Red Wing. Interstate 90 runs ten miles south of the city. The 52 and 63 exits are the way in from Sioux Falls or Chicago. Civic Center Drive follows the river along the north edge of downtown. 2nd Street Southwest is the hospital street, and it fills at every shift change.'),
  P('The carriers come off 52 at Civic Center Drive, 2nd Street, or 16th Street. The mall lot at 52 and 14 is the usual meeting spot. The big-box lots on the north end along 52 work too. So do the civic center lots downtown and the fairgrounds lots on the east side. The airport cell lot works for a fly-and-ship.'),
  P('Our office is on 3rd Avenue Southeast downtown, a few blocks east of Broadway and the clinic campus.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Pill Hill, Kutzky Park, Slatterly Park, Folwell, Elton Hills, the Northwest, Northern Hills, Meadow Park, and the Southeast',
 prose(
  L('Rochester is a dense old core around the clinic and wide new subdivisions on every edge. The truck meets the old core on a main road.'),
  P('Downtown is the clinic campus and the towers around it, with a subway and skyway system underneath. The streets are one way and full of shuttles. The driver meets you at the civic center lots or on Civic Center Drive. Pill Hill southwest of downtown is the doctors’ old neighborhood, hilly streets of big houses on narrow lots. A trailer does not enter. The handoff moves to 2nd Street or to the mall.'),
  P('Kutzky Park northwest of downtown is an old grid along the river with narrow streets and alley garages. The driver meets you on 7th Street or at the lots on Civic Center Drive. Slatterly Park and the Southeast grids around the college are plain blocks where the curb usually works. Folwell and Mayowood Road to the southwest are winding and wooded. The handoff moves to 16th Street.'),
  P('Elton Hills and the north grids are wide postwar streets, and the truck reaches the curb. The Northwest subdivisions off 52 are the newest part of the city. The streets are wide, and the cul-de-sacs are the only problem. Northern Hills and the Northeast are the same. Meadow Park, Bamber Valley, and the south subdivisions off 63 allow the curb nearly everywhere.'),
  P('Byron and Kasson ship with the same trucks and price the same as Rochester. So do Stewartville and Pine Island. Winona is forty-five miles east on 14 and adds a few hours. Austin and Owatonna sit on the 90 and 35 carriers and price with the city.'),
 )))

ROUTES=[("Minneapolis / St. Paul, MN","US-52 · ~85 mi","Same day","$160–$260"),("Madison, WI","I-90 · ~220 mi","Same day","$230–$350"),
 ("Des Moines, IA","I-35 · ~200 mi","Same day","$230–$350"),("Sioux Falls, SD","I-90 · ~240 mi","1 day","$250–$380"),
 ("Milwaukee, WI","I-90/I-94 · ~290 mi","1 day","$280–$410"),("Chicago, IL","I-90 · ~330 mi","1 day","$300–$440"),
 ("Omaha, NE","I-35/I-80 · ~330 mi","1 day","$320–$460"),("Kansas City, MO","I-35 · ~440 mi","1–2 days","$400–$570"),
 ("Denver, CO","I-80 · ~850 mi","2 days","$600–$850"),("Phoenix, AZ","I-35/I-40 · ~1,600 mi","3–4 days","$950–$1,350")]
BODY.append(rate_table('Lanes &amp; Costs','Rochester Car Shipping Lanes and Estimated Costs',
 'The lanes southeast Minnesota cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Rochester, sedan that runs, open trailer. Expect an SUV or a pickup to add 10 to 25 percent, and enclosed to add more. The week you choose and the carriers on 52 and 90 that week set the real figure.',
 prose(
  P('Rochester prices like the south end of the Twin Cities pool, because that is what it is. The Twin Cities lane rides 52 and fills every day. The Chicago lane rides 90 and 94 through Madison. The Iowa lanes ride 52 and 35 south. The Arizona lane fills each October with the snowbirds, and the price rises with the demand.'),
  P('A start date at the clinic in late June or the August move-in means a busy week. What size, condition, and timing do to the figure is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Clinic, the Construction, the Old Computer Campus, the Device Makers, the Colleges, and the Snowbirds',
 prose(
  L('Rochester relocates physicians, researchers, patients, engineers, and students. The clinic moves more households than the rest of the city combined.'),
  P('The clinic downtown is the largest employer in the state. Residents and fellows arrive every June for a July start, and a new class leaves the same week. Visiting physicians come on contracts that start all year. Nurses and technicians arrive by the hundred. Families relocating for a long treatment ship a car for the stay. The handoff for all of them happens at the civic center lots or the mall. If the clinic or an employer pays you back for the move, we write up what it needs.'),
  P('The downtown construction program has rebuilt block after block for a decade. Project managers and trades move in on contract dates. The old computer campus on the north end still houses engineers for a half-dozen tenants. The device makers around the clinic hire the same way. The hotels and the restaurants that serve the patients staff up every spring.'),
  P('The community college on the east side takes student cars in late August. The university branch downtown does the same, and the state university’s Rochester campus follows. A parent books it, and an adult meets the driver at a lot to sign. The cars go home in May. Crossing a state line adds paperwork, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page explains it.'),
  P('Retirees who came for the clinic stay for it, and many leave for Arizona each October. The Mesa and Phoenix lane is the busiest long lane out of the city. They come back in April, and the lane runs the other way.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Rochesterfest, Thursdays Downtown, the Fair, the July Changeover, Move-In Week, the Blizzards, the Ice, and the Floods',
 prose(
  L('Rochester runs on the clinic calendar. The weather problem is open prairie between the city and everywhere else.'),
  P('Rochesterfest fills downtown for a week in late June and closes streets around the river. Thursdays Downtown closes 1st Avenue every summer Thursday. The county fair fills the fairgrounds on the east side in late July. The July changeover brings a new class of residents and sends the old one home the same week. Move-in week in late August fills the blocks around the college. Book three weeks ahead for a late June date.'),
  P('Winter runs from November into March. The city plows the clinic routes first, and the subdivisions wait. A blizzard closes 52 and 90 a few times each winter. There is nothing to stop the wind. The February 2019 storms closed stretches of 90 across the south and stopped 52 for a day. The carriers wait in the Twin Cities or in Albert Lea until the plows finish. An ice storm shifts a handoff to the afternoon.'),
  P('The Zumbro flooded the city in July 1978, and the flood walls downtown came from it. The channel has held since. The August 2007 rain flooded the river towns east of the city. It closed 14 near Winona for days. A heavy summer rain closes a low crossing for a morning, and the handoff moves.'),
  P('Summer brings heat and afternoon storms with hail. A carrier does not load under a hail warning. The storms clear by evening, and the day shifts by a few hours.'),
 )+chips(["Downtown","The Clinic","Civic Center","Pill Hill","Kutzky Park","Slatterly Park","Folwell","Mayowood","Elton Hills","Northrop","The Northwest","Northern Hills","Northeast","Meadow Park","Bamber Valley","Willow Creek","Southeast","Marion Road","Eastside","Byron","Kasson","Stewartville","Pine Island","Oronoco","Chatfield","Winona","Austin","Owatonna","Red Wing"])
 +NOTE('Serving Rochester and the whole of southeast Minnesota, Pill Hill block or Northwest cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Rochester?',
 prose(
  L('Open trailers carry most of southeast Minnesota, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the salt, the brine the county sprays before a storm, and the hail. The collectors in Pill Hill book one. So do the physicians bringing a car worth more than the rest of the move. When a blizzard is coming, the car leaves on whatever truck has a spot. We tell you that up front.'),
  P('A daily driver or a student’s car rides an open trailer without any trouble. Compare the two on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('The price comes first, then a meeting spot at the mall or the civic center. The clinic start date usually picks the week.'),
  P('Once you approve the price, we assign a carrier already coming down 52 that week. The lot and the two-hour window are set the same afternoon. The driver photographs the car at pickup and notes every mark on the Bill of Lading. Your initials go on that sheet, and it settles any question at delivery.'),
 )+ULI([
  "Personal items out of the cabin and the trunk",
  "A quarter tank of fuel, no more",
  "Photos of every side and the odometer before pickup",
  "One good key, plus a note about any known faults",
  "Any add-on alarm switched off",
  "In Pill Hill, Kutzky Park, or downtown, expect to meet on a main road",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks through the sequence, and the <a href="car-shipping-preparation.html">preparation</a> page has the full checklist.'))))

BODY.append(sec('Why Ship Guy','Why Rochester Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 52 every day. We know the clinic calendar and which week it fills.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on 3rd Avenue Southeast downtown.'),
  P('One coordinator handles your move from the first call to the delivery signature. The <a href="services.html">services</a> page lays out open, enclosed, and expedited.'),
 )))

BODY.append(office('Rochester','300 3rd Ave SE Suites 258','Rochester, MN 55904','+15077131601','(507) 713-1601','CT',
 '300+3rd+Ave+SE+Suites+258,+Rochester,+MN+55904','Visit Us','Find Ship Guy in Rochester',
 'Our office is on 3rd Avenue Southeast downtown, a few blocks east of Broadway and the clinic campus.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3541.4884360944775!2d-92.458438!3d44.020280199999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87f9e1e32bc21891%3A0xecd7584828f90b9a!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629256894!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Rochester to the Twin Cities or Chicago?","The Twin Cities run one hundred sixty to two hundred sixty dollars for a sedan. That is eighty-five miles up 52 and the lowest lane on the table. Chicago runs three hundred to four hundred forty, about three hundred thirty miles on 90. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Do you ship cars for Mayo Clinic residents, fellows, and patients?","Yes, every week of the year. Residents and fellows arrive in late June for the July start. That is the busiest week on our calendar. Families here for a long treatment ship a car for the stay and send it home after. The handoff happens at the civic center lots or the mall. When the clinic or an employer reimburses the move, the documentation comes from our office. Ship Guy is a private broker with no tie to the clinic."),
 ("Can the carrier come to my street in Pill Hill or Kutzky Park?","No. Pill Hill is hilly, narrow, and tree-lined, and Kutzky Park is an old grid with alley garages. The driver meets you on 2nd Street, Civic Center Drive, or at the mall. Elton Hills, the Northwest, Northern Hills, Meadow Park, and the Southeast grids usually allow the curb."),
 ("Can you ship a car to Arizona for the winter?","Yes, and it is the busiest long lane out of Rochester. The snowbirds leave in October and come back in April. Phoenix runs nine hundred fifty to thirteen hundred fifty dollars for a sedan. Book three weeks ahead for an October date, because the whole state leaves the same month."),
 ("Can you deliver on an RCTC or UMR move-in date?","Yes. The community college takes cars in late August, and the university branch downtown follows the same week. Mom or Dad books, and an adult signs at a lot. The college blocks are packed that week, so we meet at the fairgrounds lots. Your date sets the window."),
 ("Can you ship a car to or from Byron, Stewartville, or Winona?","Yes. Byron and Stewartville ride the same carriers and price the same as Rochester. Pine Island and Kasson do too. Winona is forty-five miles east on 14 and adds a few hours on the day. The river bluffs there keep the handoff on a main road."),
 ("What happens if a blizzard closes 52 or 90 on my pickup day?","The truck holds in the Twin Cities or Albert Lea until the plows finish, usually a day. We call as soon as the closure posts. Your pickup slides to the first clear morning at the same price. Give a February date a flexible week."),
 ("Does the downtown construction affect my pickup?","Yes, a little. The blocks around the clinic have been under construction for a decade. The lane closures move every month. We do not meet downtown. The handoff happens at the civic center lots or the mall at 52 and 14. The driver never enters the work zone."),
 ("Can you ship a car that does not run from Rochester?","Yes. A winch-equipped carrier takes it, and the loading time is in the quote from the start. The mall lots and the big-box lots along 52 are flat enough. We need to know whether it rolls, steers, and brakes."),
 ("What do you need for a Rochester car shipping quote?","Both addresses with the neighborhood, the year, make, and model, and whether it runs. Then open or enclosed and the week around the start date. With those in hand, the Rochester figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Rochester FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Rochester?','Two minutes on the form above gets your lane a Rochester figure. Name the neighborhood and the week, and a carrier already coming down 52 takes it.','+15077131601','(507) 713-1601','Get your free Rochester quote'))

build({
 'slug':'auto-transport-rochester-minnesota',
 'title':'Car Shipping in Rochester, MN — Auto Transport | Ship Guy',
 'meta':'Car shipping in Rochester, MN, the clinic city on Highway 52. Residency-year and treatment-stay moves, the snowbird lane to Arizona, main-road handoffs for Pill Hill and Kutzky Park, curbside pickups in the Northwest and the Southeast, and the blizzards on 52 and 90. Local office on 3rd Avenue Southeast downtown. Free quote.',
 'h1':'Car Shipping in<br>Rochester, <span class="accent">Minnesota</span>',
 'lede':'Open, enclosed, and expedited auto transport across Rochester and southeast Minnesota, planned around 52, 90, the clinic calendar, the campus dates, and the winter.',
 'tel':'+15077131601','disp':'(507) 713-1601','brand':'Rochester','keyword':'car shipping in rochester',
 'localterms':['rochester','clinic','highway 52','twin cities','interstate 90','highway 14','highway 63','broadway','downtown','pill hill','kutzky park','civic center','2nd street','mall','airport','winona','owatonna','red wing','byron','kasson','stewartville','pine island','austin','albert lea','sioux falls','chicago','madison','des moines','milwaukee','omaha','kansas city','denver','phoenix','mesa','arizona','snowbirds','residents','fellows','physicians','researchers','patients','engineers','students','computer campus','device makers','construction','subway','skyway','shuttles','slatterly park','folwell','mayowood','elton hills','northwest','northern hills','northeast','meadow park','bamber valley','subdivisions','cul-de-sacs','community college','university branch','fairgrounds','rochesterfest','thursdays downtown','county fair','july changeover','move-in','blizzard','february 2019','zumbro','july 1978','flood walls','august 2007','hail','salt','brine','bill of lading','fmcsa','winch','prairie','16th street','7th street','1st avenue','plows'],
}, BODY, FAQ)
