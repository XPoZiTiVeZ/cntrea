data = [int(n) for n in open("17.txt").read().split()]

minv = min(filter(lambda x: str(x)[-2] == str(x)[-1], data))

candidates = []
for i in range(len(data) - 1):
    n1, n2 = data[i], data[i + 1]
    
    if str(n1)[-1] == str(n2)[-2] or str(n1)[-2] == str(n2)[-1]:
        if (n1 % 7 == 0) ^ (n2 % 7 == 0):
            if n1 ** 2 + n2 ** 2 <= minv ** 2:
               candidates.append(n1 ** 2 + n2 ** 2) 

print(len(candidates), max(candidates))