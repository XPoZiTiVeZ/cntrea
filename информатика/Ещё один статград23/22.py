data = [[int(row.split()[0]), int(row.split()[1]), [int(n) for n in row.split()[2].split(";")]] for row in open("22.txt").read().splitlines()]

table_req = {}
table_len = {}

for p, t, r in data:
    table_req[p] = r
    table_len[p] = t

def count_t(p):
    reqs = table_req[p]
    t = table_len[p]
    if reqs == [0]: return t

    # print(p, max([count_t(r) for r in reqs]))

    return t + max([count_t(r) for r in reqs])

c = 0
for p, t in table_len.items():
    if count_t(p) - t > 80:
        c += 1
        print(p, count_t(p) - t)

print(c)