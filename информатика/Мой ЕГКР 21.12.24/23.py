def path(n, e):
    if n < e or n == 24:   return 0
    if n == e:  return 1

    return path(n - 1, e) + path(n - 6, e) + path(n // 2, e)

print(path(34, 29) * path(29, 19) * path(19, 6))