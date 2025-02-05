import sys

data = [[float(n) for n in row.split()] for row in sys.stdin]

candidates = []
for x1, y1 in data:
    d = 0
    m = None
    for x2, y2 in data:
        r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        d += r
        if m == None or m < r:
            m = r
    candidates.append((d, x1, y1, len(data), m))
print(*min(candidates))