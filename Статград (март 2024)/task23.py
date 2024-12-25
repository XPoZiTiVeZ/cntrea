def path(n, e, p):
    if n > e: return []
    if n == e: return [p.copy()]
    
    return path(n + 1, e, p.copy() + [n + 1]) + path(n * 2, e, p.copy() + [n * 2])

paths = path(1, 19, [1])
c = 0
for path_ in paths:
    if len(list(filter(lambda n: n % 2 == 0, path_))) > 4: continue
    
    c += 1
    print(path_)