from itertools import permutations


words = list(sorted(permutations("ВИКТОР", r=6)))
print(*words[:10], sep="\n")
print(''.join(words[265]))