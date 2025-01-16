data = open("24.txt").read().splitlines()

freqs = {}
for row in data:
    loc_freqs = {}
    for i in range(len(row) - 1):
        l1 = row[i]
        l2 = row[i + 1]
        if l1 == "A": loc_freqs[l2] = loc_freqs.get(l2, 0) + 1
    
    maxn = max(loc_freqs.items(), key=lambda x: x[1])
    for r in loc_freqs.items():
        if r[1] == maxn[1]:
            freqs[r[0]] = freqs.get(r[0], 0) + 1
print(max(freqs.items(), key=lambda x: x[1]))