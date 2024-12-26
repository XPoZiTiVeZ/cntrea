def encode(n, base):
    if n == 0: [0]
    
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

candidates = []
for x in range(80):
    for y in range(80):
        for z in range(80):
            n1 = [9, 8, 3, x, 7, 5, 4, z, 6, 2, 1]
            n2 = [8, 7, z, 3, 5, 5, y, 4, 9, 0, 1]
            n1_ = decode(n1, 80)
            n2_ = decode(n2, 80)
            
            if n1_ * n2_ % 79 == 0:
                candidates.append([decode([x, y, z], 80)])
print(max(candidates))