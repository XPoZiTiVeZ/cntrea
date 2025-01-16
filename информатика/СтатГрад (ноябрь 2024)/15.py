
candidates = []
for x in range(300):
    for y in range(300):
        if y <= x: continue
        if x + 2 * y <= 48: continue

        candidates.append(x + 3 * y)

print(min(candidates))