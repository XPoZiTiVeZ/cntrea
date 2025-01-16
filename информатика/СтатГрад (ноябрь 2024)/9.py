data = [[int(n) for n in row.split()] for row in open("9.txt").read().splitlines()]

c = 0
for row in data:
    k = {}
    for n in row: k[row.count(n)] = k.get(row.count(n), []) + [n]
    
    if len(k.get(1, [])) != 6: continue

    maxn = max(k.get(1, []))
    minn = min(k.get(1, []))
    if (maxn + minn) / 2 <= (sum(k.get(1, [])) - maxn - minn) / 4: continue

    c += 1
print(c)