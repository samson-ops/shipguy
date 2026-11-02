import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Lansing, Michigan','Car shipping in the capital, between the Capitol dome and the campus, on 96, 69, and 127',
 ['Car shipping in Lansing runs on three freeways that box the city and one that cuts through it. Ship Guy is a licensed auto transport broker with an office on Prudden Street, north of downtown.',
  'We book vetted carriers across Ingham, Eaton, and Clinton Counties, from Delta Township to Okemos and DeWitt. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 96 runs the south and west side between Grand Rapids and Detroit. Interstate 69 wraps the west and north on its way from Fort Wayne to Flint. Interstate 496 cuts through downtown to the east side. US 127 runs north and south along the campus.',
  'This page covers the freeways, the Capitol blocks, Old Town, REO Town, East Lansing, and the townships. It also covers the state workforce, the campus calendar, the plants, the insurers, football Saturdays, and the lanes.'],
 'Lansing at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers running between Detroit, Grand Rapids, and Chicago pass the city on 96 and 69 every day.',
  'Grand Rapids, Detroit, Ann Arbor, and Toledo are a same-day haul. Chicago is the same, and so is Fort Wayne. Indianapolis, Columbus, and Cleveland take a day. Nashville takes one to two, and Florida takes three to four.'],
 'Tell us the township and whether the address is near the campus. Downtown, Old Town, and the Eastside grid meet the truck at a lot. Okemos, Holt, Delta Township, DeWitt, and Grand Ledge usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 96, Interstate 69, Interstate 496, US 127, Saginaw Highway, and Grand River Avenue',
 prose(
  L('Lansing is ringed by freeways and crossed by one. A carrier reaches every township without touching a downtown street.'),
  P('Interstate 96 is the Grand Rapids-to-Detroit road, and it runs the south edge of the city past Holt. Interstate 69 comes up from Fort Wayne, shares the west side with 96, and leaves northeast toward Flint. The two share seven miles of pavement west of the city. Interstate 496 is the downtown spur. It runs from the 96 and 69 interchange east through the Capitol blocks to 127.'),
  P('US 127 is the north-south freeway along the East Lansing line. It runs from Jackson through the 496 interchange to Saint Johns and the north. Saginaw Highway is M-43, the old road west to Grand Ledge and Lansing Mall. Grand River Avenue is the old Detroit road. Michigan Avenue runs from the Capitol to the campus, and Cedar Street runs south.'),
  P('The carriers come off 127 at Lake Lansing Road and off 96 at Cedar Street. The lots at Eastwood Towne Center on 127 are the usual meeting spot. The Meridian Mall in Okemos and the Lansing Mall on Saginaw Highway work too. So does the Frandor center at 127 and Michigan Avenue. The ballpark lots on Cedar Street work outside game nights.'),
  P('Our office is on Prudden Street on the north side of downtown, by the Grand River.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Old Town, REO Town, the Eastside, Moores Park, East Lansing, Okemos, Holt, Delta Township, and DeWitt',
 prose(
  L('Lansing is a small downtown of state buildings, a ring of old neighborhoods, and wide townships beyond. The truck reaches most of it.'),
  P('Downtown is the Capitol, the state office blocks, and the Lansing Center on Michigan Avenue. A seventy-five-foot trailer does not stop on those streets. The driver meets you at the ballpark lots on Cedar Street or the Lansing Center garage approach. Old Town along Grand River Avenue is brick storefronts and narrow blocks. The handoff moves to the lots by the river.'),
  P('REO Town south of downtown is the old plant district on Washington Avenue, rebuilt with shops and apartments. The handoff moves to Cedar Street. The Eastside between downtown and the campus is a grid of bungalows on narrow streets. Moores Park and the Westside along Saginaw are the same. The driver meets you at Frandor or on Michigan Avenue.'),
  P('East Lansing is the campus and the Grand River Avenue strip. Student streets north of the avenue are parked solid. The handoff happens at a campus lot or the Meridian Mall. Okemos and Haslett in Meridian Township are wide subdivisions, and the curb works. Holt and Mason to the south are the same, with the county fairgrounds in Mason.'),
  P('Delta Township to the west holds the Lansing Mall, the insurance campus, and the assembly plant. The subdivisions off Saginaw and Saint Joe allow the curb. Grand Ledge sits beyond it on the river. DeWitt and Bath to the north are newer subdivisions on wide streets. Williamston, Charlotte, Eaton Rapids, and Saint Johns are the towns at the edges. All of them price the same as Lansing.'),
 )))

