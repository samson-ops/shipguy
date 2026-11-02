D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for item in pairs:
        old,new=item[0],item[1]; k=item[2] if len(item)>2 else 1
        c=s.count(old); assert c==k, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')

fix('build_lansing_local.py', [
("Car shipping in Lansing runs on the three freeways that box the city and the one that cuts through it.","Car shipping in Lansing runs on three freeways that box the city and one that cuts through it."),
("We book vetted carriers across Ingham, Eaton, and Clinton Counties, from Delta Township to Okemos and Holt to DeWitt.","We book vetted carriers across Ingham, Eaton, and Clinton Counties, from Delta Township to Okemos and DeWitt."),
("Interstate 496 cuts through downtown to the east side, and US 127 runs north and south along the campus.","Interstate 496 cuts through downtown to the east side. US 127 runs north and south along the campus."),
("It also covers the state workforce, the campus calendar, the assembly plants, the insurers, football Saturdays, and the lanes.","It also covers the state workforce, the campus calendar, the plants, the insurers, football Saturdays, and the lanes."),
("Interstate 496 is the downtown spur, from the 96 and 69 interchange east through the Capitol blocks to US 127.","Interstate 496 is the downtown spur. It runs from the 96 and 69 interchange east through the Capitol blocks to 127."),
("Grand River Avenue is the old Detroit road, Michigan Avenue runs from the Capitol to the campus, and Cedar Street is the main street south.","Grand River Avenue is the old Detroit road. Michigan Avenue runs from the Capitol to the campus, and Cedar Street runs south."),
("The Meridian Mall in Okemos, the Lansing Mall on Saginaw Highway, and the Frandor center at 127 and Michigan Avenue all work.","The Meridian Mall in Okemos and the Lansing Mall on Saginaw Highway work too. So does the Frandor center at 127 and Michigan Avenue."),
("Our office is on Prudden Street on the north side of downtown, by the Grand River and minutes from 127.","Our office is on Prudden Street on the north side of downtown, by the Grand River.",2),
("Student streets north of the avenue are parked solid, and the handoff happens at a campus lot or the Meridian Mall.","Student streets north of the avenue are parked solid. The handoff happens at a campus lot or the Meridian Mall."),
("Lansing prices between Grand Rapids and Detroit on every lane, because both carrier pools reach it in ninety minutes.","Lansing prices between Grand Rapids and Detroit on every lane. Both carrier pools reach it in ninety minutes."),
("The state government is the largest employer in the city, and its departments transfer staff on start dates all year.","The state government is the largest employer in the city. Its departments transfer staff on start dates all year."),
("A parent sets up the booking, and an adult over eighteen signs at a campus lot or the Meridian Mall.","A parent sets up the booking. An adult over eighteen signs at a campus lot or the Meridian Mall."),
("The two assembly plants, one by the river south of downtown and one in Delta Township, move engineers in on launch schedules.","The two assembly plants, one south of downtown and one in Delta Township, move engineers in on launch schedules."),
("The 96 and 69 overlap west of the city ices before the plows reach it, and the carriers wait in Grand Rapids or Detroit.","The 96 and 69 overlap west of the city ices before the plows reach it. The carriers wait in Grand Rapids or Detroit."),
("At pickup the driver walks the car with you and records every existing mark on the Bill of Lading.","At pickup the driver walks the car with you. Every existing mark goes on the Bill of Lading."),
])

