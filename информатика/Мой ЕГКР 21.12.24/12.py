for n in range(3, 10000):
    s = "1" + "2" * n
    while s.find("12") != -1 or s.find("322") != -1 or s.find("222") != -1:
        if s.find("12") != -1:
            s = s.replace("12", "2", 1)
        if s.find("322") != -1:
            s = s.replace("322", "21", 1)
        if s.find("222") != -1:
            s = s.replace("222", "3", 1)

    sumn = sum([int(n) for n in s])
    if sumn == 15:
        print(n)
        break