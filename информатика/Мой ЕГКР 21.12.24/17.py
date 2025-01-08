data = [int(n) for n in open("17.txt").read().split()]

ns = lambda x: len(str(abs(x))) == 5 and str(x)[-2:] == "43"
maxn = max(data, key=lambda n: n if ns(n) else -100000)
mint = 1000000000000000000000000000000000000000
c = 0

for i in range(len(data) - 2):
    n1, n2, n3 = data[i], data[i + 1], data[i + 2]
    
    if (not ns(n1)) and (not ns(n2)) and (not ns(n3)): continue
    print(n1, n2, n3)
    if n1 ** 2 + n2 ** 2 + n3 ** 2 > maxn ** 2: continue

    c += 1
    if mint > n1 ** 2 + n2 ** 2 + n3 ** 2:
        mint = n1 ** 2 + n2 ** 2 + n3 ** 2

print(c, mint)