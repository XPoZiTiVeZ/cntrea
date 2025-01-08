data = open("24.txt").read()

ndata = data.split("FSRQ")
sdata = [len(x) for x in ndata]
maxn = 0
for i in range(len(sdata) - 80):
    sumn = sum(sdata[i:i+80])
    if maxn < sumn: maxn = sumn

print(maxn + 80 * 4)