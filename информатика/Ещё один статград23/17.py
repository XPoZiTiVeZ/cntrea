data = [int(n) for n in open("17.txt").read().split()]
n = lambda x, y: len(str(abs(x))) == y

minn = min(data, key=lambda x: x if n(x, 3) and str(abs(x))[-1] == "5" else 10 ** 5)

c = 0
maxn = 0
for i in range(len(data)-1):
    n1, n2 = data[i: i+2]

    if not n(n1, 4) ^ n(n2, 4): continue
    if (n1 ** 2 + n2 ** 2) % minn != 0: continue

    c += 1
    maxn = max(n1 ** 2 + n2 ** 2, maxn)
print(c, maxn)