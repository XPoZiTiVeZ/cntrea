data1 = [row.split() for row in open("3_1.txt", encoding="UTF-8").read().splitlines()]
data2 = [row.split() for row in open("3_2.txt", encoding="UTF-8").read().splitlines()]

Mg = [row[0] for row in data2]
Va = [[row[2], row[4], row[5], row[6]] for row in data1]

buy = 0
sell = 0
for row in Va:
    if row[0] not in Mg: continue
    if row[1] == "Продажа":
        sell += int(row[2]) * int(row[3])
    else:
        buy += int(row[2]) * int(row[3])

print(buy, sell, sell - buy)