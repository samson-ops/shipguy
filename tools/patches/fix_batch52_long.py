"""Batch 52 (Nov 9, 2026): long-sentence (>18 words) rewrites applied to the BUILDERS (not the built HTML), so a rebuild
reproduces the final pages. Idempotent: a pair whose old text is gone is accepted when its new text is present.
Run: python3 patches/fix_batch52_long.py   (then rebuild the five pages)"""
B = '/home/claude/tools/builders_city/'

def fix(fn, pairs):
    p = B + fn
    s = open(p, encoding='utf-8').read()
    n = 0
    for a, b in pairs:
        c = s.count(a)
        if c == 0:
            assert b in s, ('missing', fn, a[:70])
            continue
        s = s.replace(a, b); n += c
    open(p, 'w', encoding='utf-8').write(s)
    print(fn, 'replacements:', n)

fix('build_lakewood_local.py', [
 ("Ship Guy is a licensed auto transport broker with an office on Avenue of the States in the industrial park.","Ship Guy is a licensed auto transport broker with an office in the Lakewood industrial park."),
 ("We book vetted carriers across Lakewood, from the blocks around the yeshiva to the new streets past Cross Street.","We book vetted carriers across Lakewood, from the yeshiva blocks to the new streets past Cross Street."),
 ("The old grid between Route 9 and the lake meets the truck at the industrial park or a Route 70 lot.","The old grid between Route 9 and the lake meets the truck at the industrial park."),
 ("The carriers come off the Parkway at 88 or 91 and off Route 9 at Cedar Bridge or Route 70.","The carriers come off the Parkway at 88 or 91. On Route 9 they turn at Cedar Bridge or Route 70."),
 ("So do the big-box lots on Route 70 at the Brick line and the shopping centers on Route 9 in Howell.","So do the big-box lots on Route 70 at the Brick line. The Route 9 shopping centers in Howell work too."),
 ("Our office sits in Independence Plaza on Avenue of the States, in the industrial park off Cedar Bridge, a short walk from the ballpark.","Our office sits in Independence Plaza on Avenue of the States, in the industrial park off Cedar Bridge."),
 ("Lakewood is an old grid built for a resort town, now carrying a city of a hundred forty thousand people.","Lakewood is an old resort-town grid now carrying a city of a hundred forty thousand people."),
 ("Downtown is Clifton Avenue, two lanes of storefronts, and the blocks of older houses between Route 9 and the lake.","Downtown is Clifton Avenue, two lanes of storefronts, and blocks of older houses toward the lake."),
 ("Point Pleasant, Seaside, and Long Branch are the Shore, and the handoff happens on the mainland side of the bridges in summer.","Point Pleasant, Seaside, and Long Branch are the Shore. In summer the handoff happens on the mainland side of the bridges."),
 ("The yeshiva is the largest outside Israel, and its students and young families arrive from Brooklyn, Monsey, Baltimore, Chicago, and overseas.","The yeshiva is the largest outside Israel. Its students and young families arrive from Brooklyn, Monsey, Baltimore, Chicago, and overseas."),
 ("The joint base at Lakehurst sits fifteen miles west on Route 70, and its families rotate year round with a summer peak.","The joint base at Lakehurst sits fifteen miles west on Route 70. Its families rotate year round with a summer peak."),
 ("The weeks before the holidays are the busiest of the year, and the week after each one is quiet.","The weeks before the holidays are the busiest of the year. The week after each one is quiet."),
 ("Sandy in October 2012 took the power for a week and the trees with it, and the Shore towns east of here lost whole blocks.","Sandy in October 2012 took the power for a week and the trees with it. The Shore towns east of here lost whole blocks."),
 ("The April 2025 wildfire in the pines closed the Parkway south of Toms River for a day and sat smoke on the town.","The April 2025 wildfire in the pines closed the Parkway south of Toms River for a day. The smoke sat on the town."),
 ("Approve the figure, and we hand the car to a carrier already running the Parkway or 195 that week.","Approve the figure, and we hand the car to a carrier already on the Parkway that week."),
 ("The weeks before the fall holidays and before Passover are the busiest of the year, so book those early.","The weeks before the fall holidays and before Passover are the busiest of the year. Book those early."),
 ("The streets between Route 9 and the lake are narrow, the parking is full, and the buses fill them twice a day.","The streets between Route 9 and the lake are narrow, and the parking is full. The buses fill them twice a day."),
 ("The yellow buses fill every street from seven to nine and again from three to five, and Route 9 stalls with them.","The yellow buses fill every street from seven to nine and again from three to five. Route 9 stalls with them."),
 ("A parent or an adult signs at the lot, and the handoff happens at the industrial park or the campus lot.","A parent or an adult signs at the lot. The handoff happens at the industrial park or the campus lot."),
 ("Leisure Village and the villages in Manchester send cars to Florida each fall and bring them back in April.","Leisure Village and the Manchester villages send cars to Florida each fall and bring them back in April."),
 ("The Parkway bans trucks only north of exit 105, and Lakewood’s exits at 88 and 91 sit well south of it.","The Parkway bans trucks only north of exit 105. Lakewood’s exits at 88 and 91 sit well south of it."),
 ('"A working key and a note on anything that acts up",','"A working key, and a word if the car needs the winch",'),
 ("Sandy in 2012 took the power for a week, and a nor’easter floods the Shore roads a few times each winter.","Sandy in 2012 took the power for a week. A nor’easter floods the Shore roads a few times each winter."),
 ("Long Beach Island and the barrier islands add a day in summer, with the handoff on the mainland side of the bridge.","Long Beach Island and the barrier islands add a day in summer. The handoff happens on the mainland side of the bridge."),
])

