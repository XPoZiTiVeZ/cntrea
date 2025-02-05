def encode(n):
    res = []
    
    while n > 0:
        res = [n % 15] + res
        n //= 15
    
    return res

print(encode(855_000_000))

