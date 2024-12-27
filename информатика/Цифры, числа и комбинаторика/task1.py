def encode(n, base):
    if n == 0: return []
    
    result = []
    while n > 0:
        result = [n % base] + result
        n //= base
    return result

def decode(n, base):
    result = 0

    for i in n:
        result *= base
        result += i
    
    return result

results = []
for N in range(1, 10000):
    N12 = encode(N, 12)

    if N12[-1] == 0:
        N12 += N12[-3:]
    else:
        n12 = encode(N12[-1] * 3, 12)
        N12 = n12 + N12

    n = decode(N12, 12)
    if n >= 58000: continue
    results += [(N, n)]
print(*results, sep="\n")
print(max(results, key=lambda x: x[1]))