fix('build_elizabeth_local.py', [
 ("Car shipping in Elizabeth runs on the Turnpike, which drops two exits in the city at the port and the Goethals Bridge.","Car shipping in Elizabeth runs on the Turnpike, which drops two exits in the city at the port."),
 ("Ship Guy is a licensed auto transport broker with an office on Union Street, a few blocks from the train station.","Ship Guy is a licensed auto transport broker with an office on Union Street near the train station."),
 ("The Turnpike runs the east side with exit 13 at the Goethals and exit 13A at the port and the airport.","The Turnpike runs the east side with exit 13 at the Goethals and exit 13A at the port."),
 ("They meet at the outlet-mall lots at the port exit, the furniture store lot beside them, or the big-box lots on 1 and 9 in Linden.","They meet at the outlet-mall lots at the port exit or the furniture store lot beside them. The big-box lots on 1 and 9 in Linden work too."),
 ("The university lots on Morris Avenue work in summer, and the county park lots in Roselle work year round.","The university lots on Morris Avenue work in summer. The county park lots in Roselle work year round."),
 ("The airport is five minutes up 1 and 9 for a fly-and-ship, and the train station runs to Penn Station in half an hour.","The airport is five minutes up 1 and 9 for a fly-and-ship. The train station reaches Penn Station in half an hour."),
 ("Our office sits on Union Street at West Jersey Street, a few blocks west of Broad Street and the train station.","Our office sits on Union Street at West Jersey Street, a few blocks from the train station."),
 ("Elizabeth is a city of two-family houses on narrow streets, a port on one side and a refinery on the other.","Elizabeth is two-family houses on narrow streets, a port on one side, a refinery on the other."),
 ("The streets are one way with bus lanes, and the handoff happens at a garage entrance or on West Jersey Street.","The streets are one way with bus lanes. The handoff happens at a garage entrance or on West Jersey Street."),
 ("Linden is the old plant site, the airport strip on 1 and 9, and grids where the curb works.","Linden is the old plant site, the strip on 1 and 9, and grids where the curb works."),
 ("The port is the largest on the East Coast, and its terminals relocate managers and engineers from the other ports.","The port is the largest on the East Coast. Its terminals relocate managers and engineers from the other ports."),
 ("Families arrive from Portugal, Brazil, Colombia, Peru, and the Dominican Republic, and many ship a car up from Miami.","Families arrive from Portugal, Brazil, Colombia, Peru, and the Dominican Republic. Many ship a car up from Miami."),
 ("The joint base in Burlington County is an hour down the Turnpike, and its families pass through on the same calendar.","The joint base in Burlington County is an hour down the Turnpike. Its families pass through on the same calendar."),
 ("The weather problem is a storm surge up the Arthur Kill and a flash flood down the Elizabeth River.","The weather problem is a surge up the Arthur Kill and a flash flood down the Elizabeth River."),
 ("The port’s peak season runs from August through October, and the container trucks fill North Avenue and Dowd Avenue.","The port’s peak season runs from August through October. The container trucks fill North Avenue and Dowd Avenue."),
 ("Ida in September 2021 put the Elizabeth River through the low streets and flooded hundreds of cars in a night.","Ida in September 2021 put the Elizabeth River through the low streets. It flooded hundreds of cars in a night."),
 ("A strong wind closes the Goethals and the Turnpike bridges to high-profile vehicles, and the Staten Island pickups wait for it to drop.","A strong wind closes the Goethals and the Turnpike bridges to high-profile vehicles. The Staten Island pickups wait for it to drop."),
 ("The driver meets you on Morris Avenue or Elizabeth Avenue, or at the outlet-mall lots at the port exit.","The driver meets you on Morris Avenue, on Elizabeth Avenue, or at the outlet-mall lots."),
 ("The terminals relocate managers from the other ports, the airport hires across the city, and the refinery relocates engineers on turnaround schedules.","The terminals relocate managers from the other ports, and the airport hires across the city. The refinery relocates engineers on turnaround schedules."),
 ("A strong wind closes the Goethals and the Turnpike bridges to high-profile vehicles, and a loaded carrier is one.","A strong wind closes the Goethals and the Turnpike bridges to high-profile vehicles. A loaded carrier is one."),
])

