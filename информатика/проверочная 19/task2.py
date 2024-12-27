from functools import cache

def neighbors(pos):
    a, b = pos
    result = []

    if a == 0 or b == 0:
        return result

    if a >= 2:
        result.append((a-2, b))
    if b >= 2:
        result.append((a, b-2))
    if a >= 1 and b >= 1:
        result.append((a-1, b-1))
    if b % 2 == 0 and b > 0:
        result.append((a, b // 2))
    
    return result


@cache
def abc(pos):
    nc     = [abc(n) for n in neighbors(pos)]
    trues  = [dist for color, dist in nc if color]
    falses = [dist for color, dist in nc if not color]

    if len(falses) > 0: return True,  1 + min(falses)
    if len(trues)  > 0: return False, max(trues)

    return True, 0


for s in range(1, 1000):
    r = abc((10, s))
    if r == (True, 3):
        print(s)