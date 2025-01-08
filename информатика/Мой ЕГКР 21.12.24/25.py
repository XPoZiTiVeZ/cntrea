for n in range(0, 10 ** 10, 18579):
    ns = str(n)

    if ns[:2] == "54" and ns[3] == "1" and ns[5] == "3" and ns[-1] == "7":
        print(n, n // 18579)