fix('build_vancouver_local.py', [
("Car shipping in Vancouver depends on two bridges and the Portland carrier pool on the far side of them.","Car shipping in Vancouver depends on two bridges and the Portland carrier pool across them."),
("Interstate 5 crosses the Columbia on the Interstate Bridge and runs north through Hazel Dell and Salmon Creek to Seattle.","Interstate 5 crosses the Columbia on the Interstate Bridge. It runs north through Hazel Dell and Salmon Creek to Seattle."),
("This page covers the bridges, the lift spans, 500 and 503, downtown, the waterfront, Hazel Dell, Orchards, Camas, and the north county.","This page covers the bridges, 500 and 503, downtown, the waterfront, Hazel Dell, Orchards, Camas, and the north county."),
("Interstate 5 crosses on the Interstate Bridge, a pair of lift spans from 1917 and 1958 with no shoulders.","Interstate 5 crosses on the Interstate Bridge, a pair of lift spans from 1917 and 1958. Neither has a shoulder."),
("Our office is on Broadway in downtown Vancouver, a few blocks from Esther Short Park and minutes from the bridges.","Our office is on Broadway in downtown Vancouver, a few blocks from Esther Short Park.",2),
("The Boise and Salt Lake lanes ride 84 up the Gorge, and the Gorge closes a few days each winter.","The Boise and Salt Lake lanes ride 84 up the Gorge. The Gorge closes a few days each winter."),
("Transfers to the chip plants and the sportswear campus west of Portland land in Vancouver on start dates all year.","Transfers to the chip plants and the sportswear campus west of Portland land here on start dates all year.",2),
("The software firms downtown and the laser and wafer makers on the east side move engineers in on offer dates.","The software firms downtown and the laser and wafer makers on the east side move engineers in on offer dates."[:0]+"The software firms downtown and the wafer makers on the east side move engineers in on offer dates."),
("PCS moves to the bases near Tacoma ride the same 5 lane, and Ship Guy has no military tie.","PCS moves to the bases near Tacoma ride the same 5 lane. Ship Guy has no military tie."),
("The amphitheater beside it runs concerts from May through September, and the 179th Street exit backs up on show nights.","The amphitheater beside it runs concerts from May through September. The 179th Street exit backs up on show nights."),
("The January 2024 ice storm shut the county for most of a week and closed 84 through the Gorge for days.","The January 2024 ice storm shut the county for most of a week. It closed 84 through the Gorge for days."),
("The driver walks the car with you at pickup and records every existing mark on the Bill of Lading.","The driver walks the car with you at pickup. Every existing mark goes on the Bill of Lading."),
("Tell us the release date and the location, and we book the ocean leg separately if you need it.","Tell us the release date and the location. The ocean leg is booked separately if you need it."),
("Camas rides the same carriers east on 14, and the older hill blocks meet the truck on the flats.","Camas rides the same carriers east on 14. The older hill blocks meet the truck on the flats."),
("The Gorge east wind coats every road east of 205 in an hour, and the January 2024 storm shut the county for most of a week.","The Gorge east wind coats every road east of 205 in an hour. The January 2024 storm shut the county for most of a week."),
])

fix('build_chesapeake_local.py', [
("We book vetted carriers across the city, from Western Branch and Deep Creek to Great Bridge, Hickory, and South Norfolk.","We book vetted carriers across the city, from Western Branch and Deep Creek to Great Bridge and Hickory."),
("This page covers 64, 464, 664, the High Rise, the Expressway, Greenbrier, Great Bridge, Western Branch, Deep Creek, and Hickory.","This page covers 64, 464, 664, the High Rise, the Expressway, Greenbrier, Great Bridge, Western Branch, and Hickory."),
("It also covers the Navy families, the headquarters on Battlefield, the hospital, the drawbridges, the Outer Banks traffic, the storms, and the lanes.","It also covers the Navy families, the headquarters, the hospital, the drawbridges, the beach traffic, the storms, and the lanes."),
("Interstate 64 enters at Bowers Hill on the west and crosses the Southern Branch of the Elizabeth River on the High Rise Bridge.","Interstate 64 enters at Bowers Hill on the west. It crosses the Southern Branch of the Elizabeth River on the High Rise Bridge."),
("Interstate 464 leaves 64 at Great Bridge Boulevard and runs north past South Norfolk to downtown Norfolk and the tunnel.","Interstate 464 leaves 64 at Great Bridge Boulevard. It runs north past South Norfolk to downtown Norfolk and the tunnel."),
("Interstate 664 runs the west edge from Bowers Hill through Western Branch to the Monitor-Merrimac tunnel and the Peninsula.","Interstate 664 runs the west edge from Bowers Hill through Western Branch to the Monitor-Merrimac tunnel."),
("The Chesapeake Expressway is Route 168, a toll road south from Great Bridge to the North Carolina line and the Outer Banks.","The Chesapeake Expressway is Route 168, a toll road south from Great Bridge to the state line and the Outer Banks."),
("Battlefield Boulevard is the spine, from South Norfolk through Greenbrier and Great Bridge to Hickory and the state line.","Battlefield Boulevard is the spine. It runs from South Norfolk through Greenbrier and Great Bridge to Hickory and the state line."),
("Greenbrier at the 64 interchange is the mall, the office parks, and the hotel strip, with subdivisions behind them.","Greenbrier at the 64 interchange is the mall, the office parks, and the hotel strip. The subdivisions sit behind them."),
("Deep Creek along Route 17 sits on the Dismal Swamp Canal, with the lock and the old village by the drawbridge.","Deep Creek along Route 17 sits on the Dismal Swamp Canal. The lock and the old village sit by the drawbridge."),
("Indian River along the Virginia Beach line is tight postwar streets off Indian River Road, and the handoff moves to the shopping centers.","Indian River along the Virginia Beach line is tight postwar streets off Indian River Road. The handoff moves to the shopping centers."),
("Sailors from the Norfolk piers, Oceana, Little Creek, and the Portsmouth shipyard buy in Great Bridge and Hickory for the schools.","Sailors from the Norfolk piers, Oceana, Little Creek, and the shipyard buy in Great Bridge and Hickory for the schools."),
("At pickup the driver walks the car with you and writes every existing mark on the Bill of Lading.","At pickup the driver walks the car with you. Every existing mark goes on the Bill of Lading."),
("A carrier that takes 168 to Hickory or the state line pays the toll, and it rides inside the quote.","A carrier that takes 168 to Hickory or the state line pays the toll. It rides inside the quote."),
])

