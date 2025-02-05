def encode(n, base):
    if n == 0: return []
    
    res = []
    while n > 0:
        res = n % base + res
        n //= base
    return res

def decode(n, base):
    res = 0
    
    for i in n:
        res *= base
        res += i

    return res

for p in range(9, 100):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                for w in range(p):
                    n1 = decode([y, 2, 7, x], p)
                    n2 = decode([w, y, 8, 6], p)
                    n3 = decode([x, x, z, 3, y], p)
                    if n1 + n2 == n3:
                        print(decode([x, y, z, w], p))