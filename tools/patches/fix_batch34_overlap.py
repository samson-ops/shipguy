D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')

fix('build_rockford_local.py', [
("Snow closes the tollway a few times a winter. The carriers wait at the truck stops by the interchange for the plows. A winter pickup can slip a day, and we call before it does. The river floods Machesney Park and the near east side after a big storm. A pickup on those streets moves up the hill for a day.",
 "A few times each winter the tollway shuts, and the carriers sit at the Cherry Valley truck stops until it reopens. That can push a pickup back a day, and you hear from us first. After a big storm the river covers the streets in Machesney Park and the near east side. Those pickups move uphill until the water drops."),
("Both addresses, with the side of the river or the town here. Year, make, and model. Whether it runs. Open or enclosed. The week you want it to go. That is a complete Rockford request, and the number comes back the same day.",
 "Where the car is and where it is going, with the Rockford side of the river or the suburb. The year, make, and model. Whether it starts. Open or enclosed. The week you have in mind. Five answers, and the Rockford quote is on its way the same day."),
("'Two minutes on the form above prices your lane. Send the side of the river and your dates, and a carrier already on 90 takes it.'",
 "'The form above takes two minutes and prices the lane. Add the side of the river and your dates, and the next carrier on 90 picks it up.'"),
("Most cars leave the Rock River valley on an open trailer, and the lane prices assume one.","Nine cars in ten leave the Rock River valley on an open trailer, and the table above is priced that way."),
("A closed trailer keeps a car out of the salt, the gravel, and the weather.","An enclosed trailer shuts out the road salt, the gravel, and the sky."),
("The Minneapolis lane runs the same way.'),\n  P('Florida and Texas follow the snowbird calendar, higher in the fall and lower in the spring.",
 "The Minneapolis lane runs the same way.'),\n  P('The Florida lane climbs in October and falls in April with the snowbirds."),
("The tolls are already inside those numbers. An SUV or pickup adds 10 to 25 percent.","Those numbers include the tolls. Add 10 to 25 percent for an SUV or a pickup."),
("One coordinator carries the move from the quote to the signed delivery sheet.","One coordinator owns the move from the first number to the last signature."),
])

fix('build_champaign_local.py', [
("Snow and ice close 57 and 74 a few times a winter. The carriers wait at the truck stops by the interchange for the plows. A winter pickup can slip a day, and the call comes first. A tornado warning stops the loading until it lifts, and the sirens sound a few times each spring. The wind alone never stops a pickup.",
 "Ice shuts 57 and 74 a few times each winter, and the carriers hold at the interchange truck stops until the salt trucks pass. That can cost a pickup a day, and you hear about it before it happens. Under a tornado warning the driver stops loading until it expires. Sirens sound a few times every spring. Wind by itself never cancels a pickup."),
("A lot off the interstate works for a handoff. Send the full address for a new subdivision.","Any lot off the interstate works for the handoff. New subdivisions need the full address, since the maps lag."),
("Most cars leave Champaign County on an open trailer, and the lane prices assume one.","Open trailers carry most of the cars that leave Champaign County, and the lane table is priced for one."),
("A closed trailer keeps a car away from the salt, the gravel, and the weather. Parents","An enclosed trailer keeps a car out of the salt, the gravel, and the rain. Parents"),
("The arena lots or the mall lot give the driver level pavement. Tell us whether the car rolls, steers, and brakes.","The arena lots or the mall lot give the driver flat pavement to winch on. Say whether it rolls, whether it steers, and whether the brakes hold."),
])

fix('build_waukegan_local.py', [
("The tolls are inside those numbers. An SUV or pickup adds 10 to 25 percent.","Tolls are included. Figure 10 to 25 percent more for an SUV or a pickup."),
("The Minneapolis lane runs the same way.'),\n  P('Florida and Texas follow the snowbird calendar, higher in the fall and lower in the spring.",
 "The Minneapolis lane runs the same way.'),\n  P('Florida and Texas rise with the snowbirds each fall and ease off in the spring."),
("Most cars leave Lake County on an open trailer, and the lane prices assume one.","Open trailers move most Lake County cars, and the lane table is priced for one."),
("A closed trailer keeps a car away from the salt, the lake grit, and the weather.","An enclosed trailer keeps the salt, the lake grit, and the weather off."),
("The two addresses, with the side of Green Bay Road or the town here. Year, make, and model. Whether it drives. Open or enclosed. The week around the report date or the closing. That is a complete Waukegan request, and the number comes back the same day.",
 "Pickup and delivery addresses, with the side of Green Bay Road or the suburb. Year, make, model. Whether it drives. Open or enclosed. The week around the report date or the closing. With those five, the Waukegan quote comes back within the day."),
("The coordinator who prices the move follows it until the car is signed for.","The coordinator who prices the move is the one on the phone until the car is signed for."),
])
