from functools import cache
import sys

sys.setrecursionlimit(100000)

@cache
def F(n):
    if n > 1_000_000: return n
    else: return n + F(2 * n)

def G(n):
    return F(n) / n

n = G(1000)
for i in range(10000):
    if G(i) == n:
        print(i)