from itertools import permutations

word = "ГЛУБИНА"
c = 0
for perm in permutations(word, r=7):
    if ''.join(perm).find("Г") > ''.join(perm).find("А") + 1: c += 1

print(c)