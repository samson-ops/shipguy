import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Colorado Springs, Colorado','Car shipping at the foot of Pikes Peak, in one of the biggest military towns in the country',
 ['Car shipping in Colorado Springs starts on Interstate 25, where the Front Range carriers pass every day. Ship Guy is a licensed auto transport broker with an office on East Pikes Peak Avenue downtown.',
  'We book vetted carriers across the Pikes Peak region, from Monument to Fountain and out to Falcon. We do not own the trucks.',
  'Interstate 25 runs north and south through the middle of the city. US 24 crosses it, east to Falcon and west up Ute Pass. Powers Boulevard carries the east side, and Academy Boulevard carries the middle. Monument Hill sits between the city and Denver.',
  'This page covers the interstate, the pass, downtown, the Old North End, and the new east side. It also covers the five installations, the Academy calendar, the hail, the fires, the colleges, and the lanes.'],
 'Colorado Springs at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 25 brings the Denver and Albuquerque carriers through the city all day.',
  'Denver and Pueblo are same-day lanes. Aurora is the same day too. Albuquerque, Wichita, and Salt Lake City take a day. Dallas, Phoenix, and El Paso take one to two.'],
 'Tell us the neighborhood and the gate. The Old North End, Manitou, and the Broadmoor need a meeting spot. Briargate, Stetson Hills, and the Powers corridor usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 25, US 24, Powers Boulevard, Academy Boulevard, and Monument Hill',
 prose(
  L('Colorado Springs has one interstate and one hill, and the carriers plan around both.'),
  P('Interstate 25 runs the length of the city from Monument to Fountain. The stretch through downtown was rebuilt with wider lanes. The ramps at Bijou and Cimarron are the way in. North of the city, the Gap between Monument and Castle Rock added a third lane in each direction. Monument Hill climbs past seven thousand feet, and it closes in a blizzard.'),
  P('US 24 is Platte Avenue through the east side and Cimarron Street through the west. East, it runs to Falcon and the plains. West, it climbs Ute Pass through Manitou to Woodland Park. The pass is steep and busy, and a loaded trailer takes it slowly.'),
  P('Powers Boulevard is the east-side freeway, from the Air Force Academy down to Fountain. Academy Boulevard runs the middle of the city past the mall. Nevada Avenue and Union Boulevard carry the north and south. Woodmen Road and Austin Bluffs Parkway cross the north side. Highway 115 runs south past Fort Carson toward Cañon City.'),
  P('The carriers come off 25 at Garden of the Gods Road, Fillmore, Cimarron, and South Academy. The lots along Powers, at the mall, and off Garden of the Gods Road are the meeting spots. No road in the region charges a toll, apart from the express lanes in the Gap.'),
  P('Our office sits on East Pikes Peak Avenue downtown, a few blocks east of the Cimarron ramps.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Old North End, the Westside, the Broadmoor, and the East Side',
 prose(
  L('Colorado Springs is a Victorian core, a ring of postwar grids, and a new city growing east. Each parks differently.'),
  P('Downtown has wide streets laid out for a resort town. A trailer can stop on Pikes Peak Avenue or Cascade. The Old North End has mansions on narrow, tree-lined streets. The driver meets you on Nevada or Cascade. Shooks Run and Patty Jewett are bungalow blocks where the handoff happens on a wide avenue.'),
  P('The Westside and Old Colorado City have narrow grids and low trees. The driver meets you on Colorado Avenue. Manitou Springs climbs the canyon on streets a truck cannot enter. The handoff for Manitou happens at a lot on US 24. The Broadmoor and Cheyenne Cañon have winding estate roads. The driver stays on Lake Avenue or Highway 115.'),
  P('Rockrimmon, Mountain Shadows, and Peregrine climb the foothills on curving streets. The driver meets you on Centennial or Garden of the Gods Road. Briargate, Pine Creek, and Northgate are newer subdivisions with wide streets, and the truck usually reaches the curb. Monument and Palmer Lake sit on the hill with the same answer.'),
  P('The east side along Powers is the newest part of the city. Stetson Hills, Wolf Ranch, Cordera, and Banning Lewis Ranch have wide streets and alleys. Falcon and Peyton sit on the plains beyond Powers with room everywhere. Security, Widefield, and Fountain are the Fort Carson suburbs, and the curb works on most streets.'),
 )))

