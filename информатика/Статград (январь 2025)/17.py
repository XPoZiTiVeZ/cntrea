data = [int(n) for n in open("17.txt").read().split() ]

min_n = min(data)
max_n = max(data)
print(min_n, max_n)

candidates = []
for i in range(len(data) - 2):
    n1, n2, n3 = data[i:i + 3]
    n4 = lambda x: int(len(str(x)) == 4)
    n5 = lambda x: int((min_n % 5) == (x % 5))
    n7 = lambda x: int((max_n % 7) == (x % 7))
    
    if (n4(n1) + n4(n2) + n4(n3)) != 0:
        if (n5(n1) + n5(n2) + n5(n3)) <= 1:
            if (n7(n1) + n7(n2) + n7(n3)) >= 2:

                print(n1, n2, n3)
                candidates.append(n1 + n2 + n3)

print(len(candidates), max(candidates))