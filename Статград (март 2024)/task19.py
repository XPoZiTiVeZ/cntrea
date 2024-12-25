from functools import cache

def neighbors(pos):
    a = pos
    if a < 13: return []
    
    result = []
    for i in range(2, a+1):
        if a % i == 0:
            result.append(a - a // i)
    
    return result

@cache
def abc(pos):
    nc = [abc(n) for n in neighbors(pos)]
    trues = [dist for color, dist in nc if color]
    falses = [dist for color, dist in nc if not color]
    
    if len(falses) > 0: return True,  min(falses) + 1
    if len(trues)  > 0: return False, max(trues)
    
    return False, 0

for s in range(13, 100):
    if abc(s) == (False, 2):
        print(s)