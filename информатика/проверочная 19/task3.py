from functools import cache

def neighbors(pos):
    a, b, p = pos
    result = []

    if a == 0 or b == 0:
        return result

    if a >= 2 and p != "1":
        result.append((a-2, b, "1"))
    if b >= 2 and p != "2":
        result.append((a, b-2, "2"))
    if a >= 1 and b >= 1 and p != "3":
        result.append((a-1, b-1, "3"))
    if b % 2 == 0 and b > 0 and p != "4":
        result.append((a, b // 2, "4"))
    
    return result


@cache
def abc(pos):
    nc     = [abc(n) for n in neighbors(pos)]
    trues  = [dist for color, dist in nc if color]
    falses = [dist for color, dist in nc if not color]

    if len(falses) > 0: return True,  1 + min(falses)
    if len(trues)  > 0: return False, max(trues)

    return False, 0


for s in range(1, 20):
    r = abc((s, 8, ""))
    if r == (False, 6):
        print(s)