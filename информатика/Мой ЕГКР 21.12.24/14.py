def encode(n):
    if n == 0:
        return [0]

    result = []
    while n > 0:
        result = [n % 25] + result
        n //= 3
    return result

def decode(n):
    result = 0
    for i in n:
        result *= 25
        result += i
    return result

for x in range(25):
    n = decode([1, 1, 3, 5, 3, x, 1, 2]) + decode([1, 3, 5, x, 2, 1])
    if n % 24 == 0: print(x, n / 24)