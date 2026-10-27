D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')

fix('build_portlandme_local.py', [
("Portland runs on a ten-week summer, a fall of cruise ships, and a winter that comes in off the water.","Portland runs on a ten-week summer, a fall of cruise ships, and a winter off the water."),
("A commuter car or a work truck rides open and arrives in the shape it left. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages weigh the two.",
 "The commuter car and the lobster truck go open and come off the trailer as they went on. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages weigh the two."),
("One coordinator takes the move from the quote to the signed delivery sheet.","The coordinator who quotes the move is the one who closes it."),
("Snow runs sixty inches a year, and the Turnpike closes a few times a season. A winter pickup can lose a day or two, and you hear before it does.",
 "Sixty inches of snow falls in a normal winter, and the Turnpike shuts a few times a season. A pickup in a storm week can lose a day or two, and we call before it does."),
("It brings in nurses on contracts all year and residents each June. Physicians arrive with a closing date and a second car. The second hospital on the west side does the same.",
 "Nurses arrive on contracts all year and residents every June. Physicians come with a closing date and a second car. The second hospital on the west side hires the same way."),
("The lots on Marginal Way or the mall lot in South Portland give the driver level ground. Tell us whether the car rolls, steers, and brakes.",
 "The lots on Marginal Way or the mall lot in South Portland give the driver room to winch. Say whether it rolls, whether it steers, and whether the brakes hold."),
("Boston runs one hundred seventy to two hundred eighty dollars for a sedan. That is about one hundred ten miles down 95.",
 "A sedan to Boston runs one hundred seventy to two hundred eighty dollars, for about one hundred ten miles down 95."),
("*2026 estimates priced from Portland, Maine, for a running sedan on an open trailer. SUVs and pickups add 10 to 25 percent, and enclosed adds more. Turnpike tolls are included.",
 "*2026 estimates priced from Portland, Maine, open trailer, sedan that runs. SUVs and pickups land 10 to 25 percent higher, enclosed higher again. Turnpike tolls are inside the number."),
("Most cars leave Cumberland County on an open trailer, and the lane prices are built around one.","Open trailers carry most of the cars that leave Cumberland County, and the table above assumes one."),
("An enclosed trailer keeps the salt, the slush, and the sea air off a car.","An enclosed trailer keeps a car out of the salt, the slush, and the sea air."),
])

fix('build_lewiston_local.py', [
("The two addresses, with the side of the river or the town here. Year, make, and model. Whether it runs. Open or enclosed. A date range rather than one day, since the trucks come north on a run. That is a complete Lewiston request, and the number comes back the same day.",
 "Where the car is and where it goes, with the side of the river here. What it is, year through model. Whether it starts. Open or enclosed. A range of dates rather than one, since the trucks come north on a run. Five answers, and the Lewiston number is back within the day."),
("Portland is forty minutes and prices the lowest of all. An SUV or pickup adds 10 to 25 percent.",
 "Portland is forty minutes away and the least expensive lane. Count on 10 to 25 percent more for an SUV or a pickup."),
("Together they bring in nurses on contracts all year and residents each June. Physicians arrive with a closing date and a second car. We supply the paperwork a reimbursed move needs.",
 "Between them they hire nurses on contracts all year and take residents each June. Physicians come with a closing date and a second car. The paperwork for a reimbursed move comes from us."),
("Snow runs seventy inches a year, and the Turnpike closes a few times a season. A winter pickup can lose a day or two, and you hear before it does. The river floods the low streets in a wet April, as it did in 1987.",
 "Seventy inches of snow is a normal winter here, and the Turnpike shuts a few times a season. A pickup in a storm week can slip a day or two, with a call from us first. In a wet April the river climbs into the low streets, as it did in 1987."),
("The coordinator who quotes the move is the one who sees it through.","The person who quotes the move is the person on the phone until it is delivered."),
("A daily driver or a plant truck rides open and arrives none the worse. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages explain the trade-off.",
 "A daily driver or a plant truck goes open and comes off the trailer fine. The <a href=\"open-car-transport.html\">open</a> and <a href=\"enclosed-auto-transport.html\">enclosed</a> pages explain the trade-off."),
("The <a href=\"state-to-state-car-shipping.html\">state-to-state</a> page covers the interstate side. Ship Guy is a private broker with no military connection, and the <a href=\"military-car-shipping.html\">military</a> page covers the Guard timing.",
 "The interstate side is on the <a href=\"state-to-state-car-shipping.html\">state-to-state</a> page. Ship Guy is a private broker with no military connection, and Guard timing is on the <a href=\"military-car-shipping.html\">military</a> page."),
("'Two minutes on the form above prices your lane. Send the side of the river and a date range. The next carrier up the Turnpike takes it.'",
 "'The form above prices the lane in two minutes. Give us the side of the river and a range of dates, and the next carrier up the Turnpike takes it.'"),
])

fix('build_bangor_local.py', [
("The mall on Stillwater, the arena by Bass Park, and the truck stop in Hermon have the usual meeting lots.","The mall on Stillwater, the arena at Bass Park, and the Hermon truck stop have the usual meeting lots."),
("Bangor runs on a waterfront concert season, a fair at Bass Park, and a winter from November into April.","Bangor runs on a waterfront concert season, a fair at Bass Park, and a five-month winter."),
("  \"Leave the fuel at about a quarter tank\",\n  \"Photograph every side of the car and the odometer before the truck comes\",\n  \"Give the driver one working key and name any fault\",",
 "  \"Fuel down to a quarter tank\",\n  \"Pictures of every side and the odometer before the truck comes\",\n  \"One working key for the driver, and a word about any fault\","),
("The coordinator who prices the move keeps it until the delivery sheet is signed.","The coordinator who prices the move stays with it until the car is signed for."),
("The wing rotates airmen on orders, and the orders cover one car. The second one comes with us. Ship Guy is a private broker with no military connection, and the <a href=\"military-car-shipping.html\">military</a> page covers the timing.",
 "The wing rotates airmen on orders, and the orders pay for one car. We move the other. Ship Guy is a private broker with no military connection, and the timing is on the <a href=\"military-car-shipping.html\">military</a> page."),
("The driver goes over the car with you and records its condition on a Bill of Lading. Both of you sign, and the sheet is checked again at delivery.",
 "You and the driver go around the car together, and the Bill of Lading records its condition. Two signatures close it, and the same sheet comes out at delivery."),
("It brings in nurses on contracts all year and residents each June. Physicians arrive with a closing date and a second car. The second hospital on Broadway and the health centers in the small towns recruit the same way.",
 "Nurses come on contracts all year and residents every June. Physicians arrive with a closing date and a second car. The second hospital on Broadway and the health centers in the small towns recruit the same way."),
("Ship Guy holds FMCSA brokerage authority and a $75,000 surety bond, and the federal register shows both. Our office is on Olive Street in Bangor.",
 "Ship Guy is an FMCSA-licensed broker backed by a $75,000 surety bond. Both appear in the federal register. Our office is on Olive Street in Bangor."),
("That is a complete Bangor request, and the number comes back the same day.","Those five answers are the whole request, and the Bangor number is back within the day."),
("Yes. A winch truck is sent, and the quote carries the loading time from the first number. The mall lot on Stillwater or the truck stop in Hermon gives the driver level ground.",
 "Yes. The carrier comes with a winch, and the loading time is priced in from the first quote. The mall lot on Stillwater or the Hermon truck stop gives the driver room to work."),
])
