from itertools import product


words = list(product("АВЕСТ", repeat=5))
print(words.index(("С", "В", "Е", "Т", "А")) + 1)