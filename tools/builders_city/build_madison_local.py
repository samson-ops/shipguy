import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Madison, Wisconsin','Car shipping for the capital and the campus, on Interstate 90 and 94 between Chicago and Minneapolis',
 ['Car shipping in Madison runs on the university calendar more than the seasons. Ship Guy is a licensed auto transport broker with an office on West Washington Avenue downtown.',
  'We book vetted carriers across Dane County, from Middleton and Verona to Sun Prairie, Fitchburg, and Stoughton. We do not own the trucks.',
  'Interstate 39, 90, and 94 share one roadway along the east side of the city. The Beltline carries US 12 and 18 across the south side. US 151 runs from Verona through the city to Sun Prairie and Fond du Lac.',
  'This page covers the interstate and the Beltline, the isthmus and the campus, and the suburbs. It also covers the software campus, the hospitals, the Capitol calendar, the winter, and the lanes.'],
 'Madison at a glance',
 ['Most pickups happen within 1 to 3 days. The Chicago-to-Minneapolis carriers pass the east side on 90 and 94 all day.',
  'Milwaukee, Rockford, and Dubuque are same-day lanes. Chicago is the same day too. Minneapolis, Des Moines, and Indianapolis take a day. Detroit takes one to two.'],
 'Tell us the neighborhood. The isthmus, the campus blocks, and the near east side need a meeting spot. Middleton, Fitchburg, and the suburbs usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 39, 90, 94, the Beltline, and US 151',
 prose(
  L('Madison sits on the lane between the two biggest carrier hubs in the Upper Midwest.'),
  P('Interstate 90 and 94 run together along the east side of the city with Interstate 39. The three split north of town at Portage. Interstate 94 heads east to Milwaukee and 90 heads southeast to Rockford and Chicago. Together they carry the Chicago-to-Minneapolis traffic past Madison every hour.'),
  P('The Beltline is US 12 and 18, and it carries the south side from Middleton to the interstate. US 151 is Verona Road on the southwest side and East Washington Avenue through the city. John Nolen Drive crosses the causeway on Lake Monona into downtown.'),
  P('The interstate exits at East Washington, US 151, and the Beltline are where carriers leave the lane. East Towne and the lots along East Washington are the usual meeting spots. No road in the metro charges a toll.'),
  P('Our office sits on West Washington Avenue downtown, a few blocks from the Capitol.'),
 ), alt=True))

BODY.append(sec('The Isthmus &amp; the Suburbs','The Isthmus, the Campus, the Near East Side, and the Grids',
 prose(
  L('Madison was laid out on a strip of land between two lakes. The strip was planned for carriages.'),
  P('The isthmus between Lake Mendota and Lake Monona holds the Capitol, the campus, and the oldest neighborhoods. State Street is closed to cars. The streets around the Square and the campus are narrow and parked on both sides. The driver meets you at a lot by the Alliant Energy Center or along East Washington.'),
  P('The Near East Side, Tenney-Lapham, Marquette, and Atwood have narrow streets with alleys behind them. A main road nearby is the usual spot. Shorewood Hills, Nakoma, and Maple Bluff have curving streets with mature trees over them. The driver stays on the through road.'),
  P('Middleton, Fitchburg, Verona, Sun Prairie, and Waunakee are wide grids where the truck usually reaches the curb. New subdivisions out past the Beltline are not always on a carrier’s map yet. Send the full address and the nearest cross street.'),
  P('Winter alternate-side parking runs from mid-November to mid-March across most of the city. The driver plans the handoff with that in mind.'),
 )))

ROUTES=[("Milwaukee, WI","I-94 · ~80 mi","Same day","$160–$260"),("Rockford, IL","I-39/I-90 · ~70 mi","Same day","$150–$250"),
 ("Chicago, IL","I-90 · ~150 mi","Same day","$190–$300"),("Green Bay, WI","US-151/I-41 · ~140 mi","Same day","$190–$300"),
 ("Minneapolis, MN","I-94 · ~270 mi","1 day","$270–$400"),("Des Moines, IA","US-151/I-80 · ~290 mi","1 day","$280–$410"),
 ("Indianapolis, IN","I-90/I-65 · ~330 mi","1 day","$300–$440"),("Detroit, MI","I-94 · ~450 mi","1–2 days","$380–$540"),
 ("Denver, CO","I-90/I-80 · ~1,000 mi","2–3 days","$700–$980"),("Orlando, FL","I-65/I-75 · ~1,350 mi","3–4 days","$870–$1,220")]
