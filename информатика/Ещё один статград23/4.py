cands = []
for i in range(400000, 800000):
    N = i
    Nb = bin(N)[2:]
    if N % 5 == 0: Nb += "101"
    else: Nb += "1"
    
    if int(Nb, 7) == 0: Nb += "111"
    else: Nb += "1"
    
    if int(Nb, 2) >= 1728404: continue
    cands.append(N)
    print(N, int(Nb, 2))
print(max(cands))