from functools import cache
import sys

sys.setrecursionlimit(10000)

def neighbors(pos):
    a, b = pos
    if a + b <= 30: return []
    
    result = []
    if a > 0:
        result.append((a - 1, b))
    if a > 1:
        result.append(((a + 1) // 2, b))
    if b > 0:
        result.append((a, b - 1))
    if b > 1:
        result.append((a, (b + 1) // 2))
    
    return result

@cache
def abc(pos):
    nc = [abc(n) for n in neighbors(pos)]
    trues = [dist for color, dist in nc if color]
    falses = [dist for color, dist in nc if not color]
    
    if len(falses) > 0: return True, 1 + min(falses)
    if len(trues) > 0:  return False, max(trues)
    
    return False, 0

for S in range(13, 100):
    if abc((18, S)) == (False, 2):
        print(S)