fix('build_hampton_local.py', [
 ("Car shipping in Hampton runs on Interstate 64, which crosses the city from the Newport News line to the bridge-tunnel.","Car shipping in Hampton runs on Interstate 64, which crosses the city to the bridge-tunnel."),
 ("Interstate 64 runs the middle of the city with exits at Mercury Boulevard, Armistead Avenue, Settlers Landing, and Mallory Street.","Interstate 64 runs the middle of the city with exits at Mercury Boulevard, Armistead Avenue, and Settlers Landing."),
 ("Phoebus, downtown, Wythe, and the Fox Hill lanes meet the truck on Mercury Boulevard or at the Coliseum lots.","Phoebus, downtown, Wythe, and the Fox Hill lanes meet the truck on Mercury Boulevard."),
 ("Hampton is a flat city on a harbor with one freeway through the middle and a tunnel at the end of it.","Hampton is a flat harbor city with one freeway through the middle and a tunnel at the end."),
 ("Interstate 664 leaves 64 at the west edge, runs through Newport News, and crosses to Suffolk on the Monitor-Merrimac.","Interstate 664 leaves 64 at the west edge and crosses to Suffolk on the Monitor-Merrimac."),
 ("They meet at the Coliseum lots outside events, the Town Center lots around our office, or the big-box lots on Mercury.","They meet at the Coliseum lots outside events or the Town Center lots around our office. The big-box lots on Mercury work too."),
 ("Our office is in the office building at Peninsula Town Center, in Coliseum Central off Mercury Boulevard and 64.","Our office is in the office building at Peninsula Town Center, off Mercury Boulevard and 64."),
 ("Farmington, Magruder, Michaels Woods, and Bethel are subdivisions on the north side where the truck comes to the house.","Farmington, Magruder, Michaels Woods, and Bethel are north-side subdivisions where the truck comes to the house."),
 ("Riverdale and the Mercury corridor are apartments and strip centers, and the complexes allow a trailer at the entrance.","Riverdale and the Mercury corridor are apartments and strip centers. The complexes allow a trailer at the entrance."),
 ("Fort Monroe is the old post at the tip, closed as a base in 2011 and now a national monument with houses on its streets.","Fort Monroe is the old post at the tip, closed as a base in 2011. It is a national monument now, with houses on its streets."),
 ("Poquoson to the north is a fishing town on marsh roads that flood, and the handoff happens on Wythe Creek Road.","Poquoson to the north is a fishing town on marsh roads that flood. The handoff happens on Wythe Creek Road."),
 ("Joint Base Langley-Eustis sits on the north side of the city, and its fighter wing rotates airmen year round with a summer peak.","Joint Base Langley-Eustis sits on the north side of the city. Its fighter wing rotates airmen year round with a summer peak."),
 ("Families ship a second car on orders every week, and the handoff happens at a lot outside the gate.","Families ship a second car on orders every week. The handoff happens at a lot outside the gate."),
 ("The shipbuilder next door in Newport News relocates engineers on program schedules, and many of them live in Hampton.","The shipbuilder next door in Newport News relocates engineers on program schedules. Many of them live in Hampton."),
 ("The hospital on Coliseum Drive brings nurses all year, and the veterans’ hospital on Emancipation Drive brings staff on federal schedules.","The hospital on Coliseum Drive brings nurses all year. The veterans’ hospital on Emancipation Drive brings staff on federal schedules."),
 ("Fort Monroe closed as a post in 2011, and the naval station across the harbor rotates sailors on the same summer calendar.","Fort Monroe closed as a post in 2011. The naval station across the harbor rotates sailors on the same summer calendar."),
 ("The weather problem is a hurricane every decade, a nor’easter every winter, and a tide that floods the low streets on its own.","The weather problem is a hurricane every decade, a nor’easter every winter, and a flooding tide."),
 ("The work runs to 2027 with lane shifts and overnight closures, and the crossing shuts a few nights a year.","The work runs to 2027 with lane shifts and overnight closures. The crossing shuts a few nights a year."),
 ("Phoebus is tight blocks behind Mellen Street, Wythe is narrow lanes under oaks, and the Fox Hill lanes flood on a high tide.","Phoebus is tight blocks behind Mellen Street, and Wythe is narrow lanes under oaks. The Fox Hill lanes flood on a high tide."),
 ("Homecoming weekend in October closes the streets around the campus, and the handoff moves to the Coliseum lots that weekend.","Homecoming weekend in October closes the streets around the campus. The handoff moves to the Coliseum lots that weekend."),
 ("The research center relocates engineers and scientists on program dates, and the shipbuilder next door relocates engineers on program schedules.","The research center relocates engineers and scientists on program dates. The shipbuilder next door relocates engineers on program schedules."),
 ("Fort Monroe takes a handoff at the lots by the moat, and Poquoson takes one on Wythe Creek Road.","Fort Monroe takes a handoff at the lots by the moat. Poquoson takes one on Wythe Creek Road."),
])

