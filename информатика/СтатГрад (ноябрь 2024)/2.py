from itertools import product, permutations

def expr1(x, y, z, w):
    b1 = x == y
    b2 = (not w) or z
    return int ( b1 and b2 )

def expr2(x, y, z, w):
    b1 = (not x) or y
    b2 = w == z
    return int( (not b1) or b2 )

rows = [[], [], []]
for row in product((0, 1), repeat = 4):
    if row[0] == 1 and row[2] == 1 and row[3] == 1: rows[0].append(row)
    if row[0] == 0 and row[1] == 1 and row[2] == 0: rows[1].append(row)
    if row[1] == 0 and row[2] == 0: rows[2].append(row)

def set_xyzw(table, xyzw):
    row1 = table[0]
    row2 = table[1]
    row3 = table[2]

    return [
        [row1[xyzw[0]], row1[xyzw[1]], row1[xyzw[2]], row1[xyzw[3]]],
        [row2[xyzw[0]], row2[xyzw[1]], row2[xyzw[2]], row2[xyzw[3]]],
        [row3[xyzw[0]], row3[xyzw[1]], row3[xyzw[2]], row3[xyzw[3]]],
    ]

def good(table):
    if expr1(*table[0]) != 1 or expr2(*table[0]) != 0: return False
    if expr1(*table[1]) != 1: return False
    if expr1(*table[2]) != 0 or expr2(*table[2]) != 0: return False


    return True


for table in product(rows[0], rows[1], rows[2]):
    for perm in permutations("xyzw", r=4):
        xyzw = ["xyzw".index(l) for l in perm]
        new_table = set_xyzw(table, xyzw)

        if good(new_table):
            print(*perm, "F", "F")
            print(*new_table[0], expr1(*new_table[0]), expr2(*new_table[0]))
            print(*new_table[1], expr1(*new_table[1]), expr2(*new_table[1]))
            print(*new_table[2], expr1(*new_table[2]), expr2(*new_table[2]))
            print()