fix('build_richmond_local.py', [
("We book vetted carriers across the city and the counties, from the Fan and Church Hill to Short Pump, Midlothian, and Mechanicsville.","We book vetted carriers across the city and the counties, from the Fan to Short Pump, Midlothian, and Mechanicsville."),
("This page covers 95, 64, 295, 288, the toll roads, the Fan, Church Hill, Scott’s Addition, the West End, and the counties.","This page covers 95, 64, 295, 288, the toll roads, the Fan, Church Hill, the West End, and the counties."),
("It also covers the state workforce, the university, the headquarters, the Army post, the port, the race weekends, and the lanes.","It also covers the state workforce, the university, the headquarters, the Army post, the race weekends, and the lanes."),
("Interstate 95 runs north and south through downtown, over the James on the bridge by the old train shed.","Interstate 95 runs north and south through downtown. It crosses the James on the bridge by the old train shed."),
("Interstate 64 arrives from Charlottesville, shares the downtown miles with 95, and leaves east for Williamsburg and the coast.","Interstate 64 arrives from Charlottesville and shares the downtown miles with 95. It leaves east for Williamsburg and the coast."),
("Interstate 295 loops the north and east from Short Pump to Petersburg, and most carriers use it to skip downtown.","Interstate 295 loops the north and east from Short Pump to Petersburg. Most carriers use it to skip downtown."),
("The Expressway and the Powhite Parkway are toll roads across the river, and the toll rides inside the quote.","The Expressway and the Powhite Parkway are toll roads across the river. The toll rides inside the quote."),
("The mall lots at Short Pump and the centers along Broad in the West End are the usual meeting spots.","The mall lots at Short Pump are the usual meeting spot, and the centers along Broad in the West End work too."[:0]+"The mall lots at Short Pump are the usual meeting spot. The centers along Broad in the West End work too."),
("Our office is on West Broad Street in Scott’s Addition, at Arthur Ashe Boulevard and minutes from 195 and 95.","Our office is on West Broad Street in Scott’s Addition, at Arthur Ashe Boulevard.",2),
("The Museum District west of it is the same, and Carytown on Cary Street is the same with shops.","The Museum District west of it is the same. Carytown on Cary Street is the same with shops."),
("Shockoe Bottom and Shockoe Slip below it are cobblestones by the river, and the handoff moves to the Main Street station lots.","Shockoe Bottom and Shockoe Slip below it are cobblestones by the river. The handoff moves to the Main Street station lots."),
("Manchester and the Southside across the river are old industrial blocks turned apartments, with the handoff on Hull Street.","Manchester across the river is old industrial blocks turned apartments. The handoff happens on Hull Street."),
("The Near West End along Grove and Patterson is older and tighter, and the handoff moves to the centers on Patterson.","The Near West End along Grove and Patterson is older and tighter. The handoff moves to the centers on Patterson."),
("The credit card bank in Goochland, the used-car chain beside it, the tobacco company, the power utility, and the insurers all relocate staff on offer dates.","The credit card bank in Goochland and the used-car chain beside it relocate staff on offer dates. The tobacco company, the power utility, and the insurers do the same."),
("Richmond runs on a race schedule, a campus calendar, and a river that climbs the Bottom in a hurricane.","Richmond runs on a race schedule and a campus calendar. The river climbs the Bottom in a hurricane."),
("The raceway on Laburnum Avenue runs its big race weekend in late summer, with smaller events through the year.","The raceway on Laburnum Avenue runs its big race weekend in late summer. Smaller events fill the year."),
("The folk festival fills the riverfront downtown for a weekend in October, and the Monument Avenue 10K fills the Fan on a Saturday in April.","The folk festival fills the riverfront downtown for a weekend in October. The Monument Avenue 10K fills the Fan on a Saturday in April."),
("The state fair fills the Meadow Event Park in Doswell for ten days in late September, and the 95 exit backs up.","The state fair fills the Meadow Event Park in Doswell for ten days in late September. The 95 exit backs up."),
("A January ice storm takes the power out in the West End for days, and the hills in Church Hill and Forest Hill glaze first.","A January ice storm takes the power out in the West End for days. The hills in Church Hill and Forest Hill glaze first."),
("At pickup the driver walks the car with you and writes every existing mark on the Bill of Lading.","At pickup the driver walks the car with you. Every existing mark goes on the Bill of Lading."),
("The Fan is row houses on narrow streets with cars on both sides, and Church Hill is cobblestones on a slope.","The Fan is row houses on narrow streets with cars on both sides. Church Hill is cobblestones on a slope."),
("A carrier that crosses the river on either one pays the toll with a transponder, and it rides inside the quote.","A carrier that crosses the river on either one pays the toll with a transponder. It rides inside the quote."),
])

