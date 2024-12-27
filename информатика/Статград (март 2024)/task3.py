data = [row.split() for row in open("task3.txt").read().splitlines()]

d = {}
for row in data:
    m = row[2]
    q = int(row[5])
    r = int(row[6])
    
    d[m] = d.get(m, 0) + q * r

c = 0
for m, s in d.items():
    if s > 400000:
        c += 1
print(c)