from functools import cache

file = open("out", "w+")
def neighbors(pos):
    a, b = pos
    if a + b > 40: return []
    
    result = []
    if a > b:
        result.append((a + 1, b))
        result.append((a + 2, b))
        result.append((a + 3, b))
        result.append((a, b * 2))
    elif a < b:
        result.append((a, b + 1))
        result.append((a, b + 2))
        result.append((a, b + 3))
        result.append((a * 2, b))
    else:
        result.append((a + 1, b))
        result.append((a + 2, b))
        result.append((a + 3, b))
        result.append((a, b + 1))
        result.append((a, b + 2))
        result.append((a, b + 3))
    
    return result

@cache
def abc(pos):
    nc = [abc(n) for n in neighbors(pos)]
    trues = [dist for color, dist in nc if color]
    falses = [dist for color, dist in nc if not color]
    
    if len(falses) > 0: return True, 1 + min(falses)
    if len(trues) > 0: return False, max(trues)
    
    return False, 0

cands = []
for j in range(1, 24):
    if abc((17, j)) == (False, 2):
        cands.append(j)
print(*cands, sep="\n")