fix('build_erie_local.py', [
("Car shipping in Erie runs on Interstate 90 along the south edge of the city and Interstate 79 up from Pittsburgh.","Car shipping in Erie runs on Interstate 90 along the south edge and Interstate 79 up from Pittsburgh."),
("Peach Street is Route 19, the retail strip from 90 to downtown, and 12th Street is Route 5 along the lake.","Peach Street is Route 19, the retail strip from 90 to downtown. Route 5 runs along the lake."),
("This page covers 90, 79, Peach Street, the Bayfront Parkway, downtown, the east and west sides, Millcreek, Harborcreek, and the lake towns.","This page covers 90, 79, Peach Street, the bayfront, downtown, the old grids, Millcreek, Harborcreek, and the lake towns."),
("Carriers running between Buffalo and Cleveland pass the city on 90 all day, and the Pittsburgh trucks come up 79.","Carriers running between Buffalo and Cleveland pass the city on 90 all day. The Pittsburgh trucks come up 79."),
("Interstate 79 comes up from Pittsburgh through Edinboro and ends at 90 on the south edge of the city.","Interstate 79 comes up from Pittsburgh through Edinboro and ends at 90 on the south edge."),
("Interstate 86 begins at 90 by the New York line and runs east through Jamestown to the Southern Tier.","Interstate 86 begins at 90 by the New York line. It runs east through Jamestown to the Southern Tier."),
("Peach Street is Route 19, from the 90 interchange past the mall and the big-box strip to downtown and the bay.","Peach Street is Route 19. It runs from the 90 interchange past the mall and the big-box strip to downtown."),
("12th Street and the lakefront road are Route 5, and the Bayfront Parkway runs the shore from the west side to the port.","12th Street and the lakefront road are Route 5. The Bayfront Parkway runs the shore from the west side to the port."),
("The centers along 26th Street, the lots by the ballpark downtown, and the Harborcreek centers on Buffalo Road work too.","The centers along 26th Street and the lots by the ballpark downtown work too. So do the Harborcreek centers on Buffalo Road."),
("The west side along West 8th and West 26th is the old neighborhoods of narrow blocks and double houses.","The west side along West 8th and West 26th is old neighborhoods of narrow blocks and double houses."),
("The east side along Parade and Buffalo Road is the same grid, and the handoff moves to the Buffalo Road lots.","The east side along Parade and Buffalo Road is the same grid. The handoff moves to the Buffalo Road lots."),
("Glenwood on the south side holds the university and the zoo on wider streets, and the curb often works.","Glenwood on the south side holds the university and the zoo on wider streets. The curb often works."),
("Millcreek Township wraps the city on the south and west, and it holds the mall, the airport, and the big subdivisions.","Millcreek Township wraps the city on the south and west. It holds the mall, the airport, and the big subdivisions."),
("North East to the east is the wine town among the vineyards, and the handoff happens on Main Street.","North East to the east is the wine town among the vineyards. The handoff happens on Main Street."),
("The Catholic university downtown, the college on the south side, the state campus in Harborcreek, and the university in Edinboro all do it.","The Catholic university downtown and the college on the south side do it. So do the state campus in Harborcreek and the university in Edinboro."),
("A parent sets up the booking, and an adult over eighteen signs at a campus lot or the mall.","A parent sets up the booking. An adult over eighteen signs at a campus lot or the mall."),
("The Christmas storm of 2017 dropped more than five feet in two days and buried the city for a week.","The Christmas storm of 2017 dropped more than five feet in two days. The city stayed buried for a week."),
("The lake takes the shore in a fall gale, and the bayfront floods when the wind sets up from the west.","The lake takes the shore in a fall gale. The bayfront floods when the wind sets up from the west."),
("At pickup the driver walks the car with you and records every existing mark on the Bill of Lading.","At pickup the driver walks the car with you. Every existing mark goes on the Bill of Lading."),
("Downtown is a tight grid around Perry Square, and the old east and west sides are narrow blocks of double houses.","Downtown is a tight grid around Perry Square. The old east and west sides are narrow blocks of double houses."),
("The driver meets you at the ballpark lots, on the Bayfront Parkway, or at the centers on 26th Street.","The driver meets you at the ballpark lots, on the Bayfront Parkway, or on 26th Street."),
("A band can drop a foot in an afternoon, and the state bans trucks from the interstate until it lifts.","A band can drop a foot in an afternoon. The state bans trucks from the interstate until it lifts."),
("The New York Thruway east of the state line and the Turnpike south of Pittsburgh charge by the mile, and the toll rides inside the quote.","The Thruway east of the state line and the Turnpike south of Pittsburgh charge by the mile. The toll rides inside the quote."),
])

