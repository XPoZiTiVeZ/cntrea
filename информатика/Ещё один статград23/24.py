import re

data = open("24.txt").read()
my_re = re.compile(r'ABC|ACB|BAC|BCA|CAB|CBA')

space = [[0, 0]]

start = 0
while start < len(data):
    m = my_re.match(data, start)
    if m != None:
        start = m.start() + 1
        space.append([start, start + 2])
    start += 1

i = 0
while i < len(space) - 1:
    if space[i][1] > space[i + 1][0]:
        space[i][0] = space[i + 1][1]
        space.pop(i + 1)
    else:
        i += 1

space.append([1100006, 1100006])

maxlen = 0
for i in range(len(space) - 1):
    sp1 = space[i]
    sp2 = space[i + 1]
    maxlen = max(maxlen, sp2[0] - sp1[1])

    i += 1
print(maxlen)