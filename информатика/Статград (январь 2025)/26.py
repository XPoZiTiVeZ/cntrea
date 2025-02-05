data = [[int(n) for n in row.split()] for row in open("26.txt").read().splitlines()]

field = {}

for row in data:
    y, x = row
    n = set(field.get(y, []))
    n.add(x)
    field[y] = list(n)

rows = []
for y, dots in field.items():
    dots = list(sorted(dots))
    n = 0
    if len(dots) <= 1:
       rows.append((len(dots), y))
       continue
   
    if len(dots) == 2:
        if abs(dots[0] - dots[1]) > 500:
            rows.append((2, y))
        else:
            rows.append((0, y))
        continue
    
    if y == 58612:
        print(dots)
    
    for i in range(len(dots)):
        d1 = None
        if i > 0:
            d1 = abs(dots[i - 1] - dots[i]) > 500
        
        d2 = None
        if i < len(dots) - 1:
            d2 = abs(dots[i] - dots[i + 1]) > 500
        
        if d1 != None and d2 != None and d1 and d2:
            n += 1
            if y == 58612:
                print(d1, d2, dots[i - 1], dots[i], dots[i + 1])
        elif d1 != None and d2 == None and d1:
            n += 1
            if y == 58612:
                print(d1, d2, dots[i - 1], dots[i])
        elif d2 != None and d1 == None and d2:
            n += 1
            if y == 58612:
                print(d1, d2, dots[i], dots[i + 1])
    
    rows.append((n, y))
print(*sorted(rows)[-20:], sep="\n")