fix('build_cranston_local.py', [
("We book vetted carriers across the city and the state, from Edgewood and Pawtuxet to Garden City, Knightsville, and Western Cranston.","We book vetted carriers across the city and the state, from Edgewood and Pawtuxet to Garden City and Western Cranston."),
("Reservoir Avenue is Route 2, the retail strip that carries Garden City, and Route 295 runs the west side.","Reservoir Avenue is Route 2, the retail strip that carries Garden City. Interstate 295 runs the west side."),
("This page covers 95, Route 10, Route 37, 295, Reservoir Avenue, the bay side, the village grids, Garden City, and Western Cranston.","This page covers 95, Route 10, Route 37, 295, Reservoir Avenue, the bay side, the village grids, and Western Cranston."),
("It also covers the state campus, the prison, the hospitals, the colleges, the airport, the storms, and the lanes.","It also covers the state campus, the hospitals, the colleges, the airport, the storms, and the lanes."),
("The Providence carriers pass the city on 95 every hour, and the Boston and New York trucks run it all day.","The Providence carriers pass the city on 95 every hour. The Boston and New York trucks run it all day."),
("Cranston sits between Providence and the airport, and a carrier is never more than ten minutes from a highway.","Cranston sits between Providence and the airport. A carrier is never more than ten minutes from a highway."),
("Route 10 is the Huntington Expressway, from Route 37 north through the middle of the city to downtown Providence.","Route 10 is the Huntington Expressway. It runs from Route 37 north through the middle of the city to Providence."),
("Edgewood on the bay is big old houses on narrow streets under the trees, beside the park and the zoo.","Edgewood on the bay is big old houses on narrow streets under the trees. The park and the zoo sit beside it."),
("Oaklawn, Meshanticut, and Dean Estates along Oaklawn Avenue are the same, with bigger lots as the road runs west.","Oaklawn, Meshanticut, and Dean Estates along Oaklawn Avenue are the same. The lots get bigger as the road runs west."),
("The design school, the Ivy on the hill, the Catholic college, and the state university’s downtown campus all do it.","The design school, the Ivy on the hill, and the Catholic college all do it. So does the state university’s downtown campus."),
("The jewelry and textile shops that built the city have given way to the medical offices and the warehouses along 295.","The jewelry and textile shops that built the city have given way to medical offices and warehouses along 295."),
("The Guard units at the state armory rotate staff on orders, and the Navy base in Newport moves officers through the city.","The Guard units at the state armory rotate staff on orders. The Navy base in Newport moves officers through the city."),
("The feast in Knightsville fills Cranston Street for a weekend in July, and the streets around the church close.","The feast in Knightsville fills Cranston Street for a weekend in July. The streets around the church close."),
("The blizzard of 1978 trapped cars on 95 for days, and every big storm since has closed the state for a day.","The blizzard of 1978 trapped cars on 95 for days. Every big storm since has closed the state for a day."),
("The March 2010 flood put the river over the mall in Warwick and closed 95 at the river for days.","The March 2010 flood put the river over the mall in Warwick. It closed 95 at the river for days."),
("At pickup the driver walks the car with you and writes every existing mark on the Bill of Lading.","At pickup the driver walks the car with you. Every existing mark goes on the Bill of Lading."),
("The agencies on the state campus transfer staff on start dates all year, and the corrections academy runs a class most years.","The agencies on the state campus transfer staff on start dates all year. The corrections academy runs a class most years."),
("Campus streets are tight and move-in week clogs them, so the handoff happens at Garden City or the stadium lots.","Campus streets are tight and move-in week clogs them. The handoff happens at Garden City or the stadium lots."),
("The March 2010 flood closed 95 at the river for days and put the water over the mall in Warwick.","The March 2010 flood closed 95 at the river for days. The water went over the mall in Warwick."),
])

