data = [int(n) for n in open("27-B.txt").read().split()]

table = {
    0: [0, 0],
    1: [0, 0],
    2: [0, 0],
    3: [0, 0],
    4: [0, 0],
    5: [0, 0],
    6: [0, 0],
    7: [0, 0],
    8: [0, 0],
}

for i in range(len(data)):
    n = table[data[i] % 9]
    if data[i] > n[0]:
        n[1] = n[0]
        n[0] = data[i]

print(max([sum(v) for v in table.values()]))