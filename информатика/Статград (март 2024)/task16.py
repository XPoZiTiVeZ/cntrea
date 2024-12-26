def F(a, b):
    if b == 0: return 0
    if b > 0 and b % 2 == 0: return 2 * F(a, b / 2)
    return a + F(a, b - 1)

for y in range(1, 100000):
    for x in range(0, y):
        if F(x, y) == 89999:
            print(x, y)