data = [[int(n) for n in row.split()] for row in open("26.txt").read().splitlines()]

tasks = {}

for row in data:
    tasks[row[0]] = tasks.get(row[0], []) + [row[1]]

print(*tasks.items(), file=open("26out.txt", "w+"), sep="\n")

studs = {}

max_st, max_t = 0, 0
for st, t in tasks.items():
    t = sorted(t.copy())
    maxt = 0
    nowt = 0
    prevt = -1
    for n in t:
        if prevt + 1 != n:
            maxt = max(maxt, nowt)
            nowt = 1
            prevt = n
            continue
        
        nowt += 1
        prevt = n
    
    studs[st] = maxt

    if max_t < maxt:
        max_t = maxt
        max_st = st

        print(maxt, st)

print(max_st, max_t)

print(*studs.items(), sep="\n", file=open("26out1.txt", "w+"))