# ---- residual pass
fix('build_lansing_local.py', [
("The two assembly plants, one south of downtown and one in Delta Township, move engineers in on launch schedules.","The two assembly plants, south of downtown and in Delta Township, move engineers in on launch schedules."),
])
fix('build_vancouver_local.py', [
("This page covers the bridges, 500 and 503, downtown, the waterfront, Hazel Dell, Orchards, Camas, and the north county.","This page covers the bridges, 500 and 503, downtown, the waterfront, Hazel Dell, Orchards, and Camas."),
("Transfers to the chip plants and the sportswear campus west of Portland land here on start dates all year.","Transfers to the chip plants and the sportswear campus west of Portland land here all year.",2),
("'shoulders','replacement'","'shoulder','replacement'"),
("'wafer','laser'","'wafer','offer dates'"),
])
fix('build_chesapeake_local.py', [
("It also covers the Navy families, the headquarters, the hospital, the drawbridges, the beach traffic, the storms, and the lanes.","It also covers the Navy families, the headquarters, the hospital, the drawbridges, the storms, and the lanes."),
("The Chesapeake Expressway is Route 168, a toll road south from Great Bridge to the state line and the Outer Banks.","The Chesapeake Expressway is Route 168, a toll road from Great Bridge to the state line and the Outer Banks."),
("Sailors from the Norfolk piers, Oceana, Little Creek, and the shipyard buy in Great Bridge and Hickory for the schools.","Sailors from the Norfolk piers, Oceana, Little Creek, and the shipyard buy in Great Bridge for the schools."),
("'tunnel','peninsula'","'tunnel','monitor-merrimac tunnel'"),
])
fix('build_richmond_local.py', [
("We book vetted carriers across the city and the counties, from the Fan to Short Pump, Midlothian, and Mechanicsville.","We book vetted carriers across the city and the counties, from the Fan to Short Pump and Mechanicsville."),
("This page covers 95, 64, 295, 288, the toll roads, the Fan, Church Hill, the West End, and the counties.","This page covers 95, 64, 295, 288, the toll roads, the Fan, the West End, and the counties."),
("It also covers the state workforce, the university, the headquarters, the Army post, the race weekends, and the lanes.","It also covers the state workforce, the university, the headquarters, the Army post, the races, and the lanes."),
])
fix('build_erie_local.py', [
("This page covers 90, 79, Peach Street, the bayfront, downtown, the old grids, Millcreek, Harborcreek, and the lake towns.","This page covers 90, 79, Peach Street, the bayfront, downtown, the old grids, Millcreek, and the lake towns."),
])
fix('build_cranston_local.py', [
("We book vetted carriers across the city and the state, from Edgewood and Pawtuxet to Garden City and Western Cranston.","We book vetted carriers across the city and the state, from Edgewood to Garden City and Western Cranston."),
("This page covers 95, Route 10, Route 37, 295, Reservoir Avenue, the bay side, the village grids, and Western Cranston.","This page covers 95, Route 10, Route 37, 295, Reservoir Avenue, the village grids, and Western Cranston."),
("The jewelry and textile shops that built the city have given way to medical offices and warehouses along 295.","The jewelry and textile shops that built the city have given way to medical offices and warehouses."),
])

# ---- final pass (applied inline)
# chesapeake: "The Chesapeake Expressway is Route 168, a toll road from Great Bridge to the Outer Banks."
# vancouver: dropped the 'north county' local term (phrase removed from the intro)
