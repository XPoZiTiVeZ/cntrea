from itertools import product, permutations

def expr1(x, y, z, w):
    b1 = x or (not y)
    b2 = w == z
    return int((not b1) or b2)

def expr2(x, y, z, w):
    b1 = x or (not y)
    b2 = (not z) or w
    return int(b1 == b2)

rows1 = []
rows2 = []
rows3 = []
for row in product((0, 1), repeat=4):
    if row[0] == 0 and row[2] == 0 and row[3] == 0: rows1.append(row)
    if row[1] == 1 and row[2] == 1: rows2.append(row)
    if row[1] == 0 and row[2] == 0 and row[3] == 0: rows3.append(row)

for r1, r2, r3 in product(rows1, rows2, rows3):
    for perm in permutations("xyzw", r=4):
        xyzw = ["xyzw".index(l) for l in perm]
        
        row1 = [r1[xyzw[i]] for i in range(4)]
        row2 = [r2[xyzw[i]] for i in range(4)]
        row3 = [r3[xyzw[i]] for i in range(4)]
        
        r1e1, r1e2 = expr1(*row1), expr2(*row1)
        r2e1, r2e2 = expr1(*row2), expr2(*row2)
        r3e1, r3e2 = expr1(*row3), expr2(*row3)
        if r1e1 != 0 or r1e2 != 0: continue
        if r2e1 != 0: continue       
        if r3e2 != 0: continue
        
        print(' '.join(perm))
        print(*r1, r1e1, r1e2)
        print(*r2, r2e1, r2e2)
        print(*r3, r3e1, r3e2)
        print()










# def good(table, xyzw):
#     row1 = [table[0][i] for i in range(4)]
#     row2 = [table[1][i] for i in range(4)]
#     row3 = [table[2][i] for i in range(4)]
    
#     if row1[0] != 0: return False
#     if row1[2] != 0: return False
#     if row1[3] != 0: return False
    
#     if row2[1] != 1: return False
#     if row2[2] != 1: return False
    
#     if row3[1] != 0: return False
#     if row3[2] != 0: return False
#     if row3[3] != 0: return False
    
#     return True

# for table in permutations(rows, r=3):
#     for perm in permutations("xyzw", r=4):
#         xyzw = ["xyzw".index(l) for l in perm]
        
#         if good(table, xyzw):
#             print(perm)
#             print(*table, sep="\n")