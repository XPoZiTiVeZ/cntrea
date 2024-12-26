from functools import cache
from datetime import datetime

data = [int(n) for n in open("27-B.txt").read().split()]

N = data[0]
data = data[1:]

def count2(n, t = 0):
    if t == 5: return 0
    if n % 2 == 0: return 1 + count2(n // 2, t + 1)
    return 0

def count5(n, t = 0):
    if t == 5: return 0
    if n % 5 == 0: return 1 + count5(n // 5, t + 1)
    return 0

def count25(n):
    n2 = count2(n)
    n5 = count5(n)

    return (n2, n5)

work = 3238927
process = 0
my_data = {}
time = datetime.now()
for i, n in enumerate(data):
    c = count25(n)
    my_data[c] = my_data.get(c, []) + [i]
    new_process = int(((i + 1) / work) * 100)
    if new_process != process:
        process = new_process
        new_time = datetime.now()
        print(process, "%", (new_time - time).seconds, "s")
        time = new_time

print(*my_data.keys(), sep="\n")