fix('build_suffolk_local.py', [
 ("We book vetted carriers across Suffolk, from the brick blocks downtown to Harbour View and the villages out in the fields.","We book vetted carriers across Suffolk, from the brick blocks downtown to Harbour View and the villages."),
 ("Route 58 runs the bypass around downtown, east to the Bowers Hill interchange and west to Franklin and Interstate 95.","Route 58 runs the bypass around downtown, east to Bowers Hill and west to Franklin and Interstate 95."),
 ("It also covers the peanut plant, the warehouses, the defense complex, the hospital, and the sailors who buy here.","It also covers the peanut plant, the warehouses, the defense complex, the hospital, and the sailors."),
 ("Suffolk is four hundred square miles of city, most of it fields and swamp with a downtown in the middle.","Suffolk is four hundred square miles of city, most of it fields and swamp around one downtown."),
 ("Route 58 is the big road, four lanes from the Bowers Hill interchange in Chesapeake around the north of downtown and west to Franklin, Emporia, and Interstate 95.","Route 58 is the big road, four lanes from Bowers Hill in Chesapeake around the north of downtown. It runs west to Franklin, Emporia, and Interstate 95."),
 ("Interstate 664 runs the north end from Bowers Hill through Harbour View to the Monitor-Merrimac crossing and Newport News.","Interstate 664 runs the north end from Bowers Hill through Harbour View to the Monitor-Merrimac crossing."),
 ("They meet at the shopping centers on North Main Street, the Harbour View lots at the 664 exit, or the lots at the Route 58 and 460 split.","They meet at the North Main Street shopping centers or the Harbour View lots at the 664 exit. The lots at the 58 and 460 split work too."),
 ("The Norfolk airport is forty minutes east for a fly-and-ship, and the Newport News airport is thirty over the bridge-tunnel.","The Norfolk airport is forty minutes east for a fly-and-ship. The Newport News airport is thirty over the bridge-tunnel."),
 ("The truck meets downtown on Main Street, the north end at the curb, and the villages on the state road.","The truck meets downtown on Main Street and the north end at the curb. The villages mean the state road."),
 ("Whaleyville and Holland are farm villages on the south and west sides, and the handoff happens on the state road.","Whaleyville and Holland are farm villages on the south and west sides. The handoff happens on the state road."),
 ("Smithfield to the north is the ham town, a tight old main street with a lot on the edge.","Smithfield to the north is the ham town, a tight main street with a lot on the edge."),
 ("The peanut plant downtown has shelled and roasted since the mascot was born here, and it hires on the harvest.","The peanut plant downtown has shelled and roasted since the mascot was born here. It hires on the harvest."),
 ("The defense complex in Harbour View trains the services on simulations, and the contractors around it relocate analysts on clearance timelines.","The defense complex in Harbour View trains the services on simulations. The contractors around it relocate analysts on clearance timelines."),
 ("Sailors from the naval station and the shipyard in Portsmouth buy in Harbour View for the price and the schools.","Sailors from the naval station and the Portsmouth shipyard buy in Harbour View for the schools."),
 ("The Joint Staff’s training complex in Harbour View rotates officers on orders, and the naval station is thirty minutes east.","The Joint Staff’s training complex in Harbour View rotates officers on orders. The naval station is thirty minutes east."),
 ("The weather problem is a hurricane every decade, a tornado once in a lifetime, and a swamp that burns for months.","The weather problem is a hurricane every decade, a rare tornado, and a swamp that burns for months."),
 ("When the region evacuates for a hurricane, every car in Hampton Roads comes through Suffolk on 58 and 460.","When the region evacuates for a hurricane, every car comes through Suffolk on 58 and 460."),
 ("Isabel in September 2003 put trees across every road in the city, and the power stayed out for two weeks.","Isabel in September 2003 put trees across every road in the city. The power stayed out for two weeks."),
 ("Fog rolls off the swamp onto 58 and 13 on fall mornings, and a driver waits for it to lift.","Fog rolls off the swamp onto 58 and 13 on fall mornings. A driver waits for it to lift."),
 ("Raleigh runs two hundred twenty to three hundred forty dollars for a sedan, about one hundred sixty-five miles down 58 and 95.","Raleigh runs two hundred twenty to three hundred forty dollars for a sedan. It is about one hundred sixty-five miles down 58 and 95."),
 ("The Peninsula and the Southside price the same as each other, and Suffolk sits a few dollars under on the western lanes.","The Peninsula and the Southside price the same as each other. Suffolk sits a few dollars under on the western lanes."),
 ("Sailors from the naval station and the Portsmouth shipyard and the shipbuilders from Newport News buy in Harbour View.","Sailors from the naval station and the Portsmouth shipyard buy in Harbour View. So do the Newport News shipbuilders."),
 ("The warehouses along 58 relocate managers in spring and fall, and the defense complex and the contractors in Harbour View relocate analysts on clearance timelines.","The warehouses along 58 relocate managers in spring and fall. The defense complex and the contractors in Harbour View relocate analysts on clearance timelines."),
 ("The airport grounds on Carolina Road fill for four days each October, and the handoff moves to North Main Street that week.","The airport grounds on Carolina Road fill for four days each October. The handoff moves to North Main Street that week."),
 ("The pickup moves to the first clear day after the roads open, and the figure stays where it was.","The pickup moves to the first clear day after the roads open. The figure stays where it was."),
])

