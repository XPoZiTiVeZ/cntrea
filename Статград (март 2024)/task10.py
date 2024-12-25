data = open("10.txt", encoding="UTF-8").read()
new_data = ""

notalpha = set()

alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789 "
for s in data:
    if s.lower() not in alpha:
        notalpha.add(s)
    else:
        new_data += s.lower()

for s in list(notalpha):
    new_data = new_data.replace(s, " ")

# print(new_data, file=open("out", "w+", encoding="UTF-8"))

c = 0
for w in new_data.split():
    if w.find("пол") != -1 and w != "пол":
        print(w)
        c += 1
print(c)