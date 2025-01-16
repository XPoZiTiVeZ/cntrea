candidates = []
for i in range(34722223, 10**8):
    N = i
    Nb = bin(N)[2:]
    Nb += bin(N % 3)[2:].rjust(2, "0")
    Nb += bin(int(Nb, 2) % 5)[2:].rjust(3, "0")
    R = int(Nb, 2)
    if R >= 1_111_111_110 and R <= 1_444_444_416:
        # print(N, R, Nb)
        candidates.append(R)
print(len(candidates))