BODY.append(rate_table('Lanes &amp; Costs','Madison Car Shipping Lanes and Estimated Costs',
 'Where Madison cars go, from the campus to the coasts, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. An SUV or pickup runs about 10 to 25 percent higher, and enclosed higher again. August, the winter, and the carriers free on your dates decide the final number.',
 prose(
  P('Madison prices a little above Milwaukee, because the carriers leave the interstate for it. Chicago and Milwaukee ride 90 and 94, and Minneapolis rides 94 north.'),
  P('The Florida lane fills each October with retirees from the west side and the lake towns. The <a href="car-shipping-cost.html">cost guide</a> breaks the number down further.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Software Campus, the Hospitals, and the Capitol',
 prose(
  L('Madison relocates people on the semester, the hiring class, the residency match, and the legislative session.'),
  P('The state university brings tens of thousands of students to the isthmus each August. It sends them home each May. Most leases in the campus blocks turn over on the same two days in mid-August. The streets fill with moving trucks, and the driver meets you at a lot nearby. An adult signs for a student car.'),
  P('The software campus in Verona hires new graduates by the hundreds. They arrive from every state on start dates. The insurer on the east side and the biotech firms in Fitchburg do the same. When an employer reimburses the shipment, the paperwork it asks for comes from us.'),
  P('The university hospital and the two other systems bring in residents and fellows every June and July. Most arrive from out of state with a car. The handoff happens on University Avenue or at a lot off the Beltline, not in a hospital garage.'),
  P('State government relocates staff on the session calendar, and the agencies hire on the fiscal year in July. The Air National Guard wing at the airport rotates airmen on a smaller scale. The <a href="military-car-shipping.html">military</a> page covers a PCS move, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Move-In Week, Badger Saturdays, the Market, and the Snow',
 prose(
  L('Madison closes its streets for students, football, and farmers. The snow closes the rest.'),
  P('Lease turnover in mid-August fills the isthmus with moving trucks for two days. Home football Saturdays close the streets around the stadium on Regent Street. The farmers’ market rings the Capitol Square every Saturday morning from spring into fall. The driver meets you off the isthmus on those days.'),
  P('The Halloween street party closes State Street for a weekend. Summer festivals close the Square now and then. A downtown pickup on those weekends moves to East Washington or the Beltline.'),
  P('Winter is the long season. Madison gets about fifty inches of snow a year. Blizzards shut 90 and 94 for a day a few times each winter. The carriers hold until the plows are through. A winter pickup can lose a day. Alternate-side parking rules run all winter, so the handoff moves to a lot after a storm.'),
  P('Spring brings the thaw and the road weight limits on the county roads. Summer heat moves the loading hour earlier, and thunderstorms with hail roll through in June and July.'),
 )+chips(["Downtown","Capitol Square","State Street","Campus","Near East Side","Tenney-Lapham","Marquette","Atwood","Willy Street","Hilldale","Shorewood Hills","Nakoma","Monroe Street","Maple Bluff","Middleton","Fitchburg","Verona","Sun Prairie","Waunakee","Monona","McFarland","Stoughton","DeForest","Cottage Grove"])
 +NOTE('Serving the isthmus and all of Dane County. Tell us the neighborhood, the week, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Madison?',
 prose(
  L('Open trailers carry most of what leaves Madison, and the interstate lanes are priced that way.'),
  P('An enclosed trailer keeps salt, slush, and attention off the car. The garages in Maple Bluff and Shorewood Hills book enclosed trailers. So does a car headed to Florida or Arizona for the winter.'),
  P('A student car or a commuter car rides open without trouble. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at a lot, and a delivery at the far end. In Madison the semester sets the week.'),
  P('Accept the price, and a carrier already running 90 or 94 is booked. We choose the lot together. The driver walks the car with you and writes its condition on a Bill of Lading. You both sign it. The same sheet is checked at delivery.'),
 )+ULI([
  "Clear the car of personal items",
  "Leave the fuel at about a quarter tank",
  "Photograph each side before pickup, especially in salt season",
  "Hand over a working key and mention any mechanical issue",
  "Turn off any aftermarket alarm",
  "In August, plan for a lot off the isthmus rather than the campus curb",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages have the rest in order.'))))

BODY.append(sec('Why Ship Guy','Why Madison Drivers Choose Ship Guy',
 prose(
  L('We work 90, 94, and the Beltline every week. We plan around the semester, the Square, and the snow.'),
  P('Ship Guy’s brokerage authority is active with the FMCSA, and a $75,000 surety bond backs it. Both are on the public record. Our office is on West Washington Avenue downtown.'),
  P('One coordinator handles the booking from the first quote to the delivery signature. Open, enclosed, and expedited transport are all on the menu, and the <a href="services.html">services</a> page describes each.'),
 ), alt=True))

BODY.append(office('Madison','345 W Washington Ave #458','Madison, WI 53703','+16082086567','(608) 208-6567','CT',
 '345+W+Washington+Ave+%23458,+Madison,+WI+53703','Visit Us','Find Ship Guy in Madison',
 'Our office is on West Washington Avenue downtown, a few blocks from the Capitol Square.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3597.6658289854045!2d-89.38782429999999!3d43.0716215!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880653a647b90e81%3A0x7f2ff6bdb6fb7fa6!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792076647046!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come onto the isthmus or the campus?","Rarely. State Street is closed to cars. The streets around the Square and the campus are narrow and parked solid. The driver meets you at a lot along East Washington or by the Alliant Energy Center. In August, the lot is the only option."),
 ("How much does it cost to ship a car from Madison to Chicago or Minneapolis?","Chicago runs one hundred ninety to three hundred dollars for a sedan. That is about one hundred fifty miles on Interstate 90. Minneapolis runs two hundred seventy to four hundred, about two hundred seventy miles on 94. Both ride trucks that pass Madison every day. SUVs and pickups add 10 to 25 percent."),
 ("Can you ship a car for a UW–Madison student?","Yes. The cars come in each August and leave each May. Most campus leases turn over on the same two days in mid-August. The isthmus fills with moving trucks. The driver meets you at a lot off the isthmus. An adult signs at pickup, and a parent can sign at delivery."),
 ("Does a Badger home football Saturday affect my pickup?","On the near west side, yes. The streets around the stadium on Regent Street and Breese Terrace close hours before kickoff. We move a campus-area pickup to a weekday instead. The east side and the suburbs run normally."),
 ("Do you handle relocations to the software campus in Verona?","Yes, in every hiring class. New employees arrive from every state on start dates, and most ship a car rather than drive it. Verona and the west side subdivisions allow the curb. We plan the pickup around the first day, and we provide the paperwork an employer asks for."),
 ("What happens if a blizzard hits on my pickup day?","The driver waits for the plows and for 90 and 94 to reopen. A winter pickup can slide a day. We call as soon as the forecast changes the plan. After a storm, the handoff moves to a plowed lot."),
 ("Can you pick up in Middleton, Sun Prairie, or Fitchburg?","Yes, and those are the easiest pickups in the metro. The streets are wide grids, and the truck usually reaches the curb. The newest subdivisions past the Beltline are not always on a carrier’s map, so send the full address."),
 ("Do you ship cars for residents at the university hospital?","Yes, every June and July. Residents and fellows arrive from every state, and most bring a car. The handoff happens on University Avenue or at a lot off the Beltline, not in the hospital ramp."),
 ("Can you ship a car that does not run from Madison?","Yes. The carrier brings a winch, and the extra time to load it is in the price. The spot has to be flat, which means a lot rather than a sloped isthmus street. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Madison car shipping quote?","Both addresses, with the neighborhood or the suburb on this end. The year, make, and model. Whether it runs. Open or enclosed. Your dates, with move-in week in mind. That is everything a Madison quote needs."),
]
BODY.append(faq_section(FAQ,'Madison FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Madison?','Price the trip on the form above in about two minutes. Send the neighborhood and your dates, and a carrier already passing the east side takes it from there.','+16082086567','(608) 208-6567','Get your free Madison quote'))

build({
 'slug':'auto-transport-madison-wisconsin',
 'title':'Car Shipping in Madison, WI — Auto Transport | Ship Guy',
 'meta':'Car shipping in Madison, WI on the Chicago-to-Minneapolis lane. Isthmus and campus handoffs, mid-August lease turnover, Badger Saturdays, Verona software campus and hospital relocations, Capitol calendar, blizzard planning. Local office on West Washington Avenue. Free quote.',
 'h1':'Car Shipping in<br>Madison, <span class="accent">Wisconsin</span>',
 'lede':'Open, enclosed, and expedited auto transport across Dane County, planned around the isthmus, the semester, and the snow.',
 'tel':'+16082086567','disp':'(608) 208-6567','brand':'Madison','keyword':'car shipping in madison',
 'localterms':['madison','interstate 90','interstate 94','interstate 39','beltline','us 151','verona road','east washington','john nolen','isthmus','lake mendota','lake monona','capitol','square','state street','campus','near east side','tenney-lapham','marquette','atwood','shorewood hills','nakoma','maple bluff','hilldale','monroe street','middleton','fitchburg','verona','sun prairie','waunakee','monona','mcfarland','stoughton','deforest','cottage grove','alliant energy center','east towne','software campus','insurer','biotech','university hospital','residents','state government','air national guard','lease','move-in','regent street','breese terrace','farmers','halloween','alternate-side','blizzard','plows','hail','milwaukee','rockford','dubuque','chicago','green bay','minneapolis','des moines','indianapolis','detroit','denver','orlando','florida','arizona'],
}, BODY, FAQ)
