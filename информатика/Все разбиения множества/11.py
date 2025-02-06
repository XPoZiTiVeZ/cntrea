import sys

N, K = [int(n) for n in sys.stdin.read().split()]

def F(seq, N, K):
    if len(seq) >= N: return [' '.join([str(s) for s in seq])]

    new = seq.copy()
    res = []
    for n in range(1, min(max(seq) + 2, K + 1)):
        if n > 0:
            res.extend(F(new + [n], N, K))

    return res

if N < 1:
    print("")
else:
    print(*F([1], N, K), sep="\n")