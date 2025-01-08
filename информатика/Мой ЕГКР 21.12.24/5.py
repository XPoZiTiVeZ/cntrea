def encode(n):
    if n == 0:
        return [0]

    result = []
    while n > 0:
        result = [n % 3] + result
        n //= 3
    return result

def decode(n):
    result = 0
    for i in n:
        result *= 3
        result += i
    return result

cands = []
for i in range(11, 10000):
    N = i
    Nt = encode(N)

    if Nt[-1] == 0: Nt += Nt[-2:]
    else: Nt += encode(sum(Nt))

    R = decode(Nt)
    if R > 220: cands.append(R)
print(min(cands))