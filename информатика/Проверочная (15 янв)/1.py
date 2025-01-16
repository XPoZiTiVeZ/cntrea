from functools import cache

@cache
def path(n, e, c):
    print(n, e)
    if n > e:  return 0
    if n == e and c == 0: return 0
    if n == e and c == 1: return 1
    
    if n % 10 == 5: c = 1
    
    return path(n + 1, e, c) + path(n + 3, e, c) + path(n * 2, e, c)

print(path(1, 234, 0))
