def prime(n):
    for i in range(2, n):
        if n < i ** 2: break
        if n % i == 0: return False
    return True

for i in range(160, 200):
    if prime(i): print(i)