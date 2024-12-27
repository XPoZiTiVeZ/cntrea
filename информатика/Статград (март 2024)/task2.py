from itertools import product, permutations

def expr(x, y, z, w): 
    b1 = (not (x or y))
    b2 = (y and z)
    b3 = (w == x)
    b4 = (not (w and z))
    
    return (b1 or b2) and (b3 or b4)

rows = []
for row in  product((0, 1), repeat=4):
    if expr(*row) == 1 and row.count(1) >= 1:
        rows.append(row)

def good(table, word):
    if table[0][word[0]] != 1: return False
    if table[0][word[1]] != 0: return False
    if table[0][word[3]] != 0: return False
    
    if table[1][word[0]] != 1: return False
    if table[1][word[1]] != 0: return False
    if table[1][word[3]] != 0: return False
    
    if table[2][word[0]] != 1: return False
    if table[2][word[3]] != 0: return False
    
    return True

print(*rows, sep="\n")

for perm in permutations("xyzw", r=4):
    word = ["xyzw".find(l) for l in perm]
    
    for table in permutations(rows, r=3):
        # print(perm)
        # print(*table, sep="\n")
        # print()
        if good(table, word):
            print(perm)
            print(*table, sep="\n")