fix('build_gresham_local.py', [
 ("Car shipping in Gresham runs on Interstate 84 and the Mount Hood Highway, with 205 ten minutes west for the valley lanes.","Car shipping in Gresham runs on Interstate 84 and the Mount Hood Highway, with 205 ten minutes west."),
 ("Ship Guy is a licensed auto transport broker with an office on Eastman Parkway beside the City Hall light-rail station.","Ship Guy is a licensed auto transport broker with an office on Eastman Parkway by the light-rail station."),
 ("We book vetted carriers across Gresham, from the Rockwood apartments to the Powell Valley farms and the Persimmon hills.","We book vetted carriers across Gresham, from the Rockwood apartments to the Powell Valley farms."),
 ("Interstate 84 runs the north edge with exits at 181st, Fairview Parkway, Wood Village, and Troutdale, where the Gorge begins.","Interstate 84 runs the north edge with exits at 181st, Fairview Parkway, Wood Village, and Troutdale."),
 ("The city sits where the Interstate 84 trucks leave the Gorge and the 205 trucks reach the east side.","The city sits where the 84 trucks leave the Gorge and the 205 trucks reach the east side."),
 ("The Seattle and California carriers run 5 and 205 past the city daily, and the Boise and Spokane trucks come down 84.","The Seattle and California carriers run 5 and 205 past the city daily. The Boise and Spokane trucks come down 84."),
 ("Historic downtown, Gresham Butte, and the Persimmon hills meet the truck on a boulevard or at the Town Fair lots.","Historic downtown, Gresham Butte, and the Persimmon hills meet the truck on a boulevard."),
 ("Gresham is a grid at the foot of the Cascades with a freeway along the top and the mountain highway through the middle.","Gresham is a grid at the foot of the Cascades. A freeway runs along the top, and the mountain highway runs through the middle."),
 ("Past Troutdale the freeway enters the Gorge, where wind, ice, and rockfall close it a few times each winter.","Past Troutdale the freeway enters the Gorge. Wind, ice, and rockfall close it a few times each winter."),
 ("It comes in on Powell Boulevard, turns up Burnside through downtown, and runs east to Sandy and the ski areas.","It comes in on Powell Boulevard and turns up Burnside through downtown. Then it runs east to Sandy and the ski areas."),
 ("They meet at the Town Fair lots at Division and Eastman, the big-box lots at Gresham Station, or the Troutdale truck stops at the Gorge exit.","They meet at the Town Fair lots at Division and Eastman or the big-box lots at Gresham Station. The Troutdale truck stops at the Gorge exit work too."),
 ("Our office sits on Eastman Parkway beside the City Hall light-rail station, across from the Town Fair shopping center.","Our office sits on Eastman Parkway beside the City Hall light-rail station, across from the Town Fair."),
 ("Gresham is an old farm town swallowed by Portland’s east side, with a butte in the middle and farms still on the edge.","Gresham is an old farm town swallowed by Portland’s east side. A butte sits in the middle, and farms still ring the edge."),
 ("Rockwood along 181st, Stark, and Burnside is the densest part of town, apartment complexes and small houses on a grid.","Rockwood along 181st, Stark, and Burnside is the densest part of town. It is apartment complexes and small houses on a grid."),
 ("Powell Valley east of town is berry farms, nurseries, and houses on wide roads, and the truck reaches the driveway.","Powell Valley east of town is berry farms, nurseries, and houses on wide roads. The truck reaches the driveway."),
 ("Troutdale is the Gorge gateway, the outlets, the airport, the package hub, and old streets by the Sandy River.","Troutdale is the Gorge gateway, the outlets, the package hub, and old streets by the Sandy River."),
 ("Troutdale, Wood Village, Fairview, Happy Valley, and Damascus ship with the same trucks and price the same as Gresham.","Troutdale, Wood Village, Fairview, Happy Valley, and Damascus ride the same trucks. They price the same as Gresham."),
 ("Boise and Salt Lake City ride 84 up the Gorge, and the Gresham pickup is the last stop before the trucks climb.","Boise and Salt Lake City ride 84 up the Gorge. The Gresham pickup is the last stop before the trucks climb."),
 ("The two chip fabs on the east side, on Stark and Glisan, relocate engineers and technicians on program dates from Arizona, Texas, and overseas.","The two chip fabs on Stark and Glisan relocate engineers and technicians on program dates. They come from Arizona, Texas, and overseas."),
 ("The aerospace plant on Sandy Boulevard machines landing gear and large parts and relocates machinists from the other plants.","The aerospace plant on Sandy Boulevard machines landing gear and relocates machinists from the other plants."),
 ("Families arrive in Rockwood from Latin America, Ukraine, and the Pacific islands, and many bring a car from a relative in California.","Families arrive in Rockwood from Latin America, Ukraine, and the Pacific islands. Many bring a car from a relative in California."),
 ("The Air Guard wing at the Portland airport rotates airmen on orders, and the Guard’s post in Clackamas does the same.","The Air Guard wing at the Portland airport rotates airmen on orders. The Guard’s post in Clackamas does the same."),
 ("The weather problem is the east wind, which brings the ice to Gresham before anywhere else in the metro.","The weather problem is the east wind, which ices Gresham before the rest of the metro."),
 ("The January 2024 ice storm shut Gresham and Troutdale for a week, closed 84 at Troutdale, and left tens of thousands without power for days.","The January 2024 ice storm shut Gresham and Troutdale for a week and closed 84 at Troutdale. Tens of thousands lost power for days."),
 ("The Gorge fire in September 2017 closed 84 east of Troutdale for two weeks and dropped ash on the city.","The Gorge fire in September 2017 closed 84 east of Troutdale for two weeks. Ash fell on the city."),
 ("The September 2020 fires put the south side on evacuation notice and sat smoke on the metro for ten days.","The September 2020 fires put the south side on evacuation notice. The smoke sat on the metro for ten days."),
 ("Seattle runs two hundred twenty to three hundred forty dollars for a sedan, about one hundred eighty miles up 205 and 5.","Seattle runs two hundred twenty to three hundred forty dollars for a sedan. It is about one hundred eighty miles up 205 and 5."),
 ("The two fabs on Stark and Glisan relocate engineers from Arizona, Texas, and overseas, and the aerospace plant on Sandy Boulevard relocates machinists.","The two fabs on Stark and Glisan relocate engineers from Arizona, Texas, and overseas. The aerospace plant on Sandy Boulevard relocates machinists."),
])
print('done')
