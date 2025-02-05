import re

data = open("24.txt").read()

my_re = re.compile(r'A\d+(?:[\+\-]\d+)+')
all = my_re.findall(data)


candidates = []
for r in all:
    candidates.append((len(r), eval(r[1:]), r))

candidates.sort()
print(candidates[-10])
print(candidates[-1])