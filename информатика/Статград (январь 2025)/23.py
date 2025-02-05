def path(n, e):
    if n <  e: return 0
    if n == 16: return 0
    if n == e: return 1
    
    return path(n - 2, e) + (path(n // 3, e) if n % 3 == 0 else path(n - 4, e))

print(path(36, 4))