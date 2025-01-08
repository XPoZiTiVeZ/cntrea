from itertools import product, permutations

def expr(x, y, z, w):
    b1 = (not x) or y
    b2 = not (b1 and (not w))
    b3 = not (y and w)
    b4 = not (z and b3)
    return int(b2 or b4)

def good(table):
    if table[0][0] != 0: return False
    if table[0][3] != 1: return False

    if table[1][1] != 1: return False
    
    if table[2][0] != 1: return False
    if table[2][1] != 1: return False

    return True

rows = []
for row in product((0, 1), repeat=4):
    if expr(*row) == 0:
        rows.append(row)

print(*rows)


for table in permutations(rows, r=3):
    perm = "xyzw"
    xyzw = [0, 1, 2, 3]
    row1 = (table[0][xyzw[0]], table[0][xyzw[1]], table[0][xyzw[2]], table[0][xyzw[3]])
    row2 = (table[1][xyzw[0]], table[1][xyzw[1]], table[1][xyzw[2]], table[1][xyzw[3]])
    row3 = (table[2][xyzw[0]], table[2][xyzw[1]], table[2][xyzw[2]], table[2][xyzw[3]])

    # if good((row1, row2, row3)):
    print(*''.join(perm))
    print(*row1)
    print(*row2)
    print(*row3)
    print()
    # for perm in permutations("xyzw", r=4):
        # xyzw = ["xyzw".index(l) for l in perm]

        