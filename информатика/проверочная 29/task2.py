# ab = k(p-1)(q-1) + 1

# ab = 
# m ** 65537 % a = 123456789

def divs(n):
    divs = []
    for i in range(2, n):
        if i ** 2 > n: break
        if n % i == 0: divs += [i, n // i]
    return divs

# for i in range(1, 10000):
#     divs_ = divs(i * 2796 * 3676 + 1)
#     if len(divs_) == 2:
#         print(i, divs_)

for i in range(1000000000000):
    if pow(i, 65537, 13712759) == 123456789:
        print(i)