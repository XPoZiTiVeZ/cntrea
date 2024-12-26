data = open("24.txt").read()

# import re

# my_re = re.compile(r'[A-Z^C^D](?:C|D)')
# c - 15
# D - 50

# C - 1099960
# D - 1100002

# C_ - 42115
# D_ - 42392
# notCD = set()

# for s in data:
#     if s not in "CD":
#         notCD.add(s)

# for s in list(notCD):
#     data = data.replace(s, "")

# open("out", "w+").write(data)
# file = open("ans", "w+")
# for i in range(1500, 2000):
#     for j in range(len(data)-1500, len(data)-2000, -1):
#         C = data[i:j].count("C")
#         D = data[i:j].count("D")
        
#         # print(i, j, C, D)
#         file.write(f"{i} {j} {C} {D}\n")
# ndata = []
nd = {}
C, D = 0, 0
for i, s in enumerate(data):
    if s == "C": C += 1
    if s == "D": D += 1
    d = C - D
    nd[d] = nd.get(d, []) + [i]
    # ndata.append(d)

max_d = 0
for item in nd.items():
    n1, n2 = item[1][0], item[1][-1]
    if max_d < n2 - n1:
        max_d = n2 - n1

print(max_d)
# open("out1", "w+").write(' '.join([ for item in nd.items()]))