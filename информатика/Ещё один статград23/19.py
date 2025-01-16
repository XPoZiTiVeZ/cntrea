from functools import cache

def neighbors(pos):
    a, b = pos

    if a >= 48 or b >= 48: return []

    result = []
    if a > b:
        result.append((a + 1, b))
        result.append((a + 2, b))
        result.append((a + 3, b))
        result.append((a, b * 2))
    elif a < b:
        result.append((a * 2, b))
        result.append((a, b + 1))
        result.append((a, b + 2))
        result.append((a, b + 3))
    else:
        result.append((a + 1, b))
        result.append((a + 2, b))
        result.append((a + 3, b))
        result.append((a, b + 1))
        result.append((a, b + 1))
        result.append((a, b + 2))
    
    return result

@cache
def abc(pos):
    nc = [abc(n) for n in neighbors(pos)]
    trues = [dist for color, dist in nc if color]
    falses = [dist for color, dist in nc if not color]

    if len(falses) > 0: return True, 1 + min(falses)
    if len(trues)  > 0: return False, max(trues)

    return False, 0

# for x in range(1, 48):
for y in range(1, 48):
    if abc((39, y)) == (False, 2):
        print(39, y)