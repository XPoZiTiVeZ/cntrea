def F(n):
    if n == 0: return 0
    if n % 4 < 2: return F(n // 4) + n % 4
    return F(n // 4) + n % 4 - 1

for n in range(10 ** 6, 10 ** 10):
    if F(n) == 27 and F(n + 1) == 16:
        print(n)