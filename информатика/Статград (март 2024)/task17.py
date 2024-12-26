data = [int(n) for n in open("17.txt").read().split()]

max_n = max(data, key=lambda n: n if n % 1000 == 652 else 0)
min_n = min(data, key=lambda n: n if n % 1000 == 652 else 100000)

c = 0
max_sum = 0
for i in range(len(data)-3):
    n5 = 0
    n4 = 0
    for n in data[i:i+4]:
        if len(str(n)) == 4:
            n4 += 1
        if len(str(n)) == 5:
            n5 += 1
    if n4 >= n5: continue
    
    n3 = 0
    n7 = 0
    for n in data[i:i+4]:
        if n % 3 == 0:
            n3 += 1
        if n % 7 == 0:
            n7 += 1
    if n3 != n7: continue
    
    sum_ = sum(data[i:i+4])
    if sum_ <= 2 * (max_n + min_n): continue
    
    c += 1
    if sum_ > max_sum:
        max_sum = sum_
    print(data[i:i+4], max_n, min_n)
print(c, max_sum)