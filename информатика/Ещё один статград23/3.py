data = [row.split() for row in open("3.txt").read().splitlines()]
s = ["М08", "М10", "М12", "М17", "М19", "М22", "М27", "М29", "М30", "М37", "М39", "М44", "М45", "М46", "М52", "М54", "М59", "М64", "М66", "М68", "М69", "М75", "М77", "М85", "М86", "М87", "М94"]
c = 0

for row in data:
    if row[0] not in s: continue
    c += int(row[-2]) * int(row[-1])

print(c)