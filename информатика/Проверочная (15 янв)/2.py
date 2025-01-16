data = open("2_6.txt").read().splitlines()

table_req = {}
table_t = {}

for row in data:
    d = row.split(",")
    id = int(d[0])
    t = int(d[1])
    r = [int(n) for n in d[2].split("; ")]
    
    table_req[id] = r
    table_t[id] = t

def dur(id):
    if id == 0: return 0
    r = table_req[id]
    t = table_t[id]
    
    times = []
    for id_ in r:
        times.append(dur(id_))
        
    return max(times) + t

times3 = []
for id in table_t.keys():
    times3.append(dur(id))

print(max(times3))