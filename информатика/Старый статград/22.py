data = open("22.txt").read().splitlines()

table_req = {}
table_t = {}

for row in data:
    d = row.split("\t")
    id = int(d[0])
    t = int(d[1])
    r = [int(n) for n in d[2].split(";")]
    
    table_req[id] = r
    table_t[id] = t

def dur(id):
    if id == 0: return 0
    
    r = table_req[id]
    t = table_t[id]
    times = []
    for id_ in r:
        times.append(dur(id_) + t)
        
    return max(times)

times3 = []
f = open("out", "w+")
for id in table_t.keys():
    if dur(id) - table_t[id] < 150 and dur(id) > 150:
        times3.append(dur(id))
    print(id, dur(id), file=f)

print(len(times3))