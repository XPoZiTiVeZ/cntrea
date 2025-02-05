from functools import cache

def neighbors(pos):
    a = pos
    if a <= 15: return []
    
    result = []
    for i in range(2, 10):
        if a % i == 0:
            result.append(a - i)
    
    if len(result) == 0:
        a -= 1
        for i in range(2, 10):
            if a % i == 0:
                result.append(a - i)
    
    return result

@cache
def abc(pos):
    nc = [abc(n) for n in neighbors(pos)]
    trues = [dist for color, dist in nc if color]
    falses = [dist for color, dist in nc if not color]
    
    if len(falses) > 0: return True, 1 + min(falses)
    if len(trues) > 0:  return False, max(trues)
    
    return False, 0

for s in range(16, 100):
    r = abc(s)
    if r == (False, 2):
        print(s)