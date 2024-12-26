import sys

f = sys.stdin
k = int(f.readline())
n = int(f.readline())
data = [int(x) for x in f]

from math import gcd

d = {i: 0 for i in range(100000, 0, -1) if 100000 % i == 0}
count = 0
for i in range(2 * k, n):
    x1 = data[i - 2 * k]
    d[gcd(100000, x1)] += 1
    
    x2 = data[i]
    for y in d.keys():
        if (y * x2) % 100000 == 0:
            count += d[y]
print(count)