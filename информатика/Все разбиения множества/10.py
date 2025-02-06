import sys

N = int(sys.stdin.read())

def F(seq, N):
    if len(seq) >= N: return [' '.join([str(s) for s in seq])]

    new = seq.copy()
    res = []
    for n in range(1, max(seq) + 2):
        if n > 0:
            res.extend(F(new + [n], N))

    return res

if N < 1:
    print("")
else:
    print(*F([1], N), sep="\n")