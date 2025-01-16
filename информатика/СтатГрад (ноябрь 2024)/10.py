data = open("10.txt", encoding="UTF-8").read()
alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()

ndata = ""
for s in data:
    if s not in alpha:
        ndata += " "
    ndata += s

sdata = ndata.split()
c = 0
for word in sdata:
    i = word.find("ток")
    if i != -1 and i != 0 and i != len(word) - 3:
        c += 1
        print(word)
print(c)