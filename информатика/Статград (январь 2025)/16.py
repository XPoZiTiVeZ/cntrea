def F(n):
    if n == 0: return 0
    if n > 0 and n % 4 < 2: return F(n // 4) + n % 4
    return F(n // 4) + n % 4 - 1

for i in range(1, 10 ** 10):
    if F(i) == 27 and F(i + 1) == 16:
        print(i)