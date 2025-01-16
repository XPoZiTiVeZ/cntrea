data = [[int(n) for n in row.split()] for row in open("9.txt").read().splitlines()]

c = 0
for row in data:
    k = {}
    
    for n in row: k[row.count(n)] = k.get(n, set()) | set([n])
    
    maxn = max(row)
    if list(k.get(1, [0]))[0] != maxn: continue
    
    if len(k.get(1)) == 6: continue
    if (sum(row) - maxn) / 5 * 3 >= maxn: continue
    
    print(row)
    c += 1
print(c)