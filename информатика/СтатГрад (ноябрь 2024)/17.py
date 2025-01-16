data = [int(n) for n in open("17.txt").read().split()]

candidates = []

maxn = max(filter(lambda x: x % 100 == 19, data))
for i in range(len(data) - 2):
    n1, n2, n3 = data[i:i + 3]
    
    if ((len(str(n1)) == 4) + (len(str(n2)) == 4) + (len(str(n3)) == 4)) != 2: continue
    if n1 % 3 != 0 and n2 % 3 != 0 and n3 % 3 != 0: continue
    if n1 + n2 + n3 <= maxn: continue

    candidates.append(n1 + n2 + n3)
print(len(candidates), max(candidates))