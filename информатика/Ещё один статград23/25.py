def re(ns):
    if ns[0]   != "1":    return False
    if ns[2:6] != "7602": return False
    if ns[-1]  != "0":    return False
    return True

for n in range(0, 10 ** 10, 4891):
    if re(str(n)):
        print(n)