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

for y in range(1, 100):
    for x in range(1, 100):
        for p in range(max(x, y, 5), 100):
            if decode([1, 2], p) * decode([3, 4], p) == decode([x, y, 2], p):
                print(f"12 * 34 == {x*p+y}2", decode([1, 2], p) * decode([3, 4], p) == decode([x, y, 2], p), x, y, p)

print(decode([5, 4], 6))