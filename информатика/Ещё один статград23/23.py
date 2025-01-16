def path(n, e):
    if n == 11: return 0
    if n == 15: return 0
    if n > e:   return 0
    if n == e:  return 1

    return path(n + 1, e) + path(n * 2, e) + path(n + 3, e)

print(path(2, 8) * path(8, 20))