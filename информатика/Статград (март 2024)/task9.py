data = [[int(n) for n in row.split()] for row in open("09.txt").read().splitlines()]

rows = data.copy()
columns = [[data[i][j] for i in range(len(data))] for j in range(6)]

c = 0
for row in rows:
    line = [0] * 6
    
    for i in range(6):
        n = row[i]
        if row.count(n) != 1: continue
        if columns[i].count(n) <= 150: continue
        
        line[i] = 1
    
    if sum(line) < 2: continue
    for n in row:
        if row.count(n) > 1: break
    else: continue
    
    c += 1
    # print(row, line)
print(c)