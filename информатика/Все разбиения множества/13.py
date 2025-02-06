import sys

N = int(sys.stdin.read())

def F(n, N, d1, d2, l):
    if n >= N: return [[]]
    
    res = []
    for i in range(1, N + 1):
        if len(res) > 0 and n == 0: break
        if i not in d1 and i not in d2 and i not in l:
            nd1 = d1.copy()
            nd2 = d2.copy()
            nl = l.copy()
            nd1.append(i)
            nd2.append(i)
            nl.append(i)
            res.extend([[i] + tail for tail in F(n + 1, N, [d - 1 for d in nd1 if d - 1 > 0], [d + 1 for d in nd2 if d + 1 <= N], nl)])
    return res

print(*[' '.join([str(n) for n in row]) for row in F(0, N, [], [], [])], sep="\n")