data = [[int(n) for n in row.split()] for row in open("26.txt").read().splitlines()]

times = [[0 for _ in range(1441)] for _ in range(30)]

# print(times)
c = 0
for T, i in data:
    for j in range(len(times)):
        for k in range(i):
            if times[j][T+k] == 1: break
        else:
            for k in range(i): times[j][T+k] = 1
            break
    else: c += 1

t_ = 0
for l in range(len(times[0])):
    t = 0
    for time in times:
        if time[l] == 1: t += 1
    if t >= 15: continue
    t_ = t_ + 1

print(c, t_)
print(*times, sep="\n", file=open("out", "w+"))