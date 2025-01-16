a = 66
k = 0
for x in range(0, 49):
    for y in range(0, 26):
        if not((x + 2*y > 48) or (y > x)):
            k += 1
            print(x, y, x + 2 * y, x + 3 * y)