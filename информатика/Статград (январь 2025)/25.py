for n in range(0, 10 ** 9, 9341):
    ns = str(n)
    if ns[0] != "4": continue
    if ns[2] != "5": continue
    if ns[-1] != "3": continue
    if ns.find("07") == -1: continue
    
    print(n)