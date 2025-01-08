data = [[int(n) for n in row.split()] for row in open("9.txt").read().splitlines()]

i = 1
for row in data:
    k = {}
    for n in row: k[row.count(n)] = k.get(row.count(n), set()) | set([n])

    if len(k.get(3, [])) != 2: continue
    if sum(k.get(3, [])) / 3 >= sum(k.get(1, [])): continue

    print(i, k, sum(k.get(3, [])) / 3, sum(k.get(1, [])))
    i += 1