ROUTES=[("Grand Rapids, MI","I-96 · ~65 mi","Same day","$150–$240"),("Detroit, MI","I-96 · ~90 mi","Same day","$160–$260"),
 ("Ann Arbor, MI","I-96/US-23 · ~65 mi","Same day","$150–$240"),("Toledo, OH","US-127/US-23 · ~115 mi","Same day","$180–$290"),
 ("Fort Wayne, IN","I-69 · ~160 mi","Same day","$210–$320"),("Chicago, IL","I-69/I-94 · ~215 mi","Same day","$230–$350"),
 ("Indianapolis, IN","I-69 · ~250 mi","1 day","$260–$380"),("Columbus, OH","I-96/US-23 · ~255 mi","1 day","$260–$380"),
 ("Nashville, TN","I-69/I-65 · ~560 mi","1–2 days","$450–$650"),("Tampa, FL","I-69/I-75 · ~1,220 mi","3–4 days","$820–$1,170")]
BODY.append(rate_table('Lanes &amp; Costs','Lansing Car Shipping Lanes and Estimated Costs',
 'The lanes mid-Michigan cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Lansing for a running sedan on an open trailer. Figure 10 to 25 percent more for an SUV or a pickup, and more again for enclosed. The season and the trucks available on your dates decide the real number.',
 prose(
  P('Lansing prices between Grand Rapids and Detroit on every lane. Both carrier pools reach it in ninety minutes. The Chicago lane rides 69 to 94 and runs a same-day haul. The Fort Wayne and Indianapolis lanes ride 69 straight south. The Florida lane fills each fall with retirees and each winter with snowbirds.'),
  P('A move timed to the August move-in or a plant model changeover ships with the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State Workforce, the University, the Assembly Plants, the Insurers, and the Hospitals',
 prose(
  L('Lansing relocates state employees, faculty, plant engineers, and insurance staff. The state and the university move more people than anyone else.'),
  P('The state government is the largest employer in the city. Its departments transfer staff on start dates all year. Every four years a new administration moves an appointee class in January. The appointees come from across the state with a car to ship. A reimbursed move gets its paperwork from us.'),
  P('The university in East Lansing is one of the largest campuses in the country. It takes cars in each August and sends them home each May. Faculty and medical staff arrive on contract dates over the summer. A parent sets up the booking. An adult over eighteen signs at a campus lot or the Meridian Mall.'),
  P('The two assembly plants, south of downtown and in Delta Township, move engineers in on launch schedules. The suppliers along 96 in Delta Township and Holt do the same. The insurers headquartered here, downtown and in Delta Township, relocate staff on their own calendars. The two hospitals, one by the campus and one on Michigan Avenue, hire traveling nurses year round.'),
  P('Retirees leave for Florida and Arizona each fall and come back in spring. Families moving between Lansing and Detroit or Grand Rapids ship one car and drive the other. The Guard post in Grand Ledge rotates staff on orders, and Ship Guy has no tie to it. Orders timing is on the <a href="military-car-shipping.html">military</a> page, and the interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Football Saturdays, Move-In Week, the Ballpark, Silver Bells, the Snow, and the River',
 prose(
  L('Lansing runs on a campus calendar and a Big Ten football schedule. Winter closes the freeways a few days a year.'),
  P('Football Saturdays fill East Lansing from September through November. The campus lots close, Grand River Avenue crawls, and the 127 ramps back up for hours. A handoff near the campus moves to Friday or Sunday. Move-in week in late August clogs every street north of Grand River Avenue. The meeting spot moves to the Meridian Mall that week.'),
  P('The ballpark on Cedar Street fills its lots on game nights from April through September. The Breslin Center on campus fills the lots on basketball and concert nights. Silver Bells closes downtown for the Friday before Thanksgiving. The Capitol blocks close for the parade and the tree lighting. The county fair fills Mason for a week in late July.'),
  P('Winter brings fifty inches of snow. The 96 and 69 overlap west of the city ices before the plows reach it. The carriers wait in Grand Rapids or Detroit. The polar vortex week in early 2019 closed schools for days and kept the carriers in Detroit. A winter pickup can lose a day. We tell you before the driver does.'),
  P('The Grand River runs through downtown and Old Town, and it floods in a wet spring. The February 2018 flood put the river over the banks in Old Town and Urbandale. The low streets by the river closed for days. A pickup on the flat moves to higher ground until the water drops.'),
 )+chips(["Downtown","Capitol","Old Town","REO Town","Eastside","Westside","Moores Park","Groesbeck","Urbandale","Frandor","Lansing Township","Eastwood","East Lansing","Campus","Okemos","Haslett","Meridian Township","Williamston","Holt","Mason","Delhi Township","Delta Township","Lansing Mall","Waverly","Grand Ledge","DeWitt","Bath","Dimondale","Eaton Rapids","Charlotte","Saint Johns","Perry","Jackson"])
 +NOTE('Serving Lansing and all of Ingham, Eaton, and Clinton Counties, Capitol block or Okemos cul-de-sac. Tell us the township and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Lansing?',
 prose(
  L('Nearly every mid-Michigan car rides an open trailer, and that is what the lane table prices.'),
  P('An enclosed trailer keeps off the road salt and the winter grit on 96. The collectors around REO Town, where the first Lansing car company stood, book one. Executives relocating a new car to the insurers or the plants book one too.'),
  P('A commuter sedan or a student car rides open without a second thought. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a meeting spot at Eastwood or Frandor, and a signature at delivery. The start date or move-in day picks the week.'),
  P('Once you approve the number, we book a carrier already running 96 or 127. The meeting spot and the window are set the same day. At pickup the driver inspects the car with you. Every existing mark is noted on the Bill of Lading. You both sign. The delivery check runs against that same sheet.'),
 )+ULI([
  "Empty the cabin and the trunk of personal items",
  "Fuel at about a quarter tank",
  "Photograph each side and the odometer before the truck arrives",
  "Hand over one working key and name any fault",
  "Switch off an aftermarket alarm",
  "Downtown, in Old Town, or on the Eastside, meet the truck at a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages explain every step.'))))

BODY.append(sec('Why Ship Guy','Why Lansing Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 96, 69, and 127 through the capital. We know which campus streets a trailer cannot enter.'),
  P('Our FMCSA license and $75,000 bond sit on the federal register, open to anyone. Our office is on Prudden Street, north of downtown.'),
  P('The same coordinator handles the move from the first call to the last signature. The <a href="services.html">services</a> page lays out open, enclosed, and expedited transport.'),
 )))

BODY.append(office('Lansing','725 Prudden St #554','Lansing, MI 48906','+15176866771','(517) 686-6771','ET',
 '725+Prudden+St+%23554,+Lansing,+MI+48906','Visit Us','Find Ship Guy in Lansing',
 'Our office is on Prudden Street on the north side of downtown, by the Grand River.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3616.9795563350367!2d-84.5415489!3d42.7415818!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8822eb6181a6fe89%3A0xa55548e30d7f0113!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793287376859!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Lansing to Chicago or Florida?","Chicago runs two hundred thirty to three hundred fifty dollars for a sedan. That is about two hundred fifteen miles down 69 and 94. Tampa runs eight hundred twenty to eleven hundred seventy, about twelve hundred miles down 75. Detroit and Grand Rapids are ninety minutes away and the lowest lanes of all. Larger vehicles add 10 to 25 percent."),
 ("Can the carrier come to my street downtown or near the campus?","Usually not. The Capitol blocks and the arena streets do not fit a seventy-five-foot trailer. The student streets north of Grand River Avenue are parked solid. The driver meets you at the ballpark lots on Cedar Street, at Frandor, or at the Meridian Mall. Okemos, Holt, Delta Township, and DeWitt usually allow the curb."),
 ("Do you ship cars for state employees and university staff?","Yes, every week. The state transfers staff on start dates all year and moves an appointee class every fourth January. The university brings faculty and medical staff in on contract dates over the summer. A second car usually rides along on a trailer. The paperwork for a reimbursed move is ours to produce."),
 ("Can you deliver on the Michigan State move-in date?","Yes. Cars arrive on campus each August and leave each May. A parent arranges it, and someone over eighteen signs at a campus lot. Move-in week clogs every street north of Grand River Avenue, so the handoff happens at the Meridian Mall. The window moves with the date."),
 ("Can you ship a car to or from Okemos, Holt, or Grand Ledge?","Yes, and all three price the same as Lansing. Okemos and Haslett ride the same carriers off 127, and the curb works on most streets. Holt rides them off 96 at Cedar Street. Grand Ledge rides them off 96 at Saginaw Highway. Send the full address for a township road."),
 ("Does a football Saturday affect my pickup?","Yes, if the address is anywhere near East Lansing. The campus lots close, Grand River Avenue crawls, and the 127 ramps back up for hours. A handoff near the campus moves to Friday or Sunday. The rest of the city barely notices."),
 ("What happens if the Grand River floods on my pickup day?","A pickup on the river flat moves to higher ground until the water drops. The February 2018 flood closed the low streets in Old Town and Urbandale for days. You hear it from us first. The townships and the campus never notice."),
 ("Do you ship cars for the assembly plants and the insurers?","Yes. The two plants move engineers in on launch schedules, and the suppliers along 96 do the same. The insurers downtown and in Delta Township relocate staff on their own calendars. Executives often book an enclosed trailer for a new car. The paperwork for a reimbursed move comes from us."),
 ("Can you ship a car that does not run from Lansing?","Yes. A winch truck is assigned, and the loading time is in the quote from the start. The lots at Eastwood or the Lansing Mall give the driver level ground. Tell us whether the car rolls, steers, and brakes."),
 ("What do you need for a Lansing car shipping quote?","Pickup and delivery addresses, with the township. Year, make, model. Whether it runs. Open or enclosed. The week around the start date or move-in day. Five answers, and the Lansing number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Lansing FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Lansing?','Your lane gets a number in about two minutes on the form above. Name the township and the week, and a carrier already on 96 takes it.','+15176866771','(517) 686-6771','Get your free Lansing quote'))

build({
 'slug':'auto-transport-lansing-michigan',
 'title':'Car Shipping in Lansing, MI — Auto Transport | Ship Guy',
 'meta':'Car shipping in Lansing, MI, the capital between the Capitol dome and the campus on 96, 69, and 127. State and university relocations, Michigan State move-in timing, assembly plant and insurer moves, lot handoffs downtown and in Old Town, curbside pickups in Okemos, Holt, and Delta Township, football Saturdays, the snow, and the Grand River. Local office on Prudden Street. Free quote.',
 'h1':'Car Shipping in<br>Lansing, <span class="accent">Michigan</span>',
 'lede':'Open, enclosed, and expedited auto transport across the capital region, planned around 96, 127, the Capitol blocks, the campus calendar, and the winter.',
 'tel':'+15176866771','disp':'(517) 686-6771','brand':'Lansing','keyword':'car shipping in lansing',
 'localterms':['lansing','capitol','campus','interstate 96','interstate 69','interstate 496','us 127','prudden street','ingham','eaton','clinton','delta township','okemos','holt','dewitt','grand rapids','detroit','fort wayne','flint','downtown','old town','reo town','east lansing','townships','state workforce','assembly plants','insurers','football saturdays','ann arbor','toledo','chicago','indianapolis','columbus','cleveland','nashville','florida','saginaw highway','grand river avenue','jackson','saint johns','grand ledge','lansing mall','michigan avenue','cedar street','lake lansing road','eastwood towne center','meridian mall','frandor','ballpark','grand river','arena','lansing center','washington avenue','bungalows','moores park','westside','student streets','haslett','meridian township','mason','fairgrounds','subdivisions','saint joe','bath','williamston','charlotte','eaton rapids','retirees','snowbirds','move-in','model changeover','state employees','faculty','plant engineers','insurance','appointee','january','contract dates','launch schedules','suppliers','hospitals','traveling nurses','arizona','guard post','move-in week','silver bells','thanksgiving','parade','county fair','fifty inches','plows','february 2018','flood','road salt','bill of lading','fmcsa','eastwood','groesbeck','urbandale','breslin','lansing township','delhi township','waverly','dimondale','perry'],
}, BODY, FAQ)
