for n in range(0, 10 ** 10, 3013):
    ns = str(n)
    if ns[0] != "1": continue
    if ns[2:6] != "3948": continue
    if ns[-1] != "5": continue
    
    print(n)