ROUTES=[("Denver, CO","I-25 · ~70 mi","Same day","$150–$240"),("Pueblo, CO","I-25 · ~45 mi","Same day","$130–$210"),
 ("Albuquerque, NM","I-25 · ~380 mi","1 day","$350–$500"),("Wichita, KS","US-24/US-50/I-70 · ~520 mi","1 day","$420–$600"),
 ("Salt Lake City, UT","I-25/I-70 · ~590 mi","1–2 days","$450–$650"),("Kansas City, MO","I-25/I-70 · ~670 mi","1–2 days","$490–$700"),
 ("El Paso, TX","I-25 · ~640 mi","1–2 days","$480–$690"),("Dallas, TX","I-25/US-287 · ~720 mi","2 days","$520–$760"),
 ("Phoenix, AZ","I-25/I-40 · ~740 mi","2 days","$450–$650"),("Los Angeles, CA","I-25/I-70/I-15 · ~1,080 mi","3 days","$750–$1,050")]
BODY.append(rate_table('Lanes &amp; Costs','Colorado Springs Car Shipping Lanes and Estimated Costs',
 'The lanes that leave the Pikes Peak region most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from Colorado Springs. An SUV or pickup adds roughly 10 to 25 percent, and enclosed adds more. The report dates, the hail, and the carriers free on your dates set the final figure.',
 prose(
  P('Colorado Springs prices like Denver, because the same 25 carriers reach both an hour apart. The military lanes to Texas, Kansas, and the Carolinas run full every summer. El Paso and Albuquerque ride 25 straight south.'),
  P('Phoenix runs cheap in spring, when the snowbird trucks come back empty. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','Fort Carson, Peterson, Schriever, the Academy, and the Hospitals',
 prose(
  L('Colorado Springs relocates soldiers, guardians, cadets, and nurses, and the orders set the calendar.'),
  P('Fort Carson rotates brigades and families all year, with the heaviest moves from May through August. Peterson and Schriever host Space Force units on their own cycles. Cheyenne Mountain adds more. Orders cover one car, and the second one comes with us.'),
  P('The Air Force Academy runs on the cadet calendar. Graduation fills the north side in late May, and the new class arrives in late June. Every installation has a gate, and the handoff happens outside it. The lots along Powers and off Highway 115 are the usual spots.'),
  P('Ship Guy is a private broker with no connection to any installation. The <a href="military-car-shipping.html">military</a> page covers the timing around a report date.'),
  P('The defense contractors along Powers and in the north hire engineers on contract cycles. The two hospital systems bring in nurses and residents every summer. The college downtown and the university on Austin Bluffs bring cars in each August. An adult signs for a student car, and the handoff happens at a campus lot.'),
  P('The nonprofits headquartered in the north and the Olympic training center downtown relocate staff and athletes all year. We supply the paperwork a reimbursed move needs. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Hail, Monument Hill, the Fires, and Graduation Week',
 prose(
  L('Colorado Springs sits where the plains weather meets the mountain weather. The carriers plan around both.'),
  P('Hail falls from May through August, and the east side takes the worst of it. The 2016 storm dented cars from downtown to Powers in twenty minutes. We shift the window when a storm is forecast. A collector car rides enclosed.'),
  P('Snow closes Monument Hill a few times each winter. The Denver carriers wait at the truck stops in Monument. The chinook winds knock trailers around on Interstate 25 in winter. A winter pickup can slide a day. Spring blizzards shut the plains east of Falcon for a day.'),
  P('Wildfire is the regional fear. The 2012 fire burned into Mountain Shadows, and the 2013 fire burned Black Forest. Smoke and closures slow the foothills from June through October. When a fire is close, a foothills pickup moves to a lot on Garden of the Gods Road.'),
  P('Graduation week fills every hotel in late May. The hill climb closes the Pikes Peak Highway for a weekend in June. The balloon festival fills Memorial Park on Labor Day weekend. The rodeo fills July. We move a pickup in those blocks to another day.'),
 )+chips(["Downtown","Old North End","Shooks Run","Patty Jewett","Westside","Old Colorado City","Manitou Springs","Broadmoor","Cheyenne Cañon","Ivywild","Skyway","Rockrimmon","Mountain Shadows","Peregrine","Pleasant Valley","Briargate","Pine Creek","Northgate","Flying Horse","Wolf Ranch","Cordera","Stetson Hills","Powers Corridor","Banning Lewis Ranch","Cimarron Hills","Security","Widefield","Fountain","Falcon","Peyton","Black Forest","Monument","Palmer Lake","Woodland Park"])
 +NOTE('Serving Colorado Springs and the whole Pikes Peak region, both sides of the pass. Tell us the neighborhood, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Colorado Springs?',
 prose(
  L('Open is how the region ships, and the PCS lanes are priced for it.'),
  P('An enclosed trailer keeps the hail, the road treatment, and attention off a car. Soldiers and guardians with a restored car book enclosed for a long move. The Broadmoor garages book them for the car shows.'),
  P('A commuter car or a work truck rides open without trouble. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on Powers or outside the gate, and a delivery. The report date sets the week.'),
  P('Approve the price, and a carrier already on 25 takes the booking. We name the spot and the window the same day. The driver looks the car over with you and records its condition on a Bill of Lading. Both sign it, and that sheet comes back out at delivery.'),
 )+ULI([
  "Empty the car of personal items",
  "Leave about a quarter tank of fuel",
  "Photograph the car before pickup, especially after hail",
  "Hand over a working key and mention any mechanical issue",
  "Disable any aftermarket alarm",
  "On any installation, plan to meet the truck outside the gate",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages walk through the rest.'))))

BODY.append(sec('Why Ship Guy','Why Colorado Springs Drivers Choose Ship Guy',
 prose(
  L('We work 25 every day and plan around the gates, the hail, and Monument Hill.'),
  P('Ship Guy holds active brokerage authority with the FMCSA, and a $75,000 surety bond stands behind it. Both can be checked in the federal register. Our office is on East Pikes Peak Avenue downtown.'),
  P('One coordinator stays with your move from the first call to the last signature. You can book open, enclosed, or expedited transport, and the <a href="services.html">services</a> page describes each.'),
 ), alt=True))

BODY.append(office('Colorado Springs','559 E Pikes Peak Ave Ste 487','Colorado Springs, CO 80903','+17198004804','(719) 800-4804','MT',
 '559+E+Pikes+Peak+Ave+Ste+487,+Colorado+Springs,+CO+80903','Visit Us','Find Ship Guy in Colorado Springs',
 'Our office is on East Pikes Peak Avenue downtown, a few blocks east of Interstate 25.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4779.3124960604755!2d-104.81362320000001!3d38.833158999999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87134557787abab1%3A0x79bba5223800e89b!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792161741393!5m2!1sen!2sus'))

FAQ=[
 ("Do you handle a PCS move to Fort Carson, Peterson, or Schriever?","Yes, every week of the year, with the peak from May through August. Orders cover one car, and the second one comes with us. The gate stops the truck, so we meet you at a lot along Powers or off Highway 115. We schedule around your report date. Ship Guy is a private broker with no connection to any installation."),
 ("How much does it cost to ship a car from Colorado Springs to Texas?","Dallas runs five hundred twenty to seven hundred sixty dollars for a sedan. That is about seven hundred twenty miles down 25 and US 287. El Paso runs four hundred eighty to six hundred ninety, about six hundred forty miles straight down 25. SUVs and pickups add 10 to 25 percent."),
 ("Can you ship a car for an Air Force Academy cadet or graduate?","Yes, on the cadet calendar. Graduates ship cars to their first assignment in late May and June. Cadets can keep a car on campus from their junior year, and many ship one in each August. The handoff happens outside the north or south gate at a lot off Interstate 25."),
 ("What if hail is forecast for my pickup day?","We move the window. Hail falls from May through August, and the east side takes the worst of it. The pickup shifts to an early hour or the next clear day. Collector cars ride under a roof. We call as soon as the forecast changes."),
 ("Can the carrier come into the Old North End, Manitou, or the Broadmoor?","Usually not. The Old North End streets are narrow under old trees. Manitou climbs a canyon, and the Broadmoor roads wind. The driver meets you on Nevada, at a lot on US 24, or on Lake Avenue. Briargate, Stetson Hills, and the Powers corridor usually allow the curb."),
 ("What happens if Monument Hill closes on my pickup day?","The Denver carriers wait at the truck stops in Monument until the plows finish. The hill closes a few times each winter for a few hours or a day. A pickup headed south on 25 is not affected. A winter pickup can slide a day, and we call before it does."),
 ("Can you ship a car for a Colorado College or UCCS student?","Yes. Cars arrive each August and leave each May, and both windows book up early. The college downtown has lots along Cascade, and the university has lots off Austin Bluffs Parkway. A parent or another adult signs at pickup."),
 ("Do you pick up in Woodland Park or over Ute Pass?","Yes, with an extra day. The pass is steep, and a loaded trailer takes it slowly. The driver meets you at a lot in Woodland Park or at the bottom of the pass. In winter, a snowstorm on the pass can add a day."),
 ("Can you ship a car that does not run from Colorado Springs?","Yes. The carrier arrives with a winch, and the quote already covers the slower loading. Pick a flat, open spot, which usually means a lot along Powers or Academy. Let us know if it rolls, steers, and brakes."),
 ("What do you need for a Colorado Springs car shipping quote?","The pickup and delivery addresses, plus the gate or the neighborhood on this end. Year, make, model. Whether it runs. Open or enclosed. A date range built around the report date. That is a complete Colorado Springs request."),
]
BODY.append(faq_section(FAQ,'Colorado Springs FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Colorado Springs?','The form above prices your lane in about two minutes. Tell us the gate or the neighborhood and your dates. A carrier already on 25 handles the rest.','+17198004804','(719) 800-4804','Get your free Colorado Springs quote'))

build({
 'slug':'auto-transport-colorado-springs-colorado',
 'title':'Car Shipping in Colorado Springs, CO — Auto Transport | Ship Guy',
 'meta':'Car shipping in Colorado Springs, CO at the foot of Pikes Peak. Fort Carson, Peterson, Schriever, and Academy second cars, gate handoffs along Powers, Old North End and Manitou meeting spots, east-side curbside, hail and Monument Hill planning, college move-in. Local office on East Pikes Peak Avenue downtown. Free quote.',
 'h1':'Car Shipping in<br>Colorado Springs, <span class="accent">Colorado</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Pikes Peak region, planned around 25, the gates, the hail, and Monument Hill.',
 'tel':'+17198004804','disp':'(719) 800-4804','brand':'Colorado Springs','keyword':'car shipping in colorado springs',
 'localterms':['colorado springs','pikes peak','interstate 25','us 24','platte avenue','cimarron','ute pass','powers boulevard','academy boulevard','nevada avenue','union boulevard','woodmen road','austin bluffs','highway 115','monument hill','the gap','garden of the gods road','fillmore','downtown','old north end','shooks run','patty jewett','westside','old colorado city','colorado avenue','manitou','broadmoor','cheyenne cañon','lake avenue','rockrimmon','mountain shadows','peregrine','briargate','pine creek','northgate','stetson hills','wolf ranch','cordera','banning lewis ranch','falcon','peyton','security','widefield','fountain','monument','palmer lake','woodland park','fort carson','peterson','schriever','cheyenne mountain','air force academy','cadet','graduation','gate','orders','report date','defense contractors','hospital','nurses','residents','college','university','olympic','nonprofits','hail','2016','chinook','blizzards','wildfire','2012','2013','black forest','hill climb','balloon','rodeo','denver','pueblo','aurora','albuquerque','wichita','salt lake city','kansas city','el paso','dallas','phoenix','los angeles','texas','kansas','carolinas'],
}, BODY, FAQ)
