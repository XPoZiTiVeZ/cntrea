data = [[float(n) for n in row.split()] for row in open("27_B.txt")]

cl1 = []
cl2 = []
cl3 = []
for x, y in data:
    if x > 0 and y > 7:
        cl1.append((x, y))
    elif x > 0:
        cl2.append((x, y))
    else:
        cl3.append((x, y))

center1 = (0, 0, None)
for x1, y1 in cl1:
    d = 0
    for x2, y2 in cl1:
        if x1 == x2 and y1 == y2: continue
        
        d += (x2 - x1) ** 2 + (y2 - y1) ** 2
    
    if center1[2] == None or center1[2] > d: center1 = (x1, y1, d)

center2 = (0, 0, None)
for x1, y1 in cl2:
    d = 0
    for x2, y2 in cl2:
        if x1 == x2 and y1 == y2: continue
        
        d += (x2 - x1) ** 2 + (y2 - y1) ** 2
    
    if center2[2] == None or center2[2] > d: center2 = (x1, y1, d)

center3 = (0, 0, None)
for x1, y1 in cl3:
    d = 0
    for x2, y2 in cl3:
        if x1 == x2 and y1 == y2: continue
        
        d += (x2 - x1) ** 2 + (y2 - y1) ** 2
    
    if center3[2] == None or center3[2] > d: center3 = (x1, y1, d)

print((center1[0] + center2[0] + center3[0]) / 3 * 10000, (center1[1] + center2[1] + center3[1]) / 3 * 10000)