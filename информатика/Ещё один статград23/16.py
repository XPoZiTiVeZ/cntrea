from functools import cache
<<<<<<< Updated upstream
import sys

sys.setrecursionlimit(100000)

@cache
def F(n):
    if n > 1_000_000: return n
    else: return n + F(2 * n)
=======

@cache
def F(n):
    # print(n, n > 1_000_000)
    if n > 1_000_000: return n
    return n + F(2 * n)
>>>>>>> Stashed changes

def G(n):
    return F(n) / n

<<<<<<< Updated upstream
n = G(1000)
for i in range(10000):
    if G(i) == n:
        print(i)
=======
g = G(1000)
c = 0
for n in range(1, 10000):
    if G(n) == g:
        c += 1
        print(n)

print(c)
>>>>>>> Stashed changes
