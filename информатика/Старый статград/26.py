data = [[int(n) for n in row.split()] for row in open("26.txt").read().splitlines()]

field = [list() for _ in range(100000)]
for row in data:
    y, x = row
    if x not in field[y-1]:
        field[y-1].append(x)

for i in range(len(field)): field[i] = list(sorted(field[i]))

candidates = []
for i, row in enumerate(field, 1):
    max_t = 0
    prev = None
    start = None
    for d in row:
        if start == None:
            start = d
        
        if prev != None and d - prev > 8:
            # print(2, start, prev, d, prev - start + 1)
            max_t = max(max_t, prev - start + 1)
            prev = d
            start = d
            continue

        # print(1, start, prev, d, max_t)
        prev = d
    candidates.append((max_t, i))

print(*field[97585])
print(max(candidates, key=lambda x: (x[0], x[1])))

# for x in candidates:
#     if x[0] >= 21:
#         print(x)