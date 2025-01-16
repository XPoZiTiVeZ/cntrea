def path(n, e, c):
    if n > e: return 0
    if n == e: return 1
    
    if c == "+":
        return path(n * 2, e, "*") + path(n * 3, e, "*")
    elif c == "*":
        return path(n + 1, e, "+") + path(n + 2, e, "+")
    else:
        return path(n * 2, e, "*") + path(n * 3, e, "*") + path(n + 1, e, "+") + path(n + 2, e, "+")

print(path(1, 22, ""))