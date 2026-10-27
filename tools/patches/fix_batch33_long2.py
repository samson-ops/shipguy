D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c==1, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')
fix('build_evansville_local.py', [
("The campus on Lincoln Avenue and the one on the West Side fill with cars each August and empty in May.","The campus on Lincoln Avenue and the one on the West Side fill with cars each August. They empty in May."),
])
fix('build_aurorail_local.py', [
("The Southlake campus and the community college in Sugar Grove take cars in every August and send them out every May.","The Southlake campus and the community college in Sugar Grove take cars in every August. They send them out every May."),
])
fix('build_kapaa_local.py', [
("A West Coast origin lands on Kauai in three to four weeks, and an East Coast origin in four to five.","A West Coast origin lands on Kauai in three to four weeks. An East Coast origin takes four to five."),
("Outbound, the car boards at Nawiliwili, sails direct or by way of Honolulu, and lands at a West Coast port.","Outbound, the car boards at Nawiliwili and sails direct or by way of Honolulu. It lands at a West Coast port."),
("The gate rules run in reverse: nothing inside, a quarter tank, no red dirt, and the title in hand.","The gate rules run in reverse: nothing inside, a quarter tank, no red dirt, title in hand."),
("We match those to the next sailing and the barge, and the Kapaʻa number is firm when it arrives.","We match those to the next sailing and the barge. The Kapaʻa number is firm when it arrives."),
("Give us the mainland origin, the Kauai district, and your dates, and we aim the pickup at the next sailing.","Give us the mainland origin, the Kauai district, and your dates. We aim the pickup at the next sailing."),
])
