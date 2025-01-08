from functools import cache

def neighbors(pos):
    a = pos

    if a >= 132: return []
    result = []

    result.append(a + 3)
    result.append(a + 6)
    result.append(a * 3)

    return result

@cache
def abc(pos):
    nc = [abc(n) for n in neighbors(pos)]
    trues = [dist for color, dist in nc if color]
    falses = [dist for color, dist in nc if not color]

    if len(falses) > 0:  return True, 1 + min(falses)
    if len(trues) > 0:  return False, max(trues)

    return False, 0

for S in range(1, 132):
    r = abc(S)
    if r == (False, 1):
        print(S)