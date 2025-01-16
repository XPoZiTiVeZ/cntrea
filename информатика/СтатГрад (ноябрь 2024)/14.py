def encode(n):
    if n == 0: return [0]

    result = []
    while n > 0:
        result = [n % 37] + result
        n //= 37

    return result

def decode(n):
    result = 0

    for i in n:
        result *= 37
        result += i
    
    return result

candidates = []
for x in range(37):
    for y in range(37):
        if decode([1, 2, x, 6, 4, 3, y, 7]) % 36 == 0:
            candidates.append(decode([y, x]))

print(max(candidates))