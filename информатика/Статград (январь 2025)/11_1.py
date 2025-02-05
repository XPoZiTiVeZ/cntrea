def volume(n):
    return ((len(bin(n)[2:]) + 21 * 6 + 60 * 8 + 7) // 8) * 8 * n

for n in range(1, 100000):
    if volume(n) <= 80 * 2 ** 13:
        print(n)