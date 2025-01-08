from itertools import product

for i, word in enumerate(product("АВНРЬЯ", repeat=5), 1):
    word = "".join(word)
    if word[0] == "Я": continue
    if word.count("Ь") > 1: continue
    if word.find("ЯЯ") != -1: continue

    print(i, word)