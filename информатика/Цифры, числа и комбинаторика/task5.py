from itertools import permutations

word = "ТИМАШЕВСК"
c = 0
for perm in permutations(word, r=len(word)):
    perm = ''.join(perm)
    if perm[0] not in "ТМШВСК" or perm[-1] not in "ТМШВСК": continue
    for p in permutations("ИАЕ", r=3):
        p = ''.join(p)
        if perm.find(p) != -1: break
    else: continue
    c += 1

print(c)